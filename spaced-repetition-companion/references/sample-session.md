# Sample sessions (condensed)

What good exchanges look like in practice. Any capable agent following this
skill's `SKILL.md` should produce something of this shape. Throughout,
notice the gate running before anything is carded — and that inside the
tool, the user presses the keys.

---

## Scene 1 — Gatekeeping an import

**User:** Two candidates for SuperMemo: chapter 3 of *TCP/IP Illustrated*
(PDF), and "Top 10 AI frameworks to watch in 2026" from my feed. Import
both?

**Agent:** Context applied: networking is a **core** domain (LEARNER.md).

| Candidate | Verdict | Why |
|---|---|---|
| *TCP/IP Illustrated* ch. 3 | **IMPORT** at ~30% | durable mechanisms in a core domain; dense in extract-worthy discriminations |
| "Top 10 AI frameworks 2026" | **SKIP** | half-life < 1 year, listicle density, no judgment surface |

If one of those frameworks actually enters your work, its *manual* becomes
the import candidate — the listicle is at best one map card. For the
chapter: **Shift+F8** (or `File : Import : Files and folders` for the PDF),
then **Alt+P** → 30. Not 1% — most material isn't top-priority.

*What to notice: a verdict and a reason, not a summary of either text. One
import was refused; that refusal is the product working.*

---

## Scene 2 — Mid-reading: "what do I extract?"

**User:** Reading the chapter in SuperMemo, this paragraph — what's worth
extracting?

> TCP's congestion window starts small and doubles every RTT — so-called
> slow start, a name coined by Van Jacobson in 1988 — until it crosses
> ssthresh, after which growth becomes linear (congestion avoidance).

**Agent:** Two extracts, one skip:

1. Select and **Alt+X**: *"TCP slow start: the congestion window doubles
   every RTT until it crosses ssthresh"* — core mechanism.
2. Select and **Alt+X**: *"TCP: above ssthresh, congestion-window growth
   switches from exponential to linear (congestion avoidance)"* — the
   discrimination you'll actually need when reading packet traces.
3. Skip the Van Jacobson attribution — trivia (DISCARD).

Principle behind both: **extracts must survive alone** — I dropped
"so-called" and resolved the sentence so each fragment makes sense years
from now, shuffled among thousands.

*What to notice: exact fragment wordings to select, a named skip, one
principle taught. The agent never asked for the whole chapter.*

---

## Scene 3 — Mid-reading: "how do I cloze this?"

**User:** That first extract came up for review. Cloze what?

**Agent:** Depends on which retrieval you'll need:

- Weak on *where slow start ends*? Select **ssthresh** → **Alt+Z**:
  `…doubles every RTT until it crosses [...]` / `ssthresh`
- Weak on *how fast it grows*? Select **doubles** → **Alt+Z**:
  `…the congestion window [...] every RTT…` / `doubles`

Make **one now** — official habit is one cloze per pass, more at the next
review. If you make the ssthresh cloze, watch for interference with any
future "congestion avoidance threshold" card; a contrast card fixes that if
it appears.

*What to notice: the user chooses; the agent explains what each choice
trains and stops at one cloze (incremental cloze generation).*

---

## Scene 4 — Two weeks later: a reformulation round-trip

**User:** This cloze has failed 4 times:

> q: DNS: the [...] record at the zone apex holds the primary nameserver,
> the admin mailbox, the serial number and the timers used in zone transfers
> a: SOA

I keep answering NS.

**Agent:** Diagnosis: interference with NS (principle 6) plus a bloated
question (principle 2) — it teaches five facts but tests one. Old → new:

```
q: DNS: the [...] record stores a zone's serial number and transfer timers
a: SOA

q: DNS: SOA vs NS — which one delegates the zone to nameservers?
a: NS (SOA only describes the zone)
```

Paste the first card into the existing element (**E** to edit) and press
**Ctrl+M** to restart its schedule — after 4 lapses the old history is
noise. Add the discrimination card with **Alt+A** at an honest priority
(~40%).

*What to notice: the item came back as pasted text with a one-line symptom;
the fix came back as an old → new pair to edit **in place** (history
preserved, no duplicate), plus one new card that attacks the actual
confusion. For dozens of failing items at once, the batch route is:
**Shift+F3** → browser menu `Export : Q&A text file` → hand the file over →
import the returned rewrites-only file → dismiss the originals in that
browser.*

---

## Scene 5 — Coach question, mid-review

**User:** Honestly, what's the difference between postponing and
rescheduling? I keep doing Ctrl+J on things I can't face.

**Agent:** **Ctrl+J** (reschedule) hand-picks a date — you're overriding
the algorithm one element at a time, and habitual use means your priorities
are dishonest. Postpone (`Learn : Postpone`) shifts *low-priority overflow*
wholesale and keeps the queue sane; with `Learn : Postpone : Auto-postpone`
on, it happens by itself each morning. Better move for "can't face it":
lower the element's priority (**Alt+P**, pick a bigger number) and let
auto-sort/auto-postpone do the sorting. Source: reference.md § Priorities &
overload; deeper rationale in
`docs/wiki/rendered/ns-0-main/p5--Priority_queue.html` if you want it.

*What to notice: direct answer, the harmful pattern named gently, exact
paths, a doc anchor — and no essay.*

---

## Scene 6 — Batch card production (an Anki user)

**User:** I use Anki, not SuperMemo. Turn these study notes into cards:
"DNS TTL caps how long resolvers cache a record. `dig +short` prints
terse output. An A record maps a hostname to an IPv4 address."

**Agent:** Gate first — three units, two survive:

| Unit | Verdict | Why |
|---|---|---|
| TTL caps resolver caching | MEMORIZE | judgment anchor for stale-DNS incidents |
| A record → IPv4 | MEMORIZE | core vocabulary |
| `dig +short` | OFFLOAD | one-second lookup, verifiable on the spot — no card |

Import file (`File > Import` in Anki):

```
#separator:tab
#html:true
#notetype:Basic
DNS: what does a record's TTL limit?	how long resolvers may cache it
DNS: which record type maps a hostname to an IPv4 address?	A record
```

Workload: 2 cards, negligible. Principle applied: **minimum information**
— "caps how long resolvers cache a record" became a six-word answer.
Networking is one of your core domains, so one note, once: wording cards
yourself deepens retention — happy to switch to suggest-only mode
whenever you like.

*What to notice: the gate ran before any card existed, the skip was
named with its reason, the output matched the user's tool, and the
self-formulation nudge is one line, not a lecture.*
