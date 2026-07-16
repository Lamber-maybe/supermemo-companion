# Spaced Repetition Companion（间隔重复学习伴侣）

**内化所思，外包所查。**

[English](README.md) · **简体中文**

一个可移植的 **Agent Skill**：把任何一个能干的 AI 助手，变成你间隔重复
学习实践的伴侣——无论你用 [SuperMemo](https://super-memory.com/)、
[Anki](https://apps.ankiweb.net/) 还是其它同类软件。

## 它做什么

1. **甄别把关。**“AI 什么都能解释了，这个还值得学吗？”——站在你记忆门口
   的一道闸：素材给出 IMPORT / SKIP、单个知识点给出 MEMORIZE / MAP /
   OFFLOAD / DISCARD，每个判定附一句理由，背后是一套明确的 AI 时代学习观。
2. **制卡。**“把这些素材做成卡片。”——按 SuperMemo 的二十条表述规则做
   Q&A 卡和 Cloze（填空）卡，按你的工具输出导入格式（SuperMemo Q&A 文本 /
   Anki 文本文件）。永远先过闸：不值得制卡的部分以“跳过 + 一句话理由”
   返回，绝不凑数。
3. **手艺建议与修卡。**阅读途中该 extract 什么、怎么 cloze、卡片怎么措辞；
   修复反复记不住的卡（水蛭 leech）；审计已经淤积的收藏。
4. **SuperMemo 教练。**一切“SuperMemo 里怎么做 X”——快捷键、优先级、
   渐进阅读、设置、排障——依据技能自带的官方文档离线镜像解答，绝不靠猜。

前三件事与工具无关；第四件事对 SuperMemo 支持最深。这个技能唯一的坚持：
**绝不绕过甄别关制卡**——“给我做二十张卡”而只有六张值得存在时，你得到的
是六张卡加一份理由清单。

## 为什么做这个项目

> AI 改变的是知识检索的经济学，而不是思考的机制。

存在于外部世界的知识是**惰性的**——不去查询，它什么也不做；存在于头脑中
的知识是**可执行的**——它不经调用就直接参与感知、理解和判断。就像计算器
杀死了笔算训练、反而抬高了数感的价格一样，AI 自动化了语言性、程序性的
工作，抬高的是“领域感”的价格。所以答案不是“少学”，而是**更少的条目、
更深的领域、更好的卡片**。

完整论证——“值不值得背”的七个测试、四个去向模型、这个技能会做什么不做
什么的确切边界——装在技能本体里：
[`references/philosophy.md`](spaced-repetition-companion/references/philosophy.md)
（英文），无论技能被安装到哪里都随身携带。

## 安装

全部功能都在一个自包含目录里：
[`spaced-repetition-companion/`](spaced-repetition-companion/)——你需要
复制的就是这个目录。

| 场景 | 做法 |
|---|---|
| **直接在本仓库里工作** | 什么都不用做——根目录的 `AGENTS.md` / `CLAUDE.md` 已经指向技能入口，会自动读取它们的 Agent 直接可用。 |
| **在自己的项目里使用**（推荐） | 把 `spaced-repetition-companion/` 整个目录复制或软链接到你的 Agent 存放 Skill 的位置（例如 `.claude/skills/spaced-repetition-companion/`），目录名保持不变。 |
| **任何能读文件的 Agent** | 说一句：“阅读 spaced-repetition-companion/SKILL.md 并遵循它。” |

然后（可选，但很值这 2 分钟）：把
[`assets/LEARNER.example.md`](spaced-repetition-companion/assets/LEARNER.example.md)
复制为 `LEARNER.md`（放当前目录或主目录），填上你的目标、领域、每日复习
预算和所用软件——判定、制卡和教练建议的个性化全靠它；本仓库默认已将其
gitignore。

不需要最贵的前沿模型：技能刻意写得足够机械——清单、有序判定规则、固定
输出形态——中档模型（Sonnet 级）即可稳定执行。

### 可以先试这些提示

- “AI 什么都能解释了，我还值得深入学什么？”
- “这篇文章值得导入我的收藏吗？”（贴正文）
- “把这些笔记做成 Anki 卡片。”（贴笔记）
- “渐进阅读读到这一段，不知道该 extract 什么——给点建议？”
- “这张卡已经错五次了——帮我修一下。”
- “渐进阅读的优先级到底是怎么运作的？”

## 仓库内容

```
spaced-repetition-companion/       <- 整个可移植技能——只需复制这一个目录
  SKILL.md                          入口：核心原则、路由、行为准则、个性化
  LICENSE                           MIT，仅覆盖本技能自有文件
  references/
    worth-learning.md                方向建议 · 导入把关 · 值不值得背
    card-craft.md                    制卡（Q&A + Cloze）· extract/cloze/措辞 · 修卡
    supermemo-coach.md               解答一切 “SuperMemo 里怎么做？”
    reference.md                     提炼后的 SuperMemo 离线参考
    incremental-learning.md          渐进学习理念提炼
    philosophy.md                    AI 时代学习论证全文
    sample-session.md                标准会话样例
  docs/
    wiki/                            固定 revision 的 help.supermemo.org 离线镜像
    articles/20rules.htm             Wozniak《表述知识的二十条规则》原文
  assets/LEARNER.example.md          个人学习档案模板
  scripts/import_supermemo_help.py   重建并校验 Wiki 镜像

AGENTS.md / CLAUDE.md              <- 兼容指针，给会自动读取仓库根目录的 Agent
LEARNER.md                          <- 如果放在这里的个人档案（已 gitignore）
cards/                              <- 生成的卡片文件落在这里（已 gitignore）
```

技能自身的指令文件用英文书写（对各类模型最稳定），但 Agent 会用**你的
语言**交流。

## 设计原则

- **可移植。**一个技能目录，任何支持 Agent Skill 的 Agent 都能加载，或者
  只需一句“读 SKILL.md”。技能内部路径一律相对于技能自己的目录，与宿主
  项目无关。
- **先把关，再制卡。**制卡是一等交付物，但永远排在甄别测试之后。那些被
  点名跳过、附带理由的部分是产品的另一半：每张卡都是未来数年的复习时间。
- **内核与工具无关，边缘对 SuperMemo 最深。**甄别与表述手艺适用于任何
  间隔重复软件，同时支持 SuperMemo 与 Anki 两种导入格式；工具教练只服务
  SuperMemo，背后是完整的离线文档镜像——教练绝不猜快捷键。（在线 wiki 有
  Cloudflare 拦截，最终仍以 https://help.supermemo.org 为准。）
- **边帮边教。**每张卡、每条建议都点名生成它的那一条表述原则，让你一次
  比一次更少需要它。阅读始终在你自己手里；对你的核心领域，它会提醒一次
  ——自己动手表述，记得更牢。

## 常见问题

**AI 会让间隔重复过时吗？**
不会——反而更有价值。AI 是你能拥有的最好的讲解者，但没有留存的理解几周
内就蒸发。AI 让理解变得便宜；间隔重复让理解变得永久。

**它真的会替我制卡吗？**
会——但先过甄别关。素材被拆解成知识单元，每个单元过一遍测试
（MEMORIZE / MAP / OFFLOAD / DISCARD），通过的才按你的工具的导入格式制成
卡片；没通过的以“跳过 + 一句话理由”返回。

**我用的是 Anki，不是 SuperMemo——适合我吗？**
适合。甄别把关、制卡手艺（包括 `{{c1::…}}` 填空输出）、修卡诊所和学习
哲学完全与工具无关；只有工具教练和渐进阅读的具体操作是 SuperMemo 专属。

**隐私？**
你给伴侣看的材料会发送给驱动它的模型服务。敏感笔记请自行斟酌；
`LEARNER.md` 默认已被 gitignore。

**与 SuperMemo World 有关系吗？**
没有。非官方、未获背书。SuperMemo 是 SuperMemo World 的商标。本项目的
方法性内容提炼自官方 wiki（help.supermemo.org）与 Piotr Wozniak 的著述，
谨致谢意。

## 参与贡献

欢迎 Issue 和 PR。有价值的方向：更好的示例、翻译、对 SuperMemo 参考内容
的勘误（请引用官方 wiki 页面）、更多间隔重复软件的导入格式、更多 Agent
环境的适配说明。请保持设计轻量——增加新参考文件的门槛应当很高，而增加
任何“绕过甄别关制卡”的功能，门槛是无穷高。

## 许可证

本项目自有文件使用 MIT 许可证，见 [LICENSE](LICENSE)。

制卡原则改编自 Piotr Wozniak
[《高效学习：表述知识的二十条规则》](https://super-memory.com/articles/20rules.htm)；
SuperMemo 使用事实提炼自[官方文档](https://help.supermemo.org)。
`spaced-repetition-companion/docs/` 中镜像的官方文档（help.supermemo.org
原样 wikitext、派生渲染页与《二十条规则》一文）版权仍归 SuperMemo World /
各自作者——出处与范围详见
[`docs/README.md`](spaced-repetition-companion/docs/README.md)。
