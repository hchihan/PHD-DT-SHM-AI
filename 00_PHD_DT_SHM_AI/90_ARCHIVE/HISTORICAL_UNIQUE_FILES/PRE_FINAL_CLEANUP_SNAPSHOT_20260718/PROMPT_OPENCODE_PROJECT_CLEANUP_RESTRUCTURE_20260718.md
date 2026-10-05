# PROMPT CHO OPENCODE
## Dọn dẹp và tái cấu trúc Project PhD Limited-FEM
### Giữ file hiện hành ngày 18.07.2026 và các file hệ thống có giá trị lâu dài

**Thư mục gốc cần xử lý:**

```text
03_RESEARCH/
└── 01_PHD_DT_AI_AM/
    └── 00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/
```

**Ngày kiểm soát:** 2026-07-18  
**Chế độ:** mạnh dạn dọn dẹp nhưng không phá hủy dữ liệu nghiên cứu  
**Ngôn ngữ báo cáo:** tiếng Việt

---

# 1. MỤC TIÊU

Dọn thư mục gốc hiện đang lẫn file quản trị hệ thống, file hiện hành, file đầu ra tạm, file đã bị thay thế, backup, literature, Paper 1, chuyên đề và file từ Fable/Perplexity/OpenCode.

Sau khi hoàn thành, thư mục gốc phải:

1. Chỉ còn các file hệ thống quan trọng và các thư mục điều hướng chính.
2. Giữ lại bản mới nhất ngày `2026-07-18`.
3. Giữ các file nền tảng lâu dài dù được tạo ngày `2026-07-17`.
4. Chuyển file cũ, superseded và legacy vào archive có cấu trúc.
5. Chỉ xóa vĩnh viễn file trùng hoàn toàn sau khi kiểm tra checksum.
6. Không xóa raw data, code, Zotero library, backup quan trọng hoặc evidence chưa đánh giá.
7. Tạo Master Index mới để người dùng tìm được mọi tài liệu hiện hành.

---

# 2. SOURCE OF TRUTH VÀ FILE HỆ THỐNG PHẢI GIỮ

Các file sau có giá trị lâu dài, phải giữ ở khu vực quản trị hiện hành dù ngày tạo là 17.07.2026:

```text
00_README_START_HERE.md
CLAUDE.md
MASTER_RESEARCH_CHARTER.md
MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md
RESEARCH_DIRECTION_AND_SCOPE.md
RESEARCH_ARCHITECTURE.md
CURRENT_STATUS_AND_NEXT_DIRECTION.md
RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md
THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md
```

Giữ thêm nếu vẫn là bản hiện hành:

```text
LIVING_EVIDENCE_BASE mới nhất
MASTER_INDEX_CURRENT mới nhất
TERMINOLOGY_CONTROL mới nhất
UNRESOLVED_ITEMS tracker mới nhất
Evidence Gate matrix mới nhất
```

Nếu có nhiều phiên bản:

```text
CURRENT_APPROVED
> CURRENT_CANDIDATE mới nhất
> bản có ngày mới nhất
> bản cũ
```

Không tự thay đổi nội dung Charter hoặc ADR trong nhiệm vụ dọn file.

---

# 3. NGUYÊN TẮC GIỮ FILE NGÀY 18.07.2026

Ưu tiên giữ các file được tạo hoặc cập nhật ngày `2026-07-18` nếu chúng là:

- đầu ra mới nhất;
- evidence đã kiểm chứng;
- manuscript hiện hành;
- readiness report;
- claim/reference audit;
- outline chuyên đề;
- ma trận RQ/WP/Paper/Gate;
- Zotero deep-read outputs;
- backup report;
- OpenCode/Fable handoff có giá trị vận hành.

Tuy nhiên, ngày mới không tự động có nghĩa là file hiện hành.

Phải đọc header/status/version để phân loại:

- `CURRENT_APPROVED`
- `CURRENT_CANDIDATE`
- `TRANSITIONAL`
- `HISTORICAL`
- `SUPERSEDED`
- `DRAFT`
- `BACKUP`
- `TEMPORARY`

Nếu file mới chỉ là bản transitional nhưng có file consolidated/current mới hơn, đưa transitional vào archive.

---

# 4. CẤU TRÚC THƯ MỤC ĐÍCH

Tái cấu trúc thành:

```text
00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/
│
├── 00_GOVERNANCE/
├── 01_CURRENT_CONTROL/
├── 02_EVIDENCE_BASE/
│   ├── CURRENT/
│   ├── RQ1_GATE1/
│   ├── RQ2_GATES2_3/
│   ├── RQ3_GATE4/
│   ├── WP4_GATE5/
│   └── ZOTERO_AUDIT/
├── 03_PAPERS/
│   ├── PAPER_1/
│   ├── PAPER_2/
│   ├── PAPER_3/
│   └── PAPER_4_OPTIONAL/
├── 04_PHD_SPECIAL_TOPICS/
│   ├── CHUYEN_DE_TONG_QUAN/
│   ├── CHUYEN_DE_1/
│   └── CHUYEN_DE_2/
├── 05_DATA_CODE_AND_EXPERIMENTS/
│   ├── LAB_DATA/
│   ├── FIELD_DATA/
│   ├── CODE/
│   └── RUN_REGISTRY/
├── 06_LITERATURE_AND_ZOTERO/
│   ├── ZOTERO_MCP/
│   ├── PERPLEXITY_PRO/
│   └── REFERENCE_EXPORTS/
├── 07_PROMPTS_AND_HANDOFFS/
│   ├── OPENCODE/
│   ├── FABLE/
│   └── GPT_PROJECT_CHATS/
├── 90_BACKUP/
├── 92_ARCHIVE_SUPERSEDED_FILES/
│   ├── GOVERNANCE_OLD/
│   ├── EVIDENCE_OLD/
│   ├── PAPER_OLD/
│   ├── SPECIAL_TOPIC_OLD/
│   ├── LEGACY_PACKS/
│   └── DUPLICATES_PENDING_DELETE/
└── 99_TEMP_REVIEW/
```

Không bắt buộc tạo thư mục trống nếu chưa có nội dung.

---

# 5. PHÂN LOẠI CỤ THỂ CÁC FILE/THƯ MỤC ĐANG THẤY

## 5.1. Chuyên đề Tổng quan

Các file:

```text
CHUYEN_DE_TONG_QUAN_EVIDENCE_GAPS_v1.md
EVIDENCE_MATRIX_CHUYEN_DE_TONG_QUAN_v1.csv
MATRIX_CHUYEN_DE_RQ_WP_PAPER_GATE_v1.md
OUTLINE_CHUYEN_DE_TONG_QUAN_CHI_TIET_v1.md
```

Di chuyển vào:

```text
04_PHD_SPECIAL_TOPICS/CHUYEN_DE_TONG_QUAN/
```

Nếu có file đề xuất DOCX tương ứng, đặt cùng thư mục.

## 5.2. Phase 0 report

```text
PHASE0_SAFETY_BACKUP_AND_DRY_RUN_REPORT_20260718.md
```

Di chuyển vào:

```text
02_EVIDENCE_BASE/ZOTERO_AUDIT/
```

## 5.3. Paper 1

Thư mục hiện tại:

```text
Paper 1/
```

Đổi tên và di chuyển thành:

```text
03_PAPERS/PAPER_1/
```

Bên trong chia:

```text
CURRENT_MANUSCRIPT/
GATE1_EVIDENCE/
IT_REQUESTS/
REFERENCE_AUDIT/
REVISION_HISTORY/
ARCHIVE/
```

Bản manuscript mới nhất, readiness report, claim audit, reference audit và IT task register nằm ở khu vực hiện hành.

Bản nháp cũ như `Paper 1 (10.06).docx` chuyển vào:

```text
03_PAPERS/PAPER_1/ARCHIVE/
```

Không xóa.

## 5.4. Zotero MCP

Thư mục:

```text
Zotero MCP/
```

Di chuyển thành:

```text
06_LITERATURE_AND_ZOTERO/ZOTERO_MCP/
```

Các evidence addendum và Living Evidence Base phân loại vào `02_EVIDENCE_BASE/`. Chỉ giữ một bản canonical; nơi khác dùng index/shortcut thay vì tạo thêm bản sao.

## 5.5. Perplexity

Thư mục:

```text
Perplexity_Pro/
```

Di chuyển vào:

```text
06_LITERATURE_AND_ZOTERO/PERPLEXITY_PRO/
```

Đánh dấu:

```text
DISCOVERY_SOURCE_ONLY
NOT_CITABLE_EVIDENCE
```

Không xóa vì còn giá trị truy tìm nguồn.

## 5.6. Backup

```text
BACKUP_BEFORE_WRITEBACK_20260718/
```

Di chuyển vào:

```text
90_BACKUP/BACKUP_BEFORE_WRITEBACK_20260718/
```

Không chỉnh sửa nội dung backup.

## 5.7. Legacy pack

```text
07_FABLE_LEGACY_PACK_20260718/
```

Di chuyển vào:

```text
92_ARCHIVE_SUPERSEDED_FILES/LEGACY_PACKS/
```

Trừ khi có file vẫn là current source of truth.

## 5.8. Living Evidence Base v1.1

Nếu đã có v1.2/v1.3 current:

- chuyển v1.1 vào `92_ARCHIVE_SUPERSEDED_FILES/EVIDENCE_OLD/`;
- ghi rõ canonical replacement.

Nếu chưa có bản consolidated current:

- giữ v1.1 trong `02_EVIDENCE_BASE/CURRENT/`;
- ghi `CURRENT_BASE_WITH_PENDING_UPDATE`.

## 5.9. Unresolved items cũ

Nếu có tracker mới hơn ngày 18.07.2026:

- archive bản cũ;
- đặt bản mới thành `UNRESOLVED_ITEMS_CURRENT.md`.

Nếu chưa có tracker mới:

- giữ file hiện tại trong `01_CURRENT_CONTROL/`.

---

# 6. QUY TẮC XỬ LÝ FILE

Mỗi file phải được gắn một quyết định:

| Quyết định | Ý nghĩa |
|---|---|
| `KEEP_SYSTEM` | File nền tảng lâu dài |
| `KEEP_CURRENT` | Bản hiện hành mới nhất |
| `MOVE_TO_DOMAIN_FOLDER` | File đúng nhưng đang sai vị trí |
| `ARCHIVE_SUPERSEDED` | Đã có bản mới thay thế |
| `ARCHIVE_LEGACY` | Giữ để tham chiếu lịch sử |
| `DUPLICATE_PENDING_DELETE` | Trùng hoàn toàn, chờ kiểm tra |
| `DELETE_VERIFIED_DUPLICATE` | Chỉ xóa khi checksum giống và canonical an toàn |
| `REVIEW_REQUIRED` | Chưa đủ thông tin |

Không quyết định dựa riêng vào tên hoặc ngày file.

Phải kiểm tra:

- header/version;
- status;
- nội dung;
- checksum;
- file tham chiếu tới nó;
- có phải source of truth không.

---

# 7. QUY TẮC XÓA

Chỉ xóa vĩnh viễn khi đồng thời:

1. Hai file có cùng checksum hoặc nội dung hoàn toàn giống nhau.
2. Một bản canonical đã được giữ ở đúng thư mục.
3. Không có link nào bị phá mà chưa cập nhật.
4. File không phải raw data, code, backup, Zotero database hoặc evidence độc nhất.
5. Đã ghi vào deletion manifest.
6. Đã tạo backup trước cleanup.

Nếu chỉ là bản cũ nhưng không trùng hoàn toàn:

```text
ARCHIVE, KHÔNG DELETE
```

Không xóa:

- raw CSV;
- scripts;
- notebooks;
- checkpoints;
- Zotero attachments;
- PDF nghiên cứu;
- evidence matrix;
- audit log;
- backup;
- source-of-truth files.

---

# 8. CÁC FILE BÁO CÁO PHẢI TẠO

Tạo trong:

```text
01_CURRENT_CONTROL/PROJECT_CLEANUP_20260718/
```

## Inventory

```text
PROJECT_FILE_INVENTORY_BEFORE_CLEANUP_20260718.csv
```

Cột:

```text
Original_Path
Filename
Extension
Size
Modified_Date
Checksum
Detected_Version
Detected_Status
Domain
Decision
Reason
Destination_Path
Link_Update_Required
```

## Migration manifest

```text
PROJECT_FILE_MIGRATION_MANIFEST_20260718.csv
```

## Deletion manifest

```text
VERIFIED_DUPLICATE_DELETION_MANIFEST_20260718.csv
```

## Cleanup report

```text
PROJECT_CLEANUP_REPORT_20260718.md
```

## New Master Index

```text
MASTER_INDEX_CURRENT.md
```

## Root README

Cập nhật hoặc tạo:

```text
00_README_START_HERE.md
```

---

# 9. QUY TRÌNH THỰC HIỆN

## PHASE A — Dry run

1. Inventory toàn bộ thư mục.
2. Không di chuyển/xóa.
3. Tạo classification table và proposed manifest.
4. Báo cáo xung đột.
5. Xác định source-of-truth candidates.

## PHASE B — Backup

Tạo:

```text
90_BACKUP/PRE_CLEANUP_SNAPSHOT_20260718/
```

và lưu manifest/checksum.

## PHASE C — Move and organize

1. Tạo cấu trúc đích.
2. Di chuyển theo manifest.
3. Cập nhật links/index.
4. Không xóa trong bước này.

## PHASE D — Archive

Chuyển superseded, legacy, historical vào archive và ghi canonical replacement.

## PHASE E — Verified duplicate deletion

Chỉ xử lý duplicate checksum-identical đã ghi manifest. Nếu nghi ngờ, chuyển vào `DUPLICATES_PENDING_DELETE`.

## PHASE F — Validation

Kiểm tra:

- source-of-truth files tồn tại;
- links hoạt động;
- root sạch;
- Paper 1 current files đầy đủ;
- evidence base không mất;
- backup còn nguyên;
- không có raw data bị di chuyển sai;
- không có file unique bị xóa.

---

# 10. ROOT FOLDER SAU DỌN DẸP

Root chỉ nên còn:

```text
00_GOVERNANCE/
01_CURRENT_CONTROL/
02_EVIDENCE_BASE/
03_PAPERS/
04_PHD_SPECIAL_TOPICS/
05_DATA_CODE_AND_EXPERIMENTS/
06_LITERATURE_AND_ZOTERO/
07_PROMPTS_AND_HANDOFFS/
90_BACKUP/
92_ARCHIVE_SUPERSEDED_FILES/
99_TEMP_REVIEW/
00_README_START_HERE.md
```

---

# 11. STOP RULES

Dừng và báo cáo nếu:

- không xác định được current version;
- hai source-of-truth files mâu thuẫn;
- file được tham chiếu nhưng không tồn tại;
- archive chứa file có vẻ current;
- có nguy cơ xóa raw data/evidence unique;
- Google Drive có conflict copy;
- file đang mở hoặc chưa đồng bộ;
- thao tác có thể phá Zotero attachment links.

Không tự giải quyết mâu thuẫn nội dung nghiên cứu trong nhiệm vụ cleanup.

---

# 12. BÁO CÁO CUỐI

Báo cáo:

1. Số file inventory.
2. Số file giữ system/current.
3. Số file di chuyển.
4. Số file archive.
5. Số duplicate đã xóa.
6. Số file cần review.
7. Root folder sau cleanup.
8. Current source-of-truth list.
9. Current Paper 1 list.
10. Rủi ro còn lại.

Phải nêu rõ:

- không có raw data bị xóa;
- không có source-of-truth file bị mất;
- file cũ được archive ở đâu;
- Master Index mới nằm ở đâu.

---

# 13. YÊU CẦU THỰC THI

Thực hiện theo hai bước:

```text
BƯỚC 1: DRY RUN + INVENTORY + PROPOSED MANIFEST
BƯỚC 2: EXECUTE CLEANUP SAU KHI MANIFEST ĐƯỢC KIỂM TRA
```

Không hỏi người dùng về từng file nhỏ. Chỉ dừng để hỏi khi có:

- source-of-truth conflict;
- nguy cơ mất dữ liệu;
- hai phiên bản current mâu thuẫn;
- file unique nhưng không xác định được vai trò.
