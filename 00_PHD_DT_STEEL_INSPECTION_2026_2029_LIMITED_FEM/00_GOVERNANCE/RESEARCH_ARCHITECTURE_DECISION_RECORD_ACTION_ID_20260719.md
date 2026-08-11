# ADR — ACTION_RECORD_ID (data-model correction) — 2026-07-19
**Version:** v1.1 administrative annotation | **Status:** ACCEPTED | **Decision date:** 2026-07-19 | **Updated:** 2026-08-04
**Source-of-truth level:** 3 | **Type:** data-model correction (KHÔNG mở rộng phạm vi)
**Supersedes:** Identifier notation ending in `Action_Status`. | **Superseded by:** None.
**Change summary:** Adds a non-normative reconciliation note for the proposed Status_Event naming; the accepted Action_Record_ID decision is unchanged.
**Under:** `MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`. Bổ sung cho `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260719.md`.

## Context
Chuỗi định danh v2.0/v2.1 kết thúc bằng `Action_Status`. Nhưng `Action_Status` là **một thuộc tính trạng thái** (Normal/Watch/Inspect/Priority; hoặc open/closed…), **không phải một định danh**. Một chuỗi truy vết (traceability chain) phải kết thúc bằng một **identifier** ổn định để round-trip và audit được. Dùng thuộc tính làm mắt xích cuối là lỗi mô hình dữ liệu, làm hỏng tính accountable của chuỗi.

## Decision
Chuẩn hóa mắt xích cuối thành một identifier:

```text
Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Record_ID
```

Trong đó:
- **CEI** là thuộc tính của `Condition_Evidence_ID`.
- **`Action_Status`** là **thuộc tính** của `Action_Record_ID` (không phải mắt xích định danh).
- **`Action_Record_ID`** phải truy được: evidence (`Condition_Evidence_ID`), CEI, component (`BIM_GUID`), inspection record (`Inspection_Record_ID`), **role**, **timestamp**, **version**, **approval status**, và **management/legal reference áp dụng**.

Đây là **sửa lỗi mô hình dữ liệu**, không thêm RQ/WP/chương/Paper/Gate, không thêm phạm vi nghiên cứu. Trục evidence không đổi (vẫn kết thúc ở "justified, accountable inspection–maintenance action" — nay hiện thực hóa qua `Action_Record_ID`).

## Consequences
- Chuỗi cũ (`…→ Action_Status`) được coi là **superseded notation**; mọi file CURRENT v2.x dùng `Action_Record_ID`.
- Không để hai chuỗi định danh khác nhau cùng tồn tại trong file CURRENT.
- `Action_Status` chỉ xuất hiện như thuộc tính của `Action_Record_ID`.
- Liên quan status-event history: `Action_Status_Event_ID` (prior/new status, actor, timestamp, reason) là con của `Action_Record_ID` — nhất quán với RQ2 addendum C2-17.

## Scope of change (files CURRENT được cập nhật)
Charter v2.1 (§2.2); EVIDENCE_GATES_v2.1 (G2); RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1; AGENT_RULES; CLAUDE.md; MASTER_RESEARCH_CHARTER.md (concise); RESEARCH_ARCHITECTURE.md; TERMINOLOGY_CONTROL_CURRENT.md; Paper 2 direction.

## Không thay đổi (giữ nguyên có chủ đích)
Evidence-base snapshots (`02_EVIDENCE_BASE/…`), discovery prompts, coursework matrices và mọi file archive giữ **notation lịch sử** để không sửa nội dung evidence; sẽ được reconcile khi các addenda đó được revise chính thức (kiểm soát hiện hành: `../01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md`; tracker lịch sử: `../90_ARCHIVE/CURRENT_RESET_20260804/CURRENT_CONTROL_HISTORY/UNRESOLVED_ITEMS_TRACKER_v2.1.md`). Không sửa dữ liệu/metric/citation khoa học.

## Administrative reconciliation note — 2026-08-04

The accepted decision in this ADR is `Action_Record_ID` and the removal of `Action_Status` from the identifier chain. The exact successor naming and semantics for line 29's historical `Action_Status_Event_ID` are **not** accepted by this annotation. `ADR_ACTION_STATUS_EVENT_20260804_DRAFT.md` proposes `Status_Event_ID`, append-only history, authorization, post-action verification and guarded closure/reopen; it remains `PROPOSED — NOT YET ACCEPTED`.
