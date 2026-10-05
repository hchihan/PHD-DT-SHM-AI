# RQ – WP – CHAPTER – PAPER – GATE MATRIX — v2.1
**Version:** v2.4 | **Issued:** 2026-07-19 | **Updated:** 13/09/2026
**Status:** CURRENT | **Source-of-truth level:** 4
**Supersedes:** v2.3 matrix (retained at `../90_ARCHIVE/01_SUPERSEDED_VERSIONS/PRE_SYNC_20260913/01_CURRENT_CONTROL/`). | **Superseded by:** None.
**Changes in this version:** Adds §5A (Paper 1 claim status after the 13/09/2026 science lock) and synchronization notes under §1 and §7. Architecture rows, RQ wording and Gate states are unchanged. (v2.3 restored the 17/07 canonical chain, prevented schema-first G2–3 execution and recorded Gate status through 11/08/2026.)
**Rule:** Không tạo thêm RQ/WP/chương/Paper/Gate. FEM is nominal, uncalibrated, reference-only, not used for damage diagnosis and has no separate RQ/WP/chapter/Paper/Gate.

---

## 1. Ma trận trục chính

| RQ | Câu hỏi (rút gọn) | WP | Chapter | Paper | Evidence Gate(s) | Bằng chứng chủ đạo | Vai trò QLXD |
|---|---|---|---|---|---|---|---|
| **RQ1** | Lab evidence dưới run-aware/LORO; sensor config có chi phối kiến trúc? | WP1 | C4 | Paper 1 (Sensors, primary) | **G1** | Run registry, LORO, sensor-config effect, CEI by-product | Bằng chứng lab có định lượng độ tin cậy |
| **RQ2** | Tổ chức evidence + CEI thành chuỗi truy vết để hỗ trợ quyết định kiểm tra | WP2 | C5 | Paper 2 | **G2, G3, G6** | Canonical identifiers; approved competency questions and verification criteria; then schema/constraints/fixtures/oracle | **CORE — trụ cột nhận diện ngành QLXD** |
| **RQ3** | Field feasibility tại Rapexco dưới limited field damage data | WP3 | C6 | Paper 3 (bonus, JCSHM / Q2–Q3) | **G4, G5** | Field sensor register, Sensor→BIM, baseline, traceability scenarios | Bằng chứng khả thi hiện trường |
| — | Decision-support synthesis (4-level) | WP4 (gộp WP2/WP3) | C7 (opt., merge C6) | Paper 4 (opt., merge Paper 3) | **G5** | Transparent 4-level logic, expert review | Hỗ trợ quyết định minh bạch, human-reviewed |

Trục chịu lực: **C4 (Paper 1/RQ1) + C5 (Paper 2/RQ2)** — **field-site independent and can progress without access to Rapexco**, chạy song song ngay (có thể vẫn cần kiểm tra cảm biến/metadata hoặc bổ sung thí nghiệm — chỉ nghĩa là không phụ thuộc công trình thực). C6 (Paper 3/RQ3, Rapexco): **field preparation** được phép làm sớm; **field deployment** chỉ sau khi Paper 1–2 ổn định và G4 mở (xem Charter §6.1).

**Milestone M1 — Paper 1 Submission Readiness** nằm dưới G1 (không phải Gate mới): G1 closed + final claim table locked + candidate claims resolved + reproducibility package + limitations + figures/tables từ LORO → Paper 1 sẵn sàng nộp. Chi tiết: `EVIDENCE_GATES_v2.1.md`.

> **Sync note 13/09/2026 (architecture rows unchanged).** Two architectures currently disagree.
> - The rows above follow Charter v1.1 §10–11 and Charter v2.1 §4–5, and include G6, "bonus", Paper 4 and C7 entries.
> - The locked architecture used in the 13/09 supervisor materials and in `../README.md` is: Paper 2 → G2–G3; Paper 3 → G4–G5; WP4 = decision-support synthesis without a mandatory paper; no G6.
>
> The rows are not changed here. The conflict is recorded as C-01 in `PAPER1_SCIENCE_LOCK_PROJECT_SYNC_REPORT_20260913.md` and requires a supervisor decision and ADR.

---

## 2. Chapter ↔ RQ ↔ Paper

| Chapter | Nội dung | RQ | Paper | Vai trò QLXD |
|---|---|---|---|---|
| C1 | Giới thiệu; bối cảnh quản lý tài sản nhà thép ven biển | — | — | Đóng khung vấn đề quản lý |
| C2 | Literature & gap = thiếu chuỗi evidence→component→record→justified action | — | — | Định vị gap là gap quản lý, không phải kỹ thuật |
| C3 | Research framework; DT management-maturity; FEM nominal, uncalibrated, reference-only, not used for damage diagnosis | — | — | Tuyên bố đóng góp tích cực; không có chương FEM |
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
| **WP2 — Traceability-to-decision (CORE)** | Canonical chain + CEI; approve competency questions and verification criteria before schema; then invalid-data tests and legal mapping | Verifiable traceability-to-decision framework | G2, G3, G6 |
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

## 5A. Paper 1 claim status after the science lock (sync 13/09/2026)

This section records status only. It does not amend the Charter claims (sync report C-02, C-03, C-04). Until G1 PASS, every row remains "Candidate claim pending Gate 1 closure."

Final evidence:
- `../03_OUTPUTS/03_PAPER_1A_GATE1/Paper 1.md/PAPER1_v8.1_SHM_RISK_REDUCED.docx` (v8.1)
- `../03_OUTPUTS/03_PAPER_1A_GATE1/BAO_CAO_IT01_IT06.md`

| Claim (governance wording) | Status at 13/09/2026 | Final Paper 1 evidence | Decision required |
|---|---|---|---|
| Sensor configuration dominates architecture | **Not claimed in Paper 1; not supported by current evidence.** Moved to Paper 1B (supporting scope) | v8.1 §3.3 analyses only the fullest configuration. The sensor-subset block is single-seed and does not separate configuration effects from fold variability in CP2/CP3 (technical verdict 07/09/2026) | Supervisor to retire or re-scope the Charter v1.1 §13 / v2.1 §10 wording (C-02) |
| RF ~0.862; 1D-CNN S12 ~0.841; ResNet1D ~0.828 | **Superseded values** | v8.1 Table 4 pooled Macro-F1 (CP1 / CP2 / CP3): RF 1.000 / 0.986 / 0.875; SVM-RBF 1.000 / 0.986 / 0.690; ResNet1D 0.930 / 0.959 / 0.523; 1D-CNN 0.727 / 0.777 / 0.399 | Replace in the next Charter revision (C-03) |
| ResNet1D corroborates the finding | **Not claimed.** ResNet1D is retained as one of four models; its sensor/input mode is technically verified | Audit of 24/08/2026; technical verdict of 07/09/2026; IT-05 (612 checkpoints reproduced) | Standalone `RESNET1D_PROVENANCE_AUDIT.md` in the G1 pack |
| Laboratory evidence distinguishes controlled connection states under leakage-controlled evaluation | **Locked in the manuscript**; candidate pending G1 | RF/SVM pooled Macro-F1 above, under LORO with recording-level scoring. Deep-model dependence on hyperparameter development is disclosed | G1 sign-off (C-04) |
| Cross-campaign transportability | **Exploratory; validated transfer not established.** No LOCO protocol was executed | v8.1 Table 7: CP2 ↔ CP3, deep models only, mean balanced accuracy 0.227–0.278. CP1 not evaluated | None |

---

## 6. Quy tắc bất biến

1. FEM: nominal, uncalibrated, reference-only, not used for damage diagnosis — không RQ/WP/chương/Paper/Gate riêng.
2. Chuỗi định danh: `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status`. `Asset_ID`, `Model_Version_ID`, `Action_Record_ID`, `Workflow_Status` và `Status_Event` chỉ là noncanonical implementation metadata/proposals. `FEM_Node_ID` chỉ optional metadata.
3. CEI là first-class metadata attribute của `Condition_Evidence_ID`, không phải scalar/Health Index/severity.
4. Legal mapping neo nghĩa vụ quản lý; không tạo ngưỡng kỹ thuật.
5. Bốn lớp bằng chứng tách biệt; không "mượn" chéo.

## 7. Current gate state (11/08/2026; re-confirmed 13/09/2026)

| Gate | Status |
|---|---|
| G1 | `OPEN — PARTIAL EVIDENCE` |
| G2 | `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN` |
| G3 | `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED`; execution `NOT OPEN` pending G2 baseline |
| G4 | Readiness/preparation only; field-access confirmation required before deployment |
| G5 | OPEN; expert-reviewed management decision-support evidence missing |

No Gate is PASS. **Evidence is currently insufficient.**

Sync 13/09/2026: Gate states are unchanged. Paper 1 is `SCIENCE LOCKED`, which is a paper status, not a gate state. G1 still lacks a materialized `G1_EXECUTION_PACK` and a signed `G1_ACCEPTANCE_MATRIX.md` (sync report §3).
