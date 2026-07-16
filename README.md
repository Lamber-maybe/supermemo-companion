# Spaced Repetition Companion

**Internalize what you think with. Offload what you merely consult.**

**English** · [简体中文](README.zh-CN.md)

A portable **Agent Skill** that turns any capable AI assistant into a
companion for learning with spaced repetition —
[SuperMemo](https://super-memory.com/), [Anki](https://apps.ankiweb.net/),
or any similar tool.

## What it does

1. **Gatekeeping.** *"Is this worth learning at all, now that AI explains
   everything?"* A gate in front of your memory: verdicts with one-clause
   reasons — IMPORT / SKIP for material, MEMORIZE / MAP / OFFLOAD /
   DISCARD for single facts — grounded in an explicit philosophy of
   AI-era learning.
2. **Card production.** *"Make cards from this."* Q&A and cloze cards
   formulated by SuperMemo's twenty rules, delivered in your tool's
   import format (SuperMemo Q&A text, Anki text file). Always gate-first:
   what isn't worth carding comes back as a named skip with a reason,
   not as deck filler.
3. **Craft advice & repair.** What to extract mid-reading, how to cloze,
   how to word a card — plus repair for cards that keep failing (leeches)
   and audits for collections that have silted up.
4. **SuperMemo coaching.** Any *"how do I … in SuperMemo"* question —
   shortcuts, priorities, incremental reading, options, troubleshooting —
   answered from a bundled offline mirror of the official documentation,
   never from guesswork.

Jobs 1–3 are tool-agnostic; job 4 is SuperMemo-deep. The skill's one
standing refusal: it never cards *around* the gate — "twenty cards on X"
where six earned existence gets you six cards and a list of reasons.

## Why this exists

> AI changes the economics of retrieval, but not the mechanics of thought.

Knowledge in the world is *inert* — it does nothing until queried.
Knowledge in your head is *executable* — it runs inside perception,
comprehension, and judgment without being asked. Just as the calculator
killed arithmetic drill and *raised* the price of number sense, AI
automates verbal-procedural work and raises the price of domain sense.
So the answer isn't "learn less" — it's **fewer items, deeper domains,
better cards**.

The full argument — the seven tests for "worth memorizing?", the
four-destinations model, the skill's exact boundaries — ships inside the
skill at
[`references/philosophy.md`](spaced-repetition-companion/references/philosophy.md),
so it travels wherever the skill is installed.

## Install

Everything lives in one self-contained directory:
[`spaced-repetition-companion/`](spaced-repetition-companion/) — that
directory is the thing you copy.

| Setup | How |
|---|---|
| **Working directly in this repo** | Nothing to do — `AGENTS.md` / `CLAUDE.md` at the root already point auto-loading agents at the skill. |
| **Your own project** (recommended) | Copy or symlink `spaced-repetition-companion/` into wherever your agent looks for Agent Skills (e.g. `.claude/skills/spaced-repetition-companion/`), keeping the directory name unchanged. |
| **Any agent that just reads files** | Say once: *"Read spaced-repetition-companion/SKILL.md and follow it."* |

Then — optional but worth the 2 minutes — copy
[`assets/LEARNER.example.md`](spaced-repetition-companion/assets/LEARNER.example.md)
to `LEARNER.md` (in your working directory or your home directory) and
fill in your goals, domains, review budget, and SRS tool. It is what
makes verdicts, cards, and coaching personal, and it is gitignored here
by default.

No frontier model required: the skill is deliberately mechanical —
checklists, ordered decision rules, fixed output shapes — so a mid-tier
(Sonnet-class) model follows it reliably.

### First prompts to try

- *"What's still worth learning deeply, now that AI can explain anything?"*
- *"Is this article worth importing into my collection?"* (paste it)
- *"Make Anki cards from these notes."* (paste them)
- *"I'm reading this paragraph and don't know what to extract — suggestions?"*
- *"This card has failed five times — fix it."*
- *"How do incremental reading priorities actually work?"*

## What's inside

```
spaced-repetition-companion/       <- the whole portable skill — copy this directory, nothing else
  SKILL.md                          entry point: principle, routing, ground rules, personalization
  LICENSE                           MIT, covers this skill's own files
  references/
    worth-learning.md                direction · import gatekeeping · memorize-or-not
    card-craft.md                    card production (Q&A + cloze) · extract/cloze/wording · repair
    supermemo-coach.md               answers any "how do I … in SuperMemo?"
    reference.md                     distilled SuperMemo reference (offline)
    incremental-learning.md          the method's philosophy, distilled
    philosophy.md                    the AI-era learning argument, in full
    sample-session.md                worked example transcripts
  docs/
    wiki/                            revision-pinned offline mirror of help.supermemo.org
    articles/20rules.htm             Wozniak's formulation-rules article
  assets/LEARNER.example.md          personal profile template
  scripts/import_supermemo_help.py   rebuild and validate the wiki mirror

AGENTS.md / CLAUDE.md              <- thin pointers for agents that auto-load a repo root
LEARNER.md                          <- your profile, if kept here (gitignored)
cards/                              <- generated card files land here (gitignored)
```

The skill's own instruction files are in English (most reliable across
models); the agent converses in **your** language.

## Design principles

- **Portable.** One skill directory, loadable by any agent that supports
  Agent Skills — or just told to read `SKILL.md`. Every internal path is
  relative to the skill's own directory, never to the host project.
- **Gate before craft.** Card production is a first-class deliverable,
  but it always runs behind the worth-learning tests. The named,
  reasoned skips are half the product: every card is years of future
  review time.
- **Tool-agnostic core, SuperMemo-deep edge.** Gatekeeping and
  formulation work for any SRS and speak both SuperMemo's and Anki's
  import formats. Tool coaching is SuperMemo-only, backed by a complete
  offline documentation mirror — the coach never guesses a shortcut.
  (The online wiki sits behind a Cloudflare challenge;
  https://help.supermemo.org remains the final authority.)
- **Teach while helping.** Every card and suggestion names the one
  formulation principle behind it, so you need the skill a little less
  each time. Reading stays in your hands; for your core domains it
  nudges — once — toward formulating cards yourself.

## FAQ

**Does AI make spaced repetition obsolete?**
No — more valuable. AI is the best explainer you'll ever have, but
understanding you don't retain evaporates in weeks. AI makes
understanding cheap; spaced repetition makes it permanent.

**Will it really make the cards for me?**
Yes — after the gate. Material is decomposed into knowledge units, each
unit tested (MEMORIZE / MAP / OFFLOAD / DISCARD), and only what passes
gets carded, in your tool's import format. What fails comes back as a
named skip with a one-clause reason.

**I use Anki, not SuperMemo — is this for me?**
Yes. The gatekeeper, the card craft (including `{{c1::…}}` cloze
output), the repair clinic, and the philosophy are fully tool-agnostic.
Only the tool coaching and incremental-reading mechanics are
SuperMemo-specific.

**Privacy?**
Material you show the companion is sent to whatever model powers your
agent. Keep that in mind for sensitive notes; `LEARNER.md` is gitignored
by default.

**Is this affiliated with SuperMemo World?**
No. Unofficial, unendorsed. SuperMemo is a trademark of SuperMemo World.
Method concepts are distilled from the official wiki
(help.supermemo.org) and Piotr Wozniak's writings, with attribution and
gratitude.

## Contributing

Issues and PRs welcome. Useful contributions: better worked examples,
translations, corrections to the SuperMemo reference (cite the official
wiki page), import formats for more SRS tools, adapters for more agent
environments. Keep the design lightweight — the bar for adding a new
reference file is high, and the bar for adding anything that cards
around the gate is infinite.

## License

MIT for this project's own files — see [LICENSE](LICENSE).

Formulation principles adapted from Piotr Wozniak,
[*Effective learning: Twenty rules of formulating knowledge*](https://super-memory.com/articles/20rules.htm).
SuperMemo usage facts distilled from the
[official SuperMemo documentation](https://help.supermemo.org). The
official documentation mirrored in `spaced-repetition-companion/docs/`
(exact help.supermemo.org wikitext, derived rendered pages, and the
twenty-rules article) remains © SuperMemo World / its respective authors
— see
[`docs/README.md`](spaced-repetition-companion/docs/README.md) for
provenance.
