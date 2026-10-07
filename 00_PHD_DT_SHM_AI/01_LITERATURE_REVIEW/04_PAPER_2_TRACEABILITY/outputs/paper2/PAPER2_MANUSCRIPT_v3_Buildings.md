*Article*

# Version-Scoped BIM Component Identity for Accountable Traceability from Condition Evidence to Maintenance Action: A Steel Industrial Building Case with Duplicated IFC Identifiers

[Author 1] ^1,\*^, [Author 2] ^2^ and [Author 3] ^1^

^1^ [Department, University, City, Country]; [e-mail]\
^2^ [Department, University, City, Country]; [e-mail]\
\* Correspondence: [e-mail]

**Abstract:** Inspection findings and maintenance actions are increasingly stored in records linked to building information models, and monitoring data reach the same records through IFC GlobalIds. Such records are accountable only if each reference identifies the observed component in the model state that defined it. This study proposes a version-scoped identity rule, in which component identity is the pair (Model_Version_ID, BIM_GUID) and BIM_GUID is the exported IFC GlobalId, together with a traceability structure that links Sensor_ID, Condition_Evidence_ID, Inspection_Record_ID and Action_Status through 14 explicit rejection rules. The rule was applied to the hash-identified Revit model of a 25 m × 80 m steel industrial building with 759 structural elements. Eight stored IfcGUID values were each shared by two elements, whereas all 747 exported GlobalIds were distinct; the rule kept the 16 affected elements apart. On synthetic chain records anchored to nine real components, every chain was reconstructed forward and in reverse, and 145 of 145 mutated records were rejected with the intended failure class. A first frozen validator passed 68 of 78 challenge cases; corrective verification on the same set passed 78. The results are internal verification on one model version and do not demonstrate field performance.

**Keywords:** building information modelling; IFC GlobalId; component identity; model versioning; traceability; inspection and maintenance records; asset information management

## 1. Introduction

### 1.1. Inspection and Maintenance Information in BIM

Facility managers have used building information modelling (BIM) for operation and maintenance information for more than a decade [1,2]. Recent work places the inspection record itself inside BIM-linked structures. Bellon et al. [3] represent inspections, damage, maintenance services and costs in IFC using real bridge inspection data. Hagedorn et al. [4] route a bridge inspection finding to a repair order through linked information containers. Kim et al. [5] link 590 maintenance work records to IFC objects, and Marmo et al. [6] map an IFC subset for maintenance to a relational database. In each of these structures, the component identifier is the join that allows an asset manager to ask which evidence led to which action on which element.

### 1.2. Why a Link to a Component Is Not Yet Accountable Evidence

Monitoring data enter the same structures through the same join. Delgado et al. [7] generate IFC-compliant models of a bridge monitoring system with time-series data; Chatsuwan et al. [8] map indoor-environment sensors to IFC GlobalIds through a mapping table; Ramonell et al. [9] join IFC entities and IoT devices through shared GUIDs. Chatsuwan et al. [8] also observe that a GlobalId can be regenerated when an element is deleted and recreated during a model update, which breaks the sensor link without warning. Rogage et al. [10] tested more than 100 building models and found that very few were authored in a way that let relevant objects be identified for transfer to a maintenance database. A record that points to a GlobalId therefore carries an unstated assumption about which model state issued that GlobalId and whether that state is still current.

### 1.3. Identity, Versions and Provenance

Borkowski et al. [11] show that the same physical element receives different GUIDs in independently created design, as-built and operation files, and propose a persistent identifier above the GUID. Rico Thirion et al. [12] give bridge components a coded identifier that is kept unchanged across model updates, IFC exports and platforms. Fang et al. [13] measure completeness, validity, uniqueness and stability of IfcGUIDs and register every check with hashes, timestamps and operators. Mariniello et al. [14] log the validation of monitoring data and the reactions to alerts on a ledger, García et al. [15] tie publish/hold decisions to a specific IFC revision and named roles, and Kochovski et al. [16] issue decentralised identifiers and verifiable credentials for building logbook data. Each study addresses part of one question: can a recorded action be traced back to valid evidence about the right component?

### 1.4. Research Gap, Question and Contributions

Sensor-to-component binding, inspection-to-component linkage, inspection-to-action linkage, identifier quality checking, auditable data validation and competency-question verification are all reported (Section 2), and this study does not claim any of them as new. Among the eleven closest studies read in full, none reports one component-level chain from sensor to action status in which (a) identity is scoped to a registered model version and fails closed under any other version, (b) explicit rules reject missing, invalid and ambiguous links at every step, with deliberate invalid-data tests, and (c) the chain is exercised on a real model that contains an observed identifier anomaly. Lorvão Antunes et al. [17] reach sensors and inspections without actions or rule validation; Bellon et al. [3] reach inspections and maintenance without sensors or identity governance; Fang et al. [13] govern identifiers without a downstream chain. Rico Thirion et al. [12] come closest: on an in-service bridge, sensor events and inspection files reach approved BCF issues through one persistent component identifier, but that identifier is deliberately independent of the model version, the validation rules constrain property values rather than links, and no invalid records are tested.

The research question is: can a BIM-based, model-version-controlled identity architecture support deterministic traceability Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status, with explicit integrity failures for missing, invalid and ambiguous information?

The study makes three contributions:

1. A version-scoped component-identity rule, (Model_Version_ID, BIM_GUID) with BIM_GUID equal to the exported IFC GlobalId and with detect-not-repair handling of stored-identifier duplicates, applied to a real model in which stored and exported identifiers diverge for 16 elements.
2. A component-level traceability structure from sensor to action status with forward and reverse reconstruction and 14 integrity rules that separate missing, invalid and ambiguous links, verified internally on synthetic records anchored to real component identities.
3. A verification record that reports the first frozen run (68/78) separately from the corrective run on the same challenge set (78/78) and classifies every first-run failure.

Section 2 positions the study. Section 3 describes the materials and methods, Section 4 the results and Section 5 the discussion and limitations. Section 6 concludes.

## 2. Related Work

### 2.1. Monitoring Data Linked to BIM

Systematic reviews of BIM for health monitoring and maintenance list IFC schema extension, interoperability and data volume as open problems [18,19]. IFC Monitor extends the IFC schema to describe structural health monitoring systems [20]. Delgado et al. [7] build parametric IFC models of a fibre-optic monitoring system on a bridge, and Hu et al. [21] visualise processed IoT data on structural members of a prototype frame. Gragnaniello et al. [22] check monitoring information requirements in a viaduct model with the Information Delivery Specification. Chatsuwan et al. [8] and Ramonell et al. [9] bind live sensor streams to IFC entities through GlobalIds or shared GUIDs, and Lorvão Antunes et al. [17] model sensors as hosted by structures using the SSN ontology and link physical objects to ifcElement GUIDs in three road-authority pilots. Binding a sensor to a component is established.

### 2.2. BIM and IFC Component Identity

Lee et al. [23,24] derive rule logic for model view definitions, including GUID uniqueness, format and round-trip rules. Fang et al. [13] treat the 22-character IfcGUID as a cross-system primary key and measure four quality indicators over 820 objects in a virtual smart-home project; stability is defined as identical GlobalIds in two exports made under identical settings. Shafiq and Lockley [25] report GUID inconsistencies after modelling operations and match objects by attribute signatures. None of these studies distinguishes the GUID stored as a Revit parameter from the GlobalId written at export. Section 4.3 shows why the distinction matters.

### 2.3. Model Versioning and Identity Persistence

Borkowski et al. [11] give each element a GUID-independent URI and attach a phase-specific GUID as a backlink; cross-file matching is manual, and the authors state that the ontology is not designed for continuous monitoring. Rico Thirion et al. [12] take the opposite design choice: a hierarchy-coded persistent component identifier is stored as a shared parameter and in an IFC property set so that identity stays the same across model updates, IFC re-exports and platforms, and they report 100 % retention for 1067 bridge components. That identifier is version-independent, and no uniqueness check on it is reported. Fang et al. [13] test GlobalId stability between two exports. Persistence of identity across versions is therefore addressed in the literature, and the present study does not claim it. It claims a narrower property: a GlobalId held in a downstream record is valid only together with the model version that issued it.

### 2.4. Provenance and Asset-Information Governance

Data quality has several dimensions beyond accuracy, including traceability of origin [26]. In construction, Çelik et al. [27] record object version and responsibility for BIM objects on a blockchain, Erri Pradeep et al. [28] keep blockchain records of design information exchanges for liability control, and Tavakoli et al. [29] propose a digital-twin data provenance model for predictive asset management. Mariniello et al. [14] use smart contracts to validate monitoring data, authenticate damage-detection tools and log reactions on a real viaduct; component identity binding is not reported. García et al. [15] attach publish/hold decision records to IFC revisions and roles across 22 real deliverables, and Patacas et al. [2] validate asset information models against requirements in a common data environment. The PAV vocabulary separates authoring, provenance and versioning roles in a domain-neutral form [30]. Provenance of records is established; provenance of the component reference inside those records is less developed.

### 2.5. Inspection and Maintenance Information Linkage

Sacks et al. [31] specify information delivery requirements for bridge inspection. Bellon et al. [3] represent inspections as IfcTask, damage as IfcSurfaceFeature and the inspector as IfcActor, and link damage to maintenance services and cost items. Hagedorn et al. [4] and Wan et al. [32] connect inspection findings to repair activities in bridge management. Kim et al. [5] link maintenance work records to IFC objects, Shalabi and Turkan [33] link building-system alarms to maintenance management records through IFC, and Liu and El-Gohary [34] model deterioration and maintenance actions in a bridge ontology. Matarneh et al. [35] and Otranto et al. [36] report that manual data entry and missing verification degrade information handed over to facility management, and Godager et al. [37] and Chatsuwan et al. [38] describe limits of IFC-based delivery for asset management. None of these studies starts from sensor-derived evidence.

### 2.6. Forward and Reverse Traceability

Kim et al. [5] retrieve work records by component and across components that share objects. Lorvão Antunes et al. [17] answer competency questions such as "what are the results of a certain inspection by element". These are forward or single-step queries. Reconstruction from an action back to the originating sensor across four record types is not reported in the studies reviewed.

### 2.7. Integrity Verification and Competency Questions

Competency questions are a standard device for scoping and verifying ontologies [39] and are used by Lorvão Antunes et al. [17], Liu and El-Gohary [34] and Borkowski et al. [11]. Rule-based checking of BIM data is established [13,15,23,24]. Mutation-based test generation, in which faults are injected deliberately to check whether a test procedure detects them, is established in software engineering [40]. In BIM traceability it appears only in limited forms: a pre-test/post-test design [13] and one schema-level inconsistency test [11].

### 2.8. Positioning

Table 1 compares the eleven closest studies, read in full, against the capabilities of the present design. Seven capabilities are reported individually; none of the studies covers the version-scoped chain with rejection rules and invalid-data tests on a real model. The search was targeted (about 140 unique records from Consensus, Scopus, OpenAlex and a Zotero library, October 2026) and was not a systematic review.

**Table 1.** Positioning against the eleven closest studies (YES/PARTIAL/NO; NR = not reported). Evidence level: full text.

| Study | Sensor–BIM | Version | Inspection | Action | Reverse trace | Rules | CQs | Invalid-data tests | Real data |
|---|---|---|---|---|---|---|---|---|---|
| Borkowski et al. [11] | NO | YES | PARTIAL | NO | PARTIAL | PARTIAL | YES | PARTIAL | PARTIAL |
| Fang et al. [13] | PARTIAL | YES | NO | NO | NR | YES | NO | PARTIAL | NO |
| Lorvão Antunes et al. [17] | YES | NO | YES | NO | PARTIAL | NO | YES | NO | YES |
| Mariniello et al. [14] | PARTIAL | NR | PARTIAL | PARTIAL | NR | YES | NO | PARTIAL | YES |
| García et al. [15] | NO | YES | NO | NO | NR | YES | NO | PARTIAL | YES |
| Bellon et al. [3] | NO | NR | YES | YES | NR | PARTIAL | NO | NO | YES |
| Kim et al. [5] | NO | NO | PARTIAL | YES | YES | NO | NO | NO | YES |
| Hagedorn et al. [4] | PARTIAL | NR | YES | YES | NR | PARTIAL | NO | NO | YES |
| Chatsuwan et al. [8] | YES | NO | NO | PARTIAL | NR | NO | NO | NO | YES |
| Ramonell et al. [9] | YES | NR | PARTIAL | PARTIAL | NR | NO | NO | NO | PARTIAL |
| Rico Thirion et al. [12] | YES | PARTIAL | YES | PARTIAL | NR | PARTIAL | NO | NO | YES |
| This study | YES (synthetic) | YES | YES (synthetic) | YES (synthetic) | YES | YES | YES | YES | Identities and anomaly real; chain records synthetic |

## 3. Materials and Methods

### 3.1. Research Design and Scope

The study follows a design-science approach [41]: an information artefact (an identity rule and a traceability structure) is designed against a stated problem and evaluated on one controlled case. The evaluation tests information traceability only. It does not diagnose structural condition, calibrate a structural model or evaluate maintenance outcomes. Condition evidence is treated as a record type with an identifier, a status and a validity window; how the evidence is computed is outside the scope of this paper. Every result is labelled E1 (objective observation of source data), E2 (comparison across independent sources) or E3 (internal verification of the authors' own specification and code). E3 results are not used to establish novelty, which is argued from the literature in Section 2.

### 3.2. Case Building

The case building is a single-storey steel portal-frame industrial building with plan dimensions of 25 m × 80 m, grids 1–9 along the length (eight 10 m bays) and A–B across the span, column top at +6.300 m and ridge at +9.300 m. The building has a Revit model, an IFC export and as-built drawings in PDF. It was chosen because all three sources exist for the same structure and because the research team controlled the model, so that its state could be frozen and hashed.

A 1:10 laboratory frame of the same building, 2.5 m × 7.0 m in plan, is being built for later condition-monitoring work. Because of the available laboratory floor area it reproduces seven of the eight bays. The laboratory frame contributes no data to this paper; its relation to the full-scale model is discussed in Section 5.6.

### 3.3. Source Hierarchy and Model-Version Registration

Roles were assigned to four sources before any identity analysis. The Revit file of version 4 of the model was designated the working BIM reference after live verification; it is not claimed to be an exact as-built model. The IFC file exported from it was designated a derived exchange model, and the as-built PDF the physical as-built reference. A second Revit file in the project folder, whose relationship to the working reference could not be established from file metadata, was left unresolved and not used (Figure 1).

**Figure 1.** Source hierarchy and evidence flow from identity readiness to traceability verification. [To be drawn.]

The working reference was opened in Autodesk Revit 2027 (build 27.3.0.28) and read through a read-only programming interface. The live document path, a SHA-256 hash of the saved file (47748cbeb460229e…), the file size (37,564,416 bytes) and the flag Document_Modified = FALSE were recorded. The version identifier MV-RVT-20261005-47748cbe was then registered by the researcher as a provenance event together with the hash, the software build, the IFC file name and hash, and the known limitations. Registration is a human decision; a newer file timestamp does not make a file authoritative.

### 3.4. Identity-Governance Method

Every element in the scoped categories (structural framing, structural columns, structural foundations, generic models and floors) was read live: ElementId, UniqueId, the stored IfcGUID parameter, category, family, type and level. The IFC export was parsed with IfcOpenShell 0.8.5 and joined to the live inventory on Revit ElementId = IFC Tag, and the stored IfcGUID and the exported GlobalId were compared for each element.

Identity was then defined as follows. BIM_GUID is the exported IFC GlobalId. Component identity is the ordered pair (Model_Version_ID, BIM_GUID), not a concatenated string. UniqueId, ElementId and the stored IfcGUID are supporting evidence only. A duplicate stored IfcGUID is an integrity anomaly to be detected and reported; it is not repaired or regenerated in the source model, because a repair would erase the evidence that earlier references may be wrong. Location is derived by a separate locator rule (native level, then IFC spatial containment, then labelled geometry) and is not part of identity. Asset_ID is optional.

### 3.5. Traceability Architecture

Six entities were defined: Model_Version, BIM_Component, Sensor, Condition_Evidence, Inspection_Record and Action_Status_Record (Table 2, Figure 2). Each record holds the identifier of the record it depends on. The evidence record stores its own copy of the sensor and component reference, and the inspection and action records store the identifier of the upstream record, so a broken reference is visible in the record itself rather than inferred. Action level (NORMAL, WATCH, INSPECT, PRIORITY_INSPECTION) and action workflow status (nine states from proposed to reopened) are separate controlled vocabularies; neither encodes a maintenance decision rule.

**Table 2.** Identifier roles.

| Identifier | Role | Origin in this study |
|---|---|---|
| Model_Version_ID | Scopes every component reference | Registered (real) |
| BIM_GUID | Exported IFC GlobalId; key together with Model_Version_ID | Real |
| Revit_UniqueId | Supporting; detects ambiguous identity | Real |
| Stored_IfcGUID | Supporting; not authoritative | Real |
| Sensor_ID | Sensor placement | Synthetic |
| Condition_Evidence_ID | Evidence record; references one sensor and one component | Synthetic |
| Inspection_Record_ID | References the evidence used | Synthetic |
| Action_ID, Action_Status | References the inspection; level and workflow status | Synthetic |

![](figures/Fig2_traceability_chain.png){width=15cm}

**Figure 2.** Traceability chain with the rules evaluated at each step. Forward and reverse reconstruction use the references stored in each record; the registered model version scopes the component reference.

A BIM_GUID is resolved only within the version named in the same record. If that version is not registered, the lookup fails with MODEL_VERSION_MISMATCH even when the same GlobalId exists in the registered version, so a reference to a superseded or unknown model state becomes visible instead of resolving silently to whatever element now carries that GlobalId. The pair does not tell the user which element in a new version corresponds to an element in the old one; that requires a persistence mechanism such as the one of Borkowski et al. [11]. The two mechanisms are complementary: persistence answers "which element is this across versions", and version scoping answers "is this reference still valid as written".

A sensor is bound to exactly one active component within the declared version; the schema does not constrain how many sensors a component may carry. An inspection record names the evidence record it used, and the evidence must have a known status and a validity window covering the inspection date. An action record names the inspection, and its level and status come from controlled vocabularies. Forward traceability resolves component, evidence, inspection and action from a Sensor_ID; reverse traceability resolves inspection, evidence, component and sensor from an Action_ID, and the result must equal the forward chain. Missing values, invalid values and ambiguous values (several components in one field, a shared stored IfcGUID used as key, GlobalId and UniqueId pointing to different elements) map to disjoint groups of failure classes.

### 3.6. Integrity Rules and Competency Questions

Fourteen rules (IR-01 to IR-14) were written before any test fixture was generated and were frozen with a hash (Table 3). They are evaluated in a fixed order, and the reported failure class is that of the first failing rule. No score or index is computed, so a record is either accepted (with or without warning flags) or rejected with a named class. Twelve competency questions (CQ01–CQ12) were frozen before validation (Table 4); each has an input, an expected output, the entities and rules involved, and a pass criterion.

**Table 3.** Integrity rules.

| Rule | Condition | Failure class |
|---|---|---|
| IR-01 | Sensor_ID present and registered | MISSING_IDENTIFIER / UNKNOWN_SENSOR |
| IR-02 | Sensor maps to exactly one active component in the declared version | SENSOR_BINDING_MISMATCH |
| IR-03 | BIM_GUID exists in the registered version | MISSING_IDENTIFIER / UNKNOWN_BIM_GUID |
| IR-04 | Identity evaluated as the pair (Model_Version_ID, BIM_GUID) | MODEL_VERSION_MISMATCH / UNKNOWN_BIM_GUID |
| IR-05 | Duplicate stored IfcGUID reported and never used as BIM_GUID | AMBIGUOUS_IDENTITY / anomaly flag |
| IR-06 | Condition_Evidence_ID unique | DUPLICATE_EVIDENCE_ID |
| IR-07 | Evidence references the chain's sensor and component | BROKEN_EVIDENCE_LINK |
| IR-08 | Evidence status and validity window usable at inspection date | INVALID_EVIDENCE |
| IR-09 | Inspection references the evidence | BROKEN_INSPECTION_LINK |
| IR-10 | Action level and status from controlled vocabularies | INVALID_ACTION_STATUS |
| IR-11 | Action references the inspection | BROKEN_ACTION_LINK |
| IR-12 | Unregistered or wrong version fails lookup | MODEL_VERSION_MISMATCH |
| IR-13 | Required identity and provenance fields present | MISSING_IDENTIFIER / PROVENANCE_MISSING |
| IR-14 | No silent resolution of multiple values or of BIM_GUID/UniqueId disagreement | AMBIGUOUS_IDENTITY |

**Table 4.** Competency questions.

| CQ | Question | Rules |
|---|---|---|
| CQ01 | Given Sensor_ID, which BIM component is linked? | IR-01, IR-02 |
| CQ02 | Which Model_Version_ID was valid when the link was recorded? | IR-12 |
| CQ03 | Given Condition_Evidence_ID, which sensor produced it? | IR-06, IR-07 |
| CQ04 | Which component did that evidence refer to? | IR-07 |
| CQ05 | Was the evidence usable at the time of inspection? | IR-08 |
| CQ06 | Which inspection used that evidence? | IR-09 |
| CQ07 | What action level and status resulted from the inspection? | IR-10, IR-11 |
| CQ08 | Who or what record created or changed the status? | IR-13 |
| CQ09 | Can the chain be reconstructed from the action back to the sensor? | IR-07, IR-09, IR-11 |
| CQ10 | Does a wrong model version cause deterministic rejection? | IR-12, IR-04 |
| CQ11 | Do missing, duplicate and invalid identifiers fail explicitly? | IR-01, IR-03, IR-06, IR-13 |
| CQ12 | Are missing, invalid and ambiguous information distinguished? | IR-13, IR-01/03/08/10, IR-14 |

### 3.7. Positive and Negative Verification

Nine positive fixtures were built on real component identities from the registered model: two primary columns, a primary rafter and a ridge rafter, a gable column and a gable rafter, a placeholder brace, and both elements of one real duplicate pair. All sensor, evidence, inspection and action records attached to them were synthetic and were labelled as such in every record. Seventeen deterministic mutation classes (Table 5), in the sense of mutation-based testing [40], were applied to the nine positives to generate 145 negative fixtures with 13 intended failure classes. The fixtures were hashed before validation and re-checked unchanged afterwards. A rejection counted as a pass only if it was a controlled failure with the intended class; a crash did not count.

**Table 5.** Mutation classes.

| Class | Target | Operation | Intended class |
|---|---|---|---|
| NEG01 | Sensor_ID | empty | MISSING_IDENTIFIER |
| NEG02 | Sensor_ID | unregistered value | UNKNOWN_SENSOR |
| NEG03 | BIM_GUID | empty | MISSING_IDENTIFIER |
| NEG04 | BIM_GUID | well-formed unknown value | UNKNOWN_BIM_GUID |
| NEG05 | Model_Version_ID | unregistered version | MODEL_VERSION_MISMATCH |
| NEG06 | BIM_GUID | two values in one field | AMBIGUOUS_IDENTITY |
| NEG07 | Condition_Evidence_ID | empty | MISSING_IDENTIFIER |
| NEG08 | Condition_Evidence_ID | ID of another chain | DUPLICATE_EVIDENCE_ID |
| NEG09 | Evidence sensor reference | sensor of another chain | BROKEN_EVIDENCE_LINK |
| NEG10 | Evidence_Status | EXPIRED | INVALID_EVIDENCE |
| NEG11 | Inspection_Record_ID | empty | MISSING_IDENTIFIER |
| NEG12 | Inspection evidence reference | evidence of another chain | BROKEN_INSPECTION_LINK |
| NEG13 | Action_Status | out-of-vocabulary value | INVALID_ACTION_STATUS |
| NEG14 | Action inspection reference | inspection of another chain | BROKEN_ACTION_LINK |
| NEG15 | Provenance | empty | PROVENANCE_MISSING |
| NEG16 | BIM_GUID | shared stored IfcGUID | AMBIGUOUS_IDENTITY |
| NEG17 | BIM_GUID and UniqueId | another valid component | SENSOR_BINDING_MISMATCH |

### 3.8. Challenge Procedure

A second set of 78 challenge cases was written after the first validation and frozen: 19 expected accepts, 59 expected rejects, 8 multi-fault cases with up to three simultaneous faults, and all 8 real duplicate pairs in three variants each. It was run once against the unchanged, hash-frozen validator. The author of the challenge set had not seen validator outputs for these cases but had written the validator, so the set is classified as internal with Level C independence (blind to outputs, not to code). Every first-run failure was classified as either a validator defect or a specification gap. Defects were then corrected in a new validator version, and the same 78 cases and the original 154 fixtures were re-run. One intermediate corrected attempt, whose output files were deleted before the final run, is excluded from the evidence.

### 3.9. Use of Generative AI Tools

[To be completed by the authors: name, version and purpose of any generative-AI tool used in literature screening, coding or text preparation, and the human checks applied, following the journal policy.]

## 4. Results

### 4.1. BIM Source and Inventory

The working reference was verified live on 6 October 2026: the open document was the registered file, unmodified, with the registered hash [E1]. A targeted comparison of 16 items against the as-built drawings gave 3 matches, 4 functionally equivalent names, 4 mismatches and 5 items that could not be checked [E2]; intermediate gable columns, for example, stand at Y = 0, 4.1, 8.2, 16.8, 20.9 and 25.0 m in the model, while the printed dimension chain reads 8500 | 8000 | 8500 mm. The model is therefore treated as a working reference, not as an as-built model. The live model held 759 elements in the scoped categories: 625 structural framing, 62 structural columns, 26 structural foundations, 45 generic models and 1 floor, with 759 distinct ElementIds and UniqueIds [E1]. No element carried an Asset_ID (0 of 759) [E1]. The eight brace objects were generic-model placeholders without material or section, and none of the 18 structural framing elements sampled had a native level [E1]. The IFC header recorded the same save count (43) as the Revit file metadata [E2].

### 4.2. Objective Identity Observations

Of the 759 scoped elements, 747 were present in the IFC export and 12 opening objects were not [E2]. For the 747 exported elements, the stored IfcGUID equalled the exported GlobalId for 739 and differed for 8 (Figure 3a). In terms of identity integrity, 731 elements passed, 16 were conditional (both members of each duplicate pair) and 12 were unresolved (not exported); none failed (Table 6). The live model, the IFC export and an inventory produced earlier from the same project agreed for 739 elements, partially agreed for 20 and disagreed for none; all 232 elements in the earlier inventory had identical identifiers [E2].

**Table 6.** Objective identity observations, model MV-RVT-20261005-47748cbe.

| Observation | Count | Class |
|---|---|---|
| Scoped live elements | 759 | E1 |
| Distinct ElementIds/UniqueIds | 759/759 | E1 |
| Elements in IFC export | 747 | E2 |
| Stored IfcGUID = exported GlobalId | 739 | E2 |
| Stored IfcGUID ≠ exported GlobalId | 8 | E2 |
| Not exported (openings, no BIM_GUID) | 12 | E2 |
| Duplicate stored IfcGUID values | 8 (16 elements) | E1 |
| Distinct exported GlobalIds among exported elements | 747/747 | E2 |
| Elements with Asset_ID | 0 | E1 |

![](figures/Fig4_identity_audit.png){width=15cm}

**Figure 3.** (**a**) Comparison of the stored IfcGUID parameter with the exported IFC GlobalId for the 759 scoped elements; (**b**) structure of one of the eight duplicate pairs: the stored value is shared, the exported values differ.

### 4.3. Real Duplicate-Identifier Case

Eight stored IfcGUID values were each shared by two elements with distinct UniqueIds, and the duplication was reproduced in the live model [E1]. In the IFC export, the second element of each pair received a new GlobalId, so the 16 elements had 16 distinct GlobalIds [E2] (Figure 3b). A sensor mapping built from the stored parameter would have merged eight pairs of physically distinct members under one key each; using the exported GlobalId kept them apart. The cause of the duplication was not established, and no parameter was edited. Under the identity rule, both elements of every pair were accepted through their exported GlobalId with an anomaly flag, and a chain that used the shared stored value as BIM_GUID was rejected as AMBIGUOUS_IDENTITY; this held for all eight pairs [E3]. A chain that referenced a valid BIM_GUID under an unregistered version was rejected with MODEL_VERSION_MISMATCH for all nine positives [E3].

### 4.4. Traceability and Internal Verification

For all nine positive chains, the forward chain resolved to the registered records, and reverse reconstruction from the action record returned the same five identifiers [E3]. All 9 positives were accepted; 3 carried the expected flags (one component-metadata gap for the placeholder brace and two duplicate-identifier flags for the real pair). All 145 negatives were rejected with the intended failure class; 13 rules acted as the deciding rule at least once, and IR-04 acted as the lookup key in every test. No crash occurred. All 121 competency-question checks passed (10 each for CQ01–CQ10, 8 for CQ11 and 13 for CQ12), and missing, invalid and ambiguous cases fell into disjoint groups of failure classes [E3] (Table 7). The negative set was generated by the authors of the rules and the validator.

**Table 7.** Internal positive and negative verification [E3].

| Set | Cases | Expected | Observed |
|---|---|---|---|
| Positive fixtures | 9 | Accept (3 with flags) | 9 accepted, 3 flagged as expected |
| Negative fixtures (17 mutation classes) | 145 | Reject with intended class | 145 rejected with intended class |
| Forward reconstruction | 9 | Full chain | 9 |
| Reverse reconstruction | 9 | Equal to forward chain | 9 |
| Competency-question checks | 121 | Pass criterion | 121 |

### 4.5. Challenge Runs

On the 78-case challenge set, the frozen first validator passed 68 cases, failed 10 and crashed on none [E3]. Eight failures were validator defects: registry-level duplicates not detected (three cases), schema-required fields not enforced (three) and anomaly flags not shown on rejected records (two). Two were specification gaps: whether identifiers must match exactly (one case) and whether dates must follow ISO 8601 (one) (Table 8). In seven of the eight multi-fault cases the first validator reported the class of the earliest failing rule; the remaining case missed an anomaly flag, not a class. After the defects were corrected and the two gaps were resolved by researcher decision (exact matching after trimming leading and trailing whitespace in required text fields; ISO 8601 for dates), the new validator passed the same 78 cases and reproduced all 154 earlier outcomes without per-fixture difference [E3]. Because the corrections were made against this set, the re-run is corrective verification and not fresh evidence of robustness.

**Table 8.** Challenge runs [E3].

| Run | Validator | Set | Pass | Fail | Status |
|---|---|---|---|---|---|
| First frozen run | v1 (hash-frozen) | 78 cases | 68 | 10 | Formal evidence |
| Intermediate attempt | v2 draft | 78 cases | (76 reported) | (2) | Not evidence; outputs deleted |
| Corrective run | v2 | Same 78 cases | 78 | 0 | Corrective verification |
| Regression | v2 | 154 earlier fixtures | 154 | 0 | No per-fixture difference |
| Consistency patch | v2.1 | 78 + 154 | 0 differences | – | No regression |

### 4.6. Evidence Boundary

Table 9 separates the evidence classes. The observations in Sections 4.1 and 4.2 and the first three sentences of Section 4.3 are E1 or E2 and would stand without any test; the remaining results are E3.

**Table 9.** Claim, evidence and independence.

| Claim | Evidence | Class | Independence |
|---|---|---|---|
| Stored and exported identifiers diverge for 16 elements | Live model vs. IFC | E1/E2 | Tool outputs, not author content |
| Exported GlobalIds separate the 16 elements in this export | IFC parse | E2 | Tool output |
| Version-scoped lookup rejects unregistered versions | 9/9 | E3 | Same author |
| Chain reconstructs forward and in reverse | 9/9 and 9/9 | E3 | Synthetic records |
| Rules reject designed mutations | 145/145 | E3 | Same author |
| First validator had defects | 68/78 | E3 | Level C |
| Corrections hold on the same set | 78/78 | E3 | Same set reused |

## 5. Discussion

### 5.1. What the Objective Evidence Demonstrates

In the case model, the identifier a user reads from the Revit element (the stored IfcGUID parameter) is not always the identifier the exchange file carries (the exported GlobalId), and the stored value is shared by two elements eight times. A sensor-to-component table built from the stored parameter would bind one sensor reference to two physical members without any warning. This is a source-data observation, independent of the authors' code. It shows that the choice of key has consequences in a working model and that the choice must be recorded together with the model state. Whether such duplicates are frequent in practice cannot be inferred from one model.

### 5.2. What Is Only Internally Verified

The rejection behaviour, the reconstruction in both directions and the competency-question answers were checked by the authors on records the authors wrote. The first-run result (68/78) shows that the authors' validator was incomplete when it first met cases it had not been tuned on; the corrective result (78/78) shows only that the exposed defects were fixed.

### 5.3. Comparison with the Closest Studies

Lorvão Antunes et al. [17] go further than this study on real data, with three national pilots, real sensors and real inspection campaigns, but they do not carry the chain to actions and state that rule-based validation was not addressed. Bellon et al. [3] represent inspection, damage, maintenance and cost in IFC with real inspection data; they start from visual inspection rather than sensor evidence and validate schema conformance rather than rejecting broken references. Borkowski et al. [11] solve a harder identity problem, persistence across versions, with manual matching and no downstream records. Fang et al. [13] measure GlobalId stability across two exports, which this study did not do, and repair the mapping layer, which this study forbids for the source model. Mariniello et al. [14] and García et al. [15] apply deterministic gates to real data at the level of data streams and deliverables rather than component references.

Rico Thirion et al. [12] is the closest study. On an in-service bridge with 1067 components, 112 of them monitored, sensor threshold events and IFC inspection files are linked through a persistent component identifier to BCF issues that experts approve under a RACI matrix. It goes further than the present study on real sensor data and live operation, and it overlaps with Contribution 2. It differs on three points. First, identity is made version-independent through a stored, coded parameter, whereas the present study scopes identity to a registered model version and takes the key from the export rather than from a stored parameter; the P002 case shows that a stored identifier parameter can be duplicated across elements, and no uniqueness check is reported for the stored identifier in that study. Second, its validation rules constrain property values, not links between records, and no deliberately invalid records are injected. Third, only successful outcomes are reported (100 % identifier retention, no discrepancies), the data are confidential, and versioning and audit trails are named as future work. Kochovski et al. [16], read at abstract level only, use decentralised identifiers and verifiable credentials for provenance of building logbook data, including sensor logs and inspection records, in a real case; the abstract does not report version-scoped rejection or deliberate invalid-data testing. The difference claimed here is the combination: one component reference scoped to a model version and checked at every step from sensor to action, on a model with an observed anomaly.

### 5.4. Contribution to Construction and Asset Management

For an asset manager, the question is whether an action recorded against a component can be defended later: which evidence triggered it, which inspection used that evidence, and whether that evidence referred to the same element in the same model state. The design turns these questions into queries with yes/no answers and named failure classes, and moves part of asset-information governance (who recorded what, against which model version) from procedure into checkable records. García et al. [15] do this for deliverables; this study does it for component references in inspection and maintenance records.

Three practices follow from the case and need no new software. First, record the model version with every component reference held outside the model. Second, take the identifier from the exchange file, not from an authoring-tool parameter, and keep the parameter as evidence. Third, report identifier duplicates as anomalies instead of repairing them silently, because a repair erases the evidence that earlier references may be wrong.

### 5.5. Limitations

The study has the following limitations. (1) One building and one Revit model; no cross-project generalisation. (2) One registered model version and one IFC export; persistence of GlobalIds across re-exports or edits was not tested. (3) The model is a working reference; reconciliation with the as-built drawings was a 16-item sample with 4 mismatches and 5 items that could not be checked. (4) All sensor, condition-evidence, inspection and action records are synthetic, and only 9 of 759 components carry chains. (5) Rules, mutation generator, challenge set and validator were written by the same author; the challenge set has Level C independence. (6) The corrective 78/78 run reused the challenge set it was corrected against. (7) No external, independent or field validation was performed. (8) Component-to-sensor cardinality is not constrained, and identical repeated sensor rows were not tested. (9) The cause of the eight stored-identifier duplicates is not known. (10) Twelve opening objects have no BIM_GUID because they were not exported. (11) The output files of one intermediate validator attempt were deleted, and that attempt is excluded from the evidence. (12) The literature search was targeted, not systematic, and one directly relevant 2026 study [16] was read at abstract level only. The results do not show that the exported GlobalId is stable across re-exports, that the rule scales to many versions, that the rules are complete, or that the structure improves inspection or maintenance decisions.

### 5.6. Future Work

Two tests follow. The first is a second registered version of the same model, re-exported, so that GlobalId persistence and version-mismatch handling can be observed on real data. The second uses measured evidence in place of the synthetic records. The 1:10 laboratory frame (2.5 m × 7.0 m) reproduces seven of the eight bays of the 25 m × 80 m building, so its members map to a subset of the full-scale components and the members of the eighth bay have no physical counterpart. Under the identity rule of this study, a laboratory sensor must reference a (Model_Version_ID, BIM_GUID) pair that exists in a registered version; a reference to a member of the missing bay, or to a laboratory-only element, would be rejected rather than resolved silently. How laboratory evidence should be mapped to full-scale components is left to that work.

## 6. Conclusions

The research question asked whether a model-version-controlled identity architecture can support deterministic traceability from Sensor_ID to Action_Status, with explicit failures for missing, invalid and ambiguous information. For the case model and its single registered version, the answer is a bounded yes. The identity rule (Model_Version_ID, BIM_GUID), with BIM_GUID taken from the IFC export, kept apart 16 elements whose stored identifiers were duplicated in the source model. On synthetic chain records anchored to nine real components, the traceability structure reconstructed every chain in both directions and rejected every designed mutation with its intended class. The first frozen validator passed 68 of 78 challenge cases, and the corrected validator passed all 78 on the same set. The study does not establish field performance, persistence of identity across model versions or any effect on maintenance decisions. The next test is a second registered version of the same model with measured evidence records.

**Author Contributions:** Conceptualization, [ ]; methodology, [ ]; software, [ ]; validation, [ ]; formal analysis, [ ]; investigation, [ ]; resources, [ ]; data curation, [ ]; writing—original draft preparation, [ ]; writing—review and editing, [ ]; visualization, [ ]; supervision, [ ]; project administration, [ ]. All authors have read and agreed to the published version of the manuscript.

**Funding:** [This research received no external funding / Funding statement.]

**Institutional Review Board Statement:** Not applicable.

**Informed Consent Statement:** Not applicable.

**Data Availability Statement:** The model-version registry, identity audit tables, schema, integrity rules, competency questions, fixtures and validator supporting this study are held by the authors. [Repository name, link and DOI to be added after deposit.]

**Acknowledgments:** [To be completed, including any generative-AI tool use described in Section 3.9.]

**Conflicts of Interest:** The authors declare no conflicts of interest.

**Abbreviations**

The following abbreviations are used in this manuscript:

| | |
|---|---|
| BIM | Building information modelling |
| CQ | Competency question |
| GUID | Globally unique identifier |
| IFC | Industry Foundation Classes |
| IoT | Internet of things |
| IR | Integrity rule |
| SHM | Structural health monitoring |


## References

1. Pärn, E.A.; Edwards, D.J.; Sing, M.C.P. The building information modelling trajectory in facilities management: A review. *Autom. Constr.* **2017**, *75*, 45–55. https://doi.org/10.1016/j.autcon.2016.12.003
2. Patacas, J.; Dawood, N.; Kassem, M. BIM for facilities management: A framework and a common data environment using open standards. *Autom. Constr.* **2020**, *120*, 103366. https://doi.org/10.1016/j.autcon.2020.103366
3. Bellon, F.G.; Martins, A.C.P.; de Carvalho, J.M.F.; de Souza, C.A.F.; Ribeiro, J.C.L.; César Júnior, K.M.L.; de Oliveira, D.S. IFC framework for inspection and maintenance representation in facility management. *Autom. Constr.* **2025**, *174*, 106157. https://doi.org/10.1016/j.autcon.2025.106157
4. Hagedorn, P.; Liu, L.; König, M.; Hajdin, R.; Blumenfeld, T.; Stöckner, M.; Billmaier, M.; Großauer, K.; Gavin, K. BIM-enabled infrastructure asset management using information containers and semantic web. *J. Comput. Civ. Eng.* **2023**, *37*, [article number]. https://doi.org/10.1061/(ASCE)CP.1943-5487.0001051
5. Kim, K.; Kim, H.; Kim, W.; Kim, C.; Kim, J.; Yu, J. Integration of IFC objects and facility management work information using Semantic Web. *Autom. Constr.* **2018**, *87*, 173–187. https://doi.org/10.1016/j.autcon.2017.12.019
6. Marmo, R.; Polverino, F.; Nicolella, M.; Tibaut, A. Building performance and maintenance information model based on IFC schema. *Autom. Constr.* **2020**, *118*, 103275. https://doi.org/10.1016/j.autcon.2020.103275
7. Delgado, J.M.D.; et al. Structural performance monitoring using a dynamic data-driven BIM environment. *J. Comput. Civ. Eng.* **2018**, *32*, [article number]. https://doi.org/10.1061/(ASCE)CP.1943-5487.0000749 [complete author list]
8. Chatsuwan, M.; Ichinose, M.; Alkhalaf, H. Enhancing facility management with a BIM and IoT integration tool and framework in an open standard environment. *Buildings* **2025**, *15*, 1928. https://doi.org/10.3390/buildings15111928
9. Ramonell, C.; Chacón, R.; Posada, H. Knowledge graph-based data integration system for digital twins of built assets. *Autom. Constr.* **2023**, *156*, 105109. https://doi.org/10.1016/j.autcon.2023.105109
10. Rogage, K.; et al. Data transfer between digital models of built assets and their operation & maintenance systems. *J. Inf. Technol. Constr.* **2020**, *25*, 469–481. https://doi.org/10.36680/j.itcon.2020.027 [complete author list]
11. Borkowski, A.S.; Jarema, P.; Kładź, M.; Smoliar, A. Temporally qualified building elements: A DOLCE-based ontology for phase-dependent identity and change tracking in BIM models. *Technologies* **2026**, *14*, 413. https://doi.org/10.3390/technologies14070413
12. Rico Thirion, M.A.; Moghtadernejad, S.; Xu, Y.; Lounis, Z.; Chen, Q. Digital twin platform based on an identity-semantic-interaction framework to improve bridge management workflows. *Digit. Eng.* **2026**, *11*, 100111. https://doi.org/10.1016/j.dte.2026.100111
13. Fang, Z.; Teng, X.; Shen, Z.; Yang, D.; Lin, X. Standardizing design-stage digital-twin assets in a smart home for building data management: Workflow design and validation based on IfcGUID compliance. *Buildings* **2025**, *15*, 4096. https://doi.org/10.3390/buildings15224096
14. Mariniello, G.; Gragnaniello, C.; Asprone, D. Enhancing structural health monitoring data management and damage detection in digital twins with blockchain and smart contracts. *Autom. Constr.* **2025**, *180*, 106558. https://doi.org/10.1016/j.autcon.2025.106558
15. García, J.A.; Toledo, I.; Aragonés, L.; Bañón, L. A CDE-centered quality gate framework to operationalize ISO 19650 governance in hybrid railway depots. *Appl. Sci.* **2026**, *16*, 2562. https://doi.org/10.3390/app16052562
16. Kochovski, P.; Fujs, D.; Vavpotič, D.; Chiachío, J.; Miri, P.; Stankovski, V. Leveraging IFC semantics and W3C decentralized identifiers for Digital Building Logbooks in construction and deep renovation. *Autom. Constr.* **2026**, *189*, 107065. https://doi.org/10.1016/j.autcon.2026.107065
17. Lorvão Antunes, A.; Barateiro, J.; Marecos, V.; Petrović, J.; Cardoso, E. Ontology-based BIM-AMS integration in European highways. *Intell. Syst. Appl.* **2024**, *22*, 200366. https://doi.org/10.1016/j.iswa.2024.200366
18. Shafie Panah, R.; Kioumarsi, M. Application of building information modelling (BIM) in the health monitoring and maintenance process: A systematic review. *Sensors* **2021**, *21*, 837. https://doi.org/10.3390/s21030837
19. Sadhu, A.; Peplinski, J.E.; Mohammadkhorasani, A.; Moreu, F. A review of data management and visualization techniques for structural health monitoring using BIM and virtual or augmented reality. *J. Struct. Eng.* **2023**, *149*, [article number]. https://doi.org/10.1061/(ASCE)ST.1943-541X.0003498
20. Theiler, M.; Smarsly, K. IFC Monitor—An IFC schema extension for modeling structural health monitoring systems. *Adv. Eng. Inform.* **2018**, *37*, 54–65. https://doi.org/10.1016/j.aei.2018.04.011
21. Hu, X.; Olgun, G.; Assaad, R.H. An intelligent BIM-enabled digital twin framework for real-time structural health monitoring using wireless IoT sensing, digital signal processing, and structural analysis. *Expert Syst. Appl.* **2024**, *252*, 124204. https://doi.org/10.1016/j.eswa.2024.124204
22. Gragnaniello, C.; Mariniello, G.; Pastore, T.; Asprone, D. BIM-based design and setup of structural health monitoring systems. *Autom. Constr.* **2024**, *158*, 105245. https://doi.org/10.1016/j.autcon.2023.105245
23. Lee, Y.-C.; Eastman, C.M.; Solihin, W. Logic for ensuring the data exchange integrity of building information models. *Autom. Constr.* **2018**, *85*, 249–262. https://doi.org/10.1016/j.autcon.2017.08.010
24. Lee, Y.-C.; Eastman, C.M.; Solihin, W. Rules and validation processes for interoperable BIM data exchange. *J. Comput. Des. Eng.* **2021**, *8*, 97–114. https://doi.org/10.1093/jcde/qwaa064
25. Shafiq, M.T.; Lockley, S.R. Application of signature-based matching for IFC model comparison. *Int. J. Constr. Manag.* **2022**, *22*, 1765–1774. https://doi.org/10.1080/15623599.2020.1742630
26. Wang, R.Y.; Strong, D.M. Beyond accuracy: What data quality means to data consumers. *J. Manag. Inf. Syst.* **1996**, *12*, 5–33. https://doi.org/10.1080/07421222.1996.11518099
27. Çelik, Y.; Petri, I.; Barati, M. Blockchain supported BIM data provenance for construction projects. *Comput. Ind.* **2023**, *144*, 103768. https://doi.org/10.1016/j.compind.2022.103768
28. Erri Pradeep, A.S.; Yiu, T.W.; Zou, Y.; Amor, R. Blockchain-aided information exchange records for design liability control and improved security. *Autom. Constr.* **2021**, *126*, 103667. https://doi.org/10.1016/j.autcon.2021.103667
29. Tavakoli, P.; Yitmen, I.; Sadri, H.; Taheri, A. Blockchain-based digital twin data provenance for predictive asset management in building facilities. *Smart Sustain. Built Environ.* **2024**, *13*, 4–21. https://doi.org/10.1108/SASBE-07-2023-0169
30. Ciccarese, P.; Soiland-Reyes, S.; Belhajjame, K.; Gray, A.J.G.; Goble, C.; Clark, T. PAV ontology: Provenance, authoring and versioning. *J. Biomed. Semant.* **2013**, *4*, 37. https://doi.org/10.1186/2041-1480-4-37
31. Sacks, R.; Kedar, A.; Borrmann, A.; Ma, L.; Brilakis, I.; Hüthwohl, P.; Daum, S.; Kattel, U.; Yosef, R.; Liebich, T.; et al. SeeBridge as next generation bridge inspection: Overview, information delivery manual and model view definition. *Autom. Constr.* **2018**, *90*, 134–145. https://doi.org/10.1016/j.autcon.2018.02.033
32. Wan, C.; Zhou, Z.; Li, S.; Ding, Y.; Xu, Z.; Yang, Z.; Xia, Y.; Yin, F. Development of a bridge management system based on the building information modeling technology. *Sustainability* **2019**, *11*, 4583. https://doi.org/10.3390/su11174583
33. Shalabi, F.; Turkan, Y. IFC BIM-based facility management approach to optimize data collection for corrective maintenance. *J. Perform. Constr. Facil.* **2017**, *31*, [article number]. https://doi.org/10.1061/(ASCE)CF.1943-5509.0000941
34. Liu, K.; El-Gohary, N. Bridge deterioration knowledge ontology for supporting bridge document analytics. *J. Constr. Eng. Manag.* **2022**, *148*, [article number]. https://doi.org/10.1061/(ASCE)CO.1943-7862.0002210
35. Matarneh, S.; Elghaish, F.; Pour Rahimian, F.; Dawood, N.; Edwards, D. Automated and interconnected facility management system: An open IFC cloud-based BIM solution. *Autom. Constr.* **2022**, *143*, 104569. https://doi.org/10.1016/j.autcon.2022.104569
36. Otranto, R.B.; Miceli Junior, G.; Pellanda, P.C. BIM-FM integration through openBIM: Solutions for interoperability towards efficient operations. *J. Inf. Technol. Constr.* **2025**, *30*, 298–318. https://doi.org/10.36680/j.itcon.2025.012
37. Godager, B.; et al. Exploring the Enterprise BIM concept in practice: The case of asset management in a Norwegian hospital. *J. Inf. Technol. Constr.* **2024**, *29*, 549–572. https://doi.org/10.36680/j.itcon.2024.025 [complete author list]
38. Chatsuwan, M.; et al. BIM–FM interoperability through open standards: A critical literature review. *Architecture* **2025**, *5*, 74. https://doi.org/10.3390/architecture5030074 [complete author list]
39. Monfardini, G.K.Q.; Salamon, J.S.; Barcellos, M.P. Use of competency questions in ontology engineering: A survey. In *Conceptual Modeling. ER 2023*; Lecture Notes in Computer Science; Springer: Cham, Switzerland, 2023; pp. 45–64. https://doi.org/10.1007/978-3-031-47262-6_3
40. Jia, Y.; Harman, M. An analysis and survey of the development of mutation testing. *IEEE Trans. Softw. Eng.* **2011**, *37*, 649–678. https://doi.org/10.1109/TSE.2010.62
41. Hevner, A.R.; March, S.T.; Park, J.; Ram, S. Design science in information systems research. *MIS Q.* **2004**, *28*, 75–106. https://doi.org/10.2307/25148625
