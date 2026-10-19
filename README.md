# ml-paper-humanizer

**An agent skill for writing and revising ML conference papers across Claude Code, Codex, and other AI coding assistants—removing LLM tells so your paper reads like a human wrote it.**

[中文](README.zh-CN.md) · [Full example](examples/results-2504.13837.md)

---

## Highlights

Out-of-the-box LLMs struggle with academic writing, often defaulting to inflated claims, mechanical transitions, and unnatural phrasing. Rather than relying on a brittle list of banned words, `ml-paper-humanizer` governs the writing process through corpus-backed phrasing, structural rhetoric, and strict terminology guardrails.

### 1. Corpus-Backed Phrasing from 307 Award & Oral Papers
We analyzed the full text of all 307 award-winning and Oral papers published between 2023 and 2026 across 12 premier venues (**NeurIPS, ICML, ICLR, ACL, EMNLP, NAACL, COLM, CVPR, ICCV, ECCV, AAAI, and KDD**). From this corpus, we extracted 1,234 recurring rhetorical patterns—each appearing in at least six distinct papers—categorized by communicative function (e.g., referencing figures, reporting empirical results, scoping claims, and contrasting baselines).
* **Empirical Grounding:** A comparative analysis of 60 original human paragraphs against 318 LLM-generated drafts revealed that the "LLM accent" stems largely from missing these exact functional idioms.
* **Outcome:** The resulting prose relies on standard phrases that reviewers have read hundreds of times, eliminating expressions invented by language models.

### 2. Structural Principles from Definitive Writing Guides
Clear academic prose is defined by how information is structured, not just word choice. We distilled the mechanics most frequently mishandled by LLMs from seven authoritative texts, including Gopen & Swan's *The Science of Scientific Writing*, Williams' *Style*, Swales & Feak's *Academic Writing for Graduate Students*, and Strunk's *The Elements of Style*.
* **Syntactic Mechanics:** Places new information at sentence endings; keeps subjects adjacent to verbs; expresses actions through verbs rather than nominalizations; signals contrast early; omits conjunctions when word order suffices; enforces parallel form.
* **Calibrated Claims:** Grades reporting verbs so that claim strength strictly matches empirical evidence, and confines concessions to a single clause.
* **Outcome:** These are mechanics readers rarely notice consciously, yet immediately feel in the flow of a paper. The skill enforces them during generation and verifies them on read-back.

### 3. Subfield Terminology Alignment & Hard Guardrails
Generic "humanizer" tools degrade technical manuscripts by swapping established domain terms for synonyms—turning a specific model name into *"the system"* or *"our approach,"* which reviewers spot immediately.
* **Verified Glossary:** Extracts established subfield terminology directly from your draft and cited literature, verifies terms verbatim, and enforces a strict *one-concept-one-term* policy.
* **Immutable Redlines:** Numerical results, model and dataset names, citations, and defined terms are **never modified** (questionable metrics are only flagged for author review). Language is refined without compromising technical accuracy.

---

## Before and After

Below are two paragraphs from the results section of a NeurIPS 2025 runner-up paper ([arXiv 2504.13837](https://arxiv.org/abs/2504.13837), CC BY 4.0). The same model drafted them twice from the same content outline, without access to the published text.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="examples/compare-dark.png">
  <img alt="Two paragraphs of a results section written without the skill and with it, side by side; the left marks the writer's images and coined headings, the right marks the field's phrases and the paper's own terms" src="examples/compare.png">
</picture>

* **Without the skill (left):** The model coins its own headings, interprets the figure through an invented metaphor (*"the crossover persists"*), preemptively answers an objection before the experiment is even described, and replaces named concepts with generic descriptions.
* **With the skill (right):** Each paragraph states its purpose before introducing numbers, points to the figure using standard domain phrasing, preserves the paper's exact terms (*reasoning ability boundary*, *hacking or lucky guesses*), and introduces inferences with calibrated reporting verbs.
* **Full comparison:** Both complete drafts alongside the published passage are available in [examples/results-2504.13837.md](examples/results-2504.13837.md).

At the sentence level, the skill relies on 40 diagnostic pairs like those below—contrasting a model draft against published prose for the exact same rhetorical task:

| Writing Task                       | Model Draft                                                  | Published Text                                               |
| ---------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Say why a comparison is unfair     | That yardstick, however, measures a different goal.          | This would not be a fair comparison, because LMNet is a general method to improve the intelligence of a given LLM, with additional training cost only less than 1% of the pre-training. ([2505.12741](https://arxiv.org/abs/2505.12741)) |
| Give the question, then the number | Notably, SFT on the same data lowers mean accuracy by 5.7% relative to Prompt. | Second, one may argue that the improvement mainly relies on training data. SFT (implemented by very moderate training configurations) can hardly bring improvement over the pre-trained LLM (-5.7%). ([2505.12741](https://arxiv.org/abs/2505.12741)) |
| Mark the surprise                  | Actual LLMs, shown as gray points in the same panel, follow a similar exponent near 1. | Remarkably, we find that actual LLMs follow a similar scaling. ([2505.10465](https://arxiv.org/abs/2505.10465)) |

---

## How the Skill Works

### 1. Eliminating Five Writing Actions—Not a Banned-Word List
The "AI smell" in academic writing reduces to five habits models fall into:
* **Performing:** Presenting a standard finding as a profound insight.
* **Defending:** Writing the reviewer rebuttal preemptively into the main text.
* **Piling:** Cramming numbers, subordinate clauses, and citations into a single sentence.
* **Restating:** Making the section heading, opening sentence, closing sentence, and figure caption repeat the exact same point.
* **Drifting:** Referring to a single entity by multiple names, or leaving internal shorthand in the manuscript.

Remove the action, and natural wording follows. **The skill has no banned-word list:** word lists and sentence quotas were tested, produced drafts that read like rigid templates, and were removed.

### 2. Two Modes
* **`rewrite` (default):** Sentences that read cleanly in a single pass are kept untouched. Outputs the revised text alongside a structured change log (*before, after, reason*).
* **`write`:** Drafts new prose from an outline, rough notes, or a Chinese draft. The manuscript text remains in English, with a clause-by-clause Chinese translation available on request. Prompts in Chinese receive responses in Chinese.

### 3. The Seven-Step Pipeline
`SKILL.md` executes the following sequence on every request:
1. **Determine Orientation:** Identify the paper's archetype (*proof / effect / design / evaluation / discovery*) and load the corresponding section frame from the playbook.
2. **Build the Term Ledger:** Extract and verify domain terminology from your manuscript and cited papers.
3. **Load Exemplars:** Review the sentence bank for the rhetorical moves about to be written (plus three full exemplar passages in `write` mode).
4. **Draft or Revise:** Write the prose, establishing the logical relationship between each sentence and the one preceding it as it is written.
5. **Three-Pass Read-Back:** Audit the draft three times—first for factual fidelity, second against the term ledger, and third against the syntactic rules from the style guides.
6. **Frames Pass:** Always run in `write` mode, and on request in `rewrite` mode. Checks the draft sentence by sentence against the frames database, replacing phrasing that points to figures, reports observations, interprets trends, compares baselines, or transitions between topics with established domain idioms.
7. **Automated Checker:** Runs a document-relative check that flags abnormal repetition—such as a single concept appearing under two names, a paragraph restating its own heading, or a reported gain that never names both sides of the comparison.

### 4. Scope and Limitations (What It Does Not Do)
* **Not an AI-detector bypass:** It has not been tested against AI detectors and makes no claims about detection scores; it addresses what a human reviewer notices on the page.
* **Non-intrusive:** It does not verify citation accuracy, enforce venue-specific LaTeX formatting, or mimic personal style from your past papers. The corpus covers ML, NLP, and CV.
* **Known gaps:** Drafts produced with the skill remain slightly shorter than published text and use a narrower range of domain-specific verbs (see the example file for a direct comparison).

### 5. How It Was Tested
Every rule was validated the same way: a model drafted a section of an award-winning paper from its outline, the output was read side-by-side against the published original, and any rule that failed to improve that reading was discarded.

---

## Install and Use

### Installation

**Claude Code:**
```bash
git clone https://github.com/Fwibo/ml-paper-humanizer ~/.claude/skills/ml-paper-humanizer
```

**Codex CLI:**
```bash
git clone https://github.com/Fwibo/ml-paper-humanizer ~/.codex/skills/ml-paper-humanizer
```

* **Other Coding Agents:** Any agent that supports the Agent Skills format (a directory containing `SKILL.md`) can load the cloned folder directly.
* **claude.ai (Web):** Zip the repository folder and upload it under `Settings → Capabilities → Skills`.

### Dependencies

The structural checker and exemplar picker require only **Python 3**. Candidate extraction for the term ledger uses `spaCy`, and parsing cited PDFs requires `PyMuPDF` (if omitted, terms are proposed by the model and verified verbatim by the script):

```bash
pip install spacy pymupdf && python -m spacy download en_core_web_sm
```

### Usage Examples

Prompt the agent in plain English or Chinese. The skill triggers automatically when drafting, revising, or diagnosing a paper:

* `"Rewrite the second paragraph of my results section, it reads like AI."`
* `"Write the introduction from these notes. It is a discovery paper."`
* `"Make this abstract less defensive."`
* `"Don't change anything yet, tell me what is wrong with this section."`
* `"/ml-paper-humanizer sec/experiments.tex"`

The helper scripts can also be run standalone from the command line:

```bash
# Run document-relative repetition and structural checks
python scripts/check_tex.py paper/ --ledger ledger.json

# Extract and verify terminology from LaTeX source and cited PDFs
python scripts/term_ledger.py paper/main.tex --cited refs/*.pdf --out ledger.json

# Retrieve three exemplar passages for a specific section and paper orientation
python scripts/pick_exemplars.py results --orientation discovery
```

---

## Repository Structure

```text
SKILL.md                      Core workflow: the seven steps, reader needs, read-back checklist, and output contract
references/
  section-playbook.md         Section-by-section rhetorical goals (abstract to rebuttal) by paper orientation
  sentence-bank.md            40 pairs of model drafts vs. published text by failure mode, plus 23 sentences by move
  register-frames.md          1,234 corpus phrases categorized by communicative function, with paper counts
  connectives.md              Style guide mechanics alongside standard cause, contrast, and concession forms
  claim-strength.md           The reporting-verb ladder, separating design intent from empirical outcome
  exemplars/                  144 introduction and results passages from 30 papers, with SOURCES.md
scripts/
  check_tex.py                Document-relative repetition and structure checks (threshold-free)
  term_ledger.py              Extracts term candidates from manuscript and cited PDFs; --verify keeps verbatim matches
  pick_exemplars.py           Selects three exemplar passages matching a given section type and orientation
examples/
  results-2504.13837.md       Full results section comparison: without the skill, with the skill, and published text
  compare.html, compare*.png  The side-by-side comparison figure above and the HTML source used to render it
```

---

## Sources and Licenses

* **Code & Rules License:** The skill itself (`SKILL.md`, scripts, and custom reference files) is released under the **MIT License**; see `LICENSE`.
* **Corpus & Exemplar Copyright:** The exemplar passages are brief excerpts from 30 papers licensed under **CC BY 4.0** or **CC0 1.0**, documented in `references/exemplars/SOURCES.md`. The sentence bank quotes single sentences from award papers, with full attribution and licensing listed in its Sources section. Copyright for all quoted material remains with the original authors. Citations and cross-references in the excerpts are sanitized to `[cite]` and `REF`, and the skill strictly instructs the model never to reuse their factual content or any contiguous sequence of six or more words. The frames and connectives files contain structural phrases and frequency counts only.
* **Acknowledgments:** The principle of structuring a paper around what it achieves rather than preemptively defending against every possible objection is inspired by [anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill) (MIT). While [humanizer](https://github.com/blader/humanizer) strips general-purpose AI patterns based on Wikipedia's *"Signs of AI writing,"* `ml-paper-humanizer` is built exclusively for **ML manuscripts** and derives its rules directly from the published literature.
