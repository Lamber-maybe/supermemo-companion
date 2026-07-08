---
name: formulate
description: Turn approved knowledge into well-formed SuperMemo items — atomic questions, cloze-style cards, discriminations, mechanism and judgment cards — and deliver them in SuperMemo's Q&A import format. Use after triage, or whenever the user asks for cards/items from material they already understand, or wants existing cards improved.
---

# Formulate: turn knowledge into items worth reviewing

Prerequisite: the material has verdicts from `skills/triage/SKILL.md`, or the
user explicitly says "just make cards from this" (then apply triage silently
and mention anything you chose *not* to card, in one line).

Card only MEMORIZE and MAP units. Never card OFFLOAD or DISCARD material —
if the user insists, say once why it fails the tests, then comply.

## Formulation principles

Adapted from Piotr Wozniak's *Twenty Rules of Formulating Knowledge*
(super-memory.com/articles/20rules.htm); the numbers below are the subset an
agent must never violate.

1. **Understood first.** Never card what the learner can't already explain.
   If in doubt, give a 2–3 line explanation and ask "clear?" before carding.
2. **Minimum information.** One card = one retrieval. Answers of 1–5 words
   are ideal; more than ~12 words means the card must be split. (Map cards
   are the one exemption: problem + pointer may run to ~15 words.)
3. **Ask, don't state.** The question must force recall, not recognition.
   "What does X do?" beats "X does Y, right?"
4. **No enumerations.** Never ask for a list of more than 3 things. Decompose
   into per-member cards ("which member of SET does JOB?"), or use several
   overlapping cloze-style cards each hiding one member.
5. **Self-contained.** Every card must make sense alone, years later, shuffled
   among thousands: no "the above", no bare "it", no dependence on the source
   text. Prefix a short domain tag when the term is ambiguous ("chem:",
   "TCP:", "西班牙语:").
6. **Fight interference.** Similar facts corrupt each other. When two things
   are confusable, add an explicit contrast card ("X vs Y — the difference?")
   and make the two base cards visually/verbally distinct.
7. **Personalize.** Use the learner's own examples, projects, and mnemonics
   (from `LEARNER.md` or the conversation) — personal context beats textbook
   phrasing.
8. **Bidirectional only when needed.** term→meaning AND meaning→term only if
   both retrieval directions will actually be used (e.g. vocabulary for both
   reading and speaking).
9. **Anchors over precision.** Round numbers to the precision the learner
   will actually use ("~300 ms", "on the order of 10⁵"). Date volatile facts
   in the card itself ("as of 2026").
10. **Redundancy is allowed; vagueness is not.** Two crisp overlapping cards
    beat one clever compound card.

## Card type palette

Choose types by what the unit *is*. MEMORIZE units get 1–3 cards; MAP units
get exactly one map card.

| Type | Front pattern | Use for |
|---|---|---|
| Vocabulary | "TERM — meaning?" (and reverse if needed) | terms of art, foreign words |
| Cloze-style | "Sentence with [...] replacing one keyword" | facts embedded in understood context |
| Mechanism | "Why does X happen / work / fail?" | causal models — the think-with core |
| Discrimination | "X vs Y — when do you use each?" | confusable pairs, design choices |
| Judgment | "Situation S. First thing to check / do?" | decisions made under pressure |
| Example→concept | "CONCRETE CASE — what principle is this?" | building pattern recognition |
| Anchor | "Order of magnitude of X?" / "Roughly how many/long?" | sanity-check numbers, base rates |
| Failure mode | "Classic mistake when doing X?" | pre-loading the smell test |
| Map | "What problem does X solve, and where do details live?" | MAP-bucket units |

Procedures deserve a judgment card ("what's the first step / the step people
skip?"), never a step-by-step enumeration — the full recipe is OFFLOAD by
definition.

## Output format — SuperMemo Q&A import

Deliver the final card set as one plain-text block in SuperMemo's Q&A
format, exactly:

```
q: TCP: why can a connection hang in SYN_SENT?
a: the SYN-ACK never arrived (often dropped by a firewall)

q: TCP: the three-way handshake is SYN → [...] → ACK
a: SYN-ACK
```

Hard rules for this format (from the official documentation):

- Each item is a `q:` line plus an `a:` line; items separated by one blank
  line. Keep each `q:`/`a:` on a **single line** — that is the only form
  the official examples show, and multi-line entries import unreliably. For
  a visual line break inside a card, use `<br>` in-line.
- Plain text file, UTF-8, extension `.txt` (never `.html`, never RTF/DOC).
- Simple inline HTML tags (`<b>`, `<i>`, `<br>`, `<sub>`, `<sup>`) are
  allowed; never wrap the `q:`/`a:` prefixes themselves in HTML, and avoid
  angle-bracket comments — official guidance is that the importer ignores
  them.
- Optional multiple choice: add wrong answers as `a1:`, `a2:`, `a3:` lines
  after the correct `a:` line. Use sparingly — recognition is weaker than
  recall; it's occasionally right for discrimination training.
- Cloze-style imports are ordinary items whose question contains `[...]`.
  (Native SuperMemo clozes — Alt+Z during incremental reading — are created
  inside SuperMemo, not imported; both behave the same in review.)

Delivery:

1. Two-line header: how many cards, from which buckets, anything you merged
   or dropped.
2. The Q&A block (in a fenced code block if printing to chat).
3. If you can write files: also save it as
   `cards/<topic>-<YYYY-MM-DD>.txt` and say so.
4. One-line import instruction: **File : Import : Q&A text** in SuperMemo,
   then set priorities honestly (Alt+P — 0% is highest; most new cards
   deserve 30–90%, not 1–10%).
5. If the user explicitly asks for another format (e.g. TSV for Anki), keep
   every content rule above and emit that format instead.

## Quality checklist — run before delivering

- [ ] Every card traces to a MEMORIZE or MAP verdict.
- [ ] One retrieval per card; no answer over ~12 words.
- [ ] No enumeration of more than 3 members.
- [ ] Each card self-contained and unambiguous out of context.
- [ ] Confusable cards have a discrimination card and distinct wording.
- [ ] Numbers rounded to usable precision; volatile facts dated.
- [ ] Question language/terminology matches the learner profile.
- [ ] Format valid: single-line q/a, blank-line separated, no stray HTML.

## Worked examples

**Bad → good (enumeration):**
- ✗ `q: What are the seven OSI layers?` (7-member list — will never stick)
- ✓ `q: OSI: which layer do routers operate at?` / `a: layer 3 (network)`
- ✓ `q: OSI: TLS sits between which two layers in practice?` / `a: transport (4) and application (7)`

**Bad → good (bloated answer):**
- ✗ `q: What is DNS TTL?` / `a: the time in seconds that a resolver may cache a record before it must query the authoritative server again`
- ✓ `q: DNS: what does a record's TTL limit?` / `a: how long resolvers may cache it`
- ✓ `q: DNS: classic mistake right before changing a record?` / `a: not lowering the TTL in advance`

**Refusal (offload material):**
- ✗ `q: What flag makes grep case-insensitive?` — don't produce it; note
  instead: "grep flags are OFFLOAD — one-second lookup, verifiable on the
  spot. Skipped."

**Judgment card (the kind AI-era learners need most):**
- ✓ `q: prod incident: users get old IP after a DNS change — first thing to check?` / `a: TTL / resolver caches`

## Improving existing cards

When the user brings a card that isn't sticking: diagnose against the
principles above in order (usually it violates 2, 4, or 5), show the
rewrite as old → new, and remind them: in SuperMemo, items with many lapses
are *leeches* — reformulating beats grinding (see
`skills/supermemo-coach/reference.md`).
