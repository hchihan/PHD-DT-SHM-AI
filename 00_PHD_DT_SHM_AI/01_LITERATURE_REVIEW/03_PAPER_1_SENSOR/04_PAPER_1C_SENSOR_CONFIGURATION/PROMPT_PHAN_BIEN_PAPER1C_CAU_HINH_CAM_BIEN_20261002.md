# PROMPT – Phản biện, thiết kế lại và tìm đóng góp tốt nhất cho Paper 1C
## "Tác động của số lượng và tổ hợp cảm biến (1, 2, 3) lên các mô hình AI, qua ba đợt đo"

> Dùng cho Claude Code tại thư mục gốc luận án `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM`. Nên bật Zotero MCP.
> Lập ngày 02/10/2026.
> Văn bản dùng chung:
> - "tệp 00": `00_DONG_BO_PIPELINE_VA_PHAN_VUNG_KET_QUA.md` (v1.1)
> - `CLAUDE.md`
> - "1B": `PROMPT_PHAN_BIEN_PAPER1B_ON_DINH_QUYET_DINH_20261002.md` (bài anh em)
> - "Bài 1": `PROMPT_PHAN_BIEN_PAPER1_Q1_20261002.md`

---

## 1. Bài đang xét

**Ý định của NCS (02/10/2026):** đánh giá tác động lên các mô hình AI khi dùng cấu hình 1, 2 và 3 cảm biến, cho cả ba đợt đo. Bài dùng cùng dữ liệu với Bài 1 và 1B nhưng khác đóng góp và câu chuyện.

**Bản thảo cũ (TG):** `PAPER_DRAFTING/Q3_Paper3_Sensor_Configuration (10.06).docx`, kèm `04_PAPER_1B_SENSOR_CONFIGURATION/P1SC_*.docx`.
- Dữ liệu: 72 bản ghi, S1, S2, S12; 1 kênh mỗi cảm biến; cửa sổ 1.024/256.
- Mô hình và đánh giá: RF, SVM, LR, 1D-CNN; một lần chia cố định; chấm theo cửa sổ.
- Có DSI coi nhãn là có thứ tự; khẳng định tương tự động lực học.
- **Giao thức này không còn dùng được.** Phải thiết kế lại theo pipeline chuẩn. Bản cũ chỉ là nguồn ý tưởng và văn bản.

**Ràng buộc vật lý của dữ liệu (tệp 00, mục 2):**
- **CP1 chỉ có S1, S2.** S3 chỉ có ở CP2, CP3.
- Vì vậy "1, 2, 3 cảm biến cho cả 3 đợt" chỉ làm được như sau:
  - so sánh **qua ba đợt** trên {S1, S2, S12} (1 và 2 cảm biến);
  - cấu hình có S3 (S3, S13, S23, S123) chỉ ở CP2, CP3.
- Thiết kế phải nói rõ điều này ngay ở phần dữ liệu.

**Cảnh báo đã có:** khối tập con ngày 07/09 (ResNet1D, 17 cấu hình × 30 lần chia, một seed) **không tách được** hiệu ứng cấu hình khỏi nhiễu fold ở CP2, CP3. Câu "cấu hình chi phối hơn thuật toán" chưa có căn cứ và đang chờ thầy quyết (C-02 trong `01_CURRENT_CONTROL/PAPER1_SCIENCE_LOCK_PROJECT_SYNC_REPORT_20260913.md`). Thiết kế mới phải có đủ seed và suy luận theo khối để trả lời được câu này. Kết quả có thể là "không phân biệt được"; đó vẫn là kết quả hợp lệ nếu được thiết kế để kiểm.

---

## 2. Vai trò

Bạn là **hội đồng phản biện** kiêm **người thiết kế thí nghiệm tính toán**. Giọng gắt, có căn cứ, chỉ mục cụ thể.

| Mã | Vai | Soi |
|---|---|---|
| R1 | SHM, thiết kế hệ quan trắc | Ý nghĩa thực tế của "bớt hay thêm cảm biến" cho nhà xưởng; khoảng cách cảm biến – vị trí can thiệp (S1–B1, S2–B2, S3–B3) |
| R2 | Học máy | Công bằng giữa họ mô hình (siêu tham số, số seed, số chiều đầu vào thay đổi theo cấu hình); mô hình học sâu với dữ liệu nhỏ |
| R3 | Thống kê, thiết kế thí nghiệm | Thiết kế giai thừa mô hình × cấu hình × đợt; hiệu ứng tương tác; suy luận theo khối run; so sánh nhiều lần |
| R4 | Đóng góp, định vị | So với tài liệu bố trí, chọn cảm biến và so sánh mô hình trong SHM; ranh giới với Bài 1 và 1B |
| ED | Biên tập viên | Tổng hợp; quyết định câu chuyện; điều kiện để nộp |

Báo cáo cho NCS viết tiếng Việt. Bản nộp viết tiếng Anh.

---

## 3. Ràng buộc

1. **Pipeline chuẩn (tệp 00, mục 3):**
   - cửa sổ 400/200; chuẩn hóa theo từng cửa sổ;
   - 25 đặc trưng mỗi kênh + quan hệ theo cặp kênh; 4 kênh mỗi cảm biến;
   - chấm theo bản ghi;
   - LORO trong từng đợt; khi so giữa các đợt dùng LOCO trên cấu hình có ở cả hai đợt;
   - ≥ 5 seed cho mọi mô hình;
   - siêu tham số chọn trong vùng không chứa run kiểm thử (CV lồng nhau), hoặc cố định trước cho mọi cấu hình.
2. **Bốn mô hình chuẩn:** RF, SVM-RBF, 1D-CNN, ResNet1D. LR chỉ là mốc tham chiếu tùy chọn.
3. **Nhãn S0, B1, B2, B3 không có thứ tự.** Bỏ DSI có thứ tự. Không khẳng định tương tự động lực học.
4. **Sở hữu kết quả (tệp 00 v1.1, mục 5):**
   - **1C sở hữu R7:** tương tác cấu hình (1, 2, 3 cảm biến) × mô hình AI qua ba đợt; mức giữ hiệu năng và lợi ích biên theo họ mô hình; khuyến nghị số cảm biến tối thiểu theo họ mô hình.
   - **Không sở hữu R2 (Bài 1):** hiệu năng 4 mô hình ở cấu hình đầy đủ (S12 ở CP1; S123 ở CP2, CP3). Các số này trích Bài 1; 1C chỉ dùng làm điểm mốc.
   - **Không sở hữu R4 (Bài 1):** LOCO trên S12. Nếu 1C cần so qua đợt trên S12, trích Bài 1. Phần mới của 1C là LOCO trên S1, S2 theo từng mô hình.
   - **Không sở hữu R6 (1B):** regret và ổn định quyết định chọn cấu hình của RF trên CP2, CP3. Số RF trên 7 tập con ở CP2, CP3 trích 1B. Phần mới của 1C là các mô hình khác và tương tác.
   - Thấy cần đổi ranh giới thì ghi **đề xuất đổi ma trận** kèm lý do, chờ NCS duyệt.
5. Câu "cấu hình chi phối hơn thuật toán" chỉ được dùng nếu phân tích đã khóa trước cho thấy điều đó và thầy đã duyệt C-02.
6. Không bịa số, trích dẫn, DOI. Hạng tạp chí phải kiểm có nguồn và ngày truy cập; không kiểm được thì `[CẦN KIỂM]`. Mọi lần chạy chỉ sau khi giao thức được commit.
7. Không sửa tệp gốc. Sản phẩm ghi vào `03_PAPERS/PAPER_1C/review_YYYYMMDD/` (đường dẫn: [NCS XÁC NHẬN]).

---

## 4. Câu hỏi phản biện bắt buộc (tự trả lời ở Pha 1)

1. **Hiệu ứng trần.** Ở CP1 và CP2, RF, SVM đạt gần 1,0 với cấu hình đầy đủ (Bài 1). Còn chỗ để thấy tác động của cấu hình không? Hay chỉ thấy được ở CP3 và ở mô hình học sâu? Thiết kế có phải dựa vào đợt "khó" hay không?
2. **Khoảng cách cảm biến – can thiệp.** Bớt S3 có làm mất khả năng nhận B3 (giằng) không? Nếu có, kết quả là về "số cảm biến" hay về "phủ vị trí"? Phân tích theo trạng thái (recall từng lớp) phải trả lời câu này.
3. **Số chiều đầu vào.** Từ 1 lên 3 cảm biến, số chiều đặc trưng tăng 106 → 366, và đầu vào học sâu tăng 4 → 12 kênh. Hiệu ứng "thêm cảm biến" có lẫn với hiệu ứng "thêm chiều" không? Cần một kiểm soát (ví dụ số đặc trưng bằng nhau).
4. **Công bằng giữa mô hình.** Bài 1 có vấn đề siêu tham số học sâu chọn trên vùng chứa run kiểm thử (15/18 fold). 1C phải tránh từ đầu.
5. **Đơn vị suy luận.** Với 6 run mỗi đợt, tương tác mô hình × cấu hình có vượt nhiễu fold và seed không? Đây là chỗ khối 07/09 thất bại. Cần mô hình hiệu ứng hỗn hợp, hoặc bootstrap theo khối run.
6. **"So what".** Người thiết kế hệ quan trắc nhà xưởng rút ra được câu nào? Ví dụ: "với mô hình đặc trưng thủ công, một cảm biến ở vị trí X giữ được ≥ Y % hiệu năng; mô hình học sâu cần ≥ 2 cảm biến". Câu đó có đứng được qua cả ba đợt không?

---

## 5. Hướng đóng góp cần đánh giá (Pha 2)

Đánh giá từng hướng theo: độ mới, độ chắc với dữ liệu hiện có, công sức, độ khớp với luận án, mức tách khỏi Bài 1 và 1B.

| # | Câu chuyện | Phần mới có thể tuyên bố |
|---|---|---|
| E1 | **Tương tác mô hình × cấu hình:** họ mô hình nào nhạy với số cảm biến, nhạy đến đâu | Bảng/đồ thị tương tác có độ bất định qua ba đợt |
| E2 | **Mức giữ hiệu năng và lợi ích biên:** thêm cảm biến thứ hai, thứ ba được bao nhiêu, theo họ mô hình và theo đợt | Đường cong retention có KTC; số cảm biến tối thiểu theo ngưỡng giữ hiệu năng |
| E3 | **Phủ vị trí so với số lượng:** tác động của cấu hình lên từng trạng thái theo vị trí can thiệp | Tách "bao nhiêu cảm biến" khỏi "đặt ở đâu"; khuyến nghị bố trí có điều kiện |
| E4 | **Tính bền của khuyến nghị cấu hình qua ba đợt và hai mức đánh giá** (trong đợt / giữa đợt), theo từng mô hình | Mở rộng câu hỏi của 1B sang nhiều mô hình mà không lặp regret của RF; cần kiểm ranh giới với 1B |
| E5 | **Chi phí – hiệu năng:** số cảm biến × hiệu năng × độ bất định, trình bày như đường biên Pareto cho thiết kế | Hướng thực tiễn cho quản lý tài sản; chỉ dùng số cảm biến, không bịa đơn giá |

Đề xuất câu chuyện chính (gợi ý cân nhắc: E1 + E2, với E3 làm phần giải thích), tiêu đề, ba đóng góp. Nói rõ vì sao câu chuyện đó không trùng 1B (quyết định, regret, RF) và Bài 1 (giao thức, cấu hình đầy đủ).

---

## 6. Quy trình – dừng ở mỗi ĐIỂM DỪNG

**Pha 0 – Kiểm kê (không nhận xét).**
- Liệt kê mọi tệp liên quan: bản thảo cũ, outline P1SC, khối tập con 07/09, mã và kết quả hiện có.
- Lập ma trận dữ liệu khả dụng: đợt × cấu hình × số bản ghi × số run. Ghi rõ ô nào không tồn tại (S3 ở CP1).
- Liệt kê kết quả đã có thể dùng lại, và ai sở hữu theo tệp 00.
- **Sản phẩm:** `P1C_0_kiem_ke_YYYYMMDD.md`. → **ĐIỂM DỪNG 0**

**Pha 1 – Phản biện bản cũ và ý định mới.**
- R1–R4: phần nào của bản cũ giữ được (văn bản, ý tưởng); phần nào bỏ (giao thức, DSI, tương tự động lực học, tuyên bố bộ dữ liệu).
- R1–R4 trả lời mục 4.
- ED xếp mức Chặn / Nặng / Nhẹ.
- **Sản phẩm:** `P1C_1_phan_bien_YYYYMMDD.md`. → **ĐIỂM DỪNG 1**

**Pha 2 – Định vị đóng góp và câu hỏi nghiên cứu.**
- Đánh giá E1–E5. Đề xuất câu chuyện chính; RQ (2–3 câu); giả thuyết có thể bác bỏ; tiêu đề tiếng Anh (2–3 phương án); ba đóng góp.
- Kiểm tài liệu gần nhất. Tìm thêm thì ghi nhật ký truy vấn; `[CHƯA ĐỌC TOÀN VĂN]` khi cần.
- **Sản phẩm:** `P1C_2_dinh_vi_dong_gop_YYYYMMDD.md`. → **ĐIỂM DỪNG 2** (NCS chọn câu chuyện)

**Pha 3 – Giao thức thí nghiệm tính toán (khóa trước khi chạy).**
- Thiết kế giai thừa: mô hình (4) × cấu hình (CP1: 3; CP2, CP3: 7) × đợt (3) × seed (≥ 5) × fold (LORO 6), cùng LOCO cho {S1, S2, S12}.
- Ước tính số lần huấn luyện và thời gian chạy.
- Kiểm soát số chiều đặc trưng (ít nhất một biến thể).
- Chọn siêu tham số theo CV lồng nhau, hoặc cố định trước.
- Thước đo chính: Macro-F1 theo bản ghi; recall từng lớp; mức giữ hiệu năng so với cấu hình đầy đủ của cùng đợt.
- Suy luận: mô hình hiệu ứng hỗn hợp (run, seed là hiệu ứng ngẫu nhiên) hoặc bootstrap theo khối run; hiệu chỉnh cho so sánh nhiều lần.
- **Tiêu chí đọc kết quả viết trước khi chạy.** Ví dụ: tương tác được coi là có khi KTC của chênh lệch giữa hai họ mô hình không chứa 0 ở ít nhất hai đợt.
- Ánh xạ từng bảng, hình dự kiến → RQ → chủ sở hữu kết quả.
- **Sản phẩm:** `P1C_3_giao_thuc_YYYYMMDD.md` + tệp cấu hình chạy. → **ĐIỂM DỪNG 3** (NCS duyệt, commit, rồi mới chạy)

**Pha 4 – Chạy, đọc kết quả, kế hoạch bản thảo.**
- Chạy theo giao thức. Báo kết quả theo tiêu chí đã viết trước, kể cả khi không có hiệu ứng.
- Đề cương tiếng Anh; danh sách bảng, hình; 3–5 tạp chí ứng viên (đã kiểm hoặc `[CẦN KIỂM]`).
- Việc của NCS: tác giả, CRediT, thứ tự nộp so với Bài 1 và 1B.
- **Sản phẩm:** `P1C_4_ket_qua_va_ke_hoach_YYYYMMDD.md`. → **ĐIỂM DỪNG 4**

## 7. Báo cáo sau mỗi pha

Gồm 5 mục:
1. Đã làm (≤ 5 dòng).
2. Tệp đã tạo.
3. Tối đa 5 phát hiện, xếp theo mức chặn.
4. Câu hỏi cho NCS.
5. Việc kế tiếp.

## 8. Tự kiểm

- [ ] Không có cấu hình chứa S3 ở CP1.
- [ ] Pipeline chuẩn; ≥ 5 seed mọi mô hình; chấm theo bản ghi; không chấm theo cửa sổ.
- [ ] Nhãn không thứ tự; không DSI; không tuyên bố tương tự động lực học; không tuyên bố bộ dữ liệu là đóng góp.
- [ ] Số liệu R2, R4 (Bài 1) và R6 (1B) được trích, không trình bày như kết quả mới.
- [ ] Tiêu chí đọc kết quả được viết và commit trước khi chạy.
- [ ] Hạng tạp chí đã kiểm hoặc `[CẦN KIỂM]`.
- [ ] Đã dừng ở mỗi ĐIỂM DỪNG.

**Bắt đầu bằng Pha 0.**
