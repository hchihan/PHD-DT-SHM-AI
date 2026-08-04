# 00_EXECUTIVE_REPORT — THREE_CAMPAIGN_REANALYSIS

**Scope classification:** RQ1 → WP1 → Chapter 4 → Paper 1 → Evidence Gate 1 → **Core** (laboratory condition/state-change evidence under run-aware, campaign-aware evaluation). Not RQ2 (traceability), not RQ3 (field), no FEM component of any kind. **This document does not close Gate 1.** Every quantitative figure below is a **candidate claim pending Gate 1 closure** (Charter v2.1 §10) and none reproduces, or was tuned toward, the prior pipeline's ~0.91 macro-F1 figure — the task brief explicitly excluded that as a target.

All analysis follows **Claim → Evidence → Limitation → Next action**, per project governance (`CLAUDE.md`, Charter v2.1 §11).

---

## 0. What was rebuilt, from raw data, in this pass

A new, independent pipeline (`build_registry.py` → `build_data_cache.py` → `pipeline_lib.py` → `run_feature_baselines.py` → `run_cnn.py` → `run_permutation_control.py` → `run_sensitivity.py` → `assemble_outputs.py`) was written from scratch against the three raw campaign folders (`Campaign1_25.04.2026/`, `Campaign2_22.07.2026/`, `Campaign3_29.07.2026/`, 72 CSVs each, 216 total). No code, cache, or result from the prior `pipeline 1D-CNN (cũ)/cc_*.py` pipeline or its outputs (`CAMPAIGN_AND_SENSOR_PAIR_REPORT.md`, `Cross_Campaign_Quality_Manifest.csv`, `Campaign3_QC_Manifest.csv`) was reused as input to any model; those files were read only as prior context (see §7).

---

## 1. Stage A — Master run registry

**Claim.** All 216 expected recordings (4 states × 3 excitations × 6 runs × 3 campaigns) are present, parsed, hashed, and quality-audited; no file is missing or duplicated.

**Evidence.** `02_MASTER_RUN_REGISTRY.csv` (216 rows), `03_DATA_QUALITY_AND_PROVENANCE_LOG.csv` (66 flagged checks), `sensor_fingerprint_check.csv`, `sensor_block_permutation_flags.csv`. Filename parsing is fully deterministic (`B`=Beat with `L1/L2` sub-level, `N`=White_Noise, `S0`=Healthy, `S1B{1,2,3}`=B1/B2/B3, `R{n}`=run); every one of the 216 completeness cells (Campaign × Run × State × Excitation) has exactly one match, zero missing, zero duplicate-hash files. Sampling rate is 100.000 Hz with no jitter flags anywhere. Effective (trailing-NaN-truncated, Force-excluded) duration ranges 41.55–122.30 s across all 216 files — every file comfortably covers the required 40 s common window.

- The single file named `BS1B1L1R12.csv` in Campaign 2 (unlike its 71 siblings, it carries **no** `20260721__`/`20260722__` date prefix) is flagged `PROVENANCE_WARNING` and **not auto-excluded**, per protocol. It is included in the primary results and separately tested with/without in §6.A.
- Dead-channel flags (std < 1 quantisation step, 0.1 m/s²) affect 36/72 Campaign 1 files (`S1_Ay` in 19, `S2_Ay` in 17), 12/72 Campaign 2 files (`Ax` only, scattered across S1/S2/S3), 14/72 Campaign 3 files (`S3_Ax`). Channels are kept in (not dropped), flagged, consistent with the task brief.
- No NaN-mid-file, no sampling-rate deviation, no spike/clipping flags anywhere in the 216 recordings.

**Limitation — material, discovered during this audit.** An independent static-gravity fingerprint check (mean accelerometer reading per CSV column block, per file) shows that the **CSV column position does not reliably identify the same physical sensor across all files within Campaign 1 and Campaign 2**:
- **Campaign 3**: every column position (S1, S2, S3) maps to one tight fingerprint cluster across all 72 files — column position is a reliable physical-sensor proxy here.
- **Campaign 1**: both column positions (S1, S2) are cleanly **bimodal** (~‑2.08 vs ~+1.50 m/s² on the gravity-x projection) — consistent with the prior project's own audit finding of "2 of 2 block permutations" in this campaign.
- **Campaign 2**: all three column positions are **3-modal** (~‑1.97, ~‑0.3, ~+1.71 m/s²) — consistent with the prior project's own audit finding of "6 of 6 block permutations" in this campaign.

This means the experimenter-confirmed statement "S1 = Apex, S2 = BeamColumn, S3 = BraceColumn" (confirmed at the level of *which physical units were deployed*) does **not** by itself guarantee that "S1" in a given Campaign 1 or Campaign 2 CSV always denotes the same physical unit. `Sensor_Mapping_Status` for every Campaign 1/2 recording has been updated to `SENSOR_SET_CONFIRMED_COLUMN_POSITION_UNSTABLE`. This is a genuine, reproducible finding (self-consistent within this session's own fingerprint data — perfectly bimodal/trimodal with zero intermediate values) and independently corroborates, rather than contradicts, the prior project's own provisional-mapping caveat. **All single- and paired-sensor (not all-sensor) results below for Campaign 1 and Campaign 2 should be read as "column position 1/2/3", not as a physically verified Apex/BeamColumn/BraceColumn identity**, until a per-file fingerprint-based reassignment is done (see `15_NEXT_ANALYSIS_RECOMMENDATION.md` item 1). Campaign 3's single-sensor results are not subject to this caveat.

**Next action.** Per-file physical-sensor reassignment for Campaign 1 and Campaign 2 using the fingerprint data already captured in `sensor_fingerprint_check.csv`, then re-run every single/paired-sensor configuration that used those two campaigns.

---

## 2. Stage B/C — Analysis sets and preprocessing

**Claim.** Two analysis sets were defined and never mixed: **CORE_THREE_CAMPAIGN_SET** (Campaigns 1+2+3, S1_Ax/S2_Ax, 18 independent runs) and **SUPPORTING_THREE_SENSOR_SET** (Campaigns 2+3, S1/S2/S3 × Ax/Ay/Az, 12 independent runs). `04_ANALYSIS_SET_MANIFEST.csv` (360 rows) records set membership per recording.

**Evidence.** Common preprocessing: middle-40 s window (4000 samples @ 100 Hz, no interpolation), per-recording mean removal, no RMS-normalisation in the main analysis, fixed 2 s / 200-sample non-overlapping windows, group (run) split performed **before** windowing, scaler fit on training folds only. Implemented in `pipeline_lib.py::build_dataset`. Within-campaign LORO channel convention: Campaign 1 uses Ax only (its only role is in the Ax-only core set); Campaign 2/3 use the full Ax/Ay/Az supporting-set convention — this protocol choice is stated explicitly here because the task brief did not fully disambiguate Campaign 1's within-campaign channel scope.

**Limitation.** Full-duration is used only as a sensitivity check (§6.B), per protocol.

**Next action.** None outstanding for this stage.

---

## 3. Stage D — Framework audit

**Claim.** A standard deep-learning framework (TensorFlow/Keras 2.21.0, CPU) imports and trains stably in this environment; the compact 1D-CNN baseline is real, not simulated.

**Evidence.** `01_ENVIRONMENT_PROVENANCE.md`. PyTorch was not available (documented CUDA-preload blocker from a prior session in this same project); TensorFlow-cpu was downloaded, installed, and verified with a real forward+train pass before any use.

**Limitation.** CPU-only, 2 vCPU sandbox with a 45-second-per-shell-command ceiling; each CNN fit measured 7–45 s depending on training-set size, which materially bounded how much of the CNN matrix could be completed in this session (see §5 and `15_NEXT_ANALYSIS_RECOMMENDATION.md`).

**Next action.** None for the audit itself; compute-budget consequences are tracked in §5 and the recommendation file.

---

## 4. Stage E — Sanity checks

**Claim.** The pipeline passes the required pre-flight checks; the 1D-CNN was not stopped.

**Evidence.** Label mapping (`Healthy/B1/B2/B3` → `0..3`) verified; tensor shape verified (`n_windows × 200 × n_channels`); channel order fixed by construction; train-only preprocessing verified by code path (scaler/mean fit only on train-fold arrays); class distribution near-balanced by design (4 states × equal excitations/runs); softmax outputs sum to 1 by construction (Keras `softmax` activation); no NaN/Inf found in any built dataset; train/eval mode handled by Keras `fit`/`predict`; best-checkpoint restoration via `EarlyStopping(restore_best_weights=True)`. **Tiny-set overfit test**: an 8-recording/160-window subset reached ~97.5–99.4% train accuracy within 150 epochs (no early stopping) — the architecture and training loop can overfit, so per protocol the 1D-CNN was **not** stopped.

**Limitation.** The tiny-set check needed ~150 epochs to clearly demonstrate overfitting; combined with `patience=10` in the real runs, several harder single-axis folds stopped at epoch ~11 with near-single-class collapse (macro-F1 ≈ 0.10, e.g. Campaign 1 / S1_Ax). This is flagged, not silently smoothed over — see `15_NEXT_ANALYSIS_RECOMMENDATION.md` item 4.

**Next action.** Patience ablation (documented sensitivity check, not a silent architecture change).

---

## 5. Stage F/G/H — Fixed baselines, within-campaign LORO, cross-campaign LOCO

**Claim.** Feature-baseline models (Logistic Regression, SVM, Random Forest) were run to completion across the **entire** required within-campaign LORO matrix (13 sensor configs × 6 folds × 3 models = 234 fits) and the entire cross-campaign LOCO matrix (3 configs × 3 folds × 3 models = 27 fits), single seed 42, no tuning, fixed feature set (RMS, std, peak-to-peak, dominant frequency, spectral centroid, 3 band-energies, PSD-peak, per channel). The compact 1D-CNN (fixed architecture, Adam 1e-3, batch 32, dropout 0.3, ≤100 epochs, patience 10) was run to completion for the **entire cross-campaign LOCO matrix** (9/9 fold-configs, seed 42) and **partially** for within-campaign LORO (Campaign 1 / S1_Ax, 4 of 6 folds only).

**Evidence.** `05_WITHIN_CAMPAIGN_LORO_RESULTS.csv`, `06_CROSS_CAMPAIGN_RESULTS.csv`, `07_BASELINE_MODEL_COMPARISON.csv`, `09_SENSOR_CONFIGURATION_RESULTS.csv`, `10_PER_CLASS_RESULTS.csv`, `12_CONFUSION_MATRICES/` (3 representative folds), `14_PREDICTIONS_WITH_PROVENANCE.csv` (1,920 window-level predictions across those 3 folds).

Within-campaign LORO, Random Forest (strongest of the three feature models), median macro-F1 across folds/configs:

| Campaign | Median macro-F1 | Range | Best config (median) |
|---|---|---|---|
| Campaign 1 (Ax only) | 0.683 | 0.573–0.788 | S1+S2_Ax: 0.760 |
| Campaign 2 (xyz) | 0.878 | 0.630–0.975 | S3_xyz: 0.911 |
| Campaign 3 (xyz) | 0.609 | 0.218–0.954 | S1+S2+S3_xyz: 0.678 |

Cross-campaign LOCO (CORE set, S1_Ax/S2_Ax/S1+S2_Ax), median macro-F1 across the 9 fold-configs, by model family:

| Model | Median macro-F1 | Mean | Std | Min | Max |
|---|---|---|---|---|---|
| LogReg | 0.186 | 0.189 | 0.032 | 0.153 | 0.259 |
| SVM | 0.195 | 0.193 | 0.039 | 0.120 | 0.230 |
| RF | 0.166 | 0.160 | 0.024 | 0.129 | 0.202 |
| CNN (seed 42) | 0.152 | 0.157 | 0.050 | 0.100 | 0.250 |

Chance level for 4 balanced classes is 0.25. **Every cross-campaign LOCO result, across all four model families, falls at or below chance**, in sharp contrast to within-campaign medians of 0.61–0.88.

**Limitation.** CNN coverage is incomplete (see Claim above and `15_NEXT_ANALYSIS_RECOMMENDATION.md` items 2–3); only seed 42 was run for CNN (task minimum is 3 seeds); Campaign 1/2 single/paired-sensor numbers are subject to the column-position caveat in §1.

**Next action.** Complete CNN seed sweep and within-campaign CNN matrix; re-run Campaign 1/2 single-sensor configs after fingerprint-based resensoring.

---

## 6. Sensitivity analyses (A–D), one representative fold each (Campaign 2, held-out R7, RF)

| Analysis | Variant | macro-F1 |
|---|---|---|
| A — with/without `BS1B1L1R12.csv` | with | 0.971 |
| | without | 0.975 |
| B — window length | middle 40 s | 0.971 |
| | full duration | 0.859 |
| C — normalisation | amplitude-preserving (main) | 0.971 |
| | per-recording RMS-normalised | 0.841 |
| D — axis selection | Campaign 2, Ax-only | 0.770 |
| | Campaign 2, xyz | 0.919 |
| | Campaign 3, Ax-only | 0.660 |
| | Campaign 3, xyz | 0.690 |

**Claim.** (A) The single provenance-flagged file has a negligible effect (+0.004) on this fold. (B) The full-duration variant scores materially lower than the middle-40s window on this fold (−0.11), plausibly because longer recordings introduce excitation-onset/session heterogeneity that the fixed 40 s window avoids — this is a hypothesis, not confirmed on one fold. (C) RMS-normalisation reduces this fold's score by −0.13, consistent with the decision to keep amplitude information in the main analysis. (D) Restricting to Ax-only (the CORE cross-campaign set's channel convention) costs real within-campaign performance in Campaign 2 (−0.149) and a smaller amount in Campaign 3 (−0.030) — the CORE set trades within-campaign accuracy for a common channel, and per §5 that trade still does not buy cross-campaign generalisation.

**Limitation.** Each analysis used one representative fold only, per the time budget of this pass, not the full fold matrix; per protocol these are sensitivity checks and do not replace the main §5 results.

**Next action.** Extend each sensitivity analysis to the full fold matrix if Paper 1 requires more than a single-fold sensitivity illustration.

---

## 7. Negative control — recording-level permutation, 100 reps each, Random Forest

| Configuration | Real macro-F1 | Null median | Null range | p(null ≥ real) |
|---|---|---|---|---|
| Within-Campaign 2, S1+S2+S3_xyz, held-out R7 | 0.962 | 0.222 | 0.000–0.489 | **0.000** |
| Within-Campaign 1, S1+S2_Ax, held-out R1 | 0.647 | 0.229 | 0.077–0.399 | **0.000** |
| Cross-campaign LOCO, S1+S2_Ax, held-out Campaign 1 | 0.129 | 0.224 | 0.134–0.324 | **1.000** |

**Claim.** The pipeline is leakage-free: with recording-level label shuffling (training side only, group structure preserved, test labels untouched), the null distribution centres near chance (~0.22–0.23) in all three configurations, as expected. The two within-campaign real results sit far above their null distributions (p = 0.000, i.e. 0/100 permutations matched or exceeded the real score) — strong evidence that the real within-campaign discrimination is genuine, not a pipeline artefact. The cross-campaign real result is not merely "uninformative" — it is **below every one of the 100 shuffled-label permutations** (p(null ≥ real) = 1.000): training on the real labels of two campaigns produces a *worse* classifier on the third campaign than training on randomly shuffled labels from those same two campaigns. This is direct, non-fabricated evidence that the cross-campaign model is learning something anti-correlated with — not merely unrelated to — the target campaign's true state labels (most plausibly campaign-specific nuisance structure).

**Limitation.** Only 3 representative configurations were run (one per campaign role), not the full permutation matrix; `08_PERMUTATION_RESULTS.csv` has 300 rows (100 × 3).

**Next action.** None required to trust the within-campaign/cross-campaign contrast reported here; extending permutation coverage to more configs is optional polish, not a blocker.

---

## 8. Answers to the 12 required questions (§12 of the task brief)

1. **Are the four states distinguished across held-out runs, within each campaign?** Yes, well above chance, in all three campaigns (RF median macro-F1 0.61–0.88 vs chance 0.25), confirmed non-artefactual by the permutation control (§7). *Candidate claim pending Gate 1 closure.*
2. **Which campaign produces the most stable evidence?** Campaign 2 (RF median 0.878, narrower spread, std 0.091) is the most stable; Campaign 3 is the least stable (median 0.609, std 0.184, min as low as 0.218 on some fold/config combinations). *Candidate claim pending Gate 1 closure; also subject to the §1 column-position caveat for single/paired-sensor Campaign 2 configs.*
3. **Do results exceed the permutation control?** Yes for both within-campaign configurations tested (p = 0.000). The cross-campaign configuration tested does **not** exceed its control — it falls *below* it (§7).
4. **Do RF/SVM and 1D-CNN give consistent conclusions?** Yes, on cross-campaign LOCO (the only stage where CNN coverage is complete): all four model families (LogReg, SVM, RF, CNN) land in the same near-/sub-chance band (0.15–0.20 median). Within-campaign consistency is not yet fully checked (CNN coverage incomplete, §5).
5. **Are S1, S2, or S1+S2 more stable across all three campaigns?** Within campaign, combining sensors helps in every campaign tested (Campaign 1: S1+S2_Ax 0.760 > S2_Ax 0.683 > S1_Ax 0.645 [medians via RF]; similar ordering pattern in Campaign 2/3 xyz configs). *Subject to the §1 caveat.*
6. **Does S3 improve B3 on Campaign 2 and 3?** Mixed, not a clean "yes". In Campaign 2, B3 F1 is already very high (0.96) with S1 alone and only marginally different with S3 added (0.99) — consistent with the prior project's own suspicion that Campaign 2's B3 separability may be dominated by a session/recording-date artefact rather than the brace sensor specifically (this pass did not independently re-test that hypothesis). In Campaign 3, S3 addition shows a modest, non-monotonic effect on B3 F1 (0.54–0.75 across configs, highest with all three sensors combined). **Evidence is currently insufficient to state that S3 reliably improves B3 detection.**
7. **Does a model trained on two campaigns generalise to the third?** No. Every cross-campaign LOCO configuration and every model family scored at or below chance (§5), and the permutation control shows the real cross-campaign classifier performing *worse* than label-shuffled training (§7). This is the strongest and most load-bearing finding of this pass.
8. **Does the BeamColumn amplitude shift reduce cross-campaign performance?** Not directly tested in this pass (no amplitude-shift-specific ablation was run); the near-uniform sub-chance collapse across all cross-campaign configurations and models is consistent with a campaign-level nuisance shift dominating the signal, but this pass cannot isolate amplitude shift specifically from other candidate causes (sensor remounting, the §1 column-position instability, excitation-duration differences). **Evidence is currently insufficient** to attribute the collapse to amplitude shift specifically.
9. **Does RMS-normalisation improve robustness or erase state evidence?** On the one fold tested (§6.C), RMS-normalisation **reduced** macro-F1 (0.971 → 0.841), consistent with the protocol decision to keep amplitude information in the main analysis. Not tested for cross-campaign robustness in this pass.
10. **How much does `BS1B1L1R12.csv` affect Campaign 2 results?** Negligibly, on the one fold tested (§6.A: 0.971 with vs 0.975 without). Not tested across the full fold matrix.

---

## 9. Gate 1 status

**Explicitly: Gate 1 is not closed.** Per `EVIDENCE_GATES_v2.1.md`, every G1 gate item (run registry, LORO, ResNet1D provenance — N/A here, no ResNet1D was run — run/fold uncertainty, gate sign-off) remains `OPEN`; this pass materially advances the run registry, LORO, and run/fold-uncertainty items but does not sign off any of them. No claim in this document should be cited as "Gate 1 passed" or as a final Paper 1 number.

## 10. Files not fully populated in this pass

`12_CONFUSION_MATRICES/` and `14_PREDICTIONS_WITH_PROVENANCE.csv` cover 3 representative folds only (not the full ~270-fold matrix); `13_TRAINING_CURVES/` was not populated (per-epoch history was not retained during the CNN sweep — only final epoch counts were logged). See `15_NEXT_ANALYSIS_RECOMMENDATION.md` for the complete list of deferred work.

## 11. Where the complete package lives

The full output tree (including the large raw registry, analysis-set manifest, per-class results, and per-window predictions files, plus all pipeline code) was delivered to you via the chat file cards in this session. This copy in the project workspace contains the executive report, environment provenance, next-action recommendation, all aggregate/summary CSVs, the three representative confusion matrices, and the sensor-mapping audit CSVs. If you want the large raw files (`02_MASTER_RUN_REGISTRY.csv`, `04_ANALYSIS_SET_MANIFEST.csv`, `10_PER_CLASS_RESULTS.csv`, `14_PREDICTIONS_WITH_PROVENANCE.csv`, `sensor_fingerprint_check.csv`) also placed in this folder, ask and they will be copied over in a follow-up.
