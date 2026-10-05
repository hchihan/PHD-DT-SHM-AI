# CLAUDE.md — CHỈ DẪN VẬN HÀNH CHO MỌI PHIÊN CLAUDE COWORK
**Hiệu lực từ:** 17/07/2026 | **Kiến trúc:** Limited-FEM

## Trước khi làm việc

1. Luôn đọc `MASTER_RESEARCH_CHARTER.md` (cùng thư mục) trước mọi nhiệm vụ nghiên cứu.
2. Nếu nhiệm vụ chạm vào evidence, gate, paper: đọc thêm `05_OUTPUT/Zotero_MCP/05_MASTER_INDEX_CONTROL/MASTER_INDEX_CURRENT_v1.1.md` để biết file nào là source of truth.
3. Khai báo đầu nhiệm vụ: RQ liên quan; WP; chương/paper; Evidence Gate hiện tại hoặc kế tiếp; phân loại Core Scope / Supporting Scope / Future Work / Out of Scope; kế hoạch thực hiện ngắn.

## Quy tắc nội dung

1. Mọi đề xuất phải bám chuỗi đã khóa: dữ liệu dao động → condition evidence → BIM-linked component → inspection record → inspection-maintenance support. Chuỗi định danh: Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status.
2. Ưu tiên định vị Quản lý xây dựng và quản lý tài sản trong mọi lập luận, tiêu đề, từ khóa.
3. **Không tự mở rộng FEM.** FEM chỉ là mô hình thiết kế tham chiếu danh nghĩa; mọi lần nhắc FEM phải kèm "nominal, uncalibrated, reference-only, not used for damage diagnosis". Không đưa FEM_Node_ID thành mắt xích bắt buộc. Không đề xuất hiệu chuẩn, MAC, EMA, suy giảm độ cứng.
4. **Không tự thêm** RUL, predictive maintenance, chẩn đoán hư hỏng hiện trường, Health Index trọng số, bảo trì tự động, CFD, Smart City, Edge AI, phần mềm thương mại.
5. **Không bịa** tài liệu, DOI, Zotero key, kết quả, tiêu chuẩn, quartile, chỉ số hay metric. Thiếu bằng chứng thì ghi rõ "Evidence is currently insufficient."
6. Phân biệt rõ và không trộn lẫn ba loại bằng chứng: laboratory evidence / field feasibility / decision support.
7. Thuật ngữ theo `05_OUTPUT/Zotero_MCP/05_MASTER_INDEX_CONTROL/TERMINOLOGY_CONTROL_v1.1.md`. Ưu tiên: data-informed Digital Twin; condition evidence; state-change evidence; BIM-linked component traceability; field feasibility; inspection-maintenance support; reference-informed sensor placement; CEI = confidence/evidence indicator. Cấm trong kiến trúc lõi: calibrated FEM; physics-informed condition evidence; equivalent stiffness degradation; optimal sensor placement; damage severity; FEM-based diagnosis.

## Cảnh báo scope creep

Khi yêu cầu có dấu hiệu vượt phạm vi (chạm danh mục Out of Scope, thêm mục tiêu mới, thêm công cụ ngoài chuỗi): dừng, phân loại (Core / Supporting / Future Work / Out of Scope), cảnh báo người dùng trước khi thực hiện. Không thực hiện Out of Scope dù được diễn đạt hấp dẫn.

## Cấu trúc trả lời phân tích

Mọi output phân tích dùng cấu trúc:

```text
Claim → Evidence → Limitation → Next action
```

Không bỏ qua Limitation. Không tự đánh dấu gate hay nhiệm vụ COMPLETE khi chưa có bằng chứng được ghi nhận.

## Quy tắc file

Không xóa, không ghi đè không version, không đổi tên file cũ. File mới phải có version/ngày. File bị thay thế: tạo bản mới + ghi archive/change log, giữ nguyên bản gốc. Không sửa Zotero khi chưa được người dùng phê duyệt. Zotero MCP vận hành qua OpenCode (handoff); Cowork đọc và tổng hợp output từ `05_OUTPUT/`.

## Kết thúc nhiệm vụ

Báo cáo: files đã đọc; files đã tạo; evidence đã dùng; hạn chế chưa giải quyết; hành động kế tiếp; Evidence Gate kế tiếp có tiến gần hơn không.
