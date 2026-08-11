# Gate 2-3 Repository Evidence Synthesis

**Date:** 2026-08-02  
**Evidence boundary:** local repository only; no Zotero MCP, web search, or outside knowledge.  
**Quartile control:** **Journal quartile is unverified.** No reviewed repository file verifies current Q1/Q2 status.

## 1. Executive conclusion

### Overall judgement

The current Gate 2-3 direction has a defensible academic basis for four separate building blocks: (i) BIM/IFC objects as component identity and record-retrieval anchors; (ii) sensor/inspection linkage through IFC GlobalIds; (iii) provenance fields covering actor, operation, version and time; and (iv) competency-question and human-governance methods. The strongest reviewed precedent is Antunes et al. (2024), which already links sensors/observations, inspections and IFC GlobalIds through 13 competency questions and pilot queries. Therefore, **sensor-BIM integration, BIM-linked inspection, and competency questions are not individually novel** [F04:62-75; F05:19-23; F06:12].

The defensible candidate contribution is narrower: a context-preserving and formally constrained chain from condition evidence and confidence metadata to a BIM component, inspection record and accountable action record, tested in both directions and against invalid data. Within the reviewed evidence base, no source validates that complete chain; however, this is a corpus-bounded finding, not proof that no such study exists globally [F05:45-49; F07:2-10].

Gate 2 is **academically supported but operationally open**. Its identifier schema, CEI structure, record schemas, pre-registered SCQ/VCQ/RCQ and acceptance criteria are all still `OPEN` [F03:48-58]. Gate 3 is **not evidenced as implemented**: the end-to-end demonstration, round trip, orphan-ID, duplicate-ID, missing-CEI and invalid-data tests are all `OPEN` [F03:59-68]. The repository's formal current gate is G1, not G2 or G3 [F02:149-163; F03:5-6].

The local IFC asset is technically promising: it is IFC4X3_ADD2, carries ContentGUID/VersionGUID metadata, and contains a component GlobalId linked to an `Asset_ID` property [F15:3-5,236-266,295-306,1573662-1573666]. This demonstrates an available identity anchor, not a validated Digital Twin or a completed sensor-to-decision chain.

Cross-scale linkage between the 1:10 frame and the 1:1 Cam Ranh model is currently a **project design rule**, not an academically validated result. The only explicit mapping found defines `COMPONENT_CORRESPONDENCE` and forbids quantitative transfer [F11:76-93]. No populated `Test Component -> Prototype Component -> BIM_GUID` register, mapping-confidence model, version-stability test or human approval record was found. **Evidence is currently insufficient.**

The repository contains metadata-level literature on Digital Twin predictive maintenance, including synthetic structural decision models, systematic reviews and building-services cases [F19:5,184,188-205]. Yet predictive maintenance, RUL and autonomous maintenance are explicitly outside the locked thesis scope [F02:62-65,182-187; F11:22-30]. These sources support broader context only; they do not support a Gate 2-3 predictive-maintenance claim.

### Strength classification

| Research direction | Assessment | Basis |
|---|---|---|
| BIM/IFC information readiness and component identity | **Strong for need and feasibility; partial for project readiness** | 93-study review identifies time-series/toolchain barriers; direct IFC contains GlobalId, version metadata and `Asset_ID` [F06:10; F15:3-5,236-266]. |
| Sensor/inspection-to-BIM integration | **Strong precedent; not novel alone** | Antunes et al. and Kim et al. provide IFC/object-linked inspection or FM-record retrieval [F06:9,12]. |
| Provenance and version-aware records | **Methodologically supported; project implementation absent** | Celik et al. supports actor/operation/version/timestamp history; no project model-version register or stability audit was found [F06:11; F02:111-116]. |
| Complete evidence-to-action identifier chain | **Promising candidate gap; not yet demonstrated** | Partial precedents exist, but all G3 tests are open [F05:19-35,45-49; F03:59-68]. |
| 1:10 test component to 1:1 prototype/BIM correspondence | **Weak** | Explicit project semantics exist, but no academic validation or populated mapping was found [F11:76-93,141-163]. |
| Condition evidence to inspection and maintenance action | **Partial** | Governance and asset-condition-job traceability are supported; the four-level workflow remains unvalidated [F10:7-17,37-41]. |
| Predictive maintenance and RUL | **Outside current scope and insufficient for Gate 2-3** | Metadata literature exists, while current governance prohibits the claim [F19:194,201; F02:65,187]. |

## 2. Files reviewed

### Search and selection method

The repository root was recursively searched across `.md`, `.txt`, `.csv` and `.json` files for BIM/IFC, sensor linkage, component identity, scale transfer, provenance, model version, confidence, human review, inspection, maintenance, SHM, Digital Twin and predictive-maintenance terms. Relevant `.ifc` content was then inspected because it supplies direct project-readiness evidence. Current source-of-truth files were preferred over discovery material, backups and archives according to the repository hierarchy [F01:7-18].

Evidence was graded as follows:

- **Source evidence:** a paper-level extraction, PDF-specific page record, bibliographic export, or direct project artifact.
- **Project synthesis/design:** a current charter, gate, addendum or paper plan. It can define scope/status but cannot prove an academic finding.
- **OpenCode inference:** a conclusion obtained by comparing source evidence and project status. It is labelled explicitly.
- Metadata/abstract-only records are not treated as deep-read findings.
- Duplicate records are counted once; known attachment and metadata conflicts remain flagged [F20:3-26].

### File register

| Code | Repo-relative file | Use in this report |
|---|---|---|
| F01 | `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/00_GOVERNANCE/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` | Authority and archive exclusion rules. |
| F02 | `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/00_GOVERNANCE/MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md` | Locked scope, claims, gates and CEI definition. |
| F03 | `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/00_GOVERNANCE/EVIDENCE_GATES_v2.1.md` | Formal G2/G3 acceptance status. |
| F04 | `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/02_EVIDENCE_BASE/CURRENT/LIVING_EVIDENCE_BASE_v2.1_TRACEABILITY_CORE.md` | Current evidence source of truth. |
| F05 | `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/02_EVIDENCE_BASE/RQ2_GATES2_3/04_RQ2_TRACEABILITY_EVIDENCE_ADDENDUM_v1.2_20260718.md` | RQ2 claim register and competitor boundary. |
| F06 | `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/02_EVIDENCE_BASE/ZOTERO_AUDIT/02_NEW_DEEP_READ_EVIDENCE_MATRIX_20260718.csv` | Paper-level methods, findings, limitations, pages and DOI data. |
| F07 | `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/02_EVIDENCE_BASE/RQ2_GATES2_3/07_CLOSEST_COMPETITOR_MATRIX_PAPER2_20260718.csv` | Feature comparison across closest competitors. |
| F08 | `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/02_EVIDENCE_BASE/ZOTERO_AUDIT/10_ZOTERO_WRITEBACK_QUEUE_20260718.md` | Human-readable deep-read claims and PDF page ranges. |
| F09 | `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/02_EVIDENCE_BASE/RQ3_GATE4/05_RQ3_FIELD_FEASIBILITY_EVIDENCE_ADDENDUM_v1.0_20260718.md` | Field baseline, sensor qualification and inspection boundary. |
| F10 | `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/02_EVIDENCE_BASE/WP4_GATE5/06_WP4_DECISION_SUPPORT_EVIDENCE_ADDENDUM_v1.0_20260718.md` | Human-reviewed decision-support evidence. |
| F11 | `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/00_README_START_HERE_v2.2_UPDATED_20260720.md` | Operational cross-scale design; lower authority than F02. |
| F12 | `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/03_PAPERS/PAPER_2/PAPER2_DIRECTION_AND_GATE_v2.1_20260719.md` | Current Paper 2 plan, not source evidence. |
| F13 | `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/03_PAPERS/PAPER_3/PAPER3_FIELD_FEASIBILITY_DIRECTION_v2.1_20260719.md` | Field paper plan and unresolved requirements. |
| F14 | `03_RESEARCH_ASSETS/BIM_MODELS/IFC_mapping.txt` | Export rule mapping `Asset_ID` to IFC identity data. |
| F15 | `03_RESEARCH_ASSETS/BIM_MODELS/DT10_MODEL 13.03.26.ifc` | Direct IFC version, GUID and component-property evidence. |
| F16 | `01_KNOWLEDGE/BIM_AIM_early_phase/26.03.09_DT10_K25L80 Asset Register.csv` | Early asset categories and monitoring flags. |
| F17 | `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/05_DATA_CODE_AND_EXPERIMENTS/CANONICAL_THREE_CAMPAIGN_DATASET/07_DATA_DICTIONARY.md` | Meaning of existing `Mapping_Confidence`; sensor-block mapping only. |
| F18 | `05_MASTER_INDEX_CONTROL/Literature_Review_Master_Index.md` | Reading status and metadata/deep-read boundaries. |
| F19 | `02_PROJECTS/PAPER_01/planning/Paper 1_Manu Script.csv` | Bibliographic metadata and abstracts; used only at metadata level where not deep-read elsewhere. |
| F20 | `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/02_EVIDENCE_BASE/ZOTERO_AUDIT/08_DUPLICATE_AND_METADATA_CORRECTION_LOG_20260718.csv` | Duplicate, wrong-PDF and metadata controls. |
| F21 | `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/02_EVIDENCE_BASE/CURRENT/EVIDENCE_MIGRATION_REPORT_v2.1.md` | Migration lineage and unresolved evidence integrity. |

Backups, superseded files, prompts and Perplexity outputs were searched for conflict detection but excluded as citable evidence under F01:16-18. F21:9 incorrectly says the current RQ2 addendum contains C2-01 through C2-11, whereas F05:8-17 contains C2-12 through C2-17. This documentation inconsistency reduces confidence in inherited, unnamed C2-01 through C2-11 details.

## 3. Evidence matrix

| Source/file and citation | Claim supported | Method and object | Main result | Limitation | Gate relevance | Exact location |
|---|---|---|---|---|---|---|
| F06, `GUEJBZBZ`, Du et al. (2024), *BIM and IFC Data Readiness for AI Integration in the Construction Industry* | BIM/IFC time-series and extraction readiness remain barriers. | PRISMA-guided review; 93 studies. | Supports an external time-series architecture linked to BIM/IFC. | Background review; no persistent component-ID model or chain validation. | G2 information readiness. | F06:10; F08:80-84; PDF pp. 11-22 recorded there. |
| F06, `VI5QMSAE`, Kim et al. (2018) | IFC objects can anchor historical FM work-record retrieval. | Ontology/SPARQL case using 590 maintenance records. | Demonstrates object-to-work-record queries. | No sensors, demonstrated GlobalId, SHACL, cardinality or status history. | G2 record-linkage precedent. | F06:9; F08:74-78; PDF pp. 9-13. |
| F06, `XUN8EX6X`, Antunes et al. (2024) | CQ-driven ontology can connect inspection results to IFC GlobalIds. | CoDEC/SSN/ifcOWL; 13 CQs; SPARQL; OOPS; three pilots. | Links sensors/observations and element-level inspection results to IFC identifiers. | Mapping partly manual; SHACL not executed; no complete raw-evidence-to-action chain or action history. | Closest G2/G3 competitor. | F06:12; F08:92-96; PDF pp. 4-10. |
| F06, `EMTIHHX4`, Celik et al. (repo year conflict: 2022/2023) | Provenance should preserve actor, operation, version, timestamp and identity. | Bridge scenario and prototype BIM-object transaction network. | Reconstructs change history from transaction events. | Design/construction provenance, not inspection evidence; blockchain is not shown necessary. | G2 schema fields; G3 provenance tests. | F06:11; F08:86-90; PDF pp. 5-14. |
| F06, `LSYSC59G`, Keet and Khan (year unverified) | Scoping, validation and relationship CQs have distinct purposes. | Formal CQ taxonomy with SewerNet and ROCQS examples. | Supports labelled, executable and expected-answer CQs. | Conceptual; limited user evaluation; parent metadata incomplete. | G2 CQ pre-registration. | F06:13; F08:98-102; PDF pp. 3-12. |
| F19, Heaton and Parlikad (2020), `L52SHNEH` | BIM-based AIM can organize multi-model asset information for DT adoption. | West Cambridge campus case; BIM object model and asset classification. | Demonstrates a federated asset-information approach. | No Sensor_ID, BIM_GUID, SHM inspection record or evidence-to-action chain. | G2 asset-information context. | F19:2; reading boundary F18:66. |
| F15 plus F14 | The project has a usable IFC component identity anchor. | Direct IFC4X3_ADD2 inspection and export mapping. | One `IfcColumn` GlobalId is linked to `Asset_ID=DT10-K25L80-ST-COL-B2-01`; ContentGUID and VersionGUID are present. | One snapshot is not a GUID-stability/version-history audit; no sensor mapping. | Project readiness for G2/G3, not academic novelty. | F15:3-5,236-266,295-306,1573662-1573666; F14:1-4. |
| F16 | An early asset taxonomy exists. | Asset register with COL, BEAM, RAF, GIR, BR, BASE, CONN. | Establishes basic asset classes and partial monitoring/status fields. | No component GUID, Sensor_ID, evidence, confidence, version or approval fields. | Input to G2 schema design only. | F16:1-8. |
| F06, `YGZ32C8M`, Johannes et al. (2021) | Smart maintenance benefits from asset-condition-job traceability and human governance. | Four embedded cases, 48 interviews, records/observations and seven-expert consultation. | Supports roles, interpretation and linkage among assets, condition and jobs. | University CFM context; no four-level escalation or steel-building case. | G2 accountability and G3/G5 human review. | F06:25; F08:138-142; PDF pp. 3-12. |
| F06, `ESTEYBHA` (2021) | Transparent DT assessment should expose purpose, roles, communication, data quality, provenance, security and integration. | 27 rubrics, 40 expert responses and two cases. | Supplies unweighted trust/governance criteria. | DT maturity is not a condition-action workflow; highest maturity includes autonomy outside scope. | G2 metadata design and G5 review criteria. | F06:27; F08:144-148; PDF pp. 4-13. |
| F06, `9823WXJZ` (2006) | Continuous vibration monitoring is feasible in a real steel-frame building. | Occupied 17-storey steel building; continuous 72-channel monitoring. | Captures operational, wind and event-dependent baseline variation. | No component/BIM/inspection chain, coastal industrial context or confirmed damage. | Adjacent feasibility evidence, mainly G4; boundary for G3 claims. | F06:23; F08:130-134; source pp. 715-735. |
| F06, `TRZY4P6X`, `GE3XSAYV`, `D3TGCKXW` | Field baselines need environmental and missing-data controls. | Three-year bridge monitoring; one-year hourly GNSS; secondary long-term bridge datasets. | Temperature, freezing, wind and missingness can alter apparent condition features. | Bridge/secondary data; no transferable correction or BIM-inspection provenance. | Boundary condition for later field validation, not G3 closure. | F06:18-20,22; F09:10-16,20-53. |
| F06, `LZPF7ILT` (2023) | Low-cost nodes require application-specific qualification. | Side-by-side low/high-grade tests on a full-scale laboratory slab. | Controlled impulse performance did not guarantee ambient-vibration performance. | Laboratory-only, short sessions, no BIM chain. | Supports sensor-data quality fields, not traceability novelty. | F06:21; F08:118-122; PDF pp. 2-15. |
| F11, project cross-scale design | Lab and 1:1 BIM contexts can be represented as non-quantitative component correspondence. | Governance rule: `LABORATORY_1_10` to `CAMRANH_REVIT_1_1`. | Explicitly prevents quantitative or field-condition transfer. | Project synthesis only; no populated table, experiment or external validation. | Candidate G2 context rule and G3 test case. | F11:76-93,141-163. |
| F17, project sensor mapping | Sensor-block assignment uncertainty is already quantified in the dataset. | Static-gravity fingerprints, centroid distances and Hungarian assignment; 576 mappings. | All mappings in that pass were labelled high confidence. | This `Mapping_Confidence` concerns raw sensor-block identity, not sensor-to-BIM or test-to-prototype mapping. | Reusable concept only; cannot support G2 BIM-mapping confidence. | F17:12-20. |
| F19, Torzoni et al. (2024), `ZCPMLA5V` | DT can model repeated observations-to-decisions for maintenance planning. | Probabilistic graphical model/dynamic Bayesian network; synthetic cantilever and railway bridge cases. | Metadata abstract reports dynamic decision-making in two synthetic cases. | Metadata/abstract only in this review; no BIM/IFC traceability and no physical validation. | Broad Gate 3/PdM context only. | F19:5; status boundary F18:68. |
| F19, Yang et al. (2025), `QMPFIBQX` | BIM-DT-IoT can support real-time maintenance monitoring. | LOD 400 noise-barrier tunnel model; vibration, tilt, light, air-quality and water sensors; short demonstration. | Abstract reports stable transmission and anomaly detection; it says predictive maintenance is future groundwork. | Metadata/abstract only; short period; partial data gaps; no provenance/action-chain evidence. | Adjacent sensor-BIM and maintenance context. | F19:184. |
| F19, Van Dinter et al. (2022), `RY36NXSH` | DT-based predictive maintenance is an established research field with recurring implementation challenges. | Systematic review of 42 primary studies. | Abstract identifies computational burden, data variety and model/asset/component complexity. | Software-engineering scope; metadata/abstract only here; not proof of the thesis chain. | Broader context; predictive maintenance remains outside current G2/G3 scope. | F19:194; scope prohibition F02:62-65. |
| F19, Bouabdallaoui et al. (2021), `CD43LGST` | Building-services predictive maintenance can connect IoT/BAS data to failure prediction. | Sport-facility HVAC case; five-step ML framework. | Abstract reports potential to predict failures. | Data availability and feedback collection barriers; building services, not structural component traceability. | Outside locked scope; context only. | F19:201; scope prohibition F02:182-187. |

## 4. Evidence supporting Gate 2

### Claim G2-1: BIM/IFC information readiness is a real and relevant problem

**Status:** Strongly supported as a general problem; partially supported for the project.

**Claim ->** Operational evidence requires governed links between external time-series data and stable BIM/IFC component identities.  
**Evidence ->** Du et al.'s 93-study review records time-series and toolchain barriers [F06:10]. The project IFC exposes IFC4X3 schema metadata, model GUIDs, component GlobalId and `Asset_ID` [F15:3-5,236-266].  
**Limitation ->** The review does not validate the proposed identifier chain; one IFC snapshot does not show stability across versions.  
**Next action ->** Create an IFC readiness audit covering required fields, GUID persistence across at least two controlled exports, missing/duplicate IDs, external-store contracts and change ownership. This is an OpenCode recommendation derived from F03:52-57 and F15.

### Claim G2-2: Component-level identity can anchor operational and inspection records

**Status:** Strongly supported, but not novel alone.

**Claim ->** IFC/object identifiers can anchor retrieval of work and inspection records.  
**Evidence ->** Kim et al. demonstrate object-linked retrieval over 590 FM records [F06:9]; Antunes et al. connect inspection results to IFC GlobalIds [F06:12].  
**Limitation ->** Neither source validates the full raw sensor -> condition evidence -> accountable action chain [F05:19-23].  
**Next action ->** Position component identity as prior art and evaluate the proposed contribution on constrained forward/reverse queries and failure detection, not on visualization or linkage alone.

### Claim G2-3: Provenance, model version and accountability belong in the schema

**Status:** Partially supported.

**Claim ->** Evidence and actions should retain actor/source, operation, timestamp, version and approval context.  
**Evidence ->** Celik et al. reconstruct object transaction histories [F06:11]; Johannes et al. support governance, responsibilities and human interpretation [F06:25].  
**Limitation ->** Celik et al. concern design-stage transactions; Johannes et al. do not validate the proposed action vocabulary. The project has no located model-version register, cross-version GUID test or completed approver record.  
**Next action ->** Put version, source hash, transformation, creator, reviewer, approval state and timestamp into the minimum Condition_Evidence, Inspection_Record and Action_Record schemas; validate their presence and referential integrity.

### Claim G2-4: SCQ/VCQ/RCQ and explicit acceptance criteria are academically justified

**Status:** Supported as method; not completed in the project.

**Claim ->** Distinct competency-question types and executable expected answers improve schema evaluation.  
**Evidence ->** Keet and Khan provide the CQ taxonomy [F06:13]; Antunes et al. provide a domain precedent with 13 CQs [F06:12].  
**Limitation ->** An informal list is not validation, and every G2 CQ/acceptance artifact remains open [F03:55-57].  
**Next action ->** Pre-register each question, query, fixture, expected answer, failure condition and pass criterion before implementation, as already required by F05:25-35.

### Claim G2-5: Cross-scale correspondence can preserve context without transferring physical conclusions

**Status:** Weak; project design only.

**Claim ->** A 1:10 test component may be associated with a 1:1 BIM component while explicitly prohibiting quantitative transfer.  
**Evidence ->** F11 defines `Evidence_Context`, source/reference asset IDs, `COMPONENT_CORRESPONDENCE` and `Quantitative_Transfer_Allowed=FALSE` [F11:76-93].  
**Limitation ->** No reviewed academic source or populated register validates `Test Component -> Prototype Component -> BIM_GUID`; the terminology “Prototype Component” itself is not established in the current evidence matrix. **Evidence is currently insufficient.**  
**Next action ->** Treat this as a research hypothesis. Pre-register correspondence criteria, version, rationale, confidence, reviewer and rejected mappings; then test inter-reviewer agreement and change resilience.

### Claim G2-6: Mapping confidence and human verification can strengthen traceability

**Status:** Conceptually plausible but unsupported for BIM mapping.

**Claim ->** Mapping records should expose confidence and human verification rather than silently asserting exact correspondence.  
**Evidence ->** The dataset already calculates confidence for physical sensor-block identity [F17:12-20], and decision-support evidence supports human review [F10:13-17,26-35].  
**Limitation ->** These are different problems: F17 does not quantify sensor-to-BIM or cross-scale correspondence, and no BIM mapping verification record was found.  
**Next action ->** Define confidence as evidence-backed fields, not a universal score: mapping method, candidate set, distance/rationale, confidence class, reviewer, disposition, timestamp and model version.

## 5. Evidence supporting Gate 3

### Claim G3-1: An end-to-end traceability demonstration is publishable only if it tests integrity, not merely visualization

**Status:** Strong methodological rationale; no implementation evidence.

**Claim ->** The demonstrator should prove forward/reverse traceability and reject malformed relationships.  
**Evidence ->** Antunes et al. establish the closest query-based precedent but do not execute SHACL [F06:12]. The current addendum identifies round-trip, referential integrity, provenance and status history as required test families [F05:25-35].  
**Limitation ->** All six formal G3 items remain open [F03:59-68]; the direct SHACL source `3II2WKLN` has abstract/HTML only [F06:17].  
**Next action ->** Implement the smallest reproducible case with valid fixtures plus orphan, duplicate, missing-CEI and invalid-cardinality fixtures. Retain query outputs and test logs.

### Claim G3-2: Condition evidence should trigger inspection rather than become an unverified damage conclusion

**Status:** Supported as a conservative boundary.

**Claim ->** Environmental/contextual uncertainty and missingness require human inspection before field damage conclusions.  
**Evidence ->** Long-term field sources show environmental and missing-data effects [F09:12-16,20-53]; current governance requires anomaly -> inspection, not damage [F02:97-109].  
**Limitation ->** Those sources do not demonstrate the project's condition-evidence-to-record chain.  
**Next action ->** Make the G3 output a traceable inspection recommendation and record, not automated diagnosis or maintenance execution.

### Claim G3-3: Human-reviewed decision support has an academic basis

**Status:** Partially supported.

**Claim ->** Traceable roles, evidence, data quality and professional interpretation are defensible decision-support requirements.  
**Evidence ->** Johannes et al. and the Gemini-principles maturity work support asset-condition-job traceability, governance and explicit rubrics [F06:25,27; F10:11-17].  
**Limitation ->** No reviewed source validates `Normal -> Watch -> Inspect -> Priority`, status-event history or the project's scenario logic [F10:5-7,37-41].  
**Next action ->** Validate pre-specified scenarios with facility managers, preserving reviewer, timestamp, disposition, comments and status transitions [F10:26-35].

### Claim G3-4: Predictive maintenance is not supported as a Gate 3 output

**Status:** Unsupported and out of scope.

**Claim ->** Metadata literature shows that DT-based predictive maintenance exists as a broader field [F19:5,188-205].  
**Evidence ->** Torzoni et al. report synthetic dynamic decision cases; Van Dinter et al. review 42 studies; Bouabdallaoui et al. report an HVAC case [F19:5,194,201].  
**Limitation ->** These are not the locked structural traceability chain, several are metadata/abstract-only in this audit, and the Charter prohibits predictive-maintenance and RUL claims [F02:62-65,182-187].  
**Next action ->** Retain “condition-based inspection support” and “asset-management decision support.” Do not present G3 as predictive maintenance.

## 6. Confirmed research gaps

“Confirmed” below means confirmed **within the reviewed repository evidence**, not universal absence.

| Gap | Confirmation and boundary | Classification |
|---|---|---|
| Complete constrained evidence-to-action chain | Closest competitor has sensors, inspection and IFC GlobalIds but lacks the complete raw/derived evidence, status-history and executed-constraint chain [F06:12; F07:5]. | **Confirmed within reviewed corpus; candidate novelty.** |
| Executed invalid-data and referential-integrity validation | No current reviewed source/project artifact shows executed orphan, duplicate, missing-CEI and SHACL-equivalent tests; G3 remains open [F03:63-68; F05:37-49]. | **Confirmed implementation gap.** |
| Action status-event history | Existing sources have at most partial current status; no full transition history with actor, time, reason and linked inspection was validated [F05:17,32-35; F07:2-6]. | **Confirmed within reviewed corpus; thesis design still unvalidated.** |
| Operational provenance and model-version continuity | Provenance fields have literature support, but the project has only snapshot version metadata and no GUID-stability/change-history test [F06:11; F15:3-5]. | **Confirmed project gap; literature gap only partial.** |
| Test Component -> Prototype Component -> BIM_GUID | Only a project-level `COMPONENT_CORRESPONDENCE` rule was found, with transfer prohibited [F11:76-93]. | **Confirmed project evidence gap; universal literature gap unproven.** |
| Mapping confidence plus human verification | Confidence exists only for raw sensor-block assignment [F17:12-20]; human-review criteria are proposed but no BIM mapping review record was found [F10:26-35]. | **Confirmed project gap.** |
| Information quality/readiness acceptance | Readiness barriers are supported by a 93-study review, but the project lacks a signed-off readiness matrix and cross-version test [F06:10; F03:48-58]. | **Confirmed execution gap.** |
| Condition evidence -> inspection -> accountable action | Partial record/governance precedents exist, but the complete workflow and four-level logic are not validated [F06:9,12,25; F10:5-17]. | **Confirmed within reviewed corpus; strong paper opportunity if demonstrated.** |

## 7. Unsupported or weak claims

| Claim | Assessment | Evidence boundary and next action |
|---|---|---|
| “No prior study implements the full chain.” | **Unsupported universal claim.** | Only say “within the reviewed evidence base” [F05:45-48]. A systematic, reproducible external search would be needed later. |
| “Sensor-to-BIM integration is novel.” | **Contradicted by reviewed precedent.** | Antunes et al. already include sensors/observations and IFC GlobalId traversal [F06:12]. Novelty must rest on context, constraints, integrity tests and accountable records. |
| “The project has completed Test Component -> Prototype -> BIM traceability.” | **Unsupported.** | F11 is a design; no populated correspondence/approval register was located. **Evidence is currently insufficient.** |
| “The 1:10 results transfer quantitatively to the 1:1 asset.” | **Prohibited.** | F11:91-92 and F02:182-187 explicitly forbid quantitative transfer and field-condition claims. |
| “Existing Mapping_Confidence validates BIM correspondence.” | **Incorrect.** | It measures static-gravity sensor-block assignment only [F17:12-20]. |
| “Model versioning is handled.” | **Weak.** | One IFC carries ContentGUID/VersionGUID, but no persistence, diff, lineage or approval audit exists [F15:3-5]. |
| “Human verification is implemented.” | **Unsupported.** | Review fields are specified, not completed [F10:26-35,37-41]. |
| “CEI is a validated scalar/Health Index.” | **Unsupported and prohibited.** | Current evidence supports metadata only; universal scalar evidence is insufficient [F04:174-175; F02:122-135]. |
| “Gate 2 or Gate 3 is closed.” | **False.** | Every G2 and G3 artifact is `OPEN` [F03:48-68]. |
| “The framework performs predictive maintenance/RUL.” | **Outside scope and unsupported.** | F02:62-65,182-187; metadata-level PdM sources do not validate the proposed chain. |
| “The proposed four-level workflow is literature-validated.” | **Unsupported.** | No reviewed source implements an equivalent audited escalation [F10:5-7,37-41]. |
| “Paper targets are Q1/Q2.” | **Unverified.** | Target files explicitly say `verify rank` [F12:3; F13:3]. **Journal quartile is unverified.** |
| “Legal mapping validates technical thresholds.” | **Prohibited and unverified.** | Legal references remain pending and cannot create technical thresholds [F02:139-145]. |

## 8. Proposed Q1/Q2 paper directions

These are feasibility directions, not assertions that the journals or outputs are Q1/Q2. **Journal quartile is unverified.**

### Direction 1: Formally constrained evidence-to-action traceability

**Research question:** Can a context-preserving identifier model provide reproducible forward/reverse traceability from condition evidence and CEI metadata to BIM components, inspection records and accountable actions while detecting invalid relationships?  
**Novelty:** Complete constrained chain, explicit failure fixtures, pre-registered SCQ/VCQ/RCQ and action history; not sensor-BIM linkage itself [F05:19-35,45-49].  
**Existing evidence:** Antunes, Kim, Celik and Keet/Khan cover the principal partial building blocks [F06:9,11-13].  
**Missing evidence:** Approved schemas/CQs, three unavailable priority full texts, implementation, round-trip and invalid-data logs [F03:48-68; F06:14,16-17].  
**Method:** Design-science study; pre-register CQs and acceptance criteria; implement a minimal relational or graph schema; run valid and invalid fixtures; compare feature coverage and queries against CoDEC.  
**Expected contribution:** A reproducible, implementation-agnostic traceability and integrity-validation protocol for construction/asset-management records.  
**Reviewer risk:** “Only systems integration” unless the formal constraints, benchmark, failure tests and generalizable design principles are clear.  
**Journal type:** Construction informatics, BIM/IFC interoperability, asset-information management. Project-listed targets are in F12:3; **Journal quartile is unverified.**

### Direction 2: Cross-scale, context-preserving component correspondence

**Research question:** How can evidence from a 1:10 test component be linked to a 1:1 BIM component without implying unvalidated physical or quantitative transfer?  
**Novelty:** Explicit context, mapping type, non-transfer semantics, model version, confidence and human verification around component correspondence [F11:76-93].  
**Existing evidence:** The project has laboratory context, a 1:1 IFC identity anchor and a proposed correspondence vocabulary [F11:76-93; F15:3-5,236-266].  
**Missing evidence:** Academic precedent specific to test/prototype/BIM mapping; populated mappings; reviewer agreement; model-change robustness. **Evidence is currently insufficient.**  
**Method:** Multiple-case mapping of selected laboratory components to IFC components; independent reviewer mapping; agreement/error analysis; controlled IFC version changes; false-match and ambiguous-match fixtures.  
**Expected contribution:** A non-transfer-safe correspondence protocol that prevents laboratory evidence from being misrepresented as field evidence.  
**Reviewer risk:** High risk of being seen as naming/data engineering unless the study demonstrates ambiguity, error, version drift and reviewer reproducibility.  
**Journal type:** Engineering information management, digital engineering, BIM/asset semantics. **Journal quartile is unverified.**

### Direction 3: IFC information-readiness and GUID-stability audit for evidence integration

**Research question:** Which IFC/component identity, data-quality, version and provenance conditions are necessary before sensor-derived evidence can be linked reliably to asset records?  
**Novelty:** An evidence-oriented readiness test suite tied to actual failure modes, rather than a generic BIM checklist.  
**Existing evidence:** The readiness review identifies time-series/toolchain barriers; the project IFC exposes a testable identity/version baseline [F06:10; F15:3-5,236-266].  
**Missing evidence:** Repeated exports, controlled model edits, expected GUID behavior, duplicate/missing fields, external-store contract and practitioner review.  
**Method:** Audit at least two controlled IFC versions; define required fields; run GUID persistence, missing-ID, duplicate-ID and property-completeness tests; document causes and remediation.  
**Expected contribution:** A reproducible readiness protocol for sensor/condition-evidence integration with IFC assets.  
**Reviewer risk:** May be rejected as a project-specific QA exercise unless tested across multiple exports/models and related to prior readiness literature.  
**Journal type:** BIM interoperability, construction information quality, facility/asset information management. **Journal quartile is unverified.**

### Direction 4: Human-reviewed condition-evidence-to-inspection workflow

**Research question:** Does an explicit evidence, confidence, role and status-history record improve the traceability and reviewability of inspection recommendations under sparse field-damage data?  
**Novelty:** Integration of CEI metadata, action provenance, status transitions and facility-manager scenario review; not automated maintenance optimization [F10:26-41].  
**Existing evidence:** Asset-condition-job traceability, governance and explicit maturity rubrics are supported [F06:25,27].  
**Missing evidence:** Validated four-level definitions, realistic scenarios, facility-manager participants, inter-reviewer consistency and decision-change records.  
**Method:** Pre-specify scenarios and expected information needs; compare baseline records with the proposed traceable records; conduct structured expert/facility-manager review; report agreement, missing information and revisions.  
**Expected contribution:** A transparent, accountable, human-in-the-loop inspection-support protocol for sparse evidence.  
**Reviewer risk:** Small expert sample, subjective endpoints, overlap with Paper 2, and overclaiming maintenance benefit without longitudinal outcomes. Merge with Direction 1 unless a strong independent field/expert dataset is obtained.  
**Journal type:** Asset management, facility management, construction management, inspection/maintenance decision support. **Journal quartile is unverified.**

## 9. Priority evidence still needed

1. Acquire and deep-read `3II2WKLN` (SHACL/ifcOWL), `NUTL57KJ` (IFC inspection/maintenance representation) and `Z4IBWW9Y` (IFC defect/action model). Detailed claims are currently prohibited [F06:14,16-17; F05:37-43].
2. Reconcile the RQ2 claim-register inconsistency: F21:9 refers to C2-01 through C2-11, while the active addendum contains C2-12 through C2-17 [F05:8-17].
3. Lock and approve the G2 identifier, CEI, Inspection_Record and Action_Record schemas, then pre-register SCQ/VCQ/RCQ and per-question acceptance criteria [F03:48-58].
4. Produce a real mapping register containing test component, prototype/reference component, BIM_GUID, model version, mapping method, confidence basis, reviewer and disposition. Current project design is not evidence of execution [F11:76-93].
5. Export at least two controlled IFC versions and test GUID stability, property persistence, duplicates, missing identifiers and traceability after change [F15:3-5; planned audit F02:111-116].
6. Execute G3 with forward/reverse queries and retained orphan-ID, duplicate-ID, missing-CEI and invalid-data fixtures [F03:59-68].
7. Obtain human review records for mappings and decision scenarios, including reviewer, timestamp, disposition, comments and status transition [F10:26-35].
8. Keep predictive maintenance and RUL outside Gate 2-3 unless the Charter is formally changed and direct structural evidence is acquired [F02:62-65,182-187].
9. Verify journal quartiles from an approved ranking source before describing any target or paper as Q1/Q2. Current target files only say `verify rank` [F12:3; F13:3].
10. Reconcile Celik et al.'s 2022/2023 date conflict and complete the parent bibliographic record for Keet and Khan before submission [F04:62-64,81,186; F20:14].

## 10. Verified references found in the repo

Only bibliographic data explicitly present in the repository are listed. Inclusion does not imply Q1/Q2 status. **Journal quartile is unverified for every reference below.**

1. Antunes, António Lorvão, José Barateiro, Vânia Marecos, Jelena Petrović, and Elsa Cardoso. 2024. “Ontology-based BIM-AMS integration in European Highways.” *Intelligent Systems with Applications* 22: 200366. DOI: `10.1016/j.iswa.2024.200366`. Metadata and deep-read basis: F04:62; F06:12; local PDF title page and pp. 4-10 recorded at F08:92-96.
2. Kim, Karam, Hyunjoo Kim, Wooyoung Kim, Changduk Kim, Jaeyo Kim, and Jungho Yu. 2018. “Integration of IFC objects and facility management work information using Semantic Web.” *Automation in Construction* 87: 173-187. DOI: `10.1016/j.autcon.2017.12.019`. Basis: F04:63; F06:9; local PDF pp. 9-13 recorded at F08:74-78.
3. Celik, Yasin, Ioan Petri, and Masoud Barati. “Blockchain supported BIM data provenance for construction projects.” *Computers in Industry*. DOI: `10.1016/j.compind.2022.103768`. The repository conflicts between 2022 and 2023; publication year must be reconciled before submission. Basis: F04:64; F06:11; F20:14.
4. Du et al. 2024. “BIM and IFC Data Readiness for AI Integration in the Construction Industry.” *Buildings* 14(10): 3305. DOI: `10.3390/buildings14103305`. The current audited evidence confirms title/DOI/year but does not provide a complete creator list in the cited current matrix; do not reconstruct it. Basis: F04:65; F06:10; F20:13.
5. Johannes, Koos, Johannes Theodorus Voordijk, Adriaan Marias Adriaanse, and Guillermo Aranda-Mena. 2021. “Identifying Maturity Dimensions for Smart Maintenance Management of Constructed Assets: A Multiple Case Study.” *Journal of Construction Engineering and Management* 147(9): 05021007. DOI: `10.1061/(ASCE)CO.1943-7862.0002112`. Basis: F04:86; F06:25; F20:23.
6. Lee, Dongmin, Sang Hyun Lee, Neda Masoud, M. S. Krishnan, and Victor C. Li. 2021. “Integrated digital twin and blockchain framework to support accountable information sharing in construction projects.” *Automation in Construction* 127: 103688. DOI: `10.1016/j.autcon.2021.103688`. Basis: local PDF title page in `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/02_EVIDENCE_BASE/RQ2_GATES2_3/DEEP_READ_20.07.2026/Lee et al. (2021) - Provenance và accountability.pdf`; this source is locally present but not yet assigned a canonical key in F04.
7. Heaton, James, and Ajith K. Parlikad. 2020. “Asset Information Model to support the adoption of a Digital Twin: West Cambridge case study.” *IFAC-PapersOnLine* 53(3): 366-371. DOI: `10.1016/j.ifacol.2020.11.059`. Basis: F19:2; deep-read status F18:66.
8. Torzoni, Matteo, Marco Tezzele, Stefano Mariani, Andrea Manzoni, and Karen E. Willcox. 2024. “A digital twin framework for civil engineering structures.” *Computer Methods in Applied Mechanics and Engineering* 418: 116584. DOI: `10.1016/j.cma.2023.116584`. Basis: F19:5; metadata-screened/background status F18:68.
9. Armijo, Alberto, and Diego Zamora-Sánchez. 2024. “Integration of Railway Bridge Structural Health Monitoring into the Internet of Things with a Digital Twin: A Case Study.” *Sensors* 24(7): 2115. DOI: `10.3390/s24072115`. Basis: F19:6; deep-read status F18:69.
10. Yang, Seung-Won, Yuki Lee, and Sung-Ah Kim. 2025. “Design and Validation of a Real-Time Maintenance Monitoring System Using BIM and Digital Twin Integration.” *Buildings* 15(8): 1312. DOI: `10.3390/buildings15081312`. Basis: metadata/abstract F19:184; no deep-read claim is made here.
11. Van Dinter, Raymon, Bedir Tekinerdogan, and Cagatay Catal. 2022. “Predictive maintenance using digital twins: A systematic literature review.” *Information and Software Technology* 151: 107008. DOI: `10.1016/j.infsof.2022.107008`. Basis: metadata/abstract F19:194.
12. Bouabdallaoui, Yassine, Zoubeir Lafhaj, Pascal Yim, Laure Ducoulombier, and Belkacem Bennadji. 2021. “Predictive Maintenance in Building Facilities: A Machine Learning-Based Approach.” *Sensors* 21(4): 1044. DOI: `10.3390/s21041044`. Basis: metadata/abstract F19:201.
13. “Enhancement and validation of ifcOWL ontology based on SHACL.” 2024. DOI: `10.1016/j.autcon.2024.105293`. Full creator data and full text are not established in the current evidence matrix. **Evidence is currently insufficient** for substantive claims. Basis: F06:17.
14. Bellon et al. 2025. “IFC framework for inspection and maintenance representation in facility management.” DOI: `10.1016/j.autcon.2025.106157`. Full text unavailable. **Evidence is currently insufficient** for substantive claims. Basis: F06:14.
15. Xu et al. “A Parameter-Driven Method for Modeling Bridge Defects through IFC.” DOI: `10.1061/(ASCE)CP.1943-5487.0001026`. Abstract only; year needs final bibliographic verification in the active evidence base. **Evidence is currently insufficient** for detailed claims. Basis: F06:16; duplicate control F20:3,17.

### Final completion statement

The strongest support is for BIM/IFC component identity, object-linked records, provenance requirements, competency-question evaluation and human-governed inspection support. The strongest corpus-bounded gap is the absence of a demonstrated, constrained and failure-tested evidence-to-action chain. Cross-scale test-to-prototype mapping, BIM mapping confidence, model-version continuity, completed human verification, predictive maintenance and G2/G3 closure remain insufficiently evidenced. The four paper directions above are feasible only in the stated order of evidence acquisition and validation; Direction 1 is the clearest current priority.
