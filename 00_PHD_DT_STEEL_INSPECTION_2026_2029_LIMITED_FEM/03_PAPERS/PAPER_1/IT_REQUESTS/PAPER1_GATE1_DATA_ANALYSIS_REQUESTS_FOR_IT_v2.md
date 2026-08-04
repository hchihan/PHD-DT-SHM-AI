# PAPER 1 / GATE 1 — DATA & ANALYSIS REQUESTS FOR IT TEAM (v2)
**Date:** 2026-07-18 | **Position:** RQ1 → WP1 → C4/Paper 1 → Gate 1 | **Scope:** Core Scope (laboratory evidence)
**Manuscript served:** `../../../90_ARCHIVE/HISTORICAL_UNIQUE_FILES/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Paper 1/PAPER1_GATE1_Q2_VERIFIED_EVIDENCE_REVISED_v2_MANUSCRIPT_SOURCE_20260718.md` (canonical working source; DOCX v2 absent at cleanup).

Mỗi task dưới đây ghi rõ: input; filename; cột/định dạng; bảng/hình đầu ra; section trong manuscript; claim bị ảnh hưởng; có chặn Gate 1 hay không. Không task nào được đánh dấu hoàn thành khi chưa có artifact thực tế được lưu và kiểm tra.

## T01 — RUN_REGISTRY_LOCKED.csv  **[BLOCKS GATE 1]**
- **Input:** toàn bộ raw recordings + nhật ký thí nghiệm.
- **Filename:** `RUN_REGISTRY_LOCKED.csv`
- **Columns:** `Run_ID, Date_Time, State_Code(H/A/BC/BR), Excitation_ID, Sensors_Recorded, File_IDs, Operator_Notes, Include_Flag, Exclude_Reason`
- **Output:** bảng audit §5.1. Số run báo cáo hiện tại (6/run-class; 72 recordings) phải được đối chiếu — nếu lệch, ghi rõ.
- **Section:** 3.5, 5.1. **Claim:** C1-12, dataset integrity.

## T02 — DATASET_FILE_MANIFEST.csv  **[BLOCKS GATE 1]**
- **Input:** thư mục dữ liệu thô.
- **Filename:** `DATASET_FILE_MANIFEST.csv`
- **Columns:** `File_ID, Filename, Run_ID, Sensor_ID, Duration_s, Sample_Count, Checksum_SHA256`
- **Output:** file-count reconciliation vs T01. **Section:** 3.5, 5.1. **Claim:** dataset integrity.

## T03 — DATASET_DICTIONARY.md
- **Input:** T01, T02, acquisition scripts.
- **Filename:** `DATASET_DICTIONARY.md`
- **Content:** định nghĩa mọi cột, đơn vị, quy ước đặt tên file, mapping State_Code ↔ physical state. **Section:** 3.5–3.6. **Không chặn Gate 1** nhưng bắt buộc trước submission.

## T04 — Sensor/channel metadata  **[BLOCKS GATE 1]**
- **Input:** hardware records, acquisition config.
- **Filename:** `SENSOR_CHANNEL_METADATA_v1.csv`
- **Columns:** `Sensor_ID, Hardware_Model, Range_g, Sensitivity, Axis, Mounting, Position, Sampling_Hz, Sync_Method`
- **Output:** Table 3 manuscript. **Section:** 3.4. **Claim:** C1-17; identifier chain Sensor_ID.

## T05 — Split-before-windowing audit  **[BLOCKS GATE 1]**
- **Input:** pipeline code.
- **Filename:** `SPLIT_BEFORE_WINDOWING_AUDIT_v1.md` (+ log excerpts)
- **Output:** bằng chứng code rằng run được gán fold trước khi cắt window; không window nào vượt ranh giới fold. **Section:** 4.2, 4.9. **Claim:** C1-13.

## T06 — Train-only preprocessing audit  **[BLOCKS GATE 1]**
- **Input:** pipeline code.
- **Filename:** `TRAIN_ONLY_PREPROCESSING_AUDIT_v1.md`
- **Output:** liệt kê mọi learned transformation (scaler, selection, reduction, calibration, tuning) + bằng chứng fit trong training fold. **Section:** 4.3, 4.9. **Claim:** C1-14.

## T07 — Common LORO fold registry  **[BLOCKS GATE 1]**
- **Input:** T01.
- **Filename:** `LORO_FOLD_REGISTRY_v1.csv`
- **Columns:** `Fold_Index, HeldOut_Run_ID, Training_Run_IDs`
- **Output:** dùng chung cho mọi sensor config và model. **Section:** 4.4, 5.2. **Claim:** C1-17, fairness.

## T08 — Model configurations and seeds  **[BLOCKS GATE 1]**
- **Input:** training scripts.
- **Filename:** `MODEL_CONFIG_REGISTRY_v1.md`
- **Content:** mỗi model: hyperparameters, tuning budget, seeds, stopping criteria, software versions. **Section:** 4.5–4.6. **Claim:** model-comparison fairness.

## T09 — ResNet1D provenance  **[BLOCKS GATE 1 cho model-comparison claim]**
- **Input:** checkpoint, training script, config.
- **Filename:** `RESNET1D_PROVENANCE_v1.md`
- **Content:** channel/sensor mode; folds; seeds; preprocessing; checkpoint hash. Kết luận: INCLUDE / FORMALLY EXCLUDE. **Section:** 4.5, 5.4, 5.7. **Claim:** C1-18.

## T10 — Per-window predictions with Run_ID  **[BLOCKS GATE 1]**
- **Input:** executed LORO.
- **Filename:** `PREDICTIONS_PER_WINDOW_v1.csv`
- **Columns:** `Fold_Index, Run_ID, Window_ID, Sensor_Config, Model, True_State, Pred_State, Class_Probs...`
- **Section:** 5.2–5.6. **Claim:** mọi claim kết quả.

## T11 — Per-run predictions and metrics  **[BLOCKS GATE 1]**
- **Input:** T10 aggregated.
- **Filename:** `METRICS_PER_RUN_v1.csv`
- **Columns:** `Fold_Index, HeldOut_Run_ID, Sensor_Config, Model, MacroF1, BalancedAcc, PerClass_F1...`
- **Output:** Table §5.2 + run-level plot. **Claim:** primary RQ1 evidence.

## T12 — Confusion matrices per fold and aggregate
- **Input:** T10.
- **Filename:** `CONFUSION_MATRICES_v1/` (per fold + aggregate, CSV + PNG)
- **Section:** 5.5, 6.4. **Claim:** confusion-pattern description. **Chặn Gate 1:** không, nhưng bắt buộc cho manuscript.

## T13 — Group-preserving permutation output  **[BLOCKS GATE 1]**
- **Input:** full pipeline + T01.
- **Filename:** `PERMUTATION_NULL_RESULTS_v1.csv` + script
- **Content:** hoán vị nhãn ở cấp run, chạy lại toàn pipeline mỗi lần hoán vị; số hoán vị, thống kê quan sát, empirical p-value. **Section:** 4.8, 5.6. **Claim:** C1-15.

## T14 — Effect-size analysis
- **Input:** T11.
- **Filename:** `EFFECT_SIZE_ANALYSIS_v1.md`
- **Content:** paired per-run differences giữa sensor configs và giữa models; effect-size measure đã được phê duyệt (xem METHOD DECISION trong manuscript §4.8). **Section:** 5.3–5.4. **Chặn:** không, nhưng cần trước submission.

## T15 — Sensitivity analyses
- **Input:** pipeline + T01.
- **Filename:** `SENSITIVITY_ANALYSES_v1/`
- **Content:** non-overlapping windows; alternative overlap; excitation-specific; exclusion of questionable runs; seed sensitivity; ResNet1D in/out (nếu T09 = INCLUDE). **Section:** 5.7.

## T16 — Reproducibility environment
- **Input:** môi trường thực thi.
- **Filename:** `ENVIRONMENT_LOCK_v1.md` (+ `requirements.txt`/lockfile, commit hash)
- **Section:** 4.9, Data & Code Availability.

## T17 — Data/code repository decision
- **Input:** quyết định của tác giả/PI.
- **Filename:** `REPOSITORY_DECISION_v1.md`
- **Content:** deposit hay không, ở đâu, licence. **Section:** Data and Code Availability. **[AUTHOR CONFIRMATION REQUIRED]**

## Tổng hợp trạng thái chặn Gate 1
Chặn Gate 1: T01, T02, T04, T05, T06, T07, T08, T09, T10, T11, T13.
Không chặn nhưng bắt buộc trước submission: T03, T12, T14, T15, T16, T17.
