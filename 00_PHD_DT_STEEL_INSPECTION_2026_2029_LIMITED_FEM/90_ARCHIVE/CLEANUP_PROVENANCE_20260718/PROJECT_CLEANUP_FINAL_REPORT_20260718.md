# Báo cáo Cuối Dọn dẹp Project
**Ngày:** 2026-07-18  
**Trạng thái:** COMPLETE  
**Chế độ:** Full cleanup, checksum-controlled, backup-first.

## Kết luận

**Claim ->** Project đã được tái cấu trúc thành hierarchy hiện hành, root gọn và không mất dữ liệu nghiên cứu.  
**Evidence ->** 95 execution inputs được xử lý; 94 file di chuyển với checksum match và một README giữ tại root; 16 file superseded/legacy/temp được xóa sau snapshot; 60 active internal paths được kiểm tra với 0 broken link; snapshot 103 file có 0 checksum mismatch.  
**Limitation ->** Ba DOCX Paper 1 khác nội dung nên còn `REVIEW_REQUIRED`; các Gate/Paper control files được Master Index cũ tham chiếu đã thiếu trước cleanup và không được tái tạo bằng suy diễn; Zotero writeback vẫn pending.  
**Next action ->** Reconcile ba DOCX outline, khôi phục các missing current files nếu còn bản ngoài workspace, và xử lý Zotero writeback sau khi bật hybrid/web credentials.

## Chỉ tiêu

| Chỉ tiêu | Kết quả |
|---|---:|
| Tổng file trước cleanup | 94 dry-run files + 1 execution prompt |
| File current/system giữ lại | 45 |
| File di chuyển | 94 |
| File superseded/legacy/merged đã xóa | 6 |
| Duplicate/temp/intermediate đã xóa | 11 |
| Tổng file đã xóa | 17 |
| File archive minimal | 9, gồm 4 Paper 1 review files và 5 minimal-history files |
| File review required | 3 DOCX |
| Active internal paths checked | 60 |
| Broken links | 0 |
| Raw data bị xóa | 0 |
| Source-of-truth bị mất | 0 |
| Zotero database/attachments bị sửa | 0 |

Không có checksum-identical backup nào bị xóa. Mười bảy duplicate groups phát hiện trong dry run đều liên quan đến backup và được giữ nguyên.

## Root Sau Cleanup

Root chỉ còn:

- `00_GOVERNANCE/`
- `01_CURRENT_CONTROL/`
- `02_EVIDENCE_BASE/`
- `03_PAPERS/`
- `04_PHD_SPECIAL_TOPICS/`
- `05_DATA_CODE_AND_EXPERIMENTS/`
- `06_LITERATURE_AND_ZOTERO/`
- `07_PROMPTS_AND_HANDOFFS/`
- `90_BACKUP/`
- `92_ARCHIVE_MINIMAL/`
- `00_README_START_HERE.md`

## Source Of Truth Hiện Hành

1. `00_GOVERNANCE/MASTER_RESEARCH_CHARTER.md`
2. `00_GOVERNANCE/MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md`
3. `00_GOVERNANCE/RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md`
4. `00_GOVERNANCE/RESEARCH_DIRECTION_AND_SCOPE.md`
5. `00_GOVERNANCE/RESEARCH_ARCHITECTURE.md`
6. `00_GOVERNANCE/THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md`
7. `00_GOVERNANCE/TERMINOLOGY_CONTROL_CURRENT.md`
8. `01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md`
9. `01_CURRENT_CONTROL/UNRESOLVED_ITEMS_CURRENT.md`
10. `01_CURRENT_CONTROL/PROJECT_CLEANUP_20260718/MASTER_INDEX_CURRENT.md`

Charter và ADR chỉ được cập nhật đường dẫn điều hướng; nội dung học thuật không thay đổi.

## Current Evidence Base

- Canonical base: `02_EVIDENCE_BASE/CURRENT/LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md`.
- Transitional current update: `02_EVIDENCE_BASE/CURRENT/01_LIVING_EVIDENCE_BASE_v1.2_LIMITED_FEM_20260718.md`.
- Current pointer: `02_EVIDENCE_BASE/CURRENT/LIVING_EVIDENCE_BASE_CURRENT.md`.
- RQ1: `02_EVIDENCE_BASE/RQ1_GATE1/`.
- RQ2: `02_EVIDENCE_BASE/RQ2_GATES2_3/`.
- RQ3: `02_EVIDENCE_BASE/RQ3_GATE4/`.
- WP4: `02_EVIDENCE_BASE/WP4_GATE5/`.

v1.1 và v1.2 đều được giữ vì chưa có consolidated v1.3 và v1.2 tuyên bố không ghi đè v1.1.

## Current Paper 1

- `03_PAPERS/PAPER_1/CURRENT_MANUSCRIPT/PAPER1_GATE1_Q2_VERIFIED_EVIDENCE_REVISED_v2_MANUSCRIPT_SOURCE_20260718.md`
- `03_PAPERS/PAPER_1/GATE1_EVIDENCE/PAPER1_GATE1_READINESS_REPORT_v2.md`
- `03_PAPERS/PAPER_1/GATE1_EVIDENCE/PAPER1_GATE1_CLAIM_EVIDENCE_AUDIT_v2.md`
- `03_PAPERS/PAPER_1/IT_REQUESTS/PAPER1_GATE1_DATA_ANALYSIS_REQUESTS_FOR_IT_v2.md`
- `03_PAPERS/PAPER_1/REFERENCE_AUDIT/PAPER1_GATE1_VERIFIED_REFERENCE_AUDIT_v2.csv`
- `03_PAPERS/PAPER_1/REVISION_HISTORY/PAPER1_GATE1_MAJOR_REVISION_LOG_v2.md`

Gate 1 vẫn `NOT READY`; cleanup không thay đổi Gate status.

## Paper 1 Review Required

Ba outline DOCX được giữ tại `03_PAPERS/PAPER_1/ARCHIVE_MINIMAL/OUTLINE_VERSION_REVIEW/`:

- `OUTLINE_PAPER1_RUN_AWARE_GATE1_v3_20260718.docx`
- `OUTLINE_PAPER1_RUN_AWARE_GATE1_v4_20260718.docx`
- `OUTLINE_PAPER1_GATE1_FULL_VI_v6_20260718.docx`

File mang tên v6 có heading nội bộ tự nhận version v4; ba file khác checksum và text, nên không file nào bị xóa hoặc gắn CURRENT_APPROVED.

## Current Chuyen De Tong Quan

Tại `04_PHD_SPECIAL_TOPICS/CHUYEN_DE_TONG_QUAN/`:

- `CHUYEN_DE_TONG_QUAN_EVIDENCE_GAPS_v1.md`
- `EVIDENCE_MATRIX_CHUYEN_DE_TONG_QUAN_v1.csv`
- `MATRIX_CHUYEN_DE_RQ_WP_PAPER_GATE_v1.md`
- `OUTLINE_CHUYEN_DE_TONG_QUAN_CHI_TIET_v1.md`

Các file này là current candidates và cần reconcile với 19-source deep-read update trước phê duyệt học thuật.

## Current Zotero/Evidence Audit

Tại `02_EVIDENCE_BASE/ZOTERO_AUDIT/`:

- `02_NEW_DEEP_READ_EVIDENCE_MATRIX_20260718.csv`
- `08_DUPLICATE_AND_METADATA_CORRECTION_LOG_20260718.csv`
- `09_ZOTERO_DEEP_READ_COMPLETION_REPORT_20260718.md`
- `10_ZOTERO_WRITEBACK_QUEUE_20260718.md`
- `PHASE0_SAFETY_BACKUP_AND_DRY_RUN_REPORT_20260718.md`

Writeback: 0 tags, 0 notes, 0 metadata edits; MCP vẫn ở local-only mode. Không sửa trực tiếp Zotero SQLite.

## Literature Discovery

`06_LITERATURE_AND_ZOTERO/PERPLEXITY_PRO/` được giữ với README bắt buộc:

- `DISCOVERY_SOURCE_ONLY`
- `NOT_CITABLE_EVIDENCE`

Các report/PDF còn lại khác chủ đề hoặc là reference độc nhất; không xóa chỉ dựa trên việc chúng là AI discovery output.

## Archive Minimal

`92_ARCHIVE_MINIMAL/` giữ:

- Migration archive note.
- Superseded Gate matrix vì current detailed Gate matrix đã thiếu trước cleanup.
- Fable legacy index và Gate 1 execution checklist có giá trị vận hành/lịch sử.
- Archive README.

Charter v1.0 superseded, ba Fable mirror/snapshot files và prompt cleanup cũ đã được xóa khỏi working tree sau khi backup.

## Backup

- `90_BACKUP/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/`: 103 snapshot rows, checksum failures = 0.
- `90_BACKUP/BACKUP_BEFORE_WRITEBACK_20260718/`: backup Zotero writeback, giữ nguyên.

Mọi file bị xóa đều có record trong `DELETED_SUPERSEDED_FILES_MANIFEST_20260718.csv`; file nghiên cứu đã tồn tại trước cleanup có bản trong snapshot.

## Missing Pre-existing Controls

Các file CURRENT được Master Index v1.1 cũ tham chiếu nhưng không tìm thấy trước cleanup được ghi tại `01_CURRENT_CONTROL/MISSING_CURRENT_FILES_REGISTER_20260718.md`. Cleanup không xóa và không tái tạo các file này.

## Validation

- `ROOT CLEAN = YES`
- `CURRENT FILES IDENTIFIED = YES`
- `SUPERSEDED FILES REMOVED = YES`
- `BROKEN LINKS = 0`
- `RAW DATA LOSS = 0`
- `SOURCE-OF-TRUTH LOSS = 0`
- `MASTER INDEX = CURRENT`
