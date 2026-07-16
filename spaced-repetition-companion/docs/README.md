# Bundled official documentation

Offline primary-source material for answering SuperMemo questions without
depending on live access to help.supermemo.org. The site normally presents a
Cloudflare JavaScript challenge to programmatic clients, so this skill
ships a revision-pinned mirror.

## What is here

- **`wiki/source/`** — the exact current-revision wikitext exported by
  MediaWiki's `Special:Export`: 570 source pages in total.
  - Main namespace: 209 pages
  - Glossary namespace: 154 pages
  - File metadata: 203 pages
  - Templates: 4 pages
- **`wiki/rendered/`** — 363 readable documentation pages (Main + Glossary).
  Non-redirect pages contain the official MediaWiki parser output for the
  revision recorded in the manifest; redirects are small local pages pointing
  at their targets. This layer preserves transclusion expansion — important for
  the large `Incremental learning` master document.
- **`wiki/manifest.jsonl`** — one record per page: title, namespace, safe local
  paths, canonical/edit/oldid URLs, page and revision IDs, revision timestamp,
  redirect target, MediaWiki SHA-1, and local SHA-256.
- **`wiki/snapshot.json`** — snapshot time, coverage, counts, site version, and
  hashes for the export and manifest.
- **`wiki/_index.html`** — a searchable offline index linking both layers.
- **`articles/20rules.htm`** — Piotr Wozniak, *Effective learning: Twenty rules
  of formulating knowledge*.

The two Wiki layers have different jobs. `source/` is the provenance layer and
matches what **View source** exposes; it is never decorated with local headers.
`rendered/` is the reading layer. Raw wikitext alone is not enough for long
pages such as `Incremental learning`, because that source transcludes multiple
other pages. Rendered files add only a local wrapper and rewritten links around
the official parser output.

## Snapshot scope and provenance

- Fetched **2026-07-10 17:26:44 UTC** from
  [SuperMemo Help](https://help.supermemo.org) using MediaWiki
  `Special:AllPages` and `Special:Export` in a normal browser session.
- The mirror contains every current page enumerated in the two documentation
  namespaces used by the site (Main and Glossary), plus all File-description and
  Template pages needed as source dependencies.
- Revision history, Talk/User/MediaWiki administration namespaces, and media
  binaries are intentionally excluded. Images in rendered pages use their
  official remote URLs and therefore require a network connection.
- Every raw file's byte count and MediaWiki SHA-1 were checked against the XML
  export. Every non-redirect rendered page was checked against the same
  revision ID. The generated local links are also validated.

All mirrored content remains © SuperMemo World / its respective authors. This
project is not affiliated with SuperMemo World. This skill's MIT license
does **not** cover `docs/`.

## Lookup

Start with the manifest, because page-ID filenames deliberately avoid Windows
case and punctuation collisions:

```sh
rg -i 'priority queue' docs/wiki/manifest.jsonl
rg -l -i 'auto-postpone' docs/wiki/source docs/wiki/rendered
```

For readable expanded text, open the record's `rendered_path`; for exact
wording, templates, comments, or link targets, inspect `source_path`. Cite the
record's `canonical_url` and, when version precision matters, its `oldid_url`.

The expanded master document is
`wiki/rendered/ns-0-main/p470--Incremental_learning.html`; its exact source is
`wiki/source/ns-0-main/p470--Incremental_learning.wiki`.

## Refreshing the mirror

1. In a browser session that has passed the site's normal Cloudflare check,
   enumerate Main, Glossary, File, and Template with `Special:AllPages`.
2. Export those titles from `Special:Export`, selecting current revisions and
   templates.
3. Capture the rendered parser output for each non-redirect Main/Glossary page
   and record `pageid`, `revid`, `html`, `html_length`, `html_sha256`, and
   `capture_complete: true` as JSONL. Long HTML values must be read in chunks
   rather than through a size-limited single return value.
4. Rebuild and validate:

   ```sh
   python scripts/import_supermemo_help.py SuperMemo-Help.xml \
     --rendered-jsonl rendered.jsonl \
     --output docs/wiki
   ```

The importer refuses missing namespaces, page/revision mismatches, raw hash
failures, browser-truncated long pages, case-insensitive path collisions, and
broken local links.
