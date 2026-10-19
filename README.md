# ML Paper Humanizer

A skill for Claude Code and Codex that writes and revises the English text of ML conference papers (ICLR, NeurIPS, ICML, ACL, CVPR and the like) so that it reads as written by a person. In Chinese: 去 AI 味.

[中文](README.zh-CN.md) · [Full example](examples/results-2504.13837.md)

## Highlights

- **AI smell is five writing actions, not a word list.** The skill looks for performing, defending, piling, restating and drifting, and removes the action; the wording then follows. Word lists and sentence quotas were tested and dropped, because drafts written under them read as templates.
- **The phrases are counted from 307 award and oral papers** at NeurIPS, ICML, ICLR, ACL, CVPR and seven other venues, 2023 to 2026: 1,234 stock phrases by sentence function, each used in at least 6 of those papers, plus the connectives and reporting verbs from the same count. A ★ marks the phrases that published passages use and model drafts of the same passages rarely do.
- **The sentence rules come from the writing guides**: Gopen and Swan, Williams, Strunk, Fowler, Zinsser, Feak and Swales, and Pinker. The point of a sentence sits in its main clause, the subject stays next to its verb, and what the sentence adds lands at its end, where the reader pauses.
- **Your paper keeps its own names and numbers.** A term ledger is built from your text and the papers you cite and verified word by word; each thing then has one name. Numbers, model and dataset names, citations and defined terms are never changed, and a doubtful number is flagged rather than corrected.
- **A claim never outruns its evidence.** Reporting verbs follow a ladder from "consistent with" to "demonstrates", what a component was designed to do stays apart from what it did, and a concession takes one clause.
- **It writes as well as revises.** `write` drafts a passage from an outline, notes or a Chinese draft; `rewrite` makes minimal edits and lists each change with its reason. A LaTeX checker reports repetition that is abnormal for your own document and sets no thresholds.

## Before and after

Two paragraphs from the results section of a NeurIPS 2025 runner-up paper ([arXiv 2504.13837](https://arxiv.org/abs/2504.13837), CC BY 4.0). The same model wrote them twice from the same content outline, without the authors' text.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="examples/compare-dark.png">
  <img alt="Two paragraphs of a results section written without the skill and with it, side by side; the left marks the writer's images and coined headings, the right marks the field's frames and the paper's own names" src="examples/compare.png">
</picture>

On the left, the model coins its own headings, reads the figure through its own image ("the crossover persists"), answers an objection before the test is stated, and describes things the paper has names for. On the right, each paragraph says what it is for before the number, points to the figure with the field's phrases, keeps the paper's names (*reasoning ability boundary*, *hacking or lucky guesses*), and puts the inference behind a reporting verb. Both drafts in full, with the authors' passage, are in [examples/results-2504.13837.md](examples/results-2504.13837.md).

At sentence level, the skill's teaching material is 40 pairs like these: a model's draft beside the authors' sentence for the same job.

| Job | A model's draft | The authors |
|---|---|---|
| Say why a comparison is unfair | That yardstick, however, measures a different goal. | This would not be a fair comparison, because LMNet is a general method to improve the intelligence of a given LLM, with additional training cost only less than 1% of the pre-training. ([2505.12741](https://arxiv.org/abs/2505.12741)) |
| Give the number after the question it answers | Notably, SFT on the same data lowers mean accuracy by 5.7% relative to Prompt. | Second, one may argue that the improvement mainly relies on training data. SFT (implemented by very moderate training configurations) can hardly bring improvement over the pre-trained LLM (-5.7%). ([2505.12741](https://arxiv.org/abs/2505.12741)) |
| Mark the surprise | Actual LLMs, shown as gray points in the same panel, follow a similar exponent near 1. | Remarkably, we find that actual LLMs follow a similar scaling. ([2505.10465](https://arxiv.org/abs/2505.10465)) |

## How the skill works

**The five actions.** AI smell in a paper is a handful of things the writer does, and each has a name in the skill.

- *Performing*: a conclusion dressed up as an insight.
- *Defending*: the reviewer's rebuttal written into the paper.
- *Piling*: numbers, clauses and citations shovelled into one sentence.
- *Restating*: the heading, the first sentence, the last sentence and the caption all saying one thing.
- *Drifting*: one object under three names, or an internal label left in the paper.

**What the reader needs.** The read-back checks the draft against seven needs, taken from the writing guides and from the award papers. Clear in one pass: one point per sentence, in the main clause, with its context in a short clause before it (Williams; Gopen and Swan). Oriented: the reader knows what a paragraph is for before its detail. Linked: a sentence opens on what the reader already holds and ends on what it adds, so most links need no connective (Gopen and Swan; Strunk). Named: one name per thing, the author's (Fowler, on elegant variation). Grounded: a result sentence says what the result means, and a surprise is marked as one. Plain where it counts: a technical point is followed by the same point in plain words. Easy to follow: a paragraph keeps one topic string, actions are verbs with their agent as subject, and parallel items take parallel shape. The connectives file quotes the guides on when a connective is needed and when the order carries the relation (Zinsser, Feak and Swales, Pinker).

**The seven steps.** `SKILL.md` runs them on every request.

1. Choose the paper's orientation, proof / effect / design / evaluation / discovery, and read that section's frame in the playbook.
2. Build the term ledger from your text and the papers it cites; the script keeps only names found verbatim.
3. Read the sentence bank for the moves about to be written, three exemplar passages in `write` mode, and the connectives file once.
4. Write or revise. How a sentence follows the last is decided as it is written.
5. Read back three times: for fidelity, for the ledger, and for the reader's needs above.
6. Run the frames pass (always in `write`, on request in `rewrite`): go through the draft sentence by sentence with the frames file and add the field's phrase where a sentence points, observes, reads, compares or hands off. Connectives and verbs stay as written.
7. Run the checker and fix what is a real problem.

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

`rewrite` is the default: wording that reads in one pass is kept, and you get the revised text with a change list (before, after, reason). `write` drafts from an outline, notes or a Chinese draft; the paper text stays in English, and a clause-by-clause Chinese version can be added on request.

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
