# RESEARCH ARCHITECTURE DECISION RECORD — LIMITED-FEM
**ADR ID:** ADR-2026-001
**Date of decision:** 2026-07-17
**Status:** ACCEPTED — approved by both supervisors on 17/07/2026
**Decision source:** THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md (Verdict B)

## Decision

Adopt **Option B — Limited-FEM Architecture**: FEM is demoted from a core research axis to a limited supporting tool (nominal, uncalibrated, reference-only). The thesis skeleton is the non-FEM architecture: vibration data → condition evidence → BIM-linked component → inspection record → inspection-maintenance action support.

Options considered: A (FEM core) — rejected; B (FEM limited support) — accepted; C (FEM fully removed) — rejected.

## Rationale for removing FEM from the core

1. A core FEM axis imposes a "calibrated FEM baseline with acceptance criteria" evidence gate requiring independent EMA, connection-stiffness quantification, MAC criteria, and dynamic similitude from 1:10 to full scale — obligations not satisfiable with remaining PhD time and resources, and a predictable line of attack for a structural examiner (council red-team questions 4.1.1–4.1.10).
2. A calibrated 1:10 FEM contribution is incremental within Structural Engineering and pulls the thesis away from its Construction Management discipline.
3. Council scoring: A=28, B=40, C=38 across ten criteria; defense risk of A rated lowest (1–2/5) on verifiability and technical-risk criteria.

## Rationale for not removing FEM entirely (why B, not C)

1. Paper 1 reporting publicly promised mechanical follow-up on two anomalies (BCJ collapse under S2; Apex↔BCJ confusion); C would orphan them.
2. The provincial project commits to a "reference FEM" deliverable and mechanically informed sensor positions; C creates an academic-consistency conflict.
3. A nominal design model is the cheapest defensible basis for field sensor-placement justification (standard industry practice).

## What FEM may still do (permitted)

- Serve as a nominal, uncalibrated design reference model.
- Provide reference-informed justification of field sensor placement.
- Illustrate component locations.
- Support qualitative mechanical hypotheses for Paper 1 anomalies in Discussion/Limitation sections, labelled "hypothesis, not confirmed."
- FEM node mapping may exist as optional metadata only.

## What FEM must not do (prohibited)

- Be calibrated, or be described as calibrated.
- Diagnose damage or infer stiffness degradation / bolt preload.
- Transfer quantitative conclusions from the 1:10 model to the real building.
- Have its own RQ, WP, thesis chapter, paper, or evidence gate.
- Appear in the name of any RQ, WP, chapter, paper, or evidence gate.
- Be a required link in the identifier chain (FEM_Node_ID demoted to optional metadata).
- Anchor claims such as "physics-informed condition evidence" or "optimal sensor placement."

## Known risk and control

Risk: "zombie FEM" — any FEM mention invites "was it calibrated? what is the MAC?" Control: absolute language discipline (every FEM mention carries "nominal, uncalibrated, reference-only, not used for damage diagnosis"); FEM confined to one methods subsection (C3) and Limitation sections; prohibited-claims list in the Charter §14; TERMINOLOGY_CONTROL_v1.1.md enforcement.

## Files affected by this decision

| File | Effect |
|---|---|
| 00_SYSTEM/MASTER_CHARTER.md | SUPERSEDED by MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md; archive copy in 92_ARCHIVE_SUPERSEDED_FILES |
| 02_GATE_MATRICES/Updated_RQ_Evidence_Gate_Matrix.csv | SUPERSEDED by RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v1.1.md and EVIDENCE_GATES_v1.1_LIMITED_FEM.md |
| 01_CORE_REPORTS/Unified_Literature_Evidence_Gate_Update_20260710.md | SUPERSEDED (old chain); evidence content reused |
| 01_CORE_REPORTS/Research_Direction_Evidence_Justification_Report_20260710.md | SUPERSEDED (FEM layer no longer core); evidence content reused |
| 03_PAPER_SPECIFIC/Paper2_Gate3/Paper2_Literature_Boundary_Table.md | Demoted to supporting reference (qualitative hypotheses only); Paper 2 redefined by PAPER2_CONCEPT_NOTE_TRACEABILITY_v1.0_20260717.md |
| 03_PAPER_SPECIFIC/Paper3_Gate4/Paper3_Traceability_Gap_Table.md | Content largely transfers to new Paper 2; Paper 3 reoriented to field feasibility |
| 04_RQ_EVIDENCE_ADDENDA/PX_RQ2_FEM_Loosening_Evidence.md | Reclassified SUPPORTING_REFERENCE |
| 04_RQ_EVIDENCE_ADDENDA/PX_RQ3_BIM_FEM_Sensor_Evidence.md | Retagged to new RQ2/Paper 2 |
| 06_LIVING_EVIDENCE_BASE/Literature_Evidence_Living.md | SUPERSEDED by LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md; preserved as historical record |
| 04_AI_SYSTEM/AGENTS/AGENT_RULES.md | UPDATE_REQUIRED (flagged; not modified without user approval) |
| 04_AI_SYSTEM/AGENTS/RESEARCH_CHARTER.md | REVIEW_NEEDED (not audited in this migration) |

## Consequences

Positive: removes unfulfillable proof obligations; aligns thesis with Construction Management; single research axis (evidence → traceability → decision); frees schedule for LORO, ResNet1D verification, and field work. Negative/accepted: Paper 2 (traceability) has a "system integration" perception risk — mitigated by pre-registered competency questions and formal schema (see PAPER2_CONCEPT_NOTE §13–14); DT terminology debate ("twin without physics") — mitigated by an explicit DT maturity definition in C3.

## Non-derivable items (insufficient evidence — do not assume)

Program regulations on required technical content; actual defense-council composition; ResNet1D sensor mode; LORO stability on 6 runs; field-access agreement status. Tracked in 99_REVIEW_NEEDED/UNRESOLVED_ITEMS_AFTER_LIMITED_FEM_MIGRATION.md.
