#!/usr/bin/env python3
"""Anomaly report for a LaTeX paper. Reports repetition and possibly empty words relative to the document
itself; it has no targets and never says a count is too low or too high.

Usage: check_tex.py <dir-or-file> [more files] [--ledger ledger.json] [--json]

Input is LaTeX (.tex) or Markdown (.md, .markdown, .txt). A Markdown file is turned into minimal LaTeX in memory
(headings, bold and italics, inline code, fenced code, tables, lists, [cite] and [@key] citations) and read by the
same parser, so every flag means the same thing for both. A directory is searched for .tex files, and for .md
files only when it holds no .tex.

Flags (places to look, not verdicts):
  same-opener           the same opening word in 3+ consecutive paragraphs
  even-run              5 sentences in a row within 6 words of each other
  device-recurs         a stance adverb, reason frame, additive connective or upgrade verb (employ, utilize,
                        leverage, exploit) 3+ times in one section
  restating             a heading whose words reappear in the first or last sentence of its paragraph
  announcing            a sentence that announces a count and carries nothing else
  name-drift?           an emphasised term and a recurring near variant (same object under two names?)
  dangling-comparison   a paragraph with gap / gain / margin / advantage / improvement / difference / drop
                        that names neither the two sides nor a table, figure or number
  colon-semicolon       a section with 3+ colons and semicolons in its prose, with the published rate for reference
  maybe-empty           a word that may carry no specific meaning here
Information only: sentence count, mean and sd of sentence length, share over 30 and under 12 words, and the
emphasised or defined terms found (protected_terms, in --json).
With --ledger ledger.json: ledger names the text never uses, and recurring noun phrases the ledger lacks (coined?).

Verbatim, listing, table, equation and algorithm environments are skipped, as is any environment whose name
contains prompt, listing, box, verb, lst, code or frame; figure and table bodies are skipped but captions kept.
"""
import collections, json, os, re, statistics, sys

# ---------- LaTeX reading ----------
SKIP_ENVS = {
    "verbatim", "Verbatim", "lstlisting", "minted", "tabular", "tabular*",
    "tabularx", "tabu", "longtable", "equation", "equation*", "align",
    "align*", "gather", "gather*", "multline", "multline*", "eqnarray",
    "algorithm", "algorithmic", "algorithm2e", "tikzpicture", "thebibliography",
    "tcolorbox", "promptbox", "mdframed", "filecontents", "comment",
}
WRAP_ENVS = {"figure", "figure*", "table", "table*", "wrapfigure", "wraptable", "subfigure", "minipage"}
SKIP_HINTS = ("prompt", "listing", "box", "verb", "lst", "code", "frame")


def is_skipped(env):
    e = env.lower()
    return env in SKIP_ENVS or env in WRAP_ENVS or any(h in e for h in SKIP_HINTS)


def strip_comments(line):
    out, i = [], 0
    while i < len(line):
        c = line[i]
        if c == "\\" and i + 1 < len(line):
            out.append(line[i:i + 2]); i += 2; continue
        if c == "%":
            break
        out.append(c); i += 1
    return "".join(out)


def balanced_arg(text, start):
    """Return (content, end_index) for the {...} starting at text[start] == '{'."""
    depth, i = 0, start
    while i < len(text):
        if text[i] == "\\":
            i += 2; continue
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:i], i + 1
        i += 1
    return text[start + 1:], len(text)


def detex(s):
    s = re.sub(r"\\(cite[pt]?|citealp|citet|citep|ref|eqref|autoref|cref|Cref|label|url|href|includegraphics)\*?(\[[^\]]*\])*\{[^}]*\}", " REF ", s)
    s = re.sub(r"\$[^$]*\$", " MATH ", s)
    s = re.sub(r"\\\(.*?\\\)", " MATH ", s)
    s = re.sub(r"\\(textbf|emph|textit|texttt|underline|textsc)\{", "{", s)
    s = re.sub(r"\\[A-Za-z]+\*?(\[[^\]]*\])?", " ", s)
    s = s.replace("~", " ").replace("{", "").replace("}", "")
    s = s.replace("``", '"').replace("''", '"').replace("--", "-")
    return re.sub(r"\s+", " ", s).strip()


# ---------- Markdown reading ----------
MD_EXTS = (".md", ".markdown", ".txt")
HEADING_CMD = {1: "section", 2: "subsection", 3: "subsubsection", 4: "paragraph"}


def md_to_tex(raw):
    """Minimal Markdown -> LaTeX so that parse() and detex() see the same structure as in a .tex file."""
    out, fenced, in_table = [], False, False
    # the shallowest heading in the file is a section, whatever its number of #, so a draft of one section
    # that starts at ### is split into sections the same way as the .tex it will become
    levels = [len(m.group(1)) for l in raw for m in [re.match(r"\s*(#{1,6})\s+\S", l)] if m]
    shift = min(levels) - 1 if levels else 0
    for line in raw:
        if re.match(r"\s*(```|~~~)", line):
            fenced = not fenced
            out.append("\\begin{verbatim}" if fenced else "\\end{verbatim}"); continue
        if fenced:
            out.append(line); continue
        is_table = line.lstrip().startswith("|")
        if is_table and not in_table:
            out.append("\\begin{tabular}"); in_table = True
        elif in_table and not is_table:
            out.append("\\end{tabular}"); in_table = False
        if is_table:
            out.append(line); continue
        line = re.sub(r"<!--.*?-->", "", line)
        hm = re.match(r"\s*(#{1,6})\s+(.*?)\s*#*\s*$", line)
        if hm:
            level = min(len(hm.group(1)) - shift, 4)
            out.append("\\%s{%s}" % (HEADING_CMD[level], md_inline(hm.group(2)))); continue
        if re.match(r"\s*(-{3,}|\*{3,}|_{3,})\s*$", line):
            out.append(""); continue
        line = re.sub(r"^(\s*)>\s?", r"\1", line)
        lm = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", line)
        if lm:
            out.append("%s\\item %s" % (lm.group(1), md_inline(lm.group(3)))); continue
        out.append(md_inline(line))
    if in_table:
        out.append("\\end{tabular}")
    if fenced:
        out.append("\\end{verbatim}")
    return out


def md_inline(s):
    parts = re.split(r"(\$[^$]*\$)", s)  # leave inline math alone
    for i in range(0, len(parts), 2):
        t = parts[i]
        t = re.sub(r"(?<!\\)%", r"\\%", t)
        t = re.sub(r"`([^`]+)`", r"\\texttt{\1}", t)
        t = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", t)
        t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
        t = re.sub(r"\[(@[^\]]+|cite[^\]]*)\]", r"\\cite{x}", t, flags=re.I)
        t = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", t)
        t = re.sub(r"__(.+?)__", r"\\textbf{\1}", t)
        t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"\\emph{\1}", t)
        t = re.sub(r"(?<![\w_])_(?!\s)(.+?)(?<!\s)_(?![\w_])", r"\\emph{\1}", t)
        parts[i] = t
    return "".join(parts)


def load(paths):
    files = []
    for p in paths:
        if os.path.isdir(p):
            tex, md = [], []
            for root, _, names in os.walk(p):
                if "build" in root.split(os.sep): continue
                for n in sorted(names):
                    if n.endswith(".tex"): tex.append(os.path.join(root, n))
                    elif n.endswith(MD_EXTS) and not n.lower().startswith("readme"): md.append(os.path.join(root, n))
            files.extend(tex or md)
        elif p.endswith(".tex") or p.endswith(MD_EXTS):
            files.append(p)
    return files


def parse(path):
    """Return prose paragraphs, headings, captions with line numbers."""
    with open(path, encoding="utf-8", errors="replace") as f:
        raw = f.read().split("\n")
    if path.endswith(MD_EXTS):
        raw = md_to_tex(raw)
    paragraphs, headings, captions = [], [], []
    cur, cur_start = [], None
    stack = []  # env names

    def flush():
        nonlocal cur, cur_start
        text = " ".join(cur).strip()
        if text and not re.fullmatch(r"(\\[A-Za-z]+\*?(\[[^\]]*\])?(\{[^}]*\})*\s*)+", text):
            paragraphs.append((cur_start, text))
        cur, cur_start = [], None

    for ln, line in enumerate(raw, 1):
        line = strip_comments(line)
        for m in re.finditer(r"\\begin\{([^}]+)\}", line):
            stack.append(m.group(1))
        skipping = any(is_skipped(e) for e in stack)
        for m in re.finditer(r"\\caption(of\{[^}]*\})?\s*(\[[^\]]*\])?\s*\{", line):
            content, _ = balanced_arg(line, m.end() - 1)
            captions.append((ln, content))
        hm = re.search(r"\\(paragraph|subparagraph|section|subsection|subsubsection)\*?\s*\{", line)
        if hm:
            content, end = balanced_arg(line, hm.end() - 1)
            headings.append((ln, hm.group(1), detex(content)))
            flush()
            line = line[end:]  # run-in text after heading starts a paragraph
        for m in re.finditer(r"\\end\{([^}]+)\}", line):
            if stack and stack[-1] == m.group(1):
                stack.pop()
            elif m.group(1) in stack:
                stack.remove(m.group(1))
        if skipping:
            continue
        if not line.strip() or line.strip() in ("\\par", "\\newline", "\\\\"):
            flush(); continue
        if re.match(r"\s*\\(begin|end|clearpage|newpage|vspace|input|include|bibliography|label|centering|item)\b", line) and len(line.strip()) < 80 and not re.search(r"[a-z]{4,}\s+[a-z]{3,}\s+[a-z]{3,}", detex(line)):
            flush() if not line.strip().startswith("\\item") else None
            if line.strip().startswith("\\item"):
                cur.append(line.replace("\\item", " "))
                cur_start = cur_start or ln
            continue
        if cur_start is None:
            cur_start = ln
        cur.append(line)
    flush()
    return paragraphs, headings, captions


def sentences(text):
    text = detex(text)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"(])", text)
    return [p.strip() for p in parts if len(p.split()) >= 3]


def words(s): return re.findall(r"[A-Za-z][A-Za-z'-]*", s)


# ---------- word lists ----------
GENERAL = r"\b(get|gets|got|go|goes|went|come|comes|came|stay|stays|stayed|hold|holds|held|carry|carries|carried|keep|keeps|kept|put|puts|leave|leaves|left|pick|picks|picked|turn out|turns out|turned out|do better|does better|did better|do worse|does worse|did worse|is ahead|are ahead|stays ahead|stay above|stays above|catch up|catches up|end up|ends up)\b"
FIELD = r"\b(demonstrate|transform|maintain|utilize|employ|conduct|enhance|increase|leverage|ensure|assess|exclude|enable|quantify|investigate|incorporate|decrease|mitigate|provide|highlight|minimize|dominate|involve|induce|impose|validate|explore|determine|outperform|exceed|achieve|attain|retain|preserve|degrade|exhibit|observe|yield|attribute|remain)(s|es|ed|d|ing)?\b"
# Devices a reader spots when they recur: upgrade verbs, additive connectives, stance adverbs, reason frames.
# Result and reading frames (we find that, this suggests, however, thus, overall …) are the field's ordinary
# frames and are not listed; the frames pass adds them where the function is there.
CONNECT = ["employ", "employs", "employed", "utilize", "utilizes", "utilized", "leverage", "leverages", "leveraged", "exploit", "exploits", "exploited", "moreover", "furthermore", "specifically", "concretely", "in short", "notably", "importantly", "interestingly", "crucially", "remarkably", "surprisingly", "strikingly", "a key reason", "this is because", "we hypothesize", "we argue", "we take this as"]
EMPTY = ["novel", "significant", "significantly", "paradigm", "sheds light", "paves the way", "groundbreaking", "state-of-the-art", "it is worth noting", "it is important to note", "to the best of our knowledge", "extensive experiments", "comprehensive", "holistic", "seamless", "pivotal", "cornerstone", "showcase"]
COMPARE = r"\b(gap|gaps|gain|gains|margin|margins|advantage|advantages|improvement|improvements|difference|differences|drop|drops|degradation|lead)\b"
SIDES = r"\b(than|versus|vs\.?|compared|comparable|relative to|between|against|REF|MATH|table|figure|fig\.?|tab\.?)\b|\d|%"
ANNOUNCE = re.compile(r"^(There are|We (see|identify|make|have|present|note) (two|three|four|several)|Two|Three|Four|Several) [^.]{0,40}(follow|reasons|challenges|observations|contributions|points)[^.]{0,10}[.:]$", re.I)
# A variant counts as a possible second name only when its first word could be part of a name: not an article,
# determiner, pronoun, preposition, conjunction, auxiliary, common adverb or stray letter.
VARIANT_STOP = set("""the a an this that these those each every any some no our its their my your his her of and or but in to for
on at by with from as than into over under between against about after before during without within is are was were be been
being am has have had do does did can could will would may might shall should must not also only often still very more most
less least so too what which who whom whose how when where why whether if because since while though although it they we you
he she i one s t""".split())


# ---------- report ----------
def report(files):
    out = {"files": [], "flags": []}
    for path in files:
        paras, headings, captions = parse(path); out["files"].append(path)
        P = [(ln, detex(t)) for ln, t in paras]
        # same opener in consecutive paragraphs
        openers = [(ln, (words(t)[:1] or [""])[0].lower()) for ln, t in P]
        run = 1
        for i in range(1, len(openers)):
            run = run + 1 if openers[i][1] and openers[i][1] == openers[i-1][1] else 1
            if run == 3: out["flags"].append({"type": "same-opener", "file": path, "line": openers[i][0], "note": f"three consecutive paragraphs open with '{openers[i][1]}'"})
        # even runs of sentence length
        for ln, t in P:
            L = [len(words(s)) for s in sentences(t)]
            for i in range(len(L) - 4):
                w = L[i:i+5]
                if max(w) - min(w) <= 6: out["flags"].append({"type": "even-run", "file": path, "line": ln, "note": f"five sentences of {min(w)}–{max(w)} words in a row (paragraph at line {ln})"}); break
        # device recurring in one section; colons and semicolons per section
        sec_bounds = [(h[0], h[2]) for h in headings if h[1] in ("section", "subsection")] or [(0, "(whole)")]
        for k, (start, name) in enumerate(sec_bounds):
            end = sec_bounds[k+1][0] if k + 1 < len(sec_bounds) else 10**9
            text = " ".join(t for ln, t in P if start <= ln < end).lower()
            for c in CONNECT:
                n = len(re.findall(r"\b" + re.escape(c) + r"\b", text))
                if n >= 3: out["flags"].append({"type": "device-recurs", "file": path, "line": start, "note": f"'{c}' appears {n} times in section '{name[:40]}'"})
            words_in_sec = len(words(text)); n_col = len(re.findall(r"[a-z0-9)\]]\s?:\s+[a-z]", text)); n_semi = len(re.findall(r"[a-z0-9)\]];\s+[a-z]", text))
            if n_col + n_semi >= 3 and words_in_sec:
                out["flags"].append({"type": "colon-semicolon", "file": path, "line": start, "note": f"{n_col} colons and {n_semi} semicolons in {words_in_sec} words of section '{name[:40]}' (published body prose runs about 2.4 and 0.9 per 1,000 words); a clause or a second sentence instead?"})
        # heading restated
        for ln, kind, h in headings:
            hw = {w.lower() for w in words(h) if len(w) > 3}
            if len(hw) < 2: continue
            nxt = [t for pl, t in P if pl >= ln][:1]
            if nxt:
                S = sentences(nxt[0])
                for which, s in (("first", S[0] if S else ""), ("last", S[-1] if len(S) > 1 else "")):
                    sw = {w.lower() for w in words(s)}
                    if s and len(hw & sw) / len(hw) >= 0.6: out["flags"].append({"type": "restating", "file": path, "line": ln, "note": f"heading '{h[:50]}' is restated by the {which} sentence of its paragraph"})
        # announcing sentences
        for ln, t in P:
            for s in sentences(t):
                if ANNOUNCE.match(s.strip()) and len(words(s)) <= 12: out["flags"].append({"type": "announcing", "file": path, "line": ln, "note": f"'{s.strip()[:70]}' announces a count; check that it carries something"})
        # possibly empty words
        for ln, t in P:
            low = t.lower()
            for w in EMPTY:
                for m in re.finditer(r"\b" + re.escape(w) + r"\b", low):
                    ctx = t[max(0, m.start()-40):m.end()+40].replace("\n", " ")
                    if w.startswith("significant") and re.search(r"confidence|interval|p\s*[<=]|p-value|test|bootstrap", low[max(0, m.start()-200):m.end()+200]):
                        continue  # the statistical sense, with a test named nearby
                    out["flags"].append({"type": "maybe-empty", "file": path, "line": ln, "note": f"'{w}' … does it carry a specific meaning here? …{ctx}…"})
        # name drift: emphasised terms and near variants
        terms = sorted(set(re.findall(r"\\(?:emph|textit|textbf)\{([A-Za-z][A-Za-z -]{3,40})\}", " ".join(t for _, t in paras))))
        term_set = {t.lower() for t in terms}
        full = " ".join(t for _, t in P).lower()
        for term in terms:
            tl = term.lower(); base = tl.split()[-1]
            found = collections.Counter(re.findall(r"\b([a-z-]+ " + re.escape(base) + r")\b", full))
            # a variant is a recurring phrase whose first word is a content word, is not itself one of the
            # emphasised terms (a compound of two names is not drift) and is not part of the term
            variants = {v for v, n in found.items() if n >= 2 and v != tl and v not in tl
                        and v.split()[0] not in VARIANT_STOP and v.split()[0] not in term_set}
            if variants: out["flags"].append({"type": "name-drift?", "file": path, "line": 0, "note": f"term '{term}' also appears as {sorted(variants)[:4]}; same object?"})
        # dangling comparison: comparison noun with no sides, pointer or number in the paragraph
        for ln, t in P:
            m = re.search(COMPARE, t, flags=re.I)
            if m and not re.search(SIDES, t, flags=re.I):
                out["flags"].append({"type": "dangling-comparison", "file": path, "line": ln, "note": f"'{m.group(0)}' … between what and what, on which metric, which table? (paragraph at line {ln} names no sides, pointer or number)"})
        # information
        L = [len(words(s)) for _, t in P for s in sentences(t)]
        if L: out.setdefault("info", []).append({"file": path, "sentences": len(L), "mean_len": round(statistics.mean(L), 1), "sd_len": round(statistics.pstdev(L), 1), "share_over_30": round(sum(x > 30 for x in L) / len(L), 2), "share_under_12": round(sum(x < 12 for x in L) / len(L), 2)})
        allw = sum(L); full_text = " ".join(t for _, t in P)
        g = len(re.findall(GENERAL, full_text, flags=re.I)); fv = len(re.findall(FIELD, full_text, flags=re.I))
        if allw: out["info"][-1].update({"general_verbs_per_1k": round(1000 * g / allw, 1), "field_verbs_per_1k": round(1000 * fv / allw, 1)})
        # emphasised terms and "we call / term / refer to … as" definitions, for the ledger
        defs = re.findall(r"\b(?:we (?:call|term|name|refer to|denote)|termed|called|referred to as|which we call)\s+(?:this |the |a |an |it |the set )?(?:as )?\\?(?:emph|textit|textbf)?\{?([A-Za-z][A-Za-z0-9 -]{2,40})\}?", full_text)
        prot = sorted({t.strip() for t in list(terms) + defs if 3 < len(t.strip()) < 45})
        if prot: out["info"][-1]["protected_terms"] = prot
    return out


def main():
    a = sys.argv[1:]; js = "--json" in a; paths = [x for x in a if not x.startswith("--")]
    led = next((a[i + 1] for i, x in enumerate(a) if x == "--ledger" and i + 1 < len(a)), None)
    if led: paths = [p for p in paths if p != led]
    files = load(paths)
    if not files: print("no .tex or .md files found"); return
    R = report(files)
    if js: print(json.dumps(R, indent=1)); return
    print(f"check_tex: {len(files)} file(s). Flags are places to look; none is a target.\n")
    by = {}
    for f in R["flags"]: by.setdefault(f["type"], []).append(f)
    for t in ["same-opener", "even-run", "device-recurs", "restating", "announcing", "name-drift?", "dangling-comparison", "colon-semicolon", "maybe-empty"]:
        fs = by.get(t, [])
        if not fs: continue
        print(f"## {t} ({len(fs)})")
        for f in fs[:25]: print(f"  {os.path.basename(f['file'])}:{f['line']}  {f['note']}")
        if len(fs) > 25: print(f"  … {len(fs)-25} more")
        print()
    for i in R.get("info", []): print(f"info only (no target): {os.path.basename(i['file'])}: {i['sentences']} sentences, mean {i['mean_len']} words, sd {i['sd_len']}, over 30 words {i['share_over_30']}, under 12 words {i['share_under_12']}")
    if led and os.path.exists(led):
        L = json.load(open(led)); ents = L.get("entries", L if isinstance(L, list) else [])
        full = " ".join(" ".join(md_to_tex(open(f, errors="ignore").read().split("\n"))) if f.endswith(MD_EXTS)
                        else open(f, errors="ignore").read() for f in files)
        low = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?\{([^{}]*)\}", r"\2", full).lower()
        names = [e["term"] for e in ents if isinstance(e, dict) and e.get("term")]
        def cnt(t): return len(re.findall(r"(?<![\w-])" + re.escape(t.lower()).replace(r"\ ", r"[\s-]+") + r"(?![\w-])", low))
        unused = [t for t in names if cnt(t) == 0]
        lset = {t.lower() for t in names}
        cand = collections.Counter(m.group(0).lower() for m in re.finditer(r"\b(?:[a-z][a-z-]+ ){1,3}[a-z][a-z-]+\b", low))
        STOP = {"the","a","an","of","in","on","to","for","with","and","or","is","are","we","our","this","that","these","those","as","by","at","from","than","it","its","be","can","which","their","each","all","not","no","such","one","two","more","most","other","same","also","only","both","into","over","under","per","via"}
        coined = [t for t, n in cand.items() if n >= 3 and t not in lset and not any(t in l or l in t for l in lset) and t.split()[0] not in STOP and t.split()[-1] not in STOP and len(t) > 9]
        print(f"ledger: {len(names)} names, {len(names) - len(unused)} used; never used: {', '.join(unused[:30]) or 'none'}")
        if coined: print(f"coined? recurring phrases the ledger does not have (look, not a verdict): {', '.join(sorted(coined, key=lambda t: -cand[t])[:25])}")


if __name__ == "__main__": main()
