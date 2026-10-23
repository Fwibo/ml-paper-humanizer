# Experiments and results

One of the section files of [section-playbook.md](../section-playbook.md); read that index first for the orientation tags and the opening logic, then this file for the section being written. Sources are in [sources.md](sources.md).

## What this section does

The section says what was compared, gives the result that tests the main claim, and then answers in turn where the gain comes from, whether it is worth its cost, whether a simpler explanation would do and how far the result reaches. It carries the empirical layer: experiments that validate the main claim, isolate the key mechanism and rule out alternative explanations [Checklist].

The reviewer checks:
- a main result that validates the main claim;
- ablations that map to the contributions and motivations;
- a case study that makes the mechanism or design visible, and an efficiency analysis that says whether the gain is worth its cost;
- a likely concern answered in each subsection [Checklist];
- tables and figures readable from their captions, and the settings, error bars and compute the NeurIPS checklist asks for [刘知远] [NeurIPS].

## Frame

The section runs in four steps. Run-in headings, bold or `\paragraph` follow the venue template; the sequence does not [practice default].

1. **Setup.** What is compared, on what data, by which metric and against which baselines: a sentence or two, or a short block in the order datasets and metrics, baselines, settings [刘知远]. It gives the settings needed to read the results, including how the hyperparameters of the method and of the baselines were chosen, and points to the appendix for the rest [NeurIPS]. It does not restate the method or narrate the history of the benchmark.
2. **Main result (主实验, the main experiment).** The controlled comparison that tests the main claim on benchmarks the field accepts, with the claim's numbers and the conditions under which the method leads [刘知远]. It is not a row-by-row reading of the table.
3. **Further experiments (辅助实验, auxiliary experiments), each introduced by the question it answers.** An ablation by the contribution it tests, a case study by the mechanism it shows, an efficiency comparison by whether the gain is worth its cost, a matched-setting rerun by the confound it removes, a data-regime or robustness study by the scope it extends, an error analysis by the failure it locates [刘知远] [Checklist]. They come in the order of the doubts the main result raises, the most damaging first.
4. **Closing reading.** One sentence on what the results mean together, at the strength the evidence supports, or a short paragraph when the section has several results to read together. It adds no result and repeats no numbers.

The order departs when the argument gives a reason, and the reason is stated (in a skeleton, on its Frame line). A cost comparison may follow the main result directly when the main result raises it. A matched-setting rerun sits right after the comparison it corrects when the reported baseline numbers come from mixed settings. An error analysis may open on a case. An evaluation paper reads the overall results before the breakdown, and a discovery paper reproduces the phenomenon before it tests the mechanism (see By orientation).

## Rules

### Shape of the section

- **Give the section the space its evidence needs.** Most of an ML paper's words go to the experiments and results in full technical detail; budget two to three pages in an NLP conference paper [Nanda] [刘知远]. The space follows the evidence for the claims, not the effort the experiments took [Checklist].
- **Keep the parts balanced.** No results section with a single subsection, and no one-sentence block between paragraphs of eight; the subsection headings listed alone read as parts of one scope [Lipton].
- **Signpost by the question, not by a roadmap.** The opening sentence of each block names the question it answers; no paragraph announces what the section will do [Freeman] [Black].

### Setup and baselines

- **Name the metric in the body.** At least once, even in one sentence; a table note alone does not count [Lipton].
- **Start from the simplest baseline.** The first baseline is the simplest method that could solve the problem, and no inconvenient baseline is left out [Black] [Karpathy] [practice default].
- **Tune the baselines as hard as the method, and say so.** Tuning covers hyperparameters, prompting and scaffolding [Nanda] [Lipton & Steinhardt]. Write how each baseline was configured and with what budget.
  Wrong: "Baselines use the hyperparameters reported in their papers." Right: "Each baseline receives the same 30-trial search over learning rate and warm-up as our method (Appendix C)."
- **Show that the method beats the plausible alternative, not that it is decent.** Compare against what the reader would otherwise use, at matched budget [Nanda].

### The main result

- **Make the main experiment a controlled test of the paper's own claim.** The method against the same pipeline without it, everything else held fixed, on the benchmarks and protocols the field accepts [刘知远] [Karpathy]. It need not beat the strongest system in the field; claim state of the art only where the table shows it [刘知远].
- `effect` `design` **Say in the main-result paragraph where and why the method leads.** After the opening pointer and claim, the paragraph says under which conditions the method is best, why the advantage arises and what practical problem it solves [Black]. Name the trade-off the contribution is about before the numbers; where the paper does not lead on the usual headline metric, say which evaluation dimension, setting or comparison basis it wins on, and still report the headline metric [Checklist].
  Wrong: "Our method achieves the best result in 5 of 7 columns." Right: "At matched FLOPs our method has the lowest error on every task; without the budget match it trails the largest baseline by 0.3 points on two of them."
- **A numbered list of observations is a format; its first item is the main conclusion.** Each item (1), (2), (3) is a claim about the comparison, not a reading of a cell [刘知远].

### Further experiments

- **Give every experiment a question it answers for the argument.** State the question, or the claim tested, before the result (claim-strength.md) [Checklist]. Each subsection has an answer to what would be lost if it were cut; an experiment whose question the reader cannot name goes to the appendix [Karpathy] [Nanda].
  Wrong: "We also evaluate on WikiText." Right: "To check that the gain is not specific to code, we repeat the comparison on WikiText."
- **Match the introduction's claims to the experiments.** The challenges the introduction names, the ideas that answer them, the method's components and the experiments correspond; one experiment may test two claims, but no contribution lacks an experiment and no experiment lacks a claim [刘知远] [Checklist] [Karpathy]. Forward-reference each claim's evidence from the claim [Peyton Jones].
- **Order the results by the logic that carries the claim, not by the order the experiments were run.** Blocks may follow the conditions the method faces (small blurs, large blurs, saturated images) [Karpathy] [Mensh & Kording] [Ernst] [Freeman].
- **Head each results block with what it shows.** Where results carry subsection or run-in headings, each is a short declarative sentence of the finding, so that the headings alone read as the sequence of findings [Mensh & Kording] [exemplars].
  Wrong: "Effect of window size." Right: "Wider windows help only beyond 8k tokens."
- **Lead with the decisive experiment.** A decisive experiment is one whose outcome would differ depending on which hypothesis is true. Prefer evidence of different kinds (a matched comparison, an ablation, an intervention, a case) over more of the same kind. Write the decisive one first, say what each further one adds, and move the weaker ones to the appendix or a brief mention [Nanda].
- **Choose each further experiment for the contribution.** Design each sensitivity study, ablation, data-regime study, error analysis or case study for what the contribution needs to show, not because papers usually have one [刘知远].
- **Change one thing at a time.** An ablation removes one change, reports its effect, then the next; it never changes the method and the data together [Black] [Nanda].
- **Identify the source of the gain.** When several changes together produce a gain, say which of them are necessary. Ablation is one route; robustness checks across hyperparameters and datasets, and error analysis, are others [Lipton & Steinhardt].
- `effect` `design` **Write an ablation as a question and its answer.** Say what question each component answers and what the answer is, with the number the outline attaches to it, and tie it back to the claim the component serves [Checklist].
  Wrong: "Without the router, accuracy drops by 2.1; without the cache, by 1.4." Right: "The router carries most of the gain on long inputs: removing it costs 2.1 points, against 1.4 for the cache."
- **Answer the likely doubt where it arises.** A surprising result, including one far from prior work, names the likeliest alternative explanation in the same subsection and the experiment that rules it out [Lipton] [Freeman]. If the authors do not know whether the method works only because of X, and "no" would be damning, the experiment is run [Lipton]. A control-condition sentence from an award paper: "This implies that the loss in performance for Sharded is not explained by potential loss of information in sharded instructions, as such a loss would be reflected in lower Concat performance." (arXiv 2505.06120) [exemplars]
- **Put each experiment's technique next to its result.** When the evidence for a claim uses its own technique, explain the technique where the result is read, not in a methods block pages earlier; when the experiments use different techniques, each kind of evidence may take its own subsection [Nanda].
- **Close the loop on the motivating case.** If the introduction opened on a concrete problem, the experiments return to it; a contrived problem alone does not answer it [Lipton] [Freeman].

### Paragraphs and numbers

- **Open each results paragraph on the pointer and the claim.** One sentence carries both ("Table 2 shows that the gate lowers perplexity by 0.2 at every size"), or the paragraph opens on the question it answers ("To check that the gain is not an artefact of the tokenizer, …") and gives the answer as its last sentence; row readings come after the claim. The pointer has the figure as its subject ("Figure 4 shows"), not the authors ("In Figure 4 we show") [Black] [Karpathy] [Mensh & Kording]. A results subsection may open on a whether-question ("We first check whether …") or a five-word pointer sentence, not on a hypothesis restated from the lead-in or a stakes frame ("This would be a poor trade if …") [practice default].
- **Land every paragraph on a result or a hedged reading.** The last sentence is a result or a hedged mechanism sentence about this paragraph's evidence ("…, suggesting that …"), not a row-by-row reading of the table and not a derived takeaway that the next paragraph picks up [Nanda] [Mensh & Kording] [practice default]. Plan each paragraph's opening and closing sentences first [Nanda].
- **Keep the claim's numbers, and leave the rest in the table.** Keep every number the outline attaches to a claim (a setting, a margin, a count, a row value); never "roughly doubles" with no figure, or "in every column but one" with no value. Read out a number already in a table only when the sentence makes a claim about it; the text adds the reading, not a copy of the table [Ernst] [Black] [practice default].
- **Read the table as the authors would.** Name the comparison that matters, not the table geometry ("in every column but one", "the cells in the third block"). Every comparative names what it is compared with: "more accurate" becomes "more accurate than the strongest baseline" [Black] [practice default].
- **Say what the numbers mean, not only what they are.** The text says how the experiments validate the claims and what they reveal about what each method does differently, not only who wins [Black].
- **Keep tested explanations apart from intuitions.** An account of why the method wins that no experiment in the paper tests is labelled as an intuition or a conjecture, or kept in a clearly marked place. Test: would you rely on it to predict a result [Lipton & Steinhardt]?
  Wrong: "The gain arises because the gate removes internal noise." Right: "One reading is that the gate removes noisy tokens; Section 5.2 tests a prediction of this reading."

### Figures, tables and captions

- **Write the caption so that a reader who skipped the body can read the figure.** In one to three plain sentences the caption says what the table or figure shows, what the reader is to see in it, and whether higher or lower is better when the figure does not [Lipton] [刘知远] [Freeman] [Black]. The row readings and the numbers stay in the body, not in a bold sentence in the caption. Symbols, colours and column names get a caption sentence where the figure does not explain them; a clear legend or label in the figure is better [Black] [Nanda] [Ernst].
  Wrong: "Table 3: Results on long-context benchmarks." Right: "Table 3: Accuracy on four long-context benchmarks at matched compute (higher is better). The gap to the baselines grows with input length."
- **Let the figures and the text each stand on their own.** The figures and captions alone give the main results, the text alone gives every critical observation, and captions are not giant paragraphs [Lipton] [Black].
- **Design each figure around its takeaway.** Decide what the reader should take from the figure before choosing the plot, and emphasise the line or region that matters. Label axes with units, keep text readable without zooming, and do not let red against green carry key information [Nanda] [Black].
- **Refer to every figure and table in the text.** Results in the appendix or supplementary material are pointed to from the body [Black].
- **Bold marks the best result in each column.** One table style holds across the section [刘知远]. Bold goes to the best number whichever row holds it, and a bold baseline cell is named in the text [practice default].

### Statistics, reproducibility and cost

- **Report variance, number of seeds and significance.** A single-run number is not written as a fact. Give error bars, confidence intervals or tests at least for the results behind the main claims, and say what the bars capture (seeds, splits, initialisation), how they were computed and whether they are standard deviations or standard errors; no symmetric bars that run outside the valid range [NeurIPS]. Say whether the result is clearly distinguishable from noise; a central finding resting on a p-value just under .05 is fragile [Nanda].
- **Report the digits the measurement reproduces, and keep relative and absolute apart.** Use the same number of digits down a column. A rise from 25% to 30% is 5 percentage points or 20%, not 5%; "half as many", not "2 times fewer"; "3 times as fast" is not "3 times faster" [Ernst] [exemplars].
- **Give enough detail to rerun every experiment.** The settings needed to read the results are in the body; data splits, hyperparameters and how they were chosen, and the full setup are in the appendix, with one sentence pointing there [NeurIPS]. Say how the main results can be reproduced (code and data with the command to run, a released checkpoint, or instructions), and which experiments that covers if only some [NeurIPS] [Nanda].
- **Report the compute.** For each experiment, the type of hardware, the memory and the time per run, an estimate of the total, and whether the project used more compute than the reported runs [NeurIPS].

### Honesty and scope

- **Write the results to test the claim, not to sell it.** No "showcase"; promise only what the experiments deliver, and inform rather than persuade [Black] [Freeman] [Nanda].
- **Report weak and negative results at their size.** Write small positive gain for a small positive gain and mostly variation for a difference within noise; do not write no gain, fails or only [practice default]. Report what did not work, even before knowing why [Freeman] [Lipton & Steinhardt].
- **Show where the method fails.** Say which factors lower its performance (input length, resolution, domain) and show failure cases [NeurIPS] [Black].
- **Say how each example was chosen.** For a qualitative example, say whether it was drawn at random or picked, and from how many. A picked example is written as an illustration of the phenomenon, not as evidence of how often it occurs; add randomly drawn examples beside it; only an existence claim can rest on one example [Nanda]. Supplementary results include ones that are clearly not the picked one [Black].
- **Say which analyses were fixed before the results were seen.** A post-hoc reading is written as a reading ("suggests", "is consistent with"), not as a confirmed prediction [Nanda].
- **Scope each claim where it is made.** The claims in the abstract and introduction say how far the results generalize, and a claim tested on few datasets or few runs says so where it is made [NeurIPS]. No sentence a reviewer could falsify by naming one dataset [Lipton].
  Wrong: "Our method outperforms prior work on most datasets." Right: "Our method outperforms the three baselines on 9 of the 12 datasets we test."
- **Say which kind of generalization a result shows.** Name the one measured: train to test, one population to another, or benchmark to real use. Qualify "human-level" to the task and data [Lipton & Steinhardt].
  Wrong: "The model generalizes to new domains." Right: "Trained on news text, the model keeps 92% of its in-domain F1 on two held-out forum datasets."

## By orientation

`proof` The experiments test what the theory predicts; open them by saying so [exemplars]. The setup says which prediction each experiment checks (how a quantity scales, where a transition falls, what happens at the boundary of an assumption), and the result says whether the measurement behaves as the theorem says, including where its assumptions do not hold. Say which part is proved and which is measured; a theorem whose conclusion does not support the empirical claim does not stand beside it [Lipton & Steinhardt]. For a synthetic setting, one sentence says why it isolates the assumption and how it connects to the problem that motivated the theory [Checklist].

`effect` Make one trade-off visible and credible. Configure strong baselines fairly at matched budget, report the cost metrics that matter (parameters, FLOPs, latency, memory, tokens, labels, human effort) and say whether the gain is worth the cost. Rule out a larger model, more data, longer training or a stronger prompt, use the ablations to explain why the effect occurs, and give the advantage one figure that makes it memorable [Checklist].

`design` Use the ablations to test the necessity of each key design, each tied back to the claim and the bottleneck it answers, and a case study to show how the design works inside [Checklist].

`evaluation` Report the overall performance of existing models first, then break it down by difficulty or category, and use the last paragraph to say what these numbers mean for method design; do not read out scores model by model or cell by cell. Show that the new setting is more realistic and more meaningful, not only harder, for instance by the false conclusion the old protocol leads to. Draw insights about method families, organise the metrics around one central question, and end on guidance for future methods [Checklist]. A careful look at what an existing benchmark actually tests can itself be the finding [Lipton & Steinhardt].

`discovery` Reproduce the phenomenon clearly before analysing it, and show that it holds beyond one narrow setting. Write findings paragraphs as observation, analysis, conclusion, with short declarative run-in headings. Give the explanation a causal chain with no missing link: isolate variables, rule out alternative explanations, and run an intervention or counterfactual that changes the proposed cause and shows that the outcome changes; do not write correlation as causation [Checklist]. Write an unsettled explanation as a hedged reading (suggests, may, is likely, "We hypothesize that") and word it the same way throughout, without making "We conjecture:" the frame of every section [Lipton & Steinhardt] [practice default]. The analysis subsections that follow the results have their own file, analysis.md.

## Common mistakes

Every common mistake of this section is the negation of a rule above; the Wrong lines show them.

## Before moving on

- Does the main result test the main claim as a controlled comparison on benchmarks the field accepts? [Checklist] [刘知远]
- Does every claim of the introduction have its experiment here, every experiment a claim, and every ablation a contribution it tests? [刘知远] [Karpathy] [Checklist]
- Does each block open on the question or doubt it answers, in the order of the doubts the main result raises? [Checklist] [Lipton]
- Is there a case study that makes the mechanism or design visible, and an efficiency analysis that says whether the gain is worth its cost? [Checklist]
- Is the metric named in the body, the simplest baseline included, and every baseline tuned with the method's budget, with the text saying so? [Lipton] [Black] [Nanda]
- Can a reader say what the important thing was, and could a reviewer write the summary of the experimental validation from this section alone? [Black]
- Can each table and figure be read from its caption alone, and is each one cited in the text? [刘知远] [Black]
- Do the results behind the main claims carry error bars or tests, with what they capture stated, and are the full settings, hyperparameter choices, compute and a reproduction path given? [NeurIPS]
- Do the claims here and in the abstract and introduction match how far the results generalize, with weak results, negative results and failure cases reported at their size? [NeurIPS] [Freeman]
- Is every example's selection stated, every post-hoc analysis marked, and every explanation of a gain tested here or labelled as a conjecture? [Nanda] [Lipton & Steinhardt]

## Sources for this section

- [Checklist] lars-contribution-centered-checklist.txt
- [Black] black-writing-a-good-scientific-paper.txt
- [Freeman] freeman-how-to-write-a-good-cvpr-submission.txt
- [刘知远] liuzhiyuan-nlp-paper-zhihu-summary.txt
- [Nanda] nanda-highly-opinionated-advice.txt
- [Lipton] lipton-heuristics-for-scientific-writing.txt
- [Lipton & Steinhardt] lipton-steinhardt-troubling-trends.txt
- [NeurIPS] neurips-paper-checklist.txt
- [Karpathy] karpathy-phd-survival-guide.txt
- [Mensh & Kording] mensh-kording-ten-simple-rules.txt
- [Ernst] ernst-how-to-write-a-technical-paper.txt
- [Peyton Jones] peyton-jones-how-to-write-a-great-research-paper.txt
- [exemplars] references/exemplars/
