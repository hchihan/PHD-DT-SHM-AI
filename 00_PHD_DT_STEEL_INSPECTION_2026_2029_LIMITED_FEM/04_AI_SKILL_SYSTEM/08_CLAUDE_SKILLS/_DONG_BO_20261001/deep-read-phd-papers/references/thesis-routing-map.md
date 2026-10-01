# Thesis routing map

> **Đồng bộ 01/10/2026 với CLAUDE.md của dự án Tiểu luận tổng quan.** Khi làm việc cho tiểu luận, đọc `CLAUDE.md` của dự án trước và tệp `references/project-canon-tltq.md`; hai tệp này thắng mọi bản tóm tắt cứng trong skill (chuỗi định danh tuyến tính, câu chữ khoảng trống "đã khóa", nơi ghi kết quả). K1–K3 là giả thuyết làm việc, chỉ chốt ở Điểm duyệt 3.


Snapshot basis: `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` and `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md`. Current supplied source-of-truth files override this snapshot.

## Locked chain (narrative) and data model

Đồng bộ 01/10/2026: chuỗi dưới đây là **chuỗi trình bày** và **chuỗi định danh lõi**; mô hình dữ liệu là **schema đồ thị** (COMPONENT, MODEL_VERSION, SENSOR, SENSOR_MAPPING có thời hạn, OBS_CONTEXT, EVIDENCE, VALIDITY_SCOPE, EVIDENCE_USE, INSPECTION_RECORD, ACTION với hai trục priority_level / Action_Status, STATUS_EVENT, AGENT; ràng buộc C1–C8) theo `project-canon-tltq.md` §3. STATUS_EVENT là thực thể bắt buộc. Chi tiết chuỗi định danh chuyển sang Phụ lục A của tiểu luận.


`Vibration data → condition/state-change evidence → BIM-linked component → inspection record → inspection-maintenance action support`

Identifier chain:

`Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status`

`FEM_Node_ID` is optional metadata only.

## Literature-review routing (tiểu luận v2)

Dùng bảng ở `project-canon-tltq.md` §8 (1.2–1.4, 2.1–2.3, 3.1–3.7, Ch.4, 5.2, 5.5, 5.6, 5.7, mục giới hạn, Phụ lục A–C). AI theo gói: WP1 RF, SVM-RBF, 1D-CNN, ResNet1D; WP2 LLM trích xuất hồ sơ có kỹ sư xác nhận; WP3 Autoencoder + bù EOV + học chủ động; WP4 luật minh bạch bốn mức.

## Routing table

| Primary theme in a paper | RQ | WP | Thesis chapter | Target paper | Gate | Evidence type |
|---|---|---|---|---|---|---|
| Run-aware vibration classification; leakage control; sensor configuration; reproducibility | RQ1 | WP1 | C4 | Paper 1 | G1 | Laboratory evidence |
| Formal identifiers; BIM/IFC linkage; competency questions; bidirectional evidence-to-record traceability | RQ2 | WP2 | C5 | Paper 2 | G2–G3 | Information traceability |
| Real-building deployment; operational baseline; mapping; inspection workflow under limited field damage data | RQ3 | WP3 | C6 | Paper 3 | G4 | Field feasibility |
| Transparent Normal → Watch → Inspect → Priority Inspection logic; scenario or expert review | RQ3 | WP4 | C7 | Paper 4 or merged Paper 3 | G5 | Management decision support |
| Definitions, theory, prior work, or evidence of a gap without a direct method contribution | Cross-cutting | Supporting | C2, sometimes C3 | Background only | None | Literature evidence |

## Scope classification

- `Core Scope`: directly supplies a method, evaluation criterion, result type or gap evidence for one locked RQ/WP.
- `Supporting Scope`: contextual theory, standards, nominal FEM reference, terminology or transferable method that does not answer an RQ by itself.
- `Future Work`: defensible post-PhD extension explicitly separated from current proof obligations.
- `Out of Scope`: conflicts with the locked thesis or belongs to another independent research line.

## FEM firewall

Permitted only as a nominal, uncalibrated, reference-only design model for reference-informed sensor placement, component illustration or qualitative hypotheses labelled unconfirmed.

Prohibited: calibrated FEM, damage diagnosis, bolt-preload or stiffness-degradation inference, quantitative lab-to-field transfer, optimal sensor placement, or any FEM-specific RQ/WP/chapter/paper/Gate.

## Current priority

Read the latest authoritative current-status or Gate-specific source every time. Do not hard-code the active Gate, run count, model status, model metrics, field-access status or next action in this routing snapshot. If no current source is available, write `Evidence is currently insufficient.`
