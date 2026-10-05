# PROMPT THỰC THI CHO OPENCODE
## DỌN DẸP TOÀN BỘ PROJECT — GIỮ CURRENT, XÓA SUPERSEDED, ROOT GỌN

**Thư mục dự án:**

```text
03_RESEARCH/
└── 01_PHD_DT_AI_AM/
    └── 00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/
```

**Ngày thực thi:** 2026-07-18  
**Chế độ:** EXECUTE CLEANUP — mạnh dạn xóa file đã bị thay thế  
**Ngôn ngữ báo cáo:** Tiếng Việt

---

# 1. MỆNH LỆNH CHÍNH

Sử dụng trực tiếp các file dry run đã tạo:

```text
01_CURRENT_CONTROL/PROJECT_CLEANUP_20260718/
├── PROJECT_FILE_INVENTORY_BEFORE_CLEANUP_20260718.csv
├── PROJECT_FILE_MIGRATION_MANIFEST_20260718.csv
├── VERIFIED_DUPLICATE_DELETION_MANIFEST_20260718.csv
├── PROJECT_CLEANUP_REPORT_20260718.md
└── MASTER_INDEX_CURRENT.md
```

Thực hiện ngay Phase 2, không lặp lại dry run nếu không gặp STOP RULE:

1. Tạo snapshot backup cuối trước cleanup.
2. Tạo cấu trúc thư mục mới.
3. Di chuyển file hiện hành về đúng domain.
4. Giữ duy nhất một bản canonical/current cho mỗi nội dung.
5. Xóa mạnh tay các file đã bị thay thế, bản trùng, copy, transitional, candidate cũ, file tạm và output trung gian.
6. Cập nhật mọi link, README và Master Index.
7. Làm sạch root folder.
8. Không giữ archive dư thừa chỉ vì “có thể cần”.

---

# 2. NGUYÊN TẮC GIỮ DUY NHẤT MỘT BẢN

Cho mỗi nhóm nội dung, chỉ giữ:

```text
CURRENT_APPROVED
> CURRENT_CANDIDATE mới nhất nếu chưa có approved
> version mới nhất có audit
```

Xóa các bản thấp hơn nếu:

- nội dung đã được hợp nhất đầy đủ vào bản mới;
- không còn claim/evidence độc nhất;
- đã được ghi `SUPERSEDED`, `HISTORICAL`, `TRANSITIONAL`, `LEGACY` hoặc `REPLACED BY`;
- canonical replacement tồn tại, mở được và đã được index;
- các link tham chiếu đã cập nhật.

Không tạo nhiều bản sao cùng một file ở nhiều thư mục. Một file canonical ở một vị trí; các nơi khác chỉ dùng index/link.

---

# 3. FILE HỆ THỐNG PHẢI GIỮ

Giữ lâu dài:

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

Giữ bản mới nhất của:

```text
MASTER_INDEX_CURRENT.md
LIVING_EVIDENCE_BASE_CURRENT.md hoặc version current mới nhất
TERMINOLOGY_CONTROL_CURRENT.md
UNRESOLVED_ITEMS_CURRENT.md
EVIDENCE_GATES_CURRENT.md
```

Không sửa nội dung học thuật của Charter/ADR trong nhiệm vụ cleanup.

---

# 4. CẤU TRÚC ĐÍCH BẮT BUỘC

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
├── 06_LITERATURE_AND_ZOTERO/
│   ├── ZOTERO_MCP/
│   ├── PERPLEXITY_PRO/
│   └── REFERENCE_EXPORTS/
├── 07_PROMPTS_AND_HANDOFFS/
├── 90_BACKUP/
└── 92_ARCHIVE_MINIMAL/
```

`92_ARCHIVE_MINIMAL` chỉ giữ các tài liệu lịch sử thật sự cần thiết, không dùng làm nơi chứa mọi bản cũ.

Root sau cleanup chỉ còn các thư mục trên và `00_README_START_HERE.md`.

---

# 5. QUYẾT ĐỊNH CỤ THỂ THEO NHÓM

## 5.1. Chuyên đề Tổng quan

Di chuyển vào:

```text
04_PHD_SPECIAL_TOPICS/CHUYEN_DE_TONG_QUAN/
```

Giữ các bản mới nhất ngày 18.07.2026:

```text
CHUYEN_DE_TONG_QUAN_EVIDENCE_GAPS_v1.md
EVIDENCE_MATRIX_CHUYEN_DE_TONG_QUAN_v1.csv
MATRIX_CHUYEN_DE_RQ_WP_PAPER_GATE_v1.md
OUTLINE_CHUYEN_DE_TONG_QUAN_CHI_TIET_v1.md
```

Xóa các bản cũ hơn đã bị thay thế nếu không có nội dung độc nhất.

## 5.2. Paper 1

Đổi:

```text
Paper 1/
```

thành:

```text
03_PAPERS/PAPER_1/
```

Tổ chức:

```text
CURRENT_MANUSCRIPT/
GATE1_EVIDENCE/
IT_REQUESTS/
REFERENCE_AUDIT/
REVISION_HISTORY/
ARCHIVE_MINIMAL/
```

Giữ current:

- manuscript mới nhất;
- manuscript source mới nhất;
- readiness report mới nhất;
- claim-evidence audit mới nhất;
- reference audit mới nhất;
- IT task register mới nhất;
- revision log mới nhất.

Xóa:

- bản bị superseded hoàn toàn;
- bản copy trùng nội dung;
- candidate cũ đã có version mới;
- intermediate drafts không còn claim/evidence độc nhất;
- file export tạm.

Chỉ giữ `Paper 1 (10.06).docx` trong `ARCHIVE_MINIMAL` nếu cần audit lịch sử. Nếu revision log và snapshot đã ghi đủ, có thể xóa.

## 5.3. Zotero và Evidence

Di chuyển:

```text
Zotero MCP/
→ 06_LITERATURE_AND_ZOTERO/ZOTERO_MCP/
```

Giữ:

- deep-read completion report;
- normalized evidence matrix mới nhất;
- metadata/duplicate correction log mới nhất;
- writeback queue nếu chưa hoàn tất;
- Phase 0 report;
- evidence addenda current;
- Living Evidence Base current.

Xóa:

- evidence matrix cũ đã được normalized/consolidated đầy đủ;
- addendum version cũ đã được thay thế;
- duplicate exports;
- temporary citation exports;
- transitional Living Evidence Base nếu đã có consolidated current.

## 5.4. Living Evidence Base

Nếu có:

```text
LIVING_EVIDENCE_BASE_v1.3_CONSOLIDATED...
```

và đã được kiểm tra:

- giữ v1.3;
- xóa v1.2 transitional;
- xóa v1.1 nếu toàn bộ nội dung đã được hợp nhất và Master Index đã cập nhật.

Nếu chưa có v1.3:

- giữ v1.1 và v1.2;
- đánh dấu một bản current, một bản transitional;
- không xóa.

## 5.5. Perplexity

Di chuyển:

```text
Perplexity_Pro/
→ 06_LITERATURE_AND_ZOTERO/PERPLEXITY_PRO/
```

Giữ chỉ các report discovery mới nhất có giá trị truy tìm nguồn.

Xóa:

- bản lặp;
- export thô đã được chuyển thành evidence matrix;
- file tạm;
- file trùng nội dung.

Gắn README:

```text
DISCOVERY_SOURCE_ONLY
NOT_CITABLE_EVIDENCE
```

## 5.6. Backup

Di chuyển:

```text
BACKUP_BEFORE_WRITEBACK_20260718/
→ 90_BACKUP/BACKUP_BEFORE_WRITEBACK_20260718/
```

Tạo thêm:

```text
90_BACKUP/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/
```

Sau khi snapshot xác minh hoàn chỉnh, được phép xóa các bản superseded khỏi working tree.

Không xóa backup.

## 5.7. Fable Legacy Pack

Đánh giá từng file trong:

```text
07_FABLE_LEGACY_PACK_20260718/
```

- file còn current → chuyển về đúng domain;
- file chỉ là legacy/snapshot → xóa nếu đã có backup;
- file có nội dung độc nhất → giữ trong `92_ARCHIVE_MINIMAL/LEGACY_PACKS/`.

Không giữ nguyên cả folder chỉ vì lịch sử.

## 5.8. Cleanup artifacts

Giữ trong:

```text
01_CURRENT_CONTROL/PROJECT_CLEANUP_20260718/
```

- inventory before cleanup;
- migration manifest final;
- cleanup report final;
- deletion manifest final.

Xóa sau cleanup:

```text
_generate_dry_run_inventory.py
MASTER_INDEX_CURRENT.md bản CURRENT_CANDIDATE_BLOCKED
các script/log tạm chỉ phục vụ dry run
```

Sau khi có `MASTER_INDEX_CURRENT.md` trạng thái `CURRENT`, xóa bản blocked/candidate cũ.

---

# 6. QUY TẮC XÓA MẠNH

## A. Trùng hoàn toàn

Xóa nếu:

- checksum giống;
- cùng nội dung;
- canonical tồn tại.

## B. Đã bị thay thế

Xóa nếu header/index ghi:

```text
SUPERSEDED
HISTORICAL
TRANSITIONAL
LEGACY
REPLACED BY
```

và bản thay thế đã mở/đọc được.

## C. Version thấp không còn nội dung độc nhất

Ví dụ:

```text
v1 → v2 → v3
```

Nếu v3 đã hợp nhất đầy đủ và có revision log:

- xóa v1, v2;
- không archive tất cả.

## D. File tạm

Xóa:

- temp;
- cache;
- autosave;
- conflict copy;
- duplicate export;
- intermediate render;
- dry-run script/log.

## E. Output AI cũ đã được hợp nhất

Các output Fable/OpenCode/Perplexity cũ có thể xóa nếu:

- nội dung đã được hợp nhất vào file current;
- không còn evidence/citation độc nhất;
- có backup snapshot.

---

# 7. FILE KHÔNG ĐƯỢC XÓA

Không xóa:

- raw data;
- code đang dùng;
- notebooks có kết quả độc nhất;
- model checkpoints chưa xác minh;
- Zotero database/attachments;
- PDF nghiên cứu độc nhất;
- source-of-truth files;
- audit file current;
- current evidence matrix;
- backup;
- file có claim/evidence chưa hợp nhất.

Nếu không chắc:

```text
MOVE TO 92_ARCHIVE_MINIMAL/REVIEW_REQUIRED/
```

nhưng chỉ dùng cho số ít file thật sự mơ hồ.

---

# 8. CẬP NHẬT LINK VÀ INDEX

Sau khi di chuyển/xóa:

1. cập nhật tất cả relative links;
2. cập nhật `00_README_START_HERE.md`;
3. tạo `MASTER_INDEX_CURRENT.md`;
4. cập nhật current paths trong `CURRENT_STATUS_AND_NEXT_DIRECTION.md`, `CLAUDE.md`, Paper 1 readiness report và evidence addenda/index;
5. tìm toàn project để bảo đảm không còn link tới file đã xóa.

Tạo:

```text
BROKEN_LINK_AUDIT_20260718.md
```

Kết quả cuối phải là:

```text
BROKEN INTERNAL LINKS = 0
```

---

# 9. QUY TRÌNH THỰC THI

## Step 1 — Snapshot

Tạo backup snapshot đầy đủ và checksum.

## Step 2 — Validate current files

Xác nhận canonical/current cho từng domain.

## Step 3 — Move

Di chuyển file current vào cấu trúc mới.

## Step 4 — Delete superseded

Xóa file bị thay thế theo quy tắc trên.

## Step 5 — Delete duplicates/temp

Xóa checksum duplicates, copy, temp và dry-run files.

## Step 6 — Update links/index

Cập nhật toàn bộ navigation.

## Step 7 — Validate

Kiểm tra:

- root gọn;
- source-of-truth đầy đủ;
- current Paper 1 đầy đủ;
- evidence base đầy đủ;
- backup tồn tại;
- broken links = 0;
- raw data không mất;
- Zotero không bị sửa trực tiếp.

---

# 10. STOP RULES

Chỉ dừng khi:

1. Có hai file cùng tuyên bố CURRENT nhưng nội dung mâu thuẫn.
2. Không xác định được canonical replacement.
3. File superseded chứa evidence độc nhất chưa hợp nhất.
4. Có nguy cơ phá Zotero attachment path.
5. Google Drive đang có conflict/sync chưa hoàn tất.
6. Raw data hoặc code có nguy cơ bị mất.

Không dừng để hỏi về file copy, temp, version cũ hoặc legacy rõ ràng.

---

# 11. BÁO CÁO CUỐI

Tạo:

```text
01_CURRENT_CONTROL/PROJECT_CLEANUP_20260718/
├── PROJECT_CLEANUP_FINAL_REPORT_20260718.md
├── PROJECT_FILE_MIGRATION_MANIFEST_FINAL_20260718.csv
├── DELETED_SUPERSEDED_FILES_MANIFEST_20260718.csv
├── BROKEN_LINK_AUDIT_20260718.md
└── MASTER_INDEX_CURRENT.md
```

Báo cáo:

| Chỉ tiêu | Kết quả |
|---|---:|
| Tổng file trước cleanup | |
| File current/system giữ lại | |
| File di chuyển | |
| File superseded đã xóa | |
| Duplicate/temp đã xóa | |
| File archive minimal | |
| File review required | |
| Broken links | |
| Raw data bị xóa | 0 |
| Source-of-truth bị mất | 0 |

Phải liệt kê:

1. Source-of-truth hiện hành.
2. Current Evidence Base.
3. Current Paper 1 files.
4. Current Chuyên đề Tổng quan files.
5. Current Zotero/evidence audit files.
6. Backup location.
7. Các file duy nhất còn cần review.

---

# 12. TRẠNG THÁI CUỐI

Chỉ kết thúc khi:

```text
ROOT CLEAN = YES
CURRENT FILES IDENTIFIED = YES
SUPERSEDED FILES REMOVED = YES
BROKEN LINKS = 0
RAW DATA LOSS = 0
SOURCE-OF-TRUTH LOSS = 0
MASTER INDEX = CURRENT
```

Thực hiện ngay, không quay lại dry run lần nữa, trừ khi gặp STOP RULE.
