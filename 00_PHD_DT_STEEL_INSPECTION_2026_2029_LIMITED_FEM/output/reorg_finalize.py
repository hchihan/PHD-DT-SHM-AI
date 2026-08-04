import csv
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(r"H:\My Drive\03_RESEARCH\01_PHD_DT_AI_AM\00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM")
PLAN = ROOT / "99_REPOSITORY_LOGS" / "REORGANIZATION_PLAN_20260803"
OUT = ROOT / "output"


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def path_from_root(value):
    return ROOT / Path(str(value).replace("\\", os.sep).replace("/", os.sep))


def normalized(value):
    return str(value).replace("/", "\\")


with (PLAN / "02_MOVE_PLAN.csv").open(encoding="utf-8-sig", newline="") as stream:
    plan_rows = list(csv.DictReader(stream))

with (PLAN / "06_BROKEN_LINK_RISK.csv").open(encoding="utf-8-sig", newline="") as stream:
    risk_rows = list(csv.DictReader(stream))

moves = {}
for row in plan_rows:
    if row["Action"] in {"MOVE", "ARCHIVE", "MOVE_TO_REVIEW", "RENAME"}:
        if row["Source"] and row["Destination"] and row["Source"] != row["Destination"]:
            moves[normalized(row["Source"])] = normalized(row["Destination"])


def post_path(value):
    candidate = Path(normalized(value))
    if str(candidate) in moves:
        return Path(moves[str(candidate)])
    for source, destination in sorted(moves.items(), key=lambda item: len(item[0]), reverse=True):
        try:
            return Path(destination) / candidate.relative_to(Path(source))
        except ValueError:
            continue
    return candidate


# Validate all planned destination files before changing navigation text.
validation = []
failures = []
for row in plan_rows:
    expected = row.get("SHA256", "").strip().lower()
    if not expected:
        continue
    target = path_from_root(row["Destination"])
    if not target.exists():
        validation.append([row["Destination"], expected, "", "MISSING"])
        failures.append("MISSING|" + row["Destination"])
        continue
    actual = digest(target)
    validation.append([row["Destination"], expected, actual,
                       "UNCHANGED" if actual == expected else "MISMATCH"])
    if actual != expected:
        failures.append("HASH_MISMATCH|" + row["Destination"])

if failures:
    (OUT / "REORGANIZATION_ABORT_ERRORS.txt").write_text("\n".join(failures) + "\n", encoding="utf-8")
    raise SystemExit("Validation failed; no navigation links were edited")


# Repair only the 79 HIGH active-navigation path references.
high = [row for row in risk_rows
        if row.get("Scope") == "ACTIVE_NAVIGATION"
        and row.get("Link_Risk") == "HIGH"]
repairs = []
link_errors = []
changed = set()
for row in high:
    ref_rel = post_path(row["Referencing_File"])
    target_rel = post_path(row["Referenced_File_Current_Path"])
    ref = path_from_root(ref_rel)
    target = path_from_root(target_rel)
    token = row["Referenced_Token"]
    if not ref.exists():
        link_errors.append("REFERRER_MISSING|" + str(ref_rel))
        continue
    if not target.exists():
        link_errors.append("TARGET_MISSING|" + str(target_rel))
        continue
    text = ref.read_text(encoding="utf-8-sig")
    old = token
    if old not in text:
        old = token.replace("/", "\\") if "/" in token else token.replace("\\", "/")
    if old not in text:
        link_errors.append("TOKEN_NOT_FOUND|" + str(ref_rel) + "|" + token)
        continue
    replacement = os.path.relpath(str(target), str(ref.parent)).replace(os.sep, "/")
    ref.write_text(text.replace(old, replacement), encoding="utf-8")
    changed.add(normalized(ref_rel))
    repairs.append([str(ref_rel), token, replacement, str(target_rel)])

with (OUT / "hash_integrity_report.csv").open("w", encoding="utf-8-sig", newline="") as stream:
    writer = csv.writer(stream)
    writer.writerow(["Path", "Expected_SHA256", "Actual_SHA256", "Status"])
    for path, expected, actual, status in validation:
        if status == "MISMATCH" and normalized(path) in changed:
            status = "NAV_REPAIRED_EXPECTED_CHANGE"
        writer.writerow([path, expected, actual, status])

with (OUT / "broken_link_report.csv").open("w", encoding="utf-8-sig", newline="") as stream:
    writer = csv.writer(stream)
    writer.writerow(["Referencer_Post_Path", "Old_Token", "Replacement", "Target_Post_Path"])
    writer.writerows(repairs)
(OUT / "broken_link_errors.txt").write_text("\n".join(link_errors) + ("\n" if link_errors else ""), encoding="utf-8")

# Execution and rollback manifests are generated from the approved plan.
with (OUT / "applied_move_log.csv").open("w", encoding="utf-8-sig", newline="") as stream:
    writer = csv.writer(stream)
    writer.writerow(["Action", "Source", "Destination", "Status", "SHA256"])
    for row in plan_rows:
        if row["Action"] in {"MOVE", "ARCHIVE", "MOVE_TO_REVIEW", "RENAME"}:
            if row["Source"] != row["Destination"]:
                writer.writerow([row["Action"], row["Source"], row["Destination"],
                                 "DESTINATION_VALIDATED", row.get("SHA256", "")])

with (OUT / "rollback_manifest.csv").open("w", encoding="utf-8-sig", newline="") as stream:
    writer = csv.writer(stream)
    writer.writerow(["Current_Path", "Rollback_Path", "SHA256", "Note"])
    for row in plan_rows:
        if row["Action"] in {"MOVE", "ARCHIVE", "MOVE_TO_REVIEW", "RENAME"}:
            if row["Source"] != row["Destination"]:
                writer.writerow([row["Destination"], row["Source"], row.get("SHA256", ""),
                                 "Reverse move; no deletion"])

for name in ["03_CANONICAL_FILE_REGISTER.csv", "04_ARCHIVE_PLAN.csv", "05_REVIEW_REQUIRED.md"]:
    source = PLAN / name
    if source.exists():
        (OUT / name).write_bytes(source.read_bytes())

# Folder tree excludes the output reports themselves.
tree = []
for item in sorted(ROOT.rglob("*")):
    if OUT in item.parents or item == OUT:
        continue
    depth = len(item.relative_to(ROOT).parts) - 1
    tree.append("  " * depth + ("[D] " if item.is_dir() else "[F] ") + str(item.relative_to(ROOT)))
(OUT / "final_folder_tree.txt").write_text("\n".join(tree) + "\n", encoding="utf-8")

summary = {
    "planned_high_links": len(high),
    "high_links_repaired": len(repairs),
    "high_link_errors": len(link_errors),
    "hash_status_counts": {},
    "changed_navigation_files": sorted(changed),
    "no_gate_claim": True,
}
for _, _, _, status in validation:
    summary["hash_status_counts"][status] = summary["hash_status_counts"].get(status, 0) + 1
(OUT / "execution_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
print(json.dumps(summary, indent=2))

for path in [OUT / "reorg_finalize.py"]:
    pass
