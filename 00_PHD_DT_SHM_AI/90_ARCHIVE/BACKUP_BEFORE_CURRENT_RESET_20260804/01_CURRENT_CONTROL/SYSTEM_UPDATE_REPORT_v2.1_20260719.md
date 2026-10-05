# SYSTEM UPDATE REPORT — v2.1
**Date:** 2026-07-19 | **Scope:** đồng bộ toàn bộ hệ dẫn hướng nghiên cứu sang Traceability-Core v2.1 theo Charter v2.0 (docx) + bốn điều chỉnh học thuật bắt buộc.
**Nguyên tắc:** không sửa/xóa/bịa evidence khoa học; chỉ thay đổi phân loại, liên kết, trạng thái sử dụng và câu chữ dẫn hướng.

## Bảng thay đổi file

| File | Trạng thái trước | Hành động | Trạng thái sau | Lý do |
|---|---|---|---|---|
| `00_GOVERNANCE/MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md` | không tồn tại | **CREATE** | CURRENT_SOURCE_OF_TRUTH | Hiến chương v2.1, khóa trục + 4 điều chỉnh |
| `00_GOVERNANCE/RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md` | không tồn tại | **CREATE** | CURRENT_APPROVED | Ma trận RQ–WP–Chapter–Paper–Gate |
| `00_GOVERNANCE/EVIDENCE_GATES_v2.1.md` | không tồn tại | **CREATE** | CURRENT_APPROVED | Định nghĩa G1–G7, không gate FEM |
| `00_GOVERNANCE/RESEARCH_ARCHITECTURE_DECISION_RECORD_20260719.md` | không tồn tại | **CREATE** | CURRENT_APPROVED | ADR v2.1 |
| `00_GOVERNANCE/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` | không tồn tại | **CREATE** | CURRENT_APPROVED | Trật tự ưu tiên khi mâu thuẫn |
| `00_GOVERNANCE/AGENT_RULES.md` | không tồn tại tại 00_GOVERNANCE | **CREATE** | CURRENT_APPROVED | Agent governance thống nhất; thay vai trò AGENT_RULES cũ |
| `03_PAPERS/PAPER_1/PAPER1_DIRECTION_AND_GATE_v2.1_20260719.md` | không tồn tại | **CREATE** | CURRENT | Direction Paper 1, claims=candidate |
| `03_PAPERS/PAPER_2/PAPER2_DIRECTION_AND_GATE_v2.1_20260719.md` | thư mục rỗng | **CREATE** | CURRENT | Direction Paper 2 (QLXD core) |
| `03_PAPERS/PAPER_3/PAPER3_FIELD_FEASIBILITY_DIRECTION_v2.1_20260719.md` | thư mục rỗng | **CREATE** | CURRENT | Field: optional pub vs mandatory evidence |
| `01_CURRENT_CONTROL/SYSTEM_UPDATE_REPORT_v2.1_20260719.md` | không tồn tại | **CREATE** | CURRENT | File này |
| `01_CURRENT_CONTROL/CHANGELOG_v2.1_20260719.md` | không tồn tại | **CREATE** | CURRENT | Thay đổi từ v1.1 & v2.0 |
| `01_CURRENT_CONTROL/UNRESOLVED_ITEMS_TRACKER_v2.1.md` | không tồn tại | **CREATE** | CURRENT | Tracker mục chưa khóa |
| `../90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` | Source of truth | **HEADER → SUPERSEDED** | SUPERSEDED (giữ lại) | v2.1 thay thế; giữ lịch sử |
| `00_README_START_HERE.md` | trỏ v1.1 | **UPDATE** | CURRENT | Thứ tự đọc + source of truth = v2.1 |
| `../90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/MASTER_RESEARCH_CHARTER.md` (concise) | Limited-FEM | **UPDATE** | CURRENT_NAVIGATION | Trỏ v2.1; claims candidate; CEI; field |
| `../90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/RESEARCH_DIRECTION_AND_SCOPE.md` | v1.1 | **UPDATE** | CURRENT_APPROVED | Note v2.1: CEI, accountability, field mandatory |
| `../90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/RESEARCH_ARCHITECTURE.md` | v1.1 | **UPDATE** | CURRENT_APPROVED | Note v2.1 bốn lớp |
| `00_GOVERNANCE/TERMINOLOGY_CONTROL_CURRENT.md` | v1.1 | **UPDATE (+§5)** | CURRENT | Bổ sung allowed/prohibited + quy tắc alert/prediction |
| `../90_ARCHIVE/HISTORICAL_UNIQUE_FILES/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/CLAUDE.md` | v1.1 | **UPDATE** | CURRENT | Trỏ v2.1 + 4 điều chỉnh |
| `../90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/CURRENT_STATUS_AND_NEXT_DIRECTION.md` | v1.1 | **UPDATE (header)** | CURRENT | Note v2.1, current gate G1 |
| `MASTER_INDEX_CURRENT.md` | v1.1 authority | **UPDATE** | CURRENT | Authority order + governance table → v2.1 |

## Files đã archive/giữ lịch sử (không xóa)
- `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` → SUPERSEDED header, giữ tại 00_GOVERNANCE.
- `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md` → HISTORICAL (ADR trước).
- `MASTER_RESEARCH_CHARTER_v2_20260719.docx` → HISTORICAL_DECISION_SOURCE.
- File FEM-core cũ đã nằm sẵn trong `90_BACKUP/.../92_ARCHIVE_SUPERSEDED_FILES` và `92_ARCHIVE_MINIMAL` — không thay đổi.

## Không thực hiện (giữ nguyên có chủ đích)
- Không sửa evidence base (`02_EVIDENCE_BASE/`), metric, citation, Zotero.
- Không xóa bất kỳ file nào.
- Không đổi tên file quản trị hiện có.
- AGENT_RULES/RESEARCH_CHARTER cũ trong AI_SYSTEM/AGENTS: không tìm thấy trong Cowork write-scope hiện tại; `AGENT_RULES.md` mới tuyên bố thay vai trò nếu chúng còn tồn tại (xem UNRESOLVED tracker).

## Claim → Evidence → Limitation → Next action
- **Claim:** Hệ dẫn hướng đã đồng bộ v2.1, không mâu thuẫn trục.
- **Evidence:** 12 file tạo mới + 8 file cập nhật (bảng trên); keyword/conflict check (xem CHANGELOG §Acceptance).
- **Limitation:** legal refs chưa xác minh; G1 chưa đóng; CEI operational definition & CQ chưa pre-register; field-access chưa ký.
- **Next action:** đóng G1 (run registry → LORO → ResNet1D provenance → uncertainty); pre-register SCQ/VCQ/RCQ; xác minh legal refs.
