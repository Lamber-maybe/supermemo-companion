# SuperMemo distilled reference

Facts distilled from the official documentation (help.supermemo.org) for
desktop **SuperMemo for Windows, versions 17–20**. Menu paths are written
`Menu : Submenu : Option`. Where versions differ it is noted. Anything not
covered here should be answered via the coach skill's source-of-truth
ladder — the philosophy digest (`incremental-learning.md`), the full
revision-pinned official mirror bundled in `docs/wiki/` (expanded HTML
plus exact source and a manifest), a demonstrably fresher personal mirror
if one is configured, then https://help.supermemo.org — never from memory.

## Getting started (the official "ABC")

- Two operations carry 90% of the value: **Add new** (**Alt+A**) — type the
  question, **Esc**, type the answer, **Esc** — and **Learn** (**Ctrl+L**),
  done **daily** until "Nothing more to learn".
- The first repetitions come due only **3–5 days after adding** material; an
  empty queue in the first days is normal.
- The docs recommend staying in this mode for a week or more, and warn that
  rushing into advanced features (especially incremental reading) "can
  quickly lead to confusion and disillusionment". Master each step before
  the next.
- **One collection.** "Multiple collections make it easier for you to fail
  your own learning plans." Merge strays via `File : Merge collection`.
- **UI levels** (`File : Level`): Beginner (default; add + learn only) →
  Basic (learnbar, extracts/clozes) → Middle (options, Mercy, collection
  management) → Professional (everything). **Ctrl+Alt+F12** moves one level
  up. Shortcuts usually work even when the menu item is hidden at a lower
  level.

## Core concepts

- **Collection** — the whole body of material; one folder plus a `.kno`
  file. **Element** — one screen-page of knowledge; four types:
  - **Item** — stimulus→response pair (Q&A, cloze, occasionally multiple
    choice). Actively recalled and graded; intervals set by the algorithm.
    A typical item is repeated on the order of 7–12 times over a lifetime.
  - **Topic** — passive reading material (articles, extracts). Reviewed
    "as is", no grading of recall; intervals grow by a simple multiplier
    (the topic's **A-Factor**), fully under user control.
  - **Concept** — a hub node marking an important idea; roots a *concept
    group*; behaves like a topic if reviewed at all.
  - **Task** — a to-do entry on a tasklist; enters review only if
    explicitly introduced.
- **Element states**: **memorized** (in the learning process) · **pending**
  (waiting in the pending queue to be memorized) · **dismissed** (out of
  learning, kept in the collection for reference; priority ignored).
- **Component** — a container inside an element (HTML text, image, sound,
  video, PDF/WebView, etc.).
- **A-Factor** — per-element growth factor for intervals (items: reflects
  difficulty, min 1.2; topics: next interval = old interval × A-Factor).
  Algorithms SM-17+ no longer use item A-Factors for scheduling.
- **Retrievability / Stability** — the two variables of the memory model:
  probability of recall now, and how slowly it decays.

## The daily learning cycle

Press **Learn** (**Ctrl+L**). A full day has up to three stages:

1. **Repetitions** of outstanding material (elements whose next date ≤
   today), by default sorted by priority.
2. **Memorizing** new material — SuperMemo asks "Do you want to learn new
   material?" and pulls from the **pending queue** in order.
3. **Final drill** — same-day re-review of items that failed or scored
   poorly. Controlled by `Toolkit : Options : Learning : Skip final drill`;
   the docs consider it optional and advise overloaded users to skip it
   (useful mainly when cramming for a deadline).

**Item repetition**: read the question → recall → **Show answer** → grade.

**Grades** (Pass and above = remembering; Fail and below = forgetting —
failing grades reset the item to short intervals and count a **lapse**):

| Key | Grade | Meaning |
|---|---|---|
| 5 | Great | perfect response |
| 4 | Good | correct with hesitation |
| 3 | Pass | recalled with difficulty, perhaps slightly wrong |
| 2 | Fail | wrong, but "I knew it!" |
| 1 | Bad | wrong; the answer merely looks familiar |
| 0 | Null | complete blackout (keyboard only, rarely needed) |

Grades display as emoji from SM18 onward; restore text labels by unchecking
Grade icons in `Toolkit : Options : SuperMemo`. Response time is ignored.
**Alt+G** cancels a mis-entered grade.

**Forgetting index (FI)** — the target probability of forgetting an element
at repetition time. Default **10%**; sensible range **3%** (much slower
learning) to **20%** (faster, lower retention; beyond 20% is pointless).
Set globally in `Toolkit : Options : Learning`; per element via Element
parameters (**Shift+Ctrl+P**) or the priority dialog (**Alt+P**).

## Adding material

| Route | How | Creates |
|---|---|---|
| Add new item | **Alt+A** (`Edit : Add a new item`) | item, actively learned |
| Paste an article | **Ctrl+N** (`Edit : Add a new article`) — clipboard text | topic |
| Quick note | **Alt+N** (`Edit : Add a note`) | topic |
| Web import | **Shift+F8** (`Edit : Web import`) — imports open browser tabs (Edge/Chrome in SM19+) | topics |
| Wikipedia / YouTube | **Shift+Ctrl+W** / **Shift+Ctrl+Y** | filtered topic / video element |
| Q&A text file | `File : Import : Q&A text` | items (see spec below) |
| Files & folders | `File : Import : Files and folders` — a whole folder tree | one element per file |
| New task | **Alt+F1** | task on the current tasklist |

**Important routing rule:** `Add new`, `Ctrl+N`, `Alt+N` and imports land at
the **hook node of the current concept group** (the Concept box on the
navigation bar) — *not* at the branch selected in the Contents window. To
add children at a tree selection, use the `Add`/`Insert` buttons at the
bottom of the Contents window.

**Q&A import file spec** (`File : Import : Q&A text`):

```
q: single-line question text
a: single-line answer text

q: next question…
a: next answer…
```

Plain text, UTF-8, `.txt` extension. One blank line between items. Keep
each `q:`/`a:` on one physical line — the only form the official examples
show (use `<br>` inside the line for visual breaks). Simple inline HTML tags are allowed; never wrap the `q:`/`a:` tags
in HTML, never add angle-bracket comments, never save as RTF/DOC/HTML.
Multiple-choice: append wrong answers as `a1:`, `a2:`, `a3:` lines.
`File : Export : Q&A text file` writes the same format (first Q and A
component of each element).

After a Q&A import, verify element state: if imported items are **pending**,
either let the daily "learn new material?" stage introduce them gradually
(better for workload), or select them in a browser and Remember (**Ctrl+M**).

**Web import modes** (per row in the import dialog): HTML (**Ctrl+H**,
default, filtered page) · Parsed (**Ctrl+P**, strips ads/navigation) ·
Plain text (**Ctrl+T**) · Link only (**Ctrl+L**) · selection / picture /
YouTube / screenshot variants. When unsure, the docs suggest importing more
than one variant and deleting the worse.

**PDF**: SM19 and earlier import PDFs as **plain text only**. SM20 adds
native PDF via the WebView component — viewer + PDF editor with
highlights, read-points, `Extract → SM`, picture extracts, auto-saved scroll
position; import via web import (Article WV template), `File : Import :
Files and folders` (bulk), or the component's `Import file`.

## Incremental reading

The loop: **import → prioritize → read a little → extract → cloze → let the
queue interleave everything**.

1. Import an article (routes above). Set priority **Alt+P**; optionally
   first interval **Ctrl+J**. Same-day reading: **Shift+Ctrl+J** (Later
   today) or browser `Learning : Add to outstanding`.
2. When the topic comes up, read from the top or from the **read-point**
   (set **Ctrl+F7**, jump **Alt+F7**, clear **Shift+Ctrl+F7**). Messy HTML:
   **F6** filters formatting.
3. **Extract** (select text → **Alt+X**, `Reading : Remember extract`):
   creates a **child topic** that inherits the parent's references and
   enters the queue at a priority derived from the parent. Extract
   important fragments; make them self-contained (fix pronouns).
4. **Cloze** (select a keyword → **Alt+Z**, `Reading : Remember cloze`):
   creates a **child item** — question = the sentence with `[...]` over the
   keyword, answer = the keyword. Cloze from **one-sentence extracts**;
   simplify the sentence first; avoid "monster clozes". The new item is not
   shown (the keyword just changes color) — press **Alt+Left** (Back) to
   edit it.
5. Housekeeping: **Alt+\\** deletes text before the cursor (recoverable
   from the collection's temp folder if misapplied);
   `Reading : Ignore` (**Shift+Ctrl+I**) marks fragments to skip.
6. Finishing an article: **Done!** (**Shift+Ctrl+Enter**) — dismisses/
   deletes the exhausted article but **keeps all extracts and clozes**.
   Splitting long articles: insert a splitline (**Shift+Alt+H**) then use
   `Split article`.

Official rules of thumb:

- Interruption is the norm — stop reading when bored, confused, or out of
  time; the queue brings the rest back.
- Passive extracts stop being reliable around **200–300-day intervals** —
  convert what matters to clozes by then; mission-critical material gets
  clozed immediately.
- Generate clozes incrementally (one now, more at the next review), except
  for top-priority material.
- Keep topic inflow low: review **at least ~4 items per topic**.
- A new cloze deserves high priority for its first review, then an honest
  (lower) priority.
- **References** propagate to all extracts/clozes automatically. Fields
  (`#Title`, `#Author`, `#Date`, `#Source`, `#Link`) are set via the HTML
  component menu `Reference :` submenu (**Alt+Q** select label, **Alt+T**
  title); web imports fill them automatically. The pink area at the bottom
  of an element is the reference — don't type into it.

## Priorities & overload

- Every element has a priority expressed as a percentage: **0% = highest,
  100% = lowest** (it's a position in the priority queue, not a score).
- Set it with **Alt+P** (type a number, Enter). Nudge with
  **Shift+Ctrl+Up/Down** (for topics this also shifts the A-Factor). View
  the whole queue: `View : Priority queue`.
- **Prioritize honestly.** If everything lands at 1–10%, priorities do
  nothing. The docs suggest starting with a 3-point scale (≈1% / 33% /
  88%); when hesitating between two values, pick the lower priority.
- **Auto-sort** (`Learn : Sorting : Auto-sort repetitions`) sorts each
  day's queue by priority. **Auto-postpone** (`Learn : Postpone :
  Auto-postpone`) shifts yesterday's unfinished low-priority overflow
  forward each morning. The docs recommend keeping **both on** — together
  they make overload self-managing.
- Manual unload: `Learn : Postpone : All elements` (or Topics only);
  postpone a whole branch mid-review with `Learning : Postpone branch`.
- **Advance** (subset operation) pulls reviews earlier (e.g. before an
  exam); use cautiously on items — massed review breeds false confidence.
- **Mercy** (`Toolkit : Mercy`, **Shift+Alt+M**) respreads outstanding
  repetitions over a period (after a long break, before a vacation). The
  docs treat Postpone/Auto-postpone as the modern default and Mercy as the
  occasional tool.
- Anchors: few users sustain more than **~200 item repetitions/day**;
  under overload, low-priority material is sacrificed first and only
  top-priority material reaches the requested forgetting index. Inspect
  workload/retention in `Toolkit : Calendar` (**Ctrl+W**) and
  `Toolkit : Statistics : Analysis` (**Shift+Alt+A**).

## Element operations (states & scheduling)

| Operation | How | Effect |
|---|---|---|
| Remember | **Ctrl+M** (`Learning : Remember`) | pending/dismissed → memorized (enters learning) |
| Forget | `Learning : Forget` (element menu) | memorized → end of pending queue |
| Dismiss | **Ctrl+D** | out of learning, kept in collection |
| Done! | **Shift+Ctrl+Enter** | finish a processed article; children survive |
| Delete element | **Shift+Ctrl+Del** (editing mode) / **Del** | removes element (+children if branch) |
| Reschedule | **Ctrl+J** | pick the next review date yourself |
| Later today | **Shift+Ctrl+J** | re-queue for later the same day |
| Execute repetition | **Shift+Ctrl+R** | do a mid-interval repetition now |
| Add to outstanding | subset op: browser/Contents `Learning : Add to outstanding` | force a subset into today's queue (single element: Later today) |
| Edit texts | **E** / **Q** / **A** (presentation mode), **Ctrl+T** next component, **Ctrl+E** edit mode | |
| Swap Q↔A | **Shift+Ctrl+S** | |
| Re-memorize after heavy edits | **Ctrl+M** | restart its learning |

The learnbar's Next repetition field is color-coded by element state
(memorized / pending / dismissed).

## Leeches (items that keep failing)

- A **leech** is an ill-formulated item identified by lapse count (plus
  interval) crossing your criteria; **>20 lapses ⇒ delete-grade** according
  to the docs. All leeches are items; the root cause is almost always
  formulation, not memory.
- Find them: **Shift+F3** (`View : Other : Leeches`) → Element filter
  (Lapses min/max, Interval) → browser → **Ctrl+L** to review just those.
- Handling policy: `Toolkit : Options : Leeches` — None / **Wizard**
  (recommended: shows a Leech Alert with remedies during repetitions) /
  Auto-forget (silently back to pending) / Auto-postpone (reset +
  reschedule far out; can loop forever on true junk).
- Remedy ladder, least valuable item first: **Delete → Dismiss → Forget →
  Postpone → Reschedule sooner**; the best long-term fix for an item worth
  keeping is **Edit/reformulate** (split it, add contrast or mnemonics —
  see the reading-advisor skill's principles).
- For rewriting leeches outside SuperMemo: export the leech browser as Q&A
  text (see § Subset learning & review), re-import the fixes, dismiss the
  originals.

## Organizing material

- **The tree barely matters.** Official position: the knowledge tree "is
  NOT essential for your success" and "does not affect the learning
  process". Mixed-subject review is normal and healthy. Don't gardening-
  procrastinate; spend the effort on priorities and formulation instead.
- **Concept groups** are the practical unit: a branch rooted in a concept,
  with its own default template and hook node for new material. Switch the
  current group in the Concept box on the navigation bar (**C** to search);
  create one with `Edit : Create a concept`, or convert an existing branch
  with **Ctrl+K** in the Contents window.
- A workable pattern from the docs: dump everything into one "to do"-style
  group, and move elements to subject groups only once they're well-formed
  (`Shift+Ctrl+P` → Group, or **Shift+Ctrl+V** to move within the tree;
  drag-and-drop works in Contents).
- **Templates** define element appearance. Apply: **Shift+Ctrl+M**
  (non-destructive; `Detach template` reverts). `Save as default` makes a
  template the default for new elements of that type in the current concept
  group. Mass-apply via `File : Process collection : Template`.
- Keep branches under ~100 children (hard limits exist; SuperMemo auto-
  manages hooks when they overflow).

## Subset learning & review

Run reviews over any subset: a branch (select in Contents), a browser
result (**Ctrl+F** search, **Ctrl+Space** branch contents), or a concept.

- **Learn** (**Ctrl+L**) — outstanding material in the subset only.
- **Review all** (**Shift+Ctrl+L**) — outstanding **plus forced
  mid-interval repetitions** of everything else in the subset.
- **Review topics** — the same, topics only.
- Sort the browser first with **Ctrl+S** (applies the default sorting
  criteria, e.g. before review); randomize with **Shift+Ctrl+F11**.
- A browser subset can be **exported** (browser menu `Export : Q&A text
  file`, or `Document (HTML)` / `All texts`) and **bulk-processed**: the
  subset processing menu (`Process browser>`) includes `Learning :
  Remember / Forget / Dismiss / Undismiss / Done` applied to every element
  in the browser.

Use for pre-exam compression and for resurrecting neglected branches. The
docs warn it is **not** for everyday long-term learning — premature reviews
depart from optimal spacing.

## Maintenance

- **Back up**: `File : Copy collection` (**Shift+Ctrl+C**) to another disk
  every few days; another medium monthly. SM20 supports zipped backups.
- **Repair**: `File : Repair collection` (**Ctrl+F12**) monthly and after
  any crash — but back up first.
- Never store private files inside the collection folder; never rename or
  edit collection files on disk by hand.

## Built-in AI (SuperMemo 20)

- `AI : Explain` explains selected text without leaving SuperMemo;
  `Explain extract` makes an extract plus a short AI explanation;
  `Search : AI` runs AI-answered web search.
- Default model: a bundled free Gemini tier; configurable in
  `supermemo.ini` `[AI]` section — `Provider=gemini` or `Provider=openai`
  with `Model`, `ApiKey`, `BaseURL` (any OpenAI-compatible endpoint:
  OpenRouter, LM Studio, Ollama gateways…). Details may drift between
  releases — verify against the official `Using AI in SuperMemo` page.
- The docs' own framing matches this project: AI removes friction and
  explains; it is "a friendly assistant, not a final authority".

## Version highlights

- **SM18** → baseline for most of this reference; emoji grades.
- **SM19**: web import from Edge/Chrome; PDF-as-plain-text; unlimited
  collections in the chooser; multi-monitor layouts.
- **SM20**: 64-bit, High-DPI, WebView component; **native PDF** editor;
  EPub and EML import; **Algorithm Arena** (SM-2 / SM-15 / SM-19 / SM-20 /
  FSRS selectable); built-in **AI** features; dark mode; zipped backups;
  active final drill. RTF components deprecated. SM20 opens SM19
  collections; the reverse may fail — don't downgrade a collection.

## Curated shortcuts

| Key | Action |
|---|---|
| **Ctrl+L** | Learn (collection, branch, or browser subset) |
| **Alt+A** | Add new item (Q, Esc, A, Esc) |
| **Ctrl+N** | Paste clipboard as new article (topic) |
| **Alt+N** | Add a note (topic) |
| **Shift+F8** | Web import |
| **Shift+Ctrl+W / Shift+Ctrl+Y** | Wikipedia / YouTube import |
| **Alt+X** | Remember extract |
| **Alt+Z** | Remember cloze |
| **Alt+P** | Set priority (0% = highest) |
| **Shift+Ctrl+Up/Down** | Priority up / down |
| **Ctrl+M** | Remember (memorize now) |
| **Ctrl+D** | Dismiss |
| **Shift+Ctrl+Enter** | Done! (finish article, keep children) |
| **Shift+Ctrl+Del** | Delete current element |
| **Ctrl+J** | Reschedule (pick date) |
| **Shift+Ctrl+J** | Later today |
| **Shift+Ctrl+R** | Execute repetition now |
| **Ctrl+F7 / Alt+F7** | Set / go to read-point |
| **F6** | Filter messy HTML |
| **Ctrl+T** | Jump between Q and A when editing |
| **Shift+Ctrl+S** | Swap question ↔ answer |
| **Ctrl+F** | Find elements |
| **Ctrl+S** | Search texts / in browser: apply default sort |
| **Ctrl+Space** | Browse branch contents |
| **Shift+F3** | Find leeches |
| **Alt+G** | Cancel last grade |
| **Ctrl+W** | Calendar (workload) |
| **Shift+Alt+A** | Analysis (statistics) |
| **Shift+Alt+M** | Mercy |
| **Shift+Ctrl+C** | Copy collection (backup) |
| **Ctrl+F12** | Repair collection |
| **Ctrl+Alt+F12** | Next UI level |
| **Esc** | Close dialogs / finish Add new fields |

(Shortcuts are context-sensitive; e.g. **Ctrl+L** and **Ctrl+T** do
different things inside the Web import dialog. When a shortcut misbehaves,
check which window has focus.)

## When to defer to official docs

Answer from the bundled wiki for: registry internals, sleep chart, Plan,
mail/EML workflows, spelling components, scripting/Commander details,
algorithm mathematics, layout management edge cases, localization — and
any behavior that looks version-specific or contradicts this file. Find
the title in `docs/wiki/manifest.jsonl`, read its `rendered_path`, and
check `source_path` plus the recorded revision when exact wording matters.
Send the user to https://help.supermemo.org (and say you're doing so) only
when the bundled page is missing or looks stale. This file wins over an
agent's memory; the official wiki — bundled or online — wins over this
file.
