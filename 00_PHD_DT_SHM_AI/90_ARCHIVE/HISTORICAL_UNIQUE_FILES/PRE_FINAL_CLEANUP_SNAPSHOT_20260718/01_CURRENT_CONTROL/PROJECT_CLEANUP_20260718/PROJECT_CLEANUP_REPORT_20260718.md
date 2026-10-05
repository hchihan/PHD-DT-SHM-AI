# Báo cáo Dry Run Dọn dẹp Project
**Ngày:** 2026-07-18  
**Phạm vi:** `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/`  
**Trạng thái:** PHASE_A_COMPLETE - STOPPED_PENDING_RECOVERY_AND_SYNC  
**Chế độ:** Non-destructive; chưa di chuyển, archive hoặc xóa file.

## Kết luận

**Claim ->** Cấu trúc đích có thể áp dụng theo manifest, nhưng chưa an toàn để thực thi.  
**Evidence ->** Inventory SHA-256 bao phủ 94 file và phân loại được 91 file; ba DOCX Paper 1 cần quyết định nội dung. Master Index v1.1 tham chiếu một hierarchy `05_OUTPUT/Zotero_MCP/` không tồn tại và nhiều current files không tìm thấy. Một DOCX v6 xuất hiện/được cập nhật trong lúc audit.  
**Limitation ->** Filename chronology không chứng minh v6 thay thế v3/v4; manuscript source tham chiếu một DOCX v2 không tồn tại. Di chuyển khi Word/Google Drive chưa ổn định có thể tạo conflict copy hoặc mất bản unique.  
**Next action ->** Xác nhận Drive/Word ổn định, xác định canonical Paper 1 DOCX, và quyết định nguồn khôi phục hierarchy current trước khi phê duyệt manifest.

## Tóm tắt Inventory

| Mục | Số lượng |
|---|---:|
| Tổng file inventory | 94 |
| Markdown | 67 |
| CSV | 11 |
| DOCX | 3 |
| PDF | 13 |
| Dung lượng kiểm kê | 35,242,550 bytes |
| `KEEP_SYSTEM` | 1 |
| `KEEP_CURRENT` | 1 |
| `MOVE_TO_DOMAIN_FOLDER` | 81 |
| `ARCHIVE_LEGACY` | 5 |
| `ARCHIVE_SUPERSEDED` | 3 |
| `REVIEW_REQUIRED` | 3 |
| Link/path cần cập nhật nếu thực thi | 93 |

Inventory dùng đường dẫn tương đối theo project root. Mỗi dòng có size, modified date, SHA-256, version/status phát hiện, domain, quyết định, lý do và destination.

## Duplicate Checksum

| Mục | Kết quả |
|---|---:|
| Nhóm checksum trùng | 17 |
| Duplicate rows | 17 |
| Backup-identical được bảo vệ | 17 |
| `DELETE_VERIFIED_DUPLICATE` | 0 |
| File đã xóa | 0 |

Tất cả checksum-identical pairs phát hiện được liên quan đến `BACKUP_BEFORE_WRITEBACK_20260718/`. Backup không được xóa dù có canonical active copy. Zotero duplicate-record log không được dùng làm căn cứ xóa filesystem file.

## Source-of-Truth Conflicts

### 1. Hierarchy được tham chiếu nhưng không tồn tại

Các file governance và root README trỏ tới `05_OUTPUT/Zotero_MCP/`, nhưng thư mục này không tồn tại trong project root.

Master Index v1.1 liệt kê các current files chưa tìm thấy, gồm:

- `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v1.1.md`
- `EVIDENCE_GATES_v1.1_LIMITED_FEM.md`
- `PAPER1_SCOPE_REVIEW_v1.1_LIMITED_FEM_20260717.md`
- `PAPER2_CONCEPT_NOTE_TRACEABILITY_v1.0_20260717.md`
- `PAPER3_CONCEPT_UPDATE_v1.1_LIMITED_FEM_20260717.md`
- `PX_RQ1_Lab_Leakage_Evidence.md`
- `RQ2_TRACEABILITY_EVIDENCE_ADDENDUM_v1.0.md`
- `PX_RQ4_Inspection_Workflow_Evidence.md` (đọc theo WP4/Gate 5)
- `FINAL_CONSISTENCY_AUDIT_v1.1.md`
- `Literature_Evidence_Cowork_Ready.md` và addendum
- `Literature_Evidence_Living.md`

Không tái tạo nội dung các file này bằng suy diễn.

### 2. Control files nằm ngoài cleanup root

Các file sau tồn tại tại workspace-level `..\05_MASTER_INDEX_CONTROL\`, đồng thời có snapshot trong backup:

- `MASTER_INDEX_CURRENT_v1.1.md`
- `TERMINOLOGY_CONTROL_v1.1.md`
- `Literature_Review_Master_Index_Current.md`

Cleanup prompt chỉ định project root; vì vậy chưa có quyền tự chuyển canonical workspace-level controls vào project hoặc biến backup thành active control.

### 3. Paper 1 binary conflict

| File | Size | SHA-256 đầu | Quyết định |
|---|---:|---|---|
| `OUTLINE_PAPER1_RUN_AWARE_GATE1_v3_20260718.docx` | 221,785 | `8C2DE3FD...` | REVIEW_REQUIRED |
| `OUTLINE_PAPER1_RUN_AWARE_GATE1_v4_20260718.docx` | 34,313 | `7628F553...` | REVIEW_REQUIRED |
| `OUTLINE_PAPER1_GATE1_FULL_VI_v6_20260718.docx` | 169,254 | `AB1FBC1E...` | REVIEW_REQUIRED |

Ba file khác checksum và kích thước. Readiness report/manuscript source lại tham chiếu `PAPER1_GATE1_Q2_VERIFIED_EVIDENCE_REVISED_v2.docx`, nhưng file này không có trong project. v6 được modified lúc 15:46:17 trong quá trình audit, nên Drive/Word state chưa được xem là ổn định.

### 4. Living Evidence Base

- `LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md`: current canonical base theo Master Index v1.1.
- `Zotero MCP/01_LIVING_EVIDENCE_BASE_v1.2_LIMITED_FEM_20260718.md`: transitional update.
- Không có consolidated v1.3.

Theo prompt, đề xuất giữ cả v1.1 và v1.2 trong `02_EVIDENCE_BASE/CURRENT/`, với nhãn lần lượt `CURRENT_BASE_WITH_PENDING_UPDATE` và `TRANSITIONAL`; không archive v1.1 lúc này.

### 5. Unresolved Tracker

Tracker Fable ngày 18/07 tự xác định là mirror và ghi file gốc 17/07 vẫn là căn cứ. Vì Fable index tuyên bố pack không phải source of truth, quyết định đề xuất là:

- Giữ `UNRESOLVED_ITEMS_AFTER_LIMITED_FEM_MIGRATION.md` làm current control.
- Archive toàn bộ Fable pack vào `LEGACY_PACKS/`.

## Proposed Paper 1 Structure

### Current candidates

- `CURRENT_MANUSCRIPT/PAPER1_GATE1_Q2_VERIFIED_EVIDENCE_REVISED_v2_MANUSCRIPT_SOURCE_20260718.md`
- `GATE1_EVIDENCE/PAPER1_GATE1_READINESS_REPORT_v2.md`
- `GATE1_EVIDENCE/PAPER1_GATE1_CLAIM_EVIDENCE_AUDIT_v2.md`
- `IT_REQUESTS/PAPER1_GATE1_DATA_ANALYSIS_REQUESTS_FOR_IT_v2.md`
- `REFERENCE_AUDIT/PAPER1_GATE1_VERIFIED_REFERENCE_AUDIT_v2.csv`
- `REVISION_HISTORY/PAPER1_GATE1_MAJOR_REVISION_LOG_v2.md`

Các file này là `CURRENT_CANDIDATE`, không phải `CURRENT_APPROVED`; Gate 1 vẫn mở.

### Binary review

Ba DOCX v3/v4/v6 đề xuất vào `99_TEMP_REVIEW/PAPER1_DOCX_VERSION_REVIEW/` cho đến khi có quyết định canonical. Không file nào được archive/xóa dựa riêng vào số version.

## Proposed Domain Moves

| Nguồn hiện tại | Destination đề xuất |
|---|---|
| Root governance files | `00_GOVERNANCE/` |
| Current status/unresolved | `01_CURRENT_CONTROL/` |
| Living Evidence + addenda | `02_EVIDENCE_BASE/` theo RQ/Gate |
| `Paper 1/` | `03_PAPERS/PAPER_1/` theo subfolder |
| Chuyên đề Tổng quan | `04_PHD_SPECIAL_TOPICS/CHUYEN_DE_TONG_QUAN/` |
| Perplexity discovery corpus | `06_LITERATURE_AND_ZOTERO/PERPLEXITY_PRO/` |
| Operational prompts | `07_PROMPTS_AND_HANDOFFS/OPENCODE/` |
| Backup writeback | `90_BACKUP/BACKUP_BEFORE_WRITEBACK_20260718/` |
| Fable pack | `92_ARCHIVE_SUPERSEDED_FILES/LEGACY_PACKS/` |
| Existing archive files | structured `GOVERNANCE_OLD/` / `EVIDENCE_OLD/` |

Perplexity files phải được đánh dấu `DISCOVERY_SOURCE_ONLY` và `NOT_CITABLE_EVIDENCE`; các reference PDF được giữ nguyên, không xóa.

## Phase Status

| Phase | Trạng thái |
|---|---|
| Phase A - inventory/dry run | COMPLETED |
| Phase B - pre-cleanup snapshot | NOT STARTED - blocked |
| Phase C - move/organize | NOT STARTED |
| Phase D - archive | NOT STARTED |
| Phase E - duplicate deletion | NOT STARTED; 0 eligible |
| Phase F - validation | NOT STARTED |

## Files Created

- `PROJECT_FILE_INVENTORY_BEFORE_CLEANUP_20260718.csv`
- `PROJECT_FILE_MIGRATION_MANIFEST_20260718.csv`
- `VERIFIED_DUPLICATE_DELETION_MANIFEST_20260718.csv`
- `PROJECT_CLEANUP_REPORT_20260718.md`
- `MASTER_INDEX_CURRENT.md` (`CURRENT_CANDIDATE_BLOCKED`)
- `_generate_dry_run_inventory.py` (reproducible inventory generator)

## Safety Statement

- Raw data deleted: 0.
- Code/notebook/checkpoint deleted: 0.
- Zotero attachments/library modified: 0.
- Source-of-truth files deleted: 0.
- Files moved or renamed: 0.
- Backup contents modified: 0.

## Decisions Required Before Execution

1. Xác nhận Word đã đóng và Google Drive đã sync ổn định.
2. Xác định canonical Paper 1 DOCX: v6 có thay thế v3/v4 không, và DOCX v2 được tham chiếu hiện nằm ở đâu.
3. Quyết định nguồn khôi phục các current files bị thiếu và cách xử lý controls đang nằm ngoài project root.
4. Phê duyệt manifest theo nhóm; không cần quyết định từng file nhỏ.

## User Decisions Recorded

Ngày 2026-07-18, người dùng xác nhận:

1. **Source of truth:** dừng cleanup để khôi phục hierarchy `05_OUTPUT/Zotero_MCP/` và các current files bị thiếu.
2. **Paper 1 DOCX:** giữ cả v3/v4/v6 trong nhóm `REVIEW_REQUIRED`; không chọn canonical và không archive/xóa bản nào.
3. **Google Drive:** trạng thái đồng bộ chưa chắc chắn; không bắt đầu Phase B.

**Claim ->** Bước 2 chưa được ủy quyền.  
**Evidence ->** Hai STOP conditions còn hiệu lực: referenced current files are missing và Drive sync chưa được xác nhận.  
**Limitation ->** Root chưa được tái cấu trúc; Master Index mới chỉ là candidate trong thư mục báo cáo.  
**Next action ->** Khôi phục/định vị hierarchy CURRENT, chờ Drive sync hoàn tất, chạy lại checksum delta, rồi review manifest trước khi thực thi non-destructive moves.
