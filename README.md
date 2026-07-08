# SuperMemo Companion

**Internalize what you think with. Offload what you merely consult.**

An agent-agnostic kit that turns any capable AI assistant into a disciplined
learning companion for [SuperMemo](https://super-memory.com/) users: it
decides *with* you what deserves lifelong memory, formulates high-quality
items, and coaches you on the tool itself.

**English** · [中文](#supermemo-companion--中文版)

---

## Why this exists

> AI changes the economics of retrieval, but not the mechanics of thought.
> Learners should internalize what they need to think with, and offload what
> they merely need to consult.

Since AI can now explain almost anything on demand, it is tempting to
conclude that memorization is obsolete. That conclusion confuses two
different kinds of knowledge. Knowledge in the world is **inert** — it does
nothing until you query it. Knowledge in your head is **executable** — it
runs inside perception, comprehension, and judgment without being asked. A
chess master doesn't *recall* patterns; she *sees* the board differently.
No external oracle changes this, because the oracle sits on the wrong side
of your eyes.

Three things follow:

1. **You can't query what you can't name.** Good questions are made of
   internalized concepts. Whoever lacks the map of a domain cannot even ask
   about its territory.
2. **Generation is cheap now, so discrimination is the scarce skill.** AI
   produces fluent answers, including fluent wrong ones. Evaluating them
   requires internal anchors — mechanisms, orders of magnitude, failure
   modes. If everything is offloaded, you have no basis for doubt.
3. **Insight is collision.** Creative connections happen between pieces of
   knowledge resident in the same brain. Material you could look up but
   never internalized never participates.

The calculator is the template: it killed arithmetic drill but *raised* the
price of number sense. AI automates verbal-procedural work and raises the
price of domain sense. So the answer is not "memorize less" — it is
**fewer items, deeper domains, better cards**. AI is a multiplier on what
you know, and a multiplier is worth more the more it has to multiply.

That's what this kit operationalizes: the AI serves your memory, instead of
replacing it.

## The model: four destinations for any piece of knowledge

| Bucket | Meaning | What happens |
|---|---|---|
| **MEMORIZE** | You need it to *think with*: at conversation speed, as a foundation, as a judgment anchor | 1–3 SuperMemo items |
| **MAP** | You need to know it *exists*: what problem it solves, when it applies, where details live | exactly 1 "map card" |
| **OFFLOAD** | You merely need to *consult* it: retrievable in under a minute, verifiable on the spot | no cards; AI/reference at point of use |
| **DISCARD** | No plausible use, no connective value | nothing — deliberately |

## The seven tests

Applied to each knowledge unit during triage:

1. **Latency** — needed at the speed of thought, or is an under-a-minute
   lookup always acceptable?
2. **Foundation** — does the rest of the domain make sense without it?
3. **Map** — does knowing it exists change what you can ask?
4. **Judgment** — will you use it to sanity-check AI or human output?
5. **Collision** — do you want it available for background thinking and
   creative connection?
6. **Half-life** — will it still be true in 5–10 years? (Spaced repetition
   is a lifetime investment; buy assets that don't depreciate.)
7. **Desire** — do you simply want it to be part of you? Desire overrides
   every efficiency argument.

On top of the tests, triage applies one plainly economic check: anything you
use weekly or more earns memorization outright.

Verdicts are **role-relative**: the same fact is MEMORIZE for the surgeon
and OFFLOAD for the patient. Latency and stakes decide, not the fact.

## What this changes in practice

**Stop memorizing:** tool syntax and flags, API signatures, config formats,
exact values where an anchor suffices, step-by-step procedures always
performed with the tool open, framework-of-the-week details, isolated
trivia.

**Keep (or start) memorizing:** the vocabulary and ontology of your working
domains, mechanisms and causal models, X-vs-Y discriminations, canonical
examples and failure modes, orders of magnitude and base rates, foreign
languages (the purest latency case), and depth in your core profession —
details included, because fluency compounds.

## What's in this repository

```
AGENTS.md                        ← agent entry point (tool-agnostic)
CLAUDE.md                        ← pointer for older Claude Code versions
skills/
  triage/SKILL.md                ← sort material into the four buckets
  formulate/SKILL.md             ← turn verdicts into import-ready items
  supermemo-coach/
    SKILL.md                     ← answer any "how do I … in SuperMemo?"
    reference.md                 ← distilled SuperMemo reference (offline)
examples/
  LEARNER.example.md             ← personal profile template
  sample-session.md              ← what a good triage session looks like
  sample-cards.txt               ← import-ready Q&A file, all card types
cards/                           ← your generated card files land here (gitignored)
```

The instruction files are in English (most reliable across models); the
agent converses and writes cards in **your** language.

## Quick start

1. Clone this repository (or copy its files into your study folder). It is
   designed to *be* your study workspace: drop reading material in, keep
   generated cards in `cards/`.
2. Copy `examples/LEARNER.example.md` to `LEARNER.md` and fill it in
   (2 minutes — it's what makes triage personal).
3. Open your agent in the folder:

| Tool | Setup |
|---|---|
| **Claude Code** | none — reads `AGENTS.md` (older versions read `CLAUDE.md`) |
| **Codex CLI** | none — reads `AGENTS.md` |
| **OpenCode** | none — reads `AGENTS.md` |
| **Cursor** | recent versions read `AGENTS.md`; otherwise add it as a project rule |
| **Anything else** | say once: *"Read AGENTS.md and follow it"* — any agent that can read files qualifies |

4. First prompts to try:
   - *"Help me learn this article: …"* (triage → cards)
   - *"Should I memorize the OSI layers?"*
   - *"Here are 15 items from my collection that keep lapsing — audit them."*
   - *"How do incremental reading priorities actually work?"*

No frontier model required: the skills are deliberately mechanical —
checklists, ordered decision rules, fixed output formats — so a mid-tier
model (Sonnet-class) follows them reliably.

## The workflow, end to end

1. **Capture.** Bring material to the agent: an article, chapter, lecture
   transcript, your notes, or something the agent itself just explained.
2. **Triage.** The agent decomposes it into knowledge units and sorts them
   into the four buckets, sized against your daily review budget. Expect
   pushback — "not worth memorizing" is the product working.
3. **Formulate.** Approved units become atomic items — mechanisms,
   discriminations, judgment cards, anchors — delivered as a Q&A text file
   in `cards/`.
4. **Import.** In SuperMemo: **File : Import : Q&A text** → select the file
   → set honest priorities (**Alt+P**; 0% is *highest*, and most material
   isn't top-priority).
5. **Learn daily.** **Ctrl+L**, grade honestly, keep
   `Learn : Sorting : Auto-sort repetitions` and
   `Learn : Postpone : Auto-postpone` enabled and overload takes care of
   itself.
6. **Read incrementally** (optional but powerful): import articles into
   SuperMemo (**Ctrl+N** paste, **Shift+F8** web import), extract with
   **Alt+X**, cloze with **Alt+Z** — and bring stubborn or bloated items
   back to the agent for reformulation.
7. **Audit.** Monthly: export or paste problem items, run the collection
   audit, retire aggressively. Every retired item is reclaimed review time,
   forever.

Questions at any step — shortcuts, priorities, leeches, statistics, version
differences — go to the coach skill, which answers from a distilled offline
reference and points to [help.supermemo.org](https://help.supermemo.org)
for rare edge cases.

## SuperMemo in ten lines

- SuperMemo (SuperMemo World, Windows) pioneered spaced repetition in 1987;
  this kit targets **SuperMemo 17–20**.
- **Items** are question–answer pairs you actively recall; **topics** are
  reading material you passively review; both live as *elements* in one
  collection (keep exactly one collection).
- Daily learning = **Ctrl+L**; grade each answer honestly; the algorithm
  spaces the next review just before you'd forget (default forgetting
  index: 10%).
- New material first comes due 3–5 days after you add it — an empty queue
  in the first days is normal.
- **Priority queue**: every element has a priority from 0% (highest) to
  100%; under overload, low priority is sacrificed first — prioritize
  honestly.
- **Incremental reading**: import articles, read a little, extract
  (**Alt+X**) what matters, turn one-sentence extracts into clozes
  (**Alt+Z**), let the queue interleave everything.
- Items that keep lapsing are **leeches**: reformulate or delete; don't
  grind.
- Back up your collection (**Shift+Ctrl+C**) regularly — it's years of your
  memory.
- SuperMemo 20 ships built-in AI (`AI : Explain`) — the ecosystem itself is
  converging on AI-assisted learning; this kit is the workflow layer above
  it.
- Everything else: ask the coach skill, or see the
  [official documentation](https://help.supermemo.org).

## Design principles

- **Portable.** One entry point (`AGENTS.md`), plain markdown skills loaded
  by file path, no tool-specific features. Works in any agent that can read
  files.
- **Lightweight by intent.** Three skills, no meta-framework, no state
  beyond one optional `LEARNER.md`. Ordered rules and fixed output formats
  instead of judgment-heavy prose, so smaller models stay reliable.
- **Self-contained.** SuperMemo guidance is distilled into
  `skills/supermemo-coach/reference.md` from the official documentation —
  users don't need a local docs mirror. Version-specific edge cases are
  explicitly deferred to help.supermemo.org rather than guessed.
- **Opinionated where it counts.** The kit refuses to card offload-grade
  material. That refusal *is* the product.

## FAQ

**Does AI make spaced repetition obsolete?**
No — it makes it more valuable. AI is the best explainer you'll ever have,
but understanding you don't retain evaporates in weeks (the fluency
illusion). AI makes understanding cheap; SuperMemo makes it permanent. They
are complements: one produces, the other installs.

**Can I use this with Anki or other SRS?**
The philosophy, triage, and formulation principles transfer completely. The
import format and tool coaching are SuperMemo-specific — ask the agent for
TSV output and it will oblige, but the coach skill won't know Anki's UI.

**Why not just auto-generate cards from everything I read?**
Card generation was never the bottleneck — review time is. Every card is a
years-long stream of future repetitions. The triage step exists to spend
that budget on knowledge you'll think with.

**Which model do I need?**
Any competent mid-tier model. The skills were written so that Sonnet-class
models follow them reliably; stronger models simply triage with better
judgment.

**Privacy?**
Material you triage is sent to whatever model powers your agent. Keep that
in mind for sensitive notes; `LEARNER.md` is gitignored by default.

**Is this affiliated with SuperMemo World?**
No. Unofficial, unendorsed. SuperMemo is a trademark of SuperMemo World.
Method concepts here are distilled from the official wiki
(help.supermemo.org) and Piotr Wozniak's writings, with attribution and
gratitude.

## Contributing

Issues and PRs welcome. Useful contributions: better worked examples,
translations of the README, corrections to the SuperMemo reference (cite
the official wiki page), adapters for more agent environments. Keep the
design lightweight — the bar for adding a fourth skill is high.

## License

MIT. See [LICENSE](LICENSE).

Formulation principles adapted from Piotr Wozniak,
[*Effective learning: Twenty rules of formulating knowledge*](https://super-memory.com/articles/20rules.htm).
SuperMemo usage facts distilled from the
[official SuperMemo documentation](https://help.supermemo.org).

---

# SuperMemo Companion — 中文版

**内化所思，外包所查。**

一个与具体 AI 工具无关的开源套件：把任何一个能干的 AI 助手，变成 SuperMemo
学习者的严格把关的学习伴侣——和你一起决定哪些知识值得终身记忆、生成高质量
的记忆卡片，并解答 SuperMemo 使用中的一切问题。

[English](#supermemo-companion) · **中文**

---

## 为什么做这个项目

> AI 改变的是知识检索的经济学，而不是思考的机制。
> 学习者应当内化自己赖以思考的知识，把只需查询的知识交给外部工具。

既然 AI 随时能解释几乎一切，“背诵已经过时”似乎顺理成章。但这个结论混淆了两
种不同的知识。存在于外部世界的知识是**惰性的**——不去查询，它什么也不做；
存在于头脑中的知识是**可执行的**——它不经调用就直接参与感知、理解和判断。
棋手不是“回忆”棋型，而是直接“看见”不同的棋盘。再好的外部神谕也改变不了这
一点，因为神谕永远站在你眼睛的外面。

由此推出三件事：

1. **你无法查询你叫不出名字的东西。** 好问题由内化了的概念构成。没有领域
   地图的人，连提问都无从下手。
2. **生成已经廉价，鉴别才是稀缺技能。** AI 输出流畅的答案，也输出流畅的错
   误答案。评估它们需要内在的锚点——机制、数量级、典型失败模式。如果一切
   都外包了，你连怀疑的依据都没有。
3. **洞见来自碰撞。** 创造性的联结发生在同一个大脑里的知识之间。查得到但
   从未内化的材料，永远不会参与碰撞。

计算器是最好的先例：它消灭了笔算训练，却**抬高**了数感的价格。AI 自动化了
语言性、程序性的工作，也就抬高了“领域感”的价格。所以答案不是“少记”，而是
**更少的条目、更深的领域、更好的卡片**。AI 是你已有知识的乘数——被乘数越
大，乘数才越值钱。

这个套件要做的，就是让 AI 为你的记忆服务，而不是取代它。

## 学习模型：任何一条知识的四个去向

| 去向 | 含义 | 处理方式 |
|---|---|---|
| **深度记忆 MEMORIZE** | 你要“用它思考”：需要即时反应、是领域地基、是判断锚点 | 生成 1–3 张 SuperMemo 卡片 |
| **地图级 MAP** | 你只需知道“它存在”：解决什么问题、何时适用、细节在哪 | 恰好 1 张“地图卡” |
| **外包 OFFLOAD** | 你只需“查询它”：一分钟内可查到、当场可验证 | 不做卡片，用时问 AI / 查资料 |
| **舍弃 DISCARD** | 没有可预见的用途，也没有联结价值 | 有意识地放弃 |

## 七个判断测试

分诊（triage）时对每个知识单元逐一提问：

1. **时延** —— 需要以思考的速度调用，还是每次都来得及花一分钟去查？
2. **地基** —— 没有它，这个领域的其他内容还能理解吗？
3. **地图** —— 知道它的存在，是否改变了你能提出的问题？
4. **判断** —— 你会用它来校验 AI（或他人）的输出吗？
5. **碰撞** —— 你希望它参与后台思考和创造性联结吗？
6. **半衰期** —— 5–10 年后它还成立吗？（间隔重复是终身投资，要买不贬值的资产。）
7. **热爱** —— 你就是想让它成为自己的一部分吗？热爱压倒一切效率论证。

在七个测试之外，分诊还会叠加一条纯经济学检查：凡是每周都会用到的知识，直接
值得记忆。

判决是**因人而异的**：同一条知识，对外科医生是 MEMORIZE，对患者是
OFFLOAD。决定因素是时延与利害，而不是知识本身。

## 实践中的取舍

**停止记忆：** 工具语法和参数、API 签名、配置文件格式、有锚点即可的精确数
值、永远开着工具执行的分步操作、月抛型框架细节、孤立的冷知识。

**保持（或开始）记忆：** 工作领域的术语与本体、机制与因果模型、“X 与 Y 何
时用哪个”的辨析、典型例子与失败模式、数量级与基础比率、外语（最纯粹的时延
场景），以及核心专业领域的纵深——细节也值得，因为熟练度会复利。

## 仓库内容

```
AGENTS.md                        ← Agent 入口（与具体工具无关）
CLAUDE.md                        ← 兼容旧版 Claude Code 的指针文件
skills/
  triage/SKILL.md                ← 把材料分诊到四个去向
  formulate/SKILL.md             ← 把判决变成可直接导入的卡片
  supermemo-coach/
    SKILL.md                     ← 解答一切 “SuperMemo 里怎么做？”
    reference.md                 ← 提炼后的 SuperMemo 离线参考
examples/
  LEARNER.example.md             ← 个人学习档案模板
  sample-session.md              ← 一次标准分诊会话的样例
  sample-cards.txt               ← 可直接导入的 Q&A 示例卡片（覆盖全部卡片类型）
cards/                           ← 生成的卡片文件放这里（已 gitignore）
```

指令文件用英文书写（对各类模型最稳定），但 Agent 会用**你的语言**交流和
写卡片。

## 快速开始

1. 克隆本仓库（或把文件复制进你的学习目录）。它本身就是为“学习工作区”设计
   的：阅读材料放进来，生成的卡片留在 `cards/`。
2. 把 `examples/LEARNER.example.md` 复制为根目录的 `LEARNER.md` 并填写
   （2 分钟——分诊的个性化全靠它）。
3. 在此目录打开你的 Agent：

| 工具 | 设置 |
|---|---|
| **Claude Code** | 无需设置——自动读取 `AGENTS.md`（旧版读 `CLAUDE.md`） |
| **Codex CLI** | 无需设置——自动读取 `AGENTS.md` |
| **OpenCode** | 无需设置——自动读取 `AGENTS.md` |
| **Cursor** | 新版本支持 `AGENTS.md`；否则将其添加为项目规则 |
| **其他任何工具** | 说一句：*“阅读 AGENTS.md 并遵循它”*——凡能读文件的 Agent 都可以 |

4. 可以先试这些提示：
   - “帮我学习这篇文章：……”（分诊 → 卡片）
   - “OSI 七层模型值得背吗？”
   - “这是我收藏里反复遗忘的 15 个条目，帮我审计一下。”
   - “渐进阅读的优先级到底是怎么运作的？”

不需要最贵的前沿模型：技能文件刻意写得足够机械——清单、有序判定规则、固
定输出格式——中档模型（Sonnet 级）即可稳定执行。

## 端到端工作流

1. **收集。** 把材料交给 Agent：文章、书的章节、课程讲稿、你的笔记，或
   Agent 刚刚给你的一段讲解。
2. **分诊。** Agent 把材料拆成知识单元，按四个去向分类，并对照你的每日复习
   预算控制总量。请习惯被它拒绝——“这个不值得背”正是产品在起作用。
3. **制卡。** 通过的单元被写成原子化卡片——机制卡、辨析卡、判断卡、锚点
   卡——以 Q&A 文本文件的形式存入 `cards/`。
4. **导入。** 在 SuperMemo 中：**File : Import : Q&A text** → 选择文件 →
   诚实地设置优先级（**Alt+P**；0% 是*最高*优先级，而大多数材料并不配）。
5. **每日学习。** **Ctrl+L**，诚实评分；保持
   `Learn : Sorting : Auto-sort repetitions` 与
   `Learn : Postpone : Auto-postpone` 开启，积压问题会自动化解。
6. **渐进阅读**（可选但强大）：把文章导入 SuperMemo（**Ctrl+N** 粘贴、
   **Shift+F8** 网页导入），**Alt+X** 摘录，**Alt+Z** 挖空；难啃或臃肿的
   条目拿回来让 Agent 重新表述。
7. **审计。** 每月一次：导出或粘贴问题条目，跑一遍收藏审计，大胆退役。每
   退役一张卡，就永久收回一份复习时间。

过程中的任何问题——快捷键、优先级、水蛭条目（leech）、统计、版本差异——
都交给 coach 技能，它依据一份离线提炼的参考作答，罕见边缘情况会明确指向
[help.supermemo.org](https://help.supermemo.org)。

## 十行看懂 SuperMemo

- SuperMemo（SuperMemo World 出品，Windows 平台）1987 年开创间隔重复；本
  套件面向 **SuperMemo 17–20**。
- **Item（项目）**是需要主动回忆的问答对；**Topic（主题）**是被动复习的阅
  读材料；二者都是同一个收藏（collection）中的元素——并且请只用一个收藏。
- 每日学习 = **Ctrl+L**；对每个答案诚实评分；算法把下次复习安排在你即将遗
  忘之前（默认遗忘指数 10%）。
- 新材料要在添加后 3–5 天才首次到期——头几天队列是空的，属于正常现象。
- **优先级队列**：每个元素的优先级从 0%（最高）到 100%；积压时先牺牲低优
  先级——所以要诚实定级。
- **渐进阅读**：导入文章，读一点，**Alt+X** 摘录要点，把单句摘录用
  **Alt+Z** 变成挖空题，让队列自动穿插一切。
- 反复遗忘的条目叫**水蛭（leech）**：重新表述或删除，不要硬磨。
- 定期备份收藏（**Shift+Ctrl+C**）——那是你多年的记忆。
- SuperMemo 20 已内置 AI（`AI : Explain`）——生态本身正在走向 AI 辅助学
  习；本套件是位于其上的工作流层。
- 其余一切：问 coach 技能，或查阅
  [官方文档](https://help.supermemo.org)。

## 设计原则

- **可移植。** 单一入口（`AGENTS.md`），技能是按路径加载的纯 Markdown，不
  依赖任何工具特有功能。凡能读文件的 Agent 都能用。
- **刻意轻量。** 三个技能，没有元框架，除一个可选的 `LEARNER.md` 外没有任
  何状态。用有序规则和固定输出格式取代依赖悟性的长文，小模型也能稳定执行。
- **自包含。** SuperMemo 使用指导已从官方文档提炼进
  `skills/supermemo-coach/reference.md`，用户无需本地文档镜像；版本相关的
  边缘情况明确交给 help.supermemo.org，而不是猜。
- **在关键处有立场。** 本套件会拒绝为“外包级”材料制卡。这种拒绝本身就是产
  品。

## 常见问题

**AI 会让间隔重复过时吗？**
不会——反而更有价值。AI 是你能拥有的最好的讲解者，但没有留存的理解几周内
就蒸发（流畅性错觉）。AI 让理解变得便宜；SuperMemo 让理解变得永久。它们是
互补品：一个负责生产，一个负责安装。

**能配合 Anki 或其他间隔重复软件用吗？**
理念、分诊和制卡原则完全通用。导入格式与工具指导是 SuperMemo 专属的——让
Agent 输出 TSV 它也照办，但 coach 技能不了解 Anki 的界面。

**为什么不把我读的所有东西自动做成卡片？**
瓶颈从来不是做卡，而是复习时间。每张卡都是一条持续多年的未来复习流。分诊
这一步的意义，就是把预算花在你会用来思考的知识上。

**需要多强的模型？**
任何称职的中档模型即可。技能文件按 Sonnet 级模型可稳定执行的标准编写；更
强的模型只是分诊判断更好。

**隐私？**
你交给 Agent 分诊的材料会发送给驱动它的模型服务。敏感笔记请自行斟酌；
`LEARNER.md` 默认已被 gitignore。

**与 SuperMemo World 有关系吗？**
没有。非官方、未获背书。SuperMemo 是 SuperMemo World 的商标。本项目的方法
性内容提炼自官方 wiki（help.supermemo.org）与 Piotr Wozniak 的著述，谨致
谢意。

## 参与贡献

欢迎 Issue 和 PR。有价值的方向：更好的示例、README 翻译、对 SuperMemo 参
考内容的勘误（请引用官方 wiki 页面）、更多 Agent 环境的适配说明。请保持设
计轻量——增加第四个技能的门槛应当很高。

## 许可证

MIT，见 [LICENSE](LICENSE)。

制卡原则改编自 Piotr Wozniak
[《高效学习：表述知识的二十条规则》](https://super-memory.com/articles/20rules.htm)；
SuperMemo 使用事实提炼自[官方文档](https://help.supermemo.org)。
