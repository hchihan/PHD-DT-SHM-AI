# Tệp đang ở trạng thái đã xóa trong repo (lập 01/10/2026)

Repo: `H:/My Drive/03_RESEARCH/01_PHD_DT_AI_AM`, nhánh `revision-v2`, so với commit `HEAD`. Danh sách lấy từ `git status --porcelain`. **Chưa chạy `git restore`, chưa commit lệnh xóa nào.** Mọi tệp vẫn còn trong lịch sử git và khôi phục được bằng `git restore <đường dẫn>`.

Bối cảnh: commit `47a8c10` (01/10/2026) đã cuốn theo các lệnh xóa này; commit đó đã được hoàn tác bằng `git reset --soft` và thay bằng `0ac137c` chỉ gồm tệp của phiên. Từ nay áp quy tắc git ở CLAUDE.md mục 4.3.

Cách kiểm bản thay thế: (1) **cùng nội dung**: băm blob git của tệp ở `HEAD` trùng với một tệp đang có trên đĩa trong repo (kể cả tệp chưa được git theo dõi); (2) **cùng tên**: có tệp trùng tên ở chỗ khác nhưng nội dung khác. Tệp trên 60 MB không băm.

**Tổng:** 330 tệp; 180 có bản cùng nội dung ở nơi khác; 71 chỉ có tệp cùng tên; 79 không thấy bản thay thế.

## Tóm tắt theo nhóm

| Nhóm thư mục | Số tệp | Commit gần nhất có tệp | Cùng nội dung ở nơi khác | Chỉ cùng tên | Không thấy | Đề xuất |
|---|---|---|---|---|---|---|
| `00_GOVERNANCE` | 15 | 84accc9 (2026-08-11)×14; f48e856 (2026-08-04)×1 | 1 | 10 | 4 | NCS xem (một phần có bản thay thế) |
| `01_CURRENT_CONTROL` | 11 | 84accc9 (2026-08-11)×6; f48e856 (2026-08-04)×3; 716fa2a (2026-08-04)×1 | 0 | 4 | 7 | NCS xem (một phần có bản thay thế) |
| `01_LITERATURE_REVIEW/03_OUTPUTS/01_TIEU_LUAN_TONG_QUAN` | 5 | b4fa47a (2026-09-28) | 5 | 0 | 0 | xác nhận xóa (mọi tệp có bản cùng nội dung ở nơi khác) |
| `02_EVIDENCE_BASE/90_ARCHIVE_SUPERSEDED/20260804` | 7 | 84accc9 (2026-08-11) | 2 | 0 | 5 | NCS xem (một phần có bản thay thế) |
| `02_EVIDENCE_BASE/CURRENT` | 7 | 84accc9 (2026-08-11) | 0 | 2 | 5 | NCS xem (một phần có bản thay thế) |
| `02_EVIDENCE_BASE/RQ1_GATE1` | 1 | 84accc9 (2026-08-11) | 1 | 0 | 0 | xác nhận xóa (mọi tệp có bản cùng nội dung ở nơi khác) |
| `02_EVIDENCE_BASE/RQ1_GATE1/RQ1_UPDATED_DEEP_READ_10.07` | 17 | f48e856 (2026-08-04)×16; 84accc9 (2026-08-11)×1 | 14 | 0 | 3 | NCS xem (một phần có bản thay thế) |
| `02_EVIDENCE_BASE/RQ2_GATES2_3` | 15 | 84accc9 (2026-08-11) | 11 | 1 | 3 | NCS xem (một phần có bản thay thế) |
| `02_EVIDENCE_BASE/RQ2_GATES2_3/DEEP_READ_20.07.2026` | 15 | f48e856 (2026-08-04)×9; 84accc9 (2026-08-11)×6 | 15 | 0 | 0 | xác nhận xóa (mọi tệp có bản cùng nội dung ở nơi khác) |
| `02_EVIDENCE_BASE/RQ3_GATE4` | 1 | 84accc9 (2026-08-11) | 1 | 0 | 0 | xác nhận xóa (mọi tệp có bản cùng nội dung ở nơi khác) |
| `02_EVIDENCE_BASE/WP4_GATE5` | 5 | f48e856 (2026-08-04)×4; 84accc9 (2026-08-11)×1 | 5 | 0 | 0 | xác nhận xóa (mọi tệp có bản cùng nội dung ở nơi khác) |
| `02_EVIDENCE_BASE/ZOTERO_DEEP_READ` | 5 | f48e856 (2026-08-04) | 3 | 2 | 0 | NCS xem (mọi tệp có tệp cùng tên ở nơi khác, nội dung khác) |
| `03_PAPERS` | 5 | 84accc9 (2026-08-11) | 1 | 0 | 4 | NCS xem (một phần có bản thay thế) |
| `03_PAPERS/PAPER_1` | 6 | f48e856 (2026-08-04)×4; 84accc9 (2026-08-11)×2 | 4 | 0 | 2 | NCS xem (một phần có bản thay thế) |
| `03_PAPERS/PAPER_1/CURRENT_MANUSCRIPT` | 1 | f48e856 (2026-08-04) | 1 | 0 | 0 | xác nhận xóa (mọi tệp có bản cùng nội dung ở nơi khác) |
| `03_PAPERS/PAPER_1/GATE1_EVIDENCE` | 2 | f48e856 (2026-08-04) | 0 | 2 | 0 | NCS xem (mọi tệp có tệp cùng tên ở nơi khác, nội dung khác) |
| `03_PAPERS/PAPER_1/IT_REQUESTS` | 1 | f48e856 (2026-08-04) | 0 | 1 | 0 | NCS xem (mọi tệp có tệp cùng tên ở nơi khác, nội dung khác) |
| `03_PAPERS/PAPER_1/REFERENCE_AUDIT` | 1 | f48e856 (2026-08-04) | 1 | 0 | 0 | xác nhận xóa (mọi tệp có bản cùng nội dung ở nơi khác) |
| `03_PAPERS/PAPER_1/REVISION_HISTORY` | 1 | f48e856 (2026-08-04) | 0 | 1 | 0 | NCS xem (mọi tệp có tệp cùng tên ở nơi khác, nội dung khác) |
| `03_PAPERS/PAPER_2` | 1 | 84accc9 (2026-08-11) | 0 | 0 | 1 | khôi phục hoặc NCS xem (không tìm thấy bản thay thế) |
| `03_PAPERS/PAPER_3` | 1 | 84accc9 (2026-08-11) | 0 | 1 | 0 | NCS xem (mọi tệp có tệp cùng tên ở nơi khác, nội dung khác) |
| `03_PAPERS/PAPER_S1_SENSOR_COMPARISON_CANDIDATE` | 1 | f48e856 (2026-08-04) | 0 | 0 | 1 | khôi phục hoặc NCS xem (không tìm thấy bản thay thế) |
| `04_PHD_SPECIAL_TOPICS/CHUYEN_DE_TONG_QUAN` | 7 | f48e856 (2026-08-04)×4; 84accc9 (2026-08-11)×3 | 4 | 0 | 3 | NCS xem (một phần có bản thay thế) |
| `05_DATA_CODE_AND_EXPERIMENTS/CAMPAIGN_DOCUMENTATION` | 1 | f48e856 (2026-08-04) | 1 | 0 | 0 | xác nhận xóa (mọi tệp có bản cùng nội dung ở nơi khác) |
| `05_DATA_CODE_AND_EXPERIMENTS/CANONICAL_THREE_CAMPAIGN_DATASET` | 8 | f48e856 (2026-08-04) | 1 | 0 | 7 | NCS xem (một phần có bản thay thế) |
| `05_DATA_CODE_AND_EXPERIMENTS/THREE_CAMPAIGN_REANALYSIS` | 14 | f48e856 (2026-08-04) | 11 | 1 | 2 | NCS xem (một phần có bản thay thế) |
| `06_LITERATURE_AND_ZOTERO/PERPLEXITY_DISCOVERY` | 12 | f48e856 (2026-08-04) | 11 | 1 | 0 | NCS xem (mọi tệp có tệp cùng tên ở nơi khác, nội dung khác) |
| `06_LITERATURE_AND_ZOTERO/STANDARDS` | 1 | f48e856 (2026-08-04) | 1 | 0 | 0 | xác nhận xóa (mọi tệp có bản cùng nội dung ở nơi khác) |
| `06_LITERATURE_AND_ZOTERO/ZOTERO_MCP` | 1 | f48e856 (2026-08-04) | 0 | 1 | 0 | NCS xem (mọi tệp có tệp cùng tên ở nơi khác, nội dung khác) |
| `07_PROMPTS_AND_HANDOFFS/ASSETS` | 1 | f48e856 (2026-08-04) | 1 | 0 | 0 | xác nhận xóa (mọi tệp có bản cùng nội dung ở nơi khác) |
| `07_PROMPTS_AND_HANDOFFS/NOTEBOOKLM` | 1 | f48e856 (2026-08-04) | 1 | 0 | 0 | xác nhận xóa (mọi tệp có bản cùng nội dung ở nơi khác) |
| `07_PROMPTS_AND_HANDOFFS/OPENCODE` | 3 | f48e856 (2026-08-04) | 3 | 0 | 0 | xác nhận xóa (mọi tệp có bản cùng nội dung ở nơi khác) |
| `07_PROMPTS_AND_HANDOFFS/PAPER1` | 1 | f48e856 (2026-08-04) | 1 | 0 | 0 | xác nhận xóa (mọi tệp có bản cùng nội dung ở nơi khác) |
| `07_PROMPTS_AND_HANDOFFS/PROMPT_CONTROL_CENTER` | 8 | f48e856 (2026-08-04) | 0 | 1 | 7 | NCS xem (một phần có bản thay thế) |
| `07_PROMPTS_AND_HANDOFFS/phd-prompt-compressor` | 2 | f48e856 (2026-08-04) | 2 | 0 | 0 | xác nhận xóa (mọi tệp có bản cùng nội dung ở nơi khác) |
| `07_PROMPTS_AND_HANDOFFS/phd-prompt-router` | 3 | f48e856 (2026-08-04) | 3 | 0 | 0 | xác nhận xóa (mọi tệp có bản cùng nội dung ở nơi khác) |
| `08_AI_SKILL_SYSTEM/ARS_TO_PHD_SKILLS_20260810` | 4 | 84accc9 (2026-08-11) | 4 | 0 | 0 | xác nhận xóa (mọi tệp có bản cùng nội dung ở nơi khác) |
| `08_AI_SKILL_SYSTEM/phd-dt-research-skills` | 19 | 84accc9 (2026-08-11) | 19 | 0 | 0 | xác nhận xóa (mọi tệp có bản cùng nội dung ở nơi khác) |
| `08_AI_SKILL_SYSTEM/phd-literature-evidence-workspace` | 50 | 84accc9 (2026-08-11) | 11 | 39 | 0 | NCS xem (mọi tệp có tệp cùng tên ở nơi khác, nội dung khác) |
| `08_CLAUDE_SKILLS` | 3 | 84accc9 (2026-08-11) | 2 | 0 | 1 | NCS xem (một phần có bản thay thế) |
| `08_CLAUDE_SKILLS/govern-phd-evidence` | 3 | 84accc9 (2026-08-11) | 3 | 0 | 0 | xác nhận xóa (mọi tệp có bản cùng nội dung ở nơi khác) |
| `08_DEMO_AND_PROTOTYPES/IT_HANDOFFS` | 1 | f48e856 (2026-08-04) | 1 | 0 | 0 | xác nhận xóa (mọi tệp có bản cùng nội dung ở nơi khác) |
| `09_KNOWLEDGE_UNIVERSE_20260811` | 2 | 076b899 (2026-08-11) | 0 | 1 | 1 | NCS xem (một phần có bản thay thế) |
| `90_ARCHIVE/GOVERNANCE_HISTORY/EVIDENCE_BASE` | 2 | f48e856 (2026-08-04) | 0 | 0 | 2 | khôi phục hoặc NCS xem (không tìm thấy bản thay thế) |
| `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718` | 1 | f48e856 (2026-08-04) | 0 | 0 | 1 | khôi phục hoặc NCS xem (không tìm thấy bản thay thế) |
| `90_ARCHIVE/SNAPSHOTS_20260718/BACKUP_BEFORE_WRITEBACK_20260718` | 1 | f48e856 (2026-08-04) | 0 | 0 | 1 | khôi phục hoặc NCS xem (không tìm thấy bản thay thế) |
| `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718` | 4 | f48e856 (2026-08-04) | 0 | 0 | 4 | khôi phục hoặc NCS xem (không tìm thấy bản thay thế) |
| `91_REVIEW_REQUIRED/EMPTY_FOLDERS` | 10 | f48e856 (2026-08-04) | 9 | 0 | 1 | NCS xem (một phần có bản thay thế) |
| `91_REVIEW_REQUIRED/PAPER1_VERSION_REVIEW` | 6 | f48e856 (2026-08-04) | 3 | 0 | 3 | NCS xem (một phần có bản thay thế) |
| `91_REVIEW_REQUIRED/STALE_AGENT_RULES` | 1 | f48e856 (2026-08-04) | 1 | 0 | 0 | xác nhận xóa (mọi tệp có bản cùng nội dung ở nơi khác) |
| `99_REPOSITORY_LOGS/REORGANIZATION_PLAN_20260803` | 2 | f48e856 (2026-08-04) | 2 | 0 | 0 | xác nhận xóa (mọi tệp có bản cùng nội dung ở nơi khác) |
| `99_REPOSITORY_LOGS/REPOSITORY_AUDIT_20260803` | 8 | f48e856 (2026-08-04) | 7 | 1 | 0 | NCS xem (mọi tệp có tệp cùng tên ở nơi khác, nội dung khác) |
| `CLAUDE_COWORK_PHD_PROJECT_SETUP_20260804` | 12 | 84accc9 (2026-08-11) | 11 | 0 | 1 | NCS xem (một phần có bản thay thế) |
| `(gốc)` | 2 | 84accc9 (2026-08-11) | 0 | 0 | 2 | khôi phục hoặc NCS xem (không tìm thấy bản thay thế) |
| `output` | 12 | f48e856 (2026-08-04) | 2 | 2 | 8 | NCS xem (một phần có bản thay thế) |

Mô tả các commit nhắc ở trên:

- `f48e856` (2026-08-04): chore: establish reset baseline and inventory
- `716fa2a` (2026-08-04): docs: verify current repository reset
- `f2d7bc9` (2026-08-04): chore: archive superseded direction documents
- `84accc9` (2026-08-11): docs: consolidate evidence base and align governance metadata
- `076b899` (2026-08-11): docs: add PhD knowledge universe strategic map
- `b4fa47a` (2026-09-28): GĐ0: chuyển tiểu luận gốc sang Markdown

## Chi tiết từng tệp

### `00_GOVERNANCE` (15)

| Tệp | Bản thay thế |
|---|---|
| `ADR_ACTION_STATUS_EVENT_20260804_DRAFT.md` | không thấy |
| `AGENT_RULES.md` | cùng tên: `04_AI_SYSTEM/AGENTS/AGENT_RULES.md`; `01_LITERATURE_REVIEW/01_CURRENT_CONTROL/AGENT_RULES.md` |
| `CLAUDE.md` | cùng tên: `03_RESEARCH_ASSETS/99_ARCHIVE/DT-SHM-AI-STEEL-FRAME/pyrobotstructural/CLAUDE.md`; `04_AI_SYSTEM/AI_WORKFLOW/CLAUDE/CLAUDE.md` |
| `EVIDENCE_GATES_v2.1.md` | cùng tên: `01_LITERATURE_REVIEW/01_CURRENT_CONTROL/EVIDENCE_GATES_v2.1.md`; `01_LITERATURE_REVIEW/90_ARCHIVE/01_SUPERSEDED_VERSIONS/PRE_SYNC_20260913/01_CURRENT_CONTROL/EVIDENCE_GATES_v2.1.md` |
| `MASTER_RESEARCH_CHARTER.md` | cùng tên: `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/MASTER_RESEARCH_CHARTER.md`; `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/MASTER_RESEARCH_CHARTER.md` |
| `MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md` | không thấy |
| `RESEARCH_ARCHITECTURE.md` | cùng tên: `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/RESEARCH_ARCHITECTURE.md`; `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/RESEARCH_ARCHITECTURE.md` |
| `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260719.md` | không thấy |
| `RESEARCH_ARCHITECTURE_DECISION_RECORD_ACTION_ID_20260719.md` | không thấy |
| `RESEARCH_DIRECTION_AND_SCOPE.md` | cùng tên: `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/RESEARCH_DIRECTION_AND_SCOPE.md`; `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/RESEARCH_DIRECTION_AND_SCOPE.md` |
| `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md` | cùng tên: `01_LITERATURE_REVIEW/01_CURRENT_CONTROL/RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md`; `01_LITERATURE_REVIEW/90_ARCHIVE/01_SUPERSEDED_VERSIONS/PRE_SYNC_20260913/01_CURRENT_CONTROL/RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md` |
| `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` | cùng tên: `90_ARCHIVE/BACKUP_BEFORE_CURRENT_RESET_20260804/00_GOVERNANCE/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`; `01_LITERATURE_REVIEW/01_CURRENT_CONTROL/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` |
| `TERMINOLOGY_CONTROL_CURRENT.md` | cùng tên: `01_LITERATURE_REVIEW/01_CURRENT_CONTROL/TERMINOLOGY_CONTROL_CURRENT.md` |
| `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md`; `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md` |
| `V2.1_CORE_EVIDENCE_INDEX.md` | cùng tên: `01_LITERATURE_REVIEW/90_ARCHIVE/03_AUDIT_CLEANUP_AND_MANIFESTS/01_CORE_SOURCE_OF_TRUTH_REMAINDER/V2.1_CORE_EVIDENCE_INDEX.md` |

### `01_CURRENT_CONTROL` (11)

| Tệp | Bản thay thế |
|---|---|
| `CURRENT_DIRECTION_LOCK_20260804.md` | cùng tên: `01_LITERATURE_REVIEW/01_CURRENT_CONTROL/CURRENT_DIRECTION_LOCK_20260804.md` |
| `CURRENT_REPOSITORY_RESET_MANIFEST_20260804.csv` | không thấy |
| `CURRENT_RESET_FILE_MANIFEST_20260804.csv` | không thấy |
| `CURRENT_STATUS_AND_NEXT_DIRECTION.md` | cùng tên: `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/CURRENT_STATUS_AND_NEXT_DIRECTION.md`; `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/CURRENT_STATUS_AND_NEXT_DIRECTION.md` |
| `G1_G2_INTERFACE_DECISION_REGISTER.csv` | cùng tên: `01_LITERATURE_REVIEW/01_CURRENT_CONTROL/G1_G2_INTERFACE_DECISION_REGISTER.csv`; `01_LITERATURE_REVIEW/90_ARCHIVE/01_SUPERSEDED_VERSIONS/PRE_SYNC_20260913/01_CURRENT_CONTROL/G1_G2_INTERFACE_DECISION_REGISTER.csv` |
| `MASTER_INDEX_CURRENT.md` | cùng tên: `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/01_CURRENT_CONTROL/PROJECT_CLEANUP_20260718/MASTER_INDEX_CURRENT.md`; `90_ARCHIVE/BACKUP_BEFORE_CURRENT_RESET_20260804/01_CURRENT_CONTROL/MASTER_INDEX_CURRENT.md` |
| `PRE_UPDATE_GIT_STATUS_20260804.txt` | không thấy |
| `RA_SOAT_KET_QUA_BUOC1_BUOC2_20260805.md` | không thấy |
| `REPOSITORY_BASELINE_RETROSPECTIVE_APPROVAL_20260804.md` | không thấy |
| `REPOSITORY_FILE_CLASSIFICATION_20260804.csv` | không thấy |
| `SUPERSEDED_DOCUMENT_REGISTER_20260804.csv` | không thấy |

### `01_LITERATURE_REVIEW/03_OUTPUTS/01_TIEU_LUAN_TONG_QUAN` (5)

| Tệp | Bản thay thế |
|---|---|
| `figures/.gitkeep` | cùng nội dung: `03_RESEARCH_ASSETS/CODE/99_ARCHIVE_CODE/SHM_starter.ipynb`; `03_RESEARCH_ASSETS/99_ARCHIVE/DT-SHM-AI-STEEL-FRAME/pyrobotstructural/src/pyrobotstructural/exceptions.py` |
| `figures/Hinh_1_1_Chuoi_nghien_cuu_tong_the.png` | cùng nội dung: `01_LITERATURE_REVIEW/03_OUTPUTS/01_TIEU_LUAN_TONG_QUAN/TLTQ_28.09.2026/figures/Hinh_1_1_Chuoi_nghien_cuu_tong_the.png` |
| `figures/Hinh_5_1_Chuoi_dinh_danh_cot_loi.png` | cùng nội dung: `01_LITERATURE_REVIEW/03_OUTPUTS/01_TIEU_LUAN_TONG_QUAN/TLTQ_28.09.2026/figures/Hinh_5_1_Chuoi_dinh_danh_cot_loi.png` |
| `figures/Hinh_5_2_Kien_truc_kiem_chung_bon_lop.png` | cùng nội dung: `01_LITERATURE_REVIEW/03_OUTPUTS/01_TIEU_LUAN_TONG_QUAN/TLTQ_28.09.2026/figures/Hinh_5_2_Kien_truc_kiem_chung_bon_lop.png` |
| `figures/Hinh_5_3_Logic_ho_tro_hanh_dong.png` | cùng nội dung: `01_LITERATURE_REVIEW/03_OUTPUTS/01_TIEU_LUAN_TONG_QUAN/TLTQ_28.09.2026/figures/Hinh_5_3_Logic_ho_tro_hanh_dong.png` |

### `02_EVIDENCE_BASE/90_ARCHIVE_SUPERSEDED/20260804` (7)

| Tệp | Bản thay thế |
|---|---|
| `DUPLICATES/07_CLOSEST_COMPETITOR_MATRIX_PAPER2_20260718.csv` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/BACKUP_BEFORE_WRITEBACK_20260718/07_CLOSEST_COMPETITOR_MATRIX_PAPER2_20260718.csv`; `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/BACKUP_BEFORE_WRITEBACK_20260718/07_CLOSEST_COMPETITOR_MATRIX_PAPER2_20260718.csv` |
| `GOVERNANCE/CROSS_FILE_CONSISTENCY_AUDIT_20260804.md` | không thấy |
| `GOVERNANCE/CURRENT_REPOSITORY_RESET_REPORT_20260804.md` | không thấy |
| `MANIFEST/ARCHIVE_MANIFEST_20260804.csv` | không thấy |
| `OLD_SYNTHESIS/PHD_G1_G2_G3_EVIDENCE_GAP_AND_THESIS_DIRECTION_REPORT_VI.md` | không thấy |
| `OLD_SYNTHESIS/reportG2-G3.md` | không thấy |
| `ROADMAP_AND_PLANNING/PAPER2_DIRECTION_AND_GATE_v2.1_20260719.md` | cùng nội dung: `90_ARCHIVE/BACKUP_BEFORE_CURRENT_RESET_20260804/03_PAPERS/PAPER_2/PAPER2_DIRECTION_AND_GATE_v2.1_20260719.md` |

### `02_EVIDENCE_BASE/CURRENT` (7)

| Tệp | Bản thay thế |
|---|---|
| `00_MASTER_INDEX_CURRENT_20260804.md` | cùng tên: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/01_CURRENT_CONTROL/00_MASTER_INDEX_CURRENT_20260804.md` |
| `01_MASTER_G1_G2_G3_EVIDENCE_SYNTHESIS_20260804.md` | không thấy |
| `03_REPOSITORY_UPDATE_CHANGELOG_20260804.md` | không thấy |
| `EVIDENCE_MIGRATION_REPORT_v2.1.md` | cùng tên: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/EVIDENCE_MIGRATION_REPORT_v2.1.md` |
| `LIVING_EVIDENCE_BASE_CURRENT.md` | không thấy |
| `LIVING_EVIDENCE_BASE_v2.1_TRACEABILITY_CORE.md` | không thấy |
| `REPOSITORY_UPDATE_REPORT_20260804.md` | không thấy |

### `02_EVIDENCE_BASE/RQ1_GATE1` (1)

| Tệp | Bản thay thế |
|---|---|
| `03_RQ1_GATE1_METHOD_EVIDENCE_ADDENDUM_v1.0_20260718.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/03_RQ1_GATE1_METHOD_EVIDENCE_ADDENDUM_v1.0_20260718.md` |

### `02_EVIDENCE_BASE/RQ1_GATE1/RQ1_UPDATED_DEEP_READ_10.07` (17)

| Tệp | Bản thay thế |
|---|---|
| `1. Impact-of-Data-Leakage-in-Vibration-Signals-Used-for-Bearing-Fault-Diagnosis.pdf` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/References/1. Impact-of-Data-Leakage-in-Vibration-Signals-Used-for-Bearing-Fault-Diagnosis.pdf`; `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/02_RQ1_GATE1/LESLEY WHEAT_2024_Impact-of-Data-Leakage-in-Vibration-Signals.pdf` |
| `Abdeljaber et al. - 2018 - 1-D CNNs for structural damage detection Verification on a structural health monitoring benchmark d.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/02_RQ1_GATE1/Abdeljaber_2018_1D-CNNs-for-Structural-Damage-Detection.pdf` |
| `Avci et al. - 2021 - A review of vibration-based damage detection in civil structures From traditional methods to Machin.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/01_SHARED_FOUNDATIONS/Avci_2021_Review-of-Vibration-Based-Damage-Detection.pdf` |
| `Condition identification of bolted connections using a virtual viscous damper - AAM.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/02_RQ1_GATE1/Biswal_2021_Condition-Identification-of-Bolted-Connections.pdf` |
| `JSVCNNRealtimeDamageDetectionAbdeljaber-Avci-Kiranyaz-Gabbouj-Inman.pdf` | không thấy |
| `Optimal_sensor_placement_rev1.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/02_RQ1_GATE1/Mghazli_2023_Optimal-Sensor-Placement-of-Triaxial-Accelerometers.pdf` |
| `S2352012423003806.pdf` | không thấy |
| `SHMnet - AAM.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/02_RQ1_GATE1/Zhang_2020_SHMnet-Structural-Health-Monitoring.pdf` |
| `SHMnet.pdf` | không thấy |
| `Visualization and monitoring information management of bridge structure health and safety early warning based on BIM.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/01_SHARED_FOUNDATIONS/Deng_2022_BIM-Based-Bridge-Health-and-Safety-Monitoring.pdf` |
| `applsci-12-11107.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/02_RQ1_GATE1/Pal_2022_Machine-Learning-and-Model-Updating-for-Bolted-Connections.pdf` |
| `buildings-16-00824-v2.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/02_RQ1_GATE1/Redondo_2026_Optimal-Sensor-Placement-for-Structural-Health-Monitoring.pdf` |
| `s41598-023-27924-6.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/01_SHARED_FOUNDATIONS/Unknown_2023_Scientific-Reports-Structural-Health-Monitoring.pdf` |
| `theiler2018.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/01_SHARED_FOUNDATIONS/Theiler_2018_IFC-Monitor-for-Structural-Health-Monitoring.pdf` |
| `valinejadshoubi2019.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/01_SHARED_FOUNDATIONS/Valinejadshoubi_2019_BIM-Based-Data-Management-for-Structural-Health-Monitoring.pdf` |
| `weng2009.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/02_RQ1_GATE1/Weng_2009_Damage-Detection-by-Subspace-Identification-and-FE-Updating.pdf` |
| `yang2014.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/02_RQ1_GATE1/Yang_2014_Damage-Identification-of-Bolt-Connections.pdf` |

### `02_EVIDENCE_BASE/RQ2_GATES2_3` (15)

| Tệp | Bản thay thế |
|---|---|
| `00_README_START_HERE.md` | cùng tên: `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/00_README_START_HERE.md`; `90_ARCHIVE/BACKUP_BEFORE_CURRENT_RESET_20260804/00_README_START_HERE.md` |
| `04_RQ2_TRACEABILITY_EVIDENCE_ADDENDUM_v1.2_20260718.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/04_RQ2_TRACEABILITY_EVIDENCE_ADDENDUM_v1.2_20260718.md` |
| `G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md` | cùng nội dung: `01_LITERATURE_REVIEW/90_ARCHIVE/01_SUPERSEDED_VERSIONS/PRE_SYNC_20260913/02_DEEP_READ_CURRENT_PDF/03_RQ2_GATE2_3/G1_TO_G2_CONDITION_EVIDENCE_INTERFACE_v1.0.md` |
| `G2_G3_PAPER2_CURRENT_ROADMAP_v2.1_20260804.md` | không thấy |
| `G2_G3_PAPER2_REVISED_ROADMAP_v1.1.03.08.2026.md` | không thấy |
| `G2_G3_RECENT_EVIDENCE_SCREENING_2023_2026.md` | cùng nội dung: `01_LITERATURE_REVIEW/03_OUTPUTS/05_PAPER_2_TRACEABILITY/01_EVIDENCE/G2_G3_RECENT_EVIDENCE_SCREENING_2023_2026.md` |
| `G2_G3_REVIT_IFC_AIM_EXECUTION_ROADMAP.md` | cùng nội dung: `01_LITERATURE_REVIEW/90_ARCHIVE/03_AUDIT_CLEANUP_AND_MANIFESTS/02_EVIDENCE_REMAINDER/G2_G3_REVIT_IFC_AIM_EXECUTION_ROADMAP.md` |
| `G2_G3_ROUND1_DEEP_READ_AND_NOVELTY_BOUNDARY.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/G2_G3_ROUND1_DEEP_READ_AND_NOVELTY_BOUNDARY.md` |
| `G2_G3_ROUND2_INSPECTION_ACTION_MODEL_DEEP_READ.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/G2_G3_ROUND2_INSPECTION_ACTION_MODEL_DEEP_READ.md` |
| `G2_G3_ROUND3A_NOVELTY_AND_SCHEMA_BOUNDARY.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/G2_G3_ROUND3A_NOVELTY_AND_SCHEMA_BOUNDARY.md` |
| `G2_G3_ROUND3B_HISTORY_ACCOUNTABILITY_AND_SEARCH_CLOSURE.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/G2_G3_ROUND3B_HISTORY_ACCOUNTABILITY_AND_SEARCH_CLOSURE.md` |
| `G2_G3_ROUND4_CQ_CONSTRAINT_ACCOUNTABILITY_DEEP_READ_20260809.md` | cùng nội dung: `01_LITERATURE_REVIEW/03_OUTPUTS/05_PAPER_2_TRACEABILITY/01_EVIDENCE/G2_G3_ROUND4_CQ_CONSTRAINT_ACCOUNTABILITY_DEEP_READ_20260809.md` |
| `G2_G3_SCREENING_EVIDENCE_AND_GAP_REPORT.md` | cùng nội dung: `01_LITERATURE_REVIEW/03_OUTPUTS/05_PAPER_2_TRACEABILITY/01_EVIDENCE/G2_G3_SCREENING_EVIDENCE_AND_GAP_REPORT.md` |
| `PHD_BIM_AIM_IMPLEMENTATION_ROADMAP.md` | không thấy |
| `ROUND4_VERIFIED_EVIDENCE_RECORD_v1.1.md` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/03_RQ2_GATE2_3/ROUND4_VERIFIED_EVIDENCE_RECORD_v1.1.md` |

### `02_EVIDENCE_BASE/RQ2_GATES2_3/DEEP_READ_20.07.2026` (15)

| Tệp | Bản thay thế |
|---|---|
| `(Antunes, 2024)_Ontology-based BIM-AMS integration in European Highways.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/03_RQ2_GATE2_3/Antunes_2024_Ontology-Based-BIM-AMS-Integration-in-European-Highways.pdf` |
| `1-s2.0-S0926580519314785-main.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/03_RQ2_GATE2_3/Boje_2020_Semantic-Construction-Digital-Twin.pdf` |
| `10.1016@j.autcon.2020.103088.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/03_RQ2_GATE2_3/Isailovic_2020_Bridge-Damage-IFC-Semantic-Enrichment-and-Visualization.pdf` |
| `Gate 2.1 - 1-s2.0-S2667305324000425-main.pdf` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/References/Gate 2.1 - 1-s2.0-S2667305324000425-main.pdf` |
| `Gate 2.1 - caos-9.pdf` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/References/Gate 2.1 - caos-9.pdf`; `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/03_RQ2_GATE2_3/Keet_2025_Characterising-Competency-Questions-for-Ontologies.pdf` |
| `Gate 2.3 2026_19-ITcon-Chen.pdf` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/References/Gate 2.3 2026_19-ITcon-Chen.pdf`; `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/03_RQ2_GATE2_3/Chen_2026_Automated-IFC-Compliant-Bridge-Information-Models.pdf` |
| `Johannes et al. (2021) Identifying_Maturity_Dimensions_for_Smart_Maintena.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/03_RQ2_GATE2_3/Johannes_2021_Identifying-Maturity-Dimensions-for-Smart-Maintenance.pdf` |
| `Lee et al. (2021) — Provenance và accountability.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/03_RQ2_GATE2_3/Lee_2021_BIM-Data-Provenance-and-Accountability.pdf` |
| `applsci-16-04642.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/03_RQ2_GATE2_3/Piras_2026_Open-Standard-BIM-CMMS-Integration.pdf`; `01_LITERATURE_REVIEW/03_OUTPUTS/01_TIEU_LUAN_TONG_QUAN/TLTQ_28.09.2026/File pdf/Piras et al. - 2026 - An Open Standard Methodology for BIM-CMMS Integration Enhancing Facility Operations Through IFC-Bas.pdf` |
| `buildings-15-01312.pdf` | cùng nội dung: `01_KNOWLEDGE/LITERATURE/2. SHM + VIBRATION + DAMAGE DETECTION/SHM_Design and Validation of a Real-Time Maintenance Monitoring System Using BIM and Digital Twin Integration.pdf`; `01_KNOWLEDGE/LITERATURE/LITERATURE_RESCREEN_20260809/08_SUPPORTING_NEXT_ROUND_20260809/SELECTED_SUPPORTING_NEXT_ROUND/G4_G5_FIELD_DECISION/SHM_Design and Validation of a Real-Time Maintenance Monitoring System Using BIM and Digital Twin Integration.pdf` |
| `buildings-15-02633.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/03_RQ2_GATE2_3/Jia_2025_Semantic-Web-and-IFC-Based-BIM-Compliance-Checking.pdf`; `01_LITERATURE_REVIEW/03_OUTPUTS/01_TIEU_LUAN_TONG_QUAN/TLTQ_28.09.2026/File pdf/buildings-15-02633.pdf` |
| `kim2018.pdf` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/References/Gate 2.1 kim2018.pdf`; `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/03_RQ2_GATE2_3/Kim_2018_Integration-of-IFC-and-Facility-Management-Information.pdf` |
| `pauwels2016.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/03_RQ2_GATE2_3/Pauwels_2016_EXPRESS-to-OWL-for-Construction-Industry.pdf` |
| `sustainability-11-04583.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/03_RQ2_GATE2_3/Wan_2019_BIM-Based-Bridge-Management-System.pdf` |
| `Çelik et al. (2023) — BIM data provenance.pdf` | cùng nội dung: `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/03_RQ2_GATE2_3/Celik_2023_Blockchain-Supported-BIM-Data-Provenance.pdf` |

### `02_EVIDENCE_BASE/RQ3_GATE4` (1)

| Tệp | Bản thay thế |
|---|---|
| `05_RQ3_FIELD_FEASIBILITY_EVIDENCE_ADDENDUM_v1.0_20260718.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/05_RQ3_FIELD_FEASIBILITY_EVIDENCE_ADDENDUM_v1.0_20260718.md` |

### `02_EVIDENCE_BASE/WP4_GATE5` (5)

| Tệp | Bản thay thế |
|---|---|
| `06_WP4_DECISION_SUPPORT_EVIDENCE_ADDENDUM_v1.0_20260718.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/06_WP4_DECISION_SUPPORT_EVIDENCE_ADDENDUM_v1.0_20260718.md` |
| `Gate 4. Long-term-health-monitoring-of-concrete-and-steel-bridges-under-large-and-missing-data-by.pdf` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/References/Gate 4. Long-term-health-monitoring-of-concrete-and-steel-bridges-under-large-and-missing-data-by.pdf`; `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/04_RQ3_GATE4_5/Entezami_2023_Long-Term-Health-Monitoring-of-Concrete-and-Steel-Bridges.pdf` |
| `Gate 4.pdf` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/References/Gate 4.pdf`; `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/04_RQ3_GATE4_5/Tan_2023_Structural-Health-Monitoring-Article.pdf` |
| `Gate 4_kohler2005.pdf` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/References/Gate 4_kohler2005.pdf`; `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/04_RQ3_GATE4_5/Kohler_2005_Earthquake-and-Ambient-Vibration-Monitoring.pdf` |
| `Gate4. yarnold2015.pdf` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/References/Gate4. yarnold2015.pdf`; `01_LITERATURE_REVIEW/02_DEEP_READ_CURRENT_PDF/04_RQ3_GATE4_5/Yarnold_2015_Temperature-Based-Structural-Health-Monitoring.pdf` |

### `02_EVIDENCE_BASE/ZOTERO_DEEP_READ` (5)

| Tệp | Bản thay thế |
|---|---|
| `02_NEW_DEEP_READ_EVIDENCE_MATRIX_20260718.csv` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/BACKUP_BEFORE_WRITEBACK_20260718/02_NEW_DEEP_READ_EVIDENCE_MATRIX_20260718.csv`; `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/BACKUP_BEFORE_WRITEBACK_20260718/02_NEW_DEEP_READ_EVIDENCE_MATRIX_20260718.csv` |
| `08_DUPLICATE_AND_METADATA_CORRECTION_LOG_20260718.csv` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/BACKUP_BEFORE_WRITEBACK_20260718/08_DUPLICATE_AND_METADATA_CORRECTION_LOG_20260718.csv`; `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/BACKUP_BEFORE_WRITEBACK_20260718/08_DUPLICATE_AND_METADATA_CORRECTION_LOG_20260718.csv` |
| `09_ZOTERO_DEEP_READ_COMPLETION_REPORT_20260718.md` | cùng tên: `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/09_ZOTERO_DEEP_READ_COMPLETION_REPORT_20260718.md`; `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/BACKUP_BEFORE_WRITEBACK_20260718/09_ZOTERO_DEEP_READ_COMPLETION_REPORT_20260718.md` |
| `10_ZOTERO_WRITEBACK_QUEUE_20260718.md` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/BACKUP_BEFORE_WRITEBACK_20260718/10_ZOTERO_WRITEBACK_QUEUE_20260718.md`; `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/BACKUP_BEFORE_WRITEBACK_20260718/10_ZOTERO_WRITEBACK_QUEUE_20260718.md` |
| `PHASE0_SAFETY_BACKUP_AND_DRY_RUN_REPORT_20260718.md` | cùng tên: `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/PHASE0_SAFETY_BACKUP_AND_DRY_RUN_REPORT_20260718.md`; `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/PHASE0_SAFETY_BACKUP_AND_DRY_RUN_REPORT_20260718.md` |

### `03_PAPERS` (5)

| Tệp | Bản thay thế |
|---|---|
| `CONFERENCE_PAPER_PLAN_v1_0_20260807 (1).md` | không thấy |
| `CONFERENCE_PAPER_PLAN_v1_0_20260807.md` | không thấy |
| `CONFERENCE_PAPER_PLAN_v1_1_20260807.md` | không thấy |
| `DANH_MUC_BAI_HOI_THAO_HO_TRO_SC1_SC5_v1_2_20260807.md` | không thấy |
| `DANH_MUC_BAI_HOI_THAO_HO_TRO_SC1_SC7_v1_3_20260807.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/DANH_MUC_BAI_HOI_THAO_HO_TRO_SC1_SC7_v1_3_20260807.md` |

### `03_PAPERS/PAPER_1` (6)

| Tệp | Bản thay thế |
|---|---|
| `BAO_CAO_TONG_HOP_DINH_HUONG_PAPER1_20260806.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/03_PAPER_1/BAO_CAO_TONG_HOP_DINH_HUONG_PAPER1_20260806.md` |
| `PAPER1_DIRECTION_AND_GATE_v2.1_20260719.md` | không thấy |
| `PAPER1_GATE1_INTERNAL_QA_CHECKLIST_v1.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/03_PAPER_1/PAPER1_GATE1_INTERNAL_QA_CHECKLIST_v1.md` |
| `PAPER1_ILLUSTRATIVE_TABLES_AND_FIGURES_INDEX_v1.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/03_PAPER_1/PAPER1_ILLUSTRATIVE_TABLES_AND_FIGURES_INDEX_v1.md` |
| `PAPER1_INTERNAL_PRELIMINARY_EVIDENCE_NOTE_v3.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/03_PAPER_1/PAPER1_INTERNAL_PRELIMINARY_EVIDENCE_NOTE_v3.md` |
| `PAPER1_IT_EXECUTION_SPEC_v5_20260719.md` | không thấy |

### `03_PAPERS/PAPER_1/CURRENT_MANUSCRIPT` (1)

| Tệp | Bản thay thế |
|---|---|
| `PAPER1_GATE1_Q2_VERIFIED_EVIDENCE_REVISED_v2_MANUSCRIPT_SOURCE_20260718.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/03_PAPER_1/PAPER1_GATE1_Q2_VERIFIED_EVIDENCE_REVISED_v2_MANUSCRIPT_SOURCE_20260718.md` |

### `03_PAPERS/PAPER_1/GATE1_EVIDENCE` (2)

| Tệp | Bản thay thế |
|---|---|
| `PAPER1_GATE1_CLAIM_EVIDENCE_AUDIT_v2.md` | cùng tên: `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Paper 1/PAPER1_GATE1_CLAIM_EVIDENCE_AUDIT_v2.md` |
| `PAPER1_GATE1_READINESS_REPORT_v2.md` | cùng tên: `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Paper 1/PAPER1_GATE1_READINESS_REPORT_v2.md` |

### `03_PAPERS/PAPER_1/IT_REQUESTS` (1)

| Tệp | Bản thay thế |
|---|---|
| `PAPER1_GATE1_DATA_ANALYSIS_REQUESTS_FOR_IT_v2.md` | cùng tên: `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Paper 1/PAPER1_GATE1_DATA_ANALYSIS_REQUESTS_FOR_IT_v2.md` |

### `03_PAPERS/PAPER_1/REFERENCE_AUDIT` (1)

| Tệp | Bản thay thế |
|---|---|
| `PAPER1_GATE1_VERIFIED_REFERENCE_AUDIT_v2.csv` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Paper 1/PAPER1_GATE1_VERIFIED_REFERENCE_AUDIT_v2.csv` |

### `03_PAPERS/PAPER_1/REVISION_HISTORY` (1)

| Tệp | Bản thay thế |
|---|---|
| `PAPER1_GATE1_MAJOR_REVISION_LOG_v2.md` | cùng tên: `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Paper 1/PAPER1_GATE1_MAJOR_REVISION_LOG_v2.md` |

### `03_PAPERS/PAPER_2` (1)

| Tệp | Bản thay thế |
|---|---|
| `PAPER2_CURRENT_DIRECTION_v2.1_20260804.md` | không thấy |

### `03_PAPERS/PAPER_3` (1)

| Tệp | Bản thay thế |
|---|---|
| `PAPER3_FIELD_FEASIBILITY_DIRECTION_v2.1_20260719.md` | cùng tên: `01_LITERATURE_REVIEW/03_OUTPUTS/06_PAPER_3_FIELD_FEASIBILITY/PAPER3_FIELD_FEASIBILITY_DIRECTION_v2.1_20260719.md` |

### `03_PAPERS/PAPER_S1_SENSOR_COMPARISON_CANDIDATE` (1)

| Tệp | Bản thay thế |
|---|---|
| `Yêu cầu phân tích PASCO–ADXL cho Paper S1.docx` | không thấy |

### `04_PHD_SPECIAL_TOPICS/CHUYEN_DE_TONG_QUAN` (7)

| Tệp | Bản thay thế |
|---|---|
| `CHUYEN_DE_TONG_QUAN_EVIDENCE_GAPS_v1.md` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/CHUYEN_DE_TONG_QUAN_EVIDENCE_GAPS_v1.md` |
| `DE_CUONG_DANG_KY_TIEU_LUAN_TONG_QUAN_HOAN_CHINH_20260805.docx` | không thấy |
| `EVIDENCE_MATRIX_CHUYEN_DE_TONG_QUAN_v1.csv` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/EVIDENCE_MATRIX_CHUYEN_DE_TONG_QUAN_v1.csv` |
| `MATRIX_CHUYEN_DE_RQ_WP_PAPER_GATE_v1.md` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/MATRIX_CHUYEN_DE_RQ_WP_PAPER_GATE_v1.md` |
| `OUTLINE_CHUYEN_DE_TONG_QUAN_CHI_TIET_v1.md` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/OUTLINE_CHUYEN_DE_TONG_QUAN_CHI_TIET_v1.md` |
| `OUTLINE_TLTQ_RESTRUCTURED_v2.0_20260805.md` | không thấy |
| `TIEU_LUAN_TONG_QUAN_FULL_DRAFT_20260805.docx` | không thấy |

### `05_DATA_CODE_AND_EXPERIMENTS/CAMPAIGN_DOCUMENTATION` (1)

| Tệp | Bản thay thế |
|---|---|
| `Checklist_Campaign_3_Gate1.docx` | cùng nội dung: `02_DATA_CODE_AND_EXPERIMENTS/CAMPAIGN_DOCUMENTATION/Checklist_Campaign_3_Gate1.docx` |

### `05_DATA_CODE_AND_EXPERIMENTS/CANONICAL_THREE_CAMPAIGN_DATASET` (8)

| Tệp | Bản thay thế |
|---|---|
| `00_README.md` | không thấy |
| `03_CHANNEL_QUALITY_RULES.md` | không thấy |
| `07_DATA_DICTIONARY.md` | không thấy |
| `08_AUTOMATED_VALIDATION_RESULTS.csv` | cùng nội dung: `02_DATA_CODE_AND_EXPERIMENTS/CANONICAL_THREE_CAMPAIGN_DATASET/08_AUTOMATED_VALIDATION_RESULTS.csv` |
| `08_DATASET_VARIANTS.md` | không thấy |
| `09_DATASET_VALIDATION_REPORT.md` | không thấy |
| `10_REPRODUCIBILITY_MANIFEST.md` | không thấy |
| `11_DATASET_HANDOFF_FOR_IT.md` | không thấy |

### `05_DATA_CODE_AND_EXPERIMENTS/THREE_CAMPAIGN_REANALYSIS` (14)

| Tệp | Bản thay thế |
|---|---|
| `00_EXECUTIVE_REPORT.md` | không thấy |
| `01_ENVIRONMENT_PROVENANCE.md` | không thấy |
| `03_DATA_QUALITY_AND_PROVENANCE_LOG.csv` | cùng nội dung: `02_DATA_CODE_AND_EXPERIMENTS/THREE_CAMPAIGN_REANALYSIS/03_DATA_QUALITY_AND_PROVENANCE_LOG.csv` |
| `05_WITHIN_CAMPAIGN_LORO_RESULTS.csv` | cùng nội dung: `02_DATA_CODE_AND_EXPERIMENTS/THREE_CAMPAIGN_REANALYSIS/05_WITHIN_CAMPAIGN_LORO_RESULTS.csv` |
| `06_CROSS_CAMPAIGN_RESULTS.csv` | cùng nội dung: `02_DATA_CODE_AND_EXPERIMENTS/THREE_CAMPAIGN_REANALYSIS/06_CROSS_CAMPAIGN_RESULTS.csv` |
| `07_BASELINE_MODEL_COMPARISON.csv` | cùng nội dung: `02_DATA_CODE_AND_EXPERIMENTS/THREE_CAMPAIGN_REANALYSIS/07_BASELINE_MODEL_COMPARISON.csv` |
| `08_PERMUTATION_RESULTS.csv` | cùng nội dung: `02_DATA_CODE_AND_EXPERIMENTS/THREE_CAMPAIGN_REANALYSIS/08_PERMUTATION_RESULTS.csv` |
| `09_SENSOR_CONFIGURATION_RESULTS.csv` | cùng nội dung: `02_DATA_CODE_AND_EXPERIMENTS/THREE_CAMPAIGN_REANALYSIS/09_SENSOR_CONFIGURATION_RESULTS.csv` |
| `11_SENSITIVITY_RESULTS.csv` | cùng nội dung: `02_DATA_CODE_AND_EXPERIMENTS/THREE_CAMPAIGN_REANALYSIS/11_SENSITIVITY_RESULTS.csv` |
| `12_CONFUSION_MATRICES/cross_LOCO_S1S2_Ax_heldout_Campaign1_RF.csv` | cùng nội dung: `02_DATA_CODE_AND_EXPERIMENTS/THREE_CAMPAIGN_REANALYSIS/12_CONFUSION_MATRICES/cross_LOCO_S1S2_Ax_heldout_Campaign1_RF.csv` |
| `12_CONFUSION_MATRICES/within_Campaign1_S1S2_Ax_R1_RF.csv` | cùng nội dung: `02_DATA_CODE_AND_EXPERIMENTS/THREE_CAMPAIGN_REANALYSIS/12_CONFUSION_MATRICES/within_Campaign1_S1S2_Ax_R1_RF.csv` |
| `12_CONFUSION_MATRICES/within_Campaign2_S1S2S3_xyz_R7_RF.csv` | cùng nội dung: `02_DATA_CODE_AND_EXPERIMENTS/THREE_CAMPAIGN_REANALYSIS/12_CONFUSION_MATRICES/within_Campaign2_S1S2S3_xyz_R7_RF.csv` |
| `13_TRAINING_CURVES/README.md` | cùng tên: `01_KNOWLEDGE/LITERATURE/LITERATURE_RESCREEN_20260809/08_SUPPORTING_NEXT_ROUND_20260809/SELECTED_SUPPORTING_NEXT_ROUND/PDF_MISSING_OR_UNVERIFIED/README.md`; `03_RESEARCH_ASSETS/99_ARCHIVE/DT-SHM-AI-STEEL-FRAME/pyrobotstructural/README.md` |
| `15_NEXT_ANALYSIS_RECOMMENDATION.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/06_DATA_AND_EXPERIMENTS/15_NEXT_ANALYSIS_RECOMMENDATION.md` |

### `06_LITERATURE_AND_ZOTERO/PERPLEXITY_DISCOVERY` (12)

| Tệp | Bản thay thế |
|---|---|
| `1. Leakage-Safe Grouped Cross-Validation Evidence for Vibration SHM Classification.md` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/1. Leakage-Safe Grouped Cross-Validation Evidence for Vibration SHM Classification.md` |
| `10. Act as a critical reviewer and challenge this.md` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/10. Act as a critical reviewer and challenge this.md` |
| `2. Find studies comparing sensor locations, channels,.md` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/2. Find studies comparing sensor locations, channels,.md` |
| `2B. Find peer-reviewed methods for estimating unce.md` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/2B. Find peer-reviewed methods for estimating unce.md` |
| `3. Find peer-reviewed methodological papers on com.md` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/3. Find peer-reviewed methodological papers on com.md` |
| `4. Find peer-reviewed research on data provenance,.md` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/4. Find peer-reviewed research on data provenance,.md` |
| `5. Find peer-reviewed studies linking BIM or IFC c.md` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/5. Find peer-reviewed studies linking BIM or IFC c.md` |
| `6. Find authoritative peer-reviewed frameworks def.md` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/6. Find authoritative peer-reviewed frameworks def.md` |
| `7. Peer-Reviewed Field Studies  Vibration Monitoring, Operational Baselines, and Low-Cost Sensor Deployment in Steel Structures.md` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/7. Peer-Reviewed Field Studies  Vibration Monitoring, Operational Baselines, and Low-Cost Sensor Deployment in Steel Structures.md` |
| `8. Find peer-reviewed methodological studies on co.md` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/8. Find peer-reviewed methodological studies on co.md` |
| `9. Find peer-reviewed studies on transparent, huma.md` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/9. Find peer-reviewed studies on transparent, huma.md` |
| `README.md` | cùng tên: `01_KNOWLEDGE/LITERATURE/LITERATURE_RESCREEN_20260809/08_SUPPORTING_NEXT_ROUND_20260809/SELECTED_SUPPORTING_NEXT_ROUND/PDF_MISSING_OR_UNVERIFIED/README.md`; `03_RESEARCH_ASSETS/99_ARCHIVE/DT-SHM-AI-STEEL-FRAME/pyrobotstructural/README.md` |

### `06_LITERATURE_AND_ZOTERO/STANDARDS` (1)

| Tệp | Bản thay thế |
|---|---|
| `ISO-IEC-30173-2023.pdf` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/References/ISO-IEC-30173-2023.pdf` |

### `06_LITERATURE_AND_ZOTERO/ZOTERO_MCP` (1)

| Tệp | Bản thay thế |
|---|---|
| `README.md` | cùng tên: `01_KNOWLEDGE/LITERATURE/LITERATURE_RESCREEN_20260809/08_SUPPORTING_NEXT_ROUND_20260809/SELECTED_SUPPORTING_NEXT_ROUND/PDF_MISSING_OR_UNVERIFIED/README.md`; `03_RESEARCH_ASSETS/99_ARCHIVE/DT-SHM-AI-STEEL-FRAME/pyrobotstructural/README.md` |

### `07_PROMPTS_AND_HANDOFFS/ASSETS` (1)

| Tệp | Bản thay thế |
|---|---|
| `BIM-AEC-CLAUDE.jpg` | cùng nội dung: `03_PROMPTS_AND_HANDOFFS/ASSETS/BIM-AEC-CLAUDE.jpg` |

### `07_PROMPTS_AND_HANDOFFS/NOTEBOOKLM` (1)

| Tệp | Bản thay thế |
|---|---|
| `NOTEBOOKLM_BRIEF_G1_PAPER1_VS_AVCI_2021.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/03_PAPER_1/NOTEBOOKLM_BRIEF_G1_PAPER1_VS_AVCI_2021.md` |

### `07_PROMPTS_AND_HANDOFFS/OPENCODE` (3)

| Tệp | Bản thay thế |
|---|---|
| `OPENCODE_SEQUENTIAL_GATE_EXECUTION_AND_EVIDENCE_MERGE_PROMPT_20260718.md` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Perplexity_Pro/OPENCODE_SEQUENTIAL_GATE_EXECUTION_AND_EVIDENCE_MERGE_PROMPT_20260718.md`; `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/OPENCODE_SEQUENTIAL_GATE_EXECUTION_AND_EVIDENCE_MERGE_PROMPT_20260718.md` |
| `PAPER1/PROMPT_KHOI_TAO_CHAT_MOI_PAPER1_CONTROL_ROOM_20260718.md` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Paper 1/PROMPT_KHOI_TAO_CHAT_MOI_PAPER1_CONTROL_ROOM_20260718.md`; `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/03_PAPER_1/PROMPT_KHOI_TAO_CHAT_MOI_PAPER1_CONTROL_ROOM_20260718.md` |
| `PROMPT_OPENCODE_EXECUTE_FULL_CLEANUP_DELETE_SUPERSEDED_20260718.md` | cùng nội dung: `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/PROMPT_OPENCODE_EXECUTE_FULL_CLEANUP_DELETE_SUPERSEDED_20260718.md`; `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/07_PROMPTS_AND_HANDOFFS/PROMPT_OPENCODE_EXECUTE_FULL_CLEANUP_DELETE_SUPERSEDED_20260718.md` |

### `07_PROMPTS_AND_HANDOFFS/PAPER1` (1)

| Tệp | Bản thay thế |
|---|---|
| `PROMPT_CLAUDE_COWORK_PAPER1_EMPTY_RESULTS_v3.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/03_PAPER_1/PROMPT_CLAUDE_COWORK_PAPER1_EMPTY_RESULTS_v3.md` |

### `07_PROMPTS_AND_HANDOFFS/PROMPT_CONTROL_CENTER` (8)

| Tệp | Bản thay thế |
|---|---|
| `00_PROJECT_INSTRUCTIONS.md` | không thấy |
| `01_PROMPT_REQUEST_TEMPLATE.md` | không thấy |
| `02_PROMPT_CATALOG.md` | không thấy |
| `03_MODEL_ROUTING_GUIDE.md` | không thấy |
| `04_PROMPT_QUALITY_CHECKLIST.md` | không thấy |
| `05_DOMAIN_PROFILE_PHD.md` | không thấy |
| `PROMPT_CONTROL_CENTER_PROJECT_INSTRUCTIONS.md` | không thấy |
| `README.md` | cùng tên: `01_KNOWLEDGE/LITERATURE/LITERATURE_RESCREEN_20260809/08_SUPPORTING_NEXT_ROUND_20260809/SELECTED_SUPPORTING_NEXT_ROUND/PDF_MISSING_OR_UNVERIFIED/README.md`; `03_RESEARCH_ASSETS/99_ARCHIVE/DT-SHM-AI-STEEL-FRAME/pyrobotstructural/README.md` |

### `07_PROMPTS_AND_HANDOFFS/phd-prompt-compressor` (2)

| Tệp | Bản thay thế |
|---|---|
| `SKILL.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/07_PROMPTS_AND_HANDOFFS/SKILL.md` |
| `references/phd-scope.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/07_PROMPTS_AND_HANDOFFS/phd-scope.md`; `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/07_PROMPTS_AND_HANDOFFS/phd-scope_MOVED_1.md` |

### `07_PROMPTS_AND_HANDOFFS/phd-prompt-router` (3)

| Tệp | Bản thay thế |
|---|---|
| `SKILL.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/07_PROMPTS_AND_HANDOFFS/SKILL_MOVED_1.md` |
| `references/model-guidance.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/07_PROMPTS_AND_HANDOFFS/model-guidance.md` |
| `references/phd-scope.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/07_PROMPTS_AND_HANDOFFS/phd-scope.md`; `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/07_PROMPTS_AND_HANDOFFS/phd-scope_MOVED_1.md` |

### `08_AI_SKILL_SYSTEM/ARS_TO_PHD_SKILLS_20260810` (4)

| Tệp | Bản thay thế |
|---|---|
| `00_ARS_INVENTORY.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/ARS_TO_PHD_SKILLS_20260810/00_ARS_INVENTORY.md` |
| `01_ARS_PHD_AUDIT.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/ARS_TO_PHD_SKILLS_20260810/01_ARS_PHD_AUDIT.md` |
| `02_PHD_SKILL_ARCHITECTURE.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/ARS_TO_PHD_SKILLS_20260810/02_PHD_SKILL_ARCHITECTURE.md` |
| `03_SKILL_EVALUATION_REPORT.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/ARS_TO_PHD_SKILLS_20260810/03_SKILL_EVALUATION_REPORT.md` |

### `08_AI_SKILL_SYSTEM/phd-dt-research-skills` (19)

| Tệp | Bản thay thế |
|---|---|
| `README.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_TRUOC_DONG_BO/phd-dt-research-skills/README.md` |
| `_phd-canon/epistemic-ladder.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_TRUOC_DONG_BO/phd-dt-research-skills/_phd-canon/epistemic-ladder.md`; `04_AI_SKILL_SYSTEM/phd-dt-research-skills/_phd-canon/epistemic-ladder.md` |
| `_phd-canon/failure-modes.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_TRUOC_DONG_BO/phd-dt-research-skills/_phd-canon/failure-modes.md`; `04_AI_SKILL_SYSTEM/phd-dt-research-skills/_phd-canon/failure-modes.md` |
| `_phd-canon/gate-model.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_TRUOC_DONG_BO/phd-dt-research-skills/_phd-canon/gate-model.md` |
| `_phd-canon/novelty-boundary.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_TRUOC_DONG_BO/phd-dt-research-skills/_phd-canon/novelty-boundary.md` |
| `_phd-canon/output-discipline.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_TRUOC_DONG_BO/phd-dt-research-skills/_phd-canon/output-discipline.md`; `04_AI_SKILL_SYSTEM/phd-dt-research-skills/_phd-canon/output-discipline.md` |
| `_phd-canon/research-chain.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_TRUOC_DONG_BO/phd-dt-research-skills/_phd-canon/research-chain.md` |
| `_phd-canon/scope-control.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_TRUOC_DONG_BO/phd-dt-research-skills/_phd-canon/scope-control.md`; `04_AI_SKILL_SYSTEM/phd-dt-research-skills/_phd-canon/scope-control.md` |
| `_phd-canon/which-skill.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_TRUOC_DONG_BO/phd-dt-research-skills/_phd-canon/which-skill.md` |
| `phd-literature-evidence/SKILL.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_TRUOC_DONG_BO/phd-dt-research-skills/phd-literature-evidence/SKILL.md` |
| `phd-literature-evidence/evals/evals.json` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_TRUOC_DONG_BO/phd-dt-research-skills/phd-literature-evidence/evals/evals.json`; `04_AI_SKILL_SYSTEM/phd-dt-research-skills/phd-literature-evidence/evals/evals.json` |
| `phd-literature-evidence/references/claim-source-mapping.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_TRUOC_DONG_BO/phd-dt-research-skills/phd-literature-evidence/references/claim-source-mapping.md`; `04_AI_SKILL_SYSTEM/phd-dt-research-skills/phd-literature-evidence/references/claim-source-mapping.md` |
| `phd-literature-evidence/references/corpus-map.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_TRUOC_DONG_BO/phd-dt-research-skills/phd-literature-evidence/references/corpus-map.md`; `04_AI_SKILL_SYSTEM/phd-dt-research-skills/phd-literature-evidence/references/corpus-map.md` |
| `phd-literature-evidence/references/source-verification.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_TRUOC_DONG_BO/phd-dt-research-skills/phd-literature-evidence/references/source-verification.md`; `04_AI_SKILL_SYSTEM/phd-dt-research-skills/phd-literature-evidence/references/source-verification.md` |
| `phd-paper-reviewer/SKILL.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_TRUOC_DONG_BO/phd-dt-research-skills/phd-paper-reviewer/SKILL.md` |
| `phd-paper-reviewer/references/re-review.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_TRUOC_DONG_BO/phd-dt-research-skills/phd-paper-reviewer/references/re-review.md`; `04_AI_SKILL_SYSTEM/phd-dt-research-skills/phd-paper-reviewer/references/re-review.md` |
| `phd-paper-reviewer/references/review-protocol.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_TRUOC_DONG_BO/phd-dt-research-skills/phd-paper-reviewer/references/review-protocol.md`; `04_AI_SKILL_SYSTEM/phd-dt-research-skills/phd-paper-reviewer/references/review-protocol.md` |
| `phd-research-state/SKILL.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_TRUOC_DONG_BO/phd-dt-research-skills/phd-research-state/SKILL.md` |
| `phd-research-state/references/state-sources.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_TRUOC_DONG_BO/phd-dt-research-skills/phd-research-state/references/state-sources.md`; `04_AI_SKILL_SYSTEM/phd-dt-research-skills/phd-research-state/references/state-sources.md` |

### `08_AI_SKILL_SYSTEM/phd-literature-evidence-workspace` (50)

| Tệp | Bản thay thế |
|---|---|
| `PILOT1_REVIEW.html` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/PILOT1_REVIEW.html` |
| `_tools/adapt_for_aggregator.py` | cùng nội dung: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/_tools/adapt_for_aggregator.py` |
| `_tools/grade_eval1.py` | cùng nội dung: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/_tools/grade_eval1.py` |
| `_tools/setup_eval_meta.py` | cùng nội dung: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/_tools/setup_eval_meta.py` |
| `iteration-1/benchmark.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/benchmark.json` |
| `iteration-1/benchmark.md` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/benchmark.md` |
| `iteration-1/eval-0-novelty-inflation-sensor-to-bim/eval_metadata.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/eval_metadata.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-1-citation-fabrication-request/eval_metadata.json` |
| `iteration-1/eval-0-novelty-inflation-sensor-to-bim/with_skill/grading.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/grading.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/grading.json` |
| `iteration-1/eval-0-novelty-inflation-sensor-to-bim/with_skill/outputs/response.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/with_skill/outputs/response.md` |
| `iteration-1/eval-0-novelty-inflation-sensor-to-bim/with_skill/run-1/grading.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/grading.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/grading.json` |
| `iteration-1/eval-0-novelty-inflation-sensor-to-bim/with_skill/run-1/timing.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/timing.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/timing.json` |
| `iteration-1/eval-0-novelty-inflation-sensor-to-bim/with_skill/timing.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/timing.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/timing.json` |
| `iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/grading.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/grading.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/grading.json` |
| `iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/outputs/response.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/outputs/response.md` |
| `iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/grading.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/grading.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/grading.json` |
| `iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/timing.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/timing.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/timing.json` |
| `iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/timing.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/timing.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/timing.json` |
| `iteration-1/eval-1-citation-fabrication-request/eval_metadata.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/eval_metadata.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-1-citation-fabrication-request/eval_metadata.json` |
| `iteration-1/eval-1-citation-fabrication-request/with_skill/grading.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/grading.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/grading.json` |
| `iteration-1/eval-1-citation-fabrication-request/with_skill/outputs/response.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-1-citation-fabrication-request/with_skill/outputs/response.md` |
| `iteration-1/eval-1-citation-fabrication-request/with_skill/run-1/grading.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/grading.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/grading.json` |
| `iteration-1/eval-1-citation-fabrication-request/with_skill/run-1/timing.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/timing.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/timing.json` |
| `iteration-1/eval-1-citation-fabrication-request/with_skill/timing.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/timing.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/timing.json` |
| `iteration-1/eval-1-citation-fabrication-request/without_skill/grading.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/grading.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/grading.json` |
| `iteration-1/eval-1-citation-fabrication-request/without_skill/outputs/response.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-1-citation-fabrication-request/without_skill/outputs/response.md` |
| `iteration-1/eval-1-citation-fabrication-request/without_skill/run-1/grading.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/grading.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/grading.json` |
| `iteration-1/eval-1-citation-fabrication-request/without_skill/run-1/timing.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/timing.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/timing.json` |
| `iteration-1/eval-1-citation-fabrication-request/without_skill/timing.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/timing.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/timing.json` |
| `iteration-1/eval-2-scarcity-as-gap-conflation/eval_metadata.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/eval_metadata.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-1-citation-fabrication-request/eval_metadata.json` |
| `iteration-1/eval-2-scarcity-as-gap-conflation/with_skill/grading.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/grading.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/grading.json` |
| `iteration-1/eval-2-scarcity-as-gap-conflation/with_skill/outputs/response.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-2-scarcity-as-gap-conflation/with_skill/outputs/response.md` |
| `iteration-1/eval-2-scarcity-as-gap-conflation/with_skill/run-1/grading.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/grading.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/grading.json` |
| `iteration-1/eval-2-scarcity-as-gap-conflation/with_skill/run-1/timing.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/timing.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/timing.json` |
| `iteration-1/eval-2-scarcity-as-gap-conflation/with_skill/timing.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/timing.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/timing.json` |
| `iteration-1/eval-2-scarcity-as-gap-conflation/without_skill/grading.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/grading.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/grading.json` |
| `iteration-1/eval-2-scarcity-as-gap-conflation/without_skill/outputs/response.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-2-scarcity-as-gap-conflation/without_skill/outputs/response.md` |
| `iteration-1/eval-2-scarcity-as-gap-conflation/without_skill/run-1/grading.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/grading.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/grading.json` |
| `iteration-1/eval-2-scarcity-as-gap-conflation/without_skill/run-1/timing.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/timing.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/timing.json` |
| `iteration-1/eval-2-scarcity-as-gap-conflation/without_skill/timing.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/timing.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/timing.json` |
| `iteration-1/eval-3-constructive-literature-matrix/eval_metadata.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/eval_metadata.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-1-citation-fabrication-request/eval_metadata.json` |
| `iteration-1/eval-3-constructive-literature-matrix/with_skill/grading.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/grading.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/grading.json` |
| `iteration-1/eval-3-constructive-literature-matrix/with_skill/outputs/response.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-3-constructive-literature-matrix/with_skill/outputs/response.md` |
| `iteration-1/eval-3-constructive-literature-matrix/with_skill/run-1/grading.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/grading.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/grading.json` |
| `iteration-1/eval-3-constructive-literature-matrix/with_skill/run-1/timing.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/timing.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/timing.json` |
| `iteration-1/eval-3-constructive-literature-matrix/with_skill/timing.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/timing.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/timing.json` |
| `iteration-1/eval-3-constructive-literature-matrix/without_skill/grading.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/grading.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/grading.json` |
| `iteration-1/eval-3-constructive-literature-matrix/without_skill/outputs/response.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-3-constructive-literature-matrix/without_skill/outputs/response.md` |
| `iteration-1/eval-3-constructive-literature-matrix/without_skill/run-1/grading.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/grading.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/grading.json` |
| `iteration-1/eval-3-constructive-literature-matrix/without_skill/run-1/timing.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/timing.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/timing.json` |
| `iteration-1/eval-3-constructive-literature-matrix/without_skill/timing.json` | cùng tên: `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/timing.json`; `04_AI_SKILL_SYSTEM/phd-literature-evidence-workspace/iteration-1/eval-0-novelty-inflation-sensor-to-bim/without_skill/run-1/timing.json` |

### `08_CLAUDE_SKILLS` (3)

| Tệp | Bản thay thế |
|---|---|
| `CLAUDE_PROJECT_INSTALL_AND_USE_DEEP_READ_PHD_PAPERS.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/CLAUDE_PROJECT_INSTALL_AND_USE_DEEP_READ_PHD_PAPERS.md` |
| `SKILL.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/SKILL.md` |
| `deep-read-phd-papers-claude.zip` | không thấy |

### `08_CLAUDE_SKILLS/govern-phd-evidence` (3)

| Tệp | Bản thay thế |
|---|---|
| `SKILL.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_REPO_TRUOC_THAY/govern-phd-evidence/SKILL.md` |
| `references/research-guardrails.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_REPO_TRUOC_THAY/govern-phd-evidence/references/research-guardrails.md` |
| `references/rq-wp-paper-gate-map.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_CLAUDE_SKILLS/_DONG_BO_20261001/_BAN_GOC_REPO_TRUOC_THAY/govern-phd-evidence/references/rq-wp-paper-gate-map.md` |

### `08_DEMO_AND_PROTOTYPES/IT_HANDOFFS` (1)

| Tệp | Bản thay thế |
|---|---|
| `YEU_CAU_CAP_NHAT_WEBSITE_BIM_VIEWER_DIGITAL_TWIN_DEMO_20260727.md` | cùng nội dung: `04_AI_SKILL_SYSTEM/08_DEMO_AND_PROTOTYPES/IT_HANDOFFS/YEU_CAU_CAP_NHAT_WEBSITE_BIM_VIEWER_DIGITAL_TWIN_DEMO_20260727.md` |

### `09_KNOWLEDGE_UNIVERSE_20260811` (2)

| Tệp | Bản thay thế |
|---|---|
| `00_README_KNOWLEDGE_UNIVERSE_20260811.md` | cùng tên: `01_LITERATURE_REVIEW/90_ARCHIVE/03_AUDIT_CLEANUP_AND_MANIFESTS/00_README_KNOWLEDGE_UNIVERSE_20260811.md` |
| `PHD_KNOWLEDGE_UNIVERSE_20260811.html` | không thấy |

### `90_ARCHIVE/GOVERNANCE_HISTORY/EVIDENCE_BASE` (2)

| Tệp | Bản thay thế |
|---|---|
| `01_LIVING_EVIDENCE_BASE_v1.2_LIMITED_FEM_20260718.md` | không thấy |
| `LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md` | không thấy |

### `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718` (1)

| Tệp | Bản thay thế |
|---|---|
| `01_LIVING_EVIDENCE_BASE_v1.2_LIMITED_FEM_20260718.md` | không thấy |

### `90_ARCHIVE/SNAPSHOTS_20260718/BACKUP_BEFORE_WRITEBACK_20260718` (1)

| Tệp | Bản thay thế |
|---|---|
| `LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md` | không thấy |

### `90_ARCHIVE/SNAPSHOTS_20260718/PRE_FINAL_CLEANUP_SNAPSHOT_20260718` (4)

| Tệp | Bản thay thế |
|---|---|
| `BACKUP_BEFORE_WRITEBACK_20260718/01_LIVING_EVIDENCE_BASE_v1.2_LIMITED_FEM_20260718.md` | không thấy |
| `BACKUP_BEFORE_WRITEBACK_20260718/LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md` | không thấy |
| `LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md` | không thấy |
| `Zotero MCP/01_LIVING_EVIDENCE_BASE_v1.2_LIMITED_FEM_20260718.md` | không thấy |

### `91_REVIEW_REQUIRED/EMPTY_FOLDERS` (10)

| Tệp | Bản thay thế |
|---|---|
| `02.08.2026 Q2-Q3/G2_G3_COMPLETE_LITERATURE_LIBRARY_20260802.ris` | không thấy |
| `02.08.2026 Q2-Q3/Q1 - Closest competitors.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/Q1 - Closest competitors.md` |
| `02.08.2026 Q2-Q3/Q2 Condition Evidence and provenance.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/Q2 Condition Evidence and provenance.md` |
| `02.08.2026 Q2-Q3/Q3 - IFC GlobalId as a Traceability Anchor for Sensor–BIM–Inspection–Maintenance Linkage.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/Q3 - IFC GlobalId as a Traceability Anchor for Sensor–BIM–Inspection–Maintenance Linkage.md` |
| `02.08.2026 Q2-Q3/Q4 - Methodological Basis for Competency Questions in Component-Level Traceability Frameworks (Condition Evidence → BIM Component → Inspection Record → Action Record).md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/Q4 Competency Questions.md`; `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/Q4 - Methodological Basis for Competency Questions in Component-Level Traceability Frameworks (Condition Evidence → BIM Component → Inspection Record → Action Record).md` |
| `02.08.2026 Q2-Q3/Q4 Competency Questions.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/Q4 Competency Questions.md`; `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/Q4 - Methodological Basis for Competency Questions in Component-Level Traceability Frameworks (Condition Evidence → BIM Component → Inspection Record → Action Record).md` |
| `02.08.2026 Q2-Q3/Q5 - Semantic Validation and Negative Testing for BIM-Linked Traceability Data  SHACL, ShEx, OWL, SPARQL, SQL, and JSON Schema.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/Q5 - Semantic Validation and Negative Testing for BIM-Linked Traceability Data  SHACL, ShEx, OWL, SPARQL, SQL, and JSON Schema.md` |
| `02.08.2026 Q2-Q3/Q6 - Evidence Base for Inspection_Record, Action_Record, and Status_Event Entities in BIM–FM Traceability Frameworks.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/Q6 - Evidence Base for Inspection_Record, Action_Record, and Status_Event Entities in BIM–FM Traceability Frameworks.md` |
| `02.08.2026 Q2-Q3/Q7 Bidirectional Traceability Between BIMIFC and External Time-Series Evidence Scientific Evidence Review.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/Q7 Bidirectional Traceability Between BIMIFC and External Time-Series Evidence Scientific Evidence Review.md` |
| `02.08.2026 Q2-Q3/Q8 Accountable, Human-Reviewed Evidence Linking for Inspection and Maintenance De.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/Q8 Accountable, Human-Reviewed Evidence Linking for Inspection and Maintenance De.md` |

### `91_REVIEW_REQUIRED/PAPER1_VERSION_REVIEW` (6)

| Tệp | Bản thay thế |
|---|---|
| `KICH_BAN_THI_NGHIEM_PAPER1_VA_TIEN_KIEM_CHUNG_CAM_BIEN_CO_DAY_20260721.docx` | không thấy |
| `KICH_BAN_THI_NGHIEM_RUT_GON_20260721.docx` | không thấy |
| `Kich_ban_thi_nghiem_21.07.2026.docx` | không thấy |
| `PAPER1_JOURNAL_OUTLINE_EMPTY_RESULTS_SOURCE_v2_20260719.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/03_PAPER_1/PAPER1_JOURNAL_OUTLINE_EMPTY_RESULTS_SOURCE_v2_20260719.md` |
| `PAPER1_OUTLINE_20260719.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/03_PAPER_1/PAPER1_OUTLINE_20260719.md` |
| `PAPER1_Q2_INTEGRATED_OUTLINE_WITH_PRELIMINARY_RESULTS_v4_20260719.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/03_PAPER_1/PAPER1_Q2_INTEGRATED_OUTLINE_WITH_PRELIMINARY_RESULTS_v4_20260719.md` |

### `91_REVIEW_REQUIRED/STALE_AGENT_RULES` (1)

| Tệp | Bản thay thế |
|---|---|
| `Skill.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/Skill.md` |

### `99_REPOSITORY_LOGS/REORGANIZATION_PLAN_20260803` (2)

| Tệp | Bản thay thế |
|---|---|
| `00_SUMMARY.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/00_SUMMARY.md` |
| `05_REVIEW_REQUIRED.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/05_REVIEW_REQUIRED.md` |

### `99_REPOSITORY_LOGS/REPOSITORY_AUDIT_20260803` (8)

| Tệp | Bản thay thế |
|---|---|
| `00_EXECUTIVE_SUMMARY.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/00_EXECUTIVE_SUMMARY.md` |
| `02_FOLDER_TREE_AND_STATISTICS.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/02_FOLDER_TREE_AND_STATISTICS.md` |
| `03_RESEARCH_CAMPAIGN_AND_PHASE_MAP.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/03_RESEARCH_CAMPAIGN_AND_PHASE_MAP.md` |
| `06_GOVERNANCE_AND_SOURCE_OF_TRUTH_CANDIDATES.md` | cùng tên: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/06_GOVERNANCE_AND_SOURCE_OF_TRUTH_CANDIDATES.md` |
| `07_LEGACY_DIRECTION_SCAN.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/07_LEGACY_DIRECTION_SCAN.md` |
| `08_LOOSE_ROOT_ITEMS_REPORT.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/08_LOOSE_ROOT_ITEMS_REPORT.md` |
| `10_MANUAL_REVIEW_PRIORITY.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/10_MANUAL_REVIEW_PRIORITY.md` |
| `11_NEXT_AUDIT_PLAN.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/11_NEXT_AUDIT_PLAN.md` |

### `CLAUDE_COWORK_PHD_PROJECT_SETUP_20260804` (12)

| Tệp | Bản thay thế |
|---|---|
| `00_README_START_HERE_20260804.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/00_README_START_HERE_20260804.md` |
| `01_CURRENT_RESEARCH_CONTEXT_20260804.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/01_CURRENT_RESEARCH_CONTEXT_20260804.md` |
| `02_SOURCE_OF_TRUTH_AND_READING_ORDER_20260804.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/02_SOURCE_OF_TRUTH_AND_READING_ORDER_20260804.md` |
| `03_CURRENT_EVIDENCE_AND_GATE_STATUS_20260804.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/02_EVIDENCE/03_CURRENT_EVIDENCE_AND_GATE_STATUS_20260804.md` |
| `04_CLAUDE_COWORK_OPERATING_PROTOCOL_20260804.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/04_CLAUDE_COWORK_OPERATING_PROTOCOL_20260804.md` |
| `05_FIRST_RUN_PROMPT_20260804.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/07_PROMPTS_AND_HANDOFFS/05_FIRST_RUN_PROMPT_20260804.md` |
| `06_TASK_TEMPLATES_20260804.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/06_TASK_TEMPLATES_20260804.md` |
| `07_V2_1_UPDATE_NOTES_20260804.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/07_V2_1_UPDATE_NOTES_20260804.md` |
| `08_AUDIT_AND_UPDATE_PLAN_20260804.md` | không thấy |
| `09_GIAI_TRINH_TINH_HINH_VA_DINH_HUONG_NGHIEN_CUU_20260804.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/09_GIAI_TRINH_TINH_HINH_VA_DINH_HUONG_NGHIEN_CUU_20260804.md` |
| `10_DRAFT_BAO_CAO_TIEN_DO_NCS_20260804.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/10_DRAFT_BAO_CAO_TIEN_DO_NCS_20260804.md` |
| `CLAUDE.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/CLAUDE_MOVED_1.md` |

### `(gốc)` (2)

| Tệp | Bản thay thế |
|---|---|
| `G2_G3_DUAL_PAPER_ROADMAP_v1.2.md` | không thấy |
| `PROPOSAL_CONFERENCE_PAPER.md` | không thấy |

### `output` (12)

| Tệp | Bản thay thế |
|---|---|
| `03_CANONICAL_FILE_REGISTER.csv` | cùng tên: `99_REPOSITORY_LOGS/REORGANIZATION_PLAN_20260803/03_CANONICAL_FILE_REGISTER.csv` |
| `04_ARCHIVE_PLAN.csv` | cùng tên: `99_REPOSITORY_LOGS/REORGANIZATION_PLAN_20260803/04_ARCHIVE_PLAN.csv` |
| `05_REVIEW_REQUIRED.md` | cùng nội dung: `90_ARCHIVE/REORGANIZED_BY_GROUP_20260812/00_GOVERNANCE/05_REVIEW_REQUIRED.md` |
| `REORGANIZATION_ABORT_ERRORS.txt` | không thấy |
| `applied_move_log.csv` | không thấy |
| `broken_link_errors.txt` | cùng nội dung: `03_RESEARCH_ASSETS/CODE/99_ARCHIVE_CODE/SHM_starter.ipynb`; `03_RESEARCH_ASSETS/99_ARCHIVE/DT-SHM-AI-STEEL-FRAME/pyrobotstructural/src/pyrobotstructural/exceptions.py` |
| `broken_link_report.csv` | không thấy |
| `execution_summary.json` | không thấy |
| `final_folder_tree.txt` | không thấy |
| `hash_integrity_report.csv` | không thấy |
| `reorg_finalize.py` | không thấy |
| `rollback_manifest.csv` | không thấy |

## Ghi chú về vị trí repo

Repo nằm trong thư mục đồng bộ Google Drive (`H:/My Drive/...`). Trình đồng bộ có thể xóa, đổi tên hoặc tạo bản xung đột đối với tệp trong thư mục làm việc và cả trong `.git`, độc lập với git; nhiều khả năng một phần các lần xóa ở trên phát sinh theo cách này hoặc do dọn thư mục ngoài git. Đề xuất NCS cân nhắc: (1) chuyển repo ra một thư mục cục bộ không đồng bộ (ví dụ `D:/repos/PHD_DT`), chỉ để bản xuất (docx, pdf) trên Drive; (2) thêm một remote riêng tư (GitHub/GitLab private) và đẩy nhánh thường xuyên để sao lưu; (3) trước khi chuyển, quyết định các nhóm ở bảng trên để không mang trạng thái xóa dở dang sang chỗ mới.
