# Conclusion

One of the section files of [section-playbook.md](../section-playbook.md); read that index first for the orientation tags and the opening logic, then this file for the section being written. Sources are in [sources.md](sources.md).

## What this section does

The last statement of the contribution, for a reader who has seen the evidence: what the paper solved, proposed or proved, why it matters and what follows, at the strength the results support, adding nothing the body has not shown. The reviewer checks:

- the key ideas, the experiments that validate them and their significance, in sentences the review form can take
- no claim broader than the experiments showed
- no future-work list
- limitations positioned as future work, not ignored

## Frame

In its usual order:

1. **The contribution, restated.** One or two sentences on the insight and the result it produced, in the words the title and the introduction used for the contribution. Not the method module by module, not the sections in order.
2. **The evidence, read one step further.** The strongest result with its condition, and what it means now the reader has seen it: why the method works, where its advantage is largest, which reading of the phenomenon the results favour [Black]. No number, setting or comparison the results section lacks.
3. **Why it matters.** What the result opens up, or how it changes the way the problem is approached [Freeman], in the form the orientation gives (below). Not a stakes sentence that fits any paper, or a significance the body never argued.
4. **What follows.** One sentence on a real next step; a limitation named here is phrased as that step.

The four steps may share sentences. Where the template puts the conclusion and the limitations under one heading, they stay two paragraphs and the limits do not displace the conclusion's ending. Any other order needs a reason the argument gives; the order in which the work was done is not one.

## Rules

- **Restate what the reader should remember.** What the paper solved, proposed or proved and why it matters, like an abstract in the present tense, reading the results a step further. Wrong: "In this paper, we proposed RouteGate, which consists of a scorer, a router and a merger, and conducted extensive experiments." Right: "Routing tokens by predicted difficulty rather than by position lets a fixed compute budget follow the hard tokens; at matched FLOPs this lowers perplexity at every model size we trained." [Black] [刘知远]
- **Restate the insight, not only the technique.** Name the view that made the problem solvable as well as the module that realizes it. [Black] [Checklist]
- **Do not paste the abstract or the introduction.** Keep the claim; what the conclusion adds is the reading of the results. [Nanda] [Black]
- **Keep each claim at the strength the results gave it.** Use the verb and the condition of the results section: "suggests" does not become "shows", and "on four benchmarks" does not become "in general". [NeurIPS] [Freeman] [Nanda]
- **Do not under-claim either.** State the contribution once, clearly, with its condition; do not end in hedges. [Black]
- **Word a conjectural explanation the same way as elsewhere.** An explanation the paper did not establish keeps the wording it had in the introduction, the contributions and the results; it does not harden at the end. [practice default]
- **Mark speculation and opinion as such.** The conclusion may speculate a little more than the body, about why the method works or where the work leads, if the sentence says it is a belief or a hypothesis and keeps it apart from what the evidence showed. Wrong: "The gate works because it learns token difficulty." Right: "We believe the gate learns something like token difficulty; testing that reading directly remains open." [Karpathy] [Lipton] [Lipton & Steinhardt]
- **Keep one number, with its condition, and name no table or figure.** The strongest number, as in the abstract. [practice default]
- **One paragraph by default.** With several contributions, a short paragraph restates each with its evidence, then one closing sentence follows. [刘知远]
- **End on the conclusion, not on a new limitation.** The last sentence is on what the work showed, what it opens up, or how it changes the approach to the problem; the limits go in the Limitations paragraph. [Freeman] [practice default]
- **Name one real next step, not a list.** One step that follows from this paper's result, not "extend to more datasets and models in future work". Wrong: "In future work, we will apply our method to more tasks, larger models and other modalities." Right: "Because the router needs only per-token losses, the same scheme applies to speech models, where token difficulty varies more." [Freeman] [Black]
- **Phrase a named limitation as a path forward.** One sentence states it as the next step with a practical way to address it. Wrong: "A limitation of our approach is that it requires labelled seeds." Right: "The method still starts from labelled seeds; drawing them from the model's own confident predictions would remove that requirement." [Black] [Checklist]
- **Mark an aspiration as not attained.** A broader goal that motivated the work may appear as motivation if the sentence makes clear the paper did not reach it. [NeurIPS]
- **Say what is settled and what is open.** Draw the line between the problems the paper solved and those it leaves open. [Lipton & Steinhardt]
- **Nothing new.** No result, claim, comparison or limitation appears for the first time in the conclusion; one that does moves into the results with its evidence, or is dropped. [Black] [practice default]
- **A conclusion written on its own brings the Limitations paragraph with it.** Where the venue has a Limitations section (NeurIPS encourages a separate one), write it with the conclusion; the limits move there. [NeurIPS] [practice default]

## By orientation

- `proof` Say why the theorem matters, tied to the real problem that motivated it. Restate the guarantee with the assumption it rests on, and the gap it closes against the closest known result. A good next step is the assumption whose relaxation would matter most. [Checklist] [NeurIPS]
- `effect` Restate the advantage on the trade-off that matters, at the budget at which it was measured, with the idea that produces it, not the numbers alone. Say whether the gain is worth its cost, as the experiments did. [Checklist]
- `design` Say why this design was the natural one, not only that it works: the bottleneck, and the design principle in one conceptual sentence. [Checklist]
- `evaluation` End with actionable guidance for future methods: what the old evaluation would have led a reader to conclude, what the new one reveals about method families, and what a method designer should now do differently. Not who tops the table. [Checklist]
- `discovery` State the causal claim at the strength the intervention evidence supports, and the settings it covers. A link that rests on correlation stays a correlation; a phenomenon seen in one setting is claimed for that setting. [Checklist]

## Common mistakes

- **The closing apology** ("However, our method still has several limitations, which we leave to future work"): cut it; the limits go to the Limitations paragraph, each named with its scope. [practice default]

## Before moving on

- Can a reader state the contribution in one sentence from the conclusion alone, in the vocabulary of the title and the introduction?
- Is it in the present tense, and one paragraph unless several contributions are restated?
- Does every claim keep the verb and the condition the results section gave it, neither stronger nor hedged further?
- Does it read the results a step further than the abstract?
- Is its one number the strongest, with its condition, and is that number in the body?
- Is it free of table and figure references and of anything the body does not show?
- Is every conjecture worded as in the introduction and the results, and every opinion marked as one?
- Does it end on what the work opens up or changes, with at most one next step, specific to this result?
- Does it do what the By orientation entry for this paper asks?
- Where the venue has a Limitations section, are the limits there and not here?

## Sources for this section

- [Black] black-writing-a-good-scientific-paper.txt
- [Freeman] freeman-how-to-write-a-good-cvpr-submission.txt
- [刘知远] liuzhiyuan-nlp-paper-zhihu-summary.txt
- [Checklist] lars-contribution-centered-checklist.txt
- [NeurIPS] neurips-paper-checklist.txt
- [Nanda] nanda-highly-opinionated-advice.txt
- [Lipton] lipton-heuristics-for-scientific-writing.txt
- [Lipton & Steinhardt] lipton-steinhardt-troubling-trends.txt
- [Karpathy] karpathy-phd-survival-guide.txt
