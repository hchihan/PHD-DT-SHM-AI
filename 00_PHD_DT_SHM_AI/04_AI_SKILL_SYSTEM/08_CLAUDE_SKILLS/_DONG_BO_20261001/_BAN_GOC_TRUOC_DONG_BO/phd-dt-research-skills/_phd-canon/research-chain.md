# Canon — Locked Research Chain and Four-Layer Firewall

**v1.0 · 2026-08-10 · derived from** `00_GOVERNANCE/MASTER_RESEARCH_CHARTER.md` §6, `RESEARCH_ARCHITECTURE.md`, `RESEARCH_DIRECTION_AND_SCOPE.md` §4, `AGENT_RULES.md` §3, `01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md` §2.

This file is a convenience summary for skill execution. The governance files above remain the source of truth; when they disagree with this file, they win, and the conflict should be reported rather than silently resolved.

---

## Thesis identity

**Field:** Construction Management / Asset Management.

**Title (EN):** Developing a Data-informed Digital Twin Framework for Condition Monitoring and Inspection–Maintenance Support of Coastal Industrial Steel Buildings.

**Core problem:** condition evidence from vibration data is disconnected from component identity, inspection records, and accountable action history. The contribution is a transparent, traceable **information-management chain** — not a new damage-diagnosis algorithm. Sensors, AI, BIM and FEM are instruments, not research objects.

---

## Locked evidence chain

```text
Vibration data
→ condition/state-change evidence (+ CEI)
→ BIM-linked component
→ Inspection_Record
→ Action_Record
→ Status_Event
→ accountable, verification-controlled inspection-maintenance action support
```

## Locked identifier chain

```text
Sensor_ID
→ BIM_GUID / Asset_ID @ Model_Version_ID
→ Condition_Evidence_ID
→ Inspection_Record_ID
→ Action_Record_ID
```

Rules that are frequently violated and must be checked explicitly:

- **`Action_Status` / `Workflow_Status` is a current-state projection of `Action_Record`. It is never an identifier and never a history.**
- **`Status_Event_ID` is `PROPOSED — NOT YET ACCEPTED`** pending `00_GOVERNANCE/ADR_ACTION_STATUS_EVENT_20260804_DRAFT.md`. Write about it in proposal language.
- **CEI is a first-class structured metadata attribute of `Condition_Evidence_ID`.** It is not a scalar, not a Health Index, not severity, not damage probability, not priority.
- **Do not add `Component_ID`** to the canonical chain when `Asset_ID + BIM_GUID + Model_Version_ID` is sufficient. A database surrogate key is a technical key only.
- **A recommendation is not an `Action_Record`.**
- **`completed` is not verified closure.**
- **Defect severity is not `Action_Level`.**
- `FEM_Node_ID` is optional metadata only, never a required link.

---

## Four-layer evidence firewall

Each layer may claim only what it verifies. No layer borrows another layer's evidence. This firewall is the most common source of overclaim, so check it whenever a claim spans layers.

| Layer | May claim | May NOT claim |
|---|---|---|
| **1 — Laboratory evidence** (RQ1/WP1/C4/Paper 1, G1) | Controlled connection states on a 1:10 steel frame model are distinguishable under leakage-safe run-aware evaluation | Field diagnosis; transfer of quantitative 1:10 conclusions to a real building; "best AI" |
| **2 — Information traceability** (RQ2/WP2/C5/Paper 2, G2–G3) | Identity, records, provenance, events, competency questions and constraints form a checkable model | That the model diagnoses damage, is field-proven, or improves maintenance outcomes |
| **3 — Field feasibility** (RQ3/WP3/C6/Paper 3, G4) | The framework deploys, data returns, mapping holds, traceability scenarios run end-to-end at a real site | Real damage detection; field validation of the classifier; diagnosis |
| **4 — Inspection-maintenance support** (WP4/C7, G5) | Action support with human review, authorization, post-action verification and guarded closure/reopen | Automated decision; replacement of engineering judgement; weighted Health Index |

Every field anomaly leads to **an inspection**, never to **a damage conclusion**.

---

## RQ → WP → Chapter → Paper → Gate

| RQ | WP | Chapter | Paper | Gate | Main evidence |
|---|---|---|---|---|---|
| RQ1 | WP1 | C4 | Paper 1 | G1 | Leakage-safe, run-aware laboratory evidence |
| RQ2 | WP2 | C5 | Paper 2 | G2–G3 | Formal evidence-to-action traceability |
| RQ3 | WP3 | C6 | Paper 3 (publication optional, **minimum field evidence mandatory**) | G4 | Field feasibility, not field diagnosis |
| Synthesis | WP4 | C7 or merged C6 | Paper 4 optional | G5 | Human-reviewed inspection-action support |

Paper 2 is the single current RQ2 publication direction. Paper 2A / Paper 2B / dual-paper / split-roadmap commitments are superseded.

---

## Paper 2 design boundary (G2)

```text
Condition_Evidence
→ BIM-linked component
→ Inspection_Record
→ Action_Record
→ Status_Event
→ accountable authorization/review
→ post-action verification
→ guarded closure/reopen
```

**This is a design boundary. It is not an implemented result and not a validated system.** G3 supplies executed end-to-end validation when it opens; execution is currently `NOT OPEN`.

---

## Instrument boundary

Revit, IFC, Dynamo, Pset, IDS, SQLite, SPARQL/SHACL and any viewer are supporting implementation instruments. Their presence or successful execution is not the novelty and cannot substitute for traceability completeness, provenance, integrity validation, human review, or gate acceptance.

**Do not run Graph 02.**
