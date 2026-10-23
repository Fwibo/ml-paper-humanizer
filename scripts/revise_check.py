#!/usr/bin/env python3
"""Step 8 of `write` mode: compare a checked draft with another model's wording revision, undo the changes a
script can judge, and list the rest for the agent to keep or undo.

Usage: revise_check.py <before.md> <after.md> --skeleton skeleton.md [--names ledger.json] [--out final.md]

Paragraphs are paired one to one (a revision that moved, merged or split paragraphs is not used at all), and the
sentences inside each pair are aligned, a sentence split in two or two merged counting as one change. A change is
put back to the original wording when the revision
  - changed a number, [cite], REF, \\cite or math span,
  - added or changed a heading or a bold run-in label,
  - dropped a Keep item of the skeleton that the original carried verbatim.
Every other change goes to the change list, with flags where it
  - uses a ledger name fewer times than the original (a second name, or the name left out?),
  - brings in a strength, scope or cause word the original sentence did not have,
  - adds or removes a sentence, merges or splits sentences, or changes the length by a third or more.
Above the list stand the recurring phrases the revision renamed across the text ("RL model" 9 -> 0).
Writes the text with the undone blocks put back to --out (default: <after>.checked.md) and the list next to it as
<out>.changes.md. The agent reads the list, keeps or undoes each change in --out, and runs check_tex.py.
"""
import collections, difflib, json, os, re, sys

ABBR = ["e.g.", "i.e.", "et al.", "vs.", "cf.", "Fig.", "Figs.", "Eq.", "Eqs.", "Sec.", "Tab.", "approx.", "resp."]
STRENGTH = ["significantly", "substantially", "dramatically", "remarkably", "consistently", "systematically",
            "always", "never", "all", "every", "across", "both", "clearly", "strongly", "greatly", "crucial",
            "critical", "key", "essential", "fundamental", "inherent", "challenging", "notably", "only", "merely",
            "robust", "superior", "state-of-the-art", "demonstrates", "proves", "confirms", "reveals", "establishes",
            "shows", "indicates", "suggests", "may", "might", "likely", "because", "due", "thus", "therefore",
            "hence", "since", "leads", "causes", "enables", "ensures", "guarantees"]
PROTECT = re.compile(r"\$[^$]+\$|\\cite\w*\{[^}]*\}|\[cite[^\]]*\]|\bREF\b|\d+(?:\.\d+)?\s*%?")
BOLD = re.compile(r"\*\*[^*]+\*\*")


STOP = {"the", "a", "an", "of", "for", "to", "in", "on", "and", "or", "with", "that", "this", "these", "is", "are",
        "was", "were", "be", "at", "by", "as", "from", "its", "their", "it", "we", "our", "than", "which", "while"}


def paragraphs(text):
    return [" ".join(p.split()) for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]


def split_sentences(para):
    if para.startswith("#"):
        return [para]
    p = para
    for i, a in enumerate(ABBR):
        p = p.replace(a, f"\x00{i}\x00")
    out = []
    for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\[\\$(*])", p):
        for i, a in enumerate(ABBR):
            s = s.replace(f"\x00{i}\x00", a)
        if s.strip():
            out.append(s.strip())
    return out


def words(s):
    return re.findall(r"[a-z0-9][a-z0-9@\-]*", s.lower())


def sim(x, y):
    return difflib.SequenceMatcher(None, words(x), words(y), autojunk=False).ratio()


def align(B, A):
    """Monotone sentence alignment allowing 1-1, 1-2, 2-1, 1-0 and 0-1; returns (before list, after list) units."""
    n, m = len(B), len(A)
    NEG = float("-inf")
    dp = [[NEG] * (m + 1) for _ in range(n + 1)]
    bk = [[None] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0.0
    for i in range(n + 1):
        for j in range(m + 1):
            if dp[i][j] == NEG:
                continue
            moves = [(1, 1), (1, 2), (2, 1), (1, 0), (0, 1)]
            for di, dj in moves:
                if i + di > n or j + dj > m:
                    continue
                if di and dj:
                    s = sim(" ".join(B[i:i + di]), " ".join(A[j:j + dj])) - (0.1 if di + dj > 2 else 0)
                else:
                    s = 0.0
                if dp[i][j] + s > dp[i + di][j + dj]:
                    dp[i + di][j + dj], bk[i + di][j + dj] = dp[i][j] + s, (di, dj)
    units, i, j = [], n, m
    while i or j:
        di, dj = bk[i][j]
        units.append((B[i - di:i], A[j - dj:j])); i, j = i - di, j - dj
    return units[::-1]


def count(term, text):
    return len(re.findall(r"(?<![\w-])" + re.escape(term.lower()) + r"(?![\w-])", text.lower()))


def skeleton_parts(path):
    sk = open(path, encoding="utf-8").read()
    m = re.search(r"^Names:\s*(.*)$", sk, re.M)
    names = [re.sub(r"\s*\(.*?\)$", "", n).strip() for n in re.split(r",\s*(?![^()]*\))", m.group(1))] if m else []
    keep = []
    for ln in re.findall(r"^Keep:\s*(.*)$", sk, re.M):
        ln = re.sub(r"\(optional\)", "", ln)
        keep += [k.strip(" .\"'") for k in re.split(r";", ln) if len(k.strip().split()) >= 1]
        keep += re.findall(r"\"([^\"]+)\"", ln)
    return [n for n in names if n and not n.startswith("$")], [k for k in keep if k]


def ledger_names(path):
    d = json.load(open(path, encoding="utf-8"))
    entries = d.get("entries", d) if isinstance(d, dict) else d
    return [e["term"] for e in entries if not e["term"].startswith("$")]


def renames(before, after):
    """Recurring 2-3 word phrases whose count fell by 2 or more, with the phrases that rose."""
    def grams(t):
        w = words(t)
        return collections.Counter(" ".join(w[i:i + n]) for n in (2, 3) for i in range(len(w) - n + 1))
    gb, ga = grams(before), grams(after)
    edge = lambda g: g.split()[0] in STOP or g.split()[-1] in STOP
    fell = {g: (gb[g], ga[g]) for g in gb if gb[g] >= 2 and gb[g] - ga[g] >= 2 and not edge(g)}
    rose = {g: (gb[g], ga[g]) for g in ga if ga[g] - gb[g] >= 2 and not edge(g)}
    # keep the longest phrase of each overlapping family
    pick = lambda d: [g for g in sorted(d, key=len, reverse=True) if not any(g != h and g in h and d[h] == d[g] for h in d)]
    return [(g, *fell[g]) for g in pick(fell)], [(g, *rose[g]) for g in pick(rose)]


def judge(bb, aa, names, keep):
    bt, at = " ".join(bb), " ".join(aa)
    undo, flags = [], []
    if sorted(PROTECT.findall(bt)) != sorted(PROTECT.findall(at)):
        undo.append("a number, [cite], REF or math span changed")
    if [x for x in aa if x.startswith("#")] != [x for x in bb if x.startswith("#")] or BOLD.findall(bt) != BOLD.findall(at):
        undo.append("a heading or bold label changed")
    lost = [k for k in keep if k.lower() in bt.lower() and k.lower() not in at.lower()]
    if lost:
        undo.append("Keep item dropped: " + "; ".join(lost))
    if not undo:
        if not aa:
            flags.append("sentence removed")
        elif not bb:
            flags.append("sentence added")
        fewer = [n for n in names if count(n, bt) > count(n, at)]
        if fewer:
            flags.append("ledger name used less: " + ", ".join(fewer))
        new = sorted({w for w in words(at) if w in STRENGTH and w not in set(words(bt))})
        if new:
            flags.append("new strength/scope/cause word: " + ", ".join(new))
        if bb and aa and len(bb) != len(aa):
            flags.append(f"{len(bb)} sentence(s) became {len(aa)}")
        lb, la = len(bt.split()), len(at.split())
        if lb and la and abs(la - lb) / lb >= 1 / 3:
            flags.append(f"length {lb} -> {la} words")
    return dict(before=bt, after=at, undone=undo, flags=flags)


def check(before_text, after_text, names, keep):
    """Final paragraphs and the change list. Paragraphs are aligned one to one when their number is unchanged
    (after headings the original did not have are dropped); otherwise the revision is not used."""
    pb, pa = paragraphs(before_text), paragraphs(after_text)
    changes, notes = [], []
    added = [p for p in pa if p.startswith("#") and p not in pb]
    if added:
        pa = [p for p in pa if p not in added]
        changes.append(dict(before="", after=" / ".join(added), undone=["a heading the original does not have"], flags=[]))
    if len(pa) != len(pb):
        notes.append(f"The revision has {len(pa)} paragraphs where the original has {len(pb)}; it moved, merged or "
                     "split paragraphs, so the original text is kept whole. Rerun the revision or skip step 8.")
        return pb, changes, notes
    final = []
    for b_par, a_par in zip(pb, pa):
        out = []
        for bb, aa in align(split_sentences(b_par), split_sentences(a_par)):
            if bb == aa:
                out += bb; continue
            c = judge(bb, aa, names, keep)
            changes.append(c)
            out += bb if c["undone"] else aa
        final.append(" ".join(out))
    return final, changes, notes


def report(changes, fell, rose, notes):
    kept = [c for c in changes if not c["undone"]]
    lines = [f"# Revision check\n\n{len(changes)} change(s): {len(changes) - len(kept)} put back by the script, "
             f"{len(kept)} for you to keep or undo ({sum(1 for c in kept if c['flags'])} flagged).\n"] + notes
    if fell:
        lines.append("Recurring phrases the revision used less (a rename across the text?): "
                     + "; ".join(f'"{g}" {x} -> {y}' for g, x, y in fell[:12])
                     + (". Rose: " + "; ".join(f'"{g}" {x} -> {y}' for g, x, y in rose[:12]) if rose else "") + "\n")
    lines.append("For each change: does it move a claim's verb or scope, turn an offered cause or reading into a "
                 "fact or the reverse, add or remove a claim, qualifier, intensifier, example or closing reading, "
                 "or put a second name on a thing? If so, undo it (or repair it, keeping the original's claim); "
                 "otherwise keep it. The text in the --out file has every change below applied.\n")
    for k, c in enumerate(changes, 1):
        tag = "PUT BACK: " + "; ".join(c["undone"]) if c["undone"] else ("FLAG: " + "; ".join(c["flags"]) if c["flags"] else "wording")
        lines.append(f"## {k}. {tag}\n\n- before: {c['before'] or '(nothing)'}\n- after: {c['after'] or '(nothing)'}\n")
    return "\n".join(lines)


def run(before_p, after_p, skeleton_p, names_p=None, out=None):
    before, after = open(before_p, encoding="utf-8").read(), open(after_p, encoding="utf-8").read()
    names, keep = skeleton_parts(skeleton_p)
    if names_p:
        names = sorted(set(names) | set(ledger_names(names_p)))
    final, changes, notes = check(before, after, names, keep)
    fell, rose = renames(before, after)
    out = out or os.path.splitext(after_p)[0] + ".checked.md"
    open(out, "w", encoding="utf-8").write("\n\n".join(final) + "\n")
    rep = os.path.splitext(out)[0] + ".changes.md"
    open(rep, "w", encoding="utf-8").write(report(changes, fell, rose, notes))
    n_undo = sum(1 for c in changes if c["undone"])
    print(f"revision check: {len(changes)} changed block(s), {n_undo} put back, {len(changes) - n_undo} to review "
          f"-> {out}, {rep}")
    return out, rep


if __name__ == "__main__":
    argv = sys.argv[1:]
    if len(argv) < 2 or "--skeleton" not in argv:
        sys.exit(__doc__)
    opt = lambda k: argv[argv.index(k) + 1] if k in argv else None
    run(argv[0], argv[1], opt("--skeleton"), opt("--names"), opt("--out"))
