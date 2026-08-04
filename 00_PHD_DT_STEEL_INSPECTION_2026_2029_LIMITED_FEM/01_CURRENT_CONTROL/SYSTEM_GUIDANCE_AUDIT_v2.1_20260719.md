# SYSTEM GUIDANCE AUDIT — v2.1
**Date:** 2026-07-19 | **Scope:** audit toàn bộ file dẫn hướng còn lại; đồng bộ theo Charter v2.1; sửa 6 vấn đề cấu trúc; gom pre-v2 vào archive chung.
**Classification key:** A CURRENT v2.x · B UPDATE REQUIRED (đã update) · C HISTORICAL DECISION SOURCE · D EVIDENCE–KEEP · E SUPERSEDED–ARCHIVE · F DUPLICATE/OBSOLETE–ARCHIVE · G REVIEW NEEDED.

| File | Version trước | Vấn đề | Hành động | Version sau | Trạng thái |
|---|---|---|---|---|---|
| 00_README_START_HERE.md | v2.1 (phase1) | trỏ v1.1 path | update chain refs + archive path | v2.1 | A CURRENT |
| 00_GOVERNANCE/MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md | v2.1 | thiếu Action_Record_ID, accountability, field prep/deploy | update §2.2/§2.4/§6.1 | v2.1+ | A CURRENT (SoT) |
| 00_GOVERNANCE/MASTER_RESEARCH_CHARTER.md (concise) | v2.1 | chain Action_Status | update chain | v2.1 | A CURRENT |
| 00_GOVERNANCE/RESEARCH_DIRECTION_AND_SCOPE.md | v2.1 | field prep/deploy | update §4.2 | v2.1 | A CURRENT |
| 00_GOVERNANCE/RESEARCH_ARCHITECTURE.md | v2.1 | chain Action_Status | update Lớp 2 | v2.1 | A CURRENT |
| 00_GOVERNANCE/RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md | v2.1 | chain, workstation-only, M1 | update §6, spine, M1 | v2.1+ | A CURRENT |
| 00_GOVERNANCE/EVIDENCE_GATES_v2.1.md | v2.1 checklist | checklist → execution gate; M1 | rewrite bảng 7 cột + M1 | v2.1+ | A CURRENT |
| 00_GOVERNANCE/TERMINOLOGY_CONTROL_CURRENT.md | v1.1+§5 | accountability, Action_Record, workstation | update §5 | v2.1 | A CURRENT |
| 00_GOVERNANCE/AGENT_RULES.md | v2.1 | chain Action_Status | update §3 | v2.1 | A CURRENT |
| 00_GOVERNANCE/CLAUDE.md | v2.1 | chain Action_Status | update §Quy tắc 1 | v2.1 | A CURRENT |
| 00_GOVERNANCE/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md | v2.1 | thêm ADR Action_ID + archive path | update | v2.1+ | A CURRENT |
| 00_GOVERNANCE/RESEARCH_ARCHITECTURE_DECISION_RECORD_20260719.md | v2.1 | — | KEEP | v2.1 | A CURRENT |
| 00_GOVERNANCE/RESEARCH_ARCHITECTURE_DECISION_RECORD_ACTION_ID_20260719.md | — | (mới) | CREATE | v2.1 | A CURRENT |
| 00_GOVERNANCE/THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md | 17/07 | — | KEEP (decision authority) | — | C HISTORICAL |
| 01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md | v2.1 | field prep/deploy | update §5.4 | v2.1 | A CURRENT |
| 01_CURRENT_CONTROL/UNRESOLVED_ITEMS_TRACKER_v2.1.md | v2.1 | thêm mục Action_ID/accountability/gate-exec | update | v2.1+ | A CURRENT |
| 01_CURRENT_CONTROL/PROJECT_CLEANUP_20260718/MASTER_INDEX_CURRENT.md | v2.1 | pointer v1.1/ADR/tracker | update tables | v2.1 | A CURRENT |
| 01_CURRENT_CONTROL/MISSING_CURRENT_FILES_REGISTER_20260718.md | 18/07 | — | KEEP | — | D EVIDENCE/AUDIT |
| 01_CURRENT_CONTROL/PROJECT_CLEANUP_20260718/*.csv, *_REPORT.md | 18/07 | — | KEEP | — | D EVIDENCE/AUDIT |
| 03_PAPERS/PAPER_1/PAPER1_DIRECTION_AND_GATE_v2.1_20260719.md | v2.1 | — | KEEP | v2.1 | A CURRENT |
| 03_PAPERS/PAPER_2/PAPER2_DIRECTION_AND_GATE_v2.1_20260719.md | v2.1 | accountability, Action_Record | update | v2.1+ | A CURRENT |
| 03_PAPERS/PAPER_3/PAPER3_FIELD_FEASIBILITY_DIRECTION_v2.1_20260719.md | v2.1 | field prep/deploy | update | v2.1+ | A CURRENT |
| 03_PAPERS/PAPER_1/** (manuscript, outlines, IT, QA) | mixed | scientific content | KEEP (không sửa) | — | D PAPER-KEEP |
| 02_EVIDENCE_BASE/** (LIVING v1.1/v1.2, RQ addenda, Zotero, CSV) | v1.x | notation Action_Status cũ | KEEP (không sửa evidence) | — | D EVIDENCE–KEEP |
| 04_PHD_SPECIAL_TOPICS/CHUYEN_DE_TONG_QUAN/** | v1 | matrix/Action_Status cũ (coursework) | KEEP + reconcile | — | G REVIEW |
| 07_PROMPTS_AND_HANDOFFS/OPENCODE/** | 18/07 | prompt pre-v2 | KEEP + regenerate khi dùng | — | G REVIEW |
| 00_GOVERNANCE/MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md | v1.1 | pre-v2 | ARCHIVE (+header) | — | E SUPERSEDED–ARCHIVE |
| 00_GOVERNANCE/RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md | ADR-2026-001 | pre-v2 | ARCHIVE (+header) | — | E SUPERSEDED–ARCHIVE |
| 01_CURRENT_CONTROL/UNRESOLVED_ITEMS_CURRENT.md | v1.1 | pre-v2 | ARCHIVE (+header) | — | E SUPERSEDED–ARCHIVE |
| MASTER_RESEARCH_CHARTER_v2_20260719.docx | v2.0 | historical | KEEP | — | C HISTORICAL DECISION SOURCE |
| 90_BACKUP/**, 92_ARCHIVE_MINIMAL/** | — | backup/archive sẵn có | KEEP (không gộp) | — | D/E (đã archive) |

## Ghi chú audit
- Không tồn tại `04_AI_SYSTEM/AGENTS/RESEARCH_CHARTER.md` hay `00_SYSTEM/MASTER_CHARTER.md` trong project hiện tại (đã cleanup trước đó). AGENT_RULES.md v2.1 tuyên bố thay vai trò nếu chúng còn ở nơi khác.
- Mọi kết luận version dựa trên **đọc nội dung**, không suy từ tên file.
- Chi tiết 6 fix: `SIX_STRUCTURAL_FIXES_IMPLEMENTATION_REPORT.md`. Kiểm tra mâu thuẫn: `SOURCE_OF_TRUTH_VALIDATION_REPORT.md` + `KEYWORD_AND_CONFLICT_CHECK_REPORT.md`.
