# ML Paper Humanizer

给 Claude Code 和 Codex 用的 skill，专门写和改 ML 顶会论文（ICLR、NeurIPS、ICML、ACL、CVPR 等）的英文正文。目标只有一个：去 AI 味，让论文读起来像人写的。

[English](README.md) · [完整示例](examples/results-2504.13837.md)

## 亮点

**1. 顶会获奖论文的用语统计。** 我们收齐了 2023 到 2026 年 NeurIPS、ICML、ICLR、ACL、EMNLP、NAACL、COLM、CVPR、ICCV、ECCV、AAAI、KDD 的获奖论文和 oral 论文，共 307 篇，从里面统计出学术写作的常用词和短语，按句子功能分类：指图表、报结果、做比较、说目的、限范围、排步骤、起名字、讲方法，共 1,234 条，每条至少在 6 篇论文里出现过。连接词和 reporting verb 也出自同一次统计。我们还拿 60 段原文和 318 段模型稿做了对比，原文常用、模型几乎不用的句式打了 ★。模型写的东西"不像资深作者"，差的主要就是这批最普通的句式。

**2. 从写作指南里提炼 AI 写作常漏掉的点。** 这几本书本来就是教学术写作的：Gopen & Swan《The Science of Scientific Writing》、Williams《Style: Toward Clarity and Grace》、Strunk《The Elements of Style》、Fowler《The King's English》、Zinsser《On Writing Well》、Swales & Feak《Academic Writing for Graduate Students》、Pinker《The Sense of Style》。skill 从中挑出模型最容易忽略的几条，写的时候照着做，读回的时候照着查：

- 新信息放句末，读者在那里停顿、记住；旧信息放句首，接住上一句（Gopen & Swan，Williams）。
- 主语紧挨谓语；要点放主句，铺垫放在它前面的短从句里（Gopen & Swan）。
- 动作写成动词，做事的人当主语，别写成名词化加一个空动词（Williams）。
- 转折要早点标出来，读者才不会读到一半掉头（Zinsser）；语序说得清的关系不加连接词，说不清的才加（Strunk，Pinker）。
- 同一个东西不换说法，换了词读者就当成另一个东西（Fowler）；并列的项用同样的语法形状（Strunk）。
- 结论强度和证据匹配：reporting verb 按证据分级，consistent with、suggests、indicates、shows、demonstrates 各在各的位置；"设计来做什么"和"实际做到了什么"分开写；让步只占一个从句。

**3. 术语提取与对齐。** 论文里每个对象、机制、设置、发现，作者都有自己的叫法。skill 从你的正文和你引用的论文里把这些名字提出来，逐字核对确实出现过，做成术语表。之后一个东西只用一个名字，已经命名的东西不另起标签。数字、模型和数据集名、引用、已定义的术语一律不动，有疑问的数字只标出来，不替你改。通用的去 AI 味工具会把模型名改成"该模型"、把术语换成同义描述，这种改法审稿人一眼就能看出来。

## 改前改后

NeurIPS 2025 runner-up 论文（[arXiv 2504.13837](https://arxiv.org/abs/2504.13837)，CC BY 4.0）实验一节里的两段。同一个模型按同一份内容提纲写了两次，都没看过原文。

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="examples/compare-dark.png">
  <img alt="同一节实验的两段，左边不用 skill，右边用 skill；左边标出写手自己的比喻和自拟的标题，右边标出领域句式和论文自己的术语" src="examples/compare.png">
</picture>

左边自己拟了小标题，拿自己的比喻读图（"the crossover persists"），实验还没交代就先回应反对意见，论文已经命名的东西被换成了描述。右边每段先说这段要干什么，再给数字；指图表用的是领域里的句式；名字沿用论文自己的（*reasoning ability boundary*、*hacking or lucky guesses*）；推论前面带 reporting verb。两版全文和原作者的段落见 [examples/results-2504.13837.md](examples/results-2504.13837.md)。

到句子这一级，skill 的教材是 40 组这样的对照：同一个任务，模型怎么写，原作者怎么写。

| 任务 | 模型草稿 | 原作者 |
|---|---|---|
| 说明一个比较为什么不公平 | That yardstick, however, measures a different goal. | This would not be a fair comparison, because LMNet is a general method to improve the intelligence of a given LLM, with additional training cost only less than 1% of the pre-training.（[2505.12741](https://arxiv.org/abs/2505.12741)） |
| 先给问题，再给数字 | Notably, SFT on the same data lowers mean accuracy by 5.7% relative to Prompt. | Second, one may argue that the improvement mainly relies on training data. SFT (implemented by very moderate training configurations) can hardly bring improvement over the pre-trained LLM (-5.7%).（[2505.12741](https://arxiv.org/abs/2505.12741)） |
| 意外的结果要标出来 | Actual LLMs, shown as gray points in the same panel, follow a similar exponent near 1. | Remarkably, we find that actual LLMs follow a similar scaling.（[2505.10465](https://arxiv.org/abs/2505.10465)） |

## skill 怎么做

**AI 味是五种动作，不是一张词表。** 论文里的 AI 味，拆开看是写手做了这几件事：

- *表演*：把一个结论包装成洞见。
- *防御*：把给审稿人的辩解写进正文。
- *堆砌*：数字、从句、引用全塞进一句话。
- *复述*：标题、首句、末句、图注说的是同一件事。
- *漂移*：一个东西三个名字，或者内部代号留在了论文里。

动作去掉，措辞自然就顺了。skill 没有禁用词表，词表和句式配额试过，写出来像套模板，撤了。

**两种模式。** `rewrite` 是默认：一遍能读懂的原话保留，输出改后全文和改动清单（改前、改后、原因）。`write` 按提纲、笔记或中文草稿写新段落，论文正文保持英文，需要的话附一份逐句中文直译。用中文提要求，skill 就用中文回。

**七步。** `SKILL.md` 每次都按这个顺序走。

1. 定论文取向：proof / effect / design / evaluation / discovery，读 playbook 里这一节的框架。
2. 建术语表：从你的正文和引用的论文里提名字，脚本只留逐字存在的。
3. 读例子：例句库里将要写的那几种动作，`write` 模式再读三段同类范文，连接词表过一遍。
4. 写或改。每句怎么接上一句，写的时候就定下来。
5. 读回三遍：查保真，查术语表，查上面那些写作指南的要求。
6. 句式 pass（`write` 必跑，`rewrite` 按要求跑）：拿着句式表逐句看，凡是指图表、报观察、给解读、做比较、交接下文的句子，换成领域里的句式。连接词和动词不动。
7. 跑检查脚本：它以你这篇文档为基准报不正常的重复，比如连着几段同一个开头、一串等长的句子、同一术语两个名字、段落复述标题、说了提升却没说比的是谁。不设阈值，从不说某个数太多或太少。是问题就改，误报就说明。

**它不做什么。** 没在 AI 检测器上测过，也不承诺检测率，它对付的是审稿人读得出来的问题。不核验引用，不适配期刊格式，不从你以前的论文里学文风。语料是 ML、NLP、CV。用它写的稿子还是比原作者短，领域动词也少，示例文件里看得到差距。

**怎么测的。** 每条规则的测法都一样：按获奖论文某一节的提纲让模型写一遍，拿稿子和原文对照着读。没过关的都删了：切碎句子的可读性层，改动全是读者讨厌的动词替换的语域 pass，只会把草稿已说清的关系换个说法的连接词 pass，还有一条冒号规则，因为原文和模型稿的冒号频率本来就一样。

## 安装和使用

Claude Code：

```bash
git clone https://github.com/Fwibo/ml-paper-humanizer ~/.claude/skills/ml-paper-humanizer
```

Codex CLI：

```bash
git clone https://github.com/Fwibo/ml-paper-humanizer ~/.codex/skills/ml-paper-humanizer
```

其他支持 Agent Skills（带 `SKILL.md` 的文件夹）的 agent，放同一个文件夹就行。claude.ai 网页版把文件夹打成 zip，在 Settings → Capabilities → Skills 里上传。

检查脚本和范文抽取只要 Python 3。术语表的统计候选要装 spaCy，读引用论文的 PDF 要装 PyMuPDF；不装的话术语表由模型列、脚本核验。

```bash
pip install spacy pymupdf && python -m spacy download en_core_web_sm
```

用自己的话说就行，中英文都可以。写论文、改论文、润色论文都会触发：

- "把 results 第二段改一下，读着像 AI 写的。"
- "按这些笔记写 introduction，这是一篇 discovery 类的论文。"
- "这个摘要太防御了，改一下。"
- "先别改，告诉我这一节哪里有问题。"
- `/ml-paper-humanizer sec/experiments.tex`

脚本也能单独跑：

```bash
python scripts/check_tex.py paper/ --ledger ledger.json
python scripts/term_ledger.py paper/main.tex --cited refs/*.pdf --out ledger.json
python scripts/pick_exemplars.py results --orientation discovery
```

## 仓库结构

```
SKILL.md                      七步流程、读者需求、读回清单、输出合同
references/
  section-playbook.md         从摘要到 rebuttal 每一节做什么，按论文取向分
  sentence-bank.md            40 组草稿 vs 原作者的句子对照，按问题类型分；另有 23 句按动作分
  register-frames.md          1,234 条按句子功能分类的句式，附论文数和 ★ 标记
  connectives.md              写作指南怎么说，然后是因果、对比、让步的说法
  claim-strength.md           reporting verb 分级，设计意图和结果分开
  exemplars/                  30 篇论文的 144 段引言和实验段落，附 SOURCES.md
scripts/
  check_tex.py                以文档自身为基准的重复检查，无阈值
  term_ledger.py              从正文和引用论文里出术语候选；--verify 只留逐字存在的
  pick_exemplars.py           按章节类型和取向抽三段范文
examples/
  results-2504.13837.md       同一节实验：不用 skill、用 skill、原作者
  compare.html, compare*.png  上面的对照图和生成它的 HTML
```

## 来源与许可

skill 本身（SKILL.md、脚本和为它编写的参考文件）以 MIT 许可发布，见 `LICENSE`。

范文段落是 30 篇论文的短节选，均为 CC BY 4.0 或 CC0 1.0 许可，每篇论文及其许可见 `references/exemplars/SOURCES.md`。例句库引用的是获奖论文里的单句，Sources 一节列出每篇论文及其许可。所有引文版权归原作者。节选里的引用和交叉引用已替换为 `[cite]` 和 `REF`，skill 也要求模型不复用其中内容，连续六个词以上的原文一律不用。句式表和连接词表只有短语和计数。

"论文围绕它做到了什么来写，而不是围绕每一条可能的反对意见来写"，这个想法来自 [anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill)（MIT）。[humanizer](https://github.com/blader/humanizer) 依据维基百科的 "Signs of AI writing" 给各类文本去 AI 痕迹；这个 skill 只做 ML 论文，依据的是论文本身。
