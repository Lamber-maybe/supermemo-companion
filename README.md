# SuperMemo Companion

**Internalize what you think with. Offload what you merely consult.**

An agent-agnostic kit that turns any capable AI assistant into a coach at
the side of your [SuperMemo](https://super-memory.com/) practice — never a
substitute for it. It answers four questions:

1. **"Why still learn — and learn *what* — now that AI explains
   everything?"** Direction advice grounded in an explicit philosophy of
   AI-era learning.
2. **"Is this worth importing / memorizing?"** A gatekeeper in front of
   your collection, so review time is spent on knowledge you'll think with.
3. **"How should I extract or cloze this passage?"** Craft advice
   mid-incremental-reading — suggestions you apply yourself, plus the rule
   behind them.
4. **"How do I … in SuperMemo?"** Tool coaching answered from the official
   documentation, never from guesswork.

And it refuses one job: **doing your reading for you**. It lowers
SuperMemo's learning curve — never the learning itself.

**English** · [中文](#supermemo-companion--中文版)

---

## Why this exists

> AI changes the economics of retrieval, but not the mechanics of thought.
> Learners should internalize what they need to think with, and offload what
> they merely need to consult.

Since AI can now explain almost anything on demand, it is tempting to
conclude that learning is obsolete. That conclusion confuses two different
kinds of knowledge. Knowledge in the world is **inert** — it does nothing
until you query it. Knowledge in your head is **executable** — it runs
inside perception, comprehension, and judgment without being asked. A chess
master doesn't *recall* patterns; she *sees* the board differently. No
external oracle changes this, because the oracle sits on the wrong side of
your eyes.

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
price of domain sense. So the answer is not "learn less" — it is
**fewer items, deeper domains, better cards**. AI is a multiplier on what
you know, and a multiplier is worth more the more it has to multiply.

That's what this kit operationalizes: the AI serves your memory, instead of
replacing it.

## What should you learn, then?

Three rules of thumb for direction, before any list:

- **Deep beats broad.** AI rewards the person with the most to multiply;
  seventeen shallow hobbies multiply nothing.
- **Durable beats volatile.** Spaced repetition is a lifetime investment —
  buy assets that don't depreciate.
- **Loved beats dutiful.** Long learning runs on joy; a dutiful plan dies
  in three weeks. (This is also why the kit refuses to automate the fun
  part.)

**Stop memorizing:** tool syntax and flags, API signatures, config formats,
exact values where an anchor suffices, step-by-step procedures always
performed with the tool open, framework-of-the-week details, isolated
trivia.

**Keep (or start) memorizing:** the vocabulary and ontology of your working
domains, mechanisms and causal models, X-vs-Y discriminations, canonical
examples and failure modes, orders of magnitude and base rates, foreign
languages (the purest latency case), and depth in your core profession —
details included, because fluency compounds.

## The model: four destinations for any piece of knowledge

| Bucket | Meaning | What happens |
|---|---|---|
| **MEMORIZE** | You need it to *think with*: at conversation speed, as a foundation, as a judgment anchor | you make 1–3 items in SuperMemo |
| **MAP** | You need to know it *exists*: what problem it solves, when it applies, where details live | exactly 1 "map card" |
| **OFFLOAD** | You merely need to *consult* it: retrievable in under a minute, verifiable on the spot | no cards; AI/reference at point of use |
| **DISCARD** | No plausible use, no connective value | nothing — deliberately |

## The seven tests

Applied to each knowledge unit when you ask "is this worth memorizing?":

1. **Latency** — needed at the speed of thought, or is an under-a-minute
   lookup always acceptable?
2. **Foundation** — does the rest of the domain make sense without it?
3. **Map** — does knowing it exists change what you can ask?
4. **Judgment** — will you use it to sanity-check AI or human output?
5. **Collision** — do you want it available for background thinking and
   creative connection?
6. **Half-life** — will it still be true in 5–10 years? (Buy assets that
   don't depreciate.)
7. **Desire** — do you simply want it to be part of you? Desire overrides
   every efficiency argument.

On top of the tests, one plainly economic check: anything you use weekly or
more earns memorization outright.

Verdicts are **role-relative**: the same fact is MEMORIZE for the surgeon
and OFFLOAD for the patient. Latency and stakes decide, not the fact.

## The boundary: what this kit will not do

- It will **not read, summarize, extract, or card an article for you.**
  Bring the passage you're stuck on and it advises; hand it a whole article
  and it hands it back — with a worth-importing verdict if you want one.
- It will **not mass-generate cards.** It suggests wording; you make the
  card. Choosing what matters and formulating it *are* the learning —
  automate them away and what remains is a deck you don't own and review
  debt you do.
- Two deliberate exceptions, on explicit request only: **repairing items
  you already own** (failing items come back as old → new rewrites; a whole
  exported batch comes back as a rewrites-only import file), and
  **mechanical batches with no reading to steal** (a vocabulary list, your
  own notes). Maintenance is not outsourcing.

Why so strict? Understanding you don't retain evaporates (the fluency
illusion); retention you didn't build yourself is a deck of someone else's
thoughts. And incremental reading is *fun* — the flow belongs to you, not
to the tool.

## What's in this repository

```
AGENTS.md                        ← agent entry point (tool-agnostic)
CLAUDE.md                        ← pointer for older Claude Code versions
skills/
  worth-learning/SKILL.md        ← direction · import gatekeeping · memorize-or-not
  reading-advisor/SKILL.md       ← extract/cloze/wording advice · item repair
  supermemo-coach/
    SKILL.md                     ← answer any "how do I … in SuperMemo?"
    reference.md                 ← distilled SuperMemo reference (offline)
    incremental-learning.md      ← the method's philosophy, distilled
docs/
  wiki/ · wiki-zh/               ← the full official wiki, crawled (EN ~210 pages + ZH, offline)
  articles/20rules.htm           ← Wozniak's formulation-rules article
examples/
  LEARNER.example.md             ← personal profile template
  sample-session.md              ← what good sessions look like
cards/                           ← repair files from the leech clinic (gitignored)
```

The instruction files are in English (most reliable across models); the
agent converses in **your** language.

## Quick start

1. Clone this repository (or copy its files into your study folder).
2. Copy `examples/LEARNER.example.md` to `LEARNER.md` and fill it in
   (2 minutes — it's what makes the verdicts personal). The full official
   wiki already ships in `docs/`; only if you keep your own fresher crawl,
   put its path in the `Docs mirror` field and it takes precedence.
3. Open your agent in the folder:

| Tool | Setup |
|---|---|
| **Claude Code** | none — reads `AGENTS.md` (older versions read `CLAUDE.md`) |
| **Codex CLI** | none — reads `AGENTS.md` |
| **OpenCode** | none — reads `AGENTS.md` |
| **Cursor** | recent versions read `AGENTS.md`; otherwise add it as a project rule |
| **Anything else** | say once: *"Read AGENTS.md and follow it"* — any agent that can read files qualifies |

4. First prompts to try:
   - *"What's still worth learning deeply, now that AI can explain
     anything?"*
   - *"Is this article worth importing into SuperMemo?"* (paste it or link
     it)
   - *"I'm reading this paragraph and don't know what to extract —
     suggestions?"*
   - *"How do I cloze this extract?"*
   - *"How do incremental reading priorities actually work?"*

No frontier model required: the skills are deliberately mechanical —
checklists, ordered decision rules, fixed output shapes — so a mid-tier
model (Sonnet-class) follows them reliably.

## The loop, end to end

0. **Direction** (occasionally). "What should I go deep on?" — the
   companion argues from durability, leverage, judgment, and desire, then
   asks you to bring one concrete chapter or article.
1. **Gatekeep.** Before anything enters SuperMemo, ask "worth importing?"
   You get IMPORT (with a suggested priority) / IMPORT PART / READ OUTSIDE /
   SKIP — with the AI-era reason. Expect refusals: "not worth your review
   time" is the product working.
2. **Read incrementally — yourself.** In SuperMemo: import (**Ctrl+N**
   paste, **Shift+F8** web import), set an honest priority (**Alt+P**),
   read a little, extract what matters (**Alt+X**), cloze single sentences
   (**Alt+Z**), stop early on purpose. When you're unsure *what* to extract
   or *how* to cloze, paste the passage to the companion — you get concrete
   suggestions plus the rule behind them, and then **you** press the keys.
3. **Ask anything mid-flight.** Explanations are welcome — that's what AI
   is best at. After explaining, the companion offers once: "worth keeping?
   I can suggest a card wording; you add it." Understanding is cheap now;
   only what you install survives.
4. **Repair what fails.** An item keeps failing → paste it with a one-line
   symptom ("failed 5×", "I keep answering X") → you get an old → new
   rewrite to paste into the *same* element (**E** to edit; **Ctrl+M** to
   restart its schedule). Monthly: **Shift+F3** collects leeches into a
   browser; export via `Export : Q&A text file`, hand the file over, get
   verdicts plus a rewrites-only import file, then dismiss the originals
   (`Process browser> : Learning : Dismiss`). Every retired item is
   reclaimed review time, forever.
5. **Coach on call.** Shortcuts, priorities, statistics, version quirks,
   design rationale — answered from the distilled offline reference and
   the full official wiki bundled in `docs/`, with
   [help.supermemo.org](https://help.supermemo.org) as the final authority.

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
  converging on AI-assisted learning; this kit is the discipline layer
  above it.
- Everything else: ask the coach skill, or see the
  [official documentation](https://help.supermemo.org).

## Design principles

- **Portable.** One entry point (`AGENTS.md`), plain markdown skills loaded
  by file path, no tool-specific features. Works in any agent that can read
  files.
- **Lightweight by intent.** Three skills, no meta-framework, no state
  beyond one optional `LEARNER.md`. Ordered rules and fixed output shapes
  instead of judgment-heavy prose, so smaller models stay reliable.
- **Docs-grounded.** Tool answers come from a distilled offline reference
  (`skills/supermemo-coach/reference.md`) plus a philosophy digest
  (`incremental-learning.md`), both backed by the complete official wiki
  bundled in `docs/` (~210 pages, EN + ZH) — the online wiki sits behind
  a Cloudflare challenge, so the repo carries its own ground truth, with
  help.supermemo.org as the final authority. The coach never guesses a
  shortcut.
- **A coach, not a chauffeur.** It refuses to card offload-grade material,
  and it refuses to read or formulate *for* you. Both refusals are the
  product.

## FAQ

**Does AI make spaced repetition obsolete?**
No — it makes it more valuable. AI is the best explainer you'll ever have,
but understanding you don't retain evaporates in weeks (the fluency
illusion). AI makes understanding cheap; SuperMemo makes it permanent. They
are complements: one produces, the other installs.

**Why won't it just read my article and make the cards?**
Because those two steps — choosing what matters and formulating it — are
where the learning happens, and because every card is a years-long stream
of future reviews that *you* will pay for. Card generation was never the
bottleneck; review time is. The narrow exceptions (repairing your own
failing items; mechanical batches like vocabulary lists) exist because
there the learning is in the reviews, not in the typing.

**Can I use this with Anki or other SRS?**
The philosophy, the gatekeeping, and the formulation principles transfer
completely. The tool coaching and incremental-reading advice are
SuperMemo-specific — Anki has no real incremental reading, which is
precisely why this kit targets SuperMemo.

**Which model do I need?**
Any competent mid-tier model. The skills were written so that Sonnet-class
models follow them reliably; stronger models simply judge with better
taste.

**Privacy?**
Material you show the companion is sent to whatever model powers your
agent. Keep that in mind for sensitive notes; `LEARNER.md` is gitignored by
default.

**Is this affiliated with SuperMemo World?**
No. Unofficial, unendorsed. SuperMemo is a trademark of SuperMemo World.
Method concepts here are distilled from the official wiki
(help.supermemo.org) and Piotr Wozniak's writings, with attribution and
gratitude.

## Contributing

Issues and PRs welcome. Useful contributions: better worked examples,
translations of the README, corrections to the SuperMemo reference (cite
the official wiki page), adapters for more agent environments. Keep the
design lightweight — the bar for adding a fourth skill is high, and the bar
for adding automation that replaces the learner's own reading is infinite.

## License

MIT. See [LICENSE](LICENSE).

Formulation principles adapted from Piotr Wozniak,
[*Effective learning: Twenty rules of formulating knowledge*](https://super-memory.com/articles/20rules.htm).
SuperMemo usage facts distilled from the
[official SuperMemo documentation](https://help.supermemo.org).
The official documentation bundled verbatim in `docs/` (help.supermemo.org
wiki pages and the twenty-rules article) remains © SuperMemo World (see
`docs/README.md`); the MIT license covers this project's own files only.

---

# SuperMemo Companion — 中文版

**内化所思，外包所查。**

一个与具体 AI 工具无关的开源套件：把任何一个能干的 AI 助手，变成你
[SuperMemo](https://super-memory.com/) 学习实践**旁边的陪练**——而不是替你
学习的代练。它回答四个问题：

1. **“AI 什么都能解释了，我为什么还要学？学什么？”**——基于一套明确的
   AI 时代学习观，给出方向建议。
2. **“这个值得导入 / 值得背吗？”**——站在收藏（collection）门口把关，让
   复习时间只花在你会用来思考的知识上。
3. **“这段不知道怎么 extract / cloze？”**——渐进阅读途中给出具体建议和
   背后的规则，动手的仍然是你。
4. **“SuperMemo 里怎么做 X？”**——依据官方文档解答工具问题，绝不靠猜。

它同时拒绝一件事：**替你阅读**。它简化的是 SuperMemo 的上手难度，而不是
学习本身。

[English](#supermemo-companion) · **中文**

---

## 为什么做这个项目

> AI 改变的是知识检索的经济学，而不是思考的机制。
> 学习者应当内化自己赖以思考的知识，把只需查询的知识交给外部工具。

既然 AI 随时能解释几乎一切，“学习已经过时”似乎顺理成章。但这个结论混淆了
两种不同的知识。存在于外部世界的知识是**惰性的**——不去查询，它什么也不
做；存在于头脑中的知识是**可执行的**——它不经调用就直接参与感知、理解和
判断。棋手不是“回忆”棋型，而是直接“看见”不同的棋盘。再好的外部神谕也改变
不了这一点，因为神谕永远站在你眼睛的外面。

由此推出三件事：

1. **你无法查询你叫不出名字的东西。** 好问题由内化了的概念构成。没有领域
   地图的人，连提问都无从下手。
2. **生成已经廉价，鉴别才是稀缺技能。** AI 输出流畅的答案，也输出流畅的
   错误答案。评估它们需要内在的锚点——机制、数量级、典型失败模式。如果
   一切都外包了，你连怀疑的依据都没有。
3. **洞见来自碰撞。** 创造性的联结发生在同一个大脑里的知识之间。查得到但
   从未内化的材料，永远不会参与碰撞。

计算器是最好的先例：它消灭了笔算训练，却**抬高**了数感的价格。AI 自动化
了语言性、程序性的工作，也就抬高了“领域感”的价格。所以答案不是“少学”，而
是**更少的条目、更深的领域、更好的卡片**。AI 是你已有知识的乘数——被乘数
越大，乘数才越值钱。

这个套件要做的，就是让 AI 为你的记忆服务，而不是取代它。

## 那么，究竟该学什么？

在任何清单之前，先记三条方向性原则：

- **深胜于广。** AI 奖励“被乘数”最大的人；十七个浅尝辄止的爱好乘出来还是
  零。
- **耐久胜于易逝。** 间隔重复是终身投资，要买不贬值的资产。
- **热爱胜于应该。** 长期学习靠乐趣驱动；出于“应该”的计划三周就会死掉。
  （这也是本套件拒绝替你做有趣部分的原因。）

**停止记忆：** 工具语法和参数、API 签名、配置文件格式、有锚点即可的精确数
值、永远开着工具执行的分步操作、月抛型框架细节、孤立的冷知识。

**保持（或开始）记忆：** 工作领域的术语与本体、机制与因果模型、“X 与 Y 何
时用哪个”的辨析、典型例子与失败模式、数量级与基础比率、外语（最纯粹的时
延场景），以及核心专业领域的纵深——细节也值得，因为熟练度会复利。

## 学习模型：任何一条知识的四个去向

| 去向 | 含义 | 处理方式 |
|---|---|---|
| **深度记忆 MEMORIZE** | 你要“用它思考”：需要即时反应、是领域地基、是判断锚点 | 你自己在 SuperMemo 里做 1–3 张卡 |
| **地图级 MAP** | 你只需知道“它存在”：解决什么问题、何时适用、细节在哪 | 恰好 1 张“地图卡” |
| **外包 OFFLOAD** | 你只需“查询它”：一分钟内可查到、当场可验证 | 不做卡片，用时问 AI / 查资料 |
| **舍弃 DISCARD** | 没有可预见的用途，也没有联结价值 | 有意识地放弃 |

## 七个判断测试

当你问“这个值得背吗”，对每个知识单元逐一提问：

1. **时延** —— 需要以思考的速度调用，还是每次都来得及花一分钟去查？
2. **地基** —— 没有它，这个领域的其他内容还能理解吗？
3. **地图** —— 知道它的存在，是否改变了你能提出的问题？
4. **判断** —— 你会用它来校验 AI（或他人）的输出吗？
5. **碰撞** —— 你希望它参与后台思考和创造性联结吗？
6. **半衰期** —— 5–10 年后它还成立吗？（要买不贬值的资产。）
7. **热爱** —— 你就是想让它成为自己的一部分吗？热爱压倒一切效率论证。

在七个测试之外，还有一条纯经济学检查：凡是每周都会用到的知识，直接值得
记忆。

判决是**因人而异的**：同一条知识，对外科医生是 MEMORIZE，对患者是
OFFLOAD。决定因素是时延与利害，而不是知识本身。

## 边界：这个套件不做什么

- 它**不会替你阅读、总结、摘录或制卡**。把卡住的那一段拿来，它给建议；把
  整篇文章塞给它，它会礼貌地退回——顺带附一份“值不值得导入”的判决。
- 它**不会批量生成卡片**。它建议措辞，卡片由你来做。“选出重要的东西”和
  “把它表述成卡片”本身就是学习——把这两步自动化掉，剩下的只是一副不属于
  你的牌，和一笔属于你的复习债。
- 两个刻意保留的例外（都仅限你明确要求时）：**修复你已经拥有的条目**（反
  复出错的条目返回新旧对照的重写；整批导出的水蛭返回一份只含重写的导入文
  件），以及**没有“阅读”可言的机械批量**（生词表、你自己的笔记）。维护不
  等于外包。

为什么这么严格？没有留存的理解会蒸发（流畅性错觉）；不是自己建立的记忆，
只是别人思想的复印件。而且渐进阅读本身是**有趣的**——心流属于你，不属于
工具。

## 仓库内容

```
AGENTS.md                        ← Agent 入口（与具体工具无关）
CLAUDE.md                        ← 兼容旧版 Claude Code 的指针文件
skills/
  worth-learning/SKILL.md        ← 方向建议 · 导入把关 · 值不值得背
  reading-advisor/SKILL.md       ← extract/cloze/措辞建议 · 条目修复
  supermemo-coach/
    SKILL.md                     ← 解答一切 “SuperMemo 里怎么做？”
    reference.md                 ← 提炼后的 SuperMemo 离线参考
    incremental-learning.md      ← 渐进学习理念提炼
docs/
  wiki/ · wiki-zh/               ← 完整官方 wiki 抓取（英文约 210 页 + 中文，离线可用）
  articles/20rules.htm           ← Wozniak《表述知识的二十条规则》原文
examples/
  LEARNER.example.md             ← 个人学习档案模板
  sample-session.md              ← 标准会话的样例
cards/                           ← 水蛭诊所的修复文件放这里（已 gitignore）
```

指令文件用英文书写（对各类模型最稳定），但 Agent 会用**你的语言**交流。

## 快速开始

1. 克隆本仓库（或把文件复制进你的学习目录）。
2. 把 `examples/LEARNER.example.md` 复制为根目录的 `LEARNER.md` 并填写
   （2 分钟——判决的个性化全靠它）。完整官方 wiki 已随仓库自带
   （`docs/`）；仅当你另有更新的自爬副本时，才需把路径填进 `Docs mirror`
   一栏（它会优先生效）。
3. 在此目录打开你的 Agent：

| 工具 | 设置 |
|---|---|
| **Claude Code** | 无需设置——自动读取 `AGENTS.md`（旧版读 `CLAUDE.md`） |
| **Codex CLI** | 无需设置——自动读取 `AGENTS.md` |
| **OpenCode** | 无需设置——自动读取 `AGENTS.md` |
| **Cursor** | 新版本支持 `AGENTS.md`；否则将其添加为项目规则 |
| **其他任何工具** | 说一句：*“阅读 AGENTS.md 并遵循它”*——凡能读文件的 Agent 都可以 |

4. 可以先试这些提示：
   - “AI 什么都能解释了，我还值得深入学什么？”
   - “这篇文章值得导入 SuperMemo 吗？”（贴正文或链接）
   - “渐进阅读读到这一段，不知道该 extract 什么——给点建议？”
   - “这条 extract 该怎么做 cloze？”
   - “渐进阅读的优先级到底是怎么运作的？”

不需要最贵的前沿模型：技能文件刻意写得足够机械——清单、有序判定规则、固
定输出形态——中档模型（Sonnet 级）即可稳定执行。

## 端到端的循环

0. **定方向**（偶尔）。“我该在哪深耕？”——陪练从耐久性、杠杆、判断力、热
   爱四个角度给出有立场的建议，然后请你带一篇具体的章节或文章回来。
1. **把关。** 任何东西进 SuperMemo 之前先问一句“值得导入吗？”你会得到
   IMPORT（附建议优先级）/ IMPORT PART / READ OUTSIDE / SKIP 四种判决，以
   及 AI 时代的理由。请习惯被拒绝——“这不值得你的复习时间”正是产品在起作
   用。
2. **渐进阅读——你自己来。** 在 SuperMemo 里：导入（**Ctrl+N** 粘贴、
   **Shift+F8** 网页导入），诚实定优先级（**Alt+P**），读一点，摘录要点
   （**Alt+X**），把单句变成挖空（**Alt+Z**），主动提前停下。不确定该
   extract 什么、怎么 cloze 时，把那段贴给陪练——你会得到具体建议和背后
   的规则，然后**由你**按下快捷键。
3. **途中随便问。** 要解释尽管开口——这是 AI 最擅长的事。解释完，陪练会
   问一句：“值得留下吗？我可以建议一个卡片措辞，你来添加。”理解已经廉价，
   装进头脑的才留得下来。
4. **修复出错的。** 某条目反复出错→贴过来，附一句症状（“连错 5 次”“总是
   答成 X”）→拿回一份新旧对照重写，粘贴回**原条目**（**E** 编辑；
   **Ctrl+M** 重启其日程）。每月一次：**Shift+F3** 把水蛭收进浏览器，
   `Export : Q&A text file` 导出交给陪练，拿回逐条判决和一份只含重写的导
   入文件，然后在同一浏览器里停用原条目
   （`Process browser> : Learning : Dismiss`）。每退役一张卡，就永久收回
   一份复习时间。
5. **教练随叫随到。** 快捷键、优先级、统计、版本差异、设计理念——先查离
   线精编参考，再查仓库自带的完整官方 wiki（`docs/`），最终以
   [help.supermemo.org](https://help.supermemo.org) 为准。

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
  习；本套件是位于其上的“纪律层”。
- 其余一切：问 coach 技能，或查阅
  [官方文档](https://help.supermemo.org)。

## 设计原则

- **可移植。** 单一入口（`AGENTS.md`），技能是按路径加载的纯 Markdown，不
  依赖任何工具特有功能。凡能读文件的 Agent 都能用。
- **刻意轻量。** 三个技能，没有元框架，除一个可选的 `LEARNER.md` 外没有任
  何状态。用有序规则和固定输出形态取代依赖悟性的长文，小模型也能稳定执行。
- **以官方文档为据。** 工具问题先查离线精编参考
  （`skills/supermemo-coach/reference.md`）与理念提炼
  （`incremental-learning.md`），其下是仓库自带的完整官方 wiki
  （`docs/`，英文约 210 页 + 中文翻译）——在线 wiki 有 Cloudflare 拦截，
  程序化抓取常被挡，所以仓库自带事实底本，最终以 help.supermemo.org 为
  准。coach 绝不猜快捷键。
- **陪练，不代练。** 它拒绝为“外包级”材料制卡，也拒绝替你阅读、替你打初
  稿。这两种拒绝本身就是产品。

## 常见问题

**AI 会让间隔重复过时吗？**
不会——反而更有价值。AI 是你能拥有的最好的讲解者，但没有留存的理解几周内
就蒸发（流畅性错觉）。AI 让理解变得便宜；SuperMemo 让理解变得永久。它们是
互补品：一个负责生产，一个负责安装。

**为什么它不肯直接读完文章、把卡做好给我？**
因为“选出重要的东西”和“把它表述成卡片”这两步正是学习发生的地方，也因为每
张卡都是一条由**你**买单的、持续多年的复习流。瓶颈从来不是做卡，而是复习
时间。仅有的例外（修复你自己的水蛭条目；生词表之类的机械批量）之所以存
在，是因为那里的学习在复习里，不在打字里。

**能配合 Anki 或其他间隔重复软件用吗？**
理念、把关和制卡原则完全通用。工具指导与渐进阅读建议是 SuperMemo 专属的
——Anki 没有真正的渐进阅读，而这恰恰是本套件选择 SuperMemo 的原因。

**需要多强的模型？**
任何称职的中档模型即可。技能文件按 Sonnet 级模型可稳定执行的标准编写；更
强的模型只是判断的品味更好。

**隐私？**
你给陪练看的材料会发送给驱动它的模型服务。敏感笔记请自行斟酌；
`LEARNER.md` 默认已被 gitignore。

**与 SuperMemo World 有关系吗？**
没有。非官方、未获背书。SuperMemo 是 SuperMemo World 的商标。本项目的方法
性内容提炼自官方 wiki（help.supermemo.org）与 Piotr Wozniak 的著述，谨致
谢意。

## 参与贡献

欢迎 Issue 和 PR。有价值的方向：更好的示例、README 翻译、对 SuperMemo 参
考内容的勘误（请引用官方 wiki 页面）、更多 Agent 环境的适配说明。请保持设
计轻量——增加第四个技能的门槛应当很高，而增加“替学习者阅读”的自动化，门
槛是无穷高。

## 许可证

MIT，见 [LICENSE](LICENSE)。

制卡原则改编自 Piotr Wozniak
[《高效学习：表述知识的二十条规则》](https://super-memory.com/articles/20rules.htm)；
SuperMemo 使用事实提炼自[官方文档](https://help.supermemo.org)。
`docs/` 中逐字收录的官方文档（help.supermemo.org wiki 各页与《二十条规
则》一文）版权仍归 SuperMemo World（见 `docs/README.md`）；MIT 许可证仅
覆盖本项目自有文件。
