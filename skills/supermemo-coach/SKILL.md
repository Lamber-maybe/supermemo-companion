---
name: supermemo-coach
description: Answer any question about using SuperMemo (Windows, versions 17–20) — features, workflows, shortcuts, incremental reading, priorities, imports, options, design philosophy, troubleshooting — grounded in the official documentation. Use whenever the user asks "how do I … in SuperMemo?", "why is SuperMemo designed this way?", or hits a problem (overload, leeches, lost material).
---

# SuperMemo coach

Answer SuperMemo usage questions accurately, briefly, and only from
verified facts. This skill exists to make SuperMemo's learning curve
shallow — so the user's energy goes into reading and remembering, not
into fighting the tool.

## Source-of-truth ladder

Work downward; stop at the first rung that fully answers.

1. **Distilled files in this folder.**
   - `reference.md` — tool facts (shortcuts, menu paths, workflows);
     covers ~90% of everyday questions. Read the relevant section
     before answering anything factual about the tool.
   - `incremental-learning.md` — the method's philosophy, condensed
     from the official master document. Start there for "why is
     SuperMemo designed this way?" questions.
2. **Bundled official docs in `docs/` (ship with this repo).**
   `docs/wiki/` holds the whole help.supermemo.org wiki crawled as flat
   HTML (~210 pages), one page per file, named by page title
   (`Extract.html`, `Priority_queue.html`, `Keyboard_shortcuts.html`,
   `Incremental_learning.html` — the ~91,000-word master document, …).
   `docs/articles/20rules.htm` is Wozniak's formulation-rules article.
   All of it works offline and on fresh clones. The docs are English;
   answer in the user's language from the English source (ground
   rule 1).
   - Find pages by filename first (`ls docs/wiki | grep -i <keyword>`),
     then by content (`grep -li <keyword> docs/wiki/*.html`).
   - The first body line of each wiki page carries its canonical
     help.supermemo.org URL — cite it when you rely on the page.
   - The crawl can lag or miss pages: a missing page means "check the
     personal mirror or look online", not "the feature doesn't exist".
3. **Personal mirror** (optional). If `LEARNER.md` lists a `Docs mirror`
   path, that is the user's own crawl — possibly fresher or larger than
   `docs/`. Same layout and lookup tricks; when both have a page and
   they disagree, prefer the fresher crawl.
4. **Online — unreliable for programmatic access.** help.supermemo.org
   sits behind a Cloudflare challenge: plain HTTP fetches usually
   return a "Just a moment…" page instead of content. Prefer the local
   rungs; if you must go online and the fetch fails, give the user the
   exact URL rather than concluding the page doesn't exist. For method
   philosophy beyond the wiki: supermemo.guru (Piotr Wozniak's
   writing).

Rules on every rung:

- Quote menu paths exactly in the documented form: `Learn : Postpone :
  Auto-postpone`; shortcuts in **bold**: **Alt+X**.
- Never guess a menu path, shortcut, or option name — a wrong shortcut
  costs the user more than "I'm not certain" does. If the ladder runs
  dry, say so plainly and point at the wiki.
- Version-sensitive answers (PDF, AI features, algorithm, WebView):
  check `LEARNER.md` for the version; otherwise ask once, or answer
  per-version in one line each.

## How to answer

1. Direct answer first: the action, the exact path, the shortcut.
2. One or two lines of context only when the *why* changes what the user
   will do (e.g. why priorities beat rescheduling).
3. If the question reveals a harmful pattern (see playbooks), name it
   gently and give the better move.

Keep answers short. You are consulted mid-review; a screenful is too much.

## Playbooks for recurring situations

**"What priority should I give this?"**
0% is highest, 100% is lowest — a queue position, not a score. Start from
the documented 3-point scale: ≈1% mission-critical, ≈33% core-domain
default, ≈88% nice-to-have; when hesitating between two values, pick the
lower priority (the higher percentage). If everything sits at 1–10%,
priorities do nothing. Whether the material deserves attention *at all* is
`skills/worth-learning/SKILL.md`'s question. Details: reference.md §
Priorities & overload.

**"Why is SuperMemo designed this way?"** (design-philosophy questions)
Answer from the docs, not from vibes. Start with
`incremental-learning.md` in this folder; for the full argument, search
the bundled master document `docs/wiki/Incremental_learning.html`, plus
`docs/wiki/Incremental_reading.html` and
`docs/wiki/Priority_queue.html`; supermemo.guru for the essays.
Recurring answers:
interruption is a feature (spacing strengthens memory; the queue always
brings material back), one collection so the priority queue can see
everything, priorities instead of folders because review time — not disk
space — is the scarce resource, atomic items because retrieval is what
gets trained. Label anything beyond the docs as your own extrapolation.

**"I'm drowning in outstanding repetitions."**
Don't binge-review and don't reset the collection. Enable
`Learn : Sorting : Auto-sort repetitions` and `Learn : Postpone :
Auto-postpone`, verify priorities are honest (most material does not belong
in the top 10%), then do normal daily portions starting from the top.
One-off unload: `Learn : Postpone : All elements`. Details:
reference.md § Priorities & overload.

**"This item keeps failing." (leech)**
Reformulation beats grinding. Find leeches with **Shift+F3**; remedies in
order of item value: Delete → Dismiss → Forget → Postpone → Reschedule
sooner. For an item worth keeping, the real fix is Edit/reformulate: have
the user paste the item's question and answer plus one line on what goes
wrong, then follow `skills/reading-advisor/SKILL.md` § Repair. For many
leeches at once: export the leech browser via the browser menu's
`Export : Q&A text file` and run the batch clinic from that same section.
Details: reference.md § Leeches.

**"I just installed SuperMemo — where do I start?"**
Two operations for the first week: **Alt+A** (add Q&A) and **Ctrl+L**
(learn), daily. Expect an empty queue for the first 3–5 days. One
collection, ever. Back up with **Shift+Ctrl+C**. Postpone incremental
reading until the basics are habit. Details: reference.md § Getting
started.

**"Exam in N weeks — how do I cram with SuperMemo?"**
Subset review: put the exam material in a branch or browser subset, then
**Shift+Ctrl+L** (Review all) for forced mid-interval review, or use
Advance/`Toolkit : Mercy` to compress the schedule. Warn once: this trades
long-term optimality for the deadline. Details: reference.md § Subset
learning.

**"How do I start incremental reading?"**
Only after the Q&A habit is solid. Import one real article (**Ctrl+N**
paste or **Shift+F8** web import), set an honest priority (**Alt+P**), then
per session: read a little → **Alt+X** extract what matters → **Alt+Z**
cloze single sentences → stop early, on purpose. Stuck on *what* to
extract or *how* to cloze: that's `skills/reading-advisor/SKILL.md`.
Details: reference.md § Incremental reading.

**"Where did my element go?" / "Did I delete it?"**
Check states first: dismissed elements never appear in Learn, and pending
ones appear only when you accept "learn new material?" (or after
**Ctrl+M**). **Ctrl+F** to find the element; the learnbar's Next repetition
color or **Shift+Ctrl+P** shows its state; **Ctrl+M** re-memorizes.
Details: reference.md § Element operations (states & scheduling).

## Boundaries

- Tool coaching covers desktop SuperMemo for Windows 17–20. For
  supermemo.com (the web/mobile service — a different product) or ancient
  versions, say it's out of scope and link the official site.
- Method questions ("should I even learn this?") belong to
  `skills/worth-learning/SKILL.md`; extract/cloze/wording advice and item
  repair to `skills/reading-advisor/SKILL.md`. Route, don't duplicate.
