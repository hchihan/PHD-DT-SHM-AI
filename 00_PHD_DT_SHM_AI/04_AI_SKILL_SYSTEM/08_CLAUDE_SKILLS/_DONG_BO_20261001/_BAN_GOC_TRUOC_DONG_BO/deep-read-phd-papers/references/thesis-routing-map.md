# Thesis routing map

Snapshot basis: `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` and `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md`. Current supplied source-of-truth files override this snapshot.

## Locked chain

`Vibration data → condition/state-change evidence → BIM-linked component → inspection record → inspection-maintenance action support`

Identifier chain:

`Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status`

`FEM_Node_ID` is optional metadata only.

## Routing table

| Primary theme in a paper | RQ | WP | Thesis chapter | Target paper | Gate | Evidence type |
|---|---|---|---|---|---|---|
| Run-aware vibration classification; leakage control; sensor configuration; reproducibility | RQ1 | WP1 | C4 | Paper 1 | G1 | Laboratory evidence |
| Formal identifiers; BIM/IFC linkage; competency questions; bidirectional evidence-to-record traceability | RQ2 | WP2 | C5 | Paper 2 | G2–G3 | Information traceability |
| Real-building deployment; operational baseline; mapping; inspection workflow under limited field damage data | RQ3 | WP3 | C6 | Paper 3 | G4 | Field feasibility |
| Transparent Normal → Watch → Inspect → Priority Inspection logic; scenario or expert review | RQ3 | WP4 | C7 | Paper 4 or merged Paper 3 | G5 | Management decision support |
| Definitions, theory, prior work, or evidence of a gap without a direct method contribution | Cross-cutting | Supporting | C2, sometimes C3 | Background only | None | Literature evidence |

## Scope classification

- `Core Scope`: directly supplies a method, evaluation criterion, result type or gap evidence for one locked RQ/WP.
- `Supporting Scope`: contextual theory, standards, nominal FEM reference, terminology or transferable method that does not answer an RQ by itself.
- `Future Work`: defensible post-PhD extension explicitly separated from current proof obligations.
- `Out of Scope`: conflicts with the locked thesis or belongs to another independent research line.

## FEM firewall

Permitted only as a nominal, uncalibrated, reference-only design model for reference-informed sensor placement, component illustration or qualitative hypotheses labelled unconfirmed.

Prohibited: calibrated FEM, damage diagnosis, bolt-preload or stiffness-degradation inference, quantitative lab-to-field transfer, optimal sensor placement, or any FEM-specific RQ/WP/chapter/paper/Gate.

## Current priority

Read the latest authoritative current-status or Gate-specific source every time. Do not hard-code the active Gate, run count, model status, model metrics, field-access status or next action in this routing snapshot. If no current source is available, write `Evidence is currently insufficient.`
