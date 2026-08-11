> # ⚠ CORRECTION NOTICE — READ BEFORE USING THIS DOCUMENT
>
> **Status of this document:** `SUPERSEDED — FACTUAL FINDINGS D.1 RETRACTED`
> **Correction issued:** 2026-08-04, same day, by the author of the original audit.
> **Original text preserved below unchanged.** Nothing has been deleted or silently rewritten.
>
> ## What was wrong
>
> The original audit **failed to distinguish two separate repository operations executed on 2026-08-04**:
>
> - **Operation 1** — the `01_CURRENT_CONTROL` reset (5 Git commits, 9 files archived);
> - **Operation 2** — a later Evidence Base consolidation (30 files modified, 6 created, 6 archived, **no Git commit**).
>
> The audit found only Operation 1. It then compared Operation 1's historical reports against the post-Operation-2 worktree and misread the resulting differences as reporting errors.
>
> ## Retracted findings
>
> | Retracted finding | Why it is wrong |
> |---|---|
> | **Decision-register count.** Claimed `CROSS_FILE_CONSISTENCY_AUDIT_20260804.md` misreported the register as 20 rows when it holds 26. | **Retracted.** The register grew from `D001-D020` to `D001-D026` *during Operation 2*. The count of 20 was correct when that audit ran. |
> | **`05_GATE2/` path.** Claimed `CURRENT_REPOSITORY_RESET_REPORT_20260804.md` cited a folder that never existed. | **Retracted.** The `05_GATE2/` layout existed at the time of Operation 1. Operation 2 relocated those files into `02_EVIDENCE_BASE/RQ2_GATES2_3/`. |
>
> Both archived reports were **accurate as at their own execution time**. Both were correctly superseded and archived by Operation 2 with byte-identical copies and recorded SHA-256 hashes.
>
> ## Locations affected by this retraction
>
> - **Section A** — the two "Conflicts found" cells for `G1_G2_INTERFACE_DECISION_REGISTER.csv` and `CURRENT_REPOSITORY_RESET_REPORT_20260804.md` are **void**.
> - **Section B** — table rows 1 and 2 (the two proposed corrections) are **void and were never executed**.
> - **Section D.1** — the entire subsection is **retracted**.
> - Sections C, D.2, E, F and G are unaffected.
>
> ## No action was taken on the false findings
>
> **No file was edited, moved, archived, committed or pushed on the basis of the retracted findings.** The proposed corrections were approved but halted before execution once Operation 2 was discovered.
>
> ## Corrected conclusion
>
> The current repository package is **coherent**, subject only to the normal unresolved Gate and governance items already recorded elsewhere — the 6 `BLOCKING_OPEN` interface decisions, the unaccepted `ADR_ACTION_STATUS_EVENT_20260804_DRAFT`, the pending `LIVING_EVIDENCE_BASE_v2.2` successor, and absent supervisor review. No outstanding factual reporting error is established.
>
> ## Authoritative sources
>
> For the repository update account, use:
>
> ```text
> 02_EVIDENCE_BASE/CURRENT/REPOSITORY_UPDATE_REPORT_20260804.md
> ```
>
> For the baseline acceptance decision, use:
>
> ```text
> 01_CURRENT_CONTROL/REPOSITORY_BASELINE_RETROSPECTIVE_APPROVAL_20260804.md
> ```
>
> This document is retained as an audit-trail record only. Do not cite Sections A, B or D.1 as current findings.

---

# REPOSITORY AUDIT AND CONTROLLED UPDATE PLAN — 2026-08-04
**Prepared by:** Claude Cowork, on request per `05_FIRST_RUN_PROMPT_20260804.md`
**Status:** `SUPERSEDED — FACTUAL FINDINGS D.1 RETRACTED` (see correction notice above). Original status line as issued: *AUDIT ONLY — NO FILE EDITED, MOVED, ARCHIVED, COMMITTED OR PUSHED BY THIS SESSION*

```text
RQ:      spans RQ1–RQ3 / WP1–WP4 (repository-wide governance audit, not a single RQ)
WP:      spans WP1–WP4
Chapter: spans C4–C7
Paper:   spans Paper 1–3
Gate:    G1, G2, G3 status review; no gate closure claimed or performed
Scope:   Information traceability / repository governance layer only
Deliverable: Audit + controlled update plan (sections A–G below) per the required output of 05_FIRST_RUN_PROMPT_20260804.md
```

## 0. Critical finding before the audit body

The repository already contains a completed governance reset dated **2026-08-04** (today), documented in `01_CURRENT_CONTROL/CURRENT_REPOSITORY_RESET_REPORT_20260804.md` and `CROSS_FILE_CONSISTENCY_AUDIT_20260804.md`. That reset already did what `05_FIRST_RUN_PROMPT_20260804.md` instructs this session to *stop short of*: it archived 9 documents, rewrote the governance/navigation set, and made 5 Git commits. No record in the repository shows a supervisor/user approval step between a proposed plan and that execution.

You asked me to review that reset for correctness rather than accept it. I did. Result: the reset's **scientific content and gate status are conservative and consistent** (nothing is falsely marked closed), but the reset's **own self-reported provenance contains verifiable errors**, and there is **no recorded approval trail**. Details in Section D.1.

This document therefore serves two purposes: (1) the audit and forward-looking update plan requested by the first-run prompt, now scoped to the **post-reset state**, and (2) an independent verification report on the reset itself, since it already happened.

---

## A. Current authority map

| File | Path | Status / authority | Conflicts found |
|---|---|---|---|
| `MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md` | `00_GOVERNANCE/` | Highest academic source of truth | None found |
| `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` | `00_GOVERNANCE/` | Source-of-truth level 1 — conflict-resolution control | Internally consistent; correctly points to `RQ2_GATES2_3/G2_G3_PAPER2_CURRENT_ROADMAP_v2.1_20260804.md` |
| `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md`, `EVIDENCE_GATES_v2.1.md` | `00_GOVERNANCE/` | Approved v2.1 structural set | Gate table is conservative — every G1–G7 item is `OPEN`/`EXECUTION-NOT-OPEN`; nothing overstated |
| `RESEARCH_ARCHITECTURE_DECISION_RECORD_ACTION_ID_20260719.md` | `00_GOVERNANCE/` | ACCEPTED ADR | Establishes `Action_Record_ID`; removes `Action_Status` from identifier chain |
| `ADR_ACTION_STATUS_EVENT_20260804_DRAFT.md` | `00_GOVERNANCE/` | **PROPOSED — NOT ACCEPTED** (explicitly labeled) | Correctly excluded from identifier-chain authority everywhere I checked |
| `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md` | `00_GOVERNANCE/` | Supervisor decision, Limited-FEM scope only | Its old identifier notation is explicitly superseded by the Action-ID ADR — declared, not silently overridden |
| `CURRENT_DIRECTION_LOCK_20260804.md`, `CURRENT_STATUS_AND_NEXT_DIRECTION.md`, `MASTER_INDEX_CURRENT.md` | `01_CURRENT_CONTROL/` | Current-direction/status/navigation set | Mutually consistent on G1/G2/G3/Paper 2 state |
| `G1_G2_INTERFACE_DECISION_REGISTER.csv` | `01_CURRENT_CONTROL/` | Current decision register (20 interface decisions) | **Does not match** the count claimed for it in `CROSS_FILE_CONSISTENCY_AUDIT_20260804.md` — see D.1 |
| `CURRENT_REPOSITORY_RESET_REPORT_20260804.md` | `01_CURRENT_CONTROL/` | Self-reported account of the reset | **Contains a path claim that does not match the filesystem** — see D.1 |
| `00_MASTER_INDEX_CURRENT_20260804.md`, `01_MASTER_G1_G2_G3_EVIDENCE_SYNTHESIS_20260804.md` | `02_EVIDENCE_BASE/CURRENT/` | Evidence Base single entry point and official synthesis | Consistent with governance set |
| `LIVING_EVIDENCE_BASE_v2.1_TRACEABILITY_CORE.md` | `02_EVIDENCE_BASE/CURRENT/` | `CURRENT_SUPPORTING` — historically current on 2026-07-19, superseded-as-sole-source | No successor `v2.2` yet created; correctly still marked as requiring the Round 1–3B overlay |
| `EVIDENCE_MIGRATION_REPORT_v2.1.md` | `02_EVIDENCE_BASE/CURRENT/` | `IMMUTABLE_EVIDENCE` | Untouched, as required |
| `G2_G3_SCREENING…` / `ROUND1` / `ROUND2` / `RECENT_EVIDENCE_SCREENING` / `ROUND3A` / `ROUND3B` | `02_EVIDENCE_BASE/RQ2_GATES2_3/` | `IMMUTABLE_EVIDENCE`, hash-recorded in the master index | Not independently re-verified byte-for-byte this session; index states hashes are recorded |
| `SUPERSEDED_DOCUMENT_REGISTER_20260804.csv` | `01_CURRENT_CONTROL/` | Archive/supersession register | Spot-checked 1 of 9 entries (Paper 2 old direction) — accurate |
| `90_ARCHIVE/BACKUP_BEFORE_CURRENT_RESET_20260804/` | `90_ARCHIVE/` | Pre-reset rollback snapshot | Referenced by hierarchy as the rollback path; existence not exhaustively verified this session |

**Not reviewed in depth (out of proportion for this pass, flagged for later):** `05_DATA_CODE_AND_EXPERIMENTS/` (G1 datasets/results), `06_LITERATURE_AND_ZOTERO/`, `07_PROMPTS_AND_HANDOFFS/`, `08_DEMO_AND_PROTOTYPES/`, and the bulk of `90_ARCHIVE/` (multiple prior snapshot generations from 2026-07-17/18/19). None of these carry current-governance authority per the hierarchy, so their omission does not affect gate status.

---

## B. Required updates

| Existing file | Current problem | Proposed update | Evidence basis | Needs approval? |
|---|---|---|---|---|
| `01_CURRENT_CONTROL/CROSS_FILE_CONSISTENCY_AUDIT_20260804.md` | States the decision register parses as "20 decisions: 4 LOCKED, 6 BLOCKING_OPEN, 9 OPEN, 1 DEFERRED." Actual file has 26 rows (D001–D026) including status values (`FREEZE` ×4, `FREEZE_PROVISIONALLY` ×2, `EXPERT_REVIEW_REQUIRED` ×1, `REMOVE` ×1, `LOCKED_STRUCTURALLY` ×1) the audit's tally never mentions. | Re-run the count against the live CSV and correct the QA table, or explain the discrepancy (e.g., CSV edited post-audit) before this file is trusted as a PASS record. | Direct read of both files, this session | Yes — factual correction, low risk, but should not be silently rewritten |
| `01_CURRENT_CONTROL/CURRENT_REPOSITORY_RESET_REPORT_20260804.md` §4 | Claims the roadmap and G1–G2 interface were moved/added under `../05_GATE2/...`. No `05_GATE2` folder exists anywhere in the repository. | Correct the report to state the actual location (`02_EVIDENCE_BASE/RQ2_GATES2_3/`), which is what `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` and `MASTER_INDEX_CURRENT.md` already correctly reference. | Glob confirmed `05_GATE2` absent; both governance files point to the real path | Yes — the report is evidence of what happened and should be accurate |
| Reset process generally | No file in `01_CURRENT_CONTROL/` records an explicit supervisor/user approval preceding the 5 commits and 9 archive moves, despite `05_FIRST_RUN_PROMPT_20260804.md` instructing agents to stop before exactly this kind of action, and CLAUDE.md §10 requiring explicit permission before commit/push. | Add an approval record (who approved, when, what was approved) to `01_CURRENT_CONTROL/`, or explicitly document that this reset was performed under standing/blanket authorization if one exists outside this repository. | Absence noted across all reset-control files read this session | Yes — supervisor/PhD-owner decision |
| `LIVING_EVIDENCE_BASE_v2.1_TRACEABILITY_CORE.md` | Per `02_SOURCE_OF_TRUTH_AND_READING_ORDER` and the file's own status, it is not sufficient alone post-Round-3B but no `v2.2` successor exists yet. | Create `LIVING_EVIDENCE_BASE_v2.2_20260804.md` per the 12-point update list already specified in `07_V2_1_UPDATE_NOTES_20260804.md`. Do not make it CURRENT until reconciled and approved. | `07_V2_1_UPDATE_NOTES_20260804.md`, `02_EVIDENCE_BASE/CURRENT/00_MASTER_INDEX_CURRENT_20260804.md` | Yes |
| G1_G2_INTERFACE_DECISION_REGISTER.csv, rows D004/D005/D007/D013/D014/D016 | 6 items are `BLOCKING_OPEN` and block G2 readiness review; D016 (competency questions) also blocks any G3 implementation. | No file edit — this is a to-do, not a document defect. Resolve via Stream B work (CQ Registry, ER model, expert review) before attempting G2 baseline. | `G1_G2_INTERFACE_DECISION_REGISTER.csv` | Supervisor/expert review per register |
| Three untracked root PDFs (`applsci-16-04642.pdf`, `buildings-15-01312.pdf`, `buildings-15-02633.pdf`) | Appeared after the pre-reset inventory; explicitly left unclassified by the reset. | Classify (which Gate folder, which round) and file appropriately; not urgent, does not block G1/G2/G3. | `CURRENT_REPOSITORY_RESET_REPORT_20260804.md` §7 | No — routine filing |

---

## C. Archive candidates

None identified beyond what the 2026-08-04 reset already archived. The `SUPERSEDED_DOCUMENT_REGISTER_20260804.csv` already lists 9 files moved to `90_ARCHIVE/CURRENT_RESET_20260804/` with hash verification (1 spot-checked and confirmed accurate this session). I am not proposing additional archiving:

- No immutable evidence (Round 1–3B, screening report, EVIDENCE_MIGRATION_REPORT_v2.1) is a candidate — CLAUDE.md and the source-of-truth hierarchy both prohibit archiving/rewriting these.
- No accepted ADR is a candidate.
- The 6 `CURRENT_CONTROL_HISTORY` files and the old Paper 2 direction file already archived look correctly classified (dated, explicitly superseded, byte-identical copies retained).

---

## D. Evidence reconciliation

### D.1 Independent verification findings (new this session)

**Claim:** The 2026-08-04 reset's self-QA (`CROSS_FILE_CONSISTENCY_AUDIT_20260804.md`) is fully reliable as a PASS record.
**Evidence:** Direct comparison of the audit's decision-register tally against the live `G1_G2_INTERFACE_DECISION_REGISTER.csv`, and of the reset report's stated file destinations against an actual directory listing.
**Limitation:** Two concrete mismatches found:
1. The audit reports the decision register as 20 rows with a specific status tally; the live file has 26 rows with 5 status values absent from that tally.
2. The reset report states files were placed under `05_GATE2/...`; that folder does not exist, and the governance files that actually control navigation (`SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`, `MASTER_INDEX_CURRENT.md`) correctly reference the real path instead.
Neither issue changes gate status (both G2 and G3 remain correctly `OPEN`/`NOT OPEN` everywhere), and the actual governance/navigation files I checked are internally consistent with each other — only the *narrative* documents about the reset (the report and its own QA) contain the errors.
**Next action:** Correct or annotate the two source documents (Section B); do not treat `CROSS_FILE_CONSISTENCY_AUDIT_20260804.md`'s "PASS" as a substitute for independent QA on future resets.

**Claim:** The reset was authorized before execution, consistent with `05_FIRST_RUN_PROMPT_20260804.md`'s stop-before-execution instruction and CLAUDE.md §10.
**Evidence:** No approval record, decision-authority note, or reference to a prior plan-approval exchange exists in any `01_CURRENT_CONTROL/` file read this session.
**Limitation:** Absence of evidence is not evidence of absence — approval may have happened in a session/channel outside this repository's file record.
**Next action:** You confirmed you're not sure this was approved. Recommend explicitly recording the approval (or lack of it) now, since it affects how much trust to place in unattended agent runs going forward.

### D.2 Required reconciliations from `05_FIRST_RUN_PROMPT_20260804.md`

| Item | Position found in repository |
|---|---|
| v2.1 full-text acquisition list vs. 2026-08-04 search-closure | Reconciled correctly: `CLOSE_SEARCH` is stated as corpus-bounded everywhere (Status, Lock, Hierarchy, Gates), never as universal absence or G2 PASS. |
| `Action_Record_ID` vs. `Action_Status` | Reconciled: ACCEPTED Action-ID ADR ends the identifier chain at `Action_Record_ID`; `Action_Status`/`Workflow_Status` is consistently described as a current-state projection, not an identifier, across all current-direction files. |
| Current status vs. `Status_Event` | Reconciled: append-only `Status_Event` is "structurally frozen" per the decision register (D015 area) but exact vocabulary is `EXPERT_REVIEW_REQUIRED` — correctly not claimed as accepted. |
| Reverse lookup vs. parity | Reconciled: D025 explicitly states "Reverse lookup is not round-trip parity"; paired forward/reverse CQ contract is `FREEZE` (specification-level), not validated. |
| Generic provenance verification vs. post-action verification | Reconciled: D022 keeps these distinct; post-action verification requirement is `FREEZE`, exact criteria remain expert-review-required. |
| G2 literature closure vs. G2 Gate PASS | Reconciled everywhere: G2 is `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN`, never PASS. |
| G2 specification vs. G3 execution | Reconciled: G3 status is `EXECUTION-NOT-OPEN` in `EVIDENCE_GATES_v2.1.md`; "Do not run Graph 02" is stated in three separate current files (D019, Direction Lock §5, Status §4). |
| G1 priority vs. parallel G2 specification work | Reconciled: `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §5 explicitly authorizes three parallel streams (G1 closure, G2 specification, G4 readiness) without subordinating G1's priority. |

No reconciliation conflicts found in D.2 — this part of the reset appears to have been done carefully. The problems are confined to the two narrative-accuracy issues in D.1.

---

## E. Proposed current package

No new "current" files are proposed beyond what Section B already calls for (a corrected reset report, a corrected QA audit, an approval record, and eventually `LIVING_EVIDENCE_BASE_v2.2`). The existing current package — Charter → Source-of-Truth Hierarchy → structural v2.1 set → current-direction lock/status/roadmap/Paper-2-direction → Evidence Base entry point — is coherent and should remain the package. I am not proposing to consolidate or rename anything further; doing so would create exactly the kind of uncontrolled duplication CLAUDE.md prohibits.

---

## F. Gate table

| Gate | Status | Evidence | Missing deliverable | Next action |
|---|---|---|---|---|
| G1 | `OPEN — PARTIAL EVIDENCE` | Method addendum, three-campaign reanalysis artifacts (provisional) | Canonical run registry, sensor provenance, leakage-safe multi-seed LORO, ResNet1D provenance decision, run/fold uncertainty, signed acceptance matrix | Execute Stream A per `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §5 |
| G2 | `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN` | Round 1–3B immutable evidence, G2 Final Decision Register (26 items, 6 `BLOCKING_OPEN`) | ER model, CQ Registry with expected answers, Constraint Catalogue, Fixture/Oracle Manifest, expert review, ADR acceptance, baseline sign-off | Resolve the 6 `BLOCKING_OPEN` interface decisions first (D004, D005, D007, D013, D014, D016) |
| G3 | `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED`; execution `EXECUTION-NOT-OPEN` | Planned validation families and fixture design only | Everything — no implementation authorized until G2 baseline | Do not begin; do not run Graph 02 |
| G4 | `OPEN` | Field precedents, candidate BIM/asset resources | Field-access confirmation, sensor register, mapping, baseline, 2–3 field scenarios | Readiness prep only, in parallel, per Stream C |
| G5 | `OPEN` | Human-governance rationale (4-level logic design) | Expert/facility-manager review, no-automated-decision confirmation | Not started; not blocking G1–G3 |
| G6 (Paper 2 submission) | `OPEN` | — | Everything downstream of G2/G3 | Not applicable yet |
| G7 (Thesis synthesis / Paper 3) | `OPEN` / `N/A-until-G4` | — | Everything | Not applicable yet |

No gate is closed by this audit or by the prior reset. This matches what both the reset report and the governance files themselves claim.

---

## G. Stop point

This session has not edited, moved, archived, committed, or pushed any file. The two document-accuracy fixes and the approval-record request in Section B are **proposed**, not executed. Please tell me which of the following you want next:

1. Approve the Section B corrections (register-count fix in the QA audit, path fix in the reset report, add an approval record) and I'll make exactly those edits, nothing else.
2. Treat the 2026-08-04 reset as accepted baseline as-is (accuracy issues noted but not fixed) and move directly to Stream A/B substantive work (G1 run registry, or G2 `BLOCKING_OPEN` decisions).
3. Something else — e.g., you want the deeper file-by-file audit of `05_DATA_CODE_AND_EXPERIMENTS/` and `90_ARCHIVE/` that this pass deliberately did not do.
