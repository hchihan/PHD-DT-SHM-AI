# BẮT ĐẦU TẠI ĐÂY
**Ngày lập:** 17/07/2026 | **Cập nhật điều hướng:** 19/07/2026 | **Kiến trúc hiện hành:** Limited-FEM · **Traceability-Core v2.1** (Verdict B 17/07/2026; reframe traceability-core 19/07/2026)

> **SOURCE OF TRUTH hiện hành: `00_GOVERNANCE/MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`.** v1.1 đã SUPERSEDED (giữ làm lịch sử). Khi mâu thuẫn: xem `00_GOVERNANCE/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`.

## Dự án là gì

Luận án PhD ngành Quản lý xây dựng: **Digital Twin dựa trên dữ liệu (data-informed Digital Twin) phục vụ giám sát trạng thái và hỗ trợ kiểm tra, bảo trì nhà công nghiệp khung thép.**

## Định hướng hiện hành

Chuỗi nghiên cứu đã khóa:

```text
Dữ liệu dao động
→ bằng chứng biến đổi trạng thái (condition evidence)
→ cấu kiện liên kết BIM (BIM-linked component)
→ hồ sơ kiểm tra (inspection record)
→ hỗ trợ lựa chọn hành động kiểm tra, bảo trì
```

Trục v2.1 đã khóa: **evidence + CEI → BIM component → inspection record → justified, accountable inspection action.** FEM chỉ là mô hình thiết kế tham chiếu danh nghĩa (nominal, uncalibrated, reference-only, not used for damage diagnosis). Không mở rộng sang CFD, Smart City, Edge AI, RUL, dự báo hư hỏng, chẩn đoán hiện trường, Health Index phức tạp, phần mềm thương mại, bảo trì tự động.

## Thứ tự đọc

1. `00_GOVERNANCE/MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md` — **SOURCE OF TRUTH cao nhất**; đọc trước mọi phiên.
2. `00_GOVERNANCE/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` — trật tự ưu tiên khi mâu thuẫn.
3. `00_GOVERNANCE/RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md` + `00_GOVERNANCE/EVIDENCE_GATES_v2.1.md` — cấu trúc RQ/WP/Paper/Gate.
4. `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/RESEARCH_DIRECTION_AND_SCOPE.md` + `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/RESEARCH_ARCHITECTURE.md` — "vì sao" và kiến trúc bốn lớp.
5. `00_GOVERNANCE/AGENT_RULES.md` + `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/CLAUDE.md` — quy tắc vận hành cho agent.
6. `00_GOVERNANCE/TERMINOLOGY_CONTROL_CURRENT.md` — kiểm soát thuật ngữ.
7. `90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/CURRENT_STATUS_AND_NEXT_DIRECTION.md` + `01_CURRENT_CONTROL/UNRESOLVED_ITEMS_TRACKER_v2.1.md` — hiện trạng & mục chưa khóa.
8. `01_CURRENT_CONTROL/MASTER_INDEX_CURRENT.md` — điểm vào toàn bộ tài liệu hiện hành.

Tham chiếu lịch sử: `MASTER_RESEARCH_CHARTER_v2_20260719.docx` (v2.0, nguồn quyết định) và `99_ARCHIVE_PRE_V2_SYSTEM_20260719/` (v1.1 và ADR pre-v2 đã archive — xem `ARCHIVE_MANIFEST.md`).

## Quan hệ với tài liệu chi tiết

Bộ file này là khung định hướng chung. Direction v2.1 theo Paper: `03_PAPERS/PAPER_1|2|3/PAPER*_DIRECTION*_v2.1_20260719.md`. Evidence base hiện hành: `02_EVIDENCE_BASE/CURRENT/LIVING_EVIDENCE_BASE_v2.1_TRACEABILITY_CORE.md` (v1.1/v1.2 kế thừa, giữ lịch sử); literature discovery tại `06_LITERATURE_AND_ZOTERO/`; backup tại `90_BACKUP/`. Khi có mâu thuẫn: quyết định hai thầy 17/07/2026 > Council Review > **Charter v2.1** > file cấu trúc v2.1 > Charter v2.0 (lịch sử) > Master Index CURRENT > tài liệu chi tiết > file lịch sử (chi tiết: `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`).
