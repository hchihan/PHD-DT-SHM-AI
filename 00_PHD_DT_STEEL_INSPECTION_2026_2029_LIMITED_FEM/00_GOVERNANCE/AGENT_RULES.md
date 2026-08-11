# AGENT RULES — v2.2
**Version:** v2.2 | **Issued:** 2026-07-19 | **Updated:** 2026-08-04
**Status:** CURRENT | **Source-of-truth level:** 4 | Áp dụng: mọi phiên Claude Cowork, Claude Code, OpenCode, AI agent.
**Supersedes:** v2.1 agent rules. | **Superseded by:** None.
**Change summary:** Adds Evidence Base entry, current gate/search state, identifier/event distinctions and immutable-evidence protection.
**Governs / thay thế vai trò:** mọi `AGENT_RULES.md` / `RESEARCH_CHARTER.md` cũ trong AI_SYSTEM/AGENTS (nếu còn) — các file đó, nếu tồn tại và mâu thuẫn, được coi là superseded bởi file này.

---

## 1. Trước mỗi nhiệm vụ — đọc theo thứ tự
1. `MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md` (source of truth).
2. `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md` khi có nghi ngờ mâu thuẫn.
3. `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md` + `EVIDENCE_GATES_v2.1.md` khi chạm RQ/WP/paper/gate.
4. `TERMINOLOGY_CONTROL_CURRENT.md` cho thuật ngữ.
5. `../01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md` + `../01_CURRENT_CONTROL/CURRENT_DIRECTION_LOCK_20260804.md` cho hiện trạng và hướng thực thi hiện hành.
6. `../02_EVIDENCE_BASE/CURRENT/00_MASTER_INDEX_CURRENT_20260804.md` cho evidence entry và classification.

## 2. Khai báo đầu nhiệm vụ (bắt buộc)
`RQ → WP → Chapter/Paper → Evidence Gate → Scope classification (Core / Supporting / Future Work / Out of Scope)`.

## 3. Trục đã khóa (không được lệch)
- Evidence chain: vibration → condition/state-change evidence (+CEI) → BIM-linked component → inspection record → justified, accountable action.
- Identifier chain: Sensor_ID → BIM_GUID / Asset_ID @ Model_Version_ID → Condition_Evidence_ID → Inspection_Record_ID → Action_Record_ID. CEI = attribute của Condition_Evidence_ID; Action_Status/Workflow_Status = current projection, không phải identifier/history. Status_Event_ID là proposed, not accepted.
- FEM: nominal, uncalibrated, reference-only, not used for damage diagnosis. Mọi lần nhắc FEM kèm qualifier này. `FEM_Node_ID` chỉ optional metadata.

## 4. Bốn điều chỉnh bắt buộc v2.1
1. **Paper 1 claims = candidate pending Gate 1.** Trước G1, mọi metric/kết luận Paper 1 ghi "Candidate claim pending Gate 1 closure."
2. **CEI = first-class metadata structure**, không phải scalar/Health Index/severity. Thiếu bằng chứng → ghi "Evidence is currently insufficient to define CEI as a universal scalar index."
3. **Field: publication (Paper 3) optional; minimum field evidence mandatory.** Không ghi toàn bộ RQ3/field là "optional".
4. **Legal mapping** chỉ neo nghĩa vụ quản lý; không tạo ngưỡng kỹ thuật; tham chiếu chưa xác minh ghi "Legal reference pending official-source verification."

## 5. Không tự mở rộng (Out of Scope — dừng và cảnh báo)
calibrated FEM, MAC, EMA, stiffness degradation, FEM sensitivity, RUL, predictive maintenance, field damage diagnosis, CFD, Smart City, Edge AI, weighted/complex Health Index, commercial DT software, autonomous maintenance, direct lab-to-field classifier transfer, optimal sensor placement, ontology-engineering-as-contribution.

Không claim độc lập novelty cho sensor-to-BIM, IFC GlobalId, BIM-CMMS, CQ, provenance, SHACL/SPARQL/MVD/IDS/database validation, generic fixtures, direct/inverse navigation, human-in-the-loop hoặc viewer/website. Không dùng “first”, “no study worldwide” hoặc universal absence. `CLOSE_SEARCH` chỉ corpus-bounded và không phải G2 PASS.

## 6. Không bịa
Không bịa tài liệu, DOI, Zotero key, kết quả, tiêu chuẩn, quartile, metric, hay điều luật. Thiếu bằng chứng → ghi rõ "Evidence is currently insufficient."

## 7. Cấu trúc phân tích
Mọi output phân tích/review/status: **Claim → Evidence → Limitation → Next action.** Không bỏ Limitation. Phân biệt bốn lớp bằng chứng; không mượn chéo.

## 8. Quy tắc file
- File mới có version/ngày. File cũ bị thay thế giữ lại + header SUPERSEDED (xem `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`).
- Không sửa/xóa/ghi đè/đổi tên file quản trị nếu người dùng chưa yêu cầu rõ ràng.
- Không sửa kết quả/metric/citation khoa học nếu không có bằng chứng.
- Không sửa Zotero khi chưa được phê duyệt.
- Không sửa nội dung khoa học của Round 1, Round 2, Round 3A, Round 3B, recent screening hoặc raw evidence; chỉ metadata quản trị/link được phép theo yêu cầu rõ ràng.

## 9. Đóng gate
Không tự đánh dấu gate hay nhiệm vụ COMPLETE khi chưa có bằng chứng ghi nhận + keyword check. Không tồn tại gate FEM.

## 10. Kết thúc nhiệm vụ
Báo cáo: files đã đọc/tạo/sửa/archive; evidence đã dùng; hạn chế chưa giải quyết; hành động kế tiếp; Evidence Gate kế tiếp có tiến gần hơn không.
