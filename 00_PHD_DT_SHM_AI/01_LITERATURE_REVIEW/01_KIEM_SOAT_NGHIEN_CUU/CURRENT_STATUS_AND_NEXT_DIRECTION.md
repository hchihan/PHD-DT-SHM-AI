# CURRENT STATUS AND NEXT DIRECTION

**Version:** v2.4
**Effective date / Updated:** 13/09/2026
**Status:** CURRENT SOURCE OF EXECUTION STATUS | **Source-of-truth level:** 5
**Scope:** Execution state of the whole thesis after the Paper 1 science lock: Paper 1 status, the gap to formal G1 closure, and execution priorities P1–P3.
**Supersedes:** v2.3 (11/08/2026), retained at `../90_ARCHIVE/01_SUPERSEDED_VERSIONS/PRE_SYNC_20260913/01_CURRENT_CONTROL/`. | **Superseded by:** None.
**Changes in this version:**
- Records the Paper 1 science lock (manuscript v8.1, 13/09/2026) and the G1 evidence audits of 19/08–12/09/2026. No Gate status changes.
- Adds the WP1 → WP2 handover rule.
- Replaces the three parallel workstreams with priorities P1–P3.

Synchronization record: `PAPER1_SCIENCE_LOCK_PROJECT_SYNC_REPORT_20260913.md`.

## 1. Locked Status

| Item | Current state | Meaning |
|---|---|---|
| Paper 1 | `SCIENCE LOCKED — NOT SUBMISSION-READY — NOT SUBMITTED` | The scientific content of `PAPER1_v8.1_SHM_RISK_REDUCED.docx` is locked. Target journal: Structural Health Monitoring (SAGE). The pre-submission audit found no scientific blocker. Remaining items are author-side: metadata, figure approval, declarations and the data-availability decision. Under Milestone M1, submission readiness also requires G1 closure or an explicit written supervisor exception. Supervisor confirmation of the science lock itself: **Evidence is currently insufficient.** |
| G1 | `OPEN — PARTIAL EVIDENCE` | The laboratory evidence behind Paper 1 has been executed and audited (IT-01–IT-06, 12/09/2026). The repository-resident `G1_EXECUTION_PACK` has not been materialized, and no signed `G1_ACCEPTANCE_MATRIX.md` exists. **Evidence is currently insufficient** to record G1 as CLOSED. |
| G2 | `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN` | Round 1–3B closes the corpus-bounded structural search. The required specification artefacts, review and baseline are missing. |
| G3 | `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED` | Execution authorization is `NOT OPEN` until G2 is baselined and explicitly accepted. |
| G4 | `READINESS/PREPARATION ONLY — FIELD ACCESS UNCONFIRMED` | Literature support exists. No accepted field-access or field traceability evidence pack exists. |
| G5 | `OPEN — NOT A CURRENT PRIORITY` | Expert-reviewed decision-support evidence is missing. No G5 work is scheduled under P1–P3. |
| Paper 2 | `DESIGN AND EVIDENCE DEVELOPMENT` | One paper will report the G2 specification and, later, the executed G3 validation. |

No gate is closed by this update. Supervisor materials use the wording "Gate 1 evidence package: scientifically ready; awaiting supervisor review and formal sign-off". That wording describes the evidence, not the gate state.

## 2. Current Direction

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

- `Action_Status` is the canonical endpoint.
- `Asset_ID`, `Model_Version_ID`, `Action_Record_ID`, `Workflow_Status` and `Status_Event` remain noncanonical implementation proposals unless separately approved.
- CEI remains structured evidence metadata. It cannot be converted into a scalar, Health Index, severity, damage probability or priority without approved evidence and governance.

## 3. Paper 1 Science Lock: What RQ1/WP1 Produced

Evidence type: **Laboratory evidence** only. Until G1 PASS, governance documents cite every result below as "Candidate claim pending Gate 1 closure."

- **Dataset.**
  - 3 campaigns: CP1 on 25/04, CP2 on 21/07 and CP3 on 29/07/2026.
  - 18 acquisition runs and 216 recordings (72 per campaign, 18 per class).
  - 6,899 windows of 400 samples, step 200, at 100 Hz.
  - 216 unique source SHA-256 values and 102 NPZ artefacts reconciled with the registry (IT-01).
- **Evaluation.**
  - Whole-run partitioning: 4 training runs, 1 validation run and 1 test run, with all 30 ordered validation–test combinations per case.
  - Windows are cut within recordings, and no window crosses the split.
  - Scoring is at recording level, from mean window probabilities.
  - Candidate selection uses validation quantities only. Within the audited scope, 192 stored candidate selections were reproduced from validation quantities alone, and 612 deep-model checkpoints were reproduced.
  - Executed fits for the reported models: 540 / 180 / 72 (manuscript Table 3).
- **Models.**
  - Untuned random forest and RBF support vector machine (25 features per channel; 228 or 366 dimensions).
  - 1D-CNN and ResNet1D, seeds 42/43/44.
  - ResNet1D is **retained**. Its sensor and input mode are technically verified (audits of 24/08 and 07/09/2026).
- **Primary result.** Pooled Macro-F1 under LORO with recording-level scoring:
  - RF / SVM: 1.000 / 1.000 in CP1, 0.986 / 0.986 in CP2, 0.875 / 0.690 in CP3.
  - SD_fold in CP3 reaches 0.139.
  - The deep models ranked lower in every campaign and carry a disclosed dependence on hyperparameter development.
- **Transfer.**
  - Exploratory CP2 ↔ CP3 transfer, with deep models only, gave mean balanced accuracy of 0.227–0.278.
  - This does not establish validated transfer. CP1 transfer was not evaluated.
  - No LOCO protocol was executed.
- **Contribution wording.**
  - The evaluation controls and their combination are not claimed as novel.
  - The contribution is an experimentally documented consequence: within-campaign separability did not establish transferable condition evidence. A classification output therefore needs its provenance, protocol and observed variability before it can be used as condition evidence.
- **Not claimed.**
  - Dominance of sensor configuration over model architecture (moved to Paper 1B; not supported by current evidence).
  - Model-family superiority.
  - Field diagnosis, severity, stiffness, preload or lab-to-field transfer.

**Limitations** (manuscript §4.1 and §5.6):
- 18 runs on one specimen.
- The run is an acquisition grouping unit, not a verified independent experimental unit.
- The deep-model hyperparameter pool contained the test run in 15 of 18 folds and in all transfer cases.
- RF and SVM were run at a single seed.
- Within-campaign results are compared with theoretical chance only.
- No random-split comparator was run.
- The campaigns are not replicates, and state acquisition order was not randomised.
- Three provenance items remain unverified: training-time file identity, the physical sensor-to-position mapping and pre-export synchronisation.
- Per-window probabilities were not archived.

## 4. WP1 → WP2 Handover

```text
Vibration data
-> Condition Evidence
-> provenance + validity scope
-> BIM-linked component traceability
```

1. Paper 2 does not take raw AI predictions as unconditional ground truth. A prediction becomes `Condition_Evidence` only when provenance, validity scope and uncertainty are attached (CEI lock).
2. Until G1 is signed, records derived from Paper 1 may be used only as `CANDIDATE`/`DRAFT` instances for G2 specification and fixture design. Both eligibility flags remain false (`../02_DEEP_READ_CURRENT_PDF/03_RQ2_GATE2_3/G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md` §15). No accepted handoff exists.
3. Model probabilities are not damage probabilities. State labels denote manipulated locations, not severity.
4. The laboratory `Sensor_ID → BIM_GUID` link is candidate-only, because physical Sensor_ID identity is unverified (decision D005).

## 5. Paper 2 Boundary

- Paper 2 is the single current RQ2 publication direction.
- G2 supplies the preregistered specification and acceptance basis.
- G3, when opened, supplies executed end-to-end validation and negative-test evidence.
- Paper 2A, Paper 2B, dual-paper, and split-roadmap commitments are superseded.
- Paper 2 does not claim field damage diagnosis, autonomous action, predictive maintenance, RUL, calibrated FEM, or a universal Health Index.

**Literature decision:** `CLOSE_SEARCH`.
- The decision is bounded to the screened and deep-read corpus. It is not universal absence, does not authorize a "first" claim, and does not close G2.
- Reopen broad search only if a new question is likely to change the structural novelty boundary.

## 6. Instrument Boundary

Revit, IFC, Dynamo, Pset, IDS, SQLite, and any viewer are supporting implementation instruments. Their presence or execution is not the novelty. It cannot substitute for traceability completeness, provenance, integrity validation, human review, or gate acceptance. **Do not run Graph 02.**

FEM is **nominal, uncalibrated, reference-only, not used for damage diagnosis**. FEM was not used in Paper 1.

## 7. Current Priorities (replace the v2.3 three-stream work order)

### P1 — Finalize the Literature Review report (Báo cáo tiểu luận tổng quan)

Apply the update list in `PAPER1_SCIENCE_LOCK_PROJECT_SYNC_REPORT_20260913.md` §6.4 to `../03_OUTPUTS/01_TIEU_LUAN_TONG_QUAN/TIEU_LUAN_TONG_QUAN_HOAN_CHINH_v2_13092026.docx`, then submit for supervisor review. Do not rewrite unrelated content.

### P2 — Gate 2–3

1. **Formal traceability model.** Conceptual entities, relations and identifiers on the canonical chain, with CEI metadata. No schema build or freeze at this step.
2. **Competency questions and verification criteria.** Preregistered and approved.
3. **Identifier and integrity rules.** Constraint catalogue; resolve decisions D003–D017.
4. **Valid and invalid fixtures.** Only after the competency questions are approved.
5. **Bidirectional and end-to-end validation.** This is G3; execution is `NOT OPEN` until the G2 baseline is accepted. **Do not run Graph 02.**

### P3 — Gate 4 field preparation (preparation only)

1. Sensor_ID register.
2. BIM_GUID mapping protocol and GUID-stability audit.
3. Installation and provenance metadata template: device serial, mounting position, axis orientation, synchronisation and load-time hashes.
4. Operational-baseline protocol.
5. Field traceability feasibility scenarios (2–3).

Baseline acquisition and deployment remain conditional on confirmed field access and on G4 opening.

### Carried administrative items (run in parallel; do not displace P1–P3)

- **G1 formal closure.**
  - Materialize `G1_EXECUTION_PACK` from existing artefacts, without new analysis.
  - Obtain supervisor decisions C-04, C-05 and C-06 (sync report §5).
  - Sign `G1_ACCEPTANCE_MATRIX.md`.
- **Paper 1.** Complete the author-side items. Submit only after G1 sign-off or an approved exception.

### Not current

- G5 scenario review.
- New Paper 1 analyses (RF/SVM cross-campaign transfer, additional seeds, within-campaign permutation), unless separately authorized.

## 8. Evidence Limitation

**What the repository contains:**
- The science-locked Paper 1 manuscript and its audits.
- Substantial design evidence: Round 1–3B synthesis, Round 4 selected-page verification, and the 09–11/08 screening and audit records.

**What it does not contain:**
- An accepted G1 execution pack.
- An approved and baselined G2 package.
- An executed G3 validation package.
- An accepted G4 field pack.

Key Paper 1 evidence resides outside the repository at `D:\01_RESEARCH\08_Output_07.09\`: the Kaggle output bundles, the built NPZ dataset and the 07/09 audit set. The IT-01–IT-06 deliverable files are not stored in the project. **Evidence is currently insufficient** to claim G1, G2, G3, G4 or G5 completion.

Other open items:
- Legal and management-obligation references remain pending official-source verification.
- Field-access evidence remains unresolved for G4.

The 17/07 canonical identifier chain ending in `Action_Status` controls current documents.
