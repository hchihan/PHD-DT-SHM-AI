# Paper 2 Consolidation Plan

## Research routing

| RQ | WP | Gate | Paper | Chapter |
|---|---|---|---|---|
| RQ2 | WP2 | Gate 2–3 | Paper 2 | Chapter 5 |

Locked direction: `Condition Evidence → verified BIM/IFC component → accountable Inspection Record`.

## Authority decisions by logical group

| Group | Current file | Older files | Decision | Reason |
|---|---|---|---|---|
| Literature synthesis report | `paper2_targeted_literature/06_TARGETED_GAP_AUDIT.md`, read with files 05, 07 and 08 | Four root `deep-research-report*` files; two generated Zotero Markdown reports | Keep the corrected targeted-review set; archive earlier syntheses | The targeted set incorporates full-text Borkowski and the corrected validity/applicability definition. The supplied current decision upgrades the review status to `FULL FREEZE`; any internal `CONDITIONAL_FREEZE` wording is historical, not controlling. |
| Gap Audit | `paper2_targeted_literature/06_TARGETED_GAP_AUDIT.md` | `paper2_core5_deep_read/07_CORE5_PRELIMINARY_GAP_VERDICT.md` | Keep targeted Gap Audit active; archive preliminary CORE-5 verdict | The later audit covers 12 full-text papers and the correction pass; the CORE-5 verdict explicitly says it is preliminary and insufficient to freeze the wider gap. |
| Evidence Matrix | `paper2_targeted_literature/05_TARGETED_EVIDENCE_MATRIX.csv` | `paper2_core5_deep_read/06_CORE5_EVIDENCE_MATRIX.csv` | Keep targeted matrix as controlling; retain CORE-5 matrix as supporting evidence | The targeted matrix has corrected, separate `model_version_context` and `evidence_validity_scope` fields. The CORE-5 matrix remains unique provenance, not a competing current synthesis. |
| Borkowski evidence | `paper2_targeted_literature/07_BORKOWSKI_2026_FULLTEXT_REVIEW.md` | All abstract-only or `FULL_TEXT_NOT_AVAILABLE` statements embedded in earlier reports | Keep full-text review active; archive earlier reports | The full text was located under the duplicate Zotero parent and read completely; this directly supersedes availability assumptions. |
| Correction record | `paper2_targeted_literature/08_CORRECTION_PASS_SUMMARY.md` | Earlier uncorrected validity-scope coding embedded in old reports/notes | Keep active with authority limited to correction evidence | It records the corrected strict definition. Its `CONDITIONAL_FREEZE` label is superseded by the supplied current `FULL FREEZE` decision. |
| Paper 2 outline | `PAPER2_DRAFT_OUTLINE_GATE2_GATE3_20260914.docx` | `PAPER2_VERIFIABLE_TRACEABILITY_DETAILED_OUTLINE_v0.1_20260812.md` | Keep the 14/09 DOCX as the current working outline; archive v0.1 | The DOCX is the later annotated manuscript architecture and explicitly distinguishes proposed, fixture and unverified content. Literature claims must be governed by the targeted-review set. |
| Gate 2–3 protocol | `G2_ONE_PAGE_TRACEABILITY_DRAFT_20260914.md` | Older protocol fragments in the August roadmap/direction and detailed outline | Keep active as the latest working draft | It incorporates seven correction points but remains explicitly `DRAFT — CHƯA REVIEW — CHƯA FREEZE`; it is not a Gate Decision Record. |
| Gate 2–3 roadmap | No existing file is fully authoritative under the supplied current state | `G2_G3_PAPER2_CURRENT_ROADMAP_v2.1_20260804.md`; `PAPER2_CURRENT_DIRECTION_v2.1_20260804.md`; root `README.md` | Archive as superseded; use `README_CURRENT.md` only as the current routing/source map | These files still state Gate 1 is open and preserve a broader action/status-event contribution boundary that conflicts with the locked current state. A `CURRENT` label or header version cannot override scientific content. |
| Orientation/journal | `PAPER2_GATE2_GATE3_ORIENTATION_JOURNAL_v0.2_20260914.docx` | Earlier orientation content embedded in root reports | Retain as current supporting material | It is the latest orientation/simulation, but explicitly not a manuscript, approved protocol, or Gate Decision Record. |
| CORE-5 deep read | Files 00–06 under `paper2_core5_deep_read` | File 07 preliminary verdict | Retain unique evidence; archive only the superseded verdict | Bibliographic checks, five full-text notes and the matrix remain valid provenance cited by the later review. |
| Targeted 12-paper review | Files 01–08 and paper-level notes | None after correction | Retain in evidence area | This is the current literature evidence set. Screening/exclusions/selection/deep-read notes support auditability. |
| Zotero | Final library, import-ready records, RIS/CSV sources, logs and QA records | `zotero_master_output`; two of three identical `My Library` exports; generated Markdown syntheses | Retain final/raw/supporting records; archive superseded outputs and exact duplicate copies | SHA256 confirms the three library exports are identical. One remains active. The final library supersedes the earlier master-output stage. No Zotero database or metadata will be modified. |
| Source PDFs | Both files under `File pdf` | None | Retain as raw evidence | Source PDFs are never superseded by synthesis. Original filenames remain unchanged. |
| Cache | `.cache` and `__pycache__` | Not applicable | Archive as intermediate | Machine-generated cache is not research evidence. |

## Planned active structure

```text
05_PAPER_2_TRACEABILITY/
├── README_CURRENT.md
├── 00_CURRENT/
│   ├── G2_ONE_PAGE_TRACEABILITY_DRAFT_20260914.md
│   ├── PAPER2_DRAFT_OUTLINE_GATE2_GATE3_20260914.docx
│   └── PAPER2_GATE2_GATE3_ORIENTATION_JOURNAL_v0.2_20260914.docx
├── 01_EVIDENCE/
│   ├── CORE5/
│   ├── TARGETED_REVIEW/
│   ├── ZOTERO/
│   └── PDF/
└── 90_ARCHIVE_SUPERSEDED/
    ├── 01_OLD_LITERATURE_REPORTS/
    ├── 02_OLD_PAPER2_OUTLINES/
    ├── 03_OLD_GATE_ROADMAPS/
    ├── 04_OLD_DEEP_READ_OUTPUTS/
    ├── 05_INTERMEDIATE_PROCESSING/
    ├── 06_DUPLICATES/
    └── 99_REVIEW_NEEDED/
```

## Safety check before move

| Check | Evidence | Result |
|---|---|---|
| No `CURRENT_CORE` file will be archived | Inventory action cross-check: all six `CURRENT_CORE` rows are `KEEP_ACTIVE` | PASS |
| No unique raw evidence will be archived as superseded | All source PDFs, RIS, final/raw CSV exports and the retained Zotero library export are `KEEP_RAW`; only two SHA256-identical copies are archived | PASS |
| No cited PDF will be lost | Both PDFs are retained under `01_EVIDENCE/PDF` with unchanged filenames | PASS |
| No current correction output will be replaced by an older file | Targeted files 05–08 are retained together as current core evidence | PASS |
| Destination overwrite risk | Moves will fail rather than overwrite; every destination is checked before execution | PASS |
| Uncertain authority | No file remains unclassified; the absence of an authoritative current roadmap is recorded explicitly rather than guessed | PASS |

## Claim → Evidence → Limitation → Next action

| Claim | Evidence | Limitation | Next action |
|---|---|---|---|
| The corrected targeted review is the current literature authority | Full-text Borkowski review, corrected matrix, targeted gap audit and correction summary | The files retain an older `CONDITIONAL_FREEZE` sentence | Treat the supplied `FULL FREEZE` decision as controlling; do not reopen literature search |
| The 14/09 DOCX is the current working outline | It postdates and incorporates the older detailed-outline generation | It predates the final targeted correction and is not a completed manuscript | Keep as working architecture; do not use unsupported literature claims from it |
| No current authoritative Gate roadmap exists in the folder | August roadmap/direction conflict with the supplied locked Gate state | Consolidation does not rewrite scientific content or manufacture a new roadmap | Archive the conflicting files; use the master index for routing until a separately approved protocol exists |

