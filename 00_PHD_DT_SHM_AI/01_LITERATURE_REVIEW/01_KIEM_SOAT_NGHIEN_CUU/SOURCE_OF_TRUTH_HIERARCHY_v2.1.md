# SOURCE OF TRUTH HIERARCHY v2.1

**Version:** v2.3 current-direction consolidation
**Effective date:** 11/08/2026 | **Updated:** 11/08/2026
**Status:** CURRENT | **Source-of-truth level:** 1 (conflict-resolution control)
**Supersedes:** v2.2 administrative hierarchy. | **Superseded by:** None.
**Changes in this version:** Restores the 17/07 control baseline and canonical chains; later action/event records remain subordinate proposals where they conflict.
**Purpose:** Provide one conflict-resolution order and prevent historical, discovery, or implementation files from becoming accidental research authority.

## 1. Authority Order

When documents conflict, apply this order from highest to lowest:

1. Supervisor decision of 2026-07-17 (Verdict B), recorded unchanged in `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md`.
2. `../02_EVIDENCE_BASE/06-MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` and `../02_EVIDENCE_BASE/08-RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md` (ADR-2026-001).
3. The current synchronized structural set: `MASTER_RESEARCH_CHARTER.md`, `MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`, `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md`, `EVIDENCE_GATES_v2.1.md`, `TERMINOLOGY_CONTROL_CURRENT.md`, and `AGENT_RULES.md`. The 19/07 Action-ID and 04/08 event records are noncanonical proposals where they conflict with items 1–2.
4. The current-direction control set: `../01_CURRENT_CONTROL/CURRENT_DIRECTION_LOCK_20260804.md`, `../02_EVIDENCE_BASE/RQ2_GATES2_3/G2_G3_PAPER2_CURRENT_ROADMAP_v2.1_20260804.md`, `../03_PAPERS/PAPER_2/PAPER2_CURRENT_DIRECTION_v2.1_20260804.md`, and `../02_EVIDENCE_BASE/RQ2_GATES2_3/G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md`.
5. Current navigation and status: `../02_EVIDENCE_BASE/CURRENT/00_MASTER_INDEX_CURRENT_20260804.md`, `../01_CURRENT_CONTROL/MASTER_INDEX_CURRENT.md`, `../01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md`, `RESEARCH_DIRECTION_AND_SCOPE.md`, and `RESEARCH_ARCHITECTURE.md`.
6. Accepted gate evidence and signed gate decisions, in the evidence order defined in Section 3.
7. Current evidence bases, working specifications, paper packages and decision registers. Conflicting later ADRs and the 04/08 synthesis are recoverable historical records under `../99_TRASH_SUPERSEDED_20260811/`.
8. Supporting literature, discovery outputs, prompts, demos, and IT handoffs. These do not override governance or constitute gate evidence by themselves.
9. Review-required material, repository logs, backups, and archives. These are never current sources of truth.

The current-direction set in item 4 narrows execution and resolves navigation drift; it does not amend the Charter or create a new RQ, WP, chapter, paper, or gate.

## 2. Locked Direction

```text
Vibration data
-> condition/state-change evidence
-> BIM-linked component
-> inspection record
-> inspection-maintenance action support
```

```text
Sensor_ID
-> BIM_GUID
-> Condition_Evidence_ID
-> Inspection_Record_ID
-> Action_Status
```

`Action_Status` is the canonical endpoint. `Asset_ID`, `Model_Version_ID`, `Action_Record_ID`, `Workflow_Status` and `Status_Event` are noncanonical implementation metadata/proposals unless separately approved. CEI is structured evidence metadata, not a scalar, Health Index, severity, damage probability or priority.

FEM is **nominal, uncalibrated, reference-only, not used for damage diagnosis**.

## 3. Gate Evidence Order

For every gate claim, evidence must be read in this order:

1. Gate definition and acceptance criteria in `EVIDENCE_GATES_v2.1.md`.
2. Approved preregistration, specification, schema, or protocol.
3. Immutable input/provenance records and version identifiers.
4. Executed implementation artifacts and test outputs.
5. Validation evidence, including required positive, negative, integrity, and round-trip tests.
6. Reviewer decision and signed gate acceptance record.
7. Paper claim or submission record.

A planned filename, schema draft, report, demo, code run, Revit model, IFC file, Dynamo graph, Pset, IDS, SQLite database, or website is not sufficient to close a gate. Gate status changes only through the defined acceptance and sign-off record.

## 4. Current State Constraints

| Item | Locked state |
|---|---|
| G1 | `OPEN — PARTIAL EVIDENCE` |
| G2 | `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN` |
| G3 | `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED`; execution authorization `NOT OPEN` |
| Paper 2 | `DESIGN AND EVIDENCE DEVELOPMENT` |

Paper 2 is one paper covering G2 specification and, only after G2 readiness, G3 executed validation. Paper 2A, Paper 2B, and dual-paper roadmap commitments are superseded.

The literature decision is `CLOSE_SEARCH`, bounded to the screened/deep-read corpus. It is not universal absence, does not support a "first" claim, and may be reopened only for a new question likely to change the structural novelty boundary.

## 5. Historical and Superseded Material

- Charter v2.0 is a historical decision source only.
- The 17/07 Limited-FEM Charter, ADR-2026-001 and Council Review are active control records and must not be modified as historical prose.
- Files in `90_ARCHIVE/`, `91_REVIEW_REQUIRED/`, `99_REPOSITORY_LOGS/`, and `output/` cannot override current governance.
- Superseded documents are recorded in `../01_CURRENT_CONTROL/SUPERSEDED_DOCUMENT_REGISTER_20260804.csv` and `../02_EVIDENCE_BASE/90_ARCHIVE_SUPERSEDED/20260804/MANIFEST/ARCHIVE_MANIFEST_20260804.csv`, and preserved in a controlled archive.
- The pre-reset rollback snapshot is `../90_ARCHIVE/BACKUP_BEFORE_CURRENT_RESET_20260804/`.
- Do not delete uncertain, unique, empirical, or historical evidence. Hard deletion requires byte identity, SHA-256 proof, a retained canonical copy, and a verified backup.

## 6. Conflict Rule

When a lower-ranked file conflicts with a higher-ranked file:

1. follow the higher-ranked file;
2. record the conflict or open decision;
3. do not silently merge incompatible claims;
4. archive a superseded control document rather than rewriting historical evidence; and
5. state `Evidence is currently insufficient` when the required execution evidence does not exist.
