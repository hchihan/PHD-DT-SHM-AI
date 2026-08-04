# G1 TO G2 CONDITION EVIDENCE INTERFACE v1.0

**Document type:** Implementation-neutral interface specification  
**Status:** Proposed v1.0 for schema review  
**Current gate state:** Gate 1 is `OPEN/NOT READY`; this specification does not claim Gate 1, Gate 2, or Gate 3 completion.  
**Governing scope:** Limited-FEM. FEM is nominal, uncalibrated, reference-only, not used for damage diagnosis.  
**Contract boundary:** Gate 1 laboratory condition/state-change evidence to Gate 2 Evidence-to-Action Traceability Specification Readiness.

## 1. Purpose

This document defines the auditable handoff contract by which Gate 1 may provide laboratory condition/state-change evidence to Gate 2. It specifies:

1. required Gate 1 deliverables;
2. the meaning and granularity of a canonical `Condition_Evidence` record;
3. required, optional, conditional, and prohibited fields;
4. provenance from raw source through processing and model result;
5. sensor and BIM/component associations;
6. candidate versus verified BIM binding;
7. versioning, review, supersession, withdrawal, and immutability;
8. CEI as an explicit mandatory metadata structure attached to every evidence record;
9. testable integrity rules and negative fixtures;
10. handoff and readiness conditions; and
11. prohibited downstream interpretations.

This is not a software guide, database implementation manual, website specification, ontology-only specification, SHACL-only specification, Revit parameter guide, IFC embedding mandate, or Dynamo graph specification.

## 2. Research positioning

| Thành phần | Nội dung |
|---|---|
| RQ upstream | RQ1 |
| RQ downstream | RQ2 |
| WP | WP1 → WP2 |
| Chapter | Chương 4 → Chương 5 |
| Paper | Paper 1 → Paper 2 |
| Gate | G1 → G2 |
| Evidence type | Laboratory evidence → Information traceability |

Locked research chain:

```text
Vibration data
→ condition/state-change evidence (+ CEI)
→ BIM-linked component
→ Inspection_Record
→ Action_Record
→ Status_Event
→ inspection-maintenance action support
```

Current governance normalizes the identifier chain as:

```text
Sensor_ID
→ BIM_GUID
→ Condition_Evidence_ID
→ Inspection_Record_ID
→ Action_Record_ID
```

`Action_Status` is a controlled current-state projection or attribute of `Action_Record_ID`; it is not a substitute for `Action_Record_ID`. State changes are represented by downstream `Status_Event` records.

Upstream evidence is limited to controlled laboratory state-change evidence. It does not establish field damage, defect diagnosis, stiffness degradation, maintenance priority, or an authorized action.

## 3. Source availability and evidence basis

### 3.1 Mandatory governance and research sources

| Source | Availability / read status | Evidence basis used | Limitation |
|---|---|---|---|
| `00_GOVERNANCE/MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md` | Read completely; current highest source of truth | Locked RQ/WP/Paper/Gate mapping, identifier chain, explicit mandatory CEI structure, accountability, G2/G3 requirements, Limited-FEM boundary | G1 remains experimentally open |
| `00_GOVERNANCE/RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md` | Read completely; current approved structure | Confirms RQ1/WP1/C4/Paper 1/G1 and RQ2/WP2/C5/Paper 2/G2-G3-G6; CEI and preregistered CQs | Does not define instance-level schema |
| `00_GOVERNANCE/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` | Read completely | Resolves current versus archived authority | Historical files remain context only |
| `01_CURRENT_CONTROL/MASTER_INDEX_CURRENT.md` | Read completely | Navigation authority for existing current files and gate status | Contains legacy relative paths; source hierarchy prevails |
| `00_GOVERNANCE/MASTER_RESEARCH_CHARTER.md` | Read completely | Concise navigation entry; current chain uses `Action_Record_ID`; Paper 1 claims remain candidate pending G1 closure | Defers to the full v2.1 charter read above |
| `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` | Read completely; archived and superseded | Historical RQ/WP/chapter/paper/gate mapping and Limited-FEM rationale | Historical terminal `Action_Status` is superseded by current `Action_Record_ID` chain |
| `00_GOVERNANCE/RESEARCH_DIRECTION_AND_SCOPE.md` | Read completely | Thesis is information-management and inspection-decision traceability; separates laboratory evidence, field feasibility, and decision support | Explanatory document subordinate to current charter |
| `00_GOVERNANCE/RESEARCH_ARCHITECTURE.md` | Read completely | Four-layer architecture; G2 requires identifier integrity, bidirectional traceability, and chain completeness | Does not define the detailed interface fields |
| `01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md` | Read completely | Current gate is G1; run registry, LORO/LOGO decision, and model provenance remain unresolved; G2 criteria precede schema/demo | Contains navigation/version drift; current charter prevails |
| `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md` | Read completely; archived | Accepted Limited-FEM rationale; no calibration, diagnosis, or quantitative lab-to-field transfer | Historical supporting provenance, not current operational authority |
| `G2_G3_PAPER2_REVISED_ROADMAP_v1.1.md` | Missing repository-wide | None | **Evidence is currently insufficient.** |
| `G2_G3_DUAL_PAPER_ROADMAP_v1.2.md` | Missing repository-wide | None | **Evidence is currently insufficient.** |
| `G2_G3_ROUND1_DEEP_READ_AND_NOVELTY_BOUNDARY.md` | Read completely | Minimum evidence/BIM/provenance fields; strict negative-test definition; candidate versus verified identity boundary | Bellon full text was incomplete in that report |
| `G2_G3_ROUND2_INSPECTION_ACTION_MODEL_DEEP_READ.md` | Read completely | Minimum Condition_Evidence and Inspection/Action/Status models; workflow and accountability boundaries | Xu full text was unavailable in that report |
| `G2_G3_SCREENING_EVIDENCE_AND_GAP_REPORT.md` | Read completely | Prior-art boundary; integrated traceability, integrity, and human-review gaps | Screening evidence does not replace project execution evidence |

### 3.2 Gate 1 governance and execution sources

The following were read completely:

- `00_GOVERNANCE/EVIDENCE_GATES_v2.1.md`;
- `03_PAPERS/PAPER_1/PAPER1_DIRECTION_AND_GATE_v2.1_20260719.md`;
- `03_PAPERS/PAPER_1/PAPER1_IT_EXECUTION_SPEC_v5_20260719.md`;
- `03_PAPERS/PAPER_1/PAPER1_GATE1_INTERNAL_QA_CHECKLIST_v1.md`;
- `03_PAPERS/PAPER_1/IT_REQUESTS/PAPER1_GATE1_DATA_ANALYSIS_REQUESTS_FOR_IT_v2.md`;
- `03_PAPERS/PAPER_1/GATE1_EVIDENCE/PAPER1_GATE1_CLAIM_EVIDENCE_AUDIT_v2.md`;
- `03_PAPERS/PAPER_1/GATE1_EVIDENCE/PAPER1_GATE1_READINESS_REPORT_v2.md`; and
- `02_EVIDENCE_BASE/RQ1_GATE1/03_RQ1_GATE1_METHOD_EVIDENCE_ADDENDUM_v1.0_20260718.md`.

These sources establish that G1 is experimentally `OPEN/NOT READY`. They require a locked dataset/run/file/sensor/model/fold/reproducibility package, run-aware splitting before windowing, train-fold-only preprocessing, retained per-window predictions, recording/run-level aggregation, uncertainty, data-quality evidence, code/environment provenance, and signed acceptance. Planned filenames are not evidence of completed artifacts.

### 3.3 Extant Gate 1 data and result evidence

| Artifact group | Read / inspected | What it currently supports | Limitation for this interface |
|---|---|---|---|
| `CANONICAL_THREE_CAMPAIGN_DATASET/00_README.md`, `03_CHANNEL_QUALITY_RULES.md`, `07_DATA_DICTIONARY.md`, `08_DATASET_VARIANTS.md`, `09_DATASET_VALIDATION_REPORT.md`, `10_REPRODUCIBILITY_MANIFEST.md`, `11_DATASET_HANDOFF_FOR_IT.md` | Read completely | Intended canonical schemas, quality vocabulary, analysis sets, environment and script-hash declarations, handoff constraints | Referenced source registries, NPZ files, fold manifests, scripts, and package archive are absent |
| `CANONICAL_THREE_CAMPAIGN_DATASET/08_AUTOMATED_VALIDATION_RESULTS.csv` | All 12 rows inspected; all report `PASS` | Validation assertions for reported package counts/shapes/smoke tests | Proxy output only; no source rows, execution timestamp, output hashes, or fold membership |
| `THREE_CAMPAIGN_REANALYSIS/00_EXECUTIVE_REPORT.md` and `01_ENVIRONMENT_PROVENANCE.md` | Read completely | Preliminary pipeline, processing, models, environment, code-hash declarations, and limitations | Uses old `S1/S2/S3` block-position identity for Campaigns 1-2; not verified physical-sensor identity; G1 remains open |
| `03_DATA_QUALITY_AND_PROVENANCE_LOG.csv` | All 66 rows inspected | Recording-name quality/provenance warnings and campaign-level sensor-column stability | No source hash, canonical Recording_ID, physical Sensor_ID, inclusion decision, or quantitative quality registry |
| `05_WITHIN_CAMPAIGN_LORO_RESULTS.csv` | All 238 rows inspected | Held-out-run aggregate metrics by campaign/config/model | No predictions, probabilities, fold membership, model hash, complete seed coverage, or canonical physical-sensor mapping |
| `06_CROSS_CAMPAIGN_RESULTS.csv` | All 36 rows inspected | Held-out-campaign aggregate metrics | Near-chance results; old block-position sensor identity; no source prediction provenance |
| `07_BASELINE_MODEL_COMPARISON.csv`, `09_SENSOR_CONFIGURATION_RESULTS.csv` | All rows inspected | Derived aggregate summaries | Summary proxies; sensor summary mixes model families and incomplete CNN coverage |
| `08_PERMUTATION_RESULTS.csv` | All 300 rows inspected | Three limited permutation result sets | Missing model/seed/assignment/real-score fields; not a complete empirical-null package |
| `11_SENSITIVITY_RESULTS.csv` | All 10 rows inspected | Limited representative sensitivity cases | Missing model/seed/split provenance; some values cannot be reconciled to main rows |
| Three confusion-matrix CSVs | All rows inspected | Aggregate class-count examples | No recording/window IDs, probabilities, or complete coverage |
| `13_TRAINING_CURVES/README.md` | Read completely | Disclosure that curves were not retained | No per-epoch histories or checkpoints |
| `CAMPAIGN_DOCUMENTATION/Checklist_Campaign_3_Gate1.docx` | Located; binary content not readable through the available file reader | None used | **Evidence is currently insufficient.** |

### 3.4 Required but missing Gate 1 artifact families

The expected `05_DATA_CODE_AND_EXPERIMENTS/G1_EXECUTION_PACK/` does not exist. Required artifacts currently missing include, without limitation:

- locked Dataset Manifest and `RUN_REGISTRY_LOCKED.csv`;
- raw file provenance/source-hash registry;
- canonical sensor/channel metadata registry;
- confirmed independent-unit and fold registry;
- split-before-windowing and train-only-preprocessing audits;
- locked model configuration and complete seed registry;
- per-window and per-recording prediction files;
- complete per-run/fold metrics and uncertainty package;
- model/checkpoint hashes and Git commit;
- environment lockfile/container digest;
- complete reproducibility package;
- `G1_ACCEPTANCE_MATRIX.md` and sign-off; and
- accepted `Condition Evidence Register`.

The repository contains useful documentation and aggregate proxy evidence, but no accepted G1 `Condition_Evidence` payload. **Evidence is currently insufficient.**

### 3.5 Evidence conflicts that remain open

- The independent unit remains unresolved between recording, run, and replicate group.
- Gate 1 documents contain differing window plans; this interface does not select a window length, overlap, or threshold.
- Permutation granularity differs across planning documents and remains unresolved.
- The reanalysis uses block-position sensors while canonical documentation describes later physical-sensor reassignment; they must not be silently joined.
- Exact CEI/quality-confidence calibration is not locked.

## 4. Interface scope

| Scope class | Included |
|---|---|
| Core Scope | Gate 1 deliverable contract; Condition_Evidence semantics; source/run/recording/sensor/window/model provenance; component context; candidate/verified BIM binding; review/version/supersession; integrity rules; negative fixtures; G2 handoff/readiness |
| Supporting Scope | Raw source and preprocessing references; window predictions as supporting analytical records; recording evidence candidates; campaign synthesis; optional nominal FEM reference metadata; future Inspection_Record linkage fields |
| Future Work | Field acquisition; field feasibility evidence; full Inspection_Record/Action_Record/Status_Event implementations; storage technology; user interface; deployment architecture; policy-specific authorization workflows |
| Out of Scope | Field damage diagnosis; stiffness-degradation inference; calibrated FEM; RUL; predictive maintenance; weighted Health Index; automated inspection or action authorization; lab-to-field classifier transfer; software implementation; Revit/IFC/Dynamo changes |

Optional FEM metadata must carry the statement: `nominal, uncalibrated, reference-only, not used for damage diagnosis`. FEM cannot create or validate `Condition_Evidence` and cannot be a mandatory identifier dependency.

## 5. Definitions

| Term | Normative definition |
|---|---|
| `Source_Data` | An immutable raw acquisition artifact or registered source object identified in the Dataset Manifest and protected by a cryptographic hash. It is not a preprocessed array or model result. |
| `Run` | The locked independent or parent experimental unit identified by `Run_ID`, with campaign/session, controlled state, excitation, recordings, sensors, inclusion status, and operator notes. Its exact relationship to replicate groups remains an open Gate 1 decision. |
| `Window_Prediction` | A model output for one registered window, retaining window, recording, run, fold, sensor, preprocessing, model, and class-output provenance. It is a supporting analytical record, not official Condition_Evidence. |
| `Condition_Evidence` | A reviewed evidence claim with full provenance, formed by a pre-specified aggregation/evidence-formation rule from one `Run_ID` or a defined recording-level aggregation, scoped to one component context. It is not a diagnosis, severity, priority, or action. |
| `Evidence_Claim` | The bounded proposition represented by a Condition_Evidence record: what laboratory state distinction or state-change support was observed, at what granularity and under which method, quality, and limitation boundary. |
| `Evidence_Quality` | A structured description of data validity, model/method confidence, run/fold variability, sensor completeness, reproducibility status, quality flags, and limitations. It is not physical damage severity. |
| `CEI` | The explicit mandatory confidence/evidence indicator metadata structure attached to every `Condition_Evidence_ID`. It contains at least evidence-validity status, model confidence, run/fold variability, sensor configuration, data-quality status, provenance, and timestamp/version. It is not a scalar, Health Index, severity, or physical diagnosis. |
| `Sensor_Mode` | A controlled identifier for the sensor configuration and identity basis used by an evidence-forming analysis, including participating sensors, channels/axes, and whether identity is canonical physical sensor or legacy block position. |
| `Candidate_BIM_Link` | A proposed asset/component association supported by mapping evidence but not yet authorized as a persistent cross-system binding. |
| `Verified_BIM_Binding` | A version-specific asset/component binding whose GUID existence, model version, ambiguity, evidence, and reviewer authorization have passed the binding rules. It verifies identity linkage only, not a defect. |
| `Inspection_Trigger_Eligibility` | A governance flag indicating that evidence may be placed into human inspection review. It does not create an Inspection_Finding or order an inspection. |
| `Evidence_Status` | The controlled lifecycle state of one evidence-record version: `DRAFT`, `FOR_REVIEW`, `VERIFIED_EVIDENCE`, `REJECTED`, `SUPERSEDED`, or `WITHDRAWN`. |
| `Evidence_Record_Version` | A monotonically increasing version ordinal within one supersession lineage. Each version has its own immutable `Condition_Evidence_ID`; corrections create a new ID/version and an explicit supersession relation. |

### 5.1 Minimum controlled vocabularies

These v1.0 vocabularies are thesis-defined interface controls, not diagnostic categories.

| Vocabulary | Allowed value | Meaning |
|---|---|---|
| `Sensor_Role` | `PRIMARY` | Optional designated primary sensor; must match `Primary_Sensor_ID` |
| `Sensor_Role` | `CONTRIBUTING` | Sensor/channel directly included by the aggregation rule; every CE requires at least one |
| `Sensor_Role` | `SUPPORTING` | Sensor used for context/quality review but not directly aggregated into Evidence_Result |
| `Evidence_Type` | `LAB_STATE_EVIDENCE` | Evidence supporting distinction among controlled laboratory state labels under the declared protocol |
| `Evidence_Type` | `LAB_STATE_CHANGE_EVIDENCE` | Evidence supporting a change relative to a declared laboratory reference under the declared protocol |

`Quality_Flag` vocabulary `CE-QUALITY-FLAG-v1.0`:

| Allowed value | Basis / meaning |
|---|---|
| `NO_FLAG` | No substantive flag applies; mutually exclusive with every other flag |
| `DEAD_CONSTANT` | Source-derived channel-quality condition |
| `LOW_DYNAMIC_QUANTIZED` | Source-derived channel-quality condition |
| `VALID_DYNAMIC` | Source-derived channel-quality condition |
| `CLIPPING_WARNING` | Source-derived channel-quality warning |
| `SPIKE_WARNING` | Source-derived channel-quality warning |
| `MID_RECORDING_GAP` | Source-derived recording-quality warning |
| `EXPECTED_TRAILING_NAN` | Source-derived handled trailing-gap condition |
| `PROVENANCE_WARNING` | Source-derived provenance warning |
| `INCOMPLETE_SENSOR_SET` | Required sensor/channel completeness criterion not met |
| `BELOW_VALID_WINDOW_RATIO` | Approved valid-window criterion not met |
| `SENSOR_DISAGREEMENT` | Contributing sensors disagree under the approved formation rule |
| `WINDOW_DISAGREEMENT` | Contributing windows disagree or tie under the approved formation rule |
| `LOW_CONFIDENCE` | Approved evidence-confidence criterion not met |
| `REPRODUCIBILITY_FAILED` | Approved reproduction check failed or could not reproduce the result |

Vocabulary extensions require a versioned governance decision and cannot silently change the meaning of existing values.

Semantic separation is mandatory:

```text
Raw vibration data
!= preprocessing output
!= window prediction
!= recording/run-level Condition_Evidence
!= Inspection_Finding
!= Action_Record
!= authorized decision
```

## 6. Upstream Gate 1 deliverables

| Deliverable | Required content | Producer | Consumer | Mandatory? | Validation |
|---|---|---|---|---|---|
| Dataset Manifest | Dataset/version ID, membership, generated-at, artifact hashes, source-root policy | G1 data steward | G1 evidence formation; G2 audit | Yes | Fixed version; every source/run resolves; manifest hash verified |
| Run Registry | Run_ID, campaign/session, independent-unit relation, state, excitation, recording membership, sensor set, inclusion/exclusion | G1 experiment owner | Evidence formation | Yes | Unique Run_ID; locked count; no orphan recordings/files; approved independent-unit decision |
| Sensor Provenance | Sensor_ID, identity basis, hardware, range/sensitivity, position, mounting, channels/axes, units, sampling, synchronization | G1 instrumentation owner | Evidence formation; BIM binding review | Yes | Every contributing sensor resolves; legacy block identity never relabeled as physical identity without mapping evidence |
| Source File Hash Registry | Source_Data_ID, File_ID/path reference, Run_ID, Recording_ID, Sensor_ID, SHA256 | G1 data steward | Evidence audit | Yes | Hash syntax and recomputation; file-to-run/sensor references valid |
| Preprocessing Specification | Preprocessing_Spec_ID, operations/order, train-only fitted transforms, parameters, exclusions | G1 analysis owner | Evidence formation/reproduction | Yes | Split before windowing; training-only fit; exact spec version available |
| Model Configuration Registry | Model_Config_ID, name/version, sensor mode, inputs, hyperparameters, seed, tuning, checkpoint/hash | G1 analysis owner | Evidence formation/reproduction | Yes for model-based evidence | Configuration immutable and resolvable; candidate models excluded unless provenance complete |
| Evaluation Protocol | Evaluation_Protocol_ID, independent unit, folds, metrics, aggregation, uncertainty, null/sensitivity protocol | G1 method owner | Evidence formation; G2 review | Yes | Pre-specified and locked before final execution; fold membership resolvable |
| Per-window Predictions | Window_Prediction_ID, recording/run/fold, sensor mode, model, true/predicted state, outputs, quality/inclusion | G1 pipeline | Aggregation audit only | Yes for window-based models | Unique IDs; no leakage; every included window resolves to source and model context |
| Per-recording Predictions | Recording_ID, aggregation rule, contributing windows, result, quality and uncertainty | G1 pipeline | Run-level aggregation | Yes when recordings are aggregation inputs | Recomputable from included windows; exclusions explicit |
| Per-run Results | Run_ID, held-out fold/group, recording results, metrics, variability and limitations | G1 pipeline | Canonical evidence formation | Yes | Recomputable; all expected recordings represented; difficult runs retained or formally excluded |
| CEI Metadata Structure | Versioned CEI schema plus one populated CEI structure for every Condition_Evidence record | G1 evidence/method owner | G2 traceability and review | Yes | All mandatory CEI dimensions present; structured metadata; not a scalar/severity/Health Index |
| Condition Evidence Register | Canonical records defined in Section 7 and associations in Section 8 | G1 evidence steward and reviewer | G2 traceability intake | Yes | Sections 10-15 and signed G1 governance pass |
| Exclusion Log | Excluded source/run/recording/window/sensor, reason, actor, time, scope and impact | G1 data/method owner | Evidence formation; audit | Yes | No silent exclusion; windows are not selectively removed to alter outcomes |
| Reproducibility Manifest | Dataset/version hashes, code commit, environment, configs, seeds, rerun command/conditions, output hashes, reproducibility result | G1 reproducibility owner | G2 audit | Yes | Fixed artifacts; reproduction result recorded; failures not hidden |
| Windowing and Evidence Formation Registry | Windowing_Spec_ID, Aggregation_Rule_ID, granularity, inclusion, disagreement, abstention and threshold references | G1 method owner | Evidence formation | Yes | Approved before official CE creation; no post hoc threshold |
| Fold Registry | Split_or_Fold_ID and complete train/validation/test membership | G1 method owner | Evidence audit | Yes | Every evaluated result resolves to fold membership |
| Evidence Quality Registry | Quality flags, quantitative quality basis, uncertainty/variability references and reproducibility state | G1 quality owner | CEI and evidence review | Yes | Every CEI quality assertion resolves to source evidence |
| Asset/BIM Model Registry | Asset_ID, BIM_GUID, model version, model authority and GUID index | G2 BIM information manager | BIM binding | Conditional for BIM-linked handoff | Candidate and verified binding checks can be reproduced |
| Identity/Role Registry | Agent_ID, role, authority scope and separation policy | G1/G2 governance owner | Creation, review and binding workflows | Yes for reviewed handoff | Creator, reviewer and verifier authorization resolves |

No listed deliverable is currently accepted merely because an intended schema, README, report, or aggregate CSV exists.

Authority-name equivalence used by the data dictionary:

| Data-dictionary authority | Canonical deliverable / authority |
|---|---|
| `Session/Run Registry`, `Run/Recording Registry` | Run Registry |
| `Sensor/Channel Registry` | Sensor Provenance |
| `Windowing Specification`, `Evidence Formation Registry` | Windowing and Evidence Formation Registry |
| `Quality Registry`, quality/uncertainty package | Evidence Quality Registry and CEI Metadata Structure |
| `Fold Registry` | Fold Registry |
| `Asset/Component Registry`, `BIM Model Registry` | Asset/BIM Model Registry |
| `Identity/role registry` | Identity/Role Registry |
| `Review workflow`, `Governance evaluation` | Condition Evidence Register governed by Identity/Role Registry and this specification |

## 7. Canonical Condition_Evidence record

A `Condition_Evidence_ID` represents:

> one evidence claim with complete provenance, formed from one `Run_ID` or a pre-defined recording-level aggregation, in one defined component context.

The default canonical Gate 2 unit is `run_level_evidence`. A raw window prediction cannot be official Condition_Evidence. A different canonical unit requires an explicit, approved Gate 1 decision and evidence.

### 7.1 Identity

| Field | Definition | Type | Cardinality | Required/Optional | Source | Validation rule | Downstream use |
|---|---|---|---|---|---|---|---|
| `Condition_Evidence_ID` | Stable opaque identifier for one immutable evidence-record version representing one bounded evidence claim | Opaque identifier | 1 | Required | Condition Evidence Register | Globally unique within project; not reused; no embedded diagnosis | Primary traceability key |
| `Evidence_Record_Version` | Version ordinal within the supersession lineage | Positive version identifier | 1 | Required | Condition Evidence Register | Unique and monotonically increasing within lineage | Audit and supersession |
| `Evidence_Status` | Lifecycle status defined in Section 12 | Controlled value | 1 | Required | Evidence review workflow | Legal transition only | Eligibility and audit |
| `Supersedes_Condition_Evidence_ID` | Earlier immutable CE record replaced by this new ID/version | CE reference | 0..1 | Conditional | Evidence review workflow | Must exist; cannot self-reference; same bounded claim/component scope | Revision lineage |

### 7.2 Source provenance

| Field | Definition | Type | Cardinality | Required/Optional | Source | Validation rule | Downstream use |
|---|---|---|---|---|---|---|---|
| `Source_Data_ID` | Registered primary source object; multiple sources use Source Link association | Source identifier | 1 primary; 1..* via link | Required | Dataset Manifest / source registry | Exists, belongs to declared run/recording, and matches exactly one Source Link row | Source reconstruction |
| `Source_File_SHA256` | SHA256 of each linked source file; never a comma list | SHA256 value in source link | 1 per linked file | Required | Source File Hash Registry | Valid SHA256 and recomputation match | Integrity audit |
| `Campaign_ID` | Controlled laboratory campaign identifier | Identifier | 1 | Required | Run Registry | Exists and is consistent with session/run | Experimental context |
| `Acquisition_Session_ID` | Identifier for acquisition session containing the run | Identifier | 1 | Required for accepted handoff | Session/Run Registry | Exists; time/context consistent | Session traceability |
| `Run_ID` | Canonical evidence-forming run or locked independent group | Identifier | 1 | Required | Run Registry | Exists, included, and compatible with aggregation rule | Canonical evidence unit |
| `Recording_ID` | Primary recording when exactly one; multiple recordings use Recording Link | Identifier | 0..1 header; 1..* via link | Conditional | Run/Recording Registry | Exists; belongs to Run_ID; if present, matches exactly one Recording Link row | Recording drill-down |
| `Observation_Start_Time` | Start of evidence observation interval | Datetime with timezone/context | 1 | Required | Acquisition/Recording Registry | Not after end; within source interval | Temporal query |
| `Observation_End_Time` | End of evidence observation interval | Datetime with timezone/context | 1 | Required | Acquisition/Recording Registry | Not before start; covers included evidence | Temporal query |

### 7.3 Sensor provenance

| Field | Definition | Type | Cardinality | Required/Optional | Source | Validation rule | Downstream use |
|---|---|---|---|---|---|---|---|
| `Sensor_Mode_ID` | Controlled configuration and sensor-identity basis | Identifier | 1 | Required | Sensor/Model Config Registry | Exists; declares physical versus legacy block identity | Configuration comparison |
| `Primary_Sensor_ID` | Primary contributing sensor if governance designates one | Sensor reference | 0..1 | Optional | Sensor Link association | If present, must also appear in Sensor Link | Primary sensor display |
| `Condition_Evidence_Sensor_Link` | Association to every contributing sensor | Association reference | 1..* | Required | Section 8 | At least one valid link; composite unique | Multi-sensor provenance |
| `Channel_Schema_ID` | Versioned channel list/units/order used by evidence formation | Identifier | 1 | Required | Sensor/Channel Registry | Exists and matches model/preprocessing input | Input reconstruction |
| `Axis_Context` | Axis or axis set for this evidence; multiple per-sensor values live in links | Controlled reference | 1 summary; 1 per link | Required | Sensor/Channel Registry | Allowed by channel schema | Physical context |
| `Sampling_Rate_Hz` | Sampling rate represented without inventing a default | Positive numeric with unit | 1 per channel schema | Required | Sensor/Channel Registry | Matches source/channel metadata | Reproduction/windowing |

### 7.4 Processing provenance

| Field | Definition | Type | Cardinality | Required/Optional | Source | Validation rule | Downstream use |
|---|---|---|---|---|---|---|---|
| `Preprocessing_Spec_ID` | Versioned ordered preprocessing definition | Identifier | 1 | Required | Preprocessing Specification | Exists; train-only fitting audit passes | Reproduction |
| `Windowing_Spec_ID` | Versioned window-generation definition | Identifier | 1 for window-based evidence | Conditional | Windowing Specification | Exists; applied after split; no unapproved parameter substitution | Window audit |
| `Aggregation_Rule_ID` | Pre-specified rule forming recording/run evidence | Identifier | 1 | Required | Evidence Formation Registry | Approved before canonical record creation | Recompute evidence |
| `Model_Name` | Registered model or analytical method name | Controlled text/reference | 1 | Required for model-based evidence | Model Config Registry | Matches Model_Config_ID | Method context |
| `Model_Version` | Immutable model/method version or artifact hash reference | Version reference | 1 | Required for model-based evidence | Model Config Registry | Resolves to fixed artifact | Reproduction |
| `Model_Config_ID` | Locked configuration identifier | Identifier | 1 | Required for model-based evidence | Model Config Registry | Exists and matches sensor/channel inputs | Configuration trace |
| `Evaluation_Protocol_ID` | Locked run/fold evaluation protocol | Identifier | 1 | Required | Evaluation Protocol | Exists and independent unit is approved | Validity boundary |
| `Split_or_Fold_ID` | Primary fold/split when exactly one; multiple folds use `Condition_Evidence_Fold_Link` | Identifier | 0..1 header; 1..* via link | Required for evaluated model result | Fold Registry | Resolves to membership; if present, matches exactly one Fold Link row | Leakage audit |
| `Code_Commit` | Fixed repository commit/tag for evidence generation | Commit/tag reference | 1 | Required for accepted handoff | Reproducibility Manifest | Resolves; working state declared; no hidden changes | Reproduction |
| `Environment_ID` | Fixed software/hardware environment declaration | Identifier | 1 | Required | Environment/Reproducibility Manifest | Resolves to lockfile/container or approved manifest | Reproduction |

### 7.5 Evidence content

| Field | Definition | Type | Cardinality | Required/Optional | Source | Validation rule | Downstream use |
|---|---|---|---|---|---|---|---|
| `Evidence_Type` | Controlled non-diagnostic evidence category | Controlled value | 1 | Required | Evidence Formation Registry | Value approved; diagnostic/action categories prohibited | Filtering |
| `Evidence_Granularity` | `WINDOW`, `RECORDING`, `RUN`, or `CAMPAIGN` | Controlled value | 1 | Required | Evidence Formation Registry | Official handoff defaults to `RUN`; Section 9 applies | Governance |
| `Evidence_Result` | Structured evidence output and reference to supporting results | Structured value/reference | 1 | Required | Aggregation output | Recomputable; no hidden scalar collapse | Evidence display/audit |
| `Predicted_or_Observed_State` | Controlled laboratory state label/result under protocol | Controlled label/reference | 1 | Required | Run Registry / aggregation output | Must use upstream state registry; not mapped to physical damage | Laboratory interpretation |
| `CEI` | First-class confidence/evidence metadata structure for this CE record | Structured record/reference | 1 | Required | CEI Metadata Structure + Evidence Quality Registry | Contains validity, model confidence, run/fold variability, sensor configuration, data quality, provenance, timestamp/version; never a universal scalar/severity | G2 justification and review |
| `Quality_or_Confidence` | Human-readable/queriable projection of the corresponding CEI confidence, variability, and quality dimensions; not an independent source of truth | Structured CEI sub-record/reference | 1 | Required | CEI + Evidence Quality Registry | Must equal the referenced CEI substructure; method/scale declared; not severity/probability of damage | Human review context |
| `Quality_Flag` | One or more controlled quality flags through normalized values | Controlled association/value | 1..* | Required; use explicit `NO_FLAG` when none applies | Quality Registry | Every flag traceable to source/rule | Filtering/review |
| `Limitation_Context` | Known acquisition, sensor, processing, evaluation, or generalization limitations | Structured text/reference | 1..* | Required | Evidence reviewer and source reports | Non-empty for accepted handoff | Interpretation boundary |
| `Evidence_Interpretation_Boundary` | Explicit statement of what the evidence does and does not establish | Controlled statement/reference | 1 | Required | This contract / review | Must include non-diagnostic and non-action boundary | Prevent misuse |

### 7.6 BIM/component context

| Field | Definition | Type | Cardinality | Required/Optional | Source | Validation rule | Downstream use |
|---|---|---|---|---|---|---|---|
| `Candidate_Asset_ID` | Proposed asset/component context independent of BIM serialization | Asset identifier | 1 | Required for G2 eligibility | Asset/Component Registry | Exists; scope is one component context | Component trace |
| `Candidate_BIM_GUID` | Proposed IFC GlobalId for component | BIM GUID reference | 0..1 | Optional while `UNBOUND`; required from `CANDIDATE` | BIM model/index | Exists in declared model version before verification | Candidate mapping |
| `Model_Version_ID` | Authoritative BIM model version for GUID interpretation | Identifier | 0..1 | Required when BIM GUID exists | BIM Model Registry | Exists; version is accessible and not superseded without mapping | Revision safety |
| `BIM_Link_Status` | `UNBOUND`, `CANDIDATE`, `VERIFIED`, `REJECTED`, or `SUPERSEDED` | Controlled value | 1 | Required | BIM binding workflow | Legal transition; consistent with binding record | Binding governance |
| `BIM_Binding_ID` | Active binding record reference | Identifier | 0..1 active | Conditional | `BIM_Binding` association | Required from `CANDIDATE`; resolves and matches CE ID | Binding audit |
| `Binding_Evidence_Reference` | Mapping evidence used to propose/verify binding | Evidence/document reference | 0 while `UNBOUND`; 1..* from `CANDIDATE` | Conditional | BIM binding workflow | Resolvable; reviewer can inspect | Verification basis |

### 7.7 Accountability

| Field | Definition | Type | Cardinality | Required/Optional | Source | Validation rule | Downstream use |
|---|---|---|---|---|---|---|---|
| `Created_By` | Accountable creator/formation agent | Agent reference | 1 | Required | Identity/role registry | Authorized role; not null | Attribution |
| `Created_At` | Record creation time | Datetime | 1 | Required | Evidence Register | Append-only; not before source observation end unless machine-created with declared rule | Audit |
| `Reviewed_By` | Human reviewer for evidence semantics and eligibility | Agent reference | 0..1 | Required for `VERIFIED_EVIDENCE` | Review workflow | Authorized; separation policy applied | Accountability |
| `Reviewed_At` | Review completion time | Datetime | 0..1 | Required when reviewed | Review workflow | Not before creation; immutable | Audit |
| `Review_Status` | Review outcome distinct from evidence content | Controlled value | 1 | Required | Review workflow | Consistent with Evidence_Status | Governance |
| `Review_Rationale` | Reason and limitations supporting review outcome | Structured text/reference | 0..1 | Required for any completed review | Review workflow | Non-empty; traceable to evidence/protocol | Decision audit |

### 7.8 Downstream governance

| Field | Definition | Type | Cardinality | Required/Optional | Source | Validation rule | Downstream use |
|---|---|---|---|---|---|---|---|
| `Eligible_For_G2_Traceability` | Evidence may enter G2 traceability intake | Boolean | 1 | Required | Governance evaluation | True only when Section 15 conditions pass and BIM status is explicit | G2 intake |
| `Eligible_For_Inspection_Review` | Evidence may be queued for human inspection review | Boolean | 1 | Required | Governance evaluation | True only for `VERIFIED_EVIDENCE` with verified BIM binding and approved governance; never creates an order | Review queue eligibility |
| `Downstream_Use_Limitation` | Explicit restrictions applied to all downstream uses | Structured controlled statement | 1..* | Required | This contract / reviewer | Must include prohibited interpretations in Section 16 | Compliance |

### 7.9 Prohibited fields and meanings

The following must not be fields or inferred values inside `Condition_Evidence`:

- confirmed defect/damage diagnosis;
- physical damage severity;
- stiffness loss/degradation;
- maintenance priority or Action_Level;
- weighted Health Index;
- RUL;
- repair/maintenance recommendation;
- authorized inspection order;
- authorized maintenance action; or
- field classifier result transferred from laboratory evidence.

## 8. Association entities

### Condition_Evidence_Sensor_Link

```text
Condition_Evidence_ID
Sensor_ID
Sensor_Role
Channel_or_Axis
Contribution_Context
Link_Status
```

- **Mandatory:** yes; every Condition_Evidence has `1..*` sensor links.
- **Cardinality:** one CE to one or more sensors; one sensor may contribute to many CE records.
- **Uniqueness:** `(Condition_Evidence_ID, Sensor_ID, Channel_or_Axis, Sensor_Role)`.
- **Orphan rule:** both CE and Sensor_ID must exist; Sensor_ID identity basis must be declared.
- **Duplicate rule:** duplicate composite links fail; sensors must never be stored as comma-separated IDs.
- **Status:** `INCLUDED`, `EXCLUDED`, `DISPUTED`, or `SUPERSEDED`. Status is immutable within one CE version; correction creates a new CE version. Exclusion/dispute requires context and prevents silent contribution.

### Condition_Evidence_Window_Link

```text
Condition_Evidence_ID
Window_Prediction_ID
Contribution_Weight_or_Role
Inclusion_Status
Exclusion_Reason
```

- **Mandatory:** conditional; mandatory with `1..*` links for any evidence formed from window predictions.
- **Cardinality:** one CE to many windows; one Window_Prediction may appear in at most one active canonical CE for the same aggregation scope and cannot be silently reused across incompatible claims.
- **Uniqueness:** `(Condition_Evidence_ID, Window_Prediction_ID)`.
- **Orphan rule:** CE and Window_Prediction must exist; each window resolves to recording, run, sensor mode, fold, preprocessing, and model configuration.
- **Duplicate rule:** duplicate links fail; inclusion/exclusion cannot conflict.

### BIM_Binding

```text
BIM_Binding_ID
Condition_Evidence_ID
Asset_ID
BIM_GUID
Model_Version_ID
Binding_Status
Binding_Method
Binding_Evidence_Reference
Verified_By
Verified_At
```

- **Mandatory:** optional while CE is `UNBOUND`; required from `CANDIDATE` onward.
- **Cardinality:** one CE may have `0..*` historical binding records; one binding belongs to exactly one CE; a canonical component-scoped CE has at most one active `VERIFIED` binding.
- **Uniqueness:** active `(Condition_Evidence_ID, Asset_ID, BIM_GUID, Model_Version_ID)` must be unique.
- **Orphan rule:** CE, asset, BIM GUID/model version, and verifier references must resolve where applicable.
- **Duplicate rule:** competing active verified bindings fail until ambiguity is resolved.
- **Name equivalence:** `BIM_Binding.Asset_ID` equals the canonical value exposed as `Candidate_Asset_ID`; `BIM_Binding.BIM_GUID` equals the candidate GUID exposed as `Candidate_BIM_GUID`. Header fields are projections of the active binding, not independent identities.

### Additional normalized provenance associations

Multiple source files or recordings must not be placed in comma-separated fields.

```text
Condition_Evidence_Source_Link
Condition_Evidence_ID
Source_Data_ID
Source_File_SHA256
Source_Role
```

```text
Condition_Evidence_Recording_Link
Condition_Evidence_ID
Recording_ID
Recording_Role
Inclusion_Status
Exclusion_Reason
```

- Source Link is mandatory with `1..*` rows. One source may support many CE records. Composite key: `(Condition_Evidence_ID, Source_Data_ID, Source_Role)`. Duplicate source/hash rows fail. Header `Source_Data_ID` must match exactly one linked primary source.
- Recording Link is mandatory with `1..*` rows when evidence aggregates recordings. One recording may support many candidate/derived CE records under declared scopes. Composite key: `(Condition_Evidence_ID, Recording_ID, Recording_Role)`. Duplicate or conflicting inclusion rows fail. Header `Recording_ID`, when present, must match exactly one primary link.
- All references must resolve; exclusions require reasons; inclusion status is immutable within a CE version and correction creates a new version.

### Condition_Evidence_Fold_Link

```text
Condition_Evidence_ID
Split_or_Fold_ID
Fold_Role
Result_Reference
```

- **Mandatory:** yes with `1..*` rows for evaluated model evidence.
- **Cardinality:** one CE may aggregate results from one or more declared folds; one fold may support many CE records.
- **Uniqueness:** `(Condition_Evidence_ID, Split_or_Fold_ID, Fold_Role)`.
- **Orphan rule:** CE, fold membership, protocol, and result reference must resolve.
- **Duplicate rule:** duplicate or conflicting fold roles fail; the header `Split_or_Fold_ID`, when present, matches exactly one primary link.

### Multi-component policy

Required default policy: create component-scoped Condition_Evidence records, each with one candidate/verified component context. This prevents one ambiguous evidence claim from silently applying to multiple BIM objects.

If a genuinely inseparable result spans multiple components, use explicit `BIM_Binding` rows with declared cardinality, per-link status, evidence, and ambiguity. Such a record is not eligible for inspection review until the governance-approved one-to-many policy is satisfied. A list of BIM GUIDs in one field is prohibited.

## 9. Evidence granularity model

| Level | Record type | Official Condition_Evidence? | Purpose | Allowed downstream use | Prohibited interpretation |
|---|---|---|---|---|---|
| Window | `Window_Prediction` | No | Audit model outputs and aggregation membership | Supporting analytics, disagreement/quality analysis | Independent observation, official evidence claim, defect, severity, priority |
| Recording | `recording_evidence` | Candidate by default | Aggregate windows within one recording | Candidate formation input; review of recording consistency | Canonical G2 evidence unless Gate 1 explicitly approves this unit |
| Run | `run_level_evidence` | Yes, canonical default after all rules and review pass | Represent one evidence claim for a locked run/defined recording aggregation and component context | G2 traceability; eligible human inspection review only under Section 15 | Diagnosis, authorized inspection/action, physical severity |
| Campaign | `aggregated_campaign_evidence` | No; supporting synthesis | Cross-run/campaign synthesis and robustness context | Supporting context, comparison, limitations | Replacement for run-level records; concealment of difficult runs; direct field transfer |

The current repository has aggregate run/fold result tables but no accepted window/recording prediction package or Condition Evidence Register. Therefore no official Condition_Evidence instance is declared by this specification.

## 10. Evidence formation rules

1. **Pre-specified formation:** `Aggregation_Rule_ID` must exist, be versioned, and be approved before canonical evidence creation. The rule must identify input granularity, aggregation logic, eligible states, uncertainty method, and tie/disagreement handling.
2. **Minimum sensor completeness:** the rule must reference an approved minimum sensor/channel completeness criterion. No numeric minimum is introduced here. Each CE must have at least one contributing sensor link.
3. **Minimum valid-window ratio:** the threshold must be locked in the aggregation rule or Gate 1 governance decision. The current repository does not provide an approved threshold. **Evidence is currently insufficient.**
4. **Exclusion handling:** every excluded source, recording, sensor, channel, or window must be recorded with reason and impact. Selective exclusion to improve results is prohibited.
5. **Sensor disagreement:** per-sensor results and disagreement must remain visible. The formation rule must define consensus, dominance, abstention, or review behavior without collapsing sensor IDs.
6. **Window disagreement:** contributing window results, inclusion status, and aggregation outcome must be retained. A tied/unstable result must be flagged or abstained according to the approved rule.
7. **Low-confidence cases:** quality/confidence below an approved criterion must carry a quality flag and limitation. It cannot become inspection-eligible solely through a model output.
8. **Unavailable model version:** model-based evidence without resolvable model version/config/checkpoint cannot reach `VERIFIED_EVIDENCE` or downstream eligibility.
9. **Missing source hash:** evidence without complete source hash links cannot be official or handed off.
10. **Failed reproducibility check:** failure must be recorded in Evidence_Quality and the reproducibility manifest; `Eligible_For_G2_Traceability` and `Eligible_For_Inspection_Review` must be false until resolved and reviewed.

Window outputs are supporting analytical records. Recording evidence is candidate. Run-level evidence is canonical unless Gate 1 approves another unit with documented evidence. Campaign aggregation is supporting synthesis and cannot replace run-level evidence.

## 11. BIM binding rules

### 11.1 Binding states

| State | Meaning | Allowed transition conditions |
|---|---|---|
| `UNBOUND` | No BIM candidate has been asserted | May move to `CANDIDATE` only with Asset_ID, BIM_GUID, model version, method, and mapping evidence |
| `CANDIDATE` | Proposed mapping awaiting verification | May move to `VERIFIED`, `REJECTED`, or `SUPERSEDED` after existence, version, ambiguity, and review checks |
| `VERIFIED` | Identity binding verified for one model version | May move only to `SUPERSEDED` when corrected, remapped, or replaced; verification does not confirm a defect |
| `REJECTED` | Proposed binding failed review | Terminal for that binding record; a new proposal uses a new Binding_ID |
| `SUPERSEDED` | Binding replaced by an explicit later binding | Terminal and inactive; lineage retained |

### 11.2 Required checks

1. `BIM_GUID` must exist in `Model_Version_ID`.
2. Model version must be authoritative and accessible for review.
3. GUID format and uniqueness must be checked within the declared model version.
4. Duplicate or reused GUIDs block verification.
5. Sensor-to-component ambiguity must be explicit in binding evidence and status.
6. Candidate links cannot be treated as verified in queries, UI, handoff, or inspection eligibility.
7. A canonical component-scoped CE must have at most one active verified binding.
8. One evidence result spanning multiple components must use explicit association rows; component-scoped split records are preferred.
9. Component replacement/remapping creates a new binding, sets the prior binding to `SUPERSEDED`, and preserves forward/reverse lineage.
10. `Verified_By` and `Verified_At` are mandatory for `VERIFIED`.

`Eligible_For_G2_Traceability=true` requires an explicit `CANDIDATE` or `VERIFIED` binding status and complete mapping evidence. `Eligible_For_Inspection_Review=true` requires `VERIFIED` binding unless an approved governance rule explicitly defines a human binding-review queue; it never creates an inspection order.

## 12. Evidence lifecycle and versioning

### 12.1 Evidence statuses

| Status | Meaning | Allowed next status |
|---|---|---|
| `DRAFT` | Record being formed; mutable only before submission to review | `FOR_REVIEW`, `WITHDRAWN` |
| `FOR_REVIEW` | Frozen version awaiting authorized review | `VERIFIED_EVIDENCE`, `REJECTED`, `WITHDRAWN` |
| `VERIFIED_EVIDENCE` | Evidence formation, provenance, quality, and review passed for the stated laboratory claim | `SUPERSEDED`, `WITHDRAWN` |
| `REJECTED` | This version failed review | Terminal; correction creates a new `DRAFT` version |
| `SUPERSEDED` | This version was replaced by an explicit newer record/version | Terminal and inactive |
| `WITHDRAWN` | Record was administratively withdrawn with reason | Terminal and inactive |

`VERIFIED_EVIDENCE` means that the evidence record and its bounded laboratory claim passed governance. It does not mean verified defect, confirmed damage, physical severity, or maintenance need.

### 12.2 Lifecycle rules

- Once a version enters `FOR_REVIEW`, its content is immutable.
- Review outcomes append events; they do not overwrite prior evidence or rationale.
- Corrections create a new `Condition_Evidence_ID`, increment `Evidence_Record_Version` within the lineage, and reference the replaced CE ID.
- Supersession and withdrawal require actor, timestamp, reason, and authorization.
- Superseded, rejected, or withdrawn versions remain queryable but cannot be active or downstream-eligible.
- Evidence-status history is append-only and chronologically ordered.
- Reviewer identity, role, rationale, and completion time are mandatory for completed review.
- Evidence creator and reviewer authorization/separation must follow the approved role policy; that policy remains an open decision.

### 12.3 Evidence_Status_Event and review outcome

Every Evidence_Status change, including initial creation as `DRAFT`, is represented by an append-only event:

```text
Evidence_Status_Event_ID
Condition_Evidence_ID
Previous_Evidence_Status
New_Evidence_Status
Changed_By
Changed_At
Change_Reason
Authorization_Reference
```

- One CE has `1..*` status events. The initial event has no previous status and `New_Evidence_Status=DRAFT`; one event belongs to exactly one CE.
- `Evidence_Status_Event_ID` is unique; `(Condition_Evidence_ID, Changed_At, New_Evidence_Status)` cannot be duplicated.
- `Evidence_Status_Event_ID` is a thesis-defined identifier owned by the Condition Evidence Register.
- `Condition_Evidence_ID` must resolve. `Changed_By` and any `Authorization_Reference` must resolve to the Identity/Role Registry or approved authorization record; the transition must be legal and chronological.
- Events are immutable. Correction requires a compensating event or a new CE version, never event deletion.

`Review_Status` uses `NOT_REVIEWED`, `APPROVED`, or `REJECTED`:

- `DRAFT` implies `NOT_REVIEWED`.
- `FOR_REVIEW` remains `NOT_REVIEWED` until a completed review event.
- `VERIFIED_EVIDENCE` requires `APPROVED`.
- `REJECTED` requires `REJECTED`.
- `SUPERSEDED` and `WITHDRAWN` preserve the prior review outcome and add a lifecycle reason/event.

Association inclusion/link statuses are immutable attributes of one CE version rather than independent workflows. Any correction to an `INCLUDED`, `EXCLUDED`, `DISPUTED`, or `SUPERSEDED` contribution requires a new CE version and recomputation.

## 13. Integrity rules

Each rule is technology-neutral and must be implementable as an automated or reviewable test.

### 13.1 Identity and value integrity

| Rule ID | Testable rule |
|---|---|
| `CE-INT-001` | `Condition_Evidence_ID` is unique and never reused. |
| `CE-INT-002` | Association composite keys are unique; duplicate active links are prohibited. |
| `CE-INT-003` | Multi-valued IDs are represented by association rows; comma-separated ID values fail. |
| `CE-INT-004` | Every required source link contains SHA256 with valid form and matching recomputed content; missing hash fails. |
| `CE-INT-005` | Observation start is not after end; creation/review/status times are chronologically consistent. |

### 13.2 Referential and provenance integrity

| Rule ID | Testable rule |
|---|---|
| `CE-REF-001` | `Source_Data_ID` and every Source Link resolve to the Dataset/Source Registry. |
| `CE-REF-002` | `Run_ID`, Campaign_ID, Session_ID, and Recording Links resolve and are mutually consistent. |
| `CE-REF-003` | Every Sensor Link resolves to a sensor/channel registry and declares sensor identity basis. |
| `CE-REF-004` | Every CE has at least one contributing sensor link. |
| `CE-REF-005` | Every Window Link resolves to one registered prediction and its recording/run/fold/model provenance. |
| `CE-REF-006` | Preprocessing, windowing, aggregation, evaluation, fold, and exclusion references resolve. |
| `CE-REF-007` | Model name/version/config/checkpoint references are complete for model-based evidence. |
| `CE-REF-008` | Code commit and Environment_ID resolve to the Reproducibility Manifest. |
| `CE-REF-009` | Primary source, recording, sensor, fold, asset, and BIM header projections match exactly one corresponding association row where present. |
| `CE-REF-010` | Every registry/specification/role authority referenced by a CE exists, is versioned, and identifies an owner. |
| `CE-REF-011` | A declared canonical physical Sensor_ID or identity basis is supported by a resolvable mapping record; legacy block position cannot be relabelled without mapping evidence. |

### 13.3 Version and lifecycle integrity

| Rule ID | Testable rule |
|---|---|
| `CE-VER-001` | Reviewed versions are immutable; content changes require a new version. |
| `CE-VER-002` | Evidence versions are unique and monotonically increasing within the logical claim. |
| `CE-VER-003` | Supersession references an existing prior claim/version and cannot self-reference or form a cycle. |
| `CE-VER-004` | `REJECTED`, `SUPERSEDED`, and `WITHDRAWN` records cannot be active or downstream-eligible. |
| `CE-VER-005` | Evidence status follows the allowed transition table and has append-only event history. |
| `CE-VER-006` | A superseded CE has at most one direct successor in a non-branching lineage; duplicate successors and supersession cycles fail. |

### 13.4 BIM binding integrity

| Rule ID | Testable rule |
|---|---|
| `CE-BIM-001` | BIM link status is one controlled value and follows legal transitions. |
| `CE-BIM-002` | `CANDIDATE` is never queried, displayed, or handed off as `VERIFIED`. |
| `CE-BIM-003` | A `VERIFIED` binding has valid GUID, model version, binding evidence, authorized verifier, and verification time. |
| `CE-BIM-004` | GUID existence and uniqueness are checked within `Model_Version_ID`. |
| `CE-BIM-005` | A canonical component-scoped CE has no more than one active verified binding. |
| `CE-BIM-006` | Component remapping/replacement supersedes the old binding and preserves lineage. |
| `CE-BIM-007` | One-to-many component binding is explicit, non-ambiguous under approved policy, and never encoded as one GUID list. |

### 13.5 Formation and governance integrity

| Rule ID | Testable rule |
|---|---|
| `CE-GOV-001` | Official CE has an approved, pre-specified `Aggregation_Rule_ID`; raw window prediction alone fails. |
| `CE-GOV-002` | Included/excluded window and recording counts recompute the declared aggregation and valid-window ratio. |
| `CE-GOV-003` | A valid-window ratio below the approved threshold carries required flag/abstention and cannot be silently accepted. |
| `CE-GOV-004` | Every exclusion has reason, scope, actor/rule, and impact; conflicting inclusion states fail. |
| `CE-GOV-005` | Sensor/window disagreement is retained and handled exactly as the approved aggregation rule specifies. |
| `CE-GOV-006` | Completed review has authorized reviewer, time, status, and non-empty rationale. |
| `CE-GOV-007` | Eligibility flags are consistent with Evidence_Status, BIM status, provenance, quality, review, and reproducibility. |
| `CE-GOV-008` | Evidence interpretation boundary prohibits diagnosis, physical severity, priority, recommendation, or authorization semantics. |
| `CE-GOV-009` | Reproducibility result is recorded; a failed/unavailable reproduction blocks accepted handoff until reviewed and resolved. |
| `CE-GOV-010` | Every CE has a complete CEI structure containing validity, model confidence, run/fold variability, sensor configuration, data quality, provenance, and timestamp/version; `Quality_or_Confidence` must match its CEI substructure; scalar/severity-only CEI fails. |
| `CE-GOV-011` | `VERIFIED_EVIDENCE` and downstream eligibility default to `RUN` granularity; `WINDOW` and `CAMPAIGN` cannot be official, and `RECORDING` requires an approved alternative-unit decision. |
| `CE-GOV-012` | G2 schema approval/implementation/demo cannot proceed until SCQ/VCQ/RCQ and acceptance criteria are preregistered and versioned. |
| `CE-GOV-013` | `NO_FLAG` is mutually exclusive with substantive Quality_Flag values; substantive flags require referenced quality evidence. |

## 14. Negative test manifest

These fixtures are definitions only; this document does not claim execution.

| Test ID | Invalid condition | Expected failure | Rule ID | Severity |
|---|---|---|---|---|
| `CE-NEG-001` | Duplicate `Condition_Evidence_ID` | Reject duplicate record | `CE-INT-001` | BLOCKER |
| `CE-NEG-002` | Missing `Run_ID` | Reject official CE and handoff | `CE-REF-002` | BLOCKER |
| `CE-NEG-003` | Missing `Source_File_SHA256` | Reject source link/official CE | `CE-INT-004` | BLOCKER |
| `CE-NEG-004` | Orphan `Sensor_ID` | Reject sensor link | `CE-REF-003` | BLOCKER |
| `CE-NEG-005` | No contributing sensor | Reject CE formation | `CE-REF-004` | BLOCKER |
| `CE-NEG-006` | Comma-separated multi-sensor field | Reject non-normalized value | `CE-INT-003` | ERROR |
| `CE-NEG-007` | Orphan `Window_Prediction_ID` | Reject aggregation membership | `CE-REF-005` | BLOCKER |
| `CE-NEG-008` | Missing or invalid `Aggregation_Rule_ID` | Reject official CE | `CE-GOV-001`, `CE-REF-006` | BLOCKER |
| `CE-NEG-009` | Valid-window ratio below approved threshold without flag/abstention | Reject eligibility and flag aggregation | `CE-GOV-002`, `CE-GOV-003` | BLOCKER |
| `CE-NEG-010` | Candidate BIM GUID treated as verified | Reject query/handoff result | `CE-BIM-002` | BLOCKER |
| `CE-NEG-011` | Verified BIM binding without reviewer/time/evidence | Reject verification | `CE-BIM-003` | BLOCKER |
| `CE-NEG-012` | Duplicate active BIM binding | Reject duplicate/ambiguity | `CE-INT-002`, `CE-BIM-005` | BLOCKER |
| `CE-NEG-013` | One CE ambiguously linked to multiple components | Reject inspection eligibility pending split/policy resolution | `CE-BIM-005`, `CE-BIM-007` | BLOCKER |
| `CE-NEG-014` | Superseded record marked active | Reject status/eligibility | `CE-VER-004` | BLOCKER |
| `CE-NEG-015` | Completed review missing rationale | Reject review completion | `CE-GOV-006` | ERROR |
| `CE-NEG-016` | `Eligible_For_Inspection_Review=true` while evidence is `REJECTED` | Reject eligibility | `CE-VER-004`, `CE-GOV-007` | BLOCKER |
| `CE-NEG-017` | Missing model version/config for model-based result | Reject evidence verification | `CE-REF-007` | BLOCKER |
| `CE-NEG-018` | Missing code commit | Reject accepted handoff | `CE-REF-008` | BLOCKER |
| `CE-NEG-019` | Failed reproducibility check not recorded or eligibility remains true | Reject handoff and require review | `CE-GOV-009`, `CE-GOV-007` | BLOCKER |
| `CE-NEG-020` | Evidence result interpreted as damage severity | Reject semantic mapping/use | `CE-GOV-008` | BLOCKER |
| `CE-NEG-021` | Source hash has valid form but does not match content | Reject source integrity | `CE-INT-004` | BLOCKER |
| `CE-NEG-022` | Reviewed record edited in place | Reject mutation; require new version | `CE-VER-001` | BLOCKER |
| `CE-NEG-023` | Supersession self-reference or cycle | Reject supersession | `CE-VER-003` | BLOCKER |
| `CE-NEG-024` | Illegal Evidence_Status transition | Reject event and preserve prior state | `CE-VER-005` | ERROR |
| `CE-NEG-025` | Legacy block-position sensor labeled as canonical physical sensor without mapping evidence | Reject sensor identity assertion | `CE-REF-011` | BLOCKER |
| `CE-NEG-026` | Missing CEI structure or missing required CEI dimension | Reject verification/handoff | `CE-GOV-010` | BLOCKER |
| `CE-NEG-027` | CEI represented only as scalar, severity, or Health Index | Reject CEI semantics | `CE-GOV-010`, `CE-GOV-008` | BLOCKER |
| `CE-NEG-028` | Nonexistent BIM GUID in declared model version | Reject candidate verification | `CE-BIM-003`, `CE-BIM-004` | BLOCKER |
| `CE-NEG-029` | Duplicate Source, Recording, Window, Sensor, or Fold association row | Reject duplicate association | `CE-INT-002` | ERROR |
| `CE-NEG-030` | `WINDOW` or `CAMPAIGN` record marked `VERIFIED_EVIDENCE` or eligible | Reject status/eligibility | `CE-GOV-011`, `CE-GOV-007` | BLOCKER |
| `CE-NEG-031` | `RECORDING` record made official without approved alternative-unit decision | Reject status/eligibility | `CE-GOV-011` | BLOCKER |
| `CE-NEG-032` | Diagnosis, physical severity, maintenance priority/recommendation, or authorization field inserted into CE | Reject prohibited field/semantic mapping | `CE-GOV-008` | BLOCKER |
| `CE-NEG-033` | Header source/recording/fold/BIM projection disagrees with association row | Reject referential inconsistency | `CE-REF-009` | BLOCKER |
| `CE-NEG-034` | Verified binding points to superseded model/component without successor mapping | Reject stale binding and downstream eligibility | `CE-BIM-006`, `CE-GOV-007` | BLOCKER |
| `CE-NEG-035` | Evidence status changes without an `Evidence_Status_Event` | Reject transition | `CE-VER-005` | BLOCKER |
| `CE-NEG-036` | G2 schema approval/demo proceeds without preregistered CQs and acceptance criteria | Reject readiness/approval | `CE-GOV-012` | BLOCKER |
| `CE-NEG-037` | `NO_FLAG` coexists with a substantive quality flag | Reject contradictory quality state | `CE-GOV-013` | ERROR |

Every negative test maps to at least one integrity rule. Execution evidence, expected-versus-actual reports, and regression history belong to Gate 3 testing, not this manifest definition.

## 15. Downstream handoff contract

Gate 2 may receive an evidence package only under the following conditions.

| Handoff condition | Required state | Failure action |
|---|---|---|
| G1 governance | Signed G1 acceptance matrix or explicit approved provisional-handoff decision | Keep record candidate; set both eligibility flags false; do not claim accepted handoff |
| Dataset/source provenance | Dataset version, source links, SHA256, campaign/session/run/recording relations complete | Quarantine record and return to G1 data steward |
| Sensor provenance | At least one valid Sensor Link; identity basis/channel/axis/sampling declared | Reject evidence formation or binding review |
| Evidence formation | Approved Aggregation_Rule_ID; inputs and exclusions recomputable | Reject official CE; retain supporting analytical records only |
| Processing/model provenance | Specs, fold, model/config/version, code commit, environment resolve | Keep `DRAFT` or reject review; eligibility false |
| CEI completeness | Structured CEI contains all mandatory dimensions and preserves method/version | Reject evidence verification/handoff; do not substitute a scalar |
| Evidence quality | Structured quality/confidence, flags, uncertainty, limitations, disagreement recorded | Require review/abstention; no automatic escalation |
| Evidence lifecycle | `VERIFIED_EVIDENCE`; immutable reviewed version; rationale and reviewer complete | Reject accepted handoff |
| BIM context | Explicit `CANDIDATE` or `VERIFIED` link with model version and evidence | `UNBOUND` remains outside traceability intake; candidate is never treated as verified |
| Inspection-review eligibility | Verified evidence, verified BIM binding, approved governance, reproducibility pass | Set `Eligible_For_Inspection_Review=false`; human resolution required |
| Reproducibility | Result/status recorded and passed under approved protocol | Quarantine or reject; document limitation and corrective action |
| Downstream boundary | Prohibited interpretations attached and acknowledged | Reject downstream consumer contract |
| CQ governance | SCQ/VCQ/RCQ and acceptance criteria preregistered before G2 schema approval, implementation, or demo | Keep G2 readiness false; return to governance review |

Receiving Gate 2 does not convert Condition_Evidence into an Inspection_Finding or Action_Record. It only establishes that an evidence record is fit for traceability and, when explicitly eligible, for human inspection review.

## 16. Prohibited downstream interpretations

`Condition_Evidence` must not be interpreted as:

- confirmed damage;
- defect diagnosis;
- stiffness loss;
- maintenance priority;
- Health Index;
- RUL;
- repair recommendation;
- authorized inspection order; or
- authorized maintenance action.

Additional prohibitions:

- model confidence/softmax output is not physical damage probability;
- evidence quality/confidence is not damage severity;
- candidate BIM association is not verified identity;
- verified BIM binding is not verified defect;
- a window prediction is not an independent official evidence claim;
- campaign aggregation cannot conceal run-level disagreement;
- no quantitative laboratory result may be transferred directly to a field structure;
- no evidence record may bypass human review or an approved governance rule to create inspection/action records.

## 17. Gate 2 readiness criteria

This is a readiness checklist, not a completion declaration.

| Required | Pass evidence | Fail condition | Owner |
|---|---|---|---|
| Current governance alignment | Current charter/version cited; `Action_Record_ID` chain and Limited-FEM boundary applied | Archived chain or diagnostic FEM semantics used | Research governance owner |
| Source availability register | All used and missing sources listed; limitations explicit | Missing source treated as evidence | Evidence steward |
| Accepted G1 basis | Signed acceptance or approved provisional-handoff decision | G1 remains open with no explicit exception | G1 owner / supervisors |
| Locked IDs and registries | Dataset, run, recording, sensor, source, fold, model/config, environment references resolve | Any required ID is orphan/unlocked | G1 data/method owners |
| Canonical CE schema | Section 7 fields and Section 8 associations approved | Ambiguous field, comma-list ID, or diagnostic/action field remains | G1-G2 schema owners |
| CEI structure | First-class CEI schema and complete CEI instance for each CE | Missing dimension, scalar-only CEI, severity/Health Index interpretation | G1 evidence/method owner |
| Evidence formation | Aggregation unit/rule and thresholds approved before formation | Raw windows used as official CE; rule/threshold chosen post hoc | G1 method owner |
| Provenance and reproducibility | Source hashes, processing/model/code/environment, outputs and reproduction status complete | Missing hash/version/commit or unrecorded failure | Reproducibility owner |
| BIM binding governance | Candidate/verified states, model version, ambiguity and remapping rules approved | Candidate treated verified; stale/duplicate binding unresolved | BIM information manager |
| Lifecycle/accountability | Status transitions, immutability, reviewer authority and rationale approved | In-place edits, missing reviewer/rationale, illegal transition | Evidence review authority |
| Integrity rule catalogue | Every Section 13 rule has owner, implementation plan, and expected report | Rule cannot be tested or has no owner | G2 validation owner |
| Negative fixtures | Section 14 fixtures prepared and trace to rules | Missing mapping or hidden expected result | G2/G3 test owner |
| Competency questions | SCQ/VCQ/RCQ and acceptance criteria preregistered and versioned before schema approval/demo | CQ absent, post hoc, or not traceable to field/rule/query | RQ2/G2 owner |
| Downstream boundaries | Section 16 acknowledged in G2 design/review | Evidence mapped to diagnosis, priority, recommendation, or authorization | G2 owner / reviewers |
| Inspection-Action readiness | G1 payload can populate evidence link, BIM context, time, source, quality, limitations and accountability inputs | Required downstream provenance cannot be supplied | G1-G2 integration owner |

No criterion in this table is marked as passed by this document.

## 18. Acceptance criteria for this specification

This specification is sufficient for v1.0 review only when:

1. no field definition remains ambiguous;
2. no field conflicts with Limited-FEM or evidence/action separation;
3. every ID has an authoritative source or is explicitly marked thesis-defined/open;
4. every relationship has cardinality, uniqueness, orphan, and duplicate behavior;
5. every status has a transition rule and lifecycle meaning;
6. every negative test traces to an integrity rule;
7. prohibited interpretations are explicit and testable; and
8. the defined Gate 1 output is sufficient for Gate 2 to build the Inspection-Action Model without inventing upstream provenance.

Acceptance of this document does not accept any current Condition_Evidence instance and does not close a gate.

## 19. Open decisions

1. Final independent evidence unit: `Run_ID`, `Recording_ID`, or approved replicate-group relation.
2. Exact aggregation/evidence-formation rule and tie/disagreement behavior.
3. Minimum sensor/channel completeness and minimum valid-window ratio.
4. Confidence/quality method, scale, calibration, and abstention policy.
5. Authoritative windowing specification; current repository plans are inconsistent.
6. Permutation/exchangeability unit and its relationship to the independent unit.
7. Canonical physical Sensor_ID reconciliation for legacy `S1/S2/S3` results.
8. One-to-many BIM binding policy and when component-scoped splitting is mandatory.
9. Authoritative BIM model version, GUID persistence, replacement/remapping policy, and binding review authority.
10. Evidence creator/reviewer authorization and separation-of-duties policy.
11. Whether `Action_Status` is stored or derived from downstream immutable Status_Event history.
12. External persistence versus IFC embedding; the contract remains storage-neutral.
13. Portable dataset/code/environment packaging and canonical artifact/output hashes.

Until resolved by an approved decision record, no numeric threshold, aggregation formula, model version, hash, result, sensor mapping, or gate status may be invented.

## 20. Recommended next actions

1. Normalize and lock Gate 1 Dataset, Run, Recording, Source Hash, Sensor/Channel, Fold, Model Config, Environment, and Exclusion registries under one canonical naming scheme.
2. Create the Condition Evidence Register schema and empty positive template using Sections 7-8; do not populate accepted evidence before G1 governance allows it.
3. Lock the canonical evidence unit, Aggregation_Rule_ID, valid-window/sensor-completeness criteria, disagreement, abstention, and quality/confidence method.
4. Reconcile physical Sensor_ID with legacy block-position results and define Sensor-to-Asset/BIM binding governance, model version, ambiguity, and reviewer authority.
5. Create positive fixtures for single-sensor, multi-sensor, multi-recording, candidate BIM, verified BIM, superseded evidence, and reproducibility-pass cases.
6. Create the Section 14 negative fixtures and expected-failure manifest without executing or claiming test success.
7. Preregister G2 SCQ/VCQ/RCQ and acceptance criteria, then conduct the joint G1-G2 schema approval review and prepare Gate 3 integrity/workflow tests.
