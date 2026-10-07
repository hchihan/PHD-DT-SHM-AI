# PAPER2_OUTLINE_FINAL

Paper 2 · RQ2 / WP2 · Chapter 5 · case P002 25×80 m only · 2026-10-07.
Working title: Version-scoped component identity for traceable condition evidence, inspection and maintenance records: a BIM case with an observed identifier anomaly.
Evidence codes: OE = objective (E1/E2), IV = internal verification (E3), see `PAPER2_OBJECTIVE_EVIDENCE_MATRIX.csv`. Readiness: R = ready to draft, P = partial, N = not ready.

| § | Purpose | Main claim | Objective repository evidence | Required external refs | Table/Figure | Limitation | Ready |
|---|---|---|---|---|---|---|---|
| 1.1 | Asset-information problem | Inspection and maintenance records are being moved into BIM-linked structures | — | Bellon 2025; Hagedorn 2022; Kim 2018 | F1 | — | R |
| 1.2 | Why linked evidence alone is insufficient | A sensor link to a GUID is only as reliable as the GUID | — | Chatsuwan 2025; Borkowski 2026 | — | — | R |
| 1.3 | Identity/provenance issue | GUIDs change across files and edits; decisions need traceable evidence | — | Borkowski 2026; Shafiq 2020; Mariniello 2025; García 2026 | — | — | R |
| 1.4 | What literature provides | Each hop is precedented | — | Tier A | — | — | R |
| 1.5 | Combination gap | Not combined in Tier A | — | Tier A | — | targeted search | R |
| 1.6 | RQ2 | stated | — | — | — | — | R |
| 1.7 | Contributions | C1, C2, C3 | — | as in contribution file | — | — | R |
| 2.1 | Monitoring data → BIM | established | — | Theiler 2018; Chatsuwan 2025; Ramonell 2023; Lorvão Antunes 2024; Gragnaniello 2024 | T1 | — | R |
| 2.2 | BIM/IFC identity | GlobalId role and quality | — | Lee 2020; Fang 2025; Shafiq 2020 | T1 | — | R |
| 2.3 | Versioning and persistence | persistence addressed by Borkowski | — | Borkowski 2026; Fang 2025 | — | — | R |
| 2.4 | Provenance and governance | ledger and CDE records | — | Mariniello 2025; García 2026; Çelik 2023; Tavakoli 2023; Ciccarese 2013 | — | — | R |
| 2.5 | Inspection–maintenance linkage | established | — | Bellon 2025; Hagedorn 2022; Kim 2018; Wan 2019 | — | — | R |
| 2.6 | Forward/reverse traceability | partial in Kim, Lorvão | — | Kim 2018; Lorvão Antunes 2024 | — | — | R |
| 2.7 | Integrity verification, CQs | techniques established | — | Monfardini 2023; Lee 2020; Fang 2025 | — | — | R |
| 2.8 | Positioning | combination gap | — | all | T1 | — | R |
| 3.1 | Scope | information traceability only | — | — | — | no structural diagnosis | R |
| 3.2 | P002 case | 25×80 m steel portal frame, single working model | OE-01, OE-03 | — | — | working reference, not as-built | R |
| 3.3 | Source hierarchy | RVT working reference, IFC derived, PDF as-built | OE-11, OE-12 | — | F4 | researcher decisions | R |
| 3.4 | Version registration | hash-anchored Model_Version_ID | OE-01, OE-02 | — | — | one version | R |
| 3.5 | Identity governance | BIM_GUID = exported GlobalId; detect, not repair | OE-04..06 | Borkowski 2026; Fang 2025 | T2, F2 | one export | R |
| 3.6–3.8 | Schema, rules, CQs | 6 entities, 14 rules, 12 CQs frozen before tests | IV-01 | Monfardini 2023 | T4, T5, F3 | same author | R |
| 3.9–3.10 | Positive/negative and challenge procedures | mutation classes; Level C challenge | IV-03, IV-07 | — | F7 | internal | R |
| 3.11 | Evidence-independence classes | E1/E2/E3 | matrix | — | T8 | — | R |
| 4 | Architecture | entities, identifier roles, pair key, hops, failure handling | IV-01 | Lorvão 2024; Bellon 2025 (contrast) | F2, F3, F5 | — | R |
| 5.1–5.4 | Case implementation | BIM source, inventory, registration, anomalies | OE-01..12 | — | T3, F6 | sampled level data | R |
| 5.5–5.6 | Records and synthetic boundary | chain records synthetic | IV-02 | — | — | synthetic | R |
| 6.1–6.3 | Objective results first | divergence and duplicates | OE-03..10 | — | T3, F6 | cause unknown | R |
| 6.4–6.9 | Internal verification | 9/9, 145/145, 121/121, 68/78 → 78/78 | IV-03..08 | — | T6, T7 | E3; result CSVs not on this machine | P (numbers from evidence log) |
| 6.10 | Evidence boundary | what each class shows | matrix | — | T8 | — | R |
| 7.1–7.2 | Objective vs internal | separation | matrix | — | — | — | R |
| 7.3 | Tier-A comparison | differences named per study | — | Tier A | T1 | — | R |
| 7.4–7.5 | Contributions; CM relevance | C1–C3; accountability of evidence used in actions | — | García 2026; Hagedorn 2022 | — | — | R |
| 7.6–7.8 | Practice, boundary, field feasibility | next step = second model version and field records | — | — | — | — | R |
| 8 | Limitations | 11 items | all | — | — | — | R |
| 9 | Conclusion | answer RQ2 only | — | — | — | — | R |

Tables: T1 positioning (Tier A, from `PAPER2_LITERATURE_POSITIONING_FINAL.csv`); T2 identifier roles; T3 objective BIM/IFC observations; T4 integrity rules; T5 CQs; T6 positive/negative verification; T7 challenge first run and correction; T8 claim/evidence/independence.
Figures: F1 management chain; F2 version-scoped identity; F3 data model; F4 Gate 2 → Gate 3 procedure; F5 forward/reverse; F6 duplicate-identifier anomaly; F7 integrity-testing process. No FEM or RSAP figure.
