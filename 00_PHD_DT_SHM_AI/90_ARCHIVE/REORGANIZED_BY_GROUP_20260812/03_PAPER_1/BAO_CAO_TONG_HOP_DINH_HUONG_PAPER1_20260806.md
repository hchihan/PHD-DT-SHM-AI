# BÁO CÁO TỔNG HỢP ĐỊNH HƯỚNG PAPER 1

**Thuộc:** RQ1 – WP1 – Chương 4 – Paper 1 – Gate 1  
**Trạng thái hiện tại:** Gate 1 đang mở, bằng chứng một phần  
**Mục tiêu báo cáo:** Trình bày trung thực kết quả đã có, ý nghĩa khoa học của kiểm tra liên campaign và kế hoạch hoàn thiện Paper 1.

---

## Slide 1 — Paper 1 đang trả lời câu hỏi gì?

### Mục tiêu nghiên cứu

Đánh giá mức độ tin cậy của dữ liệu dao động trong việc phân biệt các trạng thái liên kết trên mô hình khung thép 1:10 dưới quy trình đánh giá run-aware và chống rò rỉ dữ liệu.

### Dữ liệu hiện có

- 3 đợt thí nghiệm.
- 4 trạng thái × 3 dạng kích thích × 6 lần lặp.
- Tổng 216 bản ghi.
- Đã xây dựng run registry 216/216.
- Đã kiểm toán chất lượng và provenance dữ liệu.
- Đã tách dữ liệu theo lần đo trước khi cắt cửa sổ.
- Tiền xử lý chỉ được khớp trên tập huấn luyện.

### Thông điệp chính

Paper 1 không nhằm tìm “mô hình AI tốt nhất”, mà kiểm tra liệu bằng chứng trạng thái có đáng tin cậy, có thể lặp lại và có khả năng khái quát hóa hay không.

### Gợi ý hình minh họa

```text
Dữ liệu dao động
→ Tách theo run
→ Đánh giá leakage-safe
→ Condition evidence
```

---

## Slide 2 — Kết quả đã đạt được

### Trong từng campaign

- Đã chạy các mô hình nền: Logistic Regression, SVM và Random Forest.
- Đã thực hiện đánh giá LORO theo từng lần đo.
- Một số cấu hình cho khả năng phân biệt trạng thái tương đối tốt.
- Kết quả thay đổi giữa các fold và giữa các campaign.
- Các kết quả này hiện vẫn là kết quả sơ bộ, chưa phải kết quả cuối cùng.

### Giữa các campaign

- Đã thực hiện đánh giá LOCO giữa các đợt thí nghiệm.
- Mô hình huấn luyện trên các campaign trước không hoạt động tốt trên campaign độc lập.
- Hiệu năng của nhiều họ mô hình ở mức hoặc dưới ngưỡng ngẫu nhiên.
- Kiểm định hoán vị cho thấy kết quả liên campaign không thể được diễn giải như khả năng khái quát hóa đáng tin cậy.

### Thông điệp chính

Kết quả tốt trong cùng một campaign chưa đủ chứng minh mô hình có thể áp dụng cho một đợt đo độc lập.

### Gợi ý hình minh họa

| Phạm vi đánh giá | Kết quả hiện tại | Ý nghĩa |
|---|---|---|
| Within-campaign LORO | Có khả năng phân biệt trong một số cấu hình | Repeatability sơ bộ |
| Cross-campaign LOCO | Suy giảm mạnh | Chưa có reproducibility |

---

## Slide 3 — Phát hiện khoa học quan trọng nhất

### Phát hiện

Mô hình có thể đang học đồng thời:

```text
Đặc trưng trạng thái
+ đặc trưng riêng của campaign
+ nhiễu thu nhận dữ liệu
```

### Ý nghĩa khoa học

- Tồn tại domain shift rõ giữa các đợt thí nghiệm.
- Điều kiện thu nhận dữ liệu có thể ảnh hưởng mạnh đến kết quả phân loại.
- Metric cao trong cùng campaign có thể phản ánh một phần dấu hiệu riêng của campaign.
- Nhiều kiến trúc mô hình cùng suy giảm cho thấy vấn đề không chỉ nằm ở lựa chọn thuật toán.
- Giá trị của Paper 1 nằm ở việc xác định ranh giới độ tin cậy, không chỉ ở một con số hiệu năng cao.

### Thông điệp chính

Paper 1 có thể đóng góp một khung đánh giá hai tầng: repeatability trong campaign và reproducibility giữa các campaign.

### Gợi ý hình minh họa

```text
Campaign A ── huấn luyện ──> tốt trên Campaign A
Campaign A ── kiểm tra  ──> suy giảm trên Campaign B/C
                               ↓
                        Domain shift
```

---

## Slide 4 — Vai trò của tháo–lắp và định danh cảm biến

### Giả thuyết nguyên nhân

Việc tháo và lắp lại cảm biến giữa các đợt có thể làm thay đổi:

- hướng và dấu của các trục đo;
- vị trí thực tế;
- độ tiếp xúc giữa cảm biến và kết cấu;
- đặc điểm dây dẫn và nhiễu nền;
- offset hoặc hệ số khuếch đại;
- sự tương ứng giữa cột dữ liệu và cảm biến vật lý;
- điều kiện kích thích và môi trường đo.

### Bằng chứng hỗ trợ hiện có

- Campaign 1 và 2 có vấn đề định danh cảm biến.
- Campaign 3 có dấu vân tay cảm biến ổn định hơn.
- Kết quả liên campaign suy giảm trên nhiều mô hình.

### Giới hạn tuyên bố

Chưa đủ bằng chứng để khẳng định tháo–lắp cảm biến là nguyên nhân duy nhất.

Cách diễn đạt phù hợp:

> Có dấu hiệu rõ về domain shift giữa các campaign, nhiều khả năng liên quan đến điều kiện tái lắp đặt, hướng trục và định danh cảm biến.

### Thông điệp chính

Đây là kết quả âm tính có giá trị khoa học, không phải thí nghiệm thất bại.

### Gợi ý hình minh họa

```text
Tháo–lắp cảm biến
→ thay đổi điều kiện đo
→ đặc trưng campaign
→ giảm khả năng khái quát hóa
```

---

## Slide 5 — Đóng góp dự kiến của Paper 1

### Đóng góp 1 — Đánh giá leakage-safe và run-aware

- Tách dữ liệu theo run trước khi cắt cửa sổ.
- Tiền xử lý chỉ trên tập huấn luyện.
- Không dùng random window split.

### Đóng góp 2 — Phân biệt repeatability và reproducibility

- LORO đánh giá run chưa thấy trong cùng campaign.
- LOCO đánh giá campaign độc lập sau tái lắp đặt cảm biến.

### Đóng góp 3 — Chỉ ra ảnh hưởng của điều kiện thu nhận dữ liệu

- Cấu hình và provenance cảm biến có thể quan trọng hơn việc tăng độ phức tạp của AI.
- Quản trị Sensor_ID là điều kiện để tạo condition evidence đáng tin cậy.

### Đóng góp 4 — Báo cáo trung thực giới hạn khái quát hóa

- Không che giấu kết quả liên campaign thấp.
- Xác định điều kiện biên của tính hợp lệ.
- Đưa ra yêu cầu cho thiết kế thí nghiệm và triển khai hiện trường sau này.

### Thông điệp chính

Giá trị khoa học của Paper 1 nằm ở thiết kế đánh giá, quản trị dữ liệu và ranh giới bằng chứng.

---

## Slide 6 — Công việc bắt buộc để đóng Gate 1

1. Khóa run registry.
2. Gán lại định danh cảm biến Campaign 1 và 2.
3. Chạy lại các cấu hình bị ảnh hưởng.
4. Hoàn thành LORO đa hạt giống.
5. Báo cáo độ bất định theo fold và run.
6. Xác minh sensor mode và provenance của ResNet1D.
7. Loại ResNet1D nếu không xác minh được.
8. Hoàn thành ma trận chấp nhận Gate 1 và ký xác nhận.
9. Chỉ sau đó mới khóa kết quả và hoàn thiện bản thảo Paper 1.

### Trạng thái bằng chứng

| Nội dung | Trạng thái |
|---|---|
| Ba campaign, 216 bản ghi | Đã kiểm chứng |
| Run registry | Đã dựng, chưa khóa |
| LORO mô hình nền | Có, còn cần đa hạt giống |
| LOCO liên campaign | Đã có kết quả |
| Định danh cảm biến C1–C2 | Chưa giải quyết hoàn toàn |
| ResNet1D | Bằng chứng chưa đủ |
| Gate 1 | Chưa đóng |

### Thông điệp chính

Ưu tiên hiện tại không phải chạy thêm nhiều mô hình, mà là khóa provenance, định danh cảm biến và độ tin cậy của kết quả.

---

## Slide 7 — Ranh giới tuyên bố của Paper 1

### Có thể tuyên bố sau khi Gate 1 được đóng

- Dữ liệu dao động có thể tạo bằng chứng phân biệt các trạng thái liên kết có kiểm soát trong điều kiện phòng thí nghiệm.
- Quy trình run-aware giúp hạn chế rò rỉ dữ liệu.
- Kết quả trong cùng campaign không bảo đảm khả năng khái quát hóa sang campaign khác.
- Điều kiện thu nhận và cấu hình cảm biến ảnh hưởng đáng kể đến kết quả.
- Cross-campaign evaluation là cần thiết để đánh giá reproducibility.

### Không được tuyên bố

- Chẩn đoán hư hỏng hiện trường.
- Chuyển mô hình từ khung 1:10 sang công trình thực.
- Tháo–lắp cảm biến là nguyên nhân duy nhất.
- ResNet1D là mô hình tốt nhất khi provenance chưa được xác minh.
- AI có khả năng áp dụng tổng quát.
- Gate 1 đã hoàn thành khi chưa có ma trận chấp nhận.

### Kết luận báo cáo

Paper 1 vẫn khả thi và có giá trị khoa học, nhưng hướng đóng góp cần chuyển từ “đạt độ chính xác cao” sang:

> Đánh giá run-aware, kiểm soát rò rỉ, phân biệt repeatability–reproducibility và xác định giới hạn khái quát hóa do domain shift giữa các campaign.

---

## Tên Paper 1 dự kiến

**Run-Aware Evaluation of Low-Cost Sensor Configurations for Vibration-Based Condition Classification of a Scaled Bolted Steel Frame**

---

## Prompt ngắn cho NotebookLM

Dựa trên file này và các tài liệu nguồn đã tải lên, hãy tạo 6–7 slide báo cáo riêng về Paper 1 để trình bày với thầy hướng dẫn. Tập trung vào: mục tiêu RQ1, dữ liệu 3 campaign, kết quả within-campaign và cross-campaign, ý nghĩa khoa học của domain shift, ảnh hưởng tiềm năng của tháo–lắp và định danh cảm biến, đóng góp dự kiến của Paper 1, kế hoạch đóng Gate 1 và ranh giới tuyên bố. Văn phong đơn giản, mỗi slide một thông điệp chính, ưu tiên sơ đồ, bảng so sánh và timeline. Không dùng metric cũ chưa xác minh, không trình bày ResNet1D như kết quả hoàn chỉnh, không tuyên bố Gate 1 đã đóng và không khẳng định tháo–lắp cảm biến là nguyên nhân duy nhất.
