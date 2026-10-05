# CORE-05 Deep Read

# Bibliographic identity

Seiß, S., Zheng, Y., Melzner, J., Wium, J., & Seppänen, O. (2025). Ontology-based representation of quality assurance and inspection planning in construction. *Automation in Construction*, 177, 106268. DOI: 10.1016/j.autcon.2025.106268. Zotero item key `JTF8EM7Y`. No conflict between Zotero metadata and PDF.

# Research problem

Knowledge-representation problem for **construction quality-inspection planning**: existing inspection ontologies are trade-specific, monolithic, terminologically inconsistent with ISO 9000/9001/DIN 55350, unpublished, and unable to integrate heterogeneous inspection-planning information (contract, schedule, BIM, regulation, quality history) — see the explicit evaluation of four prior ontologies against 12 criteria (Table 1, p. 4), all of which fail most criteria. The paper develops **OCQA (Ontology for Construction Quality Assurance)**, a modular OWL ontology, following the LOT methodology, and evaluates it on real project data.

# Information architecture

`BIM (IFC) → IFC2LBD converter (RDF) + Schedule + BOQ (contract, X83→CSV via iTWO) + Inspection templates + Inspection plan (planned AND executed inspections) → manual mapping + R2RML (relational/CSV → RDF) → RDF instance data → OCQA ontology (core module + catalog/regulation/contract modules + trade-specific extensions, e.g. screed) stored in Stardog graph database → SPARQL queries + OWL-axiom-based reasoning (Pellet reasoner) → prototype toolkit (Sparnatural visual query builder + result table + BIM viewer + schedule viewer, Fig. 10)`

OCQA is explicitly aligned with external ontologies (Fig. 7, p. 9): DiCon (construction workflow, foundational), BOT/ifcOWL (building/spatial, via `dicp:hasObject`), OPM + DiCon variable/context module (temporal/change-over-time), **SSN/SOSA/SAREF (sensor/observation, `sosa:Observation`/`saref:Measurement` → `ocqa:Observation`/`ocqa:Measurement`)**, FOAF (organizational/person).

# Identity mechanism

**Explicit use of the actual IFC GlobalId as the component identifier**, not a converter-internal surrogate URI. The evaluation example shows the queried building object identified as `2EXbspDnzBfQetvaNkppij` (a genuine IFC-style 22-character base64 GUID) via the triple pattern `?inspection dicp:hasObject ?UUID` (Listing 1, line 3; Table 4, CQ.1 answer, p. 11), and a second screed component with UUID `0owp2g3RTDcQ$khC3kGEsY` (p. 13, Use Case 2). This is the closest of the 5 papers to Paper 2's own BIM_GUID concept — the GUID *is* the binding key, obtained directly from the IFC2LBD conversion. **However, the paper does not discuss any identity-governance/verification layer**: no duplicate-GUID handling, no discussion of confirming the GUID matches the *actually exported* IFC rather than an authoring-tool parameter, and no model-version binding — the GUID is simply used as given from a single conversion pass.

# Linkage coverage

- **A. sensor/monitoring → BIM component:** PARTIAL/DESIGNED, not empirically demonstrated. SSN/SOSA/SAREF alignment (`sosa:Observation`, `saref:Measurement` → `ocqa:Observation`/`ocqa:Measurement`) is explicitly built into the ontology's architecture (§6.6, Fig. 7, p. 9), but the evaluated case study (screed flatness/moisture/height inspection) uses **manual spirit-level measurement**, not live sensor data — so this linkage is structurally present but never exercised with real sensor input in the paper's own evaluation.
- **B. BIM component → inspection record:** YES — the strongest and most complete demonstration among the 5 papers. Inspection `42015` is explicitly linked via `dicp:hasObject` to the screed component UUID, and the query returns the full record: characteristic (flatness), assigned value (max 0.6 cm/200 cm), governing norm chain, procedure, equipment, location, responsible inspector + employer organization, status, and failure probability — all shown with concrete values (Table 4, p. 11).
- **C. BIM component → maintenance/action record:** NOT REPORTED. The chain stops at the Inspection entity itself; there is no maintenance/repair/work-order class. `ocqa:hasStatus` on the inspection (e.g. "Planned") and `ocqa:hasInpsectionStatus` on the inspected object (e.g. "to be inspected") are the only status-like concepts, and they describe the inspection process itself, not a subsequent corrective action.
- **D. technical evidence → inspection/action:** PARTIAL. The ontology explicitly models `ocqa:AssignedCharacteristicValue` (requirement) vs. `ocqa:ActualCharacteristicValue` (the determined/measured actual value) as a designed **conformance-comparison mechanism** ("the comparison of the assigned and actual characteristic can be performed by standardized rules using a query or rule language," §6.2, p. 7) — the closest analogue across all 5 papers to an evidence-vs-requirement check. But the executed evaluation (inspections 42015/42016) concerns **planning** ("Planned" status), not a completed measurement triggering a subsequent action; the evidence→conformance→action loop is designed but not empirically closed in this paper.

# Provenance

STRONG for *requirement*-provenance, WEAK for *measurement-capture* provenance. CQ.3's full answer chain — "BOQ-Item 3310.25.5.24 contracts DIN 18560, which references tolerances for screed defined in DIN 18202" (Table 4, p. 11) — is a genuine, queryable derivation trace from a contract clause through a chain of referenced norms, arguably the best "why is this required, and where does that requirement come from" traceability of the 5 papers. Actor/organization provenance for the *inspection* is also explicit (`dica:isResponsiblefor`, `dica:isOrganizationPartOf` → "Inspector01 employed by DerichsUndKonertz"). **However**, no property records how an *actual measured value* itself was captured (device calibration state, exact timestamp of measurement, operator who took the reading as distinct from the inspector of record) — the paper's data is about planning inspections, not about auditing executed-measurement provenance.

# Model/version context

NOT REPORTED as tested. OPM + DiCon's "variable and context module" is cited as supporting representation of "changes in entities over time" via named graphs for as-planned vs. actual construction-process information (§6.6, p. 9) — this is a **designed capability**, structurally present via the ontology alignment, but **not exercised or demonstrated** anywhere in the evaluation (Use Cases 1 and 2 both operate on a single, static instantiation of project data). No IFC model version/hash/revision concept, no per-GUID version binding.

# Validity scope

PARTIAL, but a different concept than Paper 2's `Scope_of_Validity`. The assigned characteristic value (e.g., "max 0.6 cm over 200 cm") functions as a **quality-tolerance criterion** defined by a specific cited norm — this expresses *what counts as conforming*, not *in what context/campaign/protocol this evidence record may be (re)used*. NOT REPORTED for an applicability-set/context-descriptor concept analogous to Paper 2's evidence-usability scope.

# Traceability level

**LEVEL 3 (structured traceability), the strongest of the 5 papers, approaching Level 4.** Concrete evidence: (a) forward CQ-driven SPARQL queries with specific returned values for all 11 project-specific CQs in Use Case 1 (Table 4, Listing 1, p. 11); (b) a genuine **reverse/inverse traversal**: `?inspection ^dice:precedes ?activity` (line 9, backward from inspection to its preceding scheduled activity) and `?NormForScreed ^ocqa-con:contract ?BOQItem` (backward from norm to the contract clause that invokes it) — real inverse-property chaining, not merely a second forward query; (c) **axiom-based reasoning** via the Pellet reasoner automatically classifies an uncategorized inspection instance into `ocqa-screed:FlatnessInspection` (Use Case 2, Table 6, Listing 2), i.e. inference, not just retrieval. This is the only paper of the 5 that combines CQ-driven retrieval, explicit reverse-property queries, and reasoner-based inference in one evaluation.

# Validation design

**Multi-method, the most rigorous among the 5 papers**, but with one specific methodological gap relevant to Paper 2. Methods used: (1) automated consistency checking — Pellet reasoner (OWL-DL consistency/inference) + OOPS! ontology-pitfall scanner (§7.1, p. 9); (2) criteria-based evaluation (clarity, extensibility, §7.2); (3) **task-based evaluation with real project data** from a construction company (DERICHS u KONERTZ) — real BIM, schedule, executed/planned inspection plan, inspection templates, and BOQ with long-text specifications, transformed via R2RML into RDF and queried with concrete SPARQL statements whose results are tabulated (Tables 4–5, Listings 1–5); (4) **two focus-group expert interviews**, 5 + 6 domain experts (civil engineers/architects, ≥5 years' QA experience), 3–4 hours each, structured questions (Table 8, p. 15–16). **Gap:** the CQ answers in Tables 4–5 are reported as the *narrated result of running the query*, not checked against an independently pre-registered "expected answer" via an explicit, stated pass/fail comparison procedure with denominators — the paper's own Limitations (§8.3, p. 16) state the reasoning was "derived through SPARQL queries that utilize predefined reasoning knowledge," but does not report an expected-vs-observed correctness metric (e.g. "N of M CQs answered correctly").

# Invalid/negative tests

**NOT REPORTED — a clean, explicit gap even in the strongest paper of the CORE-5 set.** All evaluation data (Use Cases 1 and 2, both focus groups) concerns valid, positively-classified, correctly-structured project data. No deliberate orphan reference, duplicate GUID, stale GUID, wrong model revision, mismatched component, broken URI, or conflicting-binding case is constructed or tested anywhere in the paper. This is an important, citable absence: Paper 2's deliberate negative/invalid-fixture testing protocol would be a genuine methodological advance **even relative to the single closest prior-art paper found across the CORE-5 review.**

# Already established by this paper

- Direct use of the **actual IFC GlobalId** as the binding key between an inspection ontology instance and a BIM component, demonstrated on real project data with concrete example UUIDs — Paper 2 cannot claim to be first to bind inspection knowledge to the real IFC GUID (as opposed to a converter-internal surrogate URI, cf. CORE-01/CORE-02).
- A rigorous, **competency-question-driven, multi-method ontology-evaluation methodology** (consistency check + criteria-based + task-based/CQ + expert focus groups) on real project data — the closest existing evaluation-design precedent to Paper 2's own CQ + fixture protocol; Paper 2 must position its contribution as a specific methodological refinement (pre-registered expected answers with explicit pass/fail and denominators; deliberate negative fixtures) rather than as "the first CQ-based evaluation in this space."
- A designed (if unexercised) architectural alignment to SSN/SOSA/SAREF for sensor-derived evidence, and to OPM/DiCon's variable-context module for temporal/as-planned-vs-actual change tracking — Paper 2 must cite this as prior structural precedent even though CORE-05 never demonstrates either capability empirically.
- Reverse/inverse-property SPARQL traversal and reasoner-based axiomatic classification as genuine bidirectional-traceability and inference precedents.
- An explicit requirement-provenance chain from contract clause through referenced norms to a specific inspection — a real precedent for "why is this required" traceability that Paper 2's evidence contract should differentiate from (Paper 2's provenance chain concerns *evidence origin*, not *requirement origin*).

# Remaining gap relative to Paper 2

- No maintenance/action-record concept at all — the chain stops at the Inspection entity; nothing corresponds to `Action_Status`, an executed corrective action, or its closure/verification.
- No identity-**governance/verification** layer around the GUID: it is used as given from one IFC2LBD conversion pass, with no duplicate-GUID handling, no verification against the actually-exported IFC file as distinct from an authoring-tool parameter, and no per-GUID model-version binding.
- No deliberate identity/link-integrity negative tests anywhere — a clean, explicit, citable gap even in the strongest paper reviewed.
- No pre-registered expected-answer set with an explicit pass/fail comparison and denominators; CQ answers are narrated, not programmatically checked against an independent reference.
- Sensor-to-component evidence linkage (SSN/SOSA/SAREF alignment) and temporal/version change-tracking (OPM/DiCon context module) are both architecturally designed but **never empirically demonstrated** — Paper 2's actual sensor-derived condition-evidence chain, if executed and tested, would be a genuine empirical advance beyond this paper's structural-only alignment.
- No validity-scope/applicability-set concept for evidence *usability* across contexts (the paper's "assigned characteristic value" is a quality-conformance tolerance, a different concept).
- No provenance of the individual measurement-capture *event* itself (device/calibration/exact-operator-of-record), only of the inspection's planning/responsibility metadata.

# Claim → Evidence → Limitation → Implication

**Claim:** OCQA provides a modular, ISO-9000/9001/DIN-55350-aligned, machine-readable ontology for construction quality-inspection planning that integrates heterogeneous information sources (BIM, schedule, contract, regulation, quality history) and answers competency questions about inspection plans and knowledge via SPARQL and axiom-based reasoning.
**Evidence:** §5–7 (pp. 5–16): ORSD (Table 2, CQs), architecture (Fig. 3), core module (Fig. 4), data transformation on real project data (Fig. 8), Use Case 1 (Table 4, Listing 1, real GUIDs and concrete CQ answers), Use Case 2 (Table 5–7, Listings 2–5, reasoner-based inference), focus-group evaluation (Table 8).
**Limitation:** No negative/invalid-link testing anywhere; no pre-registered expected-answer/pass-fail protocol with denominators; sensor and temporal/version-tracking capabilities are architecturally aligned but not empirically exercised; evaluation confined to one trade (screed) for the detailed CQ demonstration (§8.3, explicitly acknowledged, p. 16); chain does not extend past the inspection record to any maintenance/action concept.
**Implication for Paper 2:** This is the single closest paper to Paper 2's Gate 2–3 contribution and the strongest threat to its claimed novelty on the *information-traceability* and *identity-binding* fronts. Paper 2's differentiated, defensible contribution must be staked specifically on: (i) extending the verified chain through an accountable Inspection_Record **and** a closed-loop Action_Status (absent here); (ii) identity **verification** against the actually-exported IFC file, not just identifier reuse (absent here); (iii) a pre-registered, denominator-reporting expected-answer protocol (absent here, even though CQ-based evaluation itself is not novel); and (iv) deliberate identity/link-integrity negative-fixture testing (absent even in this closest paper). Paper 2 cannot claim "first CQ-based ontology evaluation for inspection/BIM linkage," "first use of the actual IFC GUID for inspection binding," or "first reuse of SSN/SOSA/SAREF-style sensor alignment intent" — all three already appear here, at least as design or demonstration.

# Critical passages/pages for later citation

- p. 4, Table 1 (evaluation of 4 prior inspection ontologies against 12 criteria — explicit gap statement)
- p. 5, §5, Table 2 (ORSD, use cases, general competency questions)
- p. 6–7, §6.2, Fig. 4 (core module: `ocqa:Inspection`, `ocqa:AssignedCharacteristicValue` vs. `ocqa:ActualCharacteristicValue`)
- p. 9, §6.6, Fig. 7 (external-ontology alignment: DiCon, BOT/ifcOWL, OPM, SSN/SOSA/SAREF, FOAF)
- p. 9–11, §7.1–7.3.2, Table 3–4, Listing 1, Fig. 8–10 (evaluation methods; Use Case 1 with real IFC GUIDs `2EXbspDnzBfQetvaNkppij` and full 11-CQ answer set)
- p. 13, §7.3.3, Table 5–7, Listing 2–5 (Use Case 2, reasoner-based classification, second GUID `0owp2g3RTDcQ$khC3kGEsY`)
- p. 15–16, §7.4, Table 8 (focus-group evaluation)
- p. 16, §8.3 (explicit limitations: no negative testing discussed, single-trade CQ evaluation, manual R2RML mapping, no automated inference used for plan generation)
