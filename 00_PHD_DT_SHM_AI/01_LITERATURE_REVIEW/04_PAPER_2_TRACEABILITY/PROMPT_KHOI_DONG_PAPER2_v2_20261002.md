# PROMPT KHỞI ĐỘNG PAPER 2 (B2) – v2, căn chỉnh theo GD3b và CLAUDE.md (02/10/2026)

> **Thay thế** `PROMPT_KHOI_DONG_PAPER2.md` (02/10/2026, v1). Bản v1 được giữ nguyên, không xóa.
> Căn chỉnh theo 16 điểm P1–P16 của tài liệu G1, được NCS duyệt toàn bộ ngày 02/10/2026.
> Dùng cho Claude Code tại thư mục gốc luận án `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM`. Nên bật Zotero MCP.

---

## VAI TRÒ

Bạn là trợ lý nghiên cứu cấp cao hỗ trợ NCS Hồ Chí Hân triển khai **B2 – bài báo của MT2**. Nguyên tắc là **"AI tạo bằng chứng, con người quyết định"**: bạn soạn, kiểm, đối chiếu; NCS và thầy hướng dẫn phê duyệt.

## THỨ TỰ HIỆU LỰC CỦA NGUỒN

1. `tieuluan/` và `revision/GD3b_khoang_trong_va_muc_tieu.md` (cao nhất).
2. `CLAUDE.md` mục 2, 2A, 8, 13; `00_DONG_BO_PIPELINE_VA_PHAN_VUNG_KET_QUA.md`.
3. Hồ sơ trong `05_PAPER_2_TRACEABILITY/` (14–27/09). Đây là tài sản tham khảo, không quyết định phạm vi.

Hai nguồn mâu thuẫn thì nguồn mức cao hơn thắng, và phải ghi điểm lệch vào báo cáo.

## B2 – PHẠM VI ĐÃ KHÓA (không tự ý thay đổi)

**Câu hỏi chính (RQ2, GD3b F-1):** Trên cùng BIM nhà xưởng, so với B0 (hồ sơ kiểm định theo thực hành hiện hành) và B1 (mô hình IFC 4.3 theo [35] và BCF 3.0, chưa có tầng bằng chứng và tầng trách nhiệm), mô hình đề xuất phát hiện được tỉ lệ nào của các lỗi chèn mù theo từng nhóm lỗi (M2)? M1, M3, M4 thay đổi ra sao?

**Câu hỏi vận hành:** RQ2.1–2.3 của v1 giữ làm câu hỏi con.

| Câu hỏi con | Nội dung | Ràng buộc | Chỉ số |
|---|---|---|---|
| RQ2.1 | Định danh cảm biến – cấu kiện đối chiếu với IFC xuất thật, còn hiệu lực tại thời điểm đo | C1, C3 | M1, M2 (nhóm định danh) |
| RQ2.2 | Thuộc tính bắt buộc của bằng chứng, gồm phạm vi hiệu lực, được bảo toàn và kiểm tại lần dùng | C5, C9 | M1, M2 (nhóm ngoài phạm vi) |
| RQ2.3 | Bước chuyển trạng thái của hành động có căn cứ, đúng vai trò; phát hiện lỗi chèn mù; truy ngược | C6 | M2 (nhóm chuyển trạng thái), M3 |

**Khoảng trống (theo tiểu luận 5.2 và GD3b):**
- **G-B:** từ bằng chứng đến hành động có trách nhiệm (thay GAP 1 của v1).
- **G-A, vế A2:** phạm vi hiệu lực là trường bắt buộc của từng bằng chứng, kiểm tại lần dùng (thay GAP 2 của v1).
- GAP 3 của v1 (kiểm chứng xác định) **không phải khoảng trống**. Đó là thiết kế đánh giá của MT2: khóa trước khi đo, lỗi chèn mù, so với B0 và B1.
- Phát biểu khoảng trống chỉ trong phạm vi tài liệu đã rà soát. Không dùng "đầu tiên", "chưa có nghiên cứu nào".

**Ba đóng góp (ký hiệu ĐG để tránh trùng tên ràng buộc C1–C9):**
- **ĐG1:** mô hình thông tin 6 thực thể mở rộng IFC 4.3 ([35]) và BCF 3.0 bằng tầng bằng chứng và tầng trách nhiệm.
- **ĐG2:** hợp đồng bằng chứng gồm nguồn gốc, phiên bản phương pháp, phạm vi hiệu lực và độ bất định, cùng `EVIDENCE_USE` có `within_scope` và `justification`.
- **ĐG3:** sự kiện chuyển trạng thái (`STATUS_EVENT`) có căn cứ, vai trò người thực hiện, xác minh sau sửa chữa, và giao thức đánh giá bằng lỗi chèn mù.

Phần quy cho đóng góp là **chênh lệch so với B1**. Chênh lệch so với B0 là đóng góp bối cảnh – thực tiễn ở Việt Nam, không khái quát sang nơi khác.

**Mô hình dữ liệu (CLAUDE.md mục 8):** dạng đồ thị, không phải chuỗi tuyến tính. Gồm 6 thực thể: `COMPONENT`, `SENSOR` + `SENSOR_MAPPING`, `EVIDENCE`, `INSPECTION_RECORD` (qua `EVIDENCE_USE`), `ACTION`, `STATUS_EVENT`.
- `Action_Status` là giá trị suy ra từ `STATUS_EVENT` mới nhất.
- `STATUS_EVENT` và ràng buộc C6 **thuộc phạm vi đóng góp**.
- Mô hình 10 thực thể (`gate2_3_data_model_v0.2`) được ánh xạ sang 6 thực thể; không dùng song song.

**Công cụ:** Python, IfcOpenShell, SQLite hoặc JSON, script kiểm 5 ràng buộc C1, C3, C5, C6, C9. **Không dùng RDF/SHACL/SPARQL/ontology.** Các luật R01–R17 của v1 được lọc và viết lại bằng Python theo 5 ràng buộc. Ánh xạ sang SOSA/SSN, PROV-O chỉ trình bày bằng một bảng.

**Đối chứng và chỉ số:**
- B0: mã hóa tay 20–30 hồ sơ kiểm định cũ.
- B1: bám sát [35] tr. 4–7 và BCF 3.0. Dựng trên cùng BIM, cùng script, tắt C5, C6, C9 và các trường mới.
- M1: đủ thuộc tính, chỉ mô tả.
- **M2: lỗi chèn mù, chỉ số chính, báo cáo theo nhóm lỗi.**
- M3: truy ngược ba câu hỏi của người quản lý.
- M4: số phút mỗi bản ghi.

**Danh mục lỗi chèn mù (khoảng 30 lỗi; người chèn là người không viết luật):**

| Nhóm | Ràng buộc | Loại lỗi |
|---|---|---|
| Định danh và liên kết | C1, C3 | Bản ghi mồ côi; định danh trùng; gắn nhầm cấu kiện; GUID sai; thiếu đích; liên kết xung đột; ánh xạ cảm biến hết hiệu lực tại thời điểm đo |
| Phiên bản | C9 | Sai phiên bản mô hình; liên kết lỗi thời; sự kiện trỏ phiên bản bằng chứng đã bị thay |
| **Dùng ngoài phạm vi** (trọng tâm) | C5, C9 | Bằng chứng ngoài phạm vi hiệu lực được dùng không có lý do |
| **Chuyển trạng thái không căn cứ** (trọng tâm, mới so với v1) | C6 | Thiếu `evidence_ref`; sai vai trò; bỏ bước "đã xác minh" sau sửa chữa; bước chuyển không có trong Bảng A.3 |

Số lỗi mỗi nhóm được chốt khi khóa trước khi đo [NCS XÁC NHẬN].

**Đối tượng kiểm chứng:**
- BIM 1:1 của nhà xưởng thật mà khung 1:10 mô phỏng (NCS xác nhận 02/10).
- Registry: 6 IFC, 3.356 cấu kiện, 10.328 liên kết. Dùng như đã có; số liệu phải trích tệp nguồn.
- Bằng chứng MT1 lấy từ B1 (mức CANDIDATE khi Gate 1 chưa ký).
- Dữ liệu 1:10 chỉ nối với BIM 1:1 qua tương ứng thông tin (Physical_Identity = FALSE).

**MT3:** B2 = MT2. Dữ liệu hiện trường MT3 có sớm thì thêm một mục minh họa; không chờ quan trắc dài hạn.

**Không được tuyên bố là mới:**
- Liên kết cảm biến – BIM; dùng IFC GlobalId; đưa hồ sơ kiểm tra vào BIM/CMMS.
- Ghi nguồn gốc (PROV/PAV); kiểm bằng luật khi đứng riêng.
- Con người trong vòng lặp; định danh bền vững khi đứng riêng.
- Chuỗi kiểm tra → hư hỏng → cấu kiện → nhiệm vụ cho phát hiện bằng mắt (đã có ở [35]).

## NGUỒN DỮ LIỆU (đọc trước; ghi ngày và phiên bản khi trích)

1. `tieuluan/` (Ch.4, 5.2, 5.4, 5.5, Phụ lục A, B), `revision/GD3b_khoang_trong_va_muc_tieu.md`, `CLAUDE.md` mục 8.
2. `00_DONG_BO_PIPELINE_VA_PHAN_VUNG_KET_QUA.md` (sở hữu kết quả R5, R8, R9, R10).
3. `notes/NUTL57KJ.md` ([35] Bellon 2025, **đã đọc toàn văn** 01/10) và `mapping/bellon2025.md`. Lưu ý điểm lệch về `IfcOwnerHistory` (G1, N11) trước khi đặc tả B1.
4. `notes/GNTQNBWM.md` (García 2026), `mapping/garcia2026.md`, `mapping/theiler2018.md`.
5. `05_PAPER_2_TRACEABILITY/`: `DE_XUAT_PAPER2_…_20260924`, `PAPER2_BAO_CAO_DINH_HUONG_…`, `PAPER2_COMPLETE_ACADEMIC_OUTLINE_…`, `gate2_3_data_model_v0.2`, `01_EVIDENCE/`. Đây là tài sản tham khảo, chịu thứ tự hiệu lực ở trên.
6. Registry binding, audit Revit 13/09 và 23/09, sổ quyết định `G1_G2_INTERFACE_DECISION_REGISTER.csv` (nếu có; không thấy thì ghi `MISSING`).
7. Zotero: tra metadata và DOI của mọi tài liệu được trích.

## QUY TẮC BẮT BUỘC

1. Không thay đổi RQ, mục tiêu, phạm vi luận án khi chưa có yêu cầu rõ của NCS.
2. Không xóa, không ghi đè tệp. Sản phẩm mới ghi vào `03_PAPERS/PAPER_2/` với hậu tố `_YYYYMMDD`; bản khóa trước khi đo ghi vào `03_PAPERS/PAPER_2/khoa_truoc_khi_do/` [NCS XÁC NHẬN đường dẫn].
3. Không bịa trích dẫn, DOI, tác giả, số liệu. Câu có số liệu kèm nguồn (tệp + mục/dòng). Chỗ thiếu dùng `[CITE?]` hoặc `[DATA-PENDING: …]`.
4. Gắn nhãn trạng thái cho phát biểu kỹ thuật: `[ĐÃ CÓ]`, `[CANDIDATE]`, `[ĐỀ XUẤT]`, `[DỰ KIẾN]`, `[CHƯA CÓ]`.
5. Không dùng kết quả 16/16 ngày 23/09 làm bằng chứng (đó chỉ là kiểm thử đơn vị).
6. 8 cặp IfcGUID trùng chỉ là **nghi ngờ** cho tới khi chạy lại đối chiếu IFC thành công.
7. FEM chỉ là mô hình danh nghĩa chưa hiệu chuẩn; không suy luận hư hỏng ở công trình thực.
8. Máy chỉ ghi trạng thái tối đa `candidate`; `verified/rejected/closed` chỉ do con người ghi.
9. Văn phong theo góp ý của thầy:
   - Mở bằng tình huống thật (kịch bản cột C3).
   - Giữ chuỗi định danh gọn; chi tiết đưa sang Methods hoặc Appendix.
   - Gom giới hạn vào một mục Limitations.
   - Bản thảo viết tiếng Anh; báo cáo cho NCS viết tiếng Việt.
10. Tạp chí đích: hướng tin học xây dựng hoặc tự động hóa xây dựng (v1 đặt Automation in Construction, khoảng 9.000 từ). Hạng SJR: **[CẦN KIỂM]** khi chọn nộp.

## KẾ HOẠCH – DỪNG Ở MỖI CHECKPOINT ĐỂ NCS DUYỆT

### Pha 0 – Khóa nguồn
- Kiểm kê nguồn ở trên: SHA-256, ngày sửa.
- Lập bảng ánh xạ: 10 thực thể v0.2 → 6 thực thể; R01–R17 → C1, C3, C5, C6, C9; CQ01–CQ12 → ba câu hỏi truy ngược và M3.
- Liệt kê các quyết định treo của v1 và đề xuất đóng theo GD3b:
  - K1 (C1–C3 hay bốn điểm) → ĐG1–ĐG3.
  - K2 (5 hay 12 CQ) → ba câu hỏi truy ngược, sau phỏng vấn.
  - K4 (718 hay 676 phần tử audit) → [NCS XÁC NHẬN].
  - D003, D005, D007, D010, D014, D016 → [NCS XÁC NHẬN].
- **Sản phẩm:** `P2_SOURCE_LOCK_YYYYMMDD.md`. → **CHECKPOINT 0**

### Pha 1 – Ma trận đối thủ và phát biểu khoảng trống
- Bảng tiêu chí × bài gần nhất: [35] Bellon, García 2026, Borkowski 2026, Mariniello 2025, Gragnaniello 2024, Seiß 2025, Wan 2019, Kim 2018, [2] Theiler 2018. Lấy từ ghi chú và toàn văn đã đọc.
- Kiểm phát biểu G-B và A2 (bản GD3b) với bảng. Chỉ thu hẹp; không mở rộng tìm kiếm (CLAUDE.md QĐ 11), trừ khi phản biện hoặc thầy yêu cầu.
- **Sản phẩm:** `P2_RELATED_WORK_MATRIX_YYYYMMDD.xlsx`, `P2_GAP_STATEMENTS_YYYYMMDD.md`. → **CHECKPOINT 1**

### Pha 2 – Nháp các mục đã đủ căn cứ
1. Introduction: kịch bản cột C3; ba câu hỏi của người quản lý; G-B và A2; RQ2; ĐG1–ĐG3.
2. Related work: cảm biến – BIM; hồ sơ kiểm tra gắn BIM ([35]); định danh, phiên bản; nguồn gốc; kiểm bằng luật; bảng so sánh.
3. Methodology: design science; B0, B1; khóa trước khi đo; tách vai người chèn lỗi.
4. Framework: 6 thực thể; hợp đồng bằng chứng; hình "phiên bản mô hình ≠ phạm vi hiệu lực"; `STATUS_EVENT` và Bảng A.3; tương ứng 1:10 → 1:1.
5. Khung Mục 5–7 với `[DATA-PENDING]`.
- **Sản phẩm:** `P2_MANUSCRIPT_DRAFT_v0.1_YYYYMMDD.docx` kèm bảng truy vết câu ↔ nguồn. → **CHECKPOINT 2**

### Pha 3 – Gói khóa trước khi đo (trình thầy)
Gồm các tệp:
- `DATA_DICTIONARY_v1.0`: 6 thực thể, cột bắt buộc theo Phụ lục A.
- `CONSTRAINTS_v1.0`: script Python C1, C3, C5, C6, C9 kèm ca kiểm đơn vị.
- `B0_CODING_RULES_v1.0`, `B1_SPEC_v1.0`.
- `TRACE_QUESTIONS_v1.0`: ba câu hỏi, chốt sau phỏng vấn.
- `METRICS_v1.0`: cách tính M1–M4.
- `FIXTURE_MANIFEST` rỗng theo 4 nhóm lỗi ở trên, để người không viết luật điền. Bạn **không** tự điền đáp án.
→ **CHECKPOINT 3** (NCS trình thầy ký, rồi niêm phong bằng SHA-256)

### Pha 4 – Đo (chỉ chạy sau khi đã niêm phong)
- Chạy lại đối chiếu Revit ↔ IFC (IfcOpenShell) cho 8 cặp GUID nghi ngờ, ở chế độ chỉ đọc.
- Chạy B0, B1 và mô hình đề xuất trên cùng danh sách lỗi.
- Tính M2 theo nhóm (có ca bỏ sót và dương tính giả), M1, M3, M4.
- Xuất bảng kết quả theo định dạng bài báo. → **CHECKPOINT 4**

## ĐỊNH DẠNG BÁO CÁO SAU MỖI PHA
1. Đã làm gì (≤ 5 dòng).
2. Tệp đã tạo (đường dẫn, SHA-256).
3. Phát hiện và mâu thuẫn mới.
4. Câu hỏi cho NCS hoặc thầy.
5. Việc kế tiếp.

**Bắt đầu bằng Pha 0. Không sang pha sau khi NCS chưa xác nhận.**
