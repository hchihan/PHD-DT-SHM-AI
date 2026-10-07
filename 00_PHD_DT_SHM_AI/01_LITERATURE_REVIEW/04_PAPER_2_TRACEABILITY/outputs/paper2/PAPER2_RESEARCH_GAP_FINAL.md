# PAPER2_RESEARCH_GAP_FINAL

Paper 2 · RQ2 / WP2 · P002 25×80 m · 2026-10-07. Every statement below rests on external literature. No repository document is used to establish the gap.

## 1 What literature already establishes

| Element | Established by (full text unless noted) |
|---|---|
| Sensor data bound to BIM/IFC components through GlobalIds or GUID mapping tables | Chatsuwan et al. 2025; Ramonell et al. 2023; Lorvão Antunes et al. 2024; Theiler & Smarsly 2018 (abstract) |
| IFC GUIDs are not persistent across independently created phase files or delete-recreate edits | Borkowski et al. 2026; Chatsuwan et al. 2025; Shafiq & Lockley 2020 (abstract) |
| Persistent element identity layered above GUIDs | Borkowski et al. 2026 (manual cross-file matching) |
| Identifier quality metrics (completeness, validity, uniqueness, stability) with auditable registration | Fang et al. 2025; Lee et al. 2020 (rule level) |
| Inspection records linked to IFC components | Lorvão Antunes et al. 2024; Bellon et al. 2025; Hagedorn et al. 2022 |
| Inspection or damage linked to maintenance action | Bellon et al. 2025; Hagedorn et al. 2022; Kim et al. 2018 (work records) |
| Auditable monitoring-data validation and alert-to-reaction logging | Mariniello et al. 2025 |
| Revision-linked, role-attributed decision records | García et al. 2026 |
| Competency questions as a verification device | Lorvão Antunes et al. 2024; Borkowski et al. 2026; Monfardini et al. 2023 (abstract) |

## 2 Strongest competing studies

Borkowski et al. 2026 (identity across versions); Fang et al. 2025 (identifier governance and audit); Lorvão Antunes et al. 2024 (sensor + inspection + CQ on real pilots); Bellon et al. 2025 (inspection → maintenance in IFC); Mariniello et al. 2025 (auditable monitoring-to-reaction). Details in `PAPER2_COUNTER_EVIDENCE.md`.

## 3 What is not a gap

- Linking sensors to BIM components.
- Using the IFC GlobalId as a key.
- BIM-supported inspection or maintenance records.
- Provenance or audit trails for monitoring data.
- Competency questions or rule-based validation as techniques.
- Persistent identity across model versions (Borkowski et al. 2026 addresses it more directly than Paper 2 does).
- The existence of GUID anomalies.

## 4 Remaining gap (combination)

In the ten Tier-A studies read in full, no study reports a single traceability structure that (a) carries one monitored component from Sensor_ID through a condition-evidence record and an inspection record to an action status, (b) resolves that component only through an identifier qualified by a registered model version and rejects the identifier under any other version, (c) defines explicit integrity rules that reject missing, invalid and ambiguous links anywhere in that chain, with deliberate invalid-data tests, and (d) is exercised on a real BIM model that contains an observed identifier anomaly. Lorvão Antunes et al. (2024) reach (a) up to inspection without actions or rules; Bellon et al. (2025) reach the inspection-to-action end without sensors or identity governance; Fang et al. (2025) reach identifier governance without any downstream chain; Borkowski et al. (2026) reach cross-version identity without the chain or automated matching.

## 5 Counter-evidence that limits the gap

- Borkowski et al. (2026) solve cross-version identity more fully. Paper 2's version qualification is a validity scope, not persistence.
- Fang et al. (2025) measure GlobalId stability across two exports. Paper 2 has one export and cannot claim stability.
- Mariniello et al. (2025) and García et al. (2026) already apply deterministic gate logic to real data. Paper 2's chain records are synthetic.
- The search was targeted, not systematic (about 139 unique records screened).

## 6 Why the remaining gap matters for construction management

Inspection and maintenance decisions are accountable only if the evidence behind them can be traced to the component that was observed and to the model state that defined that component. Chatsuwan et al. (2025) and Borkowski et al. (2026) show that GUID-based links can break silently when models change; Bellon et al. (2025) and Hagedorn et al. (2022) show that inspection and maintenance records are being moved into BIM-linked structures. Where both hold, a maintenance action can end up attached to evidence about a different element or a superseded model state without any record of the break. The gap concerns detecting that failure in the information chain, which is an asset-information-governance problem rather than a sensing or structural problem.

## 7 Final bounded gap statement

Prior studies link monitoring data to BIM components, link inspection records to maintenance actions, and govern IFC identifiers, but in the literature reviewed these mechanisms have not been combined into one component-level chain from sensor to action status in which identity is scoped to a registered model version and invalid, incomplete or ambiguous links are rejected by explicit rules and exercised on a real model with an observed identifier anomaly.

Gap confidence: **MODERATE**. Ten direct competitors were read in full, but the search was targeted rather than systematic.
