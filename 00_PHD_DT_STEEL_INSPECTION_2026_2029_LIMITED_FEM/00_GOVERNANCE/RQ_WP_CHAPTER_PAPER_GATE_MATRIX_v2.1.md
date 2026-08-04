# RQ – WP – CHAPTER – PAPER – GATE MATRIX — v2.1
**Version:** v2.1 | **Date:** 2026-07-19 | **Status:** CURRENT (dưới `MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`)
**Rule:** Không tạo thêm RQ/WP/chương/Paper/Gate. Không có thành phần FEM. Khi mâu thuẫn với file khác, Charter v2.1 và file này thắng.

---

## 1. Ma trận trục chính

| RQ | Câu hỏi (rút gọn) | WP | Chapter | Paper | Evidence Gate(s) | Bằng chứng chủ đạo | Vai trò QLXD |
|---|---|---|---|---|---|---|---|
| **RQ1** | Lab evidence dưới run-aware/LORO; sensor config có chi phối kiến trúc? | WP1 | C4 | Paper 1 (Sensors, primary) | **G1** | Run registry, LORO, sensor-config effect, CEI by-product | Bằng chứng lab có định lượng độ tin cậy |
| **RQ2** | Tổ chức evidence + CEI thành chuỗi truy vết để justify & truy trách nhiệm quyết định kiểm tra | WP2 | C5 | Paper 2 (AutCon / JBE / B&E) | **G2, G3, G6** | Identifier chain + CEI, SCQ/VCQ/RCQ, invalid-data test, legal mapping | **CORE — trụ cột nhận diện ngành QLXD** |
| **RQ3** | Field feasibility tại Rapexco dưới limited field damage data | WP3 | C6 | Paper 3 (bonus, JCSHM / Q2–Q3) | **G4, G5** | Field sensor register, Sensor→BIM, baseline, traceability scenarios | Bằng chứng khả thi hiện trường |
| — | Decision-support synthesis (4-level) | WP4 (gộp WP2/WP3) | C7 (opt., merge C6) | Paper 4 (opt., merge Paper 3) | **G5** | Transparent 4-level logic, expert review | Hỗ trợ quyết định minh bạch, human-reviewed |

Trục chịu lực: **C4 (Paper 1/RQ1) + C5 (Paper 2/RQ2)** — **field-site independent and can progress without access to Rapexco**, chạy song song ngay (có thể vẫn cần kiểm tra cảm biến/metadata hoặc bổ sung thí nghiệm — chỉ nghĩa là không phụ thuộc công trình thực). C6 (Paper 3/RQ3, Rapexco): **field preparation** được phép làm sớm; **field deployment** chỉ sau khi Paper 1–2 ổn định và G4 mở (xem Charter §6.1).

**Milestone M1 — Paper 1 Submission Readiness** nằm dưới G1 (không phải Gate mới): G1 closed + final claim table locked + candidate claims resolved + reproducibility package + limitations + figures/tables từ LORO → Paper 1 sẵn sàng nộp. Chi tiết: `EVIDENCE_GATES_v2.1.md`.

---

## 2. Chapter ↔ RQ ↔ Paper

| Chapter | Nội dung | RQ | Paper | Vai trò QLXD |
|---|---|---|---|---|
| C1 | Giới thiệu; bối cảnh quản lý tài sản nhà thép ven biển | — | — | Đóng khung vấn đề quản lý |
| C2 | Literature & gap = thiếu chuỗi evidence→component→record→justified action | — | — | Định vị gap là gap quản lý, không phải kỹ thuật |
| C3 | Research framework; tự định nghĩa DT management-maturity; vai trò FEM danh nghĩa | — | — | Tuyên bố đóng góp tích cực |
| C4 | Lab evidence; run-aware/LORO; sensor-config effect; CEI | RQ1 | Paper 1 | Bằng chứng có định lượng độ tin cậy |
| C5 | Traceability-to-decision: identifier chain + CEI; SCQ/VCQ/RCQ; legal mapping | RQ2 | Paper 2 | **CORE — trụ cột định danh** |
| C6 | Rapexco field feasibility: Sensor→BIM mapping, baseline, inspection workflow | RQ3 | Paper 3 (bonus) | Bằng chứng khả thi |
| C7 | (optional, có thể gộp C6) extended 4-level logic + expert review | RQ3 | Paper 4 (opt.) | — |
| C8 | Kết luận, đóng góp, hướng mở rộng post-PhD | — | — | — |

**Không có chương FEM.**

---

## 3. Work packages

| WP | Nội dung | Output chính | Gate |
|---|---|---|---|
| **WP1 — Lab evidence** | Labelled dataset, run registry, sensor configs, run-aware/LORO, CEI by-product | Reproducible lab evidence với confidence — không phải field diagnosis | G1 |
| **WP2 — Traceability-to-decision (CORE)** | Formal chain + CEI attribute, identifier schema, pre-registered SCQ/VCQ/RCQ, invalid-data test, legal mapping | Verifiable, accountable traceability-to-decision framework | G2, G3, G6 |
| **WP3 — Field feasibility (bonus publication; evidence mandatory)** | Rapexco deployment (reference-informed placement), operational baseline, Sensor→BIM, traceability scenarios | Field-feasibility evidence — không phải field damage diagnosis | G4, G5 |
| **WP4 — Decision-support synthesis** | Extended Normal→Watch→Inspect→Priority logic, case scenarios; **gộp vào WP2 hoặc WP3** | Transparent, unweighted, human-reviewed decision logic | G5 |

---

## 4. Field feasibility: publication vs evidence (bắt buộc phân biệt)

| Hạng mục | Trạng thái | Ghi chú |
|---|---|---|
| Paper 3 publication | **Optional / bonus** | Ngoài critical path; chỉ làm nếu site window cho phép |
| Minimum field feasibility evidence | **MANDATORY cho luận án** | field sensor register; Sensor_ID→BIM_GUID; data return & completeness; operational baseline; inspection-record workflow; 2–3 traceability scenarios |

Không yêu cầu field damage diagnosis.

---

## 5. Trạng thái Paper 1 claims

| Claim | Trạng thái | Điều kiện chuyển sang allowed |
|---|---|---|
| Sensor configuration dominates architecture | **Candidate pending G1** | Gate 1 đóng |
| RF macro-F1 ~0.862 leads; 1D-CNN S12 ~0.841; ResNet1D ~0.828 | **Candidate pending G1** | run registry khóa; split-before-windowing; LORO; preprocessing train-only; common seeds; run-level uncertainty |
| ResNet1D corroborates finding | **Candidate pending G1** | ResNet1D sensor mode & provenance verified |

Trước G1, mọi con số trên phải ghi **"Candidate claim pending Gate 1 closure."**

---

## 6. Quy tắc bất biến

1. FEM: nominal, uncalibrated, reference-only, not used for damage diagnosis — không RQ/WP/chương/Paper/Gate riêng.
2. Chuỗi định danh: `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Record_ID`. `Action_Status` là **thuộc tính** của `Action_Record_ID` (không phải mắt xích — ADR Action_ID 20260719). `FEM_Node_ID` chỉ optional metadata.
3. CEI là first-class metadata attribute của `Condition_Evidence_ID`, không phải scalar/Health Index/severity.
4. Legal mapping neo nghĩa vụ quản lý; không tạo ngưỡng kỹ thuật.
5. Bốn lớp bằng chứng tách biệt; không "mượn" chéo.
