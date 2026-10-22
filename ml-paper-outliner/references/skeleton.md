# The skeleton

The skeleton is the one contract between `ml-paper-outliner`, which writes it, and `ml-paper-humanizer`, which writes prose from it in `write` mode and checks a revision against it in `rewrite` mode. It is plain Markdown, with the paper's own names, numbers and citations written as the author writes them. It holds content and the relations between pieces of content; it holds no sentence meant to go into the paper.

## Format

```markdown
# Skeleton: <paper or section>

Contribution: <one sentence the reader can repeat>
Layers: conceptual — <…>; technical — <…>; empirical — <…>
Orientation: proof | effect | design | evaluation | discovery
Names: <the ledger names the skeleton uses, or "ledger.json">

## <Section>
Frame: <the section's frame from the playbook, or the different order and the reason the argument gives for it>

### P1 <role in the frame>
Q: <the question this paragraph answers for the argument>
Claim: <what it asserts, at the strength the evidence allows; the reporting verb is part of the claim>
Evidence: <table, figure, derivation, citation or the author's note it rests on; "none" when the material gives none>
Hands off: <what the next paragraph picks up: a fact or an open question>
Keep: <numbers, conditions, wording the author fixed>  (optional)

### P2 …
```

Each field is one line or two. A paragraph that needs more than that is carrying more than one paragraph's work, and the skeleton splits it. A line is what the paragraph must carry, not a ceiling on it: the humanizer writes the paragraph at the length the exemplars say this content takes, and a Frame line may carry the author's length target for the section.

- **Q** names the question in the argument, not the topic ("whether the gain survives at matched compute", not "efficiency"). A setup paragraph's question is what the reader needs to know before the result can be read.
- **Claim** carries its condition and its verb. "Base models reach higher pass@k than their RL-trained versions at large k (shows; Figure 2, all benchmarks, all sizes)" is a claim; "pass@k results" is a topic.
- **Evidence** is a pointer the humanizer can name in the text. "none" is not an error in the skeleton; it is an open question for the author.
- **Hands off** is what the next line's Q picks up. A hands-off that is a derived takeaway ("so the bottleneck is X") which the next paragraph then restates is the template; the skeleton hands off the fact or the open question and lets the next paragraph draw the conclusion. It is a relation between two lines, not a sentence to write: the paragraph ends on its fact, and the next paragraph's opening does the picking up.
- **Keep** lists what the humanizer must carry verbatim: a margin, a seed count, a phrase the author wants.

## What the humanizer checks against it

In `write` mode the skeleton is the outline: every paragraph line becomes a paragraph, in the skeleton's order, with its claim at the skeleton's strength and its evidence named. In `rewrite` mode the fidelity read checks the revised text against the skeleton: every line is still there, no claim has been added, no claim's verb has moved up or down the ladder, each hands-off still reaches the next paragraph, and a different order has the Frame line's reason behind it. A line the revision dropped or merged is reported, not silently restored. The reverse is also true: a paragraph of the author's text that the skeleton marks "[no question found]" stays in the text, flagged, until the author cuts it; the humanizer removes nothing on the skeleton's say-so.

## Worked example

The results section "RLVR for Mathematical Reasoning" of [arXiv 2504.13837](https://arxiv.org/abs/2504.13837) (NeurIPS 2025 runner-up, CC BY 4.0), a discovery paper. The published passage is in [examples/results-2504.13837.md](../../examples/results-2504.13837.md); this is the skeleton its paragraphs answer to, written as the outliner would write it from the authors' notes.

```markdown
# Skeleton: RLVR for Mathematical Reasoning (results)

Contribution: RLVR makes a model more likely to sample a correct answer but does not give it reasoning ability beyond its base model; at large k the base model covers more solvable problems.
Layers: conceptual — the reasoning ability boundary of a model is what pass@k at large k measures, not pass@1; technical — pass@k curves of base and zero-RL models over k, with CoT validity checked by hand; empirical — base models overtake RL models on every benchmark and size tested.
Orientation: discovery
Names: pass@k, reasoning ability boundary, coverage, zero-RL, RLVR, base model, CoT, hacking, lucky guesses

## Results
Frame: what is compared, on what, by which metric; the main result that tests the main claim; a check that the result is not an artefact; a closing reading. Kept.

### P1 setup
Q: what is compared, on what, and how is a sample counted as correct
Claim: base and zero-RL models from two families are compared by pass@k on six math benchmarks of rising difficulty, with the final answer checked
Evidence: author's setup; SimpleRLZoo checkpoints (GRPO, GSM8K and MATH training set, correctness reward only); Oat-Zero-7B and DAPO-32B added for their AIME24 strength
Hands off: pass@k over k is the quantity to read
Keep: Qwen2.5 7B/14B/32B; LLaMA-3.1-8B; GSM8K, MATH500, Minerva, Olympiad, AIME24, AMC23

### P2 main result
Q: does RL training enlarge or shrink the set of problems a model can solve
Claim: at small k the RL model leads; as k grows the base model catches up and surpasses it on every benchmark (observe, indicates); the RL model is more likely to sample a correct response, the base model covers more solvable problems
Evidence: Figure (pass@k curves, all sizes and benchmarks); Minerva, 32B, about 9% at k = 128
Hands off: the crossover; whether it holds for RL models selected for strength
Keep: k = 1 equals average-case accuracy; the 9% at k = 128 reading

### P3 robustness of the result
Q: does the crossover survive for RL models with strong AIME24 results
Claim: Oat-Zero and DAPO start nearly 30% above their base models and are still surpassed at large k (shows); conclusion drawn here: RLVR raises the likelihood of correct samples at low k and narrows coverage (we conclude)
Evidence: Figure (Oat-Zero-7B, DAPO-32B curves)
Hands off: the root cause is analysed in a later section; whether the base model's rare successes are genuine

### P4 case evidence
Q: what do the base model's correct CoTs on hard problems look like
Claim: hand-picked correct CoTs are long and reflective, so the base model has the reasoning ability (highlighting)
Evidence: Figures of CoTs, selected by hand from 2048 samples on the hardest AIME24 questions
Hands off: a few cases do not rule out lucky guesses; the systematic check follows

### P5 validity check
Q: are the base model's solved problems reached by valid CoTs or by lucky guesses
Claim: on the hardest solvable GSM8K and AIME24 problems almost every solved problem has at least one correct CoT, for base and RL models alike (suggests that the base model samples valid reasoning paths)
Evidence: manual inspection following [cite]; GSM8K: base 24 of 25, RL 23 of 25; AIME24: base 5 of 6 (one ambiguous), RL 4 of 6; threshold accuracy below 5% and above 0%
Hands off: the main result stands as a result about reasoning, not answer hacking
Keep: the two count pairs; the ambiguous case noted
```

Read against the published passage, the skeleton shows what the humanizer could not have recovered from the sentences alone: that P4 and P5 exist to answer a doubt P2 raises, that the conclusion of the section is drawn in P3 and not repeated in P5, and that P5's verb is "suggests" because the inspection was by hand on a small set.
