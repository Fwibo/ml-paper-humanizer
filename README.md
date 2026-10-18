# ML Paper Humanizer

A Claude Code skill for writing and revising the English text of ML conference papers (ICLR, NeurIPS, ICML, ACL, CVPR and the like) so that it reads as written by its authors rather than by an LLM. Its rules, example sentences and phrase lists come from published award and oral papers.

一个用于撰写和修改 ML 顶会论文英文正文的 Claude Code Skill，目标是让论文读起来像作者本人写的，没有 AI 味。规则、例句和句式都取自已发表的获奖论文和 oral 论文。

[English](#english) · [中文](#中文)

## English

### What it does

The skill has two modes.

- `rewrite` (the default) makes minimal edits to your text. Wording that already reads in one pass is kept, and you get the revised text with a change list (before → after, reason).
- `write` drafts a new passage from an outline, notes or a Chinese draft.

It covers abstracts, introductions, method, experiments, analysis, related work, conclusions, limitations, appendices, rebuttals, and figure and table captions. Numbers, model and dataset names, defined terms, citations and any wording you asked to keep are never changed; a number that looks wrong is flagged, not corrected.

### What it treats as AI smell

The skill treats AI smell as five writing actions rather than a word list:

- **Performing**: dressing a conclusion up as an insight.
- **Defending**: writing the reviewer's rebuttal into the paper.
- **Piling**: numbers, clauses and citations shovelled into one sentence.
- **Restating**: the heading, first sentence, last sentence and caption all saying one thing.
- **Drifting**: one object under three names, or an internal name left in the paper.

Once the action is gone, the wording usually follows. There is no banned-word list. Earlier versions had word bans and quotas; drafts written under them read as templates, so they were withdrawn. `references/CHANGELOG.md` records each withdrawal and the reading that led to it.

### Writing techniques inside

- **Section frames** (`references/section-playbook.md`): what each section does and in what order, from the abstract to the rebuttal, with notes for five paper orientations: proof, effect, design, evaluation and discovery.
- **Sentence and paragraph rules** from the writing guides (Gopen and Swan, Williams, Strunk, Fowler). Each sentence makes one point, carried in its main clause, with the subject next to its verb and the new information at the end, where the reader pauses. A paragraph keeps one topic string, and actions are verbs with their agent as subject.
- **Term ledger** (`scripts/term_ledger.py`): the names your paper gives to things, built from your own text and the papers you cite. Each thing keeps one name, and no new label is coined for something you already named.
- **Claim strength** (`references/claim-strength.md`): reporting verbs matched to the evidence (suggests, indicates, shows, demonstrates). What a component is designed to do is kept apart from what it did, and a concession takes one clause.
- **Sentence bank** (`references/sentence-bank.md`): 40 pairs of a model draft and the authors' sentence for the same job, sorted by failure type, plus 23 further sentences sorted by move, all from award papers.
- **Phrase frames** (`references/register-frames.md`): 1,234 stock phrases by sentence function (pointer, result, comparison, purpose, hedge, scope, sequence, naming, method). Each appears in at least 6 of 307 award and oral papers from 2023–2026. A ★ marks the frames that published passages use and model drafts almost never do.
- **Connectives** (`references/connectives.md`): the cause, consequence, contrast and concession forms from the same count.
- **Exemplars** (`references/exemplars/`): 144 introduction and results passages from 30 papers, read side by side with a new draft.
- **LaTeX checker** (`scripts/check_tex.py`): reports repetition that is abnormal for your own document, such as the same opener in consecutive paragraphs, a run of same-length sentences, a term under two names, a heading restated by its paragraph, or a gain whose two sides are never named. It has no targets and never says a count is too high or too low.

### How it works

`SKILL.md` runs seven steps: choose the paper's orientation and read the section frame; build the term ledger; read the examples for the moves about to be written; write or revise; read back for fidelity, for names and for the reader's needs; run a frames pass (by default in `write` mode, on request in `rewrite`); run the checker.

### Install

Claude Code:

```bash
git clone https://github.com/Fwibo/ml-paper-humanizer ~/.claude/skills/ml-paper-humanizer
```

Other agents that load Agent Skills (a folder with a `SKILL.md`) can use the same folder.

`check_tex.py` and `pick_exemplars.py` need only Python 3. The term ledger's candidate step needs spaCy, and PDF input needs PyMuPDF:

```bash
pip install spacy pymupdf && python -m spacy download en_core_web_sm
```

### Usage

Ask in your own words. The skill triggers on writing, revising and polishing a paper, for example:

- "Rewrite the second paragraph of my results section, it reads like AI."
- "Write the introduction from these notes. It is a discovery paper."
- "Make this abstract less defensive."
- `/ml-paper-humanizer sec/experiments.tex`

The scripts also run on their own:

```bash
python scripts/check_tex.py paper/ --ledger ledger.json
python scripts/term_ledger.py paper/main.tex --cited refs/*.pdf --out ledger.json
python scripts/pick_exemplars.py results --orientation discovery
```

### FAQ

**How is this different from humanizer?**
[humanizer](https://github.com/blader/humanizer) removes the patterns in Wikipedia's "Signs of AI writing" from any kind of text. This skill covers ML papers only and works from the papers themselves: section frames, your paper's term ledger, claim strength, and phrase frames counted over 307 award and oral papers. It also writes new passages as well as revising existing ones.

**Will it lower my AIGC detector score?**
It has never been tested against AI detectors (GPTZero, Turnitin, CNKI and others) and makes no claim about them. It is aimed at what a human reader of the paper, such as a reviewer, notices.

**Will it change my results or terms?**
No. Numbers, model and dataset names, defined terms, citations and wording you asked to keep stay as they are.

**Can I start from a Chinese draft?**
Yes, in `write` mode. The paper text stays in English. If you ask in Chinese, the skill answers in Chinese, and it can add a clause-by-clause Chinese version of the result.

**What kinds of papers is it for?**
Method papers and analysis papers at ML, NLP and CV venues.

### Sources and licenses

The skill itself (SKILL.md, the scripts and the reference files written for it) is released under the MIT License; see `LICENSE`.

The exemplar passages are short excerpts from 30 papers under CC BY 4.0 or CC0 1.0, listed with their licenses in `references/exemplars/SOURCES.md`. The sentence bank quotes single sentences from award papers, and the Sources section of `references/sentence-bank.md` lists each paper and its license. Copyright in all quoted text stays with its authors. Citations and cross-references in the excerpts are replaced by `[cite]` and `REF`, and the skill tells the model never to reuse their content or any run of six or more words.

## 中文

### 能做什么

两种模式：

- `rewrite`（默认）：在你的原文上做最小改动。已经一遍能读懂的句子保持原样，输出改后全文和改动清单（改前 → 改后，原因）。
- `write`：根据提纲、笔记或中文草稿写新段落。

覆盖摘要、引言、方法、实验、分析、相关工作、结论、局限性、附录、rebuttal，以及图表标题。数字、模型和数据集名、已定义的术语、引用和你要求保留的说法一律不改；看起来有问题的数字只标出来，不替你改。

### 它怎么理解"AI 味"

这个 skill 把 AI 味看成五种写作动作，而不是一张词表：

- **表演**：把一个结论包装成洞见。
- **防御**：把给审稿人的辩解写进正文。
- **堆砌**：数字、从句和引用全塞进一句话。
- **复述**：标题、首句、末句和图注说的是同一件事。
- **漂移**：同一个东西用了三个名字，或者内部代号留在了论文里。

把这些动作去掉，措辞一般也就顺了。这个 skill 没有禁用词表。早期版本有禁用词和配额，照着写出来的稿子读起来像套模板，后来都撤掉了。每次撤掉了什么、根据哪次试读，都记在 `references/CHANGELOG.md` 里。

### 包含的写作技巧

- **章节框架**（`references/section-playbook.md`）：从摘要到 rebuttal，每一节该做哪些事、按什么顺序做，并按五类论文分别说明：proof（理论）、effect（效果）、design（方法设计）、evaluation（评测）、discovery（发现）。
- **句子和段落规则**，来自 Gopen & Swan、Williams、Strunk、Fowler 等写作指南：一句话只讲一个要点，要点放在主句；主语紧挨谓语；新信息放在句末，也就是读者停顿的地方。一个段落围绕同一组主语展开，动作用动词表达，由施事者做主语。
- **术语表**（`scripts/term_ledger.py`）：从你自己的文本和你引用的论文里整理出论文给各种东西起的名字。同一个东西始终用一个名字，你已经命名过的东西不会被另起新名。
- **结论强度**（`references/claim-strength.md`）：报告动词按证据强弱选择（suggests、indicates、shows、demonstrates）；"某个模块设计来做什么"和"它实际做到了什么"分开写；让步只用一个从句。
- **例句库**（`references/sentence-bank.md`）：40 组"模型草稿 vs. 原作者"的同功能句子对照，按问题类型分类；另有 23 句按写作动作分类。全部来自获奖论文。
- **句式表**（`references/register-frames.md`）：1,234 个按句子功能分类的常用句式（指向图表、报告结果、比较、目的、限定语气、范围、顺序、命名、方法），每个都至少出现在 2023–2026 年 307 篇获奖和 oral 论文中的 6 篇里。标 ★ 的是原文常用、模型草稿几乎不用的句式。
- **连接词**（`references/connectives.md`）：同一批论文里表示因果、结果、对比、让步的说法。
- **范文段落**（`references/exemplars/`）：30 篇论文的 144 段引言和实验结果段落，写新段落时拿来和草稿对照着读。
- **LaTeX 检查脚本**（`scripts/check_tex.py`）：以你自己的文档为基准，找出不正常的重复，比如连续几段用同一个词开头、一连串长度相同的句子、同一术语有两个名字、段落复述了标题、提到提升却没说清跟谁比。脚本不设指标，也从不说某个数量太多或太少。

### 工作流程

`SKILL.md` 分七步：确定论文类型并读对应的章节框架；建术语表；读与要写内容相关的例句；写或改；回读三遍，分别检查忠实度、术语和读者需求；过一遍句式（`write` 模式默认执行，`rewrite` 模式按需执行）；运行检查脚本。

### 安装

Claude Code：

```bash
git clone https://github.com/Fwibo/ml-paper-humanizer ~/.claude/skills/ml-paper-humanizer
```

其他支持 Agent Skills 格式（带 `SKILL.md` 的文件夹）的 agent 也能直接使用这个文件夹。

`check_tex.py` 和 `pick_exemplars.py` 只需要 Python 3。术语表的候选提取需要 spaCy，读 PDF 需要 PyMuPDF：

```bash
pip install spacy pymupdf && python -m spacy download en_core_web_sm
```

### 使用

直接用自己的话说就行，写论文、改论文、润色时都会触发，比如：

- "帮我改一下实验部分第二段，读着有 AI 味"
- "根据这些笔记写引言，这是一篇 discovery 类论文"
- "这段摘要别写得那么防御"
- `/ml-paper-humanizer sec/experiments.tex`

脚本也可以单独运行，命令见上文 Usage 一节。

### 常见问题

**和 humanizer 有什么区别？**
[humanizer](https://github.com/blader/humanizer) 依据维基百科的 "Signs of AI writing"，从各类文本中去掉 AI 写作痕迹。这个 skill 只针对 ML 论文，依据的是论文本身：章节框架、你这篇论文的术语表、结论强度，以及从 307 篇获奖和 oral 论文里统计出的句式。而且它不只能改，也能从头写。

**能降低 AIGC 检测率吗？**
没有拿任何 AI 检测工具（GPTZero、Turnitin、知网等）测过，所以不做这方面的承诺。它针对的是审稿人这样的真人读者会注意到的问题。

**会改我的实验结果或术语吗？**
不会。数字、模型和数据集名、已定义的术语、引用和你要求保留的说法都保持原样。

**可以给中文草稿吗？**
可以，用 `write` 模式。论文正文保持英文；你用中文提问，它就用中文回复，也可以附一份逐句对照的中文译文。

**适合哪类论文？**
ML、NLP、CV 会议上的方法类和分析类论文。

### 来源与许可

skill 本身（SKILL.md、脚本和为它编写的参考文件）以 MIT 许可发布，见 `LICENSE`。

范文段落是 30 篇论文的短节选，均为 CC BY 4.0 或 CC0 1.0 许可，每篇论文及其许可见 `references/exemplars/SOURCES.md`。例句库引用的是获奖论文中的单句，每篇论文及其许可列在 `references/sentence-bank.md` 的 Sources 一节。所有引文的版权归原作者所有。节选中的引用和交叉引用已替换为 `[cite]` 和 `REF`，skill 也要求模型不复用其中的内容，也不复用任何连续六个词以上的原文。
