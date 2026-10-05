# SIX STRUCTURAL FIXES — IMPLEMENTATION REPORT
**Date:** 2026-07-19 | Under Charter v2.1. Không mở rộng phạm vi; không sửa dữ liệu/metric/citation khoa học.

| Structural issue | Files affected | Change made | Validation result | Remaining limitation |
|---|---|---|---|---|
| **1. Chuỗi định danh cuối = Action_Record_ID** (Action_Status là thuộc tính) | ADR mới `RESEARCH_ARCHITECTURE_DECISION_RECORD_ACTION_ID_20260719.md`; Charter v2.1 §2.2; EVIDENCE_GATES_v2.1 G2; MATRIX §6; AGENT_RULES; CLAUDE.md; concise charter; RESEARCH_ARCHITECTURE; TERMINOLOGY; Paper 2 direction | Chain đổi thành `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Record_ID`; Action_Record_ID truy được evidence/CEI/component/inspection/role/timestamp/version/approval/legal ref | Keyword check: các file CURRENT chỉ dùng Action_Status như thuộc tính | Evidence-base snapshots, coursework, discovery prompts và Council doc giữ notation cũ (không sửa evidence); reconcile khi revise |
| **2. Định nghĩa accountability** (không phải trách nhiệm pháp lý) | Charter §2.4; TERMINOLOGY §5; Paper 2 direction (+ chỉ dẫn đưa vào CQ và schema) | Định nghĩa khóa: truy vết role/evidence/creator/approver/timestamp/version/approval status; KHÔNG quy lỗi pháp lý | Định nghĩa xuất hiện nhất quán ở 3 file; G2 yêu cầu đưa vào CQ + Action_Record schema | CQ và Inspection/Action schema chưa pre-register (G2) — sẽ nhúng định nghĩa khi soạn |
| **3. Evidence Gates: checklist → execution gate** | EVIDENCE_GATES_v2.1 (rewrite) | Mỗi Gate item có: Required artifact / Acceptance criterion / Evidence path / Owner / Reviewer-sign-off / Status. G1 liệt kê 15 artifact (dataset/registry/manifest/provenance/folds/split/preprocessing/seeds/config/metrics/uncertainty/ResNet1D/rerun/sign-off) | "Không PASS chỉ vì code chạy" ghi rõ; status = OPEN | Artifacts G1 chưa được tạo (xem G1_EXECUTION_PACK) |
| **4. Milestone M1 Paper 1 Submission Readiness** (không phải Gate mới) | EVIDENCE_GATES_v2.1 (M1 dưới G1); MATRIX (note M1) | M1 = G1 closed + claim table locked + candidate resolved + reproducibility + limitations + LORO figures → submission-ready | M1 gắn dưới G1, không tạo Gate mới | M1 OPEN cho tới khi G1 PASS |
| **5. "workstation-only" → "field-site independent"** | MATRIX (spine); TERMINOLOGY (rule) | Thay bằng "field-site independent and can progress without access to Rapexco" | Keyword check: không CURRENT file nào dùng workstation-only làm live term | — |
| **6. Tách field preparation vs field deployment** | Charter §6.1; MATRIX; RESEARCH_DIRECTION_AND_SCOPE; CURRENT_STATUS; Paper 3 direction | Preparation (agreement/BIM-GUID audit/register/mapping/template/scenarios/utilities) được phép sớm; Deployment (lắp cảm biến/baseline dài hạn/validation/Paper 3) sau khi G4 mở | Nhất quán 5 file; minimum field evidence vẫn mandatory | Field-access agreement chưa ký (điều kiện deployment) |

## Tổng kết
- 6/6 vấn đề cấu trúc đã thực hiện.
- Không tạo RQ/WP/chương/Paper/Gate mới; M1 là milestone, không phải Gate.
- Không sửa evidence/metric/citation khoa học.
