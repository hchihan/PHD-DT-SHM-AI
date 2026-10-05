# Source authority and freshness control

> **Đồng bộ 01/10/2026 với CLAUDE.md của dự án Tiểu luận tổng quan.** Khi làm việc cho tiểu luận, đọc `CLAUDE.md` của dự án trước và tệp `references/project-canon-tltq.md`; hai tệp này thắng mọi bản tóm tắt cứng trong skill (chuỗi định danh tuyến tính, câu chữ khoảng trống "đã khóa", nơi ghi kết quả). K1–K3 là giả thuyết làm việc, chỉ chốt ở Điểm duyệt 3.


## Purpose

Use this file to decide which thesis document controls a judgment. Do not treat bundled skill references as the live source of truth.

## Expected project sources

Read these files when available before routing a paper or recommending thesis action:

0. **For literature-review (tiểu luận) work:** the project `CLAUDE.md` in `01_LITERATURE_REVIEW/03_OUTPUTS/01_TIEU_LUAN_TONG_QUAN/` and `references/project-canon-tltq.md`. These control the review: graph schema, K1–K3 wording and status, citation conventions, reading template, where results are logged. NCS-approved decisions there override this skill's snapshots. Note (01/10/2026): files under `00_GOVERNANCE/` and `01_CURRENT_CONTROL/` were shown as deleted in the Git working tree; do not assume their paths.

1. `MASTER_RESEARCH_CHARTER.md`
2. `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md`
3. `RESEARCH_DIRECTION_AND_SCOPE.md`
4. `RESEARCH_ARCHITECTURE.md`
5. `CURRENT_STATUS_AND_NEXT_DIRECTION.md`
6. `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md`
7. `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md`
8. Paper-specific and Evidence-Gate records supplied for the current task

`00_README_START_HERE.md` is a navigation source, not independent evidence.

## Conflict rules

| Question | Controlling source |
|---|---|
| Literature-review content, schema, gap wording, reading template | Project `CLAUDE.md` of the literature review (NCS-approved), then this skill |
| Locked Limited-FEM architecture | Accepted Architecture Decision Record, then Charter v1.1 |
| Overall thesis purpose and scope | Master Research Charter, interpreted consistently with Charter v1.1 |
| RQ/WP/chapter/paper/Gate architecture | Charter v1.1 and accepted decision record |
| Current progress, blockers and next Gate | Latest explicitly authoritative `CURRENT_STATUS_AND_NEXT_DIRECTION` or newer Gate-specific record |
| Historical rationale | Council Review; never let it override an accepted later decision |
| Paper-specific facts or results | The latest verified evidence pack, code/log/output and original paper |

When two sources conflict, report the conflict and apply the controlling source. Do not silently merge them. A later date, a filename containing `CURRENT`, or a higher version number is not authority by itself.

## Dynamic-status rule

Never embed or repeat a status claim merely because it appears in this skill. Re-read the current status and task-specific evidence. Treat metrics, run counts, model names, signed approvals, field access and Gate completion as dynamic.

If the required controlling source is absent or internally inconsistent, write exactly:

`Evidence is currently insufficient.`

Then state which source or decision is needed.

## Superseded signals

Flag a source as potentially superseded when it:

- restores FEM as a core RQ, WP, chapter, paper or Gate;
- requires `FEM_Node_ID` in the identifier chain;
- treats field feasibility as field damage diagnosis;
- transfers a laboratory classifier directly to the field;
- builds a traceability schema before locking competency questions;
- claims predictive maintenance, RUL, severity, calibrated FEM or AI superiority;
- conflicts with an accepted decision record or an explicitly authoritative current-status record.

Use superseded files only as historical evidence unless authority is re-established.
