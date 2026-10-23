# Rebuttal

One of the section files of [section-playbook.md](../section-playbook.md); read that index first for the orientation tags and the opening logic, then this file for the section being written. Sources are in [sources.md](sources.md).

## What this section does

The response is the authors' one part in the discussion the area chair reads before deciding, and it is read in a hurry. Its job is to remove the one easy-to-point-to flaw that would sink a borderline paper, or show it is not one, and to give the reviewer who argues for the paper something to cite. The reviewers and the area chair check:

- that every decisive concern is answered
- each answer against the manuscript: the quoted sentence, its location, the number
- that each promised change is concrete
- the answers to the usual objections: a prior work already shows the contribution, experiments insufficient for the claims, more promised than delivered, important references missing, results too incremental or too different to believe, incorrect statements, poor writing

## Frame

1. **Sort the reviews.** List every point and mark the decisive ones: those several reviewers share, and those an area chair could use as the easy flaw [Freeman] [Ernst]. The order of the review text is not the order of importance.
2. **A short opening for all readers, where the venue allows one.** With a single response or a general comment, one or two sentences on the main concerns and their answers. A reviewer's summary that misstates the contribution is corrected here. Not thanks.
3. **Each concern, answered.** A short heading or one-line restatement of the point in the response's own words, so the answer reads without the review [Ernst] [Freeman]; the direct answer; the evidence (the manuscript's sentence and its location, or the one number needed); what the revision will change. Then stop.
4. **Minor points together,** at the end, one line each: the typos fixed, the citation added.

Where the venue gives each reviewer a thread (OpenReview), each thread follows that reviewer's points in their order, since each reviewer reads their own thread, and a concern several reviewers share is answered once in a general response that each thread points to. [practice default]

## Rules

- **Answer the reviewer's question directly first, then give the evidence.** The answer is the first sentence; civility takes a clause at most, and there is no opening thanks. Wrong: "We sincerely thank the reviewer for the insightful and constructive comments, which have greatly helped us improve the paper." Right: "**Baseline tuning.** Every baseline had the same 40-trial search as our method (Section 5.1); Appendix C, Table 7 lists the chosen values." [practice default] [Freeman]
- **Answer the point raised and stop.** Concede no more than the reviewer asked for, and do not turn one reviewer's local doubt into a general defect the area chair can quote. Wrong: "The reviewer is right that our method does not generalize beyond English." Right: "On the multilingual set the reviewer asks about, the gain is 0.3 points, within seed variance; Section 6 will state that the claim is made for English." [practice default]
- **Give only the supplementary numbers needed to answer the question.** One small table that settles the concern, not five. Each number gets a sentence on what it means and its setup in a clause (seeds, budget). [practice default] [Black]
- **When a review contradicts the manuscript, quote the manuscript's sentence and its location.** Not "we respectfully disagree". Right: "Section 5.2 reports this comparison (lines 340 to 342): 'At matched FLOPs, X reaches 71.2 and our method 73.0.'" [practice default]
- **Treat a misreading as a writing problem.** Say what the paper means and where it says it, and name the sentence the revision adds; do not blame the reviewer. [Freeman] [Ernst] [Peyton Jones]
- **Answer the decisive concerns first and in full.** A concern several reviewers raise, or one an area chair could use as the easy flaw, gets the most space, and none is left unanswered. [Freeman] [Ernst]
- **Answer the kind of objection it is.** "Done before" is answered by the specific difference and where the paper shows it; "experiments insufficient" by the experiment that answers it, existing or added; "promises more than it delivers" by the claim narrowed in the revision; "not believable" by the control that rules out an artefact; "incorrect statement" by the correction. [Black] [Freeman]
- **Admit a real error plainly, with its fix.** Acknowledge an error the reviewer found in a sentence and correct it; the concession covers the error and not the paper. [Freeman] [Ernst]
- **Handle a request for citations by relevance.** If the works are relevant, cite them in the revision and say in a sentence what they got right and how the paper goes further, without disparaging them; if they are not, say why in a sentence. [Lipton] [Black]
- **Make each promise a concrete change.** Not "we will clarify this" but "we will add the three-seed spread to Table 2 and the definition of coverage to Section 3.2". Promise only what the revision will deliver. [Freeman] [practice default]
- **Stay within the venue's rules on new results.** Some venues bar new experiments in the response and others allow them; follow the call for papers. [practice default]
- **Keep the tone civil and secure.** No sarcasm, no remark on the reviewer's care, competence or score; keep the argument on the science. [Freeman] [Ernst]
- **Put every answer into the revised paper.** The response says where the revision answers each question. [Lipton] [Peyton Jones]
- **Add no claim the paper does not make.** Defend the submitted claims at their strength; do not broaden a claim to meet an objection. [practice default]

## By orientation

- `proof` Likely objections: assumptions that look arbitrary or proof-driven, a proof with no visible architecture, a theorem whose importance is unclear. Answer an assumption with the counterexample or obstruction that makes it necessary, a claimed gap with the exact step and its repair (or an admission), and importance with the tie to the problem that motivated the theorem. An experiment does not answer a doubt about a proof. [Checklist]
- `effect` Likely objections: a comparison not matched in budget, untuned baselines, a simpler explanation (a larger model, more data, longer training, a stronger prompt), a cost. Answer with the matched-budget number, the control that removes the simpler explanation, and the seeds behind it. [Checklist]
- `design` Likely objections: too many modules and no central idea, a module that is not needed, a design that looks incremental over a named method. Answer with the bottleneck the design answers, the ablation that tests the module, and the one-sentence difference from the named method with its location. [Checklist]
- `evaluation` Likely objections: a setting harder but not shown more realistic, leakage, a benchmark that is only a leaderboard. Answer with the evidence of realism, the leakage check, and the insight about method families the benchmark gives. [Checklist]
- `discovery` Likely objections: correlation read as cause, a phenomenon seen in one narrow setting, an alternative explanation. Answer with the intervention that changes the proposed cause, a replication where the rules allow one, or the claim narrowed to what the evidence supports. [Checklist]

## Common mistakes

None that the rules above do not already state.

## Before moving on

- Is every point that bears on the decision answered, with the shared and decisive ones first and fullest?
- Does every answer begin with the answer?
- Can each answer be understood without opening the review it answers?
- Is every contradiction met with a quotation and its location, not with disagreement?
- Does any concession go beyond what the reviewer asked?
- Is every new number the minimum the question needs, with its setup and its meaning, and allowed by the venue?
- Is every promise a concrete change with its place in the revision?
- Is the tone civil, with no thanks preamble and nothing about the reviewer as a person?
- Does the response claim nothing the paper does not?
- Will every answer appear in the revised paper?

## Sources for this section

- [Freeman] freeman-how-to-write-a-good-cvpr-submission.txt
- [Black] black-writing-a-good-scientific-paper.txt
- [Lipton] lipton-heuristics-for-scientific-writing.txt
- [Checklist] lars-contribution-centered-checklist.txt
- [Ernst] general/ernst-how-to-write-a-technical-paper.txt
- [Peyton Jones] general/peyton-jones-how-to-write-a-great-research-paper.txt
