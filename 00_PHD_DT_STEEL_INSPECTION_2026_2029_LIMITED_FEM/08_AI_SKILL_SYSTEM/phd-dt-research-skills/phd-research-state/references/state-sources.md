# Reference — Where research state lives, and in what order to read it

**v1.0 · 2026-08-10.** Paths relative to the thesis root `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/`.

---

## Read order

Stop as soon as the question is answered. Most status questions are answered by step 1 alone.

| # | File | Answers |
|---|---|---|
| 1 | `01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md` | Gate statuses, current direction, active workstreams, evidence limitation. **Source-of-truth level 5 — the execution state.** |
| 2 | `01_CURRENT_CONTROL/CURRENT_DIRECTION_LOCK_20260804.md` | What is locked and may not drift |
| 3 | `00_GOVERNANCE/EVIDENCE_GATES_v2.1.md` | Gate items, required artifacts, acceptance criteria, sign-off. **Level 4.** |
| 4 | `02_EVIDENCE_BASE/CURRENT/00_MASTER_INDEX_CURRENT_20260804.md` | What evidence exists and how it is classified |
| 5 | `00_GOVERNANCE/MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md` | Permitted and prohibited claims, scope, contributions. **Highest source of truth.** |
| 6 | `00_GOVERNANCE/RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md` | RQ → WP → Chapter → Paper → Gate mapping |
| 7 | `00_GOVERNANCE/AGENT_RULES.md` | Operating rules, prohibited expansions, output discipline. **Level 4.** |
| 8 | `00_GOVERNANCE/TERMINOLOGY_CONTROL_CURRENT.md` | Permitted and forbidden terms |
| 9 | `01_CURRENT_CONTROL/MASTER_INDEX_CURRENT.md` | Navigation across the repository |

**When files conflict:** `00_GOVERNANCE/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` decides. Report the conflict; do not harmonise it silently.

## Compact context

`CLAUDE_COWORK_PHD_PROJECT_SETUP_20260804/01_CURRENT_RESEARCH_CONTEXT_20260804.md` carries the thesis identity, RQ/WP/Gate table, Paper 2 direction, current novelty boundary and the current priority list in two pages. Useful as an orientation read, but for gate status quote file 1 or 3, which are the governing records.

## Per-gate evidence locations

| Gate | Evidence path |
|---|---|
| G1 | `02_EVIDENCE_BASE/RQ1_GATE1/`; artifacts in `05_DATA_CODE_AND_EXPERIMENTS/` (`CANONICAL_THREE_CAMPAIGN_DATASET/`, `THREE_CAMPAIGN_REANALYSIS/`); execution pack at `05_DATA_CODE_AND_EXPERIMENTS/G1_EXECUTION_PACK/` when created |
| G2 / G3 | `02_EVIDENCE_BASE/RQ2_GATES2_3/` — Rounds 1–4, screening reports, roadmap, `G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md` |
| G4 | `02_EVIDENCE_BASE/RQ3_GATE4/` |
| G5 | `02_EVIDENCE_BASE/WP4_GATE5/` |

## Papers

- `03_PAPERS/PAPER_1/` — direction, current manuscript, `GATE1_EVIDENCE/`, `IT_REQUESTS/`, `REVISION_HISTORY/`, internal QA checklist
- `03_PAPERS/PAPER_2/PAPER2_CURRENT_DIRECTION_v2.1_20260804.md`
- `03_PAPERS/PAPER_3/PAPER3_FIELD_FEASIBILITY_DIRECTION_v2.1_20260719.md`

## Decisions and ADRs

- `00_GOVERNANCE/ADR_ACTION_STATUS_EVENT_20260804_DRAFT.md` — **`PROPOSED — NOT YET ACCEPTED`**
- `00_GOVERNANCE/RESEARCH_ARCHITECTURE_DECISION_RECORD_20260719.md`
- `00_GOVERNANCE/RESEARCH_ARCHITECTURE_DECISION_RECORD_ACTION_ID_20260719.md`
- `01_CURRENT_CONTROL/REPOSITORY_BASELINE_RETROSPECTIVE_APPROVAL_20260804.md`

## Never treat as current

`90_ARCHIVE/`, `02_EVIDENCE_BASE/90_ARCHIVE_SUPERSEDED/`, and any `92_ARCHIVE_SUPERSEDED_FILES`. These are preserved for provenance. Quoting a superseded status as current is a defect, and it is an easy one to make because the archived files look identical to the live ones.

## Reporting a status

Always give the status **verbatim**, with the file it came from and that file's `Updated:` date. Statuses in this repository are precise strings (`OPEN — PARTIAL EVIDENCE`, `EXECUTION-NOT-OPEN`) and paraphrasing them loses the distinction they were written to preserve.
