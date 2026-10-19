# ML Paper Humanizer

给 Claude Code、Codex 和其他 agent 用的论文写作 skill：撰写和修改 ML 顶会论文（ICLR、NeurIPS、ICML、ACL、CVPR 等）的英文正文，给论文去 AI 味：让它读起来像人写的，不像 AI 写的。

它的规则、句式和例句统计自 307 篇获奖和 oral 论文，不是一张禁用词表。它沿用你论文自己的术语，让每个结论的强度和证据匹配，不动任何数字和引用，并且既能改也能从头写。

[English](README.md) · [示例：同一节的三种写法](examples/results-2504.13837.md) · [每一版改了什么、撤了什么](references/CHANGELOG.md)

## 改前改后

NeurIPS 2025 runner-up 论文（[arXiv 2504.13837](https://arxiv.org/abs/2504.13837)，CC BY 4.0）实验一节里的两段。同一个模型按同一份内容提纲写了两次，都没有看到原文措辞；只有用 skill 的那次建了术语表。

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="examples/compare-dark.png">
  <img alt="同一节实验的两段，左边不用 skill，右边用 skill；左边标出写手自己的比喻和自拟的标题，右边标出领域句式和论文自己的术语" src="examples/compare.png">
</picture>

不用 skill 的稿子自拟小标题，用写手自己的比喻读图（"the crossover persists"），在实验还没说清之前就先和一个反对意见辩论，论文已经命名的东西被换成描述。用 skill 的稿子先说这段要干什么再给数字，按这个领域的习惯指向图表，沿用论文自己的名字（*reasoning ability boundary*、*hacking or lucky guesses*），推论带上 reporting verb，最后交接到分析一节。整节两个版本的全文，连同原作者的段落，见 [examples/results-2504.13837.md](examples/results-2504.13837.md)。

到句子层面，skill 的教材是 40 组这样的对照，每组是模型草稿和原作者为同一个任务写的句子：

| 任务 | 模型草稿 | 原作者 |
|---|---|---|
| 说明一个比较为什么不公平 | That yardstick, however, measures a different goal. | This would not be a fair comparison, because LMNet is a general method to improve the intelligence of a given LLM, with additional training cost only less than 1% of the pre-training.（[2505.12741](https://arxiv.org/abs/2505.12741)） |
| 先给问题再给数字 | Notably, SFT on the same data lowers mean accuracy by 5.7% relative to Prompt. | Second, one may argue that the improvement mainly relies on training data. SFT (implemented by very moderate training configurations) can hardly bring improvement over the pre-trained LLM (-5.7%).（[2505.12741](https://arxiv.org/abs/2505.12741)） |
| 把意外标成意外 | Actual LLMs, shown as gray points in the same panel, follow a similar exponent near 1. | Remarkably, we find that actual LLMs follow a similar scaling.（[2505.10465](https://arxiv.org/abs/2505.10465)） |
| 两个问题分两句问 | As the degree of superposition and the structure of the data change, when does the loss follow a power law in width, and, when it does, what is its exponent? | Varying the degree of superposition and data structure, when is the loss a power law? And if the loss is a power law, what will the exponent be?（[2505.10465](https://arxiv.org/abs/2505.10465)） |

## 为什么用这个

**AI 味是五种写作动作，不是词表。** skill 找的是表演（把结论包装成洞见）、防御（把给审稿人的辩解写进正文）、堆砌（数字、从句、引用全塞进一句）、复述（标题、首句、末句、图注说同一件事）和漂移（一个东西三个名字）。动作去掉，措辞自然就对了。禁用词表和句式配额在前五个版本里都试过，又都撤了：照着写出来的稿子像套模板，而且模型会把任何计数或禁令用到每一个能用的地方，一轮之内就变成新的破绽。

**规则是从论文里数出来的，不是说出来的。** 句式、连接词和 reporting verb 统计自 NeurIPS、ICML、ICLR、ACL、EMNLP、NAACL、COLM、CVPR、ICCV、ECCV、AAAI、KDD 2023 到 2026 年的 307 篇获奖和 oral 论文。句式表按句子功能列了 1,234 个常用句式，每个至少出现在其中 6 篇里；标 ★ 的是原文常用、模型写同一段时几乎不用的。在 60 段原文和 318 段模型草稿上做短语挖掘的结果是：读者说的"不像资深作者"，差的主要是这个领域最普通的指向和衔接句式，不是生僻词。

**沿用你论文自己的术语。** 术语表从你的文本和你引用的论文里建，每个名字都逐字核验过出处。之后一个东西只有一个名字，是作者起的那个，已经命名的东西不会被另起新标签。通用 humanizer 把模型名改成"该模型"、把定义过的术语换成同义描述，正是审稿人第一眼就能看出来的问题。

**结论强度和证据匹配，数字一个不动。** reporting verb 按证据强弱分级（consistent with、suggests、indicates、shows、demonstrates）。模块"设计来做什么"和"实际做到了什么"分开写。让步只占一个从句，不写成一段自我辩护。数字、模型和数据集名、已定义术语、引用和你要求保留的说法一律不改；看起来有问题的数字只标出，不替你改。

**章节框架按论文的论证类型分。** 从摘要到 rebuttal 每一节都有框架，读者的期待按五种论文取向分开写：proof（理论）、effect（效果）、design（方法设计）、evaluation（评测）、discovery（发现）。方法论文和分析论文的实验一节写法不同，skill 知道自己在写哪一种。

**检查以你自己的文档为基准，不设阈值。** LaTeX 检查脚本只报这篇论文里不正常的重复：连续几段同一个开头、一连串等长的句子、同一术语两个名字、段落复述标题、提了提升却没说比的是哪两边、术语表里有却从未用过的名字。它从不说某个数量太多或太少，因为原文偶尔也会做这些事，只是不按节奏做。

**能写，不只能改。** `write` 模式按提纲、笔记或中文草稿写新段落，动笔前先读三段同类范文，写完过一遍句式 pass。`rewrite` 模式做最小改动，输出改动清单，每处附原因。

**每条规则都是测出来留下的。** [CHANGELOG](references/CHANGELOG.md) 记了每一版加了什么，以及哪次盲读或哪个统计把它撤掉了：把句子切碎的可读性层，"改进"全是读者讨厌的动词替换的语域 pass，只会把草稿已说清的关系换个说法的连接词 pass，因为原文和草稿冒号频率一样而撤掉的冒号规则。范文池和例句库逐篇列出来源论文和许可证。

## 和同类工具的区别

| | 词表式 humanizer | 这个 skill |
|---|---|---|
| 什么算 AI 味 | 通用清单上的词和模式（delve、tapestry、破折号） | 论文论证里的五种写作动作 |
| 规则来源 | 适用于任何文本的风格指南 | 307 篇 ML 获奖和 oral 论文的统计 |
| 你的术语和数字 | 可能被改写 | 术语逐字核验；数字、引用、已定义术语不动 |
| 结论强度 | 按指令删或加限定词 | reporting verb 按证据选；让步一个从句 |
| 范围 | 任何文本 | ML 论文全部章节，五种论文取向 |
| 写新内容 | 只改 | 按提纲或中文草稿写，带范文和句式 pass |
| 检查 | 靠模型判断 | 脚本拿文档和它自己比，再加模型 |
| 效果依据 | 截图 | 撤回记录；对照原文的盲读 |

最接近的通用工具是 [humanizer](https://github.com/blader/humanizer)，它依据维基百科的 "Signs of AI writing" 从各类文本里去掉 AI 痕迹。"论文围绕它做到了什么来写，而不是围绕每一条可能的反对意见来写"这个想法来自 [anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill)；在这里它是五种动作之一，背后多了一个 reporting verb 分级。

## 安装

Claude Code：

```bash
git clone https://github.com/Fwibo/ml-paper-humanizer ~/.claude/skills/ml-paper-humanizer
```

Codex CLI：

```bash
git clone https://github.com/Fwibo/ml-paper-humanizer ~/.codex/skills/ml-paper-humanizer
```

其他支持 Agent Skills（带 `SKILL.md` 的文件夹）的 agent 用同一个文件夹即可。claude.ai 网页版把文件夹打成 zip，在 Settings → Capabilities → Skills 里上传。

检查脚本和范文抽取只需要 Python 3。术语表的统计候选需要 spaCy，读引用论文的 PDF 需要 PyMuPDF；没装的话，术语表由模型列、脚本核验。

```bash
pip install spacy pymupdf && python -m spacy download en_core_web_sm
```

## 怎么用

直接用自己的话说。只要是写论文、改论文、润色论文，中英文都会触发（去 AI 味、润色、改论文、别太防御、回审稿意见）：

- "把 results 第二段改一下，读着像 AI 写的。"
- "按这些笔记写 introduction，这是一篇 discovery 类的论文。"
- "这个摘要写得太防御了，改一下。"
- "先别改，告诉我这一节哪里有问题。"
- `/ml-paper-humanizer sec/experiments.tex`

两种模式。`rewrite`（默认）保留一遍能读懂的原话，输出改后全文和改动清单（改前、改后、原因）。`write` 按提纲、笔记或中文草稿写新段落；论文文本保持英文，需要的话可以附一份逐句的中文直译。用中文提要求时 skill 用中文回复。

脚本也可以单独跑：

```bash
python scripts/check_tex.py paper/ --ledger ledger.json
python scripts/term_ledger.py paper/main.tex --cited refs/*.pdf --out ledger.json
python scripts/pick_exemplars.py results --orientation discovery
```

## 工作流程

`SKILL.md` 每次按七步走。

1. **定取向和章节。** 选 proof / effect / design / evaluation / discovery，读 playbook 里这一节的框架。
2. **建术语表。** 从你的文本和引用的论文里整理论文给各种东西起的名字，脚本只保留逐字存在的。
3. **读例子。** 读例句库里将要写的那些动作，`write` 模式再抽三段同类范文，连接词表读一遍。
4. **写或改。** 每句怎么接上一句，写的时候就定；多数句子不需要连接词。
5. **读回三遍。** 一遍查保真，一遍查术语表，一遍按读者需求（一句一个要点，要点在主句，新信息在句末）。
6. **句式 pass。** `write` 模式必跑，`rewrite` 模式按要求跑：通读句式表，逐句看这句是否在做指向、报告、解读、比较这类事，是就换成领域里对应的句式。连接词和动词不动。
7. **跑检查脚本。** 是问题的改，是误报的说明。

## 它不做什么

- 没有在任何 AIGC 检测器（GPTZero、Turnitin、知网）上测过，也不对检测率做任何承诺。它针对的是审稿人读出来的东西。
- 不核验引用，不检查被引论文是否真的说了你说的话。
- 不适配目标期刊或会议的格式习惯，也不从你以前的论文里学你的个人文风。
- 覆盖 ML、NLP、CV 论文。其他领域可以用它的句子规则，但语料是 ML 的。
- 用它写出的稿子仍比原作者短，领域动词也更少；示例文件里能看到目前的差距。

## 仓库里有什么

```
SKILL.md                      七步流程、读者需求、读回清单、输出合同
references/
  section-playbook.md         从摘要到 rebuttal 每一节做什么，按论文取向分
  sentence-bank.md            40 组草稿 vs 原作者的句子对照，按问题类型分；另有 23 句按动作分
  register-frames.md          1,234 个按句子功能分类的句式，附论文数和 ★ 标记
  connectives.md              同一批统计里的因果、结果、对比、让步说法
  claim-strength.md           reporting verb 分级、设计意图与结果分开、诚实线
  exemplars/                  30 篇论文的 144 段引言和实验段落，附 SOURCES.md
  CHANGELOG.md                每一版加了什么、被什么撤掉
scripts/
  check_tex.py                以文档自身为基准的异常检查，无阈值
  term_ledger.py              从你的文本和引用论文里出术语候选；--verify 只留逐字存在的
  pick_exemplars.py           按章节类型和取向抽三段范文
examples/
  results-2504.13837.md       同一节实验：不用 skill、用 skill、原作者
  compare.html, compare*.png  上面的左右对照图和生成它的 HTML
```

## 来源与许可

skill 本身（SKILL.md、脚本和为它编写的参考文件）以 MIT 许可发布，见 `LICENSE`。

范文段落是 30 篇论文的短节选，均为 CC BY 4.0 或 CC0 1.0 许可，每篇论文及其许可见 `references/exemplars/SOURCES.md`。例句库引用的是获奖论文中的单句，Sources 一节列出每篇论文及其许可。所有引文的版权归原作者所有。节选中的引用和交叉引用已替换为 `[cite]` 和 `REF`，skill 也要求模型不复用其中的内容，也不复用任何连续六个词以上的原文。句式表和连接词表只含短语和计数，不含论文正文。
