# Run-Aware Evaluation of Low-Cost Sensor Configurations for Vibration-Based Condition Classification of a Scaled Bolted Steel Frame

**Manuscript version:** v2 — Verified-Evidence Controlled | **Date:** 2026-07-18 | **Target tier:** Q2 international journal (construction/monitoring scope)
**Note:** Đây là bản nguồn Markdown của `PAPER1_GATE1_Q2_VERIFIED_EVIDENCE_REVISED_v2.docx` (bàn giao qua Cowork outputs), lưu trong thư mục dự án theo quy tắc file.

---

## Highlights

- A run-aware dataset governance protocol, built on a locked run registry, is defined for labelled vibration data from a scaled bolted steel frame under controlled connection states.
- A leakage-safe evaluation workflow enforces run-level partitioning before windowing and restricts all learned preprocessing to training runs only.
- Low-cost sensor configurations and model families are compared under identical held-out runs, seeds, tuning budgets, and metric implementations.
- Uncertainty is reported at the level of independent runs, supported by group-preserving empirical-null analysis rather than window-level statistics.
- The study delivers bounded laboratory condition evidence intended to inform sensing decisions in inspection-oriented construction asset management.

---

## Abstract

Condition monitoring of bolted steel frames requires that vibration measurements be converted into trustworthy condition evidence, and the trustworthiness of that evidence depends jointly on the sensing configuration and on the validity of the evaluation protocol. Windows derived from the same measurement run are not independent experimental observations, and evaluation schemes that split windows at random can substantially inflate apparent classification performance; in addition, sensor configuration is commonly fixed while only models are compared, so its influence on reported performance is rarely isolated under controlled conditions. This paper addresses that methodological gap for a laboratory case: a scaled bolted steel frame measured with low-cost accelerometers under controlled connection states (healthy, apex connection, beam–column connection, and brace connection states, treated as categorical). A run-aware evaluation protocol is specified in which the independent measurement run is the unit of splitting and inference, run assignment precedes windowing, all learned preprocessing is fitted on training runs only, and all sensor configurations and model families are evaluated on identical leave-one-run-out (LORO) folds with locked seeds and tuning budgets. Classification performance is reported as macro-F1 per held-out run, with run-level uncertainty and group-preserving permutation analysis in place of window-level statistics. **[DATA REQUIRED – Final LORO results: per-run macro-F1 for each sensor configuration (S1, S2, S1+S2) and each retained model family, from the locked run registry and executed LORO protocol; required before any quantitative statement can be made in this abstract.]** The contribution is a transparent, reproducible evaluation protocol and bounded laboratory evidence on how sensor configuration affects apparent classification performance under leakage-controlled conditions. The evidence is limited to controlled connection states of one laboratory specimen; the study does not address in-service condition assessment, physical damage quantification, lab-to-field transfer, or maintenance prognosis.

**Keywords:** run-aware evaluation; data leakage; vibration monitoring; sensor configuration; controlled connection states; scaled bolted steel frame; machine learning; condition evidence

---

## 1. Introduction

Industrial steel-frame buildings depend on bolted connections whose condition can change over the service life of the asset. For owners and asset managers, the practical question is not only whether vibration measurements can be classified by a machine-learning model, but whether the resulting classification constitutes trustworthy condition evidence that can support inspection decisions. Trustworthy condition evidence requires two things simultaneously: an appropriate sensing configuration, which bounds the information available to any model, and a valid evaluation protocol, which determines whether reported performance reflects genuine generalisation or an artefact of the data handling.

The second requirement is frequently violated in vibration-based classification studies through the treatment of derived signal windows as if they were independent experiments. Windows cut from the same measurement run share the excitation event, the physical state, the environmental context, and the sensor placement of that run; they are derived observations, not independent experimental units. Sample-size analysis for classification models shows that multiplying derived observations does not increase the number of independent experimental units, and that the precision of performance estimates is governed by the number of independent groups (Beleites et al., 2013). When windows from one run are distributed at random across training and test partitions, information leaks between partitions and apparent performance can be substantially inflated: this effect has been demonstrated directly on vibration signals, where classification performance collapsed once all segments from one physical source were kept in a single partition (Matania et al., 2024), and where the choice of grouping scale — run, day, or physical part — together with sensor position materially changed apparent performance on bearing vibration data (Wheat et al., 2024). Comparable inflation of record-wise over subject-wise validation has been quantified in other signal domains (Tougui et al., 2021).

At the same time, sensor configuration is usually held fixed while models are compared. The available information for classification is set by the number, position, and quality of the sensors, yet controlled studies that compare sensor configurations and model families under identical run-aware controls — same held-out runs, same preprocessing rules, same tuning budget — are rare within the reviewed evidence base. This leaves practitioners without controlled evidence on a first-order deployment question: whether changing the sensing configuration or changing the model has more influence on the evidence a monitoring system can produce.

This paper addresses that methodological gap in a controlled laboratory case: a scaled bolted steel frame instrumented with low-cost accelerometers and measured under four controlled connection states. The paper deliberately does not develop a new machine-learning architecture, does not diagnose damage in field structures, and does not claim severity assessment. Its research question is:

> How reliably can vibration data from different low-cost sensor configurations produce evidence distinguishing controlled connection states in a scaled bolted steel frame under a run-aware, leakage-controlled evaluation protocol?

The scope of the claim is laboratory condition evidence under controlled connection states and a run-aware evaluation protocol. The contributions are: (1) a run-aware dataset governance protocol for laboratory vibration data, with a locked run registry as the auditable basis for all splits; (2) a leakage-safe LORO evaluation workflow in which run assignment precedes windowing and all learned preprocessing is fitted on training runs only; (3) a fair comparison of low-cost sensor configurations and model families under identical folds, seeds, and budgets; and (4) run-level uncertainty reporting with group-preserving empirical-null analysis appropriate for small numbers of independent runs.

The remainder of the paper is organised as follows. Section 2 reviews related work on controlled vibration evidence for bolted connections, leakage and group-aware validation, small-group uncertainty, and fair sensor/model comparison. Section 3 describes the experimental programme and data governance. Section 4 specifies the run-aware evaluation protocol. Section 5 reports results. Section 6 discusses implications for construction asset management. Section 7 states limitations, and Section 8 concludes.

---

## 2. Related Work

### 2.1. Controlled vibration evidence for bolted connections

Laboratory studies have established that controlled changes at bolted connections alter measurable vibration response and can be classified from accelerometer data. Zhang et al. (2020) classified bolted-connection conditions of a laboratory steel frame from single-accelerometer data with repeated measurements, providing a direct steel-frame precedent, although the study does not establish a leakage-safe run-level protocol. Eraliev et al. (2022) classified multiple bolt-loosening conditions from vibration data and illustrate the window-split caveat that motivates the present protocol. Valdez-Yepez et al. (2024) documented a labelled bolt-loosening vibration dataset with explicit sensor metadata and repeated runs on a jacket-type structure, demonstrating the dataset-documentation practice adopted here. Review evidence confirms the general transition from signal processing to learned classifiers for vibration-based assessment and the recurring validation limitations of that literature (Avci et al., 2021). Within the reviewed evidence base, no study of a bolted steel frame combines controlled multi-state classification with a fully run-aware, leakage-controlled comparison of sensor configurations and model families.

### 2.2. Leakage and group-aware validation

Direct evidence from vibration classification shows the consequences of ignoring the grouped structure of signal data. Matania et al. (2024) demonstrated on two vibration benchmark datasets that source-group separation must precede segmentation: models evaluated with random segment-level splits appeared to perform well, but performance collapsed under proper held-out grouping. Wheat et al. (2024) showed on bearing vibration data that the grouping scale used for splitting — run, day, or physical part — and the sensor position can materially change apparent classification performance, and that comparisons are only meaningful on identical folds. Beyond vibration, Tougui et al. (2021) compared cross-validation techniques on grouped signal data and found that group-wise and leave-one-group-out (LOGO) validation better estimate performance on unseen sources than record-wise or random splitting, and that preprocessing must remain inside training folds. Beleites et al. (2013) provide the sample-size rationale: derived observations do not increase independent experimental units, so the effective sample size of a windowed vibration dataset is the number of independent runs, not the number of windows. The first two sources constitute direct methodological evidence from vibration classification; the latter two are methodological evidence from adjacent domains, and none of them quantifies performance for a bolted steel frame.

### 2.3. Small-group uncertainty and empirical chance

Small numbers of independent groups constrain what can be inferred from classification results. Combrisson and Jerbi (2015) showed that small samples can yield apparently above-chance classification purely by chance, and that empirical chance analysis — rather than the theoretical chance level — is required when samples are small. Ojala and Garriga (2010) formalised permutation tests for classifier performance, in which the full training-and-evaluation pipeline is repeated under permuted labels to estimate an empirical null distribution; the framework presumes that the permuted unit is exchangeable, which for grouped vibration data means that complete runs, not individual correlated windows, must be the permutation unit. Beleites et al. (2013) additionally show that precision of performance estimates degrades rapidly at small numbers of independent groups, which mandates explicit uncertainty reporting rather than point estimates. Together these sources justify the group-preserving empirical-null analysis adopted in Section 4.8, while none of them validates the specific run count of the present experiment.

### 2.4. Fair sensor and model comparison

Comparing sensor configurations or model families fairly requires that all candidates be evaluated under identical conditions. Wheat et al. (2024) provide direct evidence that sensor position can alter apparent vibration-classification performance as much as methodological choices, and that fold-identical comparison is a precondition for attributing performance differences to the sensor configuration rather than to the split. For statistical comparison of models, Demšar (2006) established the standard non-parametric machinery (Wilcoxon signed-ranks and Friedman tests) for comparisons over multiple data sets; that machinery, however, presumes defensibly independent paired units, and overlapping LORO fold scores — whose training sets share most of their runs — are not independent data sets in Demšar's sense. This limitation is explicit in the present protocol: fold-level significance tests are treated as exploratory at most (Section 4.8). Ramasso et al. (2024) — a preprint, cited with that boundary — used campaign/reassembly holdout with sensor comparison, and Goodarzi et al. (2025) quantified the inflation of K-fold relative to LOGO validation, both reinforcing group-aware comparison practice.

### 2.5. Literature gap

Table 1 summarises the reviewed evidence against the requirements of the present study. Within the reviewed evidence base, no single study combines independent-run grouping, explicit leakage control, sensor-configuration comparison, model-family comparison, and run-level uncertainty on a bolted steel frame.

**Table 1. Literature gap within the reviewed evidence base.**

| Study | Independent grouping | Leakage control | Sensor comparison | Model comparison | Run-level uncertainty | Steel-frame relevance |
|---|---|---|---|---|---|---|
| Zhang et al. (2020) | Partial (repeated data; not run-level protocol) | Not established | No (single accelerometer) | Partial | Not reported | Direct (bolted steel frame) |
| Eraliev et al. (2022) | Partial | Window-split caveat noted | Not reported | Partial | Not reported | Adjacent (multi-bolt structure) |
| Valdez-Yepez et al. (2024) | Runs documented | Not the study focus | Sensor metadata documented | No | Not reported | Adjacent (jacket structure) |
| Goodarzi et al. (2025) | Yes (LOGO) | Yes (inflation quantified) | No | Partial | Not reported | Methodological |
| Ramasso et al. (2024, preprint) | Yes (campaign holdout) | Yes | Yes | Partial | Not reported | Adjacent |
| Tougui et al. (2021) | Yes (subject-wise) | Yes (fold-contained preprocessing) | No | Yes | Partial | None (healthcare audio) |
| Matania et al. (2024) | Yes (source groups) | Yes (direct vibration evidence) | No | Partial | Limited | None (bearings) |
| Wheat et al. (2024) | Yes (run/day/part) | Yes (direct vibration evidence) | Yes (two positions) | Partial | Partial | None (bearings) |
| **This study** | **Run-level (locked registry)** | **Split-before-windowing; train-only preprocessing** | **S1 / S2 / S1+S2 under identical folds** | **Under identical folds, seeds, budgets** | **Per-run reporting; group-preserving null** | **Direct (scaled bolted steel frame)** |

---

## 3. Experimental Programme and Data Governance

### 3.1. Specimen

The specimen is a scaled bolted steel frame (nominal scale 1:10) representing a single-bay industrial steel-frame configuration with bolted connections at the apex, the beam–column joints, and the bracing. **[AUTHOR CONFIRMATION REQUIRED – Verified specimen documentation: member sections, materials, connection details, boundary conditions, and specimen drawings or photographs for Figure 1; only facts documented in the experimental records may be stated.]** No quantitative similitude claim or full-scale transfer claim is made: the specimen provides controlled laboratory conditions for generating labelled vibration data, not a validated surrogate of a full-scale building. A nominal design model of the frame, where referenced in this paper, is nominal, uncalibrated, reference-only, and not used for damage diagnosis.

### 3.2. Controlled connection states

Four controlled connection states are studied and treated as categorical classes, not as an ordinal severity scale:

**Table 2. Controlled connection states (categorical).**

| State | Code | Description |
|---|---|---|
| Healthy | H | All connections in the reference tightened condition |
| Apex connection state | A | Controlled change at the apex connection |
| Beam–column connection state | BC | Controlled change at a beam–column connection |
| Brace connection state | BR | Controlled change at a brace connection |

**[AUTHOR CONFIRMATION REQUIRED – Exact physical definition of each controlled state (which bolts, what change was applied, verification procedure, and reset procedure between runs), from the experimental log; required for Table 2 and for the reproducibility statement.]**

### 3.3. Excitation protocol

**[DATA REQUIRED – Verified excitation metadata for each run: excitation type(s), application point, input device, repetition procedure, and any environmental notes, reconciled against the run registry (Section 3.5). The draft reports three excitation types per state, but this is not yet verified against per-run records and must not be stated as final until reconciled. Used in: Section 3.3 text and the run registry; supports the run-independence claim.]**

### 3.4. Sensors and configurations

Two low-cost accelerometer positions are used: S1 at the frame apex and S2 at a beam–column joint. Three sensor configurations are evaluated under the study protocol: S1 only, S2 only, and S1+S2 (both channels).

**[DATA REQUIRED – Verified sensor and channel metadata: hardware model, measurement range, sensitivity, axis/channel definitions, mounting method, orientation, sampling frequency, synchronisation method between channels, and the Sensor_ID assigned to each physical channel. The draft reports MEMS accelerometers at 100 Hz sampling; this must be confirmed against acquisition records before being stated as final. Used in: Table 3 (sensor metadata table), Section 3.4; supports the sensor-configuration comparison claim (C1-17) and the identifier chain Sensor_ID → downstream records.]**

**[TABLE REQUIRED – Table 3: Sensor and channel metadata (one row per physical channel: Sensor_ID, hardware model, range, sensitivity, axis, mounting, position, sampling rate, synchronisation). Input: acquisition records. Used in: Section 3.4.]**

### 3.5. Run registry and file manifest

The run registry is the auditable foundation of the entire evaluation and is mandatory before any split is defined. Each independent measurement run receives a unique Run_ID and one registry row recording: Run_ID; date/time; connection state; excitation descriptor; sensor configuration(s) recorded; file reference(s); operator notes; and inclusion status.

**[DATA REQUIRED – `RUN_REGISTRY_LOCKED.csv`: one row per physical run with columns Run_ID, Date_Time, State_Code, Excitation_ID, Sensors_Recorded, File_IDs, Operator_Notes, Include_Flag, Exclude_Reason. The draft reports 72 recordings (4 states × 3 excitations × 6 runs), but the run count is reported, not locked; the registry must reconcile every raw file to exactly one run. Used in: Sections 3.5, 5.1; blocks Gate 1.]**

**[DATA REQUIRED – `DATASET_FILE_MANIFEST.csv`: one row per raw data file with columns File_ID, Filename, Run_ID, Channel/Sensor_ID, Duration, Sample_Count, Checksum. Used in: Section 5.1 dataset audit; blocks Gate 1.]**

### 3.6. Data quality and exclusion rules

Data quality is audited before evaluation, with pre-declared rules: reconciliation of the file count against the run registry; detection of corrupted or incomplete recordings; detection of clipping; identification of unequal recording durations; identification of missing channels; and a recorded inclusion/exclusion reason for every run. Exclusions are made at run level, never at window level, and are reported in Section 5.1.

**[ANALYSIS REQUIRED – Data-quality audit script over the file manifest: file-count reconciliation, clipping detection, duration statistics, missing-channel report, and a per-run include/exclude table with reasons. Output: audit table for Section 5.1. Supports: dataset integrity claim; blocks Gate 1.]**

---

## 4. Run-Aware Evaluation Protocol

This section is the methodological core of the paper.

### 4.1. Independent unit

The independent experimental unit is the measurement run. Windows derived from a run by segmentation are derived observations that share the run's excitation event, physical state, and measurement context; they are not independent experiments, and the window count is not the effective sample size (Beleites et al., 2013). All partitioning, uncertainty reporting, and inference in this study therefore operate at run level.

### 4.2. Split before windowing

Partitioning precedes windowing, so that no derived observation can cross a partition boundary (Matania et al., 2024; Tougui et al., 2021). The required workflow is:

```
Run registry
→ hold out complete run
→ window training runs
→ fit preprocessing on training runs
→ train/tune using training data only
→ transform and evaluate held-out run
```

### 4.3. Preprocessing

Fixed signal operations (e.g., detrending or filtering with pre-declared constants) are distinguished from learned transformations (e.g., standardisation statistics, feature selection, dimensionality reduction, calibration). All learned transformations are fitted on training runs only, inside each fold, and then applied unchanged to the held-out run (Tougui et al., 2021).

**[METHOD DECISION REQUIRED – Final preprocessing specification: the exact fixed operations and learned transformations, with parameters, per model family. Input: project preprocessing code. Used in: Section 4.3 and the leakage audit (Section 4.9); supports claim C1-14.]**

### 4.4. LORO folds

Evaluation uses leave-one-run-out (LORO) cross-validation: each fold holds out one complete run (all of its windows, all of its channels) and trains on the remaining runs. All sensor configurations and all model families are evaluated on identical held-out runs, so that performance differences cannot be attributed to differing splits (Wheat et al., 2024).

**[DATA REQUIRED – Common LORO fold registry: fold index, held-out Run_ID, training Run_IDs, applied identically across all sensor configurations and models. Input: locked run registry. Used in: Sections 4.4, 5.2; blocks Gate 1.]**

### 4.5. Models

Only model families with verified provenance are retained: for each model, the configuration, tuning procedure, seed policy, and software environment must be documented and reproducible.

**[METHOD DECISION REQUIRED – Final model roster with verified provenance: candidate families from the draft are Random Forest, SVM, Logistic Regression, and a 1D convolutional network; each is retained only if its configuration, tuning budget, and seeds are documented and re-executable under the final LORO protocol. Used in: Sections 4.5, 5.4.]**

**ResNet1D.** A ResNet1D model is reported in project working materials, but its sensor/channel mode and provenance (folds, seeds, preprocessing, checkpoint) are not yet verified, and the reviewed literature cannot repair missing project provenance (claim C1-18). The model is included only if channel mode, folds, seeds, preprocessing, and checkpoint are verified; otherwise it is formally excluded from the results, and the exclusion and its reason are stated. **[AUTHOR CONFIRMATION REQUIRED – ResNet1D provenance verification: channel/sensor mode, fold assignment, seeds, preprocessing, training script, and checkpoint hash; decision to include or formally exclude. Used in: Sections 4.5, 5.4, 5.7; blocks the model-comparison claim if unresolved.]**

### 4.6. Fairness controls

The following are locked identically across all compared configurations and models before any final run: fold assignments; random seeds; hyperparameter tuning budget; preprocessing rules; stopping criteria; and the metric implementation.

### 4.7. Metrics

The primary metric is macro-F1, computed per held-out run. Secondary reporting includes per-class F1, balanced accuracy (or accuracy where class balance justifies it), confusion matrices per fold and in aggregate, and retained run-level prediction outputs enabling re-analysis.

### 4.8. Uncertainty and statistical analysis

Uncertainty reporting follows these principles, each grounded in the reviewed methodological evidence:

1. Every held-out-run result is reported individually; no point estimate replaces the run-level distribution (Beleites et al., 2013).
2. Windows are not treated as independent observations, and no bootstrap of individual windows is performed.
3. The set of LORO fold scores is not presented as a set of independent data sets: training sets of different folds overlap in most of their runs, so the independence assumptions of Wilcoxon/Friedman machinery are not met (Demšar, 2006); any such test is exploratory at most.
4. Small numbers of independent runs make apparently above-chance performance possible by chance, so an empirical chance analysis is mandatory (Combrisson and Jerbi, 2015).
5. The preferred inferential tool is group-preserving, full-pipeline permutation: state labels are permuted at run level, the complete pipeline (preprocessing, training, evaluation) is re-executed per permutation, and the observed statistic is compared to the resulting empirical null (Ojala and Garriga, 2010; Combrisson and Jerbi, 2015). Effect sizes and transparent sensitivity analyses accompany the permutation results.
6. No confidence intervals are stated unless produced by a pre-declared, group-respecting procedure.

**[METHOD DECISION REQUIRED – Final inferential procedure: exact permutation scheme (number of permutations, permuted unit = complete run, statistic definition), effect-size measure, and any exploratory fold-level test, to be approved before the final analysis is run. Used in: Sections 4.8, 5.6.]**

### 4.9. Leakage audit

A completed leakage-audit checklist is reported with the results:

- grouping (run assignment) performed before partitioning;
- no run shared across folds;
- scaling statistics fitted on training runs only;
- feature selection fitted on training runs only;
- calibration and hyperparameter tuning on training runs only;
- no reuse of held-out data across analysis iterations;
- identical folds across all compared configurations and models;
- full provenance (code version, seeds, environment) retained.

**[ANALYSIS REQUIRED – Executed leakage audit: item-by-item evidence (code references, log excerpts) for each checklist entry above. Output: completed checklist table for Section 5.1/appendix. Blocks Gate 1.]**

---

## 5. Results

All results in this section must come from the final Gate 1 outputs (locked run registry, executed LORO protocol, verified provenance). Numbers from earlier single-split working analyses are preliminary — not verified under the final LORO protocol — and are not reported here.

### 5.1. Dataset and run-registry audit

**[TABLE REQUIRED – Dataset audit table: runs per state, files per run, windows per run (with windowing parameters), excluded runs with reasons, and leakage-audit checklist outcome. Input: RUN_REGISTRY_LOCKED.csv, DATASET_FILE_MANIFEST.csv, audit script output. Supports: dataset integrity claim.]**

### 5.2. LORO performance by held-out run

**[TABLE REQUIRED – Per-fold macro-F1 table: rows = held-out Run_ID; columns = sensor configuration × model family; plus run-level summary (median, min, max). Input: per-run predictions from executed LORO. Supports: primary RQ1 evidence.]**

**[FIGURE REQUIRED – Run-level performance plot: macro-F1 per held-out run, grouped by sensor configuration, one panel per model family (or equivalent). Input: same as above.]**

### 5.3. Sensor-configuration comparison

**[ANALYSIS REQUIRED – Sensor-configuration contrast on identical folds: per-run paired differences in macro-F1 between S1, S2, and S1+S2 for each model family, with effect sizes and group-preserving permutation results. Supports claim C1-17 (sensor configuration may materially affect apparent performance); no optimality claim is permitted.]**

### 5.4. Model-family comparison

**[ANALYSIS REQUIRED – Model-family contrast on identical folds: per-run paired differences between retained model families under each sensor configuration, with effect sizes; exploratory fold-level tests only, labelled as exploratory (Section 4.8). ResNet1D appears here only if provenance is verified (Section 4.5).]**

### 5.5. Per-class confusion patterns

**[TABLE REQUIRED – Confusion matrices per fold and aggregated, per sensor configuration and model family; per-class F1 table. Input: retained per-window predictions with Run_ID, aggregated to run level. Supports: descriptive confusion-pattern discussion (Section 6.4).]**

### 5.6. Uncertainty and empirical-null results

**[ANALYSIS REQUIRED – Group-preserving full-pipeline permutation results: empirical null distribution of macro-F1 under run-level label permutation, observed statistic position, and empirical p-value; per sensor configuration. Supports claim C1-15; required before any above-chance statement.]**

### 5.7. Sensitivity analyses

Where data are available, the following pre-declared sensitivity analyses are reported: non-overlapping windows versus the primary windowing; alternative overlap settings; excitation-specific analysis; exclusion of questionable runs; seed sensitivity; and a ResNet1D included/excluded comparison if that model's provenance is resolved.

**[ANALYSIS REQUIRED – Sensitivity analysis suite as listed above; each analysis reports the same run-level macro-F1 structure as Section 5.2. Supports: robustness of the primary findings.]**

### 5.8. Confidence/evidence indicator (CEI)

A CEI is reported only if all of the following are available: a formal definition; a rationale; a calibration or reliability analysis; a run-aware evaluation of the indicator; and a claim bounded as confidence/evidence, not severity. These conditions are not yet met; the CEI is therefore excluded from the main results and specified as a future analysis request. **[ANALYSIS REQUIRED – CEI definition and run-aware reliability analysis, if the indicator is to be included in a future revision; otherwise this subsection is removed at submission.]**

---

## 6. Discussion

### 6.1. Effect of run-aware evaluation

**[ANALYSIS REQUIRED – Leakage-prone versus leakage-safe contrast: this comparison may be reported only if a random-window-split evaluation is deliberately executed alongside the LORO protocol on the same data, as a controlled illustration; otherwise this subsection discusses the protocol's rationale only, citing the direct vibration evidence (Matania et al., 2024; Wheat et al., 2024) without project numbers.]**

### 6.2. Sensor configuration under common controls

The protocol isolates the sensor-configuration effect by holding folds, seeds, budgets, and preprocessing identical. Interpretation is bounded: a configuration that performs better under this protocol is better *under the study protocol*, on this specimen, for these states; no universal optimality is claimed. No statement that the sensor effect exceeds the model effect is made unless the final LORO evidence supports it. **[DATA REQUIRED – Final sensor-configuration findings from Section 5.3 before any comparative statement is written here.]**

### 6.3. Model comparison under small independent n

With a small number of independent runs, model-family differences must be interpreted conservatively: run-level paired differences and effect sizes are descriptive, the permutation analysis addresses chance-level performance rather than model ranking, and no claim of general superiority of one model family over another is made. **[DATA REQUIRED – Final model-comparison findings from Section 5.4 before any comparative statement is written here.]**

### 6.4. Confusion patterns

Empirical confusion patterns among the controlled states are described from the final confusion matrices. Where a qualitative mechanical interpretation is offered, it may be supported by the nominal design model of the frame — which is nominal, uncalibrated, reference-only, and not used for damage diagnosis — and any such interpretation is labelled *hypothesis, not confirmed*. No inference about physical stiffness loss or bolt preload is made. **[DATA REQUIRED – Final confusion matrices from Section 5.5 before this subsection is written.]**

### 6.5. Relevance to construction asset management

For construction and asset management, the implications of this study are limited to four points. First, sensing choices are resource-allocation decisions: the number and placement of low-cost sensors is a budgetable design variable whose effect on evidence quality can be evaluated with the protocol presented here. Second, the protocol makes the cost–information trade-off explicit: identical-fold comparison of sensor configurations shows what information a marginal sensor adds under controlled conditions. Third, trustworthy evidence generation — not model sophistication — is the binding constraint for monitoring programmes that must feed auditable inspection records: leakage-controlled evaluation is what makes laboratory performance claims defensible to asset owners. Fourth, the run registry and audit artefacts constitute a reproducible monitoring-design practice transferable to other laboratory programmes. No claim is made about maintenance effectiveness or field deployment readiness.

---

## 7. Limitations

This study is bounded by the following limitations. The evidence comes from one laboratory specimen at nominal 1:10 scale; the connection states are controlled and categorical, not naturally occurring deterioration; the number of independent runs is small, which constrains the precision of every performance estimate; windows are derived observations and may overlap, so all inference is restricted to run level; no physical severity is measured or inferred; no field damage assessment is performed; no quantitative lab-to-field transfer is claimed; the nominal design model is uncalibrated and reference-only, and no calibrated finite-element analysis is used; external validity beyond the specimen, sensors, and excitation conditions studied is limited; and the uncertainty of all findings is constrained by the small independent n, which no window-level statistic can repair.

---

## 8. Conclusions

This paper answers RQ1 — how reliably vibration data from different low-cost sensor configurations can produce evidence distinguishing controlled connection states in a scaled bolted steel frame — by specifying and executing a run-aware, leakage-controlled evaluation protocol in which the independent run is the unit of splitting and inference, partitioning precedes windowing, learned preprocessing is confined to training runs, all comparisons share identical folds, and uncertainty is reported at run level with a group-preserving empirical null.

**[DATA REQUIRED – Final quantitative answer to RQ1 from Sections 5.2–5.6; until the locked run registry, executed LORO folds, train-only preprocessing audit, verified model provenance, and permutation results are available, no quantitative conclusion is stated.]**

Gate 1 is not yet closed; the manuscript specifies the remaining experimental controls: the locked run registry and file manifest, the executed common LORO folds, the train-only preprocessing and leakage audits, verified model provenance (including the ResNet1D include/exclude decision), run-level results with group-preserving permutation analysis, and the pre-declared sensitivity analyses.

---

## Data and Code Availability

**[AUTHOR CONFIRMATION REQUIRED – Repository decision: whether the run registry, raw data, and evaluation code will be deposited (and where), and the licence; until confirmed, no repository statement is made.]**

---

## References

*Verified new methodological sources (full texts deep-read; metadata verified):*

1. Beleites, C., Neugebauer, U., Bocklitz, T., Krafft, C., Popp, J. (2013). Sample size planning for classification models. *Analytica Chimica Acta*, 760, 25–33. https://doi.org/10.1016/j.aca.2012.11.007
2. Combrisson, E., Jerbi, K. (2015). Exceeding chance level by chance: The caveat of theoretical chance levels in brain signal classification and statistical assessment of decoding accuracy. *Journal of Neuroscience Methods*. https://doi.org/10.1016/j.jneumeth.2015.01.010 **[REFERENCE METADATA CHECK REQUIRED – volume/pages from the journal record.]**
3. Demšar, J. (2006). Statistical comparisons of classifiers over multiple data sets. *Journal of Machine Learning Research*, 7, 1–30.
4. Matania, O., et al. (2024). Test-training leakage in evaluation of machine learning algorithms for condition-based maintenance. *Proceedings of the PHM Society European Conference*, 8(1). https://doi.org/10.36001/phme.2024.v8i1.4125 **[REFERENCE METADATA CHECK REQUIRED – complete author list from the conference PDF.]**
5. Ojala, M., Garriga, G. C. (2010). Permutation tests for studying classifier performance. *Journal of Machine Learning Research*, 11, 1833–1863.
6. Tougui, I., Jilbab, A., El Mhamdi, J. (2021). Impact of the choice of cross-validation techniques on the results of machine learning-based diagnostic applications. *Healthcare Informatics Research*, 27(3), 189–199. https://doi.org/10.4258/hir.2021.27.3.189
7. Wheat, et al. (2024). Impact of data leakage in vibration signals used for bearing fault diagnosis. *IEEE Access*, 12, 169883–169892. https://doi.org/10.1109/ACCESS.2024.3497716 **[REFERENCE METADATA CHECK REQUIRED – complete author list and initials from the IEEE record.]**

*Canonical RQ1 sources retained from the existing Living Evidence Base (full texts previously deep-read; bibliographic details to be confirmed against Zotero records before submission):*

8. Avci, O., et al. (2021). A review of vibration-based damage detection in civil structures: From traditional methods to machine learning and deep learning applications. *Mechanical Systems and Signal Processing*. **[REFERENCE METADATA CHECK REQUIRED – volume/article/pages.]**
9. Eraliev, O., Lee, K.-H., Lee, C.-H. (2022). Multi-bolt loosening classification from vibration data. **[REFERENCE METADATA CHECK REQUIRED – exact title, venue, volume, DOI.]**
10. Goodarzi, et al. (2025). Leave-one-group-out versus K-fold validation: leakage inflation evidence. **[REFERENCE METADATA CHECK REQUIRED – exact title, venue, DOI.]**
11. Ramasso, E., et al. (2024). Campaign/reassembly holdout with sensor comparison (preprint; cited with preprint boundary). **[REFERENCE METADATA CHECK REQUIRED – exact title, repository, identifier.]**
12. Valdez-Yepez, et al. (2024). Labelled bolt-loosening vibration dataset with sensor metadata and repeated runs (jacket structure). **[REFERENCE METADATA CHECK REQUIRED – exact title, venue, DOI.]**
13. Zhang, Y., Biswal, S., Wang, Y. (2020). SHMnet: condition classification of bolted connections of a laboratory steel frame from single-accelerometer data. **[REFERENCE METADATA CHECK REQUIRED – exact title, venue, volume, DOI.]**
