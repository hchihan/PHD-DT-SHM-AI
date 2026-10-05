# SOURCE OF TRUTH HIERARCHY — v2.1
**Version:** v2.1 | **Date:** 2026-07-19 | **Status:** CURRENT
**Mục đích:** một và chỉ một trật tự ưu tiên khi các tài liệu mâu thuẫn. Không được để nhiều file cùng tự nhận "source of truth".

---

## 1. Trật tự ưu tiên (cao → thấp)

1. **Quyết định hai thầy hướng dẫn 17/07/2026 (Verdict B)** + Council review 17–19/07/2026 → `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md` (DECISION_AUTHORITY).
2. **Charter v2.1 (SOURCE OF TRUTH cao nhất)** → `MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`.
3. **Bộ file cấu trúc v2.1 đồng cấp dưới Charter v2.1:** `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md`, `EVIDENCE_GATES_v2.1.md`, `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260719.md`, `RESEARCH_ARCHITECTURE_DECISION_RECORD_ACTION_ID_20260719.md`, `TERMINOLOGY_CONTROL_CURRENT.md`, `AGENT_RULES.md`.
4. **Charter v2.0** → `MASTER_RESEARCH_CHARTER_v2_20260719.docx` — **nguồn quyết định lịch sử** (historical decision source); dùng để tra cứu ngữ cảnh reframe, không phải nguồn hiện hành khi khác v2.1.
5. **File điều hướng hiện hành:** `00_README_START_HERE.md`, `../90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/MASTER_RESEARCH_CHARTER.md` (concise), `RESEARCH_DIRECTION_AND_SCOPE.md`, `RESEARCH_ARCHITECTURE.md`, `../01_CURRENT_CONTROL/MASTER_INDEX_CURRENT.md`.
6. **Current status / trackers:** `CURRENT_STATUS_AND_NEXT_DIRECTION.md`, `UNRESOLVED_ITEMS_TRACKER_v2.1.md`, `UNRESOLVED_ITEMS_CURRENT.md`.
7. **Evidence base & Paper packages hiện hành** (`02_EVIDENCE_BASE/`, `03_PAPERS/`).
8. **Discovery / literature / prompts** (`06_...`, `07_...`) — không citable làm evidence.
9. **v1.1 (LIMITED-FEM) — SUPERSEDED, ĐÃ ARCHIVE** → `../90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` + `../90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md`: giữ làm lịch sử, không dùng hiện hành.
10. **Archive chung pre-v2 + backup/archive cũ** (`99_ARCHIVE_PRE_V2_SYSTEM_20260719/`, `90_BACKUP/`, `92_ARCHIVE_MINIMAL/`) — không bao giờ là source of truth.

---

## 2. Trạng thái các charter

| File | Trạng thái | Vai trò |
|---|---|---|
| `MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md` | **SOURCE OF TRUTH** | Hiện hành cao nhất |
| `MASTER_RESEARCH_CHARTER_v2_20260719.docx` | HISTORICAL DECISION SOURCE | Reframe v2.0; tra cứu ngữ cảnh |
| `MASTER_RESEARCH_CHARTER.md` (concise) | CURRENT NAVIGATION | Điểm vào ngắn, trỏ về v2.1 |
| `../90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` | **SUPERSEDED — ARCHIVED** | Lịch sử; đã chuyển vào archive chung |

## 3. Quy tắc file cũ
- v2.1 = source of truth cao nhất; v2.0 = nguồn quyết định lịch sử; v1.1 = superseded (đã archive vào `99_ARCHIVE_PRE_V2_SYSTEM_20260719/`).
- File dẫn hướng pre-v2 còn lẫn trong active locations → gom vào `99_ARCHIVE_PRE_V2_SYSTEM_20260719/` (xem `ARCHIVE_MANIFEST.md`). File FEM-core cũ đã nằm sẵn trong `90_BACKUP/` và `92_ARCHIVE_MINIMAL` — giữ nguyên.
- Evidence file có giá trị: không xóa; chỉ đổi phân loại/liên kết/trạng thái sử dụng.
- Không sửa kết quả nghiên cứu, metric, citation nếu không có bằng chứng.
- File superseded phải có header: `Status: SUPERSEDED` / `Superseded by: [v2.1 file]` / `Preserved for: historical traceability only.`
- Không xóa khi chưa chắc chắn — đưa vào archive thay vì xóa.
