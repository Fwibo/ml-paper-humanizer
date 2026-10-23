# Limitations

One of the section files of [section-playbook.md](../section-playbook.md); read that index first for the orientation tags and the opening logic, then this file for the section being written. Sources are in [sources.md](sources.md).

## What this section does

It says how far the paper's knowledge reaches: the assumptions the results rest on, the conditions the evidence covers, and the conditions under which the method is known to do poorly. It bounds the claims; it does not retract them. The reviewer checks:

- every weakness the reviewer would write in the Weaknesses entry, already stated here
- no limitation the reviewer finds that the paper does not acknowledge
- each limit clear and specific, with the main contribution left standing
- the abstract's claim within the scope stated here

## Frame

In its usual order:

1. **The assumptions.** The strong assumptions the results rest on (independence, noiseless data, a well-specified model, an approximation that holds only locally) and the implicit ones of the experiments (a test distribution like the training one, a fixed prompt, a tuning budget), each with what happens to the results when it fails in practice [NeurIPS].
2. **The scope of the evidence.** What the evidence covers, in numbers (datasets, runs, model sizes, languages or domains), stated as the conditions under which the work is untested, not as a doubt [NeurIPS].
3. **The factors that affect performance.** Where the method is known or expected to do poorly, with the evidence the paper has, such as a failure case or a setting where the gain shrinks [NeurIPS] [Black]. Cost goes here when it decides whether the method is usable.
4. **What remains.** For each limit, the conclusion it affects and the one it leaves standing, and the practical path to removing it where one exists [Black] [Checklist]. The paragraph ends on what still holds, not on the weakest point.

Within each step, the limit that bears most on the main claim comes first. A paper with one dominant limitation may open on it, since the reader needs it to weigh everything else.

## Rules

- **Write the real limitations, all at once, in one paragraph.** Two paragraphs where the venue asks for a separate section and the assumptions need several sentences. Real means the limits that bound the main claims, not harmless ones such as "we did not test every possible dataset". The results paragraphs do not repeat them as closing caveats. [NeurIPS] [practice default]
- **For each limitation, say which conclusion it affects and which it does not.** Wrong: "Our evaluation is limited to English, so the results should be interpreted with caution." Right: "All benchmarks are English, so the ranking of the three methods may differ in other languages; the speed-up does not depend on the text and holds as measured." [Checklist]
- **Say under which conditions the work is untested, not that it "may not generalize".** "Generalization" packs together train-to-test performance, transfer to another population and validity in real use; say which is meant. Right: "We trained models up to 1.3B parameters; whether the effect persists at larger scale is untested." [NeurIPS] [Lipton & Steinhardt]
- **Name each strong assumption and what happens when it fails.** Say how it might be violated in practice and what that would do to the results; report any robustness check the paper has. [NeurIPS]
- **Articulate the implicit assumptions of the experiments.** Name the choices a result depends on: the split, the prompt template, the tuning budget, the data source. [NeurIPS]
- **State the scope of the evidence in numbers.** How many datasets, how many runs, which sizes. A claim tested on few datasets or few runs says so here and where it is made. [NeurIPS]
- **Name the factors that affect performance.** Say where the method does poorly as concretely as "at low resolution or in poor light" for a face recognizer, and point to the failure cases in the appendix. [NeurIPS] [Black]
- **Keep the abstract and the introduction within this scope.** If only 7B models were tested, the abstract does not claim "language models". A scoped claim takes the form "X is the best method for situations V and W". [NeurIPS] [Nanda]
- **Mention a limitation early where it bears on the reading, and detail it here.** State an important assumption in a clause with the claim it bounds in the abstract or the introduction, and in the method where the reader needs it to read the method; the full discussion comes here. [NeurIPS] [Ernst]
- **Do not hide a limitation.** Report what did not work, and convey the right impression of performance. [Freeman] [NeurIPS] [Nanda]
- **Test a limitation that can be tested.** If a modest experiment can settle a likely weakness, including a reviewer's "is it possible this only works because X?", run it and report the result instead of listing the doubt; the bolder the claim, the more this applies. [Nanda] [Lipton]
- **Say how the result could be over-read.** Name the misreading a reader is likely to make (a gain on a benchmark taken as a gain on the task, a correlation taken as a mechanism) and what the evidence does not show, including whether the evidence could hold while the claim is false. [Nanda]
- **Say what was not isolated.** Where components were not ablated separately, or the method and the baselines were tuned with different effort, say which part of the gain is not attributed. [Lipton & Steinhardt]
- **Scope a comparison with humans or a broad capability.** Bound a claim of human-level performance, or of "understanding", by the task and the test data measured, and say what the comparison does not cover, such as conditions a person meets and the test set does not. [Lipton & Steinhardt]
- **Separate what is open from what is solved.** Say which questions the paper leaves open, including "under what circumstances won't it work?" [Lipton & Steinhardt]
- **Pair a limit with its path forward, in a sentence.** Where a practical way to address a limit exists, say it in one sentence per limit, not a research plan. [Black] [Checklist]
- **Bound the claim without undermining it.** Size each limit and say what still holds; no vague, sweeping or apologetic wording ("results should be taken with caution", "unfortunately"). [Checklist] [practice default]

## By orientation

- `proof` State the full set of assumptions, as each theorem must [NeurIPS]; say which are necessary, with the counterexample or obstruction that shows it, and which serve the proof technique. Say where the guarantee is loose (constants, asymptotic only, local) and how far the setting of any experiment departs from the setting proved. [NeurIPS] [Checklist]
- `effect` Give the budget and the settings at which the advantage was measured, where it shrinks or reverses, and whether the gain is worth its cost there. Say which simpler explanation (a larger model, more data, longer training, a stronger prompt) was not ruled out. [Checklist]
- `design` Say what the design assumes of its inputs (information available at test time, a resource it needs), which modules were not ablated or were ablated only together, and the regime in which the targeted bottleneck is absent and the design should bring nothing. [Checklist] [Lipton & Steinhardt]
- `evaluation` Say what the benchmark covers and does not (sources, domains, languages, time span), what gap between the new setting and real use remains, how far the leakage and annotation checks go, and which conclusions about method families it cannot support. [Checklist]
- `discovery` Name the settings in which the phenomenon was observed and those not tested; say which links of the causal chain rest on intervention and which on correlation, and which alternative explanations remain. [Checklist]

## Common mistakes

None that the rules above do not already state.

## Before moving on

- Is each strong assumption named, with how it might be violated in practice and what that does to the results?
- Are the implicit assumptions of the experiments (split, prompt, tuning budget, data source) stated where a result depends on them?
- Is the scope given in numbers and stated as the conditions under which the work is untested?
- Are the factors that make the method do poorly named, with the failure cases pointed to?
- Does each limitation say which conclusion it affects and which it does not, and does the paragraph end on what still holds?
- Do the abstract and the introduction claim no more than this scope, and mention the important limits where they bear?
- Would a reviewer filling in the Weaknesses entry find a weakness that is not here?
- Has every limit that a modest experiment could settle been tested?
- Are the limits in one place, without the same caveat repeated across the results?

## Sources for this section

- [NeurIPS] neurips-paper-checklist.txt
- [Black] black-writing-a-good-scientific-paper.txt
- [Lipton & Steinhardt] lipton-steinhardt-troubling-trends.txt
- [Nanda] nanda-highly-opinionated-advice.txt
- [Checklist] lars-contribution-centered-checklist.txt
- [Freeman] freeman-how-to-write-a-good-cvpr-submission.txt
- [Lipton] lipton-heuristics-for-scientific-writing.txt
- [Ernst] general/ernst-how-to-write-a-technical-paper.txt
