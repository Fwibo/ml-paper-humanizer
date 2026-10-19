# ML Paper Humanizer

A skill for Claude Code and Codex that writes and revises the English text of ML conference papers (ICLR, NeurIPS, ICML, ACL, CVPR and the like). It has one goal: the paper reads as written by a person. In Chinese, 去 AI 味.

[中文](README.zh-CN.md) · [Full example](examples/results-2504.13837.md)

## Highlights

**1. The phrases of award-winning papers, counted.** We collected every award and oral paper from NeurIPS, ICML, ICLR, ACL, EMNLP, NAACL, COLM, CVPR, ICCV, ECCV, AAAI and KDD, 2023 to 2026, 307 papers in all, and counted the words and phrases academic writing runs on. They are sorted by what a sentence does: point to a figure, report a result, compare, state a purpose, limit scope, order steps, name a thing, describe a method. There are 1,234 of them, each used in at least 6 of the papers. The connectives and reporting verbs come from the same count. We also compared 60 original passages with 318 model drafts of the same content; the phrases the originals use and the drafts almost never do are marked ★. When a model draft reads as "not senior", the gap is mostly these ordinary phrases.

**2. What the writing guides say and models skip.** These books teach academic writing: Gopen and Swan, *The Science of Scientific Writing*; Williams, *Style: Toward Clarity and Grace*; Strunk, *The Elements of Style*; Fowler, *The King's English*; Zinsser, *On Writing Well*; Swales and Feak, *Academic Writing for Graduate Students*; Pinker, *The Sense of Style*. The skill takes from them the points a model most often misses, follows them while writing and checks them in the read-back:

- New information goes at the end of the sentence, where the reader pauses and remembers; old information opens the sentence and picks up the one before (Gopen and Swan, Williams).
- The subject stays next to its verb; the point sits in the main clause, with its context in a short clause before it (Gopen and Swan).
- An action is a verb, and whoever does it is the subject, not a nominalization on an empty verb (Williams).
- A turn is marked early, so the reader does not read half a sentence in the wrong direction (Zinsser); a connective is added only where the order of the sentences does not carry the relation (Strunk, Pinker).
- One thing keeps one name, because a second word suggests a second thing (Fowler); parallel items take parallel form (Strunk).
- Claims match the evidence: reporting verbs follow a ladder, consistent with, suggests, indicates, shows, demonstrates; what a component was designed to do stays apart from what it did; a concession takes one clause.

**3. Terms extracted and aligned.** Every object, mechanism, setting and finding in a paper has the authors' own name. The skill extracts these names from your text and the papers you cite, verifies each one word for word, and keeps them in a term ledger. From then on each thing has one name, and nothing already named gets a new label. Numbers, model and dataset names, citations and defined terms are never changed; a doubtful number is flagged, not corrected. A general humanizer that turns a model name into "the model" or a defined term into a paraphrase makes the change a reviewer notices first.

## Before and after

Two paragraphs from the results section of a NeurIPS 2025 runner-up paper ([arXiv 2504.13837](https://arxiv.org/abs/2504.13837), CC BY 4.0). The same model wrote them twice from the same content outline, without the authors' text.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="examples/compare-dark.png">
  <img alt="Two paragraphs of a results section written without the skill and with it, side by side; the left marks the writer's images and coined headings, the right marks the field's frames and the paper's own names" src="examples/compare.png">
</picture>

On the left, the model coins its own headings, reads the figure through its own image ("the crossover persists"), answers an objection before the test is stated, and describes things the paper has names for. On the right, each paragraph says what it is for before the number, points to the figure with the field's phrases, keeps the paper's names (*reasoning ability boundary*, *hacking or lucky guesses*), and puts the inference behind a reporting verb. Both drafts in full, with the authors' passage, are in [examples/results-2504.13837.md](examples/results-2504.13837.md).

At sentence level, the skill's teaching material is 40 pairs like these: the same job, written by a model and by the authors.

| Job | A model's draft | The authors |
|---|---|---|
| Say why a comparison is unfair | That yardstick, however, measures a different goal. | This would not be a fair comparison, because LMNet is a general method to improve the intelligence of a given LLM, with additional training cost only less than 1% of the pre-training. ([2505.12741](https://arxiv.org/abs/2505.12741)) |
| Give the question, then the number | Notably, SFT on the same data lowers mean accuracy by 5.7% relative to Prompt. | Second, one may argue that the improvement mainly relies on training data. SFT (implemented by very moderate training configurations) can hardly bring improvement over the pre-trained LLM (-5.7%). ([2505.12741](https://arxiv.org/abs/2505.12741)) |
| Mark the surprise | Actual LLMs, shown as gray points in the same panel, follow a similar exponent near 1. | Remarkably, we find that actual LLMs follow a similar scaling. ([2505.10465](https://arxiv.org/abs/2505.10465)) |

## How the skill works

**AI smell is five actions, not a word list.** Taken apart, the AI smell in a paper is a few things the writer does:

- *Performing*: a conclusion dressed up as an insight.
- *Defending*: the reviewer's rebuttal written into the paper.
- *Piling*: numbers, clauses and citations shovelled into one sentence.
- *Restating*: the heading, the first sentence, the last sentence and the caption all saying one thing.
- *Drifting*: one object under three names, or an internal label left in the paper.

Remove the action and the wording follows. The skill has no banned-word list; word lists and sentence quotas were tested, produced drafts that read as templates, and were dropped.

**Two modes.** `rewrite` is the default: wording that reads in one pass is kept, and you get the revised text with a change list (before, after, reason). `write` drafts a passage from an outline, notes or a Chinese draft; the paper text stays in English, and a clause-by-clause Chinese version can be added on request. Ask in Chinese and the skill answers in Chinese.

**Seven steps.** `SKILL.md` runs them in this order on every request.

1. Choose the paper's orientation, proof / effect / design / evaluation / discovery, and read that section's frame in the playbook.
2. Build the term ledger from your text and the papers it cites; the script keeps only names found verbatim.
3. Read the examples: the sentence bank for the moves about to be written, three exemplar passages in `write` mode, and the connectives file once.
4. Write or revise. How a sentence follows the last is decided as it is written.
5. Read back three times: for fidelity, for the ledger, and for the points from the writing guides above.
6. Run the frames pass (always in `write`, on request in `rewrite`): go through the draft sentence by sentence with the frames file, and where a sentence points to a figure, reports an observation, gives a reading, compares, or hands off, use the field's phrase. Connectives and verbs stay as written.
7. Run the checker. It reports repetition that is abnormal for this document: the same opener in consecutive paragraphs, a run of same-length sentences, a term under two names, a heading restated by its paragraph, a gain whose two sides are never named. It sets no thresholds and never says a count is too high or too low. Fix what is a real problem and say when a flag is a false alarm.

**What it does not do.** It has not been tested against AI detectors and makes no claim about them; it is aimed at what a reviewer notices. It does not verify citations, adapt to a venue's house style, or learn your voice from earlier papers. The corpus is ML, NLP and CV. A draft written with it still runs shorter and uses fewer of the field's verbs than the authors do; the example file shows the gap.

**How it was tested.** Every rule was tried the same way: a model wrote a section of an award paper from its outline, and the draft was read against the original. What failed that reading was dropped: a readability layer that chopped sentences, a register pass whose changes were verb swaps readers disliked, a connective pass that only re-cast relations the draft already stated, and a rule on colons, because originals and drafts had the same rate.

## Install and use

Claude Code:

```bash
git clone https://github.com/Fwibo/ml-paper-humanizer ~/.claude/skills/ml-paper-humanizer
```

Codex CLI:

```bash
git clone https://github.com/Fwibo/ml-paper-humanizer ~/.codex/skills/ml-paper-humanizer
```

Any other agent that loads Agent Skills (a folder with a `SKILL.md`) can use the same folder. For claude.ai, zip the folder and upload it under Settings → Capabilities → Skills.

The checker and the exemplar picker need only Python 3. The term ledger's candidate step needs spaCy, and reading cited PDFs needs PyMuPDF; without them the ledger is listed by the model and verified by the script.

```bash
pip install spacy pymupdf && python -m spacy download en_core_web_sm
```

Ask in your own words, in English or Chinese. The skill triggers on writing, revising or polishing a paper:

- "Rewrite the second paragraph of my results section, it reads like AI."
- "Write the introduction from these notes. It is a discovery paper."
- "Make this abstract less defensive."
- "Don't change anything yet, tell me what is wrong with this section."
- `/ml-paper-humanizer sec/experiments.tex`

The scripts also run on their own:

```bash
python scripts/check_tex.py paper/ --ledger ledger.json
python scripts/term_ledger.py paper/main.tex --cited refs/*.pdf --out ledger.json
python scripts/pick_exemplars.py results --orientation discovery
```

## What is in the repository

```
SKILL.md                      the seven steps, the reader's needs, the read-back list, the output contract
references/
  section-playbook.md         what each section does, from abstract to rebuttal, by paper orientation
  sentence-bank.md            40 draft-vs-authors pairs by failure type, 23 further sentences by move
  register-frames.md          1,234 stock phrases by sentence function, with paper counts and ★ marks
  connectives.md              what the writing guides say, then the cause, contrast and concession forms
  claim-strength.md           the reporting-verb ladder, design intent apart from outcome
  exemplars/                  144 introduction and results passages from 30 papers, with SOURCES.md
scripts/
  check_tex.py                repetition checks relative to the document itself, no thresholds
  term_ledger.py              ledger candidates from your text and cited papers; --verify keeps verbatim names
  pick_exemplars.py           three exemplar passages for a section type and orientation
examples/
  results-2504.13837.md       one results section: without the skill, with it, and the authors
  compare.html, compare*.png  the figure above and the HTML it is rendered from
```

## Sources and licenses

The skill itself (SKILL.md, the scripts and the reference files written for it) is released under the MIT License; see `LICENSE`.

The exemplar passages are short excerpts from 30 papers under CC BY 4.0 or CC0 1.0, listed with their licenses in `references/exemplars/SOURCES.md`. The sentence bank quotes single sentences from award papers, and its Sources section lists each paper and its license. Copyright in all quoted text stays with its authors. Citations and cross-references in the excerpts are replaced by `[cite]` and `REF`, and the skill tells the model never to reuse their content or any run of six or more words. The frames and connectives files contain phrases and counts only.

The idea of writing a paper around what it achieves rather than around every objection comes from [anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill) (MIT). [humanizer](https://github.com/blader/humanizer) removes the patterns in Wikipedia's "Signs of AI writing" from any kind of text; this skill covers ML papers and works from the papers themselves.
