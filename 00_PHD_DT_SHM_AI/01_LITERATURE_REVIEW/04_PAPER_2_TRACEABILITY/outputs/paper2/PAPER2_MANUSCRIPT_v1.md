# Version-scoped component identity for traceable condition evidence, inspection and maintenance records: a BIM case with an observed identifier anomaly

Manuscript v1 · 2026-10-07 · RQ2 / WP2 · case P002 (25 m × 80 m steel portal-frame building).
Drafting order followed: Methods, Results, Limitations, Discussion, Related work, Introduction, Conclusion, Abstract. Sections are printed in journal order.
Evidence tags in square brackets ([E1], [E2], [E3]) mark objective source evidence, cross-source evidence and internal verification. They are for review and will be removed or converted to a table note before submission.

---

## Abstract

Inspection and maintenance records are increasingly attached to building information models, and monitoring data are attached to the same models through IFC GlobalIds. A maintenance action is accountable only if the evidence behind it can be traced to the component that was observed and to the model state that defined that component. Published work links sensors to components, inspections to components and inspections to maintenance actions, and it governs identifier quality, but in the ten closest studies these mechanisms are not combined into one component-level chain with explicit rejection of broken links. This paper asks whether a BIM-based identity rule scoped to a registered model version can support deterministic traceability from Sensor_ID through BIM_GUID, Condition_Evidence_ID and Inspection_Record_ID to Action_Status, with explicit failures for missing, invalid and ambiguous links. The rule takes the ordered pair (Model_Version_ID, BIM_GUID) as component identity, uses the exported IFC GlobalId rather than the stored Revit IfcGUID parameter, and requires duplicates to be reported, never silently repaired. It was applied to a hash-identified Revit model of a 25 m × 80 m steel industrial building with 759 structural elements. In that model, 8 stored IfcGUID values were shared by 16 elements, while all 747 exported GlobalIds were distinct; the rule kept the 16 elements distinguishable and rejected the shared stored value as a key. A six-entity schema with 14 integrity rules and 12 competency questions was then verified internally on synthetic chain records anchored to nine real component identities: 9/9 chains were reconstructed forward and in reverse and 145/145 mutated records were rejected with the intended failure class. On a 78-case challenge set the first frozen validator passed 68 cases; after correcting 8 validator defects and 2 specification gaps, the same set passed 78/78. These results are internal verification on one model version and one export, with synthetic downstream records. They show that the identity rule and the rejection logic work on a real model with a real anomaly; they do not show field performance or persistence of identity across model versions.

Keywords: building information modelling; IFC GlobalId; component identity; traceability; inspection and maintenance records; asset information management

---

## 1 Introduction

### 1.1 Inspection and maintenance information in BIM

Owners and asset managers now hold inspection findings and maintenance actions in BIM-linked structures. Bellon et al. (2025) represent inspections, damage, maintenance services and costs in IFC using real bridge inspection data. Hagedorn et al. (2022) route a bridge inspection finding to a repair order through linked information containers. Kim et al. (2018) link 590 maintenance work records to IFC objects. In these structures the component identifier is the join that lets an asset manager ask which evidence led to which action on which element.

### 1.2 Why a link to a component is not yet accountable evidence

Monitoring data enter the same structures through the same join. Chatsuwan et al. (2025) map indoor-environment sensors to IFC GlobalIds through a mapping table, and Ramonell et al. (2023) join IFC entities and IoT devices through shared GUIDs. Chatsuwan et al. (2025) also note that a GlobalId can be regenerated when an element is deleted and recreated, which breaks the sensor link without warning. A record that points to a GlobalId therefore carries an implicit assumption about which model state issued that GlobalId.

### 1.3 Identity, versions and provenance

Borkowski et al. (2026) show that the same physical element receives different GUIDs in independently created design, as-built and operation files, and propose a persistent identifier above the GUID. Fang et al. (2025) measure completeness, validity, uniqueness and stability of IfcGUIDs and register every check with hashes and operators. Mariniello et al. (2025) log the validation of monitoring data and the reactions to alerts on a ledger, and García et al. (2026) tie publish/hold decisions to a specific IFC revision and named roles. Each addresses one part of the question of whether a recorded action can be traced back to valid evidence about the right component.

### 1.4 What the literature already provides

Sensor-to-component binding, inspection-to-component linkage, inspection-to-action linkage, identifier quality checking, auditable data validation and competency-question verification are all reported (Section 2). This paper does not claim any of them.

### 1.5 Remaining gap

In the ten closest studies, read in full (Section 2.8), no study reports one component-level chain from sensor to action status in which (a) identity is scoped to a registered model version and fails closed under any other version, (b) explicit rules reject missing, invalid and ambiguous links at every hop, with deliberate invalid-data tests, and (c) the chain is exercised on a real model that contains an observed identifier anomaly. Lorvão Antunes et al. (2024) reach sensors and inspections without actions or rule validation; Bellon et al. (2025) reach inspections and maintenance without sensors or identity governance; Fang et al. (2025) govern identifiers without a downstream chain.

### 1.6 Research question

RQ2: Can a BIM-based, model-version-controlled identity architecture support deterministic traceability Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status, with explicit integrity failures for missing, invalid and ambiguous information?

### 1.7 Contributions

1. A version-scoped component-identity rule, (Model_Version_ID, BIM_GUID) with BIM_GUID = exported IFC GlobalId and detect-not-repair handling of stored-identifier duplicates, applied to a real model in which stored and exported identifiers diverge for 16 elements.
2. A component-level traceability structure from sensor to action status with forward and reverse reconstruction and 14 integrity rules that separate missing, invalid and ambiguous links, verified internally on synthetic records anchored to real component identities.
3. A verification record that reports the first frozen run (68/78) separately from the corrective run on the same challenge set (78/78) and classifies every first-run failure.

---

## 2 Related work

### 2.1 Monitoring data linked to BIM

IFC Monitor extends the IFC schema to describe structural health monitoring systems (Theiler and Smarsly, 2018). Gragnaniello et al. (2024) check SHM information requirements in a viaduct model with IDS. Chatsuwan et al. (2025) and Ramonell et al. (2023) bind live sensor streams to IFC entities through GlobalIds or shared GUIDs. Lorvão Antunes et al. (2024) model sensors as hosted by structures using the SSN ontology and link physical objects to ifcElement GUIDs in three road-authority pilots. Binding a sensor to a component is established.

### 2.2 BIM/IFC component identity

Lee et al. (2020) derive GUID uniqueness, format and round-trip rules for two model view definitions. Fang et al. (2025) treat the 22-character IfcGUID as a cross-system primary key and measure four quality indicators over 820 objects in a virtual smart-home project, with stability defined as identical GlobalIds in two exports made under identical settings. Shafiq and Lockley (2020) report GUID inconsistencies after modelling operations and match objects by attribute signatures instead. None of these studies distinguishes the GUID stored as a Revit parameter from the GlobalId written at export, which is the distinction that matters in Section 6.3.

### 2.3 Model versioning and identity persistence

Borkowski et al. (2026) give each element a GUID-independent URI and attach a phase-specific GUID as a backlink; cross-file matching is manual, and the authors state the ontology is not designed for continuous monitoring. Fang et al. (2025) test GlobalId stability between two exports. Persistence of identity across versions is therefore addressed in the literature. The present study does not claim persistence. It claims a narrower property: a GlobalId held in a downstream record is valid only together with the model version that issued it.

### 2.4 Provenance and asset-information governance

Mariniello et al. (2025) use smart contracts to validate monitoring data, authenticate damage-detection tools and log reactions on a real viaduct; component identity binding is not reported. Çelik et al. (2023) record object version and responsibility for BIM objects on a blockchain, and Tavakoli et al. (2023) propose a digital-twin data provenance model for predictive asset management. García et al. (2026) attach publish/hold decision records to IFC revisions and roles across 22 real deliverables. The PAV vocabulary separates authoring, provenance and versioning roles in a domain-neutral form (Ciccarese et al., 2013). Provenance of records is established; provenance of the component reference inside those records is less developed.

### 2.5 Inspection and maintenance information linkage

Bellon et al. (2025) represent inspections as IfcTask, damage as IfcSurfaceFeature and the inspector as IfcActor, and link damage to maintenance services and cost items. Hagedorn et al. (2022) and Wan et al. (2019) connect inspection findings to repair activities in bridge management. Kim et al. (2018) link maintenance work records to IFC objects. None of these studies starts from sensor-derived evidence.

### 2.6 Forward and reverse traceability

Kim et al. (2018) retrieve work records by component and across components that share objects. Lorvão Antunes et al. (2024) answer competency questions such as "what are the results of a certain inspection by element". These are forward or single-hop queries; reconstruction from an action back to the originating sensor across four record types is not reported in the studies reviewed.

### 2.7 Integrity verification and competency questions

Competency questions are a standard device for scoping and verifying ontologies (Monfardini et al., 2023) and are used by Lorvão Antunes et al. (2024) and Borkowski et al. (2026). Rule-based checking of BIM data is established (Lee et al., 2020; Fang et al., 2025; García et al., 2026). Deliberate invalid-data testing appears in limited forms: a pre-test/post-test design (Fang et al., 2025) and one schema-level inconsistency test (Borkowski et al., 2026).

### 2.8 Positioning

Table 1 compares the ten Tier-A studies against the eight capabilities of the present design. Seven capabilities are reported individually; four studies cover three or more; none covers the version-scoped chain with rejection rules and invalid-data tests on a real model. The search behind Table 1 was targeted (about 139 unique records from Consensus, Zotero and OpenAlex, 2026-10-07), not systematic.

Table 1. Tier-A positioning (YES / PARTIAL / NO / NOT_REPORTED). Source: `PAPER2_LITERATURE_POSITIONING_FINAL.csv`.

| Study | Sensor–BIM | Version | Inspection | Action | Reverse trace | Rules | CQs | Invalid-data tests | Real data |
|---|---|---|---|---|---|---|---|---|---|
| Borkowski et al. 2026 | NO | YES | PARTIAL | NO | PARTIAL | PARTIAL | YES | PARTIAL | PARTIAL |
| Fang et al. 2025 | PARTIAL | YES | NO | NO | NOT_REPORTED | YES | NO | PARTIAL | NO |
| Lorvão Antunes et al. 2024 | YES | NO | YES | NO | PARTIAL | NO | YES | NO | YES |
| Mariniello et al. 2025 | PARTIAL | NOT_REPORTED | PARTIAL | PARTIAL | NOT_REPORTED | YES | NO | PARTIAL | YES |
| García et al. 2026 | NO | YES | NO | NO | NOT_REPORTED | YES | NO | PARTIAL | YES |
| Bellon et al. 2025 | NO | NOT_REPORTED | YES | YES | NOT_REPORTED | PARTIAL | NO | NO | YES |
| Kim et al. 2018 | NO | NO | PARTIAL | YES | YES | NO | NO | NO | YES |
| Hagedorn et al. 2022 | PARTIAL | NOT_REPORTED | YES | YES | NOT_REPORTED | PARTIAL | NO | NO | YES |
| Chatsuwan et al. 2025 | YES | NO | NO | PARTIAL | NOT_REPORTED | NO | NO | NO | YES |
| Ramonell et al. 2023 | YES | NOT_REPORTED | PARTIAL | PARTIAL | NOT_REPORTED | NO | NO | NO | PARTIAL |
| This study | YES (synthetic) | YES | YES (synthetic) | YES (synthetic) | YES | YES | YES | YES | identities and anomaly real; chain records synthetic |

---

## 3 Research method

### 3.1 Scope

The study tests information traceability only. It does not diagnose structural condition, calibrate a structural model or evaluate maintenance outcomes. Condition evidence is treated as a record type with an identifier, a status and a validity window; how the evidence is computed is outside scope.

### 3.2 Case

The case is P002, a single-storey steel portal-frame industrial building with nominal plan dimensions of 25 m × 80 m, grids 1–9 and A–B, column top at 6.300 m and ridge at 9.300 m [E1]. The building has a Revit model, an IFC export and as-built drawings in PDF. P002 was chosen because all three sources were available for the same building and because the model was under the research team's control, so its state could be frozen and hashed.

### 3.3 Source hierarchy

Four sources were assigned roles before any identity analysis. The Revit file `P002_KCNX_80m_v4_APPLY_TARGET.rvt` was designated the working BIM reference after live verification; it is not claimed to be an exact as-built model. The IFC file exported from it was designated a derived exchange model. The as-built PDF was designated the physical as-built reference. A second Revit file in the project folder, whose relationship to the working reference could not be established from file metadata, was left unresolved and not used [E1].

### 3.4 Model-version registration

The working reference was opened in Revit 2027 (build 27.3.0.28) and read through a read-only bridge. The live document path, a SHA-256 hash of the saved file (47748cbeb460229e…), the file size (37 564 416 B) and Document_Modified = FALSE were recorded [E1]. The version identifier MV-RVT-20261005-47748cbe was then registered by the researcher as a provenance event with the hash, build, IFC file name and hash and known limitations. Registration is a human decision; a newer timestamp does not make a file authoritative.

### 3.5 Identity-governance method

Every scoped element was read live (ElementId, UniqueId, stored IfcGUID parameter, category, family, type, level). The IFC export was parsed with IfcOpenShell 0.8.5 and joined to the live inventory on Revit id = IFC Tag. For each element the stored IfcGUID and the exported GlobalId were compared. Identity was then defined as follows: BIM_GUID is the exported IFC GlobalId; component identity is the ordered pair (Model_Version_ID, BIM_GUID), not a concatenated string; UniqueId, ElementId and the stored IfcGUID are supporting evidence only. A duplicate stored IfcGUID is an integrity anomaly to be detected and reported; it is never repaired or regenerated in the source model. Location is derived by a separate locator rule (native level, then IFC spatial containment, then labelled geometry) and is not part of identity.

### 3.6 Traceability schema

Six entities were defined: Model_Version, BIM_Component, Sensor, Condition_Evidence, Inspection_Record and Action_Status_Record (Table 2). Action level (NORMAL, WATCH, INSPECT, PRIORITY_INSPECTION) and action workflow status (nine states from proposed to reopened) are separate controlled vocabularies; neither encodes a maintenance decision rule. Asset_ID is optional because no element carried one.

Table 2. Identifier roles.

| Identifier | Role | Source in P002 |
|---|---|---|
| Model_Version_ID | Scopes every component reference | Registered (real) |
| BIM_GUID | Exported IFC GlobalId; key together with Model_Version_ID | Real |
| Revit_UniqueId | Supporting; detects ambiguous identity | Real |
| Stored_IfcGUID | Supporting; not authoritative | Real |
| Sensor_ID | Sensor placement | Synthetic |
| Condition_Evidence_ID | Evidence record; references one sensor and one component | Synthetic |
| Inspection_Record_ID | References the evidence used | Synthetic |
| Action_ID / Action_Status | References the inspection; level + workflow status | Synthetic |

### 3.7 Integrity rules

Fourteen rules (IR-01 to IR-14) were written before any test fixture was generated and frozen with a hash (Table 4). They cover existence of each identifier, one-to-one sensor binding within the declared version, existence of BIM_GUID in the registered version, evaluation of identity as an ordered pair, handling of duplicate stored identifiers, uniqueness of evidence identifiers, consistency of the evidence with the chain's sensor and component, evidence status and validity window at inspection time, inspection-to-evidence and action-to-inspection references, controlled vocabularies, version mismatch, required provenance, and refusal to resolve ambiguous identity silently. Rules are evaluated in a fixed order; the reported failure class is that of the first failing rule. No score or index is computed.

Table 4. Integrity rules (abridged).

| Rule | Condition | Failure class |
|---|---|---|
| IR-01 | Sensor_ID present and registered | MISSING_IDENTIFIER / UNKNOWN_SENSOR |
| IR-02 | Sensor maps to exactly one active component in the declared version | SENSOR_BINDING_MISMATCH |
| IR-03 | BIM_GUID exists in the registered version | MISSING_IDENTIFIER / UNKNOWN_BIM_GUID |
| IR-04 | Identity evaluated as (Model_Version_ID, BIM_GUID) | MODEL_VERSION_MISMATCH / UNKNOWN_BIM_GUID |
| IR-05 | Duplicate stored IfcGUID reported, never used as BIM_GUID | AMBIGUOUS_IDENTITY / anomaly flag |
| IR-06 | Condition_Evidence_ID unique | DUPLICATE_EVIDENCE_ID |
| IR-07 | Evidence references the chain's sensor and component | BROKEN_EVIDENCE_LINK |
| IR-08 | Evidence status and validity usable at inspection date | INVALID_EVIDENCE |
| IR-09 | Inspection references the evidence | BROKEN_INSPECTION_LINK |
| IR-10 | Action level and status from controlled vocabularies | INVALID_ACTION_STATUS |
| IR-11 | Action references the inspection | BROKEN_ACTION_LINK |
| IR-12 | Unregistered or wrong version fails lookup | MODEL_VERSION_MISMATCH |
| IR-13 | Required identity and provenance fields present | MISSING_IDENTIFIER / PROVENANCE_MISSING |
| IR-14 | No silent resolution of multiple values or BIM_GUID/UniqueId disagreement | AMBIGUOUS_IDENTITY |

### 3.8 Competency questions

Twelve competency questions (CQ01–CQ12) were frozen before validation (Table 5). Each has an input, an expected output, the entities and rules involved, and a pass criterion. CQ01–CQ09 ask chain questions (which component a sensor is linked to, under which version, which inspection used an evidence record, which action resulted, who recorded it, whether the chain can be reconstructed from the action back to the sensor). CQ10–CQ12 ask whether a wrong version is rejected, whether missing, duplicate and invalid identifiers fail explicitly, and whether missing, invalid and ambiguous information fall into disjoint failure-class groups.

### 3.9 Positive and negative verification

Nine positive fixtures were built on real component identities from the registered model: primary columns, a primary rafter and a ridge rafter, a gable column and gable rafter, a placeholder brace, and both elements of one real duplicate pair (RD-001). All sensor, evidence, inspection and action records attached to them were synthetic and labelled as such. Seventeen deterministic mutation classes (NEG01–NEG17) were applied to the positives to generate 145 negative fixtures with 13 intended failure classes; the fixtures were hashed before validation and re-checked unchanged afterwards. A rejection counted as a pass only if it was a controlled failure with the intended class; a crash did not count.

### 3.10 Challenge procedure

A second set of 78 challenge cases (19 expected accept, 59 expected reject; 8 multi-fault cases with up to three simultaneous faults; all 8 real duplicate pairs in three variants each) was written and frozen after the first validation and run once against the unchanged, hash-frozen validator. The author of the challenge set had not seen validator outputs for these cases but had written the validator; we classify this as internal, Level C independence. Every first-run failure was classified as a validator defect or a specification gap. Defects were then corrected in a new validator version, and the same 78 cases and the original 154 fixtures were re-run. An intermediate corrected attempt whose output files were deleted before the final run is excluded from the evidence.

### 3.11 Evidence-independence classification

Every result is labelled E1 (objective observation of source data), E2 (comparison across independent sources) or E3 (internal verification of the authors' own specification and code). E3 results are reported as internal verification and are not used to establish novelty.

---

## 4 Traceability architecture

### 4.1 Entities

The six entities form a chain in which each record holds the identifier of the record it depends on (Figure 3). The evidence record stores its own copy of the sensor and component reference, and the inspection and action records store the identifier of the upstream record, so that a broken reference is visible in the record itself rather than inferred.

### 4.2 Identifier roles

Table 2 separates the key (Model_Version_ID with BIM_GUID) from supporting identifiers. The stored IfcGUID is retained because its disagreement with the exported GlobalId is evidence; it is never the key.

### 4.3 The pair (Model_Version_ID, BIM_GUID)

A BIM_GUID is resolved only within the version named in the same record. If the version is not registered, the lookup fails with MODEL_VERSION_MISMATCH even when the same GlobalId exists in the registered version (Figure 2). This makes a reference to a superseded or unknown model state visible. It does not tell the user which element in a new version corresponds to the old one; that requires a persistence mechanism of the kind proposed by Borkowski et al. (2026).

### 4.4 Sensor to component

A sensor is bound to exactly one active component within the declared version (IR-02). The schema does not constrain how many sensors a component may carry.

### 4.5 Evidence to inspection

An inspection record names the evidence record it used. The evidence must have a known status and a validity window covering the inspection date (IR-08); expired or invalid evidence fails.

### 4.6 Inspection to action

An action record names the inspection; its level and workflow status come from controlled vocabularies (IR-10, IR-11).

### 4.7 Forward traceability

From a Sensor_ID, the component, evidence, inspection and action are resolved in sequence (Figure 5).

### 4.8 Reverse traceability

From an Action_ID, the inspection, evidence, component and sensor are resolved backwards; the result must equal the forward chain (CQ09).

### 4.9 Invalid and ambiguous data

Missing values (empty identifiers, missing provenance), invalid values (unknown identifiers, wrong version, expired evidence, out-of-vocabulary status) and ambiguous values (multiple components in one field, a shared stored IfcGUID used as key, GlobalId/UniqueId disagreement) map to disjoint failure-class groups (CQ12).

---

## 5 Case implementation

### 5.1 BIM source

The working reference was verified live on 2026-10-06: the open document was the registered file, unmodified, with the registered hash [E1]. A targeted comparison of 16 items against the as-built drawings found 3 matches, 4 functionally equivalent names, 4 mismatches and 5 items that could not be checked [E2]; the model is therefore treated as a working reference, not as an as-built model.

### 5.2 Revit and IFC inventory

The live model held 759 elements in the scoped categories: 625 structural framing, 62 structural columns, 26 structural foundations, 45 generic models and 1 floor, with 759 distinct ElementIds and UniqueIds [E1]. No element carried an Asset_ID or other asset shared parameter (0/759) [E1]. The eight brace objects were generic-model placeholders without material or section; structural framing had no native level in all 18 elements sampled [E1].

### 5.3 Model-version registration

One version, MV-RVT-20261005-47748cbe, was registered. The IFC header recorded the same save count (43) as the file metadata [E2].

### 5.4 Objective identifier anomalies

The anomalies reported in Section 6 were found in the source data. They were not injected.

### 5.5 Traceability records

Nine chains were instantiated, one per positive fixture, each with one synthetic sensor, evidence, inspection and action record (Section 3.9).

### 5.6 Synthetic and internal test-data boundary

Every record downstream of BIM_Component is synthetic. The real parts of each chain are the model version, the component identities and the duplicate-pair anomaly. Results in Sections 6.4–6.9 therefore show that the logic works on real identities; they say nothing about real sensors, real inspections or maintenance outcomes.

---

## 6 Results

### 6.1 Objective BIM/IFC observations

Of the 759 scoped elements, 747 were present in the IFC export and 12 opening objects were not [E2]. For the 747 exported elements, the stored IfcGUID equalled the exported GlobalId for 739 and differed for 8. Classified for identity integrity, 731 elements passed, 16 were conditional (both members of each duplicate pair) and 12 were unresolved (not exported); none failed (Table 3).

Table 3. Objective identity observations, model MV-RVT-20261005-47748cbe.

| Observation | Count | Class |
|---|---|---|
| Scoped live elements | 759 | E1 |
| Distinct ElementIds / UniqueIds | 759 / 759 | E1 |
| Elements in IFC export | 747 | E2 |
| Stored IfcGUID = exported GlobalId | 739 | E2 |
| Stored IfcGUID ≠ exported GlobalId | 8 | E2 |
| Not exported (openings, no BIM_GUID) | 12 | E2 |
| Duplicate stored IfcGUID values | 8 (16 elements) | E1 |
| Distinct exported GlobalIds among exported elements | 747 / 747 | E2 |
| Elements with Asset_ID | 0 | E1 |

### 6.2 Model-version and identity findings

Comparison of the live model, the IFC export and an inventory produced earlier from the same project found 739 elements consistent across all three, 20 partially consistent (8 re-identified at export, 12 not exported) and none inconsistent; all 232 elements present in the earlier inventory had identical identifiers [E2]. Internally, a chain referencing a valid BIM_GUID under an unregistered version was rejected with MODEL_VERSION_MISMATCH for all 9 positives [E3].

### 6.3 Real duplicate-identifier case

Eight stored IfcGUID values were each shared by two elements with distinct UniqueIds (RD-001 to RD-008); the duplication was reproduced in the live model [E1]. In the IFC export, the second element of each pair received a new GlobalId, so the 16 elements had 16 distinct GlobalIds [E2]. Using the stored parameter as the component key would have merged eight pairs of physically distinct members; using the exported GlobalId kept them apart (Figure 6). The cause of the duplication was not established, and no parameter was edited.

Under the identity rule, both elements of every pair were accepted through their exported GlobalId with an anomaly flag, and a chain that used the shared stored value as BIM_GUID was rejected as AMBIGUOUS_IDENTITY; this held for 8/8 pairs [E3].

### 6.4 Forward traceability

For all 9 positive chains, Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status resolved to the registered records [E3].

### 6.5 Reverse traceability

For all 9 positive chains, the reverse reconstruction from the action record returned the same five identifiers as the forward chain; a mutated chain with a broken action-to-inspection reference was rejected as BROKEN_ACTION_LINK [E3].

### 6.6 Internal positive and negative verification

All 9 positives were accepted; 3 carried the expected flags (one component-metadata gap for the placeholder brace, two duplicate-stored-identifier flags for RD-001). All 145 negatives were rejected with the intended failure class; 13 rules acted as the deciding rule at least once, and IR-04 acted as the lookup key in every test. No crash occurred (Table 6) [E3]. The negative set was generated by the authors of the rules and the validator.

### 6.7 First-run challenge failures

On the 78-case challenge set, the frozen first validator passed 68 cases, failed 10 and crashed on none [E3]. Eight failures were validator defects: registry-level duplicates not detected (three cases), schema-required fields not enforced (three), and anomaly flags not visible on rejected records (two). Two were specification gaps: whether identifiers must match exactly (one case) and whether dates must follow ISO 8601 (one) (Table 7). In 7 of the 8 multi-fault cases the first validator reported the failure class of the earliest failing rule; the remaining case missed an anomaly flag, not a class. All 8 real duplicate pairs behaved as specified on the first run.

Table 7. Challenge results.

| Run | Validator | Set | Pass | Fail | Status |
|---|---|---|---|---|---|
| First frozen run | v1 (hash-frozen) | 78 cases | 68 | 10 | Formal evidence |
| Intermediate attempt | v2 draft | 78 cases | (76 reported) | — | Not evidence; outputs deleted |
| Corrective run | v2 | same 78 cases | 78 | 0 | Corrective verification |
| Regression | v2 | 154 Gate 3 fixtures | 154 | 0 | No per-fixture difference |
| Consistency patch | v2.1 | 78 + 154 | 0 differences | — | No regression |

### 6.8 Corrective verification

After the eight defects were corrected and the two specification gaps resolved by researcher decision (exact matching with trimming of leading and trailing whitespace for required text fields; ISO 8601 for dates), the new validator passed the same 78 cases and reproduced all 154 earlier outcomes without per-fixture difference [E3]. This is corrective verification on a set the corrections were designed against; it is not fresh evidence of robustness.

### 6.9 Competency-question results

All 121 CQ checks passed: 10 each for CQ01–CQ10, 8 for CQ11 and 13 for CQ12 [E3]. Missing, invalid and ambiguous cases fell into disjoint failure-class groups (CQ12).

### 6.10 Evidence boundary

Table 8 separates the evidence classes. The observations in Sections 6.1–6.3 (first two paragraphs) are E1/E2 and would stand without any test. Sections 6.4–6.9 are E3.

Table 8. Claim, evidence and independence.

| Claim | Evidence | Class | Independence |
|---|---|---|---|
| Stored and exported identifiers diverge for 16 elements | Live model vs IFC | E1/E2 | Tool outputs, not author content |
| Exported GlobalIds separate the 16 elements in this export | IFC parse | E2 | As above |
| Version-scoped lookup rejects unregistered versions | 9/9 | E3 | Same author |
| Chain reconstructs forward and in reverse | 9/9 + 9/9 | E3 | Synthetic records |
| Rules reject designed mutations | 145/145 | E3 | Same author |
| First validator had defects | 68/78 | E3 | Level C |
| Corrections hold on the same set | 78/78 | E3 | Same set reused |

---

## 7 Discussion

### 7.1 What the objective P002 evidence demonstrates

The P002 model contains a concrete case in which the identifier a user would read from the Revit element (the stored IfcGUID parameter) is not the identifier the exchange file carries (the exported GlobalId), and in which the stored value is shared by two elements eight times. A sensor mapping built from the stored parameter would have bound one sensor reference to two physical members without any warning. This is a source-data observation, independent of the authors' code. It shows that the choice of which identifier is the key has consequences in a working model, and that the choice must be recorded with the model state.

### 7.2 What is only internally verified

The rejection behaviour, the reconstruction in both directions and the competency-question answers were checked by the authors on records the authors wrote. The first-run result (68/78) shows that the authors' own validator was incomplete when first exposed to cases it had not been tuned on; the corrective result (78/78) shows only that the exposed defects were fixed.

### 7.3 Comparison with Tier-A studies

Lorvão Antunes et al. (2024) go further than this study on real data: three national pilots, real sensors and real inspection campaigns. They do not carry the chain to actions and state that rule-based validation was not addressed. Bellon et al. (2025) represent inspection, damage, maintenance and cost in IFC with real inspection data, but start from visual inspection, not sensor evidence, and validate schema conformance rather than rejecting broken references. Borkowski et al. (2026) solve a harder identity problem, persistence across versions, but with manual matching and no downstream records. Fang et al. (2025) measure GlobalId stability across two exports, which this study did not do, and they repair the mapping layer, which this study forbids for the source model. Mariniello et al. (2025) and García et al. (2026) apply deterministic gates to real data, but at the level of data streams and deliverables rather than component references. The present study's difference is the combination: one component reference scoped to a model version and checked at every hop from sensor to action, on a model with an observed anomaly.

### 7.4 Scientific contribution

The first contribution is the version-scoped identity rule together with the observation that motivates it. The second is the traceability structure with rejection rules; its novelty is argued from the literature in Section 2, and its function is shown by internal verification. The third is a reporting practice: publishing the first-run failure rate of one's own checker and keeping corrective runs separate.

### 7.5 Construction-management contribution

For an asset manager, the question is whether an action recorded against a component can be defended later: which evidence triggered it, which inspection used that evidence, and whether that evidence referred to the same element in the same model state. The design turns these into queries with yes/no answers and named failure classes. It moves part of asset-information governance (who recorded what, against which model version) from procedure into checkable records, in the spirit of revision-linked decision records at deliverable level (García et al., 2026), but at component level.

### 7.6 Practical implications

Three practices follow from the case and require no new software. Record the model version with every component reference held outside the model. Take the identifier from the exchange file, not from an authoring-tool parameter, and keep the parameter as evidence. Treat identifier duplicates as reportable anomalies rather than repairing them silently, because the repair erases the evidence that the earlier references may be wrong.

### 7.7 Interpretation boundary

The results do not show that the exported GlobalId is stable across re-exports, that the rule scales to many versions, that the rules are complete, or that the structure improves inspection or maintenance decisions.

### 7.8 Link to field feasibility

The next test is a second registered version of the same model, re-exported, so that GlobalId persistence and version-mismatch handling can be observed on real data, followed by field-acquired sensor and inspection records in place of the synthetic ones.

---

## 8 Limitations

1. One building (P002) and one Revit model; no cross-project generalisation.
2. One registered model version and one IFC export; persistence of GlobalIds across re-exports or edits was not tested.
3. The model is a working reference; reconciliation with the as-built drawings was a 16-item sample with 4 mismatches and 5 uncheckable items.
4. All sensor, condition-evidence, inspection and action records are synthetic; nine of 759 components carry chains.
5. Rules, mutation generator, challenge set and validator were written by the same author; the challenge set is Level C (blind to outputs, not to code).
6. The corrective 78/78 run reused the challenge set it was corrected against.
7. No external or independent validation and no field validation were performed.
8. Component-to-sensor cardinality is not constrained; identical repeated sensor rows were not tested.
9. The cause of the eight stored-identifier duplicates is not known.
10. Twelve opening objects have no BIM_GUID because they were not exported.
11. The output files of one intermediate validator attempt were deleted; that attempt is excluded from evidence.

---

## 9 Conclusion

RQ2 asked whether a model-version-controlled identity architecture can support deterministic traceability from Sensor_ID to Action_Status with explicit failures for missing, invalid and ambiguous information. For the P002 model and its single registered version, the answer is a bounded yes. The identity rule (Model_Version_ID, BIM_GUID), with BIM_GUID taken from the IFC export, kept 16 elements distinguishable whose stored identifiers were duplicated in the source model. On synthetic chain records anchored to nine real components, the structure reconstructed every chain in both directions and rejected every designed mutation with its intended class; the first frozen validator passed 68 of 78 challenge cases and the corrected validator passed all 78 on the same set. The study does not establish field performance, persistence of identity across model versions, or any effect on maintenance decisions.

---

## References

(Reference style to be converted to the target journal. DOIs verified against OpenAlex or the publisher PDF on 2026-10-07.)

Bellon, F.G., Martins, A.C.P., de Carvalho, J.M.F., de Souza, C.A.F., Ribeiro, J.C.L., César Júnior, K.M.L., de Oliveira, D.S., 2025. IFC framework for inspection and maintenance representation in facility management. Automation in Construction 174, 106157. https://doi.org/10.1016/j.autcon.2025.106157

Borkowski, A., Jarema, M., Kładź, M., Smoliar, A., 2026. Temporally qualified building elements: a DOLCE-based ontology for phase-dependent identity and change tracking in BIM models. Technologies 14(7), 413. https://doi.org/10.3390/technologies14070413

Çelik, Y., Petri, I., Barati, M., 2023. Blockchain supported BIM data provenance for construction projects. Computers in Industry. https://doi.org/10.1016/j.compind.2022.103768

Chatsuwan, M., Ichinose, M., Alkhalaf, H., 2025. Enhancing facility management with a BIM and IoT integration tool and framework in an open standard environment. Buildings 15, 1928. https://doi.org/10.3390/buildings15111928

Ciccarese, P., Soiland-Reyes, S., Belhajjame, K., Gray, A.J.G., Goble, C., Clark, T., 2013. PAV ontology: provenance, authoring and versioning. Journal of Biomedical Semantics 4, 37. https://doi.org/10.1186/2041-1480-4-37

Fang, Z., Teng, X., Shen, Z., Yang, D., Lin, X., 2025. Standardizing design-stage digital-twin assets in a smart home for building data management: workflow design and validation based on IfcGUID compliance. Buildings 15, 4096. https://doi.org/10.3390/buildings15224096

García, J.A., et al., 2026. A CDE-centered quality gate framework to operationalize ISO 19650 governance in hybrid railway depots. Applied Sciences 16, 2562. https://doi.org/10.3390/app16052562

Gragnaniello, C., et al., 2024. BIM-based design and setup of structural health monitoring systems. Automation in Construction 158, 105245. https://doi.org/10.1016/j.autcon.2023.105245

Hagedorn, P., Liu, L., König, M., Hajdin, R., Blumenfeld, T., Stöckner, M., Billmaier, M., Großauer, K., et al., 2022. BIM-enabled infrastructure asset management using information containers and semantic web. Journal of Computing in Civil Engineering. https://doi.org/10.1061/(ASCE)CP.1943-5487.0001051

Kim, K., Kim, H., Kim, W., Kim, C., Kim, J., Yu, J., 2018. Integration of IFC objects and facility management work information using Semantic Web. Automation in Construction. https://doi.org/10.1016/j.autcon.2017.12.019

Lee, Y.-C., et al., 2020. Rules and validation processes for interoperable BIM data exchange. Journal of Computational Design and Engineering. https://doi.org/10.1093/jcde/qwaa064

Lorvão Antunes, A., Barateiro, J., Marecos, V., Petrović, J., Cardoso, E., 2024. Ontology-based BIM-AMS integration in European highways. Intelligent Systems with Applications 22, 200366. https://doi.org/10.1016/j.iswa.2024.200366

Mariniello, G., et al., 2025. Enhancing structural health monitoring data management and damage detection in digital twins with blockchain and smart contracts. Automation in Construction 180, 106558. https://doi.org/10.1016/j.autcon.2025.106558

Monfardini, G.K.Q., Salamon, J.S., Barcellos, M.P., 2023. Use of competency questions in ontology engineering: a survey. In: Conceptual Modeling (ER 2023). https://doi.org/10.1007/978-3-031-47262-6_3

Ramonell, C., Chacón, R., Posada, H., 2023. Knowledge graph-based data integration system for digital twins of built assets. Automation in Construction 156, 105109. https://doi.org/10.1016/j.autcon.2023.105109

Shafiq, M.T., Lockley, S.R., 2020. Application of signature-based matching for IFC model comparison. International Journal of Construction Management. https://doi.org/10.1080/15623599.2020.1742630

Tavakoli, P., Yitmen, I., Sadri, H., Taheri, A., 2023. Blockchain-based digital twin data provenance for predictive asset management in building facilities. Smart and Sustainable Built Environment. https://doi.org/10.1108/SASBE-07-2023-0169

Theiler, M., Smarsly, K., 2018. IFC Monitor: an IFC schema extension for modeling structural health monitoring systems. Advanced Engineering Informatics. https://doi.org/10.1016/j.aei.2018.04.011

Wan, C., Zhou, Z., Li, S., Ding, Y., Xu, Z., Yang, Z., Xia, Y., Yin, F., 2019. Development of a bridge management system based on the building information modeling technology. Sustainability 11, 4583. https://doi.org/10.3390/su11174583

No internal report, ADR, manifest or unpublished paper by the authors is cited. Study data and code will be cited only after a public repository exists.

---

## Draft notes for authors (remove before submission)

- Result CSVs for Gate 3 and the challenge runs (`outputs/gate3/…`, `outputs/wp2_final/…`) are not on this workstation; the numbers in Sections 6.2–6.9 were checked against the append-only evidence log (EV-RQ2-031…042), the Gate 3 closure report and the robustness assessment, and fixture counts were re-counted from the frozen fixture CSVs. Re-check against the result CSVs before submission.
- Missing bibliographic details (volume/pages) for Çelik 2023, Hagedorn 2022, Kim 2018, Lee 2020, Shafiq & Lockley 2020, Tavakoli 2023, Theiler & Smarsly 2018 must be completed from the publisher record.
- Figures F1–F7 are planned, not drawn.
