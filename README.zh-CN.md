# ML Paper Humanizer

给 Claude Code 和 Codex 用的 skill，写和改 ML 顶会论文（ICLR、NeurIPS、ICML、ACL、CVPR 等）的英文正文，让它读起来像人写的。一句话：去 AI 味。

[English](README.md) · [完整示例](examples/results-2504.13837.md) · [版本记录](references/CHANGELOG.md)

## 亮点

- **AI 味是五种写作动作，不是词表。** skill 找的是表演、防御、堆砌、复述、漂移，去掉动作，措辞自然就顺了。禁用词表和句式配额在前五个版本里试过，又撤了，因为照着写出来的稿子像套模板。
- **句式统计自 307 篇获奖和 oral 论文**，来自 NeurIPS、ICML、ICLR、ACL、CVPR 等 12 个会议，2023 到 2026 年：1,234 个按句子功能分类的常用句式，每个至少出现在其中 6 篇里，连接词和 reporting verb 出自同一次统计。标 ★ 的是原文常用、模型写同一段时几乎不用的句式。
- **句子规则来自写作指南**：Gopen & Swan、Williams、Strunk、Fowler、Zinsser、Feak & Swales、Pinker。一句话的要点放在主句，主语挨着动词，新信息放在句末，读者在那里停顿。
- **论文沿用自己的术语和数字。** 术语表从你的文本和引用的论文里建，逐字核验，一个东西只有一个名字。数字、模型和数据集名、引用、已定义的术语一律不改，有疑问的数字只标出来。
- **结论不超过证据。** reporting verb 从 consistent with 到 demonstrates 分级，模块设计来做什么和实际做到了什么分开写，让步只占一个从句。
- **能写也能改。** `write` 按提纲、笔记或中文草稿写新段落；`rewrite` 做最小改动，每处改动附原因。LaTeX 检查脚本以你自己的文档为基准报不正常的重复，不设阈值。

## 改前改后

NeurIPS 2025 runner-up 论文（[arXiv 2504.13837](https://arxiv.org/abs/2504.13837)，CC BY 4.0）实验一节里的两段。同一个模型按同一份内容提纲写了两次，都没有看到原文。

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="examples/compare-dark.png">
  <img alt="同一节实验的两段，左边不用 skill，右边用 skill；左边标出写手自己的比喻和自拟的标题，右边标出领域句式和论文自己的术语" src="examples/compare.png">
</picture>

左边的稿子自拟小标题，用自己的比喻读图（"the crossover persists"），实验还没说清就先回应一个反对意见，论文已经命名的东西被换成描述。右边的稿子先说这段要干什么再给数字，用领域的句式指向图表，沿用论文自己的名字（*reasoning ability boundary*、*hacking or lucky guesses*），推论带上 reporting verb。两版全文和原作者的段落见 [examples/results-2504.13837.md](examples/results-2504.13837.md)。

到句子层面，skill 的教材是 40 组这样的对照：模型草稿和原作者为同一个任务写的句子。

| 任务 | 模型草稿 | 原作者 |
|---|---|---|
| 说明一个比较为什么不公平 | That yardstick, however, measures a different goal. | This would not be a fair comparison, because LMNet is a general method to improve the intelligence of a given LLM, with additional training cost only less than 1% of the pre-training.（[2505.12741](https://arxiv.org/abs/2505.12741)） |
| 先给问题再给数字 | Notably, SFT on the same data lowers mean accuracy by 5.7% relative to Prompt. | Second, one may argue that the improvement mainly relies on training data. SFT (implemented by very moderate training configurations) can hardly bring improvement over the pre-trained LLM (-5.7%).（[2505.12741](https://arxiv.org/abs/2505.12741)） |
| 把意外标成意外 | Actual LLMs, shown as gray points in the same panel, follow a similar exponent near 1. | Remarkably, we find that actual LLMs follow a similar scaling.（[2505.10465](https://arxiv.org/abs/2505.10465)） |

## skill 怎么做

**五种动作。** 论文里的 AI 味是写手做的几件事，skill 给每件起了名字。

- *表演*：把一个结论包装成洞见。
- *防御*：把给审稿人的辩解写进正文。
- *堆砌*：数字、从句、引用全塞进一句话。
- *复述*：标题、首句、末句、图注说的是同一件事。
- *漂移*：一个东西三个名字，或者内部代号留在了论文里。

**读者需要什么。** 读回按七条需求检查稿子，这七条来自写作指南和获奖论文。一遍读懂：一句一个要点，要点在主句，语境放在它前面的短从句（Williams；Gopen & Swan）。有定向：读者在看到细节之前知道这段要干什么。有衔接：句子从读者已经拿着的东西开头，以新加的东西结尾，多数衔接不需要连接词（Gopen & Swan；Strunk）。一物一名：每个东西只用作者起的那个名字（Fowler 论 elegant variation）。有根据：结果句说结果意味着什么，意外标成意外。要紧处说白话：技术表述之后再用白话说一遍。顺着读：一段守一条主题串，动作用动词、施事者做主语，并列的东西用同样的语法形状。连接词表开头摘了各本指南对"什么时候需要连接词、什么时候语序就够了"的说法（Zinsser、Feak & Swales、Pinker）。

**七步。** `SKILL.md` 每次按这个顺序走。

1. 选论文取向，proof / effect / design / evaluation / discovery，读 playbook 里这一节的框架。
2. 从你的文本和引用的论文里建术语表，脚本只留逐字存在的名字。
3. 读例句库里将要写的那些动作，`write` 模式再读三段同类范文，连接词表读一遍。
4. 写或改。每句怎么接上一句，写的时候就定。
5. 读回三遍：查保真，查术语表，查上面的读者需求。
6. 跑句式 pass（`write` 必跑，`rewrite` 按要求跑）：拿着句式表逐句看，句子在指向、观察、解读、比较、交接的地方换成领域的句式。连接词和动词不动。
7. 跑检查脚本，是问题的改。

**它不做什么。** 没在 AI 检测器上测过，也不对检测率做承诺，它针对的是审稿人读出来的东西。不核验引用，不适配期刊格式，不从你以前的论文里学文风。语料是 ML、NLP、CV。用它写出的稿子仍比原作者短，领域动词也少，示例文件里能看到差距。

**怎么来的。** 每个版本的测法都一样：按获奖论文某一节的提纲让模型写一遍，把稿子和原文对照着读。[CHANGELOG](references/CHANGELOG.md) 记了每一版加了什么、被哪次阅读撤掉：把句子切碎的可读性层，改动全是读者讨厌的动词替换的语域 pass，只会把草稿已说清的关系换个说法的连接词 pass，因为原文和草稿冒号频率一样而撤掉的冒号规则。

## 安装和使用

Claude Code：

```bash
git clone https://github.com/Fwibo/ml-paper-humanizer ~/.claude/skills/ml-paper-humanizer
```

Codex CLI：

```bash
git clone https://github.com/Fwibo/ml-paper-humanizer ~/.codex/skills/ml-paper-humanizer
```

其他支持 Agent Skills（带 `SKILL.md` 的文件夹）的 agent 用同一个文件夹。claude.ai 网页版把文件夹打成 zip，在 Settings → Capabilities → Skills 里上传。

检查脚本和范文抽取只需要 Python 3。术语表的统计候选需要 spaCy，读引用论文的 PDF 需要 PyMuPDF；没装的话术语表由模型列、脚本核验。

```bash
pip install spacy pymupdf && python -m spacy download en_core_web_sm
```

用自己的话说就行，中英文都可以。写论文、改论文、润色论文都会触发：

- "把 results 第二段改一下，读着像 AI 写的。"
- "按这些笔记写 introduction，这是一篇 discovery 类的论文。"
- "这个摘要太防御了，改一下。"
- "先别改，告诉我这一节哪里有问题。"
- `/ml-paper-humanizer sec/experiments.tex`

`rewrite` 是默认模式：一遍能读懂的原话保留，输出改后全文和改动清单（改前、改后、原因）。`write` 按提纲、笔记或中文草稿写；论文文本保持英文，需要的话附一份逐句中文直译。用中文提要求时 skill 用中文回复。

脚本也可以单独跑：

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
  register-frames.md          1,234 个按句子功能分类的句式，附论文数和 ★ 标记
  connectives.md              写作指南怎么说，然后是因果、对比、让步的说法
  claim-strength.md           reporting verb 分级，设计意图和结果分开
  exemplars/                  30 篇论文的 144 段引言和实验段落，附 SOURCES.md
  CHANGELOG.md                每一版加了什么、被什么撤掉
scripts/
  check_tex.py                以文档自身为基准的重复检查，无阈值
  term_ledger.py              从你的文本和引用论文里出术语候选；--verify 只留逐字存在的
  pick_exemplars.py           按章节类型和取向抽三段范文
examples/
  results-2504.13837.md       同一节实验：不用 skill、用 skill、原作者
  compare.html, compare*.png  上面的对照图和生成它的 HTML
```

## 来源与许可

skill 本身（SKILL.md、脚本和为它编写的参考文件）以 MIT 许可发布，见 `LICENSE`。

范文段落是 30 篇论文的短节选，均为 CC BY 4.0 或 CC0 1.0 许可，每篇论文及其许可见 `references/exemplars/SOURCES.md`。例句库引用的是获奖论文中的单句，Sources 一节列出每篇论文及其许可。所有引文的版权归原作者所有。节选中的引用和交叉引用已替换为 `[cite]` 和 `REF`，skill 也要求模型不复用其中的内容，也不复用任何连续六个词以上的原文。句式表和连接词表只含短语和计数。

"论文围绕它做到了什么来写，而不是围绕每一条可能的反对意见来写"这个想法来自 [anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill)（MIT）。[humanizer](https://github.com/blader/humanizer) 依据维基百科的 "Signs of AI writing" 从各类文本里去 AI 痕迹；这个 skill 只做 ML 论文，依据的是论文本身。
