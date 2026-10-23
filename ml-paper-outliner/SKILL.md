---
name: ml-paper-outliner
description: >
  Building and checking the argument skeleton of an AI conference paper (ICLR/NeurIPS/ICML/ACL/CVPR
  and the like) before or apart from its English wording: the contribution in one sentence, what each
  section has to establish for the paper's orientation (proof, effect, design, evaluation, discovery),
  and, per section, a writing brief with one numbered note per paragraph saying what question it
  answers, what it claims and at what strength, what evidence carries the claim, what it does not say
  and what it hands to the next paragraph. Works from a storyline, notes, an outline or an
  existing draft (as a reverse outline), and writes no paper prose. Use it
  whenever the user wants the logic of a paper or a section sorted out (理逻辑, 搭框架, 打磨底稿,
  反向大纲, 故事线, 贡献点怎么写, 实验怎么组织, 这段到底在说什么, 逻辑不顺, 逻辑断了, 先把结构定下来),
  when a polished passage reads well but has lost a step of the argument, and before
  ml-paper-humanizer writes a section from an outline.
---
# ML Paper Outliner (v1.3)

Companion to [ml-paper-humanizer](../SKILL.md). The humanizer turns a skeleton into prose that reads as the authors'; this skill makes the skeleton and checks it. The split follows from how polishing loses logic: a rewrite that answers only to the author's sentences compresses whatever is not stated, and what a draft leaves unstated is usually a step of the argument. Written down as a skeleton, the step survives the rewrite, and the humanizer checks the revised text against it. The skeleton's format, the one contract between the two skills, is in [references/skeleton.md](references/skeleton.md); what the check looks for, with examples, is in [references/checks.md](references/checks.md).

## What this skill does and does not do

A skeleton is content, not wording. It carries the paper's own names verbatim and no sentence meant to go into the paper. The usual input is the author's storyline for a section, often in the order the work was done; the skeleton puts it in the order the argument needs, and the storyline's facts are the only facts it uses.

The check is of the argument, not of the science. It asks whether the premises, evidence and claims in the supplied material are compatible with each other: whether a claim has a premise, whether the evidence named can carry the verb and the scope the claim is given, whether a mechanism claim has a controlled test behind it. It does not verify that data are real, that a derivation is right or that a cited paper says what the author says it does. A suspected scientific problem is recorded as a doubt with the claims it touches, in the open questions; the skeleton is not repaired around it, and the author's conclusions are not rewritten.

## Hard lines

These hold in every mode and are not weighed against anything.

- No fact enters the skeleton that the material does not give. A gap is marked, never filled.
- The author's numbers, names, terms and citations are never changed.
- A claim never outruns its evidence: the verb and the scope are those the named evidence supports ([claim-strength.md](../references/claim-strength.md)).
- The skeleton removes nothing from the author's text. A paragraph the check cannot place is flagged for the author, who decides.

Everything else in this skill and in checks.md is a default the field's writing guides agree on; a line may depart from it where the argument gives a reason, and the reason is written into the skeleton.

## Order of work

Two modes: `skeleton` (from a storyline, notes, an outline or the paper so far; a section or the whole paper) and `reverse` (from an existing draft: what the draft argues as it stands, then what it should). Neither produces paper prose. One skeleton file per paper: the header is written once and sections are added under it, so a section's logic is always checked against the paper's contribution. When no header exists, draft it from the material and mark it provisional; it stays provisional, whatever the material covers, until the author confirms it.

1. **Contribution and orientation.** Write the contribution sentence and, as far as the material shows them, its conceptual, technical and empirical layers, each marked present, not stated in the material, or not applicable to this paper. The layers are a lens for seeing what the paper claims, not a bar it must clear: a theory paper may have no empirical layer, and a solid method paper is not given a conceptual layer it does not have. Pick the primary orientation from what the contribution is, and a secondary one when the paper has two kinds of contribution (a design paper with a discovery section); read the opening logic and common risks for the primary in [section-playbook.md](../references/section-playbook.md), the index of the section files. Then note what the writing guides settle before any outline: the nearest works and the coordinate on which this paper differs, the reviewer's likeliest doubt and what answers it, what Figure 1 shows and whether Table 1 positions or reports. Each is one line when the material gives it and "provisional" when it does not; none of them stops the work. The Contribution line itself carries no `[?]`: a contribution still open is written as the candidates it is open between, in the open questions. The one thing that stops the work is a contribution the material leaves open between candidates that would give the sections different structures; then the candidates are written out, with the structure each implies, and the rest waits for the author.
2. **Names.** Take the humanizer's ledger (`ledger.json`, `names.json`) when one exists. Otherwise list the names the author's text gives to the objects, mechanisms, settings and findings the skeleton will refer to, each as the author writes it; the humanizer's ledger step takes the list over. Figure and table numbers are pointers, not names, and stay out of the list. When the storyline is not in English, a term the author wrote only in their language gets an English rendering, and the rendering is listed under "not in ledger" for the author to confirm or replace. The skeleton uses these names and describes nothing it can name. The same names run through every section.
3. **Section frames.** For each section, read its file in [../references/sections/](../references/sections/) (`introduction.md`, `method.md`, `experiments.md`, …): its frame (where the frame gives one list per orientation, the list of the paper's orientation, plus the paragraph on departures and mixed papers) and the lines tagged with the orientation, including those under Rules. Only the files of the sections being outlined are read. The frame gives the paragraphs and their usual order; the storyline is mapped onto it, and a slot the frame has and the storyline does not is a gap to put to the author, not content to invent. The section's `Carries` line names the part of the contribution this section proves or clarifies; a section that carries none is a question for the author. A different order needs a reason the argument gives, written into the Frame line.
4. **Paragraph notes.** One numbered note per paragraph, a few sentences written to the writer in the imperative, covering five things: the question the paragraph answers, the claim with its verb and scope in parentheses, the evidence with its status (provided, referenced but not provided, planned, or not identified in the supplied material), what the paragraph does not say, and what it ends on, which the next note opens on. A `Keep:` line under the note holds what the writer carries verbatim. The note tells the writer what the paragraph carries and contains no sentence meant for the paper; a note that reads as paper prose is rewritten. The number of notes follows from what the section has to carry at the paragraph length of published sections: a note that would need two paragraphs' worth of content is two notes. What the author still has to settle goes to the open questions with the note's number, and the note carries only a `[?]` where the gap is, not the question itself.
   In `reverse` mode, write the notes first for the draft as it stands, paragraph by paragraph, improving nothing: a paragraph that yields no note, or two, or a question nothing before it raised, is the finding. For an introduction, tag each paragraph with the move it makes (territory; niche by counter-claim, gap, question or continued line; occupying the niche by purpose, present work, findings or structure). Then write the proposed skeleton: it may reorder, split or merge paragraphs, lower a verb or narrow a scope to what the evidence supports, and put one object under one name, and it adds no fact. Each proposed note names in its heading the draft paragraphs it comes from (`P3 → P2`, `P4 + P5 → P3`, `P6 → appendix, author to decide`), so that no paragraph is lost and none is removed without the author.
5. **Chain check.** Read the skeleton once top to bottom as a reader who knows the field and has not seen the paper: does each note follow from the notes before it and the evidence it names, and does each note's ending get picked up by the next note's opening? Then against the contribution sentence: every part of it has a section whose `Carries` line names it and paragraphs that carry it. Then the correspondence across sections: every challenge the introduction names has an idea that answers it, every component of the method has a reason before it, every claim has a test, and every experiment tests a claim; one idea may answer two challenges and one experiment may test two claims, so the counts need not match, and an item with no partner that the material cannot explain is the finding. Then against the ladder and the scopes in claim-strength. Then across sections: one object, one name. Last, as the reviewer: assume there is a hole between the evidence and the story, and say where it would be. The detailed list is in [references/checks.md](references/checks.md).
6. **Hand-off.** Return the skeleton, the open questions and, in `reverse` mode, the change list. Open questions are few: only what would change a note of the skeleton is asked, each with the note it affects (`Experiments P3`), and in two groups. First what blocks writing (a fact a note asserts and the material does not give, a verb that waits on what the evidence is, a decision that changes the paragraph order); then what can wait. A question whose answer would change nothing in the skeleton is not asked. The humanizer's `write` mode takes the skeleton as its outline; its `rewrite` mode checks the revised text against it.

## Output contract

- `skeleton`: the skeleton in the format; then, under a separator and a heading saying it is not part of the skeleton, the chain check's findings in a few lines, with the correspondence table when the material spans more than one section; then the open questions; then "not in ledger: …" for any name the skeleton uses that the author's text does not, renderings of the author's terms included. The skeleton is written in English whatever the language of the storyline, because the humanizer's ledger and checker match its names verbatim against the paper; the open questions are in the author's language.
- `reverse`: the current skeleton (the draft as it stands, unimproved), the proposed skeleton (with the paragraph mapping in each note's heading), the change list (each change with its reason: "P3 → P2: answers the question P1 raised"; "P5: 'demonstrates' lowered to 'shows', one seed"; "intro P2: niche move missing"), then the open questions. The draft's text is not revised; that is the humanizer's job, with the proposed skeleton as its check. The whole output is read beside the draft, so it is shorter than the draft it describes.

## Reference files

- [references/skeleton.md](references/skeleton.md): the skeleton format (header, section brief, numbered paragraph notes and the five things each covers), what the humanizer checks against it, and a worked example from a published results section.
- [references/checks.md](references/checks.md): what the chain check looks for, the defaults and when to depart from them, a correspondence table with one-to-many entries, and a short reverse outline with a missing link.
- [../references/section-playbook.md](../references/section-playbook.md): shared with the humanizer and read from the parent folder; the index of the section files, with the orientation opening logic. One file per section in [../references/sections/](../references/sections/), each a full guide: what the section does for the reader and the reviewer, its frame with the reason for the order, its rules with reasons, examples and sources, what it must do per orientation, the common mistakes and a checklist; sources in `sections/sources.md`. The outliner reads a section's "What this section does", "Frame" (the list of the paper's orientation) and "By orientation" parts and the orientation-tagged rules to plan it, and its "Before moving on" checklist in the chain check.
- [../references/claim-strength.md](../references/claim-strength.md): shared with the humanizer and read from the parent folder; the reporting verbs by what the evidence is, the scope of a claim, design intent kept apart from outcome.

## Sources

The skeleton's fields and checks restate, in one format, what these guides ask of an outline. The skill is for AI conference papers, so guides written for that field are primary and a rule stands on them alone; guides from other fields are secondary and a rule from them stands only where a primary guide or the exemplar passages agree. None is reproduced. The playbook's Sources paragraph gives the fuller account; copies are kept outside the repository.

Primary (AI conferences):

- The Contribution-Centered Paper Writing Checklist (LARS Group, 2026): the one-sentence contribution and its three layers, the five orientations, Figure 1 and Table 1 planned before writing, the nearest works and the reviewer's main doubt, and each section asked what part of the contribution it proves. The section playbook shared with the humanizer is drawn from it.
- Black, *Writing a good scientific paper* (MPI-IS, 2024): goal, problem, solution as the rhythm of abstract and introduction; the insight apart from the technical contribution; the simplest baseline and one change at a time; the conclusion as a present-tense abstract read a step further.
- Freeman, *How to write a good CVPR submission* (2014), quoting Kajiya: the problem and why it matters, other solutions and why they fall short, the solution and the comparison; a toy example before the algorithm; end on conclusions or on what the work opens up, not on future work.
- 刘知远《如何写一篇合格的NLP论文》: the introduction's challenges, the ideas, the method's components and the experiments answer to one another; the introduction sketches the method and the method section details it; the main experiment is a controlled test of the paper's claim.
- Nanda, *Highly Opinionated Advice on How to Write ML Papers* (2025): a paper is one to three claims; a claim's scope follows its evidence; a section earns its place by what the argument would lose without it; red-team by asking where the hole between evidence and story is.
- Lipton, *Heuristics for Scientific Writing (a Machine Learning Perspective)* (2018): section balance, the contribution reached early, the reviewer's question answered before it is asked.
- NeurIPS Paper Checklist: the claims in the abstract and introduction match the results and their scope; a limitations section names assumptions, robustness and scope.
- Karpathy, *A Survival Guide to a PhD* (2016): one contribution; the experiments answer the introduction's challenges.
- Farquhar, *How to Write ML Papers* (2024; page no longer online): recursive outlining from sections to paragraphs to points; each results block says what the experiment shows and how it bears on the contribution.

Secondary (other fields, used where the primary guides or the exemplars agree):

- Mensh & Kording, *Ten simple rules for structuring papers* (2017): an outline is one informal sentence per paragraph; a results paragraph asks a question, gives the data and answers it.
- Peyton Jones, *How to write a great research paper*: the contribution list is written first, refutable, and forward-references the section that carries each item.
- Widom, *Tips for Writing Technical Papers*: the introduction answers what the problem is, why it matters, why it is hard, why it was not solved before, and what the approach and results are.
- Swales, the CARS model: territory, niche, occupying the niche; used as tags in `reverse` mode.
- Ernst, *How to write a technical paper*: the point first and the support after, at the level of the paper, the section and the paragraph; the method as output and key idea before steps.
- Whitesides, *Writing a Paper* (2004): the outline is written at the start of the project and revised with coauthors before any sentence is.

中文说明：用户用中文提问时照常回复中文，论文术语、表号和数字保持原文；骨架本身用英文写，开放问题用中文。
