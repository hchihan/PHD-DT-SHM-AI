# HT2 – Pha 2, trục T3: Sự tương thích của phương pháp (02/10/2026)

Tiêu chí (prompt mục 3): mỗi RQ có phương pháp, dữ liệu, chỉ số, đối chứng tương ứng; có bảng hoặc đoạn chỉ rõ vì sao phương pháp phù hợp, kế thừa từ đâu, khác tiền lệ ở đâu. Kèm sửa T2 theo thông tin NCS: mô hình 1:10 mô phỏng nhà xưởng ở Khánh Hòa; nhà xưởng MT3 ở Đắk Lắk (Phú Yên cũ).

## 1. Ma trận T3 trước / sau
| Vị trí | Trước (HT0) | Sau |
|---|---|---|
| 1.8 | Yếu: "chín nhóm" ≠ 5 cụm; không nêu Consensus | 1.8.2 nêu chín nhóm gom thành năm cụm của ma trận 30 tài liệu; 1.8.5 thêm đoạn về Consensus, kiểm Crossref, Zotero, mức đã đọc ghi trong ma trận |
| 3.4 | Yếu: chưa định nghĩa mốc "đánh giá cùng lần chạy" | 3.4.3 thêm định nghĩa, dẫn [48], Eraliev 2022, nối với vế A1 |
| 3.3.1 | Mâu thuẫn: cấu hình cảm biến gán cho RQ1 | Cấu hình cảm biến là thành phần của phạm vi hiệu lực, ghi vào bối cảnh quan trắc |
| 4.4.3, Bảng 4.2, Bảng 5.1 | Mâu thuẫn: luận án dùng IDS, đặt bản ghi trên SOSA | Kiểm bằng năm ràng buộc Python; IDS là hướng mở rộng (thêm vào Bảng 5.7); SOSA chỉ đối chiếu qua Bảng A.3 |
| 5.4–5.5 | Yếu: chỉ số RQ1 chưa gọi tên; RQ3 không nối kịch bản C3 | 5.5.2 Bước 1 nêu chỉ số phân loại chấm theo bản ghi, khóa trong Bài báo 1 (sơ bộ, theo QĐ của NCS); Bước 4 gọi tên kịch bản cột C3 (Mục 1.4). M1–M4 đã gọi tên ở Pha 1 |
| Bảng tổng hợp | Thiếu | **Mục 5.5.3 mới** với đoạn "vì sao phù hợp" và **Bảng 5.4** (Câu hỏi – Phương pháp – Dữ liệu – Chỉ số – Đối chứng – Kế thừa từ – Khác tiền lệ ở) |
| 5.7, Phụ lục B | Đạt | Giữ |

**Kết luận T3: Đạt.**

## 2. Đánh số lại bảng
- 01_chuong1.md: Bảng 5.6 -> 5.7 (1)
- 05_chuong5.md: Bảng 5.6 -> 5.7 (3)
- 05_chuong5.md: Bảng 5.5 -> 5.6 (3)
- 05_chuong5.md: Bảng 5.4 -> 5.5 (3)
- phuluc.md: Bảng 5.4 -> 5.5 (1)

## 3. Trước / sau chi tiết
| Mã | Tệp | Trước | Sau |
|---|---|---|---|
| T2-sửa | `01_chuong1.md` | Mô hình 1:10 mô phỏng chính nhà xưởng này; hai bên chỉ được nối qua tương ứng thông tin, và luận án không khẳng định tương tự động lực học giữa chúng (Mục 3.4.3). | Mô hình 1:10 mô phỏng một nhà xưởng thực tế ở tỉnh Khánh Hòa; nhà xưởng của Mục tiêu 3 ở tỉnh Đắk Lắk (địa bàn tỉnh Phú Yên cũ). Vì là hai công trình khác nhau, kết quả trên mô hình 1:10 được nối với nhà xưởng ở Mục tiêu 3 qua nguyên tắc tổ chức bằng chứng, và luận án không khẳng định tương tự động lực học giữa chúng (Mục 3.4.3). |
| N29 | `03_chuong3.md` | Luận án sử dụng hai giao thức đánh giá theo nhóm để trả lời hai câu hỏi khác nhau. | Mốc so sánh của luận án là **đánh giá cùng lần chạy** (within-run evaluation): tập huấn luyện và tập kiểm tra được chia bên trong cùng các lần chạy, nên dữ liệu kiểm tra có thể đến từ lần chạy đã có trong huấn luyện. Hai nghiên cứu đã rà soát cho bài toán phân loại liên kết bu lông trên khung thép chia tập trong cùng lần lắp ráp hoặc cùng bản ghi \[48\], \[@VVBGM9EN\] (Mục 5.2.1). Chênh lệch giữa mốc này và hai giao thức dưới đây là đại lượng mà vế A1 của KT1 cần đo. ⏎  ⏎ Luận án sử dụng hai giao thức đánh giá theo nhóm để trả lời hai câu hỏi khác nhau. |
| N20 | `03_chuong3.md` | cấu hình cảm biến giữ vai trò hỗ trợ cho Câu hỏi nghiên cứu 1 (đánh giá chất lượng bằng chứng dưới các cấu hình khác nhau); | cấu hình cảm biến là một thành phần của phạm vi hiệu lực và được ghi vào bối cảnh quan trắc của mỗi bằng chứng (Phụ lục A); |
| N19 | `04_chuong4.md` | Luận án dùng cơ chế thứ nhất cho yêu cầu thông tin ở cấp cấu kiện và cơ chế thứ hai cho tính toàn vẹn của chuỗi truy vết. | Luận án kiểm tính toàn vẹn của chuỗi truy vết bằng năm ràng buộc viết bằng Python (Phụ lục B); dùng IDS cho yêu cầu thông tin ở cấp cấu kiện là hướng mở rộng (Bảng 5.7). |
| N19 | `04_chuong4.md` | \| Bản ghi bằng chứng nên đặt trên lớp quan trắc chuẩn thay vì lược đồ riêng; giao thức đánh giá và phạm vi hiệu lực nằm ngoài phạm vi của từ vựng này \| | \| Khái niệm của bản ghi bằng chứng cần đối chiếu được với lớp quan trắc chuẩn (Phụ lục A, Bảng A.3); giao thức đánh giá và phạm vi hiệu lực nằm ngoài phạm vi của từ vựng này \| |
| N19 | `05_chuong5.md` | \| Kết hợp kiểm tra thuộc tính cấu kiện với kiểm tra quan hệ của chuỗi bằng chứng \| | \| Kiểm quan hệ của chuỗi bằng chứng bằng ràng buộc (Phụ lục B); kết hợp với IDS là hướng mở rộng \| |
| N19 | `05_chuong5.md` | bù EOV bằng đồng liên kết khi có nguồn biến động chưa đo được \| | bù EOV bằng đồng liên kết khi có nguồn biến động chưa đo được; kiểm yêu cầu thông tin cấp cấu kiện bằng IDS \| |
| N26 | `01_chuong1.md` | vào các nhãn quá rộng như “trí tuệ nhân tạo”, “BIM” hay “Song sinh số”. | vào các nhãn quá rộng như “trí tuệ nhân tạo”, “BIM” hay “Song sinh số”. Trong ma trận 30 tài liệu đọc sâu, chín nhóm này được gom thành năm cụm: song sinh số; theo dõi trạng thái – liên kết bu lông – biến đổi môi trường và vận hành; độ tin cậy của đánh giá; truy vết thông tin; giá trị của thông tin cho quyết định. |
| N26 | `01_chuong1.md` | có thể sử dụng để đối chiếu, phản biện. ⏎  | có thể sử dụng để đối chiếu, phản biện. ⏎  ⏎ Một phần tài liệu ứng viên được gợi ý qua công cụ tìm kiếm học thuật có dùng trí tuệ nhân tạo (Consensus). Mỗi ứng viên được kiểm tên bài, tác giả, năm và DOI qua Crossref, nhập vào thư viện Zotero và chỉ được trích sau khi đọc ít nhất phần tóm tắt; mức đã đọc của từng tài liệu được ghi trong ma trận tài liệu. ⏎  |
| N36 | `05_chuong5.md` | báo cáo biến thiên theo seed và fold cùng kiểm định hoán vị; ghi mỗi kết quả | báo cáo biến thiên theo seed và fold cùng kiểm định hoán vị; hiệu năng đo bằng chỉ số phân loại chấm theo bản ghi, chỉ số cụ thể được khóa trong Bài báo 1; ghi mỗi kết quả |
| T3-RQ3 | `05_chuong5.md` | chạy kịch bản một bất thường dẫn tới bằng chứng gắn cột, | chạy kịch bản cột C3 ở Mục 1.4, trong đó một bất thường dẫn tới bằng chứng gắn cột, |
| T3-bảng | `05_chuong5.md` | xác minh sau sửa chữa và truy ngược; đối chiếu ánh xạ với thực địa. ⏎  | xác minh sau sửa chữa và truy ngược; đối chiếu ánh xạ với thực địa. ⏎  ⏎ ### 5.5.3. Sự phù hợp của phương pháp với câu hỏi nghiên cứu ⏎  ⏎ Phương pháp của mỗi câu hỏi đo trực tiếp điều câu hỏi cần biết. RQ1 hỏi mức chênh lệch giữa các cách chia dữ liệu, nên được đo bằng chính các cách chia đó trên cùng dữ liệu và cùng mô hình. RQ2 hỏi mô hình thông tin phát hiện được lỗi nào, nên được đo bằng lỗi chèn mù do một người không tham gia thiết kế đưa vào, trên cùng BIM cho cả ba phương án. RQ3 hỏi chuỗi có vận hành được trên công trình thật hay không, nên được đo bằng một kịch bản đầu cuối và các số… |

## 4. Trích dẫn
Không thêm tài liệu mới. Bảng 5.4 dùng lại các nguồn đã có trong thân bài: [2], [14], [15], [19], [21], [35], [44], [53], [59], [75], [76], `D28DT7CE`, `K5SGFIGW`, `TDRPDWJE`, `G98ZWHKW`, `23TBQTIP`; 3.4.3 dùng [48], `VVBGM9EN`.

## 5. Phát hiện, câu hỏi cho NCS
1. **Mâu thuẫn với tệp 00:** `00_DONG_BO_PIPELINE_VA_PHAN_VUNG_KET_QUA.md` mục 2 ghi "BIM 1:1 là nhà xưởng thật mà khung 1:10 mô phỏng". Theo NCS, hai nhà xưởng khác nhau (Khánh Hòa, Đắk Lắk). Đề nghị sửa tệp 00.
2. **BIM của MT2:** 5.4.2 và Bảng 5.4 ghi "BIM nhà xưởng thật". Đó là BIM nhà xưởng Đắk Lắk (MT3) hay nhà xưởng Khánh Hòa mà mô hình 1:10 mô phỏng? Cần câu trả lời để ghi rõ ở 1.2.4 và 5.4.2.
3. Đoạn 1.8.5 về Consensus mô tả đúng cách làm được ghi trong CLAUDE.md 4.1; NCS xác nhận trước khi chốt khai báo AI tạo sinh.

ĐIỂM DỪNG 2 – T3. Trục kế tiếp: T4 (tách đóng góp khoa học – thực tiễn ở 5.8, bảng đóng góp; bỏ từ tuyệt đối ở 1.1.2, 5.1.3).
