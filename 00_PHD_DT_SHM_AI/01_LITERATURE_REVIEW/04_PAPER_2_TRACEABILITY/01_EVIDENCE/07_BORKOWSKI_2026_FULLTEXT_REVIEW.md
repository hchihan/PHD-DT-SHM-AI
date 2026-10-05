# 07 — Borkowski, Jarema, Kładź & Smoliar (2026) — Full-Text Review

**Status: FULL_TEXT_AVAILABLE — read in full (26/26 pages) via Zotero MCP `zotero_read_pdf_pages` on item key `CVGD2BLV`.**

**Correction note (this pass):** The prior correction pass incorrectly concluded `FULL_TEXT_NOT_AVAILABLE` based on a check of item key `NQ3KGDWN` alone. A library-wide search revealed a **duplicate bibliographic item** (`JSYCVGH9`) for the same paper, which owns the PDF attachment. `NQ3KGDWN` genuinely has zero attachments (metadata-only duplicate); `JSYCVGH9` has one child attachment (`CVGD2BLV`, `application/pdf`, 2,199,040 bytes, local path `C:\Users\VNT\Zotero\storage\CVGD2BLV\Borkowski et al. - 2026 - Temporally Qualified Building Elements...pdf`). No Zotero metadata was modified; both items are left as-is per the stop condition.

---

# Bibliographic verification

| Field | `NQ3KGDWN` (no PDF) | `JSYCVGH9` (PDF owner — used for this review) |
|---|---|---|
| Title | Temporally Qualified Building Elements: A DOLCE-Based Ontology for Phase-Dependent Identity and Change Tracking in BIM Models | identical |
| Authors | Borkowski, Andrzej Szymon; Jarema, Paulina; Kładź, Magdalena; Smoliar, Anatolii | identical |
| Journal | Technologies, 14(7), 413 | identical |
| DOI | 10.3390/technologies14070413 | identical |
| Date | 2026/7 | identical |
| Collections | F3YAG68Y | QETBUAR8 |
| numChildren | 0 | 1 |
| Attachment | none | `CVGD2BLV` (PDF, 2.2 MB) |
| Item version | 4793 | 5393 |

**Duplicate-detection outcome (per this task's checklist):**
- **A. Duplicate bibliographic items:** YES — `NQ3KGDWN` and `JSYCVGH9` are two separate Zotero items for the identical publication (same DOI, title, authors, journal, issue, page).
- **B. PDF attached to another duplicate/parent item:** YES — the PDF is a child of `JSYCVGH9`, not `NQ3KGDWN`.
- **C. PDF exists as a standalone attachment:** No — it is a proper child attachment of `JSYCVGH9` (not a loose top-level attachment item).
- **D. `NQ3KGDWN` has metadata only while another item owns the PDF:** YES — confirmed exactly as suspected.

**Correct Version-of-Record identification:** DOI, title, full author list, journal, volume/issue/page, and abstract are identical across both items and match the publisher record (MDPI *Technologies* 14(7):413, https://www.mdpi.com/2227-7080/14/7/413) exactly. `JSYCVGH9` / `CVGD2BLV` is used as the full-text source for this review; no discrepancy between the two duplicate records' metadata was found (both are faithful copies of the same Version of Record).

**PDF content verification:** the PDF's own header/footer confirm: title, all four authors (Andrzej Szymon Borkowski, Paulina Jarema, Magdalena Kładź, Anatolii Smoliar), affiliations (Warsaw University of Technology; Cherkasy State Technological University, Ukraine), DOI, "Technologies, 413" running header, received/revised/accepted/published dates (18 May 2026 / 1 Jul 2026 / 3 Jul 2026 / 6 Jul 2026), Academic Editor Ioannis K. Brilakis, CC BY 3.0 license, 26 total pages.

---

# Research problem

**CONFIRMED, full-text.** IFC treats every building element as a static, single-state snapshot with no formal mechanism linking the *same physical element* across the separate IFC files produced at successive life-cycle phases (design, as-built, operation/FM). Each phase file assigns the element a different GUID, causing (1) identity fragmentation at the object level, (2) loss of property-change history (new values silently overwrite old ones), and (3) inability to formulate cross-phase semantic queries (e.g., "which structural elements changed material between design and as-built?"). The paper frames this as a genuine research gap at the intersection of three areas: (a) DOLCE-style fundamental ontologies offer mature machinery for this (endurant/perdurant, constitution, temporal qualification) but have not been applied to BIM; (b) existing construction ontologies (ifcOWL, BOT, PROPS) faithfully mirror IFC's atemporal structure and inherit its limitation; (c) semantic-enrichment research enriches single model snapshots but does not link snapshots together. Three explicit research questions are posed (RQ1: how to formally separate element identity from phase-state; RQ2: how to model phase-dependent scalar/material/meronomic properties in OWL 2 DL without breaking decidability; RQ3: how to represent phase transitions as processes, not just state differences).

---

# Identity concept

**Q1 answer — CONFIRMED as primarily reading (A), with (B) and (C) present as concrete instantiating mechanisms, not as separate concerns:**

- **(A) Same physical element across multiple lifecycle phases** — YES, this is the paper's explicit and central framing: "the same physical element may have different GUIDs... there is no formal relationship establishing that they refer to the same entity" (Sec. 1); the `BuildingElement` (endurant) class is explicitly defined to represent "a single physical object regardless of how many times it has changed its properties, material, or relationships."
- **(B) Same BIM object across file revisions** — YES, and this is *how* (A) manifests concretely: each life-cycle phase in the case study is a **separate Revit project file (.rvt)**, independently exported to a separate IFC file. The paper treats "phase" and "file" as effectively coextensive in its case study ("the design model file generates a DesignPhase instance, the as-built file generates an AsBuiltPhase instance...").
- **(C) Same object across IFC export/re-export** — YES, explicitly named as a related, generalized instance of the same underlying problem: "element identity is unstable. GUIDs are guaranteed to persist only within a single authoring environment. Export, import, and re-export operations frequently regenerate identifiers. **This last problem is the direct concern of the present work.**" (Sec. 2.2). The case study's own three IFC files were independently exported from three independently authored Revit files, so GUID non-persistence-under-re-export is empirically what produces the three different GUIDs for the same wall.
- **(D) Same object between authoring system and IFC** — NOT directly addressed; the paper does not discuss authoring-tool-internal identifiers (e.g., Revit's own persistent ElementId) versus IFC GUIDs as a distinct concern.
- **(E) Semantic identity across models (in the sense of ontology alignment/equivalence between different modeling paradigms)** — NOT addressed; this is not an ontology-alignment paper.

**Conclusion: the paper's identity concept is (A), operationalized through (B)/(C) — i.e., "the same physical element, exported across independent, phase-labeled IFC files, receiving a different GUID each time."** This is squarely and precisely the GAP-B framing this correction pass and the underlying targeted review are concerned with.

---

# Persistent identity mechanism

**Q2 — IFC GUID's status, CONFIRMED:** explicitly treated as an **insufficient / unstable, phase-local identifier**, not a primary persistent identity. Direct quotes: "GUIDs are guaranteed to persist only within a single authoring environment"; "IFC does not guarantee GUID preservation across exports"; the paper's own conclusion states this "solves the problem of unstable GUIDs at the semantic level." In the proposed mechanism, the GUID is **demoted to a phase-level attribute** (`hasIFCGuid`, e.g. `"2O2Fr$t4X7Zf8NOew3FNr2"`) used only for backtracking to the specific source IFC file — it is explicitly **not** the identity anchor.

**Q3 — mechanism of the proposed persistent identifier, CONFIRMED in full technical detail:**
- **New identifier?** YES — a brand-new URI (e.g., `bph:wall-W01`) is minted, "independent of IFC GUIDs."
- **Ontology entity?** YES — this URI identifies a single instance of the `BuildingElement` class, itself a subclass of `DOLCE:PhysicalEndurant`.
- **URI?** YES, explicitly.
- **Temporal-object identity (DOLCE endurant/perdurant)?** YES — this is the entire architectural basis: `BuildingElement` = endurant (persists identically); `LifecyclePhase` = perdurant/`DOLCE:State` (a temporal segment); properties/material/parthood are attached not to the endurant directly but to **reified `PhaseQualifiedRelation` instances** that each point to exactly one `BuildingElement` (`appliesToElement`), exactly one `LifecyclePhase` (`holdsAtPhase`), and a value (`hasValue`) — following the W3C n-ary-relation pattern, kept within OWL 2 DL (only binary properties used).
- **Mapping relation?** PARTIAL — the per-phase `hasIFCGuid` attribute is a simple backlink from a phase instance to its source-file GUID, not a formal mapping/equivalence structure.
- **External registry?** NO — nothing external; identifiers are minted within the project's own Turtle/OWL knowledge graph.
- **Equivalence relation?** NO — the mechanism does **not** assert `owl:sameAs` (or similar) between the different per-phase GUIDs; instead, it introduces a wholly new superordinate identity object (the endurant) that subsumes all phases, with each phase carrying its own GUID as an attribute.

**Full formal apparatus:** 9 classes, 6 object relations + 1 data relation (`hasPropertyName`), 6 axioms in OWL 2 DL:
1. Every `BuildingElement` has ≥1 `hasPhase` relation.
2. Every `PhaseQualifiedRelation` has exactly 1 `appliesToElement` and exactly 1 `holdsAtPhase`.
3. `BuildingElement` and `LifecyclePhase` are disjoint.
4. `precedes` is transitive.
5. `DesignPhase`/`AsBuiltPhase`/`FacilityManagementPhase` are pairwise disjoint.
6. `hasPhase` ≡ inverse of `isPhaseOf`.

An optional, explicitly "first-class but modular" **event-based extension** adds a `PhaseTransitionEvent` class (subclass of `DOLCE:Perdurant`) with functional relations `transitionsFrom`, `transitionsTo`, `affectsElement`, linking two reified phase-states — enabling a transition itself (e.g., a "ConstructionEvent" or "MaintenanceEvent") to be queried as a first-class graph entity.

---

# Model/revision handling

**Q7 — CONFIRMED, with important nuance.** The paper **does** handle actual, real IFC files representing model phases/revisions, but **not** via explicit version identifiers, hashes, or a CDE (Common Data Environment) revision scheme:

- **Model revision identifiers:** NO explicit version-numbering scheme (no v1/v2/rev-A style IDs).
- **IFC file versions:** YES, concretely — 3 independently authored Revit files (.rvt), each exported to its own IFC file via Revit 2026.2's built-in exporter, one per phase (Design / As-Built / Facility Management).
- **Hashes:** NO — no file or content hashing is used anywhere.
- **Export timestamps:** implied by "chronology of file creation" but not modeled as an explicit timestamp property in the ontology.
- **Version graph / previous-next revision:** YES — the `precedes` object relation (transitive) explicitly orders `LifecyclePhase` instances chronologically, forming exactly a "previous/next revision" chain, confirmed by axiom 4 and used directly to answer CQ8 ("What is the temporal order of a given element's phases?").
- **CDE revision (ISO 19650-style):** NO — not mentioned or engaged with at all.

**Model/revision binding at the instance level:** each `LifecyclePhase` instance is directly and explicitly bound to one source IFC file/GUID via the `hasIFCGuid` attribute recorded on its reified property instances — this is a genuine "specific model snapshot binding," just without hash- or CDE-based versioning machinery.

---

# Validation design

**Q6 — CONFIRMED, multi-part, and materially more concrete than the abstract suggested:**

1. **Ontology-consistency validation via reasoner:** YES — HermiT reasoner in Protégé 5.6, checked for contradictions and cardinality-constraint satisfaction over the full case-study knowledge graph (3 endurants, 9 phases, 27 reification instances).
2. **Deliberate negative test (axiom-level, NOT identity-mapping-level):** YES, one concrete instance — "The third axiom (disjointness of the `BuildingElement` and `LifecyclePhase` classes) was tested by intentionally introducing an individual with dual classification. The reasoner reported an inconsistent ontology, which confirms the validity of the disjointness axiom." This is a genuine, deliberate invalid-case test — but it tests **schema/axiom violation**, not identity-mapping integrity (no duplicate/orphan/wrong/stale-GUID test was performed — see "Negative/invalid identity cases" below).
3. **Case study:** YES — single-family residential building (~120 m², masonry, gable roof), modeled in Autodesk Revit 2026.2, 3 representative elements (exterior wall W-01, floor slab S-01, column C-01) covering the 3 modeled change types (scalar property, material constitution, meronomic/parthood), tracked across exactly 3 phases.
4. **Deterministic expected-answer / competency-question testing:** YES, and fully itemized — 8 competency questions (CQ1–CQ8), each mapped in a published table (Table 3) to the specific classes/relations/axioms required to answer it; "all eight questions were answered correctly on the published knowledge graph" via SPARQL 1.1 queries executed in Protégé's SPARQL interface.
5. **Manual verification:** YES, and explicitly confirmed as a limitation, not a strength — "the knowledge graph instances were entered manually based on the Revit model rather than generated automatically from an IFC file."
6. **Identity-matching accuracy:** **NOT measured / NOT applicable** — identity matching across the three phase files was performed by the authors' own judgement ("expert knowledge or heuristics"), not validated against any ground truth or accuracy metric.
7. **Reproducibility:** the full ontology (Turtle/OWL 2 DL), instance graph, and SPARQL queries are published in the Warsaw University of Technology open research data repository (DOI: 10.71724/be6h-n995) — genuinely reproducible, a methodological strength.

---

# Negative/invalid identity cases

**Q5 — CONFIRMED ABSENT, with one important partial exception.** Checked systematically against the full Q5 taxonomy:

| Case | Status |
|---|---|
| Deleted object | NOT tested |
| Recreated object | NOT tested |
| Split/merge object | NOT tested — explicitly named as **out of scope**: "The ontology also does not model uncertainty or competing model versions... Parallel design variants or branching renovation scenarios cannot be represented without extending the phase ordering to a partial order." |
| Duplicate GUID | NOT tested (GUID regeneration across exports is the *premise* the paper solves around, not a negative case it deliberately injects and detects) |
| GUID regeneration | This is the motivating *problem*, not a *test case* — the paper does not inject a regenerated-GUID scenario and verify correct/incorrect detection; it simply accepts that GUIDs differ per phase and routes around this via the endurant URI |
| Wrong mapping | NOT tested |
| Conflicting mapping | NOT tested |
| Missing mapping | NOT tested |
| Stale mapping | NOT tested |
| **Schema/axiom violation (disjointness)** | **YES, tested and confirmed** (see Validation design #2 above) — but this is a different category from identity-*mapping* integrity |

**Conclusion:** the paper performs exactly **one** deliberate negative/invalid test, and it is at the **ontology-schema level** (class disjointness), not at the **identity-mapping/data-instance level** the targeted review's GAP-D/GAP-H concern. No orphan-record, duplicate-identifier, wrong-model-revision, mismatched-component, or conflicting-binding test was performed anywhere in the paper.

---

# Provenance

**Q9 — PARTIAL, confirmed via full text (upgraded from EVIDENCE_INSUFFICIENT).** The only provenance-like mechanism present is the `hasIFCGuid` attribute recorded on each reified phase-relation instance, which enables "backtracking to the source file" — i.e., a bare source-file/source-GUID backlink. There is:
- NO explicit assertion-timestamp property (who/when a given reified fact was entered into the graph — recall these were manually entered).
- NO processing provenance (no record of *how* a value was derived/transcribed from the IFC file).
- NO human-actor provenance (no property records which person/role authored, curated, or verified a given phase-state or transition event).
- The event-based extension (`PhaseTransitionEvent`) records a causal/structural link between two phase-states but does **not** record who or what performed/caused the transition (no `performedBy`, `causedBy`, or similar).

**Conclusion:** provenance is present only in the narrowest "which source file did this value come from" sense (source provenance only); measurement, processing, and human-actor provenance are all absent.

---

# Evidence validity/applicability

**Q10 — CONFIRMED ABSENT (NOT_REPORTED, per the strict definition used in this correction pass).** Systematically checked: no `valid_from`/`valid_to` bound, no operating-condition/protocol/configuration-applicability concept, no explicit "supersedes"/"do not reuse outside this context" rule for evidence values. Two things that could be superficially confused with this concept, and are explicitly distinguished here per this task's Section 7 rule:
- The `precedes` phase-ordering chain and the disjoint `DesignPhase`/`AsBuiltPhase`/`FacilityManagementPhase` subclasses are a **MODEL_VERSION_CONTEXT** mechanism (which phase/file a value belongs to and its chronological position) — **not** an evidence-validity/applicability rule about the conditions under which a given property value is trustworthy or reusable.
- The FM-phase property change from `"constructed"` to `"requires repair"` status is a **condition/state value**, not an applicability rule.

No valid-time, protocol, confidence, or supersession-of-evidence concept was found anywhere in the 26-page full text.

---

# Links to sensor/evidence/inspection

**Q8 — CONFIRMED, with an important, explicit forward-looking statement that materially raises (not lowers) the novelty-threat relevance, though still not implemented:**

> "Sensor readings, inspection results, and maintenance events can then refer to one and the same persistent element across the whole life cycle." (Sec. 5.1, Discussion — "Evaluation")

This is a **direct, explicit statement connecting the BIM-Phase identity mechanism to sensor data, inspection results, and maintenance events**, framed as a stated *complementary vision/implication*, not as an implemented or validated feature of the paper. Concretely, in the case study itself:
- A **crack is recorded** in the structural layer during the FM phase, and the element's status changes to `"requires repair"` — this is condition-evidence-*like* content, but modeled only as a bare `PhaseQualifiedProperty` value change, with no separate `Condition_Evidence` record, no evidence source, no measurement metadata.
- Column C-01 is reinforced with CFRP **"following a technical inspection"** — the inspection is named as a narrative trigger for a material-constitution change, but is **not** modeled as a distinct `Inspection_Record` entity with performer/reviewer/timestamp/status.
- The event layer's `MaintenanceEvent` (one interpretation of a `PhaseTransitionEvent`) is a bare transition-type label, not a maintenance-record entity with accountability fields.
- **No sensor data, IoT stream, or Sensor_ID concept appears anywhere in the ontology, case study, or implementation** — sensor integration is explicitly named only as future-work-adjacent ("Long-term sensor-based monitoring... is an established practice... Such systems... do not represent the identity of its elements... The BIM-Phase ontology is complementary to this trend. It provides the semantic anchor to which operational data streams can be attached.")

**Conclusion:** Borkowski explicitly envisions exactly the kind of integration Paper 2's core chain performs (identity as the anchor for sensor/evidence/inspection data), but does **not implement, model, or validate** any part of the Sensor_ID → Condition_Evidence_ID → Inspection_Record_ID portion of that chain — it stops at the identity-anchor layer.

---

# Already established

Based on the full text, the following can now be stated as **confirmed, not provisional**:

1. The GUID-fragmentation-across-life-cycle-phase-files problem is explicitly named, analyzed, and diagrammed (Figure 1) in a peer-reviewed 2026 publication.
2. A concrete mechanism — a DOLCE endurant/perdurant-grounded, reification-pattern-based OWL 2 DL ontology (`BuildingElement` as persistent URI-identified endurant; `LifecyclePhase` as perdurant; GUID demoted to a phase-level backlink attribute) — has been proposed, implemented in Protégé, and validated via HermiT reasoner + 8 competency questions on a real (if small, manually-instantiated) 3-file Revit/IFC case study.
3. The paper explicitly and directly states (not merely implies) that this identity mechanism is intended as "the semantic anchor to which... sensor readings, inspection results, and maintenance events" can refer.
4. The paper explicitly claims, in its own comparison table (Table 1) against ifcOWL, BOT, PROPS, and OPM, to be the **first** construction ontology to ground element identity across lifecycle phases in a foundational ontology ("To our knowledge, BIM-Phase is the first construction ontology that grounds element identity across lifecycle phases in a foundational ontology").

---

# Remaining difference vs Paper 2

Now full-text-confirmed (not merely abstract-plausible):

1. **Manual vs. automatable identity linking.** Borkowski's cross-phase identity matching (the step that actually links `wall-W01` across three GUIDs) is explicitly performed by human expert judgement/heuristics, not automated or deterministically validated — a self-acknowledged limitation. If Paper 2's core chain implies a deterministically validated or auditable identity-linking step (consistent with its "deterministic integrity validation" and "deliberate invalid-link testing" requirements), this remains clearly distinct and unaddressed by Borkowski.
2. **No Condition_Evidence_ID or Inspection_Record_ID as first-class, accountable entities.** Borkowski's crack/inspection/repair content is folded into bare property-value changes on the endurant, with zero accountability fields (no performer/reviewer/approver/status/supersession) anywhere in the ontology.
3. **No deliberate identity-mapping negative/invalid-case testing.** Only one schema-level axiom-violation test was performed; none of the orphan/duplicate/wrong/stale/conflicting-mapping taxonomy was tested.
4. **No evidence validity/applicability concept** in the strict sense used by this correction pass (valid-time, protocol/configuration applicability, supersession-of-evidence) — confirmed absent, not merely unconfirmed.
5. **No forward/reverse traceability across a multi-record, cross-system chain** — Borkowski's traceability (CQ1–CQ8) is confined to querying one endurant's own property/state history across its own phases; it does not traverse Sensor→Evidence→Inspection-record boundaries.
6. **Small, single-case, manually-instantiated validation** (1 building, 3 elements, 27 reification instances) — explicitly and repeatedly flagged by the authors as a scale/generalizability limitation, not resolved.
7. **No CDE/ISO 19650-style model-revision governance** — phase ordering is by file-creation chronology only, not integrated with a formal Common Data Environment revision-status concept, which Paper 2's Gate 2 ("BIM information readiness/governance") plausibly requires.

---

# Novelty threat assessment

**HIGH — specifically and narrowly to Paper 2's "identity governance" / GAP-B sub-claim. Confirmed NOT to extend to a VERY_HIGH threat against Paper 2's full 8-component core contribution, because 6 of those 8 components (evidence provenance beyond a bare source-file backlink, evidence validity/applicability, accountable inspection records, forward/reverse cross-system traceability, deterministic multi-hop integrity validation, and deliberate invalid-link testing of the identity-mapping kind) are confirmed absent from Borkowski's paper.**

**Reasoning:**
- This rating is **upgraded from the prior provisional MODERATE** (assigned when only the abstract was available) now that full-text reading confirms — rather than merely suggests — a concrete, implemented, peer-reviewed mechanism that directly and precisely overlaps Paper 2's identity-governance component: naming the exact problem (GUID fragmentation across phase files), proposing a persistent URI-based identifier independent of GUIDs, and validating it (at small scale) via reasoner + competency questions on a real Revit/IFC case study. The paper's own claim to be "the first construction ontology that grounds element identity across lifecycle phases in a foundational ontology" is a direct, explicit priority claim over the same territory.
- It is **not rated VERY_HIGH** because: (a) the identity-linking mechanism itself is manual/non-automated, unlike what a "deterministic traceability validation" (Gate 3) framing would need; (b) it categorically does not address evidence provenance beyond a bare backlink, evidence validity/applicability, inspection-record accountability, or deliberate identity-mapping negative testing — i.e., 6 of Paper 2's 8 stated core-contribution components; (c) validation is small-scale and self-acknowledged as non-generalized.
- **This confirms, rather than merely suggests, that Paper 2 cannot claim novelty for the "identity governance" component in isolation** (see "Already established" and Final Decision Q2 in file 06). Paper 2's defensible novelty must rest on the *integration* of identity governance with the remaining 6 components into one verifiable, deterministically-validated, cross-system chain — which Borkowski does not attempt.

---

# Claim → Evidence → Limitation → Implication

**CLAIM:** Borkowski et al. (2026) is a full-text-confirmed, directly overlapping novelty threat to Paper 2's identity-persistence-across-model-revisions sub-claim (GAP-B), via a concrete, implemented, validated (small-scale) DOLCE-based ontology that separates a persistent URI-identified endurant from GUID-carrying, file-bound phase instances.

**EVIDENCE:** Full text read in its entirety (26/26 pages) from item key `CVGD2BLV` (child attachment of Zotero item `JSYCVGH9`, a duplicate record of `NQ3KGDWN`). Direct quotations reproduced above for: the research problem (Sec. 1, Fig. 1), the identity mechanism (Sec. 3.1–3.2), the IFC translation rules and their manual identity-matching step (Sec. 3.3), the case study (Sec. 4.1–4.2), the competency-question validation (Sec. 4.3, Table 3), the one deliberate axiom-violation negative test (Sec. 5.1), the explicit sensor/inspection/maintenance-anchor statement (Sec. 5.1), and the self-acknowledged limitations (Sec. 5.2) including the manual, non-automated, small-scale nature of the validation.

**LIMITATION:** This review remains bounded by what is stated or directly demonstrable from the published text; it cannot verify claims about real-world deployability, generalization to large/federated BIM models, or behavior of the proposed automatic converter (explicitly stated as *future* work, not yet built). The prior correction pass's `FULL_TEXT_NOT_AVAILABLE` conclusion was itself an artifact of a duplicate-item/attachment-linking issue in this Zotero library (Zotero UI vs. MCP tool discrepancy), now resolved and documented above; no Zotero metadata was altered in resolving it.

**IMPLICATION:** The Gap Audit (file 06) and Evidence Matrix (file 05) must now treat Borkowski et al. (2026) as a **HIGH, full-text-confirmed novelty threat specifically to the identity-governance/GAP-B sub-claim**, while explicitly noting it leaves Paper 2's other 6 core-contribution components untouched. Per this task's own freeze rule (file 06, Section 10–11), the literature gap can now move from `NOT_READY_TO_FREEZE`/`CONDITIONAL_FREEZE` toward `FULL_FREEZE` **only if** no other unread novelty threat remains — see file 06 for the final freeze determination.
