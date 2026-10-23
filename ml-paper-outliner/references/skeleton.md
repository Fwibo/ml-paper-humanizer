# The skeleton

The skeleton is the one contract between `ml-paper-outliner`, which writes it, and `ml-paper-humanizer`, which writes prose from it in `write` mode and checks a revision against it in `rewrite` mode. It is plain Markdown, with the paper's own names, numbers and citations written as the author writes them. It holds content and the relations between pieces of content; it holds no sentence meant to go into the paper. One file per paper: the header once, then a block per section, added as sections are outlined.

A section's block is a writing brief: what the section is for, how it runs and why in that order, then one numbered note per paragraph, written to the writer in the imperative ("open on…", "point to Table 2…", "do not explain…", "end on…"). The notes are the unit the humanizer writes from and checks against, so each is numbered and each is the content of exactly one paragraph of the paper.

## Format

```markdown
# Skeleton: <paper>

Contribution: <one sentence the reader can repeat>
Layers: conceptual — <…>; technical — <…>; empirical — <…>   (each: present | not stated in the material | not applicable)
Orientation: proof | effect | design | evaluation | discovery  (a secondary one after a comma when the paper has two kinds of contribution)
Nearest work: <three to five works and the coordinate on which this paper differs>  (optional)
Main doubt: <the reviewer's likeliest objection, and the paragraph that answers it>  (optional)
Figure 1 / Table 1: <what Figure 1 shows; whether Table 1 positions or reports>  (optional)
Names: <the ledger names the skeleton uses, or "ledger.json">

## <Section>
Carries: <the part of the contribution sentence this section proves or clarifies>
Frame: <the paragraphs in order, from the frame in the section's file (references/sections/); where the order departs from it, the reason the argument gives; what the material has no evidence for and the section therefore leaves out>
Figures: <each figure and table the section points to, with the one comparison the reader is to see in it>  (optional)

### P1 <role in the frame>
<A few sentences to the writer. What the paragraph opens on and the question it answers. What it claims, with the reporting verb and the scope in parentheses. What evidence it points to, with the status: provided | referenced, not provided | planned | not identified in the supplied material. What it does not say. What it ends on, which is what P2 opens on.>
Keep: <numbers, conditions, wording the writer carries verbatim>  (optional)

### P2 <role>
…
```

### What a paragraph note covers

A note is prose, but it is not free: the humanizer reads five things out of it and the outliner's check looks for each. A note missing one of them is a finding, not a style.

1. **The question.** What the paragraph answers for the argument, not its topic ("whether the gain survives at matched compute", not "efficiency"). A paragraph that only prepares the reader answers what the reader needs before what follows can be read. Usually the note's first sentence: "Open on…", "Answer…", "Tell the reader…".
2. **The claim, at its strength.** What the paragraph asserts, with the reporting verb and the scope in parentheses after it: "(shows; these four baselines and three benchmarks)", "(existence, one case)", "(is consistent with; redundancy itself was never measured)". A paragraph that asserts nothing carries no verb, and its parenthesis says what it does instead ("states the setup", "describes the design"). Otherwise the verb and scope are set by the evidence ([claim-strength.md](../../references/claim-strength.md)) and are part of the contract: the humanizer writes the claim at that strength and `rewrite` checks that it has not moved. In `reverse` mode the current skeleton records the draft's verb and scope as written and the proposed skeleton writes the ones the evidence supports.
3. **The evidence and its status.** A pointer the humanizer can name in the text: a table or figure, a derivation, a citation key as the author writes it (`[cite:smith2024]`, `\cite{smith2024}`), or the author's note. *provided*: the material gives the content, the numbers or the statement, whether or not the table or figure itself is attached ("provided, the storyline's Table 2 numbers"). *referenced, not provided*: the author points to it and the content is not in the material (a figure described but not shown, a row named without its number); usual when a single section is outlined, and not a defect. *planned*: the author intends to produce it; the humanizer writes a planned experiment as planned, never as a finding. *not identified in the supplied material*: the claim needs evidence and the material names none; this status goes to the open questions. A pointer without a status reads as provided.
4. **What it does not say.** The fact the material does not give, the explanation the author has not earned, the result that belongs to a later paragraph. Written as "Do not…", because the writer's instinct is to fill these.
5. **The ending.** The fact or the open question the paragraph ends on, which the next note opens on. It is a relation between two notes, not a sentence to write: the paragraph ends on its fact and the next paragraph's opening does the picking up. The last note of a section ends on what the next section takes up, named as that section ("which the Experiments test"), whether or not that section is outlined in the same skeleton. An ending that is a derived takeaway ("so the bottleneck is X") which the next paragraph restates is the template; the note ends on the fact or the open question and lets the next paragraph draw the conclusion.

Two further rules on the notes.

- **No paper sentence.** The note tells the writer what the paragraph carries; it does not write the paragraph. The imperative mood and the parenthesised verb keep it on the right side: "Open on Table 2 and the claim together: CoRe raises F1 over the four baselines tested (shows; …)" is a note; "Table 2 shows that CoRe consistently outperforms all four baselines" is a sentence for the paper and does not belong here. A note that reads as a paragraph of the paper is rewritten, because a humanizer given paper sentences paraphrases them instead of writing from the exemplars.
- **One note, one paragraph.** A note that carries two paragraphs' worth of content is split; a paragraph the frame expects and the material has nothing for is a note of one line saying what is missing, with a `[?]`, not a paragraph invented to fill the slot. A note states what the paragraph must carry, not a ceiling on it: the humanizer writes the paragraph at the length the exemplars say this content takes, and a Frame line may carry the author's length target for the section.

A note carries only a `[?]` where something is open; the question itself goes to the open questions with the note's number (`Experiments P3`), so that a note stays readable.

### Header and section lines

- **Header lines** are the decisions the writing guides ask for before an outline. `Nearest work` and `Main doubt` are optional in form and rarely skipped in practice: the first fixes what the related work and Table 1 compare against, the second names the paragraph the experiments cannot do without. None of them holds up a section: a line the material does not settle says "provisional" and the work goes on. A header written from a single section's material is marked `(provisional)` after the title until the paper settles it. The layers and the orientation are a lens, not a bar: a layer marked "not applicable" is a finding about the paper, not a defect in it. The Contribution line carries no `[?]`; a contribution that is still open is written as the candidates it is open between, in the open questions.
- **Carries** ties the section to the contribution sentence. The humanizer reads it to know what the section is for; the outliner's check reads it to find a section that carries nothing or a part of the contribution that no section carries. A conclusion's Carries line names the contribution as a whole, restated at the strength the sections before it reached; it proves no part of it and adds none, and that is not a finding.
- **Frame** is the section's running order and its reasons: the paragraphs in sequence, a reason for every departure from the section file's frame ("cost comes right after the main result because the main result raises it"), and what the section leaves out because the material has nothing for it. The humanizer follows the order; `rewrite` accepts a different order only with a reason here.
- **Figures** is the section's plan for its figures and tables: which ones it points to and, for each, the one comparison the body reads it by. The humanizer names them in the text and does not read a table cell by cell. Figure and table numbers are pointers, not names, and do not go in the Names line.
- **Keep** lists what the humanizer must carry verbatim: a margin, a seed count, a phrase the author wants. It stays a separate line under the note, because the revision checker reads it by that label.

## What the humanizer checks against it

In `write` mode the skeleton is the outline: every note becomes one paragraph, in the Frame's order, with its claim at the note's verb and scope and its evidence named; the section's `Carries` line is what the section is for, and its `Figures` line is how its figures are read. Evidence marked *referenced, not provided* is named as the author names it; evidence marked *planned* is written as planned; a note whose evidence is *not identified* or that carries a `[?]` is left as a marked gap in the text, not written around. In `rewrite` mode the fidelity read checks the revised text against the skeleton note by note: every note still has its paragraph, no claim has been added, no claim's verb or scope has moved up or down, each paragraph still ends on what its note says and the next still picks it up, and a different order has the Frame line's reason behind it. A note the revision dropped or merged is reported, not silently restored. The reverse is also true: a paragraph of the author's text that the current skeleton marks "[no question found]", or that the proposed skeleton maps to the appendix or to a cut, stays in the text, flagged, until the author decides; the humanizer removes nothing on the skeleton's say-so. A `reverse` run hands the humanizer the proposed skeleton with its paragraph mapping in each note's heading, so that a merge (`P3 ablation (P4 + P5 → P3)`) is a rewrite of two paragraphs into one and a move (`P2 (P3 → P2)`) is a reorder, each with its reason in the change list. Without a skeleton the humanizer works from the author's outline or notes as before; nothing here is required of a user who only writes.

## Worked example

The results section "RLVR for Mathematical Reasoning" of [arXiv 2504.13837](https://arxiv.org/abs/2504.13837) (NeurIPS 2025 runner-up, CC BY 4.0), a discovery paper. The published passage is in [examples/results-2504.13837.md](../../examples/results-2504.13837.md); this is the skeleton its paragraphs answer to, written as the outliner would write it from the authors' notes. The header is written from the paper as a whole; the `Nearest work` and `Main doubt` lines are as the paper's introduction and its validity check imply them.

```markdown
# Skeleton: Does RL Really Incentivize Reasoning Beyond the Base Model?

Contribution: RLVR makes a model more likely to sample a correct answer but does not give it reasoning ability beyond its base model; at large k the base model covers more solvable problems.
Layers: conceptual — the reasoning ability boundary of a model is what pass@k at large k measures, not pass@1 (present); technical — pass@k curves of base and zero-RL models over k, with CoT validity checked by hand (present); empirical — base models overtake RL models on every benchmark and size tested (present).
Orientation: discovery
Nearest work: zero-RL training recipes (SimpleRLZoo, Oat-Zero, DAPO) evaluated at pass@1; this paper evaluates the same checkpoints at large k against their own base models.
Main doubt: a correct final answer at large k may come from a lucky guess rather than reasoning; answered by the validity check (Results P5).
Figure 1 / Table 1: Figure 1 is the pass@k crossover on one benchmark; no positioning table.
Names: pass@k, reasoning ability boundary, coverage, zero-RL, RLVR, base model, CoT, hacking, lucky guesses

## Results
Carries: the empirical layer: base models overtake RL models at large k on every benchmark and size tested, and the overtaking is by valid reasoning.
Frame: setup; the main result, which tests the main claim; the same result on RL models picked for strength; two cases; the systematic check behind the cases; the frame's closing reading is drawn in P3 and not repeated. Two case paragraphs before the check because the check answers the doubt the cases raise.
Figures: pass@k curves, base against RL-trained at each size and benchmark, read by the crossover; the Oat-Zero and DAPO curves, read by the same crossover from a 30% head start; two CoT figures, read as cases.

### P1 setup
Tell the reader what is compared, on what, and how a sample counts as correct, before any curve: base and zero-RL models from two families, by pass@k on six math benchmarks of rising difficulty, with the final answer checked. Name the SimpleRLZoo checkpoints [cite] and what they were trained with (GRPO, GSM8K and MATH training set, correctness reward only), and say why Oat-Zero-7B and DAPO-32B [cite] are added: their AIME24 strength (provided; author's setup). End on pass@k over k as the quantity the next paragraph reads.
Keep: Qwen2.5 7B/14B/32B; LLaMA-3.1-8B; GSM8K, MATH500, Minerva, Olympiad, AIME24, AMC23

### P2 main result
Answer whether RL training enlarges or shrinks the set of problems a model can solve. Open on the curves and the crossover together: at small k the RL model leads, as k grows the base model catches up and surpasses it on every benchmark (observe, indicates; systematic across all sizes and benchmarks tested; provided, the pass@k figure). Read one point as the example: Minerva, 32B, about 9% at k = 128. State the two sides of the reading as the paper does, the RL model more likely to sample a correct response, the base model covering more solvable problems. End on the crossover and on whether it holds for RL models chosen for their strength.
Keep: k = 1 equals average-case accuracy; the 9% at k = 128 reading

### P3 robustness of the result
Answer whether the crossover survives for RL models with strong AIME24 results. Oat-Zero and DAPO start nearly 30% above their base models and are still surpassed at large k (shows; provided, the Oat-Zero-7B and DAPO-32B curves). Draw the section's conclusion here and nowhere else: RLVR raises the likelihood of correct samples at low k and narrows coverage (we conclude). End on two things left open: the root cause, which a later section analyses, and whether the base model's rare successes are genuine.

### P4 case evidence
Show what the base model's correct CoTs on hard problems look like: long and reflective, so the base model has the reasoning ability (highlighting; existence, two cases; provided, the two CoT figures). Say how the cases were chosen, by hand from 2048 samples on the hardest AIME24 questions; write them as cases, not as how often this happens. End on the limit of cases: a few of them do not rule out lucky guesses.

### P5 validity check
Answer whether the base model's solved problems are reached by valid CoTs or by lucky guesses, systematically. On the hardest solvable GSM8K and AIME24 problems almost every solved problem has at least one correct CoT, for base and RL models alike (suggests that the base model samples valid reasoning paths; provided, manual inspection following [cite]). Give the counts and the threshold, and note the one ambiguous case. Do not draw a stronger verb: the inspection was by hand on a small set. End on the main result standing as a result about reasoning, not answer hacking; nothing new after it.
Keep: GSM8K: base 24 of 25, RL 23 of 25; AIME24: base 5 of 6 (one ambiguous), RL 4 of 6; threshold accuracy below 5% and above 0%
```

Read against the published passage, the skeleton shows what the humanizer could not have recovered from the sentences alone: that P4 and P5 exist to answer the doubt the header names and P3 ends on, that the conclusion of the section is drawn in P3 and not repeated in P5, that P4 is an existence claim on two cases and P5 the systematic check behind it, and that P5's verb is "suggests" because the inspection was by hand on a small set.
