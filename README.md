# ML Paper Humanizer

A skill for Claude Code and Codex that writes and revises the English text of ML conference papers (ICLR, NeurIPS, ICML, ACL, CVPR and the like). Its goal is to remove the AI smell, so that the paper reads as written by a person.

[中文](README.zh-CN.md) · [Full example](examples/results-2504.13837.md)

## Highlights

**1. The phrases of award-winning papers, counted.** The corpus is every award and oral paper from NeurIPS, ICML, ICLR, ACL, EMNLP, NAACL, COLM, CVPR, ICCV, ECCV, AAAI and KDD, 2023 to 2026, 307 papers in all. From it we counted the words and phrases of academic writing and sorted them by sentence function: pointing to a figure, reporting a result, comparing, stating a purpose, limiting scope, ordering steps, naming, describing a method. There are 1,234 phrases, each used in at least 6 of the papers. A comparison of 60 original passages with 318 model drafts of the same content shows that the academic register a model draft lacks lies mostly in these common phrases.

**2. The points AI writing omits, taken from authoritative guides.** Seven standard references: Gopen and Swan, *The Science of Scientific Writing* (*American Scientist*, a staple of scientific writing courses); Williams, *Style: Toward Clarity and Grace* and Swales and Feak, *Academic Writing for Graduate Students* (writing textbooks from the University of Chicago Press and the University of Michigan Press); Strunk, *The Elements of Style* and Fowler, *The King's English* (the classic authorities on English style); Zinsser, *On Writing Well*; Pinker, *The Sense of Style*. The points a model most often omits are followed while writing and checked in the read-back:

- New information goes at the end of the sentence; old information opens it and connects to the sentence before (Gopen and Swan, Williams).
- The subject stays next to its verb; the point sits in the main clause, its context in a short clause before it (Gopen and Swan).
- An action is a verb with its agent as subject (Williams).
- A turn is marked early (Zinsser); a connective is added only where the order of the sentences does not carry the relation (Strunk, Pinker).
- One thing keeps one name (Fowler); parallel items take parallel form (Strunk).
- Claims match the evidence: reporting verbs follow the ladder consistent with, suggests, indicates, shows, demonstrates; design intent is stated apart from outcome; a concession takes one clause.

**3. Terms extracted and aligned.** Each sub-field has established names for its objects, mechanisms, settings and findings. The skill extracts these terms from your text and the papers you cite, verifies that each occurs verbatim, and keeps them in a term ledger. From then on each thing has one name, and nothing already named receives a new label. Numbers, model and dataset names, citations and defined terms are never changed; a doubtful number is flagged rather than corrected. General humanizers often turn a model name into "the model" or a term into a paraphrase, and a reviewer identifies such changes at once.

## Before and after

Two paragraphs from the results section of a NeurIPS 2025 runner-up paper ([arXiv 2504.13837](https://arxiv.org/abs/2504.13837), CC BY 4.0). The same model wrote them twice from the same content outline, without access to the published text.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="examples/compare-dark.png">
  <img alt="Two paragraphs of a results section written without the skill and with it, side by side; the left marks the writer's images and coined headings, the right marks the field's phrases and the paper's own terms" src="examples/compare.png">
</picture>

On the left, the model coins its own headings, interprets the figure through its own image ("the crossover persists"), answers an objection before the experiment is described, and replaces named things with descriptions. On the right, each paragraph states its purpose before the number, points to the figure with the field's phrases, keeps the paper's terms (*reasoning ability boundary*, *hacking or lucky guesses*), and introduces the inference with a reporting verb. Both drafts in full, with the published passage, are in [examples/results-2504.13837.md](examples/results-2504.13837.md).

At sentence level, the skill's teaching material is 40 pairs like these: the same writing task, one sentence from a model draft and one from a published paper.

| Task | Model draft | Published text |
|---|---|---|
| Say why a comparison is unfair | That yardstick, however, measures a different goal. | This would not be a fair comparison, because LMNet is a general method to improve the intelligence of a given LLM, with additional training cost only less than 1% of the pre-training. ([2505.12741](https://arxiv.org/abs/2505.12741)) |
| Give the question, then the number | Notably, SFT on the same data lowers mean accuracy by 5.7% relative to Prompt. | Second, one may argue that the improvement mainly relies on training data. SFT (implemented by very moderate training configurations) can hardly bring improvement over the pre-trained LLM (-5.7%). ([2505.12741](https://arxiv.org/abs/2505.12741)) |
| Mark the surprise | Actual LLMs, shown as gray points in the same panel, follow a similar exponent near 1. | Remarkably, we find that actual LLMs follow a similar scaling. ([2505.10465](https://arxiv.org/abs/2505.10465)) |

## How the skill works

**AI smell is five writing actions, not a word list.** The AI smell in a paper reduces to five things the writer does:

- *Performing*: a conclusion presented as an insight.
- *Defending*: the reviewer's rebuttal written into the paper.
- *Piling*: numbers, clauses and citations packed into one sentence.
- *Restating*: the heading, the first sentence, the last sentence and the caption all expressing one point.
- *Drifting*: one object under several names, or an internal label left in the paper.

Remove the action and the wording follows. The skill has no banned-word list: word lists and sentence quotas were tested, produced drafts that read as templates, and were removed.

**Two modes.** `rewrite` is the default: wording that reads in one pass is kept, and the output is the revised text with a change list (before, after, reason). `write` drafts a passage from an outline, notes or a Chinese draft; the paper text stays in English, and a clause-by-clause Chinese version can be added on request. A request in Chinese receives an answer in Chinese.

**Seven steps.** `SKILL.md` runs them in this order on every request.

1. Determine the paper's orientation (proof / effect / design / evaluation / discovery) and read that section's frame in the playbook.
2. Build the term ledger from your text and the papers it cites.
3. Read the examples: the sentence bank for the moves about to be written, and three exemplar passages in `write` mode.
4. Write or revise. The relation between each sentence and the one before it is decided as the sentence is written.
5. Read back three times: for fidelity, for the ledger, and for the points from the writing guides above.
6. Run the frames pass (always in `write`, on request in `rewrite`): check the draft sentence by sentence against the frames file, and where a sentence points to a figure, reports an observation, gives a reading, compares, or hands off, use the field's phrase.
7. Run the checker, which reports repetition that is abnormal for this document, such as a term under two names, a heading restated by its paragraph, or a gain whose two sides are never named.

**What it does not do.** It has not been tested against AI detectors and makes no claim about them; it addresses what a reviewer can read. It does not verify citations, adapt to a venue's house style, or learn a personal voice from earlier papers. The corpus covers ML, NLP and CV. A draft written with it is still shorter than the published text and uses fewer of the field's verbs; the example file shows the gap.

**How it was tested.** Every rule was tested the same way: a model wrote a section of an award paper from its outline, the draft was read against the original, and rules that failed this reading were removed.

## Install and use

Claude Code:

```bash
git clone https://github.com/Fwibo/ml-paper-humanizer ~/.claude/skills/ml-paper-humanizer
```

Codex CLI:

```bash
git clone https://github.com/Fwibo/ml-paper-humanizer ~/.codex/skills/ml-paper-humanizer
```

Any other agent that loads Agent Skills (a folder containing `SKILL.md`) can use the same folder. For claude.ai, zip the folder and upload it under Settings → Capabilities → Skills.

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
  sentence-bank.md            40 pairs of model draft and published text by failure type, 23 further sentences by move
  register-frames.md          1,234 phrases by sentence function, with paper counts
  connectives.md              the points from the writing guides, then the cause, contrast and concession forms
  claim-strength.md           the reporting-verb ladder, design intent apart from outcome
  exemplars/                  144 introduction and results passages from 30 papers, with SOURCES.md
scripts/
  check_tex.py                repetition checks relative to the document itself, no thresholds
  term_ledger.py              term candidates from your text and cited papers; --verify keeps verbatim terms
  pick_exemplars.py           three exemplar passages for a section type and orientation
examples/
  results-2504.13837.md       one results section: without the skill, with it, and the published text
  compare.html, compare*.png  the figure above and the HTML it is rendered from
```

## Sources and licenses

The skill itself (SKILL.md, the scripts and the reference files written for it) is released under the MIT License; see `LICENSE`.

The exemplar passages are short excerpts from 30 papers under CC BY 4.0 or CC0 1.0, listed with their licenses in `references/exemplars/SOURCES.md`. The sentence bank quotes single sentences from award papers, and its Sources section lists each paper and its license. Copyright in all quoted text remains with its authors. Citations and cross-references in the excerpts are replaced by `[cite]` and `REF`, and the skill instructs the model never to reuse their content or any run of six or more words. The frames and connectives files contain phrases and counts only.

The idea of writing a paper around what it achieves rather than around every possible objection comes from [anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill) (MIT). [humanizer](https://github.com/blader/humanizer) removes the patterns in Wikipedia's "Signs of AI writing" from any kind of text; this skill covers ML papers only and works from the papers themselves.
