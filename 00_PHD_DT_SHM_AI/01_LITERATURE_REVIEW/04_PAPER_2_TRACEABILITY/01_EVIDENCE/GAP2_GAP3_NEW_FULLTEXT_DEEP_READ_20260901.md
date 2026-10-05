# Gap 2-Gap 3 New Full-Text Deep Read

**Date:** 2026-09-01  
**Status:** `EVIDENCE RECORD - NEW`; no prior file was edited, deleted, or overwritten.  
**Research mapping:** RQ2 / WP2 / Chapter 5 / Paper 2 / Evidence Gates G2-G3.  
**Corpus:** exactly two requested works: Sedigh & Müller (2025) and Wu, El-Assady & De Wolf (2026).  
**Canonical identifier chain retained unchanged:** `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status`. The source terms `Asset Identifier`, IFC `GlobalId`, inventory index, prediction, review point, recommendation, and status inventory are comparators only; none replaces a canonical identifier.  
**Limited-FEM firewall:** `nominal, uncalibrated, reference-only, not used for damage diagnosis`. This record does not open calibrated FEM, damage diagnosis, predictive maintenance, RUL, autonomous maintenance, field diagnosis, or commercial software development.  
**Locator convention:** `PDF p.` is the physical attachment page. Sedigh & Müller's repository/download cover is PDF p. 1, so article-page locators are also supplied as `[article p.]`.  
**Evidence codes:** `AUTHOR-STATED`, `READER-INFERRED`, and `FULLTEXT_DEEP_READ` have the same meanings used in the current deep-read evidence area.

**SUPERSEDES (content/status only; no old-file edit):** where prior screening for these two works relied on title/abstract/metadata or an anticipated publication status, this record supplies the current full-text extraction and claim boundary. It does not supersede any RQ, WP, Paper, Evidence Gate, canonical-identifier, or Limited-FEM governance decision.

## 1. Zotero parent, PDF, and version audit

| Work counted once | Parent and attachment read | Version finding | Evidence status |
|---|---|---|---|
| Sedigh & Müller (2025), DOI `10.1088/1742-6596/3140/4/042023` | Parent `B9YNJDR4`; PDF `RFLLRDWT`; 8 physical pages, comprising a one-page IOP access cover and a 7-page CISBAT 2025 article in *Journal of Physics: Conference Series* 3140(4), 042023. | Parent metadata, PDF title/authors/venue, and DOI agree. No second parent, related item, or competing version was found. The citable year is **2025**, as printed in the article. | `FULLTEXT_DEEP_READ`; `VERSION_VERIFIED`; `ONE_PAGE_COVER_OFFSET` |
| Wu, El-Assady & De Wolf (2026), DOI `10.1016/j.eswa.2025.130514` | Parent `F6XUPQKG`; PDF `RRG6NTQP`; 12 pages; *Expert Systems with Applications* 302, 130514, issue date 2026-03-15. | HTML snapshot `MTSZRGM8` is a child of the same article and is not counted separately. The DOI contains 2025 because of online/article registration history, while the volume/issue publication is 2026; this is one work, cited as **2026**. No competing parent or PDF version was found. | `FULLTEXT_DEEP_READ`; `VERSION_VERIFIED`; `ONLINE_DOI_YEAR/ISSUE_YEAR_RECONCILED` |

**Audit decision:** the corpus contains exactly two distinct works. HTML or cover material does not create additional evidence items.

## 2. Sedigh & Müller (2025) - `B9YNJDR4`

**Citation:** Sedigh, M., & Müller, J. (2025). IFC-based digital twin for real-time building data integration and its case study. *Journal of Physics: Conference Series, 3140*(4), 042023. https://doi.org/10.1088/1742-6596/3140/4/042023

| Extraction item | Full-text finding | Locator |
|---|---|---|
| Problem | Existing IFC/sensor integrations do not efficiently handle rapidly growing time-series data, while operational data also need to be exported back into a standard IFC representation for handover or archiving. | PDF pp. 2-4 [article pp. 1-3], Abstract, Sections 1-3. |
| Method/framework | Hybrid architecture: IFC building information in a relational database; historical sensor data in a time-series database; a JSON configuration maps communication-protocol `Asset Identifier` values to IFC `GlobalId`; BACnet acquisition updates GUID-named time-series tables and a current-value IFC property. The prototype extends `ifc-pipeline`/IfcOpenShell with Flask, PostgreSQL/TimescaleDB, BAC0, BIMSurfer, and Chart.js, then reintegrates timestamps/values through `IfcTimeSeries` for IFC export. | PDF pp. 3-7 [article pp. 2-6], Sections 2-4, Figures 1-4. |
| Unit of analysis | One air handling unit in TH Köln's Automation Laboratory. The operational identity unit is an IFC equipment/sensor element linked to its time-series table by GUID; eight major AHU components plus temperature, humidity, and differential-pressure sensors are described. There is no inspection-record, condition-evidence qualification, maintenance action, or action-status event as a tested unit. | PDF p. 4 [article p. 3], Section 3.1 and Figure 1; PDF p. 7 [article p. 6], Section 5. |
| Verification design | Proof-of-concept case: import Revit-exported IFC, configure GUID mappings, discover BACnet points, collect current/historical data, visualize values, and export integrated time-series data to IFC. Verification is functional and positive-path on one laboratory AHU; no controlled orphan, duplicate, stale/reused GUID, wrong-type, cardinality, chronology, or round-trip equality fixtures are reported. | PDF pp. 5-7 [article pp. 4-6], Sections 4-5 and Figures 2-4. |
| Main results | The prototype demonstrates real-time monitoring, historical storage, GUID-based retrieval, current-value display, chart visualization, and IFC-based export of integrated operational data. The authors report successful proof-of-concept use while retaining IFC as the standardized model. | PDF pp. 6-7 [article pp. 5-6], Sections 4.4-6 and Figure 4. |
| Limitations | `AUTHOR-STATED/SCOPED`: separate-database scalability is outside the proof-of-concept scope; implementation is BACnet-specific. `READER-INFERRED`: one AHU lab case, no scale/performance/error analysis, no negative integrity fixtures, no exact exported-versus-reimported semantic parity test, and no inspection/evidence/action governance. | PDF p. 6 [article p. 5], Section 4.2; pp. 7 [article p. 6], Sections 5-6. |
| Future work | Support additional building communication protocols and provide APIs for integration with external services and applications. | PDF p. 7 [article p. 6], Section 6. |
| Claim boundary | **Allowed:** an implemented prototype links IFC relational data and sensor time-series data by GUID, acquires BACnet values, visualizes current/history data, and exports integrated data into IFC on one AHU. **Not allowed:** call this the complete canonical traceability chain, evidence qualification, inspection accountability, maintenance action, governed `Action_Status`, verified closure, or exact source-target-source round-trip parity. | PDF pp. 4-7 [article pp. 3-6], Sections 3-6 and Figures 1-4. |

**Direct gap effect:** Sedigh materially weakens any Gap 2 or Gap 3 wording based only on the absence of `sensor/time-series ↔ IFC element` identity linkage, hybrid storage, historical retrieval, or IFC re-export. It does not close either exact gap because the implementation stops at sensor/equipment data integration and does not instantiate or verify `Condition_Evidence_ID → Inspection_Record_ID → Action_Status`.

## 3. Wu, El-Assady & De Wolf (2026) - `F6XUPQKG`

**Citation:** Wu, P.-Y., El-Assady, M., & De Wolf, C. (2026). A unified intelligence-augmented framework for building audits via physical and virtual inspection. *Expert Systems with Applications, 302*, 130514. https://doi.org/10.1016/j.eswa.2025.130514

| Extraction item | Full-text finding | Locator |
|---|---|---|
| Problem | Pre-demolition/pre-renovation audits remain manual, fragmented, costly, and non-standardized across desk study, field survey, inventory, recommendations, and reporting. The paper seeks an integrated human-AI design space for scalable circular-construction audits. | PDF pp. 1-2, Abstract and Section 1. |
| Method/framework | Multi-phase formal analysis: scoping review (25 screened publications), interviews with four industry representatives, iterative co-design with seven HCI and five circular-construction researchers, mapping of existing applications and prospective tasks, and expert user studies with eight Swiss companies. Five principles (adaptability, accessibility, affordability, acceleration, alignment) underpin the R2PIVS pipeline: retrieval, reality capture, prediction, interaction, visualization, and summarization. | PDF pp. 2-3, Section 2 and Figure 1; pp. 4-6, Sections 3-4 and Figures 2-4. |
| Unit of analysis | The main design unit is the building-audit workflow/module. Information is organized across building, floor/room, element, and product/component granularities; proposed machine-learning tasks are geometry measurement, visual assessment, and hazard estimation. This is a `status inventory` design, not an operational maintenance action lifecycle. | PDF pp. 3-6, Sections 3-4 and Figures 2-4; pp. 6-9, Section 5 and Figures 5-9. |
| Verification design | Requirements and framework logic were evaluated through participatory co-design, use-case mapping, wireframes/application-schema presentation, open discussion, and survey responses from industry experts. The paper verifies perceived utility/design alignment, not a deployed technical system. The authors explicitly defer prototype implementation and testing to subsequent work. | PDF pp. 2-3, Sections 2.3-2.5 and Figure 1; pp. 9-10, Section 6 and Figure 10. |
| Main results | Experts viewed the modular structure positively. All acknowledged modular value; three-quarters regarded it as scalable for information collection/management; half supported cost-effective cross-project collaboration; five of seven respondents indicated support for standardized iteration/workflow integration. The output is an expert-evaluated application schema and framework, not measured automation accuracy or an executed traceability database. | PDF pp. 9-10, Sections 6.1-6.2 and Figure 10. |
| Limitations | `AUTHOR-STATED`: sparse feedback limits model improvement; multimodal representation/visualization remains difficult; BIM integration into structured interactive attributes remains unresolved; a prototyping system is still needed. `READER-INFERRED`: small Swiss expert sample with continuity between interview and later study participants; scenario mappings use candidate models but do not report implemented task accuracy, referential constraints, authorization, event history, or intervention outcomes. | PDF pp. 10-11, Sections 7-7.1. |
| Future work | Build and test the technical prototype; study real-time egocentric interaction, bidirectional human-model feedback patterns, sparse-feedback learning, multimodal visualization, and integration with Revit/Archicad and domain software. | PDF pp. 10-11, Sections 7.1-8. |
| Claim boundary | **Allowed:** cite an expert-evaluated, human-in-the-loop framework/application schema for pre-demolition audit inventory and standardized information management. **Not allowed:** describe it as a deployed audit platform, validated ML inspection system, implemented database traceability chain, accountable action workflow, or governed action-status history. `Bi-directional interaction` means human-model feedback, not IFC/source-target-source parity or physical action closure. | PDF pp. 2-3, Sections 1-2; pp. 9-11, Sections 6-8 and Figure 10. |

**Direct gap effect:** Wu materially weakens broad claims that human-in-the-loop audit workflow design, multimodal inventory, product-level identifiers, expert validation, or iterative review are absent. It does not implement the canonical chain or an action-status lifecycle, and therefore does not close the exact Gap 2 conjunction. Its traceability language is prospective data/workflow traceability, not a tested Gap 3 integrity and round-trip contract.

## 4. Cross-source comparison

| Dimension | Sedigh & Müller (2025) | Wu et al. (2026) | Boundary for RQ2/G2-G3 |
|---|---|---|---|
| Physical/digital input | Live BACnet sensor values and IFC model | Documents, scans, point clouds, video, expert feedback, proposed model outputs | Both establish prior art for heterogeneous input integration; neither qualifies the thesis's condition evidence. |
| Identity/linkage | `Asset Identifier` mapped to IFC `GlobalId`; GUID names sensor table | Product/component-specific index and structured multigranular inventory are design requirements | Generic sensor/component identity linkage is not novel. Stability, uniqueness, provenance, and chain semantics still require explicit implementation and tests. |
| Implementation level | Working positive-path prototype on one lab AHU | Framework, wireframes/application schema, scenario mapping, expert evaluation; prototype deferred | Do not merge the two evidence levels into a claim that a complete audit-to-action system exists. |
| Human review | Not an inspection-review workflow | Human-in-the-loop validation and correction are central | Human review is prior framework-level art, but actor/role/authorization/event accountability remains untested. |
| IFC/BIM interaction | IFC import, relational representation, current values, historical lookup, IFC export | BIM integration remains a limitation/future integration target | IFC re-export exists in Sedigh; exact semantic round-trip parity and invalid-fixture rejection do not. |
| Inspection/action/status | None | Audit inventory, recommendations, review point; no implemented maintenance action/status history | The exact `Condition_Evidence_ID → Inspection_Record_ID → Action_Status` conjunction remains absent in these two works. |
| Validation | Functional single-case demonstration | Perceived utility/design evaluation by experts | Neither executes the G3 exact-oracle acceptance contract. |

## 5. Chapter update implications

This section records required literature-pressure updates only. It does not edit Chapter 5.

| Chapter/claim area | Full-text implication |
|---|---|
| Sensor-to-IFC linkage | State that GUID-based linkage between IFC element records and separate sensor time-series storage has been implemented. Do not claim this generic linkage as novelty. |
| Time-series handover | Acknowledge Sedigh's implemented current/history display and IFC export. Distinguish export capability from exact round-trip semantic parity, referential integrity, and lifecycle reconstruction. |
| Human-in-the-loop inspection | Acknowledge Wu's expert-evaluated mixed-initiative audit framework and component-level inventory scenarios. Do not claim the general concept of human review or multimodal audit workflow as absent. |
| Evidence qualification | Preserve the distinction between raw/current/historical sensor values or predicted inventory annotations and a governed `Condition_Evidence_ID` with source, method, uncertainty, scope, and review provenance. Neither source supplies the complete thesis contract. |
| Action/closure | Do not reinterpret Wu's management recommendations/review point or Sedigh's automation potential as an implemented `Action_Status`, authorized transition, post-action verification, or closure. |
| Gap 3 tests | Retain chain-specific negative fixtures and exact expected/actual forward-reverse result sets. Neither paper tests orphan, duplicate, stale/reused ID, wrong type/cardinality, chronology, authorization, or closure violations. |
| Limited-FEM | Keep `nominal, uncalibrated, reference-only, not used for damage diagnosis`; neither source changes the FEM boundary. |

## 6. Impact on Gap 2

**Current exact gap:** integrated, identified traceability from condition evidence to verified action.

**Full-text verdict:** `NARROWED_BUT_DEFENSIBLE_AS_A_CHAIN-SPECIFIC_CONJUNCTION_GAP`.

Sedigh closes the generic prior-art question for GUID-linked IFC and time-series data on a functioning prototype. Wu closes the generic framework-level question for human-in-the-loop, multimodal building-audit inventory and expert-evaluated workflow design. Therefore, Gap 2 must not be stated as the absence of sensor-BIM linkage, external time-series storage, IFC export, component-level inventory, human review, or audit recommendations.

The residual gap in this two-paper comparison is the implemented conjunction of the unchanged chain `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status` with evidence qualification, stable identity governance, accountable review, explicit status history, and formal post-action verification/guarded closure. This is corpus-bounded and cannot be written as a universal “first” claim. Literature evidence does not freeze G2.

## 7. Impact on Gap 3

**Current exact gap:** integrated referential integrity combined with bidirectional traceability.

**Full-text verdict:** `GENERIC_IDENTITY/EXPORT_FORM_WEAKENED; EXACT_CHAIN_ORACLE_FORM_REMAINS_DEFENSIBLE`.

Sedigh demonstrates GUID-based cross-database lookup and IFC re-export, so a broad claim that sensor/IFC data cannot be linked or returned to IFC is false. Wu proposes iterative traceability of inputs, predictions, feedback, and downstream inventory outputs, so generic workflow traceability is also prior framework art.

Neither paper executes exact expected-versus-actual paired forward/reverse result sets across the canonical chain, source-target-source semantic reconstruction under declared normalization, or rejection of controlled orphan/duplicate/stale/type/cardinality/chronology/authorization/closure failures. `Bi-directional interaction` in Wu concerns human-model feedback; `export` in Sedigh is not an exact round-trip oracle. The chain-specific G3 acceptance contract therefore remains the defensible residual, subject to implementation and execution.

## 8. Prohibited claims and corrected wording

- Do not claim that no prior work links sensor time-series records to IFC elements by GUID.
- Do not claim that IFC export of operational time-series data is absent; Sedigh implements a proof of concept.
- Do not call Sedigh's AHU prototype an inspection/evidence/action system or a verified lifecycle closure chain.
- Do not call Wu's framework/application schema a deployed prototype or tested ML inspection platform; prototype implementation/testing is future work.
- Do not interpret Wu's `bi-directional interaction` as bidirectional IFC synchronisation, reverse traceability, or exact round-trip parity.
- Do not claim that human-in-the-loop building audit, component inventory, standardized iteration, or expert-evaluated audit workflow design is absent.
- Do not alter `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status` or add source-specific identifiers to it.
- Do not open calibrated FEM, damage diagnosis, predictive maintenance, RUL, autonomous maintenance, field diagnosis, or commercial software development.

## 9. Evidence limitations and gate statement

**Evidence limitation:** the two sources occupy different evidence levels. Sedigh is an implemented but small positive-path laboratory prototype; Wu is a broader expert-evaluated framework whose technical prototype and task testing are explicitly deferred. Their capabilities cannot be combined as if one integrated system had implemented both.

**Governance limitation:** this record evaluates literature pressure only. It does not approve the identifier registry, schema, competency questions, Constraint Catalogue, Fixture/Oracle Manifest, ADR, G2 baseline, or G3 execution.

**Gate statement:** G2 remains `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN`. G3 remains `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED`, with execution `EXECUTION-NOT-OPEN` until the G2 package is approved and baselined. No RQ, WP, Chapter, Paper, Evidence Gate, canonical identifier, or Limited-FEM boundary changes through this evidence record.
