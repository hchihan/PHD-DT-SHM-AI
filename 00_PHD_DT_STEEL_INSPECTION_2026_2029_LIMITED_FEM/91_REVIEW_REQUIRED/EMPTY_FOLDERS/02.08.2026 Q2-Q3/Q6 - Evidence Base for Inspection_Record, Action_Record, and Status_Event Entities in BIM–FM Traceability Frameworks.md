## Overview

Literature across BIM–bridge inspection, IFC schema extensions, CMMS/work-order models, and provenance/digital-twin research provides strong support for inspection-entity and work-order-entity design, moderate support for status/workflow modeling, and only partial, indirect support for a four-level action-priority taxonomy (Normal/Watch/Inspect/Priority Inspection) and for a fully explicit Status_Event log with actor/timestamp/reason/before-after state. No single reviewed study integrates all three proposed entities (Inspection_Record, Action_Record, Status_Event) into one formal, IFC-linked traceability schema — this integration is the thesis's original contribution.

## Comparative Table of Reviewed Studies

| Study | Inspection entity | Action or work-order entity | Action priority/level | Workflow status | Status history | Actor/time/reason | Evidence linkage | Limitation |
|---|---|---|---|---|---|---|---|---|
| Artus & Koch (2022), IFC-based defect modeling in bridge BIM (Xu 2021 thesis)[^1] | IfcSurfaceFeature/IfcVoidingFeature defect entity with geometry, location, grouping via IfcGroup; IfcTask represents inspection activity | Maintenance decision grouping via IfcGroup, but no dedicated work-order entity | Not modeled | Not modeled | Not modeled | Inspection task has date/agent implicitly via IfcTask, not detailed | Defects geometrically linked to IFC host elements | No status/action lifecycle; single-snapshot defect model |
| Ren, Ding & Li (2019), bridge maintenance ontology[^2] | Ontological classes for condition/defect | Maintenance action classes in knowledgebase | Some severity concepts | Not detailed | Not detailed | Not detailed | Semantic (ontology-level) linkage, not IFC geometry | Knowledgebase, not implemented schema with IDs |
| Lee et al. (2020), extended IFC + bridge inspection ontology (ifcOWL/RDF)[^3] | Bridge inspection ontology mapped to AASHTO element taxonomy; four condition grades; SPARQL-queryable inspection instances | Five "feasible actions" concept class from AASHTO taxonomy | Yes — feasible-action categories tied to condition grade | Not modeled | Not modeled | Not detailed | Direct RDF/ifcOWL linkage of defect data to IFC bridge elements | Actions are categorical labels, not full work-order records; no lifecycle status |
| Zhou et al. (2022), parameter-driven IFC defect modeling, J. Computing in Civil Eng.[^4] | Defect geometry, spatial placement parametrically modeled | Interrelationships to "maintenance actions" represented as IFC relationships | Not a level scale; case-based decision only | Not modeled | Not modeled | Not detailed | Direct IFC entity-to-entity relationship (defect-cause-action) | Validated on one bridge; scalability of decision logic unproven |
| Cardiff ORCA (2025), IFC-linked defect schedule for DT[^5] | Defect schedule keyed to ComponentID (IFC GlobalId); RTK-geolocated defect capture | Not explicit — defects feed decision but no formal work order | Not modeled | Not modeled | Not modeled | Not detailed | ComponentID traceability across systems via GlobalId | Prototype; database–IFC link only, no action/status layer |
| Artus, Koch & Borrmann (2018), TUM RC bridge defect information model, J. Computing in Civil Eng., DOI 10.1061/(ASCE)CP.1943-5487.0000744[^6] | Hierarchical defect information objects mapped to new IFC entities (IfcMeasuredRegion, IfcDegradation) | Not modeled as work order | Not modeled | Not modeled | Not modeled | Not detailed | Direct mapping of defect objects to bridge IFC elements | Proof-of-concept; no lifecycle/status tracking |
| TUM mediatum (2023), SIB-Bauwerke to Linked Data for digital twins[^7] | Object-oriented inspection documentation structure, linked at object level | Not modeled | Not modeled | Not modeled | Not modeled | Not detailed | Automated Linked Data transformation enabling IFC-element-level linking | Focused on data conversion; no action/workflow entities |
| Bahreini (Concordia PhD, 2022), OCSD ontology[^8] | Ontology covering inspection, diagnosis, and 3R (repair/rehab/replace) concepts and defect concepts | 3R concepts act as action categories | Implicit severity/diagnosis concepts, not a 4-level scale | Not modeled | Not modeled | Not detailed | Ontology-level semantic linkage | Conceptual ontology; not implemented as records with IDs/status |
| Hammad et al. (2018), unified ontology for lifecycle inspection & repair information models (IRIM)[^9] | Explicit inspection process fields: date, inspector name/ID/qualifications, method/tool; defect fields: host/impacted element, type, detection date, severity, causes | 3R (repair/rehab/replace) process modeling with host/impacted elements and post-repair model changes | Severity and cause fields feed decision, no fixed 4-level scale | Not modeled | Not modeled | **Yes** — inspector identity and inspection date explicitly required | Conceptual mapping to IFC entities (IfcTask, IfcDate, IfcBuildingElementProxy) | Ontology framework only; not validated with full status/audit trail |
| Sacks et al. (2018) SeeBridge MVD, Automation in Construction (Pure Hud)[^10] | ElementDefect as IfcSurfaceFeature with detailed geometric/descriptive attributes per AASHTO/State manuals | Not modeled as discrete work order, but MVD supports process entities (IfcTask, IfcTaskTime) | Not modeled as levels | Not modeled | Not modeled | Process attributes via IfcTaskTime possible | Direct IFC MVD binding of defect to bridge element type | No action-priority or status-history entities defined |
| Nature Sci. Rep. (2023), BIM-based bridge maintenance system (BMS)[^11] | Defect model library (damage/corrosion/deficiency/distortion) linked to BIM components via IFD-encoded GUIDs | Defect database drives maintenance visualization, no discrete work-order ID scheme shown | Not modeled | Not modeled | Not modeled | GUID/IFD-based linkage of defect records to BIM model elements | Visualization/informatization focus; no workflow or approval logic |
| Chen et al. (2018), BIM-based automatic MWO scheduling framework[^12] | Failure component identification from BIM/FM data | Maintenance Work Order (MWO) entity with IFC extension of maintenance tasks, integrated with CMMS/FMS via COBie | Not modeled as levels — uses failure/priority in path planning only | Not modeled explicitly as states | Not modeled | Not detailed | Bidirectional IFC/COBie data mapping between BIM and CMMS work orders | No explicit approval/closure workflow or audit trail entity |
| buildingSMART IFC4.3, Pset_ProjectOrderMaintenanceWorkOrder[^13] | N/A | MaintenanceWorkOrder property set: WorkTypeRequested, MaintenanceType enum (ConditionBased, Corrective, PlannedCorrective, Scheduled), ScheduledFrequency | MaintenanceType is categorical, not an ordinal 4-level scale | Not defined in this Pset | Not defined | Not defined | Formal IFC standard property linkage to IfcTask/IfcProjectOrder | Standard defines properties, not lifecycle states or audit entities |
| buildingSMART IFC4.3, IfcTask entity[^14][^15] | N/A | IfcTask: identifiable unit of work, milestone flag, work method | IfcTask.Priority: IfcInteger, ordinal but undefined categories ("determined by local usage") | IfcTask.Status: IfcLabel, free text (examples: "Not Yet Started," "Started," "Completed") | Not defined — no history entity, single current-status attribute only | Not defined | IfcRelAssignsToControl links IfcProjectOrder/MaintenanceWorkOrder to IfcTask | Status is a mutable label with no versioned history; Priority is unstructured integer |
| Maryland IAC/school CMMS Work-Order Template[^16] | N/A | WOID (unique work order ID), Title/Description, Source Asset/Equipment | Priority field: High/Medium/Low/Emergency (categorical) | Status field: New Request, In Progress, Assigned, Deferred, Completed, Closed, Awaiting Approval, etc. | Not modeled as separate entity — status is a single mutable field | Request Date, Actual Completion Date, Action Taken narrative; no explicit actor ID field | Source Asset/Equipment Item # links WO to physical asset | Industry template; not tied to IFC model or formal audit-event entity |
| FactVerse CMMS/EAM data model[^17] | N/A | Work-order header: WO ID, provider ID, status, priority, requester, owner, assignee | Priority/severity fields present, categorical | common_status (normalized) + source_status (retained original) — dual-status design | Lifecycle timestamps entity: created, approved, assigned, started, completed, closed, canceled, reopened, last updated — explicit multi-stage timestamp log | Requester, owner, assignee fields present; reason captured via "resolution note" / "root cause" | Asset reference field links WO to asset/equipment/location | Industry documentation, not peer-reviewed; no BIM/IFC-native linkage shown |
| Salesforce WorkOrder object model[^18] | N/A | WorkOrder with 76 fields incl. RootWorkOrderId, ParentWorkOrderId | Priority (picklist) | Status (picklist) + StatusCategory | IsClosed/IsStopped booleans; CreatedDate/LastModifiedDate audit fields (standard CRM metadata) | CreatedById, LastModifiedById fields (actor); no explicit "reason" or "previous state" field | AssetId lookup field | Commercial CRM schema, not built for BIM/civil-infrastructure inspection |
| PROV-O / W3C Provenance Ontology, applied to audit trails (MarkLogic 2017)[^19] | N/A | N/A (general data entity) | N/A | Example shows `<workflowStatus>Draft</workflowStatus>` as a versioned field | PROV-O formally separates Entity/Activity/Agent with wasAttributedTo, wasAssociatedWith, wasGeneratedBy relations — closest literature analogue to a Status_Event log | Agent, timestamp (startedAtTime/endedAtTime) explicitly modeled | Not domain-specific to BIM, but structurally matches actor/time/state-change requirement | Generic provenance standard; requires custom mapping to inspection/action domain |
| Blockchain-based DT data provenance (Lu et al., Emerald, SASBE)[^20] | Not detailed | Not detailed | Not detailed | Not detailed | Blockchain-based immutable provenance log for asset information model maintenance | Distributed ledger provides tamper-evident actor/time record | Focus is data provenance/immutability, not specifically inspection/action semantics | Domain applied to predictive maintenance, not directly to inspection ontologies |
| AASHTO/FHWA NBI condition rating scale and Bridge Preservation Guide[^21][^22] | NBI general condition ratings 0–9 per component (deck/superstructure/substructure/culvert) | "Commonly Employed Feasible Actions" mapped per rating band (e.g., Preventive Maintenance, Repairs, Rehabilitation, Replacement) | **Yes — ordinal condition-to-action mapping is well established**, but expressed as a 10-point numeric scale or 4-state condition-state model (Good/Fair/Poor/Severe), not the thesis's specific 4-label Normal/Watch/Inspect/Priority Inspection scheme | Not modeled as a record workflow | Ratings assigned per inspection cycle, historical ratings retained per cycle but not as a discrete event-log entity | Bridge inspector is agent of record per cycle, implicit not schema-explicit | Rating tied to specific structural element/component | Established practice, but priority bands and labels differ from thesis terminology; not a workflow/action-record schema |
| Kentucky DOT / element-level condition state–feasible action matrix[^23] | Element-level condition states (1–4: Good/Fair/Poor/Severe) | Feasible Action Catalog: Do Nothing, Protect, Preserve, Repair, Rehab, Reset, Replace, mapped per condition state | Ordinal condition-state-to-action linkage confirmed at element level | Not modeled | Not modeled | Not detailed | Condition state tied to specific bridge element | Catalog-based decision support, not a digital record/workflow schema |

## Inspection Record Fields Supported by Literature

Studies consistently converge on a core inspection-record field set: unique component/element identifier (often the IFC GlobalId), inspection date, inspector identity/qualifications, inspection method/equipment, defect type, defect location (host element and geometric placement), severity/condition rating, and detected causes. The AASHTO/FHWA National Bridge Inventory (NBI) rating system — a 0–9 numeric scale mapped to categorical feasible-action bands — is the most authoritative and widely cited precedent for linking condition severity to prescribed maintenance actions. Regional agencies also use narrower categorical condition-state models (Good/Fair/Poor/Severe, 4 states), which is structurally closer to — but not identical to — the thesis's proposed Action_Level categories.[^5][^9][^11][^21][^22][^23]

## Linking Inspection Findings to BIM/IFC Components

Multiple independent research groups (TUM, Curtin, Cardiff, Concordia) have demonstrated defect-to-IFC-element linkage using distinct mechanisms: extending IFC with new entities (IfcSurfaceFeature, IfcMeasuredRegion, IfcDegradation) that reference host elements geometrically; mapping ifcOWL/RDF triples so inspection ontology instances resolve via SPARQL to bridge IFC element URIs; and using the IFC GlobalId as a stable ComponentID key to a separate relational defect database, retrievable via JSON export. buildingSMART's native IFC schema also provides IfcRelDefinesByProperties and IfcRelAssociatesDocument as generic mechanisms for attaching condition properties or external inspection documents to any IFC element. This body of evidence directly supports the thesis's intent to bind Inspection_Record entries to specific BIM/IFC components — the mechanism is well established, though no single study formalizes a distinct "Inspection_Record" object with a unique persistent ID separate from the defect/component entity itself.[^1][^3][^6][^24][^10][^5]

## Identifying Maintenance Actions and Work Orders

Work-order identity is well supported outside pure BIM–inspection literature. The buildingSMART IFC4.3 standard defines IfcProjectOrder and its subtype MaintenanceWorkOrder, linked to IfcTask via IfcRelAssignsToControl, with a dedicated Pset_ProjectOrderMaintenanceWorkOrder carrying a MaintenanceType enumeration (ConditionBased, Corrective, PlannedCorrective, Scheduled). Chen et al.'s BIM-based automatic work-order scheduling framework operationalizes this by mapping IFC maintenance-task extensions to CMMS/FM system work orders via COBie, giving each MWO a scheduling identity tied to failed components. Industry CMMS templates (Maryland school CMMS standard, FactVerse EAM normalization schema, Salesforce WorkOrder object) confirm that a unique Work Order ID/WOID is the near-universal anchor field, generally distinct from the asset/component ID it targets.[^12][^16][^25][^13][^17][^18][^14]

## Do Existing Studies Distinguish Action Identity, Priority, Workflow Status, and Event History?

| Distinction in thesis design | Literature status |
|---|---|
| Action identity (unique Action_Record_ID) | **Directly supported** — WOID/Work Order # is standard across CMMS/IFC literature[^16][^13][^17][^18] |
| Action priority/level (categorical) | **Indirectly supported** — Priority fields exist everywhere (IfcTask.Priority as integer, CMMS Priority picklists, AASHTO feasible-action bands) but none use the specific four-label Normal/Watch/Inspect/Priority Inspection taxonomy[^15][^16][^22][^23] |
| Workflow status (multi-state lifecycle) | **Directly supported for existence, indirectly for the specific label set** — CMMS status vocabularies (New Request, Assigned, In Progress, Completed, Closed, Awaiting Approval) closely parallel Draft/Open/Approved/In Progress/Completed/Closed[^16][^17][^18]; IFC's IfcTask.Status is only a free-text label with no enumerated set[^15] |
| Event/status history as a discrete logged entity | **Weakly/indirectly supported** — FactVerse's "lifecycle timestamps" table (created/approved/assigned/started/completed/closed/reopened) is the closest industry precedent to a Status_Event log[^17]; PROV-O formally separates Entity/Activity/Agent with time-stamped state transitions, offering a generic modeling analogue[^19]; no bridge/BIM inspection study reviewed implements a dedicated, versioned Status_Event table |

No reviewed study explicitly separates "action identity" from "action recommendation/priority" as two independent attributes of the same record the way the thesis proposes; priority is typically embedded as one field within a single work-order/task record rather than conceptually distinguished from identity.[^16][^13][^15]

## Actor, Timestamp, Reason, Approval, and Before/After State

Actor and timestamp capture is well precedented: Hammad et al. require inspector name/ID/qualifications and inspection date as mandatory ontology fields; CRM/CMMS schemas log CreatedById/LastModifiedById and multiple lifecycle timestamps; PROV-O formally models wasAttributedTo (agent) and startedAtTime/endedAtTime (time) as core relations. Reason/justification fields appear as free-text "Action Taken" or "resolution note"/"root cause" fields in CMMS templates, but are narrative rather than structured. Approval as a distinct step appears in CMMS status vocabularies ("Awaiting Approval") and in FactVerse's lifecycle timestamp field "approved," and IFC separately defines IfcRelAssociatesApproval for linking approval objects to project entities. However, an explicit "previous state → new state" pair recorded per event — the core structural feature of the thesis's Status_Event — is not directly evidenced in any bridge/BIM inspection study reviewed; the closest analogue is PROV-O's activity-based state transition modeling and generic audit-trail practice documentation, which are domain-general rather than BIM/FM-specific.[^9][^17][^18][^19][^26][^16]

## Auditability

Auditability in the reviewed literature is maintained primarily through persistent identifiers (IFC GlobalId, WOID) that allow cross-system traceability, and through timestamped lifecycle fields rather than a fully separate immutable event log. Blockchain-based provenance research proposes an immutable ledger specifically to strengthen tamper-evidence for digital twin asset information over time, indicating that standard relational/status-field designs are seen in the literature as insufficient for strong auditability and motivating append-only event-record approaches. This supports the thesis's Status_Event design conceptually (as an append-only audit mechanism) but the specific field set (actor, timestamp, reason, previous/new state) is thesis-defined rather than drawn verbatim from a cited implementation.[^17][^18][^20][^5]

## Linking Condition Evidence Directly to Inspection and Action Records

Several studies link condition/defect evidence to inspection records and, separately, to actions, but a continuous three-entity chain (evidence → Inspection_Record → Action_Record) with persistent IDs at each stage is not fully demonstrated in any single source. The Cardiff ORCA framework links RTK-captured defect images directly to IFC ComponentIDs and a defect database; Zhou et al. model IFC relationships connecting defect, cause, and maintenance action; and Chen et al. connect failure components identified from BIM data to scheduled maintenance work orders. These represent partial chains (evidence→component, or component→action) rather than the full three-tier record structure with explicit Inspection_Record and Action_Record identities the thesis proposes.[^4][^5][^12]

## Evidence for Human Approval and Closure Workflows

Human approval is evidenced by IFC's IfcRelAssociatesApproval relationship, by CMMS status labels including "Awaiting Approval," "Awaiting Funding," and "Declined/Refused," and by FactVerse's explicit "approved" lifecycle timestamp. Closure is evidenced by "Completed"/"Closed"/"Archived" status values common across CMMS templates and Salesforce's IsClosed boolean field. These confirm that approval and closure are recognized workflow stages in industry practice, but none of the reviewed sources model approval/closure as generating a discrete, queryable Status_Event record with actor and reason — this remains thesis-defined.[^18][^26][^16][^17]

## Literature-Supported vs. Thesis-Defined Elements of the Four-Level Action Logic

The four-level action taxonomy (Normal, Watch, Inspect, Priority Inspection) is **not validated by any single cited study**. What literature does support is the underlying principle that condition severity should drive tiered response — evidenced by AASHTO's NBI rating-to-action bands and Kentucky's condition-state-to-feasible-action catalog, both of which establish ordinal, multi-level condition-to-action mappings using different labels and granularity (numeric 0–9 or 4-state Good/Fair/Poor/Severe). The concept of graduated monitoring intensity (i.e., something resembling "Watch" as an intermediate surveillance state between "normal" and "requires physical action") is not directly evidenced in the reviewed bridge/BIM inspection literature. The specific four labels, their exact semantics, and their boundaries are thesis-defined design decisions inspired by, but not equivalent to, established condition-rating scales.[^21][^22][^23]

## Proposed Minimum Schema with Evidence Labeling

### Inspection_Record

| Field | Evidence status |
|---|---|
| Inspection_Record_ID (unique identifier) | Indirectly supported — component/defect IDs are standard (GlobalId, GUID) but a dedicated "Inspection_Record" ID separate from the component/defect ID is not explicitly modeled in reviewed studies[^5][^11] |
| Linked_Component_ID (IFC GlobalId reference) | Directly supported — GlobalId/GUID linkage is the standard mechanism across multiple independent studies[^5][^11][^3][^1] |
| Inspection_Date | Directly supported[^9] |
| Inspector_ID / Qualifications | Directly supported[^9] |
| Inspection_Method / Equipment | Directly supported[^9] |
| Defect_Type / Description | Directly supported[^9][^10] |
| Defect_Location / Geometry | Directly supported[^1][^6][^10] |
| Condition_Rating / Severity | Directly supported (AASHTO NBI, element condition states)[^21][^23] |
| Detected_Cause | Directly supported[^9] |
| Evidence_Attachment (image/point cloud reference) | Directly supported[^5][^17] |

### Action_Record

| Field | Evidence status |
|---|---|
| Action_Record_ID (identity) | Directly supported — WOID/Work Order # pattern is universal in CMMS/IFC[^16][^13][^17][^18] |
| Linked_Inspection_Record_ID | Indirectly supported — defect-to-action relationships exist[^4][^12], but explicit Inspection_Record-to-Action_Record ID linkage as two distinct persistent identifiers is not directly evidenced |
| Action_Level (Normal/Watch/Inspect/Priority Inspection) | Thesis-defined — ordinal condition-to-action tiering is literature-supported in principle (AASHTO/Kentucky)[^21][^23], but the specific four labels are not found in any source |
| Action_Type / Work_Type | Directly supported (MaintenanceType enum, Purpose/Work Type field)[^13][^16] |
| Assigned_Actor / Craft | Directly supported[^16][^17] |
| Scheduled/Due_Date | Directly supported[^16][^17] |
| Workflow_Status (Draft/Open/Approved/In Progress/Completed/Closed) | Indirectly supported — CMMS status vocabularies closely parallel this set but use varying labels (New Request, Assigned, Awaiting Approval, etc.); no source uses this exact six-state set[^16][^17][^18] |
| Cost / Labor fields | Directly supported[^16] |

### Status_Event

| Field | Evidence status |
|---|---|
| Status_Event_ID | Thesis-defined — no reviewed inspection/BIM study models a discrete event-record ID for status transitions |
| Linked_Action_Record_ID | Thesis-defined (structural necessity, not directly evidenced in inspection/BIM sources) |
| Actor | Indirectly supported — actor fields (CreatedById, inspector ID, PROV-O Agent) are established generally, though not specifically as a per-event log entry tied to status change[^18][^19] |
| Timestamp | Directly supported in principle — PROV-O's startedAtTime/endedAtTime and CMMS lifecycle timestamp tables (created/approved/started/completed/closed) closely match this[^19][^17] |
| Reason | Indirectly supported — free-text "Action Taken"/"resolution note" fields exist but are not formalized as a structured reason-for-transition field[^16][^17] |
| Previous_State | Evidence currently insufficient — no reviewed source explicitly stores the prior status value per transition; closest analogue is FactVerse's dual common_status/source_status fields, which is not equivalent[^17] |
| New_State | Evidence currently insufficient — same limitation as Previous_State; current practice generally overwrites status rather than logging both endpoints of each transition[^16][^18] |

## Summary of Evidentiary Strength

Inspection-record fields and IFC-based defect-to-component linkage are the most strongly evidenced portions of the proposed schema, resting on multiple peer-reviewed studies and the formal IFC4.3 standard. Action-record identity and basic priority/status fields are well precedented in CMMS/work-order literature and the IFC MaintenanceWorkOrder property set, though the exact label sets proposed (four-level Action_Level, six-state Workflow_Status) are thesis-specific refinements rather than adoptions of an existing standard. The Status_Event entity — particularly its previous-state/new-state pairing — has the weakest direct evidentiary support in the BIM–FM and infrastructure-inspection literature reviewed; it draws its closest conceptual grounding from the general-purpose PROV-O provenance model and blockchain-based digital-twin provenance research rather than from domain-specific inspection or CMMS studies. This gap is precisely where the thesis's proposed integration of Inspection_Record, Action_Record, and Status_Event into one traceable, auditable schema constitutes a genuine, literature-motivated but not literature-validated contribution.[^3][^6][^13][^20][^19][^1][^5][^9][^16][^17]

---

## References

1. [School of Design and the Built Environment](https://espace.curtin.edu.au/bitstream/handle/20.500.11937/87645/Xu%20S%202021.pdf;jsessionid=F54D7744E0F0078638D04F5CC83A084C?sequence=1)

2. [Building an ontological knowledgebase for bridge maintenance](https://www.sciencedirect.com/science/article/abs/pii/S0965997818307634)

3. [Integration of Extended IFC-BIM and Ontology for Information ...](https://www.jcoseik.or.kr/articles/xml/0zro/)

4. [A Parameter-Driven Method for Modeling Bridge Defects through IFC | Journal of Computing in Civil Engineering | Vol 36, No 4](https://ascelibrary.org/doi/abs/10.1061/(ASCE)CP.1943-5487.0001026) - AbstractBridges experience regular inspections from transport agencies/authorities periodically. How...

5. [ORCA – Online Research @](https://orca.cardiff.ac.uk/id/eprint/178445/1/template-iccbei2025-fullpaper.pdf)

6. [[PDF] Integrating RC Bridge Defect Information into BIM Models - TUM](https://publications.cms.bgu.tum.de/2018_Borrmann_bridgedefects.pdf)

7. [Enabling object-based documentation of existing bridge inspection data using Linked Data](https://mediatum.ub.tum.de/doc/1688385/)

8. [Ontological and Machine Learning Approaches for](https://spectrum.library.concordia.ca/id/eprint/991029/1/Bahreini_PhD_F2022.pdf)

9. [[PDF] Towards Unified Ontology for Modeling Lifecycle Inspection and ...](https://spectrum.library.concordia.ca/id/eprint/994160/1/paper_icccbe2018_FINAL-Dr_Hammad.pdf)

10. [Automation in Construction](https://pure.hud.ac.uk/ws/files/12923249/AutCon_2017_.pdf)

11. [Development of a BIM-based bridge maintenance system (BMS) for managing defect data](https://www.nature.com/articles/s41598-023-27924-6) - Bridges might experience many defects during use, such as pavement cracks and reinforcement corrosio

12. [BIM-based framework for automatic scheduling of facility maintenance work orders](https://2024.sci-hub.se/6704/eb7789634cc246d3e530a39f2733422d/chen2018.pdf)

13. [6.5.4.5 Pset_ProjectOrderMaintenanceWorkOrder - IFC 4.3.2 ...](https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_ProjectOrderMaintenanceWorkOrder.htm)

14. [5.3.3.6 IfcTask - IFC 4.3.2 Documentation](https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcTask.htm)

15. [IfcTask](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcprocessextension/lexical/ifctask.htm)

16. [Work-Order-Data-Template-07082024.xlsx](https://iac.mdschoolconstruction.org/wp-content/uploads/2024/07/Work-Order-Data-Template-07082024.xlsx)

17. [Connect CMMS and EAM Data to FactVerse | FactVerse Docs](https://datamesh.com/factverse-docs/modules/cmms-data-integration/) - Prepare CMMS and EAM work-order data for FactVerse CMMS Operations, multi-provider consolidation, Fa...

18. [WorkOrder](https://soft-builder.com/en/docs/SamplesDocs/Salesforce_Health_Cloud_Documentation/objects/o685.html)

19. [Effective Audit Trail of Data With PROV-O](https://d117h1jjiq768j.cloudfront.net/docs/default-source/marklogic-docs/2017_mlw_chi_effective-audit-trail-with-prov-o_henninger_final_05142017.pdf?sfvrsn=4f3b76b0_7)

20. [Blockchain-based digital twin data provenance for predictive ...](https://www.emerald.com/sasbe/article/13/1/4/1215461/Blockchain-based-digital-twin-data-provenance-for) - The purpose of this study is to focus on structured data provision and asset information model maint...

21. [[PDF] Bridge Preservation Guide](https://transportation.ky.gov/maintenance/documents/aashto%20presentations/bridges%20technical%20working%20group/bridge%20preservation%20guide-5-12-2011.pdf)

22. [4.1-i](https://www.dot.state.mn.us/bridge/pdf/insp/birm/birmchapt4-bridgeinspreporting.pdf)

23. [Handbook Sections - Transportation Research Board](https://onlinepubs.trb.org/onlinepubs/nchrp/docs/NCHRP14-23_FR-HandbookSections.pdf)

24. [Frontiers | Semi-automated creation of IFC bridge models from point clouds for maintenance applications](https://www.frontiersin.org/journals/built-environment/articles/10.3389/fbuil.2024.1375873/full) - Bridge maintenance activities benefit from digital models, provided in the interoperable IFC format....

25. [A BIM-based Facility Management Framework for ...](https://researchportal.hkust.edu.hk/en/publications/a-bim-based-facility-management-framework-for-automatic-schedulin)

26. [Contents - IFC 4.3.2 Documentation - IFC4.3](https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/toc.html)

