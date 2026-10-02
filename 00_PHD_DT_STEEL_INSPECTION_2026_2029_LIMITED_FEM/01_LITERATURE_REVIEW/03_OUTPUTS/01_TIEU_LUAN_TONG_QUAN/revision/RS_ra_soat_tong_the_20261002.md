# Rà soát tổng thể Tiểu luận tổng quan (02/10/2026, sau HT3 Chương 1)

Phạm vi: toàn bộ 10 tệp trong `tieuluan/` ở trạng thái làm việc hiện tại (chưa commit), cùng 4 hình ở `TLTQ_28.09.2026/figures/`.
Cách làm: đọc toàn văn Dẫn nhập, Thuật ngữ, Chương 1–5, Phụ lục; chạy script kiểm trích dẫn, tham chiếu chéo, bảng, thuật ngữ cấm.
Phiên này **không sửa** `tieuluan/`.

## 1. Kết luận nhanh

Bản hiện tại đã đủ khung để chốt: luận đề, hai khoảng trống, ba mục tiêu, ba câu hỏi, Bảng 5.4 (phương pháp) và Bảng 5.7 (đóng góp) khớp nhau. Trước khi nộp còn **13 việc phải sửa** (mục 3). Trong đó có 3 điểm cần NCS quyết định (A3, A10, A8). Ngoài ra, Pha 3 (văn phong) mới làm cho Chương 1.

| Trục | Đánh giá | Lý do chính |
|---|---|---|
| T1 Mục đích | Đạt | Luận đề ở Dẫn nhập và 5.3.1 trùng nguyên văn; MT ↔ RQ 1:1; ba câu hỏi ở 1.4 |
| T2 Đối tượng – phạm vi | **Mâu thuẫn** | 5.9.5 và 2.4 nói "không gán trước mức song sinh số", trái với khai báo bóng số (A1); 1.2.4 nói "hai môi trường" nhưng tả ba công trình (A3) |
| T3 Phương pháp | Đạt, có rủi ro | Bảng 5.4 đủ cột; còn nguồn hồ sơ B0 (A3) và độ khớp với bản thảo Bài 1 (A10) |
| T4 Đóng góp | Đạt | Bảng 5.7 tách khoa học (so với mốc cùng lần chạy, B1) và thực tiễn (B0, MT3) |

## 2. Các mục kiểm tự động: đạt

- Trích dẫn: 79 số cũ và 35 khóa `@` đều có trong `99_tailieu.md`; 35 khóa đều có trong `matrix/doi_chieu_danh_muc.csv`. [63], [65], [77], [80], [84] không còn được trích và đã chuyển vào chú thích ẩn.
- Không còn: K1–K3, UV-xx, G-A/G-B, "ba khoảng trống", "bốn họ", "đường cơ sở B0", nhãn 1.2A/5.6A, MLflow/DVC/LLM; không có số liệu hay kết quả của Paper 1.
- Bảng đánh số liên tục: 1.1, 2.1, 3.1, 4.1–4.2, 5.1–5.8, A.1–A.3, B.1–B.2. Mỗi bảng được nhắc trước khi xuất hiện. Mọi "Mục x.y" đều trỏ tới mục có thật.
- Năm của Ramasso (2025) và Kamariotis (2023) khớp với danh mục (N9). Câu về [82] đã sửa (N14). IFC4 đã có khóa `@63XPSMIR` (N11 một phần).

## 3. Việc phải sửa

### A. Sai hoặc mâu thuẫn

| # | Vị trí | Vấn đề | Đề xuất |
|---|---|---|---|
| A1 | 5.9.5; 2.4 đoạn 4 | Viết "không khẳng định hệ thống đã đạt một mức Song sinh số cụ thể" và "không tự gán trước một mức trưởng thành". Câu này trái với Dẫn nhập, 1.1.3, 5.6.6 và Thuật ngữ, nơi hệ thống đã được khai báo ở mức bóng số | Viết lại theo một ý: bóng số là **mức thiết kế**, khai báo theo [8]; **năng lực đạt được** đánh giá sau triển khai theo [9], [10]. Câu ở 2.5 đoạn 3 đã viết đúng theo cách này |
| A2 | 4.4.3, câu cuối | "hướng mở rộng (Bảng 5.7)": Bảng 5.7 nay là bảng đóng góp | Sửa thành Bảng 5.8 |
| A3 | 1.2.4; 5.3.3; 5.4.2; 5.10.2–5.10.3 | (a) Câu "phạm vi không gian gồm hai môi trường" nhưng mục này tả ba đối tượng: khung 1:10, BIM nhà xưởng Khánh Hòa (MT2), nhà xưởng Đắk Lắk (MT3). (b) 5.10.3 thu hồ sơ B0 khi khảo sát nhà xưởng MT3. Trong khi đó MT2 so B0, B1 "trên cùng BIM" Khánh Hòa. Văn bản chưa nói hồ sơ B0 của công trình nào. (c) CLAUDE.md mục 2A và 8 chưa ghi quyết định Khánh Hòa | NCS chọn công trình lấy hồ sơ B0, rồi sửa 1.2.4 thành "ba công trình, hai môi trường" và ghi nguồn B0. Sau đó cập nhật CLAUDE.md 2A, 8 |
| A4 | Dẫn nhập, đoạn 6 | "bằng một tầng bằng chứng và một tầng trách nhiệm": HT0 đã quyết bỏ cụm "một tầng" | "bằng tầng bằng chứng và tầng trách nhiệm" |
| A5 | 1.8.2, câu cuối | "ma trận 30 tài liệu đọc sâu", nhưng GĐ2 đóng với 29/30 ([80] bỏ) | "29 tài liệu" hoặc "30 tài liệu key, 29 đọc toàn văn" |
| A6 | 1.2.2 | "cấp C3" (cấp ăn mòn) trùng ký hiệu với cột trục C3 và ràng buộc C3 | Viết rõ "cấp ăn mòn C3" |
| A7 | 5.7.5, câu cuối | Câu "Việc sử dụng AI tạo sinh … được khai báo ở phần đầu" trỏ tới một mục chưa có trong `tieuluan/` | Chèn khai báo ở Pha 4 (bản nháp: `nhap_khai_bao_AI_tao_sinh.md`), hoặc tạm bỏ câu trỏ |
| A8 | 1.1.4 | Còn ba thẻ `[CẦN KIỂM]` cho Nghị định 207/2026/NĐ-CP: điều khoản thay thế NĐ 06/2021, Điều 34, Điều 37 | NCS đối chiếu văn bản gốc. Câu ở 1.6.2 dùng cùng căn cứ này |
| A9 | 1.4; 5.6.2 (câu liệt kê sáu thực thể); Bảng 5.6 dòng WP2; Hình 1.1; Hình 5.2 | Thực thể `INSPECTION_RECORD` lúc gọi "bản ghi kiểm tra", lúc gọi "hồ sơ kiểm tra" (HT1 đã chốt "bản ghi kiểm tra") | Khi nói về thực thể thì dùng "bản ghi kiểm tra". "Hồ sơ kiểm tra/kiểm định" chỉ dùng cho tài liệu thực hành và B0 |
| A10 | MT1, RQ1, Bảng 5.3, 5.4, 5.6; 5.7.2; 5.8.1 | Tiểu luận mô tả bốn mô hình và LOCO trên ba đợt. Theo ghi nhớ phiên trước (chưa kiểm lại bản thảo), Bài 1 v3.0 chỉ có 1D-CNN và ResNet-1D, và phần chéo đợt chỉ có CP2↔CP3 | NCS chốt: bổ sung RF, SVM-RBF và LOCO đủ ba đợt vào Bài 1, hoặc sửa tiểu luận cho khớp. Nếu không chốt, phần thiết kế đã tả sẽ lệch với bài báo |
| A11 | 5.7.3; Bảng 5.4 dòng RQ3 | [@G98ZWHKW] Ghazimoghadam mới đọc tóm tắt (N15). Ngoài ra, `thieu_toan_van.md` liệt kê 25 tài liệu thiếu toàn văn | Giữ câu ở mức tóm tắt. Không viết "mọi trích dẫn đều được đối chiếu với bản gốc" trong khai báo AI (CLAUDE 6.4) |
| A12 | Hình 1.1, 5.1–5.3 | Các hình là ảnh cắt từ PDF của bản .docx cũ, nằm trong thư mục chưa đưa vào git `TLTQ_28.09.2026/`; `figures/` đang ở trạng thái bị xóa. Hình 1.1 xếp "Bằng chứng → Cấu kiện", còn Hình 5.1 xếp `BIM_GUID → Condition_Evidence_ID`. Hình 1.1 và 5.2 ghi "Hồ sơ kiểm tra". Hình 5.2 đặt tên lớp 3 là "Khả thi hiện trường", còn văn bản gọi "Khả năng áp dụng trong bối cảnh thực tế" | Vẽ lại bốn hình (Mermaid/SVG trong `figures/`) với thứ tự và nhãn khớp văn bản, trước khi xuất Word |
| A13 | 00_bia.md | "tháng 09 năm 2026" | Sửa theo tháng nộp |

### B. Văn phong (Pha 3: Chương 2–5, Dẫn nhập, Phụ lục chưa làm)

- **Bôi đậm trong văn xuôi:** còn nhiều ở 5.1.1–5.1.4, 5.9.2–5.9.4, 3.4, 3.5, 4.2–4.5, 2.3. Chương 1 đã về 0.
- **"Song sinh số" viết hoa giữa câu:** khoảng 30 chỗ (1.1.2, 1.1.3, 1.6.4, 1.7, 1.8, Ch.2, 5.9.5), không thống nhất với cách viết thường ở Dẫn nhập và 1.1.3 đoạn 2. Bìa dùng "song sinh kỹ thuật số" theo tên đề tài, nên giữ ở bìa.
- **Ngôi viết lẫn:** có các cách "Tiểu luận rút ra" (3.2.1), "diễn giải của tiểu luận" (1.2.3, 3.2.2, 3.2.3), "Theo nhận định của nghiên cứu sinh" (2.2.3, 4.5.4) và "nghiên cứu này". Quyết định HT0 là "Theo đánh giá của phần tổng quan nghiên cứu này"; Dẫn nhập và 1.2.1 giữ "Từ thực tế kiểm định".
- **Lặp ý:**
  - Quy tắc "bất thường → kiểm tra, không → kết luận hư hỏng" xuất hiện ở 1.5.2, 1.6.3, 1.7.5, 3.1.3, 5.8.2, 5.9.2. Đề xuất giữ ở 1.7.5 và 5.9.2.
  - Đoạn về theo dõi theo quần thể [57] có ở cả 3.2.4 và 3.4.3.
  - Danh sách chín mục "không xem là đóng góp mới" ở 5.1.3 trùng với Bảng 5.1, và thuộc loại câu B của CLAUDE 4.5. Đề xuất bỏ danh sách, giữ bảng.
  - Câu "Các nguyên tắc … cũng không mới" ở 5.1.2 cũng thuộc loại B.
- **Câu dài (trên 45 âm tiết, ngoài bảng):**

  | | Ch.1 (đã biên tập) | Ch.2 | Ch.3 | Ch.4 | Ch.5 |
  |---|---|---|---|---|---|
  | Số câu dài / tổng số câu | 57/326 | 42/129 | 44/165 | 38/149 | 55/256 |
  | Tỉ lệ | 17 % | 33 % | 27 % | 26 % | 21 % |

### C. Đồng bộ tệp điều phối

- CLAUDE.md mục 8 còn ghi "Bảng A.3" cho bước chuyển trạng thái, nay là Bảng A.2. Mục này cũng chưa ghi quyết định BIM Khánh Hòa (A3).
- `revision/changelog.md` dừng ở HT1 phiên 1. Các phiên HT1 p2, p3, HT2 T1–T4 và HT3 Ch.1 chưa có dòng changelog và **chưa commit**: 11 tệp, khoảng 350 dòng thêm và 180 dòng bớt, đang nằm trên Google Drive.

## 4. Câu hỏi cho NCS

1. **A3:** Hồ sơ B0 (20–30 hồ sơ kiểm định cũ) lấy của nhà xưởng nào: Khánh Hòa (cùng BIM của MT2) hay Đắk Lắk (MT3)?
2. **A10:** Bài 1 sẽ chạy đủ bốn mô hình và LOCO ba đợt như tiểu luận mô tả, hay tiểu luận phải thu về hai mô hình và CP2↔CP3?
3. **Duyệt các phiên đang chờ:** HT1 p2–p3, HT2 T1–T4, HT3 Ch.1 đã được duyệt chưa, để commit trước khi sửa tiếp?
4. **Thứ tự làm tiếp:** đề xuất một phiên sửa A1, A2, A4–A7, A9 (sửa nhỏ, nhiều chương), rồi tiếp Pha 3 cho Chương 5.
