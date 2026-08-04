# PAPER 1 / GATE 1 — CLAIM–EVIDENCE AUDIT (v2)
**Date:** 2026-07-18 | **Current manuscript source:** `../../../90_ARCHIVE/HISTORICAL_UNIQUE_FILES/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Paper 1/PAPER1_GATE1_Q2_VERIFIED_EVIDENCE_REVISED_v2_MANUSCRIPT_SOURCE_20260718.md` | Referenced DOCX v2 is absent and must be regenerated if required.
**Status options:** VERIFIED / PENDING PROJECT DATA / REWRITE / REMOVE / SUPPORTING ONLY

## A. Core methodological claims (from verified claim register)

| Claim | Project evidence | Literature evidence | Limitation | Status |
|---|---|---|---|---|
| C1-12 Independent run/group is the effective split and inference unit | Run registry chưa khóa | Beleites 2013; Tougui 2021; Matania 2024; Wheat 2024 | Domains differ; exact steel-frame design not validated | VERIFIED (methodological) |
| C1-13 Group assignment must precede windowing / whole source groups intact | Split-before-windowing audit chưa có | Matania 2024 (direct); Wheat 2024; Tougui 2021 | Some sources window first but preserve groups | VERIFIED (methodological); project audit PENDING |
| C1-14 Learned preprocessing fitted on training groups only | Preprocessing audit chưa có | Tougui 2021; Wheat 2024 | Exact scaler implementations not always reported | VERIFIED (methodological); project audit PENDING |
| C1-15 Small independent-group counts require explicit uncertainty + empirical chance | Permutation chưa chạy | Beleites 2013; Combrisson & Jerbi 2015; Ojala & Garriga 2010 | No source proves adequacy at ~6 runs/class | VERIFIED (methodological); project analysis PENDING |
| C1-16 Wilcoxon/Friedman requires independent paired units; overlapping LORO folds are not independent datasets | N/A | Demšar 2006 | Exploratory use only | VERIFIED |
| C1-17 Sensor configuration may materially affect apparent classification performance | Final LORO chưa có | Wheat 2024 (direct, bearings) | Bearing sensors ≠ steel-frame configuration | VERIFIED as possibility; project quantification PENDING PROJECT DATA |
| C1-18 Literature cannot verify project ResNet1D sensor mode/provenance | Provenance chưa xác minh | Absence across reviewed corpus | Missing provenance cannot be repaired by literature | VERIFIED; include/exclude decision PENDING |

## B. Ten strictly controlled claims (prompt §11)

| # | Claim | Project evidence | Literature evidence | Limitation | Status |
|---|---|---|---|---|---|
| 1 | Random-window leakage inflates apparent performance | Chưa chạy leakage-prone vs leakage-safe contrast trên data dự án | Matania 2024; Wheat 2024; Tougui 2021; Goodarzi 2025 | Project numbers absent; manuscript §6.1 chỉ nêu rationale | VERIFIED (literature); project contrast PENDING PROJECT DATA |
| 2 | Run as independent unit | Run registry chưa khóa | Beleites 2013 + nhóm C1-12 | — | VERIFIED (methodological) |
| 3 | Adequacy of LORO for this dataset | LORO chưa thực thi | Tougui 2021 (LOGO rationale) | No source validates ~6 runs/class | PENDING PROJECT DATA; manuscript dùng placeholder |
| 4 | Sensor-configuration effect (S1/S2/S1+S2) | Chỉ có số sơ bộ single-split — không dùng | Wheat 2024 | Không được suy ra optimality | PENDING PROJECT DATA |
| 5 | Model-family differences | Số sơ bộ single-split — không dùng | Demšar 2006 (framework + caveat) | Small n; conservative language bắt buộc | PENDING PROJECT DATA |
| 6 | Statistical significance | Chưa có permutation output | Ojala & Garriga 2010; Combrisson & Jerbi 2015 | Method decision chưa phê duyệt | PENDING PROJECT DATA + METHOD DECISION REQUIRED |
| 7 | ResNet1D inclusion | Provenance thiếu | C1-18 | — | PENDING (include/exclude quyết định bởi T09) |
| 8 | CEI interpretation | Chưa có definition/calibration/run-aware evaluation | — | CEI = confidence/evidence indicator, không phải severity | REMOVE khỏi main results; giữ như future analysis request (§5.8) |
| 9 | Asset-management relevance | N/A (khung lập luận) | Charter §2; bounded theo §6.5 | Không claim maintenance effectiveness / field readiness | SUPPORTING ONLY |
| 10 | Gate 1 closure | Thiếu toàn bộ artifact chặn gate (T01–T11, T13) | Literature không thể đóng gate | — | NOT CLOSED — manuscript ghi rõ "Gate 1 is not yet closed" |

## C. Draft claims removed (audit trail — xem thêm MAJOR_REVISION_LOG_v2)

| Draft claim | Decision | Reason |
|---|---|---|
| DSI ordinal proxy, Pearson R = 0.953, RMSE/MAE | REMOVE | Severity/DSI prohibited; số sơ bộ single-split |
| "Softmax preserves severity" | REMOVE | Prohibited terminology + unverified |
| RF macro-F1 0.862 / CNN 0.841 / mọi số Table 6–9 | REMOVE (thay bằng placeholder) | PRELIMINARY — NOT VERIFIED UNDER FINAL LORO PROTOCOL |
| "Adding a sensor > switching algorithm" (định lượng) | REWRITE | Chỉ được nêu sau final LORO (§6.2) |
| RF outperforms 1D-CNN under small data | REWRITE | Không claim superiority từ single split |
| BCJ "catastrophically" undetectable từ S2 (F1=0.475) | REMOVE | Số sơ bộ |
| FEM model updating / physics-informed DSI / OSP future work | REMOVE | Out of Scope (Limited-FEM) |
| Field validation (ADXL345/CV) as planned result | REMOVE | Out of Scope cho Paper 1; field = feasibility only, thuộc Paper 3 |
| Digital Twin platform integration | REMOVE | Overclaim ngoài phạm vi Paper 1 |
