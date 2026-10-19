# ML Paper Humanizer

A skill for Claude Code, Codex and other agents that writes and revises the English prose of ML conference papers (ICLR, NeurIPS, ICML, ACL, CVPR and the like) so that it reads as written by its authors rather than by a model.

Its rules, phrase lists and examples are counted from 307 award and oral papers, not from a list of banned words. It keeps your paper's own vocabulary, sizes every claim to its evidence, never touches a number or a citation, and writes new passages as well as revising existing ones.

[中文说明](README.zh-CN.md) · [Example: one section written three ways](examples/results-2504.13837.md) · [What changed and what was withdrawn](references/CHANGELOG.md)

## Before and after

Two paragraphs from the results section of a NeurIPS 2025 runner-up paper ([arXiv 2504.13837](https://arxiv.org/abs/2504.13837), CC BY 4.0). The same model wrote it twice from the same content outline, without seeing the authors' wording; only the run with the skill built a term ledger.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="examples/compare-dark.png">
  <img alt="Two paragraphs of a results section written without the skill and with it, side by side, with the writer's images and coined labels marked on the left and the field's frames and the paper's own names marked on the right" src="examples/compare.png">
</picture>

Without the skill, the model coins its own headings, reads the figure through its own images ("the crossover persists"), argues with an objection before the test is stated, and describes things the paper has names for. With the skill, each paragraph says what it is for before the number, points to the figure the way the field does, keeps the paper's names (*reasoning ability boundary*, *hacking or lucky guesses*), puts the inference behind a reporting verb, and hands off to the analysis section. The full section in both versions, with the authors' passage for comparison, is in [examples/results-2504.13837.md](examples/results-2504.13837.md).

At sentence level, the skill's teaching material is 40 pairs like these, each a model's draft set against the authors' sentence for the same job:

| Job | A model's draft | The authors |
|---|---|---|
| Say why a comparison is unfair | That yardstick, however, measures a different goal. | This would not be a fair comparison, because LMNet is a general method to improve the intelligence of a given LLM, with additional training cost only less than 1% of the pre-training. ([2505.12741](https://arxiv.org/abs/2505.12741)) |
| Give the number after the question it answers | Notably, SFT on the same data lowers mean accuracy by 5.7% relative to Prompt. | Second, one may argue that the improvement mainly relies on training data. SFT (implemented by very moderate training configurations) can hardly bring improvement over the pre-trained LLM (-5.7%). ([2505.12741](https://arxiv.org/abs/2505.12741)) |
| Mark the surprise | Actual LLMs, shown as gray points in the same panel, follow a similar exponent near 1. | Remarkably, we find that actual LLMs follow a similar scaling. ([2505.10465](https://arxiv.org/abs/2505.10465)) |
| Ask two questions as two sentences | As the degree of superposition and the structure of the data change, when does the loss follow a power law in width, and, when it does, what is its exponent? | Varying the degree of superposition and data structure, when is the loss a power law? And if the loss is a power law, what will the exponent be? ([2505.10465](https://arxiv.org/abs/2505.10465)) |

## Why this one

**AI smell is five writing actions, not a word list.** The skill looks for performing (a conclusion dressed up as an insight), defending (the reviewer's rebuttal written into the paper), piling (numbers, clauses and citations in one sentence), restating (heading, first sentence, last sentence and caption all saying one thing) and drifting (one object under three names). Remove the action and the wording follows. Banned-word lists and sentence quotas were tried in the first five versions and withdrawn: drafts written under them read as templates, and the model applies any count or ban at every opportunity until it becomes a new mannerism.

**Counted from the papers, not asserted.** The phrase frames, connectives and reporting verbs come from 307 award and oral papers at NeurIPS, ICML, ICLR, ACL, EMNLP, NAACL, COLM, CVPR, ICCV, ECCV, AAAI and KDD, 2023 to 2026. The frames file lists 1,234 stock phrases by sentence function, each used in at least 6 of those papers, and a ★ marks the ones published passages use and model drafts of the same passages almost never do. Mining 60 original passages against 318 drafts showed that what readers call "not senior" is mostly this gap: the field's ordinary pointers and connectives, not rare words.

**Your paper's own vocabulary.** A term ledger is built from your text and the papers you cite, and every name in it is verified verbatim against the source. Each thing then keeps one name, the author's, and no new label is coined for a thing you already named. A generic humanizer that turns a model name into "the model" or a defined term into a paraphrase is doing the thing reviewers notice first.

**Claims sized to evidence, numbers untouched.** Reporting verbs follow a ladder (consistent with, suggests, indicates, shows, demonstrates). What a component is designed to do stays apart from what it did. A concession takes one clause, never a paragraph of self-defence. Numbers, model and dataset names, defined terms, citations and any wording you asked to keep are never changed; a number that looks wrong is flagged, not corrected.

**Section frames by what the paper argues.** The playbook covers every section from abstract to rebuttal, with the reader's expectations split by five orientations: proof, effect, design, evaluation and discovery. A method paper and an analysis paper do not write their results section the same way, and the skill knows which one it is writing.

**Checks relative to your own document, with no thresholds.** The LaTeX checker reports what is abnormal for this paper: the same opener in consecutive paragraphs, a run of same-length sentences, a term under two names, a heading restated by its paragraph, a gain whose two sides are never named, a ledger name the draft never uses. It never says a count is too high or too low, because the originals do each of these things sometimes and never on a schedule.

**Writes as well as rewrites.** `write` mode drafts a passage from an outline, notes or a Chinese draft, reads three exemplar passages of the same section type first, and runs the frames pass afterwards. `rewrite` mode makes minimal edits and returns a change list with a reason for each.

**Every rule earned its place.** The [changelog](references/CHANGELOG.md) records each version, what it added, and the blind reading or measurement that withdrew it: the readability layer that chopped sentences, the register pass whose "improvements" were verb swaps readers disliked, the connective pass that only re-cast relations the draft already stated, the colon rule withdrawn because originals and drafts had the same rate. The exemplar pool and the sentence bank list every source paper with its license.

## How it compares

| | Word-list humanizers | This skill |
|---|---|---|
| What counts as AI smell | Words and patterns from a general list (delve, tapestry, em dashes) | Five writing actions in a paper's argument |
| Where the rules come from | A style guide for any text | 307 award and oral ML papers, counted |
| Your terms and numbers | May be paraphrased | Ledger-verified names; numbers, citations and defined terms never change |
| Claim strength | Hedges removed or added by instruction | Reporting verb chosen by what the evidence is; concession in one clause |
| Scope | Any text | ML papers, every section, five paper orientations |
| New text | Edits only | Writes from an outline or a Chinese draft, with exemplars and a frames pass |
| Checks | Model judgement | Scripts that compare the document with itself, plus the model |
| Evidence | Screenshots | Changelog of withdrawals; blind reads against the originals |

The closest general tool, [humanizer](https://github.com/blader/humanizer), removes the patterns in Wikipedia's "Signs of AI writing" from any kind of text. The idea of writing a paper around what it achieves rather than around every objection comes from [anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill); here that is one of the five actions, with a reporting-verb ladder behind it.

## Install

Claude Code:

```bash
git clone https://github.com/Fwibo/ml-paper-humanizer ~/.claude/skills/ml-paper-humanizer
```

Codex CLI:

```bash
git clone https://github.com/Fwibo/ml-paper-humanizer ~/.codex/skills/ml-paper-humanizer
```

Any other agent that loads Agent Skills (a folder with a `SKILL.md`) can use the same folder. For claude.ai, zip the folder and upload it under Settings → Capabilities → Skills.

The checker and the exemplar picker need only Python 3. The term ledger's candidate step needs spaCy, and reading cited PDFs needs PyMuPDF; without them, the ledger is listed by the model and verified by the script.

```bash
pip install spacy pymupdf && python -m spacy download en_core_web_sm
```

## Use

Ask in your own words. The skill triggers on writing, revising or polishing a paper, including requests in Chinese (去 AI 味, 润色, 改论文, 别太防御, 回审稿意见):

- "Rewrite the second paragraph of my results section, it reads like AI."
- "Write the introduction from these notes. It is a discovery paper."
- "Make this abstract less defensive."
- "Don't change anything yet, tell me what is wrong with this section."
- `/ml-paper-humanizer sec/experiments.tex`

Two modes. `rewrite` (default) keeps wording that already reads in one pass and returns the revised text with a change list (before, after, reason). `write` drafts a new passage from an outline, notes or a Chinese draft; the paper text stays in English, and a clause-by-clause Chinese version can be added on request.

The scripts also run on their own:

```bash
python scripts/check_tex.py paper/ --ledger ledger.json
python scripts/term_ledger.py paper/main.tex --cited refs/*.pdf --out ledger.json
python scripts/pick_exemplars.py results --orientation discovery
```

## How it works

`SKILL.md` runs seven steps on every request.

1. **Orientation and section.** Choose proof / effect / design / evaluation / discovery and read that section's frame in the playbook.
2. **Term ledger.** Build the paper's names from your text and the papers it cites; the script keeps only names found verbatim.
3. **Read the examples** for the moves about to be written: the sentence bank, three exemplar passages (in `write` mode), and the connectives file once.
4. **Write or revise.** How each sentence follows the last is decided as it is written; most need no connective.
5. **Read back** three times: for fidelity, for the ledger, and for the reader's needs (one point per sentence, the point in the main clause, what the sentence adds at its end).
6. **Frames pass** (always in `write`, on request in `rewrite`): go through the draft sentence by sentence with the full frames file and add the field's marking frames where a sentence does that job. Connectives and verbs are not touched.
7. **Run the checker** and fix what is a real problem; say when a flag is a false alarm.

## What it does not do

- It has never been tested against AI detectors (GPTZero, Turnitin, CNKI) and makes no claim about them. It is aimed at what a reviewer notices.
- It does not verify citations or check that a cited paper says what you say it says.
- It does not adapt to a target venue's house style or match your personal voice from your earlier papers.
- It covers ML, NLP and CV papers. Other fields may use the sentence rules, but the corpus is ML.
- A draft written with it still runs shorter and uses fewer of the field's verbs than the authors do; the example file shows the current gap.

## What is in the repository

```
SKILL.md                      the seven steps, the reader's needs, the read-back list, the output contract
references/
  section-playbook.md         what each section does, from abstract to rebuttal, by paper orientation
  sentence-bank.md            40 draft-vs-authors pairs by failure type, 23 further sentences by move
  register-frames.md          1,234 stock phrases by sentence function, with paper counts and ★ marks
  connectives.md              cause, consequence, contrast and concession forms from the same count
  claim-strength.md           reporting-verb ladder, design intent vs outcome, the honesty line
  exemplars/                  144 introduction and results passages from 30 papers, with SOURCES.md
  CHANGELOG.md                every version, what it added, what withdrew it
scripts/
  check_tex.py                anomaly checks relative to the document itself, no thresholds
  term_ledger.py              ledger candidates from your text and cited papers; --verify keeps verbatim names
  pick_exemplars.py           three exemplar passages for a section type and orientation
examples/
  results-2504.13837.md       one results section: without the skill, with it, and the authors
  compare.html, compare*.png  the side-by-side figure above and the HTML it is rendered from
```

## Sources and licenses

The skill itself (SKILL.md, the scripts and the reference files written for it) is released under the MIT License; see `LICENSE`.

The exemplar passages are short excerpts from 30 papers under CC BY 4.0 or CC0 1.0, listed with their licenses in `references/exemplars/SOURCES.md`. The sentence bank quotes single sentences from award papers, and its Sources section lists each paper and its license. Copyright in all quoted text stays with its authors. Citations and cross-references in the excerpts are replaced by `[cite]` and `REF`, and the skill tells the model never to reuse their content or any run of six or more words. The frames and connectives files contain phrases and counts only, no paper text.
