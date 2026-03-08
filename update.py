#!/usr/bin/env python3
"""
Fetch Apple Developer docs for Swift and SwiftUI and convert to Markdown.

Uses ETags for incremental updates — only re-fetches pages that have
changed on Apple's servers since the last run.

Usage:
    ./update.py                  # default depth 2, both swift and swiftui
    ./update.py --depth 3        # crawl 3 levels deep
    ./update.py --depth 1        # articles only (no type overviews)
    ./update.py --targets swift  # only fetch Swift docs
    ./update.py --no-push        # don't push to remote after updating
    ./update.py --full           # ignore cached ETags, re-fetch everything
"""

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

BASE_URL = "https://developer.apple.com/tutorials/data"
SCRIPT_DIR = Path(__file__).resolve().parent
ETAGS_FILE = SCRIPT_DIR / ".etags.json"


def load_etags():
    """Load saved ETags from disk."""
    if ETAGS_FILE.exists():
        return json.loads(ETAGS_FILE.read_text())
    return {}


def save_etags(etags):
    """Save ETags to disk."""
    ETAGS_FILE.write_text(json.dumps(etags, indent=2) + "\n")


def fetch_json(path, etags):
    """Fetch a documentation JSON file from Apple's API.

    Returns (data, changed) where changed is False if the server
    returned 304 Not Modified.
    """
    url = f"{BASE_URL}{path}.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    cached_etag = etags.get(path)
    if cached_etag:
        headers["If-None-Match"] = cached_etag

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp:
            etag = resp.headers.get("ETag")
            if etag:
                etags[path] = etag
            data = json.loads(resp.read())
            print(f"  Fetching: {path} -> updated")
            return data, True
    except urllib.error.HTTPError as e:
        if e.code == 304:
            print(f"  Fetching: {path} -> not modified")
            return None, False
        print(f"  Fetching: {path} -> HTTP {e.code}")
        return None, None  # actual error
    except Exception as e:
        print(f"  Fetching: {path} -> Error: {e}")
        return None, None


# ---------------------------------------------------------------------------
# Markdown rendering
# ---------------------------------------------------------------------------

def render_inline(nodes, references=None):
    """Render inline content nodes to markdown text."""
    parts = []
    for node in nodes:
        t = node.get("type")
        if t == "text":
            parts.append(node["text"])
        elif t == "codeVoice":
            parts.append(f'`{node["code"]}`')
        elif t == "emphasis":
            inner = render_inline(node.get("inlineContent", []), references)
            parts.append(f"*{inner}*")
        elif t == "strong":
            inner = render_inline(node.get("inlineContent", []), references)
            parts.append(f"**{inner}**")
        elif t == "reference":
            ref_id = node.get("identifier", "")
            ref_data = references.get(ref_id, {}) if references else {}
            title = ref_data.get("title", ref_id.split("/")[-1])
            ref_url = ref_data.get("url", "")
            if ref_url:
                parts.append(f"[{title}]({ref_url})")
            else:
                parts.append(title)
        elif t == "link":
            title = node.get("title", "")
            if not title:
                title = render_inline(node.get("inlineContent", []), references)
            parts.append(f'[{title}]({node.get("destination", "")})')
        elif t == "image":
            ref_id = node.get("identifier", "")
            ref_data = references.get(ref_id, {}) if references else {}
            alt = ref_data.get("alt", "image")
            parts.append(f"![{alt}]")
        elif t == "inlineHead":
            inner = render_inline(node.get("inlineContent", []), references)
            parts.append(f"**{inner}**")
        elif t == "newTerm":
            inner = render_inline(node.get("inlineContent", []), references)
            parts.append(f"*{inner}*")
        elif t == "superscript":
            inner = render_inline(node.get("inlineContent", []), references)
            parts.append(f"<sup>{inner}</sup>")
        elif t == "subscript":
            inner = render_inline(node.get("inlineContent", []), references)
            parts.append(f"<sub>{inner}</sub>")
        else:
            if "text" in node:
                parts.append(node["text"])
            elif "inlineContent" in node:
                parts.append(render_inline(node["inlineContent"], references))
    return "".join(parts)


def render_content_blocks(blocks, references=None, indent=0):
    """Render content blocks to markdown lines."""
    lines = []
    prefix = "  " * indent

    for block in blocks:
        t = block.get("type")

        if t == "heading":
            level = block.get("level", 2)
            text = block.get("text", "")
            lines.append(f"{'#' * level} {text}")
            lines.append("")

        elif t == "paragraph":
            text = render_inline(block.get("inlineContent", []), references)
            lines.append(f"{prefix}{text}")
            lines.append("")

        elif t == "codeListing":
            syntax = block.get("syntax", "")
            code = "\n".join(block.get("code", []))
            lines.append(f"{prefix}```{syntax}")
            lines.append(code)
            lines.append(f"{prefix}```")
            lines.append("")

        elif t == "unorderedList":
            for item in block.get("items", []):
                content = item.get("content", [])
                if content:
                    first = content[0]
                    text = render_inline(first.get("inlineContent", []), references)
                    lines.append(f"{prefix}- {text}")
                    if len(content) > 1:
                        sub = render_content_blocks(content[1:], references, indent + 1)
                        lines.extend(sub)
            lines.append("")

        elif t == "orderedList":
            for i, item in enumerate(block.get("items", []), 1):
                content = item.get("content", [])
                if content:
                    first = content[0]
                    text = render_inline(first.get("inlineContent", []), references)
                    lines.append(f"{prefix}{i}. {text}")
                    if len(content) > 1:
                        sub = render_content_blocks(content[1:], references, indent + 1)
                        lines.extend(sub)
            lines.append("")

        elif t == "aside":
            name = block.get("name", "Note")
            lines.append(f"{prefix}> **{name}:**")
            for c in block.get("content", []):
                text = render_inline(c.get("inlineContent", []), references)
                lines.append(f"{prefix}> {text}")
            lines.append(f"{prefix}>")
            lines.append("")

        elif t == "table":
            rows = block.get("rows", [])
            if rows:
                headers = []
                for cell in rows[0]:
                    cell_content = cell if isinstance(cell, list) else cell.get("content", [cell])
                    cell_parts = []
                    for c in cell_content:
                        if isinstance(c, dict):
                            cell_parts.append(render_inline(c.get("inlineContent", []), references))
                    headers.append(" ".join(cell_parts) if cell_parts else "")
                lines.append(f"{prefix}| " + " | ".join(headers) + " |")
                lines.append(f"{prefix}| " + " | ".join(["---"] * len(headers)) + " |")
                for row in rows[1:]:
                    cells = []
                    for cell in row:
                        cell_content = cell if isinstance(cell, list) else cell.get("content", [cell])
                        cell_parts = []
                        for c in cell_content:
                            if isinstance(c, dict):
                                cell_parts.append(render_inline(c.get("inlineContent", []), references))
                        cells.append(" ".join(cell_parts) if cell_parts else "")
                    lines.append(f"{prefix}| " + " | ".join(cells) + " |")
                lines.append("")

        elif t == "termList":
            for term_item in block.get("items", []):
                term = term_item.get("term", {})
                term_text = render_inline(term.get("inlineContent", []), references)
                lines.append(f"{prefix}**{term_text}**")
                definition = term_item.get("definition", {})
                for c in definition.get("content", []):
                    sub = render_content_blocks([c], references, indent)
                    lines.extend(sub)
            lines.append("")

        elif t == "links":
            pass

        else:
            if "inlineContent" in block:
                text = render_inline(block["inlineContent"], references)
                lines.append(f"{prefix}{text}")
                lines.append("")

    return lines


def convert_doc_to_markdown(data):
    """Convert a full documentation JSON response to markdown."""
    if not data:
        return None

    lines = []
    metadata = data.get("metadata", {})
    title = metadata.get("title", "Untitled")

    lines.append(f"# {title}")
    lines.append("")

    abstract = data.get("abstract", [])
    if abstract:
        lines.append(render_inline(abstract, data.get("references", {})))
        lines.append("")

    for section in data.get("primaryContentSections", []):
        kind = section.get("kind")
        if kind == "content":
            content_lines = render_content_blocks(
                section.get("content", []),
                data.get("references", {})
            )
            lines.extend(content_lines)
        elif kind == "declarations":
            for decl in section.get("declarations", []):
                tokens = decl.get("tokens", [])
                code_text = "".join(t.get("text", "") for t in tokens)
                lines.append("```swift")
                lines.append(code_text)
                lines.append("```")
                lines.append("")
        elif kind == "parameters":
            lines.append("## Parameters")
            lines.append("")
            for param in section.get("parameters", []):
                name = param.get("name", "")
                content = param.get("content", [])
                desc = ""
                for c in content:
                    desc += render_inline(c.get("inlineContent", []), data.get("references", {}))
                lines.append(f"- **{name}**: {desc}")
            lines.append("")

    for section_list_key in ["topicSections", "seeAlsoSections"]:
        sections = data.get(section_list_key, [])
        if sections:
            if section_list_key == "seeAlsoSections":
                lines.append("## See Also")
                lines.append("")
            for sec in sections:
                sec_title = sec.get("title", "")
                if sec_title:
                    lines.append(f"### {sec_title}")
                    lines.append("")
                refs = data.get("references", {})
                for ident in sec.get("identifiers", []):
                    ref = refs.get(ident, {})
                    ref_title = ref.get("title", ident.split("/")[-1])
                    ref_url = ref.get("url", "")
                    ref_abstract = ref.get("abstract", [])
                    desc = render_inline(ref_abstract, refs) if ref_abstract else ""
                    if ref_url:
                        line = f"- [{ref_title}]({ref_url})"
                    else:
                        line = f"- {ref_title}"
                    if desc:
                        line += f": {desc}"
                    lines.append(line)
                lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Crawling
# ---------------------------------------------------------------------------

def collect_topic_paths(data, base_path, skip_members=False):
    """Collect sub-topic paths from a documentation page.

    If skip_members is True, skip individual methods/properties (symbols
    nested more than one level below the framework root).
    """
    paths = []
    refs = data.get("references", {})

    for section_key in ["topicSections", "seeAlsoSections"]:
        for section in data.get(section_key, []):
            for ident in section.get("identifiers", []):
                ref = refs.get(ident, {})
                url = ref.get("url", "")
                if not url or not url.startswith("/documentation/"):
                    continue

                if skip_members:
                    role = ref.get("role", "")
                    path_parts = url.strip("/").split("/")
                    # /documentation/swift/int/init(_:) = 4 parts -> member, skip
                    # /documentation/swift/int            = 3 parts -> type overview, keep
                    if len(path_parts) > 3 and role == "symbol":
                        continue

                paths.append(url)

    return paths


def doc_path_to_filepath(doc_path, output_subdir):
    """Convert a doc API path to a local .md file path."""
    rel = doc_path.replace("/documentation/", "").strip("/")
    filename = rel.replace("/", "_") + ".md"
    return SCRIPT_DIR / output_subdir / filename


def crawl_and_convert(root_path, output_subdir, max_depth=2, etags=None,
                      delete=False):
    """Crawl documentation starting from root_path and convert all pages.

    Uses ETags for conditional requests. Only pages that have changed
    are re-converted. Pages that haven't changed are left as-is.
    """
    out_dir = SCRIPT_DIR / output_subdir
    out_dir.mkdir(parents=True, exist_ok=True)

    if etags is None:
        etags = {}

    visited = set()
    queue = [(root_path, 0)]
    updated = 0
    skipped = 0
    errors = 0
    # Track which files should exist at this depth so we can prune removed pages
    expected_files = set()

    while queue:
        doc_path, depth = queue.pop(0)
        if doc_path in visited:
            continue
        visited.add(doc_path)

        filepath = doc_path_to_filepath(doc_path, output_subdir)
        expected_files.add(filepath)

        data, changed = fetch_json(doc_path, etags)

        if changed is None:
            # Actual error (not 304)
            errors += 1
            time.sleep(0.3)
            continue

        if changed:
            # Content changed — re-convert
            md = convert_doc_to_markdown(data)
            if md:
                filepath.write_text(md, encoding="utf-8")
                updated += 1

            # Need data to discover children
            if depth < max_depth:
                skip = depth >= 1
                child_paths = collect_topic_paths(data, doc_path, skip_members=skip)
                for cp in child_paths:
                    root_prefix = root_path.rstrip("/").split("/")[2]
                    if f"/documentation/{root_prefix}" in cp or cp.startswith(doc_path):
                        if cp not in visited:
                            queue.append((cp, depth + 1))
        else:
            # 304 — not modified, but we still need to crawl children
            # Re-read existing file to get topic structure (from cached data)
            skipped += 1
            if depth < max_depth:
                # We need the JSON to discover children, so fetch without ETag
                req = urllib.request.Request(
                    f"{BASE_URL}{doc_path}.json",
                    headers={"User-Agent": "Mozilla/5.0"},
                )
                try:
                    with urllib.request.urlopen(req, timeout=30) as resp:
                        data = json.loads(resp.read())
                    skip = depth >= 1
                    child_paths = collect_topic_paths(data, doc_path, skip_members=skip)
                    for cp in child_paths:
                        root_prefix = root_path.rstrip("/").split("/")[2]
                        if f"/documentation/{root_prefix}" in cp or cp.startswith(doc_path):
                            if cp not in visited:
                                queue.append((cp, depth + 1))
                except Exception:
                    pass  # Can't discover children, not fatal

        time.sleep(0.2)

    # Check for files that no longer exist in the doc tree
    stale = []
    for existing in out_dir.glob("*.md"):
        if existing not in expected_files:
            stale.append(existing)

    deleted = 0
    for f in stale:
        if delete:
            f.unlink()
            deleted += 1
            print(f"    Deleted removed page: {f.name}")
        else:
            print(f"    Warning: {f.name} no longer in doc tree (use --delete to remove)")

    return updated, skipped, errors, deleted, len(stale)


def git_commit_and_push(push=True):
    """Stage all changes, commit if there are diffs, and optionally push."""
    os.chdir(SCRIPT_DIR)

    subprocess.run(["git", "add", "-A"], check=True)

    result = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        capture_output=True,
    )
    if result.returncode == 0:
        print("\nNo changes detected — docs are already up to date.")
        return

    subprocess.run(
        ["git", "commit", "-m", "Update Apple developer documentation"],
        check=True,
    )

    if push:
        print("\nPushing to remote...")
        subprocess.run(["git", "push"], check=True)
        print("Pushed.")
    else:
        print("\nCommitted locally (--no-push).")


def main():
    parser = argparse.ArgumentParser(
        description="Fetch Apple Developer docs and convert to Markdown.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
examples:
  ./update.py                       # default: depth 2, swift + swiftui
  ./update.py --depth 1             # articles only (shallow)
  ./update.py --depth 3             # include nested types and conformances
  ./update.py --depth 0             # just the root index pages
  ./update.py --targets swift       # only fetch Swift docs
  ./update.py --no-push             # commit but don't push
  ./update.py --no-commit           # just fetch, no git operations
  ./update.py --full                # ignore ETags, re-fetch everything
  ./update.py --delete              # auto-delete stale files
""",
    )
    parser.add_argument(
        "--depth", type=int, default=2,
        help="How deep to crawl the doc tree (default: 2). "
             "0=root only, 1=articles, 2=articles+type overviews, "
             "3+=include members",
    )
    parser.add_argument(
        "--targets", nargs="+", default=["swift", "swiftui"],
        help="Which frameworks to fetch (default: swift swiftui)",
    )
    parser.add_argument(
        "--no-push", action="store_true",
        help="Commit but don't push to remote",
    )
    parser.add_argument(
        "--no-commit", action="store_true",
        help="Just fetch docs, skip git commit and push",
    )
    parser.add_argument(
        "--full", action="store_true",
        help="Ignore cached ETags and re-fetch everything",
    )
    parser.add_argument(
        "--delete", action="store_true",
        help="Delete local .md files for pages no longer in the doc tree "
             "(default: warn only)",
    )
    args = parser.parse_args()

    # Load or reset ETags
    if args.full:
        etags = {}
    else:
        etags = load_etags()

    print("=" * 60)
    print("Apple Developer Documentation -> Markdown")
    print(f"  Targets: {', '.join(args.targets)}")
    print(f"  Depth:   {args.depth}")
    print(f"  Mode:    {'full refresh' if args.full else 'incremental (ETag)'}")
    print("=" * 60)

    for target in args.targets:
        print(f"\n{'='*60}")
        print(f"Crawling: {target} (depth={args.depth})")
        print(f"{'='*60}")
        updated, skipped, errors, deleted, stale = crawl_and_convert(
            f"/documentation/{target}", target,
            max_depth=args.depth, etags=etags, delete=args.delete,
        )
        summary = (f"  {target}: {updated} updated, {skipped} unchanged, "
                   f"{errors} errors")
        if stale:
            summary += f", {stale} stale"
            if args.delete:
                summary += " (deleted)"
        print(f"\n{summary}")

    # Always save ETags (even if we don't commit)
    save_etags(etags)

    if not args.no_commit:
        git_commit_and_push(push=not args.no_push)

    print(f"\nAll documentation saved to: {SCRIPT_DIR}")


if __name__ == "__main__":
    main()
