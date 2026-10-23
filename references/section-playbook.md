# How each section goes, by paper orientation (index)

Each section opens with its frame, the things that section does and their usual order. The frame is kept; the wording is free; bold, boxes and run-in headings are format and follow the venue. A different order needs a reason the argument gives (a proof that states the theorem first, an error analysis that opens on a case). The orientation-tagged lines below are references for what readers of that paper type expect.

Core principle. The contribution is the spine of the paper, and every section must let the reader understand, locate, trust and remember it. Before writing, state the contribution in one sentence. If that sentence is only "we propose a method and it works better", the contribution is not yet clear. Write the conceptual layer (a new view, problem formulation, mechanism or principle), the technical layer (the algorithm, model, proof technique, module or benchmark design that realizes it) and the empirical layer (the evidence that it matters) separately. The technical layer alone is rarely enough.

Rules carry orientation tags. `proof` covers a theorem, condition, bound or guarantee. `effect` covers a performance, efficiency, scaling or robustness advantage on an important trade-off. `design` covers a new method, framework, architecture or system that follows from a bottleneck. `evaluation` covers a benchmark, dataset, split, metric or protocol. `discovery` covers a phenomenon, mechanism or empirical law. An untagged rule applies to every orientation.

### Orientation opening logic (light reference)

The opening logic per orientation is a light reference, not a template. Use it to decide what the first two paragraphs must establish, never as a sentence pattern.

- `proof` Why the general problem is impossible, and what assumption removes the obstruction.
- `effect` The trade-off that matters.
- `design` The reformulated problem and the design principle, before any module.
- `evaluation` The mismatch between current evaluation and real use.
- `discovery` The phenomenon, then why existing explanations fall short.

The common risks per type (numbers without an idea, implementation before motivation, correlation written as cause, harder but not more realistic) are the honest failure modes to avoid. None of them is fixed by a sentence template.

## The section files

One file per section, in [sections/](sections/). Read this index and the file of the section being written; nothing else of the playbook is needed for that section. Shared rules (orientation tags, opening logic, common risks) are above and are not repeated in the files. Each file runs the same way: what the section does for the reader and the reviewer; its frame, step by step, with the reason for the order (one list per orientation where the section's shape changes with it, as in the introduction); its rules, each with the reason, an example where one helps and the guide it comes from in square brackets ([Checklist], [Black], [Nanda], … ; [practice default] where no guide was found); what the section must do for each orientation; the common mistakes and how a reviewer reads them; a checklist to run on the finished section; and the sources used.

| Section | File |
|---|---|
| Abstract | [sections/abstract.md](sections/abstract.md) |
| Introduction | [sections/introduction.md](sections/introduction.md) |
| Method | [sections/method.md](sections/method.md) |
| Experiments and results | [sections/experiments.md](sections/experiments.md) |
| Analysis and discussion | [sections/analysis.md](sections/analysis.md) |
| Related work | [sections/related-work.md](sections/related-work.md) |
| Conclusion | [sections/conclusion.md](sections/conclusion.md) |
| Limitations | [sections/limitations.md](sections/limitations.md) |
| Appendix | [sections/appendix.md](sections/appendix.md) |
| Rebuttal | [sections/rebuttal.md](sections/rebuttal.md) |

The guides behind every line, primary (AI conferences) and secondary (other fields), are in [sections/sources.md](sections/sources.md). The two skills read this folder from their own SKILL.md; the outliner reaches it as `../references/`.
