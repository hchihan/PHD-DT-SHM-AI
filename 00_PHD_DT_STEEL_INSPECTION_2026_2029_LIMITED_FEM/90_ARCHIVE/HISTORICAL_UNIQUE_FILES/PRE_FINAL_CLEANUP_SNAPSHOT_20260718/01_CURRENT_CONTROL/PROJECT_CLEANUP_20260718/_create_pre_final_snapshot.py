from __future__ import annotations

import csv
import hashlib
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SNAPSHOT = ROOT / "90_BACKUP" / "PRE_FINAL_CLEANUP_SNAPSHOT_20260718"


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest().upper()


def source_files() -> list[Path]:
    result = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        try:
            path.relative_to(SNAPSHOT)
            continue
        except ValueError:
            result.append(path)
    return sorted(result, key=lambda item: str(item.relative_to(ROOT)).lower())


def main() -> None:
    SNAPSHOT.mkdir(parents=True, exist_ok=True)
    rows = []
    for source in source_files():
        relative = source.relative_to(ROOT)
        target = SNAPSHOT / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        source_hash = digest(source)
        target_hash = digest(target)
        if source_hash != target_hash:
            raise RuntimeError(f"Snapshot checksum mismatch: {relative}")
        rows.append(
            {
                "Original_Path": str(relative),
                "Snapshot_Path": str(target.relative_to(ROOT)),
                "Size": source.stat().st_size,
                "Modified_Date": datetime.fromtimestamp(source.stat().st_mtime).isoformat(timespec="seconds"),
                "SHA256": source_hash,
                "Verification": "MATCH",
            }
        )
    manifest = SNAPSHOT / "SNAPSHOT_CHECKSUM_MANIFEST_20260718.csv"
    with manifest.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"snapshot_files={len(rows)}")
    print(f"snapshot_bytes={sum(int(row['Size']) for row in rows)}")
    print(f"verification_failures={sum(row['Verification'] != 'MATCH' for row in rows)}")


if __name__ == "__main__":
    main()
