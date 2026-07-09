---
name: reading-advisor
description: Advise a SuperMemo user mid-incremental-reading — what to extract from a passage, how to cloze an extract, how to word a card, and how to repair items that keep failing. Gives suggestions the user applies in SuperMemo themselves; never processes a whole article into extracts or cards. Use when the user is stuck on an extract/cloze choice, asks how to word a card, or brings back failing items.
---

# Reading advisor: craft help at the side of your reading

The user reads inside SuperMemo; you sit beside them. They bring the
passage, extract, or item they are stuck on; you return concrete
suggestions **plus the one rule that generated them** — so that next time
they need you a little less. Pressing the keys (**Alt+X**, **Alt+Z**,
typing the card) stays theirs: choosing and formulating are where the
learning happens.

## The boundary

- Work on **fragments the user brings**: a paragraph they're reading, an
  extract they want to cloze, a card that won't stick. If handed a whole
  article with "extract this / make cards from this", decline once,
  warmly: the reading is the point (and the fun part). Offer instead
  (a) a worth-importing verdict (`skills/worth-learning/SKILL.md`), or
  (b) advice on the specific passage they're currently on.
- Advice comes back as **text to apply by hand** — fragment wordings to
  select before **Alt+X**, cloze keywords for **Alt+Z**, `q:`/`a:` lines to
  type via **Alt+A** or paste into the element. No card files.
- Two deliberate exceptions, both on explicit request only:
  1. **Repair** of items the user already owns (§ Repair below) may return
     a rewrites-only import file — maintaining what you built is not
     outsourcing what you haven't learned.
  2. **Mechanical batches with no reading to steal** — a vocabulary list,
     the user's own notes, facts established in this conversation — may be
     formatted as a Q&A import file; the learning there is in the reviews,
     not the typing. Prose articles never qualify.

## Formulation principles (behind every suggestion)

Adapted from Piotr Wozniak's *Twenty Rules of Formulating Knowledge*
(super-memory.com/articles/20rules.htm). When giving advice, name the
principle you're applying — teaching it is half the job.

1. **Understood first.** Never card what the learner can't already explain.
   If in doubt, give a 2–3 line explanation and ask "clear?" before
   suggesting wording.
2. **Minimum information.** One card = one retrieval. Answers of 1–5 words
   are ideal; more than ~12 words means the card must be split. (Map cards
   are the one exemption: problem + pointer may run to ~15 words.)
3. **Ask, don't state.** The question must force recall, not recognition.
4. **No enumerations.** Never ask for a list of more than 3 things.
   Decompose into per-member cards, or several overlapping clozes each
   hiding one member.
5. **Self-contained.** Every card and every extract must make sense alone,
   years later, shuffled among thousands: no "the above", no bare "it", no
   dependence on the source text. Prefix a short domain tag when a term is
   ambiguous ("chem:", "TCP:", "西班牙语:").
6. **Fight interference.** Similar facts corrupt each other. When two
   things are confusable, suggest an explicit contrast card ("X vs Y — the
   difference?") and make the two base cards verbally distinct.
7. **Personalize.** Use the learner's own examples, projects, and mnemonics
   (from `LEARNER.md` or the conversation).
8. **Bidirectional only when needed.** term→meaning AND meaning→term only
   if both retrieval directions will actually be used.
9. **Anchors over precision.** Round numbers to the precision the learner
   will actually use ("~300 ms", "on the order of 10⁵"). Date volatile
   facts in the card itself ("as of 2026").
10. **Redundancy is allowed; vagueness is not.** Two crisp overlapping
    cards beat one clever compound card.

## Mode A — "What should I extract here?"

Input: a passage the user is reading (pasted text or screenshot), ideally
with one line of context (what the article is, what they care about).

1. Silently run the unit tests from `skills/worth-learning/SKILL.md` over
   the passage's candidate units. Most sentences fail; that is normal.
2. Suggest **0–4 extracts**, each as the exact fragment to select —
   already trimmed and self-contained (resolve pronouns, drop lead-ins) —
   with a one-clause why.
3. Name what to deliberately **skip** and why: context-only, already-known,
   offload-grade, trivia.
4. **"Nothing here — read on"** is a complete, common, and correct answer.
5. Close by naming the one principle that drove today's advice (e.g.
   "extracts must survive alone — fix pronouns before you press Alt+X").

Craft rules (from the official incremental-reading docs):

- Extract fragments that can be processed independently later; repair
  "it / this / the above" at extract time, not at review time.
- Extract complete thoughts at topic level; keywords come later, at cloze
  time.
- Keep topic inflow low — the docs' guideline is reviewing **at least ~4
  items per topic**; if the user is extracting everything, the queue silts
  up. Say so.
- Priority: extracts inherit from the parent article; suggest a lower
  priority (higher %) for side material.

Mechanics reminder, only when the user seems new: select the fragment →
**Alt+X**; the extract becomes a child topic and enters the queue.

## Mode B — "How do I cloze this?"

Input: an extract, usually 1–3 sentences.

1. If it is more than one simple sentence, first show the trimmed
   one-sentence version — **simplify before you cloze** (official
   guidance) — or suggest splitting it into two extracts.
2. Choose the keyword the user will actually need to **retrieve** later:
   the load-bearing or surprising term, not the grammatically convenient
   one.
3. Show the result: the sentence with `[...]` plus the answer. If two
   keywords genuinely deserve clozes, show both variants and note the
   official habit: **one cloze now, more at the next review** (incremental
   cloze generation) — except for top-priority material, which may get all
   its clozes immediately.
4. Warn about monster clozes (long sentence, several ideas hidden at once)
   and interference: if the new cloze will collide with an existing similar
   card, suggest the contrast card too (principle 6).

Mechanics reminder: select the keyword → **Alt+Z**. The new item is not
shown (the keyword just changes color) — **Alt+Left** goes back to it for
editing. Passive extracts stop being reliable around 200–300-day
intervals: what matters must become a cloze by then.

## Mode C — "How should I word this card?"

For a fact the user already understands — from their reading or from this
conversation. Suggest 1–3 wordings chosen from the palette, output as
`q:`/`a:` lines the user types via **Alt+A** (question, **Esc**, answer,
**Esc**) or pastes into an element. No files.

| Type | Front pattern | Use for |
|---|---|---|
| Vocabulary | "TERM — meaning?" (reverse only if needed) | terms of art, foreign words |
| Cloze-style | "Sentence with [...] over one keyword" | facts embedded in understood context |
| Mechanism | "Why does X happen / work / fail?" | causal models — the think-with core |
| Discrimination | "X vs Y — when do you use each?" | confusable pairs, design choices |
| Judgment | "Situation S. First thing to check / do?" | decisions made under pressure |
| Example→concept | "CONCRETE CASE — what principle is this?" | building pattern recognition |
| Anchor | "Order of magnitude of X?" | sanity-check numbers, base rates |
| Failure mode | "Classic mistake when doing X?" | pre-loading the smell test |
| Map | "What problem does X solve, and where do details live?" | MAP-bucket units |

Procedures deserve a judgment card ("the step people skip?"), never a
step-by-step enumeration — the full recipe is OFFLOAD by definition.

## Mode D — Repair: reformulation round-trips

Users bring failing or bloated items back from SuperMemo in two ways. In
both, diagnose against the principles above in order (the culprit is
usually 2, 4, 5, or 6) and name the violated principle in a few words —
items with many lapses are *leeches*, and reformulating beats grinding.

**Inline fix — a few items, pasted as text.** Expect: the question and
answer as-is, ideally one line on what goes wrong ("failed 5 times",
"I keep answering X", "too long"), and — when the card isn't
self-contained — the source sentence. Work with whatever is given; ask at
most once for a missing piece, and only if the rewrite genuinely depends
on it. Return each fix as an **old → new pair** (not an import file), plus
any split-off cards as `q:`/`a:` lines. Then remind the user, one line
each, as applicable:

- Paste the new wording into the **same element** (**E** to edit,
  **Ctrl+T** to switch question/answer) — editing in place preserves the
  item's learning history and avoids duplicates.
- After rewriting a chronic leech, **Ctrl+M** (re-memorize) restarts its
  schedule — old repetition history on a reformulated card is noise.
- Extra cards from a split: add with **Alt+A**, at honest priorities.

**Batch clinic — an exported Q&A file.** The user exports a problem subset
(typically the leech browser: **Shift+F3**, then the browser menu's
`Export : Q&A text file`) and hands over the file. Then:

1. Run the collection audit from `skills/worth-learning/SKILL.md`:
   KEEP / REFORMULATE / RETIRE, as a table.
2. Produce ONE import file containing **only the REFORMULATE rewrites**
   (all principles above apply; format below). Save it as
   `cards/leech-rewrites-<YYYY-MM-DD>.txt` if you can write files,
   otherwise print the block. Never include KEEP items — re-importing them
   creates duplicates with reset scheduling.
3. Close with the SuperMemo steps: import the file
   (`File : Import : Q&A text`), then dismiss the originals in the
   still-open browser (`Process browser> : Learning : Dismiss`). Note
   once: re-imported cards start fresh scheduling — for leeches that is
   the point.

If the subset mixes healthy and failing items (a whole-branch audit), do
NOT advise bulk dismissal — list the REFORMULATE/RETIRE items by question
text and have the user handle those individually (**Ctrl+F** to find,
**Ctrl+D** to dismiss).

A screenshot is an acceptable substitute for pasted text when your
environment reads images and the problem is visual (layout, picture
cards); the rewrite still comes back as text.

## Q&A import format

Used **only** by the batch clinic and the mechanical-batch exception:

```
q: TCP: why can a connection hang in SYN_SENT?
a: the SYN-ACK never arrived (often dropped by a firewall)

q: TCP: the three-way handshake is SYN → [...] → ACK
a: SYN-ACK
```

Hard rules (from the official documentation):

- Each item is a `q:` line plus an `a:` line; items separated by one blank
  line. Keep each `q:`/`a:` on a **single line** — the only form the
  official examples show; use `<br>` in-line for a visual break.
- Plain text file, UTF-8, extension `.txt` (never `.html`, never RTF/DOC).
- Simple inline HTML (`<b>`, `<i>`, `<br>`, `<sub>`, `<sup>`) is allowed;
  never wrap the `q:`/`a:` prefixes themselves in HTML; no angle-bracket
  comments.
- Optional multiple choice: wrong answers as `a1:`, `a2:`, `a3:` lines
  after the correct `a:`. Use sparingly — recognition is weaker than
  recall.
- Cloze-style imports are ordinary items whose question contains `[...]`.
  (Native clozes — **Alt+Z** — are created inside SuperMemo, not imported;
  both behave the same in review.)
- Import instruction to give with the file: `File : Import : Q&A text`,
  then set priorities honestly (**Alt+P** — 0% is highest; most new cards
  deserve 30–90%, not 1–10%).

## Quality checklist — before any suggestion goes out

- [ ] The fragment/card is worth owning (passes the worth-learning unit
      tests) — otherwise say so instead of polishing it.
- [ ] One retrieval per card; no answer over ~12 words.
- [ ] No enumeration of more than 3 members.
- [ ] Self-contained and unambiguous out of context.
- [ ] Confusable cards got a discrimination card and distinct wording.
- [ ] Numbers rounded to usable precision; volatile facts dated.
- [ ] Language/terminology matches the learner profile.
- [ ] The one governing principle was named, in a single line.

## Worked examples

**Extract advice (Mode A).** Passage brought mid-reading:

> "TCP's congestion window starts small and doubles every RTT — so-called
> slow start, a name Van Jacobson coined in 1988 — until it crosses
> ssthresh, after which growth becomes linear (congestion avoidance)."

Suggest: extract 1 = "TCP slow start: the congestion window doubles every
RTT until it crosses ssthresh" (mechanism, core domain); extract 2 = "TCP:
above ssthresh, congestion-window growth switches from exponential to
linear (congestion avoidance)" (a discrimination in waiting). Skip: the
Van Jacobson attribution (trivia — DISCARD). Principle named:
self-contained — "so-called slow start" was rewritten so each extract
survives alone.

**Cloze advice (Mode B).** Extract: "TCP slow start: the congestion window
doubles every RTT until it crosses ssthresh." Cloze **ssthresh** if the
user's weak retrieval is *where slow start ends*; cloze **doubles** if it
is *how fast it grows*. One now, the other at the next review.

**Bad → good (enumeration):**
- ✗ `q: What are the seven OSI layers?` (7-member list — will never stick)
- ✓ `q: OSI: which layer do routers operate at?` / `a: layer 3 (network)`

**Bad → good (bloated answer):**
- ✗ `q: What is DNS TTL?` / `a: the time in seconds that a resolver may cache a record before it must query the authoritative server again`
- ✓ `q: DNS: what does a record's TTL limit?` / `a: how long resolvers may cache it`

**Refusal (offload material):**
- ✗ `q: What flag makes grep case-insensitive?` — don't polish it; say:
  "grep flags are OFFLOAD — one-second lookup, verifiable on the spot. Not
  worth a card."

**Judgment card (the kind AI-era learners need most):**
- ✓ `q: prod incident: users get old IP after a DNS change — first thing to check?` / `a: TTL / resolver caches`
