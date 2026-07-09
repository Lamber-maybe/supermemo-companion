# Bundled official documentation

Verbatim offline copies of the official SuperMemo documentation, so any
agent working in this repository can answer from primary sources
**without network access** — help.supermemo.org sits behind a
Cloudflare challenge that blocks most programmatic fetches.

What's here:

- **`wiki/`** — the help.supermemo.org wiki crawled as flat HTML (~210
  pages), one page per file, named by page title. The first body line
  of each page carries its canonical URL. The centerpiece is
  `wiki/Incremental_learning.html`, the ~91,000-word master document of
  the method (the wiki title `Incremental_learning_(Full)` is a
  redirect to this same page — it is the full text). Its distilled
  companion lives at `skills/supermemo-coach/incremental-learning.md`.
- **`wiki-zh/`** — Chinese translations under the same filenames;
  roughly two-thirds substantially translated. Verify facts against the
  English page when precision matters.
- **`articles/20rules.htm`** — Piotr Wozniak, *Effective learning:
  Twenty rules of formulating knowledge*
  (https://super-memory.com/articles/20rules.htm), the source of the
  reading-advisor skill's formulation principles.

Notes:

- **Attribution.** All content is © SuperMemo World / its authors; this
  project is not affiliated with SuperMemo World. The copies are
  verbatim and included solely as offline reference material for study.
  The repository's MIT license does not cover this folder.
- **Images** are referenced from the original sites and appear only
  when online; the text is complete offline.
- **Provenance.** Wiki crawled June 2026; the twenty-rules article
  fetched July 2026. To refresh, re-crawl and replace the files.
- **Lookup.** Find pages by filename first
  (`ls docs/wiki | grep -i <keyword>`), then by content
  (`grep -li <keyword> docs/wiki/*.html`) — see the coach skill's
  source-of-truth ladder for how these copies rank against a personal
  mirror and the live site.
