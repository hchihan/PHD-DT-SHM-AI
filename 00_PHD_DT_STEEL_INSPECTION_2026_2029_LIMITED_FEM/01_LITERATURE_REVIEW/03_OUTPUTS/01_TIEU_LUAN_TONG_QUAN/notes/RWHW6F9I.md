# RWHW6F9I — Ramasso, Teloli & Marcel (2025) — [19]

Ramasso E, de O. Teloli R, Marcel R. On the condition monitoring of bolted joints through acoustic emission and deep
transfer learning: generalization, ordinal loss and super-convergence. *Structural Health Monitoring*.
DOI 10.1177/14759217241259668 (thông tin thư mục theo `matrix/doi_chieu_danh_muc.csv`).

**Bản đã đọc:** toàn văn **bản tiền in arXiv 2405.20887v1** (29/05/2024, 26 tr.) trong kho Zotero; trang đầu ghi bài đã
được tạp chí SHM chấp nhận. **Số trang dưới đây là trang của bản tiền in**; chưa đối chiếu với bản in của tạp chí. Đọc ngày
01/10/2026, phiên T1-2. Hình chỉ đọc qua chú thích và lời bàn.

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | RWHW6F9I / [19] |
| Tier / Cụm | Tier 1 / SHM–bu lông–EOV |
| Luận điểm | Phân loại mức lực siết bu lông từ phát xạ âm bằng mạng CNN học chuyển giao đạt độ chính xác rất cao khi huấn luyện và kiểm tra trong cùng đợt đo, nhưng giảm mạnh khi kiểm tra trên một đợt đo chưa thấy (sau tháo – lắp lại), vì mỗi lần lắp lại tạo ra một hệ "mới" (tr. 3, 5, 13–15, 20). |
| Bằng chứng | Bộ dữ liệu chuẩn ORION-AE: hai dầm nhôm nối ba bu lông M4, 5 đợt đo, mỗi đợt bắt đầu sau khi tháo và lắp lại toàn bộ; 7 mức lực siết của bu lông trên; ba cảm biến phát xạ âm (tr. 3–4). So sánh trường hợp cùng đợt ("NO-SHM") với trường hợp để riêng một đợt ("SHM") (tr. 12–15). |
| Giới hạn | Xem mục 5. |
| Tác động K1/K2/K3 | K1: mở rộng (đơn vị suy luận phải là đợt lắp đặt; đánh giá trong cùng đợt cho kết quả lạc quan). K2, K3: không liên quan. |
| Vị trí sử dụng | 3.3 (hiện có); 3.4 (thiết kế đánh giá: tách theo đợt); 3.6 mới (chuyển giao giữa các lần lắp); 1.3A (phạm vi hiệu lực gắn đợt lắp đặt). |
| Mức đã đọc | Toàn văn (bản tiền in arXiv v1) |

## 1. Câu hỏi nghiên cứu và đối tượng

- Hai câu hỏi (tr. 2–3): đặc trưng nào phù hợp để phân loại mức siết; các đặc trưng đó khái quát thế nào qua nhiều đợt đo.
  Trọng tâm là khả năng khái quát.
- Đối tượng: dầm Orion trong phòng thí nghiệm, kích thích 120 Hz bằng máy rung, bu lông trên được nới dần từ 60 cNm xuống
  5 cNm, các bu lông khác giữ 80 cNm (tr. 3–4). Dữ liệu là phát xạ âm tần số cao (lấy mẫu 5 MHz), rất nhiễu (tỷ số tín
  hiệu/nhiễu khoảng 2,3 dB) (tr. 4, 6).

## 2. Phương pháp và kiến trúc thông tin

- Chuỗi xử lý ba khối (tr. 5–8, Hình 3): cắt dòng phát xạ âm theo chu kỳ dao động từ tín hiệu máy đo rung laser; biến đổi
  wavelet liên tục thành ảnh 224×224; phân loại bằng CNN đã huấn luyện trước (GoogLeNet, ResNet18, MobileNetV2,
  EfficientNetB5) (tr. 10–11).
- Xét: khử nhiễu trước hay không; một cảm biến hay gộp ba cảm biến; đóng băng hay tinh chỉnh toàn bộ lớp; bộ lập lịch tốc
  độ học "1cycle"; các hàm mất mát có thứ tự (tr. 7–12).
- Không có kiến trúc thông tin hay chuẩn dữ liệu.

## 3. Cách kiểm chứng

- Dữ liệu thí nghiệm thật, công khai (ORION-AE). Hai thiết kế đánh giá (tr. 12–13):
  - **Cùng đợt (tác giả gọi NO-SHM):** huấn luyện, kiểm định, kiểm tra lấy từ cùng một đợt, chia 80/10/10.
  - **Để riêng một đợt (tác giả gọi SHM):** huấn luyện trên bốn đợt, kiểm tra trên đợt thứ năm.
- Chỉ số: độ chính xác và độ chính xác cho phép lệch một lớp (ACC±1), cùng R, P, F1 tương ứng (tr. 14, 22–23). Kiểm định
  chéo 5 lần khi thêm dần nhãn (tr. 15); lặp 5 lần theo cấu hình (tr. 16, 22).
- Đường cơ sở: cấu hình của Fu và cs. (đóng băng lớp, cùng đợt) (tr. 13–14, Bảng 8).

## 4. Luận điểm chính

1. Mỗi đợt đo bắt đầu sau khi tháo – lắp lại; vi tiếp xúc ở bề mặt không lặp lại cấu hình sau khi tháo lắp, nên dù hình học
   giống nhau, các đợt nên được coi như những hệ khác nhau (quần thể không đồng nhất) (tr. 4–5, 20).
2. Khi toàn bộ điều kiện có mặt trong tập huấn luyện, chuẩn hóa ngầm (lớp chuẩn hóa theo lô) làm kết quả kiểm tra bị thiên
   lệch; nghiên cứu trước dùng thiết kế này là không phù hợp với theo dõi trạng thái (tr. 2, 12).
3. Trong cùng đợt, độ chính xác khoảng 99 %; khi để riêng một đợt, cấu hình cơ sở còn khoảng 26–35 % (chính xác) hay
   52–66 % (lệch một lớp), cấu hình tốt nhất đạt 78,8–86,4 % lệch một lớp (tr. 12–14, 19, Bảng 8, 9).
4. Thêm dần nhãn của đợt kiểm tra (từ 60 cNm xuống 10 cNm), mô phỏng tình huống các đợt kiểm tra định kỳ cho phép gán nhãn
   dữ liệu đã thu, làm độ chính xác tăng; chênh lệch khoảng 15 % giữa hai thiết kế đánh giá ở mỗi đợt (tr. 15).
5. Hàm mất mát có thứ tự cho kết quả tốt và ổn định hơn entropy chéo; hội tụ trong khoảng 3 vòng huấn luyện (tr. 16–19).

## 5. Giới hạn

**(b) Tác giả tự nêu:**
- Nhãn thật không đủ tin cậy vì bất định về vị trí của cờ-lê lực khi đặt mức siết (dùng cờ-lê lực tương tự); vì vậy dùng
  chỉ số cho phép lệch một lớp, là một xấp xỉ có thể gây vấn đề trong một số ứng dụng (tr. 14, 21).
- Hướng tiếp: mã hóa bất định của nhãn vào mạng; thử cảm biến dải tần cao hơn (tr. 21).
- Các thử nghiệm cấu hình chỉ làm trên đợt #B rồi áp cho các đợt khác (tr. 15, 18).

**[NCS] nhận định:**
- Mẫu nhôm nhỏ, bu lông M4, một bu lông được nới, phòng thí nghiệm; không có tải vận hành, nhiệt độ, nhiễu công trường.
- Nhãn là mức siết đặt trước theo thứ tự giảm dần; thời gian và mức siết đi cùng nhau, có thể lẫn với trôi theo thời gian
  trong đợt (bài không bàn).
- Bản đọc là tiền in; số liệu cần đối chiếu bản in trước khi trích.

## 6. Điều bài KHÔNG xử lý, xét theo chuỗi của luận án

| Ý | Mức | Căn cứ |
|---|---|---|
| Nguồn gốc bằng chứng cảm biến | xử lý một phần (ở mức thí nghiệm) | Mô tả đầy đủ cảm biến, lấy mẫu, chuỗi xử lý, cấu hình mạng (tr. 3–12); không có bản ghi, phiên bản |
| Phạm vi hiệu lực của bằng chứng | xử lý một phần | Tách rõ hai thiết kế đánh giá và chỉ ra kết quả trong cùng đợt không khái quát sang đợt mới (tr. 12–15); không phát biểu thành phạm vi của từng kết quả |
| Quan hệ bằng chứng – cấu kiện có thời hạn | không xử lý | Không có. Ý liên quan: mỗi lần lắp lại là một hệ mới (tr. 5) |
| Trách nhiệm, thẩm quyền | không xử lý | Không có |
| Trạng thái hành động và lịch sử chuyển trạng thái | không xử lý | Không có |
| Truy ngược từ hành động về dữ liệu gốc | không xử lý | Không có. Ý liên quan: nhãn từ kiểm tra định kỳ (tr. 15) |

## 7. Tác động tới K1/K2/K3

- **K1: mở rộng.** Thiết kế đánh giá quyết định mức tin được của kết quả: cùng đợt khoảng 99 %, đợt mới thấp hơn nhiều
  (tr. 13–14); tác giả coi mỗi lần lắp lại là hệ mới (tr. 5). [NCS] Đơn vị suy luận và cách chia dữ liệu phải được ghi
  trong phạm vi hiệu lực. Tài liệu thuộc nhóm 2025 (bản in).
- **K2, K3: không liên quan.** Gợi ý cho vòng lặp kiểm tra tạo nhãn: nhãn từ kiểm tra định kỳ (tr. 15) và bất định của nhãn (tr. 21).

## 8. Vị trí sử dụng trong tiểu luận v2

- 3.3/3.4: thiết kế đánh giá để riêng đợt đo; thiên lệch khi mọi điều kiện có trong huấn luyện.
- 3.6 mới: khó chuyển giao giữa các lần lắp; vai trò của nhãn từ kiểm tra.
- 1.3A: ví dụ vì sao phạm vi hiệu lực ghi đợt lắp đặt.
- Dẫn số liệu theo bản in sau khi đối chiếu; ghi rõ đối tượng là dầm nhôm thí nghiệm.
