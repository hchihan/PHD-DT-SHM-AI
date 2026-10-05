# CORE-01 Deep Read

# Bibliographic identity

Jäkel, J.-I., Heinlein, E., Morgenstern, H., Kim, H., & Klemt-Albert, K. (2025). System- and data-integrated linking of digital 3D models of existing bridge structures with Knowledge Graphs of non-destructive diagnostic methods. *Journal of Information Technology in Construction (ITcon)*, 30, 603–630. DOI: 10.36680/j.itcon.2025.025. Zotero item key `VC5ELKN2`.

**See `00_BIBLIOGRAPHIC_VERIFICATION.md`: current Zotero metadata omits first author Jan-Iwo Jäkel entirely — resolved here using the PDF Version of Record, which lists Jäkel first on the title page, in the running header of every page, and in the paper's own reference line.**

# Research problem

Technical/information-management problem: results of non-destructive (NDE) structural diagnostic methods on existing bridges are produced in heterogeneous, incompatible data formats that are hard to integrate with 3D BIM/IFC bridge models, and IFC-based integration alone causes data loss and interoperability limits (p. 604–606). The paper develops an ontology (SODIA — Structural Diagnostics Ontology) for NDE inspection knowledge and compares two ways of linking it to a BIM/IFC bridge model: (a) data-integrated (RDF graph database) vs. (b) system-integrated (ICDD information containers, ISO 21597).

# Information architecture

`IFC bridge model (Revit-authored, 3 submodels + a "diagnostics" submodel) → IFCtoLBD converter → RDF/TTL (BOT/PRODUCT/PROPS ontologies) → manual reclassification into BROT/BRCOMP bridge-specific ontologies → SODIA ontology instances (InspectionMethod, InspectionTask, InspectionResult, InspectionParticipant, InspectionTool, Evaluation, Regulation) → graph database (Stardog) → SPARQL queries`

Second path (system-integrated): `IFC file + TTL file + SODIA ontology → ICDD information container (ISO 21597, RUB ICDD Platform) → linksets (Directed1toNLink) → SPARQL queries on the container`

Components: BIM/IFC, RDF converter (IFCtoLBD), graph database (Stardog), 7 reused domain ontologies (BROT, BRCOMP, BRIDGE, BRSTR, DOT, BMAT, FOAF), information container (ICDD/ISO 21597). No sensor stream, no CDE beyond the ICDD container, no digital twin.

# Identity mechanism

Dual mechanism, explicitly distinguished by the authors:
- **Data-integrated path:** each IFC object becomes an RDF instance with a *converter-generated* URI (e.g. `inst:buildingelement_e6904e30-a4f3-4171-b98b-4c9130275d10`), **not** the IFC GlobalId itself. The actual IFC GlobalId is retained only as a **property value** on that instance: `props:globalIdIfcRoot_attribute_simple "3ca4umfFD1SRcBJ94m9rqG"` (Table 3, p. 615). So the RDF-instance URI and the IFC GUID are two different identifiers for the same object, and the GUID is demoted to metadata rather than being the primary key.
- **System-integrated (ICDD) path:** the linkset explicitly uses **two different identifier types** for the two sides of the link — the converted TTL instance is identified by `ls:URIBasedIdentifier`, while the object in the IFC file itself is identified by `ls:StringBasedIdentifier` **with the actual IFC GUID** (p. 622, §5.3.1). This is a genuine precedent for binding a linkset directly to the real IFC GlobalId string, distinct from a converter's internal surrogate URI.

No discussion anywhere of GUID persistence across model revisions, duplicate-GUID detection, or verifying that the GUID recorded matches the *actually exported* IFC file rather than an authoring-tool parameter.

# Linkage coverage

- **A. sensor/monitoring → BIM component:** PARTIAL. Not continuous sensor monitoring; it is static NDE inspection-method results (rebound hammer, radiography) linked to a bridge component (abutment) via `sodia:inspects` — Query 01 (p. 615–616), demonstrated on 15 rebound-hammer points + 2 radiography points on one BIM model of one pedestrian bridge.
- **B. BIM component → inspection record:** YES. `sodia:InspectionResult` and `sodia:Evaluation` classes exist, and Query 09 (p. 619–620) returns an evaluation record (durability/stability/traffic-safety grades + free-text comment) tied to an inspection result.
- **C. BIM component → maintenance/action record:** NOT REPORTED. There is no maintenance, work-order, or action class anywhere in the ontology (§4.3.1 lists all classes; none is a maintenance/action concept). The chain stops at `Evaluation`.
- **D. technical evidence → inspection/action:** PARTIAL. Evidence (`InspectionResult`) → `Evaluation` (assessment score + comment) is shown (Query 09), but nothing beyond that evaluation — no link from the evaluation to any subsequent decision or action record.

# Provenance

PARTIAL. Data properties capture: inspector name + qualification/certificate (`sodia:hasQualification`, Query 03, p. 617), inspection date (`sodia:inspectionDate`), inspection tool name/producer/ID (Query 08, p. 618–619), and a free-text evaluation comment. This is real actor+date+tool metadata for who/when/with-what an inspection was done. **However:** no property records *how* the diagnostic signal itself was processed/derived (no algorithm/software version for interpreting the raw NDE reading), no review/approval history, and the transformation step itself (IFC→RDF conversion) is not recorded as provenance metadata on the resulting instances — the paper's own Discussion (p. 625) names "data loss during transformation" as an unaddressed **limitation**, not something the ontology tracks.

# Model/version context

NOT REPORTED. No IFC model version/revision field, no model hash, no versioning of the RDF graph or the ICDD container. The paper treats the BIM model as a single static snapshot for validation; Future Work (p. 626) proposes extending to "further life cycle phases" as an unaddressed gap, confirming this was out of scope here.

# Validity scope

NOT REPORTED. `sodia:inspectionDate` is an event timestamp, not an applicability/validity-interval concept. No property expresses "this evidence is valid for context X" or an expiry/supersession rule.

# Traceability level

**LEVEL 2 (bidirectional retrieval)**, with one genuine consistency check going slightly beyond simple retrieval: Query 05 "Inverse Relationship" (p. 618) deliberately tests that the inverse object property `sodia:isInspectedBy` is correctly derivable from the asserted `sodia:inspects` triple — i.e. the authors explicitly verify forward/reverse consistency of one relation, not just execute forward queries. Ten queries total (data-integrated) + two more (ICDD) all retrieve *existing, correctly asserted* data; none of the 12 queries is a reverse/backward-chaining query starting from an inspection record to recover the original raw evidence source in a different sense than "inspects/isInspectedBy". No test reaches Level 3/4 (no negative cases, no formal expected-vs-observed pass/fail protocol — see Q8/Q9 below).

# Validation design

Genuine **competency-question-driven validation**: 13 CQs specified up front (§4.1, p. 606, derived from 5 expert interviews with 6 domain experts), 10 SPARQL queries executed against manually-created RDF triples (data-integrated approach) with results shown in paired Structure/Results tables (Tables 4–23, p. 615–620), plus 2 more SPARQL queries on the ICDD platform (p. 622–623). Each query's *observed* result is shown, and the narrative confirms it matches what was expected — but there is no separate, pre-registered "expected answer" artefact shown independently of the query result; the paper does not report a formal pass/fail count or denominator (e.g. "N of M queries correct"). This is "system works and returns sensible answers", closer to but not fully reaching "relationship is verified against an independent reference" in the strict sense the task distinguishes.

# Invalid/negative tests

PARTIAL — one genuine deliberate rule-violation test exists. **Query 02 "Access"** (p. 616–617) is explicitly designed to test a domain business rule: radiography requires two access points; when a component has only one, the SPARQL query is constructed with a `BIND` clause to emit an explicit error message ("Error: Radiography requires 2 accesses"), and Table 7 shows this error actually fires for the tested instance. This is a genuine negative/rule-violation test — but it tests a **domain semantic rule** (measurement-method feasibility), not an **identity/link-integrity** case. NOT REPORTED for any of: orphan reference, duplicate GUID, stale GUID, wrong model revision, mismatched component, broken URI, conflicting binding, or missing target record. The paper's own Discussion explicitly lists "susceptibility to errors and possibility of data loss during the transformation from IFC to RDF" as an acknowledged, **untested** limitation (p. 625).

# Already established by this paper

- Sensor/diagnostic-method-to-BIM-component linkage via a domain ontology plus SPARQL, demonstrated on a real (if small) BIM model — cannot be claimed as a first.
- A competency-question-driven ontology validation methodology (13 CQs → 10+2 SPARQL queries with results shown) is a direct precedent for Paper 2's CQ-based evaluation design.
- A deliberate domain-rule-violation test embedded in a validation query (Query 02) is a precedent for "integrity rule → explicit error" style testing, though at the semantic/business-rule level, not the identity/link level.
- Explicit distinction between a converter-generated internal URI and the actual IFC GlobalId as two separate identifiers, with the ICDD linkset variant explicitly binding to the real GUID via `StringBasedIdentifier` — a real precedent that Paper 2's BIM_GUID definition (§3.2 of the Paper 2 draft) must cite and differentiate from, not claim as novel.
- One genuine forward/reverse (inverse-property) consistency check (Query 05).

# Remaining gap relative to Paper 2

- **No maintenance/action record concept at all** — the chain (`Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status`) is only covered up to something resembling `Condition_Evidence_ID`/`Evaluation`; nothing corresponds to `Inspection_Record_ID` as a first-class, reviewable, accountable record with reviewer/approval state, and nothing corresponds to `Action_Status` at all.
- **No identity-governance/verification layer**: GUID handling is descriptive (two identifier types named) but not verified — no duplicate-GUID detection, no check that the GUID in the linkset matches the *actually exported* IFC file rather than an authoring-tool parameter, no model-version binding.
- **No provenance of the transformation/derivation process itself**, and no uncertainty/confidence representation for the diagnostic result.
- **No validity-scope/applicability concept** for when/where an inspection result may be (re)used.
- **No deliberate identity/link-integrity negative tests** (orphan, duplicate, stale, wrong-version) — only one domain business-rule negative test exists.
- Validation reports observed query answers narratively; it does not report a pre-registered expected-answer set with an explicit pass/fail count and denominators (Paper 2's protocol design is a real methodological step beyond this).

# Claim → Evidence → Limitation → Implication

**Claim:** SODIA + two integration approaches let heterogeneous NDE diagnostic data be linked to a 3D bridge model and queried.
**Evidence:** §5, Tables 4–23 and Figures 12–21 (pp. 613–624; appendix pp. 629–632 of the PDF, i.e. printed pages 629–632/appx. 1–4), showing 12 executed SPARQL queries with results.
**Limitation:** Validation is qualitative/demonstrative (no expected-answer pre-registration, no denominators, no negative/identity-integrity tests); explicitly acknowledged by the authors as providing "no further quantitative parameters for measuring quality and efficiency" (p. 625).
**Implication for Paper 2:** Paper 2 cannot claim novelty for "linking inspection results to BIM components via an ontology + SPARQL" as a general idea. Paper 2's genuine differentiation must rest on (i) extending the chain through a first-class, accountable Inspection_Record and Action_Status, (ii) identity **verification** (not just identifier naming) against the actual exported IFC, and (iii) a pre-registered expected-answer + denominator protocol including deliberate identity/link-integrity negative cases — none of which CORE-01 provides.

# Critical passages/pages for later citation

- p. 604–606 (Introduction, research gap statement)
- p. 606 (§4.1, 13 competency questions)
- p. 611, Table 1 (7 reused ontologies)
- p. 613–614 (§5.1, BIM model description, Fig. 4)
- p. 615, Table 3 (converted IFC instance with `props:globalIdIfcRoot_attribute_simple`)
- p. 615–620, Tables 4–23 (Queries 01–10, data-integrated validation)
- p. 616–617, Query 02 "Access" (deliberate rule-violation test)
- p. 617–618, Query 05 "Inverse Relationship" (bidirectional consistency check)
- p. 620–623 (§5.3, ICDD approach; §5.3.1 identifier types: `ls:URIBasedIdentifier` vs `ls:StringBasedIdentifier` with GUID)
- p. 624–626 (§6, Discussion & Conclusion, explicit limitations)
