#!/usr/bin/env python3
"""Index headings and limitation/future-work signals in converted Markdown."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


GROUPS = {
    "limitations": [
        r"\blimit(?:ation|ations|ed)\b",
        r"\bconstraint(?:s)?\b",
        r"\bshortcoming(?:s)?\b",
        r"threat(?:s)? to validity",
        r"\bnot considered\b",
    ],
    "future_work": [
        r"future work",
        r"further research",
        r"future research",
        r"should investigate",
        r"could be explored",
        r"remains to be",
    ],
    "transfer_validation": [
        r"generaliz",
        r"external valid",
        r"single case",
        r"small sample",
        r"laboratory",
        r"field validation",
        r"data leakage",
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    source = args.markdown.expanduser().resolve()
    if not source.is_file():
        parser.error("markdown must be an existing file")
    text = source.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    headings = []
    hits = {name: [] for name in GROUPS}
    for number, line in enumerate(lines, start=1):
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if heading:
            headings.append({"line": number, "level": len(heading.group(1)), "text": heading.group(2)})
        for group, patterns in GROUPS.items():
            if any(re.search(pattern, line, flags=re.IGNORECASE) for pattern in patterns):
                hits[group].append({"line": number, "text": line[:500]})

    payload = {
        "markdown": str(source),
        "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "line_count": len(lines),
        "headings": headings,
        "keyword_hits": hits,
        "warning": "Keyword hits are navigation aids, not verified author-stated limitations.",
    }
    destination = args.output.expanduser().resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
