# ml-paper-humanizer

**专为机器学习顶会论文打造的英文写作与润色 Agent Skill（适配 Claude Code、Codex 及主流 AI 编程助手）——剥离生成式痕迹，让正文读起来像人写的。**

[English](README.md) · [完整示例](examples/results-2504.13837.md)

---

## 亮点

直接用大模型起草或润色论文，往往会产生浮夸的修辞、防御性的辩解以及生造的学术短语。`ml-paper-humanizer` 不依赖简单的"禁用词表"，而是通过顶会语料约束、经典修辞法则和子领域术语对齐，从底层重建模型的学术写作方式。

### 1. 顶会获奖论文的用语统计：只用审稿人最熟悉的句式
我们对 2023–2026 年间 **NeurIPS、ICML、ICLR、ACL、EMNLP、NAACL、COLM、CVPR、ICCV、ECCV、AAAI、KDD** 共 12 个顶会的全部获奖及 Oral 论文（307 篇）进行了语料库分析，按句子功能（指图表、报结果、比较、目的、弱化断言、范围、步骤、命名、方法）提取出 1,234 条高频学术句式，每条均在至少 6 篇独立论文中复现。
* **实证依据：** 在对比 60 段人类原文与 318 段模型生成稿后，我们发现模型稿缺失的"学术感"核心就在于未能掌握这批标准功能句式。
* **实际效果：** 写出来的句子是审稿人已经读过上百遍的地道表达，而非大模型自己发明的说法。

### 2. 权威写作指南的句法提炼：补齐 AI 最欠缺的隐形文笔
良好的学术文风取决于信息的组织方式，而非表面的词汇替换。我们将 Gopen & Swan《The Science of Scientific Writing》、Williams《Style》、Swales & Feak《Academic Writing for Graduate Students》以及 Strunk、Fowler、Zinsser、Pinker 等七部权威写作指南的核心原则，转化为模型在写作时遵循、回读时逐条核查的清单：
* **句法与信息流：** 新信息放句末、主语紧邻谓语、动作用动词而非名词化结构、转折早标、语序够用就不加连接词、一物一名、并列同形。
* **结论与证据匹配：** 对 reporting verb 进行强度分级，让步逻辑收敛于单个从句，确保主张的语气强度与实验证据严格对齐。
* **实际效果：** 这些是读者看不出但读得出的底层功夫。模型无法自发写出，由本 Skill 在写时执行、读回时逐条核查。

### 3. 子领域术语提取与对齐：绝不把模型名改成"该模型"
通用的"去 AI 味"工具常通过同义词替换来规避模式（例如把具体的模型架构名泛化为"该模型"或"所提出的框架"），审稿人一眼即可看穿。
* **术语核验：** 自动从当前正文及引用论文中提取子领域的既定术语，逐字核验并建立术语表（Term Ledger），全篇贯彻"一物一名"。
* **事实红线：** 实验数字、模型与数据集名称、引用标记、已定义术语**一律锁死不改**（存疑数字仅作标出提示），确保语言润色绝不越界干扰科学事实。

---

## 改前改后

以下为 NeurIPS 2025 runner-up 论文（[arXiv 2504.13837](https://arxiv.org/abs/2504.13837)，CC BY 4.0）实验章节中的两段。同一模型按同一份内容提纲写了两次，均未见过发表原文。

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="examples/compare-dark.png">
  <img alt="同一节实验的两段，左侧不用 skill，右侧用 skill；左侧标出写手自己的比喻和自拟的标题，右侧标出领域句式和论文自身的术语" src="examples/compare.png">
</picture>

* **不用 Skill（左）：** 模型自拟小标题，用生造的比喻解读图表（*"the crossover persists"*），实验尚未交代便提前回应审稿质疑，并将论文已命名的概念替换成了泛化描述。
* **使用 Skill（右）：** 每段先交代目的再给数字，用领域标准句式指向图表，严格沿用论文自身的术语（*reasoning ability boundary*、*hacking or lucky guesses*），推论均由恰当的 reporting verb 引出。
* **完整对照：** 两版完整生成稿及发表原文见 [examples/results-2504.13837.md](examples/results-2504.13837.md)。

在句子层面，Skill 内置了 40 组如下的对照教材——针对同一写作任务，对比模型初稿与顶会发表原文的真实差距：

| 写作任务               | 模型初稿 (Model draft)                                       | 顶会发表原文 (Published text)                                |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 说明一个比较为何不公平 | That yardstick, however, measures a different goal.          | This would not be a fair comparison, because LMNet is a general method to improve the intelligence of a given LLM, with additional training cost only less than 1% of the pre-training.（[2505.12741](https://arxiv.org/abs/2505.12741)） |
| 先给问题，再给数字     | Notably, SFT on the same data lowers mean accuracy by 5.7% relative to Prompt. | Second, one may argue that the improvement mainly relies on training data. SFT (implemented by very moderate training configurations) can hardly bring improvement over the pre-trained LLM (-5.7%).（[2505.12741](https://arxiv.org/abs/2505.12741)） |
| 标出意外的结果         | Actual LLMs, shown as gray points in the same panel, follow a similar exponent near 1. | Remarkably, we find that actual LLMs follow a similar scaling.（[2505.10465](https://arxiv.org/abs/2505.10465)） |

---

## 工作原理

### 1. 消除五种写作动作，而非维护禁用词表
论文中的"AI 味"本质上源于模型的五种写作动作：
* **表演（Performing）：** 把一个普通结论包装成深刻洞见。
* **防御（Defending）：** 把本该放在 Rebuttal 里的辩解提前写进正文。
* **堆砌（Piling）：** 将数字、从句、引用全部挤在同一句话中。
* **复述（Restating）：** 小标题、首句、末句和图注反复表达同一个意思。
* **漂移（Drifting）：** 同一个事物换用多个名称，或将内部代号遗留在正文中。

去除这些动作，措辞随之自然。**本 Skill 不设禁用词表：** 我们在测试中发现，硬性词表和句式配额会导致生成稿读起来像刻板模板，因此已将其彻底移除。

### 2. 两种工作模式
* **`rewrite`（默认修改模式）：** 一遍即可读懂的原句予以保留；输出修改后的英文正文及逐条改动清单（改前、改后、修改原因）。
* **`write`（起草模式）：** 根据提纲、笔记或中文草稿撰写新段落；论文正文保持英文，可按需附带逐句中文直译。使用中文提问时，Skill 会以中文回复沟通。

### 3. 七步执行流水线
`SKILL.md` 对每次请求严格按以下顺序执行：
1. **定取向：** 确定论文类型（proof / effect / design / evaluation / discovery），读取 Playbook 中对应章节的结构框架。
2. **建术语表：** 从当前正文和引用文献中提取并核验领域术语。
3. **读范例：** 检索例句库中即将写到的句法动作；在 `write` 模式下额外精读三段同类顶会范文。
4. **写或改：** 撰写或重写正文，在落笔时同步确立句与句之间的逻辑衔接。
5. **三遍回读：** 一查事实保真，二查术语表一致性，三查权威写作指南的各项句法要点。
6. **句式对齐（Frames Pass）：** `write` 模式必做，`rewrite` 模式按需执行。对照句式库逐句检查，凡涉及指向图表、报告观察、给出解读、基线比较或承上启下的句子，统一替换为领域标准句式。
7. **脚本终检：** 运行检查脚本，以当前文档自身为基准报告异常重复（如同一概念使用了两个名称、段落首尾复述小标题、提及性能提升却未指明比较基准等）。

### 4. 边界与局限（它不做什么）
* **不针对 AI 检测器：** 本工具未在任何 AI 检测器上测试，也不对检测率作任何承诺；它解决的是**人类审稿人**能读出来的问题。
* **不越界：** 不核验引文真伪，不强制套用特定期刊的排版格式，也不从你过往的论文中学习个人文风。语料覆盖范围为 ML、NLP 与 CV。
* **已知差距：** 使用本工具写出的段落通常仍比发表原文略短，领域特定动词的丰富度也略低（具体差距可在示例文件中查看）。

### 5. 验证方法
仓库中的每一条规则均经过相同的盲测验证：让模型仅根据获奖论文某一节的大纲起草正文，将生成稿与发表原文直接对照阅读；凡未能在对照阅读中展现正向效果的规则，均已被剔除。

---

## 安装与使用

### 安装 Skill

**Claude Code：**
```bash
git clone https://github.com/Fwibo/ml-paper-humanizer ~/.claude/skills/ml-paper-humanizer
```

**Codex CLI：**
```bash
git clone https://github.com/Fwibo/ml-paper-humanizer ~/.codex/skills/ml-paper-humanizer
```

* **其他 AI Coding Agent：** 凡支持加载 Agent Skills（即读取含 `SKILL.md` 的目录）的工具，可直接指向同一文件夹。
* **claude.ai 网页版：** 将本仓库文件夹打包为 `.zip`，在 `Settings → Capabilities → Skills` 中上传即可。

### 环境依赖

基础检查脚本与范文抽取仅需 **Python 3**。若需使用自动术语候选提取（依赖 `spaCy`）及引用 PDF 解析（依赖 `PyMuPDF`），请安装可选依赖（未安装时，术语表将由模型提取并交由脚本逐字核验）：

```bash
pip install spacy pymupdf && python -m spacy download en_core_web_sm
```

### 触发示例

用自然语言（中文或英文）直接提出写作、修改或诊断请求即可触发：

* `"把 results 第二段改一下，读着像 AI 写的。"`
* `"按这些笔记写 introduction，这是一篇 discovery 类的论文。"`
* `"这个摘要太防御了，改一下。"`
* `"先别改，告诉我这一节哪里有问题。"`
* `"/ml-paper-humanizer sec/experiments.tex"`

配套工具脚本也可在命令行下独立运行：

```bash
# 运行文档级异常重复与结构检查
python scripts/check_tex.py paper/ --ledger ledger.json

# 从 LaTeX 源码及引用 PDF 中提取并核验术语表
python scripts/term_ledger.py paper/main.tex --cited refs/*.pdf --out ledger.json

# 按章节类型与论文取向抽取三段顶会范文
python scripts/pick_exemplars.py results --orientation discovery
```

---

## 仓库结构

```text
SKILL.md                      核心指令：七步工作流、读者需求、回读核查表与输出契约
references/
  section-playbook.md         按论文取向划分的各章节（从 Abstract 到 Rebuttal）写作任务框架
  sentence-bank.md            40 组模型初稿与顶会原文的病句对照（按问题分类）及 23 句动作范例
  register-frames.md          1,234 条按句子功能分类的顶会高频句式（附出现篇数统计）
  connectives.md              权威写作指南要点，以及因果、对比、让步的标准表达形式
  claim-strength.md           Reporting verb 强度分级表，区分设计意图与实验结果
  exemplars/                  取自 30 篇顶会论文的 144 段引言与实验范文，附 SOURCES.md
scripts/
  check_tex.py                基于文档自身分布的无阈值重复与结构检查脚本
  term_ledger.py              从正文与引用 PDF 提取术语候选；--verify 仅保留逐字匹配的术语
  pick_exemplars.py           按章节类型和论文取向抽取三段参考范文
examples/
  results-2504.13837.md       完整实验章节对比：不用 Skill、使用 Skill 与发表原文
  compare.html, compare*.png  README 顶部的对比图及用于渲染该图的 HTML 源码
```

---

## 来源与许可

* **代码与规则许可：** 本 Skill 自身（含 `SKILL.md`、各类脚本及为此编写的参考规则文件）基于 **MIT License** 开源，详见 `LICENSE`。
* **语料与范文版权：** 范文库（`references/exemplars/`）收录的 30 篇论文短节选均遵循 **CC BY 4.0** 或 **CC0 1.0** 协议，具体来源与许可详见 `references/exemplars/SOURCES.md`。例句库（`sentence-bank.md`）引用的获奖论文单句均在文末 Sources 章节列出了原论文及许可。所有引文版权归原作者所有。节选中的文献引用与交叉引用已脱敏替换为 `[cite]` 和 `REF`，且 Skill 明确限制模型严禁复用范文中的内容或任何连续六个词以上的原文片段。句式表与连接词表仅包含短语结构与统计计数。
* **致谢：** "围绕论文实际成果行文，而非围绕每一条潜在审稿质疑做防御"的理念启发自 [anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill)（MIT）。此外，[humanizer](https://github.com/blader/humanizer) 致力于依据维基百科总结的"AI 写作特征"洗掉通用文本的 AI 痕迹；而本仓库仅专注于 **ML 学术论文**，且所有规则均直接从顶会论文本身提炼而来。
