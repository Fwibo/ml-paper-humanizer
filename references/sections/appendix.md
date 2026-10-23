# Appendix

One of the section files of [section-playbook.md](../section-playbook.md); read that index first for the orientation tags and the opening logic, then this file for the section being written. Sources are in [sources.md](sources.md).

## What this section does

It holds what the main text cannot fit: the full technical detail needed to check and reproduce the work. The details needed to make sense of the results stay in the main paper. The reviewer checks:

- that every main-text promise of detail is kept
- polish equal to the main text, and brevity
- results that are plainly not the picked ones, and failure cases
- no new experiment the venue's rules forbid
- that the sections the NeurIPS checklist answers cite actually support them

## Frame

In its usual order:

1. **Notation and setup.** A table of every symbol [Black] or a glossary of key terms [Nanda], and the shared setup later sections refer to. Not a second introduction.
2. **Proofs.** Complete proofs of every theoretical result; the main text keeps a short sketch [NeurIPS]. No result the main text does not state.
3. **Protocols, algorithms and implementation.** Algorithm boxes, architecture, splits, hyperparameters, compute and code [NeurIPS]. Not a log of what was built.
4. **Prompts and instructions.** Every prompt, and for a study with people the full instructions they were given [NeurIPS].
5. **Additional experiments.** One subsection per experiment, in four parts (Rules), each answering a question the main text raises.
6. **Full tables.** The per-method, per-dataset and per-seed results the main text summarises.
7. **Cases and failure cases.** Examples that are plainly not the picked ones, and the failures [Black] [Nanda].
8. **Extended related work, limitations, broader impact,** where the venue puts them in the appendix.

The order may instead follow the order in which the main text points to the appendix, for instance extended related work first when the related-work section is the first to point there. It never follows the order in which the work was done. [practice default]

## Rules

- **Treat the appendix as part of the paper, not an internal report.** Write for a reader who did not do the work: no analysis notes, source records, driver output, script names, workspace names, batch names or session ids. Wrong: "Results of batch run_0423 (results/v3_final.csv) are below." Right: "Table 9 reports all five seeds of each configuration." [practice default]
- **Make it as polished as the text, and short.** The same care in figures, tables and wording as the main text. [Black]
- **Organise sections by type of material.** One type per section, as in the Frame; no section holds a piece of the main text's argument. [practice default]
- **Give each additional-experiment subsection four parts.** Setup (which configuration, compared against what), Measures (the metric definitions), Results (walk through the table by the comparisons that matter, not by its geometry, and close on the result), Reading (state the boundary once). [practice default]
- **Make each subsection self-contained.** Cite main-text tables and sections, not paragraphs of other appendix subsections; restate a definition from elsewhere in one sentence. [practice default]
- **Write protocols as algorithm boxes.** A procedure the reader must rerun goes in numbered steps with inputs and outputs, not in prose. [practice default]
- **Put prompts in boxes verbatim.** One sentence before the box says who uses it and when; nothing after it interprets it. Wrong: "We used the following prompt, which encourages careful reasoning:" Right: "The judge model receives this prompt once per pair of responses, with the two responses in random order." [practice default] [NeurIPS]
- **Point from the main text to the subsection and the table.** "Appendix C.2, Table 8", not "see the appendix". The main text mentions the supplementary material wherever the reader needs it. [Black] [practice default]
- **Do what the text promised.** Every "details are in the appendix" in the main text has its details there. [Black]
- **Add results that are plainly not the picked ones, and failure cases.** Say how the examples were chosen (at random, or picked, and from how many). [Black] [Nanda]
- **Add no new experiment the rules forbid.** The appendix is not a way around the venue's rules on what may be added after the deadline. [Black] [NeurIPS]
- **Keep the claims in the main text.** A claim whose evidence sits in the appendix is still stated in the main text with its pointer, and the details needed to make sense of the results stay there too. [NeurIPS] [Nanda]
- **Give the full experimental details.** The data splits, every hyperparameter and how it was chosen, and the full architecture or algorithm where it is the contribution, enough for a reader to rerun it. [NeurIPS] [Nanda]
- **Define the error bars.** What variability they capture (split, initialization, sampling), how they were computed, whether they show a standard deviation or a standard error, and the assumptions made. [NeurIPS]
- **Report the compute.** The type of compute worker, memory and time per run, the total, and whether the full project used more compute than the runs reported, preliminary and failed ones included. [NeurIPS]
- **Give a path to reproduction.** Code, data and the exact commands and environment that reproduce the main results, anonymised at submission, and which experiments the release covers; where code cannot be released, the other path to verification. The codebase runs on a fresh machine, with a README pointing to weights and data. [NeurIPS] [Nanda]
- **Give complete proofs with their assumptions.** Every theorem states or references its assumptions and the lemmas it relies on; an informal argument in the main text has its formal proof here. [NeurIPS]
- **Document the assets.** For existing data, code and models: the creators cited, the version used, the license named. For new assets: their documentation. For a study with people: the full instructions, screenshots and compensation. [NeurIPS]
- **Keep a notation table and a glossary.** A table of every symbol, started early and extended as symbols are added, and a glossary of key terms for a reader who lacks the authors' context. [Black] [Nanda]
- **Write replication advice for the reader.** How the hyperparameters were found, the fiddly steps a replicator will meet, common misreadings of the results, possibly as an FAQ section; advice to a reader, not the history of the project. [Nanda] [Karpathy] [practice default]

## By orientation

- `proof` Complete proofs in the order of the proof roadmap, each lemma saying what it contributes to the theorem; the counterexamples that show each assumption is needed; every theorem restated with its full assumptions. [Checklist] [NeurIPS]
- `effect` The matched-budget comparisons in full; the tuning budget and search space of every baseline, so the claim of fair tuning can be checked; the cost metrics per configuration; the settings where the advantage shrinks. [Checklist] [Nanda]
- `design` The full architecture and every hyperparameter; the ablations that did not fit in the main text, each tied to the claim it tests; the case studies that show how the design works inside. [NeurIPS] [Checklist]
- `evaluation` The dataset documentation (sources, construction, the principles behind the split and the metric, leakage control, annotation instructions, license and consent); the full per-model results; examples for each category. [Checklist] [NeurIPS]
- `discovery` Every setting in which the phenomenon was reproduced and those in which it was not; the details of each intervention and control; randomly selected examples with how they were drawn. [Checklist] [Nanda]

## Common mistakes

- **A checklist answer with nothing behind it** ("Yes, see Appendix D", where Appendix D lacks how the hyperparameters were chosen or the compute): check each answer against the section it cites. [NeurIPS]

## Before moving on

- Does the main text point to the appendix where the reader needs it, naming a subsection and a table, and does each target hold what was promised?
- Is each section one type of material, and each subsection readable on its own?
- Does each additional-experiment subsection have its setup, measures, results and reading?
- Are there results that are plainly not the picked ones, with how they were chosen, and failure cases?
- Is it as polished as the main text, and free of internal records?
- Is every new result one the venue's rules allow, and is every claim it supports stated in the main text?
- Are the data splits, the hyperparameters and how they were chosen, the full architecture, the error-bar definition and the compute per run and in total given?
- Are the code, data and exact commands provided, or the other path to reproduction stated?
- Are all proofs complete, with their assumptions and the lemmas they cite?
- Are the assets' versions and licenses and any participant instructions given, and does every checklist answer's cited section hold what it claims?

## Sources for this section

- [Black] black-writing-a-good-scientific-paper.txt
- [NeurIPS] neurips-paper-checklist.txt
- [Nanda] nanda-highly-opinionated-advice.txt
- [Karpathy] karpathy-phd-survival-guide.txt
- [Checklist] lars-contribution-centered-checklist.txt
