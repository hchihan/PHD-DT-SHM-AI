# PAPER 1 / GATE 1 — INTERNAL QA CHECKLIST (v1)
**Date:** 2026-07-18 | **Position:** RQ1 → WP1 → Chương 4 → Paper 1 → Gate 1
**Mục đích:** giữ toàn bộ nội dung QA nội bộ TÁCH KHỎI outline tạp chí. Không đưa bảng/checklist này vào thân outline journal.

> Nguyên tắc: mock data trong outline journal chỉ để hướng dẫn trình bày. Không con số mock nào được dùng làm project evidence, đưa vào Abstract/Conclusion, hoặc claim audit.

## 1. Independent-unit decision — BLOCKER SỐ 1
- [ ] Xác định độ độc lập: một "run" là một *recording* hay một *replicate group* nhiều recordings?
- [ ] Nếu replicate group gồm nhiều state/excitation → fold hold out **toàn bộ** group; permutation không gán một nhãn cho cả group.
- [ ] Thống nhất tên: File → Recording → Independent Group → Window.
- [ ] Quyết định tên phương pháp: **LORO** (nếu run độc lập) hay **LOGO/leave-one-replicate-group-out**.
- [ ] Cập nhật title/abstract: "Run-Aware" ↔ "Group-Aware" theo unit cuối cùng.

## 2. Registry và data-quality audit
- [ ] `RUN_REGISTRY_LOCKED.csv` tồn tại; mọi raw file khớp đúng một run.
- [ ] `DATASET_FILE_MANIFEST.csv` với checksum; file-count reconciliation PASS.
- [ ] Số run/recording/group đối chiếu với con số báo cáo (6/class, 72 recordings) — ghi rõ chênh lệch nếu có.
- [ ] Data-quality audit: missing/corrupted, clipping, duration mismatch, missing channel/sync.
- [ ] Exclusion ở cấp group/recording, **không** ở cấp window; mọi loại có lý do.

## 3. Leakage audit
- [ ] Group assignment trước windowing (C1-13).
- [ ] Không group nào chia sẻ giữa các fold.
- [ ] Scaling/feature selection/calibration/tuning chỉ fit trên training groups (C1-14).
- [ ] Held-out group không tái sử dụng qua các vòng phân tích.
- [ ] Common folds cho mọi sensor config và model.
- [ ] Provenance (code version, seeds, environment) được giữ.

## 4. Model provenance
- [ ] LR, SVM, RF, 1D-CNN: config, tuning budget, seeds, stopping, software version được ghi và tái lập.
- [ ] Windowing giống nhau giữa các model, hoặc chênh lệch được biện minh.
- [ ] Metric implementation dùng chung một code.

## 5. ResNet1D decision box
```
ResNet1D status: PENDING PROVENANCE VERIFICATION
Required: sensor mode, input channels, folds, seeds, preprocessing, checkpoint hash.
Decision: INCLUDE (đủ provenance) hoặc FORMALLY EXCLUDE (ghi rõ lý do).
```
- [ ] Không đưa ResNet1D vào main results khi chưa xác minh (C1-18).
- [ ] Outline được thiết kế hoàn chỉnh mà không cần ResNet1D.

## 6. CEI
> CEI may be reconsidered only after a formal definition, calibration/reliability analysis and run-aware validation are available.
- [ ] CEI đã loại khỏi outline chính Paper 1.
- [ ] Không mô tả CEI là severity hoặc Health Index.

## 7. Statistical/uncertainty controls
- [ ] Group-preserving full-pipeline permutation; permutation unit = independent group; số permutations + empirical p-value.
- [ ] Không bootstrap individual windows.
- [ ] Không trình bày overlapping fold scores như independent datasets; Wilcoxon/Friedman chỉ *exploratory* (C1-16).
- [ ] Không bịa confidence intervals; phương pháp suy luận cuối được phê duyệt (`[METHOD DECISION REQUIRED]`).

## 8. Reference conflict control
- [ ] Ojala & Garriga: trích JMLR 2010 (pp. 1833–1863), không gắn DOI ICDM 2009, không bịa DOI JMLR.
- [ ] Demšar: một tác giả, 2006, JMLR 7:1–30.
- [ ] Matania: conference paper (PHM Society European Conference 8(1)).
- [ ] Zotero key không xuất hiện trong manuscript/bibliography.
- [ ] Zotero writeback (local-only mode) chưa phải source of truth; xử lý queue trước khi xuất bibliography.

## 9. Gate blockers (chặn Gate 1)
| Blocker | Trạng thái |
|---|---|
| Independent unit chưa khóa | OPEN — số 1 |
| Run registry + file manifest | OPEN |
| Common LORO/LOGO folds chưa chạy | OPEN |
| Split-before-windowing + train-only audit | OPEN |
| ResNet1D provenance | OPEN |
| Permutation + effect size + sensitivity | OPEN |
| Phương pháp suy luận cuối chưa phê duyệt | OPEN |

## 10. Bảng/hình còn thiếu (thay mock bằng dữ liệu thật)
Table 4 (group inventory) · Table 5 (data-quality) · Table 6 (fold registry) · Table 7 (fairness/leakage checklist) · Table 8 (group-level performance) · Table 9 (sensor contrasts) · Table 10 (model contrasts) · Table 11 (per-class/confusion) · Table 12 (sensitivity). Figure 2 (data hierarchy) · Figure 3 (pipeline) · Figures 4–8 (final run-aware plots).

## 11. Thứ tự hoàn thiện
A. Data governance lock → Figure (data hierarchy) + Table 4 (T01, T02).
B. Method lock → pipeline + fold registry + fairness (T05–T08).
C. Final common-fold analysis → Tables 8–11, empirical-null (T10, T11, T13).
D. Robustness + writing → sensitivity (T15); viết Results/Discussion/Conclusion.
E. Submission control → reference metadata, supplementary, declarations.

## 12. Gate 1 readiness
**NOT READY.** READY FOR GATE REVIEW chỉ khi: data hierarchy + Tables 4–7 xác nhận integrity; Tables 8–10 + final plots cung cấp common-fold evidence; empirical-null xác nhận; ResNet1D INCLUDE (có provenance) hoặc FORMALLY EXCLUDE; không còn số preliminary/mock trong claim; không còn blocker ảnh hưởng claim chính. Gate 1 **không** được tuyên bố đóng dựa trên văn liệu hay mock data.
