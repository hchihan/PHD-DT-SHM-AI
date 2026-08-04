# MASTER RESEARCH CHARTER
**Version:** v1.1 — LIMITED-FEM ARCHITECTURE
**Date:** 2026-07-17
**Status:** Source of truth. Supersedes the FEM-core MASTER_CHARTER.md (00_SYSTEM). Approved basis: supervisor decision 17/07/2026 (Verdict B) and THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md.
**Field:** Construction Management / Asset Management.

---

## 1. Project identity

Vietnamese title: **Phát triển khung Digital Twin dựa trên dữ liệu phục vụ giám sát trạng thái và hỗ trợ kiểm tra, bảo trì nhà công nghiệp khung thép ven biển.**

English title: **Developing a Data-informed Digital Twin Framework for Condition Monitoring and Inspection–Maintenance Support of Coastal Industrial Steel Buildings.**

## 2. Central thesis statement

A data-informed Digital Twin framework — which organizes, links, and traces condition evidence from vibration data to BIM components and inspection records — can support transparent and verifiable inspection–maintenance action selection for industrial steel buildings, even under limited field damage data. A nominal FEM design model serves only as a sensor-placement reference, not as a diagnostic source.

### Core evidence chain (locked)

```text
Vibration data
→ condition/state-change evidence
→ BIM-linked component
→ inspection record
→ inspection-maintenance action support
```

### Core identifier chain (locked)

```text
Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status
```

`FEM_Node_ID` may exist only as optional metadata. It must never appear as a required link.

## 3. Locked scope

In scope: laboratory vibration evidence under a run-aware, leakage-controlled protocol; a formalized component-level traceability data model linking condition evidence to BIM objects and inspection records; field feasibility of the framework at a real industrial steel building; a transparent four-level decision-support logic.

Out of scope (do not begin): RUL/failure-time prediction, predictive maintenance claims, CFD, Smart City integration, Edge AI deployment, commercial software development, autonomous maintenance optimization, complex weighted Health Index, direct lab-to-field classifier transfer, calibrated FEM and FEM-based diagnosis.

## 4. Research object

Coastal industrial steel buildings, with emphasis on steel-frame connections, vibration response, condition monitoring, component-level information traceability, and condition-based inspection–maintenance support.

## 5. Laboratory case

A 1:10 steel frame model produces controlled, labelled vibration evidence for: healthy state; apex connection condition; beam–column connection (BCJ) condition; brace connection condition. Runs are documented in a run registry; evaluation is run-aware (including LORO) to prevent train–test leakage.

## 6. Field case

An industrial steel building of similar structural form but different scale supports: Sensor_ID → BIM_GUID mapping, operational baseline acquisition, field traceability scenarios, and inspection-oriented decision-support scenarios. No quantitative conclusions transfer from the 1:10 model to the field structure.

## 7. Research questions

**RQ1.** How reliably can vibration data from the 1:10 steel frame model and different sensor configurations produce evidence distinguishing controlled connection states under a run-aware, leakage-controlled evaluation protocol?

**RQ2.** How can state evidence from sensor data be organized and linked to BIM components and inspection records to ensure component-level traceability?

**RQ3.** How can a data-informed Digital Twin framework support the selection and recording of inspection actions at a real building under limited field damage data?

## 8. Work packages

| WP | Content | Primary output |
|---|---|---|
| WP1 — Laboratory vibration evidence | Labelled dataset, run registry, sensor configurations, run-aware/LORO evaluation, sensor-mode verification (incl. ResNet1D) | Reproducible laboratory evidence, not field diagnosis |
| WP2 — BIM–Sensor–Inspection traceability | Formal traceability data model, identifier schema, competency questions, evaluation criteria, end-to-end lab demonstration | Verifiable component-level traceability framework |
| WP3 — Field feasibility and inspection support | Field sensor deployment (reference-informed placement), operational baseline, field traceability scenarios, inspection record workflow | Field-feasibility evidence, not field damage diagnosis |
| WP4 — Decision-support synthesis | Normal → Watch → Inspect → Priority Inspection logic, case scenarios, expert/facility-manager review | Transparent decision-support logic; no weighted Health Index |

## 9. Chapter architecture

C1 Introduction; C2 Literature review and gap (gap = missing end-to-end evidence-to-action traceability chain: vibration → evidence → BIM component → inspection record → action); C3 Research framework and validation design (includes "Digital Twin definition and maturity level in this thesis" and the subsection "Limited role of the nominal FEM model"); C4 Laboratory evidence (Paper 1); C5 Traceability framework (Paper 2); C6 Field feasibility (Paper 3); C7 Decision-support framework (Paper 4 / stretch); C8 Conclusions. **There is no FEM chapter.**

## 10. Paper portfolio

| Paper | Working title | Core content |
|---|---|---|
| Paper 1 | Run-Aware Evaluation of Low-Cost Sensor Configurations for Vibration-Based Condition Classification of a Scaled Bolted Steel Frame | Dataset integrity, run registry, run-aware/LORO evaluation, sensor configuration effects, CEI as confidence/evidence indicator |
| Paper 2 | A Verifiable Component-Level Traceability Framework Linking Vibration-Based Condition Evidence to BIM Objects and Inspection Records for Industrial Steel Buildings | Formal traceability data model, identifier schema, pre-registered competency questions, scenario validation |
| Paper 3 | Field Feasibility of a Data-Informed Digital Twin Framework for Condition-Based Inspection Support of an Industrial Steel Building | Field deployment, operational baseline, field traceability scenarios, inspection record workflow |
| Paper 4 (optional / may merge into Paper 3) | From Condition Evidence to Inspection Priority | Four-level decision logic, scenario review |

## 11. Evidence Gates (summary; full definitions in EVIDENCE_GATES_v1.1_LIMITED_FEM.md)

G1 dataset integrity and run-aware evaluation; G2 traceability data model and competency questions; G3 end-to-end laboratory traceability; G4 field mapping and baseline feasibility; G5 inspection-action scenario review; G6 Paper 2 submission; G7 Paper 3 submission and thesis synthesis. **No FEM calibration, MAC, equivalent-stiffness, or FEM sensor-sensitivity gate exists.**

## 12. Validation ladder

| Level | Meaning |
|---|---|
| V1 — Laboratory validity | Controlled connection states are distinguishable and repeatable under run-aware/LORO evaluation |
| V2 — Traceability validity | Identifier chain runs bidirectionally (warning ↔ component ↔ record), measured by pre-registered competency questions and criteria |
| V3 — Field feasibility | Framework deploys at a real building; data return; traceability scenarios execute |
| V4 — Decision validity | Recommendations are transparent, explainable, and judged reasonable by facility management |

## 13. Allowed claims

Laboratory state evidence distinguishes controlled connection states under leakage-controlled evaluation. Sensor configuration influences classification more strongly than model architecture choice. The traceability framework links warnings to components and inspection records, verified through scenarios. The framework is feasibly deployable at a real building. The nominal FEM provides a sensor-placement reference. CEI is a confidence/evidence indicator.

## 14. Prohibited claims

Field damage diagnosis without confirming inspection; inference of bolt preload or real stiffness degradation from FEM; any claim based on a calibrated FEM; quantitative transfer of 1:10 conclusions to the real building; ordinal severity/DSI claims; RUL or predictive maintenance; general AI superiority; weighted Health Index; "optimal" sensor placement; autonomous maintenance decisions; describing CEI as physical severity.

## 15. Role of the nominal FEM

FEM is retained solely as a **nominal, uncalibrated, reference-only design model**. Permitted uses: (i) preliminary justification of field sensor placement ("reference-informed sensor placement"); (ii) illustration of component locations; (iii) qualitative mechanical hypotheses for Paper 1 anomalies in Discussion/Limitation sections, labelled "hypothesis, not confirmed." Prohibited uses: calibration, damage diagnosis, stiffness-degradation inference, quantitative lab-to-field transfer, appearance in the name of any RQ, WP, chapter, paper, or evidence gate. Every mention of FEM must carry the qualifier "nominal, uncalibrated, reference-only, not used for damage diagnosis."

## 16. Terminology controls

Governed by TERMINOLOGY_CONTROL_v1.1.md. Allowed: condition evidence; state-change evidence; component-level traceability; BIM-linked inspection record; field feasibility; inspection-maintenance support; nominal reference model; reference-informed sensor placement. Controlled/removed: calibrated FEM; physics-informed condition evidence; equivalent stiffness degradation; mechanical damage interpretation; optimal sensor placement; FEM-based diagnosis; damage severity; RUL; predictive maintenance; autonomous maintenance decision.

## 17. Post-PhD expansions (explicitly deferred)

Calibrated FEM and model updating with EMA; similitude-based lab-to-field transfer; predictive maintenance and RUL; weighted Health Index; multi-building deployment; commercial platform; Edge AI; Smart City integration.

## 18. Change summary from v1.0 (FEM-core charter)

| Element | v1.0 (FEM-core) | v1.1 (Limited-FEM) |
|---|---|---|
| Evidence chain | Vibration → classification → FEM interpretation → BIM traceability → evidence level → recommendation | Vibration → condition evidence → BIM-linked component → inspection record → action support |
| Identifier chain | Sensor_ID → FEM_Node_ID → BIM_GUID | Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status; FEM_Node_ID optional metadata |
| RQ2 | RSAP/FEM interpretation, equivalent stiffness degradation, sensor-sensitive locations | Organization and linkage of state evidence to BIM components and inspection records (traceability) |
| RQ3 | Sensor_ID–FEM_Node_ID–BIM_GUID linkage | Field feasibility and inspection-action support under limited field damage data |
| WP2 | FEM mechanical interpretation (calibrated baseline) | BIM–Sensor–Inspection traceability |
| Paper 2 | FEM-supported interpretation of connection loosening | Verifiable component-level traceability framework |
| Chapters | Dedicated FEM chapter (old C4) | No FEM chapter; FEM confined to a C3 methods subsection and Limitations |
| Validation V2 | Calibrated FEM reproduces modal trends | Traceability validity via competency questions |
| Gates | Included calibrated-FEM baseline gate | G1–G7 without any FEM gate |
| FEM status | Core contribution | Nominal reference tool only |
