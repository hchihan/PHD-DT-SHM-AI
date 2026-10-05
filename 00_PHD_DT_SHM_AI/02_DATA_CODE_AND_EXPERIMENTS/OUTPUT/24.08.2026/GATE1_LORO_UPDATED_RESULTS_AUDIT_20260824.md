# Gate 1 Updated LORO Results Audit

**Audit date:** 2026-08-24
**Auditor role:** independent scientific auditor (adversarial, not result-defending)
**Audited delivery:** `OUTPUT_18.08.2026/Output_added_24.08.2026/`
**Scope of this document:** RQ1 / WP1 / Chapter 4 / Paper 1 / Evidence Gate 1
**Evidence hierarchy applied:** source code + `run_info.json` + `scores.json` + raw `predictions.json` **over** narrative README/Note text.

---

## Executive Verdict

**GATE 1 VERDICT: PARTIALLY CLOSED.**

The *evaluation machinery* required by Gate 1 is now genuinely in place and is verifiable from code and raw artefacts: run-grouped LORO splitting, leakage-safe preprocessing, recording-level metrics, per-run predictions with probabilities, seed/split/model-version provenance, and a cross-campaign protocol. That is a real advance over the previous state.

What is **not** closed is the *dataset-integrity half of the gate*. The delivered folder contains **no canonical dataset tree and no registry files** (`campaigns.csv`, `runs.csv`, `recordings.csv`, `manifest.json` are all absent). Every experiment points at an external Kaggle path (`/kaggle/input/datasets/platformciviltwin/signal-dataset-v1/v1/...`) that is not part of this delivery. Consequently:

* The CP2_21 vs CP2_2122 question **cannot be resolved from the audited artefacts**. Every result folder refers only to `cp2_s123`. No output file anywhere records session date, source CSV, or a `borrowed` flag. The claim in `Note.md` is plausible and internally coherent, but it is **not independently verified here**.
* The chain "aggregate metric → prediction → recording → source raw file → measurement session" **breaks at the recording-ID level**. Recording IDs are anonymised (`R12:REC0001`), and the mapping back to raw CSV/session is not in the delivery.

Three substantive scientific findings emerged, two of them negative and important:

1. **Within-campaign, run-aware discrimination is repeatable for CP1 and CP2** (recording-level macro-F1 0.94–1.00 across all 30 held-out-run folds, several independent pipelines agreeing), **but not for CP3** (0.37–0.86 depending on model, with large fold-to-fold spread).
2. **Cross-campaign transfer collapses to at-or-below chance** (macro-F1 0.11–0.23; balanced accuracy 0.18–0.36 against a 0.25 chance level) with explicit **class collapse** — one CP2→CP3 ResNet1D configuration predicts `B1` for 377 of 432 recordings and never predicts `Healthy` or `B3`. This is a campaign/session-dependence and domain-shift result, **not** a "damage detection failure".
3. **The hypothesis "sensor configuration influences classification reliability more strongly than model architecture" is NOT supported by these results.** The observed effect ordering is: **campaign/session effect ≫ model/pipeline effect > held-out-run effect > sensor-configuration effect.**

Five blocking issues are listed in §19. The single most important one is that the canonical dataset and its registry were not delivered with the results.

---

## 1. Research Alignment

### RQ
> How reliably can vibration data from the 1:10 steel frame model and different sensor configurations produce evidence distinguishing controlled connection states under a run-aware, leakage-controlled evaluation protocol?

This audit addresses the *reliability* and *leakage-control* clauses directly, and the *sensor configuration* clause partially (S1/S2/S3 as recorded channel groups, not as verified physical positions).

### WP
WP1 — Laboratory vibration evidence.

### Chapter
Chapter 4.

### Paper
Paper 1.

### Evidence Gate
Evidence Gate 1 — Dataset integrity and run-aware evaluation.

### Scope boundaries

Layer processed in this audit:

```text
Vibration data → laboratory condition evidence
```

**Explicitly out of scope and not claimed anywhere below:** field damage diagnosis, lab-to-field classifier transfer, RUL, predictive maintenance, severity/DSI, calibrated FEM, stiffness-degradation inference, bolt-preload inference, "optimal sensor placement", "best AI model" in any general sense, autonomous maintenance, or a composite Health Index.

The four classes `Healthy / B1 / B2 / B3` are treated throughout as **controlled connection states of a laboratory specimen**, never as diagnosed damage.

---

## 2. Source and Experiment Inventory

### 2.1 Delivered top level

```text
Output_added_24.08.2026/
├── Note.md                      (1 816 B)  CP2_21 vs CP2_2122 narrative
├── Readme.md                    (3 590 B)  requirement list (the file named "Readme(3).md" in the brief)
├── signal_loro_v1/              intra-campaign LORO, deep models
├── loro-each-sensor-v1/         intra-campaign LORO, sensor ablation
├── ml_loro_v1/                  intra-campaign LORO, classical ML
└── loro-cross-campaign-v1/      cross-campaign transfer
```

Each of the four result folders also ships a full copy of the `signal_experiments` source repository. The leakage-critical module `src/lib/npz/data.py` is **byte-identical** between the `signal_loro_v1` and `loro-cross-campaign-v1` copies (verified by `diff`); `src/lib/npz/loro.py` differs only in progress-logging code, not in split generation.

### 2.2 Table B — Experiment matrix

| Folder | Experiment objective | Dataset root (per `run_info.json`) | CP | Sensors (channels) | Models | Split protocol | Seeds | Primary outputs |
|---|---|---|---|---|---|---|---|---|
| `signal_loro_v1/` | Intra-campaign repeatability of deep models under run-aware LORO | `.../signal-dataset-v1/v1/cp{1,2,3}_s*` | CP1, CP2, CP3 | cp1_s12 (8 ch), cp2_s123 (12 ch), cp3_s123 (12 ch) | `1dcnn` (Conv1DClassifier), `resnet1D` (ResNet1D) | 30 unique LORO splits: 4 train runs / 1 val run / 1 test run | 42 only | 6 experiments × 30 splits × {scores, predictions, run_info, history, confusion PNG, .pt} + `summary/` |
| `loro-each-sensor-v1/` | Effect of sensor subset on intra-campaign reliability | `.../v1/cp{1,2,3}_s<subset>` | CP1, CP2, CP3 | CP1: s1, s2, s12 (4/4/8 ch); CP2 & CP3: s1, s2, s3, s12, s13, s23, s123 (4/4/4/8/8/8/12 ch) | `resnet1D` only | same 30-split LORO | 42 only | 17 configurations × 30 splits + `summary/` |
| `ml_loro_v1/` | Classical feature-based baselines under the identical LORO protocol | `.../v1/cp{1,2,3}_s*` | CP1, CP2, CP3 | cp1_s12 (8 ch), cp2_s123 (12 ch), cp3_s123 (12 ch) | `random_forest`, `extra_trees`, `hist_gradient_boosting`, `svm_rbf` | same 30-split LORO | 42 only | 12 combinations × 30 splits (+ `.joblib` model) + `summary/` |
| `loro-cross-campaign-v1/` | Transportability of a campaign-trained model to a different campaign | train/val root = one campaign, test root = the other | CP2↔CP3 | s123 (12 ch) both sides | `1dcnn`, `resnet1D` | `--train-val-loro`: 5 train runs / 1 val run, **fixed external test = all 6 runs of the other campaign** | 42 only | 4 experiments × 6 splits + `summary/` |

**Total distinct trained-and-evaluated runs audited: 1 044** (180 + 510 + 360 + 24, with 30/30 or 6/6 present in every experiment — no run is missing, so there is no survivorship bias in the reported means).

### 2.3 Model / configuration identity (taken from `run_info.json`, not from the notebook)

| Experiment family | Model | git version tag | lr | weight decay | batch | epochs | model config |
|---|---|---|---|---|---|---|---|
| `signal_loro_v1` CP1 1dcnn | `1dcnn` | `1dcnn-75d5c1e` | 3e-4 | 1e-2 | 64 | 80 | fc_dim 64, dropout 0.5 |
| `signal_loro_v1` CP2 resnet | `resnet1D` | `resnet1D-75d5c1e` | — | — | 64 | 80 | n_feature_maps 16 |
| `loro-each-sensor-v1` | `resnet1D` | `resnet1D-843fbf2` | 3e-4 | 3e-2 | 64 | 100 | n_feature_maps 16 |
| `loro-cross-campaign-v1` | `1dcnn` / `resnet1D` | `*-06dfe3b` | 3e-4 | 3e-2 | 64 | 100 | fc_dim 64, dropout 0.5 / n_feature_maps 16 |
| `ml_loro_v1` | 4 sklearn models | `*-536c3a4` | n/a | n/a | n/a | 1 fit | 366 features (12 ch), `time_frequency_v1`, n_bands 12 |

> **Discrepancy recorded.** `signal_loro_v1/signal_experiments/notebook/signal-loro-v1.ipynb` states `--learning-rate 8e-4` (CP1/CP2) and `6e-4` (CP3). The `run_info.json` written by the actual runs records `learning_rate: 0.0003` throughout. Per the evidence hierarchy, **`run_info.json` is authoritative and the notebook does not correspond to the delivered results.** The notebook should not be cited in Paper 1 as the run specification.

---

## 3. Dataset and Run Registry Audit

### 3.1 Table A — Dataset audit

| Requirement (from `Readme.md`) | Present in delivery? | Evidence | Problem |
|---|---|---|---|
| `dataset/canonical/campaigns/CP*/RUN*/REC*.csv` | **No** | No `dataset/`, `canonical/`, `campaigns/` directory anywhere under `Output_added_24.08.2026/` | Canonical file layout cannot be verified |
| `registry/campaigns.csv` | **No** | Exhaustive filename scan of all four folders returns no such file | Campaign metadata unverifiable |
| `registry/runs.csv` | **No** | idem | Run metadata unverifiable |
| `registry/recordings.csv` | **No** | idem | Recording → source-file → session mapping unverifiable |
| `registry/manifest.json` | **Not delivered** | Referenced by every run as `/kaggle/input/datasets/platformciviltwin/signal-dataset-v1/v1/manifest.json`; file itself absent from the delivery | `class_map`, `windows_per_recording` unverifiable |
| `processed/{full_duration,middle_40s,model_npz}` | **No** | Absent | Preprocessing lineage unverifiable |
| `experiments/{intra_campaign,cross_campaign,sensor_ablation}` | **Partially, by convention** | The four result folders correspond to these three roles, but not under the prescribed path names | Naming does not follow the agreed canonical structure |
| Campaign ID | **Yes, implicitly** | Run-ID blocks 1–6 = CP1, 7–12 = CP2, 13–18 = CP3, consistent across all 1 044 runs (`run_info.json → split.train/val/test_run_ids`) | Encoded in run IDs, not in an explicit campaign field |
| Run ID | **Yes** | `R{n}.npz` files; `data.py:47` raises if `R{n}.npz` contains any other run ID | Verified, enforced in code |
| Recording ID | **Yes, but anonymised** | `predictions.json → recording_id = ["R12:REC0001", …]` | No mapping back to raw CSV filename |
| Class / state | **Yes** | `classes: ["Healthy","B1","B2","B3"]` in every `run_info.json`; `data.py:21-33` enforces exactly `{B1,B2,B3,HEALTHY}` and labels 0–3 | Verified |
| Excitation (BEAT_L1 / BEAT_L2 / WN) | **No** | Not present in any output file | Cannot stratify or report by excitation type |
| Sensor | **Partially** | Only via dataset-root suffix (`_s1`, `_s12`, `_s123`) and channel count | Physical sensor position (AP/BCJ/BR or equivalent) not recoverable |
| Source file | **No** | Absent | Blocks full provenance chain |
| Session / date | **No** | Absent | Blocks CP2 verification and session-confounding audit |
| Borrowed status | **No** | Absent | The `borrowed=yes` flag described in `Note.md` appears in no delivered artefact |
| Uniqueness | **Enforced in code** | `data.py:52-55` prefixes every recording with its run (`f"R{run}:{name}"`) then `np.unique`, so a recording cannot be double-counted or collide across runs | Verified |
| Missing recordings | **None detected** | Every held-out test run yields exactly 12 recordings; every 30-fold experiment pools to exactly 360 recording decisions | Verified |
| Duplicate recordings | **None detected** | idem; also `data.py:44-46` enforces equal array lengths across `X/y/recording_id/run_id` | Verified |
| Label consistency | **Enforced in code** | `evaluation.py:50-51` raises `ValueError` if any recording carries conflicting window labels | Verified — never triggered |
| Run boundaries | **Enforced in code** | `data.py:47-48` rejects an NPZ whose `run_id` set ≠ `{run}` | Verified |

### 3.2 Derived dataset shape (from artefacts, not from narrative)

| Quantity | Value | Source |
|---|---|---|
| Runs per campaign | 6 | `--loro 1,2,3,4,5,6` / `7…12` / `13…18` and split IDs |
| Recordings per run | 12 | `predictions.json` for any single-run test split (12 entries) |
| Recordings per campaign | 72 | 6 × 12; matches the 72-file total stated in `Note.md` |
| Recordings per class per run | 3 | `true = [0,0,0,1,1,1,2,2,2,3,3,3]` in `predictions.json` |
| Recordings per class per campaign | 18 | 6 × 3; matches `Note.md` |
| Window length | 400 samples | `run_info.json → config.data.window` |
| Channels per sensor | **4** | `cp2_s1` = 4 ch, `cp*_s12` = 8 ch, `cp*_s123` = 12 ch |
| Windows per recording | **Not recorded** | `run_info.json → config.data.windows_per_recording = null` |

The *counts* in `Note.md` (72 recordings, 18 per class, 4 classes) are therefore **corroborated**. The *provenance claims* in `Note.md` (which session each class came from, and the `borrowed` flag) are **not**.

---

## 4. CP2_21 vs CP2_2122 Decision

### 4.1 What `Note.md` asserts

* `cp2_21` = all CSVs from `cp2/thinghiem_210726_PASCO/` — all four classes from the 21/07 session, 18 files/class, 72 total, `borrowed = no`.
* `cp2_2122` = Healthy/B1/B2 from the 22/07 session (53 files + 1 recovered file `BS1B1L1R12_bo_sung_file_thieu_dot_2.csv` = 54) **plus** 18 B3 files borrowed from 21/07, flagged `borrowed = yes`; also 72 total, 18 per class.
* Risk explicitly acknowledged: in `cp2_2122`, the whole of class B3 comes from a different measurement day than Healthy/B1/B2.

### 4.2 What the delivered evidence can and cannot confirm

| Assertion | Verified? | Evidence / obstruction |
|---|---|---|
| 72 recordings, 18 per class, 4 classes for the CP2 branch actually used | **Yes** | 6 runs × 12 recordings; `true` label vector in `predictions.json` |
| `cp2_21` and `cp2_2122` are distinguished by a `campaign` column in `07b_campaign_manifest.csv` | **Not verifiable** | Neither the manifest nor `07b_resolve_campaigns.py` nor `13_export_sensor_signal_analyzer.py` is present in this delivery (the paths in `Note.md` are absolute paths on a different machine) |
| B3 in `cp2_2122` carries `borrowed = yes` | **Not verifiable** | No `borrowed` field exists in any delivered artefact |
| **Which CP2 branch the delivered results used** | **Not verifiable** | Every run points at `.../v1/cp2_s123`; the folder name carries no `_21` / `_2122` marker and no output records a session date |

`Readme.md` states, in the section on the sensor/ML re-runs, "*Chạy lại trên bộ dữ liệu đã bỏ bớt 1 nhánh CP2*" ("re-run on the dataset with one CP2 branch removed"). This is consistent with there now being a single CP2 branch in `signal-dataset-v1/v1`, but **it does not say which branch survived**, and nothing in the outputs resolves it.

### 4.3 Verdict

```text
PRIMARY CANONICAL CP2      = CP2_21   (all four classes recorded in the 21/07 session)
SECONDARY / SENSITIVITY CP2 = CP2_2122 (Healthy/B1/B2 from 22/07 + B3 borrowed from 21/07)
```

**Basis for this verdict — scientific, not performance-based.** In `cp2_2122`, class membership for B3 is perfectly aligned with measurement session. Under RQ1's own wording ("evidence distinguishing *controlled connection states*"), any classifier trained on `cp2_2122` can achieve the correct answer by learning the 21/07-vs-22/07 acquisition signature instead of the connection state, and no run-aware split can break that confound because the confound is at the **class** level, not the run level. LORO controls run-level leakage; it is structurally incapable of controlling a class-aligned session confound. `cp2_21` has no such alignment and is therefore the only CP2 branch that can support a state-discrimination claim.

`cp2_2122` retains value **only** as a sensitivity/robustness analysis — specifically as a deliberate positive control for session confounding — and any result from it must be labelled as such.

**Selection was not influenced by accuracy.** No comparison of `cp2_21` vs `cp2_2122` accuracy exists in this delivery, so no such influence was possible; equally, no such comparison can be reported.

**Required action before Paper 1:** state in `recordings.csv` (or equivalent) the session date and `borrowed` flag for every CP2 recording, and record in `manifest.json` / `run_info.json` which CP2 branch a given `cp2_s*` NPZ set was built from. Until then, the CP2 results below are reported as "CP2 as delivered", branch unidentified.

---

## 5. Leakage-Safe Protocol Audit

This audit was performed on the source code, independently of the folder name "LORO".

### 5.1 Split construction (verified)

`src/lib/npz/loro.py:58-89` generates splits as `combinations(run_ids, 4)` × `permutations(held_out, 2)` = **15 × 2 = 30 unique splits**, each with 4 training runs, 1 validation run, 1 test run, all disjoint. Each run serves as the test run in exactly 5 splits. The 30 `split_*` directories present in every deep/ML experiment match this exactly.

`src/lib/npz/loro.py:92-122` generates the cross-campaign `--train-val-loro` variant: 6 splits of 5 train runs / 1 validation run within the source campaign, with a **fixed external test set** (`--test-run-ids`) pointing at the other campaign. This matches the requirement `--train-run-ids 7,8,9,10,11 --val-run-ids 12` — that exact permutation is `train_val_split_01_train7-8-9-10-11_val12`, and the other five permutations were run as well.

`src/lib/npz/data.py:103-104` hard-fails if train/validation/test run IDs are not pairwise disjoint.

### 5.2 Table H (part 1) — Leakage audit

| # | Check | Verdict | Evidence |
|---|---|---|---|
| 1 | Split before or after segmentation? | **PASS** | Windows are pre-segmented **per run** into `R{n}.npz`. `data.py:36-48` loads only the NPZ files named by the split's run list. A window cannot enter a split whose run it does not belong to. |
| 2 | Where is the scaler/normaliser fitted? | **PASS** | `data.py:61` — `(values - values.mean(2)) / (values.std(2) + 1e-8)`, i.e. **per-window, per-channel instance normalisation**. No statistic is estimated on any pooled set, so there is nothing to fit on train and leak to test. For `svm_rbf`, `StandardScaler` lives inside an sklearn `Pipeline` (`ml/models.py:48-58`), so `.fit()` touches training features only. |
| 3 | Where is feature selection fitted? | **PASS** | No feature selection anywhere. `ml/features.py` computes a fixed deterministic 366-feature vector per window (`ml/training.py:30-33` applies the same function separately to train, validation and test). |
| 4 | Where is augmentation fitted/applied? | **PASS (vacuously)** | No augmentation is implemented in any audited path. |
| 5 | Do windows from the same recording appear in both train and test? | **PASS** | Impossible by construction: a recording lives in exactly one run's NPZ, and run sets are disjoint. |
| 6 | Do windows from the same run leak into test? | **PASS** | `data.py:47-48` raises if `R{n}.npz` contains any foreign `run_id`; splits are disjoint by `data.py:103-104`. |
| 7 | Does campaign metadata or the filename encode the class? | **PASS WITH LIMITATION** | The model sees only `X` tensors; labels come from `y`. However, recording IDs are ordered `REC0001–REC0012` **in class order** (`true = [0,0,0,1,1,1,2,2,2,3,3,3]`). That ordering is not exposed to the model, but it means recording IDs are not class-blind — a hazard for any future analysis that touches IDs. |
| 8 | Session-label confounding in `cp2_2122`? | **NOT VERIFIABLE** | No session/date/borrowed field exists in the delivery. The risk described in `Note.md` is real and structurally uncontrollable by LORO (§4.3), but it cannot be measured from these artefacts. |
| 9 | Is sensor channel ordering consistent? | **PASS WITH LIMITATION** | Channel count scales exactly 4 per sensor (`s1`=4, `s12`=8, `s123`=12) and `ml/features.py` names channels `ch1…ch12` positionally. Within one dataset root the ordering is necessarily fixed. **Across** campaigns (CP2 vs CP3, the cross-campaign case) nothing in the artefacts proves that channel *k* is the same physical sensor/axis in both. This is a candidate explanation for §9. |
| 10 | Are class labels mapped identically across campaigns? | **PASS** | `data.py:21-33` derives the class order from `class_map`/`label_map` in the shared `manifest.json` and rejects anything other than `{B1,B2,B3,HEALTHY}` with labels 0–3. All 1 044 runs record the same `classes: ["Healthy","B1","B2","B3"]`. Since a single manifest serves all campaigns, mapping is identical by construction. |

### 5.3 Model-selection hygiene

* **Deep pipeline:** checkpoint selection uses validation loss on the held-out **validation run**, with the extra condition `val_balanced_accuracy > chance` (`training.py:153`). The test run is never touched during training or selection. **PASS.**
* **Failure-mode note:** if no epoch beats chance on the validation run, `training.py:173-183` raises and the run produces no artefacts. Such a run would vanish silently from the aggregate. **In this delivery it never happened** — all 30/30 (and 6/6) splits are present in every experiment — so the reported means are complete. This should nevertheless be recorded as a known bias mechanism.
* **Classical ML pipeline:** the model is fitted once on the training runs; validation metrics are computed and stored but **never used for selection** (`ml/training.py:42-49, 63`). This is cleaner than the deep path (no selection at all), and it makes the ML numbers slightly more conservative rather than less.

---

## 6. Intra-Campaign LORO Results

All metrics below are **recording-level**: the softmax probabilities of every window of a recording are averaged, then `argmax` is taken (`evaluation.py:47-54` for deep models, `ml/evaluation.py:26-37` for classical models — identical rule). Every fold's test set is one held-out run = **12 recordings** (3 per class). `mean ± SD` is over the 30 LORO folds, single seed 42.

### 6.1 Table C — Primary recording-level LORO results (deep models)

| Campaign | Model | Macro-F1 | Balanced Acc. | Accuracy | ROC-AUC (macro) | min F1 | max F1 | folds at F1 = 1.000 |
|---|---|---|---|---|---|---|---|---|
| CP1 (s12, 8 ch) | `1dcnn` | 0.5999 ± 0.1105 | 0.6306 ± 0.0867 | 0.6306 ± 0.0867 | 0.8910 ± 0.0322 | 0.4125 | 0.8375 | 0 / 30 |
| CP1 (s12, 8 ch) | `resnet1D` | **0.9400 ± 0.0400** | 0.9417 ± 0.0388 | 0.9417 ± 0.0388 | 0.9991 ± 0.0037 | 0.9143 | 1.0000 | 9 / 30 |
| CP2 (s123, 12 ch) | `1dcnn` | 0.6432 ± 0.1328 | 0.6583 ± 0.1355 | 0.6583 ± 0.1355 | 0.8840 ± 0.0635 | 0.4111 | 0.8375 | 0 / 30 |
| CP2 (s123, 12 ch) | `resnet1D` | **0.9547 ± 0.0618** | 0.9556 ± 0.0609 | 0.9556 ± 0.0609 | 0.9997 ± 0.0017 | 0.8286 | 1.0000 | 18 / 30 |
| CP3 (s123, 12 ch) | `1dcnn` | 0.3639 ± 0.1086 | 0.4306 ± 0.1074 | 0.4306 ± 0.1074 | 0.7343 ± 0.0806 | 0.1705 | 0.6583 | 0 / 30 |
| CP3 (s123, 12 ch) | `resnet1D` | 0.5334 ± 0.1816 | 0.5694 ± 0.1738 | 0.5694 ± 0.1738 | 0.8108 ± 0.1272 | 0.1964 | 0.8375 | 0 / 30 |

Source: `signal_loro_v1/<experiment>/summary/summary.csv`, row `aggregate_over = "seed+split"`.

### 6.2 Per-held-out-run breakdown (macro-F1, mean of the 5 folds that hold out that run)

| Held-out test run | CP1 `resnet1D` | CP2 `resnet1D` | CP2 `1dcnn` | CP3 `resnet1D` |
|---|---|---|---|---|
| R1 / R7 / R13 | 0.931 | 0.983 | 0.786 | 0.691 |
| R2 / R8 / R14 | 0.931 | 0.966 | 0.610 | **0.739 (best)** |
| R3 / R9 / R15 | 0.949 | 1.000 | **0.458 (worst)** | 0.498 |
| R4 / R10 / R16 | 0.949 | 1.000 | 0.656 | **0.323 (worst)** |
| R5 / R11 / R17 | **0.966 (best)** | **0.880 (worst)** | 0.758 | 0.556 |
| R6 / R12 / R18 | **0.914 (worst)** | 0.899 | 0.591 | 0.393 |

Two things follow. For CP1 and CP2 with `resnet1D` the **floor** across every held-out run is high (0.914 and 0.880), so the mean is not carried by a few lucky folds. For CP3, the spread is 0.323–0.739 — a factor of more than two — so the CP3 mean is **not** a safe summary statistic and must always be reported with its worst fold.

### 6.3 Reproducibility cross-check across independent runs

`cp2_s123` with `resnet1D` was trained twice, under two different git commits and two different hyper-parameter settings (`75d5c1e`, wd 1e-2, 80 epochs, in `signal_loro_v1`; `843fbf2`, wd 3e-2, 100 epochs, in `loro-each-sensor-v1`):

| Source | Macro-F1 | Balanced Acc. |
|---|---|---|
| `signal_loro_v1/cp2_s123_resnet1d_batch64_v3` | 0.9547 ± 0.0618 | 0.9556 ± 0.0609 |
| `loro-each-sensor-v1/.../cp2/cp2_s123` | 0.9575 ± 0.0576 | 0.9583 ± 0.0569 |

Agreement to 0.003 macro-F1 across independent code versions and hyper-parameters. Same check for CP1 `resnet1D`: 0.9400 vs 0.9429 (`cp1_s12`). This is the strongest internal reproducibility evidence in the delivery and is worth reporting in Paper 1.

---

## 7. Sensor-Specific LORO Results

Model held fixed at `resnet1D` (`resnet1D-843fbf2`), 30 LORO folds each, seed 42. CP1 has **two** sensors, CP2 and CP3 have **three**.

### 7.1 Sensor identity — mapping status

**Evidence is currently insufficient to map S1/S2/S3 to physical positions.** The audited artefacts record only the dataset-root suffix (`_s1`, `_s2`, `_s3`, `_s12`, …) and the resulting channel count (4 per sensor). No AP/BCJ/BR or equivalent label appears in any code, manifest or output file in this delivery. All statements below are therefore about **recorded channel groups**, not about instrumented locations, and Paper 1 must not name positions until the registry supplies the mapping.

### 7.2 Table D — Per-sensor comparison (recording-level macro-F1)

| CP | Config | Channels | Macro-F1 (mean ± SD) | Balanced Acc. | min fold | max fold | Worst held-out run (its mean F1) | folds at F1 = 1.000 |
|---|---|---|---|---|---|---|---|---|
| CP1 | s12 | 8 | **0.9429 ± 0.0520** | 0.9444 ± 0.0505 | 0.829 | 1.000 | R1 (0.914) | 12 / 30 |
| CP1 | s1 | 4 | 0.9316 ± 0.0520 | 0.9333 ± 0.0509 | 0.829 | 1.000 | R2 (0.864) | 9 / 30 |
| CP1 | s2 | 4 | 0.8150 ± 0.0596 | 0.8111 ± 0.0654 | 0.748 | 0.914 | R5 (0.769) | 0 / 30 |
| CP2 | s13 | 8 | **0.9657 ± 0.0427** | 0.9667 ± 0.0415 | 0.914 | 1.000 | R11 (0.914) | 18 / 30 |
| CP2 | s123 | 12 | 0.9575 ± 0.0576 | 0.9583 ± 0.0569 | 0.829 | 1.000 | R11 (0.897) | 18 / 30 |
| CP2 | s12 | 8 | 0.9346 ± 0.0764 | 0.9361 ± 0.0748 | 0.731 | 1.000 | R12 (0.883) | 14 / 30 |
| CP2 | s23 | 8 | 0.9270 ± 0.0585 | 0.9306 ± 0.0540 | 0.812 | 1.000 | R9 (0.911) | 9 / 30 |
| CP2 | s1 | 4 | 0.9254 ± 0.0681 | 0.9278 ± 0.0647 | 0.720 | 1.000 | R11 (0.875) | 10 / 30 |
| CP2 | s2 | 4 | 0.9021 ± 0.0741 | 0.9056 ± 0.0717 | 0.748 | 1.000 | R8 (0.860) | 7 / 30 |
| CP2 | s3 | 4 | 0.8957 ± 0.0595 | 0.9000 ± 0.0554 | 0.732 | 1.000 | R12 (0.861) | 3 / 30 |
| CP3 | s123 | 12 | **0.5384 ± 0.1763** | 0.5722 ± 0.1677 | 0.196 | 0.838 | R16 (0.350) | 0 / 30 |
| CP3 | s13 | 8 | 0.5277 ± 0.1646 | 0.5667 ± 0.1425 | 0.167 | 0.833 | R16 (0.306) | 0 / 30 |
| CP3 | s3 | 4 | 0.5129 ± 0.1478 | 0.5694 ± 0.1240 | 0.303 | 0.838 | R16 (0.361) | 0 / 30 |
| CP3 | s23 | 8 | 0.4713 ± 0.1492 | 0.5222 ± 0.1434 | 0.225 | 0.731 | R16 (0.327) | 0 / 30 |
| CP3 | s1 | 4 | 0.4280 ± 0.1196 | 0.4639 ± 0.1130 | 0.215 | 0.649 | R18 (0.373) | 0 / 30 |
| CP3 | s12 | 8 | 0.3925 ± 0.1983 | 0.4500 ± 0.1799 | 0.050 | 0.742 | R18 (0.226) | 0 / 30 |
| CP3 | s2 | 4 | 0.3723 ± 0.1511 | 0.4500 ± 0.1250 | 0.183 | 0.660 | R18 (0.239) | 0 / 30 |

### 7.3 Reading of the sensor evidence — robustness first, not maxima

* **Within a campaign the sensor effect is real but modest.** CP2 spans 0.896 (s3) to 0.966 (s13), i.e. **Δ ≈ 0.070 macro-F1** across all seven configurations. CP1 spans 0.815 (s2) to 0.943 (s12), **Δ ≈ 0.128**. CP3 spans 0.372 (s2) to 0.538 (s123), **Δ ≈ 0.166**, but CP3's fold-to-fold SD (0.12–0.20) is of the same order as the entire between-configuration spread, so the CP3 sensor ranking is **not separable from fold noise**.
* **Adding sensors is not monotonically better.** In CP2, `s13` (8 ch) slightly exceeds `s123` (12 ch); in CP3, `s12` (8 ch, 0.393) is worse than `s3` alone (4 ch, 0.513). More channels do not guarantee more reliable evidence.
* **Single-sensor configurations are not catastrophic in CP1/CP2.** `cp2_s1` alone reaches 0.925 ± 0.068 with a worst-run floor of 0.875. This is a genuinely useful finding for instrumentation planning — but it is *not* an "optimal sensor placement" claim, and must not be stated as one.
* **Configurations that look good on average but fail on some runs.** `cp2_s12` has a strong mean (0.935) but the lowest single-fold floor of the CP2 8-channel group (0.731). `cp3_s12` is the extreme case: mean 0.393 with a single fold at **0.050**, i.e. near-total collapse on one held-out run.
* **Which class is sensor-sensitive?** In CP2 the residual errors are few (16 recording errors in 360 for `s123`) and concentrated in `Healthy↔B1` and `B2↔B3`; in CP3 the errors are spread across every off-diagonal cell (§10), so no clean class-by-sensor interaction can be isolated at this sample size.

### 7.4 Test of the stated hypothesis

> *Hypothesis: Sensor configuration may influence classification reliability more strongly than model architecture.*

**Not supported by these results.** On the same campaign and the same sensor set (`cp2_s123`), changing the architecture moves macro-F1 from 0.6432 (`1dcnn`) to 0.9547 (`resnet1D`) to 0.9857 (all four classical ML models) — a spread of **Δ ≈ 0.34**. Changing the sensor configuration within CP2 while holding `resnet1D` fixed moves it by **Δ ≈ 0.07**. On CP3 the corresponding numbers are Δ ≈ 0.48 (model: `1dcnn` 0.364 → `random_forest` 0.846) versus Δ ≈ 0.17 (sensor). In both campaigns the model/pipeline effect is roughly **2× to 5× larger** than the sensor-configuration effect.

The observed effect ordering in this dataset is:

```text
campaign / session effect  ≫  model & pipeline effect  >  held-out-run effect  >  sensor configuration effect
```

---

## 8. Traditional ML LORO Results

Exact model names taken from `ml/models.py:10-15` and from `run_info.json → model_name`: **`random_forest`, `extra_trees`, `hist_gradient_boosting`, `svm_rbf`**. Features: `time_frequency_v1`, 12 bands, 366 features for 12 channels (10 time-domain + 12 band-power + 3 spectral per channel, plus all pairwise channel correlations). Same 30-fold LORO, same recording-level aggregation, seed 42.

### 8.1 Table E — ML model comparison

| CP | Model | Macro-F1 | Balanced Acc. | Accuracy | ROC-AUC | min fold | max fold | Worst held-out run | Best held-out run |
|---|---|---|---|---|---|---|---|---|---|
| CP1 s12 | `random_forest` | 1.0000 ± 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.000 | 1.000 | all 1.000 | all 1.000 |
| CP1 s12 | `extra_trees` | 1.0000 ± 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.000 | 1.000 | all 1.000 | all 1.000 |
| CP1 s12 | `svm_rbf` | 1.0000 ± 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.000 | 1.000 | all 1.000 | all 1.000 |
| CP1 s12 | `hist_gradient_boosting` | 0.9971 ± 0.0156 | 0.9972 | 0.9972 | 1.0000 | 0.914 | 1.000 | R3 (0.983) | R1 (1.000) |
| CP2 s123 | `random_forest` | 0.9857 ± 0.0325 | 0.9861 | 0.9861 | 1.0000 | 0.914 | 1.000 | **R12 (0.914)** | R7 (1.000) |
| CP2 s123 | `extra_trees` | 0.9857 ± 0.0325 | 0.9861 | 0.9861 | 1.0000 | 0.914 | 1.000 | **R12 (0.914)** | R7 (1.000) |
| CP2 s123 | `hist_gradient_boosting` | 0.9857 ± 0.0325 | 0.9861 | 0.9861 | 0.9960 | 0.914 | 1.000 | **R12 (0.914)** | R7 (1.000) |
| CP2 s123 | `svm_rbf` | 0.9857 ± 0.0325 | 0.9861 | 0.9861 | 1.0000 | 0.914 | 1.000 | **R12 (0.914)** | R7 (1.000) |
| CP3 s123 | `random_forest` | **0.8464 ± 0.1719** | 0.8611 | 0.8611 | 0.9420 | 0.475 | 1.000 | R16 (0.611) | R14 (1.000) |
| CP3 s123 | `extra_trees` | 0.8070 ± 0.2087 | 0.8333 | 0.8333 | 0.9435 | 0.375 | 1.000 | R16 (0.537) | R14 (1.000) |
| CP3 s123 | `hist_gradient_boosting` | 0.8052 ± 0.1699 | 0.8083 | 0.8083 | 0.9361 | 0.488 | 0.950 | R16 (0.571) | R14 (0.950) |
| CP3 s123 | `svm_rbf` | 0.6793 ± 0.1727 | 0.6889 | 0.6889 | 0.8778 | 0.375 | 1.000 | R16 (0.454) | R14 (0.898) |

### 8.2 The strongest run-effect evidence in the delivery

On CP2, **all four classical models make exactly 5 recording errors out of 360, and all five errors are `B1 → B2`, and all five occur in precisely the five folds whose test run is R12** (`train7-8-10-11_val9_test12`, `train7-8-9-10_val11_test12`, `train7-8-9-11_val10_test12`, `train7-9-10-11_val8_test12`, `train8-9-10-11_val7_test12`).

Four algorithmically unrelated classifiers — a bagged tree ensemble, a randomised tree ensemble, a boosted histogram model and an RBF-SVM — failing identically on the same held-out run is not model variance. It is a **run-level property of R12**: one specific `B1` recording in R12 is systematically read as `B2` regardless of the decision rule. This is exactly the kind of artefact that run-aware evaluation is supposed to expose, and it should be reported as a positive result of the protocol.

The same pattern appears in CP3: **R16 is the worst held-out run for all four ML models and for `resnet1D`**, and R14 is the best for all four ML models. The run effect is model-independent.

### 8.3 How to phrase model comparisons (and how not to)

**Permitted phrasing, supported by the data:**

> Under the evaluated campaigns, sensor configurations and 30-fold run-aware LORO protocol with a single seed, `random_forest` on 366 deterministic time–frequency features achieved the highest observed recording-level macro-F1 on CP3 (0.846 ± 0.172), and the four classical models were indistinguishable from one another on CP1 and CP2 (identical macro-F1 to four decimal places on CP2).

**Not permitted:** "Random Forest is the best model." Three reasons: (a) hyper-parameters were not tuned under a common budget — the deep models used a single fixed setting per campaign, whereas the classical models used library defaults with no tuning at all; (b) only one seed was run, so no estimate of model-initialisation variance exists; (c) on CP1 and CP2, three of the four classical models are tied at exactly 1.0000 / 0.9857, which is a ceiling, not a ranking.

### 8.4 Separating the four effect types

| Effect | Isolated by | Magnitude observed (macro-F1) |
|---|---|---|
| **Campaign / session** | Same model, same sensor set, different campaign | `resnet1D` s123: CP2 0.955 → CP3 0.533 → **Δ 0.42**. Cross-campaign: 0.955 → 0.147 → **Δ 0.81** |
| **Model / pipeline** | Same campaign, same sensors, different model | `cp2_s123`: 0.643 (`1dcnn`) → 0.955 (`resnet1D`) → 0.986 (ML) → **Δ 0.34** |
| **Run** | Same campaign, same model, different held-out run | CP3 `resnet1D`: 0.323 (R16) → 0.739 (R14) → **Δ 0.42**; CP2 `resnet1D`: 0.880 (R11) → 1.000 (R9/R10) → **Δ 0.12** |
| **Sensor configuration** | Same campaign, same model, different sensor subset | CP2 `resnet1D`: 0.896 (s3) → 0.966 (s13) → **Δ 0.07**; CP3: **Δ 0.17** but within fold-noise |

---

## 9. Cross-Campaign Results

Protocol as verified in code: train on 5 runs of the source campaign, select the checkpoint on 1 held-out validation run of the source campaign, test on **all 6 runs (72 recordings) of the target campaign**. Six validation permutations per direction per model, seed 42. Chance level for a balanced 4-class problem: accuracy = balanced accuracy = 0.25, macro-F1 ≈ 0.25, ROC-AUC = 0.50.

### 9.1 Table F — Cross-campaign generalization

| Train | Validation | Test | Sensor config | Model | Macro-F1 | Balanced Acc. | Accuracy | ROC-AUC |
|---|---|---|---|---|---|---|---|---|
| CP2 R7,8,9,10,11 | R12 | CP3 (R13–18) | s123 (12 ch) | `1dcnn` | 0.1990 | 0.3056 | 0.3056 | 0.5463 |
| CP2 R7,8,9,10,12 | R11 | CP3 | s123 | `1dcnn` | 0.1168 | 0.2361 | 0.2361 | 0.6613 |
| CP2 R7,8,9,11,12 | R10 | CP3 | s123 | `1dcnn` | 0.2427 | 0.3333 | 0.3333 | 0.6319 |
| CP2 R7,8,10,11,12 | R9 | CP3 | s123 | `1dcnn` | 0.1479 | 0.2222 | 0.2222 | 0.6245 |
| CP2 R7,9,10,11,12 | R8 | CP3 | s123 | `1dcnn` | 0.2439 | 0.3333 | 0.3333 | 0.5983 |
| CP2 R8,9,10,11,12 | R7 | CP3 | s123 | `1dcnn` | 0.2155 | 0.2917 | 0.2917 | 0.5972 |
| **CP2 → CP3, `1dcnn`, mean ± SD (n=6)** | | | | | **0.1943 ± 0.0518** | **0.2870 ± 0.0478** | 0.2870 ± 0.0478 | 0.6099 ± 0.0392 |
| **CP2 → CP3, `resnet1D`, mean ± SD (n=6)** | | | | | **0.1139 ± 0.0221** | **0.2315 ± 0.0190** | 0.2315 ± 0.0190 | 0.5051 ± 0.0275 |
| CP3 R13,14,15,16,17 | R18 | CP2 (R7–12) | s123 | `1dcnn` | 0.2288 | 0.3056 | 0.3056 | 0.6469 |
| CP3 R13,14,15,16,18 | R17 | CP2 | s123 | `1dcnn` | 0.2360 | 0.3056 | 0.3056 | 0.5795 |
| CP3 R13,14,15,17,18 | R16 | CP2 | s123 | `1dcnn` | 0.1702 | 0.2778 | 0.2778 | 0.5774 |
| CP3 R13,14,16,17,18 | R15 | CP2 | s123 | `1dcnn` | 0.1370 | 0.2500 | 0.2500 | 0.5802 |
| CP3 R13,15,16,17,18 | R14 | CP2 | s123 | `1dcnn` | 0.2804 | 0.3611 | 0.3611 | 0.6168 |
| CP3 R14,15,16,17,18 | R13 | CP2 | s123 | `1dcnn` | 0.3120 | 0.3056 | 0.3056 | 0.5224 |
| **CP3 → CP2, `1dcnn`, mean ± SD (n=6)** | | | | | **0.2274 ± 0.0656** | **0.3009 ± 0.0369** | 0.3009 ± 0.0369 | 0.5872 ± 0.0420 |
| **CP3 → CP2, `resnet1D`, mean ± SD (n=6)** | | | | | **0.1473 ± 0.0413** | **0.2153 ± 0.0349** | 0.2153 ± 0.0349 | 0.4931 ± 0.0687 |

### 9.2 Degradation relative to intra-campaign

| Comparison | Intra-campaign macro-F1 | Cross-campaign macro-F1 | Absolute drop |
|---|---|---|---|
| `resnet1D` s123, tested on CP3 | 0.5334 (trained on CP3) | 0.1139 (trained on CP2) | **−0.420** |
| `resnet1D` s123, tested on CP2 | 0.9547 (trained on CP2) | 0.1473 (trained on CP3) | **−0.807** |
| `1dcnn` s123, tested on CP3 | 0.3639 | 0.1943 | −0.170 |
| `1dcnn` s123, tested on CP2 | 0.6432 | 0.2274 | −0.416 |

### 9.3 Diagnosis of the sub-chance results — reported straight, not explained away

Balanced accuracy falls **below the 0.25 chance level** in 2 of 4 configurations (`resnet1D` CP2→CP3: 0.2315; `resnet1D` CP3→CP2: 0.2153). This is not noise; it is the signature of confident, systematically wrong prediction. The required diagnostic checks:

**Class collapse — CONFIRMED.** Pooled confusion matrices over all six splits (432 recording decisions each; rows = true, columns = predicted):

*CP2 → CP3, `resnet1D`:*

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 0 | 100 | 8 | 0 |
| B1 | 0 | 88 | 20 | 0 |
| B2 | 0 | 96 | 12 | 0 |
| B3 | 0 | 93 | 15 | 0 |

The model emits `B1` for 377/432 recordings and `B2` for the remaining 55. `Healthy` and `B3` are **never predicted**. Two of four classes are structurally unreachable.

*CP3 → CP2, `1dcnn`:*

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 26 | 16 | 6 | 60 |
| B1 | 28 | 15 | 5 | 60 |
| B2 | 17 | 27 | 6 | 58 |
| B3 | 10 | 13 | 2 | 83 |

Predictions concentrate on `B3` (261/432) and `Healthy` (81/432); `B2` is almost never predicted (19/432). The `B3` row is the only one with a majority-correct outcome (83/108), and it is correct only because the model defaults to `B3`.

**Label mapping — PASS.** A single shared `manifest.json` defines the class map for all campaigns; `data.py:21-33` rejects any deviation; all runs record the same class order. Mislabelling is ruled out as the cause.

**Preprocessing — PASS.** Identical `data.py` (byte-identical file) and identical per-window instance normalisation in both directions.

**Session confounding — NOT VERIFIABLE.** No session field exists (§3, §4).

**Sensor/channel ordering across campaigns — NOT VERIFIABLE and a live suspect.** Nothing in the artefacts proves that channel *k* of `cp2_s123` and channel *k* of `cp3_s123` are the same physical sensor and axis. Because both campaigns feed the same 12-channel input tensor, a permuted or re-mounted sensor set between campaigns would produce exactly this failure mode. **This is the cheapest hypothesis to test and it has not been tested.**

**Campaign-specific signatures — CONSISTENT WITH THE DATA.** The `1dcnn` retains ROC-AUC of 0.59–0.61 cross-campaign, meaningfully above the 0.50 chance line, while its balanced accuracy sits near 0.29. That combination means *some* rank-ordering information transfers, but the decision boundary and the implied class priors do not. That is the classic signature of covariate shift plus prior shift, not of an absent signal.

**Interpretation, stated within scope.** These results demonstrate **campaign/session dependence and limited transportability of a laboratory-trained classifier between measurement campaigns**. They say nothing about damage detection capability, and nothing whatsoever about field generalization — the test target is another laboratory campaign on the same specimen, not a structure in service.

---

## 10. Class-Level Error Analysis

### 10.1 Table G — Pooled class-wise confusion, intra-campaign (30 folds, 360 recording decisions each)

| Experiment | Errors / 360 | Dominant confusions |
|---|---|---|
| CP1 `resnet1D` s12 | 21 | `B2→B3` 13, `B3→B2` 7, `Healthy→B1` 1 |
| CP1 `1dcnn` s12 | 133 | `B2→B1` 26, `B2→B3` 26, `B1→B2` 17, `B1→Healthy` 14, `Healthy→B2` 13 |
| CP1 `random_forest` / `extra_trees` / `svm_rbf` | **0** | none |
| CP1 `hist_gradient_boosting` | 1 | `B3→B2` 1 |
| CP2 `resnet1D` s123 | 16 | `Healthy→B1` 5, `B3→B2` 5, `B1→B2` 4, `B1→Healthy` 1, `B2→B3` 1 |
| CP2 `1dcnn` s123 | 123 | `B1→Healthy` 44, `Healthy→B1` 24, `B1→B2` 17, `B2→B1` 10, `B2→Healthy` 9 |
| CP2 all four ML models | 5 each | `B1→B2` 5 (all in test-run-R12 folds) |
| CP3 `resnet1D` s123 | 155 | `B2→B1` 25, `Healthy→B2` 24, `B2→Healthy` 23, `Healthy→B1` 21, `B1→Healthy` 20, `B1→B2` 15 |
| CP3 `1dcnn` s123 | 205 | `B2→Healthy` 46, `B1→Healthy` 43, `B2→B1` 25, `Healthy→B1` 21, `B1→B3` 18 |
| CP3 `random_forest` s123 | 50 | `B1→Healthy` 31, `B2→Healthy` 11, `Healthy→B1` 4, `Healthy→B2` 4 |
| CP3 `extra_trees` s123 | 60 | `B1→Healthy` 37, `B2→Healthy` 17 |
| CP3 `hist_gradient_boosting` s123 | 69 | `B1→Healthy` 22, `Healthy→B1` 11, `Healthy→B2` 10, `B2→Healthy` 10 |
| CP3 `svm_rbf` s123 | 112 | `B1→Healthy` 24, `B2→Healthy` 15, `Healthy→B1` 14, `Healthy→B2` 12 |

### 10.2 What is consistent across pipelines

* **`Healthy ↔ B1` is the principal confusion axis.** It dominates CP2 `1dcnn` (68 of 123 errors in the two directions), CP3 `resnet1D` (41), and every CP3 ML model (`B1→Healthy` is the single largest error cell for all four: 31, 37, 22, 24). Where the protocol is hardest, the model's difficulty is distinguishing the *baseline state from the first perturbed state* — the physically expected difficulty, and the one that matters most for any downstream inspection trigger.
* **`B2 ↔ B3` is a secondary, CP1-specific axis.** It accounts for 20 of CP1 `resnet1D`'s 21 errors, and it barely appears in CP2 or CP3.
* **`B3` is the most separable class in CP1/CP2 intra-campaign** (2 `B3` errors in CP2 `resnet1D`, 1 in CP1 ML) — and, in the cross-campaign CP3→CP2 case, it becomes the collapse attractor. Separability within a campaign does not survive between campaigns.
* **CP3 `1dcnn` shows a `Healthy` over-prediction bias** (89 recordings of other classes pushed into `Healthy`). For any future inspection-support framing this is the dangerous direction of error, and it must be reported as such.

---

## 11. Variability Across Runs and Seeds

### 11.1 Across folds/runs — measured

Every table above reports `mean ± SD` over the 30 LORO folds (or 6 cross-campaign splits), and every one is accompanied by its min, max and worst held-out run. Key worst-case figures, which must travel with the means in Paper 1:

| Configuration | Mean macro-F1 | Worst single fold | Worst held-out run (5-fold mean) |
|---|---|---|---|
| CP1 `resnet1D` s12 | 0.9400 | 0.9143 | R6, 0.914 |
| CP2 `resnet1D` s123 | 0.9547 | 0.8286 | R11, 0.880 |
| CP2 `random_forest` s123 | 0.9857 | 0.9143 | R12, 0.914 |
| CP3 `random_forest` s123 | 0.8464 | 0.4750 | R16, 0.611 |
| CP3 `resnet1D` s123 | 0.5334 | 0.1964 | R16, 0.323 |
| CP3 `resnet1D` s12 | 0.3925 | **0.0500** | R18, 0.226 |
| CP2→CP3 `resnet1D` | 0.1139 | 0.0955 | n/a (fixed test) |

### 11.2 Across seeds — NOT measured

**Evidence is currently insufficient.** Every single run in this delivery uses `seed = 42`. `summary.csv` confirms this: every per-split row has `n_runs = 1` and a null `*_sd`, and the `aggregate_over = "seed+split"` row is numerically identical to the `aggregate_over = "split"` row, because there is only one seed to aggregate over.

The consequence is precise: **all reported SDs are fold-to-fold variability only. None of them contain model-initialisation, data-shuffling, or training-stochasticity variance.** The Gate 1 requirement "mean ± SD theo fold **và seed**" is therefore half-met. The aggregation code (`aggregate_runs.py:66-93`) and the launcher (`--seeds 42,43,44`) already support multiple seeds; only the runs are missing.

### 11.3 Indirect evidence that seed variance is small for the strong configurations

The two independent `cp2_s123` `resnet1D` runs (different git commit, different weight decay, different epoch budget — §6.3) agree to 0.003 macro-F1, and the two `cp1_s12` runs agree to 0.003. This suggests low run-to-run instability **where performance is high**. It says nothing about CP3 or about cross-campaign, where instability is precisely what is suspected.

---

## 12. Prediction Provenance and Reproducibility

Every completed run writes six artefacts (`ARCHITECTURE.md`, "Stable NPZ output contract"; implemented in `npz/artifacts.py:121-180` and `ml/artifacts.py`).

### 12.1 Table H (part 2) — Provenance audit

| Required provenance field | Present? | Location | Problem |
|---|---|---|---|
| Prediction (per recording) | **Yes** | `predictions.json → pred` | — |
| Score / probability | **Yes** | `predictions.json → probabilities` (per-class, post-aggregation) | Per-**window** probabilities are not stored; only the recording-level mean |
| True label | **Yes** | `predictions.json → true` | — |
| Recording ID | **Yes** | `predictions.json → recording_id` (`"R12:REC0001"`) | **Anonymised** — no mapping to source CSV or session |
| Run ID | **Yes** | `run_info.json / scores.json → split.{train,val,test}_run_ids`; also embedded in the recording ID prefix | — |
| Campaign | **Implicit only** | Inferable from run-ID block and from `dataset_root` path string | No explicit `campaign_id` field |
| Sensor configuration | **Implicit only** | `dataset_root` path suffix (`cp2_s123`) + `config.data.channels` | No explicit sensor list; no physical position mapping |
| Seed | **Yes** | `run_info.json`, `scores.json`, `predictions.json`, and the `ddp_seed42` / `ml_seed42` directory name | Single value only |
| Split | **Yes** | `split_id` (e.g. `train7-8-9-10_val11_test12`) plus the full `split` object with roots and manifest path | — |
| Model | **Yes** | `model_name` + `config.model` + full `args` dict | — |
| Model version | **Yes** | `version` = `<model>-<git short SHA>`, with `git_dirty` boolean (`artifacts.py:23-36, 76`) | All audited runs report `git_dirty: false` |
| Timestamp / config | **Yes** | `started_at`, `finished_at`, `best_epoch`, `epochs_ran`, complete optimiser block | — |
| Trained model object | **Yes** | `best_<dataset>_<model>.pt` / `model_<...>.joblib` in every run directory | — |
| Learning curve | **Yes** | `history.json` per epoch | — |
| Per-run confusion figure | **Yes** | `confusion_matrix.png` per run | — |
| Feature definition (ML) | **Yes** | `run_info.json → config.features.names` (366 named features) | — |
| Canonical registry linkage | **No** | — | **Blocks the final hop of the provenance chain** |

### 12.2 Traceability test — can a headline metric be traced back to individual predictions?

**Partially. The chain holds for four of five hops and breaks on the fifth.**

Worked example, CP2 `resnet1D`, headline macro-F1 0.9547:

1. `signal_loro_v1/cp2_s123_resnet1d_batch64_v3/summary/summary.csv`, row `aggregate_over = seed+split` → `f1_macro_mean = 0.954663`. ✔
2. `aggregate_runs.py:36-57` walks every `scores.json` under the tree; the 30 per-split rows in the same CSV each carry `split_id`. ✔
3. Split `train7-8-9-10_val11_test12` → `split_01_7-8-9-10-11-12/ddp_seed42/scores.json` → `f1_macro`, `confusion`, `seed`, `version`. ✔
4. Same directory → `predictions.json` → 12 recordings with `true`, `pred`, per-class probabilities, and `recording_id = R12:REC0001…REC0012`. ✔
5. `R12:REC0004` → *which physical recording, from which raw CSV, from which session?* → **no artefact in this delivery answers this.** ✘

I independently reproduced hop 1 from hops 2–4 for several experiments (e.g. re-summing the 30 per-split `confusion_sum` matrices reproduces the pooled confusion in `summary/pooled_confusion_*_counts.csv` exactly), so the aggregation arithmetic itself is sound.

**Conclusion: predictions are fully traceable within the experiment, but not traceable to the physical measurement.** Under the stated Gate 1 criterion — "if you cannot trace back, Gate 1 cannot be considered fully closed" — this alone prevents a CLOSED verdict.

---

## 13. ResNet1D Sensor-Mode Verification

Verified by reading `src/resnet1d/model.py`, `src/lib/npz/training.py`, `src/lib/npz/data.py` and the recorded `run_info.json`, not by inferring from experiment names.

| Property | Finding | Evidence |
|---|---|---|
| Input shape | `(batch, in_channels, window)` = `(N, C, 400)` | `data.py:56-57` enforces `(N, channels, time)`; `run_info.json → config.data.window = 400` |
| `in_channels` source | `args.expected_channels`, passed straight into `ResNet1D(...)` | `training.py:33` — `ResNet1D(args.expected_channels, num_classes, window, args.n_feature_maps)` |
| Channels per sensor | **4** | `cp2_s1` → 4; `cp1_s12` → 8; `cp2_s123`/`cp3_s123` → 12; all read from `run_info.json → config.data.channels` |
| Sensor channels vs feature channels | **All input channels are raw sensor channels.** No hand-crafted features enter the deep model | `data.py:50-66` passes the raw `X` tensor (only per-window z-scored) into `TensorDataset`; no feature module is imported by `npz/training.py` |
| Sensor fusion | **Early fusion at the input-channel dimension.** `block1` is `Conv1d(in_channels → n_feature_maps, k=8, padding="same")`, so every sensor's channels are mixed in the first convolution | `resnet1d/model.py:10, 36` |
| Single- vs multi-sensor | **Both, determined entirely by `--expected-channels` and the dataset root.** The architecture is identical; only `in_channels` changes | `training.py:25-34`; `run_info.json` for `cp2_s1` (4) vs `cp2_s123` (12) |
| Channel ordering | Fixed and positional within one dataset root; enforced by the shape check at `data.py:56`. **Cross-campaign consistency is not provable from these artefacts** | see §5.2 item 9 |
| Head | `AdaptiveAvgPool1d(1)` → `Flatten` → `Linear(2·n_feature_maps → 4)`; window-length-independent | `resnet1d/model.py:39-41` |
| `n_feature_maps` used | 16 in all audited runs (not the code default of 64) | `run_info.json → config.model.n_feature_maps = 16` |

```text
ResNet1D sensor mode = VERIFIED
```

Specifically: **multi-sensor early fusion at the raw-channel level, 4 channels per sensor, no feature channels, no per-sensor branch, no late fusion.** The single remaining gap is not the model's sensor mode but the *physical* identity and cross-campaign consistency of the channels (§5.2 item 9, §7.1), which is a dataset-registry problem rather than a model problem.

---

## 14. Main Scientific Findings

### Finding 1 — Within-campaign discrimination is repeatable across every held-out run for CP1 and CP2

**Claim.** For CP1 and CP2, distinguishing the four controlled connection states from vibration recordings is repeatable under run-aware, leakage-controlled evaluation: performance does not depend on which run is held out.

**Evidence.** Recording-level macro-F1 0.9400 ± 0.0400 (CP1, `resnet1D`, `signal_loro_v1/cp1_s12_resnet1d_batch64_v3/summary/summary.csv`) and 0.9547 ± 0.0618 (CP2, `resnet1D`, `.../cp2_s123_resnet1d_batch64_v3/summary/summary.csv`) across 30 LORO folds. The **worst** held-out run averages 0.914 (CP1 R6) and 0.880 (CP2 R11); the worst single fold is 0.914 and 0.829. Classical models corroborate independently: `random_forest` reaches 1.0000 ± 0.0000 on CP1 and 0.9857 ± 0.0325 on CP2 across the same 30 folds, with four unrelated algorithms agreeing to four decimal places on CP2. Two independent `resnet1D` training campaigns (different git commit and hyper-parameters) agree to 0.003 macro-F1.

**Limitation.** Single seed, so no initialisation variance is included. Each fold's test set is only 12 recordings, making the per-fold metric granular (one recording ≈ 0.083 accuracy). CP3 does **not** show this behaviour (Finding 3). Which CP2 branch (`cp2_21` or `cp2_2122`) produced these numbers is not recorded anywhere in the delivery, so a session-confounding explanation for the CP2 result cannot be excluded.

**Next action.** Re-run at least the CP1/CP2 headline configurations with seeds 42, 43, 44 (the launcher already accepts `--seeds`), and record the CP2 branch identity in `manifest.json` and `run_info.json`.

---

### Finding 2 — Cross-campaign transfer collapses to at-or-below chance, with explicit class collapse

**Claim.** A classifier trained on one campaign does not transport to another campaign of the same specimen: performance falls to or below the chance level, and the failure takes the form of collapse onto one or two classes rather than graceful degradation.

**Evidence.** Macro-F1 0.1139 ± 0.0221 (CP2→CP3, `resnet1D`), 0.1943 ± 0.0518 (CP2→CP3, `1dcnn`), 0.1473 ± 0.0413 (CP3→CP2, `resnet1D`), 0.2274 ± 0.0656 (CP3→CP2, `1dcnn`), all from `loro-cross-campaign-v1/*/summary/summary.csv`, each over 6 validation permutations with 72 test recordings. Balanced accuracy 0.2153–0.3009 against a 0.25 chance level. Pooled confusion for CP2→CP3 `resnet1D`: 377/432 predictions are `B1`, 55 are `B2`, and `Healthy` and `B3` are never predicted (§9.3). Against the intra-campaign result on the same target, the drop is −0.807 macro-F1 (CP2 target) and −0.420 (CP3 target).

**Limitation.** This is campaign-to-campaign, laboratory-to-laboratory. It is **not** a damage-detection failure and **not** evidence about field generalization. Three candidate causes remain untested and unseparated: cross-campaign channel/sensor-ordering inconsistency, genuine physical differences in specimen assembly or excitation between campaigns, and acquisition-chain differences. The retained ROC-AUC of ~0.61 for `1dcnn` indicates some rank information survives, so "no transferable signal" would be an over-statement.

**Next action.** Before any further modelling, verify from the registry that channel *k* of `cp2_s123` and channel *k* of `cp3_s123` are the same physical sensor and axis. This is a metadata check, not an experiment, and it is the cheapest possible discriminator between an instrumentation artefact and a physical campaign effect.

---

### Finding 3 — CP3 is a qualitatively different regime, and its mean is not a safe summary

**Claim.** CP3 does not reproduce the CP1/CP2 behaviour: performance is both substantially lower and highly dependent on which run is held out, so a single mean misrepresents it.

**Evidence.** CP3 `resnet1D` s123: 0.5334 ± 0.1816 with per-run means from 0.323 (R16) to 0.739 (R14) — a range wider than the whole between-sensor spread. CP3 `1dcnn`: 0.3639 ± 0.1086. Best CP3 result of any pipeline: `random_forest` 0.8464 ± 0.1719, but still with R16 at 0.611 and a worst fold at 0.475. `cp3_s12` reaches a single-fold macro-F1 of **0.050**. Sources: `signal_loro_v1/cp3_s123_*/summary/summary.csv`, `ml_loro_v1/ml_loro_v1/cp3_s123/*/summary/summary.csv`, `loro-each-sensor-v1/.../cp3/*/summary/summary.csv`.

**Limitation.** The cause is not identified. R16 being the worst held-out run for *every* model and every sensor configuration points to a run-level property of R16 rather than a model deficiency, but with no session/excitation metadata that property cannot be named.

**Next action.** Inspect R16's raw recordings and acquisition metadata directly; if the registry records excitation type per recording, stratify the CP3 LORO results by excitation before drawing any conclusion about CP3.

---

### Finding 4 — Model/pipeline choice dominates sensor configuration; the stated hypothesis is not supported

**Claim.** Within these experiments, changing the classification pipeline changes reliability substantially more than changing which sensors are used.

**Evidence.** On `cp2_s123` (identical data, identical splits): 0.6432 (`1dcnn`) → 0.9547 (`resnet1D`) → 0.9857 (all four classical models), Δ ≈ 0.34. Across all seven CP2 sensor configurations with `resnet1D` fixed: 0.8957 (s3) → 0.9657 (s13), Δ ≈ 0.07. On CP3: model Δ ≈ 0.48 versus sensor Δ ≈ 0.17, and the CP3 sensor spread is comparable to its own fold-to-fold SD. Sources: Tables C, D, E.

**Limitation.** The models were **not** tuned under a common protocol — the deep models used one fixed hyper-parameter setting per campaign, and the classical models used untuned library defaults. The `1dcnn` result in particular may reflect an unfavourable configuration rather than an architectural limit. Consequently this finding establishes that *the pipeline choice matters a lot in this study*, not that any specific architecture is inherently superior. Sensor configurations, by contrast, *were* compared under fully matched conditions, so the sensor Δ is the better-controlled of the two numbers.

**Next action.** Do not include the hypothesis "sensor configuration matters more than model architecture" in Paper 1 as a supported claim. Either report the effect ordering as observed with the tuning caveat stated explicitly, or run a matched hyper-parameter budget for `1dcnn` and `resnet1D` before making any architecture statement.

---

### Finding 5 — Run-aware evaluation exposed a real, model-independent run artefact

**Claim.** The LORO protocol did the job it was introduced to do: it surfaced a run-level anomaly that pooled or random-split evaluation would have averaged away.

**Evidence.** On CP2, all four classical models make exactly 5 errors in 360 recording decisions; all 5 are `B1 → B2`; and all 5 occur in exactly the five folds whose test run is R12 (`ml_loro_v1/ml_loro_v1/cp2_s123/*/summary/summary.csv`). On CP3, R16 is the worst held-out run for all four classical models *and* for `resnet1D`, and R14 is the best for all four classical models. Four algorithmically unrelated decision rules cannot fail identically by chance on the same run.

**Limitation.** Without `recordings.csv` the offending R12 recording cannot be identified, and the anomaly cannot be attributed to a physical cause (mounting, excitation, operator, or acquisition event).

**Next action.** Once the registry is delivered, resolve `R12:REC0004`-class identifiers to source files and inspect the specific `B1` recording in R12 and the whole of R16 in CP3.

---

## 15. Negative and Null Findings

Recorded explicitly, none suppressed:

1. **Cross-campaign transfer fails at or below chance in all four configurations tested.** Balanced accuracy 0.2153–0.3009 versus 0.25 chance; two of four are below chance.
2. **Two of four classes are never predicted** by `resnet1D` in the CP2→CP3 direction (`Healthy`, `B3`, 0/432 predictions each).
3. **`resnet1D` is worse than `1dcnn` cross-campaign** (0.1139 vs 0.1943 CP2→CP3; 0.1473 vs 0.2274 CP3→CP2), reversing the intra-campaign ordering. Higher intra-campaign capacity did not buy transportability — it appears to have cost it.
4. **Deep models did not outperform classical feature-based models anywhere.** `random_forest` ≥ `resnet1D` on all three campaigns (1.000 vs 0.940; 0.986 vs 0.955; 0.846 vs 0.533). The gap on CP3 is 0.31 macro-F1 in favour of the classical model.
5. **No seed-variance estimate exists.** Every reported SD is fold-only.
6. **The "sensor configuration > architecture" hypothesis is contradicted** by the measured effect sizes (§7.4).
7. **More sensors is not monotonically better.** CP2 `s13` (8 ch) ≥ `s123` (12 ch); CP3 `s3` (4 ch) > `s12` (8 ch).
8. **The canonical dataset structure specified in `Readme.md` is not present in the delivery**, so the "Raw data (Done)" item cannot be confirmed from these files.
9. **`Note.md`'s provenance claims are unverified.** Its recording counts are corroborated; its session and `borrowed` claims are not, because no delivered artefact carries those fields.
10. **The delivered notebook does not match the delivered results** (learning rate 8e-4/6e-4 in the notebook vs 3e-4 in every `run_info.json`).
11. **`Healthy ↔ B1` — the state boundary that matters most for any inspection trigger — is the dominant error axis** wherever the problem is non-trivial.

---

## 16. Implications for CEI / Condition Evidence Interface

Stated strictly as an implication for the Gate 2 interface design. This section is not Paper 2, and nothing here is claimed to be validated.

The cross-campaign result (§9, Finding 2) has one direct design consequence:

> A condition-evidence object should not carry only a predicted state. It must also carry provenance and the evaluated scope within which that prediction was shown to hold.

A prediction that reaches macro-F1 0.95 within CP2 and 0.11 when the same model is applied to CP3 is not "a state estimate with an accuracy figure" — it is a state estimate that is only meaningful **inside a stated evaluation envelope**. Recording the envelope is therefore not documentation overhead; it is what makes the number interpretable at all.

Metadata fields that the present evidence indicates are necessary:

```text
Campaign_ID
Run_ID
Recording_ID           (must resolve to a source file and session)
Session_Date
Borrowed_Flag          (per §4 — a class-aligned session confound must be visible)
Sensor_Config          (with physical position mapping, per §7.1)
Channel_Order          (per §5.2 item 9 and §9.3)
Model_ID
Model_Version          (already implemented: <model>-<git SHA> + git_dirty)
Evaluation_Protocol    (already implemented: split_id + seed + level="recording")
Confidence             (already implemented: per-class probabilities)
Validated_Scope        (NEW — the campaign/session envelope inside which the metric was measured)
```

Six of these twelve fields are already written by the current pipeline. `Validated_Scope`, `Session_Date`, `Borrowed_Flag`, `Channel_Order`, and the resolvable `Recording_ID` are the additions this audit indicates are needed.

---

## 17. What Can and Cannot Be Claimed in Paper 1

### Can be claimed (with the stated conditions attached)

1. Vibration recordings from the 1:10 steel-frame laboratory model support **repeatable four-state discrimination within a measurement campaign** under a run-aware, leakage-controlled protocol, for CP1 and CP2 — recording-level macro-F1 0.94–1.00, worst held-out run ≥ 0.88, 30 LORO folds, multiple independent pipelines agreeing.
2. The evaluation protocol is **leakage-safe by construction**: run-disjoint splits, per-window instance normalisation with no fitted statistics, no feature selection, no augmentation, and enforced recording-label consistency — all verifiable in code (§5).
3. All primary metrics are **recording-level**, with an explicitly stated aggregation rule (mean of window softmax probabilities, then argmax), applied identically to deep and classical pipelines.
4. **Cross-campaign transfer between laboratory campaigns is at or below chance**, with class collapse — a substantive negative finding about campaign/session dependence and limited transportability.
5. **Reliability is not uniform across campaigns**: CP3 behaves qualitatively differently from CP1/CP2, and its fold-to-fold variability is large enough that its mean must never be reported alone.
6. **Run-aware evaluation surfaced a model-independent run artefact** (CP2 R12; CP3 R16) that pooled evaluation would have hidden — evidence that the protocol change was worth making.
7. Reported sensor-configuration differences within a campaign are **modest relative to pipeline differences** (with the tuning caveat of Finding 4).

### Cannot be claimed

1. Anything about **damage diagnosis**. These are controlled connection states of a laboratory specimen.
2. Anything about **field performance, field generalization, or lab-to-field transfer**. The cross-campaign test target is another laboratory campaign.
3. **"Model X is the best model."** Only: "under the evaluated campaigns, sensor configurations and LORO protocol, model X achieved the highest observed recording-level macro-F1", with the tuning and single-seed caveats.
4. **"Optimal sensor placement."** Sensor positions are not even identified in the delivered artefacts (§7.1).
5. **"Sensor configuration influences reliability more strongly than model architecture."** Contradicted (§7.4).
6. **That `cp2_2122` is clean.** Its B3 class comes from a different measurement session (per `Note.md`), and no delivered artefact refutes or confirms it.
7. **That cross-campaign degradation is a "damage detection failure."** It is domain shift and limited transportability.
8. **Seed-level stability.** Not measured.
9. **Any statement requiring `p`-values.** These experiments were not designed for inferential comparison; the reported quantities are descriptive with dispersion, and must be presented that way.
10. **That Gate 1 is closed.** See §18.

---

## 18. Evidence Gate 1 Assessment

### Table I — Gate 1 evidence checklist

| Gate 1 requirement | Status | Evidence | Remaining issue |
|---|---|---|---|
| **Canonical dataset** | **NOT CLOSED** | No `dataset/canonical/` tree, no `manifest.json` in the delivery; all roots point at an external Kaggle path | Canonical structure and class map cannot be verified from the delivered files |
| **Run registry** | **NOT CLOSED** | `campaigns.csv`, `runs.csv`, `recordings.csv` all absent | No recording → source-file → session mapping; excitation type, sensor position, session date and `borrowed` flag are all unrecorded |
| **CP2 decision** | **PARTIALLY CLOSED** | `Note.md` documents the two branches and the risk; §4 issues the scientific verdict (`cp2_21` primary, `cp2_2122` sensitivity only) | Which branch produced the delivered `cp2_s123` results is not recorded in any artefact |
| **Leakage-safe splits** | **CLOSED** | `npz/loro.py:58-122`, `npz/data.py:36-66, 103-104`, `ml/features.py`, `ml/models.py:48-58`; 10-point audit in §5.2 with 8 PASS, 2 conditional | Cross-campaign channel-ordering consistency (item 9) and CP2 session confounding (item 8) remain NOT VERIFIABLE |
| **Recording-level metrics** | **CLOSED** | `npz/evaluation.py:26-80` and `ml/evaluation.py:20-39` — identical rule; `level: "recording"` stamped on every `scores.json` and `predictions.json`; macro-F1, balanced accuracy, accuracy, ROC-AUC and confusion all present | Window-level metrics are not stored even as a supporting diagnostic; window count per recording is `null` |
| **LORO** | **CLOSED** | 30 unique 4/1/1 splits per campaign per configuration, generated in code and matched by 30 output directories in every one of 23 intra-campaign experiments; 1 044/1 044 runs present | Single seed only |
| **Cross-campaign evaluation** | **CLOSED (executed); FINDING NEGATIVE** | 4 experiments × 6 validation permutations, including the required `--train-run-ids 7,8,9,10,11 --val-run-ids 12`, with the full 72-recording external test set | Results are at or below chance with class collapse; causes not yet separated |
| **Predictions saved** | **CLOSED** | `predictions.json` in all 1 044 run directories: recording ID, true, pred, per-class probabilities | Per-window probabilities not retained; recording IDs anonymised |
| **Seeds / splits saved** | **PARTIALLY CLOSED** | `seed` and full `split` object (run IDs, roots, manifest path) in `run_info.json`, `scores.json` and `predictions.json`; also in the directory name | Only one seed was ever run, so `mean ± SD across seeds` cannot be computed |
| **Model version saved** | **CLOSED** | `version = <model>-<git short SHA>`, plus `git_commit` and `git_dirty`; aggregation is version-aware (`aggregate_runs.py`) | Notebook in the repo does not match the recorded run parameters |
| **ResNet1D sensor mode** | **CLOSED — VERIFIED** | `resnet1d/model.py:32-49`, `npz/training.py:25-34`, `config.data.channels` 4/8/12 | Physical sensor identity and cross-campaign channel consistency unverified (a registry issue, not a model issue) |

### Verdict

```text
GATE 1 VERDICT: PARTIALLY CLOSED
```

Seven of eleven requirements are closed. The four that are not — canonical dataset, run registry, CP2 branch identity, and seed replication — are not cosmetic: the first three together break the provenance chain at its final hop, which the gate's own criterion names as disqualifying.

---

## 19. Remaining Blocking Issues

**B1. The canonical dataset and its registry were not delivered with the results.**
No `dataset/canonical/`, no `campaigns.csv` / `runs.csv` / `recordings.csv`, no `manifest.json`. Every run points at `/kaggle/input/datasets/platformciviltwin/signal-dataset-v1/v1/`. Consequences: recording IDs cannot be resolved to raw files; session date, excitation type, sensor position and `borrowed` status are unrecorded; the CP2 branch identity is unknown. *Fix:* deliver the canonical tree and registry alongside the results, and add `campaign_id`, `session_date`, `sensor_positions` and `channel_order` to `manifest.json` so `run_info.json` inherits them.

**B2. The CP2 branch that produced the delivered results is not identified.**
The scientific verdict (§4) is that `cp2_21` must be primary and `cp2_2122` sensitivity-only, but nothing in the artefacts says which one was used. Until this is recorded, every CP2 number in this report — including the headline 0.9547 — carries an unquantified session-confounding risk. *Fix:* record the branch in the manifest and re-emit `run_info.json`, or re-run CP2 from an explicitly named `cp2_21` root.

**B3. Cross-campaign results are at or below chance with confirmed class collapse, and the cause has not been separated.**
Three candidates remain open: cross-campaign channel/sensor ordering, genuine physical campaign differences, and acquisition-chain differences. *Fix:* verify channel-order identity between `cp2_s123` and `cp3_s123` from the registry first — a metadata check, not an experiment. Do not attribute the result to any cause until that check is done.

**B4. Only one seed (42) was run, so all reported SDs are fold-only.**
The Gate 1 requirement is `mean ± SD` across folds **and** seeds. The tooling already supports `--seeds 42,43,44`. *Fix:* re-run at minimum the Paper 1 headline configurations (CP1/CP2/CP3 `resnet1D` s123, `random_forest`, and all four cross-campaign experiments) with three seeds.

**B5. The delivered notebook does not describe the delivered runs.**
`signal-loro-v1.ipynb` specifies learning rates of 8e-4 and 6e-4; every `run_info.json` records 3e-4. Anyone attempting to reproduce Paper 1 from the notebook would not reproduce the results. *Fix:* regenerate the notebook from the recorded `args` in `run_info.json`, or delete it from the delivery and cite `run_info.json` as the run specification.

---

## 20. Recommended Paper 1 Result Tables and Figures

### Tables (all already computable from the delivered `summary.csv` files — no re-training needed)

| Paper 1 table | Content | Source |
|---|---|---|
| T1 | Dataset audit: campaigns, runs, recordings/run, recordings/class, channels/sensor, window length, and an explicit column for what is **not** recorded | §3 of this audit |
| T2 | Intra-campaign recording-level LORO: macro-F1, balanced accuracy, accuracy, ROC-AUC — mean ± SD **plus min and worst held-out run** | Table C |
| T3 | Sensor-configuration comparison, `resnet1D` fixed, with worst-fold and worst-run columns | Table D |
| T4 | Classical ML comparison, four named models × three campaigns | Table E |
| T5 | Cross-campaign matrix with pooled confusion, chance level marked on the same row | Table F + §9.3 |
| T6 | Leakage and provenance audit (condensed to ~8 rows) | Table H |

### Figures — priority order

1. **LORO fold/run performance plot.** Box or strip plot of the 30 fold macro-F1 values per campaign and model, with the chance line drawn. This is the single figure that shows repeatability *and* worst-case behaviour together. **Must be generated** from `summary.csv` (`aggregate_over == "seed"` rows) — no such aggregate figure exists in the delivery.
2. **Sensor-configuration comparison.** Same style, one panel per campaign, 17 configurations. **Must be generated** from the 17 `loro-each-sensor-v1/.../summary/summary.csv` files.
3. **Cross-campaign degradation.** Paired intra vs cross macro-F1 per direction and model, with the chance line. **Must be generated** from Table F.
4. **Normalized confusion matrices**, intra vs cross side by side. Row-normalised matrices already exist as data:
   ```text
   ![CP2 resnet1D pooled confusion](signal_loro_v1/cp2_s123_resnet1d_batch64_v3/summary/pooled_confusion_01_cp2_s123_resnet1d_resnet1d_row_normalized.csv)
   ![CP2→CP3 resnet1D pooled confusion](loro-cross-campaign-v1/cross_cp2_s123_to_cp3_s123_resnet_loro_batch64_v1/summary/pooled_confusion_01_cross_cp2_s123_to_cp3_s123_resnet1D_row_normalized.csv)
   ```

### Existing figures worth reusing directly

Per-run confusion PNGs are the only rendered figures in the delivery (one per run, 1 044 of them). Two are worth promoting as illustrative examples:

```text
![CP2 resnet1D, worst LORO fold (train 7-8-9-10 / val 12 / test 11, macro-F1 0.829)](signal_loro_v1/cp2_s123_resnet1d_batch64_v3/split_02_7-8-9-10-12-11/ddp_seed42/confusion_matrix.png)
![CP2→CP3 resnet1D, class collapse](loro-cross-campaign-v1/cross_cp2_s123_to_cp3_s123_resnet_loro_batch64_v1/train_val_split_01_train7-8-9-10-11_val12/ddp_seed42/confusion_matrix.png)
```

No other figures should be generated. The remaining 1 042 per-run PNGs are diagnostic artefacts, not publication material.

---

## 21. Immediate Next Actions

Ordered by cost-to-value, cheapest first. Actions 1–3 require **no re-training**.

1. **Deliver the canonical dataset and registry** (`campaigns.csv`, `runs.csv`, `recordings.csv`, `manifest.json`) alongside these results, with session date, source file, excitation, sensor position and `borrowed` flag per recording. Resolves B1 and completes the provenance chain. *(Effort: hours. Unblocks everything else.)*
2. **Record the CP2 branch identity** in `manifest.json` and confirm whether the delivered `cp2_s123` is `cp2_21` or `cp2_2122`. Resolves B2 and determines whether the CP2 headline number is reportable in Paper 1 at all. *(Effort: minutes, once B1 is done.)*
3. **Verify cross-campaign channel-order identity** between `cp2_s123` and `cp3_s123` from the registry. This is the highest-value single check in the whole list: it discriminates an instrumentation artefact from a physical campaign effect in §9, and it costs one metadata comparison. *(Effort: minutes.)*
4. **Generate the four aggregate figures** in §20 from the existing `summary.csv` files. *(Effort: one plotting script. No models re-run.)*
5. **Re-run the headline configurations with seeds 42, 43, 44** — CP1/CP2/CP3 `resnet1D` s123, `random_forest` s123, and all four cross-campaign experiments — to convert fold-only SDs into fold-and-seed SDs. Resolves B4 and is the last remaining item for a `mean ± SD` claim that meets the gate wording. *(Effort: the launcher already supports it; ~3× current compute for the selected subset.)*
6. **Regenerate or remove the notebook** so the delivered run specification matches `run_info.json`. Resolves B5. *(Effort: minutes.)*
7. **Resolve and inspect the two named anomalies** once B1 lands: the `B1` recording in CP2 R12 that all four classical models misread as `B2`, and the whole of CP3 R16.

---

## Appendix A. Experiment Matrix

| # | Folder | Dataset | CP | Runs | Sensors (ch) | Model | Splits × seeds | Runs on disk | git version |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `signal_loro_v1/cp1_s12_1dcnn_batch64_v3` | `cp1_s12` | CP1 | 1–6 | s12 (8) | `1dcnn` | 30 × 1 | 30 | `1dcnn-75d5c1e` |
| 2 | `signal_loro_v1/cp1_s12_resnet1d_batch64_v3` | `cp1_s12` | CP1 | 1–6 | s12 (8) | `resnet1D` | 30 × 1 | 30 | `resnet1D-75d5c1e` |
| 3 | `signal_loro_v1/cp2_s123_1dcnn_batch64_v3` | `cp2_s123` | CP2 | 7–12 | s123 (12) | `1dcnn` | 30 × 1 | 30 | `1dcnn-75d5c1e` |
| 4 | `signal_loro_v1/cp2_s123_resnet1d_batch64_v3` | `cp2_s123` | CP2 | 7–12 | s123 (12) | `resnet1D` | 30 × 1 | 30 | `resnet1D-75d5c1e` |
| 5 | `signal_loro_v1/cp3_s123_1dcnn_batch64_v3` | `cp3_s123` | CP3 | 13–18 | s123 (12) | `1dcnn` | 30 × 1 | 30 | `1dcnn-75d5c1e` |
| 6 | `signal_loro_v1/cp3_s123_resnet1d_batch64_v3` | `cp3_s123` | CP3 | 13–18 | s123 (12) | `resnet1D` | 30 × 1 | 30 | `resnet1D-75d5c1e` |
| 7–9 | `loro-each-sensor-v1/.../cp1/cp1_{s1,s2,s12}` | CP1 subsets | CP1 | 1–6 | 4/4/8 | `resnet1D` | 30 × 1 each | 90 | `resnet1D-843fbf2` |
| 10–16 | `loro-each-sensor-v1/.../cp2/cp2_{s1,s2,s3,s12,s13,s23,s123}` | CP2 subsets | CP2 | 7–12 | 4/4/4/8/8/8/12 | `resnet1D` | 30 × 1 each | 210 | `resnet1D-843fbf2` |
| 17–23 | `loro-each-sensor-v1/.../cp3/cp3_{s1,s2,s3,s12,s13,s23,s123}` | CP3 subsets | CP3 | 13–18 | 4/4/4/8/8/8/12 | `resnet1D` | 30 × 1 each | 210 | `resnet1D-843fbf2` |
| 24–27 | `ml_loro_v1/ml_loro_v1/cp1_s12/{random_forest,extra_trees,hist_gradient_boosting,svm_rbf}` | `cp1_s12` | CP1 | 1–6 | s12 (8) | 4 classical | 30 × 1 each | 120 | `*-536c3a4` |
| 28–31 | `ml_loro_v1/ml_loro_v1/cp2_s123/{...}` | `cp2_s123` | CP2 | 7–12 | s123 (12) | 4 classical | 30 × 1 each | 120 | `*-536c3a4` |
| 32–35 | `ml_loro_v1/ml_loro_v1/cp3_s123/{...}` | `cp3_s123` | CP3 | 13–18 | s123 (12) | 4 classical | 30 × 1 each | 120 | `*-536c3a4` |
| 36 | `loro-cross-campaign-v1/cross_cp2_s123_to_cp3_s123_1dcnn_loro_batch64_v1` | train `cp2_s123`, test `cp3_s123` | CP2→CP3 | tr 7–12, te 13–18 | s123 (12) | `1dcnn` | 6 × 1 | 6 | `1dcnn-06dfe3b` |
| 37 | `loro-cross-campaign-v1/cross_cp2_s123_to_cp3_s123_resnet_loro_batch64_v1` | idem | CP2→CP3 | idem | s123 (12) | `resnet1D` | 6 × 1 | 6 | `resnet1D-06dfe3b` |
| 38 | `loro-cross-campaign-v1/cross_cp3_s123_to_cp2_s123_1dcnn_loro_batch64_v1` | train `cp3_s123`, test `cp2_s123` | CP3→CP2 | tr 13–18, te 7–12 | s123 (12) | `1dcnn` | 6 × 1 | 6 | `1dcnn-06dfe3b` |
| 39 | `loro-cross-campaign-v1/cross_cp3_s123_to_cp2_s123_resnet_loro_batch64_v1` | idem | CP3→CP2 | idem | s123 (12) | `resnet1D` | 6 × 1 | 6 | `resnet1D-06dfe3b` |

**Total: 39 experiment configurations, 1 044 completed runs, 0 missing.**

---

## Appendix B. Key Metrics

All values are recording-level, `mean ± SD` across LORO folds, seed 42. Chance level for four balanced classes: accuracy = balanced accuracy = 0.25, macro-F1 ≈ 0.25, ROC-AUC = 0.50.

### B.1 Intra-campaign, deep models (30 folds)

| Dataset | Model | Accuracy | Balanced Acc. | Macro-F1 | ROC-AUC |
|---|---|---|---|---|---|
| cp1_s12 | 1dcnn | 0.6306 ± 0.0867 | 0.6306 ± 0.0867 | 0.5999 ± 0.1105 | 0.8910 ± 0.0322 |
| cp1_s12 | resnet1D | 0.9417 ± 0.0388 | 0.9417 ± 0.0388 | 0.9400 ± 0.0400 | 0.9991 ± 0.0037 |
| cp2_s123 | 1dcnn | 0.6583 ± 0.1355 | 0.6583 ± 0.1355 | 0.6432 ± 0.1328 | 0.8840 ± 0.0635 |
| cp2_s123 | resnet1D | 0.9556 ± 0.0609 | 0.9556 ± 0.0609 | 0.9547 ± 0.0618 | 0.9997 ± 0.0017 |
| cp3_s123 | 1dcnn | 0.4306 ± 0.1074 | 0.4306 ± 0.1074 | 0.3639 ± 0.1086 | 0.7343 ± 0.0806 |
| cp3_s123 | resnet1D | 0.5694 ± 0.1738 | 0.5694 ± 0.1738 | 0.5334 ± 0.1816 | 0.8108 ± 0.1272 |

### B.2 Sensor ablation, `resnet1D` (30 folds)

| Config | Accuracy | Balanced Acc. | Macro-F1 | ROC-AUC |
|---|---|---|---|---|
| cp1_s1 | 0.9333 ± 0.0509 | 0.9333 ± 0.0509 | 0.9316 ± 0.0520 | 0.9978 ± 0.0058 |
| cp1_s2 | 0.8111 ± 0.0654 | 0.8111 ± 0.0654 | 0.8150 ± 0.0596 | 0.9818 ± 0.0164 |
| cp1_s12 | 0.9444 ± 0.0505 | 0.9444 ± 0.0505 | 0.9429 ± 0.0520 | 0.9985 ± 0.0043 |
| cp2_s1 | 0.9278 ± 0.0647 | 0.9278 ± 0.0647 | 0.9254 ± 0.0681 | 0.9957 ± 0.0072 |
| cp2_s2 | 0.9056 ± 0.0717 | 0.9056 ± 0.0717 | 0.9021 ± 0.0741 | 0.9892 ± 0.0140 |
| cp2_s3 | 0.9000 ± 0.0554 | 0.9000 ± 0.0554 | 0.8957 ± 0.0595 | 0.9809 ± 0.0180 |
| cp2_s12 | 0.9361 ± 0.0748 | 0.9361 ± 0.0748 | 0.9346 ± 0.0764 | 0.9944 ± 0.0121 |
| cp2_s13 | 0.9667 ± 0.0415 | 0.9667 ± 0.0415 | 0.9657 ± 0.0427 | 0.9969 ± 0.0078 |
| cp2_s23 | 0.9306 ± 0.0540 | 0.9306 ± 0.0540 | 0.9270 ± 0.0585 | 0.9960 ± 0.0076 |
| cp2_s123 | 0.9583 ± 0.0569 | 0.9583 ± 0.0569 | 0.9575 ± 0.0576 | 0.9994 ± 0.0023 |
| cp3_s1 | 0.4639 ± 0.1130 | 0.4639 ± 0.1130 | 0.4280 ± 0.1196 | 0.7096 ± 0.1041 |
| cp3_s2 | 0.4500 ± 0.1250 | 0.4500 ± 0.1250 | 0.3723 ± 0.1511 | 0.7432 ± 0.1364 |
| cp3_s3 | 0.5694 ± 0.1240 | 0.5694 ± 0.1240 | 0.5129 ± 0.1478 | 0.8056 ± 0.1200 |
| cp3_s12 | 0.4500 ± 0.1799 | 0.4500 ± 0.1799 | 0.3925 ± 0.1983 | 0.7198 ± 0.1177 |
| cp3_s13 | 0.5667 ± 0.1425 | 0.5667 ± 0.1425 | 0.5277 ± 0.1646 | 0.8336 ± 0.0983 |
| cp3_s23 | 0.5222 ± 0.1434 | 0.5222 ± 0.1434 | 0.4713 ± 0.1492 | 0.7914 ± 0.1268 |
| cp3_s123 | 0.5722 ± 0.1677 | 0.5722 ± 0.1677 | 0.5384 ± 0.1763 | 0.8148 ± 0.1247 |

### B.3 Classical ML (30 folds)

| Dataset | Model | Accuracy | Balanced Acc. | Macro-F1 | ROC-AUC |
|---|---|---|---|---|---|
| cp1_s12 | random_forest | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 |
| cp1_s12 | extra_trees | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 |
| cp1_s12 | svm_rbf | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 |
| cp1_s12 | hist_gradient_boosting | 0.9972 ± 0.0152 | 0.9972 ± 0.0152 | 0.9971 ± 0.0156 | 1.0000 ± 0.0000 |
| cp2_s123 | random_forest | 0.9861 ± 0.0316 | 0.9861 ± 0.0316 | 0.9857 ± 0.0325 | 1.0000 ± 0.0000 |
| cp2_s123 | extra_trees | 0.9861 ± 0.0316 | 0.9861 ± 0.0316 | 0.9857 ± 0.0325 | 1.0000 ± 0.0000 |
| cp2_s123 | svm_rbf | 0.9861 ± 0.0316 | 0.9861 ± 0.0316 | 0.9857 ± 0.0325 | 1.0000 ± 0.0000 |
| cp2_s123 | hist_gradient_boosting | 0.9861 ± 0.0316 | 0.9861 ± 0.0316 | 0.9857 ± 0.0325 | 0.9960 ± 0.0099 |
| cp3_s123 | random_forest | 0.8611 ± 0.1506 | 0.8611 ± 0.1506 | 0.8464 ± 0.1719 | 0.9420 ± 0.0788 |
| cp3_s123 | extra_trees | 0.8333 ± 0.1764 | 0.8333 ± 0.1764 | 0.8070 ± 0.2087 | 0.9435 ± 0.0742 |
| cp3_s123 | hist_gradient_boosting | 0.8083 ± 0.1669 | 0.8083 ± 0.1669 | 0.8052 ± 0.1699 | 0.9361 ± 0.0796 |
| cp3_s123 | svm_rbf | 0.6889 ± 0.1750 | 0.6889 ± 0.1750 | 0.6793 ± 0.1727 | 0.8778 ± 0.1188 |

### B.4 Cross-campaign (6 validation permutations, external 72-recording test set)

| Direction | Model | Accuracy | Balanced Acc. | Macro-F1 | ROC-AUC |
|---|---|---|---|---|---|
| CP2 → CP3 | 1dcnn | 0.2870 ± 0.0478 | 0.2870 ± 0.0478 | 0.1943 ± 0.0518 | 0.6099 ± 0.0392 |
| CP2 → CP3 | resnet1D | 0.2315 ± 0.0190 | 0.2315 ± 0.0190 | 0.1139 ± 0.0221 | 0.5051 ± 0.0275 |
| CP3 → CP2 | 1dcnn | 0.3009 ± 0.0369 | 0.3009 ± 0.0369 | 0.2274 ± 0.0656 | 0.5872 ± 0.0420 |
| CP3 → CP2 | resnet1D | 0.2153 ± 0.0349 | 0.2153 ± 0.0349 | 0.1473 ± 0.0413 | 0.4931 ± 0.0687 |

---

## Appendix C. Files Audited

All paths relative to `OUTPUT_18.08.2026/Output_added_24.08.2026/`.

### C.1 Requirement and narrative documents

```text
Note.md
Readme.md                                          (the "Readme(3).md" of the brief)
signal_loro_v1/signal_experiments/README.md
signal_loro_v1/signal_experiments/ARCHITECTURE.md
ml_loro_v1/signal_experiments/README.md
signal_loro_v1/signal_experiments/notebook/signal-loro-v1.ipynb
loro-cross-campaign-v1/cross_cp2_s123_to_cp3_s123_1dcnn_loro_batch64_v1/summary/summary.md
ml_loro_v1/ml_loro_v1/cp2_s123/random_forest/summary/summary.md
```

### C.2 Source code read line by line

```text
signal_loro_v1/signal_experiments/src/lib/npz/data.py          (split resolution, NPZ loading, normalisation)
signal_loro_v1/signal_experiments/src/lib/npz/loro.py          (30-split and train/val-LORO generation)
signal_loro_v1/signal_experiments/src/lib/npz/training.py      (training loop, checkpoint selection, evaluation)
signal_loro_v1/signal_experiments/src/lib/npz/evaluation.py    (recording aggregation, metric computation)
signal_loro_v1/signal_experiments/src/lib/npz/artifacts.py     (provenance, output contract)
signal_loro_v1/signal_experiments/src/lib/npz/arguments.py
signal_loro_v1/signal_experiments/src/lib/npz/cli.py
signal_loro_v1/signal_experiments/src/lib/npz/parallel_cli.py
signal_loro_v1/signal_experiments/src/resnet1d/model.py         (ResNet1D architecture — sensor-mode verification)
signal_loro_v1/signal_experiments/src/cnn1d/model.py            (Conv1DClassifier)
signal_loro_v1/signal_experiments/src/lib/engine/metrics.py
signal_loro_v1/signal_experiments/src/lib/data/preprocessing.py
signal_loro_v1/signal_experiments/src/lib/utils/seed.py
signal_loro_v1/signal_experiments/scripts/aggregate_runs.py     (summary generation)
ml_loro_v1/signal_experiments/src/lib/ml/features.py            (366-feature extractor)
ml_loro_v1/signal_experiments/src/lib/ml/data.py
ml_loro_v1/signal_experiments/src/lib/ml/models.py              (four classical model definitions)
ml_loro_v1/signal_experiments/src/lib/ml/training.py
ml_loro_v1/signal_experiments/src/lib/ml/evaluation.py
ml_loro_v1/signal_experiments/src/lib/ml/loro.py
loro-cross-campaign-v1/signal_experiments/src/lib/npz/data.py   (diffed: identical)
loro-cross-campaign-v1/signal_experiments/src/lib/npz/loro.py   (diffed: logging only)
```

### C.3 Aggregated result files parsed (39 files, all `summary/summary.csv`)

```text
signal_loro_v1/{cp1_s12_1dcnn,cp1_s12_resnet1d,cp2_s123_1dcnn,cp2_s123_resnet1d,cp3_s123_1dcnn,cp3_s123_resnet1d}_batch64_v3/summary/summary.csv
loro-each-sensor-v1/sensor_loro_batch64_v1/cp1/cp1_{s1,s2,s12}/summary/summary.csv
loro-each-sensor-v1/sensor_loro_batch64_v1/cp2/cp2_{s1,s2,s3,s12,s13,s23,s123}/summary/summary.csv
loro-each-sensor-v1/sensor_loro_batch64_v1/cp3/cp3_{s1,s2,s3,s12,s13,s23,s123}/summary/summary.csv
ml_loro_v1/ml_loro_v1/{cp1_s12,cp2_s123,cp3_s123}/{random_forest,extra_trees,hist_gradient_boosting,svm_rbf}/summary/summary.csv
loro-cross-campaign-v1/cross_{cp2_s123_to_cp3_s123,cp3_s123_to_cp2_s123}_{1dcnn,resnet}_loro_batch64_v1/summary/summary.csv
```

Each of these contains 30 (or 6) per-split rows plus two aggregate rows; **1 044 per-run `scores.json` records are represented in total.**

### C.4 Individual run artefacts inspected directly

```text
signal_loro_v1/cp1_s12_1dcnn_batch64_v3/split_01_1-2-3-4-5-6/ddp_seed42/run_info.json
signal_loro_v1/cp2_s123_resnet1d_batch64_v3/summary/confusion_summary.json
loro-each-sensor-v1/sensor_loro_batch64_v1/cp2/cp2_s1/split_01_7-8-9-10-11-12/ddp_seed42/run_info.json
loro-each-sensor-v1/sensor_loro_batch64_v1/cp2/cp2_s123/split_01_7-8-9-10-11-12/ddp_seed42/run_info.json
loro-each-sensor-v1/sensor_loro_batch64_v1/cp2/cp2_s123/split_01_7-8-9-10-11-12/ddp_seed42/predictions.json
loro-cross-campaign-v1/cross_cp2_s123_to_cp3_s123_1dcnn_loro_batch64_v1/train_val_split_01_train7-8-9-10-11_val12/ddp_seed42/run_info.json
loro-cross-campaign-v1/cross_cp2_s123_to_cp3_s123_1dcnn_loro_batch64_v1/train_val_split_01_train7-8-9-10-11_val12/ddp_seed42/predictions.json
loro-cross-campaign-v1/cross_cp3_s123_to_cp2_s123_1dcnn_loro_batch64_v1/train_val_split_01_train13-14-15-16-17_val18/ddp_seed42/run_info.json
ml_loro_v1/ml_loro_v1/cp2_s123/random_forest/split_01_7-8-9-10-11-12/ml_seed42/run_info.json
ml_loro_v1/ml_loro_v1/cp2_s123/random_forest/split_01_7-8-9-10-11-12/ml_seed42/scores.json
ml_loro_v1/ml_loro_v1/cp2_s123/{random_forest,svm_rbf}/summary/confusion_summary.json
```

### C.5 Files sought and NOT found

```text
dataset/canonical/                       (entire tree)
dataset/canonical/registry/campaigns.csv
dataset/canonical/registry/runs.csv
dataset/canonical/registry/recordings.csv
dataset/canonical/registry/manifest.json
dataset/processed/{full_duration,middle_40s,model_npz}/
07b_campaign_manifest.csv
07b_resolve_campaigns.py
13_export_sensor_signal_analyzer.py
```

Confirmed absent by an exhaustive filename scan of every entry in all four result folders.

---

*Prepared as an independent audit. No raw data or source code was modified. No model was re-trained. Every numeric value in this report was recomputed from the delivered `summary.csv`, `scores.json`, `predictions.json` and `run_info.json` files and traces to the file paths listed in Appendix C.*
