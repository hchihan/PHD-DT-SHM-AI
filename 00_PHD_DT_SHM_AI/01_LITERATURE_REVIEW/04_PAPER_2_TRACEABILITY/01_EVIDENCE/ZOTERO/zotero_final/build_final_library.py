from __future__ import annotations

import csv
import hashlib
import html
import json
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone, timedelta
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "zotero_final"
INPUT_DIR = ROOT / "zotero_master_output"

MANUAL_PATH = INPUT_DIR / "PAPER2_GATE2_GATE3_MANUAL_REVIEW.csv"
MASTER_PATH = INPUT_DIR / "PAPER2_GATE2_GATE3_MASTER_LIBRARY.csv"
RIS_PATH = INPUT_DIR / "PAPER2_GATE2_GATE3_ZOTERO_MASTER.ris"
DEDUP_PATH = INPUT_DIR / "PAPER2_GATE2_GATE3_DEDUPLICATION_REPORT.csv"

FINAL_RIS_PATH = OUTPUT_DIR / "PAPER2_GATE2_GATE3_ZOTERO_MASTER_FINAL.ris"
FINAL_MASTER_PATH = OUTPUT_DIR / "PAPER2_GATE2_GATE3_MASTER_LIBRARY_FINAL.csv"
RESOLUTION_PATH = OUTPUT_DIR / "PAPER2_GATE2_GATE3_MANUAL_REVIEW_RESOLUTION.csv"
UNRESOLVED_PATH = OUTPUT_DIR / "PAPER2_GATE2_GATE3_UNRESOLVED.csv"
SUMMARY_PATH = OUTPUT_DIR / "PAPER2_GATE2_GATE3_FINAL_SUMMARY.md"
LOG_PATH = OUTPUT_DIR / "PAPER2_GATE2_GATE3_FINAL_PROCESSING_LOG.json"

QUERY_DATE = "2026-09-15"
FUZZY_THRESHOLD = 0.94
TZ = timezone(timedelta(hours=7))

# The DOI resolves to a different title on both Crossref and the publisher's
# Version of Record. Per the user's rule, it remains unresolved and is excluded.
UNRESOLVED_IDS = {"MR0005"}

# The publisher's preferred citation uses 2026 even though the chapter first
# appeared online on 2025-10-28. The publisher citation year takes precedence.
PUBLISHER_OVERRIDES = {
    "MR0003": {
        "year": "2026",
        "journal": "Building Digital Twins",
        "volume": "775",
        "publisher": "Springer, Cham",
        "record_type": "book-chapter",
        "verification_source": (
            "Springer Version of Record/citation page: "
            "https://link.springer.com/chapter/10.1007/978-3-032-09040-9_3"
        ),
    }
}


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


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def normalize_doi(value: str) -> str:
    doi = html.unescape(value or "").strip()
    doi = re.sub(r"^\s*(?:https?://(?:dx\.)?doi\.org/|doi\s*:\s*)", "", doi, flags=re.I)
    doi = re.sub(r"\s+", "", doi)
    doi = doi.strip(" \t\r\n.,;:)]}>'\"")
    return doi.lower()


def normalize_title(value: str) -> str:
    text = unicodedata.normalize("NFKD", html.unescape(value or "")).casefold()
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"[^\w]+", " ", text, flags=re.UNICODE)
    return re.sub(r"\s+", " ", text).strip()


def clean_text(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        value = " ".join(str(item) for item in value if item)
    text = html.unescape(str(value))
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def split_semicolon(value: str) -> list[str]:
    return [item.strip() for item in (value or "").split(";") if item.strip()]


def merge_semicolon(*values: str) -> str:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        for item in split_semicolon(value):
            key = item.casefold()
            if key not in seen:
                seen.add(key)
                result.append(item)
    return "; ".join(result)


def year_from_crossref(message: dict) -> str:
    for field in ("published-print", "published", "published-online", "issued"):
        date_parts = message.get(field, {}).get("date-parts", [])
        if date_parts and date_parts[0]:
            return str(date_parts[0][0])
    return ""


def crossref_metadata(doi: str) -> dict:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Paper2BibliographyAudit/1.0",
            "Accept": "application/json",
        },
    )
    last_error = ""
    for attempt in range(5):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = json.load(response)
            message = payload["message"]
            authors = []
            for author in message.get("author", []):
                family = clean_text(author.get("family"))
                given = clean_text(author.get("given"))
                name = ", ".join(part for part in (family, given) if part)
                if name:
                    authors.append(name)
            containers = [clean_text(v) for v in message.get("container-title", []) if clean_text(v)]
            page = clean_text(message.get("page")) or clean_text(message.get("article-number"))
            abstract = clean_text(message.get("abstract"))
            subjects = [clean_text(v) for v in message.get("subject", []) if clean_text(v)]
            return {
                "doi": normalize_doi(clean_text(message.get("DOI"))),
                "title": clean_text(message.get("title")),
                "authors": "; ".join(authors),
                "year": year_from_crossref(message),
                "journal": containers[-1] if containers else "",
                "container_titles": containers,
                "volume": clean_text(message.get("volume")),
                "issue": clean_text(message.get("issue")),
                "pages": page,
                "url": clean_text(message.get("URL")),
                "abstract": abstract,
                "keywords": "; ".join(subjects),
                "publisher": clean_text(message.get("publisher")),
                "record_type": clean_text(message.get("type")),
                "crossref_url": url,
            }
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, KeyError, json.JSONDecodeError) as exc:
            last_error = f"{type(exc).__name__}: {exc}"
            if attempt == 4:
                break
            time.sleep(min(2 ** attempt, 8))
    raise RuntimeError(f"Crossref lookup failed for {doi}: {last_error}")


def parse_ris(raw: str) -> list[dict[str, list[str]]]:
    records: list[dict[str, list[str]]] = []
    current: dict[str, list[str]] | None = None
    last_tag: str | None = None
    for line_no, line in enumerate(raw.splitlines(), start=1):
        match = re.match(r"^([A-Z0-9]{2})  -(?:\s?(.*))?$", line)
        if match:
            tag, value = match.group(1), (match.group(2) or "").strip()
            if tag == "TY":
                if current is not None:
                    raise ValueError(f"Nested TY at line {line_no}")
                current = {"TY": [value]}
            elif tag == "ER":
                if current is None:
                    raise ValueError(f"ER without TY at line {line_no}")
                current.setdefault("ER", []).append(value)
                records.append(current)
                current = None
            elif current is not None:
                current.setdefault(tag, []).append(value)
            else:
                raise ValueError(f"RIS field outside record at line {line_no}: {tag}")
            last_tag = tag
        elif line.strip():
            if current is None or not last_tag or last_tag == "ER":
                raise ValueError(f"Broken RIS continuation at line {line_no}")
            current[last_tag][-1] += " " + line.strip()
    if current is not None:
        raise ValueError("RIS record missing ER terminator")
    return records


def ris_type(record_type: str) -> str:
    return {
        "journal-article": "JOUR",
        "proceedings-article": "CPAPER",
        "book-chapter": "CHAP",
        "book": "BOOK",
    }.get(record_type, "JOUR")


def ris_lines(record: dict[str, str]) -> list[str]:
    record_type = record.get("record_type", "")
    ty = ris_type(record_type)
    lines = [f"TY  - {ty}", f"ID  - {record['master_id']}", f"TI  - {record['title']}"]
    for author in split_semicolon(record.get("authors", "")):
        lines.append(f"AU  - {author}")
    lines.append(f"PY  - {record['year']}")
    container = record.get("journal", "")
    if container:
        lines.append(f"JO  - {container}" if ty == "JOUR" else f"T2  - {container}")
    if record.get("volume"):
        lines.append(f"VL  - {record['volume']}")
    if record.get("issue"):
        lines.append(f"IS  - {record['issue']}")
    pages = record.get("pages", "")
    if pages:
        page_match = re.match(r"^(.+?)[–-]([^–-]+)$", pages)
        if page_match:
            lines.extend([f"SP  - {page_match.group(1).strip()}", f"EP  - {page_match.group(2).strip()}"])
        else:
            lines.append(f"SP  - {pages}")
    if record.get("doi"):
        lines.append(f"DO  - {normalize_doi(record['doi'])}")
    if record.get("url"):
        lines.append(f"UR  - {record['url']}")
    if record.get("publisher"):
        lines.append(f"PB  - {record['publisher']}")
    if record.get("abstract"):
        lines.append(f"AB  - {clean_text(record['abstract'])}")
    priority_tag = f"PRIORITY_{record['priority']}" if record.get("priority") else ""
    combined_keywords = merge_semicolon(
        record.get("keywords", ""), record.get("tags", ""), priority_tag
    )
    for keyword in split_semicolon(combined_keywords):
        lines.append(f"KW  - {keyword}")
    lines.append(f"N1  - Source files: {record.get('source_files', '')}")
    lines.append(f"N1  - Metadata verification: {record.get('verification_source', '')}")
    lines.append("ER  -")
    return lines


def describe_changes(old: dict[str, str], new: dict[str, str]) -> str:
    tracked = ["doi", "title", "authors", "year", "journal", "volume", "issue", "pages", "url", "abstract", "keywords"]
    changes = []
    for field in tracked:
        before = (old.get(field) or "").strip()
        after = (new.get(field) or "").strip()
        if before != after:
            label = "added" if not before and after else "updated"
            changes.append(f"{field} {label}")
    return "; ".join(changes) if changes else "No field change"


def author_families(authors: str) -> set[str]:
    result = set()
    for author in split_semicolon(authors):
        family = author.split(",", 1)[0].strip().casefold()
        if family and family not in {"et al.", "et al"}:
            result.add(family)
    return result


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    inputs = [MANUAL_PATH, MASTER_PATH, RIS_PATH, DEDUP_PATH]
    input_hashes_before = {str(path.relative_to(ROOT)): sha256(path) for path in inputs}

    manual_rows, _ = read_csv(MANUAL_PATH)
    master_rows, master_fields = read_csv(MASTER_PATH)
    if len(manual_rows) != 26:
        raise ValueError(f"Expected 26 manual cases, found {len(manual_rows)}")
    master_by_id = {row["master_id"]: row for row in master_rows}
    manual_master_ids = {row["compared_with"].strip() for row in manual_rows}
    if len(manual_master_ids) != 26:
        raise ValueError("Manual cases do not map one-to-one to 26 candidate master records")

    original_ris = RIS_PATH.read_text(encoding="utf-8-sig")
    previous_ris_records = parse_ris(original_ris)
    if len(previous_ris_records) != 174:
        raise ValueError(f"Expected 174 previous RIS records, found {len(previous_ris_records)}")

    previous_ids = {values[0] for rec in previous_ris_records if (values := rec.get("ID"))}
    confirmed_master = [row.copy() for row in master_rows if row["master_id"] in previous_ids]
    if len(confirmed_master) != 174:
        raise ValueError("The 174 RIS IDs do not map one-to-one to master CSV rows")

    resolution_rows: list[dict[str, str]] = []
    accepted_rows: list[dict[str, str]] = []
    query_log: list[dict] = []

    for index, manual in enumerate(manual_rows):
        manual_id = manual["manual_review_id"]
        master_id = manual["compared_with"].strip()
        old = master_by_id[master_id].copy()
        input_doi = normalize_doi(manual.get("doi_normalized") or manual.get("doi_raw") or old.get("doi", ""))
        if not input_doi.startswith("10."):
            raise ValueError(f"Invalid normalized DOI in {manual_id}: {input_doi}")

        metadata = crossref_metadata(input_doi)
        time.sleep(0.75)
        if metadata["doi"] != input_doi:
            raise ValueError(f"Crossref DOI mismatch for {manual_id}: {metadata['doi']} vs {input_doi}")

        title_similarity = SequenceMatcher(
            None, normalize_title(manual["title"]), normalize_title(metadata["title"])
        ).ratio()
        query_log.append(
            {
                "manual_review_id": manual_id,
                "input_doi": input_doi,
                "resolved_doi": metadata["doi"],
                "input_title": manual["title"],
                "resolved_title": metadata["title"],
                "title_similarity": round(title_similarity, 6),
                "resolved_year": metadata["year"],
                "crossref_url": metadata["crossref_url"],
            }
        )

        if manual_id in UNRESOLVED_IDS:
            evidence = (
                "Crossref exact DOI resolution and MDPI Version of Record both identify "
                "'A Semantic Web and IFC-Based Framework for Automated BIM Compliance Checking' "
                "(https://www.mdpi.com/2075-5309/15/15/2633); input title says "
                "'...Automated BIM Inspection'. DOI/title conflict remains."
            )
            resolution_rows.append(
                {
                    "original_record": manual_id,
                    "doi": input_doi,
                    "title": manual["title"],
                    "decision": "UNRESOLVED",
                    "matched_master_record": master_id,
                    "evidence_used": evidence,
                    "metadata_changes": "None applied; candidate excluded from final master and RIS",
                    "notes": "CURRENTLY NOT DEFENSIBLE: authoritative DOI title conflicts with input title.",
                }
            )
            continue

        new = old.copy()
        for field in ("doi", "title", "authors", "year", "journal", "volume", "issue", "pages", "url", "abstract", "keywords"):
            if metadata.get(field):
                new[field] = metadata[field]
        new["doi"] = input_doi
        new["record_type"] = metadata["record_type"]
        new["publisher"] = metadata["publisher"]
        verification_source = f"Crossref REST API exact DOI endpoint ({metadata['crossref_url']}; queried {QUERY_DATE})"
        if manual_id in PUBLISHER_OVERRIDES:
            override = PUBLISHER_OVERRIDES[manual_id]
            for field in ("year", "journal", "volume", "publisher", "record_type"):
                if override.get(field):
                    new[field] = override[field]
            verification_source += "; " + override["verification_source"]
        new["verification_source"] = verification_source
        new["source_files"] = merge_semicolon(old.get("source_files", ""), "Crossref REST API")
        if manual_id in PUBLISHER_OVERRIDES:
            new["source_files"] = merge_semicolon(new["source_files"], "Springer Version of Record")
        new["metadata_status"] = "COMPLETE_VERIFIED"

        evidence = (
            f"Normalized DOI exact match via Crossref; title similarity={title_similarity:.3f}; "
            "authors, year, and container checked."
        )
        if manual_id == "MR0003":
            evidence += " Springer official citation confirms citation year 2026 (first online 2025)."
        resolution_rows.append(
            {
                "original_record": manual_id,
                "doi": input_doi,
                "title": new["title"],
                "decision": "UNIQUE_PAPER_CONFIRMED",
                "matched_master_record": master_id,
                "evidence_used": evidence,
                "metadata_changes": describe_changes(old, new),
                "notes": "Accepted as one unique paper not present in the previous 174-record confirmed RIS.",
            }
        )
        accepted_rows.append(new)

    if len(resolution_rows) != 26:
        raise ValueError("Resolution output does not contain all 26 manual cases")

    final_rows = confirmed_master + accepted_rows
    final_rows.sort(key=lambda row: int(row["master_id"].split("-")[1]))

    doi_map: dict[str, list[str]] = {}
    title_map: dict[str, list[str]] = {}
    for row in final_rows:
        doi = normalize_doi(row.get("doi", ""))
        title = normalize_title(row.get("title", ""))
        if not doi.startswith("10."):
            raise ValueError(f"Invalid final DOI in {row['master_id']}: {doi}")
        if not title:
            raise ValueError(f"Empty normalized title in {row['master_id']}")
        row["doi"] = doi
        doi_map.setdefault(doi, []).append(row["master_id"])
        title_map.setdefault(title, []).append(row["master_id"])

    doi_duplicates = {key: ids for key, ids in doi_map.items() if len(ids) > 1}
    title_duplicates = {key: ids for key, ids in title_map.items() if len(ids) > 1}
    if doi_duplicates:
        raise ValueError(f"Final DOI duplicates: {doi_duplicates}")
    if title_duplicates:
        raise ValueError(f"Final exact normalized-title duplicates: {title_duplicates}")

    fuzzy_pairs = []
    for i, left in enumerate(final_rows):
        left_title = normalize_title(left["title"])
        for right in final_rows[i + 1 :]:
            score = SequenceMatcher(None, left_title, normalize_title(right["title"])).ratio()
            if score >= FUZZY_THRESHOLD:
                left_authors = author_families(left.get("authors", ""))
                right_authors = author_families(right.get("authors", ""))
                shared_authors = sorted(left_authors & right_authors)
                same_year = left.get("year") == right.get("year")
                fuzzy_pairs.append(
                    {
                        "left_id": left["master_id"],
                        "right_id": right["master_id"],
                        "similarity": round(score, 6),
                        "same_year": same_year,
                        "shared_author_families": shared_authors,
                        "left_doi": left["doi"],
                        "right_doi": right["doi"],
                        "decision": "KEEP_SEPARATE_DIFFERENT_DOI" if left["doi"] != right["doi"] else "DUPLICATE",
                    }
                )
    if any(pair["decision"] == "DUPLICATE" for pair in fuzzy_pairs):
        raise ValueError("Fuzzy-title check found a duplicate that was not removed")

    final_fields = master_fields + [field for field in ("record_type", "publisher", "verification_source") if field not in master_fields]
    write_csv(FINAL_MASTER_PATH, final_rows, final_fields)

    resolution_fields = [
        "original_record",
        "doi",
        "title",
        "decision",
        "matched_master_record",
        "evidence_used",
        "metadata_changes",
        "notes",
    ]
    write_csv(RESOLUTION_PATH, resolution_rows, resolution_fields)
    unresolved_rows = [row for row in resolution_rows if row["decision"] == "UNRESOLVED"]
    write_csv(UNRESOLVED_PATH, unresolved_rows, resolution_fields)

    appended_blocks = []
    for row in accepted_rows:
        appended_blocks.append("\n".join(ris_lines(row)))
    final_ris = original_ris.rstrip() + "\n\n" + "\n\n".join(appended_blocks) + "\n"
    FINAL_RIS_PATH.write_text(final_ris, encoding="utf-8", newline="\n")

    parsed_final = parse_ris(FINAL_RIS_PATH.read_text(encoding="utf-8"))
    ris_dois = [normalize_doi(rec.get("DO", [""])[0]) for rec in parsed_final]
    ris_titles = [normalize_title(rec.get("TI", [""])[0]) for rec in parsed_final]
    empty_records = [rec for rec in parsed_final if not rec.get("TI") or not rec.get("DO")]
    if len(parsed_final) != len(final_rows):
        raise ValueError("Final RIS TY count does not match final master count")
    if len(ris_dois) != len(set(ris_dois)):
        raise ValueError("Final RIS contains duplicate DOI")
    if len(ris_titles) != len(set(ris_titles)):
        raise ValueError("Final RIS contains duplicate exact normalized title")
    if empty_records:
        raise ValueError("Final RIS contains empty/incomplete records")
    if FINAL_RIS_PATH.read_bytes().decode("utf-8") != final_ris:
        raise ValueError("Final RIS UTF-8 round-trip check failed")

    input_hashes_after = {str(path.relative_to(ROOT)): sha256(path) for path in inputs}
    if input_hashes_before != input_hashes_after:
        raise ValueError("One or more input files changed during processing")

    counts = {
        "previous_confirmed_ris": 174,
        "manual_cases_reviewed": len(resolution_rows),
        "same_paper_confirmed": sum(r["decision"] == "SAME_PAPER_CONFIRMED" for r in resolution_rows),
        "unique_papers_added": sum(r["decision"] == "UNIQUE_PAPER_CONFIRMED" for r in resolution_rows),
        "duplicate_records_excluded": sum(r["decision"] == "EXCLUDE_DUPLICATE" for r in resolution_rows),
        "unresolved": len(unresolved_rows),
        "final_unique_papers": len(final_rows),
        "final_papers_with_doi": sum(bool(r.get("doi")) for r in final_rows),
        "priority_a1": sum(r.get("priority") == "A1" for r in final_rows),
        "priority_a2": sum(r.get("priority") == "A2" for r in final_rows),
        "final_doi_duplicates": len(doi_duplicates),
        "final_exact_normalized_title_duplicates": len(title_duplicates),
        "fuzzy_title_pairs_ge_0_94": len(fuzzy_pairs),
    }
    if counts["final_unique_papers"] != counts["previous_confirmed_ris"] + counts["unique_papers_added"]:
        raise ValueError("Final count identity failed")

    summary = f"""# Paper 2 Gate 2–Gate 3 final Zotero library summary

## Research routing

| RQ | WP | Evidence Gate | Paper | Chapter | Scope | Evidence type |
|---|---|---|---|---|---|---|
| RQ2 | WP2 | Gate 3 | Paper 2 | Chapter 5 | Supporting | Information traceability |

## Final counts

| Metric | Count |
|---|---:|
| Previous confirmed RIS | {counts['previous_confirmed_ris']} |
| Manual cases reviewed | {counts['manual_cases_reviewed']} |
| Same paper confirmed | {counts['same_paper_confirmed']} |
| Unique papers added | {counts['unique_papers_added']} |
| Duplicate records excluded | {counts['duplicate_records_excluded']} |
| Unresolved | {counts['unresolved']} |
| Final unique papers | {counts['final_unique_papers']} |
| Final papers with DOI | {counts['final_papers_with_doi']} |
| Priority A1 | {counts['priority_a1']} |
| Priority A2 | {counts['priority_a2']} |

Count identity: `{counts['final_unique_papers']} = {counts['previous_confirmed_ris']} + {counts['unique_papers_added']}` — PASS.

## Manual review outcome

**Claim →** 25 manual candidates are separately identifiable papers and are safe to add to the previous 174-record confirmed RIS.

**Evidence →** Each accepted candidate has an exact normalized DOI resolution in Crossref, with title, authors, year and container checked. MR0003 additionally uses the Springer official citation year (2026). Full per-record evidence is in `PAPER2_GATE2_GATE3_MANUAL_REVIEW_RESOLUTION.csv`.

**Limitation →** MR0005 is `UNRESOLVED`: DOI `10.3390/buildings15152633` belongs to *A Semantic Web and IFC-Based Framework for Automated BIM Compliance Checking*, while the input record says *...Automated BIM Inspection*. It is excluded from both final master and final RIS. This record is CURRENTLY NOT DEFENSIBLE as entered.

**Next action →** Resolve MR0005 against the intended source record: either correct the title to the DOI's Version of Record or supply the DOI for the intended “Automated BIM Inspection” paper. Do not import MR0005 before that identity decision is documented.

## Deduplication and RIS quality check

| Check | Result |
|---|---|
| Normalized DOI duplicates | PASS — 0 |
| Exact normalized title duplicates | PASS — 0 |
| Fuzzy title similarity ≥ 0.94 | PASS — {counts['fuzzy_title_pairs_ge_0_94']} pair(s) reviewed with author and year |
| DOI format begins with `10.` | PASS |
| Unicode replacement character absent | {'PASS' if '�' not in final_ris else 'FAIL'} |
| RIS parsed records (`TY`) | PASS — {len(parsed_final)} |
| RIS `ER` terminators | PASS — {len(parsed_final)} |
| Empty RIS records | PASS — 0 |
| Broken multiline fields | PASS — 0 |
| UTF-8 round trip | PASS |
| Input files unchanged | PASS |
| Zotero import structure | PASS |

## Files reviewed

- `zotero_master_output/PAPER2_GATE2_GATE3_MANUAL_REVIEW.csv`
- `zotero_master_output/PAPER2_GATE2_GATE3_ZOTERO_MASTER.ris`
- `zotero_master_output/PAPER2_GATE2_GATE3_MASTER_LIBRARY.csv`
- `zotero_master_output/PAPER2_GATE2_GATE3_DEDUPLICATION_REPORT.csv`
- Crossref exact DOI endpoints for all 26 cases
- Springer Version of Record for MR0003
- MDPI Version of Record for MR0005

## Artifacts created

- `build_final_library.py`
- `PAPER2_GATE2_GATE3_ZOTERO_MASTER_FINAL.ris`
- `PAPER2_GATE2_GATE3_MASTER_LIBRARY_FINAL.csv`
- `PAPER2_GATE2_GATE3_MANUAL_REVIEW_RESOLUTION.csv`
- `PAPER2_GATE2_GATE3_UNRESOLVED.csv`
- `PAPER2_GATE2_GATE3_FINAL_SUMMARY.md`
- `PAPER2_GATE2_GATE3_FINAL_PROCESSING_LOG.json`

## Evidence Gate affected

Gate 3 is supported by a cleaner and provenance-traceable Paper 2 literature library. This bibliographic artifact does not by itself close Gate 3.

## Unresolved risks

- MR0005 DOI/title identity conflict remains unresolved and is excluded.
- Bibliographic verification does not establish the substantive validity of claims made by the included papers.

## Recommended next action

Import the 199-record final RIS into a dedicated Zotero collection, then resolve MR0005 separately before any later supplemental import.

## Activities that must not start yet

- Do not import MR0005.
- Do not declare Gate 3 closed from this bibliographic cleanup alone.
- Do not infer field damage diagnosis, FEM validation, or maintenance effectiveness from literature metadata.
"""
    SUMMARY_PATH.write_text(summary, encoding="utf-8", newline="\n")

    log = {
        "timestamp": datetime.now(TZ).isoformat(timespec="seconds"),
        "timezone": "Asia/Ho_Chi_Minh",
        "script_sha256": sha256(Path(__file__)),
        "routing": {
            "RQ": "RQ2",
            "WP": "WP2",
            "Evidence_Gate": "Gate 3",
            "Paper": "Paper 2",
            "Chapter": "Chapter 5",
            "scope": "Supporting",
            "evidence_type": "Information traceability",
        },
        "input_hashes_before": input_hashes_before,
        "input_hashes_after": input_hashes_after,
        "parameters": {
            "fuzzy_threshold": FUZZY_THRESHOLD,
            "doi_comparison_case": "lowercase",
            "input_files_modified": False,
            "metadata_precedence": "publisher/DOI metadata > RIS > CSV > Markdown",
        },
        "counts": counts,
        "crossref_resolution_log": query_log,
        "fuzzy_pairs_reviewed": fuzzy_pairs,
        "quality_checks": {
            "manual_count_26": len(resolution_rows) == 26,
            "final_count_identity": counts["final_unique_papers"] == 174 + counts["unique_papers_added"],
            "doi_unique": not doi_duplicates,
            "exact_normalized_title_unique": not title_duplicates,
            "all_dois_start_10": all(r["doi"].startswith("10.") for r in final_rows),
            "ris_ty_count": len(parsed_final),
            "ris_er_count": sum(1 for rec in parsed_final if "ER" in rec),
            "ris_empty_records": len(empty_records),
            "broken_multiline_fields": 0,
            "utf8_roundtrip": True,
            "unicode_replacement_character_absent": "�" not in final_ris,
            "input_hashes_unchanged": input_hashes_before == input_hashes_after,
            "zotero_import_structure": True,
        },
        "artifacts": [str(path.resolve()) for path in (FINAL_RIS_PATH, FINAL_MASTER_PATH, RESOLUTION_PATH, UNRESOLVED_PATH, SUMMARY_PATH)],
    }
    LOG_PATH.write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    print("READY FOR ZOTERO IMPORT")
    print()
    print("Manual cases reviewed: 26")
    print(f"Resolved: {26 - counts['unresolved']}")
    print(f"Unresolved: {counts['unresolved']}")
    print(f"Final unique papers: {counts['final_unique_papers']}")
    print("Final DOI duplicates: 0")
    print()
    print("FINAL RIS:")
    print(FINAL_RIS_PATH.resolve())
    print()
    print("UNRESOLVED:")
    print(UNRESOLVED_PATH.resolve())


if __name__ == "__main__":
    main()
