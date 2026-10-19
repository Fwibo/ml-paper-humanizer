# ML Paper Humanizer

面向 Claude Code 和 Codex 的论文写作 skill，用于撰写和修改 ML 顶会论文（ICLR、NeurIPS、ICML、ACL、CVPR 等）的英文正文。目标是去除 AI 味，使论文读起来像人写的。

[English](README.md) · [完整示例](examples/results-2504.13837.md)

## 亮点

**1. 顶会获奖论文的用语统计。** 语料为 2023 至 2026 年 NeurIPS、ICML、ICLR、ACL、EMNLP、NAACL、COLM、CVPR、ICCV、ECCV、AAAI、KDD 的全部获奖论文和 oral 论文，共 307 篇。从中统计出学术写作的常用词和短语，按句子功能分类：指向图表、报告结果、比较、说明目的、限定范围、排列步骤、命名、描述方法，共 1,234 条，每条至少出现在 6 篇论文中。连接词和 reporting verb 出自同一次统计。另外以 60 段原文对照 318 段同内容的模型稿，原文常用而模型稿几乎不用的句式以 ★ 标出。模型稿读起来缺少学术味，差距主要就在这批最常见的句式上。

**2. 从权威学术写作指南中提取 AI 常忽略的要点。** 依据七本标准参考：Gopen & Swan《The Science of Scientific Writing》（American Scientist，科技写作课程的常用读物）、Williams《Style: Toward Clarity and Grace》和 Swales & Feak《Academic Writing for Graduate Students》（芝加哥大学、密歇根大学出版的写作教材）、Strunk《The Elements of Style》和 Fowler《The King's English》（英语文体的经典规范）、Zinsser《On Writing Well》、Pinker《The Sense of Style》。模型最常忽略的几条，写作时遵循，读回时逐条检查：

- 新信息置于句末，旧信息置于句首承接上一句（Gopen & Swan，Williams）。
- 主语紧邻谓语；要点放在主句，背景放在其前的短从句（Gopen & Swan）。
- 动作用动词表达，施事者作主语（Williams）。
- 转折尽早标出（Zinsser）；语序已能表达的关系不加连接词（Strunk，Pinker）。
- 同一事物不换说法（Fowler）；并列成分采用相同的语法形式（Strunk）。
- 结论强度与证据匹配：reporting verb 按 consistent with、suggests、indicates、shows、demonstrates 分级；设计意图与实际结果分开；让步限于一个从句。

**3. 术语提取与对齐。** 每个子领域对其中的对象、机制、设置和发现都有固定的叫法。skill 从你的正文和你引用的论文中提取这些术语，逐字核验其确实出现，整理成术语表。此后一物一名，已有名称的事物不再另起标签。数字、模型和数据集名、引用、已定义的术语一律不改，存疑的数字只标出，不代为修改。通用的去 AI 味工具常把模型名改成"该模型"、把术语换成同义描述，这类改动审稿人一眼即可识别。

## 改前改后

NeurIPS 2025 runner-up 论文（[arXiv 2504.13837](https://arxiv.org/abs/2504.13837)，CC BY 4.0）实验一节中的两段。同一模型按同一份内容提纲写了两次，均未见过原文。

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="examples/compare-dark.png">
  <img alt="同一节实验的两段，左侧不用 skill，右侧用 skill；左侧标出写手自己的比喻和自拟的标题，右侧标出领域句式和论文自身的术语" src="examples/compare.png">
</picture>

左侧自拟小标题，以自己的比喻解读图表（"the crossover persists"），实验尚未交代便先回应反对意见，论文已命名的事物被换成描述。右侧每段先说明目的再给数字，以领域句式指向图表，沿用论文自身的术语（*reasoning ability boundary*、*hacking or lucky guesses*），推论由 reporting verb 引出。两版全文及发表原文见 [examples/results-2504.13837.md](examples/results-2504.13837.md)。

在句子层面，skill 的教材是 40 组这样的对照：同一写作任务，模型稿与发表原文各一句。

| 任务 | 模型稿 | 发表原文 |
|---|---|---|
| 说明一个比较为何不公平 | That yardstick, however, measures a different goal. | This would not be a fair comparison, because LMNet is a general method to improve the intelligence of a given LLM, with additional training cost only less than 1% of the pre-training.（[2505.12741](https://arxiv.org/abs/2505.12741)） |
| 先给问题，再给数字 | Notably, SFT on the same data lowers mean accuracy by 5.7% relative to Prompt. | Second, one may argue that the improvement mainly relies on training data. SFT (implemented by very moderate training configurations) can hardly bring improvement over the pre-trained LLM (-5.7%).（[2505.12741](https://arxiv.org/abs/2505.12741)） |
| 标出意外的结果 | Actual LLMs, shown as gray points in the same panel, follow a similar exponent near 1. | Remarkably, we find that actual LLMs follow a similar scaling.（[2505.10465](https://arxiv.org/abs/2505.10465)） |

## skill 的工作方式

**AI 味是五种写作动作，而非词表。** 论文中的 AI 味可以归结为五种写作动作：

- *表演*：把一个结论包装成洞见。
- *防御*：把对审稿人的辩解写进正文。
- *堆砌*：数字、从句、引用挤在同一句中。
- *复述*：标题、首句、末句、图注表达同一件事。
- *漂移*：一个事物有多个名称，或内部代号遗留在论文中。

去除动作，措辞随之自然。skill 不设禁用词表：词表和句式配额经过测试，所得稿件读起来像模板，已经移除。

**两种模式。** `rewrite` 为默认模式：一遍可读懂的原句保留，输出修改后的全文和改动清单（改前、改后、原因）。`write` 按提纲、笔记或中文草稿撰写新段落，论文正文保持英文，可按需附逐句中文直译。用中文提出请求时，skill 以中文回复。

**七个步骤。** `SKILL.md` 对每次请求按此顺序执行。

1. 确定论文取向（proof / effect / design / evaluation / discovery），阅读 playbook 中该章节的框架。
2. 建立术语表：从正文和引用论文中提取术语，脚本只保留逐字存在的条目。
3. 阅读范例：例句库中即将写到的动作，`write` 模式另读三段同类范文，连接词表通读一遍。
4. 撰写或修改。句与句之间的关系在写作时确定。
5. 读回三遍：查保真，查术语表，查上述写作指南的要点。
6. 句式 pass（`write` 模式必做，`rewrite` 模式按需）：对照句式表逐句检查，凡指向图表、报告观察、给出解读、进行比较、交接下文的句子，改用领域句式。连接词和动词保持不变。
7. 运行检查脚本。脚本以本文档为基准报告异常重复：连续段落以同一开头起句、一串等长的句子、同一术语两个名称、段落复述标题、提及提升却未说明比较对象。脚本不设阈值，不判断数量多少。确为问题则修改，误报则说明。

**不做的事。** 未在 AI 检测器上测试，也不对检测率作任何承诺；skill 针对的是审稿人能读出的问题。不核验引用，不适配期刊格式，不从你以往的论文中学习个人文风。语料限于 ML、NLP、CV。用它写出的稿件仍比发表原文短，领域动词也较少，差距可在示例文件中查看。

**测试方法。** 每条规则的测试方式相同：按获奖论文某一节的提纲让模型写一遍，将稿件与原文对照阅读。未通过的规则已移除：切碎句子的可读性层，改动全为读者反感的动词替换的语域 pass，只把稿件已表达的关系换一种说法的连接词 pass，以及一条冒号规则，因为原文与模型稿的冒号频率并无差异。

## 安装与使用

Claude Code：

```bash
git clone https://github.com/Fwibo/ml-paper-humanizer ~/.claude/skills/ml-paper-humanizer
```

Codex CLI：

```bash
git clone https://github.com/Fwibo/ml-paper-humanizer ~/.codex/skills/ml-paper-humanizer
```

其他支持 Agent Skills（含 `SKILL.md` 的文件夹）的 agent 可直接使用同一文件夹。claude.ai 网页版将文件夹打包为 zip，在 Settings → Capabilities → Skills 中上传。

检查脚本和范文抽取仅需 Python 3。术语表的统计候选需要 spaCy，读取引用论文的 PDF 需要 PyMuPDF；未安装时，术语表由模型列出、脚本核验。

```bash
pip install spacy pymupdf && python -m spacy download en_core_web_sm
```

用自己的话提出请求即可，中英文均可。撰写、修改、润色论文都会触发：

- "把 results 第二段改一下，读着像 AI 写的。"
- "按这些笔记写 introduction，这是一篇 discovery 类的论文。"
- "这个摘要太防御了，改一下。"
- "先别改，告诉我这一节哪里有问题。"
- `/ml-paper-humanizer sec/experiments.tex`

脚本也可单独运行：

```bash
python scripts/check_tex.py paper/ --ledger ledger.json
python scripts/term_ledger.py paper/main.tex --cited refs/*.pdf --out ledger.json
python scripts/pick_exemplars.py results --orientation discovery
```

## 仓库结构

```
SKILL.md                      七个步骤、读者需求、读回清单、输出合同
references/
  section-playbook.md         从摘要到 rebuttal 每一节的任务，按论文取向分
  sentence-bank.md            40 组模型稿与发表原文的句子对照，按问题类型分；另有 23 句按动作分
  register-frames.md          1,234 条按句子功能分类的句式，附论文数和 ★ 标记
  connectives.md              写作指南的要点，以及因果、对比、让步的表达
  claim-strength.md           reporting verb 分级，设计意图与结果分开
  exemplars/                  30 篇论文的 144 段引言和实验段落，附 SOURCES.md
scripts/
  check_tex.py                以文档自身为基准的重复检查，无阈值
  term_ledger.py              从正文和引用论文中提取术语候选；--verify 只保留逐字存在的
  pick_exemplars.py           按章节类型和取向抽取三段范文
examples/
  results-2504.13837.md       同一节实验：不用 skill、用 skill、发表原文
  compare.html, compare*.png  上文的对照图及生成它的 HTML
```

## 来源与许可

skill 本身（SKILL.md、脚本及为其编写的参考文件）以 MIT 许可发布，见 `LICENSE`。

范文段落为 30 篇论文的短节选，均为 CC BY 4.0 或 CC0 1.0 许可，每篇论文及其许可见 `references/exemplars/SOURCES.md`。例句库引用获奖论文中的单句，其 Sources 一节列出每篇论文及其许可。所有引文版权归原作者所有。节选中的引用和交叉引用已替换为 `[cite]` 和 `REF`，skill 要求模型不复用其中内容，也不复用任何连续六个词以上的原文。句式表和连接词表仅含短语和计数。

"论文围绕其成果来写，而非围绕每一条可能的反对意见"这一思路来自 [anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill)（MIT）。[humanizer](https://github.com/blader/humanizer) 依据维基百科的 "Signs of AI writing" 去除各类文本的 AI 痕迹；本 skill 仅针对 ML 论文，依据是论文本身。
