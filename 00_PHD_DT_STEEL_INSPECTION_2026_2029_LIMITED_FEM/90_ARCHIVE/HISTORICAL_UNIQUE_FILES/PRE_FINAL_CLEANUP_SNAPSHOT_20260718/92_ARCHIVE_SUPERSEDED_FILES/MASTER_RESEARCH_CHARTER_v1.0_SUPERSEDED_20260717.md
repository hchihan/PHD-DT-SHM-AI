# [ARCHIVED COPY]
**Archived:** 2026-07-17
**Reason superseded:** FEM-core architecture replaced by Limited-FEM architecture (Verdict B, supervisors' approval 17/07/2026). Superseded by `01_CORE_REPORTS/MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md`.
**Original location (preserved, not deleted):** `00_SYSTEM/MASTER_CHARTER.md`
**Note:** the original file self-labels "v1.1 — Locked research scope"; in the migration lineage it is treated as v1.0 (pre-Limited-FEM). Content below is a verbatim copy.

---

# MASTER CHARTER

**Version:** v1.1 — Locked research scope
**Research field:** Construction Management / Asset Management
**Status:** Governing document for the PhD Research OS

---

## 1. Project identity

### Vietnamese title
**Phát triển khung Digital Twin dựa trên dữ liệu phục vụ giám sát trạng thái và hỗ trợ kiểm tra, bảo trì nhà công nghiệp khung thép ven biển.**

### English title
**Developing a Data-informed Digital Twin Framework for Condition Monitoring and Inspection–Maintenance Support of Coastal Industrial Steel Buildings.**

---

## 2. Central thesis statement

This research develops a data-informed Digital Twin framework that organizes vibration sensing, RSAP/FEM interpretation, and BIM-linked asset information into traceable condition evidence for inspection–maintenance support of coastal industrial steel buildings.

### Central evidence chain

```text
Vibration data
→ condition classification or warning
→ FEM-based mechanical interpretation
→ BIM-linked component traceability
→ condition evidence level
→ inspection and maintenance recommendation
```

---

## 3. Research object and scope

### Research object
Coastal industrial steel buildings, with emphasis on steel-frame connections, vibration response, condition monitoring, and condition-based inspection–maintenance support.

### Laboratory case
A 1:10 steel frame model creates controlled, labelled vibration evidence for:

- Healthy state;
- Apex connection condition;
- Beam–column connection condition;
- Brace connection condition.

### Field case
An industrial steel building with similar structural form but different scale supports:

- BIM–FEM–Sensor traceability;
- feasibility of condition monitoring;
- inspection-oriented decision-support scenarios.

### Scope boundary
The PhD demonstrates traceable evidence and decision-support feasibility. It does **not** claim direct field damage diagnosis, universal applicability, fully autonomous maintenance, or commercial Digital Twin completion.

---

## 4. Research questions, work packages, chapters, and papers

| RQ | Research question | WP | Thesis chapter | Paper |
|---|---|---|---|---|
| **RQ1** | How can vibration data from a 1:10 steel frame and different sensor configurations identify controlled connection states? | **WP1 — Laboratory vibration evidence** | Chapter 3 | **Paper 1** |
| **RQ2** | How can RSAP/FEM interpret vibration changes, equivalent connection stiffness degradation, and sensor-sensitive locations? | **WP2 — FEM mechanical interpretation** | Chapter 4 | **Paper 2** |
| **RQ3** | How can Sensor_ID, FEM_Node_ID, and BIM_GUID be linked to support traceable condition-based inspection and maintenance actions for a real industrial steel building? | **WP3 — BIM–FEM–Sensor traceability** | Chapter 5 | **Paper 3** |
| **Synthesis** | How can multi-source condition evidence be translated into transparent inspection-priority actions? | **WP4 — Decision-support synthesis** | Chapter 6 | **Paper 4 — optional / stretch** |

---

## 5. Work packages

### WP1 — Laboratory vibration evidence
Create and validate a labelled vibration dataset; evaluate practical sensor configurations and run-aware condition classification.

**Primary output:** reproducible laboratory evidence, not field diagnosis.

### WP2 — FEM mechanical interpretation
Build and calibrate a healthy RSAP/FEM baseline; simulate equivalent connection stiffness degradation; compare relative modal trends; identify sensor-sensitive locations.

**Primary output:** mechanical interpretation of laboratory evidence, not a perfect structural replica.

### WP3 — BIM–FEM–Sensor traceability
Link `Sensor_ID`, `FEM_Node_ID`, and `BIM_GUID`; demonstrate traceability from a monitoring warning to a component-specific inspection action.

**Primary output:** traceable inspection workflow for a field-feasibility case.

### WP4 — Decision-support synthesis
Translate evidence into four practical action levels:

```text
Normal → Watch → Inspect → Priority Inspection
```

**Primary output:** transparent decision-support logic, not autonomous maintenance optimization.

---

## 6. Publication portfolio

| Paper | Working title | Core evidence | Intended contribution |
|---|---|---|---|
| **Paper 1** | *Run-Aware Evaluation of Low-Cost Sensor Configurations for Vibration-Based Condition Classification of a Scaled Bolted Steel Frame* | Dataset quality, run-level split, sensor configuration, classification results | Controlled laboratory evidence and practical sensor configuration |
| **Paper 2** | *FEM-Supported Interpretation of Connection-Loosening Scenarios and Sensor Sensitivity in a Scaled Steel Frame* | FEM calibration, modal comparison, stiffness scenarios, sensitivity map | Mechanical interpretation and sensor sensitivity |
| **Paper 3** | *A Traceable BIM–FEM–Sensor Information Framework for Condition-Based Inspection of an Industrial Steel Building* | Sensor_ID–FEM_Node_ID–BIM_GUID mapping, traceability workflow, inspection scenarios | BIM-linked inspection traceability |
| **Paper 4** | *From Condition Evidence to Inspection Priority: A Digital Twin Decision-Support Framework for Coastal Industrial Steel Buildings* | Evidence level, confidence/data quality, FEM-sensitive location, component criticality | Optional synthesis of inspection priority |

---

## 7. Allowed claims

- The laboratory model creates controlled, labelled evidence of connection-state changes.
- RSAP/FEM provides mechanical interpretation of modal trends and sensor-sensitive locations.
- BIM–FEM–Sensor mapping enables traceability from monitoring evidence to asset components.
- The framework supports condition-based inspection and maintenance decisions under limited field-label conditions.
- The Digital Twin is a decision-support prototype, not a commercial platform.

---

## 8. Prohibited claims

- Remaining useful life prediction.
- Exact failure-time prediction.
- Direct transfer of lab classifier to field diagnosis.
- Confirmed field damage without inspection evidence.
- “Best AI model” claims in general.
- Fully autonomous maintenance optimization.
- Universal applicability to all building types.
- Commercial Digital Twin completion.

---

## 9. Validation ladder

| Validation level | Meaning |
|---|---|
| **V1 — Laboratory validity** | Controlled connection states produce repeatable vibration differences. |
| **V2 — FEM validity** | Calibrated FEM reproduces relative modal trends and sensor-sensitive locations. |
| **V3 — Traceability feasibility** | Sensor warnings can be linked to FEM nodes and BIM components. |
| **V4 — Decision validity** | Case scenarios produce transparent and reasonable inspection actions. |

---

## 10. Decision levels

| Level | Decision meaning |
|---|---|
| **Normal** | No persistent abnormal evidence; continue routine monitoring. |
| **Watch** | Minor or unstable change; increase monitoring frequency and review visually if necessary. |
| **Inspect** | Persistent signal change with FEM-supported sensitive location; perform targeted technical inspection. |
| **Priority Inspection** | Strong, persistent evidence at a critical component; conduct detailed assessment and recommend repair/strengthening through expert review. |

---

## 11. Scope-creep watchlist

Do not begin these activities before their evidence prerequisites are complete:

- CFD;
- Smart City integration;
- edge AI deployment;
- RUL / failure-time prediction;
- commercial software development;
- complex Health Index weighting;
- real-time field dashboard as a main research outcome;
- multi-building deployment;
- direct lab-to-field classifier transfer.

---

## 12. Core operating rule

Every proposed activity must answer:

```text
Which RQ?
Which WP?
Which Chapter?
Which Paper?
Which Evidence Gate?
```

If it does not strengthen an active Evidence Gate, it is **NOT NOW**.
