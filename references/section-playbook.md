# How each section goes, by paper orientation

Each section opens with its frame, the things that section does and their usual order. The frame is kept; the wording is free; bold, boxes and run-in headings are format and follow the venue. A different order needs a reason the argument gives (a proof that states the theorem first, an error analysis that opens on a case). The orientation-tagged lines below are references for what readers of that paper type expect.

Core principle. The contribution is the spine of the paper, and every section must let the reader understand, locate, trust and remember it. Before writing, state the contribution in one sentence. If that sentence is only "we propose a method and it works better", the contribution is not yet clear. Write the conceptual layer (a new view, problem formulation, mechanism or principle), the technical layer (the algorithm, model, proof technique, module or benchmark design that realizes it) and the empirical layer (the evidence that it matters) separately. The technical layer alone is rarely enough.

Rules carry orientation tags. `proof` covers a theorem, condition, bound or guarantee. `effect` covers a performance, efficiency, scaling or robustness advantage on an important trade-off. `design` covers a new method, framework, architecture or system that follows from a bottleneck. `evaluation` covers a benchmark, dataset, split, metric or protocol. `discovery` covers a phenomenon, mechanism or empirical law. An untagged rule applies to every orientation.

### Orientation opening logic (light reference)

The opening logic per orientation is a light reference, not a template. Use it to decide what the first two paragraphs must establish, never as a sentence pattern.

- `proof` Why the general problem is impossible, and what assumption removes the obstruction.
- `effect` The trade-off that matters.
- `design` The reformulated problem and the design principle, before any module.
- `evaluation` The mismatch between current evaluation and real use.
- `discovery` The phenomenon, then why existing explanations fall short.

The common risks per type (numbers without an idea, implementation before motivation, correlation written as cause, harder but not more realistic) are the honest failure modes to avoid. None of them is fixed by a sentence template.

## Abstract

Frame. Context, the gap, the idea, the mechanism that closes the gap, the evidence, in that order; the last sentence states what the result means. Each step is a sentence or two.

- By the end of the first few sentences the reader knows the problem, what existing methods miss, the paper's idea and its strongest result. Implementation details, the research process and long background come later or not at all.
- `effect` `design` Give the result sentence one strongest number and its condition ("improves X by 12 points on Y at the same cost"). Do not list every dataset.
- `design` State the design in one conceptual sentence and say why it addresses the gap.
- `discovery` Write findings as contrastive statements ("X raises scores more often, yet breaks correct answers just as often"), one sentence per finding, never three layers of clauses.
- `evaluation` Say what is measured, why existing evaluation cannot measure it, the scale, and one surprising result from existing models.
- Make the title reveal the core contribution, not only the task. A `design` title says what method is used for what problem, an `evaluation` title reveals the evaluation perspective, and a `discovery` title makes the reader curious about the phenomenon.
- Let the last sentence state the significance or the next step, not a limitation.

## Introduction

Frame. Background, the limitation of existing work, the insight that explains the limitation, the solution that follows from the insight, the contributions. The limitation is structural, not a convenient weakness; the insight paragraph comes before the method; the contribution items match the gap and the experiments.

Plan Figure 1 and Table 1 with the introduction. Both should show the contribution before the reader reaches the details.

- `proof` Make Figure 1 a counterexample, the modeling rationale or the proof architecture, so that it shows the problem is impossible or ill-posed without the assumptions. Let Table 1 compare assumptions and guarantees across existing theories.
- `effect` Make Figure 1 the trade-off plot that matters (accuracy against parameters or FLOPs, performance against supervision budget, robustness against shift severity), not a cherry-picked metric. The advantage should be visible before the main table, and one figure, not many tables, should make it memorable. Let Table 1 report matched-budget comparisons.
- `design` Make Figure 1 contrast the old pipeline with the new design, or show the overall framework, so that the difference is simple and memorable. Let Table 1 compare capabilities such as dynamic behavior, end-to-end optimization, use of heterogeneous information, interpretability and supervision needs.
- `evaluation` Make Figure 1 set the old evaluation against the new one, and show that the difference is realistic and consequential. Let Table 1 compare benchmark properties such as distribution shift, cold start, long-tail coverage, leakage control, metric realism and reproducibility.
- `discovery` Make Figure 1 show the mechanism chain or failure chain as a testable sequence of causes, not a vague correlation or a qualitative story. Let Table 1 compare existing explanations by whether they locate the source, explain the mechanism, predict outcomes and support intervention.

### First paragraph

- Run from broad background, to narrow background (optional), to the task at hand, to how existing methods handle it, to the problem hidden in them.
- Make the first sentence plain, complete and uncompressed. Let the second sentence tighten to technical content.
- Let the last sentence only show that the problem exists ("… remains poorly understood" / "… remains open"). Do not write "this paper answers the question".
- Do not answer the paper's open question inside the first paragraph, not even as a hint ("…, which we trace to X"). State the gap there; the answer comes in the insight or method paragraph.
- Put no data in the first paragraph. The account of how existing methods work may plant the hidden flaw that later text develops.

The opening logic differs by orientation and runs over the first paragraph and the one after it. This spells out the light reference above; it is not a template.

- `proof` Do not open with a complex theorem. First show why the fully general problem is impossible, then which assumptions remove the obstruction, then why the algorithm or relaxation is natural.
- `effect` Open with the single trade-off that matters. Then show that existing methods are limited on it and that the method moves the frontier. Strong numbers with no idea behind them are not a contribution.
- `design` Reformulate the problem first and name the bottleneck that makes the design necessary. Then state the design principle. Modules and implementation details come only after that.
- `evaluation` Open with the mismatch between current evaluation and real deployment or scientific use. Name the realistic factor that current evaluation misses and the false conclusion it can lead to. Present the new evaluation as the response to that mismatch.
- `discovery` Open with a phenomenon important enough to explain. Say which existing explanations fall short and why. Then propose a mechanism to be validated by controlled evidence, not only by correlation.

### Middle paragraphs

- Let each paragraph's first sentence catch the end of the one before. If the previous paragraph ends on why X remains unclear, this one opens with "To study this question, we …".
- End each paragraph on a fact or a result, not on a derived takeaway that the next paragraph picks up ("The bottleneck is thus X." → "To remove this bottleneck, …"). Picking up an open question that the previous paragraph stated as a fact is fine; picking up a "thus" conclusion is the template. Do not close the introduction with a roadmap paragraph or hand-off sentence unless the paper's outline asks for one.
- Do not name specific datasets, model versions or hyperparameters. Say which kind of dataset and which kind of model, and keep the citations.
- Let each paragraph cover only its own role. The framework paragraph covers the framework and does not run ahead into the findings.
- `design` Tell the method paragraph as what the gap suggests, what the core idea is and why that idea closes the gap. Do not list modules.
- `discovery` Give each finding one conclusion sentence and one evidence sentence, without mechanical numbering such as At the first / At the second. The introduction keeps only numbers that surprise at a glance.
- Tell a paragraph about an improvement or a method's effect as a story. It runs from the finding to what we think should be done, what we did, how well it worked and what follows. Leave out design details.

### Contributions

- Use three items in a fixed shape. A `design` or `effect` paper gives the problem or framework, the technical point and the result. A `discovery` paper gives the framework or protocol, the findings and the improvement or implications. An `evaluation` paper gives the resource, the evaluation protocol and the findings. A `proof` paper gives the assumptions and why they are needed, the main theorem and its comparison with the closest known theorems.
- Four or more items mean the main line is not yet clear.
- Do not restate abstract sentences in the contribution items, and do not write "We are the first to".

## Method

Frame. The problem setup and the overall framework first, then the components, each introduced by the bottleneck it answers; the connection to, and the difference from, prior methods where a reader would ask. Symbols appear when needed and keep their names. The section reads as a blueprint, not as a log of what was built.

- Explain what and why in the body. Move configuration notation, data sizes and per-split question counts to the appendix, with one sentence pointing there.
- Display only the equations the paper actually uses to define an object or state a claim. Do not display derived identities, ideal-case equalities or symbols added to look formal. Do not write seven equations where three will do.
- Define each symbol at first use and never rename it.
- Do not pile explanations into parentheses.
- `design` `effect` Give the whole in one sentence first, then describe the modules in data-flow order. Each module answers which problem the previous paragraph left open. Do not write "we carefully design".
- `design` Tie every module to a specific bottleneck and connect all modules by one logic instead of assembling them independently. Do not let the module count outgrow the central idea.
- `design` State the motivation of every module before its details. Do not describe the implementation before the motivation.
- `effect` Present the idea behind the advantage, so that the method does not read as a set of tuning tricks.
- `proof` Before the theorem, explain each main assumption with a simple example or an information-theoretic obstruction, so that no assumption looks arbitrary or proof-driven.
- `proof` Derive the algorithm or relaxation from an ideal but intractable objective. Compare the main theorem against the closest known theorems.
- `proof` Give a proof roadmap before the technical lemmas, so that the proof has a visible architecture. Say what each lemma contributes to the theorem.
- `evaluation` Justify the split, the metric, the data source and the task construction. Organize the metrics around one central question instead of piling them up.
- `discovery` Give the object of the audit or measurement first, then the reference (what counts as correct and what counts as noise), then the measure. If the reference and the noise are unclear, no later number can be read.

## Experiments and results

Frame. What is compared, on what and by which metric, in a sentence or two; the main result, which tests the main claim; then each further experiment introduced by the question it answers (an ablation by the contribution it tests, a case study by the mechanism it shows, an efficiency comparison by whether the gain is worth its cost, a matched-setting rerun by the confound it removes); a closing sentence on what the results mean together. Every results paragraph opens on the pointer and the claim and lands on a result or a hedged reading. Whether the blocks carry run-in headings, bold or `\paragraph` follows the venue template; the sequence does not.

- State the metric in the body at least once, even in one sentence. A table note alone does not count.
- A caption says what the table or figure shows, in one or two plain sentences, and stops; the reading it supports goes in the body, not in a bold sentence in the caption. Symbols and column names get a sentence only where the body does not explain them.
- Give every experiment a question it answers for the argument (claim-strength.md). An experiment whose question the reader cannot name goes to the appendix.
- Open each results paragraph on one sentence that carries both the pointer and the claim ("Table 2 shows that the gate lowers perplexity by 0.2 at every size"); row readings come after the claim. A results subsection may open on a whether-question ("We first check whether …") or a five-word pointer sentence, not on a hypothesis restated from the lead-in or a stakes frame ("This would be a poor trade if …").
- Keep every number the outline attaches to a claim (a setting, a margin, a count, a row value). "Roughly doubles" with no figure, or "in every column but one" with no value, reads as evasion. Numbers already in a table are read out when the sentence makes a claim about them, and left in the table otherwise.
- Read the table as the authors would, by naming the comparison that matters, not by table geometry ("in every column but one", "the cells in the third block").
- Land every analysis paragraph on a result or a hedged mechanism sentence about this paragraph's evidence ("…, suggesting that …"), not on a row-by-row reading of the table and not on a derived takeaway that the next paragraph picks up.
- Report variance, number of seeds and significance. A single-run number is one sample and is not written as a fact.
- `effect` `design` Once the opening sentence has given the pointer and the claim, let the main-results paragraph say under which conditions the method is best, why the advantage arises and what practical problem it solves. Do not expect the reviewer to find this in the table. Do not make a metric you do not lead on the main battleground. Change the evaluation dimension, setting or comparison basis to say which contest the paper wins. Do not write ablations as a list such as "removing A drops 2.1, removing B drops 1.4". Write what question each component answers and what the answer is, with the number the outline attaches to it.
- `effect` Configure strong baselines fairly and match their budget. Report the cost metrics that matter (parameters, FLOPs, latency, memory, tokens, labels, human effort) and say whether the gain is worth the cost.
- `effect` Rule out simpler explanations such as a larger model, more data, longer training or a stronger prompt. Use the ablations to explain why the effect occurs.
- `design` Use the ablations to test the necessity of each key design, and tie each ablation back to a claim. Use a case study to show how the design works inside.
- `discovery` Write findings paragraphs as observation, analysis, conclusion. Make run-in headings short declarative sentences. Write an unsettled explanation as a hedged reading (suggests, may, is likely, "We hypothesize that") and word it the same way throughout, without turning "We conjecture:" into the frame of every section.
- `discovery` Reproduce the phenomenon clearly before analyzing it, and show that it holds beyond one narrow setting.
- `discovery` Give the explanation a causal chain with no missing link. Isolate variables, rule out alternative explanations and run an intervention or counterfactual that changes the proposed cause and shows that the outcome changes. Do not write correlation as causation.
- `evaluation` Report the overall performance of existing models first, then break it down by difficulty or category, and use the last paragraph to say what these numbers mean for method design. Do not read out scores model by model or cell by cell.
- `evaluation` Show that the new setting is more realistic and more meaningful, not only harder. Draw new insights about method families, so that the benchmark is more than a leaderboard of who wins.
- Report negative results honestly but without exaggeration. Write small positive gain for a small positive gain and mostly variation for a difference within noise. Do not write no gain, fails or only.

## Analysis and discussion

Frame. One question per subsection, with a heading that answers it in a short sentence; inside, observation, then analysis, then conclusion; one boundary sentence at the end of the subsection, not at the end of every paragraph.

- Ask one question per section, and make the heading a short sentence that answers it.
- Run observation, analysis, conclusion. Do not open with "X fails, as …".
- Keep each concession to one clause, and put one boundary sentence at the end.
- Do not string paragraphs together with rhetorical questions.

## Related work

Frame. A map of the field organised by the dimensions that matter for this paper, each paragraph ending on what this paper adds to that line, and a final paragraph that names the coordinate none of them occupies. Not a list of papers one by one.

- Organize by topic. End each paragraph on the coordinate this paper adds. Do not write the stock "Unlike these works, we…" and do not restate papers one by one.
- Give every factual statement a citation, and check before writing that the cited work really supports it.
- Aim for accuracy, not count. Do not cite analogies with a different mechanism. Cite same-mechanism work from a different setting with cf. Do not use an as or since clause to import a cause from the literature.
- Put at most three papers in one parenthesis. More means the sentence is too general.
- When main-text pages are tight, keep one main-text paragraph with inline bold topic names and move the full version to the appendix.

## Conclusion

Frame. What the paper solved, proposed or proved, and why it matters, at the strength the evidence supports; one sentence on what follows. Nothing new.

- Restate what the reader should remember: what the paper solved, proposed or proved, and why it matters.
- End on that, not on a new limitation. Limits belong in the Limitations paragraph.
- Word conjectural explanations the same way as in the introduction, the contributions and the results.
- Do not write the all-purpose "extend to more datasets and models in future work". Name one real next step.
- `proof` Say why the theorem matters, and tie it back to the real problem that motivated it.
- `design` Say why this design was the natural one, not only that it works.
- `evaluation` End with actionable guidance for future methods.
- `discovery` State the causal claim at the strength the intervention evidence supports, and name the settings it covers.

## Limitations

Frame. The real limitations in one paragraph, each with the conclusion it affects and the one it does not; positioned as what remains, not as a retraction.

- Write the real limitations, all at once, in one paragraph.
- For each limitation, say which conclusion it affects and which it does not.
- Do not use a negative judgment wider than the evidence ("may not generalize"). Say under which conditions the work is untested.

## Appendix

- Treat the appendix as part of the paper, not an internal report. Do not write the original analysis, source records, driver output, script names, workspace names, batch names or session ids.
- Organize sections by type of material (extended related work, notation and setup, protocols and algorithms, prompts, additional experiments, full per-method tables, cases, limitations), not by the main-text argument. Each section holds one type of material.
- Give each additional-experiment subsection four parts. Setup (which configuration, compared against what), Measures (metric definitions), Results (walk through the table by the comparisons that matter, not by its geometry, and close on the result), Reading (state the boundary once).
- Make each subsection self-contained. Cite main-text tables and sections, not paragraphs of other appendix subsections. When a definition from elsewhere is needed, restate it in one sentence.
- Write protocols as algorithm boxes. Put prompts in boxes verbatim, with one sentence before the box saying who uses it and when, and no interpretation after it.
- When the main text points to the appendix, point to the subsection and the table.

## Rebuttal

- Answer the reviewer's question directly first, then give the evidence. Do not open with three lines of thanks.
- Answer the point raised and stop. Concede no more than the reviewer asked for, and do not turn one reviewer's local doubt into a general defect.
- Give only the supplementary numbers needed to answer the question.
- When a review contradicts the manuscript, quote the manuscript's sentence and its location. Do not write "we respectfully disagree".
