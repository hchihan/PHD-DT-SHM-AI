## Overview

Competency Questions (CQs) are natural-language questions that specify what an ontology or information model must be able to answer, functioning as functional requirements that scope, guide, and later verify a knowledge representation artefact. Grüninger and Fox originated the notion as a mechanism to evaluate whether a proposed ontology is sufficient for its intended purpose, and this remains the foundational reference cited across subsequent methodological work. This report establishes the methodological grounding for defining and pre-registering CQs for a traceability chain linking condition evidence, BIM components, inspection records, and action records/statuses, and delivers a synthesis table plus thirty thesis-proposed CQs.[^1][^2][^3]

## How CQs are developed in ontology and information-model research

CQs are typically elicited early in the requirements-specification phase, most systematically in the NeOn methodology's Ontology Requirements Specification Document (ORSD), where stakeholder interviews or use-case analysis produce natural-language questions the artefact must answer. Espinoza et al.'s CODEP process formalises this into discrete phases — Problem Identification and Scope, Application Domain Analysis, Competency Question Elicitation and Definition, Knowledge Rules Definition, and Validation Criteria Definition — explicitly recommending that "ontology validation criteria" be defined *before* the ontology is built. Monfardini et al.'s survey of 63 ontology engineers found CQs help define scope (92.1%) and support evaluation (82.5%), but engineers struggle with ensuring necessity/sufficiency of the CQ set (77.8%) and with tooling, indicating that CQ elicitation is common practice but weakly standardised.[^4][^5][^6][^2]

## Types of competency questions proposed in the literature

The most granular typology comes from Keet and Khan (2024), whose Model for Competency Questions (QuO) distinguishes five purpose-driven types: Scoping (SCQ), Validating (VCQ), Foundational (FCQ), Relationship (RCQ), and Metaproperty (MpCQ) questions, each with distinct constituent elements (domain entities, subject domain, prospective/target ontology, foundational entity, or relational property). This model was first presented as a position paper at EKAW'24 and later extended with a full annotated dataset (ROCQS, n=438 CQs: 323 SCQ, 38 FCQ, 33 VCQ, 27 RCQ, 17 MpCQ) in the arXiv technical report and a JOWO'25 workshop paper. Other authors use coarser distinctions — e.g., "general" versus "domain/use-case-specific" CQs in Lorvão Antunes et al. (2024), or CQ "patterns" mined from SPARQL-OWL formalisations by Wiśniewski et al..[^7][^8][^9][^10][^11][^5][^12][^13]

## How scoping, validation, and relationship CQs differ

According to Keet and Khan's QuO model, a Scoping CQ (SCQ) identifies domain entities and the subject domain to delimit what the prospective ontology should cover (e.g., "What can the pipes in a sewer network convey?") and is used chiefly before or during conceptualisation. A Validating CQ (VCQ) mentions at least one domain entity and is used to verify that implemented content — instance data and its structure — is actually present and correctly represented (e.g., "Is there an affogato drink in the knowledge base?"), and is applied post-implementation against a populated ontology or knowledge graph. A Relationship CQ (RCQ) interrogates the nature of a relation itself — its arity, direction, or relational metaproperties — rather than instance content (e.g., determining whether a relation is symmetric or transitive). The table below distinguishes these purposes formally.[^8][^9][^14][^15]

| CQ Type | Primary Purpose | Typical Use Point | Example Question Form |
|---|---|---|---|
| Scoping (SCQ) | Delimit domain entities and subject domain | Requirements/conceptualisation | "What types of X exist in domain D?" |
| Validating (VCQ) | Verify implemented content coverage | Post-implementation testing | "Is there an instance of X with property Y?" |
| Relationship (RCQ) | Examine relation arity/properties | Modelling/formalisation | "What is the arity of relation R?" |
| Foundational (FCQ) | Align entity to foundational ontology | Formalisation/alignment | "Is E mapped to a DOLCE perdurant?" |
| Metaproperty (MpCQ) | Classify entity by rigidity/identity | Formalisation | "Is every instance of E necessarily E?" |

[^9][^15][^7]

## CQs for ontology design versus implemented-model validation

CQs serve a dual role across the lifecycle: in early stages they suggest concepts and relations to model (design/scoping), while in later stages they verify and validate the knowledge encapsulated in an implemented ontology or knowledge base. Keet and Khan's position paper explicitly frames CQs as "not merely intended for scoping... but serv[ing] manifold purposes," including knowledge acquisition, knowledge organisation, and validation across the whole engineering process. However, Keet has separately cautioned that answering CQs alone is "not enough to evaluate your ontology," because CQs check minimum content coverage but do not guarantee logical correctness, completeness, or absence of modelling pitfalls — additional evaluation (e.g., OOPS! pitfall scanning, reasoner consistency checks) is required.[^16][^17][^18][^6][^19]

## Studies defining expected answers, test data, executable queries, failure conditions, and acceptance criteria

Formal test-driven treatments exist but are comparatively rare. Wiśniewski et al. define a CQ as a pair ⟨Q, σ⟩ where Q is a query in a formal language and σ is the expected answer expressed as a variable substitution, and define a "satisfied" CQ as one where O ∪ Q ⊨ σ — establishing executable-query and expected-answer semantics with a defined satisfaction (pass/fail) condition. Their CQ2SPARQLOWL dataset and Data-in-Brief article operationalise this at scale: 234 CQs paired with 131 SPARQL-OWL queries serve as a "gold standard" for benchmarking, i.e., providing test data and executable queries but not explicit acceptance-criteria documentation beyond query-answer equivalence. The Poznań PhD thesis by Wiśniewski extends this into a full test-driven ontology development loop: translate CQ → SPARQL-OWL, run tests, and branch on presupposition satisfaction, entailment pass/fail, and ontology refactoring on failure — explicitly modelling failure conditions as test outcomes that trigger axiom updates or regression testing. Espinoza et al. (2021) separately define "validation criteria" collected from subject-matter experts, who judge post-hoc whether query responses meet expectations — an acceptance criterion defined by domain expert consensus rather than a formal entailment check. In BIM-specific work, Ait-Lamallam-style and TUM graph-based studies demonstrate SPARQL queries against ontology instance data and manually verify results against ground truth, but rarely publish formal failure/acceptance criteria as distinct artefacts.[^20][^21][^12][^22][^23][^2][^24][^1]

## Evidence for pre-registering CQs before implementation

The strongest explicit support for CQ definition prior to implementation comes from Espinoza et al., whose CODEP lifecycle places "Competency Question Elicitation and Definition" and "Validation Criteria Definition" in Phase I, before ontology building begins in Phase II, with a formal "Milestone I: Ontology Vision and Scope" gate. NeOn methodology similarly mandates the ORSD (containing CQs) as an early deliverable preceding conceptualisation, formalisation, and implementation. Wiśniewski's test-driven development approach operationalises the same principle computationally: CQs and their SPARQL-OWL formalisations are established as an executable test suite prior to (and iteratively during) ontology construction, analogous to test-driven software development. Collectively, this constitutes methodological precedent — though not a standardised "pre-registration" protocol in the clinical-trial sense — for fixing CQs, expected answers, and queries before implementation to prevent post-hoc rationalisation of results.[^5][^23][^2][^25]

## Application in BIM, IFC, inspection, maintenance, and asset management

CQs are a recurring evaluation instrument across BIM/AMS ontology papers. Lorvão Antunes et al. (2024) define 13 CQs (five general, plus pilot-specific sets for tunnels/sensors, bridges/inspection-risk, and pavements) to evaluate their Engineering Structures ontology linking BIM, sensor observations, and inspection-derived Risk and Condition data, validating formalisation separately with the OOPS! pitfall scanner. The Building Topology Ontology (BOT) defines seven CQs (e.g., zonal containment, adjacency, element composition) with matching SPARQL queries as its core validation mechanism. Robotic-inspection ontology work (OBRNIT) uses CQs to define defect localisation and sensor-mismatch detection requirements for BIM-linked navigation. Quality-assurance/inspection-planning ontology work explicitly tabulates CQs against use cases and includes fully worked expected answers for individual inspection instances (e.g., UUIDs, inspector identity, status values), representing one of the more complete test-data-inclusive examples in the BIM/inspection domain. LOD-sensitive BIM-data research formalises CQs into SPARQL queries and validates them using a Pellet reasoner to check consistency against source-of-truth standards, an approach directly analogous to a component-traceability check.[^26][^27][^21][^28][^5]

## Limitations of competency questions as scientific validation

Multiple sources converge on the limitation that CQs, even when fully answered, do not constitute a complete correctness proof. Keet notes that satisfying CQs demonstrates the presence of minimum required content but says nothing about logical consistency, redundancy, or broader design quality, requiring supplementary evaluation methods. Monfardini et al.'s practitioner survey identifies persistent difficulties in judging whether a CQ set is necessary and sufficient, and in ensuring CQs are unambiguous and truly representative of scope, undermining CQ sets as an exhaustive validation instrument. The JATIT learning-analytics paper explicitly flags that a fixed CQ set may fail to reveal new requirements or expose alternative ontological needs, and that formal CQ-answering validation does not test runtime scalability or real-world performance. Keet and Khan further argue that ambiguous or poorly formulated CQs (lacking clear constituent elements) reduce their diagnostic value, motivating their typed QuO model as a partial remedy. Additionally, SPARQL-based CQ testing is limited by SPARQL's lack of full subsumption-reasoning power, meaning some entailed answers may not be retrievable via simple query execution even when the ontology logically supports them.[^18][^6][^29][^7][^4][^9][^1]

## Verified bibliographic metadata

**Keet and Khan — position paper (EKAW'24):**
Keet, C.M., Khan, Z.C. (2024). "On the Roles of Competency Questions in Ontology Engineering." *24th International Conference on Knowledge Engineering and Knowledge Management (EKAW'24)*, Lecture Notes in Computer Science / LNAI, Springer, vol. 15370, pp. 123–132, Amsterdam, Netherlands, 26–28 November 2024. DOI: 10.1007/978-3-031-77792-9_8. Open access chapter available via Springer/colab.ws.[^17][^15][^16]

**Keet and Khan — extended technical report (arXiv):**
Keet, C.M., Khan, Z.C. (2024). "Discerning and Characterising Types of Competency Questions for Ontologies." arXiv:2412.13688 [cs.AI], submitted 18 December 2024, 16 pages. Full text (PDF, HTML, TeX source) freely accessible at arxiv.org/abs/2412.13688.[^13][^7]

**Keet and Khan — follow-on workshop paper (JOWO'25/CAOS'25):**
Keet, C.M., Khan, Z.C. (2025). "Characterising Competency Questions for Ontologies." *9th Cognition And OntologieS workshop (CAOS'25)*, part of JOWO'25, 8–9 September 2025, Catania, Italy. CEUR-WS Vol-4176, paper caos-9. Open access PDF at ceur-ws.org/Vol-4176/caos-9.pdf.[^14][^8]

**Lorvão Antunes et al. (2024) — full review:**
Lorvão Antunes, A., Barateiro, J., Marecos, V., Petrović, J., Cardoso, E. (2024). "Ontology-based BIM-AMS integration in European Highways." *Intelligent Systems with Applications*, Vol. 22, Article 200366. Received 23 November 2023; revised 15 March 2024; accepted 1 April 2024; available online 5 April 2024. DOI: 10.1016/j.iswa.2024.200366. Open access under CC BY-NC-ND, hosted on ScienceDirect and institutional repository (repositorio.iscte-iul.pt).[^5]

The paper reports the EU CEDR-funded CoDEC project, which links Asset Management Systems (AMS) and BIM for European highway structures (bridges, tunnels, pavements) via an Engineering Structures ontology built on the NeOn methodology, extending the EurOTL framework and the W3C Semantic Sensor Network (SSN) ontology. Thirteen CQs are defined: five general (structure end-of-construction date, location, measurements, owner, element composition) and eight pilot-specific — two for sensor/tunnel data (which sensors are hosted, how many observations; location of sensor data), three for bridge risk/condition inspection data (inspection results by element, structure risk per inspection, last risk-analysis result per element), and three for pavement sections/layers. Validation combines CQ-answering with the OOPS! (OntOlogy Pitfall Scanner!) tool; the ontology links to BIM via ifcOWL GUIDs and stores sensor/inspection observations following the SSN pattern (Observation → hasSimpleResult/hasResult → Risk and Condition Indicator/Result), closely mirroring the condition-evidence → component → inspection chain targeted by this thesis. Limitations acknowledged by the authors include a predominantly uni-directional BIM-to-ontology data flow and reliance on Protégé/SPARQL for analysis rather than user-friendly visualisation.[^5]

## Synthesis table

| Study | CQ purpose | CQ categories | Expected answer | Executable query | Failure condition | Acceptance criterion | Domain | Limitation |
|---|---|---|---|---|---|---|---|---|
| Grüninger & Fox (1995), cited in [^3][^2] | Evaluate ontology sufficiency for intended purpose | Undifferentiated (foundational) | Not formalised | Not specified | Not specified | Ontology answers question correctly | General ontology engineering | No formal test protocol; qualitative judgement |
| Keet & Khan (2024) [^7][^16][^14] | Scope, validate, align, classify, relate | SCQ, VCQ, FCQ, RCQ, MpCQ (typed model, QuO) | Constituent-based (per type), not per-instance | Not the paper's focus (typology paper) | Ambiguous/atypical CQ formulation | Distinct constituent elements present per type | General ontology engineering (438-CQ ROCQS repository) | No benchmark evaluation against external gold standard; self-curated dataset |
| Wiśniewski et al. (2019) [^11][^1] | Formalize CQs as testable pairs | Not typed; TBox-focused | σ (expected variable substitution) | SPARQL-OWL query Q | O ∪ Q ⊭ σ | O ∪ Q ⊨ σ (entailment) | General ontology engineering (234-CQ dataset) | SPARQL limited reasoning power vs. full DL entailment |
| Wiśniewski PhD thesis [^23] | Test-driven ontology development | Presupposition-based test cases | Expected entailment result | SPARQL-OWL, iterative test suite | Test fails → refactor/regression | Test passes (entailed) | General ontology engineering | Requires existing formalized CQs/queries; scalability for large ontologies unclear |
| Espinoza et al. (2021), CODEP [^2] | Elicit and validate CQs before build | Domain CQs + Knowledge Rules | SME-judged response adequacy | Query against knowledge base | SME rejects response as inadequate | SME confirms validation criteria met | Medical/general ontology engineering | Subjective (expert judgement) criterion, not formally entailed |
| Monfardini et al. (2023) survey [^4][^6] | Empirical study of CQ practice | Practitioner-reported use cases | N/A (survey) | N/A | Practitioner-reported difficulty | N/A | Cross-domain ontology engineering | Self-reported bias; no standardized guidance found |
| Rasmussen et al. BOT (2020) [^28] | Validate building topology ontology | Zonal containment/adjacency CQs | Query result set (e.g., selected zones/elements) | SPARQL SELECT queries | Query returns incorrect/empty set | Query returns expected entity set | BIM/Linked Building Data | Limited to topological relations; no inspection/action semantics |
| LOD-sensitive BIM ontology (LDAC'21) [^21] | Validate LOD-versioned BIM data model | Framework/data/process CQs | Query result compared to standard | SPARQL queries + Pellet reasoning | Inconsistent/incorrect inference | Result matches source standard | BIM/LOD data management | Small-scale demonstration; not tested on production data |
| Ontology-based QA/inspection planning [^27] | Represent inspection plans and support planning | Use-case CQs (description, planning knowledge) | Fully worked instance answers (e.g., UUID, status) | Not explicit (ontology query implied) | Not explicit | Answer matches documented instance data | Construction QA/inspection | Domain-specific (screed/flatness); generalisability unclear |
| Lorvão Antunes et al. (2024) [^5] | Scope and evaluate BIM–AMS ontology | General + pilot-specific (sensor, inspection/risk, pavement) | Not explicitly tabulated per CQ | Not published in paper (implied SPARQL/Protégé) | Not explicit | CQ answerable + OOPS! pitfall thresholds | BIM/AMS, European highway infrastructure (bridges, tunnels, pavements) | Uni-directional BIM→ontology flow; no user-friendly visualization; expected answers/test data not published |

## Thesis-proposed competency questions

The following thirty questions are proposed by this thesis to operationalise the condition-evidence → BIM-component → inspection-record → action-record/status traceability chain. They are **thesis-proposed competency questions**, not findings extracted from the cited studies, and are structured following the Keet and Khan SCQ/VCQ/RCQ typology  combined with the executable-query/expected-answer/failure-condition formalism of Wiśniewski et al..[^7][^9][^1]

### Thesis-proposed Scoping Competency Questions (SCQ)

1. What types of condition-evidence sources (e.g., sensor, visual inspection, drone imagery) does the framework need to represent for a given BIM component?
2. Which BIM component identity attributes (GUID, IFC type, spatial location) must be captured to uniquely resolve a component across its lifecycle?
3. What categories of inspection records (routine, triggered, follow-up) must the model distinguish?
4. What types of action records or action statuses (planned, in-progress, completed, rejected) must the framework represent?
5. What provenance metadata (originating sensor/evidence ID, timestamp, responsible agent) must be captured to support reverse traceability from an action back to its originating evidence?

### Thesis-proposed Validating Competency Questions (VCQ)

1. Does every condition-evidence instance in the knowledge base link to at least one BIM component identifier?
2. Can the model retrieve all inspection records associated with a given BIM component GUID and confirm none reference a non-existent component?
3. Is there any inspection record in the knowledge base with no linked action record or explicit "no action required" status?
4. Are there duplicate component identifiers (same GUID or IFC tag) associated with conflicting condition-evidence entries?
5. Does every action-status transition in the data conform to the defined valid-status transition set (e.g., no direct jump from "planned" to "closed" without "in-progress")?

### Thesis-proposed Relationship Competency Questions (RCQ)

1. What is the cardinality of the relationship between a BIM component and its condition-evidence instances (one-to-many, many-to-many)?
2. Is the relationship linking an inspection record to its triggering condition evidence directional and traceable in reverse (evidence ← inspection)?
3. What is the relational path connecting an action record back through its inspection record to the originating condition evidence and sensor source?
4. Is the relationship between an action record and a BIM component transitive through the inspection record, or must it be asserted directly for querying efficiency?
5. Does the relationship between duplicate component identifiers and their respective inspection histories need to be merged (equivalence) or kept distinct (provenance-preserving) in the traceability model?

These proposed CQs collectively target the eight required coverage areas — source sensor/evidence, BIM component identity, inspection records, action records, reverse provenance, missing links, duplicate identifiers, and invalid status changes — and are intended as candidates for formal pre-registration (expected answers, executable SPARQL/SHACL queries, and acceptance thresholds) prior to ontology or information-model implementation, following the precedent set by Espinoza et al.'s pre-build validation-criteria definition  and Wiśniewski's test-driven CQ formalisation.[^23][^2][^1]

---

## References

1. [Verifying Description Logic Ontologies based on ...](https://ceur-ws.org/Vol-1908/paper16.pdf)

2. [A validation & verification driven ontology: An iterative process - Angelina Espinoza, Ernesto Del-Moral, Alfonso Martínez-Martínez, Nour Alí, 2021](https://journals.sagepub.com/doi/10.3233/AO-210251) - Designing an ontology that meets the needs of end-users, e.g., a medical team, is critical to suppor...

3. [Validation of Course Ontology Elements for Automatic](https://www.dcs.warwick.ac.uk/~msj/publications/fulltext/ibrahim-teo_joy_eleot_2017_accepted.pdf)

4. [Use of Competency Questions in Ontology Engineering](https://link.springer.com/chapter/10.1007/978-3-031-47262-6_3) - viết bởi GKQ Monfardini · 2023 · Trích dẫn 57 bài viết — We performed a survey with 63 ontology engi...

5. [Ontology-based BIM-AMS integration in European Highways](https://repositorio.iscte-iul.pt/bitstream/10071/31507/1/article_103722.pdf)

6. [Use of Competency Questions in Ontology Engineering - Nemo](https://nemo.inf.ufes.br/wp-content/papercite-data/pdf/use_of_competency_questions_in_ontology_engineering__a_survey_2023.pdf)

7. [Discerning and Characterising Types of Competency ...](https://arxiv.org/abs/2412.13688) - viết bởi CM Keet · 2024 · Trích dẫn 11 bài viết — Abstract:Competency Questions (CQs) are widely use...

8. [August 2025 - Keet blog](https://keet.wordpress.com/2025/08/) - 2 posts published by keet during August 2025

9. [[Literature Review] Discerning and Characterising Types of ...](https://www.themoonlight.io/en/review/discerning-and-characterising-types-of-competency-questions-for-ontologies) - ... Competency Questions for Ontologies" by C. Maria Keet and Zubeida Casmod Khan presents a systema...

10. [Competency Questions for ontologies](http://www.meteck.org/teaching/ESAO24-CQs.pdf) - What is assessed in the walking task? What level of expertise is required to use TexShop? Is [this a...

11. [Analysis of Ontology Competency Questions and their formalizations in SPARQL-OWL | Web Semantics: Science, Services and Agents on the World Wide Web](https://dl.acm.org/doi/10.1016/j.websem.2019.100534) - Abstract Competency Questions (CQs) are natural language questions outlining and constraining the sc...

12. [Ontology Competency Questions to SPARQL-OWL Queries ...](https://data.mendeley.com/datasets/pp6hmfxgfg/1) - This data article reports on a new set of 234 competency questions for ontology development and thei...

13. [Discerning and Characterising Types of Competency Questions for ...](https://arxiv.org/html/2412.13688v1)

14. [Characterising Competency Questions for Ontologies](https://ceur-ws.org/Vol-4176/caos-9.pdf) - viết bởi CM Keet · 2025 · Trích dẫn 3 bài viết — Abstract. Competency Questions (CQs) are widely use...

15. [On the Roles of Competency Questions in Ontology](http://www.meteck.org/files/EKAW24positionPaperCQs.pdf)

16. [On the Roles of Competency Questions in Ontology Engineering](https://colab.ws/articles/10.1007%2F978-3-031-77792-9_8) - Competency Questions (CQs) are not merely intended for scoping the prospective content of an ontolog...

17. [On the Roles of Competency Questions in Ontology ...](https://dl.acm.org/doi/abs/10.1007/978-3-031-77792-9_8) - viết bởi CM Keet · 2024 · Trích dẫn 23 bài viết — This position paper argues that CQs should be view...

18. [Only answering competency questions is not enough to evaluate ...](https://keet.wordpress.com/2022/06/08/only-answering-competency-questions-is-not-enough-to-evaluate-your-ontology/) - How do you know whether the ontology you developed or want to reuse is any good? It’s not a new ques...

19. [A Review and Comparison of Competency Question ...](https://livrepository.liverpool.ac.uk/3184940/1/EKAW2024-2.pdf)

20. [[PDF] Graphbasierter Ansatz zur Analyse von BIM-Raumbeziehungen](https://mediatum.ub.tum.de/doc/1752274/1752274.pdf)

21. [Ontological approach for LOD-sensitive BIM-data](https://linkedbuildingdata.net/ldac2021/files/papers/CIB_W78_2021_paper_131.pdf)

22. [Dataset of ontology competency questions to SPARQL-OWL queries translations](https://www.sciencedirect.com/science/article/pii/S2352340919314544) - This data article reports on a new set of 234 competency questions for ontology development and thei...

23. [FACULTY OF COMPUTING AND TELECOMMUNICATIONS](https://bip-archiwum.put.poznan.pl/sites/default/files/wisniewski_rozprawa.pdf)

24. [Dataset of ontology competency questions to SPARQL-OWL queries ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC6971340/) - This data article reports on a new set of 234 competency questions for ontology development and thei...

25. [Analysis of Ontology Competency Questions and their ...](https://www.semanticscholar.org/paper/Analysis-of-Ontology-Competency-Questions-and-their-Wisniewski-Potoniec/b7cdcbb05da062896fc6048c4ba7f80b0ea56b0d) - This paper proposes an extension of test-driven ontology development approach by formalization of pr...

26. [[PDF] Ontology for BIM-Based Robotic Navigation and Inspection Tasks](https://spectrum.library.concordia.ca/id/eprint/994159/1/buildings-14-02274-v2-1.pdf)

27. [Ontology-based representation of quality assurance and inspection ...](https://www.sciencedirect.com/science/article/pii/S0926580525003085)

28. [BOT: The building topology ontology of the W3C linked building data group - Mads Holten Rasmussen, Maxime Lefrançois, Georg Ferdinand Schneider, Pieter Pauwels, 2020](https://journals.sagepub.com/doi/10.3233/SW-200385) - Actors in the Architecture, Engineering, Construction, Owner and Operation (AECOO) industry traditio...

29. [Microsoft Word - 2 60470 74197388 Integrating Competency Question-Driven Ontology Authoring with Ontology Validation for Learning Analytics from Heterogeneous Platforms_JATIT_Reviewer Comment.docx](http://www.jatit.org/volumes/Vol103No19/2Vol103No19.pdf)

