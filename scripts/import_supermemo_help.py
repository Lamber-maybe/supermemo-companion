#!/usr/bin/env python3
"""Build the bundled SuperMemo Help mirror from a MediaWiki XML export.

The official site is commonly protected by a Cloudflare JavaScript
challenge.  Use MediaWiki's Special:Export in a normal browser to download
the current revisions, then pass that XML file to this script.  A rendered
JSONL capture is required as well so transcluded pages remain readable as a
single expanded document.

The generated mirror deliberately separates:

* byte-for-byte wikitext copied from Special:Export (``source/``),
* revision and provenance data (``manifest.jsonl``), and
* expanded MediaWiki parser output (``rendered/``).
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import posixpath
import re
import shutil
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


SITE_ORIGIN = "https://help.supermemo.org"
DOCUMENT_NAMESPACES = {0, 100}
DEPENDENCY_NAMESPACES = {6, 10}
EXPECTED_NAMESPACES = DOCUMENT_NAMESPACES | DEPENDENCY_NAMESPACES
MINIMUM_PAGE_COUNTS = {0: 209, 6: 203, 10: 4, 100: 154}
REDIRECT_RE = re.compile(
    r"^\s*#redirect\s*:?\s*\[\[\s*([^\]|#]+?)(?:#([^\]|]*))?(?:\|[^\]]*)?\]\]",
    re.IGNORECASE | re.DOTALL,
)
ATTRIBUTE_RE = re.compile(
    r"(?P<name>\b(?:href|src|poster|srcset))=(?P<quote>[\"'])(?P<value>.*?)(?P=quote)",
    re.IGNORECASE | re.DOTALL,
)


@dataclass
class Page:
    title: str
    namespace: int
    pageid: int
    revid: int
    parentid: int | None
    revision_timestamp: str
    contributor: str | None
    comment: str | None
    contentmodel: str
    contentformat: str
    source: str
    source_bytes: int
    source_sha1: str
    source_sha256: str
    redirect_target: str | None
    redirect_fragment: str | None
    source_path: str = ""
    rendered_path: str | None = None
    rendered_kind: str | None = None


def qname(namespace: str, tag: str) -> str:
    return f"{{{namespace}}}{tag}"


def text_of(parent: ET.Element, tag: str, namespace: str, default: str = "") -> str:
    value = parent.findtext(qname(namespace, tag))
    return default if value is None else value


def optional_int(value: str | None) -> int | None:
    return int(value) if value not in (None, "") else None


def base36(number: int) -> str:
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
    if number == 0:
        return "0"
    digits: list[str] = []
    while number:
        number, remainder = divmod(number, 36)
        digits.append(alphabet[remainder])
    return "".join(reversed(digits))


def mediawiki_sha1(data: bytes) -> str:
    # MediaWiki stores SHA-1 as a zero-padded 31-character base-36 value.
    return base36(int(hashlib.sha1(data).hexdigest(), 16)).zfill(31)


def safe_slug(value: str, limit: int = 170) -> str:
    # Keep local paths readable without putting URL escape sequences such as
    # ``%3F`` in the actual filename. Browsers decode those sequences before
    # requesting a local file, which would otherwise create broken links.
    slug = "".join(
        character if character.isalnum() or character in "-_.()" else "_"
        for character in value
    )
    slug = re.sub(r"_+", "_", slug).strip(" ._")[:limit].rstrip(" .")
    return slug or "page"


def namespace_directory(namespace: int, namespace_name: str) -> str:
    label = "main" if namespace == 0 else namespace_name.lower().replace(" ", "-")
    label = re.sub(r"[^a-z0-9-]+", "-", label).strip("-") or "unnamed"
    return f"ns-{namespace}-{label}"


def title_without_namespace(title: str, namespace: int) -> str:
    if namespace and ":" in title:
        return title.split(":", 1)[1]
    return title


def canonical_url(title: str) -> str:
    slug = urllib.parse.quote(title.replace(" ", "_"), safe="():,._-'")
    return f"{SITE_ORIGIN}/wiki/{slug}"


def edit_url(title: str) -> str:
    query_title = urllib.parse.quote(title, safe="")
    return f"{SITE_ORIGIN}/index.php?title={query_title}&action=edit"


def oldid_url(title: str, revid: int) -> str:
    query_title = urllib.parse.quote(title, safe="")
    return f"{SITE_ORIGIN}/index.php?title={query_title}&oldid={revid}"


def parse_export(export_path: Path) -> tuple[dict[str, Any], dict[int, str], list[Page]]:
    tree = ET.parse(export_path)
    root = tree.getroot()
    match = re.match(r"\{([^}]+)\}", root.tag)
    if not match:
        raise ValueError("MediaWiki export XML has no namespace")
    namespace = match.group(1)

    siteinfo_element = root.find(qname(namespace, "siteinfo"))
    if siteinfo_element is None:
        raise ValueError("MediaWiki export XML has no siteinfo")

    namespace_names: dict[int, str] = {}
    namespaces_element = siteinfo_element.find(qname(namespace, "namespaces"))
    if namespaces_element is not None:
        for element in namespaces_element:
            namespace_names[int(element.attrib["key"])] = element.text or ""

    siteinfo = {
        "sitename": text_of(siteinfo_element, "sitename", namespace),
        "dbname": text_of(siteinfo_element, "dbname", namespace),
        "base": text_of(siteinfo_element, "base", namespace),
        "generator": text_of(siteinfo_element, "generator", namespace),
        "case": text_of(siteinfo_element, "case", namespace),
    }

    pages: list[Page] = []
    for page_element in root.findall(qname(namespace, "page")):
        title = text_of(page_element, "title", namespace)
        page_namespace = int(text_of(page_element, "ns", namespace))
        pageid = int(text_of(page_element, "id", namespace))
        revisions = page_element.findall(qname(namespace, "revision"))
        if len(revisions) != 1:
            raise ValueError(
                f"{title!r} has {len(revisions)} revisions; export current revision only"
            )
        revision = revisions[0]
        text_element = revision.find(qname(namespace, "text"))
        if text_element is None:
            raise ValueError(f"{title!r} has no revision text")

        source = text_element.text or ""
        source_data = source.encode("utf-8")
        recorded_bytes = int(text_element.attrib.get("bytes", len(source_data)))
        if recorded_bytes != len(source_data):
            raise ValueError(
                f"{title!r}: XML byte count {recorded_bytes} != {len(source_data)}"
            )

        recorded_sha1 = text_element.attrib.get("sha1") or text_of(
            revision, "sha1", namespace
        )
        calculated_sha1 = mediawiki_sha1(source_data)
        if recorded_sha1 and recorded_sha1 != calculated_sha1:
            raise ValueError(
                f"{title!r}: MediaWiki SHA-1 {recorded_sha1} != {calculated_sha1}"
            )

        contributor_element = revision.find(qname(namespace, "contributor"))
        contributor: str | None = None
        if contributor_element is not None:
            contributor = (
                contributor_element.findtext(qname(namespace, "username"))
                or contributor_element.findtext(qname(namespace, "ip"))
            )

        redirect_match = REDIRECT_RE.match(source)
        pages.append(
            Page(
                title=title,
                namespace=page_namespace,
                pageid=pageid,
                revid=int(text_of(revision, "id", namespace)),
                parentid=optional_int(revision.findtext(qname(namespace, "parentid"))),
                revision_timestamp=text_of(revision, "timestamp", namespace),
                contributor=contributor,
                comment=revision.findtext(qname(namespace, "comment")),
                contentmodel=text_of(revision, "model", namespace),
                contentformat=text_of(revision, "format", namespace),
                source=source,
                source_bytes=len(source_data),
                source_sha1=recorded_sha1 or calculated_sha1,
                source_sha256=hashlib.sha256(source_data).hexdigest(),
                redirect_target=redirect_match.group(1).strip() if redirect_match else None,
                redirect_fragment=(
                    redirect_match.group(2).strip()
                    if redirect_match and redirect_match.group(2)
                    else None
                ),
            )
        )

    pageids = [page.pageid for page in pages]
    if len(pageids) != len(set(pageids)):
        raise ValueError("MediaWiki export contains duplicate page IDs")
    return siteinfo, namespace_names, pages


def load_rendered_jsonl(path: Path) -> dict[int, dict[str, Any]]:
    rows: dict[int, dict[str, Any]] = {}
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            row = json.loads(line)
            pageid = int(row["pageid"])
            if pageid in rows:
                raise ValueError(f"rendered JSONL repeats page ID {pageid}")
            rendered_html = row.get("html")
            if not rendered_html:
                raise ValueError(f"rendered JSONL line {line_number} has no HTML")
            if row.get("capture_complete") is not True:
                raise ValueError(
                    f"rendered JSONL line {line_number} is not marked capture_complete"
                )
            if int(row.get("html_length", -1)) != len(rendered_html):
                raise ValueError(
                    f"rendered JSONL line {line_number} has an HTML length mismatch"
                )
            calculated_hash = hashlib.sha256(rendered_html.encode("utf-8")).hexdigest()
            if row.get("html_sha256") != calculated_hash:
                raise ValueError(
                    f"rendered JSONL line {line_number} has an HTML hash mismatch"
                )
            rows[pageid] = row
    return rows


def relative_link(from_path: str, to_path: str) -> str:
    return posixpath.relpath(to_path, start=str(PurePosixPath(from_path).parent))


def normalized_link_title(value: str) -> str:
    return urllib.parse.unquote(value).replace("_", " ").strip()


def follow_redirects(page: Page, resolve_title) -> tuple[Page, str | None]:
    """Resolve a local redirect chain and carry its first section fragment."""
    current = page
    fragment: str | None = None
    seen: set[int] = set()
    while current.redirect_target and current.pageid not in seen:
        seen.add(current.pageid)
        if fragment is None and current.redirect_fragment:
            fragment = current.redirect_fragment
        target = resolve_title(current.redirect_target)
        if target is None:
            break
        current = target
    return current, fragment


def build_title_resolver(pages: Iterable[Page]):
    exact = {page.title: page for page in pages}
    folded: dict[str, list[Page]] = defaultdict(list)
    for page in pages:
        folded[page.title.casefold()].append(page)

    def resolve(value: str) -> Page | None:
        candidate = normalized_link_title(value)
        if candidate in exact:
            return exact[candidate]
        if candidate:
            first_letter = candidate[0].upper() + candidate[1:]
            if first_letter in exact:
                return exact[first_letter]
        matches = folded.get(candidate.casefold(), [])
        return matches[0] if len(matches) == 1 else None

    return resolve


def rewrite_single_url(
    value: str,
    current_path: str,
    resolve_title,
) -> str:
    decoded = html.unescape(value)
    if decoded.startswith("//"):
        return "https:" + decoded
    if decoded.startswith("/wiki/"):
        page_and_fragment = decoded[len("/wiki/") :]
        page_part, separator, fragment = page_and_fragment.partition("#")
        target = resolve_title(page_part)
        if target is not None:
            target, redirect_fragment = follow_redirects(target, resolve_title)
            target_path = target.rendered_path or target.source_path
            rewritten = relative_link(current_path, target_path)
            effective_fragment = fragment if separator else redirect_fragment
            if effective_fragment:
                rewritten += "#" + urllib.parse.quote(
                    effective_fragment, safe="-_.:()"
                )
            return rewritten
        return SITE_ORIGIN + decoded
    if decoded.startswith("/"):
        return SITE_ORIGIN + decoded
    return decoded


def rewrite_html_links(body: str, current_path: str, resolve_title) -> str:
    def replace_attribute(match: re.Match[str]) -> str:
        name = match.group("name")
        quote = match.group("quote")
        value = match.group("value")
        if name.lower() == "srcset":
            candidates: list[str] = []
            for candidate in html.unescape(value).split(","):
                pieces = candidate.strip().split(None, 1)
                if not pieces:
                    continue
                rewritten = rewrite_single_url(pieces[0], current_path, resolve_title)
                candidates.append(
                    rewritten + (f" {pieces[1]}" if len(pieces) == 2 else "")
                )
            new_value = ", ".join(candidates)
        else:
            new_value = rewrite_single_url(value, current_path, resolve_title)
        return f"{name}={quote}{html.escape(new_value, quote=True)}{quote}"

    return ATTRIBUTE_RE.sub(replace_attribute, body)


STYLE = """
body { font-family: Georgia, 'Times New Roman', serif; max-width: 1040px; margin: 0 auto; padding: 1.5rem; color: #202122; line-height: 1.58; }
h1, h2, h3, h4, h5, h6 { font-family: system-ui, sans-serif; line-height: 1.25; }
a { color: #0645ad; } a:visited { color: #0b0080; }
.mirror-meta { color: #54595d; font: 0.85rem/1.45 system-ui, sans-serif; border-bottom: 1px solid #eaecf0; padding-bottom: .8rem; margin-bottom: 1.2rem; }
.mirror-meta code { color: #202122; }
table { border-collapse: collapse; margin: 1rem 0; max-width: 100%; }
td, th { border: 1px solid #a2a9b1; padding: .4rem .6rem; vertical-align: top; }
th { background: #eaecf0; }
img, video { max-width: 100%; height: auto; }
pre { background: #f8f9fa; border: 1px solid #eaecf0; padding: 1rem; overflow-x: auto; }
code { background: #f8f9fa; padding: .1rem .25rem; }
.toc, .navbox { background: #f8f9fa; border: 1px solid #a2a9b1; padding: .8rem; }
.redirect { background: #f8f9fa; border-left: .3rem solid #36c; padding: .8rem 1rem; }
""".strip()


def wrap_rendered_page(
    page: Page,
    body: str,
    current_path: str,
    used_content_root: bool,
) -> str:
    index_href = relative_link(current_path, "_index.html")
    raw_href = relative_link(current_path, page.source_path)
    content = body if used_content_root else f'<div class="mw-parser-output">{body}</div>'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(page.title)} — SuperMemo Help mirror</title>
<style>{STYLE}</style>
</head>
<body>
<div class="mirror-meta">
<a href="{html.escape(index_href, quote=True)}">Mirror index</a> ·
<a href="{html.escape(raw_href, quote=True)}">View raw source</a> ·
<a href="{html.escape(canonical_url(page.title), quote=True)}">Official page</a> ·
revision <a href="{html.escape(oldid_url(page.title, page.revid), quote=True)}"><code>{page.revid}</code></a>
</div>
<h1>{html.escape(page.title)}</h1>
<main id="mw-content-text">{content}</main>
</body>
</html>
"""


def wrap_redirect_page(
    page: Page,
    target: Page | None,
    target_fragment: str | None,
    current_path: str,
) -> str:
    index_href = relative_link(current_path, "_index.html")
    raw_href = relative_link(current_path, page.source_path)
    if target is not None:
        target_href = relative_link(current_path, target.rendered_path or target.source_path)
    else:
        target_href = canonical_url(page.redirect_target or "")
    if target_fragment:
        target_href += "#" + urllib.parse.quote(target_fragment, safe="-_.:()")
    target_label = target.title if target is not None else (page.redirect_target or "unknown target")
    if target_fragment:
        target_label += "#" + target_fragment
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(page.title)} — SuperMemo Help mirror</title>
<style>{STYLE}</style>
</head>
<body>
<div class="mirror-meta">
<a href="{html.escape(index_href, quote=True)}">Mirror index</a> ·
<a href="{html.escape(raw_href, quote=True)}">View raw source</a> ·
<a href="{html.escape(canonical_url(page.title), quote=True)}">Official page</a> ·
revision <a href="{html.escape(oldid_url(page.title, page.revid), quote=True)}"><code>{page.revid}</code></a>
</div>
<h1>{html.escape(page.title)}</h1>
<p class="redirect">Redirect to <a href="{html.escape(target_href, quote=True)}">{html.escape(target_label)}</a>.</p>
</body>
</html>
"""


def manifest_row(page: Page) -> dict[str, Any]:
    return {
        "pageid": page.pageid,
        "namespace": page.namespace,
        "title": page.title,
        "canonical_url": canonical_url(page.title),
        "edit_url": edit_url(page.title),
        "oldid_url": oldid_url(page.title, page.revid),
        "revid": page.revid,
        "parentid": page.parentid,
        "revision_timestamp": page.revision_timestamp,
        "contributor": page.contributor,
        "comment": page.comment,
        "contentmodel": page.contentmodel,
        "contentformat": page.contentformat,
        "source_bytes": page.source_bytes,
        "source_sha1": page.source_sha1,
        "source_sha256": page.source_sha256,
        "source_path": page.source_path,
        "rendered_path": page.rendered_path,
        "rendered_kind": page.rendered_kind,
        "redirect_target": page.redirect_target,
        "redirect_fragment": page.redirect_fragment,
    }


def render_index(pages: list[Page], snapshot: dict[str, Any]) -> str:
    rows: list[str] = []
    for page in pages:
        source_link = f'<a href="{html.escape(page.source_path, quote=True)}">source</a>'
        rendered_link = (
            f'<a href="{html.escape(page.rendered_path, quote=True)}">rendered</a>'
            if page.rendered_path
            else "—"
        )
        redirect = html.escape(page.redirect_target) if page.redirect_target else ""
        rows.append(
            "<tr>"
            f"<td>{page.namespace}</td>"
            f"<td>{html.escape(page.title)}</td>"
            f"<td><code>{page.revid}</code></td>"
            f"<td>{source_link}</td>"
            f"<td>{rendered_link}</td>"
            f"<td>{redirect}</td>"
            "</tr>"
        )
    namespace_summary = ", ".join(
        f"ns {key}: {value}" for key, value in snapshot["page_counts_by_namespace"].items()
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SuperMemo Help — local mirror</title>
<style>{STYLE}
body {{ max-width: 1280px; }}
input {{ width: min(38rem, 100%); padding: .55rem; margin: .5rem 0 1rem; }}
tbody tr[hidden] {{ display: none; }}
</style>
</head>
<body>
<h1>SuperMemo Help — local mirror</h1>
<p><strong>{snapshot['page_count']}</strong> raw current revisions; <strong>{snapshot['rendered_page_count']}</strong> rendered documentation pages.</p>
<p>{html.escape(namespace_summary)}. Media binaries are not bundled.</p>
<p><a href="manifest.jsonl">manifest.jsonl</a> · <a href="snapshot.json">snapshot.json</a> · <a href="../README.md">documentation notes</a> · <a href="https://help.supermemo.org">official site</a></p>
<label for="filter">Filter by title or namespace</label><br>
<input id="filter" type="search" placeholder="e.g. priority, Glossary, keyboard">
<table>
<thead><tr><th>NS</th><th>Title</th><th>Revision</th><th>Raw</th><th>Rendered</th><th>Redirect target</th></tr></thead>
<tbody id="pages">{''.join(rows)}</tbody>
</table>
<script>
const filter = document.getElementById('filter');
filter.addEventListener('input', () => {{
  const needle = filter.value.toLocaleLowerCase();
  for (const row of document.querySelectorAll('#pages tr')) {{
    row.hidden = !row.textContent.toLocaleLowerCase().includes(needle);
  }}
}});
</script>
</body>
</html>
"""


def validate_local_links(output: Path) -> list[str]:
    failures: list[str] = []
    for rendered_file in (output / "rendered").rglob("*.html"):
        body = rendered_file.read_text(encoding="utf-8")
        for match in re.finditer(r"\bhref=[\"']([^\"']+)[\"']", body, re.IGNORECASE):
            href = html.unescape(match.group(1))
            if not href or href.startswith(("#", "http://", "https://", "mailto:", "javascript:")):
                continue
            path_part = urllib.parse.unquote(href.split("#", 1)[0].split("?", 1)[0])
            target = (rendered_file.parent / Path(path_part)).resolve()
            if not target.exists():
                failures.append(f"{rendered_file.relative_to(output)} -> {href}")
    return failures


def ensure_safe_output(repo_root: Path, output: Path) -> None:
    repo_root = repo_root.resolve()
    output = output.resolve()
    docs_root = (repo_root / "docs").resolve()
    if output.parent != docs_root or not output.name.startswith("wiki"):
        raise ValueError(f"refusing unsafe output directory: {output}")


def remove_tree_with_retries(path: Path, attempts: int = 12) -> None:
    """Remove a generated tree despite short-lived Windows indexer locks."""
    for attempt in range(attempts):
        if not path.exists():
            return
        try:
            shutil.rmtree(path)
            return
        except OSError:
            if attempt == attempts - 1:
                raise
            time.sleep(min(0.25 * (attempt + 1), 1.5))


def rename_with_retries(source: Path, destination: Path, attempts: int = 12) -> None:
    for attempt in range(attempts):
        try:
            source.replace(destination)
            return
        except OSError:
            if attempt == attempts - 1:
                raise
            time.sleep(min(0.25 * (attempt + 1), 1.5))


def install_staged_tree(staging: Path, output: Path) -> None:
    """Swap a validated staging tree into place without deleting live output first."""
    backup = output.with_name(f".{output.name}.previous")
    remove_tree_with_retries(backup)
    had_output = output.exists()
    if had_output:
        rename_with_retries(output, backup)
    try:
        rename_with_retries(staging, output)
    except Exception:
        if had_output and backup.exists() and not output.exists():
            rename_with_retries(backup, output)
        raise
    if backup.exists():
        remove_tree_with_retries(backup)


def build_mirror(
    export_path: Path,
    rendered_path: Path,
    output: Path,
    fetched_at: str,
    allow_shrink: bool = False,
) -> dict[str, Any]:
    repo_root = Path(__file__).resolve().parents[1]
    ensure_safe_output(repo_root, output)
    siteinfo, namespace_names, pages = parse_export(export_path)
    rendered = load_rendered_jsonl(rendered_path)

    actual_namespaces = {page.namespace for page in pages}
    missing_namespaces = EXPECTED_NAMESPACES - actual_namespaces
    if missing_namespaces:
        raise ValueError(f"export is missing expected namespaces: {sorted(missing_namespaces)}")

    incoming_counts = Counter(page.namespace for page in pages)
    required_counts = dict(MINIMUM_PAGE_COUNTS)
    previous_snapshot_path = output / "snapshot.json"
    if previous_snapshot_path.exists():
        previous_snapshot = json.loads(previous_snapshot_path.read_text(encoding="utf-8"))
        for key, value in previous_snapshot.get("page_counts_by_namespace", {}).items():
            namespace_id = int(key)
            required_counts[namespace_id] = max(required_counts.get(namespace_id, 0), int(value))
    shortfalls = {
        namespace_id: {"required": required, "received": incoming_counts[namespace_id]}
        for namespace_id, required in required_counts.items()
        if incoming_counts[namespace_id] < required
    }
    if shortfalls and not allow_shrink:
        raise ValueError(
            f"export page counts shrank; verify AllPages coverage or pass --allow-shrink: {shortfalls}"
        )

    pages.sort(key=lambda page: (page.namespace, page.title.casefold(), page.title, page.pageid))
    paths_casefolded: set[str] = set()
    for page in pages:
        directory = namespace_directory(
            page.namespace, namespace_names.get(page.namespace, f"ns-{page.namespace}")
        )
        slug = safe_slug(title_without_namespace(page.title, page.namespace))
        page.source_path = f"source/{directory}/p{page.pageid}--{slug}.wiki"
        if page.namespace in DOCUMENT_NAMESPACES:
            page.rendered_path = f"rendered/{directory}/p{page.pageid}--{slug}.html"
            page.rendered_kind = (
                "local-redirect" if page.redirect_target else "official-parser-output"
            )
        for candidate in filter(None, [page.source_path, page.rendered_path]):
            folded = candidate.casefold()
            if folded in paths_casefolded:
                raise ValueError(f"case-insensitive path collision: {candidate}")
            paths_casefolded.add(folded)

    expected_rendered = {
        page.pageid
        for page in pages
        if page.namespace in DOCUMENT_NAMESPACES and not page.redirect_target
    }
    if set(rendered) != expected_rendered:
        missing = sorted(expected_rendered - set(rendered))
        extra = sorted(set(rendered) - expected_rendered)
        raise ValueError(f"rendered JSONL page mismatch; missing={missing}, extra={extra}")

    pages_by_id = {page.pageid: page for page in pages}
    for pageid, row in rendered.items():
        page = pages_by_id[pageid]
        if int(row["revid"]) != page.revid:
            raise ValueError(
                f"{page.title!r}: rendered revision {row['revid']} != XML {page.revid}"
            )
        if "Just a moment" in row["html"]:
            raise ValueError(f"{page.title!r}: rendered HTML contains Cloudflare challenge")

    staging = output.with_name(f".{output.name}.build")
    remove_tree_with_retries(staging)
    (staging / "source").mkdir(parents=True)
    (staging / "rendered").mkdir(parents=True)

    for page in pages:
        source_file = staging / Path(page.source_path)
        source_file.parent.mkdir(parents=True, exist_ok=True)
        source_file.write_bytes(page.source.encode("utf-8"))

    resolve_title = build_title_resolver(pages)
    for page in pages:
        if page.rendered_path is None:
            continue
        rendered_file = staging / Path(page.rendered_path)
        rendered_file.parent.mkdir(parents=True, exist_ok=True)
        if page.redirect_target:
            target, target_fragment = follow_redirects(page, resolve_title)
            if target.pageid == page.pageid:
                target = resolve_title(page.redirect_target)
                target_fragment = page.redirect_fragment
            document = wrap_redirect_page(
                page, target, target_fragment, page.rendered_path
            )
        else:
            row = rendered[page.pageid]
            rewritten = rewrite_html_links(row["html"], page.rendered_path, resolve_title)
            document = wrap_rendered_page(
                page,
                rewritten,
                page.rendered_path,
                bool(row.get("used_content_root")),
            )
        rendered_file.write_text(document, encoding="utf-8", newline="\n")

    manifest_rows = [manifest_row(page) for page in pages]
    manifest_body = "".join(
        json.dumps(row, ensure_ascii=False, separators=(",", ":"), sort_keys=True) + "\n"
        for row in manifest_rows
    )
    manifest_path = staging / "manifest.jsonl"
    manifest_path.write_text(manifest_body, encoding="utf-8", newline="\n")

    namespace_counts = incoming_counts
    redirect_counts = Counter(page.namespace for page in pages if page.redirect_target)
    rendered_count = sum(page.rendered_path is not None for page in pages)
    snapshot: dict[str, Any] = {
        "schema_version": 1,
        "fetched_at": fetched_at,
        "source": SITE_ORIGIN,
        "export_file": export_path.name,
        "export_sha256": hashlib.sha256(export_path.read_bytes()).hexdigest(),
        "manifest_sha256": hashlib.sha256(manifest_body.encode("utf-8")).hexdigest(),
        "siteinfo": siteinfo,
        "page_count": len(pages),
        "page_counts_by_namespace": {
            str(key): namespace_counts[key] for key in sorted(namespace_counts)
        },
        "redirect_counts_by_namespace": {
            str(key): redirect_counts[key] for key in sorted(redirect_counts)
        },
        "rendered_page_count": rendered_count,
        "rendered_official_page_count": len(rendered),
        "scope": {
            "documentation_namespaces": sorted(DOCUMENT_NAMESPACES),
            "dependency_namespaces": sorted(DEPENDENCY_NAMESPACES),
            "current_revision_only": True,
            "revision_history_included": False,
            "media_binaries_included": False,
            "talk_user_and_mediawiki_namespaces_included": False,
        },
    }
    (staging / "snapshot.json").write_text(
        json.dumps(snapshot, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    (staging / "_index.html").write_text(
        render_index(pages, snapshot), encoding="utf-8", newline="\n"
    )

    link_failures = validate_local_links(staging)
    if link_failures:
        preview = "\n".join(link_failures[:20])
        raise ValueError(f"generated mirror has broken local links:\n{preview}")

    install_staged_tree(staging, output)
    return snapshot


def default_fetched_at() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("export_xml", type=Path, help="MediaWiki Special:Export XML")
    parser.add_argument(
        "--rendered-jsonl",
        required=True,
        type=Path,
        help="JSONL containing pageid, revid, title and expanded HTML",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("docs/wiki"),
        help="mirror directory inside this repository (default: docs/wiki)",
    )
    parser.add_argument(
        "--fetched-at",
        default=default_fetched_at(),
        help="UTC ISO-8601 snapshot time",
    )
    parser.add_argument(
        "--allow-shrink",
        action="store_true",
        help="allow namespace counts below the bundled/previous snapshot after manual review",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    repo_root = Path(__file__).resolve().parents[1]
    output = args.output if args.output.is_absolute() else repo_root / args.output
    snapshot = build_mirror(
        args.export_xml.resolve(),
        args.rendered_jsonl.resolve(),
        output.resolve(),
        args.fetched_at,
        args.allow_shrink,
    )
    counts = ", ".join(
        f"ns {key}={value}" for key, value in snapshot["page_counts_by_namespace"].items()
    )
    print(
        f"Built {output}: {snapshot['page_count']} sources ({counts}), "
        f"{snapshot['rendered_page_count']} rendered pages."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
