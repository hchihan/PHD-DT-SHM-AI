# G2-G3 Recent Evidence Screening 2023-2026

**Research mapping:** RQ2/WP2 -> Chapter 5 -> Paper 2 -> Gate 2-3  
**Screening date:** 2026-08-04  
**Zotero scope:** `RQ2_RQ3_CORE_DEEP_READ_20260803` (`C9J2V33M`) and `Deep_read_04.08.2026` (`GZYTA3TB`)  
**Locked chain:** `Condition_Evidence -> BIM component -> Inspection_Record -> Action_Record -> Status_Event -> accountable human review`  
**Excluded scope:** calibrated FEM, damage diagnosis, predictive maintenance, RUL, autonomous maintenance, and commercial software development.

This is a bounded evidence-screening report, not a systematic-review claim of universal absence. **Trong phạm vi các tài liệu đã sàng lọc và tìm kiếm...** all novelty conclusions below are corpus-bounded. `Yes` is used only for content described and implemented in the paper; a capability statement, UI screenshot, or future-work statement is not sufficient.

## 1. Executive summary

- **Zotero corpus:** 37 distinct current records were listed: 34 direct members of `C9J2V33M` plus three direct members of `GZYTA3TB`. Eight papers already deep-read in Rounds 1-2 were excluded from repeat reading: Bellon (`NUTL57KJ`), Lorvão Antunes (`XUN8EX6X`), Lee (`GWP87WLC`), Oraskari (`AQDJR2UE`), Sacks (`F8RMUZ44`), Xu (`Z4IBWW9Y`), Wan (`Y44EIXWG`), and Isailović (`9TDVUE9Q`). The remaining **29 current Zotero records**, listed with keys in Section 2, were screened using title, year, abstract, keywords, notes, and targeted method/results/conclusion text where needed.
- **Remaining-Zotero decisions:** **6 DIRECTLY_RELEVANT**, **10 SUPPORTING**, **6 BACKGROUND**, and **7 EXCLUDE**. Excluded records are duplicates, non-bibliographic attachments, unverified webpages, or studies whose substantive contribution is outside the locked scope.
- **Recent search:** 13 documented, non-duplicate 2023-2026 peer-reviewed records were retained after DOI/publisher, Crossref, or OpenAlex metadata verification and targeted full-text inspection where accessible. Discovery records that could not support a bounded claim were not counted as screened evidence. No item was imported into or edited in Zotero.
- **Closest new operational competitor:** **Li et al. (2023)** implements defect IDs, component linkage, inspection-data storage, maintenance recommendations, stored repair records, and a current `completed` flag. It narrows the operational chain substantially, but does not implement a timestamped status-event sequence or linked post-action verification.
- **Closest new interoperability competitor:** **Piras et al. (2026)** preserves `IfcGlobalId` in OpenMAINT, imports 428 maintainable assets from IFC to CMMS, maps current condition and last-check fields, executes IFC validation, and supports GUID-based CMMS-to-BIM visual lookup/navigation. It does not demonstrate an `Action_Record` instance, persisted `Status_Event` sequence, CMMS-to-IFC transactional write-back, strict negative fixtures, or post-action verification.
- **Strongest new validation pressure:** **Nuyts et al. (2024)** already implements paired compliant/non-compliant construction-data fixtures across several validation approaches. **Hagedorn et al. (2023)** already implements SHACL-based cross-domain link validation and direct/inverse navigation in ICDD. Therefore, generic deliberate invalid fixtures and generic bidirectional link checks are not safe standalone novelty claims.
- **Novelty-boundary decision:** the boundary is **narrowed but not fundamentally displaced**. Paper 2 must not claim novelty for BIM-CMMS integration, SHACL/SPARQL checking, valid/invalid compliance fixtures, or bidirectional linking separately. The defensible contribution remains their chain-specific combination: stable identities across condition evidence, component, inspection, action and events; preserved evidence basis; accountable authorization; formal verified closure; chain-specific integrity mutations; and paired forward/reverse acceptance tests.
- **Stopping rule:** searching stopped after two consecutive query families, covering component IDs plus post-repair verification and approval/rejection plus execution/verification/closure, produced no new in-scope study capable of changing the integrated novelty boundary. This is saturation within the executed search, not proof of universal absence.
- **Round 3 queue:** six papers are recommended: Li et al. (2023), Piras et al. (2026), Nuyts et al. (2024), Hagedorn et al. (2023), Mohamed et al. (2023), and Celik et al. (2023). This queue prioritizes recent direct competitors and covers Groups A-D. Jia et al. (2025) received sufficient targeted full-text screening for the current boundary decision; Yang et al. (2025) does not warrant Round 3 because it stops at monitoring and alerts.

**Overall verdict: Narrowed.** **Trong phạm vi các tài liệu đã sàng lọc và tìm kiếm...** broad inspection-maintenance integration and generic validation methods are established prior art, while the complete accountable record-event chain and formal post-action closure remain unestablished. For any stronger universal claim, the verdict is **Evidence insufficient**.

## 2. Remaining Zotero screening matrix

| Zotero key | Citation | Year | Relevance | Relevant question group | What it may establish | Main limitation | Decision |
|---|---|---:|---|---|---|---|---|
| `JZVZCHRI` | Hüthwohl et al., *Integrating RC bridge defect information into BIM models* | 2018 | DIRECTLY_RELEVANT | A | IFC/BIM schema for component-linked bridge defect and inspection attributes | Pre-2023; broad defect/inspection representation overlaps Round 2; action/event/accountability not established from current screening | Retain; deep-read only if an exact field-level comparison remains unresolved |
| `2ILY9YZ3` | Theiler & Smarsly, *IFC Monitor - An IFC schema extension for modeling structural health monitoring systems* | 2018 | SUPPORTING | A, C | IFC extension, identity context, and deliberately invalid schema-model checks for monitoring systems | Monitoring-system model, not inspection-action records; strict four-part fixture-oracle evidence was not re-read here | Retain as schema-method support; **Evidence insufficient** for a strict negative-test claim |
| `YIJ57IV5` | Pauwels & Terkaj, *EXPRESS to OWL for construction industry* | 2016 | BACKGROUND | C | Methodological basis for converting IFC EXPRESS to ifcOWL | No domain workflow, negative fixtures, or accountability | Background only |
| `VI5QMSAE` | Kim et al., *Integration of IFC objects and facility management work information using Semantic Web* | 2018 | DIRECTLY_RELEVANT | A, D | Semantic link from BIM elements to historical FM work records and work-record retrieval | Current abstract does not establish stable action IDs, status-event history, authorization, or post-action verification | Retain as historical work-record comparator; not in the recent-priority queue |
| `XSKNR656` | Armijo & Zamora-Sánchez, *Integration of Railway Bridge Structural Health Monitoring into the Internet of Things with a Digital Twin* | 2024 | EXCLUDE | - | Long-term sensor storage and anomaly monitoring | Dominant contribution is SHM/anomaly detection and automated warnings, outside the locked evidence-to-action information-model scope | Exclude from Paper 2 evidence queue |
| `N54RGGHL` | *Development of a Bridge Management System Based on the Building Information Modeling Technology* | n.d. | EXCLUDE | - | Possible duplicate/surrogate record | Webpage has no verified authors/date and duplicates a journal paper already deep-read | Exclude duplicate/unverified record |
| `Q4PJY4QN` | Monfardini et al., *Use of competency questions in ontology engineering: a survey* | 2023 | SUPPORTING | C | CQ use for ontology scope and conceptual evaluation | Generic ontology-engineering survey; no inspection-action chain or executed integrity fixtures | Retain as the fuller bibliographic representation |
| `K9TSRA2X` | Monfardini et al., conference record with the same CQ-survey title | 2023 | EXCLUDE | - | Duplicate representation of the 63-participant CQ survey | Does not add independent evidence beyond `Q4PJY4QN` | Exclude duplicate from evidence counts |
| `TMZJ5PYK` | *PROV-O: The PROV Ontology* webpage | n.d. | EXCLUDE | - | Provenance vocabulary | Duplicate webpage record; canonical bibliographic PROV-O item is present | Exclude duplicate record |
| `JDCNEFI7` | *IfcRoot - IFC 4.3.2 Documentation* webpage | n.d. | EXCLUDE | - | IFC identity definition | Duplicate/unstructured webpage record; canonical buildingSMART item is present | Exclude duplicate record |
| `2H6XA32D` | *ISO 55000:2024* webpage | n.d. | EXCLUDE | - | Asset-management vocabulary | Duplicate webpage record and not peer-reviewed study evidence | Exclude duplicate record |
| `MSI2K38K` | Carvalho et al., *BIM model to support O&M tasks* | 2023 | DIRECTLY_RELEVANT | A, B | Maintenance-sheet structure linking Element ID to inspection, cleaning, correction, replacement, schedule and cost | Abstract/notes do not establish event identity, status transitions, inverse queries, or verified closure | Retain; exact fields remain useful but stronger recent competitors take Round 3 priority |
| `JGM5YHH8` | Quinn et al., *Building automation system-BIM integration using a linked data structure* | 2020 | SUPPORTING | A, C | Naming convention and linked-data relation between BAS points/time series and BIM/FM context | Sensor-point linkage only; no inspection/action/review workflow | Retain for identity-pattern support |
| `8PB7EN2E` | ISO, *Asset management - vocabulary, overview and principles* | 2024 | BACKGROUND | A, D | Current asset-management vocabulary and lifecycle framing | Standard, not empirical peer-reviewed implementation evidence | Use for terminology only |
| `TXRF6GUC` | Ciccarese et al., *PAV ontology: provenance, authoring and versioning* | 2013 | SUPPORTING | D | Creator, importer, retriever, version, and previous-version properties | Domain-neutral; no authorization or evidence-to-action implementation | Retain as provenance vocabulary support |
| `WFVDNKSJ` | U.S. GSA, *BIM Guide Series 08: Facility Management* | 2011 | BACKGROUND | A | Persistent human-readable Asset ID alongside BIM GUID for CMMS/BAS exchange | Guidance rather than peer-reviewed research; pre-2023 | Background/requirements context only |
| `3S858MKE` | Theiler et al., *BIM-based design of structural health monitoring systems* | 2017 | SUPPORTING | A, C | Implementation precedent for IFC-modeled sensors and monitoring systems | Laboratory SHM design; no inspection/action/event/accountability chain | Retain as technical foundation only |
| `B8QZMS77` | Moreau & Missier, *PROV-DM: the PROV data model* | 2013 | BACKGROUND | D | Entity-activity-agent provenance relations | Normative domain-neutral model; no construction implementation or review workflow | Background vocabulary |
| `FJJAV9T4` | Lebo et al., *PROV-O: the PROV ontology* | 2013 | BACKGROUND | D | OWL encoding for usage, derivation, generation, and attribution | Normative vocabulary; no chain validation | Background vocabulary |
| `SEZBLZHH` | Rasmussen et al., *Building topology ontology (BOT)* | 2020 | SUPPORTING | A, C | Lightweight identity/topology relations alignable with IFC | Topology only; no inspection, action, event, or accountability semantics | Retain as component-relation support |
| `EY3GJVZV` | buildingSMART, *IfcRoot and IfcGloballyUniqueId - IFC 4.3.2.0 official documentation* | 2024 | SUPPORTING | A, C | Mandatory `GlobalId`, uniqueness rule, and identifier semantics | Normative documentation, not workflow evidence or cross-version identity validation | Retain as normative identity basis |
| `8HJN7D7E` | Stolk & McGlinn, *Validation of IfcOWL datasets using SHACL* | 2020 | SUPPORTING | C | SHACL shapes derived from OWL restrictions for cardinality, class, datatype, and values, with instance-graph validation reports | No target-domain records, strict mutation suite, reverse chain, or parity; Zotero abstract overstates WHERE-rule coverage | Retain as validation-method support |
| `GUEJBZBZ` | Du et al., *BIM and IFC Data Readiness for AI Integration in the Construction Industry* | 2024 | BACKGROUND | C | Review-level evidence on IFC data-preparation and time-series/toolchain barriers | AI-readiness review; does not test the locked record chain | Background only |
| `EMTIHHX4` | Celik et al., *Blockchain supported BIM data provenance for construction projects* | 2023 | SUPPORTING | B, D | Transaction, object version, issuing discipline, actor/time, responsibility/liability, and queryable provenance history | Design/construction information exchange rather than inspection-maintenance actions | Round 3 candidate for exact event/accountability fields and implementation boundary |
| `3II2WKLN` | Wang et al., *Enhancement and validation of ifcOWL ontology based on SHACL* | 2024 | DIRECTLY_RELEVANT | C | Executable conversion of IFC WHERE rules to SHACL/SPARQL constraints and ifcOWL validation | Generic IFC integrity; no evidence-to-action records, strict negative manifest, or accountability | Retain; reserve deep-read if Hagedorn/Nuyts leave a rule-translation question open |
| `LSYSC59G` | *Gate 2.1 - caos-9* | n.d. | EXCLUDE | - | Project attachment | Non-bibliographic attachment; cannot serve as peer-reviewed academic evidence | Exclude |
| `QMPFIBQX` | Yang et al., *Design and Validation of a Real-Time Maintenance Monitoring System Using BIM and Digital Twin Integration* | 2025 | SUPPORTING | A, B | Implemented sensor-to-cloud-to-BIM pipeline, persisted time series, alert flags, and field reliability observations | No stable asset ID contract, inspection/action entity, accountable event history, reverse query, or post-action verification; predictive maintenance is future direction | Targeted screening complete; do not place in Round 3 queue |
| `SWDG5DIH` | Jia et al., *A Semantic Web and IFC-Based Framework for Automated BIM Compliance Checking* | 2025 | DIRECTLY_RELEVANT | C | Executed Jena/IfcOWL mapping and SPARQL compliance queries with component-level violations | Design-deliverable compliance, not operational inspection-maintenance; no action/status/accountability/closure or strict negative fixture | Targeted screening complete; use as constraint-method evidence, not closest domain competitor |
| `P3YLFNJZ` | Piras et al., *An Open Standard Methodology for BIM-CMMS Integration* | 2026 | DIRECTLY_RELEVANT | A, C | `IfcGlobalId`-preserving IFC-to-OpenMAINT import, current condition/last-check fields, IFC validation, and asset lookup | Static one-directional handover; no instantiated work order, persisted event history, strict negative suite, transactional write-back, or post-action verification | Round 3 direct-competitor priority |

**Corpus reconciliation:** the current 34-item membership differs from the earlier screening snapshot. The earlier report listed Keet and Khan (2025), whereas the current collection contains `LSYSC59G` instead. The sibling collection `RQ2/WP2/Paper 2/Gate 2-3` (`C2J6ITDM`) was also checked: its eight records are already represented in `C9J2V33M` and add no distinct screening item. This report uses the live Zotero membership retrieved on 2026-08-04 and records the drift rather than silently combining snapshots.

## 3. New 2023-2026 candidate matrix

The search used combinations of BIM/IFC/CMMS, inspection/work order, component identity, status/event/approval/closure, SHACL/IDS/ICDD, referential integrity, negative fixtures, bidirectional/round-trip, provenance, accountability, and post-action verification. Discovery used OpenAlex, Crossref, publisher search, and citation chaining; metadata were checked through DOI/publisher and Crossref/OpenAlex records. Only peer-reviewed journal articles or peer-reviewed proceedings/chapters were retained.

- **Group A:** inspection-maintenance information models and record/component linkage.
- **Group B:** workflow state, persisted status events, approval/rejection, execution, verification, and closure.
- **Group C:** referential integrity, constraints, negative fixtures, direct/inverse links, and round-trip parity.
- **Group D:** accountability, provenance, authorization, responsibility, and audit trail.

Groups are non-exclusive; one paper can contribute to multiple groups.

| Rank | Citation | DOI | Group A/B/C/D | What it appears to contribute | Full-text status | Deep-read priority |
|---:|---|---|---|---|---|---|
| 1 | Li, S., Zhang, Z., Lin, D., Zhang, T., & Han, L. (2023). *Development of a BIM-based bridge maintenance system (BMS) for managing defect data*. Scientific Reports, 13, 846. | `10.1038/s41598-023-27924-6` | A, B | Implements generated defect IDs, component/defect model linkage, MySQL inspection-data storage, maintenance recommendations, stored repair records, and a current `completed` flag. It directly narrows the operational chain, but no timestamped event history or linked post-action verification is demonstrated. | Open-access publisher full text inspected | P1 - direct competitor |
| 2 | Nuyts, E., Bonduel, M., & Verstraeten, R. (2024). *Comparative analysis of approaches for automated compliance checking of construction data*. Advanced Engineering Informatics, 60, 102443. | `10.1016/j.aei.2024.102443` | C | Implements multiple validators and deliberate compliant/non-compliant datasets with stored outputs. It establishes generic paired fixtures, but the screened artifacts do not show an automated exact expected-versus-actual violation-set assertion, record-chain foreign keys, lifecycle events, or round-trip reconstruction. | Full text and OSF reproducibility artifacts inspected | P1 - changes validation novelty boundary |
| 3 | Hagedorn, P., Pauwels, P., & König, M. (2023). *Semantic rule checking of cross-domain building data in information containers for linked document delivery using the shapes constraint language*. Automation in Construction, 156, 105106. | `10.1016/j.autcon.2023.105106` | C | Implements SHACL-SPARQL cross-document validation, identifier resolution, and inferred direct/inverse relations in ICDD. Strong prior art for generic link integrity and reverse navigation; no write-back parity or exact inverse-edge oracle is demonstrated. | Full text, benchmark code, and data inspected | P1 - changes referential-integrity boundary |
| 4 | Mohamed, A. G., Khaled, A., & Abotaleb, I. S. (2023). *A Bridge Information Modeling (BrIM) Framework for Inspection and Maintenance Intervention in Reinforced Concrete Bridges*. Buildings, 13(11), 2798. | `10.3390/buildings13112798` | A, B | Implements an as-is BrIM bridge inventory with inspection, maintenance, and repaired/unrepaired defect histories, discovery dates, current status, and next inspection/maintenance dates. Current status is a field, not a demonstrated append-only event sequence; structured action-to-verification linkage remains unclear. | Publisher full text inspected | P1 - direct schema/workflow competitor |
| 5 | Jeon, C.-H., Nguyen, D.-C., Roh, G., & Shim, C.-S. (2023). *Development of BrIM-Based Bridge Maintenance System for Existing Bridges*. Buildings, 13(9), 2332. | `10.3390/buildings13092332` | A | Derives owner/manager/inspector requirements, uses an inventory-code system, maps inspection information, and supports assessment/reporting. It narrows component-record identity and inspection-information requirements, but does not establish a work-order event lifecycle or verified closure. | Open-access publisher full text | P2 - supporting direct competitor |
| 6 | Jaskula, K., Kifokeris, D., Papadonikolaki, E., & Rovas, D. (2025). *Blockchain-Based Decentralized Common Data Environment: User Requirements and Conceptual Framework*. Journal of Construction Engineering and Management, 151(9), 04025112. | `10.1061/JCEMD4.COENG-14852` | B, D | Elicits requirements for accountable, transparent, tamper-resistant whole-asset history and proposes a blockchain/IPFS CDE. It narrows generic immutable-history claims, but the framework is conceptual and lacks operational maintenance transitions and authorization tests. | Publisher metadata and author-accepted manuscript verified | P2 - accountability requirements support |
| 7 | Schuler, P.-C., Mirboland, M., Voigt, C., & Koch, C. (2025). *Using Linked Data Containers for BIM Based Structural Inspection Workflows*. In Advances in Information Technology in Civil and Building Engineering, pp. 398-409. | `10.1007/978-3-031-84224-5_32` | A, D | Implements an ISO 21597 ICDD bridge material-test case linking heterogeneous evidence from test design to results. Directly relevant to evidence-basis preservation; no actor authorization, action closure, negative links, or parity test is reported. | Publisher chapter endpoint verified | P2 - evidence-provenance support |
| 8 | Pauwels, P., van den Bersselaar, E., & Verhelst, L. (2024). *Validation of technical requirements for a BIM model using semantic web technologies*. Advanced Engineering Informatics, 60, 102426. | `10.1016/j.aei.2024.102426` | C | Implements semantic and geometric requirement checking, including a known-invalid dimensional condition and reported violations. Useful for violation-result structure; not a chain-level mutation suite or exact round-trip test. | Open-access full text verified | P2 - validation support |
| 9 | Oliveira, A., Granja, J., Bolpagni, M., Motamedi, A., & Azenha, M. (2024). *Development of standard-based information requirements for the facility management of a canteen*. Journal of Information Technology in Construction, 29, 281-307. | `10.36680/j.itcon.2024.014` | A, C | Demonstrates purpose-driven EIR/LOIN/IFC information requirements for ongoing FM. Strong basis for specifying required fields before implementation, but no executed CMMS work-order states or closure verification. | Open-access publisher full text | P2 - requirements support |
| 10 | Cerovšek, T., & Omar, M. (2025). *Advancing Semantic Enrichment Compliance in BIM: An Ontology-Based Framework and IDS Evaluation*. Buildings, 15(15), 2621. | `10.3390/buildings15152621` | C | Executes seven IDS checks across five tools and exposes divergent results. This is cross-tool differential evidence, not authoritative oracle comparison, source-target-source parity, or a controlled certification suite. | Open-access publisher full text inspected | P2 - checker-reliability support |
| 11 | Cavieres-Lagos, S., Muñoz La Rivera, F., Atencio, E., & Herrera, R. F. (2024). *Integration of BIM Tools for the Facility Management of Railway Bridges*. Applied Sciences, 14(14), 6209. | `10.3390/app14146209` | A, C | Implements bidirectional Revit-Dynamo-Excel exchange linking structural-condition records to bridge elements. It narrows generic bidirectional exchange, but lacks action identity, event history, accountability, and post-action verification. | Open-access publisher full text | P2 - exchange support |
| 12 | Jeon, C.-H., Kwon, T. H., Kim, J., Jung, K.-S., & Park, K.-T. (2024). *Health Index-Based Maintenance of Prestressed Concrete Bridges Considering Building Information Modeling Application*. Buildings, 14(12), 4032. | `10.3390/buildings14124032` | A, B | Uses accumulated inspection/repair reports and documents a subsequent condition-grade observation after repair. It supports the need for post-repair assessment, but does not encode the repair-to-inspection relation as a verification transaction or closure guard. | Open-access publisher full text inspected | P2 - post-repair reasoning support |
| 13 | Gao, Y., Xiong, G., Hu, Z., Chai, C., & Li, H. (2024). *Bridge Digital Twin for Practical Bridge Operation and Maintenance by Integrating GIS and BIM*. Buildings, 14(12), 3731. | `10.3390/buildings14123731` | A | Integrates WebGIS/WebBIM/CDE and JSON defect information for inspection and maintenance planning. Useful system context, but does not establish stable cross-system record IDs, completed work orders, status history, or verified closure. | Open-access publisher full text | P3 - background |

This matrix reports only sources used in the novelty decision. Discovery hits that remained metadata-only, duplicated stronger evidence, or fell outside the operational inspection-action boundary are not used to support absence or novelty conclusions.

## 4. Analysis of the three newly added full-text papers

### 4.1 Jia et al. (2025)

**Claim -> Evidence available -> Relevance to G2/G3 -> Main limitation -> Need for deep-read**

- **Claim:** semantic-web/IFC mapping and executable SPARQL can automate architectural design-code checking and identify non-compliant BIM components.
- **Evidence available:** a Jena/Fuseki prototype converts IFC to IfcOWL, applies mapping/query rules, and executes a railing-height rule. Two `IfcRailing` entities at 900 mm are returned against an 1100 mm requirement and checked against locations in the original model.
- **Relevance to G2/G3:** strong method evidence for executable constraints, requirement-to-result forward traceability, and result-to-model checking. It supports how G3 could report rule, focus component, offending value, and violation.
- **Main limitation:** this is design-deliverable compliance, not in-service inspection. It does not persist an operational inspection record, action, status history, accountable approval, or remediation verification. The non-compliant railings are not documented as deliberately injected fixtures with a predeclared oracle.
- **Need for deep-read:** targeted full-text screening is sufficient for the current novelty decision. Further reading is only needed if Paper 2 adopts its exact SPARQL result schema or requires its source artifacts.

| Component | Yes / Partial / No | Strict basis |
|---|---|---|
| Stable component/asset identity | Partial | Same RDF entities are mapped and violating `IfcRailing` objects are located, but no `GlobalId` persistence, URI policy, or cross-version identity test is reported |
| Condition or inspection record | Partial | Executed component-level compliance findings exist, but they are design-check results without an operational inspection-record ID, inspector, date, version, or disposition |
| Action/work-order record | No | Users may modify components, but no action instance, work order, assignee, execution, or closure is recorded |
| Persisted status/event history | No | IfcOWL data are stored, but no successive status events or transition history are modeled |
| Provenance/accountability | Partial | The IFC-to-RDF-to-query processing chain and code source are identifiable; record-level actor, approval, rule version, and audit fields are absent |
| Executable constraints | Yes | Jena mapping rules and SPARQL templates are executed; the railing rule returns two violations |
| Deliberate negative tests | No | Non-compliance is detected, but intentional fixture creation, predefined expected failure, and actual-versus-expected assertion are not reported |
| Forward traceability | Yes | Code clause -> SPARQL rule -> execution -> violating component is demonstrated within one run |
| Reverse traceability | Partial | Results are checked against original IFC locations, but no persistent automated result-to-source backlink/query is demonstrated |
| Post-action verification | No | No corrected model, rerun, pass result, or closure record is reported |

### 4.2 Piras et al. (2026)

**Claim -> Evidence available -> Relevance to G2/G3 -> Main limitation -> Need for deep-read**

- **Claim:** a vendor-neutral IFC enrichment workflow can populate an open-source CMMS while retaining asset identity and operational fields.
- **Evidence available:** 12 models from two residential buildings, about 9000 IFC elements, 428 imported maintainable assets, custom FM Psets, buildingSMART validation, cross-viewer checks, JSON field mapping, and preservation of `IfcGlobalId` in OpenMAINT. The authors report a one-to-one IFC-CMMS correspondence and positive-path import success.
- **Relevance to G2/G3:** strongest new evidence for stable asset identity, condition/last-check fields, forward IFC-to-CMMS transfer, generic IFC constraints, and reverse visual lookup. It directly removes any safe novelty claim based only on open-standard BIM-CMMS integration.
- **Main limitation:** the implemented transfer is static and one-directional. Work orders are described as associateable with assets but no actual work-order record, action ID, status sequence, execution result, or closure is tested. CMMS updates, inspection outcomes, and replacements are not written back to the AIM. No strict negative fixture or post-action verification exists.
- **Need for deep-read:** highest Round 3 priority. Extract exact mapping fields, keys, OpenMAINT record structures, validation reports, processing logs, and the boundary between visual bidirectional lookup and transactional synchronization.

| Component | Yes / Partial / No | Strict basis |
|---|---|---|
| Stable component/asset identity | Yes | Original `IfcGlobalId` is preserved as the CMMS asset identifier for 428 assets; no duplicate/broken GUID link is reported in the tested import |
| Condition or inspection record | Partial | `Condition` and `Last_Check_Date` are populated from inspection/on-site or latest maintenance records and checked after import, but no explicit `Inspection_Record` identity or history is implemented |
| Action/work-order record | Partial | OpenMAINT can associate work orders with components, but no instantiated work-order ID, assignee, status, execution, or result is presented |
| Persisted status/event history | No | Scalar current/latest fields are demonstrated; no event identity, previous/new status, append-only sequence, or history query is tested |
| Provenance/accountability | Partial | Attribute source/assignment logic and processing logs exist; record-level source IDs, responsible actors, approval, signatures, and immutable audit history do not |
| Executable constraints | Yes | buildingSMART validation executes STEP syntax, IFC4 schema, inverse, cardinality, and type checks; FM workflow rules are not validated |
| Deliberate negative tests | No | Successful valid imports are reported; no intentionally invalid record and expected rejection are tested |
| Forward traceability | Yes | IFC/Pset/`IfcGlobalId` -> JSON mapping -> OpenMAINT asset is demonstrated and sample fields are compared |
| Reverse traceability | Partial | GUID-based CMMS-to-BIM lookup/navigation is available, but CMMS-to-IFC transactional write-back is explicitly absent |
| Post-action verification | No | No completed maintenance action, reinspection, before/after evidence, acceptance decision, or closure guard is demonstrated |

### 4.3 Yang et al. (2025)

**Claim -> Evidence available -> Relevance to G2/G3 -> Main limitation -> Need for deep-read**

- **Claim:** a BIM-Digital Twin-IoT system can continuously monitor a noise-barrier tunnel and flag anomalous structural/environmental sensor behavior.
- **Evidence available:** an operational field demonstration from 22 October to 7 November 2024, CSV/JSON time series, a sensor-to-cloud-to-dashboard pipeline, threshold/status rules, measured transmission coverage, and observed data gaps or failed streams.
- **Relevance to G2/G3:** supports minimum `Condition_Evidence` context, sensor status, sampling interval, data-completeness fields, and the need to distinguish naturally occurring failures from controlled validation fixtures.
- **Main limitation:** the system ends at monitoring, alerts, and decision support. It does not define stable asset identity, an inspection/action record, accountable status-event history, reverse query, or verified closure. Predictive maintenance is future direction and remains outside thesis scope.
- **Need for deep-read:** no Round 3 deep-read is recommended. Additional screenshots are unlikely to change the entity/workflow boundary; underlying data schemas or test logs would be needed instead.

| Component | Yes / Partial / No | Strict basis |
|---|---|---|
| Stable component/asset identity | Partial | Sensors and locations are distinguished, but no asset ID/IFC GlobalId contract, uniqueness rule, model-version binding, or stability test is reported |
| Condition or inspection record | Partial | Timestamped CSV/JSON condition evidence is persisted; no formal `Inspection_Record` with inspector, approval, version, or lifecycle exists |
| Action/work-order record | No | Alerts support decisions, but no recommendation/action/work-order entity or execution record exists |
| Persisted status/event history | Partial | Sensor values and alert/status flags are logged, but not as append-only action events with prior/new state, actor, reason, and transition rules |
| Provenance/accountability | Partial | Sensor type/location/time and the technical pipeline are identifiable; no creator, inspector, reviewer, approver, rationale, or audit lineage exists |
| Executable constraints | Partial | Threshold and hardware-status rules execute, but they are not identity, foreign-key, authorization, or lifecycle constraints |
| Deliberate negative tests | No | Data loss and failed streams occurred naturally; no seeded invalid fixture, predefined failure, or oracle is reported |
| Forward traceability | Partial | Physical sensor -> cloud -> processing -> BIM/dashboard is demonstrated, but not the locked record chain |
| Reverse traceability | No | No component/action/status-to-originating-evidence query or parity test is reported |
| Post-action verification | No | Communication testing validates the monitoring system, not a maintenance action or closure outcome |

## 5. Novelty stress test

### 5.0 Cross-candidate capability check

This matrix extends the detailed three-paper assessment to the other high-impact candidates. A compact label is used only where the screened evidence is sufficient; `Partial` includes implemented subchains and explicitly conceptual but relevant models. It does not mean the complete G2/G3 capability exists.

| Study | Stable component/asset identity | Condition or inspection record | Action/work-order record | Persisted status/event history | Provenance/accountability | Executable constraints | Deliberate negative tests | Forward traceability | Reverse traceability | Post-action verification |
|---|---|---|---|---|---|---|---|---|---|---|
| Piras et al. (2026) | Yes | Partial | Partial | No | Partial | Yes | No | Yes | Partial | No |
| Jia et al. (2025) | Partial | Partial | No | No | Partial | Yes | No | Yes | Partial | No |
| Yang et al. (2025) | Partial | Partial | No | Partial | Partial | Partial | No | Partial | No | No |
| Li et al. (2023) | Partial | Yes | Partial | Partial | Partial | No | No | Yes | No | No |
| Mohamed et al. (2023) | Yes | Yes | Partial | Partial | Partial | No | No | Yes | No | No |
| Nuyts et al. (2024) | Partial | No | No | No | Partial | Yes | Yes | Partial | No | No |
| Hagedorn et al. (2023) | Partial | No | No | No | Partial | Yes | No | Yes | Yes | No |
| Jeon et al. (2023) | Partial | Yes | Partial | No | Partial | No | No | Partial | No | No |
| Celik et al. (2023) | Partial | No | No | Partial | Yes | Partial | No | Partial | Partial | No |
| Schuler et al. (2025) | Partial | Partial | No | No | Partial | No | No | Partial | No | No |
| Jaskula et al. (2025) | No | No | No | Partial | Partial | No | No | No | No | No |

Interpretive controls:

- Piras's reverse result is only GUID-based lookup/navigation; transactional CMMS-to-IFC synchronization is absent.
- Li's `completed` marker is a current field, not a timestamped `Status_Event`; stored repair records are not linked to a formal verification record.
- Mohamed's repaired/unrepaired history and current status narrow the action/status boundary, but the screened implementation does not demonstrate immutable transitions or guarded closure.
- Hagedorn's `Yes` for reverse traceability is limited to implemented direct/inverse ICDD links; it is not lifecycle reconstruction or round-trip parity.
- Nuyts's `Yes` for negative tests concerns deliberately compliant/non-compliant compliance-checking models; it does not cover identity, foreign-key, workflow, authorization, or closure mutations.
- Jeon's `Yes` for inspection records reflects implemented inspection-information mapping and reporting; stable global identity and action lifecycle still require full-text confirmation.
- Jaskula's event-history and accountability ratings remain `Partial` because the blockchain/IPFS CDE is conceptual rather than an operational maintenance ledger.

### 5.0.1 Novelty-impact matrix

| Proposed novelty claim | Prior art that changes the claim | Impact on Paper 2 | Corpus-bounded limitation | Verdict |
|---|---|---|---|---|
| BIM-linked inspection and maintenance information | Li (2023), Mohamed (2023), Jeon (2023), Bellon (2025), Wan (2019) | Cannot be claimed independently; Paper 2 must specify record identities, relations, event semantics, and executable acceptance criteria | Implementations differ in exact entities and validation depth | **Established** |
| Open-standard BIM-CMMS integration using IFC identity | Piras (2026) | Cannot be claimed independently; stable record IDs beyond `IfcGlobalId` and update/write-back behavior remain relevant | One-directional positive-path import, not complete lifecycle synchronization | **Established** |
| Generic SHACL/SPARQL/IDS compliance checking | Jia (2025), Wang (2024), Nuyts (2024), Hagedorn (2023), Cerovšek and Omar (2025) | Rule-language or checker use is not novelty; contribution must be the chain-specific validation contract | These studies do not test the complete evidence-action chain | **Established** |
| Deliberately valid/invalid construction-data fixtures | Nuyts (2024), with pre-2023 precursor evidence from Theiler and Smarsly (2018) | Generic invalid-fixture use is not novelty; exact expected-versus-actual assertions and chain-specific mutation coverage remain defensible | Nuyts provides deliberate fixtures and stored outputs, but no automated exact violation-set oracle was identified | **Established** |
| Chain-specific controlled integrity failure testing | Nuyts (2024), Hagedorn (2023), Lee (2021), and Theiler and Smarsly (2018) establish constituent methods | Paper 2 must limit novelty to predeclared mutations and exact oracles for identity, typed relations, authorization, lifecycle, and closure across the locked chain | No screened source executes this complete mutation-and-oracle contract | **Narrowed** |
| Stable mandatory `Inspection_Record -> Action_Record` relation | Li (2023), Mohamed (2023), Carvalho (2023), Kim (2018), Piras (2026) | The surrounding linkage is prior art; novelty must be limited to explicit IDs, cardinality, evidence basis, inverse retrieval, and lifecycle outcome | Exact action identity and mandatory relation are not consistently exposed | **Narrowed** |
| Immutable/queryable maintenance `Status_Event` history | Celik (2023) implements generic BIM transaction history; Li and Mohamed expose current/history fields | Generic transaction history is prior art, but the strict maintenance event model remains defensible | No screened implementation combines prior/new state, actor, reason, authorization, verification, and closure | **Still strong** |
| End-to-end evidence-basis preservation | Schuler (2025), Hagedorn (2023), Lorvão Antunes (2024), Jia (2025), Yang (2025) | Generic provenance and linked evidence are prior art; Paper 2 must preserve derivation, interpretation, decision, and closure evidence in one chain | Existing subchains stop before accountable action closure | **Narrowed** |
| Bidirectional traceability or exchange | Hagedorn (2023), Cavieres-Lagos (2024), Piras (2026) | Generic direct/inverse links or two-way exchange are not novelty; source-target-source parity under a declared normalization policy remains defensible | No screened study asserts full-chain equality or semantic equivalence after reconstruction | **Narrowed** |
| Generic provenance/audit history | Celik (2023), Jaskula (2025), PROV/PAV foundations | Cannot be claimed independently | Construction exchange or conceptual CDE evidence does not establish maintenance authorization | **Established** |
| Accountable inspection-action approval/rejection/rework | Lorvão Antunes (2024), Celik (2023), Jaskula (2025), Wan (2019) provide roles, agents, responsibility, or review steps | Paper 2 may claim the integrated authorization/event contract if implemented and tested | Authenticated role permissions, separation of duties, rationale, and override tests were not found together | **Still strong** |
| Formal post-action verification and guarded closure | Jeon (2024) gives post-repair observational evidence; Li (2023) stores repair records and a completion flag | Paper 2 may claim explicit verification identity, criteria, before/after evidence, acceptance/rework, and closure guard if implemented | The observed post-repair condition is not encoded as a verification transaction tied to action closure | **Still strong** |
| Complete accountable identity-governed evidence-to-action chain | All screened studies establish only components or subchains | The integrated chain remains the defensible unit of contribution, not its individual techniques | This is a bounded corpus result, not proof of universal absence | **Still strong** |
| Universal “first” or universal absence claim | Targeted rather than exhaustive/systematic search | Do not make this claim | Search saturation cannot establish universal absence | **Evidence insufficient** |

### 5.1 Explicit `Inspection_Record`-`Action_Record` linkage

**Verdict: Narrowed.** Li et al. store repair records and mark solved defects completed; Mohamed et al. model inspection/maintenance and repaired/unrepaired histories; Kim et al. link BIM objects to historical FM work records; Carvalho et al. define element-linked maintenance sheets; Piras et al. preserve IFC identity into a CMMS that can associate work orders; Jeon et al. map component inventory and inspection information. These studies establish most surrounding building blocks. They do not yet demonstrate a stable, mandatory `Inspection_Record_ID -> Action_Record_ID` relation with evidence basis, cardinality, inverse query, and lifecycle outcome. A stronger claim that this exact relation is universally absent has verdict **Evidence insufficient**.

### 5.2 Immutable/queryable `Status_Event` history

**Verdict: Still strong.** Celik et al. provide BIM transaction provenance, while Jaskula et al. propose an immutable accountable lifecycle history. Li and Mohamed expose repair/history/current-status data, while Piras and Yang persist only current/latest fields or monitoring flags. No screened study implements the complete action-state sequence with event ID, previous/new state, actor, reason, authorization, rejection/rework, verification and closure queries.

### 5.3 Evidence-basis preservation

**Verdict: Narrowed.** Schuler et al. link test-design documents through results in an ICDD container; Hagedorn et al. validate linked cross-domain container data; Jia exposes code-to-result lineage; Yang preserves sensor time series. The remaining gap is not generic provenance, but preservation of source evidence, derivation/version, inspection interpretation, action rationale, review decision, and closure evidence in one queryable chain.

### 5.4 Bidirectional traceability and parity

**Verdict: Narrowed.** Hagedorn et al. construct direct and inverse ICDD relations; Cavieres-Lagos et al. report bidirectional BIM-spreadsheet exchange; Piras provides GUID-based visual navigation in both directions. Among the screened studies discussed here, none demonstrates transactionally synchronized `source -> target -> source` reconstruction with equality/semantic-equivalence assertions across evidence, inspection, action and status. Cross-checker agreement in Cerovšek and Omar is not round-trip parity.

### 5.5 Controlled integrity failure testing

**Verdict: Narrowed.** Nuyts et al. already establish the generic method of paired compliant/non-compliant construction-data fixtures, and Pauwels et al. execute a narrow known-invalid requirement case. Therefore, “using deliberate invalid fixtures” is not a standalone novelty. The remaining contribution must be chain-specific mutation coverage for duplicate/reused IDs, orphan and wrong-type relations, missing evidence basis, illegal transitions, unauthorized approval, stale mappings and closure without verification, with predefined violation codes and actual-versus-expected results.

### 5.6 Accountable review/approval

**Verdict: Still strong.** Existing papers provide inspectors/managers, transaction responsibility, attribution, or conceptual accountable history. No screened implementation combines authenticated inspector/reviewer/approver identities, role authorization, rationale, separation of duties, approval/rejection events, override handling, and reverse evidence lineage. A generic human-in-the-loop or blockchain audit trail is insufficient.

### 5.7 Formal post-action verification

**Verdict: Still strong.** Li stores repair records and a current completion flag without a linked verification transaction; Jeon (2024) reports a later post-repair condition observation without an encoded closure relation; Piras does not instantiate work orders or write outcomes back; Jia does not rerun after correction; Yang does not record maintenance; Wan's Round 2 qualified/not-qualified screen remains only partial process/UI evidence. No screened study demonstrates a `Verification_Record` with verifier, criteria, before/after evidence, acceptance/rejection, rework path, and closure guard. A universal absence claim has verdict **Evidence insufficient**.

### 5.8 Complete integrated chain

**Verdict: Still strong.** The screened evidence establishes each surrounding technique separately and several substantial subchains. It does not establish their integration as stable condition-evidence, component, inspection, action, immutable event, accountable review, and verified-closure records with executable forward/reverse and failure contracts.

### Stress-test conclusion

**Trong phạm vi các tài liệu đã sàng lọc và tìm kiếm...** four gaps have verdict **Still strong**: queryable action-event history, accountable authorization, formal post-action verification, and the complete identity-governed evidence-to-action chain. Evidence preservation, bidirectional link validation, chain-specific controlled integrity failure testing, and the inspection-action relation have verdict **Narrowed**. Generic valid/invalid fixture use is **Established**. Paper 2 should claim the integrated chain and chain-specific validation contract, not any one generic technique.

## 6. Deep-read queue

| Order | Study | Why it can change the specification or novelty boundary | Round 3 extraction target |
|---:|---|---|---|
| 1 | Li et al. (2023), `10.1038/s41598-023-27924-6` | Strongest recent operational defect-to-repair-record competitor | Exact database keys, component/defect relations, repair-record fields, completion semantics, actor/time fields, and whether any hidden verification relation exists |
| 2 | Piras et al. (2026), `10.3390/app16104642` | Closest new BIM-CMMS and stable-ID competitor | Exact key mappings, Psets, OpenMAINT entities, work-order capability versus instances, sync direction, logs, validation reports, and update lifecycle |
| 3 | Nuyts et al. (2024), `10.1016/j.aei.2024.102443` | Removes generic valid/invalid fixtures as standalone novelty | Fixture manifest, implicit/explicit oracle, fault granularity, tool outputs, and absent identity/relation/workflow failures |
| 4 | Hagedorn et al. (2023), `10.1016/j.autcon.2023.105106` | Strongest recent referential/inverse-link validation pressure | ICDD identifiers, direct/inverse rules, missing-link cases, benchmark datasets, result schema, and absence of write-back parity |
| 5 | Mohamed et al. (2023), `10.3390/buildings13112798` | May alter the minimum inspection/maintenance history and status model | Bridge/component keys, inspection and maintenance history entities, repaired/unrepaired fields, current-status semantics, actor/time data, and next-action logic |
| 6 | Celik et al. (2023), `10.1016/j.compind.2022.103768` | Strongest current Zotero implementation for BIM transaction provenance and responsibility | Transaction/event identity, actor/time/version fields, role/permission behavior, history queries, tamper evidence, and boundary to operational maintenance authorization |

Not queued:

- **Jia et al. (2025):** targeted full-text screening already establishes its role as design-compliance validation support; it is unlikely to change the operational record-event boundary.
- **Yang et al. (2025):** valuable condition-monitoring context, but no action/status/accountability/verification model.
- **Jeon et al. (2023):** retained as a direct domain comparator, but Li and Mohamed provide stronger immediate pressure on action/history semantics.
- **Kim et al. (2018) and Carvalho et al. (2023):** remain useful field-level comparators; the bounded queue prioritizes recent 2023-2026 evidence with greater novelty impact.
- **Schuler et al. (2025) and Jaskula et al. (2025):** retained as provenance/accountability support, but neither displaces a queue item with a stronger implemented operational or validation boundary.
- **Pauwels et al. (2024):** useful validation support, but Nuyts and Hagedorn have higher boundary impact for the immediate Round 3.
- **Cerovšek & Omar (2025):** useful for checker parity, but Paper 2's immediate risk is chain semantics rather than IDS-tool comparison.

## 7. Recommended next decision

### 7.1 Is Round 3 deep-read needed?

**Yes, but bounded to the six-paper queue.** Li, Piras, Nuyts, Hagedorn, Mohamed, and Celik cover the strongest recent pressures on the operational entity model, interoperability, negative tests, link integrity, status/history, and accountability. Do not deep-read the whole collection.

### 7.2 Which paper should be read first?

1. **Li et al. (2023)** first, because it is the closest operational competitor for defect-to-repair records and completion semantics.
2. **Piras et al. (2026)** second, because it can change asset/action mapping and cross-system identity decisions.
3. **Nuyts et al. (2024)** third, because it changes how negative-fixture novelty must be framed.
4. **Hagedorn et al. (2023)** fourth, because it changes the generic referential and bidirectional-link boundary.
5. **Mohamed et al. (2023)** fifth, because its history/status fields may change the minimum event model.
6. **Celik et al. (2023)** sixth, because its implemented transaction provenance may change accountability and audit requirements.

### 7.3 Does Paper 2's central claim need revision?

**A minor but important revision is needed; the central contribution does not need replacement.** Replace any wording implying novelty in BIM-CMMS integration, SHACL, bidirectional links, or invalid fixtures alone with:

> **Trong phạm vi các tài liệu đã sàng lọc và tìm kiếm...** Paper 2 proposes and evaluates an implementation-neutral, identity-governed evidence-to-action specification that links `Condition_Evidence`, an IFC-identified component, `Inspection_Record`, `Action_Record`, immutable `Status_Event` history and accountable review/verification. Its validation contribution is the combined, chain-specific use of predeclared competency questions, integrity and authorization constraints, controlled identity/relation/workflow mutations, paired forward/reverse queries, and verified-closure guards.

This remains a proposed contribution until G3 executes the tests. Do not describe it as validated before accepted G2 specifications and retained G3 outputs exist.

### 7.4 Which parts of G2 Specification v0.1 can continue to be locked?

- Separation of `Condition_Evidence`, BIM component identity, `Inspection_Record`, `Action_Record`, `Status_Event`, actor/review, and verification entities.
- Use of stable record identities distinct from `IfcGlobalId`, with an explicit cross-system mapping contract; Piras strengthens `IfcGlobalId` as an asset anchor but does not replace record IDs.
- `Action_Status` as a projection or controlled attribute rather than a substitute for `Action_Record_ID`; no screened evidence justifies collapsing identity into status.
- Minimum evidence provenance: source reference, component binding, observation time, method/version, quality context, responsible actor, and review disposition.
- Technology-neutral constraint families: uniqueness, requiredness, cardinality, typed reference, inverse consistency, allowed value, chronology, authorization, and closure guard.
- Predeclared valid/invalid fixture manifests and paired forward/reverse query contracts, provided the claim is framed as chain-specific integration rather than invention of these methods.
- Explicit separation between positive interoperability/conformance results and controlled failure testing.

### 7.5 Which parts must wait for more evidence?

- Exact `Inspection_Record -> Action_Record` cardinality and whether one action may aggregate multiple inspections/findings.
- Minimum `Action_Record` fields and boundaries among recommendation, work order, execution record, and maintenance history.
- Canonical status vocabulary, allowed transitions, immutable-event ownership, rejection/rework semantics, and one-current-state projection.
- Role/permission matrix for inspector, reviewer, proposer, approver, assignee and verifier, including separation of duties and override rationale.
- Formal `Verification_Record`, acceptance criteria, required before/after evidence, independent-verifier rule, and closure/reopen guard.
- Definition of round-trip parity: identifier equality, set equality, semantic equivalence, permitted loss, version context, and stale-link handling.
- Cross-version identity persistence and replacement/retirement behavior after CMMS updates or IFC revisions.

Until Round 3 resolves these points, the verdict for locking exact fields and rules is **Evidence insufficient**. G2 may continue specification development, but G3 should remain unopened and no schema/workflow should be described as accepted or validated.

## 8. Verification boundaries and disclosure

- This was a targeted novelty-boundary screen, not a PRISMA-complete systematic review. Search saturation is reported only for the executed query families.
- DOI, title, author, year, and venue metadata were checked against publisher pages, Crossref, or OpenAlex. Detailed implementation claims were used only when full text, reproducibility artifacts, or existing verified Zotero notes supported them.
- Closed or metadata-only discovery hits were not used to infer missing fields or capabilities. They require full-text review before entering a field-level comparison.
- AI-assisted research tools were used for discovery, corpus reconciliation, evidence extraction, and consistency checking. The report preserves source identifiers and bounded language so each substantive comparison can be audited against the cited paper.
- No Zotero record, collection, tag, note, or attachment was modified during this screening.
