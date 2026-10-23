# What the chain check looks for

The hard lines are in [SKILL.md](../SKILL.md): no invented fact, no changed number or name, no claim beyond its evidence, nothing removed without the author. Everything here is a default: what the field's writing guides agree a reader needs, applied unless the argument gives a reason to depart, in which case the reason goes into the skeleton (a Frame line, a Hands off, a Keep). A default applied on a schedule becomes a template; the check asks whether the reader is served, not whether the pattern was followed.

## The spine

- A contribution sentence that only names a method ("we propose X and it works better"), when the material shows a conceptual or empirical layer it leaves out. A layer the material does not show is marked, not demanded.
- A contribution item that cannot be refuted ("we describe a system") or that no section carries; more items than the main line has parts.
- A section whose `Carries` line names no part of the contribution.

## The chain

- A paragraph whose question nothing before it raised; a conclusion whose premise is in no earlier line and in no named evidence.
- A paragraph that ends on a derived takeaway the next paragraph restates, instead of the fact or the open question it draws the takeaway from.
- A note that reads as a paragraph of the paper (declarative sentences in the paper's voice, no imperative, no verb and scope in parentheses). The humanizer would paraphrase it; the note is rewritten as instructions to the writer.
- A note missing one of its five parts: the question, the claim with verb and scope, the evidence with status, what it does not say, the ending.
- A paragraph the argument would not miss. Default: it goes to the appendix or is cut. Reasons to keep it: it introduces a concept a later line needs, or states a condition the reader must hold; then its note says so.
- An introduction paragraph that closes on a conclusion where the next paragraph needs an open question. Default: the paragraph ends on what is still unknown at its level. Reasons to depart: a background paragraph that only sets up a concept, or the last paragraph, which states the contributions.
- The introduction's account of the method repeated, rather than detailed, in the method section.

## Correspondence across sections

The gaps the introduction names, the answers to them, the parts of the paper that realize the answers and the experiments that test the claims answer to one another. The columns take the orientation's names: for `design` and `effect` challenge, idea, component of the method; for `evaluation` the realistic factor missed, the construction principle, the construction element; for `discovery` the link of the chain, the hypothesis part, the measurement or intervention; for `proof` the obstruction, the assumption, the lemma or construction. The example below is a design paper. The check is for completeness of the correspondence, not for equal counts: one idea may answer two challenges, several components may serve one bottleneck, one experiment may test two claims, and one claim may need several experiments of different kinds. The finding is an item with no partner that the material cannot explain.

| Challenge (introduction) | Idea | Component (method) | Claim tested | Experiment |
|---|---|---|---|---|
| top-k chunks repeat one fact | judge a chunk by what it adds to the chunks already selected | diversity scorer | removing the scorer lowers F1 | Table 3, scorer row |
| the facts a question needs are spread over its sub-questions | split the budget per sub-question | budget allocator | removing the allocator lowers F1 | Table 3, allocator row |
| (none named) | (none) | evidence verifier | removing it lowers F1 by 0.4 | Table 3, verifier row |
| both | both | both | CoRe raises F1 over four baselines | Table 2; Figure 3 for the cost |

The third row is the finding: a component with no challenge before it. The last row is not a finding: one experiment tests the claim that both ideas together make. The question to the author is whether the verifier answers a challenge the introduction should name, or is a detail of the method that the contribution does not rest on.

## Evidence and claims

- An experiment with no question in the argument; a question in the argument with no experiment; a main result that does not test the main claim.
- Many similar experiments where one decisive one, or several of different kinds, would carry the claim.
- A claim without its condition; a verb above its evidence (demonstrates on a correlation); a verb below what the evidence, read with its controls, supports.
- A systematic claim on one example, or an example written as a trend; a planned experiment written as a finding.
- A design intent standing where an outcome should be; correlation written as cause; a mechanism claim with no intervention or controlled comparison behind it. These are recorded as doubts with the claims they touch; the skeleton writes the claim at the strength the evidence supports and does not repair the science.
- A number in the abstract or introduction that the reader has no reason to remember. Default: the abstract and introduction keep the numbers that surprise; a number that sets a condition (a budget, a scale) is kept for that reason.

## Names and sections

- One object under two names across sections; a gap, a bottleneck and an ablated component that are not the same thing under the same name.
- A section doing another's job: an introduction that runs ahead into the findings, a conclusion that adds a result or ends on a new limitation, a limitation that retracts a conclusion instead of bounding it.

## A reverse outline with a missing link

A four-paragraph results draft, as it stands. The current skeleton records what each paragraph does, improving nothing:

```markdown
### P1 setup
Tell what is compared and on what: the gate and the no-gate model on three benchmarks by perplexity (provided; Table 2 setup). Ends on perplexity at each size as the quantity to read.

### P2 main result
Does the gate lower perplexity: by 0.2 at every size (shows; provided, Table 2). Ends on the gain being uniform across sizes.

### P3 mechanism
[no question found] The gate removes distractor tokens, which is why perplexity falls (demonstrates; evidence not identified in the supplied material). Ends on the gate as the component to keep.

### P4 ablation
Which component carries the gain: removing the gate loses the whole 0.2 (shows; provided, Table 3). Ends on nothing.
```

Proposed:

```markdown
### P1 setup (P1)
unchanged

### P2 main result (P2)
unchanged, except the ending: end on the gain being uniform across sizes and on which component carries it being open.

### P3 ablation (P4 → P3)
Answer which component carries the gain: removing the gate loses the whole 0.2 (shows; provided, Table 3). End on the gate carrying the gain and on why it does being open.

### P4 mechanism (P3 → P4)
Answer why the gate lowers perplexity, at the strength the material allows: the gate is designed to drop distractor tokens, and the ablation is consistent with its doing so (is consistent with; Table 3). Keep design intent and outcome in separate clauses. Do not write that it drops them: no count of dropped distractors is in the material [?]. End on the gate as the component to keep.
```

Change list: P4 → P3, because P3's question (why) needs P4's answer (which component) first; P3 → P4, verb lowered from "demonstrates" to "is consistent with", since no measurement of distractor tokens is in the material; design intent and outcome split into two clauses. Open question, blocking: is there a measurement of distractor tokens dropped (affects P4's verb)? Nothing was removed; nothing was added.
