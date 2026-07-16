# Worth-learning: the gate in front of your memory

Purpose: apply the skill's core principle — *internalize what you think
with, offload what you merely consult* — at whatever altitude the user
brings it: a life direction, a candidate import, or a single fact. This
file produces **verdicts and reasons — never summaries**. Card production
itself lives in `references/card-craft.md`, and every card made there
must first pass this file's tests: the gate runs *before* the craft.
Works for any spaced-repetition tool; SuperMemo mechanics are marked.

## Step 0 — Learner context

Look for `LEARNER.md` using this skill's discovery order (`SKILL.md` §
Personalization: current working directory, then the user's home
directory). If it doesn't exist, and the verdicts would genuinely change
based on the answers, ask at most these three questions (one short message,
then proceed with stated assumptions if unanswered):

1. What do you do / what are you working toward? (defines **core** domains)
2. Is this material core, adjacent, or peripheral to that?
3. Roughly how much daily review time do you want to spend?

Afterwards, offer once to save the answers as `LEARNER.md`
(template: `assets/LEARNER.example.md`).

## Altitude 0 — "Why learn at all, now that AI answers everything?"

When the user doubts the point of learning, make this case briefly, in your
own words, tied to their situation — then steer to something concrete:

- Knowledge in the world is **inert**: it does nothing until queried.
  Knowledge in your head is **executable**: it runs inside perception,
  comprehension, and judgment without being asked. No external oracle
  changes this — the oracle sits on the wrong side of your eyes.
- Three consequences: **you can't query what you can't name** (good
  questions are made of internalized concepts); **discrimination is now the
  scarce skill** (fluent wrong answers are cheap; doubt needs internal
  anchors); **insight is collision** (creative connections form only
  between ideas resident in the same brain).
- The calculator precedent: it killed arithmetic drill and *raised* the
  price of number sense. AI automates verbal-procedural work and raises the
  price of domain sense.
- Conclusion: not "learn less" — **fewer items, deeper domains, better
  cards**. AI multiplies what you know, and a multiplier is worth more the
  more it has to multiply.

Full essay: `references/philosophy.md`. Close by offering to apply the
argument: "name a domain, or bring a concrete article, and I'll run the
tests."

## Altitude 1 — Direction ("what should I learn?")

A conversation, not a table. Anchor every recommendation in four questions:

1. **Durability** — will it still be true and valuable in 5–10 years?
   Prefer mechanisms, fundamentals, domain vocabulary, and canonical
   examples over tool-of-the-year details.
2. **Leverage** — does it multiply what the user already has (core domains,
   daily work), or open an unrelated 37th front?
3. **Judgment surface** — will it help them evaluate AI and human output in
   domains where being wrong costs them?
4. **Desire** — do they *want* it as part of themselves? Long learning runs
   on joy; a dutiful plan dies in three weeks. (This is also why the
   reading itself stays in the user's hands.)

Output: a short, opinionated recommendation — one or two domains to go
**deep** on and why; what to explicitly **not** invest in (offload-grade or
fast-depreciating material); and the next concrete step, which is always
small: "find one real chapter or article and bring it back for a
gatekeeping verdict." Never produce a grand curriculum or a 12-month plan.

## Altitude 2 — Material ("should I import this?")

The user names or pastes a candidate for their collection or deck:
article, chapter, book, course, video, feed. Do **not** summarize it —
gatekeeping returns a verdict, so skim only enough to judge. Work
through:

1. **Domain fit** — core / adjacent / peripheral (from `LEARNER.md`).
2. **Half-life** — mechanisms and fundamentals, or news, releases, and
   listicles that expire within a year?
3. **Density** — will working through this yield extracts and cards the
   user wants to own, or is it motivation, entertainment, or repetition
   of what they already know?
4. **Redundancy** — is this already covered by something in the collection?

Then exactly one verdict:

| Verdict | Meaning | Also say |
|---|---|---|
| **IMPORT** | worth incremental reading / careful carding | suggested priority (SuperMemo) + one-clause why |
| **IMPORT PART** | only some sections qualify | which parts; why the rest fails |
| **READ OUTSIDE** | worth one enjoyable pass, not a review stream | "read it for fun; bring back anything that surprises you" |
| **SKIP** | fails the tests | the one-clause AI-era reason |

Priority suggestion (SuperMemo): use the documented 3-point scale
(≈1% / 33% / 88%, where 0% is highest), relative to the user's core
domains; when hesitating between two values, pick the *lower* priority
(the higher percentage). Most material is not top-priority.

Volume sanity: a collection is not a read-later app. Importing feels like
learning but isn't; every import either costs review time or silts up the
queue. If imports are visibly outrunning reading, say so — the kindest
verdict is often SKIP.

## Altitude 3 — Single units ("should I memorize this?")

A unit is a single concept, distinction, mechanism, cause–effect claim,
number, term, procedure, or example — not a paragraph and not a whole
topic.

**Pre-check:** if the learner has explicitly said they want this unit
memorized, the verdict is MEMORIZE — desire overrides the cascade below.
Skip the remaining checks.

Otherwise work through the checks **in this order**; first verdict that
fires wins.

1. **DISCARD** if the unit has no plausible use for this learner within a
   few years AND no connective value (it wouldn't help them understand or
   find anything else). Trivia, padding, author asides, redundant
   restatements.

2. **OFFLOAD** if the unit is needed only occasionally AND can be retrieved
   in under a minute at the moment of use AND is verifiable on the spot.
   Classic offloads: tool syntax and flags, config formats, API signatures,
   exact values where a rough anchor suffices, step-by-step procedures
   always performed with the tool open, anything that changes faster than
   yearly.

3. **MEMORIZE** if ANY of these is true (and the unit will still be true in
   5–10 years, or the learner knowingly accepts maintaining volatile
   knowledge because it is core to their work):
   - **Latency** — needed at the speed of thought or conversation, or under
     pressure with no tools (interviews, incidents, patient/client in front
     of you, speaking a language).
   - **Foundation** — other things in the domain won't make sense without
     it (core vocabulary, central mechanisms, canonical examples).
   - **Judgment anchor** — used to sanity-check AI or human output: orders
     of magnitude, base rates, failure modes, "X vs Y" discriminations.
   - **Collision** — material the learner wants resident for background
     thinking and creative connection, in a domain where they aim to build
     or create.
   - **Frequency** — comes up weekly or more in the learner's actual work.
   - **Desire** — the learner explicitly wants it as part of themselves.
     Desire overrides every efficiency argument; don't argue with it.

4. **MAP** for everything left that has connective value: the learner
   should know it *exists*, what problem it solves, roughly when it
   applies, and where the details live — but not the details themselves.

**Domain-centrality modifier:** for the learner's core domain, be generous
— details near the MEMORIZE/MAP boundary go to MEMORIZE (fluency
compounds). For peripheral domains, be strict — near-boundary units drop to
MAP or OFFLOAD.

**Tie-breaker:** when genuinely torn between MEMORIZE and MAP, choose MAP
and note the **rule of three lookups**: the third time the learner catches
themselves looking something up, it has earned promotion to MEMORIZE.

**Reporting.** For a single unit: the verdict plus one clause naming the
test that fired — no table. For a batch:

| # | Knowledge unit | Verdict | Why (one clause) |
|---|---------------|---------|------------------|

plus counts per bucket and a workload sanity note (each ~10 new items add
roughly 1–2 minutes to daily review in the first weeks; 10–20 new items per
day is a sustainable habit — if the batch exceeds the learner's budget, say
which units you'd drop to MAP first).

**What MEMORIZE leads to:** cards, made either by the user themselves —
extracting and clozing during incremental reading, **Alt+A**, or their
SRS's add dialog — or by you, on request, via `references/card-craft.md`
(gate-first, principles applied, importable output). Offer the choice
once, in one line; for core-domain material note that self-formulating
deepens retention, then respect whichever mode the user picks.

## Collection audit mode

When the user brings *existing* items (pasted, or exported — SuperMemo:
`File : Export : Q&A text file` or a browser's `Export : Q&A text file`;
Anki: any plain-text note export): apply the unit cascade to each item's
underlying knowledge, but report verdicts as `KEEP` / `REFORMULATE`
(state what's wrong — usually too broad, enumeration, or no context; the
rewrite itself happens in `references/card-craft.md` § Repair) / `RETIRE`
(dismiss or delete — SuperMemo users: explain once that dismissing
removes an element from review without deleting content; Anki:
suspend/delete). Be aggressive: every retired item is a permanent
reduction of the review tax. Summarize: "kept X, reformulate Y, retire Z —
about N minutes of daily review reclaimed."

## Worked micro-examples

Unit level — material: "TCP handshake is SYN → SYN-ACK → ACK. The SYN flag
is bit 1 of byte 13 of the TCP header. Firewalls that drop SYN-ACK cause
connections to hang in SYN_SENT."

| # | Knowledge unit | Verdict | Why |
|---|---------------|---------|-----|
| 1 | Three-way handshake sequence | MEMORIZE | foundation of all connection reasoning |
| 2 | SYN flag's exact bit/byte offset | OFFLOAD | rarely needed, instantly retrievable, verifiable |
| 3 | Dropped SYN-ACK ⇒ stuck in SYN_SENT | MEMORIZE | judgment anchor for debugging |

Material level — "Should I import *Top 10 AI frameworks to watch in
2026*?" → **SKIP**: half-life under a year, listicle density, near-zero
judgment surface. If one of those frameworks matters to your work, *its
manual* is the import candidate; this article is at best one map card
("these names exist").

Material level — "Should I import chapter 3 of *TCP/IP Illustrated*?"
(networking = core domain) → **IMPORT** at ~30%: durable mechanisms in a
core domain, dense in extract-worthy discriminations.

## Anti-patterns

- Summarizing or digesting the material while judging it — gatekeeping
  returns a verdict, not a digest.
- Carding everything "to be safe" — the failure mode this project exists
  to prevent.
- Waving every import through because "priorities will absorb it".
- Grand curricula and 12-month plans at Altitude 1.
- More than one round of questions before judging.
- Producing summaries anywhere in this skill — and producing cards *here*:
  carding happens in `references/card-craft.md`, after this gate has run.
- Treating the learner's stated desire to memorize something as an error.
