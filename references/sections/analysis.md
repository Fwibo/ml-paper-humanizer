# Analysis and discussion

One of the section files of [section-playbook.md](../section-playbook.md); read that index first for the orientation tags and the opening logic, then this file for the section being written. Sources are in [sources.md](sources.md).

## What this section does

The analysis subsections come after the main results and ask why: how the method or the phenomenon works, where an advantage comes from and where it stops [Lipton & Steinhardt]. The summary of findings, the limitations and the outlook have their own files (conclusion.md, limitations.md), and nothing here restates the results section.

The reviewer checks:
- that each explanation rests on an experiment in the paper, not on a story [Lipton & Steinhardt];
- that the text says what the numbers mean [Black];
- that the claims match how far the results generalize, with their assumptions stated [NeurIPS].

## Frame

Each subsection asks one question. Inside, the steps run in this order.

1. **Observation.** What the data show, with the pointer to the figure or table, stated so that a reader could check it [Checklist].
2. **Analysis.** The proposed reading, the alternative readings, and the evidence that separates them: a control, an ablation, an intervention [Checklist] [Nanda]. It does not stack a second conjecture on an untested first one.
3. **Conclusion.** The answer to the subsection's question, at the strength and scope the evidence supports, worded the same way wherever it appears (claim-strength.md) [Nanda].
4. **Boundary.** One sentence at the end of the subsection on where the answer stops holding or what stays open [practice default].

The order departs when the argument gives a reason. An error analysis may open on a case before the count. A test fixed in advance may state its prediction before the observation [Nanda].

## Rules

- **Ask one question per subsection, and make the heading a short sentence that answers it.** Split a subsection that asks two, so that the headings alone read as what the paper learned [Mensh & Kording] [exemplars].
  Wrong: "Attention patterns" or "Why does the gate help?" Right: "The gate suppresses distractors late in the input."
- **Run observation, analysis, conclusion.** Do not open with "X fails, as …" [Checklist] [practice default].
- **Back every why-sentence with an experiment, or label it.** A sentence that says why something happens is either supported by an experiment in this paper or marked as intuition or conjecture; speculation may also sit in a separate, clearly marked motivation passage. Test: would you rely on it to predict a result or to get a system to work [Lipton & Steinhardt]?
  Wrong: "This is because deeper layers store factual knowledge." Right: "This is consistent with deeper layers storing factual knowledge (cf. [cite]); we do not test that here."
- **Size each conclusion by the kind of evidence behind it.** Decide per subsection which claim the evidence supports: an existence claim (at least one case), a narrow claim (under stated conditions), a systematic claim (across the range tested) or a hedged claim (suggestive evidence); the verbs for each are in claim-strength.md [Nanda].
- **Prefer the narrow claim that holds.** Write a simple, rigorous finding under stated conditions, not an ambitious claim the evidence half supports [Nanda].
- **Give a causal claim its whole chain.** A claim that A causes B names each link, isolates the variable, rules out the alternatives and, where it can, intervenes on A and shows that B changes; without an intervention or a controlled test it is written as a correlation [Checklist]. Prefer several kinds of evidence on the same link over repeats of one kind [Nanda].
  Wrong: "Longer warm-up causes the stability gain." Right: "Runs with longer warm-up are more stable (Figure 6); varying warm-up alone, with every other setting fixed, removes the loss spikes above 2k steps (Table 7)."
- **Mark readings found after the fact.** A pattern noticed once the results were in is written as a reading, not as a confirmed prediction [Nanda].
- **Use terms that claim no more than was measured.** Define a word with a colloquial meaning ("understands", "reasons", "curiosity") or a suitcase word ("interpretability", "generalization") by what was measured, or use a plainer one [Lipton & Steinhardt].
- **Keep formal and informal claims apart.** When a subsection mixes a theorem with an empirical reading, each sentence makes clear which it rests on; a statement that sounds formal but has no theorem behind it is written as the numerical observation it is [Lipton & Steinhardt].
- **Say what the answer means for the contribution.** Each subsection's conclusion says what it tells the reader about the method or the phenomenon [Black]. An analysis that clarifies no part of the contribution goes to the appendix [Checklist].
- **Keep each concession to one clause, and put one boundary sentence at the end.** The subsection's boundary is stated once, at its end, not in every paragraph, and the paper's real limitations go to the Limitations section [practice default]. Name the questions that stay open [Lipton & Steinhardt].
- **Do not string paragraphs together with rhetorical questions.** A paragraph may open on the one question it answers ("We next test whether …"), not on a chain such as "Why does this happen? Is it the data? Or the optimizer?" [practice default] [Mensh & Kording] [exemplars].

## By orientation

`proof` Say where the assumptions bite: what happens empirically when an assumption is relaxed, and how far the measured behaviour sits from the bound. An assumption that looks arbitrary or proof-driven gets an experiment at its boundary [Checklist].

`effect` Explain why the effect occurs and where it shrinks: the ablations behind the gain, the simpler explanations ruled out (a larger model, more data, longer training, a stronger prompt) and the regime in which the advantage disappears [Checklist] [NeurIPS]. Identify the source of the gain [Lipton & Steinhardt].

`design` Show in the analysis or a case study how the design works inside, each finding tied to the bottleneck a component answers, so that a reader can say why this design was the natural one [Checklist].

`evaluation` Say what the benchmark reveals about method families: which conclusion the old evaluation got wrong, which families fail on which realistic factor, and what that means for designing the next method, ending on guidance future work can act on [Checklist].

`discovery` The analysis is the paper's core. Reproduce the phenomenon before explaining it and show it beyond one narrow setting; test the existing explanations and show them insufficient; give the proposed mechanism a causal chain with no missing link, isolated variables and an intervention that changes the cause and moves the outcome [Checklist]. Write an unsettled mechanism as a hedged reading, worded the same way throughout [Lipton & Steinhardt].

## Common mistakes

- **A chain with a missing link.** A mechanism that looks complete in the figure while one step has no evidence: give each link its evidence and mark the link that stays open [Checklist].

## Before moving on

- Does each subsection ask one question, with a declarative heading that answers it?
- Does each subsection run observation, analysis, conclusion, without opening on a verdict?
- Is every why-sentence backed by an experiment in this paper, or marked as intuition or conjecture? [Lipton & Steinhardt]
- Does every causal claim have an intervention or a controlled test behind it, and is every other relation written as a correlation? [Checklist]
- Is each conclusion worded at the strength and scope its evidence supports, the same way wherever it recurs? [Nanda]
- Are readings found after the results marked as such? [Nanda]
- Is there one boundary sentence per subsection, and no concession longer than a clause?
- Do the claims here match how far the results generalize, with their assumptions stated? [NeurIPS]
- Does each subsection say what it means for the contribution? [Black] [Checklist]

## Sources for this section

- [Lipton & Steinhardt] lipton-steinhardt-troubling-trends.txt
- [Nanda] nanda-highly-opinionated-advice.txt
- [Checklist] lars-contribution-centered-checklist.txt
- [Black] black-writing-a-good-scientific-paper.txt
- [NeurIPS] neurips-paper-checklist.txt
- [Mensh & Kording] mensh-kording-ten-simple-rules.txt
- [exemplars] references/exemplars/
