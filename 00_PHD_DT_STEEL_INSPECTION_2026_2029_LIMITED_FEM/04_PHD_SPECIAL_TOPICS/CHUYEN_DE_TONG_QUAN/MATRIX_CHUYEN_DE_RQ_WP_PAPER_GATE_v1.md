# MA TRẬN LIÊN KẾT — CHUYÊN ĐỀ TỔNG QUAN ↔ LUẬN ÁN
**Phiên bản:** v1 | **Ngày:** 18/07/2026 | **Kiến trúc:** Limited-FEM

---

## Bảng 1. Liên kết phần chuyên đề với RQ/WP/Paper/Gate

| Phần chuyên đề | RQ | WP | Paper | Gate | Evidence type | Scope |
|---|---|---|---|---|---|---|
| Ch.1 Mở đầu | — | — | — | — | — | Nền tảng |
| Ch.2 Cơ sở khái niệm DT | — | — | — | — | BACKGROUND / NORMATIVE | Core (DT definition) |
| Ch.3.1–3.2 Vibration data & labelled lab | RQ1 | WP1 | Paper 1 | Gate 1 | LABORATORY EVIDENCE | Core |
| Ch.3.3 Classification vs anomaly vs diagnosis | RQ1, RQ3 | WP1, WP3 | Paper 1, 3 | Gate 1, 4 | METHODOLOGICAL | Core |
| Ch.3.4 Run-aware & leakage control | RQ1 | WP1 | Paper 1 | Gate 1 | METHODOLOGICAL | Core |
| Ch.3.5 Sensor config vs model choice | RQ1 | WP1 | Paper 1 | Gate 1 | LABORATORY EVIDENCE | Core |
| Ch.3.6 Small-n uncertainty | RQ1 | WP1 | Paper 1 | Gate 1 | METHODOLOGICAL | Core |
| Ch.4.1–4.2 Sensor_ID → BIM_GUID mapping | RQ2 | WP2 | Paper 2 | Gate 2 | INFORMATION TRACEABILITY | Core |
| Ch.4.3 Provenance & bidirectional queries | RQ2 | WP2 | Paper 2 | Gate 3 | INFORMATION TRACEABILITY | Core |
| Ch.4.4 Constraint & invalid-data tests | RQ2 | WP2 | Paper 2 | Gate 3 | INFORMATION TRACEABILITY | Core |
| Ch.4.5 Sensor qualification | RQ3 | WP3 | Paper 3 | Gate 4 | FIELD FEASIBILITY | Supporting |
| Ch.4.6 Operational baseline & anomaly evidence | RQ3 | WP3 | Paper 3 | Gate 4 | FIELD FEASIBILITY | Core |
| Ch.4.7 Environmental/operational variability | RQ3 | WP3 | Paper 3 | Gate 4 | FIELD FEASIBILITY | Core |
| Ch.5.1–5.3 Decision support & 4 mức hành động | — (WP4) | WP4 | Paper 4 (opt.) | Gate 5 | MANAGEMENT DECISION SUPPORT | Core |
| Ch.5.4 Vai trò và giới hạn FEM | — | — | — | — | BACKGROUND | Supporting |
| Ch.6.1 Khoảng trống nghiên cứu | RQ1–3 | WP1–4 | Paper 1–4 | Gate 1–5 | Tổng hợp | Core |
| Ch.6.2 Kiến trúc nghiên cứu đề xuất | RQ1–3 | WP1–4 | Paper 1–4 | Gate 1–5 | Tổng hợp | Core |
| Ch.7 Kết luận | — | — | — | — | — | Nền tảng |

---

## Bảng 2. Liên kết CH tổng quan với RQ luận án

| CH tổng quan | Nội dung | RQ luận án tương ứng | Paper | Gate |
|---|---|---|---|---|
| CH1 | Định nghĩa và phân loại DT; mức tự động hóa | Nền tảng lý luận (không có RQ riêng) | — | — |
| CH2 | Vibration → condition evidence; rủi ro giảm độ tin cậy | RQ1 | Paper 1 | Gate 1 |
| CH3 | Sensor config; run-aware; LORO; uncertainty | RQ1 | Paper 1 | Gate 1 |
| CH4 | BIM/IFC linking; provenance; inspection records | RQ2 | Paper 2 | Gates 2–3 |
| CH5 | Field unlabelled data; baseline; anomaly evidence | RQ3 | Paper 3 | Gate 4 |
| CH6 | Human-reviewed decision support; 4 mức hành động | WP4 (không có RQ4) | Paper 4 (opt.) | Gate 5 |
| CH7 | Khoảng trống tích hợp toàn chuỗi | Tổng hợp RQ1–3 | — | — |

---

## Bảng 3. Chuỗi nghiên cứu đã khóa → vị trí trong chuyên đề

| Mắt xích chuỗi | Chuỗi định danh | Chương chuyên đề | RQ/WP |
|---|---|---|---|
| Vibration data | Sensor_ID | Ch.3 | RQ1/WP1 |
| Condition/state-change evidence | Condition_Evidence_ID | Ch.3 | RQ1/WP1 |
| BIM-linked component | BIM_GUID | Ch.4.1–4.4 | RQ2/WP2 |
| Inspection record | Inspection_Record_ID | Ch.4.1–4.4 | RQ2/WP2 |
| Action support | Action_Status | Ch.5.1–5.3 | WP4 |
| Field feasibility | (toàn chuỗi tại field) | Ch.4.5–4.7 | RQ3/WP3 |

**Ghi chú:** FEM_Node_ID chỉ là metadata tùy chọn, không phải mắt xích bắt buộc trong chuỗi.

---

## Bảng 4. Phân loại Scope theo phần chuyên đề

| Scope | Các phần chuyên đề |
|---|---|
| **Core** | Ch.3 (evidence & reliability); Ch.4.1–4.4 (traceability); Ch.4.6–4.7 (field feasibility); Ch.5.1–5.3 (decision support); Ch.6 (gaps & architecture) |
| **Supporting** | Ch.2 (DT concepts); Ch.4.5 (sensor qualification); Ch.5.4 (FEM role) |
| **Future Work** | Calibrated FEM; RUL; predictive maintenance; multi-building deployment |
| **Out of Scope** | Field damage diagnosis; calibrated FEM trong core; stiffness degradation; weighted Health Index; Edge AI; Smart City; autonomous maintenance |
