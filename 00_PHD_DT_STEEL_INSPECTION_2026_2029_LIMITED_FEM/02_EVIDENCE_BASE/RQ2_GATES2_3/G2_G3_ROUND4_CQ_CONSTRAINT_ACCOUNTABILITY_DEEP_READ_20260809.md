# G2-G3 Round 4 — Deep Read: CQ Method, Constraint Execution, FM Work Linkage, Accountability, ifcOWL

**Version:** v1.0
**Date:** 2026-08-09
**Status:** EVIDENCE RECORD (immutable once accepted) | **Source-of-truth level:** evidence, not navigation authority
**Supersedes:** None. | **Superseded by:** None.
**Architecture:** Limited-FEM, Traceability-Core
**Governance read before writing:** `02_EVIDENCE_BASE/RQ2_GATES2_3/00_README_START_HERE.md` (v2.2, 2026-08-04); `G2_G3_ROUND1_DEEP_READ_AND_NOVELTY_BOUNDARY.md`; Round 2, Round 3A, Round 3B section headings.

## 0. Scope and conventions

Corpus for this round: five papers from `DEEP_READ_20.07.2026/` that were **not** deep-read in Rounds 1–3B.

- `PDF p.` = page index of the PDF file. Printed journal page given in brackets where it differs.
- Labels: `SOURCE-VERIFIED` (paper states it, locator given); `TUTOR-EXPLANATION` (reconstruction to make implicit logic explicit); `THESIS-APPLICATION` (proposed use, not an author claim); `UNKNOWN` / `Evidence is currently insufficient.`
- Novelty language is bounded: *within the papers deep-read in Rounds 1–4*.
- FEM firewall applies: nothing in this record uses or implies calibrated FEM, damage diagnosis, severity, RUL, predictive maintenance, or a weighted Health Index.
- Text was extracted with PyMuPDF from the original PDFs; every locator cited below was read from that extraction against the page markers. Figures and diagrams were **not** visually inspected — claims resting on figure content only are marked `Evidence is currently insufficient.`

## 1. Corpus identification (15 PDFs in DEEP_READ_20.07.2026)

| # | File | Paper | Status |
|---|---|---|---|
| 1 | `(Antunes, 2024)_Ontology-based...pdf` | Lorvão Antunes et al. (2024), *ISWA* 22, 200366 | Already deep-read (Round 1) |
| 2 | `Gate 2.1 - 1-s2.0-S2667305324000425-main.pdf` | **Duplicate of #1** | Duplicate |
| 3 | `Gate 2.1 - caos-9.pdf` | **Keet & Khan (2025)**, *Characterising Competency Questions for Ontologies*, JOWO/FOIS 2025, CEUR-WS | **Round 4 — NEW** |
| 4 | `kim2018.pdf` | **Kim, K. et al. (2018)**, *Autom. Constr.* 87, 173–187 | **Round 4 — NEW** |
| 5 | `buildings-15-02633.pdf` | **Jia, L. et al. (2025)**, *Buildings* 15, 2633 | **Round 4 — NEW** |
| 6 | `Lee et al. (2021) — Provenance và accountability.pdf` | **Lee, D. et al. (2021)**, *Autom. Constr.* 127, 103688 (DT + blockchain) — **not** Lee, Y.-C. et al. (2021) from Round 1 | **Round 4 — NEW** |
| 7 | `pauwels2016.pdf` | **Pauwels & Terkaj (2016)**, *Autom. Constr.* 63, 100–133 | **Round 4 — NEW** |
| 8 | `sustainability-11-04583.pdf` | Wan et al. (2019) | Already deep-read (Round 2) |
| 9 | `10.1016@j.autcon.2020.103088.pdf` | Isailović et al. (2020) | Already deep-read (Round 2) |
| 10 | `applsci-16-04642.pdf` | Piras et al. (2026) | Already deep-read (Round 3A) |
| 11 | `Çelik et al. (2023) — BIM data provenance.pdf` | Çelik, Petri & Barati (2023), *Computers in Industry* | Already deep-read (Round 3B) |
| 12 | `1-s2.0-S0926580519314785-main.pdf` | Boje, Guerriero, Kubicki & Rezgui (2020), *Autom. Constr.* — semantic Construction DT review | Not read in Round 4 — Chapter 2 background candidate |
| 13 | `Gate 2.3 2026_19-ITcon-Chen.pdf` | Chen, Lin, Sui et al. (2026), *ITcon* 31, 420, DOI 10.36680/j.itcon.2026.019 | Not read — IFC model **generation**, not traceability |
| 14 | `Johannes et al. (2021) Identifying_Maturity...pdf` | Johannes, Voordijk, Adriaanse & Aranda-Mena (2021) | Not read — WP4 / maturity, secondary |
| 15 | `buildings-15-01312.pdf` | Yang, S.-W., Lee, Y. & Kim, S.-A. (2025), *Buildings* 15, 1312 | Not read — real-time monitoring demo |

**Filename caution (control finding):** file #6 is labelled "Lee et al. (2021) — Provenance và accountability", but it is **Dongmin Lee et al., DT + blockchain**, a different paper from Round 1's **Lee, Y.-C., Eastman & Solihin (2021)**, *JCDE* 8(1), 97–114. Two distinct "Lee et al. (2021)" citations now exist in the evidence base. Citation keys must be disambiguated before any Paper 2 draft.

## 2. Per-paper evidence extraction

### 2.1 Keet & Khan (2025) — Characterising Competency Questions for Ontologies

**Citation:** Keet, C. M., & Khan, Z. C. (2025). Characterising Competency Questions for Ontologies. In *Proceedings of the Joint Ontology Workshops (JOWO) — Episode XI*, co-located with FOIS 2025, Catania, Italy. CEUR-WS, ISSN 1613-0073. Published 2026-03-02.
**Academic role:** methodological authority on **what a CQ is and what makes it faulty**. Closest methodological reference for the G2 competency-question registry.

| Claim | Evidence | Validation used | Limitation | Thesis implication |
|---|---|---|---|---|
| Very limited guidance exists for formulating CQs or judging whether a CQ is good; ambiguity and unusable formulations result | Abstract, PDF p. 1; §2, PDF pp. 2–3 | Literature analysis | Positional claim, not measured | Gap statement usable for Paper 2 §CQ methodology (`CITE`) |
| CQs fall into five principal types: Scoping (SCQ), Validation (VCQ), Foundational (FCQ), Relationship (RCQ), Metaproperty (MpCQ) | Abstract p. 1; §3.2, PDF pp. 4–8, Definitions 1–6, Figs. 1–4 | Conceptual model (QuO) + FOL formalisation | Authors state the list may not be exhaustive (§3.2, PDF p. 4); no user-based evaluation yet (§6, PDF p. 13) | G2 CQ registry must **type** each CQ, not list them flat (`ADAPT`) |
| **SCQ need not be answerable or even formalisable; VCQ must be both formalisable and answerable**, and the logic of the VCQ must not exceed the logic of the ontology (`Lv ⊆ Lo`) | §3.2, PDF p. 5, Definition 3 and surrounding text | Definitional | Constraint is language-relative; the authors call it "debatable" | **Decisive for G2**: scoping questions and acceptance-test questions are different artifacts and must be separated (`ADAPT`) |
| Questions that verify disjointness or cardinality are **not CQs**; they are general constraint-checking queries | §4.2, PDF pp. 11–12, bulleted examples | Definitional/analytical | Boundary is argued, not empirically tested | **Decisive for G2**: the constraint catalogue and the CQ registry are two different artifacts with different acceptance semantics (`ADAPT`) |
| A CQ can be faulty for four causes: (i) syntax/semantics, (ii) expressivity mismatch of query or ontology language, (iii) ontology content, (iv) mismatch with its own CQ type | §4.2, PDF p. 11 | Analytical taxonomy with examples | Only causes (ii) and (iv) elaborated, "due to space limitations" | Gives G2 a **CQ quality-review checklist** (`ADAPT`) |
| Problematic question patterns are named: vague quantifiers ("to what extent"), too-broad how-to questions, requests for modelling instruction, imprecise reference | Fig. 6, PDF p. 12 | Annotated examples | From figure text; sampling only | CQ authoring rules for the registry (`ADAPT`) |
| ROCQS repository contains 558 CQs across all types, FAIR-compliant, with annotated problematic questions | §4.2, PDF p. 12 | Artifact release | Not independently validated; edit access planned, not delivered | External benchmark for CQ coverage (`BENCHMARK`) |
| Different CQ types map to different NeOn methodology stages | §4.1.2, PDF pp. 9–10, Fig. 5 | Mapping proposal; "leaving the how for future work" | Figure-based; no evaluation of the mapping | Weak evidence — use only as a structuring aid |
| SewerNet use case shows each CQ type being used, including an MpCQ that separated `Maintenance` (atelic, `dolce:accomplishment`) from `Repair` | §4.1.1, PDF p. 9 | Single retrospective use case | One ontology, retrospective narration, no comparison against a no-CQ baseline | **Directly relevant analogue**: the Maintenance/Repair distinction mirrors the thesis `Action_Record` semantics (`CITE`) |

**Component audit against the thesis chain**

| Component | Yes / Partial / No | Evidence |
|---|---|---|
| CQ typology and definitions | Yes | §3.2, PDF pp. 4–8 |
| CQ answerability / formalisability criterion | Yes | Definition 3, PDF p. 5 |
| CQ-versus-constraint boundary | Yes | §4.2, PDF pp. 11–12 |
| Expected-answer shape as a required CQ field | Partial | Answer expectations discussed per type (pp. 5–8); no formal "expected answer" slot in the QuO model |
| Acceptance criteria / pass–fail execution for a CQ set | No | Not addressed |
| Domain content for inspection, action, status, BIM identity | No | Domain-neutral paper |
| User-based evaluation of QuO / ROCQS | No | Explicit future work, §6, PDF p. 13 |

**Verdict:** conceptual model + repository present; empirical evaluation of effectiveness absent (`AUTHOR-STATED` future work, §5–6, PDF pp. 12–13).

---

### 2.2 Kim, K. et al. (2018) — Integration of IFC objects and FM work information using Semantic Web

**Citation:** Kim, K., Kim, H., Kim, W., Kim, C., Kim, J., & Yu, J. (2018). Integration of ifc objects and facility management work information using Semantic Web. *Automation in Construction, 87*, 173–187. https://doi.org/10.1016/j.autcon.2017.12.019
**Academic role:** closest prior art for **linking maintenance work records to IFC objects** — i.e. the `Inspection_Record` / `Action_Record` ↔ BIM component edge.

| Claim | Evidence | Validation used | Limitation | Thesis implication |
|---|---|---|---|---|
| BIM-based facility information from construction is hard to access in O&M because FMS DB structure is work-activity-based while BIM is object-based | Abstract, PDF p. 1; §6, PDF p. 14 | Positional + practice survey of five Korean FM companies (Table 1, PDF p. 9) | Convenience sample, one country, no sampling frame | Gap statement for Paper 2 (`CITE`) |
| An OWL ontology links three concept groups — IFC concepts, COBie concepts, Work concepts (work area, work cycle, work category) | §3.1, PDF p. 4, Figs. 2–4 (Figs. 3–4 on PDF p. 5) | Ontology design | Class list not published in full; no CQ registry | Reusable ER pattern; **not** a novelty claim available to the thesis (`AVOID` claiming novelty) |
| Six-layer architecture: IFC extraction, COBie exchange, FMS data management, ontology management, reasoning (Jena + BOSSAM), query (SPARQL/ARQ) | §3.2, PDF pp. 5–9, Fig. 6 (PDF p. 6) | Architecture description + implementation | Layered description only; no interface contract, no versioning | Shows the **implementation stack is not the contribution** (`AVOID`) |
| Work scope is attached to IFC objects via `IfcRelSpaceBoundary` → `relatedElements` → `IfcBuildingElement`, with material via `IfcMaterialLayerSetUsage` | §3.2 layer 1, PDF p. 7, Figs. 7–8; extracted values Tables 3–4, PDF pp. 10–11 | Executed extraction on a sample IFC file | Space-boundary elements only; deliberately excludes furniture/other elements to bound scope (PDF p. 7) | **Direct warning**: the component an evidence item attaches to depends on a chosen IFC relationship path; G2 must fix that path explicitly (`ADAPT`) |
| Case study: 590 occasional architectural maintenance records (Company E, 2016-01-01 to 2016-06-02) linked to buildingSMART "common BIM file – office"; Level 1 has 60 spaces, 262 walls, 66 doors, 25 windows, 2 stairs, 1 elevator, 1814.786 m² | §4.1, PDF pp. 9–10; §4.2, PDF p. 10, Fig. 9 | Single case, real records + synthetic reference model | Records are real, model is a **reference sample file, not the actual building** — no as-is correspondence | **Critical**: this is a linkage demonstration, not a validated correspondence. Directly analogous to a risk in G3 (`AVOID`) |
| SPARQL retrieval returned 12 maintenance records for space '139' (meeting room), resolving to 7 wall objects with two finish materials | §4.2.1, PDF pp. 11–12, Table 5 (PDF p. 12) | Executed query | Happy-path retrieval; no precision/recall, no ground truth, no negative case | Forward retrieval only — same boundary as Antunes (Round 1) (`BENCHMARK` weakly) |
| Adjacent spaces sharing an IFC object (wall #31982, door #66803 between spaces 139 and 140) let records be grouped across spaces | §4.2.2, PDF pp. 12–13, Table 6 (PDF p. 12) | Executed query | Two spaces, two objects | Shows component-level (not space-level) linking changes the result set |
| Maintenance works at a shared building element in two adjacent spaces "increases the resulting quantity of work records by about 200%" | §5, PDF p. 14 | Stated outcome of the case | **No derivation, no denominator, no baseline definition, no uncertainty.** Quantity retrieved is not the same as retrieval quality | **Do not cite as a performance result.** `Evidence is currently insufficient.` Use only as an illustration that linking granularity changes recall |
| Author-stated limitations: BIM models are seldom updated in FM practice; facility managers lack BIM/Semantic Web skill; validation of the handed-over BIM/COBie is future work; updating as-is conditions of an existing building needs a method | §4.2.2, PDF p. 13; §6, PDF p. 14 | — | — | **Model-version drift is an author-stated open problem.** Supports the thesis' `Model_Version_ID` requirement (`CITE`) |

**Component audit**

| Component | Yes / Partial / No | Evidence |
|---|---|---|
| BIM/IFC identity | Partial — IFC entity **instance numbers** (`#32465`) used as identifiers, not `GlobalId` | Tables 3–4, PDF pp. 10–11 |
| Inspection record | No — records are maintenance work entries, not inspection findings | Table 2, PDF p. 9 |
| Action record | Partial — date, area, element, work contents, labours, work time, floor; no ID, no owner, no approval, no verification | Table 2, PDF p. 9 |
| Condition evidence | No — no defect/condition object; work text only | Table 2, PDF p. 9 |
| Status event / history | No | — |
| Provenance / accountability | No — no actor identity, reviewer or approver field | — |
| Competency questions | No — ad hoc SPARQL, no pre-specified CQ registry | §4.2.1, PDF p. 11 |
| Executable constraints | No — reasoning is classification, not integrity checking | §3.2 layer 5, PDF p. 8 |
| Deliberate negative tests | No | — |
| Forward traceability | Partial — object → related work records | Table 5, PDF p. 12 |
| Reverse traceability | No — no work record → originating evidence/inspection query | — |
| Round-trip parity | No | — |
| Human review | No | — |

**Verdict:** implemented ontology + executed forward retrieval on one case; **identity governance, record schema, integrity constraints, negative tests, reverse traceability and accountability all absent.** The reported "200% more records" is an unsupported effectiveness statement.

---

### 2.3 Jia, L. et al. (2025) — A Semantic Web and IFC-Based Framework for Automated BIM Compliance Checking

**Citation:** Jia, L., Chen, M., Chen, C., & Jin, Y. (2025). A Semantic Web and IFC-Based Framework for Automated BIM Compliance Checking. *Buildings, 15*, 2633. https://doi.org/10.3390/buildings15152633
**Academic role:** most recent competitor for **executable rule checking over IFC-derived RDF** — relevant to the G2 constraint catalogue and query contract.

| Claim | Evidence | Validation used | Limitation | Thesis implication |
|---|---|---|---|---|
| A code provision decomposes into three parts: **constrained object, constrained content, preconditions** | §3, PDF p. 4; §5.2.1, PDF pp. 15–16 | Analytical decomposition | Applied to Chinese residential code only | **Transferable rule-authoring skeleton** for the G2 constraint catalogue (`ADAPT`) |
| Quantifiable descriptions reduce to three types — property, construction, spatial (positional / distance) — with named element structures | §5.2.1, PDF pp. 15–16, Table 7 (PDF p. 16) | Analytical classification | Non-quantifiable ("basic requirement") provisions excluded from the mechanism | Gives a **rule typology**; the thesis needs a fourth family (referential integrity) not present here (`ADAPT`) |
| SPARQL query templates are given per description type, with `[]` variables bound to ontology classes/properties | §5.2.2, PDF pp. 16–18, Tables 8–9 | Template design + worked examples (Figs. 9–10) | Templates are illustrative; no coverage claim over the code | Reusable **query-template pattern** for CQ formalisation (`ADAPT`) |
| Jena rules (not SWRL) were chosen because SWRL cannot do coordinate transformation/vector calculation, scales poorly on large IFC-derived triple sets, and handles long attribute paths badly | §5.1, PDF p. 11 | Design rationale | **No measured comparison** — no runtime numbers, no triple counts, no SWRL baseline executed | Rationale is plausible but **unevidenced**. `Evidence is currently insufficient.` for any performance claim |
| Mapping rules bridge IfcOWL and a domain "building object ontology" in three families: entity correspondence, entity object information (attributes + position), inter-entity relationships | §5.1.1–5.1.3, PDF pp. 11–15, Tables 3–6 | Rule listings | Listings are examples, not a complete rule set; no rule IDs, no severity, no expected-violation semantics | **Key gap for the thesis to occupy**: rules exist, but no violation taxonomy or oracle (`ADAPT`) |
| Case: 21-storey residential unit, uniform 5th–21st floor; IFC exported, converted by an IFC-to-RDF tool, stored in Jena TDB, served by Fuseki | §6.1, PDF p. 19, Figs. 11–12 | Prototype system | Single building, single code (GB 50096-2011), one standard floor | Feasibility, not generalisation |
| Executed check: "clear height of balcony railings in buildings with seven or more storeys shall not be less than 1.10 m" returned **two `IfcRailing` entities at 900 mm**, confirmed by visual location match in BIMversion | §6.2, PDF pp. 20–21, Figs. 13–14 | Executed query + visual cross-check | **n = 1 rule, 2 hits.** No confusion matrix, no false-positive/false-negative accounting, no ground-truth manifest of known violations | **The nearest thing in the whole corpus to a negative test — and it still fails the strict criterion**, because the 900 mm railings were not deliberately seeded with a predefined expected outcome (`AVOID` mislabelling) |
| Railings lack direct spatial association in IFC, forcing bounding-box coordinate containment inference | §6.2, PDF p. 21, Fig. 15 | Rule implementation | Bounding-box containment is an approximation; axis-aligned assumption | **Direct warning for G2**: not every component the thesis needs to attach evidence to has a usable IFC relationship; some links must be *derived*, and derived links need their own integrity test (`ADAPT`) |
| Author-stated limitations: ontology insufficient for complex buildings; Jena inference performance degrades badly at scale (hundreds of thousands of artifacts, deep rule nesting); ontology and rules are bound to Chinese national standards | §7, PDF pp. 22–23 | — | — | Scalability and locale-binding are `AUTHOR-STATED` limitations (`CITE`) |

**Component audit**

| Component | Yes / Partial / No | Evidence |
|---|---|---|
| BIM/IFC identity | Partial — IfcOWL individuals; no `GlobalId` governance or persistence discussion | §5.1, PDF pp. 11–15 |
| Executable constraints | Yes — Jena mapping rules + SPARQL query rules, executed on Fuseki | §5.1–5.2, PDF pp. 10–18; §6.2, PDF pp. 20–21 |
| Rule typology / templates | Yes | Table 7, PDF p. 16; Tables 8–9, PDF pp. 17–18 |
| Competency questions | No — code provisions, not CQs; no expected-answer registry | — |
| Deliberate negative tests | No (under the strict four-condition criterion) | §6.2, PDF pp. 20–21 |
| Referential-integrity rules (orphan, duplicate, wrong target type) | No — rules are domain-value and spatial, not link-integrity | Tables 3–6 |
| Condition evidence / inspection / action / status | No — design-phase compliance only | Whole paper |
| Provenance / accountability | No | — |
| Reverse traceability, round-trip parity | No | — |

**Verdict:** implemented and executed rule-checking pipeline; **no integrity-rule family, no fixture manifest, no oracle, no domain lifecycle chain.**

---

### 2.4 Lee, D. et al. (2021) — Integrated digital twin and blockchain framework for accountable information sharing

**Citation:** Lee, D., Lee, S. H., Masoud, N., Krishnan, M. S., & Li, V. C. (2021). Integrated digital twin and blockchain framework to support accountable information sharing in construction projects. *Automation in Construction, 127*, 103688. https://doi.org/10.1016/j.autcon.2021.103688
**Academic role:** accountability/immutability competitor. Pairs with Çelik et al. (2023) from Round 3B.

| Claim | Evidence | Validation used | Limitation | Thesis implication |
|---|---|---|---|---|
| Digital-twin data is vulnerable to overwriting; historical state of virtual assets can be lost, and DT data management (storage, immutability, traceability) "has not been thoroughly realized" | §2, PDF p. 2 | Positional argument from literature | Positional | **Strong gap statement for the thesis' `Status_Event` history requirement** (`CITE`) |
| Framework stores only a small **compliance statement** on-chain; bulk sensor and BIM data go to a distributed ledger | §4.1, PDF p. 3, Fig. 1; §4.2, PDF pp. 3–4, Fig. 2 | Architecture | Selective-storage decision is asserted, not evaluated against alternatives | **Transferable design principle**: separate the *evidence payload* from the *attestation record* (`ADAPT`) |
| Case: virtual robotic assembly of a 49-brick mock-up bridge; as-planned BIM 876 MB; 49 compliance statements of ~0.5 kB each; 49 blocks generated | §5.1, PDF p. 5; §5.2, PDF p. 5, Figs. 3–6 | Executed case on Azure/Quorum + Unity | **Virtual/hypothetical sensors** ("the authors assumed that virtual hypothetical sensors … are attached to each brick", §5.1, PDF p. 5). No physical deployment | **Do not cite as field evidence.** It is a simulated pipeline test (`AVOID`) |
| 3 of 10 nodes were **intentionally given invalid signatures** by modifying previous blocks; those nodes were excluded from consensus; valid nodes synchronised at 2.41 s, all nodes at 3.42 s | §5.1, PDF p. 5; §5.2, PDF pp. 5–6, Fig. 7 | Executed consensus test | Single scenario; no repetition, no variance, no load variation; compliance check limited to brick location and type | **This is the closest thing in Rounds 1–4 to a deliberate invalid-fixture test with a predefined expected outcome** — but it tests *ledger consensus*, not *domain referential integrity* (`BENCHMARK`) |
| Compliance checking compares as-built against as-planned BIM to produce a legally-framed statement | §4.1, PDF p. 3; §5.1, PDF p. 5, Fig. 4 | Implemented module | Only location and type checked, "for the simplicity of testing" | Narrow comparator; the statement's *content model* is not published |
| Blockchain trilemma: security, scalability and decentralisation cannot all be maximised; the proof of concept was a **private** chain with inherent security/centralisation risk | §6, PDF p. 8 | Author-stated discussion | — | **Reason not to adopt blockchain in G2/G3.** Adopting it imports an unresolved trilemma and a new proof obligation without serving RQ2 (`REJECT` for the current Gate) |

**Component audit**

| Component | Yes / Partial / No | Evidence |
|---|---|---|
| Immutable event history | Yes — chained blocks with timestamps | §4.1, PDF p. 3; §5.2, PDF pp. 5–6 |
| Attestation separated from payload | Yes | §4.1, PDF p. 3 |
| Deliberate invalid fixture + expected outcome + execution + comparison | Partial — satisfied for **node signature validity**, not for domain records | §5.1, PDF p. 5; §5.2, PDF p. 6 |
| Accountable human review (reviewer, approver, rationale, authorisation) | No — nodes consent cryptographically; no role model, no rationale, no separation of duties | §5.2, PDF pp. 5–6 |
| Condition evidence / inspection record / action record | No | Whole paper |
| BIM/IFC identity governance | No — bricks, not IFC `GlobalId` | §5.1, PDF p. 5 |
| Reverse traceability, round-trip parity | No | — |
| Field validation | No — hypothetical sensors | §5.1, PDF p. 5 |

**Verdict:** implemented and executed simulated pipeline demonstrating traceable, immutable attestation; **domain semantics, human-review accountability and field evidence absent.**

---

### 2.5 Pauwels & Terkaj (2016) — EXPRESS to OWL for construction industry: ifcOWL

**Citation:** Pauwels, P., & Terkaj, W. (2016). EXPRESS to OWL for construction industry: Towards a recommendable and usable ifcOWL ontology. *Automation in Construction, 63*, 100–133. https://doi.org/10.1016/j.autcon.2015.12.003
**Academic role:** the foundational reference for the IFC→OWL representation that Kim (2018), Jia (2025) and Antunes (2024) all sit on top of. Decisive for the G2 **implementation-neutrality** decision.

| Claim | Evidence | Validation used | Limitation | Thesis implication |
|---|---|---|---|---|
| Absence of a single agreed ifcOWL ontology means applications are built on slightly different ontologies and "work as isolated examples" | §1.3.2, PDF p. 4 [p. 103] | Positional analysis of prior converters | Positional | **Direct support for keeping the G2 specification implementation-neutral** (`CITE`) |
| Three design criteria, in order: (1) stay in OWL2 DL; (2) match the EXPRESS schema as closely as possible; (3) primarily support IFC-file→RDF conversion, not authoring from scratch | §1.3.4, PDF pp. 4–5 [pp. 103–104]; restated §6, PDF p. 33 [p. 132] | Design decision with stated trade-offs | Criterion 1 is explicitly bought at a cost in reasoning performance (§1.3.4, PDF p. 4) | **Criterion 3 is the one that matters here**: ifcOWL is a *conversion target*, not an authoring schema (`CITE`) |
| Procedural `RULE` and `FUNCTION` declarations **cannot** be converted into OWL2 DL class expressions; `WHERE` rules are not included in the conversion | §6, PDF p. 33 [p. 132]; rationale §1.3.4, PDF p. 5 | Author-stated open issue | Partial conversion is possible per Terkaj & Šojić | **Decisive**: converting IFC to OWL **loses the schema's own constraint layer**. Any G2 constraint catalogue must be authored separately, not inherited from ifcOWL (`ADAPT`) |
| ifcOWL is a "maximal" OWL2 DL ontology and should later be decomposed into less expressive profiles | §6, PDF p. 33 [p. 132] | Author-stated future work | Not done in the paper | Performance risk if the thesis binds to ifcOWL; matches Jia's `AUTHOR-STATED` scalability limitation |
| Through ontological analysis, ifcOWL "might be greatly simplified so that it would become easier to use" | §6, PDF p. 33 [p. 132] | Author-stated future work, citing Borgo et al., Venugopal et al., de Farias et al. | Not demonstrated | Usability of ifcOWL is an `AUTHOR-STATED` open problem, not a solved base |
| Consistency checking is expected to happen in the native CWA BIM tool, not in the OWA RDF graph | §1.3.4, PDF p. 5 [p. 104] | Design rationale | Assumes a one-directional BIM→RDF workflow | **Warning**: if the thesis validates only in RDF, it validates in a world model (OWA) where "missing" ≠ "violation" (`ADAPT`) |

**Component audit**

| Component | Yes / Partial / No | Evidence |
|---|---|---|
| IFC→OWL schema conversion procedure | Yes | §3 (begins PDF p. 7); converter implementation §4.1, PDF p. 28 |
| Handling of INVERSE attributes | Yes, with stated exceptions | §3.6.5; restated §6, PDF p. 33 |
| Constraint layer (`RULE`/`FUNCTION`/`WHERE`) preserved | **No** | §6, PDF p. 33 |
| Identifier governance / `GlobalId` persistence across files or versions | No | Not addressed |
| Domain chain (evidence, inspection, action, status) | No | Out of scope |
| Competency questions, negative fixtures, parity | No | Out of scope |

**Verdict:** implemented and documented converter with explicit, honest boundary statements. Its most important contribution to this thesis is a **negative** one: the IFC constraint layer does not survive the trip to OWL.

## 3. Cross-paper comparison (Round 4)

| Study | Main artifact | Identity | Domain chain coverage | CQ | Executable constraints | Deliberate negative test | Forward / reverse | Main missing element |
|---|---|---|---|---|---|---|---|---|
| Keet & Khan (2025) | CQ typology (QuO) + ROCQS (558 CQs) | n/a | None (domain-neutral) | **Method authority** | Explicitly *excludes* constraint queries from CQs | No | n/a | Empirical evaluation; acceptance semantics |
| Kim et al. (2018) | OWL ontology + 6-layer FM system | IFC instance `#id`, not `GlobalId` | Work record ↔ IFC object only | No | No | No | Forward partial; reverse no | Record schema, identity, integrity, review |
| Jia et al. (2025) | IfcOWL + domain ontology + Jena/SPARQL rules on Fuseki | IfcOWL individuals | None (design-phase) | No | **Yes, executed** | No (2 real 900 mm railings, not seeded) | Forward only | Integrity-rule family, oracle, coverage |
| Lee, D. et al. (2021) | DT (Unity) + private Quorum blockchain | Brick IDs | None | No | Compliance = location + type only | **Partial — 3/10 nodes seeded invalid, expected exclusion confirmed** | Forward only | Domain semantics, human roles, field data |
| Pauwels & Terkaj (2016) | EXPRESS→OWL converter, ifcOWL | n/a | None | No | **Constraint layer explicitly not converted** | No | n/a | Identity persistence; constraint preservation |

## 4. What Round 4 changes in the novelty boundary

### 4.1 Newly closed (must not be claimed as novelty)

1. **Linking maintenance/FM work records to IFC objects via a Semantic Web ontology** — Kim et al. (2018), §3–4, PDF pp. 4–13, implemented and queried. Round 1 had already closed inspection-side linkage via Antunes; Round 4 closes the work-record side.
2. **Deriving component association through IFC relationship paths (`IfcRelSpaceBoundary`) and through bounding-box containment when no relationship exists** — Kim §3.2, PDF p. 7; Jia §6.2, PDF p. 21.
3. **SPARQL/Jena rule templates for translating a written provision into an executable query** — Jia §5.2, PDF pp. 15–18.
4. **Separating a small immutable attestation record from a large evidence payload** — Lee, D. et al. §4.1, PDF p. 3.
5. **Typing competency questions and distinguishing scoping from validation questions** — Keet & Khan §3.2, PDF pp. 4–8. The thesis may *apply* this typology but cannot claim it.

### 4.2 Newly strengthened thesis positions

| Position | Strengthened by | Why |
|---|---|---|
| The G2 specification must be **implementation-neutral** | Pauwels §1.3.2 and §1.3.4, PDF pp. 4–5; §6, PDF p. 33 | Because ifcOWL is a conversion target whose own constraint layer is not preserved, binding the specification to ifcOWL would silently drop constraints |
| The **constraint catalogue and the CQ registry are two artifacts**, not one | Keet & Khan §4.2, PDF pp. 11–12 | Constraint-checking queries are explicitly *not* CQs |
| Every G2 CQ must carry a **type**, an **expected answer shape** and a **logic-expressivity check** | Keet & Khan Definition 3, PDF p. 5; §4.2, PDF p. 11 | Otherwise VCQs are unanswerable and the acceptance test is vacuous |
| **`Model_Version_ID` is mandatory**, not optional metadata | Kim §4.2.2, PDF p. 13; §6, PDF p. 14 | Author-stated: BIM models are seldom updated in FM practice; as-is updating is unsolved |
| **Referential-integrity rules are a distinct rule family** absent from prior art | Jia Tables 3–6, PDF pp. 11–15 (value + spatial rules only); Lee Y.-C. Round 1 (generic IFC/MVD only) | No paper in Rounds 1–4 executes orphan / duplicate / wrong-target-type / stale-crosswalk / illegal-transition fixtures over a domain chain |

### 4.3 Newly sharpened risk

**The "derived link" problem.** Jia §6.2, PDF p. 21 shows that `IfcRailing` has no direct spatial association and containment had to be *computed* from bounding boxes. Kim §3.2, PDF p. 7 shows component association was *chosen* to be `IfcRelSpaceBoundary`. `THESIS-APPLICATION`: for a coastal steel portal frame, the component a `Condition_Evidence` item attaches to may likewise have no single canonical IFC relationship. G2 must therefore declare, per link type, whether the link is **asserted** or **derived**, and derived links require their own integrity rule and their own negative fixture. This is a specification obligation that Rounds 1–3B did not state explicitly.

## 5. Candidate research ideas from Round 4

| Idea | Source limitation | Fit | Evidence | Data | Method | Novelty | Boundary | Priority | Decision |
|---|---|---|---|---|---|---|---|---|---|
| **A1. Typed, acceptance-executable CQ registry** — every CQ carries type (SCQ/VCQ), expected-answer shape, expressivity check, fixture, pass criterion; paired forward/reverse VCQs across the full chain | Keet & Khan: no acceptance semantics, no empirical evaluation (§6, PDF p. 13); Antunes (R1): CQs stop before action/status | PASS | PASS (Keet + Antunes) | PASS (spec-level) | PASS | PASS — typology is Keet's, chain-complete acceptance registry is not | PASS | Closes G2 directly | **ADOPT NOW** |
| **A2. Asserted-versus-derived link declaration + integrity fixtures per link type** | Jia §6.2, PDF p. 21 (bounding-box derivation); Kim §3.2, PDF p. 7 (chosen relationship path) | PASS | PASS (2 papers) | PASS | PASS | PASS — no paper declares link provenance as a schema obligation | PASS — pure information modelling, no FEM/diagnosis | Closes a G2 specification hole | **ADOPT NOW** |
| **A3. Constraint catalogue authored independently of serialization, with an explicit note that ifcOWL does not carry IFC's `RULE`/`WHERE` layer** | Pauwels §6, PDF p. 33 | PASS | PARTIAL — one paper; needs a second source on constraint loss | PASS | PASS | PARTIAL — the fact is Pauwels'; the *design consequence* is the thesis' | PASS | Supports the G2 constraint catalogue | **ADD TO REVIEW** — verify with a second source before claiming |
| **A4. Attestation record separated from evidence payload, without blockchain** | Lee, D. §4.1, PDF p. 3; trilemma §6, PDF p. 8 | PARTIAL | PARTIAL | PASS | PASS | PARTIAL — the pattern is Lee's | **Risk** — must not drift into a blockchain thesis | Not needed for G2 | **DEFER** |
| **A5. Adopt blockchain for accountability** | — | FAIL — creates a security/scalability/decentralisation proof obligation unrelated to RQ2 | — | — | — | FAIL — Lee (2021) and Çelik (2023) already occupy it | FAIL | — | **REJECT** |

## 6. Claim → Evidence → Limitation → Next action

**Claim.** Within the papers deep-read in Rounds 1–4, no study publishes a typed competency-question registry with expected-answer shapes and pass criteria, executed against deliberately invalid fixtures, over a complete `Condition_Evidence → BIM component → Inspection_Record → Action_Record → Status_Event` chain, with asserted-versus-derived link provenance declared per link type.

**Evidence.** Keet & Khan (2025) supply the CQ typology but explicitly exclude constraint-checking queries from CQs and provide no acceptance semantics (§3.2, PDF pp. 4–8; §4.2, PDF pp. 11–12; §6, PDF p. 13). Antunes (2024) publishes CQs and a forward query but no action/status and no SHACL/SWRL (R1). Jia (2025) executes rules but has no integrity-rule family and no seeded fixtures (§5.1–6.2, PDF pp. 10–21). Kim (2018) links work records to IFC objects with no record identity, no constraints and no reverse query (§3–4, PDF pp. 4–13). Lee, D. (2021) seeds invalid nodes with an expected outcome but only for ledger consensus, on hypothetical sensors (§5.1–5.2, PDF pp. 5–6). Pauwels & Terkaj (2016) state that IFC's `RULE`/`FUNCTION` layer is not converted to OWL2 DL (§6, PDF p. 33).

**Limitation.** This is a corpus-bounded conclusion over 4 + 4 + 4 + 2 + 5 papers, not a claim about the literature. Bellon et al. (2025) remains paywalled at entity level (R1) and could still overlap. Figures in all five Round 4 papers were not visually inspected. Six PDFs in `DEEP_READ_20.07.2026` (Boje, Chen, Johannes, Yang, and the two duplicates) are not deep-read. `CLOSE_SEARCH` from Round 3B is corpus-bounded and is not a gate decision.

**Next action (G2, in order).**

1. Rewrite the G2 CQ registry schema to carry, per CQ: `CQ_ID`, type (`SCQ`/`VCQ`), wording, input, **expected answer shape**, expressivity check (`Lv ⊆ Lo`), paired inverse CQ, fixture reference, pass criterion. Cite Keet & Khan Definition 3, PDF p. 5.
2. Add a `Link_Provenance` attribute (`asserted` | `derived`) with a required `derivation_rule` field to every typed edge in the Evidence-to-Action ER model; add one negative fixture per derived link type. Cite Jia §6.2, PDF p. 21.
3. Add a standing note to the constraint catalogue that IFC's `RULE`/`WHERE` layer is not inherited through ifcOWL, so every integrity rule must be authored explicitly. Cite Pauwels §6, PDF p. 33. Seek a second confirming source before treating this as settled.
4. Add `Model_Version_ID` to the mandatory (not optional) identifier set, with a stale-crosswalk fixture. Cite Kim §6, PDF p. 14.
5. Disambiguate the two "Lee et al. (2021)" citations across all evidence-base files before any Paper 2 draft.
6. Decide whether Boje (2020), Chen (2026), Johannes (2021) and Yang (2025) are Round 5 or Chapter 2 background only. Do **not** reopen `CLOSE_SEARCH` without a stated trigger.

**Gate status.** This record does not change any Gate state. G2 remains `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN`; G3 execution remains `NOT OPEN`. No artifact in this record constitutes validation evidence.
