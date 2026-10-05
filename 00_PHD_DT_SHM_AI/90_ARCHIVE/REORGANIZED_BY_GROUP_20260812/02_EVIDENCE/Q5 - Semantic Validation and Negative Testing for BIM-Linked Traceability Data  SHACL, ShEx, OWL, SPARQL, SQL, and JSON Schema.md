## Overview

Validating BIM-linked traceability data (e.g., sensor-to-asset-to-GUID chains) sits at the intersection of two literatures: (1) Semantic Web / Linked Building Data research on constraint languages for ifcOWL and IFC-derived RDF graphs, and (2) mainstream data-quality/database research on referential integrity, schema validation, and negative testing. Both strands provide direct, citable evidence relevant to a PhD prototype, but neither strand has published a study that tests the exact traceability fixtures (orphan Sensor_ID, unaccountable status change, broken reverse traceability) used in a typical BIM asset-tracking model. This report distinguishes peer-reviewed academic sources from official technical specifications throughout, per the request.

## How SHACL and Equivalent Technologies Have Been Applied to IFC/ifcOWL/BIM/Digital Twins

The foundational academic work is Stolk and McGlinn's "Validation of IfcOWL datasets using SHACL" (LDAC 2020), which proposes two methods for generating SHACL shapes for ifcOWL: (1) extracting validation information from ifcOWL's OWL restrictions via SPARQL and SHACL Rules, and (2) embedding SHACL generation directly into the EXPRESStoOWL conversion pipeline that produces ifcOWL from the EXPRESS/STEP schema. The paper explicitly argues that OWL restrictions in ifcOWL are being used for a purpose (data validation) for which SHACL is "more appropriate," because OWL was designed for open-world inference, not closed-world constraint checking. This paper has been cited over 30 times, including by a VLDB 2024 paper on efficient SHACL reasoning, indicating sustained academic uptake.[^1][^2][^3]

A more recent and more rigorous paper, Wang et al., "Enhancement and validation of ifcOWL ontology based on Shapes Constraint Language (SHACL)" (Automation in Construction, 2024), operationalizes this idea at scale: the authors built a Python tool that scrapes the IFC documentation for all EXPRESS "WHERE rules" (the schema's native integrity constraints), automatically translates these rules into SPARQL-based SHACL constraints, and validates real ifcOWL instance graphs against them, reporting detected errors and inconsistencies. This is the strongest published evidence that SHACL constraint technology can operationalize IFC's native data-integrity rules (which functionally resemble check constraints and cardinality rules) and produce structured error reports.[^4][^5][^6]

Applied/university-level evidence extends SHACL to BIM quality control workflows. A TU Eindhoven MSc thesis (van den Bersselaar, 2022) built a SHACL-based rule-checking prototype for validating technical requirements documents against BIM models, structured into four stages — rule interpretation, model preparation, rule execution, and reporting — and concluded that SHACL is "a suitable rule-checking language" for a "substantial part" of technical-requirement documents, while noting dependencies on prior BIM modelling quality. A 2023 LDAC paper on validating building models against legislation similarly used SHACL (via the RASE methodology) to encode regulatory requirements as machine-readable Turtle constraints, explicitly combining compliance checking with "quality constraints... ensuring that all necessary data is present," to avoid "false compliance". LDAC/BIM4Ren teaching material further documents SHACL cardinality and datatype constraints applied directly to ifcOWL classes such as IfcWallStandardCase (e.g., enforcing exactly one GUID per wall).[^7][^8][^9]

On explicit accountability/provenance SHACL use, a 2026 arXiv paper on "Ontological Knowledge Blocks" compiles governance requirements into RDF/OWL schemas plus SHACL shapes plus PROV-O provenance links, with SHACL shapes specifically enforcing "logging, provenance linkage, and model traceability" for regulatory accountability (EU AI Act context, not BIM, but methodologically transferable). This is the closest academic precedent for validating provenance completeness and traceability with SHACL, though it is domain-adjacent rather than BIM-specific.[^10]

For IFC-native, non-RDF validation, buildingSMART's Information Delivery Specification (IDS) — an official technical standard (not peer-reviewed research) finalized in June 2024 — is the industry's machine-readable requirement-checking format for IFC files, using XML-based "specifications" with applicability/requirement facets, producing pass/fail reports per element (e.g., "7/10 walls passed"). The Xbim.IDS.Validator library reports a "100% pass rate [against] all current IDS TestCases," evidencing an existing negative/positive test-case suite maintained by the standard's developer community, though this is engineering documentation rather than an academic study.[^11][^12][^13][^14][^15]

## Constraints Tested in Prior Work

| Constraint type | Evidence |
|---|---|
| Cardinality (min/max/exact count) | ifcOWL OWL restrictions use `owl:minQualifiedCardinality`/`maxQualifiedCardinality`; SHACL equivalents (`sh:minCount`/`maxCount`) shown for GUID uniqueness on walls[^16][^7] |
| Mandatory property presence | SHACL "missing information" checks (e.g., missing ThermalTransmittance) in BIM4Ren teaching material[^7]; IDS required properties (e.g., FireRating)[^11] |
| Value range/datatype | SHACL `sh:datatype`, numeric range checks (U-value < 3 W/m²K) in LDAC teaching examples[^7] |
| WHERE-rule integrity constraints (EXPRESS-native) | Automatically converted to SPARQL-based SHACL and tested against real ifcOWL graphs[^4][^5][^6] |
| Class/entity typing | SHACL `sh:targetClass`, `sh:class`; OWL restriction-based subclassing in ifcOWL[^16][^17] |
| Regulatory/legislative compliance + completeness ("false compliance" prevention) | RASE-to-SHACL methodology for building legislation[^9] |
| Provenance/traceability/logging | SHACL shapes plus PROV-O links enforcing provenance completeness (non-BIM domain)[^10] |

## Negative Testing and Invalid Fixtures: Direct Evidence

Deliberate negative testing (intentionally broken data used to prove a validator correctly fails) is well established in general RDF/SHACL data-quality engineering guidance, which explicitly recommends: "Test against golden data: Valid examples must pass; intentionally broken examples must fail with expected messages" and warns that "No golden negative tests — only testing valid data misses shape bugs. Maintain invalid fixtures that must produce specific violations". This is a practitioner/methodological source rather than a peer-reviewed BIM paper, but it is the clearest direct statement of negative-fixture testing methodology found in the SHACL literature and is directly transferable.[^18]

Within the IFC/IDS ecosystem, buildingSMART's official test-case repository is used to audit IDS implementations, and validator implementations report pass rates against these test cases, confirming that structured pass/fail test suites (including presumably invalid cases) already exist as an accepted validation practice for IFC-linked data, though this is standards infrastructure, not an academic negative-testing study.[^19][^14]

No study identified in this search explicitly and systematically tests the specific fixture types requested (orphan identifiers, duplicate identifiers, missing mandatory relationships, invalid cardinality, incorrect entity type/domain-range, missing provenance, conflicting status, unauthorized status change) as a named, itemized negative-test battery against an ifcOWL/IFC/BIM/digital-twin traceability model. The closest analogues are: (a) SHACL/ShEx methodological literature that treats cardinality, datatype, and class-membership violations as canonical SHACL Core constraint types testable via standard tooling; (b) general database/data-quality tooling papers and product literature on referential-integrity "orphan record" detection between parent/child tables, which is a mature, decades-old SQL practice documented in commercial data-quality tools (iceDQ, Jailer, foreign-key validators); and (c) digital-twin data-provenance research establishing "data passports" with location, status, installation, and organizational responsibility fields, and recommending cross-validation of sensor data and blockchain-based immutable provenance records — directly relevant to "missing provenance" and "unauthorized status change" but validated via blockchain/consensus rather than SHACL/SQL constraints.[^20][^17][^21][^22][^23][^24]

## Reproducible Machine-Readable PASS/FAIL Validation Methods

| Method | Machine-readable report | Reproducibility evidence |
|---|---|---|
| SHACL | `sh:conforms true/false` plus itemized `ValidationResult` per violation, in RDF | W3C-recommendation vocabulary; used identically across pyshacl, Jena SHACL, TopBraid[^25][^18] |
| ShEx | Shape map: pass/fail per node, but "no vocabulary for defining validation report... other than pass/fail," less detailed than SHACL[^20] |
| IDS/IFC checking | Standardized BCF-style reports, percentage pass per specification (e.g., "7/10 walls passed")[^11][^19] |
| SPARQL ASK/CONSTRUCT queries | Boolean or graph-based result; used as extraction mechanism feeding SHACL, and as SHACL-SPARQL extension mechanism[^1][^17] |
| SQL constraints (FK, UNIQUE, CHECK) | Binary insert/update rejection at the engine level; violation surfaced as a database error/exception, not a structured report by default | Decades of RDBMS practice; commercial data-quality tools add structured reporting on top (iceDQ reconciliation reports)[^23] |
| JSON Schema | Boolean valid/invalid plus a standardized array of validation error objects (keyword, path, message) — widely implemented (ajv, jsonschema) though not evidenced in the BIM-specific sources retrieved here | General software-engineering practice; no IFC-specific academic paper located |

## Simplest Defensible Validation Architecture for a Small PhD Prototype

Across the sources reviewed, a minimal, academically defensible architecture combines: (1) a relational or lightweight graph store holding the traceability model (sensors, BIM_GUIDs, condition-evidence records, status events); (2) SQL-level referential integrity (foreign keys, unique constraints, check constraints) as the first-line defense against orphan IDs, duplicates, and invalid enumerations, exploiting native RDBMS enforcement that fails at write time; and (3) a schema-validation layer (JSON Schema if data interchange is JSON-based, or SHACL if the model is expressed in RDF/ifcOWL) to check structural completeness, cardinality, and mandatory relationships before ingestion, mirroring the "validate then load" governance pattern documented in asset-management practice. The van den Bersselaar four-stage pattern (rule interpretation → model preparation → rule execution → reporting) is a directly citable, reproducible architecture template already validated for BIM technical-requirement checking and is appropriately scoped for a prototype.[^8][^22][^26][^23]

## Is SHACL Academically Necessary, or Can SQL/JSON Validation Suffice?

The evidence indicates SHACL is not strictly necessary if the underlying data model is relational or JSON rather than RDF/OWL — SQL constraints and JSON Schema can enforce equivalent orphan-key, duplicate-key, cardinality, and mandatory-field rules with mature, decades-old tooling. SHACL becomes necessary specifically when the traceability data is expressed as RDF linked to ifcOWL/IFC ontologies, because OWL's open-world assumption cannot natively reject incomplete or invalid data — multiple academic sources state this explicitly, describing SHACL as filling a validation gap OWL cannot address under closed-world semantics. If the PhD prototype's BIM linkage is via IFC-SPF/COBie/relational bridge tables rather than an RDF ifcOWL graph, SQL and JSON Schema provide scientifically defensible, reproducible, and simpler evidence; SHACL would be an additive but not essential technology, useful mainly if reviewers expect Semantic-Web-native validation aligned with the ifcOWL/LDAC literature.[^2][^17][^22][^23][^1][^4][^7][^8][^18]

## Required Comparative Table: Academic Studies

| Study | Data model | Validation technology | Constraints tested | Invalid fixtures | Automated execution | Reported results | Limitation |
|---|---|---|---|---|---|---|---|
| Stolk & McGlinn, LDAC 2020[^1][^2] | ifcOWL RDF | SHACL (2 generation methods from OWL/EXPRESS) | Cardinality, datatype, class constraints extracted from ifcOWL OWL restrictions | Not explicitly reported as named negative fixtures | Yes, SHACL-compliant tooling produces validation report | Method feasible; SHACL preferable to OWL for validation purpose | Coverage limited to constraints expressible via extraction method; no large-scale invalid-data benchmark |
| Wang et al., Automation in Construction 2024[^4][^5][^6] | ifcOWL instance graphs | SPARQL-based SHACL generated from EXPRESS WHERE rules | All EXPRESS WHERE-rule integrity constraints in IFC schema (broad set) | Real-world ifcOWL graphs with existing errors/inconsistencies detected | Yes, custom Python tool automates rule scraping, conversion, and validation | Detected and corrected data errors/inconsistencies tied to WHERE rules | Relies on web-scraping IFC docs; constraint coverage bounded by parseable WHERE-rule syntax |
| van den Bersselaar, TU Eindhoven MSc thesis 2022[^8] | BIM model + technical requirements document | SHACL rule-checking prototype | Technical requirement rules (properties, values) translated into SHACL shapes | Not explicit; framed around requirement-document coverage | Yes, four-stage rule-checking pipeline | SHACL validates "substantial part" of requirements document | Depends heavily on upstream BIM modelling quality/consistency |
| LDAC 2023 legislation-validation paper[^9] | Building graph + legislative text (RASE) | SHACL (Turtle) plus IDS for completeness | Regulatory numeric/property constraints; data-presence/completeness checks | Explicitly addresses "false compliance" from missing data | Yes, machine-readable SHACL rules | Methodology generalizable to prescriptive legislation | Applicability limited to legislation expressible against defined ontology/graph |
| Ontological Knowledge Blocks, arXiv 2026[^10] | RDF/OWL knowledge base (AI governance, not BIM) | SHACL shapes + PROV-O provenance links | Provenance completeness, logging, model-artifact traceability, fairness metrics | Not BIM-specific; profile-based enforcement of accountability | Yes, SHACL validation over compiled knowledge base | Accountability/fairness/transparency profiles validated | Domain is AI governance; BIM transfer is inferential, not demonstrated |
| Xbim.IDS.Validator engineering docs[^14] | IFC/COBie models | IDS (buildingSMART XML standard, not SHACL) | Property, entity, classification, material presence per IDS specification | Official IDS TestCases suite (implies both valid/invalid cases) | Yes, .NET library validates model against .ids file, outputs detailed outcome breakdown | "100% pass rate [on] all current IDS TestCases"; tested at scale on real models | This is a technical specification/library, not peer-reviewed research |

## Required Classification Table: Proposed G3 Tests

| Proposed test | Direct academic support | Indirect support | Thesis-defined requirement |
|---|---|---|---|
| Orphan Sensor_ID | None found specific to BIM/IFC sensor linkage | General RDBMS referential-integrity "orphan record" detection is mature, well-documented practice[^22][^23] | Yes — must be defined and justified by the thesis for the sensor-traceability context |
| Orphan BIM_GUID | None found testing orphan GUIDs specifically | ifcOWL SHACL work enforces GUID cardinality (exactly one GUID per element), implying orphan/duplicate GUID detection is a natural corollary[^7][^16] | Yes — extension of GUID-cardinality shape logic to cross-table orphan detection |
| Duplicate ID | Not tested in BIM literature directly | SHACL `sh:uniqueLang`/cardinality constraints and SQL UNIQUE constraints are standard mechanisms for uniqueness enforcement[^17][^22] | Yes |
| Missing Condition_Evidence | Not tested in BIM literature directly | SHACL/IDS "missing property" checks (e.g., missing ThermalTransmittance, missing FireRating) are directly analogous mandatory-field tests[^7][^11] | Yes — Condition_Evidence is thesis-specific terminology requiring its own shape/constraint definition |
| Missing provenance | Not BIM-specific; found in AI-governance SHACL/PROV-O work[^10] and digital-twin provenance frameworks[^21] | PROV-O + SHACL provenance-completeness enforcement is a demonstrated, transferable pattern[^10]; digital-twin "data passport" literature stresses provenance fields[^21] | Yes — no BIM-specific precedent; must be thesis-defined using transferred PROV-O/SHACL pattern |
| Invalid cardinality | Directly supported — ifcOWL OWL restrictions and SHACL shapes enforce min/max/exact cardinality, and this is explicitly tested in Stolk & McGlinn and Wang et al.[^1][^4][^16] | — | No — sufficient direct academic support exists |
| Invalid entity relationship (domain/range) | Indirectly supported via OWL restriction-based class typing and SHACL `sh:class`/`sh:targetClass`[^17][^16] | ShEx/SHACL comparative literature confirms both languages test class-membership/relationship constraints[^20] | Partial — general RDF-constraint precedent exists but not BIM-traceability-specific validation of relationship type |
| Conflicting status | Not found in BIM/IFC/SHACL literature | Digital-twin data-provenance/asset-management literature discusses status/event data quality and cross-validation of sensor data, but not explicit "conflicting status" logic tests[^21][^26] | Yes — must be thesis-defined; no direct precedent |
| Unaccountable status event | Not found in BIM/IFC literature | AI-governance SHACL+PROV-O accountability shapes (logging/provenance linkage) are the closest transferable precedent[^10]; digital-twin blockchain provenance work addresses immutable, accountable status logging[^21] | Yes — requires thesis-level adaptation of provenance/accountability shape patterns to BIM status events |
| Broken reverse traceability | Not found directly in BIM/IFC/SHACL literature | Traceability-matrix and requirements-verification literature in digital-twin V&V discusses traceability as a verification concern generally, but not "reverse" traceability testing specifically[^27] | Yes — thesis must define reverse-traceability test logic; no direct precedent identified |

## Comparative Evaluation: SHACL vs. SQL Constraints vs. JSON Schema

| Criterion | SHACL | SQL constraints (FK/UNIQUE/CHECK) | JSON Schema |
|---|---|---|---|
| Scientific defensibility | Strong — W3C Recommendation since 2017, extensive peer-reviewed application to ifcOWL/BIM specifically[^1][^4][^5][^8][^9] | Strong but generic — foundational RDBMS theory, not BIM-specific in academic literature; defensibility rests on general database science, not domain-specific papers | Moderate — widely used engineering practice; no BIM/IFC-specific peer-reviewed validation study located in this search |
| Reproducibility | High — standardized RDF validation-report vocabulary (`sh:conforms`, `ValidationResult`) works identically across pyshacl, Jena, TopBraid[^25][^18] | High — constraint violations are deterministic at the engine level, though error reporting format is vendor-specific unless wrapped by a data-quality tool[^23] | High — standardized error-object array (ajv, python-jsonschema), deterministic pass/fail |
| Complexity | Higher — requires RDF/ifcOWL data conversion (EXPRESS→OWL→SHACL pipeline), SPARQL knowledge, and shape-authoring skill[^4][^5] | Lower — native to any relational database, no additional conversion layer required[^22] | Lower — lightweight, no ontology conversion needed if data is already JSON |
| Compatibility with IFC-linked data | Native compatibility once data is expressed as ifcOWL RDF; directly demonstrated for cardinality, datatype, and WHERE-rule constraints[^1][^4][^7][^16] | Compatible only if IFC/BIM data is bridged into a relational schema (e.g., via COBie or custom extraction); no native IFC-RDF alignment | Compatible only via a JSON serialization of IFC/BIM data (e.g., IFC-JSON efforts), not natively aligned with EXPRESS/ifcOWL constraint semantics |
| Suitability for a minimal PhD prototype | Lower suitability alone — steep learning curve and tooling overhead for a small prototype unless RDF is already the chosen data model | High suitability — fastest to implement, directly enforces orphan/duplicate/cardinality tests with mature, well-documented tooling[^22][^23] | High suitability if data interchange is JSON-based; simple to implement and test negative fixtures against, though offers less BIM-specific literature backing |

For a small PhD prototype whose core traceability model is relational (Sensor_ID, BIM_GUID, Condition_Evidence, status fields), SQL constraints combined with a lightweight JSON Schema validation layer for data-interchange checks offer the most defensible, reproducible, and low-complexity architecture, with SHACL reserved as an optional enhancement only if the model is explicitly expressed as an RDF/ifcOWL graph, consistent with the academic precedent set by Stolk & McGlinn and Wang et al..[^5][^1][^4][^8]

---

## References

1. [Validation of IfcOWL datasets using SHACL](https://linkedbuildingdata.net/ldac2020/files/papers/07paper.pdf) - viết bởi S Stolk · Trích dẫn 31 bài viết — SHACL for ifcOWL involves two steps: (1) extracting the d...

2. [Validation of IfcOWL datasets using SHACL](https://linkedbuildingdata.net/ldac2020/files/presentations/LDAC2020_7_WouterLubbers.pdf) - viết bởi S Stolk · Trích dẫn 31 bài viết — Here we present a method for validating ifcOWL using SHAC...

3. [Efficient Validation of SHACL Shapes with Reasoning](https://www.vldb.org/pvldb/vol17/p3589-acosta.pdf) - viết bởi J Ke · Trích dẫn 21 bài viết — The SHApes Constraint Language (SHACL) allows for express- i...

4. [Enhancement and validation of ifcOWL ontology based on ...](https://www.sciencedirect.com/science/article/pii/S0926580524000293) - viết bởi C Wang · 2024 · Trích dẫn 17 bài viết — The ifcOWL with WHERE rules was enhanced via SHACL ...

5. [Enhancement and validation of ifcOWL ontology based on Shapes Constraint Language (SHACL)](https://www.sciencedirect.com/science/article/abs/pii/S0926580524000293) - In the domain of Building Information Modeling (BIM), although ifcOWL ontology has already achieved ...

6. [Enhancement and validation of ifcOWL ontology based on ...](https://colab.ws/articles/10.1016%2Fj.autcon.2024.105293) - This paper aims to achieve the conversion and validation of WHERE rules used for defining data integ...

7. [DC.BIGBIM](https://linkedbuildingdata.net/ldac2023/summerschool/files/presentations/230613_SHACL_lecture.pdf)

8. [Eindhoven University of Technology](https://pure.tue.nl/ws/portalfiles/portal/215386995/Bersselaar_van_den_0894574_CME_Vries_d.pdf)

9. [Validation of building models against legislation using](https://linkedbuildingdata.net/ldac2023/files/papers/papers/LDAC2023_paper_8284.pdf)

10. [[PDF] Ontological Knowledge Blocks: Executable Compliance and Profile ...](https://arxiv.org/pdf/2605.23297.pdf)

11. [Information Delivery Specification (IDS) - buildingSMART International](https://www.buildingsmart.org/standards/bsi-standards/information-delivery-specification-ids/) - Define your exchange requirements to build confidence, clarity and enhance interoperability

12. [GitHub - buildingSMART/IDS: Computer interpretable (XML) standard to define Information Delivery Specifications for BIM (mainly used for IFC)](https://github.com/buildingSMART/IDS) - Computer interpretable (XML) standard to define Information Delivery Specifications for BIM (mainly ...

13. [Information Delivery Specification IDS - buildingSMART Technical](https://technical.buildingsmart.org/projects/information-delivery-specification-ids/) - Machine readable Information Delivery Specification An Information Delivery Specification (IdS) is a...

14. [xBimTeam/Xbim.IDS.Validator](https://github.com/xBimTeam/Xbim.IDS.Validator) - Library to validate IFC and COBie models using IDS1.0 and xbim Toolkit - xBimTeam/Xbim.IDS.Validator

15. [Information Delivery Specification - Wikipedia](https://en.wikipedia.org/wiki/Information_Delivery_Specification)

16. [[PDF] BuildingSMART Final Standard: The ifcOWL ontology](https://standards.buildingsmart.org/documents/20170830_LDWG_ifcOWLontology.pdf)

17. [SHACL-ShEx-Comparison - RDF Data Shapes Working Group - W3C](https://www.w3.org/2014/data-shapes/wiki/SHACL-ShEx-Comparison)

18. [SHACL - RDF Validation Guide | Data AI Hub](https://www.dataaihub.co/learn/shacl) - Complete guide to SHACL - validating RDF knowledge graphs with shapes, constraints, SPARQL-based rul...

19. [Checking IDS Against IFC Models | buildingSMART/IDS | DeepWiki](https://deepwiki.com/buildingSMART/IDS/5.2-checking-ids-against-ifc-models) - This page documents the technical lifecycle of verifying an IFC model against an Information Deliver...

20. [Chapter 7 Comparing ShEx and SHACL](https://book.validatingrdf.com/bookHtml013.html)

21. [[PDF] Blockchain-based digital twin data provenance for predictive asset ...](https://pdfs.semanticscholar.org/9354/69e69ac250d25980f6a905f881bf8183ab27.pdf)

22. [Foreign Key Validator | Online Free Tool](https://elysiatools.com/en/tools/data-foreign-key-validator)

23. [Ensure Referential Integrity with iceDQ: Validate Foreign Keys Across Tables](https://www.youtube.com/watch?v=e3xS2wjPc7I) - In today’s video, we walk you through how to perform referential integrity testing using iceDQ. We’l...

24. [Jailer download | SourceForge.net](https://sourceforge.net/projects/jailer/) - Download Jailer for free. Database Subsetter and Relational Data Browser. Database Subsetting and Re...

25. [Guide to Validate Using SHACL - datos.gob.es](https://datos.gob.es/sites/default/files/documentacion/files/guia_validacion-rdf-shacl_en.pdf)

26. [© 2020 Rizing LLC or a Rizing LLC affiliate company. All rights reserved.](https://rizing.com/wp-content/uploads/2020/04/202004-EAM-Whitepaper-How-to-Govern-Your-Digital-Twin-EN-NL.pdf)

27. [1](https://www.arxiv.org/pdf/2507.04555.pdf)

