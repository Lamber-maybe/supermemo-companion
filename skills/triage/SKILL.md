---
name: triage
description: Decide what knowledge is worth memorizing. Sorts learning material into four buckets — memorize deeply, keep map-level awareness, offload to AI/references, or discard — using the "internalize what you think with" tests. Use when the user brings material to learn, asks "should I memorize this?", or wants an existing SuperMemo collection audited.
---

# Triage: decide what deserves memory

Purpose: apply the project's core principle — *internalize what you think
with, offload what you merely consult* — to concrete material, one knowledge
unit at a time. Triage produces verdicts, not cards. Card-making lives in
`skills/formulate/SKILL.md`.

## Step 0 — Learner context

Read `LEARNER.md` at the repository root if it exists. If it doesn't, and the
verdicts would genuinely change based on the answers, ask at most these three
questions (one short message, then proceed with stated assumptions if
unanswered):

1. What do you do / what are you working toward? (defines **core** domains)
2. Is this material core, adjacent, or peripheral to that?
3. Roughly how much daily review time do you want to spend?

Afterwards, offer once to save the answers as `LEARNER.md`
(template: `examples/LEARNER.example.md`).

## Step 1 — Decompose into knowledge units

Split the material into units that can each receive one verdict. A unit is a
single concept, distinction, mechanism, cause–effect claim, number, term,
procedure, or example — not a paragraph and not a whole topic. Typical
paragraph yields 1–4 units. Ignore filler, transitions, and repetition.

## Step 2 — Apply the decision procedure to each unit

**Pre-check:** if the learner has explicitly said they want this unit
memorized, the verdict is MEMORIZE — desire overrides the cascade below.
Skip the remaining checks.

Otherwise work through the checks **in this order**; first verdict that
fires wins.

1. **DISCARD** if the unit has no plausible use for this learner within a few
   years AND no connective value (it wouldn't help them understand or find
   anything else). Trivia, padding, author asides, redundant restatements.

2. **OFFLOAD** if the unit is needed only occasionally AND can be retrieved
   in under a minute at the moment of use AND is verifiable on the spot.
   Classic offloads: tool syntax and flags, config formats, API signatures,
   exact values where a rough anchor suffices, step-by-step procedures always
   performed with the tool open, anything that changes faster than yearly.

3. **MEMORIZE** if ANY of these is true (and the unit will still be true in
   5–10 years, or the learner knowingly accepts maintaining volatile
   knowledge because it is core to their work):
   - **Latency** — needed at the speed of thought or conversation, or under
     pressure with no tools (interviews, incidents, patient/client in front
     of you, speaking a language).
   - **Foundation** — other things in the domain won't make sense without it
     (core vocabulary, central mechanisms, canonical examples).
   - **Judgment anchor** — used to sanity-check AI or human output: orders of
     magnitude, base rates, failure modes, "X vs Y" discriminations.
   - **Collision** — material the learner wants resident for background
     thinking and creative connection, in a domain where they aim to build
     or create.
   - **Frequency** — comes up weekly or more in the learner's actual work.
   - **Desire** — the learner explicitly wants it as part of themselves.
     Desire overrides every efficiency argument; don't argue with it.

4. **MAP** for everything left that has connective value: the learner should
   know it *exists*, what problem it solves, roughly when it applies, and
   where the details live — but not the details themselves.

**Domain-centrality modifier:** for the learner's core domain, be generous —
details near the MEMORIZE/MAP boundary go to MEMORIZE (fluency compounds).
For peripheral domains, be strict — near-boundary units drop to MAP or
OFFLOAD.

**Tie-breaker:** when genuinely torn between MEMORIZE and MAP, choose MAP and
note the **rule of three lookups**: if the learner catches themselves looking
something up for the third time, it has earned promotion to MEMORIZE.

## Step 3 — Report

Output exactly this structure:

1. A one-line summary of the learner context you applied.
2. The triage table:

   | # | Knowledge unit | Verdict | Why (one clause) |
   |---|---------------|---------|------------------|

   Verdicts: `MEMORIZE` / `MAP` / `OFFLOAD` / `DISCARD`. Keep "why" to a
   single clause naming the test that fired (e.g. "judgment anchor",
   "volatile — offload", "no connective value").
3. Counts per bucket and an estimated card yield (MEMORIZE ≈ 1–3 cards per
   unit, MAP = 1 card per unit) with a workload sanity note. Rule of thumb:
   each ~10 new items add roughly 1–2 minutes to *daily* review time in the
   first weeks; a sustainable habit for most people is 10–20 new items per
   day, so if this batch exceeds the learner's budget, say which units you'd
   cut first (lowest-value MEMORIZE units drop to MAP).
4. Closing line: invite corrections, then "say the word and I'll formulate
   the cards" (→ `skills/formulate/SKILL.md`). Exception: in the
   single-response pipeline (AGENTS.md, small inputs), skip the closing line
   and continue straight into formulation.

Do not argue every verdict at length; the table's "why" clause is enough.
Expand only if the user pushes back on a specific row.

## Collection audit mode

When the user brings *existing* SuperMemo items (pasted, or exported via
`File : Export : Q&A text file`): apply the same procedure to each item's
underlying knowledge, but report verdicts as `KEEP` / `REFORMULATE` (state
what's wrong — usually too broad, enumeration, or no context) / `RETIRE`
(dismiss or delete in SuperMemo; explain: dismissing removes it from review
without deleting content). Be aggressive: every retired item is a permanent
reduction of the review tax. Summarize: "kept X, reformulate Y, retire Z —
about N minutes of daily review reclaimed."

## Worked micro-examples

Material: "TCP handshake is SYN → SYN-ACK → ACK. The SYN flag is bit 1 of
byte 13 of the TCP header. Firewalls that drop SYN-ACK cause connections to
hang in SYN_SENT."

| # | Knowledge unit | Verdict | Why |
|---|---------------|---------|-----|
| 1 | Three-way handshake sequence | MEMORIZE | foundation of all connection reasoning |
| 2 | SYN flag's exact bit/byte offset | OFFLOAD | rarely needed, instantly retrievable, verifiable |
| 3 | Dropped SYN-ACK ⇒ stuck in SYN_SENT | MEMORIZE | judgment anchor for debugging |

Material: "Zettelkasten was popularized by sociologist Niklas Luhmann, who
wrote 70 books. Its core move: every note links to at least one other note."

| # | Knowledge unit | Verdict | Why |
|---|---------------|---------|-----|
| 1 | Luhmann wrote ~70 books | DISCARD | trivia, no connective value |
| 2 | Zettelkasten: every note must link | MAP | know the idea exists and when to reach for it |

## Anti-patterns

- Carding everything "to be safe" — that is the failure mode this project
  exists to prevent.
- More than one round of questions before triaging.
- Producing cards inside this skill (hand off to `formulate`).
- Treating the learner's stated desire to memorize something as an error.
