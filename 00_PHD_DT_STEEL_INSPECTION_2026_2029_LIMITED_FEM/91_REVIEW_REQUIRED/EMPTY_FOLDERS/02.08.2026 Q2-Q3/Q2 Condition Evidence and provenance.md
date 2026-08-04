## Introduction and Scope

This review synthesizes peer-reviewed and standards-track literature relevant to defining a formal information entity — termed here **Condition_Evidence_ID** — capable of representing sensor-derived observations, assessment results, or condition evidence from vibration data while preserving provenance and avoiding the conflation of statistical confidence with physical damage severity. Six literature domains were searched: structural health monitoring (SHM) ontologies, condition-based monitoring, BIM/Digital Twin information models, asset management standards, scientific data provenance frameworks, and observation/evidence-uncertainty models. Sources are marked as full-text (FT), abstract-only (AO), or metadata/standard-document (MD) where full content was not directly retrievable.

## Representing Sensor-Derived Observations and Evidence in Prior Work

The W3C/OGC **SOSA/SSN** ontology is the most mature formalization of a "Result" entity that is distinct from the raw stimulus and the sensor itself. SOSA models `sosa:Observation` as an event that generates a `sosa:Result`, with `sosa:hasSimpleResult` for literal values or `sosa:hasResult` for a fully described result individual, and explicitly separates `sosa:phenomenonTime` (when the observed condition held) from `sosa:resultTime` (when the observation act completed). This time-role separation is directly relevant to a Condition_Evidence_ID, since it structurally supports distinguishing "when the vibration state existed" from "when the evidence was produced." SOSA's primary classes are explicitly aligned to **PROV-O**: `sosa:hasResult` is a sub-property of `prov:generated`, `sosa:isResultOf` of `prov:wasGeneratedBy`, and `sosa:madeByActuator`/analogous sensor properties align with `prov:wasAssociatedWith`. This alignment is the clearest literature bridge between "observation result" and "evidence record with provenance."[^1][^2][^3]

In the SHM domain specifically, an ontological framework for SHM was proposed to formalize monitoring objects and procedures using OWL, establishing that "evidence" in this domain has historically been represented as isolated dataset/procedure descriptions rather than a first-class, provenance-bearing entity  (FT-partial). A more directly relevant contribution is the **Structural Health Monitoring Ontology (SHMO)**, a modular ontology integrating IFC-based BIM (ifcOWL), SOSA for sensing, a purpose-built Sensor Network Ontology (SNO), the **Damage Topology Ontology (DOT)**, the **DASB assessment ontology** for inspection results, and a Structural Analysis Ontology (SAO)  (FT-partial). SHMO is significant because it is one of the only published frameworks that links sensor observation classes to a distinct damage/assessment result class rather than merging them.[^4][^5]

The **Damage Topology Ontology (DOT)** by Hamdan et al. explicitly separates damage *topology* (spatial extent, affected element) from damage *classification* and *assessment*, and is designed to be extended by mechanical-degradation modules — a structural precedent for keeping "evidence of a condition" distinct from "diagnosis of severity"  (FT). DOT's design intent — enabling initial recording of damage without geometry, then later linking richer representations — mirrors the thesis requirement that evidence be recorded even before full interpretation is finalized.[^6][^7]

## Metadata Linking Evidence to Sensor, Raw Data, Session, Location, Preprocessing, Model, and Confidence

No single study in the reviewed literature defines all eight linkage fields (sensor, raw data, acquisition session, component location, preprocessing, algorithm/model version, checkpoint, confidence) in one entity. Coverage is distributed:

- **Sensor linkage**: SOSA's `sosa:madeBySensor`, `sosa:hasFeatureOfInterest`, and `sosa:observedProperty` properties formally connect a Result back to the originating sensor and the property/location observed. SSN Extensions further support `sosa:ObservationCollection`, allowing homogeneous batches of observations to share sensor, feature-of-interest, and time metadata — relevant to representing an acquisition "run" or "session"  (FT).[^2][^8][^1]
- **Raw data / derivation linkage**: PROV-O's `prov:wasDerivedFrom` and `prov:used` properties are the literature-established mechanism for tracing a derived Entity (e.g., a processed feature) back to a raw Entity (e.g., raw time series) through an intervening Activity  (FT).[^9][^10]
- **Component location**: Addressed indirectly through `sosa:hasFeatureOfInterest` (SOSA) and through DOT's topology classes that relate damage instances to construction elements and spatial zones.[^7][^6]
- **Preprocessing and algorithm/model version**: Not addressed by SOSA/SSN or DOT. The closest literature analogue is from ML provenance research: a production ML library's provenance design explicitly records dataset transformation lists, training algorithm, hyperparameters, and machine/environment state as required provenance fields for a Model or Evaluation entity  (FT-partial). "Model Cards" literature similarly recommends recording training data source, license, framework, and precision (e.g., fp16/fp32) as standard provenance fields for a model output  (AO/FT-partial).[^11][^12]
- **Model checkpoint / version identity**: The DataCite Metadata Schema formalizes `Version`, together with `RelatedIdentifier` relation types `IsNewVersionOf`/`IsPreviousVersionOf` (sequential versions) and `HasVersion`/`IsVersionOf` (canonical-to-instance versioning), as the accepted mechanism for uniquely identifying a specific state of a versioned artifact. This is the strongest literature precedent for a "model checkpoint" identifier field, although it originates in dataset/software citation practice rather than SHM specifically.[^13][^14][^15][^16]
- **Confidence or uncertainty**: Vibration-based SHM literature treats uncertainty as a first-class, quantified output distinct from the damage decision itself. Kernicky and Whelan explicitly state that a damage-detection method "needs to not only be capable of providing parameter estimates for damage identification, but also provide information on the confidence that may be placed on the identification," using interval bounds around identified stiffness parameters rather than a severity label  (FT). Bayesian and interval-based operational modal analysis studies similarly report confidence intervals/posterior distributions on modal parameters as separate outputs from the damage inference itself  (AO, several FT-partial). Dzvukamanja's dissertation frames the deliverable of a UQ-augmented SHM framework explicitly as "a quantitative measure of confidence in the diagnosis," reported alongside — not merged with — the damage-sensitive feature value  (AO).[^17][^18][^19][^20][^21][^22][^23]

## Data-Quality Warnings and Validity Status

The **W3C Data Quality Vocabulary (DQV)** is the principal literature source for representing data-quality metadata as structured statements rather than free text. DQV defines `dqv:QualityAnnotation` (feedback/certificates), `dqv:QualityMeasurement` (quantitative/qualitative metric values against a `dqv:Metric` under a `dqv:Dimension`), `dqv:QualityPolicy`, and a `dqv:QualityMetadata` container class that groups these statements and can be linked to PROV-O for provenance of the quality statement itself. This directly supports representing a "data-quality warning" as a typed annotation attached to evidence, and a "validity status" as a `dqv:QualityMeasurement` against a defined dimension (e.g., completeness, accuracy). No SHM-specific study was found that reuses DQV directly, indicating this is a cross-domain transfer rather than an established SHM practice — classified as **indirectly supported**.[^24][^25][^26][^27][^28]

## Traceability to Creator, Source, Operation, Timestamp, and Version

PROV-O provides the canonical, most literature-validated model for this requirement: `prov:Entity`, `prov:Activity`, and `prov:Agent` are the three top-level classes, with `prov:wasAttributedTo` linking an entity to its responsible agent, `prov:wasGeneratedBy` linking an entity to the activity that produced it, and `prov:startedAtTime`/`prov:endedAtTime` recording activity timestamps. DataCite's metadata-provenance tracking service (operational since March 2019) is a production-scale implementation of exactly this pattern for dataset DOIs, recording `prov:wasGeneratedBy`, `prov:generatedAtTime`, `prov:wasDerivedFrom`, and `prov:wasAttributedTo` for every metadata change  (FT). Together, these establish full creator–source–operation–timestamp–version traceability as an **established** literature pattern, though again not natively embedded in an SHM- or BIM-specific ontology.[^10][^29][^30][^9]

## Context, Intended Use, Limitations, and Bounded Validity

Several literature strands explicitly capture scope/limitation metadata, though terminology varies:

- ML provenance and Model Card literature explicitly requires recording "intended uses," "relevant bias or fairness analysis," and licensing/context as mandatory fields distinct from performance metrics  (FT-partial/AO).[^12][^11]
- DataCite versioning guidance recommends a `description` field (with `descriptionType="Methods"`) to record what changed and why, and to note whether newer versions may supersede a cited snapshot — an explicit bounded-validity statement  (FT).[^16]
- DQV's non-quantifiable "Quality Note" and `dqv:QualityPolicy` classes are designed to record contextual quality statements that do not reduce to a single metric, which is analogous to recording assumptions or bounded applicability of evidence.[^28][^31]
- No SHM/vibration-specific study explicitly formalizes an "intended use" or "bounded validity" field for a damage-evidence record; this is a **thesis-defined gap**, addressed only by analogy from adjacent domains.

## Confidence vs. Damage Severity: Explicit Literature Distinctions

Multiple vibration-SHM papers explicitly warn against conflating statistical confidence with physical damage magnitude. Kernicky and Whelan note that "while it can be confidently stated that no significant damage is present [in one parameter], the same confidence cannot be placed on [another]," framing confidence as a property of the *estimate*, not of the *structure's condition*. The interval-arithmetic and Bayesian FFT literature consistently reports damage magnitude (e.g., stiffness ratio α) and its uncertainty interval as two separate numeric outputs, never merging them into a single "severity score". Similarly, non-probabilistic surrogate-model studies compute a "Possibility of Damage Existence (PoDE)" and a separate "Damage Measure Index (DMI)," explicitly keeping detection likelihood distinct from damage extent. These findings substantiate the thesis constraint that a Condition_Evidence_ID must carry confidence/uncertainty as an independent field from any damage-severity indicator, and that neither should be inferred from the other.[^19][^23][^32][^17]

## Evidence Summary Table

| Study | Evidence entity | Raw-data linkage | Sensor linkage | Context metadata | Confidence/uncertainty | Provenance | Versioning | Scope/limitation |
|---|---|---|---|---|---|---|---|---|
| SOSA/SSN (Janowicz et al. 2018 [^3]; W3C 2017 [^1]) | sosa:Result / Observation | Not modeled directly | sosa:madeBySensor, hasFeatureOfInterest | phenomenonTime vs resultTime | Not modeled | Aligned to PROV-O (generated, wasGeneratedBy) | Not modeled | Not modeled |
| SHMO (Smarsly et al. [^5]) | Assessment result (via DASB) | Partial via SNO | Yes (SNO+SOSA) | Partial (IFC location) | Not addressed | Implicit via module linkage | Not modeled | Not addressed |
| DOT (Hamdan et al. [^6][^7]) | Damage instance (topology) | Not modeled | Indirect (location/element) | Spatial/element context | Not modeled | Not modeled | Not modeled | Separates topology from classification |
| Kernicky & Whelan 2019 [^17][^20] | Parameter estimate + interval | Modal test data referenced narratively | Sensor count/placement discussed | Test configuration described in text | Explicit interval confidence, separate from damage ratio | Not formalized | Not modeled | Identifiability limits discussed |
| Dzvukamanja 2008 [^18] | Damage-sensitive feature + probability | Raw vibration test data | Referenced narratively | Environmental/operational conditions noted | Explicit probabilistic confidence measure | Not formalized | Not modeled | Generalization limits discussed |
| PROV-O (Lebo et al. 2013 [^10]) | Generic Entity | wasDerivedFrom | wasAssociatedWith | Not domain-specific | Not modeled | Core model (Entity/Activity/Agent) | Not modeled | Not modeled |
| DQV (W3C 2016 [^24]; Albertoni & Isaac 2020 [^25]) | QualityMeasurement/Annotation | Linked via PROV-O | Not modeled | Quality dimension/category | Represented as quality metric, not physical confidence | Reuses PROV-O | Not modeled | QualityPolicy/Note fields |
| DataCite Metadata Schema [^13][^15][^16] | Versioned resource record | RelatedIdentifier (IsDerivedFrom) | Not applicable | Description/Methods field | Not modeled | wasGeneratedBy, wasAttributedTo (activities API) | Version, IsNewVersionOf/IsPreviousVersionOf, HasVersion/IsVersionOf | Description field for change scope |
| ML provenance/Model Cards [^11][^12] | Model/Evaluation provenance object | Dataset provenance (source, hash, timestamp) | Not applicable | Intended use, licensing, bias notes | Performance metrics reported separately from provenance | Trainer/Dataset/Model provenance chain | Framework/hyperparameter version tracked | Explicit intended-use/limitation fields |

## Classification of Candidate Metadata Fields

**Established by prior research** (direct, named literature support):
- Sensor identity and observed property/feature-of-interest linkage — SOSA `madeBySensor`, `observedProperty`[^1][^2]
- Result/observation timestamp, split into phenomenon time and result time — SOSA[^3][^1]
- Provenance chain (creator/agent, generating activity, derivation from prior entity) — PROV-O, operationalized by DataCite[^29][^30][^9][^10]
- Version identifier and version-lineage relations (IsNewVersionOf, HasVersion) — DataCite Metadata Schema[^14][^15][^13][^16]
- Confidence/uncertainty as an interval or probabilistic measure, reported independently of damage magnitude — vibration-based SHM UQ literature[^18][^21][^22][^23][^32][^17][^19]
- Data-quality measurement against a named dimension/metric — W3C DQV[^25][^24]

**Supported indirectly by multiple studies** (cross-domain analogues, not SHM-native):
- Component/location linkage — supported by SOSA feature-of-interest and DOT topology classes but not integrated with vibration-confidence metadata in any single study[^6][^7][^1]
- Preprocessing/transformation step description — supported by ML provenance's dataset-transformation logging and DataCite's Methods-typed description field, not by SHM ontologies[^12][^16]
- Algorithm/model version and checkpoint identity — supported by ML provenance and DataCite versioning, not by SOSA/SSN or DOT[^15][^11][^12]
- Data-quality warning/validity-status flag — supported by DQV's QualityAnnotation/QualityPolicy classes, not natively present in SHM ontologies[^24][^28]
- Intended use / bounded validity statement — supported by Model Card and DataCite description-field practice, absent from vibration-SHM literature[^11][^16]

**Thesis-defined requirement** (no direct or indirect literature precedent found for the exact field, requiring the thesis to specify it):
- Acquisition session/run identifier as a distinct entity linking a batch of observations to a single field visit or test campaign (SSN's ObservationCollection supports batching but does not define a "session" concept with operational metadata such as operator, weather, equipment calibration state)[^8]
- A single unified Condition_Evidence_ID that co-locates sensor linkage, raw-data linkage, preprocessing, model/checkpoint version, confidence, and scope/limitation in one schema — no reviewed study integrates all these fields in one entity
- Explicit non-equivalence flag or schema-level separation preventing confidence/uncertainty fields from being interpreted as severity fields — implied by SHM UQ literature's practice but never formalized as a schema constraint

**Q2 — Evidence currently insufficient** (topic touched on tangentially; further primary-source retrieval needed):
- Formal ontological treatment of "acquisition session" as a first-class entity in SHM (beyond SSN's ObservationCollection pattern)[^8]
- Peer-reviewed SHM-specific application of DQV or an equivalent quality vocabulary to vibration-monitoring data streams
- Formal linkage of model checkpoint identifiers to physical sensor/location metadata within a single published SHM information model
- Legal/audit-grade "chain of custody" formalization for condition evidence in a BIM/Digital Twin context (partial precedent only in blockchain-based DT provenance research for facilities predictive asset management, which is abstract-only in the retrieved source)  (AO)[^33]

## Proposed Minimum Metadata Dictionary for Condition_Evidence_ID

The dictionary below distinguishes fields with direct literature grounding from those the thesis must define to close the gaps identified above.

| Field | Status | Literature basis |
|---|---|---|
| Evidence_ID (unique identifier) | Literature-derived | DataCite Identifier/DOI pattern [^13][^15] |
| Source_Sensor_ID | Literature-derived | SOSA madeBySensor [^1] |
| Raw_Data_Reference (link/hash to unprocessed signal) | Literature-derived | PROV-O wasDerivedFrom, ML provenance dataset hash [^9][^12] |
| Acquisition_Session_ID | Thesis-proposed | Extends SSN ObservationCollection pattern [^8] |
| Component_Location_Reference | Literature-derived (indirect) | SOSA hasFeatureOfInterest, DOT topology [^1][^6] |
| Phenomenon_Time / Result_Time | Literature-derived | SOSA time roles [^1][^3] |
| Preprocessing_Steps_Description | Thesis-proposed (indirect basis) | ML provenance transformation logging, DataCite Methods description [^12][^16] |
| Algorithm_Model_ID | Literature-derived (indirect) | Model Card provenance fields [^11][^12] |
| Model_Checkpoint_Version | Literature-derived (indirect) | DataCite Version/IsNewVersionOf [^13][^15] |
| Confidence_Or_Uncertainty_Value | Literature-derived | Vibration-SHM UQ interval/probabilistic confidence [^17][^18][^23] |
| Confidence_Severity_Non-Equivalence_Flag | Thesis-proposed | Formalizes practice implied in [^17][^32] but never schematized |
| Data_Quality_Warning | Literature-derived (indirect) | W3C DQV QualityAnnotation [^24][^28] |
| Validity_Status | Literature-derived (indirect) | W3C DQV QualityMeasurement against Dimension [^24][^27] |
| Creator_Agent_ID | Literature-derived | PROV-O wasAttributedTo, DataCite Creator [^10][^29] |
| Generating_Activity_ID | Literature-derived | PROV-O wasGeneratedBy [^9][^10] |
| Intended_Use_Statement | Thesis-proposed (indirect basis) | Model Card "intended uses" field [^11] |
| Bounded_Validity_Or_Limitation_Note | Thesis-proposed (indirect basis) | DataCite Methods description, DQV QualityPolicy [^28][^16] |
| Version_Lineage_Reference (IsNewVersionOf/IsPreviousVersionOf) | Literature-derived | DataCite RelatedIdentifier [^13][^14][^15] |

Mandatory fields for a minimally sound Condition_Evidence_ID, based on convergence across SOSA/PROV-O/DQV/DataCite and SHM uncertainty literature, are: Evidence_ID, Source_Sensor_ID, Raw_Data_Reference, Phenomenon_Time/Result_Time, Confidence_Or_Uncertainty_Value, Creator_Agent_ID, Generating_Activity_ID, and Model_Checkpoint_Version. Acquisition_Session_ID, Confidence_Severity_Non-Equivalence_Flag, Intended_Use_Statement, and Bounded_Validity_Or_Limitation_Note remain thesis-defined additions necessary to close documented gaps in SHM-specific formalization, and should be explicitly justified in the thesis as novel contributions rather than presented as literature-established practice.

---

## References

1. [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/) - The Semantic Sensor Network (SSN) ontology is an ontology for describing sensors and their observati...

2. [The SOSA/SSN Ontology: A Joint W3C and OGC Standard Specifying the Semantics of Sensors, Observations, Actuation, and Sampling](https://www.semantic-web-journal.net/system/files/swj1804.pdf)

3. [SOSA: A Lightweight Ontology for Sensors, Observations ...](https://arxiv.org/abs/1805.09979) - viết bởi K Janowicz · 2018 · Trích dẫn 771 bài viết — The Sensor, Observation, Sample, and Actuator ...

4. [An ontological approach to structural health monitoring](https://eprints.whiterose.ac.uk/id/eprint/169410/1/imac_20_GT_1.pdf)

5. [Ontology- and temporal-logic-based knowledge ...](https://smarsly.wordpress.com/wp-content/uploads/2026/03/smarsly2026hj.pdf)

6. [Articles - Über - Al-Hakam Hamdan](https://www.hakam-hamdan.de/articles) - The Damage Topology Ontology (DOT) is presented, a web ontology that provides terminology to represe...

7. [An ontological model for the representation of damage to ...](https://ceur-ws.org/Vol-2389/05paper.pdf) - viết bởi AH Hamdan · Trích dẫn 87 bài viết — The Damage Topology Ontology (DOT) is presented, a web ...

8. [Extensions to the Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn-ext/) - The Semantic Sensor Network (SSN) ontology is an ontology for describing sensors and their observati...

9. [[PDF] PROV and Real Things - MSSANZ](https://www.mssanz.org.au/modsim2015/C4/cox.pdf)

10. [The University of Manchester Research](https://pure.manchester.ac.uk/ws/portalfiles/portal/31956469/FULL_TEXT.PDF)

11. [Responsible AI @ ONNX: Metadata, Model Cards, and Provenance](https://www.youtube.com/watch?v=U6L-bBKApA4) - The space of AI is growing rapidly. At this pace, it can be challenging for key AI stakeholders to i...

12. [[PDF] Provenance Design and Evolution in a Production ML Library](https://openreview.net/pdf?id=VrbDf3UDgv)

13. [Versioning](https://support.datacite.org/docs/versioning) - When content underlying a DOI is updated, we recommend updating the DOI metadata and, for major chan...

14. [Connecting to Works - DataCite Support](https://support.datacite.org/docs/connecting-to-works) - Related identifiers The DataCite Metadata Schema includes a RelatedIdentifier property to facilitate...

15. [DataCite-MetadataKernel_v4.1.pdf](https://schema.datacite.org/meta/kernel-4.1/doc/DataCite-MetadataKernel_v4.1.pdf)

16. [Practical Guidelines for Versioning with DataCite](https://nfdixcs.org/fileadmin/PR/NFDIxCS/guidelines_for_versioning_research_data_in_space_and_time__1_.pdf)

17. [Vibration-based damage detection with uncertainty quantification by structural identification using nonlinear constraint satisfaction with interval arithmetic - Timothy Kernicky, Matthew Whelan, Ehab Al-Shaer, 2019](https://journals.sagepub.com/doi/10.1177/1475921718806476) - Structural identification has received increased attention over recent years for performance-based s...

18. [Application of vibration-based damage detection techniques to civil infrastructure : incorporating uncertainty quantification](https://open.uct.ac.za/items/78dff31a-1553-4853-b669-585946af3051) - Literature was reviewed with an aim to identify research needs in vibration based damage detection t...

19. [Efficient Bayesian FFT method for damage detection using ambient vibration data with consideration of uncertainty](https://onlinelibrary.wiley.com/doi/abs/10.1002/stc.2659)

20. [Vibration-based Damage Detection with Uncertainty ...](https://ninercommons.charlotte.edu/record/3992/files/whelmat_etal_vibba_ir_2018.pdf) - viết bởi M Whelan · 2018 — Abstract. Structural identification has received increased attention over...

21. [Uncertainty quantification in the vibration-based damage assessment of a reinforced concrete beam](https://past.isma-isaac.be/downloads/isma2010/papers/isma2010_0371.pdf)

22. [UNCERTAINTY QUANTIFICATION IN OPERATIONAL MODAL ANALYSIS AND CONTINUOUS MONITORING OF SPECIAL STRUCTURES](https://core.ac.uk/download/pdf/302962411.pdf)

23. [Quantifying uncertainty for structural damage identification in the presence of model errors from a deterministic sensitivity-based regime](https://www.sciencedirect.com/science/article/abs/pii/S014102962200774X) - Structural damage identification is often recast as the procedure to find the damage parameters from...

24. [Data on the Web Best Practices: Data Quality Vocabulary](https://www.w3.org/TR/vocab-dqv/) - Quality metadata containers (dqv:QualityMetadata) can group together different quality statements, s...

25. [Introducing the Data Quality Vocabulary (DQV) - Riccardo Albertoni, Antoine Isaac, 2020](https://journals.sagepub.com/doi/full/10.3233/SW-200382) - The Data Quality Vocabulary (DQV) provides a metadata model for expressing data quality. DQV was dev...

26. [Data Quality Vocabulary (DQV) by World Wide Web Consortium (W3C) on TriplyDB](https://triplydb.com/w3c/dqv) - The Data Quality Vocabulary (DQV) provides a framework in which the quality of a dataset can be desc...

27. [Quality of Metadata in Open Data Portals](https://zaguan.unizar.es/record/109641/files/texto_completo.pdf)

28. [ASSESSMENT SUMMARY v1.0.0 - Interoperable Europe Portal](https://interoperable-europe.ec.europa.eu/sites/default/files/distribution/access_url/2024-06/82a08042-3be9-424e-a7ea-8c51f5793e72/CAMSS_Assessment%20Summary_DQV_EIF%20Scenario_v2.0.pdf) - DQV is a vocabulary for expressing data quality and according to the W3C Data on the Web Best. Pract...

29. [Abstract](https://arxiv.org/html/2412.05128v2)

30. [Tracking metadata provenance](https://support.datacite.org/docs/tracking-provenance) - 📘 Provenance definition according to the Prov Data Model (PROV-DM): Provenance is information about ...

31. [Spesifikasjon for beskrivelse av kvalitet på datasett](https://data.norge.no/specification/spesifikasjon-for-beskrivelse-av-kvalitet-pa-datasett) - Spesifikasjon for beskrivelse av kvalitet på datasett

32. [Uncertainty Handling in Structural Damage Detection via Non-Probabilistic Meta-Models and Interval Mathematics, a Data-Analytics Approach](https://www.mdpi.com/2076-3417/11/2/770?type=check_update&version=1) - Recent advancements in sensor technology have resulted in the collection of massive amounts of measu...

33. [Blockchain-based digital twin data provenance for predictive asset management in building facilities](http://hj.diva-portal.org/smash/record.jsf?pid=diva2:1816800) - Purpose: The purpose of this study is to focus on structured data provision and asset information mo...

