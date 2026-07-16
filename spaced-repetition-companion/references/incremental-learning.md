# Incremental learning, distilled

The method's philosophy, condensed in this project's own words from the
official master document — the ~91,000-word wiki page that explains why
SuperMemo works the way it does. Distilled July 2026 and checked against
the revision-pinned July 2026 mirror.

- **Full expanded original, bundled in this skill:**
  `docs/wiki/rendered/ns-0-main/p470--Incremental_learning.html`.
- **Exact View Source wikitext:**
  `docs/wiki/source/ns-0-main/p470--Incremental_learning.wiki` (the raw
  file contains transclusions; use the rendered file for continuous
  reading).
- **Canonical URL:** https://help.supermemo.org/wiki/Incremental_learning
  (the wiki title `Incremental_learning_(Full)` redirects to the same
  page — this *is* the full text).
- Each section below names the original headings it distills. To verify
  a claim or go deeper, search that heading text inside the rendered HTML
  and read from there. Quote the original when the exact wording
  matters; label anything beyond it as your own extrapolation.

## The core claim

*(Original: "What is incremental learning?", "General outline of
incremental learning", "Components of incremental learning")*

Incremental learning is consuming many sources in parallel — articles,
video, audio, mail, notes — in small portions, in priority order, with
everything worth keeping converted into spaced-repetition review. The
promise: roughly **95% lifetime retention of your top-priority
material** at a marginal time cost (the docs' example: an educated
native speaker's vocabulary maintained for ~20 minutes a day in the
first years, mere minutes later).

The learner stays **in the driving seat**: they decide what enters the
process, when, in what detail, at what priority, and at what target
retention. All areas of knowledge grow in parallel, in proportion to
interest and importance — deliberately the opposite of school's
few-subjects-per-semester model, where mastering one area means
forgetting another. Incremental reading is the oldest and most mature
component; the others (video, audio, mail, creative elaboration) apply
the same loop to other streams.

## Interruption is a feature

*(Original: "The value of interruption in learning", "Interruption is
not a problem")*

The method interrupts constantly — mid-article, many times a day — and
the docs claim three advantages and, literally, no disadvantages
(interruption is always optional):

1. **Memory** — spaced encounters beat massed reading (spacing effect).
2. **Priorities** — you can only rank what you have previewed;
   interleaved reading *is* continuous preview, so prioritization
   happens on the go.
3. **Attention** — when focus flags, changing the subject is the
   cheapest remedy short of stopping.

You never owe an article a finish. A well-written text delivers value
sentence by sentence (the docs walk through reading a Nasser biography
one self-contained fact at a time, deferring the rest for months —
possibly forever, via dismiss or delete). Texts that resist increments —
code, proofs, tightly-argued papers — are read whole when they come up;
what you then process incrementally are **your own verbalized
conclusions**, with the source kept as reference.

## Knowledge evolves; it is not transcribed

*(Original: "Evolution of knowledge in incremental reading")*

Three principles govern what happens to material inside the process:

- **Decreasing complexity** — articles become paragraphs, paragraphs
  become self-contained sentences, sentences get trimmed to maximize
  the information-to-wording ratio.
- **Active recall** — everything that must be *remembered* ends up as a
  test: cloze deletion, question-and-answer, recognition. Passive
  re-reading is only the supply chain.
- **Incrementalism** — the conversion happens gradually, in proportion
  to available time and the material's priority, as memory traces
  strengthen.

Extract (**Alt+X**) then cloze (**Alt+Z**) is the assembly line that
implements the first two principles; the review queue implements the
third.

## Topics carry reading; items carry memory

*(Original: "Topics vs. Items")*

- **Topics** are things you want to *read* — passive review only; they
  never test you. Short topics exist to be milked for clozes. Once
  converted, the user dismisses them (or marks them done) — never
  automatic.
- **Items** are things you want to *remember* — they actively test
  recall. Only items train memory.
- **Concepts** (SuperMemo 17+) link related elements into a concept
  map, the skeleton for spreading activation and neural review
  (`Learn : Go neural`).
- **Tasks** are jobs ranked by value/time.

## Overload is the normal state — and it is managed, not eliminated

*(Original: "Skill 5: Handling large volumes of knowledge", "Reading
overload", "Auto-sort and auto-postpone", "Priorities", "Complexity of
incremental learning")*

Far more passes the worth-learning bar than anyone can review; the docs
call this *optimistic* — it means selection, not capacity, is where the
gains are. The tools:

- **The priority queue.** Every element gets a priority from 0% (most
  important) to 100%. The famous "why is SuperMemo upside down?"
  complaint is answered in the docs: professionals type `1`, `2`, `3`
  for their top material daily; the scale serves heavy users.
- **Honest consequences.** Low-priority material *should* receive less
  meticulous treatment and carry a higher risk of forgetting — that is
  the design working, not failing.
- **Auto-sort + auto-postpone** (`Learn : Sorting : Auto-sort
  repetitions`, `Learn : Postpone : Auto-postpone`). Each morning the
  outstanding queue is sorted by priority and its low-priority excess
  postponed; top-priority elements always stay in the queue, and
  today's material is never touched.
- **Scale limits.** Few users sustain more than ~200 item repetitions a
  day; a one-off backlog is unloaded with `Postpone` (delay all) or
  `Toolkit : Mercy` (spread over time).

## Why SuperMemo feels hard — from the official docs themselves

*(Original: "Complexity of incremental learning")*

The docs are blunt: incremental learning "requires skills that take
months to develop" and personal strategies "that may mature over
years"; SuperMemo is "optimized to make a life of a pro easy" and never
trades learning efficiency for sleekness, so beginners find it hard.
The steep learning curve is acknowledged, deliberate, and worth
climbing. That is precisely the gap this project fills: flatten the
*tool's* curve while leaving the method — including the effort of
reading and thinking — intact.

## What the method promises

*(Original: "Advantages of incremental reading" — 17 subsections,
condensed)*

- **Massive, parallel learning** with no limit on concurrent subjects,
  and **uniform progress** across all of them.
- **Lifetime 95% retention**, because review never ends and never
  overwhelms.
- **Comprehension** — knowledge assembles like a jigsaw: details wait
  in the queue until their foundations exist.
- **Creativity** — unpredictable interleaving of subjects associates
  remote ideas ("brainstorming with yourself").
- **Consistency** — contradictions between sources surface and must be
  resolved; the process "does not tolerate information discrepancy".
- **Stress-free attention** — nothing can be lost, so the mind stops
  guarding it; when a text bores you, the next element is one keypress
  away.
- **Speed** — skim the unimportant fast and let comprehension arrive
  late on purpose; cloze deletion is the fastest route from text to
  item.
- **A by-product archive** — a searchable personal knowledge base you
  consult before Google.
- **Fun** — listed in the official docs as an advantage in its own
  right; this project treats it as a boundary (the reading loop belongs
  to the user).

## The myths, answered

*(Original: "Incremental learning myths" — 13 subsections)*

Written in 2013, these already answer 2026's AI-era doubts: myths 7 and
8 are this project's core principle in earlier clothing.

| # | Myth | The documented answer |
|---|---|---|
| 1 | Successful people manage without SuperMemo | So did Newton without computers; as knowledge compounds in value, stable breadth becomes a competitive advantage |
| 2 | Natural forgetting already keeps what matters | Forgetting evolved blind to your goals; it spares what is *used often*, not what you *decide* matters |
| 3 | Memory cannot be improved by training | At the synapse, true; in practice, formulation and review strategy change everything — and both are trainable |
| 4 | Repetitions cost too much time | Three well-chosen items a day beat a hundred crammed facts; reserve high retention for material that deserves it |
| 5 | The repetition load grows unmanageable | Simulations and measurements show constant daily time sustains a steady inflow — per-item cost falls as intervals grow |
| 6 | Everyone forgets at the same rate | Raw forgetting is similar; *representation* makes items cheap or expensive, which is where fast learners win |
| 7 | Hypertext can substitute for memory | Thinking is associative and runs only on knowledge resident in the head; you cannot reason with what you would have to look up |
| 8 | An index to sources is enough | The index itself decays without review, and creative output depends on knowledge held, not knowledge locatable |
| 9 | You spend mere seconds per topic | Time follows need: seconds for low-priority material, a full day before an exam or deep in research |
| 10 | Memorization is not needed | Followed to its conclusion, nobody would learn languages (dictionaries exist) or anatomy (references exist); comprehension is built from remembered parts |
| 11 | High retention means slow learning | Retention is a dial, not a tax: run high-retention-low-volume on top priorities and fast low-retention skimming on the rest, simultaneously |
| 12 | We are good at remembering important things | Brains adapted for survival 200,000 years ago, not abstract knowledge; felt importance does not create durability |
| 13 | We remember what we use | Frequently used memories still lapse suddenly (the forgotten-PIN effect) — frequency of use is not spaced review |

## Beyond reading

*(Original: "Incremental video", "Incremental mail processing",
"Incremental problem solving", "Incremental writing", "Incremental
brainstorming", "Neural creativity", "History of incremental learning")*

The same loop — chop, prioritize, interleave, remember — applies to any
stream: video and audio (parallel processing of recordings), mail
(overload triage that feeds learning), problem solving (for problems
too big for working memory), writing (the master document itself was
written incrementally in SuperMemo), brainstorming, and neural review
(spreading activation over the concept network). The name "incremental
reading" first appeared in SuperMemo 2000; the components matured over
the following two decades.

## Where each question lands in the original

| Question is about … | Search these headings in `docs/wiki/rendered/ns-0-main/p470--Incremental_learning.html` |
|---|---|
| The method in one chapter | *What is incremental learning?* |
| Import / read / extract / cloze / review mechanics | *Five basic skills of incremental reading* (Skills 1–5) |
| Extract and cloze technique in depth | *Skill 3: Extracting fragments, questions and answers*, *Generating clozes* |
| Topic vs item semantics | *Topics vs. Items* |
| Priorities, overload, auto-sort/postpone | *Skill 5*, *Reading overload*, *Auto-sort and auto-postpone* |
| Design rationale and benefits | *Advantages of incremental reading* |
| Skeptical "is this worth it?" questions | *Incremental learning myths* |
| Video, mail, writing, creativity | Their like-named chapters |
| Hints and micro-techniques | *Hints and tips* |
