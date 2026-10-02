# HT3 – Pha 3, Dẫn nhập và Phụ lục: Biên tập văn phong (02/10/2026)

Làm theo prompt mục 6, cùng cách làm với các chương trước. Phiên này cũng chuyển "Song sinh số" sang viết thường ở Chương 1, như đã nêu ở việc còn mở của HT3 Chương 2.
Giữ nguyên trích dẫn, số liệu và thuật ngữ, không thêm tài liệu. Có 12 lệnh sửa, xem `revision/HT3_dannhap_phuluc_edits.json`.

## 1. Số đo trước / sau

Chỉ đếm văn xuôi, bỏ bảng và chú thích ẩn; độ dài câu tính theo âm tiết.

| Tệp | Câu > 45 âm tiết | Câu > 60 âm tiết | Bôi đậm | Trích dẫn |
|---|---:|---:|---:|---|
| Dẫn nhập | 7 → 3 | 5 → 0 | 1 → 0 | không đổi |
| Phụ lục | 2 → 1 | 1 → 0 | 12 → 11 | không đổi |
| Chương 1 (chỉ đổi chữ hoa) | — | — | — | không đổi |

- Dẫn nhập còn 3 câu dài, dài nhất 58 âm tiết. Một trong số đó là luận đề, giữ nguyên văn cho khớp 5.3.1.
- Phụ lục còn 11 chỗ bôi đậm, đều là từ mục của danh mục định nghĩa ở A.3 (dạng **Thuật ngữ.** Định nghĩa). Đây là nhãn tra cứu nên giữ.
- Trong văn xuôi Dẫn nhập không còn câu giới hạn. Script vẫn đếm 1 cụm, nhưng đó là cụm "không phải hỏi lại từng người" trong kịch bản, không phải câu giới hạn.

## 2. Thay đổi

| Tệp | Nhóm | Nội dung |
|---|---|---|
| Dẫn nhập | Tách câu (7) | Đoạn 3: tách câu liệt kê nền nghiên cứu và câu về điểm nối. Đoạn 5: tách câu về loại tài sản. Đoạn 6: tách phát biểu KT1, KT2 thành câu nêu tên và câu nêu nội dung. Đoạn cuối: tách câu "phương tiện / đối tượng quản lý" |
| Dẫn nhập | Bôi đậm (1) | "bằng chứng trạng thái" |
| Dẫn nhập | Giới hạn phát biểu khoảng trống (1) | "xác định hai khoảng trống" → "xác định hai khoảng trống trong tập tài liệu đã rà soát" (prompt 6.2; khớp cách viết ở 5.2) |
| Phụ lục | Bôi đậm (1) | "bản ghi sử dụng bằng chứng" ở A.2 |
| Phụ lục | Tách câu (1) | B.3: câu tiền lệ [21] tách thành ba câu, không mở câu bằng số trích dẫn |
| Chương 1 | Thuật ngữ (17 chỗ) | "Song sinh số" giữa câu → "song sinh số". Giữ viết hoa ở đầu tiêu đề 1.1.3 và ở đầu câu (1.6.4) |

## 3. Ví dụ trước / sau

| Nhóm | Trước | Sau |
|---|---|---|
| Tách câu | Khó khăn nằm ở các điểm nối giữa những thành phần đó: một kết quả … còn đúng; và khi đi vào hồ sơ kiểm tra, quyết định xử lý, kết quả đó phải truy ngược được … | Khó khăn nằm ở các điểm nối giữa những thành phần đó. Một kết quả … còn đúng. Khi kết quả đó đi vào hồ sơ kiểm tra và quyết định xử lý, nó phải truy ngược được … |
| Tách câu | Khoảng trống thứ hai (KT2) là đường đi từ bằng chứng đến hành động có trách nhiệm: chuỗi … chưa đi vào chuỗi đó, và mỗi lần đổi trạng thái … | Khoảng trống thứ hai (KT2) là đường đi từ bằng chứng đến hành động có trách nhiệm. Chuỗi … chưa đi vào chuỗi đó. Mỗi lần đổi trạng thái … cũng chưa được ghi … |
| Tách câu | … đã có tiền lệ trong quản lý tiến độ 4D: \[21\] kiểm mỗi cấu kiện …, là kỹ thuật tương tự C1, và kiểm các công việc … | … đã có tiền lệ trong quản lý tiến độ 4D. Nghiên cứu \[21\] kiểm mỗi cấu kiện …, kỹ thuật tương tự C1. Nghiên cứu này cũng kiểm các công việc … |

## 4. Kết thúc Pha 3

Đã biên tập văn phong xong toàn văn: Chương 1–5, Dẫn nhập, Phụ lục. Bảng thuật ngữ (`00_thuatngu.md`) không thuộc phạm vi Pha 3; tiêu đề bảng ở đó còn bôi đậm.

Việc tiếp theo là Pha 4 (GĐ6):
- A8: kiểm Nghị định 207/2026;
- A11: rà cột `muc_da_doc`, rồi chèn khai báo AI tạo sinh;
- A12: vẽ lại bốn hình;
- A13: sửa ngày ở bìa;
- đánh số lại trích dẫn theo IEEE, xuất Word;
- soạn bản giải trình G1–G7 và danh sách "Chuyển sang luận án".

ĐIỂM DỪNG 3 – Dẫn nhập, Phụ lục.
