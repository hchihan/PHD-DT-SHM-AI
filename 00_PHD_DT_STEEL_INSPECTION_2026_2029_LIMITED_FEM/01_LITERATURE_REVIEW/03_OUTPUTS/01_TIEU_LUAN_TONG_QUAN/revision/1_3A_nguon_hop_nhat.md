# Nguồn hợp nhất cho mục 1.3A và 1.4A

Lập ngày 30/09/2026 (bước 4.3 của Giai đoạn 4). Danh sách mọi đoạn hiện có định nghĩa hoặc giải thích "bằng chứng trạng thái", và mọi chỗ trình bày chuỗi định danh. Cột cuối là **đề xuất cho Giai đoạn 5**; chưa sửa đoạn nào trong phiên này.

Vị trí ghi theo tên mục, vì số dòng thay đổi sau khi chèn 1.3A và 1.4A. Các mục 1.3A và 1.4A đã nằm sau mục 1.2 hiện có ("Vấn đề nghiên cứu"); mục 1.2 mới ("Đối tượng") chưa viết.

## A. Định nghĩa hoặc giải thích "bằng chứng trạng thái"

| Vị trí | Nội dung tóm tắt | Đề xuất ở GĐ5 |
|---|---|---|
| `00_dannhap.md`, đoạn 2 và 3 | Tính liên tục của bằng chứng; dùng khái niệm bằng chứng trạng thái thay cho đồng nhất đầu ra mô hình với chẩn đoán hư hỏng | Giữ ý; viết lại khi làm Dẫn nhập kịch bản (bước 4.9), dẫn về 1.3A |
| `00_thuatngu.md`, dòng Condition_Evidence_ID | Định nghĩa định danh bản ghi bằng chứng: kết quả phân loại kèm nguồn gốc, giao thức đánh giá, độ bất định, phạm vi hiệu lực | Giữ (bảng thuật ngữ); bổ sung dòng "Bằng chứng trạng thái" theo mục 10 CLAUDE.md |
| 1.2.2, đoạn 2 | Định nghĩa "kết quả tạo từ dữ liệu dao động cùng thông tin diễn giải"; phân biệt với chẩn đoán hư hỏng; bất thường dùng để kích hoạt kiểm tra | Viết lại thành "bằng chứng trạng thái từ dữ liệu dao động" như một loại con của khái niệm ở 1.3A, kèm câu trỏ về 1.3A; giữ câu "bất thường dùng để kích hoạt kiểm tra" |
| 1.3.1, đoạn 2 | Bằng chứng kỹ thuật mang theo điều kiện và giới hạn của chính nó; người ra quyết định cần nhãn kèm mức chắc chắn và bối cảnh | Giữ (lý do cần thiết); có thể nối bằng một câu trỏ 1.3A |
| 1.5.3 (Bốn loại bằng chứng), quy tắc chung | "Bất thường dẫn tới xem xét và kiểm tra, không dẫn trực tiếp tới kết luận hư hỏng" | Rút gọn: ý đã có ở 1.3A và 1.2.2; giữ "bốn loại bằng chứng" như khái niệm riêng (loại theo lớp kiểm chứng) |
| 1.9, phần giới thiệu Chương 3 | Tóm tắt Chương 3 nói kết quả trở thành bằng chứng khi đủ điều kiện | Giữ |
| 3.1.3 | Định nghĩa "bằng chứng trạng thái" là đầu ra của mô hình phân loại; lập luận hai chiều nhãn ↔ trạng thái vật lý; ba nguyên tắc | Giữ lập luận hai chiều và ba nguyên tắc; câu định nghĩa mở đầu: viết lại thành "bằng chứng trạng thái từ dữ liệu dao động" như một loại con của khái niệm ở 1.3A, kèm câu trỏ về 1.3A |
| 3.4.1 | Bản ghi bằng chứng là bản ghi có bối cảnh; hai mức tin cậy (dự đoán riêng lẻ và hiệu năng đã kiểm chứng); danh mục sáu yếu tố kèm bản ghi | Giữ (chiều sâu kỹ thuật); rút gọn câu mở đầu; đối chiếu danh mục sáu yếu tố với ba thành phần ở 1.3A |
| 3.4.2, 3.4.3 | Phạm vi hiệu lực; nguồn gốc dữ liệu | Giữ; 1.3A đã trỏ tới 3.4.2 |
| 3.5, đoạn "Từ góc nhìn của luận án…" | Nhắc lại điều kiện để kết quả phân loại thành bằng chứng | Viết lại thành "bằng chứng trạng thái từ dữ liệu dao động" như một loại con của khái niệm ở 1.3A, kèm câu trỏ về 1.3A và 3.4 |
| 2.x (`02_chuong2.md`, đoạn về hệ quả của sự phân mảnh) | Nhắc "bằng chứng trạng thái" như đối tượng người phụ trách phải truy ngược | Giữ |
| 4.x (tóm tắt Chương 4, mục ánh xạ cảm biến – cấu kiện) | Bằng chứng gắn với cấu kiện; ánh xạ có thời hạn | Giữ |
| 5.2.1 và các mục 5.x | Khoảng trống 1 dùng khái niệm; đóng góp 1 | Giữ; kiểm tra thuật ngữ khi viết lại 5.2 (ĐD3) |
| 5.6A.1 | Đầu ra AI ghi thành bản ghi bằng chứng có phiên bản phương pháp, độ bất định, phạm vi hiệu lực | Giữ; khớp với 1.3A |

## B. Chuỗi định danh (Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status)

Theo CLAUDE.md mục 6.2, chuỗi chi tiết và thang V1–V4 chuyển sang Phụ lục A.

| Vị trí | Nội dung tóm tắt | Đề xuất ở GĐ5 |
|---|---|---|
| 1.2.5 | Hình 1.1 (chuỗi nghiên cứu) và chuỗi định danh với lời giải thích năm mã | Giữ Hình 1.1; chuyển đoạn chuỗi định danh sang Phụ lục A, để lại một câu trỏ |
| 1.7.1, câu hỏi nghiên cứu 2 | Nhắc "chuỗi định danh" như trọng tâm của RQ2 | Giữ (RQ chuyển sang Chương 5 ở GĐ5) |
| 1.8.1 | Bốn lớp và chuỗi định danh lõi; ghi chú FEM_Node_ID; ghi chú Action_Status | Rút gọn thành câu trỏ Phụ lục A |
| 4.x (mục ánh xạ cảm biến – cấu kiện) | Lập luận quan hệ Sensor_ID → BIM_GUID chỉ là ánh xạ | Giữ lập luận; thay ký hiệu chuỗi bằng câu trỏ nếu trùng |
| 5.4.2, 5.6.1–5.6.2 (Hình 5.1) | Chuỗi định danh cốt lõi, giải thích năm mã, lớp kiểm chứng | Chuyển chi tiết sang Phụ lục A; Chương 5 giữ mô hình dữ liệu dạng đồ thị (5.5) |
| 5.9, tóm tắt hướng nghiên cứu | Nhắc chuỗi ở Hình 5.1 | Cập nhật tham chiếu sau khi chuyển |
| `00_dannhap.md`, cuối phần | Chuỗi logic (dữ liệu dao động → bằng chứng → cấu kiện → hồ sơ → hành động) | Giữ khi viết lại Dẫn nhập; đây là chuỗi nghiên cứu, không phải chuỗi định danh |

## C. Điểm cần NCS xem khi duyệt

1. **Thứ tự nhãn tạm.** Nhãn 1.3A và 1.4A đứng trước mục "1.3. Sự cần thiết" hiện có, vì mục 1.2 mới ("Đối tượng") chưa viết. Sẽ đánh số lại ở GĐ5.
2. **Ba thành phần và sáu yếu tố (đã quyết, 30/09/2026).** Giữ ba thành phần; 1.3A ghi nguồn gốc bao gồm nguồn thu, cấu hình cảm biến, phiên bản dữ liệu – chuỗi xử lý và giao thức đánh giá, trỏ về 3.4.1.
3. **Phạm vi khái niệm (đã quyết, 30/09/2026).** 1.3A nêu ba nguồn của bằng chứng trạng thái (mô hình trên dữ liệu cảm biến, quan sát của kỹ sư, phép đo kiểm tra không phá hủy); Bảng 1.3A đã sửa. 1.2.2, 3.1.3 và 3.5 sẽ viết lại ở GĐ5 thành loại con "bằng chứng trạng thái từ dữ liệu dao động".
4. **Trích dẫn.** 1.3A dùng [14], [15]; 1.4A dùng [16], [17]. Cả bốn đã được dùng đúng ý ở 1.2.2 và 1.2.4; không có tài liệu mới.
