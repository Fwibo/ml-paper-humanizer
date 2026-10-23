# Abstract

One of the section files of [section-playbook.md](../section-playbook.md); read that index first for the orientation tags and the opening logic, then this file for the section being written. Sources are in [sources.md](sources.md).

## What this section does

The abstract carries the whole message to a cold reader who knows neither the subfield nor its techniques [Nanda]: the introduction in miniature, each of its parts cut to a sentence or two, in about 100 to 200 words [刘知远]. The reviewer checks that:
- context, gap, idea, mechanism and evidence are all present [Checklist];
- the gap is a sharp pain point, and the method sentence says why the method addresses it [Checklist];
- the results are concrete enough to trust [Checklist];
- the claims stay within the paper's contributions and scope [NeurIPS].

## Frame

Context, gap, idea, mechanism, evidence, meaning, in that order; each step a sentence or two, one idea to a sentence [Nanda] [Black].

**1. Context.** One sentence or phrase that places the paper in its subfield and says something no reader would dispute [Nanda] [Lipton]. It does not grow into background.

**2. Gap.** A specific shortfall of existing approaches that the reader can check, stated in terms the authors of those approaches would accept [Checklist] [Lipton]. It does not name every prior method.

**3. Idea.** The paper's insight in one sentence: the way of seeing the problem that makes it solvable [Black] [Nanda]. It is not a list of what was built.

**4. Mechanism.** How the idea closes the gap [Checklist]. When the idea fixes one thing and leaves a second, this step states what remains and the further step that solves it [Black]. Implementation details, hyperparameters and the research process stay out.

**5. Evidence.** The strongest result, with a number and the condition under which it holds [Lipton] [Nanda] [Checklist]. It is not a list of every dataset.

**6. Meaning.** The last sentence says what the result means for the gap: what it implies for the field, the next step it opens, or the standard of evidence the paper claims (a first step toward X; practitioners should take care with Y) [Nanda] [Mensh & Kording] [Black]. Where the venue expects a line on code and data, it comes after this sentence [Black].

The order departs only for a reason the argument gives. A paper whose single result is the news may lead with the contribution and fold the context into a phrase; the reader still learns what is measured before any number [Lipton]. In a `discovery` abstract the idea and mechanism slots hold the findings; in an `evaluation` abstract the mechanism slot holds the evaluation design.

## Rules

### Content and order

- **The first sentences carry the paper.** By the end of the first few sentences the reader knows the problem, what existing methods miss, the paper's idea and its strongest result. Most of the abstract, counted in sentences, says what this paper does; implementation details, the research process and long background are left out. [Lipton] [Nanda] [Checklist]
- **Goal, problem, solution, possibly twice.** Make the reader want the goal, show what blocks it, then remove the block with the idea; when the idea leaves a second block, the method's further step removes it. An abstract without the turns ("Unfortunately", "In contrast", "While promising", "Therefore", or their equivalents) is probably not telling the story. [Black]
- **One story.** The abstract carries one contribution. A second, unrelated idea stays out of the abstract even if it stays in the paper. [Black] [Karpathy]
- **A first sentence that belongs to this subfield.** It names the part of ML the paper works in, in terms no reader disputes, and could not open any other paper. Wrong: "Large language models have achieved remarkable success across many tasks." Right: "Speculative decoding speeds up inference by letting a small model draft tokens that a large model verifies." [Lipton] [Nanda]
- **A sharp gap.** The gap says what fails, where, and how badly. Wrong: "However, efficient inference remains challenging." Right: "Drafters trained on web text have their tokens accepted half as often on code." [Checklist]
- **A method sentence that says why.** It states the design as the answer to the gap. Wrong: "We propose X, which consists of a router, a memory and a fusion module." Right: "X adapts the drafter to each domain from the target model's own outputs, which removes the mismatch without new labels." [Checklist]
- **No modules without their relation.** If two parts must be named, the sentence says how one serves the other or which shortfall each removes. [Checklist] [Ernst]
- **Give away the result.** Say what was found, not only what was evaluated. Wrong: "We evaluate how pruning affects calibration." Right: "Pruning raises calibration error long before it lowers accuracy." [Lipton] [Ernst]
- `effect` `design` **One strongest number, with its condition.** Give the result sentence one strongest number and its condition ("improves X by 12 points on Y at the same cost"). Do not list every dataset; breadth fits in a phrase ("across four benchmarks"). [Lipton] [Nanda] [Checklist]
- **Words a cold reader can follow.** Use simple language, define any jargon the claim needs unless it is standard in the field, and leave out acronyms other than the method's name. [Nanda] [Mensh & Kording]
- **The contribution's own words.** Name the contribution with the same terms as the title, the introduction and the later sections. [Checklist]
- **End on what the result means.** The last sentence states the significance or the next step, and may say how strong the evidence is; limitations go to their own section. Wrong: "However, our analysis is limited to English." Right: "The results point to domain mismatch as the main limit on speculative decoding outside web text." [Nanda] [Mensh & Kording]
- **Short.** About 100 to 200 words, one sentence per idea. [刘知远] [Lipton] [Nanda] [Peyton Jones]
- **Draft it first, revise it last.** Write the abstract before the body, and rewrite it as the body settles. [Nanda] [Ernst]

### Claims

- **Promise only what the body delivers.** Every claim in the abstract has its evidence in the paper; check each claim against its table or theorem. Do not underclaim a real contribution either. [Freeman] [Black] [NeurIPS]
- **Claim at the scope of the evidence.** A claim says where it was shown (which models, tasks or settings) and is as strong as the evidence: an existence proof, a systematic claim, a hedged one or a narrow one. An aspirational goal may motivate the paper as long as the abstract does not imply it is reached. Wrong: "X eliminates hallucination in summarization." Right: "X halves unsupported statements on three summarization benchmarks." [Nanda] [NeurIPS]
- **No speculation stated as explanation, no suggestive labels.** State an untested account of why the method works as a hypothesis, avoid terms with human connotations ("understands", "human-level"), and say what was measured. Wrong: "X works by reducing internal feature drift." Right: "X improves accuracy by 3 points, and removing its normalization step removes most of the gain." Wrong: "X achieves human-level reading comprehension." Right: "X matches annotator accuracy on a multiple-choice reading benchmark." [Lipton & Steinhardt]

### Title

- **The title names the contribution, not only the task.** It summarizes the abstract's main idea instead of listing modules. A `design` title says what method is used for what problem, an `evaluation` title reveals the evaluation perspective, and a `discovery` title makes the reader curious about the phenomenon. Wrong: "Calibration of Pruned Neural Networks". Right: "Pruning Breaks Calibration Before Accuracy". [Checklist] [Black] [Mensh & Kording]
- **Short and suggestive, not cute.** No marketing tone; a question works when the paper answers it. Preliminary work that should not overclaim can be a "Towards" paper; work that offers an insight or opens an area can be an "On" paper. [Black] [Freeman]
- **A method name that is short and distinctive.** Use an acronym that is pronounceable, lets the reader recover the words it came from, and is not a common word a search cannot find. [Black]

## By orientation

`proof` State what is proved, under which assumption, and in a clause why the assumption is needed (without it the general problem is impossible or ill-posed). Compare the result with the closest known one (a weaker assumption, a tighter bound, the first guarantee in a setting), name a property of the algorithm the theorem covers where it helps (such as its running time), and state why the theorem matters. [Checklist] [Lipton] [NeurIPS]

`effect` Name the trade-off on which the advantage holds, give one strongest number at a matched budget, and name the idea behind the number in one sentence. When the advantage is efficiency, give the cost axis (parameters, FLOPs, latency, labels). [Checklist]

`design` Name the bottleneck that makes the design necessary, state the design in one conceptual sentence that says why it addresses the gap, and name modules only through the principle that joins them. One number with its condition carries the evidence. [Checklist]

`evaluation` Say what is measured, why existing evaluation cannot measure it, the scale (tasks, examples, models evaluated) and one surprising result from existing models: the false conclusion the old evaluation supported, or a finding about a family of methods. Make clear that the new setting is more realistic, not only harder, and close on the guidance the results give to future methods. [Checklist]

`discovery` State the phenomenon, then the findings as contrastive statements ("X raises scores more often, yet breaks correct answers just as often"), one sentence per finding, never three layers of clauses. Name the kind of evidence (an intervention, a controlled comparison, a correlation across settings) and the range of settings in which the phenomenon holds. [Checklist] [Nanda] [Lipton & Steinhardt]; the contrastive form is a [practice default].

## Common mistakes

- **A number before its meaning.** A result given before the reader knows what it measures is the commonest fault of abstracts. Fix: put the evidence after the idea and the mechanism, and say what the number measures. [Mensh & Kording] [Nanda]

## Before moving on

- Does the abstract give context, gap, idea, mechanism, evidence and meaning, in that order or in an order the argument justifies, within about 200 words or the venue's limit?
- Could the first sentence open no other paper, and does the gap say what fails and where?
- Does the method sentence say why the method addresses the gap, and is every named component related to the others and to the gap?
- Is the strongest result there, with a number and its condition, after the reader knows what it measures?
- Could a reviewer write a three-to-five-sentence summary of the key ideas, experiments and significance from the abstract alone?
- Does every claim match the results in strength and scope, with any aspirational goal not claimed as reached and every untested explanation stated as a hypothesis?
- Is every term a cold reader needs either defined or avoided?
- Does the last sentence state what the result means, not a limitation?
- Does the title name the contribution and not only the task, with the same terms for it as the abstract and the introduction?
- Can a reader understand the paper from the title, the abstract and Figure 1?

## Sources for this section

- [Checklist] lars-contribution-centered-checklist.txt
- [Black] black-writing-a-good-scientific-paper.txt
- [Nanda] nanda-highly-opinionated-advice.txt
- [Lipton] lipton-heuristics-for-scientific-writing.txt
- [Lipton & Steinhardt] lipton-steinhardt-troubling-trends.txt
- [NeurIPS] neurips-paper-checklist.txt
- [Freeman] freeman-how-to-write-a-good-cvpr-submission.txt
- [刘知远] liuzhiyuan-nlp-paper-zhihu-summary.txt
- [Karpathy] karpathy-phd-survival-guide.txt
- [Mensh & Kording] general/mensh-kording-ten-simple-rules.txt
- [Ernst] general/ernst-how-to-write-a-technical-paper.txt
- [Peyton Jones] general/peyton-jones-how-to-write-a-great-research-paper.txt
