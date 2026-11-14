#!/usr/bin/env python3
"""Import the public Substack RSS feed as reviewable Jekyll Markdown posts.

Only files named *_substack-* under _posts are managed by this importer.
Never commits, pushes, or publishes; the GitHub Action creates a PR separately.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import hashlib
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import urlparse
from urllib.request import Request, urlopen

import feedparser
from bs4 import BeautifulSoup
from markdownify import markdownify as to_markdown

FEED_URL = "https://gboschbo.substack.com/feed"
POSTS = Path("_posts")
TRANSLATIONS_FILE = Path("_data/substack_translations.json")


def translation_groups() -> dict[str, tuple[str, str | None]]:
    """Map full Substack URLs to a shared group key for multilingual siblings."""
    if not TRANSLATIONS_FILE.exists():
        return {}
    data = json.loads(TRANSLATIONS_FILE.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Substack translations mapping must be a JSON object")
    groups = {}
    for group, urls in data.items():
        if not isinstance(group, str) or not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_-]*", group):
            raise ValueError(f"Invalid translation group: {group}")
        if not isinstance(urls, list):
            raise ValueError(f"Group {group} must list URLs")
        for item in urls:
            if isinstance(item, str):
                url, language = item, None
            elif isinstance(item, dict):
                url, language = item.get("url"), item.get("lang")
            else:
                raise ValueError(f"Invalid translation entry in group {group}")
            if not isinstance(url, str) or (language is not None and language not in {"ca", "es", "en"}):
                raise ValueError(f"Invalid URL or language in group {group}: {item}")
            normalized = canonical(url)
            parsed = urlparse(normalized)
            if parsed.scheme != "https" or parsed.netloc.lower() != "gboschbo.substack.com" or not parsed.path.startswith("/p/"):
                raise ValueError(f"Unrecognized Substack URL: {url}")
            if normalized in groups:
                raise ValueError(f"Duplicate translation URL: {url}")
            groups[normalized] = (group, language)
    return groups
SOURCE_LINE = re.compile(r'^substack_url:\s*["\x27]?(.+?)["\x27]?\s*$', re.MULTILINE)


def quote_yaml(value: str) -> str:
    # JSON strings are valid quoted YAML scalars; ensure Jekyll-safe metadata.
    import json
    return json.dumps(value, ensure_ascii=False)


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", value.lower())).strip("-") or "post"


def canonical(url: str) -> str:
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}".rstrip("/")


def published_date(entry) -> str:
    for field in ("published", "updated"):
        if entry.get(field):
            try:
                return parsedate_to_datetime(entry[field]).date().isoformat()
            except (ValueError, TypeError, IndexError):
                pass
    for field in ("published_parsed", "updated_parsed"):
        if entry.get(field):
            return datetime(*entry[field][:6], tzinfo=timezone.utc).date().isoformat()
    raise ValueError(f"Post lacks a usable publication date: {entry.get('link')}")


def detect_language(entry) -> str:
    # Default to the original Catalan; language can be corrected in the PR.
    # Explicit Substack tags (ca/es/en, català/español/english) take precedence.
    tags = [t.get("term", "").strip().lower() for t in entry.get("tags", [])]
    for language, labels in (
        ("ca", {"ca", "català", "catala", "catalan"}),
        ("es", {"es", "español", "espanyol", "spanish"}),
        ("en", {"en", "english", "anglès", "angles"}),
    ):
        if any(t in labels for t in tags):
            return language
    return "ca"


def body_markdown(entry) -> str:
    html = ""
    for part in entry.get("content", []):
        if part.get("value"):
            html = part["value"]
            break
    if not html:
        html = entry.get("summary", "") or ""
    soup = BeautifulSoup(html, "html.parser")
    for node in soup(["script", "style", "iframe", "form", "button", "noscript"]):
        node.decompose()
    # Preserve images as Markdown linked to their Substack-hosted URLs.
    for image in soup.select("img"):
        if not image.get("src") and image.get("data-src"):
            image["src"] = image["data-src"]
    text = to_markdown(str(soup), heading_style="ATX", bullets="-")
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text + "\n"


def existing_imports() -> dict[str, Path]:
    found = {}
    for path in POSTS.glob("*-substack-*.md"):
        match = SOURCE_LINE.search(path.read_text(encoding="utf-8"))
        if match:
            found[canonical(match.group(1).strip().strip('"\x27'))] = path
    return found


def render(entry, url: str, slug: str, date: str, groups: dict[str, tuple[str, str | None]]) -> str:
    title = entry.get("title", "").strip() or slug.replace("-", " ").capitalize()
    mapped_group, mapped_language = groups.get(url, (None, None))
    language = mapped_language or detect_language(entry)
    source_hash = hashlib.sha256(url.encode("utf-8")).hexdigest()[:12]
    # Sibling translations are linked by explicit URL grouping in the data file.
    group_key = mapped_group or f"substack-{source_hash}"
    head = [
        "---",
        "layout: conversa",
        f"title: {quote_yaml(title)}",
        f"date: {date}",
        "categories: [personal]",
        "tags: [converses-de-casa]",
        f"lang: {language}",
        f"translation_key: {quote_yaml(group_key)}",
        f"permalink: /{'es/' if language == 'es' else 'en/' if language == 'en' else ''}converses-de-casa/{slug}/",
        f"substack_url: {quote_yaml(url)}",
        "author_profile: true",
        "comments: false",
        "share: false",
        "related: false",
        "---",
        "",
    ]
    return "\n".join(head) + body_markdown(entry)


def sync(feed_bytes: bytes) -> tuple[int, int]:
    feed = feedparser.parse(feed_bytes)
    if feed.bozo and not feed.entries:
        raise ValueError(f"Invalid RSS feed: {feed.get('bozo_exception')}")
    if not feed.entries:
        raise ValueError("RSS feed has no entries; refusing to treat an empty feed as a successful sync")
    POSTS.mkdir(exist_ok=True)
    known = existing_imports()
    groups = translation_groups()
    created = updated = 0
    for entry in feed.entries:
        url = canonical(entry.get("link", ""))
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.netloc.lower() != "gboschbo.substack.com" or not parsed.path.startswith("/p/"):
            print(f"Skipping unexpected entry URL: {url}")
            continue
        slug = slugify(parsed.path.rsplit("/", 1)[-1])
        date = published_date(entry)
        path = known.get(url)
        if path is None:
            path = POSTS / f"{date}-substack-{slug}.md"
            if path.exists():
                raise FileExistsError(f"Unmanaged path collision: {path}")
        content = render(entry, url, slug, date, groups)
        if not path.exists():
            path.write_text(content, encoding="utf-8")
            created += 1
            print(f"Created {path}")
        elif path.read_text(encoding="utf-8") != content:
            path.write_text(content, encoding="utf-8")
            updated += 1
            print(f"Updated {path}")
    print(f"Substack sync: {created} created, {updated} updated; {len(feed.entries)} feed entries.")
    return created, updated


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--feed-file", type=Path, help="Local RSS fixture for testing")
    args = parser.parse_args()
    if args.feed_file:
        raw = args.feed_file.read_bytes()
    else:
        req = Request(FEED_URL, headers={"User-Agent": "ConversesDeCasaSync/1.0 (+https://github.com/guiem/guiem.github.io)"})
        with urlopen(req, timeout=30) as response:
            raw = response.read()
    sync(raw)


if __name__ == "__main__":
    main()
