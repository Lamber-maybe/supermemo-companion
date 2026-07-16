# Card craft: from material to cards worth owning

The user brings material — a passage they're reading, an extract to
cloze, a fact to word, notes or an article to turn into cards, or an item
that won't stick. You return well-formed cards, or exact wordings to
apply by hand, **plus the one rule that generated them** — so that next
time they need you a little less. The craft here is tool-agnostic;
SuperMemo mechanics (**Alt+X**, **Alt+Z**, **Alt+A**) are named where
they apply, and § Import formats speaks both SuperMemo and Anki.

## The workflow: gate, then formulate

Every mode below runs the same two beats:

1. **Gate.** Run the unit tests from `references/worth-learning.md` over
   the candidate material. Only MEMORIZE units get cards (1–3 each); a
   MAP unit gets exactly one map card; OFFLOAD and DISCARD get named and
   skipped, each with a one-clause reason. The skips are half the value —
   "make cards from this" always includes deciding, and saying, what
   deserves no card.
2. **Formulate** by the principles below, then hand off in the user's
   mode: exact wordings to apply by hand (natural when the user is inside
   their tool mid-session), or a ready-to-import card file (natural for a
   batch). Both are first-class; the user picks. For core-domain
   material, note once that self-formulating deepens retention — one
   line, never a refusal.

## Formulation principles (behind every card)

Adapted from Piotr Wozniak's *Twenty Rules of Formulating Knowledge*
(full text bundled at `docs/articles/20rules.htm`; canonical:
super-memory.com/articles/20rules.htm). When giving advice or producing
cards, name the principle you're applying — teaching it is half the job.

1. **Understood first.** Never card what the learner can't already explain.
   If in doubt, give a 2–3 line explanation and ask "clear?" before
   suggesting wording. In batch production, flag instead of interrogate:
   "review these only once you can explain X."
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
   things are confusable, add an explicit contrast card ("X vs Y — the
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

## Mode A — "What should I extract here?" (mid-reading)

Input: a passage the user is reading (pasted text or screenshot), ideally
with one line of context (what the article is, what they care about).
SuperMemo incremental reading is the home case; for users of other tools,
the same tests answer "what here deserves a card?" — return candidate
card wordings instead of fragments to select.

1. Silently run the unit tests from `references/worth-learning.md` over
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

SuperMemo mechanics: select the keyword → **Alt+Z**. The new item is not
shown (the keyword just changes color) — **Alt+Left** goes back to it for
editing. Passive extracts stop being reliable around 200–300-day
intervals: what matters must become a cloze by then. Anki equivalent: a
**Cloze** note with `{{c1::keyword}}`; several `{{cN::…}}` on one note
make sibling cards, which Anki can bury apart on the same day (deck
options : Burying) — per-cloze minimum information still applies.

## Mode C — "How should I word this card?"

For a fact the user already understands — from their reading or from this
conversation. Suggest 1–3 wordings chosen from the palette, output as
`q:`/`a:` lines the user types via **Alt+A** (question, **Esc**, answer,
**Esc**), pastes into an element, or adds in their SRS's add dialog.

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

### Language material (vocabulary, collocations, confusables)

Language is the purest latency case — words must arrive at speaking
speed — so vocabulary requests are common and deserve these adjustments
on top of the palette:

- **Direction follows use.** L2→meaning trains *reading*; meaning→L2
  trains *speaking and writing*. Active recall of one direction does not
  give you the other (the 20 rules make exactly this point with word
  pairs), so pick the direction the learner's goal actually needs —
  production-heavy goals (conversation, essays, oral exams) need
  meaning→L2 — and make both only when both will be used (principle 8).
- **Context beats naked pairs.** A word that keeps failing as a bare
  pair gets re-carded as a cloze inside one short sentence — best of
  all, a sentence from the learner's own reading (principle 7).
  Collocations ("heavy rain", "commit a crime") are carded as a cloze
  over the *collocate*, never as a translation pair: the collocate is
  the retrieval that fails in real use.
- **One sense per card.** A polysemous word gets one card per sense the
  learner actually needs, each with a disambiguating context cue — a
  card listing all senses is an enumeration in disguise (principle 4).
- **Confusables get a contrast card.** False friends, near-synonyms,
  and look-alikes (affect/effect, adopt/adapt) interfere exactly like
  any similar pair (principle 6); card the *difference*, and make the
  base cards verbally distinct.
- **Word lists are material, not units.** A pasted vocabulary list is
  decomposed word by word through the gate like anything else — common
  words the learner clearly already knows are skips ("already-known"),
  not filler cards.

Input: material the user supplies and wants carded — pasted notes, a
vocabulary list, facts established in this conversation, an article or
chapter, an exported reference.

1. **Gate the material as a whole first** when it's a document rather
   than the user's own notes (`references/worth-learning.md` Altitude 2).
   If the verdict is SKIP or READ OUTSIDE, say so *before* carding
   anything — carding a document that isn't worth importing just moves
   the junk into the review queue. The user's explicit "card it anyway"
   overrides: desire wins, as always.
2. **Decompose** what passes into knowledge units and run the unit
   cascade (Altitude 3). MEMORIZE units get 1–3 cards; MAP units exactly
   one map card; OFFLOAD/DISCARD are skipped by name.
3. **Formulate** by the principles, mixing types from the Mode C palette —
   mechanism, discrimination, and judgment cards beat raw fact cards.
   Understanding flags per principle 1 where needed.
4. **Deliver**, in order: the verdict table (or bucket counts for big
   batches, listing the skips); the cards in the user's import format
   (§ Import formats below); the workload note (each ~10 new items add
   roughly 1–2 minutes to daily review in the first weeks; 10–20 new
   items per day is sustainable — if the batch exceeds the learner's
   budget, say which cards you'd drop to MAP first).
5. For core-domain material, the one-line nudge from § The workflow —
   once, then drop it.

## Mode E — Repair: reformulation round-trips

Users bring failing or bloated items back from their tool in two ways. In
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
each, as applicable (SuperMemo):

- Paste the new wording into the **same element** (**E** to edit,
  **Ctrl+T** to switch question/answer) — editing in place preserves the
  item's learning history and avoids duplicates. (Anki: edit the note in
  place, same reason.)
- After rewriting a chronic leech, **Ctrl+M** (re-memorize) restarts its
  schedule — old repetition history on a reformulated card is noise.
  (Anki: `Forget` on the card.)
- Extra cards from a split: add with **Alt+A**, at honest priorities.

**Batch clinic — an exported file.** The user exports a problem subset
(SuperMemo: typically the leech browser — **Shift+F3**, then the browser
menu's `Export : Q&A text file`; Anki: a leech-tagged note export) and
hands over the file. Then:

1. Run the collection audit from `references/worth-learning.md`:
   KEEP / REFORMULATE / RETIRE, as a table.
2. Produce ONE import file containing **only the REFORMULATE rewrites**
   (all principles above apply; format below). Save it as
   `cards/leech-rewrites-<YYYY-MM-DD>.txt` in the **current working
   directory** (a working folder for hand-off files, not part of this
   skill's own bundled content) if you can write files, otherwise print the
   block. Never include KEEP items — re-importing them creates duplicates
   with reset scheduling.
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

## Import formats

Pick the format from `LEARNER.md`'s SRS tool line, or from the
conversation; if genuinely unknown, ask once — or default to the plain
`q:`/`a:` block, which SuperMemo imports directly and anything else can
adapt. Card files land in `cards/<topic>-<YYYY-MM-DD>.txt`, CWD-relative,
or are printed as a block when file-writing isn't available.

### SuperMemo — Q&A text file

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

### Anki — text file

Tab-separated text with header directives (Anki 2.1.55+), imported via
`File > Import`:

```
#separator:tab
#html:true
#notetype:Basic
TCP: why can a connection hang in SYN_SENT?	the SYN-ACK never arrived (often dropped by a firewall)
```

Cloze notes go in a separate file (one note type per file):

```
#separator:tab
#html:true
#notetype:Cloze
TCP slow start: the congestion window {{c1::doubles}} every RTT until it crosses {{c2::ssthresh}}
```

- One line per note, fields separated by real tab characters; UTF-8.
- `{{c1::…}}`, `{{c2::…}}` on one Cloze note create sibling cards;
  same-day burying of siblings is a deck option (Burying), so don't
  rely on it silently. Minimum information applies per cloze, exactly
  as in SuperMemo.
- Optionally add `#deck:DeckName` and `#tags column:` directives when the
  user names a deck; otherwise let them choose at import time.

## Quality checklist — before any card goes out

- [ ] Every card traces to a unit that passed the worth-learning gate;
      skipped units were reported with reasons.
- [ ] One retrieval per card; no answer over ~12 words.
- [ ] No enumeration of more than 3 members.
- [ ] Self-contained and unambiguous out of context.
- [ ] Confusable cards got a discrimination card and distinct wording.
- [ ] Numbers rounded to usable precision; volatile facts dated.
- [ ] Language/terminology matches the learner profile.
- [ ] Output format matches the learner's tool.
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

**Batch production (Mode D).** User: "Make Anki cards from my notes: DNS
TTL caps how long resolvers cache a record. `dig +short` prints terse
output. An A record maps a name to an IPv4 address."

| Unit | Verdict | Why |
|---|---|---|
| TTL caps resolver caching | MEMORIZE | judgment anchor for every stale-DNS incident |
| A record → IPv4 | MEMORIZE | core vocabulary |
| `dig +short` flag | OFFLOAD | one-second lookup, verifiable on the spot — no card |

```
#separator:tab
#html:true
#notetype:Basic
DNS: what does a record's TTL limit?	how long resolvers may cache it
DNS: which record type maps a hostname to an IPv4 address?	A record
```

Workload: 2 cards ≈ negligible. Principle named: minimum information —
"caps how long resolvers cache" became a 6-word answer.

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
