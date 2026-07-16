# Spaced Repetition Companion

**Internalize what you think with. Offload what you merely consult.**

A portable **Agent Skill** that turns any capable AI assistant into a
companion for learning with spaced repetition —
[SuperMemo](https://super-memory.com/), [Anki](https://apps.ankiweb.net/),
or any similar tool. Drop the `spaced-repetition-companion/` directory into
any agent that supports Agent Skills and it does four jobs:

1. **"Is this worth learning at all, now that AI explains everything?"**
   A gatekeeper in front of your memory, grounded in an explicit philosophy
   of AI-era learning — so review time is spent only on knowledge you'll
   think with.
2. **"Make cards from this."** Q&A cards and cloze deletions produced from
   material you supply, formulated by SuperMemo's twenty rules and
   delivered in your tool's import format (SuperMemo Q&A text, Anki text
   file) — always gate-first: what isn't worth carding comes back as a
   named skip with a reason, not as deck filler.
3. **"How should I extract / cloze / word this?"** Craft advice
   mid-reading, plus repair for cards that keep failing (leeches) and
   audits for collections that have silted up.
4. **"How do I … in SuperMemo?"** Tool coaching answered from a bundled
   offline mirror of the official documentation, never from guesswork.

Jobs 1–3 are tool-agnostic; job 4 is SuperMemo-deep. The skill's one
standing refusal: it never cards *around* the gate — "twenty cards on X"
where six earned existence gets you six cards and a list of reasons.

**English** · [中文](#spaced-repetition-companion--中文版)

---

## Why this exists (short version)

> AI changes the economics of retrieval, but not the mechanics of thought.
> Learners should internalize what they need to think with, and offload what
> they merely need to consult.

Knowledge in the world is *inert* — it does nothing until queried. Knowledge
in your head is *executable* — it runs inside perception, comprehension, and
judgment without being asked. AI automates verbal-procedural work the same
way the calculator automated arithmetic — and just as the calculator raised
the price of number sense, AI raises the price of domain sense. So the
answer isn't "learn less," it's **fewer items, deeper domains, better
cards**.

The full argument — the seven tests for "is this worth memorizing," the
four-destinations model (MEMORIZE / MAP / OFFLOAD / DISCARD), and the exact
boundary of what this skill will and won't do — ships *inside* the skill
itself at `spaced-repetition-companion/references/philosophy.md`, so it
travels with the skill wherever it's installed rather than living only in
this README.

## Install

This repository's entire functionality lives in one self-contained
directory: `spaced-repetition-companion/`. (The repository keeps its
historical name; the skill directory is the thing you copy.) Two ways to
use it:

| Setup | How |
|---|---|
| **Working directly in this repo** | Nothing to do — `AGENTS.md` / `CLAUDE.md` at the repo root already point any agent that auto-loads them at `spaced-repetition-companion/SKILL.md`. |
| **Using it from your own project** (recommended if you juggle other repos too) | Copy or symlink `spaced-repetition-companion/` into wherever your agent looks for Agent Skills (e.g. `.claude/skills/spaced-repetition-companion/`), keeping the directory name unchanged. |
| **Any agent that just reads files** | Say once: *"Read spaced-repetition-companion/SKILL.md and follow it."* |

Then, optionally, copy
`spaced-repetition-companion/assets/LEARNER.example.md` to `LEARNER.md`
(current directory or your home directory — see `SKILL.md` §
Personalization) and fill it in; 2 minutes, and it's what makes verdicts,
cards, and coaching personal. A revision-pinned SuperMemo Help mirror
already ships inside the skill at `spaced-repetition-companion/docs/wiki/`.

First prompts to try:

- *"What's still worth learning deeply, now that AI can explain anything?"*
- *"Is this article worth importing into my collection?"* (paste it or link it)
- *"Make Anki cards from these notes."* (paste them)
- *"I'm reading this paragraph and don't know what to extract — suggestions?"*
- *"This card has failed five times — fix it."*
- *"How do incremental reading priorities actually work?"*

No frontier model required: the skill is deliberately mechanical —
checklists, ordered decision rules, fixed output shapes — so a mid-tier
model (Sonnet-class) follows it reliably.

## What's inside

```
spaced-repetition-companion/       <- the whole portable skill — copy this directory, nothing else
  SKILL.md                          entry point: principle, routing, ground rules, personalization
  LICENSE                           MIT, covers this skill's own files
  references/
    worth-learning.md                direction · import gatekeeping · memorize-or-not
    card-craft.md                    card production (Q&A + cloze) · extract/cloze/wording craft · repair
    supermemo-coach.md               answers any "how do I … in SuperMemo?"
    reference.md                     distilled SuperMemo reference (offline)
    incremental-learning.md          the method's philosophy, distilled
    philosophy.md                    the AI-era learning argument, in full
    sample-session.md                worked example transcripts
  docs/
    wiki/                            revision-pinned SuperMemo Help mirror (938 files)
    articles/20rules.htm             Wozniak's formulation-rules article
  assets/
    LEARNER.example.md               personal profile template
  scripts/
    import_supermemo_help.py         rebuild and validate the wiki mirror

AGENTS.md / CLAUDE.md              <- thin pointers, for agents that auto-load a repo root
LEARNER.md                          <- your own profile if you keep it here (gitignored)
cards/                              <- generated card files land here (gitignored)
```

The skill's own instruction files are in English (most reliable across
models); the agent converses in **your** language.

## Design principles

- **Portable.** One skill directory, loaded by any agent that supports
  Agent Skills (or just told to read `SKILL.md`). Every path the skill
  refers to is relative to its own directory, never to whatever project
  it's installed alongside.
- **Gate before craft.** Card production is a first-class deliverable, but
  it always runs behind the worth-learning tests. The skips — named, with
  reasons — are half the product: every card is years of future review
  time.
- **Tool-agnostic core, SuperMemo-deep edge.** Gatekeeping and formulation
  work for any SRS and speak both SuperMemo's and Anki's import formats.
  Tool coaching is SuperMemo-only, backed by a genuinely complete offline
  documentation mirror rather than a trimmed-down summary — the coach never
  guesses a shortcut. (The online wiki sits behind a Cloudflare challenge;
  help.supermemo.org remains the final authority.)
- **Teach while helping.** Every card and every suggestion comes with the
  one formulation principle that generated it, so the user needs the skill
  a little less each time. Reading stays in the user's hands; for core
  domains the skill nudges — once — toward formulating cards yourself.

## FAQ

**Does AI make spaced repetition obsolete?**
No — it makes it more valuable. AI is the best explainer you'll ever have,
but understanding you don't retain evaporates in weeks. AI makes
understanding cheap; spaced repetition makes it permanent. Full answer:
`spaced-repetition-companion/references/philosophy.md`.

**Will it really make the cards for me?**
Yes — after the gate. Material you supply is decomposed into knowledge
units, each unit is tested (MEMORIZE / MAP / OFFLOAD / DISCARD), and only
what passes gets carded, in your tool's import format. What fails comes
back as a named skip with a one-clause reason.

**I use Anki, not SuperMemo — is this for me?**
Yes. The gatekeeper, the card craft (including `{{c1::…}}` cloze output),
the repair clinic, and the philosophy are fully tool-agnostic. Only the
tool coaching and incremental-reading mechanics are SuperMemo-specific.

**Which model do I need?**
Any competent mid-tier model. The skill is written so Sonnet-class models
follow it reliably; stronger models simply judge with better taste.

**Privacy?**
Material you show the companion is sent to whatever model powers your
agent. Keep that in mind for sensitive notes; `LEARNER.md` is gitignored by
default.

**Is this affiliated with SuperMemo World?**
No. Unofficial, unendorsed. SuperMemo is a trademark of SuperMemo World.
Method concepts are distilled from the official wiki (help.supermemo.org)
and Piotr Wozniak's writings, with attribution and gratitude.

## Contributing

Issues and PRs welcome. Useful contributions: better worked examples,
translations, corrections to the SuperMemo reference (cite the official
wiki page), import formats for more SRS tools, adapters for more agent
environments. Keep the design lightweight — the bar for adding a new
reference file is high, and the bar for adding anything that cards around
the gate is infinite.

## License

MIT. See [LICENSE](LICENSE).

Formulation principles adapted from Piotr Wozniak,
[*Effective learning: Twenty rules of formulating knowledge*](https://super-memory.com/articles/20rules.htm).
SuperMemo usage facts distilled from the
[official SuperMemo documentation](https://help.supermemo.org).
The official documentation mirrored in `spaced-repetition-companion/docs/`
(exact help.supermemo.org wikitext, derived rendered pages, and the
twenty-rules article) remains © SuperMemo World / its respective authors
(see `spaced-repetition-companion/docs/README.md`); the MIT license covers
this project's own files only.

---

# Spaced Repetition Companion — 中文版

**内化所思，外包所查。**

一个可移植的 **Agent Skill**：把任何一个能干的 AI 助手，变成你间隔重复学习
实践的伴侣——无论你用的是 [SuperMemo](https://super-memory.com/)、
[Anki](https://apps.ankiweb.net/) 还是其它同类软件。把
`spaced-repetition-companion/` 目录放进任何支持 Agent Skill 的 Agent，它就
能做四件事：

1. **“AI 什么都能解释了，这个还值得学吗？”**——基于一套明确的 AI 时代学习
   观，站在你的记忆门口把关，让复习时间只花在你会用来思考的知识上。
2. **“把这些素材做成卡片。”**——对你给出的素材做 Q&A 卡和 Cloze（填空）卡：
   按 SuperMemo 的二十条表述规则制卡，按你的工具输出导入格式（SuperMemo
   Q&A 文本 / Anki 文本文件）——并且永远先过甄别关：不值得制卡的部分会以
   “跳过 + 一句话理由”的形式返回，而不是变成凑数的卡片。
3. **“这段怎么 extract / cloze / 措辞？”**——阅读途中的手艺建议，外加修复
   反复记不住的卡（水蛭 leech）、审计已经淤积的收藏。
4. **“SuperMemo 里怎么做 X？”**——依据技能自带的官方文档离线镜像解答工具
   问题，绝不靠猜。

前三件事与工具无关；第四件事对 SuperMemo 有最深的支持。这个技能唯一的
坚持是：**绝不绕过甄别关制卡**——“给我做二十张卡”而只有六张值得存在时，
你得到的是六张卡加一份理由清单。

[English](#spaced-repetition-companion) · **中文**

---

## 为什么做这个项目（精简版）

> AI 改变的是知识检索的经济学，而不是思考的机制。
> 学习者应当内化自己赖以思考的知识，把只需查询的知识交给外部工具。

存在于外部世界的知识是**惰性的**——不去查询，它什么也不做；存在于头脑中
的知识是**可执行的**——它不经调用就直接参与感知、理解和判断。AI 自动化了
语言性、程序性的工作，就像计算器自动化了笔算——笔算训练消失了，数感的价格
反而升高了；同理，AI 抬高的是“领域感”的价格。所以答案不是“少学”，而是
**更少的条目、更深的领域、更好的卡片**。

完整论证——“值不值得背”的七个测试、四个去向模型（深度记忆 MEMORIZE / 地图
级 MAP / 外包 OFFLOAD / 舍弃 DISCARD），以及这个技能会做什么、不做什么的确
切边界——就装在技能本体里：
`spaced-repetition-companion/references/philosophy.md`（英文）。这样无论
这个技能被安装到哪里，论证都随身携带，而不是只留在这份 README 里。

## 安装

本仓库的全部功能都在一个自包含目录里：`spaced-repetition-companion/`
（仓库沿用旧名，你需要复制的是这个技能目录）。两种用法：

| 场景 | 做法 |
|---|---|
| **直接在本仓库里工作** | 什么都不用做——根目录的 `AGENTS.md` / `CLAUDE.md` 已经指向 `spaced-repetition-companion/SKILL.md`，任何会自动读取这两个文件的 Agent 都能识别。 |
| **在自己的项目里使用**（如果你手上还有别的仓库，推荐这种） | 把 `spaced-repetition-companion/` 整个目录复制或软链接到你的 Agent 存放 Skill 的位置（例如 `.claude/skills/spaced-repetition-companion/`），目录名保持不变。 |
| **任何能读文件的 Agent** | 说一句：“阅读 spaced-repetition-companion/SKILL.md 并遵循它。” |

然后可以把 `spaced-repetition-companion/assets/LEARNER.example.md` 复制为
`LEARNER.md`（放在当前目录或你的主目录——见 `SKILL.md` 的“Personalization”
一节）并填写，2 分钟——判决、制卡和教练建议的个性化全靠它。固定 revision 的
SuperMemo Help 镜像已经装在技能内部：
`spaced-repetition-companion/docs/wiki/`。

可以先试这些提示：

- “AI 什么都能解释了，我还值得深入学什么？”
- “这篇文章值得导入我的收藏吗？”（贴正文或链接）
- “把这些笔记做成 Anki 卡片。”（贴笔记）
- “渐进阅读读到这一段，不知道该 extract 什么——给点建议？”
- “这张卡已经错五次了——帮我修一下。”
- “渐进阅读的优先级到底是怎么运作的？”

不需要最贵的前沿模型：技能刻意写得足够机械——清单、有序判定规则、固定输出
形态——中档模型（Sonnet 级）即可稳定执行。

## 仓库内容

```
spaced-repetition-companion/       <- 整个可移植技能——只需复制这一个目录
  SKILL.md                          入口：核心原则、路由、行为准则、个性化
  LICENSE                           MIT，仅覆盖本技能自有文件
  references/
    worth-learning.md                方向建议 · 导入把关 · 值不值得背
    card-craft.md                    制卡（Q&A + Cloze）· extract/cloze/措辞手艺 · 条目修复
    supermemo-coach.md               解答一切 “SuperMemo 里怎么做？”
    reference.md                     提炼后的 SuperMemo 离线参考
    incremental-learning.md          渐进学习理念提炼
    philosophy.md                    AI 时代学习论证全文
    sample-session.md                标准会话样例
  docs/
    wiki/                            固定 revision 的 SuperMemo Help 镜像（938 个文件）
    articles/20rules.htm             Wozniak《表述知识的二十条规则》原文
  assets/
    LEARNER.example.md               个人学习档案模板
  scripts/
    import_supermemo_help.py         重建并校验 Wiki 镜像

AGENTS.md / CLAUDE.md              <- 兼容指针，给会自动读取仓库根目录的 Agent
LEARNER.md                          <- 如果放在这里的个人档案（已 gitignore）
cards/                              <- 生成的卡片文件落在这里（已 gitignore）
```

技能自身的指令文件用英文书写（对各类模型最稳定），但 Agent 会用**你的语
言**交流。

## 设计原则

- **可移植。** 一个技能目录，任何支持 Agent Skill 的 Agent 都能加载（或者
  只需说一句“读 SKILL.md”）。技能内提到的路径一律相对于技能自己的目录，
  与它被安装进哪个项目无关。
- **先把关，再制卡。** 制卡是一等交付物，但永远排在甄别测试之后。那些被点
  名跳过、附带理由的部分是产品的另一半：每张卡都是未来数年的复习时间。
- **内核与工具无关，边缘对 SuperMemo 最深。** 甄别与表述手艺适用于任何间
  隔重复软件，同时支持 SuperMemo 与 Anki 两种导入格式。工具教练只服务
  SuperMemo，背后是一份真正完整的离线文档镜像而非精简摘要——coach 绝不猜
  快捷键。（在线 wiki 有 Cloudflare 拦截，最终仍以 help.supermemo.org 为
  准。）
- **边帮边教。** 每张卡、每条建议都附上生成它的那一条表述原则，让你一次比
  一次更少需要它。阅读始终在你自己手里；对你的核心领域，它会提醒一次——
  自己动手表述，记得更牢。

## 常见问题

**AI 会让间隔重复过时吗？**
不会——反而更有价值。AI 是你能拥有的最好的讲解者，但没有留存的理解几周内
就蒸发。AI 让理解变得便宜；间隔重复让理解变得永久。完整回答见
`spaced-repetition-companion/references/philosophy.md`。

**它真的会替我制卡吗？**
会——但先过甄别关。你给的素材会被拆解成知识单元，每个单元过一遍测试
（MEMORIZE / MAP / OFFLOAD / DISCARD），通过的才按你的工具的导入格式制成
卡片；没通过的以“跳过 + 一句话理由”返回。

**我用的是 Anki，不是 SuperMemo——适合我吗？**
适合。甄别把关、制卡手艺（包括 `{{c1::…}}` 填空输出）、卡片修复诊所和学习
哲学完全与工具无关；只有工具教练和渐进阅读的具体操作是 SuperMemo 专属。

**需要多强的模型？**
任何称职的中档模型即可。技能按 Sonnet 级模型可稳定执行的标准编写；更强的
模型只是判断的品味更好。

**隐私？**
你给伴侣看的材料会发送给驱动它的模型服务。敏感笔记请自行斟酌；
`LEARNER.md` 默认已被 gitignore。

**与 SuperMemo World 有关系吗？**
没有。非官方、未获背书。SuperMemo 是 SuperMemo World 的商标。本项目的方法
性内容提炼自官方 wiki（help.supermemo.org）与 Piotr Wozniak 的著述，谨致
谢意。

## 参与贡献

欢迎 Issue 和 PR。有价值的方向：更好的示例、翻译、对 SuperMemo 参考内容的
勘误（请引用官方 wiki 页面）、更多间隔重复软件的导入格式、更多 Agent 环境
的适配说明。请保持设计轻量——增加新参考文件的门槛应当很高，而增加任何“绕
过甄别关制卡”的功能，门槛是无穷高。

## 许可证

MIT，见 [LICENSE](LICENSE)。

制卡原则改编自 Piotr Wozniak
[《高效学习：表述知识的二十条规则》](https://super-memory.com/articles/20rules.htm)；
SuperMemo 使用事实提炼自[官方文档](https://help.supermemo.org)。
`spaced-repetition-companion/docs/` 中镜像的官方文档（help.supermemo.org
原样 wikitext、派生渲染页与《二十条规则》一文）版权仍归 SuperMemo World /
各自作者（见 `spaced-repetition-companion/docs/README.md`）；MIT 许可证仅
覆盖本项目自有文件。
