# Method

One of the section files of [section-playbook.md](../section-playbook.md); read that index first for the orientation tags and the opening logic, then this file for the section being written. Sources are in [sources.md](sources.md).

## What this section does

The technical layer of the contribution: what the method takes in and puts out, the idea that makes it work, and each part with its reason, in enough detail to rebuild it, in two to three pages of an eight-page paper [刘知远]. It realizes the insight the introduction stated without arguing for it again; the reader leaves able to say the key idea in one sentence and point to the part that carries it.

The reviewer checks:
- the key ideas, easy to lift into a three-to-five-sentence summary [Black];
- what is new and what is borrowed [Freeman] [Black];
- that the design follows from a stated bottleneck or principle [Checklist];
- that each part is needed, so the paper has an idea and not a set of tricks [Checklist];
- that the method can be reproduced from the paper and appendix, and every theorem states its assumptions [NeurIPS].

## Frame

The section reads as a blueprint of the method, not a log of what was built [Checklist].

1. **Setup and notation.** State the task as inputs, outputs and what is optimized or estimated, in the symbols the rest of the section uses and only those [刘知远]. Background the method builds on (the standard model, the known estimator) is stated briefly here, cited and marked as known [Nanda]. The setup does not open on implementation.

2. **Key idea and framework.** One sentence gives the whole: what the method outputs and the idea that makes it work. A short paragraph, with a figure when the method has several parts, says how the components connect. The toy or running example goes in this step, before the algorithm [Freeman].

3. **Components, one subsection each.** The parts in data-flow order, each subsection opened by the bottleneck it answers [Karpathy] [刘知远]. The objective and the inference procedure usually close the section as its last subsection, as a "Learning and Prediction" subsection does [刘知远].

4. **Theory, when the method has it.** A guarantee or an analysis follows the component it concerns, in the order the `proof` paragraph below gives: assumptions, roadmap, statement, comparison with the closest known result, proof sketch [Checklist] [NeurIPS].

The order departs only for a reason the argument gives, written in the skeleton's Frame line. Where data-flow order and the order of the bottlenecks disagree, or the material gives no data flow, the order the argument needs wins [practice default]. A proof paper may state the main theorem before the construction that proves it. A dataset or benchmark paper replaces the method with the construction and analysis of the data [刘知远], and a discovery paper with the measurement setup [practice default]; the frame then runs on that object (By orientation).

## Rules

### Order and structure

- **Setup and framework before any component.** The opening defines the task's notation and names the parts, by steps or by modules. [Checklist] [刘知远]
- **Output and key idea before steps.** Say what the method produces and the idea that makes it work, then give the steps. Wrong: "We first embed each sentence, then cluster the embeddings, then take each centroid." Right: "The method returns one representative sentence per topic: it treats topics as clusters in embedding space and returns the member nearest each cluster's centre." [Ernst] [Freeman]
- **A toy or running example before the algorithm.** Reuse the same example in the method, its figure and the case study instead of introducing a second one. [Freeman] [Black] [Ernst] [Peyton Jones]
- **Whole to parts at every level (总-分).** After the whole come the parts, one named subsection each, and each subsection again runs whole then parts. Keep a planned organization and keep telling the reader where in it the text is. [刘知远] [Freeman]
- **Detail the introduction, do not repeat it (前略后详).** The introduction gives the method briefly (前略, brief in front) and this section gives it in detail (后详, detailed later), with a pointer back ("as described in Section 1"). Text or equations that repeat the introduction mean the flow is wrong. [刘知远] [Black]
- **One subsection per design choice that matters.** Each subsection carries a meaningful design choice or technical contribution. Space follows the contribution, not the effort. A data pipeline the claims do not rest on goes to the appendix. [Checklist] [Ernst]
- **Why before how, for every component.** Within a subsection the order is what it does, the challenge, what a baseline or prior work does about it, why this design answers it, then its definition. Across subsections, each part solves what the previous one left open. Wrong: "The refiner has two layers and a gate (Eq. 4)." Right: "Coarse masks bleed across thin structures, so a refiner re-predicts the boundary pixels; it has two layers and a gate (Eq. 4)." [Checklist] [Karpathy] [Black]
- **No laundry list.** "First we do X, then Y, then Z" reports what was done and not why. Justify each step and set it against the alternatives or against what others do; a step that is common practice says so, with a citation. [Karpathy]
- **The approach that works first; an inferior one flagged where it appears.** Do not develop a technique and then abandon it. A failed alternative comes after the successful approach, flagged as inferior, briefly, with what it teaches. A simpler version may come first when the full method is a direct modification of it and the text says so at once. [Ernst] [Checklist]
- **Say what is borrowed and what is new.** Name a standard component as standard and cite it where it is used, not only in the related work, and name the new part as new. Wrong: "We align the two views with a contrastive loss." Right: "We align the two views with the standard InfoNCE loss [12]; what is new is how negatives are drawn, described next." [Freeman] [Nanda] [Lipton]
- **Connection and difference, where the reader would ask.** Explain both the connection to prior methods and the difference from them. The difference from the nearest prior method goes in the subsection of the component that makes it; a paragraph of its own is only for a difference the reader would ask about before reaching the components. [Checklist] [Karpathy] [practice default]

### Equations and notation

- **A symbol when needed, defined at first use, never renamed.** Introduce each symbol where the text first needs it, define it there, and keep its name and meaning to the end: no second name for one object, and no one symbol for two objects (x for pixels and for positions). [Checklist] [刘知远] [Black] [Ernst]
- **Display only the equations that define or claim.** Display an equation when the paper uses it to define an object or to state a claim. Derived identities, ideal-case equalities and symbols added to look formal stay out. [practice default]
- **No mathematics for show.** Leave out a theorem whose conclusion does not support the paper's claims and a statement that looks formal without being a theorem. Test: would the authors rely on the statement to predict anything or to make a system work? If not, cut it or state what it gives the method. [Lipton & Steinhardt]
- **Equations match the code.** Write the equations together with the code. Once the experiments are done, the equation is whatever the code does, an awkward choice included. [Black]
- **A notation convention and a notation table.** Fix how scalars, vectors, matrices, sets and learned parameters are written, and keep to it. Keep a table of every symbol as it appears and put it in the appendix, with a glossary of key terms when there are many. Punctuate an equation as part of its sentence. [Black] [Nanda]
- **An important concept three ways.** The text gives the gist in plain terms, the equation makes it precise and the figure gives the intuition. [Black]
- **An overview subsection only for a complicated method.** A method with many parts gets a short overview, preferably with a figure, before the details. Otherwise the section does not announce what it will do ("In this section we…"). [Black]

### Detail and claims

- **What and why in the body; configuration in the appendix.** The body keeps what each part is, why it is there, and what a reader needs to make sense of the results. Configuration notation, data sizes and per-split counts go to the appendix, with one sentence pointing there. [Karpathy] [Nanda] [NeurIPS] [Ernst]
- **Enough to reimplement.** For a new algorithm, the paper and appendix together make clear how to reproduce it; a new architecture is described in full. [NeurIPS] [Nanda]
- **The method describes; the experiments claim.** A method paragraph describes the design and gives its purpose as intent ("is designed to"); whether the design achieves it is a result, left to the experiment that tests it. Intuition for why a part should help is allowed, written as intuition and kept apart from conclusions the evidence supports. Wrong: "The gate removes redundant tokens, which improves accuracy." Right: "The gate is designed to drop tokens that repeat earlier context; Section 5.2 tests whether the gain comes from it." [Lipton & Steinhardt]
- **Sober names for components.** Name a component by what it computes, not after a human faculty ("an intuition head"), and do not reuse an established term in a new sense. [Lipton & Steinhardt]
- **The method computes; "we" decides.** The method, model or algorithm is the subject of what it computes, and "we" is kept for what the authors chose. Say what it does, not what it can do: "The loss is", not "The loss can be written as". Wrong: "We then project the features onto the subspace." Right: "The encoder then projects the features onto the subspace, whose rank we set on validation data." [Black] [Ernst]
- **What the method does, not what it does not.** Describe the method by what it does; contrasts belong where the comparison is the point. [Lipton]
- **No self-praise in the description.** No "we carefully design", "an elaborate module" or "a novel mechanism". [Black] [Lipton]
- **No explanations piled into parentheses.** A parenthesis holds one short gloss; an explanation the reader needs gets its own clause or sentence. [practice default]

## By orientation

`design` Give the design in one conceptual sentence first, then the modules in data-flow order, each tied to a specific bottleneck. The modules follow one logic instead of being assembled independently, and their number does not outgrow the central idea. [Checklist]

`effect` Name the idea the adjustments serve, so the method is not a list of tuning tricks [Checklist]. When several changes are proposed, say which one carries the idea [Lipton & Steinhardt]. Say where the method's extra cost enters (a second pass, more parameters, more labels), for the matched-budget comparison in the experiments [practice default].

`proof` Before the theorem, explain each main assumption with a simple example or an information-theoretic obstruction, so that none looks chosen to make the proof go through. Derive the algorithm or relaxation from an ideal but intractable objective. Give a proof roadmap before the technical lemmas, say what each lemma contributes, and compare the main theorem with the closest known theorems. Keep the theory tied to the problem that motivated it [Checklist]. State the full set of assumptions in the theorem itself, reference the theorems and lemmas the proof relies on, and when the proof is in the appendix give a sketch in the body [NeurIPS].

`evaluation` The method is the construction of the benchmark. Justify the split, the metric, the data source and the task construction, each by the realistic factor that current evaluation misses, and say how leakage is controlled. Organize the metrics around one central question. Say what makes the new setting more meaningful, not only harder [Checklist]. Credit reused datasets to their creators, with the version used [NeurIPS].

`discovery` The method is the measurement. Give the object of the measurement first, then the reference (what counts as correct and what counts as noise), then the measure [practice default]. Define the measured quantity precisely enough that a statement about it can be true or false [Lipton & Steinhardt]. Set up the measurement so that the phenomenon is reproduced clearly before any analysis [Checklist].

## Common mistakes

- **Many modules, no central idea.** Fix: state the design in one sentence and tie every module to a bottleneck and to the ablation that tests it; cut or move to the appendix a module tied to neither. [Checklist] [Lipton & Steinhardt]

## Before moving on

- After the key-idea paragraph, can the reader say what the method outputs and the idea that makes it work? [Ernst]
- Could a reviewer write a three-to-five-sentence summary of the key ideas from this section alone? [Black]
- Does each component answer a challenge the introduction names, and does an experiment test it? [刘知远]
- Does the section read as a blueprint ordered by the argument, not as a log of what was built? [Checklist]
- Can the reader point to the citation of every borrowed part and name the part that is new? [Freeman]
- Does every displayed equation define an object or state a claim, and match the code as run? [Black] [practice default]
- Is every outcome left to the experiment that tests it, with no "which improves" clause in the method? [Lipton & Steinhardt]
- Could a reader reimplement the algorithm, or rebuild the architecture, from the paper and appendix? [NeurIPS]
- Does every theorem state all its assumptions, with a sketch in the body when the proof is in the appendix? [NeurIPS]
- Does the section use the same contribution vocabulary as the title, abstract and introduction? [Checklist]

## Sources for this section

- [Checklist] lars-contribution-centered-checklist.txt
- [Black] black-writing-a-good-scientific-paper.txt
- [Freeman] freeman-how-to-write-a-good-cvpr-submission.txt
- [刘知远] liuzhiyuan-nlp-paper-zhihu-summary.txt
- [Nanda] nanda-highly-opinionated-advice.txt
- [Karpathy] karpathy-phd-survival-guide.txt
- [Lipton] lipton-heuristics-for-scientific-writing.txt
- [Lipton & Steinhardt] lipton-steinhardt-troubling-trends.txt
- [NeurIPS] neurips-paper-checklist.txt
- [Ernst] general/ernst-how-to-write-a-technical-paper.txt (secondary)
- [Peyton Jones] general/peyton-jones-how-to-write-a-great-research-paper.txt (secondary)
