---
name: ml-paper-outliner
description: >
  Building and checking the argument skeleton of an AI conference paper (ICLR/NeurIPS/ICML/ACL/CVPR
  and the like) before or apart from its English wording: the contribution in one sentence, what each
  section has to establish for the paper's orientation (proof, effect, design, evaluation, discovery),
  and one line per paragraph saying what question it answers, what it claims, what evidence carries
  the claim and what it hands to the next paragraph. Works from notes, an outline or an existing draft
  (as a reverse outline), and writes no paper prose. Use it
  whenever the user wants the logic of a paper or a section sorted out (理逻辑, 搭框架, 打磨底稿,
  反向大纲, 故事线, 贡献点怎么写, 实验怎么组织, 这段到底在说什么, 逻辑不顺, 逻辑断了, 先把结构定下来),
  when a polished passage reads well but has lost a step of the argument, and before
  ml-paper-humanizer writes a section from an outline.
---
# ML Paper Outliner (v1.0)

Companion to [ml-paper-humanizer](../SKILL.md). The humanizer turns a skeleton into prose that reads as the authors'; this skill makes the skeleton and checks it. The split follows from how polishing loses logic: a rewrite that answers only to the author's sentences compresses whatever is not stated, and what a draft leaves unstated is usually a step of the argument. Written down as a skeleton, the step survives the rewrite, and the humanizer checks the revised text against it.

A skeleton is content, not wording. It carries the paper's own names verbatim and no sentence meant to go into the paper. It checks that the argument is stated and connected, not whether the science behind it is right: a comparison the author made is recorded as made, and a doubt about the analysis itself is one line among the open questions, never a change to a line of the skeleton. Its format, the one contract between the two skills, is in [references/skeleton.md](references/skeleton.md).

Two things are hard lines here as in the humanizer. A claim never outruns its evidence, and the author's numbers, names, terms and citations are never changed. A skeleton that needs a fact the material does not give marks the gap ("Evidence: none") instead of filling it.

## What the reader needs from the argument

- **A spine.** The contribution in one sentence the reader can repeat, with its conceptual layer (a new view, formulation, mechanism or principle), its technical layer (what realizes it) and its empirical layer (why it matters) told apart. "We propose a method and it works better" is a technical layer alone, and the skeleton is not finished until the other two are there or the author has said there are none.
- **A reason for every paragraph.** Each paragraph answers a question the argument has raised by then: the introduction's gap, the method's bottleneck, the claim an experiment tests, the doubt a check removes. A paragraph whose question the reader cannot name is appendix material or nothing.
- **A chain with no missing link.** Each conclusion has its premise in an earlier line or in named evidence. The hand-off between paragraphs is a fact or an open question that the next paragraph picks up, not a derived "thus" that the next paragraph repeats.
- **One set of objects.** The gap in the introduction, the bottleneck in the method, the component each ablation removes and the limitation at the end are the same objects under the same names, the author's.
- **Claims at their strength.** Each claim carries its condition and the reporting verb its evidence earns ([references/claim-strength.md](references/claim-strength.md)); design intent and measured outcome are two lines, not one.

## Order of work

Two modes: `skeleton` (from notes, an outline or the paper so far; a section or the whole paper) and `reverse` (from an existing draft: what the draft argues as it stands, then what it should). Both produce a skeleton in the format of [references/skeleton.md](references/skeleton.md); neither produces paper prose.

1. **Contribution and orientation.** Write the contribution sentence and the three layers from the material. Pick proof / effect / design / evaluation / discovery from what the contribution is, and read the orientation's opening logic and common risks at the top of [references/section-playbook.md](references/section-playbook.md). When the material does not settle the contribution, write the candidates and stop there for the author to choose; the rest of the skeleton depends on it.
2. **Names.** Take the humanizer's ledger (`ledger.json`, `names.json`) when one exists. Otherwise list the names the author's text gives to the objects, mechanisms, settings and findings the skeleton will refer to, each as the author writes it; the humanizer's ledger step takes the list over. The skeleton uses these names and describes nothing it can name.
3. **Section frames.** For each section, read its frame and the lines tagged with the orientation in the playbook. The frame gives the paragraphs and their order. A different order needs a reason the argument gives, written into the skeleton's Frame line.
4. **Paragraph lines.** One line per paragraph: the question it answers, the claim with its verb, the evidence, what it hands on, the names it uses. The number of lines follows from what the section has to carry at the paragraph length of published sections, not from how few paragraphs the content could be squeezed into: a line that would need two paragraphs' worth of content to write is two lines. The evidence names a table, figure, derivation, citation or the author's note; where the material gives none, the line says so and the item goes to the open questions. In `reverse` mode write these lines first for the draft as it stands, paragraph by paragraph, improving nothing: a paragraph that yields no line, or two, or a question nothing before it raised, is the finding. Then write the target skeleton beside it and list the differences. The target keeps every paragraph of the draft: a paragraph whose question nothing raised is kept with its line marked "[no question found]" for the author to supply one or cut it, and a paragraph is moved or merged only where the chain breaks without it. The target changes a line only where the chain breaks; a verb above its evidence, a name under two forms or a heading that states a topic is a tag in the difference list, not a rewritten line.
5. **Chain check.** Read the skeleton once top to bottom as a reader who knows the field and has not seen the paper: does each line follow from the lines before it and the evidence it names? Then against the contribution sentence: every part of the sentence has a paragraph that carries it, and every paragraph carries a part of it or answers a question the argument raised. Then against the ladder in claim-strength: each claim's verb matches its evidence. Then across sections: one object, one name.
6. **Hand-off.** Return the skeleton, the open questions for the author and, in `reverse` mode, the difference list. The open questions come in two groups: first what the humanizer cannot write without (a fact a line asserts and the material does not give, a verb that waits on what the evidence is, a decision that changes the paragraph order), then what can wait, one line each. The author reads both in one sitting, so a question that would not change a line of the skeleton is not asked. The humanizer's `write` mode takes the skeleton as its outline; its `rewrite` mode checks the revised text against it.

## What the check looks for

- A contribution sentence with a technical layer only; a method paragraph with no bottleneck before it; a module count that outgrows the central idea.
- A paragraph whose question nothing before it raised; a conclusion whose premise is in no earlier line; a hand-off that is a derived takeaway the next paragraph restates.
- An experiment with no question in the argument; a question in the argument with no experiment; a main result that does not test the main claim.
- A claim without its condition; a verb above its evidence (demonstrates on a correlation) or below it (suggests on an ablated result); a design intent standing where an outcome should be; correlation written as cause; a causal chain with a missing link or no intervention behind a mechanism claim.
- One object under two names across sections; a gap, a bottleneck and an ablated component that are not the same thing.
- A section doing another's job: an introduction that runs ahead into the findings, a conclusion that adds a result or ends on a new limitation, a limitation that retracts a conclusion instead of bounding it.
- A contribution list with more items than the main line has parts; a number in the abstract or introduction that does not surprise at a glance.

## Output contract

- `skeleton`: the skeleton in the format, then the open questions for the author, then "not in ledger: …" for any name the skeleton uses that the author's text does not. Names and claim nouns as the author writes them.
- `reverse`: the draft's skeleton as it stands, the target skeleton, the difference list ("P3: answers a question P2 did not raise"; "P5: 'demonstrates' on one seed"), then the open questions. The draft's text is not revised; that is the humanizer's job, with this skeleton as its check. The whole output is read beside the draft, so it is shorter than the draft it describes.

## Reference files

- [references/skeleton.md](references/skeleton.md): the skeleton format, what the humanizer checks against it, and a worked example from a published results section.
- [references/section-playbook.md](references/section-playbook.md): shared with the humanizer (a link to its file); the orientation opening logic, each section's frame and the orientation-tagged lines on what readers of that paper type expect.
- [references/claim-strength.md](references/claim-strength.md): shared with the humanizer (a link to its file); the reporting verbs by what the evidence is, design intent kept apart from outcome.

中文说明：用户用中文提问时照常回复中文，论文术语、表号和数字保持原文。
