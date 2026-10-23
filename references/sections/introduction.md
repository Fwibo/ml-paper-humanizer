# Introduction

One of the section files of [section-playbook.md](../section-playbook.md); read that index first for the orientation tags and the opening logic, then this file for the section being written. Sources are in [sources.md](sources.md).

## What this section does

The introduction is an extended abstract of about a page: it states the key claims, motivates them, places them in the literature that matters and summarizes the evidence, so that a reader who stops there knows the paper's narrative, what is new and what is not, and its implications [Nanda] [Freeman] [刘知远]. The reviewer checks that:
- it moves from background to gap to what the paper does, in the steps its orientation asks for (Frame) [Checklist];
- the gap is structural and what the paper does follows from it: for `design` and `effect` an insight paragraph comes before the method, for `discovery` the phenomenon before its explanation, for `evaluation` the mismatch before the construction, for `proof` the obstruction before the assumptions [Checklist];
- the contributions match the gap and the experiments [Checklist];
- the claims match the contributions and their scope, with the important assumptions and limitations [NeurIPS];
- the nearest prior work is named and the difference from it is stated [Freeman] [Black].

## Frame

Three moves hold for every orientation: establish the territory (the task or object, why it matters, and the existing approaches, evaluations or explanations), open the gap (what they leave unsolved and why the first remedy a reader would reach for does not close it), and fill it (what this paper does, the evidence, what it changes, the contributions) [Swales] [Black] [刘知远]. The rhythm is goal, problem, solution [Black]. A step is usually a paragraph; the first paragraph holds the background and the existing work, and two short steps may share a paragraph. What fills the three moves differs by orientation; the four lists below give the steps, and the skeleton's Frame line names the list followed and any departure with its reason. Swales's third move ends with a paragraph on the article's structure; that step is left out [Swales] [Black] [刘知远].

### `design` `effect`: the method story

**1. Background and existing approaches.** The task, why it matters, and the strongest, most representative existing methods (the ones the paper sets out to improve), narrowing to the problem hidden in them [Nanda] [刘知远] [Karpathy]. It carries no data and does not answer the question it raises.

**2. The limitation.** The key challenge the existing approaches leave, structural and stated fairly; the challenges it names are exactly the ones the paper answers later [Checklist] [刘知远] [Karpathy]. For `effect`, the limitation is where existing methods sit on the single trade-off that matters [Checklist]. It ends on what remains unsolved, not on the answer.

**3. Why the obvious fix does not remove it.** The remedy a reader would reach for first (more data, a larger model, a known correction) and the reason it leaves the limitation in place [Black]. The fix is not dismissed without a reason or a citation.

**4. The insight.** The way of seeing the problem that makes it solvable [Black] [Checklist]. A small example, or Figure 1, can carry it alongside the text [Freeman] [刘知远]. It is not a list of what was built.

**5. The solution.** The method as what the insight suggests: its core idea and why that idea removes the limitation [Checklist]. For `design`, the design principle in one conceptual sentence, with each module named only as the answer to a bottleneck; for `effect`, the idea that produces the gain [Checklist]. When the solution leaves a second obstacle, the paragraph names it and the further step that removes it [Black]. No implementation or hyperparameters.

**6. The evidence and what it changes.** The most critical evidence for the main claim, then its implications: what the reader should now believe or do differently, which misconception it corrects [Nanda] [Freeman] [Lipton]. For `effect`, it says that the comparison is budget-matched, which simpler explanations it rules out, and the cost where it matters [Checklist]. It does not report every experiment.

**7. The contributions.** A short list of refutable claims, each pointing to the section that carries its evidence [Black] [刘知远] [Peyton Jones].

### `discovery`: the phenomenon and its explanation

**1. Background.** The setting in which the phenomenon arises, why that setting matters, and the practice or line of work it concerns [Checklist] [exemplars 2510.04212, 2503.14858]. No data, no answer.

**2. The phenomenon.** Shown clearly before any analysis: what is observed, in which settings, and the question it raises; a reproducible case the community already knows is the strongest form [Checklist] [exemplars 2510.04212, 2505.17638]. It states the observation, not its cause.

**3. Why the existing explanations fall short.** Each explanation named fairly with what it accounts for, then the observation it cannot account for (the transition persists when every known regularizer is present; a model can be coerced to output almost any string, so generation does not prove memorization) [Checklist] [exemplars 2505.17638, 2505.24832]. It ends on the open question.

**4. The hypothesis and how it is tested.** The proposed mechanism, or the question made operational: the quantity measured, the controlled setting that isolates it, the intervention that would change the outcome if the mechanism is right [Checklist] [Nanda] [exemplars 2505.24832, 2504.13837]. This is the counterpart of the insight: it says how the question becomes answerable, not what was found.

**5. The findings.** One claim per paragraph or item, in the order of the chain, each with a conclusion sentence and an evidence sentence, at the strength the evidence reaches (an existence proof, a systematic finding, a hedged one) and with the number of settings it holds in [Nanda] [Checklist] [exemplars 2504.13837, 2505.24832]. No mechanical numbering (At the first / At the second).

**6. The test that settles it.** The intervention or control that changes the proposed cause and with it the outcome, and the alternative explanations it rules out [Checklist]. When the paper also offers a fix, it appears here as what the mechanism predicts should work, and its success as confirmation of the mechanism (a minimal change to the rounding that removes the bias; an inference order that sidesteps the subproblems found to be hard), not as the contribution the introduction sells [exemplars 2510.04212, 2502.06768].

**7. Implications and contributions.** What the reader should now believe or do differently; then the items: the framework or protocol, the findings, the improvement or implication [Nanda] [Checklist]. A fix the paper offers is listed as the improvement the mechanism points to, after the findings, not as a method of its own.

### `evaluation`: the mismatch and the new measurement

**1. Background.** How the systems are used, in deployment or in scientific use, and how they are evaluated today [exemplars 2505.06120, 2406.04327]. No data.

**2. The mismatch.** The realistic factor current evaluation misses and the false conclusion it can lead to, in terms the owners of the current evaluation would accept [Checklist]. It ends on the gap.

**3. Why the nearest attempts do not close it.** The benchmarks or protocols closest to the new one and what each still lacks: it is harder but not more realistic, it measures an architecture rather than a model, it rests on an untested assumption [Checklist] [exemplars 2505.06120, 2406.04327].

**4. The new evaluation as the response.** The construction principle in one sentence and the key terms defined; then the principles of split, metric, data source and task construction, a sentence each with forward references, each justified by the realistic factor it restores [Checklist]. The scale (tasks, examples, models) where it sets a condition.

**5. What the evaluation reveals.** The headline result about existing models or method families, stated as the false conclusion corrected, with the strongest number and its condition [Checklist] [exemplars 2505.06120, 2504.13837]. Not who wins.

**6. Why.** The decomposition of the result or the explanations examined, where the paper has them [exemplars 2505.06120]. Optional.

**7. Implications and contributions.** The gap between use and evaluation now shown; the guidance for future methods; then the items: the resource, the protocol, the findings [Checklist].

### `proof`: the obstruction and the theorem

**1. Background.** The object and the line of theory about it, with the results known so far [exemplars 2510.19315, 2605.00768].

**2. The obstruction or the puzzle.** Why the fully general problem is impossible or ill-posed (a counterexample, an information-theoretic obstruction), or the observation that known results cannot explain (a restriction that should weaken a model yet improves it) [Checklist] [exemplars 2605.00768]. Not the theorem.

**3. Why existing results do not settle it.** What the closest results prove and the question each leaves open [Checklist] [exemplars 2402.09963].

**4. The assumptions and the lens.** The assumptions that remove the obstruction, each with a simple example of what it means (which objects, which observations, which algorithm), and why the algorithm or relaxation is natural, ideally derived from an ideal but intractable objective [Checklist].

**5. The main result, informally.** Stated with its assumptions named, compared with the closest known theorems, and tied back to the motivating problem [Checklist] [NeurIPS]. The full statement waits for the body.

**6. Consequences.** What the theorem explains or predicts about the motivating problem, and the empirical check where there is one [exemplars 2402.09963, 2605.00768].

**7. Contributions.** The assumptions and why they are needed, the main theorem, its comparison with the closest known theorems [Checklist].

**Departures and mixed papers.** Departures need a reason the argument gives. A paper with two or three claims gives each a short paragraph of claim and evidence before the contributions [Nanda]. A paper with a secondary orientation (skeleton header) follows the primary list and takes from the secondary list the step where that contribution sits: a discovery paper that also proposes a fix puts the fix in its step 6; a design paper with a finding puts the finding in its step 6 with the test behind it. A paper that builds directly on one prior work gives that work its own sentences: what it showed and what this paper adds [Nanda]. The form may vary (a dialogue, a question-and-answer, a run of bold findings) provided every step of the list is still made [Karpathy].

## Rules

### The whole introduction

- **Goal, problem, solution.** Make the reader want the goal by saying why it matters, take it away with the obstacle, then give it back with the idea; when the idea leaves a second obstacle, run the cycle again. [Black]
- **Order it as you would teach it.** Order the introduction as you would explain the work in a talk or at a whiteboard: what the listener needs first to understand the contribution, then what they would ask next. [Black]
- **One contribution.** The paper sells a single thing that was not obvious before. State it in one sentence before writing; a second, unrelated contribution goes to the body or to another paper. [Karpathy] [Black] [Checklist]
- **Every gap the introduction names has its answer.** `design` `effect` Each challenge named corresponds to an idea that answers it, a component of the method and an experiment that tests it; one idea may answer two challenges, but no challenge and no component is left without a partner [刘知远] [Karpathy] [Checklist]. `evaluation` Each realistic factor named is matched by a construction principle and by a result that shows the factor matters [Checklist]. `discovery` Each link of the proposed chain is matched by a finding and by the test behind it [Checklist]. `proof` Each assumption named is matched by the obstruction it removes [Checklist]. No gap is named that the paper does not address.
- **Reach the contribution early.** Most of the introduction, counted in paragraphs, says what this paper does. One paragraph of background is the default for an established task, and the gap arrives by the second paragraph. [Lipton] [刘知远] [Black]
- **About one page.** A literature review or a method description that makes it longer belongs in another section. [刘知远] [Karpathy] [Peyton Jones]
- **Say what is new and what is not.** Make clear which parts are this paper's and which come from prior work. Cite the three to five nearest works and say the exact point where this work differs from each. Wrong: "We propose a new contrastive objective for pruning." Right: "We keep the contrastive objective of [cite] and change what it contrasts: dense against pruned outputs instead of two augmentations." [Freeman] [Nanda] [Black] [Checklist]
- **Describe prior work so its authors would agree.** State precisely what it gets right, then what it leaves open, and keep criticism on the method, never on its authors. Wrong: "Existing methods fail to handle long contexts." Right: "Sliding-window attention [cite] keeps memory linear in length but cannot attend to tokens outside its window." [刘知远] [Nanda] [Black] [Freeman]
- **The strongest alternative is the foil.** Measure the paper against the best and most representative alternative, the one a reviewer would name: for `design` and `effect` the strongest existing method [刘知远] [Freeman]; for `evaluation` the benchmark or protocol the field relies on; for `discovery` the accepted explanation; for `proof` the closest known theorem [Checklist].
- **Cite each step of the argument.** Give at least one citation for each step of an important argument (that the problem is real, that it matters, that others have tried), and cite methods the paper builds on where they are used, not only in the related work. Cite for context, not for coverage. [Nanda] [Lipton]
- **Define what the claims need.** Define the key terms and concepts behind the claims in the introduction, before their first use. [Nanda] [刘知远]
- **Claims as strong as the evidence, and no stronger.** Scope each claim to the settings where it was shown and phrase it at the strength the evidence reaches (an existence proof, a systematic finding, a hedged one, a narrow one). Do not underclaim either. [Nanda] [NeurIPS] [Freeman] [Black]
- **Mark speculation, aspirations and open problems.** Label an intuition the paper does not test as one, or keep it in a clearly marked passage. An aspirational goal may motivate the work if the text makes clear the paper does not reach it, and the introduction says plainly which problems remain open. Name components by what they compute, not after a human faculty. Wrong: "Models fail here because they lack a world model." Right: "One possible cause is the lack of a world model, which this paper does not test." [Lipton & Steinhardt] [NeurIPS]
- `design` `effect` **Say where the gain comes from.** When the method makes several changes, name the change that carries the gain, and present a change as necessary only where the ablations show it. [Lipton & Steinhardt]
- **Teach the argument; do not log the project.** Write around the problem clarified or the gap filled, by the most direct route to the idea, not the chronology of what was tried. [Karpathy] [Checklist] [Peyton Jones]
- **Name kinds, not instances.** Do not name specific datasets, model versions or hyperparameters. Say which kind of dataset and which kind of model, and keep the citations. The name of a method the argument turns on (the baseline whose shortfall motivates the paper) is kept, with its citation. Wrong: "On HotpotQA with Llama-3-8B at learning rate 2e-5, …". Right: "On multi-hop question answering with an open 8B model [cite], …". [practice default]
- **One vocabulary for the contribution.** The contribution keeps the same name and terms in the title, abstract, introduction, related work, method and experiments. [Checklist] [Mensh & Kording]
- **Answer the first doubt in passing.** Answer the likeliest reviewer objection in the evidence paragraph by naming the control that rules it out: for `design` and `effect` that the gain comes from more compute or appears in one setting; for `discovery` that the link is a correlation or holds in one narrow setting; for `evaluation` that the new setting is only harder; for `proof` that the assumptions were chosen to make the proof go through. [Lipton] [Checklist]
- **No roadmap paragraph.** Do not close with a roadmap paragraph ("The rest of this paper is organized as follows") or a hand-off sentence unless the paper's outline asks for one; forward references from the contributions do its job. [Black] [刘知远] [Peyton Jones]

### The opening paragraph

- **Narrow from the field to the hidden problem.** Run from broad background, to narrow background (optional), to the task at hand, to how existing methods, evaluations or explanations handle it, to the problem hidden in them, narrowing the gap at each step until it is the one this paper fills. [刘知远] [Karpathy] [Mensh & Kording]
- **A first sentence that belongs to this paper.** If it could open any paper in ML, delete it. It names the topic and says something true and uncontroversial about it. Wrong: "In recent years, deep learning has achieved great success in many areas." Right: "Pruning removes most of a network's weights so that it fits on a phone." [Lipton] [Nanda]
- **Plain first sentence, technical second.** Make the first sentence plain, complete and uncompressed. Let the second sentence tighten to technical content. [practice default]
- **Why it matters and why it is unsolved.** Write why the problem matters and why it is unsolved, never what the authors are interested in or want. Wrong: "We are interested in making pruned models reliable." Right: "Pruned models run on devices where no larger model checks their errors, so an overconfident mistake goes uncaught." [Black]
- **Argue importance only as far as needed.** An established task gets a sentence on why it matters; a new task gets enough argument that the reader accepts it as a task worth solving. [刘知远]
- **A concrete case before the abstract problem.** Show a specific failure the reader can picture instead of repeating that the problem is important; the experiments can return to the same case. [Lipton] [Peyton Jones]
- **End on the existence of the problem.** Let the last sentence only show that the problem exists ("… remains poorly understood", "… remains open"). Do not write "this paper answers the question". [Mensh & Kording] [exemplars]
- **Do not answer the question yet.** Do not answer the paper's open question inside the first paragraph, not even as a hint ("…, which we trace to X"). The answer comes in the insight, hypothesis or construction paragraph. [practice default]
- **No data.** Put no data in the first paragraph; the numbers come with the evidence. The account of how existing work operates may plant the hidden flaw that later text develops. [practice default]

### The middle paragraphs

- **One point per paragraph, stated first.** Each paragraph is organized around a single point given in its first sentence and supported by the rest. Plan each paragraph's opening and closing sentence before its body. [Karpathy] [Nanda]
- **Open on the end of the paragraph before.** Let each paragraph's first sentence catch the end of the one before. If the previous paragraph ends on why X remains unclear, this one opens with "To study this question, we …". [practice default]
- **Close on a fact, a result or an open question.** Each paragraph before the insight, hypothesis or construction lands on what is still unknown at its level, which the next paragraph takes up. End each paragraph on a fact or a result, not on a derived takeaway that the next paragraph picks up ("The bottleneck is thus X." followed by "To remove this bottleneck, …"). Picking up an open question that the previous paragraph stated as a fact is fine; picking up a "thus" conclusion is the template. [Mensh & Kording] [exemplars] for the landing on the unknown; the ban on the "thus" hand-off is a [practice default].
- **Each paragraph keeps to its role.** The framework paragraph covers the framework and does not run ahead into the findings. [practice default]
- **A structural gap, stated fairly.** The gap is a property of how the existing work is built, important enough that removing it changes what that work can do, not a weakness picked because this paper happens to avoid it: for `design` and `effect` a limitation of how the existing methods are built; for `evaluation` a factor the current evaluation cannot measure; for `discovery` an observation the existing explanations cannot account for; for `proof` an obstruction the known results do not remove. Wrong: "Existing methods do not use our proposed signal." Right: "Magnitude pruning ranks weights by size alone, so it cannot tell a small weight that carries rare-class evidence from one that carries none." [Checklist] [刘知远]
- **Show why the obvious fix fails.** Name the remedy a reader would try first and the reason it does not remove the gap: a known correction or a larger model (`design` `effect`), a harder version of the old benchmark (`evaluation`), the first explanation that comes to mind (`discovery`), the general problem without assumptions (`proof`). Right: "Recalibrating with temperature scaling after pruning restores the average error but not the error on rare classes, so the fault is not a global shift in confidence." [Black] [Checklist]
- `design` `effect` **The insight paragraph carries the insight, before the method.** It carries the way of seeing the problem that makes it solvable, which the method then realises, not the technical contribution, and it comes before the method paragraph. Wrong: "We propose a two-stage pipeline with a mask predictor and a recalibration head." Right: "Small weights carry much of the network's uncertainty about rare classes, so pruning by magnitude removes uncertainty before it removes accuracy." [Black] [Checklist]
- **No laundry list.** "First we do X, then Y, then Z" is a report, not an argument. Each step the introduction mentions comes with its reason, and with what others did instead where that matters. [Karpathy]
- **Say what the method, benchmark or analysis does.** Describe it by what it does. Set up the contrast with prior work once; do not describe it by what it avoids. [Lipton]
- **Brief here, detailed in the body.** The introduction gives the short account of the idea and the method, construction or measurement; the body section details it and refers back instead of repeating it (前略后详, "brief before, detailed after"). [刘知远]
- `design` `effect` **Tell an improvement as a story.** A paragraph about an improvement or a method's effect runs from the finding to what we think should be done, what we did, how well it worked and what follows. Leave out design details. [practice default]
- **Numbers that surprise, and numbers that set a condition.** Put the headline number in the introduction instead of withholding it. Keep only the numbers that surprise at a glance, and a number that sets a condition (a budget, a scale). [Lipton] [practice default]
- **Spell out the implications.** Say what follows from the result: who should change what they do, what it corrects, what it makes possible. Right: "Pruning schedules tuned for accuracy should therefore also be checked for calibration on rare classes." [Freeman] [Nanda]
- **An example can carry the insight.** A simple toy example or a revealing case can state the main idea, in the introduction or right after it; a single operational equation that captures the idea can also appear in the introduction. [Freeman] [Black] [Lipton]

### Figure 1 and Table 1

- **Plan Figure 1 and Table 1 with the introduction.** Decide what each shows before the introduction is drafted; both show the contribution before the reader reaches the details. [Checklist]
- **Figure 1 and its caption tell the main story.** A reader who sees only Figure 1 and its caption gets the paper's main point. The figure shows the core contribution, not a secondary implementation detail; its most visually prominent element is the most important idea; the caption says what to notice. [Checklist] [Black] [Freeman]
- **Choose the form the contribution needs.** A teaser can summarise the results, illustrate the problem (where current methods fail and how this one differs) or give a system overview; an overview goes on the first page only as a cartoon that is easy to digest. A figure combining the key plots, or one explanatory diagram, also works. The form per orientation is under By orientation. [Black] [Nanda]
- **The text stands without the figure, and cites it.** The argument is complete in words, with Figure 1 as visual support, and the text refers to the figure. [Lipton] [Black]
- **On page one or two.** The pull figure sits on the first or second page. [Karpathy]
- **Table 1 positions the paper.** Make Table 1 a positioning table, not a result table. Its columns are the dimensions the introduction names (the bottlenecks for `design`, the trade-off axes for `effect`, benchmark properties for `evaluation`, the criteria an explanation must meet for `discovery`, assumptions and guarantees for `proof`); its rows are method families or close representative works, described fairly; the last row, this paper, fills a meaningful missing combination instead of collecting checkmarks; a reader can locate the paper from it without reading the related work. [Checklist]

### Contributions

- **A list the reviewer can lift.** End with a list of contributions that puts the key ideas in one place, for the reviewer to carry into the review's summary. [Black] [刘知远] [Nanda]
- **Three items in a fixed shape.** Use three items, within Nanda's one to three claims, in a shape fixed by orientation. A `design` or `effect` paper gives the problem or framework, the technical point and the result. A `discovery` paper gives the framework or protocol, the findings and the improvement or implications. An `evaluation` paper gives the resource, the evaluation protocol and the findings. A `proof` paper gives the assumptions and why they are needed, the main theorem and its comparison with the closest known theorems. [Nanda] for the count; the shapes are a [practice default].
- **Four or more items mean the main line is not yet clear.** Cut to the items that carry the main line; an extra item dilutes the others. [Karpathy] [Black]
- **Each item refutable, with its evidence and its section.** An item says something an experiment, proof or measurement could show false, and points to the section that supports it; together the items match the gap the introduction named and the experiments that follow. Wrong: "We conduct extensive experiments to validate our method." Right: "At matched sparsity, X lowers rare-class calibration error by a third relative to magnitude pruning with recalibration (Section 5)." [Peyton Jones] [Nanda] [Checklist]
- **No abstract sentences, no "first".** Do not restate abstract sentences in the items, and do not write "We are the first to". The items compress the introduction in new words at more detail, and priority shows in the difference from the nearest work. [刘知远] [Black]

## By orientation

The paragraph sequence per orientation is in the Frame. This section holds what the Frame does not: the form of Figure 1 and Table 1, and the rules that bind one orientation only.

`proof` Figure 1 is a counterexample, the modeling rationale or the proof architecture, showing the problem is impossible or ill-posed without the assumptions; Table 1 compares assumptions and guarantees across existing theories. A theorem whose conclusion does not support the main claim is not listed as a contribution. [Checklist] [NeurIPS] [Lipton & Steinhardt]

`effect` Figure 1 is the trade-off plot that matters (accuracy against parameters or FLOPs, performance against supervision budget, robustness against shift severity), not a cherry-picked metric, and shows the advantage before the main table; Table 1 reports matched-budget comparisons. [Checklist]

`design` Figure 1 contrasts the old pipeline with the new design, or shows the overall framework; Table 1 compares capabilities such as dynamic behavior, end-to-end optimization, use of heterogeneous information, interpretability and supervision needs. Each module the introduction mentions answers a named bottleneck, and one logic joins the modules. [Checklist]

`evaluation` Figure 1 sets the old evaluation against the new one and shows that the difference is realistic and consequential; Table 1 compares benchmark properties such as distribution shift, cold start, long-tail coverage, leakage control, metric realism and reproducibility. The new evaluation is presented as more realistic, not only harder. One award paper, having shown that underspecified requests are common in real use, sets against it that "LLM systems are typically evaluated in single-turn, fully-specified settings" [exemplars, arXiv 2505.06120]. [Checklist]

`discovery` Figure 1 shows the mechanism or failure chain as a testable sequence of causes, not a correlation or a qualitative story; Table 1 compares existing explanations by whether they locate the source, explain the mechanism, predict outcomes and support intervention. For each finding say whether it comes from an intervention or from observation, and whether it was predicted or found after the fact; state an existence proof as one. [Checklist] [Nanda]

## Common mistakes

Each common mistake of this section is the negation of a rule above and is stated there.

## Before moving on

- Does the introduction run the steps of its orientation's list (or depart for a reason the argument states), within about a page, with most paragraphs on what this paper does?
- Is the gap structural (a limitation, a mismatch, an observation the explanations miss, an obstruction), stated so its owners would accept it, and does the text say why the first remedy does not close it?
- `design` `effect` Is there an insight paragraph before the method, and does the method follow from it? `discovery` Is the phenomenon shown before any explanation, and does each finding say whether it comes from an intervention or from observation? `evaluation` Does the construction answer the mismatch, with each principle justified, and is the result stated as the false conclusion corrected, with guidance for future methods? `proof` Does the obstruction come before the assumptions, each assumption with an example, and is the informal theorem compared with the closest known ones?
- Does every gap named have its answer (idea, component and experiment; principle and result; finding and test; assumption and obstruction)?
- Are the strongest and nearest prior works named with citations, the difference from each stated, and each described in terms its authors would accept?
- Do the claims match the results in strength and scope, with speculation, aspirational goals and open problems marked as such?
- Do the evidence steps (steps 5 and 6 of the list) give the headline result, the control that answers the likeliest doubt, and the implications?
- Does the first sentence belong to this paper, does the first paragraph end on the gap without answering it and without data, and does every later paragraph state its point first and end on a fact, a result or an open question, not on a "thus"?
- Are there at most three contributions, each refutable, matched to the gap and the experiments, pointing to its section, and free of abstract sentences and "first" claims?
- Can a reader get the main story from Figure 1 and its caption, and do the columns of Table 1 correspond to the dimensions the introduction names?

## Sources for this section

- [Checklist] lars-contribution-centered-checklist.txt (Part III gives the opening logic, checklist and risks per orientation)
- [Black] black-writing-a-good-scientific-paper.txt
- [Nanda] nanda-highly-opinionated-advice.txt
- [Freeman] freeman-how-to-write-a-good-cvpr-submission.txt
- [刘知远] liuzhiyuan-nlp-paper-zhihu-summary.txt
- [Lipton] lipton-heuristics-for-scientific-writing.txt
- [Lipton & Steinhardt] lipton-steinhardt-troubling-trends.txt
- [NeurIPS] neurips-paper-checklist.txt
- [Karpathy] karpathy-phd-survival-guide.txt
- [Mensh & Kording] general/mensh-kording-ten-simple-rules.txt
- [Peyton Jones] general/peyton-jones-how-to-write-a-great-research-paper.txt
- [Swales] general/swales-cars-model.txt
- [exemplars] ../exemplars/intro_*.md. The `discovery` list follows intro_2510.04212, 2503.14858, 2505.17638, 2505.24832, 2502.06768 and 2504.13837; the `evaluation` list follows intro_2505.06120, 2406.04327 and 2502.01926; the `proof` list follows intro_2510.19315, 2402.09963 and 2605.00768. Black, Freeman, 刘知远 and Karpathy write for method papers, so the `design` `effect` list rests on them; the other three lists rest on the Checklist and the exemplars.
