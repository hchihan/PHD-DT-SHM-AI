# PAPER1 v8.1: pre-submission risk audit (Structural Health Monitoring, SAGE)

**File audited:** `PAPER1_v8.1_SHM_RISK_REDUCED.docx`, 13 September 2026.
**Perspective:** SHM handling editor and technical reviewer.
**Evidence base:** the manuscript and the project files only. Submission optimism is not a criterion.
**Automated status:** 50/50 checks PASS (`check_v81.py`: citations, cross-references, table identity to v8, numeric preservation, protected limitations, banned-word scan, image resolution); Office XSD validation PASS.

Status key:

- **CLOSED:** resolved in the file.
- **MITIGATED:** the risk is reduced by text or evidence but an editor or reviewer could still raise it.
- **OPEN BUT DISCLOSED:** a genuine limitation that is stated transparently.
- **AUTHOR ACTION REQUIRED:** cannot be resolved without the author or source files.

---

## 1. The six submission-risk items from the v8.1 brief

| # | Risk item | Status | Evidence in v8.1 | Remaining action |
|---|---|---|---|---|
| 1 | Figure 3 contradicts §3.6 (standardisation labelled "training data only") | **CLOSED** (scientifically) / AUTHOR ACTION (approval) | The contradictory raster is replaced by a redrawn schematic stating "Per-window channel standardisation (applied independently to all partitions)" and "SVM StandardScaler (fitted on training data only)". The caption repeats the logic, and the AI disclosure covers the redraw | **[AUTHOR ACTION: approve the redrawn Figure 3 or replace it with a corrected source diagram]** |
| 2 | Acquisition-order / state confounding not stated explicitly | **CLOSED** as a disclosure. The underlying limitation is OPEN BUT DISCLOSED | New §5.6 sentence on non-randomised acquisition and the consistent reference-state position, with no mechanism asserted | none |
| 3 | Figure 2: duplicate photo in (b), two photos under (d), sub-300 dpi photos | **MITIGATED** / AUTHOR ACTION | (b) is explicitly declared a repeated view of Figure 1(d). The second (d) photo is now its own panel (e) with a neutral description. Figure 1(a) is replaced by its native-resolution original (404 dpi) | **[AUTHOR ACTION: supply a true B1 photograph if one exists; confirm what panel (e) shows]**. **[AUTHOR ACTION: upload camera originals for Figures 1(b–c) (299 dpi), 2(d) (211 dpi) and 2(e) (290 dpi)]** |
| 4 | Author metadata and declarations | **AUTHOR ACTION REQUIRED** | Nothing was invented. SAGE-compliant default wording remains in place for COI, funding and data | See §4 |
| 5 | Data and code availability | **AUTHOR ACTION REQUIRED** (decision) / MITIGATED (inventory) | The conservative statement is kept. A substantial reproducibility archive exists locally (§5) | Decide on a repository before submission |
| 6 | Desk-rejection risk "known grouped validation applied to one small dataset" | **MITIGATED** | Explicit advancement sentence in the Abstract and §1, framed as the documented consequence of a known principle. Three verified references anchor the argument in SHM literature (§2.3, §5.3, §5.5, §5.6). Repetitive defensive passages were trimmed (§2.4, §3.4, §5.2, §5.3, §5.4, §5.5) | A residual editorial judgement remains; see A1 and A3 |

## 2. Desk-rejection risks

| Code | Risk | Status | Assessment |
|---|---|---|---|
| A1 | Insufficient novelty or advancement | **MITIGATED** | The paper states plainly that neither the controls nor their combination is new. It claims an experimentally documented consequence: near-perfect within-campaign separation (CP1/CP2), weaker run-dependent separation (CP3) and near-chance exploratory transfer on one bolted steel frame. This is honest and coherent. An editor who wants methodological or algorithmic novelty may still decline. The paper's value rests on the provenance-aware reporting and the campaign-dependence evidence, which fit the SHM journal's information-quality literature (now cited: Makhoul, Kamariotis, Zorzi) |
| A2 | Journal mismatch | **CLOSED** | Vibration-based SHM of bolted steel-frame connections, generalisation limits, and SHM information quality. It cites SHM-journal precedents (Zhang 2020, Biswal 2022, Ramasso 2025, Zorzi 2025), and the OpenAlex cross-check independently rated SHM fit as STRONG |
| A3 | Empirical basis too small | **OPEN BUT DISCLOSED** | 18 runs, one specimen, 12-recording test folds, and quantisation at 1/12 are stated in §3.10 and §5.6. Nothing can be done without new experiments, which are out of scope. The framing converts small size into a stated boundary rather than hiding it |
| A4 | Confusing contribution | **MITIGATED** | Abstract, §1 and §6 now state the same contribution: bounded separability and variability evidence plus the interpretive consequence. The research question in §1 is unchanged |
| A5 | Excessive methodological defensiveness | **MITIGATED** | Six repetitive passages were shortened, and every limitation still appears at least once in full (checked). The manuscript remains caveat-dense by design; this is the price of the locked framing and is not a blocker |

## 3. Reviewer risks

| Code | Risk | Status | Where handled | Assessment |
|---|---|---|---|---|
| B1 | Acquisition-order confounding | **OPEN BUT DISCLOSED** | Table 2; §3.4; §4.4 (CP3 order groups); §4.5 (S0/B1 position); §5.3; **§5.6 new sentence** | The design cannot separate state from measurement history, and the paper now says so in one explicit sentence. Randomised acquisition would require new experiments |
| B2 | Definition of the experimental unit / run | **OPEN BUT DISCLOSED** | §3.5 ("design decision … not a verified property"; "independent experimental unit is avoided"); §5.4; §5.6 | Clearly defined as the acquisition grouping unit. Reassembly between runs is undocumented |
| B3 | Deep-model HPO dependence | **OPEN BUT DISCLOSED** (MITIGATED for the primary claim) | §3.9; Table 5; §4.3; §5.4; §5.6; Figure 3 side box | The primary result rests on untuned feature-based models. The dependence is disclosed, not corrected; nested re-selection was not done |
| B4 | Cross-campaign validity | **OPEN BUT DISCLOSED** | §3.8; §4.7 (four limits); §5.1; §5.5; §6 | Exploratory only: deep models only, 2 directions, CP1 not evaluated, permutation exchangeability not justified, and the target was in the HPO pool. The optional RF/SVM transfer (§6 below) would strengthen this |
| B5 | FFT-band reproducibility | **CLOSED** | §3.6 | Band groups now fully specified from the executed extractor: 12 contiguous groups of 16–17 of the 201 `rfft` bins, about 4.2 Hz each, 0–50 Hz, Hanning window, DC zeroed, relative power. The pair feature is identified as Pearson correlation. The 228/366 dimensions are verified (IT-03) |
| B6 | Resultant-channel treatment | **MITIGATED** | §3.3; Table 1; §3.6 | Provenance is closed: exported by PASCO, not computed by the build (IT-02). A reviewer may note that the resultant is a deterministic function of x, y, z and so adds redundant input. It is documented, not analysed; no ablation was run, which is out of scope |
| B7 | Wireless-sensor synchronisation | **OPEN BUT DISCLOSED** | §3.6 (alignment by sample index; not called synchronisation); §4.1 third limit; §5.6 | PASCO pre-export synchronisation is undocumented. **[AUTHOR TO CONFIRM: any PASCO acquisition setting or record on multi-sensor synchronisation]** |
| B8 | Data and code availability | **AUTHOR ACTION REQUIRED** | Data availability statement | See §5 |
| B9 | Physical interpretation limits | **OPEN BUT DISCLOSED** | §1 last paragraph; §3.1; §3.2; §4.6; §5.6 (including the **new** laboratory-EOV sentence, ref. 38); §6 | No torque, preload, stiffness or modal data; no lab-to-field transfer; labels are locations, not severity. Consistent throughout |
| B10 | Physical sensor-to-position mapping | **OPEN BUT DISCLOSED** | §3.3; §4.1 second limit; §5.6 | Assigned by gravity orientation in code, with no device record. **[AUTHOR TO CONFIRM: a device-serial or mounting log, if one exists]** |
| B11 | Training-time file identity | **OPEN BUT DISCLOSED** | §4.1 first limit; §5.6 | No load-time hashes exist; the reconciliation covers archive consistency only |

## 4. Author metadata and declarations: items requiring the author

Placeholders appear **here only**. The manuscript carries no bracketed placeholder text (checked).

| Item | Current manuscript text | Status |
|---|---|---|
| Final author name format and order | "Han – Ho Chi; Tri – Ngo Ngoc; Duc – Pham Anh" | **[AUTHOR TO CONFIRM]** the print form and order; it must match the submission system exactly |
| Affiliation wording | "Da Nang University of Science and Technology (DUT), Da Nang, Vietnam" | **[AUTHOR TO CONFIRM]** the official English name (e.g. "The University of Danang – University of Science and Technology") |
| Department / faculty | absent | **[AUTHOR TO CONFIRM]** |
| Corresponding author | "Tri – Ngo Ngoc" (author's own v8 edit, kept) | **[AUTHOR TO CONFIRM]**; SAGE requires the corresponding author's full contact details on the title page |
| Corresponding e-mail | absent | **[AUTHOR TO CONFIRM]**; required |
| ORCID | absent | **[AUTHOR TO CONFIRM]**; required for the submitting author |
| Funding | SAGE nil statement | **[AUTHOR TO CONFIRM]**; replace with funder and grant number if any scholarship or grant supported the work |
| Conflict of interest | SAGE nil statement | **[AUTHOR TO CONFIRM]** for all three authors |
| Data availability | "available from the corresponding author upon reasonable request" | **[AUTHOR TO CONFIRM]**; keep, or replace with a repository DOI (§5) |
| AI disclosure | names Claude (Anthropic) and Consensus; discloses the Figure 3 redraw | **[AUTHOR TO CONFIRM]**: (i) whether other generative-AI tools were used (none are recorded in the project, but OpenAI Codex is installed on the working machine); (ii) versions, if you wish to state them; (iii) **whether the original Figure 3 raster was generated or edited with generative AI** (its rendering style suggests it may have been; no record exists); (iv) **whether any analysis code used for the reported results was written with AI assistance** (no AI co-author or assistant trace was found in the archived code, commit logs or notebooks, but absence of a trace is not confirmation). If (iv) is yes, SAGE policy requires the disclosure to say so |

## 5. Data and code availability: inventory and recommendation

**Available locally** (`D:\01_RESEARCH\08_Output_07.09\`):

| Material | Location | Status |
|---|---|---|
| Built dataset (NPZ windows, all sensor configurations) | `v1/cp*_s*/R*.npz` (102 files) + `index.csv`, `manifest.json` (window 400, step 200, 216 recordings, 6,899 windows, 951 dropped samples, canonical-manifest SHA-256), `label_map.json`, `schema.json` | available |
| QC record | `v1/qc/build_report.json`, `v1/qc/rejected_windows.csv`, `v1/logs/build.log` | available |
| Split definitions | `v1/splits/coverage.json`, `representative.json`, `worst_case.json`; manifest refers to `selected_splits.json` (18 selected) | available, but **[AUTHOR TO CONFIRM]** how these relate to the 30 ordered combinations per case. The source `selected_splits.json` is not local |
| Dataset-build and feature code | `_AUDIT_WORKSPACE/*/signal_experiments/`: `datasets/build_canonical.py`, `preprocessing_scripts/07_map_sensor_blocks.py`, `15_build_npz.py`, `src/lib/ml/features.py` | available |
| Model configurations | hyperparameter-tuning configs (`protocol.yaml`, search spaces, candidate registries) and notebooks `signal-loro-*.ipynb` | available |
| Run outputs | 1,490 `predictions.json` (recording level), 1,482 `scores.json`, `run_info.json`, `permutation_test.json`, 1,122 `.pt` checkpoints, 360 `.joblib` feature-based models, summary reports | available |
| Kaggle output bundles | four zips in the working folder (about 1.7 GB) | available |

**Not available locally:**

- Raw PASCO CSVs and canonical CSVs. The manifest's `canonical_root` points to another machine.
- The IT-01 to IT-06 deliverables and the `evidence/` folder (`DATASET_REGISTRY_FINAL.csv`, `SENSOR_CHANNEL_MAP.csv`, `FEATURE_DEFINITION.csv`, `CHANNEL_SYNCHRONISATION_NOTE.md`, `MODEL_OUTPUT_AND_SELECTION.md`, `METRIC_AGGREGATION_CHECK.csv`).

**Public repository or DOI:** none found. The code repositories referenced in the notebooks (`github.com/civiltwin/signal_experiments`, cloned with an access token; `github.com/vinhveer/sensor_signal_analyzer`) are not evidence of public availability. The Data Availability statement is therefore kept unchanged.

**Recommendation.** This is not created automatically. Before or at submission, consider depositing a versioned package (Zenodo, Mendeley Data or an institutional repository) with a DOI, containing:

1. The acquisition registry and sensor-channel map (IT-01/IT-02 deliverables).
2. The canonical CSVs or the NPZ windows with their manifest.
3. Run and split definitions.
4. The feature definition and extractor.
5. Model configurations.
6. Recording-level predictions and scores.
7. The evaluation and aggregation scripts.
8. The IT audit evidence.

Scrub access-token cells from the notebooks before release. Then replace the statement with "The data and code supporting this study are openly available in [repository] at [DOI]." This would also move risk B8 from AUTHOR ACTION to CLOSED.

## 6. Optional analysis: recommendation only

The current paper contains **no** cross-campaign RF/SVM results, and none exist in the archive.

**Potential high-ROI optional analysis:** CP2 ↔ CP3 cross-campaign transfer using the untuned RF and SVM, under the same recording-level evaluation logic (source-campaign training and validation runs, whole target campaign as test, the same selection rule and permutation reference).

**Reason:** these models carry no deep-model hyperparameter-development dependence. Their transfer scores would therefore separate "campaign shift" from "selection dependence" in the transfer boundary (B4) better than the deep models can.

**Status:** **NOT executed.** No approved cross-campaign script for RF/SVM was found in the archive, and no rerun was authorised. **[AUTHOR ACTION: decide whether to authorise this analysis; if run, it must be reported as an addition, and Table 3 and Table 7 would change]**

## 7. Scientific blockers

**None found.**

- The claims are bounded by the evidence.
- The Figure 3 contradiction is removed.
- Every number and table is unchanged from the IT-verified v8.
- The protected limitations are intact.
- The new references are used only for claims their abstracts support.

## 8. Verdict

### READY AFTER AUTHOR METADATA / FIGURE FIXES

The manuscript is scientifically ready. The following items remain, all of them author-side or file-side rather than scientific:

1. **[AUTHOR TO CONFIRM]** author names, affiliation and department, corresponding e-mail and ORCID.
2. **[AUTHOR TO CONFIRM]** funding and conflict-of-interest statements.
3. **[AUTHOR TO CONFIRM]** the AI-disclosure completeness points (i)–(iv) in §4.
4. **[AUTHOR ACTION]** approve the redrawn Figure 3, or replace it with a corrected source diagram.
5. **[AUTHOR ACTION]** Figure 2(b): supply a true B1 photograph if one exists (possibly the panel-(e) photo), and confirm the panel-(e) description.
6. **[AUTHOR ACTION]** upload original-resolution photographs for Figures 1(b–c), 2(d) and 2(e).
7. **[AUTHOR ACTION]** decide on data and code deposit, then update the Data availability statement.

Item 7 is not a SAGE requirement: a justified "on request" statement is accepted.
