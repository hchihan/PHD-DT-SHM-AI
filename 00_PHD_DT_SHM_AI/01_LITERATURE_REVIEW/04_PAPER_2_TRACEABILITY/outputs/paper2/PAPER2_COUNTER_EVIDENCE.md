# PAPER2_COUNTER_EVIDENCE

Paper 2 · RQ2 / WP2 · P002 25×80 m · prepared 2026-10-07.
Purpose: record the external studies that already achieve parts of the candidate Paper-2 contribution, and downgrade every candidate claim they cover. All ten Tier-A papers were read in full text (PDF text extracted from the Zotero storage on 2026-10-07; method, results, validation and limitation sections read). Evidence levels are in `PAPER2_LITERATURE_POSITIONING_FINAL.csv`.

Falsification query used: does any study combine model-version-qualified BIM identity + sensor/evidence linkage + inspection records + action records + forward and reverse traceability + integrity rules + competency questions + invalid-data testing? Answer from the screened corpus (about 139 unique records, 10 Tier-A full texts): no single study reports all eight. Seven of the eight are reported individually, and four studies cover three or more. The combination is the only defensible gap.

## 1 Borkowski et al. (2026), Technologies 14(7):413

- **Already achieved.** States that IFC GUIDs differ when the same physical element is exported from independently created phase files; mints a persistent, GUID-independent element URI and keeps the per-phase GUID as a `hasIFCGuid` backlink; verifies the ontology with 8 competency questions and a reasoner.
- **Overlap.** Identity across model versions (Candidate A); CQ verification (Candidate D); one deliberate inconsistency test (Candidate E, schema level).
- **Invalidates.** Any claim that Paper 2 solves identity persistence across versions. Borkowski addresses persistence directly; Paper 2 does not. The pair (Model_Version_ID, BIM_GUID) scopes an identifier to one registered version and rejects it under any other; it does not link the same physical element across versions. Candidate A is downgraded from CORE to SUPPORTING.
- **Remains different.** Borkowski matches elements across files manually, has no sensor, evidence, inspection or action records, and states the ontology is not adequate for continuous monitoring. Paper 2 tests rejection of identifiers that arrive with the wrong version inside a sensor-to-action chain.

## 2 Fang et al. (2025), Buildings 15:4096

- **Already achieved.** IfcGUID as cross-system primary key; four identifier-quality metrics (completeness, validity, uniqueness, stability across two exports v1/v2); duplicate-cluster detection; registration of inputs and outputs with hashes, timestamps and operator so that reruns are auditable; pre-test, repair, post-test design.
- **Overlap.** Identifier-integrity governance (Candidate A, F); audit registration of identity evidence; deterministic rerun protocol (Candidate E, partially).
- **Invalidates.** Claims that "using IFC GlobalId as an auditable cross-system key" or "detecting duplicate identifiers" are new. Both are established.
- **Remains different.** Fang works on a virtual design-stage smart home with game-engine consumers, repairs the mapping layer, and has no condition evidence, inspection or action records. Fang does test stability across two exports, which Paper 2 does not; Paper 2 must say so. Paper 2 adds a real model in which the stored Revit IfcGUID parameter and the exported GlobalId diverge (8 pairs, 16 elements) and a rule that forbids silent repair.

## 3 Lorvão Antunes et al. (2024), Intelligent Systems with Applications 22:200366

- **Already achieved.** Ontology connecting structures, structural elements, SSN sensors and observations, and inspections (as observation procedures) for national road authorities; PhysicalObject linked to an ifcElement GUID; 13 competency questions answered with SPARQL; three real pilots.
- **Overlap.** Sensor-to-BIM linking (Candidate B, first hops); inspection linkage; CQ-based evaluation (Candidate D).
- **Invalidates.** Claims that sensor-and-inspection information linked to IFC components and evaluated with CQs is new.
- **Remains different.** No maintenance action or status records; the authors state SHACL/SWRL validation was not addressed and that population and IFC mapping are manual; no model-version handling; no invalid-data tests.

## 4 Mariniello et al. (2025), Automation in Construction 180:106558

- **Already achieved.** Blockchain smart contracts that validate SHM data quality, validate damage-detection tools, and log alert reactions (inspection dispatch) with authorised actors, on a real viaduct.
- **Overlap.** Provenance and auditability of monitoring evidence; evidence-to-reaction trace; validation logic.
- **Invalidates.** Claims that auditable, rule-checked handling of monitoring data from acquisition to reaction is new.
- **Remains different.** No IFC component identity binding or model-version rule is reported. The trace is ledger-based, not anchored to a BIM component.

## 5 García et al. (2026), Applied Sciences 16:2562

- **Already achieved.** Publish/hold decision records tied to a specific IFC file revision and named roles; persistent evidence package; tested on 22 real deliverables (14 held).
- **Overlap.** Revision-qualified accountability; deterministic gate rules on real data.
- **Invalidates.** Claims that revision-linked, role-attributed decision records in openBIM are new.
- **Remains different.** Governance is at deliverable level. There is no component-level condition evidence, inspection or maintenance action chain.

## 6 Bellon et al. (2025), Automation in Construction 174:106157

- **Already achieved.** IFC representation of inspection (IfcTask), damage (IfcSurfaceFeature), maintenance services and costs, with the inspector as IfcActor; real inspection data from the DNIT database.
- **Overlap.** Inspection-to-action linkage in BIM (Candidate B, last hops).
- **Invalidates.** Claims that linking inspection records to maintenance actions in IFC is new.
- **Remains different.** No sensor-derived evidence, no identifier governance or version rule; validation is schema conformance, not invalid-link rejection.

## 7 Kim et al. (2018), Automation in Construction (doi 10.1016/j.autcon.2017.12.019)

- **Already achieved.** 590 real maintenance work records linked to IFC objects; retrieval by component and across shared objects.
- **Overlap.** Component-to-work-record traceability in both directions.
- **Invalidates.** Claims that BIM-anchored retrieval of maintenance history is new.
- **Remains different.** No sensors, evidence, version or integrity rules.

## 8 Hagedorn et al. (2022), Journal of Computing in Civil Engineering (doi 10.1061/(ASCE)CP.1943-5487.0001051)

- **Already achieved.** ICDD containers linking a BIM model with inspection damage and the repair order sent to a contractor.
- **Overlap.** Inspection-to-action management flow.
- **Remains different.** No sensor chain, no identity versioning, no invalid-data testing reported.

## 9 Chatsuwan et al. (2025), Buildings 15:1928

- **Already achieved.** IEQ sensors mapped to IFC GlobalIds through a mapping table; the paper warns that GlobalIds can be regenerated when elements are deleted and recreated, breaking the sensor link.
- **Overlap.** Sensor_ID to BIM_GUID binding; motivation for identity governance.
- **Remains different.** The risk is stated, not governed: no version qualification, detection rule or test.

## 10 Ramonell et al. (2023), Automation in Construction 156:105109

- **Already achieved.** Knowledge graph joining IFC entities and IoT things through shared GUIDs; maintenance process information in the graph.
- **Overlap.** Sensor-to-component integration through GUIDs.
- **Remains different.** No identifier-integrity rules, versioned identity or invalid-data testing.

## Net effect on candidate contributions

| Candidate | Strongest counter-evidence | Classification after falsification |
|---|---|---|
| A Model-version-qualified identity | Borkowski 2026 (persistence solved differently, more fully); Fang 2025 (stability metric) | SUPPORTING_CONTRIBUTION (version-scoped validity and fail-closed lookup only; not persistence) |
| B Auditable Sensor→…→Action chain, forward and reverse | Lorvão Antunes 2024 (sensor + inspection), Bellon 2025 (inspection → maintenance), Kim 2018, Mariniello 2025 | CORE_CONTRIBUTION only as the full five-identifier chain; each hop is ESTABLISHED |
| C Explicit integrity rules | Lee et al. 2020; Fang 2025; García 2026; SHACL literature | IMPLEMENTATION_DETAIL (technique established); content of the 14 rules is case design |
| D Competency-question verification | Lorvão Antunes 2024; Borkowski 2026; Monfardini et al. 2023 | ESTABLISHED_IN_LITERATURE (used as method) |
| E Deterministic invalid-data testing | Fang 2025 (pre/post); Mariniello 2025 (validation contracts); Borkowski 2026 (one inconsistency test) | SUPPORTING_CONTRIBUTION (systematic mutation classes across the chain are not reported in Tier A; still E3 only) |
| F Real identifier anomaly exercising governance | Fang 2025 (1 duplicate in a virtual model); Shafiq & Lockley 2020; Chatsuwan 2025 | SUPPORTING_CONTRIBUTION (objective E1/E2 evidence; anomalies as a phenomenon are known) |
| G Combined operationalisation | none of 10 Tier-A papers reports A+B+C+E together | CORE_CONTRIBUTION, PARTIALLY_SUPPORTED |

Central contribution candidate ("operationalizes model-version-qualified BIM component identity within an auditable condition-evidence-to-inspection-to-action traceability structure, with explicit integrity controls and bounded internal verification"): **PARTIALLY_SUPPORTED**. The combination is not reported in the screened corpus. Each element is precedented, the chain records are synthetic, and the search was targeted, not systematic.

## Residual risks not closed

1. The search was targeted (6 Consensus queries, 3 Zotero semantic queries, OpenAlex verification), not a PRISMA review. A study combining the full chain could exist outside it.
2. Ten Tier-B items are abstract-only or rely on earlier deep-read notes from 2026-09-15/16.
3. Bridge digital-twin dissertations and grey literature (e.g., the 2025 UPC dissertation on graph-driven bridge digital twins found in search) were screened at abstract level only.

## Addendum 2026-10-07 (Scopus search): two 2026 studies read at abstract level only

- **Rico Thirion et al. (2026), Digital Engineering 11:100111.** Abstract reports a bridge digital-twin platform with "a unified property and identifier system", persistent component identifiers (PCIDs), IoT data and inspection records, and improved data traceability. This is the closest new competitor to Contributions 1 and 2. Full text was blocked (HTTP 403). It must be read in full before submission; if it reports version-scoped rejection or invalid-data testing, Contribution 1 must be narrowed further.
- **Kochovski et al. (2026), Automation in Construction 189:107065.** Decentralised identifiers and verifiable credentials for provenance of digital building logbook data, including sensor logs and inspection records, on a real case. Overlaps on provenance and auditability; the abstract does not report component-level version scoping or a chain to action status.

Effect: gap confidence remains MODERATE but is now conditional on the full text of Rico Thirion et al. (2026).

## Addendum 2026-10-07 (later): Rico Thirion et al. (2026) read in full

Full text read (14 pages; `01_EVIDENCE/11_RICO_THIRION_2026_FULLTEXT_REVIEW.md`). The study does **not** report version-scoped identity, link-level rejection rules or invalid-data testing. Its persistent identifier is deliberately version-independent and held as a stored parameter. It does reach sensor → inspection → BCF issue with RACI approval on a real bridge, so Contribution 2 is narrowed to conditions (a) and (b) in Section 1.4. The manuscript v3 was revised accordingly (Sections 1.3, 1.4, 2.3, 2.8/Table 1, 5.3, 5.5). Gap confidence: MODERATE, no longer conditional on this study; only Kochovski et al. (2026) remains at abstract level.
