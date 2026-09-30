# Nhật ký ứng viên khoảng trống — Giai đoạn 2

Tạo ngày 30/09/2026 (phiên T1-3). Đây là nhật ký **làm việc**; khoảng trống chỉ được chốt ở Giai đoạn 3 (Điểm duyệt 3).
Mọi ứng viên là giả thuyết, chưa phải kết luận.

Quy ước:
- **K1** = xác lập chất lượng và phạm vi hiệu lực của bằng chứng trạng thái; **K2** = bảo toàn chất lượng bằng chứng
  trong truy vết cấp cấu kiện; **K3** = từ bằng chứng đến hành động (theo mục 5.2 của bản gốc). Đây là các giả thuyết
  làm việc.
- Căn cứ được đếm là **độc lập** khi thuộc các nhóm tác giả khác nhau và đã được đọc toàn văn hoặc đúng phần liên quan.
  Ngưỡng của Giai đoạn 3: mỗi khoảng trống cần từ 3 căn cứ, trong đó không thuộc nhóm 2025–2026 (CLAUDE.md 4.1).
- Loại căn cứ: **TG** = tác giả tự nêu; **NCS** = nhận định của NCS từ việc bài không xử lý một ý; ghi rõ khi lẫn.
- Nguồn đã đọc toàn văn đến hết phiên T1-3: [8], [7], [3] (30/09/2026). Phiên T1-1 (ba tiền lệ [2], [35], [44]) **chưa
  thực hiện**; căn cứ từ ba bài đó sẽ được bổ sung khi có. Căn cứ đã dùng ở 5.6A (Bull 2022, Wang & Cha 2021, [57],
  Hughes 2022, Figueiredo 2011) chưa được đưa vào nhật ký; cần rà lại ở phiên Tier 2.

## Bảng tóm tắt

| Mã | Phát biểu | K | Số căn cứ độc lập hiện có | Năm các căn cứ | Ghi chú |
|---|---|---|---|---|---|
| UV-01 | Chuỗi từ cảnh báo đến hành động không được ghi thành trạng thái xử lý có truy vết trong các khung song sinh số cho công trình | K3 | 2 ([3], [7]) | 2020, 2020 | Chưa đủ; cần [35], [44], [16], [17] |
| UV-02 | Đầu ra phát hiện bất thường trong khung song sinh cho công trình chưa được ghi cùng nguồn gốc xử lý, phiên bản phương pháp và phạm vi hiệu lực | K1 | 2 ([3], [7]) | 2020, 2020 | Chưa đủ; cần [18], [45], 23TBQTIP |
| UV-03 | Gắn dữ liệu cảm biến với đối tượng BIM chưa kèm thời hạn hiệu lực và lịch sử thay đổi ghép | K2 | 2 ([3], [7]) | 2020, 2020 | Chưa đủ; cần [2], [35] |
| UV-04 | Thiếu phân loại mức tích hợp DM/DS/DT áp cho kiểm tra – bảo trì kết cấu công trình có con người ra quyết định | mới (định vị) | 2 ([8], [7]) | 2018, 2020 | Chỉ phục vụ định vị ở 2.3, không dự kiến thành khoảng trống |
| UV-05 | Ở công trình đang vận hành thiếu dữ liệu có nhãn về bất thường; nhãn phụ thuộc đánh giá con người | mới (nhãn hiện trường; liên quan L2.3, 5.6A) | 1 ([3]) | 2020 | Căn cứ đã có ở 5.6A chưa nhập nhật ký |

## UV-01 — Chuỗi cảnh báo → hành động

- **Phát biểu:** Trong các khung song sinh số đã đọc, chuỗi từ phát hiện bất thường đến hành động bảo trì dừng ở cảnh
  báo và hỗ trợ quyết định của con người, không được ghi thành trạng thái xử lý và lịch sử chuyển trạng thái có thể
  truy ngược.
- **Căn cứ:**
  - Lu và cs. 2020 [3], tr. 6 (Hình 4: kết thúc ở báo cáo – sửa chữa), tr. 13–14 (mục đích là hỗ trợ quyết định; Hình 18
    chỉ hiển thị cảnh báo), tr. 5–6 (chỉ ra IFC4 thiếu giá trị `IfcChangeActionEnum` cho FM và đề xuất
    `IfcInspectionHistory`, `IfcMaintenanceHistory`, nhưng ca nghiên cứu không dùng chúng).
  - Boje và cs. 2020 [7], tr. 12 (cảnh báo và khuyến nghị "cần người dùng xác nhận và cho phép"; không nêu mô hình ghi lại
    xác nhận), tr. 10 (Bảng 2: "chấp hành" là một khả năng, không có trạng thái hành động).
- **Loại căn cứ:** TG một phần ([3] tr. 5 tự nêu IFC4 thiếu thực thể; [7] tr. 12 tự nêu cần kiểm chứng AI trước khi
  chuyển tác vụ) + **NCS** (việc chuỗi không có trạng thái xử lý là suy từ phần bài không mô tả).
- **Liên quan:** K3.
- **Ghi chú:** đối tượng của [3] là bơm HVAC, của [7] là công trường thi công; không trực tiếp là kết cấu thép vận hành.

## UV-02 — Nguồn gốc, phiên bản phương pháp, phạm vi hiệu lực của đầu ra phát hiện

- **Phát biểu:** Đầu ra phát hiện bất thường và dự đoán trong các khung song sinh số công trình chưa được ghi như một
  bản ghi có nguồn gốc xử lý, phiên bản phương pháp và phạm vi hiệu lực.
- **Căn cứ:**
  - [3], tr. 5 (Hình 3: dữ liệu thô có Sensor_ID, Sensor_Timestamp), tr. 13–14 (đầu ra là điểm thay đổi và cảnh báo hiển
    thị; không mô tả phiên bản thuật toán, tham số hay điều kiện áp dụng). Đối chiếu ngữ cảnh vận hành để lọc điểm thay
    đổi (tr. 6) là xử lý một phần.
  - [7], tr. 9 (độ tin cậy dữ liệu nguồn là mối quan ngại; cần phân biệt dữ liệu cảm biến thật và mô phỏng; tính hợp lệ
    của dự đoán cần kiểm chứng), tr. 11 (kiểm chứng tính đúng và đủ của dữ liệu còn khó). Tìm trong văn bản: không có
    provenance, traceability, accountability, audit.
- **Loại căn cứ:** TG ([7] tr. 9, 11) + **NCS** (không có cơ chế ghi nguồn gốc/phạm vi là suy từ phần bài không xử lý).
- **Liên quan:** K1.
- **Ghi chú:** cần đối chiếu với [18], [45], Figueiredo 2011 (Tier 2) về phạm vi hiệu lực phụ thuộc điều kiện huấn luyện.

## UV-03 — Ghép cảm biến – cấu kiện có thời hạn

- **Phát biểu:** Việc gắn dữ liệu cảm biến với đối tượng BIM, khi có, được thực hiện bằng bảng ghép hoặc tương đương
  mà không có thời hạn hiệu lực và lịch sử thay đổi ghép.
- **Căn cứ:**
  - [7], tr. 7 (các nghiên cứu cảm biến trong xây dựng **không xử lý việc căn chỉnh dữ liệu cảm biến với chính mô hình BIM**),
    tr. 2 (dữ liệu từ nhiều nguồn phải được đối chiếu với BIM ở mức đối tượng và nhất quán theo thời gian).
  - [3], tr. 6, 10 (Hình 7, 11: bảng ghép GUID ↔ ID nguồn dữ liệu; chỉ bảng ghép cần bảo trì); không nêu thời hạn hiệu
    lực hoặc cách xử lý khi cảm biến được thay hay dời.
- **Loại căn cứ:** TG ([7] tr. 7 tự nêu chưa giải quyết) + **NCS** (không thời hạn hiệu lực là suy từ [3]).
- **Liên quan:** K2.
- **Ghi chú:** [3] là **tiền lệ** cho việc ghép; điểm còn thiếu là thời hạn và lịch sử. Cần đối chiếu [2] (IFC Monitor),
  [35] ở phiên T1-1 trước khi coi đây là khoảng trống.

## UV-04 — Định vị mức tích hợp DM/DS/DT cho kiểm tra – bảo trì

- **Phát biểu:** Chưa có phân loại mức tích hợp DM/DS/DT gắn với các khung có con người ra quyết định cho kiểm tra –
  bảo trì kết cấu công trình.
- **Căn cứ:**
  - Kritzinger và cs. 2018 [8], tr. 1020 (chưa có định nghĩa chung; cần mô hình tham chiếu theo lĩnh vực và các ca nghiên
    cứu); phạm vi bài là sản xuất (tr. 1018).
  - [7], tr. 12–13 (thang ba thế hệ cho song sinh số xây dựng, thế hệ 2 có xác nhận của người dùng).
- **Loại căn cứ:** TG ([8] tr. 1020) + **NCS** (việc chưa có phân loại cho kiểm tra – bảo trì kết cấu là suy từ phạm vi hai bài).
- **Liên quan:** mới, chỉ phục vụ **định vị** (mục 2.3 và câu khai báo mức DS ở Dẫn nhập). **[NCS]** Không nên phát triển
  thành khoảng trống của luận án: đây là câu hỏi khái niệm, không phải điều luận án kiểm chứng.

## UV-05 — Thiếu nhãn hư hỏng ở hiện trường

- **Phát biểu:** Ở công trình đang vận hành, khó có dữ liệu có nhãn về bất thường; phân biệt bình thường – bất thường phụ
  thuộc nhiều vào đánh giá của con người, nên nhãn cần đến từ kiểm tra.
- **Căn cứ:** [3], tr. 2 (dữ liệu có nhãn tốt thường không sẵn có ở môi trường xây dựng), tr. 3 (khó phân biệt điều
  kiện bình thường và bất thường, hiện phụ thuộc đánh giá của con người), tr. 13 (huấn luyện bộ phân loại một lớp cần dữ
  liệu lớn ở nhiều điều kiện bình thường, không thực tế).
- **Loại căn cứ:** TG.
- **Liên quan:** mới (nhãn hiện trường, vòng lặp kiểm tra tạo nhãn). Trong GD1 đây là luận điểm L2.3 ("thiếu dữ liệu hư
  hỏng có nhãn ở hiện trường"), đã có nguồn ở 5.6A (Bull 2022, Wang & Cha 2021, [57]) mà chưa đưa vào nhật ký này.
- **Ghi chú:** đối tượng của [3] là bơm HVAC; chỉ dùng như căn cứ cùng chiều.
