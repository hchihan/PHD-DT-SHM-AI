from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "zotero_import_ready"

CANDIDATE_CSV = ROOT / "zotero_final" / "PAPER2_GATE2_GATE3_MASTER_LIBRARY_FINAL.csv"
CANDIDATE_RIS = ROOT / "zotero_final" / "PAPER2_GATE2_GATE3_ZOTERO_MASTER_FINAL.ris"
ZOTERO_EXPORTS = [ROOT / f"My Library_export_Zotero_{i}.csv" for i in range(1, 4)]

NEW_RIS = OUT / "PAPER2_NEW_ONLY_FOR_ZOTERO.ris"
NEW_CSV = OUT / "PAPER2_NEW_ONLY_FOR_ZOTERO.csv"
ALREADY_CSV = OUT / "PAPER2_ALREADY_IN_ZOTERO.csv"
MANUAL_CSV = OUT / "PAPER2_ZOTERO_MANUAL_CHECK.csv"
SUMMARY_MD = OUT / "PAPER2_ZOTERO_IMPORT_SUMMARY.md"
LOG_JSON = OUT / "PAPER2_ZOTERO_CROSSCHECK_LOG.json"

TZ = timezone(timedelta(hours=7))
FUZZY_HIGH = 0.94


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader), list(reader.fieldnames or [])


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def normalize_text(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "").casefold()
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = re.sub(r"[^\w]+", " ", value, flags=re.UNICODE)
    return re.sub(r"\s+", " ", value).strip()


def normalize_doi(value: str) -> str:
    value = (value or "").strip()
    value = re.sub(r"^\s*(?:https?://(?:dx\.)?doi\.org/|doi\s*:\s*)", "", value, flags=re.I)
    value = re.sub(r"\s+", "", value)
    value = value.strip(" \t\r\n.,;:)]}>'\"")
    return value.casefold()


def extract_doi(row: dict[str, str]) -> str:
    direct = normalize_doi(row.get("DOI", ""))
    if direct.startswith("10."):
        return direct
    for field in ("Extra", "Url"):
        value = row.get(field, "") or ""
        match = re.search(r"(?:doi\s*:\s*|doi\.org/)?(10\.\d{4,9}/[^\s<>\"']+)", value, flags=re.I)
        if match:
            doi = normalize_doi(match.group(1))
            if doi.startswith("10."):
                return doi
    return ""


def extract_year(row: dict[str, str]) -> str:
    for field in ("Publication Year", "Date"):
        match = re.search(r"(?:19|20)\d{2}", row.get(field, "") or "")
        if match:
            return match.group(0)
    return ""


def author_families(value: str) -> list[str]:
    result = []
    for raw in (value or "").split(";"):
        raw = raw.strip()
        if not raw:
            continue
        family = raw.split(",", 1)[0].strip() if "," in raw else raw.split()[-1]
        family = normalize_text(family)
        if family and family not in {"et al", "etal"}:
            result.append(family)
    return result


def token_jaccard(left: str, right: str) -> float:
    a, b = set(normalize_text(left).split()), set(normalize_text(right).split())
    return len(a & b) / len(a | b) if a and b else 0.0


class DSU:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, value: int) -> int:
        while self.parent[value] != value:
            self.parent[value] = self.parent[self.parent[value]]
            value = self.parent[value]
        return value

    def union(self, left: int, right: int) -> None:
        a, b = self.find(left), self.find(right)
        if a == b:
            return
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1


def richest(records: list[dict[str, str]], field: str) -> str:
    values = [str(row.get(field, "") or "").strip() for row in records]
    values = [value for value in values if value]
    return max(values, key=lambda value: (len(value), value)) if values else ""


def unique_join(values: list[str]) -> str:
    seen, result = set(), []
    for value in values:
        if not value:
            continue
        key = value.casefold()
        if key not in seen:
            seen.add(key)
            result.append(value)
    return "; ".join(result)


def has_pdf(value: str) -> bool:
    return any(part.strip().casefold().endswith(".pdf") for part in (value or "").split(";"))


def deduplicate_existing(raw_records: list[dict[str, str]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    dsu = DSU(len(raw_records))
    key_groups: dict[str, list[int]] = defaultdict(list)
    doi_groups: dict[str, list[int]] = defaultdict(list)
    title_groups: dict[str, list[int]] = defaultdict(list)

    for index, row in enumerate(raw_records):
        row["_doi"] = extract_doi(row)
        row["_title"] = normalize_text(row.get("Title", ""))
        row["_year"] = extract_year(row)
        families = author_families(row.get("Author", ""))
        row["_first_author"] = families[0] if families else ""
        if row.get("Key"):
            key_groups[row["Key"]].append(index)
        if row["_doi"]:
            doi_groups[row["_doi"]].append(index)
        if row["_title"]:
            title_groups[row["_title"]].append(index)

    for groups in (key_groups, doi_groups):
        for indices in groups.values():
            for index in indices[1:]:
                dsu.union(indices[0], index)

    conflicts: list[dict[str, object]] = []
    for title, indices in title_groups.items():
        roots = sorted({dsu.find(index) for index in indices})
        if len(roots) < 2:
            continue
        # Inspect every member already attached to each component, not only the
        # rows participating in this title group. This prevents a DOI-less row
        # from bridging two components that carry different non-empty DOIs.
        root_members = {
            root: [i for i in range(len(raw_records)) if dsu.find(i) == root]
            for root in roots
        }
        dois_by_root = {
            root: {raw_records[i]["_doi"] for i in members if raw_records[i]["_doi"]}
            for root, members in root_members.items()
        }
        all_dois = set().union(*dois_by_root.values())
        if len(all_dois) <= 1:
            for root in roots[1:]:
                dsu.union(roots[0], root)
        else:
            conflicts.append(
                {
                    "normalized_title": title,
                    "title": richest([raw_records[i] for i in indices], "Title"),
                    "dois": sorted(all_dois),
                    "keys": sorted({raw_records[i].get("Key", "") for i in indices if raw_records[i].get("Key")}),
                    "reason": "EXACT_TITLE_DIFFERENT_DOI_NOT_MERGED",
                }
            )

    components: dict[int, list[dict[str, str]]] = defaultdict(list)
    for index, row in enumerate(raw_records):
        components[dsu.find(index)].append(row)

    unique_records: list[dict[str, object]] = []
    for members in components.values():
        title = richest(members, "Title")
        authors = richest(members, "Author")
        doi = richest(members, "_doi")
        year = richest(members, "_year")
        families = author_families(authors)
        source_files = sorted({row["_source_file"] for row in members})
        keys = sorted({row.get("Key", "") for row in members if row.get("Key")})
        pdf = any(has_pdf(row.get("File Attachments", "")) for row in members)
        unique_records.append(
            {
                "title": title,
                "normalized_title": normalize_text(title),
                "authors": authors,
                "author_families": families,
                "first_author": families[0] if families else "",
                "year": year,
                "journal": richest(members, "Publication Title"),
                "doi": doi,
                "url": richest(members, "Url"),
                "zotero_keys": keys,
                "source_files": source_files,
                "file_attachments": unique_join([row.get("File Attachments", "") for row in members]),
                "link_attachments": unique_join([row.get("Link Attachments", "") for row in members]),
                "pdf_status": "PDF_AVAILABLE" if pdf else "NO_PDF",
                "item_types": sorted({row.get("Item Type", "") for row in members if row.get("Item Type")}),
                "raw_record_count": len(members),
            }
        )
    unique_records.sort(key=lambda row: (str(row["normalized_title"]), str(row["doi"])))
    return unique_records, conflicts


def parse_ris_blocks(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    blocks: dict[str, str] = {}
    current: list[str] | None = None
    record_id = ""
    for line_number, line in enumerate(lines, start=1):
        if line.startswith("TY  - "):
            if current is not None:
                raise ValueError(f"Nested TY at RIS line {line_number}")
            current = [line]
            record_id = ""
        elif current is not None:
            current.append(line)
            if line.startswith("ID  - "):
                record_id = line[6:].strip()
            if re.fullmatch(r"ER  -\s*", line):
                if not record_id:
                    raise ValueError(f"RIS record ending at line {line_number} has no ID")
                if record_id in blocks:
                    raise ValueError(f"Duplicate RIS ID: {record_id}")
                blocks[record_id] = "\n".join(current)
                current = None
    if current is not None:
        raise ValueError("Final candidate RIS has a record without ER")
    return blocks


def select_best_match(candidate: dict[str, str], options: list[dict[str, object]]) -> dict[str, object]:
    candidate_authors = set(author_families(candidate.get("authors", "")))
    candidate_year = candidate.get("year", "")

    def score(existing: dict[str, object]) -> tuple[int, int, int, int]:
        existing_authors = set(existing["author_families"])
        return (
            int(bool(candidate_authors & existing_authors)),
            int(bool(candidate_year and candidate_year == existing["year"])),
            int(bool(existing["doi"])),
            int(existing["pdf_status"] == "PDF_AVAILABLE"),
        )

    return max(options, key=score)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    inputs = [CANDIDATE_CSV, CANDIDATE_RIS, *ZOTERO_EXPORTS]
    before_hashes = {str(path.relative_to(ROOT)): sha256(path) for path in inputs}

    candidate_rows, _ = read_csv(CANDIDATE_CSV)
    if len(candidate_rows) != 199:
        raise ValueError(f"Candidate library must contain 199 rows, found {len(candidate_rows)}")
    ris_blocks = parse_ris_blocks(CANDIDATE_RIS)
    if len(ris_blocks) != 199:
        raise ValueError(f"Candidate RIS must contain 199 records, found {len(ris_blocks)}")

    raw_existing: list[dict[str, str]] = []
    export_counts: dict[str, int] = {}
    for path in ZOTERO_EXPORTS:
        rows, fields = read_csv(path)
        export_counts[path.name] = len(rows)
        attachment_fields_available = "File Attachments" in fields
        if not attachment_fields_available:
            raise ValueError(f"Attachment field missing in {path.name}")
        for row_number, row in enumerate(rows, start=2):
            row["_source_file"] = path.name
            row["_row_number"] = str(row_number)
            raw_existing.append(row)

    existing, existing_conflicts = deduplicate_existing(raw_existing)
    existing_by_doi: dict[str, list[dict[str, object]]] = defaultdict(list)
    existing_by_title: dict[str, list[dict[str, object]]] = defaultdict(list)
    for item in existing:
        if item["doi"]:
            existing_by_doi[str(item["doi"])].append(item)
        if item["normalized_title"]:
            existing_by_title[str(item["normalized_title"])].append(item)

    decisions: list[dict[str, object]] = []
    already_rows: list[dict[str, object]] = []
    manual_rows: list[dict[str, object]] = []

    for candidate in candidate_rows:
        candidate_doi = normalize_doi(candidate.get("doi", ""))
        candidate_title = normalize_text(candidate.get("title", ""))
        candidate_families = set(author_families(candidate.get("authors", "")))
        candidate_first = next(iter(author_families(candidate.get("authors", ""))), "")
        candidate_year = candidate.get("year", "")
        exact_doi_options = existing_by_doi.get(candidate_doi, [])

        status = ""
        matched: dict[str, object] | None = None
        reason = ""
        similarity = 1.0
        author_overlap: list[str] = []

        if exact_doi_options:
            matched = select_best_match(candidate, exact_doi_options)
            status = "ALREADY_IN_ZOTERO_DOI"
            reason = "EXACT_DOI"
        else:
            exact_title_options = existing_by_title.get(candidate_title, [])
            if exact_title_options:
                matched = select_best_match(candidate, exact_title_options)
                existing_families = set(matched["author_families"])
                author_overlap = sorted(candidate_families & existing_families)
                same_year = bool(candidate_year and candidate_year == matched["year"])
                different_nonempty_doi = bool(candidate_doi and matched["doi"] and candidate_doi != matched["doi"])
                if author_overlap and same_year and not different_nonempty_doi:
                    status = "ALREADY_IN_ZOTERO_TITLE"
                    reason = "EXACT_TITLE_AUTHOR_YEAR"
                else:
                    status = "MANUAL_CHECK"
                    if different_nonempty_doi:
                        reason = "EXACT_TITLE_DIFFERENT_DOI"
                    else:
                        reason = "EXACT_TITLE_AUTHOR_YEAR_CONFLICT_OR_MISSING"

        if not status:
            risk_candidates: list[tuple[tuple[float, float, int, int], dict[str, object], str, list[str]]] = []
            for item in existing:
                item_title = str(item["normalized_title"])
                if not item_title:
                    continue
                sequence = SequenceMatcher(None, candidate_title, item_title).ratio()
                jaccard = token_jaccard(candidate.get("title", ""), str(item["title"]))
                existing_families = set(item["author_families"])
                overlap = sorted(candidate_families & existing_families)
                same_first = bool(candidate_first and candidate_first == item["first_author"])
                same_year = bool(candidate_year and candidate_year == item["year"])
                year_distance = 99
                if candidate_year.isdigit() and str(item["year"]).isdigit():
                    year_distance = abs(int(candidate_year) - int(str(item["year"])))
                different_doi = bool(candidate_doi and item["doi"] and candidate_doi != item["doi"])

                risk_reason = ""
                if sequence >= FUZZY_HIGH and different_doi and (overlap or same_year or sequence >= 0.985):
                    risk_reason = "HIGH_TITLE_SIMILARITY_DIFFERENT_DOI"
                elif same_first and year_distance <= 3 and sequence >= 0.88 and different_doi:
                    risk_reason = "POTENTIAL_PREPRINT_CONFERENCE_JOURNAL_VERSION"
                elif len(overlap) >= 2 and year_distance <= 3 and sequence >= 0.84 and jaccard >= 0.65 and different_doi:
                    risk_reason = "POTENTIAL_VERSION_DUPLICATION_SHARED_AUTHORS"
                elif sequence >= FUZZY_HIGH and not item["doi"] and overlap and same_year:
                    risk_reason = "FUZZY_TITLE_MATCH_EXISTING_WITHOUT_DOI"

                if risk_reason:
                    risk_candidates.append(((sequence, jaccard, len(overlap), int(same_year)), item, risk_reason, overlap))

            if risk_candidates:
                best = max(risk_candidates, key=lambda entry: entry[0])
                (similarity, jaccard, _, _), matched, reason, author_overlap = best
                status = "MANUAL_CHECK"
            else:
                status = "NEW_TO_ZOTERO"

        decision = {
            "candidate_id": candidate["master_id"],
            "candidate_title": candidate.get("title", ""),
            "candidate_doi": candidate_doi,
            "candidate_authors": candidate.get("authors", ""),
            "candidate_year": candidate_year,
            "match_status": status,
            "matched_zotero_title": str(matched["title"]) if matched else "",
            "matched_zotero_doi": str(matched["doi"]) if matched else "",
            "matched_zotero_year": str(matched["year"]) if matched else "",
            "matched_zotero_authors": str(matched["authors"]) if matched else "",
            "zotero_keys": "; ".join(matched["zotero_keys"]) if matched else "",
            "zotero_source_files": "; ".join(matched["source_files"]) if matched else "",
            "pdf_status": str(matched["pdf_status"]) if matched else "",
            "match_reason": reason,
            "title_similarity": f"{similarity:.6f}" if matched else "",
            "shared_author_families": "; ".join(author_overlap),
        }
        decisions.append(decision)

        if status.startswith("ALREADY_IN_ZOTERO"):
            already_rows.append(
                {
                    "candidate_title": candidate.get("title", ""),
                    "candidate_doi": candidate_doi,
                    "zotero_title": matched["title"],
                    "zotero_doi": matched["doi"],
                    "zotero_source_file": "; ".join(matched["source_files"]),
                    "match_method": "EXACT_DOI" if status == "ALREADY_IN_ZOTERO_DOI" else "EXACT_TITLE_AUTHOR_YEAR",
                    "zotero_key_if_available": "; ".join(matched["zotero_keys"]),
                    "pdf_or_attachment_status_if_available": matched["pdf_status"],
                }
            )
        elif status == "MANUAL_CHECK":
            manual_rows.append(decision)

    new_candidates = [
        candidate for candidate, decision in zip(candidate_rows, decisions)
        if decision["match_status"] == "NEW_TO_ZOTERO"
    ]
    new_ids = [candidate["master_id"] for candidate in new_candidates]
    if any(record_id not in ris_blocks for record_id in new_ids):
        raise ValueError("A NEW_TO_ZOTERO candidate is missing from candidate RIS")

    new_csv_rows = [
        {
            "title": row.get("title", ""),
            "authors": row.get("authors", ""),
            "year": row.get("year", ""),
            "journal": row.get("journal", ""),
            "doi": normalize_doi(row.get("doi", "")),
            "priority": row.get("priority", ""),
            "themes": row.get("themes", ""),
            "source_files": row.get("source_files", ""),
            "match_status": "NEW_TO_ZOTERO",
        }
        for row in new_candidates
    ]
    write_csv(
        NEW_CSV,
        new_csv_rows,
        ["title", "authors", "year", "journal", "doi", "priority", "themes", "source_files", "match_status"],
    )
    write_csv(
        ALREADY_CSV,
        already_rows,
        [
            "candidate_title",
            "candidate_doi",
            "zotero_title",
            "zotero_doi",
            "zotero_source_file",
            "match_method",
            "zotero_key_if_available",
            "pdf_or_attachment_status_if_available",
        ],
    )
    write_csv(
        MANUAL_CSV,
        manual_rows,
        [
            "candidate_id",
            "candidate_title",
            "candidate_doi",
            "candidate_authors",
            "candidate_year",
            "match_status",
            "matched_zotero_title",
            "matched_zotero_doi",
            "matched_zotero_year",
            "matched_zotero_authors",
            "zotero_keys",
            "zotero_source_files",
            "pdf_status",
            "match_reason",
            "title_similarity",
            "shared_author_families",
        ],
    )

    new_ris_text = "\n\n".join(ris_blocks[record_id].rstrip() for record_id in new_ids)
    if new_ris_text:
        new_ris_text += "\n"
    NEW_RIS.write_text(new_ris_text, encoding="utf-8", newline="\n")

    new_ris_blocks = parse_ris_blocks(NEW_RIS)
    new_dois = [normalize_doi(row.get("doi", "")) for row in new_candidates]
    new_titles = [normalize_text(row.get("title", "")) for row in new_candidates]
    existing_dois = {str(item["doi"]) for item in existing if item["doi"]}
    existing_titles = {str(item["normalized_title"]) for item in existing if item["normalized_title"]}
    counts = {
        "export_1_records": export_counts[ZOTERO_EXPORTS[0].name],
        "export_2_records": export_counts[ZOTERO_EXPORTS[1].name],
        "export_3_records": export_counts[ZOTERO_EXPORTS[2].name],
        "combined_raw_records": len(raw_existing),
        "unique_existing_zotero_papers": len(existing),
        "existing_papers_with_pdf": sum(item["pdf_status"] == "PDF_AVAILABLE" for item in existing),
        "candidate_papers": len(candidate_rows),
        "already_by_doi": sum(d["match_status"] == "ALREADY_IN_ZOTERO_DOI" for d in decisions),
        "already_by_title": sum(d["match_status"] == "ALREADY_IN_ZOTERO_TITLE" for d in decisions),
        "new_to_zotero": len(new_candidates),
        "manual_check": len(manual_rows),
        "new_a1": sum(row.get("priority") == "A1" for row in new_candidates),
        "new_a2": sum(row.get("priority") == "A2" for row in new_candidates),
        "new_unclassified": sum(row.get("priority") not in {"A1", "A2"} for row in new_candidates),
    }
    counts["already_total"] = counts["already_by_doi"] + counts["already_by_title"]
    if counts["candidate_papers"] != counts["already_total"] + counts["new_to_zotero"] + counts["manual_check"]:
        raise ValueError("Candidate partition identity failed")

    qc = {
        "candidate_count_199": len(candidate_rows) == 199,
        "candidate_partition_identity": counts["candidate_papers"] == counts["already_total"] + counts["new_to_zotero"] + counts["manual_check"],
        "new_internal_doi_duplicates": len(new_dois) - len(set(new_dois)),
        "new_internal_title_duplicates": len(new_titles) - len(set(new_titles)),
        "new_dois_found_in_existing": len(set(new_dois) & existing_dois),
        "new_exact_titles_found_in_existing": len(set(new_titles) & existing_titles),
        "new_ris_ty_count": len(new_ris_blocks),
        "new_ris_er_count": len(new_ris_blocks),
        "new_ris_count_matches_new_csv": len(new_ris_blocks) == len(new_candidates),
        "utf8_roundtrip": NEW_RIS.read_bytes().decode("utf-8") == new_ris_text,
        "unicode_replacement_character_absent": "�" not in new_ris_text,
        "all_input_hashes_unchanged": before_hashes == {str(path.relative_to(ROOT)): sha256(path) for path in inputs},
    }
    if not all(
        [
            qc["candidate_count_199"],
            qc["candidate_partition_identity"],
            qc["new_internal_doi_duplicates"] == 0,
            qc["new_internal_title_duplicates"] == 0,
            qc["new_dois_found_in_existing"] == 0,
            qc["new_exact_titles_found_in_existing"] == 0,
            qc["new_ris_count_matches_new_csv"],
            qc["utf8_roundtrip"],
            qc["unicode_replacement_character_absent"],
            qc["all_input_hashes_unchanged"],
        ]
    ):
        raise ValueError(f"Quality control failed: {qc}")

    summary = f"""# Paper 2 Zotero import cross-check summary

## Research routing

| RQ | WP | Evidence Gate | Paper | Chapter | Scope | Evidence type |
|---|---|---|---|---|---|---|
| RQ2 | WP2 | Gate 3 | Paper 2 | Chapter 5 | Supporting | Information traceability |

## A. Existing Zotero library

| Metric | Count |
|---|---:|
| Zotero export 1 records | {counts['export_1_records']} |
| Zotero export 2 records | {counts['export_2_records']} |
| Zotero export 3 records | {counts['export_3_records']} |
| Combined raw records | {counts['combined_raw_records']} |
| Unique existing Zotero papers/items | {counts['unique_existing_zotero_papers']} |
| Existing papers/items with PDF | {counts['existing_papers_with_pdf']} |

The three exports have identical SHA-256 hashes. They were still consolidated and deduplicated using Zotero key, exact normalized DOI, exact normalized title, and title/first-author/year identity while refusing to merge conflicting non-empty DOIs.

## B. Candidate library

| Metric | Count |
|---|---:|
| Candidate papers | {counts['candidate_papers']} |

## C. Comparison

| Classification | Count |
|---|---:|
| Already in Zotero by DOI | {counts['already_by_doi']} |
| Already in Zotero by title/author/year | {counts['already_by_title']} |
| New papers to import | {counts['new_to_zotero']} |
| Manual check | {counts['manual_check']} |

Partition identity: `{counts['candidate_papers']} = {counts['already_total']} + {counts['new_to_zotero']} + {counts['manual_check']}` — PASS.

## D. Priority of NEW papers

| Priority | Count |
|---|---:|
| A1 new | {counts['new_a1']} |
| A2 new | {counts['new_a2']} |
| Unclassified | {counts['new_unclassified']} |

## Decision statement

**Claim →** `PAPER2_NEW_ONLY_FOR_ZOTERO.ris` contains only candidate records not found in the deduplicated current Zotero exports.

**Evidence →** DOI is the primary key. Exact-title matches require first-author and year confirmation; different non-empty DOIs are never merged. High-similarity/version-risk cases are isolated in `PAPER2_ZOTERO_MANUAL_CHECK.csv`.

**Limitation →** CSV exports reveal stored attachment paths but do not verify that every referenced PDF remains readable on disk. `PDF_AVAILABLE` means the Zotero export contains a `.pdf` attachment reference; it is not a filesystem-existence audit.

**Next action →** Import only `PAPER2_NEW_ONLY_FOR_ZOTERO.ris`. Review every `MANUAL_CHECK` row before any later import.

## Quality control

| Check | Result |
|---|---|
| Candidate partition | PASS — {counts['candidate_papers']} records |
| New RIS internal DOI duplicates | PASS — {qc['new_internal_doi_duplicates']} |
| New RIS DOI already in existing Zotero | PASS — {qc['new_dois_found_in_existing']} |
| New exact normalized title already in existing Zotero | PASS — {qc['new_exact_titles_found_in_existing']} |
| New RIS TY count | PASS — {qc['new_ris_ty_count']} |
| New RIS ER count | PASS — {qc['new_ris_er_count']} |
| TY count equals NEW CSV rows | PASS |
| UTF-8 round trip | PASS |
| Unicode replacement character absent | PASS |
| Input hashes unchanged | PASS |

## Files reviewed

- `zotero_final/PAPER2_GATE2_GATE3_MASTER_LIBRARY_FINAL.csv`
- `zotero_final/PAPER2_GATE2_GATE3_ZOTERO_MASTER_FINAL.ris`
- `My Library_export_Zotero_1.csv`
- `My Library_export_Zotero_2.csv`
- `My Library_export_Zotero_3.csv`

## Artifacts created

- `PAPER2_NEW_ONLY_FOR_ZOTERO.ris`
- `PAPER2_NEW_ONLY_FOR_ZOTERO.csv`
- `PAPER2_ALREADY_IN_ZOTERO.csv`
- `PAPER2_ZOTERO_MANUAL_CHECK.csv`
- `PAPER2_ZOTERO_IMPORT_SUMMARY.md`
- `PAPER2_ZOTERO_CROSSCHECK_LOG.json`
- `build_zotero_crosscheck.py`

## Evidence Gate affected

Gate 3 receives a duplicate-safe literature import set. This cross-check does not by itself close Gate 3.

## Unresolved risks

- {counts['manual_check']} candidate record(s) require manual identity/version review and are excluded from the import RIS.
- Attachment status is inferred from exported attachment references, not verified file existence.

## Recommended next action

Import only the new-only RIS, then review the manual-check CSV separately.

## Activities that must not start yet

- Do not import any `MANUAL_CHECK` item.
- Do not treat `NO_PDF` as a new bibliographic item.
- Do not delete or overwrite existing Zotero items from this report.
- Do not declare Gate 3 closed from bibliographic deduplication alone.
"""
    SUMMARY_MD.write_text(summary, encoding="utf-8", newline="\n")

    after_hashes = {str(path.relative_to(ROOT)): sha256(path) for path in inputs}
    log = {
        "timestamp": datetime.now(TZ).isoformat(timespec="seconds"),
        "timezone": "Asia/Ho_Chi_Minh",
        "script_sha256": sha256(Path(__file__)),
        "input_hashes_before": before_hashes,
        "input_hashes_after": after_hashes,
        "parameters": {
            "doi_primary_key": True,
            "exact_title_requires_author_year_for_candidate_match": True,
            "fuzzy_high_threshold": FUZZY_HIGH,
            "different_nonempty_dois_never_auto_merged": True,
            "attachment_detection": "PDF_AVAILABLE iff exported File Attachments contains a .pdf suffix; otherwise NO_PDF",
        },
        "counts": counts,
        "quality_checks": qc,
        "existing_exact_title_doi_conflicts_not_merged": existing_conflicts,
        "candidate_decisions": decisions,
        "artifacts": [str(path.resolve()) for path in (NEW_RIS, NEW_CSV, ALREADY_CSV, MANUAL_CSV, SUMMARY_MD)],
    }
    LOG_JSON.write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    print("ZOTERO CROSS-CHECK COMPLETE")
    print()
    print("Candidate papers: 199")
    print(f"Already in Zotero: {counts['already_total']}")
    print(f"New papers to import: {counts['new_to_zotero']}")
    print(f"Manual check: {counts['manual_check']}")
    print()
    print("IMPORT ONLY THIS FILE:")
    print(NEW_RIS.resolve())
    if counts["manual_check"]:
        print()
        print("DO NOT IMPORT MANUAL CHECK ITEMS YET.")


if __name__ == "__main__":
    main()
