# FABLE LEGACY PACK — INDEX
**Ngày lập:** 2026-07-18 | **Phiên lập:** Claude (Cowork) | **Kiến trúc:** Limited-FEM (Verdict B, khóa 17/07/2026)
**Vị thế:** Pack bàn giao phiên làm việc. **KHÔNG phải Source of Truth.** Khi mâu thuẫn, thứ tự ưu tiên: quyết định hai thầy hướng dẫn 17/07/2026 > THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md > MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md > bộ khung Cowork > pack này.

## Mục đích

Cố định lại (snapshot) trạng thái đã kiểm chứng của Project tại 18/07/2026 để mọi phiên làm việc sau (Claude/Fable hoặc agent khác) khởi động nhanh, đúng phạm vi, không tái diễn scope creep.

## Danh mục file trong pack

| File | Mục đích |
|---|---|
| `00_LEGACY_PACK_INDEX_20260718.md` | Index, vị thế pháp lý của pack, giao thức khởi động phiên |
| `01_PROJECT_STATE_SNAPSHOT_20260718.md` | Hiện trạng đã kiểm chứng theo Claim → Evidence → Limitation → Next action, tách bốn loại: laboratory evidence / information traceability / field feasibility / management decision support |
| `02_GATE1_EXECUTION_CHECKLIST_20260718.md` | Checklist thực thi khóa Gate 1: run registry → LORO → xác nhận sensor mode ResNet1D |
| `03_SCOPE_AND_FEM_GUARDRAILS_20260718.md` | Rào chắn phạm vi và ngôn ngữ: tuyên bố được phép/bị cấm, vai trò FEM, thuật ngữ |
| `04_UNRESOLVED_ITEMS_TRACKER_20260718.md` | Tracker 14 mục chưa giải quyết (mirror từ UNRESOLVED_ITEMS_AFTER_LIMITED_FEM_MIGRATION.md, trạng thái tại 18/07/2026) |

## Giao thức khởi động phiên sau (handoff protocol)

1. Đọc theo thứ tự: `00_README_START_HERE.md` → `MASTER_RESEARCH_CHARTER.md` → `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` → `RESEARCH_DIRECTION_AND_SCOPE.md` → `RESEARCH_ARCHITECTURE.md` → `CLAUDE.md` → `CURRENT_STATUS_AND_NEXT_DIRECTION.md` → `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md`; sau đó dùng pack này để nắm nhanh hiện trạng.
2. Khai báo đầu nhiệm vụ: RQ → WP → Chapter/Paper → Evidence Gate → phân loại Core / Supporting / Future Work / Out of Scope.
3. Mọi output phân tích theo Claim → Evidence → Limitation → Next action; thiếu bằng chứng ghi đúng "Evidence is currently insufficient."
4. Không sửa/xóa/đổi tên file quản trị; file mới phải có ngày hoặc version; file bị thay thế phải giữ trong archive.
5. Không dùng file trong `92_ARCHIVE_SUPERSEDED_FILES/` và các file bị supersede (danh mục tại ADR-2026-001 §"Files affected") làm cơ sở hiện hành.
