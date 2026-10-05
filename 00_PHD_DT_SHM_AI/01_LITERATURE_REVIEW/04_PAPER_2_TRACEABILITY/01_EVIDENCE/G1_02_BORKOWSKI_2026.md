# G1_02 -- Borkowski, Jarema, Kładź & Smoliar (2026)

**Temporally Qualified Building Elements: A DOLCE-Based Ontology for Phase-Dependent Identity and Change Tracking in BIM Models.** Technologies, 14(7), 413. DOI: 10.3390/technologies14070413. Zotero key: NQ3KGDWN.

**Source read:** ABSTRACT ONLY. No PDF attachment exists for this item in Zotero (confirmed via `zotero_get_attachment_path` and `zotero_get_item_fulltext` during Stage B PDF-availability verification). Per task instructions, this item was retained in the corpus despite lacking a PDF because its content is highly load-bearing for GAP-B, and is documented here using its unusually detailed publisher abstract as the sole evidence source. All answers below are conservatively bounded by what the abstract states; anything not stated is marked NOT_REPORTED or EVIDENCE_INSUFFICIENT rather than inferred as NO.

---

**Q1 -- Research problem.** CLAIM (from abstract): IFC does not define a formal mechanism linking the same physical building element across successive life-cycle phases; design, construction, and operation are recorded in separate IFC files, and the same element receives a *different* GUID in each, causing "fragmentation of the element's identity, loss of the history of property changes, and the inability to formulate cross-phase queries."

**Q2 -- Information architecture.** PARTIAL (abstract-level only). The proposed BIM-Phase ontology distinguishes a building element as a DOLCE *endurant* from its life-cycle phases as DOLCE *perdurants*, with phase properties/relations represented via a reification pattern in OWL 2 DL. No source->mechanism->record->output chain is described; the architecture is ontological (endurant/perdurant + reification), not a data/record pipeline.

**Q3 -- Identity representation.** YES. Explicitly and centrally about IFC GUID as the identity mechanism, and about its failure to persist across phases.

**Q4 -- Identity persistence across model revisions.** NO (this is the paper's central finding, stated as an unresolved problem in current practice, which the paper then proposes to address). CLAIM: "different GUIDs in each [phase file]... fragmentation of the element's identity." EVIDENCE: stated directly in the abstract as the motivating problem, validated (per abstract) via a case study tracking three structural elements (external wall, floor slab, column) across three life-cycle phases in a single-family residential building modeled in Autodesk Revit, with eight competency questions all "answered correctly on the published knowledge graph" and logical consistency confirmed by the HermiT reasoner. LIMITATION: full validation methodology, dataset size, and generalizability cannot be assessed without the PDF (EVIDENCE_INSUFFICIENT beyond the abstract's summary claims). IMPLICATION: this is the single most direct and recent (2026) statement in the entire targeted corpus of the identity-fragmentation problem that Paper 2's core chain (Sensor_ID -> BIM_GUID/IFC identity -> ...) must confront, and it proposes a competing solution (a DOLCE-based phase-ontology layer with persistent, phase-independent identifiers) rather than leaving the gap open.

**Q5a-d -- Four provenance types.** NOT_REPORTED. Abstract does not discuss source/measurement/processing/human-actor provenance; its scope is change-tracking of element properties across phases, not inspection or sensor-evidence provenance.

**Q5e -- Review/approval provenance.** NOT_REPORTED.

**Q6 -- Model/version context.** YES (at ontology-design level). The endurant/perdurant distinction is explicitly a model/version-context mechanism -- each phase is a perdurant instance of the enduring element.

**Q7 -- Validity/applicability scope.** PARTIAL. Abstract states validation "using an example of a single-family residential building" with three structural element types across three phases -- a small, single-case validation; scope beyond this is EVIDENCE_INSUFFICIENT without the PDF.

**Q8 -- Forward and reverse traceability.** PARTIAL. The eight competency questions "covering scalar, constitutional, and mereological changes" imply query-based traceability of property change across phases, which functions as a form of forward/reverse traceability of element state, though not framed in Paper 2's Sensor->Record vocabulary.

**Q9 -- Validation method.** YES (per abstract). Case-study validation (3 elements x 3 phases, Autodesk Revit), 8 competency questions all answered correctly against a published knowledge graph, plus formal logical-consistency verification via the HermiT OWL reasoner.

**Q10 -- Deliberate invalid-case testing.** EVIDENCE_INSUFFICIENT. Abstract does not mention orphan/duplicate/stale-GUID or broken-reference negative testing; cannot be confirmed without the PDF.

**Q11 -- G3 record fields.** NOT_APPLICABLE -- this is a G1 identity paper.

**Q12 -- ALREADY_ESTABLISHED vs REMAINING_GAP.** **This paper is the strongest novelty threat identified in the entire targeted review.** CLAIM: it explicitly names the exact mechanism-level problem (GUID fragmentation across IFC life-cycle-phase files) that would otherwise be assumed an open gap for Paper 2, and proposes a working, reasoner-validated solution (BIM-Phase / DOLCE ontology layer) with a concrete recommendation to add "persistent, phase-independent identifiers of building elements alongside IFC GUIDs." IMPLICATION: Paper 2 cannot claim novelty for "recognizing that IFC GUIDs do not persist across life-cycle-phase files" or for "proposing a persistent-identifier layer alongside IFC GUIDs" in the abstract sense described here -- that specific framing is already claimed by this 2026 publication. Paper 2's positioning must be differentiated (e.g., by grounding persistence in a verifiable, auditable multi-record traceability framework spanning Sensor/Evidence/Inspection records rather than a pure ontology/reasoner-validated change-tracking layer) or must explicitly engage with and distinguish itself from this paper. LIMITATION on this conclusion: based on abstract only; the actual mechanism, its practical deployability outside a single-case Revit demonstration, and whether it addresses record-level accountability (G3) at all remain EVIDENCE_INSUFFICIENT until the full text is read (explicitly out of scope for this task per the STOP CONDITION).
