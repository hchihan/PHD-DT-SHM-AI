# Condition Evidence Information (CEI) Profile for the Limited-FEM PhD Thesis

## Gate-1 Core Specification, Thesis-Wide Role, and Scope Firewall

**Document version:** 1.1  
**Date:** 12 August 2026  
**Language:** English  
**Status:** Revised thesis construct specification for supervisor review; not a claim that Gate 1 is closed  
**Field:** Construction Management / Built-Asset Management  
**Supersedes for current use:** `CEI_SCIENTIFIC_BASIS_AND_THESIS_SPECIFICATION_v1.0_20260812(2).md`  
**Preservation rule:** Version 1.0 remains a historical record and must not be overwritten.

---

## Executive decision

This version retains the acronym **CEI** but revises its formal meaning to:

> **Condition Evidence Information (CEI) profile:** a versioned, traceable record that states what a defined vibration dataset supports, how that support was evaluated, what limitations apply, and whether the evidence is qualified for handover to the next thesis layer.

The word **Indicator** is discontinued as the preferred formal expansion because it may imply a single numerical index. CEI is neither a weighted score nor a physical damage indicator. It is an **information profile attached to a `Condition_Evidence_ID`**.

The Gate-1 role of CEI is deliberately narrow:

```text
vibration data
→ leakage-controlled, run-aware result
→ CEI-Lab core record
→ qualified condition evidence for bounded handover
```

CEI does not create a new research question, work package, chapter, paper, Evidence Gate, validation programme, or software product. It packages evidence produced by the locked thesis architecture.

At Gate 1, CEI must not require work beyond the obligations already approved in the Charter. The mandatory Gate-1 obligations remain:

1. locked and internally consistent data/run registry;
2. leakage-safe run-aware/LORO evaluation;
3. train-only fitting of learned preprocessing and model-selection operations;
4. verified sensor configuration and sensor mode for every reported model;
5. reproducible result provenance and explicit scope of validity.

Confidence calibration, expert content validation, synthetic negative fixtures, a field CEI schema, BIM competency questions, and action thresholds may be useful later, but they are **not new mandatory conditions for closing Gate 1 unless formally approved through thesis governance**.

**Current claim boundary:** Evidence is currently insufficient to state that final Gate-1 CEI records are qualified unless a later verified Gate-specific evidence pack demonstrates that all locked Gate-1 obligations have been satisfied.

---

## 1. Research routing and scope classification

### 1.1 Gate-1 primary route

| Element | Position |
|---|---|
| Research question | RQ1 — reliability of vibration-derived evidence for controlled connection states |
| Work package | WP1 — Laboratory vibration evidence |
| Thesis chapter | Chapter 4 — Laboratory evidence |
| Paper | Paper 1 |
| Evidence Gate | Gate 1 — dataset integrity and run-aware evaluation |
| Core Scope | CEI-Lab core record and qualification status |
| Supporting Scope | Benchmark models, sensor-configuration comparison, uncertainty reporting |
| Future Work | Field-specific baseline evidence, if justified and approved |
| Out of Scope | Damage severity, field diagnosis, lab-to-field classifier transfer, weighted Health Index, predictive maintenance, autonomous decisions |

### 1.2 Thesis-wide downstream route

| Thesis layer | CEI role | Ownership boundary |
|---|---|---|
| Laboratory evidence — RQ1/WP1/Paper 1/Gate 1 | Produce a qualified and bounded evidence record | Paper 1 owns evidence qualification, not traceability schema |
| Information traceability — RQ2/WP2/Paper 2/Gates 2–3 | Receive `Condition_Evidence_ID` and minimum handover metadata | Paper 2 owns BIM binding, competency questions, constraints, and bidirectional queries |
| Field feasibility — RQ3/WP3/Paper 3/Gate 4 | Create field baseline-deviation evidence under a separately approved method | Paper 3 owns field deployment and baseline feasibility, not lab-class transfer |
| Decision support — WP4/Gate 5 | Use evidence as one input to human-reviewed action logic | WP4 owns `Action_Status`; CEI does not determine maintenance action |

### 1.3 Locked thesis chain

```text
Vibration data
→ condition/state-change evidence
→ BIM-linked component
→ inspection record
→ inspection-maintenance action support
```

```text
Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status
```

CEI is an information profile within the `Condition_Evidence` object. It is not an additional identifier in the chain.

The FEM remains **nominal, uncalibrated, reference-only, and not used for damage diagnosis**. `FEM_Node_ID`, if retained, is optional metadata and is not part of CEI qualification.

---

## 2. Construct definition and terminology control

### 2.1 Formal definition

> **Condition Evidence Information (CEI) profile** is a versioned information record associated with a `Condition_Evidence_ID`. It identifies the evidence unit, states the bounded claim supported by the data, records the run-aware validation context, sensing configuration, data-quality outcome, uncertainty or confounding limitations, provenance, and qualification status needed for inspection-oriented information handover.

### 2.2 What CEI answers

> What does this evidence support, under which validated conditions, with what limitations, and may it be handed to the next information layer?

### 2.3 What CEI does not answer

> What physical damage exists, how severe it is, which component caused the signal, or which maintenance action must be executed?

### 2.4 Object distinctions

| Object | Meaning |
|---|---|
| `Condition_Evidence_ID` | Persistent identity of one evidence record |
| `CEI_Profile` | Information describing its qualification basis and limitations |
| `CEI_Qualification_Status` | Whether it may be handed forward within a stated boundary |
| `BIM_GUID` | Identity of a BIM component used in the traceability layer |
| `Inspection_Record_ID` | Identity of an inspection workflow record |
| `Action_Status` | Status of the separate downstream action workflow |

### 2.5 Preferred and prohibited language

| Use | Avoid |
|---|---|
| condition evidence | confirmed damage, unless inspection confirms it |
| CEI information profile | CEI damage index |
| qualified within the tested scope | universally valid |
| model score | confidence, unless calibration has been assessed |
| controlled laboratory state | field damage state |
| sensor configuration effect | optimal sensor placement |
| field baseline deviation | transfer of laboratory class to field |
| inspection-oriented handover | autonomous maintenance decision |

---

## 3. Scientific basis and claim boundary

CEI remains a thesis-defined construct. The targeted basis assembled in version 1.0 supports its components but does not establish CEI as an international standard or pre-existing universal index.

| Principle | Scientific basis | CEI use | Boundary |
|---|---|---|---|
| Measured change is not automatically damage | SHM literature on condition-sensitive features and environmental/operational variability [1]–[5] | Separate observed support from physical diagnosis | No source validates thesis-specific CEI thresholds |
| Sensor and acquisition context affect results | Condition-monitoring and sensing studies [1], [6] | Record sensor mode, channels, axes, and acquisition settings | Does not prove universal sufficiency of three sensors |
| Data quality must accompany monitoring evidence | SHM data-quality literature [7], [8] | Record pass/fail/limitation outcomes for defined checks | No composite data-quality score is adopted |
| Dependence-aware validation is required | Grouped validation and leakage literature [9], [10] | Keep related windows within the same held-out physical group | Sources do not replace the thesis run registry |
| Model probability is not necessarily confidence | Calibration and dataset-shift literature [11], [12] | Label unassessed outputs as model scores | Calibration is optional unless confidence is claimed |
| Evidence needs reproducible provenance | W3C PROV and FAIR principles [13], [14] | Record source, processing, model, configuration, and time | Provenance alone does not establish structural validity |
| Dynamic evidence must connect to asset information | Construction Digital Twin and information-processing literature [15]–[17] | Motivate bounded handover to Paper 2 | Paper 1 does not own the traceability schema |

The defensible thesis claim is therefore:

> CEI is a thesis-defined information profile for qualifying and handing over condition evidence; it is grounded in established validation, data-quality, uncertainty, and provenance principles but must be empirically instantiated using the thesis data and locked protocol.

---

## 4. CEI-Lab core profile for Gate 1

### 4.1 Unit of evidence

The primary independent unit must be the physical grouping justified by the final run registry. Overlapping windows are analytical samples, not independent experimental replicates.

The final Gate-1 evidence pack must state explicitly:

- how `Campaign_ID`, `Session_ID`, `Run_ID`, `Recording_ID`, and `Window_ID` relate;
- what physical action separates one run from another;
- which group is held out in each fold;
- whether repeated recordings share one physical setup;
- which dataset version is canonical.

If independence cannot be demonstrated, the CEI must disclose the weaker unit and reduce the claim accordingly.

### 4.2 Mandatory Gate-1 fields

| Group | Mandatory field | Purpose |
|---|---|---|
| Identity | `Condition_Evidence_ID` | Persistent identity of the evidence record |
| Version | `CEI_Profile_Version` | Version of the CEI rules used |
| Context | `Evidence_Context = LAB_CONTROLLED_STATE` | Prevents confusion with field evidence |
| Claim | `Evidence_Statement` | Narrow statement supported by the result |
| Evidence unit | `Campaign_ID`, `Run_ID`, `Recording_ID` or justified equivalents | Makes independence auditable |
| Dataset | `Dataset_Manifest_ID` and source hash/reference | Identifies the canonical inputs |
| Sensor context | `Sensor_Mode_ID`, `Sensor_IDs`, axes/channels, sampling settings | Defines the sensing boundary |
| Split control | `Split_Policy`, `Held_Out_Group`, `Group_Overlap_Check` | Demonstrates run-aware separation |
| Preprocessing | `Preprocessing_Config_ID`, `Fit_Scope` | Demonstrates train-only fitting |
| Model context | `Model_Family`, `Model_Config_ID`, retained seed/fold identifiers | Identifies the benchmark instrument |
| Result | run-level prediction/metric references and class-specific result references | Links the evidence statement to source results |
| Quality | `Data_Quality_Status` and issue references | Exposes signal or metadata defects |
| Confounding | `Confounding_Status` and test references where performed | Prevents invalid evidence handover |
| Scope | `Applicability_Boundary` | Prevents lab-to-field or cross-campaign overclaim |
| Provenance | code/version/config/result references, generation time | Supports regeneration and audit |
| Status | `CEI_Qualification_Status` | Controls downstream handover |
| Rationale | `Qualification_Rationale` | Explains limitations and decision basis |

### 4.3 Optional Gate-1 fields

| Field | When used | Rule |
|---|---|---|
| `Model_Score` | A model produces class scores/probabilities | Do not call it confidence if calibration is not assessed |
| `Calibration_Status` and calibration metrics | The manuscript makes a confidence claim | Optional otherwise; `NOT_ASSESSED` is valid |
| `Permutation_Test_Reference` | A permutation test is part of the confirmatory protocol | Supporting control, not automatically a Gate requirement |
| `Metadata_Only_Control_Reference` | Confounding is tested using metadata | Include when available and relevant |
| `Cross_Campaign_Test_Reference` | Scope beyond a single campaign is examined | Report as scope/confounding evidence, not automatic failure |
| `Sensor_Ablation_Reference` | Sensor configurations are compared | Supports bounded configuration findings, not optimality |
| `FEM_Reference` | A qualitative anomaly hypothesis is discussed | Optional; must carry the Limited-FEM qualifier |

### 4.4 Explicitly excluded from Gate-1 CEI core

The following do not belong in the mandatory Paper-1 profile:

- `BIM_GUID` binding rules;
- `Sensor_Host_GUID`, `Observation_Zone_ID`, or component-selection logic;
- `Inspection_Record_ID` creation rules;
- competency questions and round-trip queries;
- field baseline definition and persistence thresholds;
- `Normal → Watch → Inspect → Priority Inspection` logic;
- expert/facility-manager validation;
- weighted CEI or Health Index;
- damage severity, stiffness loss, bolt preload, or causal diagnosis.

These elements belong to later thesis layers or remain out of scope.

---

## 5. Gate-1 qualification logic

### 5.1 Status model

| Status | Meaning | Permitted use |
|---|---|---|
| `PROVISIONAL` | Record generated while one or more Gate-1 obligations remain unresolved | Development, audit, and internal review only |
| `QUALIFIED` | All locked Gate-1 obligations pass for the stated evidence and scope | Handover to Paper 2 as qualified condition evidence |
| `QUALIFIED_WITH_LIMITATIONS` | Core provenance and independence are valid, but a non-fatal limitation narrows interpretation | Handover only with the limitation preserved |
| `NOT_QUALIFIED` | Critical provenance, leakage, independence, sensor-mode, or reproducibility requirement fails | Diagnostic/control analysis only; must not support the main condition claim |

The status describes **evidential usability**, not structural condition severity.

### 5.2 Mandatory qualification conditions

A CEI-Lab record may be `QUALIFIED` only when:

1. the canonical dataset and run registry are locked and internally consistent;
2. the evidence unit and held-out grouping reflect justified physical independence;
3. no train–test group overlap exists;
4. every learned preprocessing, feature selection, tuning, and model-selection step is fitted without access to the held-out group;
5. the reported result is traceable to prediction, split, model, configuration, and source-data artifacts;
6. the sensor configuration and sensor mode are verified for the reported model;
7. critical data-quality and label/provenance conflicts are resolved;
8. the result is reproducible under the declared configuration;
9. the evidence statement and applicability boundary match what was actually tested.

These conditions operationalize the existing Gate-1 obligations; they do not add a separate CEI validation Gate.

### 5.3 Status effects of common conditions

| Condition | Status effect |
|---|---|
| Random window split mixes windows from the same physical run across train/test | `NOT_QUALIFIED` for main evidence; may remain a diagnostic comparison |
| Test-group information influences preprocessing or model selection | `NOT_QUALIFIED` |
| Source recording or label cannot be resolved | `NOT_QUALIFIED` |
| Reported model sensor mode cannot be confirmed | Model-specific evidence remains `PROVISIONAL` or model is excluded |
| Critical sensor/channel corruption affects the evidence unit | `NOT_QUALIFIED`, unless a pre-specified valid handling rule applies |
| Model score is uncalibrated but no confidence claim is made | No automatic status penalty; report as model score |
| Cross-campaign performance declines | Preserve as scope/confounding evidence; status depends on the stated claim boundary |
| Multi-seed variation is material | `QUALIFIED_WITH_LIMITATIONS` or narrowed claim, based on pre-declared reporting logic |
| A benchmark model fails while the protocol and data remain valid | Does not invalidate other evidence; report the failure transparently |

### 5.4 Gate-1 closure relationship

CEI is an output packaging mechanism, not an additional closure condition. Gate 1 closes according to the approved Charter and Gate documents:

```text
locked metadata/run registry
+ leakage-safe run-aware/LORO evaluation
+ verified sensor mode for every retained reported model
+ reproducible evidence
= Gate-1 closure basis
```

If ResNet1D is removed through an approved manuscript decision, its sensor-mode verification is no longer required for a result that is not reported. This must be recorded explicitly rather than silently omitted.

---

## 6. Minimum handover from Paper 1 to Paper 2

Paper 1 must hand over only the information needed to identify and interpret evidence. Paper 2 then owns component-level linkage and traceability validation.

### 6.1 Gate-1 handover package

| Handover item | Required content |
|---|---|
| Evidence identity | `Condition_Evidence_ID` |
| Qualification | `CEI_Qualification_Status` and rationale |
| Evidence statement | Controlled state or state-support statement |
| Source provenance | Campaign/run/recording references and dataset manifest |
| Sensor provenance | `Sensor_ID`, `Sensor_Mode_ID`, relevant acquisition context |
| Evaluation provenance | Split policy, held-out group, preprocessing fit scope, model/config/result references |
| Scope | Applicability boundary and known limitations |

### 6.2 Paper-2 enrichment boundary

Paper 2 may add:

- `BIM_GUID` and binding status;
- model/version context;
- `Inspection_Record_ID` and `Action_Status` linkage;
- competency-question results;
- identity integrity, completeness, orphan, ambiguity, and round-trip tests.

Paper 2 must not change a CEI qualification result to make traceability appear successful. It may report the evidence as qualified, limited, provisional, or not qualified and then test whether that status is preserved end to end.

---

## 7. Thesis-wide variants without scope leakage

### 7.1 CEI-Lab

**Purpose:** qualify evidence distinguishing controlled connection states on the 1:10 frame under the tested run-aware protocol.

**Permitted claim:**

> The vibration evidence supports discrimination of a controlled experimental state within the stated campaign, excitation, sensor configuration, and validation boundary.

**Prohibited claim:**

> The evidence measures field damage severity or proves an equivalent state in a full-scale building.

### 7.2 CEI-Traceability view

This is not a new evidence calculation. It is Paper 2's view of the Gate-1 record plus traceability relationships and constraint-test results.

```text
CEI-Lab record
→ Condition_Evidence_ID
→ BIM binding
→ Inspection_Record_ID
→ Action_Status history
```

The scientific contribution in Paper 2 remains the formal traceability model and verifiable competency-question framework, not CEI itself.

### 7.3 CEI-Field concept

Field evidence must be defined separately because the laboratory classifier and laboratory class scores are not transferred to Rapexco.

The defensible field statement is limited to:

> A field observation is within, outside, or indeterminate relative to a versioned operational baseline under the documented operating and data-quality context.

The detailed baseline schema, persistence rule, installation mapping, environmental/operating envelope, and inspection linkage belong to WP3/Paper 3/Gate 4. They are not frozen by this v1.1 document.

Until a field method is approved and verified:

> **Evidence is currently insufficient** to define final CEI-Field thresholds or claim field damage detection.

### 7.4 Decision-support use

CEI may be one transparent input to the four-level action logic. CEI never directly determines `Action_Status`. Human review, inspection findings, operating context, and the rules validated in WP4 remain separate.

---

## 8. Minimal machine-readable Gate-1 example

The example is conceptual and intentionally provisional:

```yaml
condition_evidence_id: CE-LAB-C3-S0-L1-R07-001
cei_profile_version: "1.1"
evidence_context: LAB_CONTROLLED_STATE
evidence_statement:
  statement_type: CONTROLLED_STATE_SUPPORT
  supported_state: S0
  applicability_boundary: "Scaled-frame laboratory protocol only"
evidence_unit:
  campaign_id: C3
  run_id: R07
  recording_id: REC-001
dataset:
  manifest_id: TBD
  source_hash_reference: TBD
sensor_context:
  sensor_mode_id: TBD
  sensor_ids: [S1, S2]
  axes_channels: TBD
  sampling_hz: 100
evaluation:
  split_policy: LORO
  held_out_group: R07
  group_overlap_check: PASS
  preprocessing_fit_scope: TRAIN_ONLY
  model_config_id: TBD
result_reference:
  prediction_file: TBD
  fold_metric_file: TBD
quality_and_limits:
  data_quality_status: TBD
  confounding_status: TBD
  model_score_calibration: NOT_ASSESSED
provenance:
  code_version: TBD
  configuration_hash: TBD
  generated_at: TBD
cei_qualification_status: PROVISIONAL
qualification_rationale: "Example only; Gate-1 source artifacts not supplied here."
```

This example is not a database schema, a validated record, or a field-transfer template.

---

## 9. Required thesis and paper wording

### 9.1 Thesis methodology wording

> The thesis uses a Condition Evidence Information (CEI) profile to package condition evidence as a versioned and traceable information record. CEI records the evidence statement, independent evaluation unit, run-aware validation context, sensor and data-quality context, provenance, uncertainty limitations, applicability boundary, and qualification status. It is not a weighted score, a damage-severity index, or an autonomous decision rule.

### 9.2 Paper 1 wording

> A CEI-Lab record packages leakage-controlled, out-of-group results as bounded laboratory condition evidence. Qualification requires a locked run registry, justified physical grouping, train-only preprocessing and model selection, verified sensor configuration, reproducible provenance, and a claim limited to the tested controlled states. CEI does not transform model accuracy into a damage diagnosis.

### 9.3 Paper 2 wording

> Paper 2 receives the `Condition_Evidence_ID`, CEI qualification status, provenance, and applicability boundary from Paper 1. It then tests whether the evidence can be linked verifiably to BIM components and inspection records without changing its scientific meaning or qualification status.

### 9.4 Paper 3 wording

> Field evidence is evaluated relative to a versioned operational baseline under documented data-quality and operating conditions. It does not inherit laboratory class labels or classifier confidence. Any persistent unexplained deviation supports review or inspection, not a direct field damage diagnosis.

### 9.5 Decision-support wording

> CEI provides a traceable evidence input to a separate, human-reviewed inspection-action process. The resulting action status is governed by the decision-support layer and is not encoded as evidence strength or damage severity.

---

## 10. Validation responsibilities by Evidence Gate

| Gate | CEI-related responsibility | Not required at this Gate |
|---|---|---|
| Gate 1 | Demonstrate provenance, independence, leakage control, sensor mode, reproducibility, and bounded evidence qualification | BIM binding, field baseline, action logic, expert review of maintenance rules |
| Gate 2 | Define schema, identifiers, constraints, competency questions, and evaluation criteria before full implementation | Recalculate Paper-1 model evidence |
| Gate 3 | Demonstrate end-to-end laboratory traceability and preservation of CEI status/limitations | Field diagnosis |
| Gate 4 | Demonstrate field mapping, baseline feasibility, data return, and field scenarios | Transfer of laboratory classifier or class confidence |
| Gate 5 | Evaluate transparent action scenarios with human review | Autonomous maintenance or weighted Health Index |

---

## 11. Gate-1 action list

### 11.1 Blocking actions

| Priority | Action | Required evidence | CEI effect |
|---:|---|---|---|
| 1 | Lock the canonical dataset and run registry | immutable campaign–session–run–recording mapping with conflict resolution | Establishes valid evidence units |
| 2 | Demonstrate leakage-safe LORO/run-aware evaluation | split manifests, group-overlap checks, train-only preprocessing evidence | Establishes independence and validity |
| 3 | Verify sensor mode for each retained reported model | configuration, input-channel mapping, model artifact | Establishes sensing boundary |
| 4 | Lock reproducible result provenance | prediction files, metrics, configs, code/version references, source hashes | Supports regeneration and claim traceability |
| 5 | Issue the Gate-1 evidence qualification table | claim → evidence → limitation → CEI status | Enables bounded handover |

### 11.2 Non-blocking unless claimed in Paper 1

| Action | Status rule |
|---|---|
| Confidence calibration | Required only if calibrated confidence is claimed; otherwise report model score and `NOT_ASSESSED` |
| Expert content review of CEI fields | Useful for thesis governance but not a locked Gate-1 requirement |
| Synthetic sensor-fault fixtures | Optional robustness/supporting analysis |
| Full field CEI schema | Deferred to WP3/Gate 4 |
| BIM competency questions | Owned by WP2/Gate 2 |
| Action thresholds and facility-manager review | Owned by WP4/Gate 5 |

No additional experiment should be proposed solely to validate CEI unless the existing evidence audit demonstrates that a locked Gate-1 claim cannot otherwise be supported.

---

## 12. Final self-audit

### Claim → Evidence → Limitation → Next action

**Claim**  
CEI is suitable as a thesis-wide information interface when it is defined as a bounded information profile rather than a numerical indicator or physical-damage index.

**Evidence**  
The approved Charter locates CEI in Paper 1 as a confidence/evidence construct, locks the evidence-to-action chain, and prohibits severity, lab-to-field transfer, weighted Health Index, field diagnosis, and autonomous maintenance. Established literature supports dependence-aware validation, leakage control, data quality, cautious uncertainty interpretation, provenance, and information linkage [1]–[17].

**Limitation**  
CEI is not an established universal SHM standard. This specification does not supply the final run registry, canonical result artifacts, sensor-mode verification, or Gate-1 evaluation results. **Evidence is currently insufficient** to claim that a final CEI record is `QUALIFIED`.

**Next action**  
Complete the five blocking Gate-1 actions in Section 11.1, then populate the CEI-Lab core profile from verified artifacts. Do not expand the Gate-1 workload into field schema, competency-question validation, or action logic.

---

## 13. Version 1.1 change record

| Version-1.0 element | Version-1.1 decision | Reason |
|---|---|---|
| Formal name `Condition Evidence Indicator` | Revised to `Condition Evidence Information (CEI) profile` | Avoids implying a single numerical index while retaining the established acronym |
| Broad 800-line thesis construct and validation programme | Reorganized around Gate-1 core plus bounded downstream views | Focuses work on the next Evidence Gate |
| Mandatory expert content validation before Gate 1 | Reclassified as optional governance review | Not an approved Gate-1 obligation in the Charter |
| Mandatory confidence calibration | Conditional: required only when confidence is claimed | Prevents a new blocking obligation when model scores are reported conservatively |
| Mandatory negative fixtures | Reclassified as optional supporting robustness analysis | Useful but not locked in Gate 1 |
| Full CEI-Field data model | Deferred to WP3/Paper 3/Gate 4 | Prevents premature field-method claims and lab-to-field leakage |
| BIM fields inside CEI core | Removed from Gate-1 mandatory fields; retained as Paper-2 enrichment | Protects Paper-2 traceability contribution |
| Inspection and action fields inside CEI core | Removed from Gate-1 core | Preserves separation between evidence, traceability, and decision support |
| Statuses `ACCEPTED/LIMITED/REJECTED` | Revised to `QUALIFIED/QUALIFIED_WITH_LIMITATIONS/NOT_QUALIFIED` | Clarifies that the status concerns evidence handover, not administrative approval or structural condition |
| Requirement to generate an `ACCEPTED` CEI to close Gate 1 | Removed | CEI packages Gate-1 evidence; it does not create an additional Gate |
| Cross-campaign failure treated as potential rejection | Reframed as scope/confounding evidence governed by the stated claim | Avoids misinterpreting domain shift as simple model failure |
| Detailed traceability queries in CEI validation | Assigned to Gates 2–3 | Keeps Paper 1 from absorbing Paper 2's scientific contribution |
| Detailed Rapexco scenarios in CEI validation | Assigned to Gate 4 | Keeps laboratory evidence separate from field feasibility |

---

## References

### External scientific and standards sources retained from version 1.0

[1] International Organization for Standardization, **ISO 16587:2004 — Mechanical vibration and shock: Performance parameters for condition monitoring of structures**, 2004. <https://www.iso.org/standard/32318.html>.

[2] K. Worden, C. R. Farrar, G. Manson, and G. Park, “The fundamental axioms of structural health monitoring,” *Proceedings of the Royal Society A*, vol. 463, no. 2082, pp. 1639–1664, 2007. <https://doi.org/10.1098/rspa.2007.1834>.

[3] H. Sohn, “Effects of environmental and operational variability on structural health monitoring,” *Philosophical Transactions of the Royal Society A*, vol. 365, no. 1851, pp. 539–560, 2007. <https://doi.org/10.1098/rsta.2006.1935>.

[4] E. J. Cross, K. Worden, and Q. Chen, “Cointegration: a novel approach for the removal of environmental trends in structural health monitoring data,” *Proceedings of the Royal Society A*, vol. 467, no. 2133, pp. 2712–2732, 2011. <https://doi.org/10.1098/rspa.2011.0023>.

[5] E. Figueiredo, G. Park, C. R. Farrar, K. Worden, and J. Figueiras, “Machine learning algorithms for damage detection under operational and environmental variability,” *Structural Health Monitoring*, vol. 10, no. 6, pp. 559–572, 2011. <https://doi.org/10.1177/1475921710388971>.

[6] E. Favarelli, E. Testi, and A. Giorgetti, “The impact of sensing parameters on data management and anomaly detection in structural health monitoring,” *Journal of Civil Structural Health Monitoring*, vol. 12, pp. 1413–1425, 2022. <https://doi.org/10.1007/s13349-022-00566-4>.

[7] N. Makhoul, “Review of data quality indicators and metrics, and suggestions for indicators and metrics for structural health monitoring,” *Advances in Bridge Engineering*, vol. 3, article 17, 2022. <https://doi.org/10.1186/s43251-022-00068-9>.

[8] N. Makhoul, “Bayesian Decision-Making Process Including Structural Health Monitoring Data Quality for Bridge Management,” *KSCE Journal of Civil Engineering*, vol. 28, pp. 2818–2835, 2024. <https://doi.org/10.1007/s12205-024-0030-y>.

[9] D. R. Roberts et al., “Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure,” *Ecography*, vol. 40, no. 8, pp. 913–929, 2017. <https://doi.org/10.1111/ecog.02881>.

[10] S. Kapoor and A. Narayanan, “Leakage and the reproducibility crisis in machine-learning-based science,” *Patterns*, vol. 4, no. 9, article 100804, 2023. <https://doi.org/10.1016/j.patter.2023.100804>.

[11] C. Guo, G. Pleiss, Y. Sun, and K. Q. Weinberger, “On Calibration of Modern Neural Networks,” in *Proceedings of the 34th International Conference on Machine Learning*, PMLR 70, pp. 1321–1330, 2017. <https://proceedings.mlr.press/v70/guo17a.html>.

[12] Y. Ovadia et al., “Can You Trust Your Model’s Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift,” in *Advances in Neural Information Processing Systems 32*, 2019. <https://proceedings.neurips.cc/paper_files/paper/2019/hash/8558cb408c1d76621371888657d2eb1d-Abstract.html>.

[13] W3C, **PROV-O: The PROV Ontology**, W3C Recommendation, 2013. <https://www.w3.org/TR/prov-o/>.

[14] M. D. Wilkinson et al., “The FAIR Guiding Principles for scientific data management and stewardship,” *Scientific Data*, vol. 3, article 160018, 2016. <https://doi.org/10.1038/sdata.2016.18>.

[15] C. Boje, A. Guerriero, S. Kubicki, and Y. Rezgui, “Towards a semantic Construction Digital Twin: Directions for future research,” *Automation in Construction*, vol. 114, article 103179, 2020. <https://doi.org/10.1016/j.autcon.2020.103179>.

[16] International Organization for Standardization, **ISO 13374-2:2007 — Condition monitoring and diagnostics of machines: Data processing, communication and presentation — Part 2: Data processing**, 2007. <https://www.iso.org/standard/36645.html>.

[17] International Organization for Standardization, **ISO 13374-4:2015 — Condition monitoring and diagnostics of machine systems: Data processing, communication and presentation — Part 4: Presentation**, 2015. <https://www.iso.org/standard/54933.html>.

### Internal thesis governance sources

[P1] `MASTER_RESEARCH_CHARTER.md`, 17 July 2026.  
[P2] `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md`, source of truth.  
[P3] `RESEARCH_DIRECTION_AND_SCOPE.md`, 17 July 2026.  
[P4] `RESEARCH_ARCHITECTURE.md`, 17 July 2026.  
[P5] `CURRENT_STATUS_AND_NEXT_DIRECTION.md`, 17 July 2026.  
[P6] `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md`, accepted ADR.  
[P7] `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md`, Verdict B basis.

---

## Source-control note

This document governs the **definition and scope** of CEI v1.1. Dynamic research facts—including the canonical dataset, final run count, completed LORO results, retained models, sensor-mode verification, field-access status, and Gate completion—must be taken from the latest verified Gate-specific evidence pack. A later evidence pack may update those dynamic facts without changing the scope firewall defined here.
