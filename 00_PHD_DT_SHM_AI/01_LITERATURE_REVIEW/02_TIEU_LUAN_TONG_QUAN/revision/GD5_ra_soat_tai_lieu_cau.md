# Rà soát 6 tài liệu về cầu (GĐ5, 02/10/2026; CLAUDE.md 6.2)

Tiêu chí (CLAUDE.md 6.2): giữ nếu còn làm căn cứ, loại nếu không. Kiểm thêm: nội dung câu trích có khớp tóm tắt hoặc toàn văn
không, có vai trò riêng hay trùng vai trò với nguồn đã đọc sâu ([6], [34], [35], [36], [29], [17]). Không có tài liệu nào
trong 6 bài có ghi chú đọc sâu; mức kiểm dưới đây là tóm tắt (OpenAlex) hoặc tìm theo từ khóa trong PDF Zotero.

| Số | Tài liệu | Nơi trích | Câu trích nói gì | Khớp nguồn | Vai trò riêng | Đề xuất |
|---|---|---|---|---|---|---|
| [63] | Isailović và cs. 2020, làm giàu ngữ nghĩa IFC bằng hư hỏng cầu | 4.3.1 | Làm giàu mô hình bằng thông tin hư hỏng và dữ liệu kiểm tra | Mức tiêu đề (OpenAlex không có tóm tắt; tệp PDF Zotero mở lỗi tên) | Trùng [64] | **Loại** khỏi 4.3.1, giữ [64] cho cùng ý |
| [64] | Xu và cs. 2022, mô hình hóa khiếm khuyết cầu qua IFC | 4.3.1 | Mô hình hóa khiếm khuyết cùng quan hệ với cấu kiện | Khớp tóm tắt: khiếm khuyết có quan hệ với cấu kiện, nguyên nhân và hành động bảo trì trong IFC | Tiền lệ cùng chiều với [35] cho chuỗi khiếm khuyết → hành động | **Giữ** (mức tóm tắt; không có PDF) |
| [65] | Mohamed và cs. 2023, khung BrIM kiểm tra – can thiệp | 4.3.1 | Tổ chức lịch sử kiểm tra và bảo trì trong khung BrIM | Một phần: tóm tắt nêu kiểm kê, dữ liệu kiểm tra, khiếm khuyết trên mô hình, báo cáo; không nêu "lịch sử" | Trùng [34], [6] | **Loại** |
| [66] | Jeon và cs. 2023, hệ bảo trì cầu dựa trên BrIM | 4.3.1 | Hệ bảo trì xuất phát từ yêu cầu của các bên sử dụng | Khớp tóm tắt: yêu cầu thông tin lấy từ phỏng vấn chủ sở hữu, người quản lý, kiểm tra viên; hệ mã kiểm kê | Tiền lệ cho cách lấy yêu cầu bằng phỏng vấn (QĐ 12) | **Giữ** |
| [77] | Sacks và cs. 2018, SeeBridge (IDM, MVD) | 4.5.3 | Kiểm soát chất lượng và xác nhận trong quy trình kiểm tra cầu | Một phần: PDF nêu kiểm soát chất lượng mô hình IFC và kỹ sư cầu rà soát IDM qua hội thảo; là xác nhận đặc tả, không phải xác nhận kết quả kiểm tra | Câu ở 4.5.3 đã có [78], [29], [17] | **Loại** |
| [78] | Wan và cs. 2019, hệ quản lý cầu dựa trên BIM | 4.5.3; 5.1.3 | Người quản lý rà soát, kiểm tra kết quả sửa chữa; gắn hồ sơ bảo trì, kiểm tra với cấu kiện trên dữ liệu thực | Khớp tóm tắt cho ý ở 5.1.3 (hệ thực cho một cầu dây văng, quản lý cộng tác nhiều người dùng); ý "rà soát kết quả sửa chữa" chưa kiểm trong toàn văn | Trích hai nơi | **Giữ**; kiểm ý ở 4.5.3 trong PDF ở GĐ6 |

Kết quả đề xuất: giữ 3 ([64], [66], [78]), loại 3 ([63], [65], [77]). Sửa văn bản cần:
- 4.3.1 câu 2: bỏ "qua làm giàu mô hình bằng thông tin hư hỏng và dữ liệu kiểm tra \[63\] hoặc", còn "mô hình hóa khiếm khuyết cùng quan hệ của chúng với cấu kiện và hành động bảo trì \[64\]".
- 4.3.1 đoạn 2: bỏ "tổ chức lịch sử kiểm tra và bảo trì trong khung BrIM \[65\]", đổi "ba cách" thành "hai cách".
- 4.5.3: bỏ "kiểm soát chất lượng và xác nhận trong quy trình kiểm tra cầu \[77\],".
- Danh mục tự rút ở GĐ6 (tạo lại từ trích dẫn thực có).
Ghi chú đối tượng: cả 6 bài về cầu; câu trích ở 4.3.1, 4.5.3, 5.1.3 nói về BIM cho kiểm tra – bảo trì nói chung, không dùng làm căn cứ cho luận điểm riêng về nhà công nghiệp.
