#!/usr/bin/env python3
"""Print 3 passages of published papers for the section being written (style reference, read before writing).
Usage: pick_exemplars.py <intro|results> [--orientation ...] [--n 3] [--seed k]
Passages come from references/exemplars/ (award / reference papers, macros expanded, cites and refs neutralised).
The pool holds introductions and results sections only; "method", "experiments" and "analysis" draw from results,
anything else from intro. Three different papers are drawn; with --orientation one of the three matches it when available."""
import json, os, random, sys
a = sys.argv[1:]; sec = a[0] if a else "intro"; sec = "results" if sec in ("results", "experiments", "analysis", "method") else "intro"
orient = a[a.index("--orientation") + 1] if "--orientation" in a else None
n = int(a[a.index("--n") + 1]) if "--n" in a else 3
rng = random.Random(int(a[a.index("--seed") + 1]) if "--seed" in a else None)
here = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references", "exemplars")
pool = [p for p in json.load(open(os.path.join(here, "index.json"))) if p["section"] == sec]
ids = sorted({p["id"] for p in pool}); rng.shuffle(ids); chosen = []
if orient:
    m = [i for i in ids if any(p["id"] == i and p["orientation"] == orient for p in pool)]
    if m: chosen.append(m[0]); ids = [i for i in ids if i != m[0]]
chosen += ids[:n - len(chosen)]
print("# Passages from published papers, same section type. Read for pacing, where the claim sits, how pointers fold in, how much is hedged. Their content and terms are off limits, and no run of six or more words from them may appear in your text.\n")
for k, i in enumerate(chosen, 1):
    p = rng.choice([q for q in pool if q["id"] == i])
    print(f"## Passage {k}\n"); print(open(os.path.join(here, p["file"])).read())
