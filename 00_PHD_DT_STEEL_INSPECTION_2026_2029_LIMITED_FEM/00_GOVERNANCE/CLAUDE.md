# CLAUDE.md — CHỈ DẪN VẬN HÀNH CHO MỌI PHIÊN CLAUDE COWORK
**Version:** v2.2 | **Hiệu lực từ:** 17/07/2026 | **Cập nhật:** 2026-08-04
**Status:** CURRENT SUPPORTING AGENT INSTRUCTION | **Source-of-truth level:** 7
**Supersedes:** v2.1 instruction. | **Superseded by:** None.
**Change summary:** Aligns Evidence Base entry, four-layer firewall, identifier/event rules and current gate/search state.

> Chi tiết quy tắc agent: `AGENT_RULES.md`. SOURCE OF TRUTH: `MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`.

## Trước khi làm việc

1. Luôn đọc `MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md` trước mọi nhiệm vụ; khi mâu thuẫn xem `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`.
2. Nếu nhiệm vụ chạm evidence/gate/paper: đọc thêm `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md`, `EVIDENCE_GATES_v2.1.md`, và `../02_EVIDENCE_BASE/CURRENT/00_MASTER_INDEX_CURRENT_20260804.md`.
3. Khai báo đầu nhiệm vụ: `RQ → WP → Chapter/Paper → Evidence Gate → Scope classification (Core / Supporting / Future Work / Out of Scope)` + kế hoạch ngắn.

## Bốn điều chỉnh bắt buộc v2.1
- Paper 1 claims = **candidate pending Gate 1** (ghi nhãn trước G1).
- CEI = **first-class metadata structure**, không scalar/Health Index/severity.
- Field: Paper 3 publication optional; **minimum field evidence mandatory**.
- Legal mapping chỉ neo nghĩa vụ quản lý; tham chiếu chưa xác minh → "Legal reference pending official-source verification."

## Quy tắc nội dung

1. Mọi đề xuất phải bám chuỗi đã khóa: dữ liệu dao động → condition/state-change evidence (+CEI) → BIM-linked component → inspection record → Action_Record → candidate Status_Event history → accountable verification-controlled inspection-maintenance support. Chuỗi định danh: Sensor_ID → BIM_GUID / Asset_ID @ Model_Version_ID → Condition_Evidence_ID → Inspection_Record_ID → Action_Record_ID. Action_Status/Workflow_Status là current projection; exact Status_Event_ID remains proposed.
2. Ưu tiên định vị Quản lý xây dựng và quản lý tài sản trong mọi lập luận, tiêu đề, từ khóa.
3. **Không tự mở rộng FEM.** FEM chỉ là mô hình thiết kế tham chiếu danh nghĩa; mọi lần nhắc FEM phải kèm "nominal, uncalibrated, reference-only, not used for damage diagnosis". Không đưa FEM_Node_ID thành mắt xích bắt buộc. Không đề xuất hiệu chuẩn, MAC, EMA, suy giảm độ cứng.
4. **Không tự thêm** RUL, predictive maintenance, chẩn đoán hư hỏng hiện trường, Health Index trọng số, bảo trì tự động, CFD, Smart City, Edge AI, phần mềm thương mại.
5. **Không bịa** tài liệu, DOI, Zotero key, kết quả, tiêu chuẩn, quartile, chỉ số hay metric. Thiếu bằng chứng thì ghi rõ "Evidence is currently insufficient."
6. Phân biệt rõ và không trộn lẫn bốn lớp: laboratory evidence / information traceability / field feasibility / management decision support.
7. Thuật ngữ theo `TERMINOLOGY_CONTROL_CURRENT.md`. Ưu tiên: data-informed Digital Twin; condition evidence; state-change evidence; BIM-linked component traceability; field feasibility; inspection-maintenance support; reference-informed sensor placement; CEI = confidence/evidence indicator. Cấm trong kiến trúc lõi: calibrated FEM; physics-informed condition evidence; equivalent stiffness degradation; optimal sensor placement; damage severity; FEM-based diagnosis.

## Cảnh báo scope creep

Khi yêu cầu có dấu hiệu vượt phạm vi (chạm danh mục Out of Scope, thêm mục tiêu mới, thêm công cụ ngoài chuỗi): dừng, phân loại (Core / Supporting / Future Work / Out of Scope), cảnh báo người dùng trước khi thực hiện. Không thực hiện Out of Scope dù được diễn đạt hấp dẫn.

## Cấu trúc trả lời phân tích

Mọi output phân tích dùng cấu trúc:

```text
Claim → Evidence → Limitation → Next action
```

Không bỏ qua Limitation. Không tự đánh dấu gate hay nhiệm vụ COMPLETE khi chưa có bằng chứng được ghi nhận.

## Quy tắc file

Không ghi đè file học thuật đã phát hành mà không version. File mới phải có version/ngày; file superseded được xử lý theo cleanup/deletion manifest và backup snapshot. Không sửa Zotero khi chưa được người dùng phê duyệt. Zotero MCP vận hành qua OpenCode; evidence output hiện hành nằm tại `../02_EVIDENCE_BASE/`.

## Kết thúc nhiệm vụ

Báo cáo: files đã đọc; files đã tạo; evidence đã dùng; hạn chế chưa giải quyết; hành động kế tiếp; Evidence Gate kế tiếp có tiến gần hơn không.
