# PAPER 1 — ILLUSTRATIVE TABLES & FIGURES INDEX (v1)
**Date:** 2026-07-18 | Kèm outline `PAPER1_JOURNAL_OUTLINE_WITH_ILLUSTRATIVE_RESULTS_v1.docx`

> ⚠️ Mọi bảng/hình dưới đây chứa **ILLUSTRATIVE MOCK DATA — NOT PROJECT EVIDENCE**. Kịch bản minh họa: 6 nhóm độc lập; 4 trạng thái H/A/BC/BR; 3 cấu hình S1/S2/S1+S2; 4 model (LR, SVM, RF, 1D-CNN); ResNet1D ngoài main results. Thay toàn bộ sau khi independent unit của dữ liệu thật được khóa.

## Bảng minh họa

| Bảng/Hình | Mục đích | Dữ liệu đầu vào cuối cùng | Người phụ trách | Trạng thái |
|---|---|---|---|---|
| Bảng 1 | Dataset & independent-group summary | RUN_REGISTRY_LOCKED.csv + file manifest (T01, T02) | SV IT | MOCK — chờ thay |
| Bảng 2 | Median macro-F1 sensor × model | Final LORO/LOGO metrics (T11) | SV IT | MOCK — chờ thay |
| Bảng 3 | Per-group macro-F1 (RF, 1D-CNN) | Per-run predictions/metrics (T10, T11) | SV IT | MOCK — chờ thay |
| Bảng 4 | Per-class F1 (Random Forest) | Final per-class metrics (T11, T12) | SV IT | MOCK — chờ thay |
| Bảng 5 | Paired sensor-configuration effects | Paired diff + effect size (T14) | SV IT | MOCK — chờ thay |
| Bảng 6 | Empirical-null results | Group-preserving permutation (T13) | SV IT | MOCK — chờ thay |
| Bảng 7 | Sensitivity summary | Sensitivity suite (T15) | SV IT | MOCK — chờ thay |

## Hình minh họa (PAPER1_ILLUSTRATIVE_RESULTS_ASSETS/, PNG 300 dpi)

| Bảng/Hình | Mục đích | Dữ liệu đầu vào cuối cùng | Người phụ trách | Trạng thái |
|---|---|---|---|---|
| Fig1_research_story.png | Research story (khung khái niệm) | Không cần dữ liệu — sơ đồ khái niệm | Tác giả | Dùng được (schematic) |
| Fig2_specimen_sensors.png | Specimen + S1/S2 + connection states | Ảnh/bản vẽ specimen có kích thước xác minh | Tác giả | PLACEHOLDER — cần ảnh thật |
| Fig3_pipeline.png | Run-aware evaluation pipeline | Không cần dữ liệu — sơ đồ quy trình | Tác giả | Dùng được (schematic) |
| Fig4_run_level_macroF1.png | Group-level macro-F1 (RF ví dụ) | Per-run metrics (T11) | SV IT | MOCK — chờ thay |
| Fig5_paired_sensor_effect.png | Paired sensor effect theo group | Per-run metrics (T11) | SV IT | MOCK — chờ thay |
| Fig6_confusion_matrices.png | Confusion S1/S2/S1+S2 | Retained predictions (T10, T12) | SV IT | MOCK — chờ thay |
| Fig7_empirical_null.png | Empirical-null distribution | Permutation output (T13) | SV IT | MOCK — chờ thay |
| Fig8_sensor_vs_model.png | Sensor effect vs model effect | Final metrics (T11) | SV IT | MOCK — chờ thay |

## Ghi chú kỹ thuật cho nhóm IT
- Primary metric: macro-F1 tính **per held-out group**; báo cáo median + range + giá trị từng group (không chỉ mean).
- Fig4/Fig5 dùng dot/connected-points theo group, không dùng bar chart của mean.
- Confusion matrices: cùng class order (H, A, BC, BR) và cùng color scale giữa các cấu hình.
- Empirical-null: permutation unit = independent group; ghi số permutations + empirical p-value trong caption.
- Mỗi bảng/hình khi thay số thật phải gỡ nhãn mock và đối chiếu QA checklist mục 9–10.
- Script sinh hình mock: `make_figs.py` (giữ để tái tạo layout với dữ liệu thật).
