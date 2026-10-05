# HT3 – Pha 3, Chương 5: Biên tập văn phong (02/10/2026)

Làm theo prompt mục 6 và cùng cách làm với HT3 Chương 1. Giữ nguyên trích dẫn, số liệu và thuật ngữ; không đổi nghĩa; không thêm tài liệu. Phiên này làm sau HT4 (sửa gộp A).

Có hai điểm nội dung nhỏ, theo quyết định của NCS ngày 02/10: ghi "LOCO trên cả ba đợt" ở MT1, Bảng 5.3, Bước kiểm chứng 1 và 5.7.2; ghi "Đắk Lắk" ở MT3.

## 1. Số đo trước / sau

Chỉ đếm văn xuôi, bỏ bảng và chú thích ẩn; độ dài câu tính theo âm tiết.

| Chỉ tiêu | Trước | Sau |
|---|---:|---:|
| Số âm tiết | 12.061 | 12.080 |
| Số câu | 298 | 341 |
| Câu > 45 âm tiết | 50 | 24 |
| Câu > 60 âm tiết | 26 | 4 |
| Bôi đậm | 45 | 11 |
| Ngoặc kép cong | 3 | 0 |
| Cụm câu giới hạn (năm cụm của CLAUDE 4.5 và "không mới", "chưa đủ") | 6 | 0 |
| Trích dẫn (số lượng từng khóa) | — | không đổi |

Về số âm tiết: phần bỏ đi gồm danh sách 9 mục ở 5.1.3, câu liệt kê năm ràng buộc ở 5.8.2 và hai câu lặp. Phần thêm vào là các câu mở khi tách câu, nên tổng số âm tiết gần như không đổi.

11 chỗ bôi đậm còn lại là nhãn tiêu đề nhỏ (Mục tiêu 1–3, Bước kiểm chứng 1–4, Lớp 1–4), dùng như các nhãn a)–e) ở 1.8.5.

4 câu dài hơn 60 âm tiết còn lại:
- luận đề (5.3.1), giữ nguyên văn cho khớp Dẫn nhập;
- câu hỏi nghiên cứu 1 và 2 (một câu hỏi không tách được);
- câu liệt kê ở 5.11 đoạn 1.

## 2. Nhóm thay đổi (61 lệnh sửa, xem `revision/HT3_ch5_edits.json`)

| Nhóm | Số chỗ |
|---|---:|
| Tách câu dài | 37 (gồm 1 câu chuyển thành danh mục) |
| Bỏ bôi đậm trong văn xuôi | 10, cùng các dòng bảng và 3 câu hỏi nghiên cứu (chuyển sang dạng trích khối) |
| Câu giới hạn loại B → câu kế thừa | 3 (5.1.1, 5.1.2, 5.1.3) |
| Câu giới hạn ở 5.9 viết theo hướng khẳng định | 2 khối (5.9.2, 5.9.4) |
| Bỏ lặp ý | 4 (danh sách 9 mục ở 5.1.3 trùng Bảng 5.1; năm ràng buộc ở 5.8.2 trùng Phụ lục B; quy tắc "bất thường → kiểm tra" ở 5.8.2 và 5.10.3) |
| Thống nhất thuật ngữ | "song sinh số", "thành phố thông minh" viết thường; "autoencoder" viết thường giữa câu |
| Từ cấm | "toàn diện" (5.9.4) |

## 3. Ví dụ trước / sau

| Nhóm | Trước | Sau |
|---|---|---|
| Giới hạn B | Các nguyên tắc phương pháp về đánh giá cũng không mới và bao phủ gần hết các rủi ro của một thí nghiệm dao động: phân biệt số quan sát tính toán… \[14\]; ảnh hưởng của cấp nguồn vật lý… \[15\]; … \[19\]. | Các nguyên tắc phương pháp về đánh giá đã được xác lập và bao phủ gần hết các rủi ro của một thí nghiệm dao động. Số quan sát tính toán cần được phân biệt với số đơn vị độc lập thực \[14\], … (tách thành bốn câu) |
| Lặp ý | Luận án không xem các nội dung sau là đóng góp mới tự thân: (9 gạch đầu dòng) | Luận án kế thừa từ các nghiên cứu trên việc liên kết cảm biến với BIM, dùng định danh IFC, … Bảng 5.1 ghi phần kế thừa và phần còn lại cho từng nhóm nội dung. |
| Tách câu | Nghiên cứu này kiểm hai điều: mức chênh lệch … (Mục tiêu 1), và khả năng kiểm bằng máy … (Mục tiêu 2). | Nghiên cứu này kiểm hai điều. Điều thứ nhất là mức chênh lệch … (Mục tiêu 1). Điều thứ hai là khả năng kiểm bằng máy … (Mục tiêu 2). |
| Danh mục song song | Trước lần đo đầu tiên, khóa và lưu có phiên bản: quy tắc mã hóa…; đặc tả B1…; danh sách…; bộ câu hỏi…; cách tính bốn chỉ số… (một câu 155 âm tiết) | Năm gạch đầu dòng, mỗi dòng một nội dung được khóa |
| Giới hạn, viết khẳng định | **Bằng chứng phòng thí nghiệm** chỉ chứng minh … Nó không chứng minh hư hỏng trong bối cảnh sử dụng thực. (lặp cho bốn loại) | Bằng chứng phòng thí nghiệm xác lập khả năng phân biệt các trạng thái có kiểm soát trong điều kiện đã kiểm chứng; hư hỏng trong bối cảnh sử dụng thực được xác lập qua kiểm tra của kỹ sư. (gộp một đoạn, trỏ Bảng 5.5) |

## 4. Việc còn mở
- Pha 3 cho Chương 2, 3, 4, Dẫn nhập và Phụ lục.
- 5.1.3 còn một đoạn dài dẫn 12 nguồn liên tiếp. Đoạn đúng nội dung nhưng dày; có thể gom theo bốn mắt xích nếu NCS muốn.

ĐIỂM DỪNG 3 – Chương 5.
