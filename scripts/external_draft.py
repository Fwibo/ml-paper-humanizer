#!/usr/bin/env python3
"""Step 4 of `write` mode on another model: assemble the writer's prompt from the skill's own files, send it to an
OpenAI-compatible endpoint, save the draft and report any run of six or more words it shares with the material.

Usage: external_draft.py <section> --skeleton skeleton.md [--orientation o] [--names ledger.json|names.txt]
                         [--brief brief.md] [--revise draft.md] [--lean] [--out draft.md] [--model m] [--seed k]
                         [--exclude arxiv-id,…] [--temperature t] [--max-tokens n] [--dry-run]

Endpoint from the environment: HUMANIZER_LLM_BASE_URL (…/v1), HUMANIZER_LLM_API_KEY, HUMANIZER_LLM_MODEL
(--model overrides). Nothing is sent unless these are set; --dry-run writes the prompt next to --out instead.

The system prompt is the two hard lines and "What the reader needs" from SKILL.md and the "Write or revise" step,
cut by heading so the rules have one source. The user prompt is the skeleton, the ledger names, the section's frame
and orientation lines from the playbook, the sentence bank, three exemplar passages (pick_exemplars.py, same seed
gives the same passages), the connectives file and claim-strength, then the brief. --lean leaves out the bank, the
passages and the connectives. --exclude drops a paper's passages and bank entries (for tests that rewrite a
published section). The read-back, frames pass and checker stay with the agent.

--revise draft.md is step 8 of `write` mode: the checked draft goes to the other model for wording only, with the
skeleton as what must not move. The raw revision is saved as <out>.raw.md, revise_check.py puts back what a script
can judge and writes the text to --out and the change list to <out>.changes.md for the agent to keep or undo.
"""
import json, os, re, subprocess, sys, time, urllib.error, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
REF = os.path.join(ROOT, "references")
# section name as the user types it -> file in references/sections/
PLAYBOOK = {"abstract": "abstract", "intro": "introduction", "introduction": "introduction", "method": "method",
            "results": "experiments", "experiments": "experiments", "analysis": "analysis", "related": "related-work",
            "related-work": "related-work", "conclusion": "conclusion", "limitations": "limitations",
            "appendix": "appendix", "rebuttal": "rebuttal"}


def read(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def block(text, heading, level="##"):
    """The text under `heading` up to the next heading of the same or a higher level."""
    lines, out, on = text.splitlines(), [], False
    depth = len(level)
    for ln in lines:
        m = re.match(r"(#+) ", ln)
        if m and on and len(m.group(1)) <= depth:
            break
        if on:
            out.append(ln)
        if ln.strip() == f"{level} {heading}":
            on = True
    return "\n".join(out).strip()


# SKILL.md is written for an agent that has the whole skill; these phrases point at files the writer does not get.
DETACH = [("Everything else in this skill is", "Everything else here is"),
          (", with the orienting frames the frames file lists", ""),
          (", and the frames file shows what they look like", "")]

TASK_DRAFT = (
    "# The draft\n\n"
    "- Every numbered paragraph note (### P…) of the skeleton becomes one paragraph, in the skeleton's order, with its claim at the "
    "skeleton's strength and scope (the reporting verb and the scope in parentheses after the claim are part of it) and "
    "its evidence named. Add no claim, number, fact or qualifier the skeleton and brief do not give; leave a gap as a "
    "visible [TODO: …].\n"
    "- Use the ledger's names verbatim, one name per thing; coin no label for a thing the ledger names.\n"
    "- Keep [cite], REF, math and every number exactly as given. Keep the Keep lines verbatim.\n"
    "- The passages and the bank show pacing and the placement of a claim. Their content and terms are not "
    "yours, and no run of six or more words from them may appear in your text.\n"
    "- Output the section text only: no preamble, no notes, no change list.")
TASK_REVISE = (
    "# The revision\n\n"
    "- The draft at the end of the request was written from the skeleton and checked against it. Its paragraphs and "
    "their order, every claim with its reporting verb and scope, every number, name, [cite] and REF stay as they are.\n"
    "- Change the wording only where a sentence does not yet read the way the authors of a strong paper in this field "
    "write: an orienting frame the reader needs, a link the reader has to work out, two points in one sentence, a "
    "phrase no author in this field would use. A sentence that already reads that way is left exactly as it is.\n"
    "- Add no claim, qualifier, intensifier, example or closing reading the draft does not have, and remove none.\n"
    "- No run of six or more words from the passages or the bank may appear in your text.\n"
    "- Output the revised section only: no preamble, no notes, no change list.")


def system_prompt(revise=False):
    skill = read(os.path.join(ROOT, "SKILL.md"))
    body = skill.split("\n# ", 1)[1].split("\n", 1)[1]
    lead = body.split("\n## ", 1)[0].strip()
    needs = block(skill, "What the reader needs")
    step = re.search(r"^\d+\. \*\*Write or revise\.\*\*(.*)$", skill, re.M).group(1).strip()
    role = ("You are revising one section of an AI conference paper for its authors. Revise it in English, in Markdown, "
            "so that it reads as the authors of a strong paper in this field would write it." if revise else
            "You are drafting one section of an AI conference paper for its authors, from their skeleton. Write the "
            "section in English, in Markdown, as the authors of a strong paper in this field would write it.")
    text = (f"{role}\n\n{lead}\n\n# What the reader needs\n\n{needs}\n\n# How sentences follow each other\n\n{step}\n\n"
            + (TASK_REVISE if revise else TASK_DRAFT))
    for old, new in DETACH:
        text = text.replace(old, new)
    return text


def bank(exclude):
    text = read(os.path.join(REF, "sentence-bank.md"))
    if not exclude:
        return text
    out, skip = [], False
    for ln in text.splitlines():
        if re.match(r"\*\*[AB]\d+\*\*", ln):
            skip = any(x in ln for x in exclude)
        elif ln.startswith("#"):
            skip = False
        if not skip:
            out.append(ln)
    return "\n".join(out)


def exemplars(section, orientation, seed, exclude):
    cmd = [sys.executable, os.path.join(HERE, "pick_exemplars.py"), section, "--seed", str(seed)]
    if orientation:
        cmd += ["--orientation", orientation]
    if exclude:
        cmd += ["--exclude", ",".join(exclude)]
    return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout


def names(path):
    if not path:
        return ""
    if path.endswith(".json"):
        d = json.load(open(path, encoding="utf-8"))
        entries = d.get("entries", d) if isinstance(d, dict) else d
        return "\n".join(f"- {e['term']}" + (f" ({e['kind']})" if e.get("kind") else "") for e in entries)
    return read(path).strip()


def user_prompt(a, ex_text):
    playbook = read(os.path.join(REF, "section-playbook.md"))  # the index: orientation tags and opening logic
    section_file = os.path.join(REF, "sections", PLAYBOOK.get(a["section"].lower(), a["section"].lower()) + ".md")
    section_text = read(section_file) if os.path.exists(section_file) else ""
    # the file's first paragraph points at the index and sources.md, which the writer does not get
    section_text = "\n".join(ln for ln in section_text.splitlines() if "section-playbook.md" not in ln).strip()
    parts = [
        ("Skeleton", read(a["skeleton"])),
        ("Ledger names", names(a.get("names")) or "Use the Names line of the skeleton."),
        ("Orientation", (a.get("orientation") or "see the skeleton") + "\n\n" + block(playbook, "Orientation opening logic (light reference)", "###")),
        (f"Section frame and what readers expect: {a['section']}", section_text),
    ]
    if not a.get("lean"):
        parts += [("Sentence bank", bank(a["exclude"])), ("Exemplar passages", ex_text),
                  ("Connectives this field uses", read(os.path.join(REF, "connectives.md")))]
    parts.append(("How strong each claim is", read(os.path.join(REF, "claim-strength.md"))))
    if a.get("brief"):
        parts.append(("Brief from the authors", read(a["brief"])))
    if a.get("revise"):
        parts += [("Draft to revise", read(a["revise"]).strip()), ("Task", "Revise the draft above.")]
    else:
        parts.append(("Task", f"Write the {a['section']} section from the skeleton above."))
    return "\n\n".join(f"# {h}\n\n{t}" for h, t in parts)


def call(system, user, model, temperature, max_tokens):
    base, key = os.environ.get("HUMANIZER_LLM_BASE_URL"), os.environ.get("HUMANIZER_LLM_API_KEY")
    if not (base and key and model):
        sys.exit("set HUMANIZER_LLM_BASE_URL, HUMANIZER_LLM_API_KEY and HUMANIZER_LLM_MODEL (or --model)")
    body = {"model": model, "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
            "max_tokens": max_tokens}
    if temperature is not None:
        body["temperature"] = temperature
    url = base.rstrip("/") + "/chat/completions"
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers)
            with urllib.request.urlopen(req, timeout=600) as r:
                d = json.load(r)
            break
        except urllib.error.HTTPError as e:
            err = e.read()[:500].decode(errors="replace")
            if e.code == 400 and "max_completion_tokens" in err and "max_tokens" in body:
                body["max_completion_tokens"] = body.pop("max_tokens"); continue  # OpenAI reasoning models
            if e.code in (429, 500, 502, 503, 504) and attempt < 3:
                time.sleep(5 * 2 ** attempt); continue
            sys.exit(f"HTTP {e.code}: {err}")
        except (urllib.error.URLError, TimeoutError) as e:
            if attempt < 3:
                time.sleep(5 * 2 ** attempt); continue
            sys.exit(f"request failed: {e}")
    ch = d["choices"][0]
    text = re.sub(r"<think>.*?</think>", "", ch["message"].get("content") or "", flags=re.S).strip()
    u = d.get("usage", {})
    print(f"model {d.get('model', model)}, finish {ch.get('finish_reason')}, prompt {u.get('prompt_tokens')} "
          f"tokens, completion {u.get('completion_tokens')} tokens", file=sys.stderr)
    if ch.get("finish_reason") == "length":
        print("warning: the draft was cut at max_tokens; raise --max-tokens", file=sys.stderr)
    return text


def shared_runs(draft, sources, n=6):
    """Runs of n+ words the draft shares with any source, longest first."""
    tok = lambda s: re.findall(r"[a-z0-9]+(?:'[a-z]+)?", s.lower())
    d = tok(draft)
    grams = set()
    for s in sources:
        t = tok(s)
        grams |= {tuple(t[i:i + n]) for i in range(len(t) - n + 1)}
    runs, i = [], 0
    while i <= len(d) - n:
        if tuple(d[i:i + n]) in grams:
            j = i + 1
            while j <= len(d) - n and tuple(d[j:j + n]) in grams:
                j += 1
            runs.append(" ".join(d[i:j + n - 1])); i = j + n - 1
        else:
            i += 1
    return sorted(set(runs), key=len, reverse=True)


def main():
    argv = sys.argv[1:]
    if not argv or argv[0].startswith("-"):
        sys.exit(__doc__)
    opt = lambda k, d=None: argv[argv.index(k) + 1] if k in argv else d
    a = {"section": argv[0], "skeleton": opt("--skeleton"), "orientation": opt("--orientation"),
         "names": opt("--names"), "brief": opt("--brief"), "revise": opt("--revise"), "lean": "--lean" in argv,
         "exclude": [x for x in (opt("--exclude") or "").split(",") if x]}
    if not a["skeleton"]:
        sys.exit("--skeleton is required: the skeleton is the outline of `write` mode and the check of a revision")
    out = opt("--out", "draft.external.md")
    seed = int(opt("--seed", "0"))
    ex_text = "" if a["lean"] else exemplars(a["section"], a["orientation"], seed, a["exclude"])
    system, user = system_prompt(bool(a["revise"])), user_prompt(a, ex_text)
    if "--dry-run" in argv:
        p = os.path.splitext(out)[0] + ".prompt.md"
        open(p, "w", encoding="utf-8").write(f"# SYSTEM\n\n{system}\n\n# USER\n\n{user}\n")
        print(f"prompt -> {p} ({len((system + user).split())} words)"); return
    t = opt("--temperature")
    model = opt("--model", os.environ.get("HUMANIZER_LLM_MODEL"))
    draft = call(system, user, model, float(t) if t is not None else None, int(opt("--max-tokens", "16000")))
    runs = [] if a["lean"] else shared_runs(draft, [ex_text, bank(a["exclude"])])
    if a["revise"]:
        import revise_check
        raw = os.path.splitext(out)[0] + ".raw.md"
        open(raw, "w", encoding="utf-8").write(draft + "\n")
        before = read(a["revise"])
        runs = [r for r in runs if r not in " ".join(re.findall(r"[a-z0-9]+(?:'[a-z]+)?", before.lower()))]
        print(f"revision ({model}) -> {raw}")
        revise_check.run(a["revise"], raw, a["skeleton"], a["names"] if (a["names"] or "").endswith(".json") else None, out)
    else:
        open(out, "w", encoding="utf-8").write(draft + "\n")
        print(f"draft -> {out} ({len(draft.split())} words, model {model})")
    if runs:
        print(f"{len(runs)} run(s) of 6+ words shared with the exemplars or the bank (rewrite these):")
        for r in runs:
            print(f"  - {r}")
    else:
        print("no run of 6+ words shared with the exemplars or the bank")


if __name__ == "__main__":
    main()
