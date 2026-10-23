# Related work

One of the section files of [section-playbook.md](../section-playbook.md); read that index first for the orientation tags and the opening logic, then this file for the section being written. Sources are in [sources.md](sources.md).

## What this section does

A map of the field drawn for this paper: the lines of work that bear on its problem, what each got right and what it missed, and where this paper sits among them [Black] [刘知远]. After it the reader can say the key idea of each significant work, how the works group and how this paper differs from each group [Black] [Ernst].

The reviewer checks:
- that no important reference is missing and the main idea has not been done before [Freeman];
- whether a specific prior work already demonstrates the key contributions [Black];
- that each cited work, often the reviewer's own, is described fairly [Black] [Lipton] [刘知远];
- that the novelty claim is exact, not inflated [Nanda];
- a map rather than a list, groups along the dimensions that matter here, a closing missing coordinate, and agreement with Table 1 [Checklist].

## Frame

1. **Before the first sentence.** List the three to five closest works and the exact coordinate on which this paper differs from each [Checklist]. The dimensions of the map are the dimensions the introduction named (bottlenecks, trade-off axes, benchmark properties, explanation criteria, assumptions and guarantees, by orientation), which are also the columns of Table 1 when the paper has one [Checklist].

2. **One paragraph per line of work.** Each paragraph takes one group of works that share an idea along one of those dimensions. It says what they have in common, follows the line back in time, says what it got right and what it missed for this paper's problem, and ends on what this paper adds to it [Black] [刘知远]. The paragraphs follow technical routes or, when the history is the point, the order of development [刘知远]; the line nearest this paper usually comes last, next to the closing paragraph [practice default].

3. **The missing coordinate.** The last paragraph locates the gap (rule below). It reports no results and does not praise the method [Checklist] [刘知远].

When main-text pages are tight, the main text keeps one paragraph and the full section moves to the appendix (the length rule). The section's position follows the position rule; the frame inside it stays.

## Rules

### What the section is made of

- **Group by topic, along the dimensions that matter here.** The groups are this paper's dimensions, not the field's generic subareas. Wrong topic: "Large language models." Right topic: "Checking an answer after it is generated." [Black] [Checklist] [刘知远]
- **Analyse, do not report.** Each paragraph says what the prior art on its topic got right and what it missed, and compares the works with this paper and with each other, narrating and commenting together (夹叙夹议) with the challenge this paper addresses in view. Wrong: "A [3] proposes X. B [4] proposes Y. C [5] proposes Z." Right: "Retrieval-based checkers [3, 4] verify each claim against a corpus, which makes them precise where the corpus has coverage and silent elsewhere [5]." [Black] [刘知远] [Ernst]
- **End each paragraph on what this paper adds to that line.** The last sentence names the coordinate in the paragraph's own terms, not with the stock "Unlike these works, we propose…", which names none. Right: "None of these checkers conditions on the model's own uncertainty, the signal Section 3 builds on." [Checklist] [刘知远] [practice default for the stock phrase]
- **Close on the missing coordinate.** The final paragraph locates the precise gap the paper fills, as the combination no line occupies and in the terms of Table 1, and lands on the new idea and the challenge it takes up there. [Checklist] [刘知远]
- **Agree with Table 1.** When the paper has a positioning table, its columns are the bottlenecks from the introduction, its rows are method families or close representative works, its comparison is fair to prior work, and its last row fills a meaningful missing combination instead of collecting checkmarks. The section's groups carry the same names as the rows. [Checklist]
- **Say exactly what is and is not new.** Cite the most relevant papers and say why this work is and is not different from each. If it is not very different, say so: name parallel work as parallel, and state a flaw fixed in prior work politely. Wrong: "We are the first to study calibration under paraphrase." Right: "Calibration under paraphrase has been measured for classifiers [7]; this paper measures it for free-form generation, where a paraphrase can change the answer itself." [Nanda] [Freeman]
- **Say which problems are open and which are solved.** [Lipton & Steinhardt]

### Fairness and credit

- **Describe prior work so that its authors would agree.** Each assessment is precise and objective. State what was good about a work and how this paper goes further. A criticism concerns the flaw and why it matters for this problem, never the authors or their motives. Where possible, ask the authors of the closest work whether the description is fair. Wrong: "X [2] fails badly on long inputs." Right: "X [2] is accurate up to 512 tokens; its memory grows quadratically beyond that, which rules it out for the documents studied here." [刘知远] [Black] [Freeman] [Nanda] [Peyton Jones]
- **Follow the chain back in time.** Trace the idea as far back as it goes; a claim to be first may not rest on citations from the last few years. Have someone who knows the area check the coverage before submission. [Black] [Freeman] [刘知远]
- **Cite generously, and throughout the paper.** Cite every relevant work and no irrelevant one, and do not cover every vaguely related paper for show. Cite a prior method where the paper uses it, not only in this section. [Lipton] [Karpathy] [Nanda]

### Citations

- **Every factual statement has a citation, and the cited work supports it.** Check before writing that the work says what the sentence attributes to it. Attribute a claim to its authors ("Smith et al. argue that…"), not to nobody ("X is claimed to…"). Do not cite as fact what the source offered as speculation. [Lipton] [Lipton & Steinhardt]
- **Accuracy, not count.** Cite work that shares the mechanism, not an analogy whose mechanism differs. Work with the same mechanism in a different setting, or similar techniques on a different problem, is discussed and cited with cf. Do not use an as or since clause to import a cause from the literature. Wrong: "As [9] shows, attention heads specialize, so the gate learns to…" Right: "Attention heads specialize by syntactic role in encoder models [9]; Section 5 tests whether the decoder studied here does the same." [Lipton & Steinhardt] [Freeman] [practice default for cf.]
- **At most three papers in one parenthesis.** A longer parenthesis means the sentence is too general: split it until each citation has its own claim. Keep the section's citation density neither sparse nor crowded. [Karpathy] [practice default]
- **Present tense, with the work or its authors as the subject.** "Smith et al. [4] propose", not "proposed". A bracket is not a subject: write "Smith et al. [4] show", or a sentence about the idea with the citation at its end, not "[4] shows". [Black]
- **The field's terms in their established sense.** A term that prior work uses with a precise meaning keeps that meaning; if this paper uses it differently, say so once. [Lipton & Steinhardt]
- **The definitive version, and credit for assets.** Cite the published version of a paper rather than its preprint, and cite the creators of reused code, data and models, with the version used. [Black] [NeurIPS]

### Place and length

- **Where it goes follows the work.** After the introduction when the paper is a close refinement of prior work and the reader needs the relation before the method, or when the motivation depends on the literature (plugging a gap, correcting a mistake). Before the conclusion when the paper is a framework built largely from existing methods, or when an early section would make independent work look derivative or stand between the reader and the idea. When none of these decides, it goes second, after the introduction. [刘知远] [Nanda] [Karpathy] [Ernst] [Peyton Jones] [practice default for the tie-break]
- **Length, and the appendix when pages are tight.** About half a page to a page in an eight-page paper. When main-text pages are tight, keep one main-text paragraph with inline bold topic names and move the full version to the appendix. [刘知远] [Karpathy] [Nanda] [practice default for the bold topic names]

## By orientation

`proof` Group prior theory by its assumptions and its guarantees, the columns of a proof paper's Table 1, and say for each line which assumption it needs and what it guarantees under it. Compare the main theorem with the closest known results, here or next to the statement in the method, on points the reader can check: which assumption is weaker, which rate is better, which case is newly covered [Checklist] [NeurIPS]. Do not invoke a broad theorem whose formal content does not bear on the claim [Lipton & Steinhardt].

`effect` Group prior methods by where they sit on the trade-off that matters (accuracy against compute, labels or shift) and by what each pays for its position [Checklist]. Report a prior gain with the budget and setting under which it was measured [Lipton & Steinhardt]; the matched-budget comparison itself belongs to Table 1 and the experiments [Checklist]. The closing paragraph names the part of the trade-off no method reaches.

`design` Group prior methods by the bottleneck the paper names and by the design principle each follows, with Table 1's capabilities as the dimensions: dynamic behavior, end-to-end optimization, use of heterogeneous information, interpretability, supervision needs [Checklist]. The missing coordinate is a combination of capabilities that follows from the bottleneck.

`evaluation` Group prior benchmarks and protocols by the properties Table 1 compares: distribution shift, cold-start setting, long-tail coverage, leakage control, metric realism and reproducibility. For each, say which realistic factor it leaves out and what false conclusion it can lead to, so that the new benchmark answers that mismatch and is not merely a harder test [Checklist].

`discovery` Group the existing explanations of the phenomenon by whether they locate its source, explain the mechanism, predict outcomes and support intervention, the columns of a discovery paper's Table 1, and say why each one falls short [Checklist]. Keep apart the explanations that were tested and those that were proposed and then repeated as fact [Lipton & Steinhardt].

## Common mistakes

- **The closest work met only here, late in the paper.** Fix: name the three to five closest works in the introduction with how this paper differs; this section expands that account. [Nanda]

## Before moving on

- Could a reader state the key idea of each significant work, how the works group and how this paper differs from each group? [Black] [Ernst]
- Are the groups the bottlenecks the introduction names, under the same names as Table 1's rows, with a comparison fair to prior work? [Checklist]
- Does each paragraph say what its line got right and what it missed, and end on a named coordinate? [Black] [刘知远]
- Does the final paragraph name the missing coordinate in Table 1's terms, without results or praise? [Checklist]
- Is it clear what is and is not new, parallel work included, and does every "first" rest on the history traced back? [Nanda] [Black]
- Would the authors of each cited work accept its description? [刘知远] [Black]
- Has someone who knows the area checked that no major work is missing? [Black] [Freeman]
- Does the section use the same contribution vocabulary as the introduction and the method? [Checklist]

## Sources for this section

- [Checklist] lars-contribution-centered-checklist.txt
- [Black] black-writing-a-good-scientific-paper.txt
- [Freeman] freeman-how-to-write-a-good-cvpr-submission.txt
- [刘知远] liuzhiyuan-nlp-paper-zhihu-summary.txt
- [Nanda] nanda-highly-opinionated-advice.txt
- [Karpathy] karpathy-phd-survival-guide.txt
- [Lipton] lipton-heuristics-for-scientific-writing.txt
- [Lipton & Steinhardt] lipton-steinhardt-troubling-trends.txt
- [NeurIPS] neurips-paper-checklist.txt
- [Ernst] general/ernst-how-to-write-a-technical-paper.txt (secondary)
- [Peyton Jones] general/peyton-jones-how-to-write-a-great-research-paper.txt (secondary)
