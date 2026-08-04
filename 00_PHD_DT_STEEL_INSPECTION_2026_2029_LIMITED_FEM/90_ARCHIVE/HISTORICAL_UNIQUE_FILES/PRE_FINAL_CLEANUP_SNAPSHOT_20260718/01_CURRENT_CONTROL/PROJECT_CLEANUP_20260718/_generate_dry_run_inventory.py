from __future__ import annotations

import csv
import hashlib
import os
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
EXCLUDED_TOP_LEVEL = {"01_CURRENT_CONTROL"}

GOVERNANCE_FILES = {
    "CLAUDE.md",
    "MASTER_RESEARCH_CHARTER.md",
    "MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md",
    "RESEARCH_DIRECTION_AND_SCOPE.md",
    "RESEARCH_ARCHITECTURE.md",
    "RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md",
    "THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md",
}

SPECIAL_TOPIC_FILES = {
    "CHUYEN_DE_TONG_QUAN_EVIDENCE_GAPS_v1.md",
    "EVIDENCE_MATRIX_CHUYEN_DE_TONG_QUAN_v1.csv",
    "MATRIX_CHUYEN_DE_RQ_WP_PAPER_GATE_v1.md",
    "OUTLINE_CHUYEN_DE_TONG_QUAN_CHI_TIET_v1.md",
}

TEXT_EXTENSIONS = {".md", ".csv", ".txt", ".json", ".yaml", ".yml", ".py"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def read_header(path: Path) -> str:
    if path.suffix.lower() not in TEXT_EXTENSIONS:
        return ""
    try:
        return path.read_text(encoding="utf-8", errors="replace")[:20000]
    except OSError:
        return ""


def detect_version(name: str, header: str) -> str:
    matches = re.findall(r"(?i)(?:version\s*[:=]?\s*)?(v\d+(?:\.\d+)*)", name + "\n" + header[:3000])
    return matches[0] if matches else "UNVERSIONED"


def detect_status(path: Path, header: str) -> str:
    relative_parts = path.relative_to(ROOT).parts
    if "SUPERSEDED" in path.name.upper():
        return "SUPERSEDED"
    if relative_parts and relative_parts[0] == "BACKUP_BEFORE_WRITEBACK_20260718":
        return "BACKUP"
    if relative_parts and relative_parts[0] == "92_ARCHIVE_SUPERSEDED_FILES":
        return "HISTORICAL"
    haystack = (path.name + "\n" + header[:1200]).upper()
    if "KHÔNG PHẢI SOURCE OF TRUTH" in haystack or "NOT SOURCE OF TRUTH" in haystack:
        return "HISTORICAL"
    checks = (
        ("CURRENT_APPROVED", "CURRENT_APPROVED"),
        ("CURRENT_CANDIDATE", "CURRENT_CANDIDATE"),
        ("SOURCE OF TRUTH", "CURRENT_APPROVED"),
        ("STATUS:** ACCEPTED", "CURRENT_APPROVED"),
        ("STATUS: ACCEPTED", "CURRENT_APPROVED"),
        ("VỊ THẾ:** FILE ĐỊNH HƯỚNG HỌC THUẬT CAO NHẤT", "CURRENT_APPROVED"),
        ("STATUS:** NEW EVIDENCE UPDATE", "TRANSITIONAL"),
        ("SUPERSEDED", "SUPERSEDED"),
        ("HISTORICAL", "HISTORICAL"),
        ("TRANSITIONAL", "TRANSITIONAL"),
        ("BACKUP", "BACKUP"),
        ("DRAFT", "DRAFT"),
        ("TEMPORARY", "TEMPORARY"),
        ("PARTIAL", "PARTIAL"),
    )
    for token, status in checks:
        if token in haystack:
            return status
    if path.suffix.lower() in {".docx", ".pdf"}:
        return "BINARY_REVIEW"
    return "UNDECLARED"


def destination(relative: Path, filename: str, detected_status: str) -> tuple[str, str, str, str]:
    parts = relative.parts
    top = parts[0]

    if len(parts) == 1:
        if filename == "00_README_START_HERE.md":
            return "Governance navigation", "KEEP_SYSTEM", "Root entry point required by target structure", str(relative)
        if filename in GOVERNANCE_FILES:
            return "Governance", "MOVE_TO_DOMAIN_FOLDER", "Long-lived governance/source-of-truth file", str(Path("00_GOVERNANCE") / filename)
        if filename in {"CURRENT_STATUS_AND_NEXT_DIRECTION.md", "UNRESOLVED_ITEMS_AFTER_LIMITED_FEM_MIGRATION.md"}:
            return "Current control", "MOVE_TO_DOMAIN_FOLDER", "Current status/control record", str(Path("01_CURRENT_CONTROL") / filename)
        if filename == "LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md":
            return "Evidence current", "KEEP_CURRENT", "Current canonical base because no consolidated v1.3 exists", str(Path("02_EVIDENCE_BASE/CURRENT") / filename)
        if filename in SPECIAL_TOPIC_FILES:
            return "PhD special topic", "MOVE_TO_DOMAIN_FOLDER", "Current Chuyen de Tong quan candidate", str(Path("04_PHD_SPECIAL_TOPICS/CHUYEN_DE_TONG_QUAN") / filename)
        if filename == "PHASE0_SAFETY_BACKUP_AND_DRY_RUN_REPORT_20260718.md":
            return "Zotero audit", "MOVE_TO_DOMAIN_FOLDER", "Phase 0 Zotero audit report", str(Path("02_EVIDENCE_BASE/ZOTERO_AUDIT") / filename)
        if filename == "PROMPT_OPENCODE_PROJECT_CLEANUP_RESTRUCTURE_20260718.md":
            return "Prompt/handoff", "MOVE_TO_DOMAIN_FOLDER", "Operational OpenCode prompt", str(Path("07_PROMPTS_AND_HANDOFFS/OPENCODE") / filename)
        return "Unclassified root", "REVIEW_REQUIRED", "Unique root file with no deterministic rule", str(Path("99_TEMP_REVIEW/UNCLASSIFIED") / filename)

    if top == "Paper 1":
        if filename.startswith("PAPER1_GATE1_Q2_VERIFIED_EVIDENCE_REVISED"):
            sub = "CURRENT_MANUSCRIPT"
        elif "READINESS_REPORT" in filename or "CLAIM_EVIDENCE_AUDIT" in filename:
            sub = "GATE1_EVIDENCE"
        elif "DATA_ANALYSIS_REQUESTS_FOR_IT" in filename:
            sub = "IT_REQUESTS"
        elif "VERIFIED_REFERENCE_AUDIT" in filename:
            sub = "REFERENCE_AUDIT"
        elif "MAJOR_REVISION_LOG" in filename:
            sub = "REVISION_HISTORY"
        elif filename.startswith("PROMPT_"):
            return "Prompt/handoff", "MOVE_TO_DOMAIN_FOLDER", "Paper 1 control-room prompt", str(Path("07_PROMPTS_AND_HANDOFFS/OPENCODE/PAPER1") / filename)
        elif path_suffix(filename) == ".docx":
            return "Paper 1 binary review", "REVIEW_REQUIRED", "v3/v4/v6 chronology is not enough to establish supersession", str(Path("99_TEMP_REVIEW/PAPER1_DOCX_VERSION_REVIEW") / filename)
        else:
            sub = "ARCHIVE"
        return "Paper 1", "MOVE_TO_DOMAIN_FOLDER", "Paper 1 controlled asset", str(Path("03_PAPERS/PAPER_1") / sub / filename)

    if top == "Zotero MCP":
        if filename.startswith("01_LIVING_EVIDENCE_BASE"):
            sub = "CURRENT"
            reason = "Transitional v1.2 retained beside current v1.1 pending consolidation"
        elif filename.startswith("03_RQ1"):
            sub = "RQ1_GATE1"
            reason = "RQ1/Gate 1 evidence addendum"
        elif filename.startswith("04_RQ2") or filename.startswith("07_CLOSEST"):
            sub = "RQ2_GATES2_3"
            reason = "RQ2/Gates 2-3 evidence or competitor control"
        elif filename.startswith("05_RQ3"):
            sub = "RQ3_GATE4"
            reason = "RQ3/Gate 4 evidence addendum"
        elif filename.startswith("06_WP4"):
            sub = "WP4_GATE5"
            reason = "WP4/Gate 5 evidence addendum"
        else:
            sub = "ZOTERO_AUDIT"
            reason = "Zotero evidence matrix, audit, report, or writeback queue"
        return "Evidence base", "MOVE_TO_DOMAIN_FOLDER", reason, str(Path("02_EVIDENCE_BASE") / sub / filename)

    if top == "Perplexity_Pro":
        remainder = Path(*parts[1:])
        return "Literature discovery", "MOVE_TO_DOMAIN_FOLDER", "DISCOVERY_SOURCE_ONLY; NOT_CITABLE_EVIDENCE", str(Path("06_LITERATURE_AND_ZOTERO/PERPLEXITY_PRO") / remainder)

    if top == "BACKUP_BEFORE_WRITEBACK_20260718":
        remainder = Path(*parts[1:])
        return "Backup", "MOVE_TO_DOMAIN_FOLDER", "Backup must remain intact; no content modification", str(Path("90_BACKUP/BACKUP_BEFORE_WRITEBACK_20260718") / remainder)

    if top == "07_FABLE_LEGACY_PACK_20260718":
        remainder = Path(*parts[1:])
        return "Legacy handoff", "ARCHIVE_LEGACY", "Fable legacy pack; historical operational reference", str(Path("92_ARCHIVE_SUPERSEDED_FILES/LEGACY_PACKS/07_FABLE_LEGACY_PACK_20260718") / remainder)

    if top == "92_ARCHIVE_SUPERSEDED_FILES":
        if "CHARTER" in filename.upper():
            sub = "GOVERNANCE_OLD"
        elif "MATRIX" in filename.upper() or "EVIDENCE" in filename.upper():
            sub = "EVIDENCE_OLD"
        else:
            sub = "EVIDENCE_OLD"
        return "Existing archive", "ARCHIVE_SUPERSEDED", "Already archived; place in structured archive subfolder", str(Path("92_ARCHIVE_SUPERSEDED_FILES") / sub / filename)

    return "Unclassified", "REVIEW_REQUIRED", "No deterministic classification rule", str(Path("99_TEMP_REVIEW/UNCLASSIFIED") / relative)


def path_suffix(filename: str) -> str:
    return Path(filename).suffix.lower()


def iter_source_files() -> list[Path]:
    files: list[Path] = []
    for current, dirs, names in os.walk(ROOT):
        current_path = Path(current)
        relative_dir = current_path.relative_to(ROOT)
        if relative_dir.parts and relative_dir.parts[0] in EXCLUDED_TOP_LEVEL:
            dirs[:] = []
            continue
        dirs[:] = [name for name in dirs if name not in EXCLUDED_TOP_LEVEL and name != ".git"]
        for name in names:
            files.append(current_path / name)
    return sorted(files, key=lambda p: str(p.relative_to(ROOT)).lower())


def write_inventory(rows: list[dict[str, str]]) -> None:
    fields = [
        "Original_Path",
        "Filename",
        "Extension",
        "Size",
        "Modified_Date",
        "Checksum",
        "Detected_Version",
        "Detected_Status",
        "Domain",
        "Decision",
        "Reason",
        "Destination_Path",
        "Link_Update_Required",
    ]
    with (OUT / "PROJECT_FILE_INVENTORY_BEFORE_CLEANUP_20260718.csv").open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_migration_manifest(rows: list[dict[str, str]]) -> None:
    fields = [
        "Original_Path",
        "Destination_Path",
        "Decision",
        "Checksum",
        "Detected_Status",
        "Reason",
        "Precondition",
        "Execution_Status",
    ]
    with (OUT / "PROJECT_FILE_MIGRATION_MANIFEST_20260718.csv").open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            precondition = "MANIFEST_REVIEW"
            if row["Decision"] == "REVIEW_REQUIRED":
                precondition = "USER_DECISION_REQUIRED"
            elif row["Domain"] == "Backup":
                precondition = "VERIFY_BACKUP_INTEGRITY"
            writer.writerow(
                {
                    "Original_Path": row["Original_Path"],
                    "Destination_Path": row["Destination_Path"],
                    "Decision": row["Decision"],
                    "Checksum": row["Checksum"],
                    "Detected_Status": row["Detected_Status"],
                    "Reason": row["Reason"],
                    "Precondition": precondition,
                    "Execution_Status": "DRY_RUN_NOT_EXECUTED",
                }
            )


def write_deletion_manifest(rows: list[dict[str, str]]) -> None:
    by_checksum: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_checksum[row["Checksum"]].append(row)
    fields = [
        "Checksum",
        "Canonical_Candidate",
        "Duplicate_Candidate",
        "Size",
        "Decision",
        "Reason",
        "Deletion_Status",
    ]
    with (OUT / "VERIFIED_DUPLICATE_DELETION_MANIFEST_20260718.csv").open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for checksum, group in sorted(by_checksum.items()):
            if len(group) < 2:
                continue
            non_backup = [row for row in group if not row["Original_Path"].startswith("BACKUP_BEFORE_WRITEBACK_20260718")]
            canonical = non_backup[0] if non_backup else group[0]
            for duplicate in group:
                if duplicate is canonical:
                    continue
                involves_backup = duplicate["Original_Path"].startswith("BACKUP_BEFORE_WRITEBACK_20260718") or canonical["Original_Path"].startswith("BACKUP_BEFORE_WRITEBACK_20260718")
                decision = "KEEP_BACKUP_COPY" if involves_backup else "DUPLICATE_PENDING_DELETE"
                reason = "Checksum-identical backup is protected" if involves_backup else "Checksum-identical but links/canonical role require review"
                writer.writerow(
                    {
                        "Checksum": checksum,
                        "Canonical_Candidate": canonical["Original_Path"],
                        "Duplicate_Candidate": duplicate["Original_Path"],
                        "Size": duplicate["Size"],
                        "Decision": decision,
                        "Reason": reason,
                        "Deletion_Status": "NOT_DELETED",
                    }
                )


def main() -> None:
    rows: list[dict[str, str]] = []
    for path in iter_source_files():
        relative = path.relative_to(ROOT)
        header = read_header(path)
        status = detect_status(path, header)
        domain, decision, reason, target = destination(relative, path.name, status)
        rows.append(
            {
                "Original_Path": str(relative),
                "Filename": path.name,
                "Extension": path.suffix.lower(),
                "Size": str(path.stat().st_size),
                "Modified_Date": datetime.fromtimestamp(path.stat().st_mtime).isoformat(timespec="seconds"),
                "Checksum": sha256(path),
                "Detected_Version": detect_version(path.name, header),
                "Detected_Status": status,
                "Domain": domain,
                "Decision": decision,
                "Reason": reason,
                "Destination_Path": target,
                "Link_Update_Required": "NO" if str(relative) == target else "YES",
            }
        )
    write_inventory(rows)
    write_migration_manifest(rows)
    write_deletion_manifest(rows)
    print(f"inventory_rows={len(rows)}")
    print(f"review_required={sum(row['Decision'] == 'REVIEW_REQUIRED' for row in rows)}")
    print(f"move_or_archive={sum(row['Decision'] in {'MOVE_TO_DOMAIN_FOLDER', 'ARCHIVE_LEGACY', 'ARCHIVE_SUPERSEDED'} for row in rows)}")


if __name__ == "__main__":
    main()
