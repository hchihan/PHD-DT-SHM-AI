#!/usr/bin/env python3
"""Run MinerU safely and record a conversion manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_pdf", type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--backend", default="pipeline")
    args = parser.parse_args()

    source = args.input_pdf.expanduser().resolve()
    output = args.output_dir.expanduser().resolve()
    if not source.is_file() or source.suffix.lower() != ".pdf":
        parser.error("input_pdf must be an existing PDF file")

    mineru = shutil.which("mineru")
    if not mineru:
        print(
            "MinerU CLI is unavailable. Follow the official MinerU installation "
            "instructions or provide an existing Markdown/JSON extraction.",
            file=sys.stderr,
        )
        return 2

    output.mkdir(parents=True, exist_ok=True)
    command = [mineru, "-p", str(source), "-o", str(output), "-b", args.backend]
    completed = subprocess.run(command, check=False)
    if completed.returncode:
        return completed.returncode

    files = sorted(path for path in output.rglob("*") if path.is_file())
    markdown = [str(path.relative_to(output)) for path in files if path.suffix.lower() == ".md"]
    json_files = [str(path.relative_to(output)) for path in files if path.suffix.lower() == ".json"]
    manifest = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "input_pdf": str(source),
        "input_sha256": sha256(source),
        "converter": "MinerU",
        "backend": args.backend,
        "command": command,
        "markdown_files": markdown,
        "json_files": json_files,
        "quality_status": "UNVERIFIED_AGAINST_PDF",
    }
    manifest_path = output / "conversion_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(manifest_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

