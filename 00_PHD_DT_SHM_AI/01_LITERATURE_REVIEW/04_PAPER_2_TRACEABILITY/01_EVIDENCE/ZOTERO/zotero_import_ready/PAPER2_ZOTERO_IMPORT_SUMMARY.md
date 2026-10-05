# Paper 2 Zotero import cross-check summary

## Research routing

| RQ | WP | Evidence Gate | Paper | Chapter | Scope | Evidence type |
|---|---|---|---|---|---|---|
| RQ2 | WP2 | Gate 3 | Paper 2 | Chapter 5 | Supporting | Information traceability |

## A. Existing Zotero library

| Metric | Count |
|---|---:|
| Zotero export 1 records | 434 |
| Zotero export 2 records | 434 |
| Zotero export 3 records | 434 |
| Combined raw records | 1302 |
| Unique existing Zotero papers/items | 415 |
| Existing papers/items with PDF | 300 |

The three exports have identical SHA-256 hashes. They were still consolidated and deduplicated using Zotero key, exact normalized DOI, exact normalized title, and title/first-author/year identity while refusing to merge conflicting non-empty DOIs.

## B. Candidate library

| Metric | Count |
|---|---:|
| Candidate papers | 199 |

## C. Comparison

| Classification | Count |
|---|---:|
| Already in Zotero by DOI | 35 |
| Already in Zotero by title/author/year | 0 |
| New papers to import | 164 |
| Manual check | 0 |

Partition identity: `199 = 35 + 164 + 0` — PASS.

## D. Priority of NEW papers

| Priority | Count |
|---|---:|
| A1 new | 8 |
| A2 new | 15 |
| Unclassified | 141 |

## Decision statement

**Claim →** `PAPER2_NEW_ONLY_FOR_ZOTERO.ris` contains only candidate records not found in the deduplicated current Zotero exports.

**Evidence →** DOI is the primary key. Exact-title matches require first-author and year confirmation; different non-empty DOIs are never merged. High-similarity/version-risk cases are isolated in `PAPER2_ZOTERO_MANUAL_CHECK.csv`.

**Limitation →** CSV exports reveal stored attachment paths but do not verify that every referenced PDF remains readable on disk. `PDF_AVAILABLE` means the Zotero export contains a `.pdf` attachment reference; it is not a filesystem-existence audit.

**Next action →** Import only `PAPER2_NEW_ONLY_FOR_ZOTERO.ris`. Review every `MANUAL_CHECK` row before any later import.

## Quality control

| Check | Result |
|---|---|
| Candidate partition | PASS — 199 records |
| New RIS internal DOI duplicates | PASS — 0 |
| New RIS DOI already in existing Zotero | PASS — 0 |
| New exact normalized title already in existing Zotero | PASS — 0 |
| New RIS TY count | PASS — 164 |
| New RIS ER count | PASS — 164 |
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

- 0 candidate record(s) require manual identity/version review and are excluded from the import RIS.
- Attachment status is inferred from exported attachment references, not verified file existence.

## Recommended next action

Import only the new-only RIS, then review the manual-check CSV separately.

## Activities that must not start yet

- Do not import any `MANUAL_CHECK` item.
- Do not treat `NO_PDF` as a new bibliographic item.
- Do not delete or overwrite existing Zotero items from this report.
- Do not declare Gate 3 closed from bibliographic deduplication alone.
