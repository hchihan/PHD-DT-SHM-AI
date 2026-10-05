# PROMPT – Phản biện và tìm đóng góp tốt nhất cho Paper 1B
## "Tính ổn định của quyết định chọn cấu hình cảm biến giữa các đợt đo"

> Dùng cho Claude Code tại thư mục gốc luận án `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM`. Nên bật Zotero MCP.
> Lập ngày 02/10/2026. **Thay thế** `PROMPT_RA_SOAT_PAPER1B_20261002.md`. Bản đó gộp nhầm 1B với bài cấu hình cảm biến, nay bài này là 1C.
> Văn bản dùng chung:
> - `00_DONG_BO_PIPELINE_VA_PHAN_VUNG_KET_QUA.md` (gọi tắt "tệp 00", bản v1.1);
> - `CLAUDE.md`;
> - `PROMPT_PHAN_BIEN_PAPER1C_CAU_HINH_CAM_BIEN_20261002.md` (bài anh em, gọi tắt "1C").

---

## 1. Bài đang xét

- **Bản thảo:** `04_PAPER_1B_SENSOR_CONFIGURATION/P1B_main_ban_NCS_gui_20261002.pdf`. Đây là bản NCS gửi ngày 02/10, mới hơn `PAPER_DRAFTING/Q2_Paper 2_Uncertainty.pdf`. Tìm tệp nguồn (.tex/.docx), mã và kết quả; không thấy thì ghi `MISSING`.
- **Tác giả hiện ghi:** Nguyễn Quang Vinh (IT hỗ trợ xử lý AI). NCS chốt tác giả và CRediT trước khi nộp.
- **Câu chuyện hiện tại (TG = theo bản thảo):**
  - Quyết định chọn cấu hình cảm biến rút từ một đợt đo có được bảo toàn ở đợt đo khác không?
  - Dữ liệu: CP2 và CP3 (bản thảo gọi là đợt 1, đợt 2), 7 tập con S1…S123.
  - Mô hình và đánh giá: RF cố định, LORO, 5 seed, chấm theo bản ghi.
  - Thước đo: selection regret, Kendall τb, bootstrap, phân tích theo run và theo trạng thái.
- **Kết quả chính (TG, cần tái lập):**
  - Đợt 1 đạt 0,964–1,000; S2 đứng đầu ở cả 5 seed.
  - Đợt 2: S2 kém nhất; regret 0,159 (KTC 95 % 0,099–0,229).
  - S123 chỉ thua 0,014.
  - Ổn định theo seed không đồng nghĩa với ổn định theo đợt đo.
- **Chỗ trống tự ghi trong bản thảo:** mô tả kết cấu, cảm biến, cách tạo trạng thái, kích thích ("[cần bổ sung…]").

---

## 2. Vai trò

Bạn là **hội đồng phản biện** của một tạp chí SHM hoặc đo lường, kiêm **cố vấn định vị đóng góp**. Giọng gắt, có căn cứ, mỗi nhận xét chỉ mục, bảng hoặc dòng cụ thể.

| Mã | Vai | Soi |
|---|---|---|
| R1 | SHM, thiết kế hệ cảm biến | Ý nghĩa của "quyết định chọn cấu hình" với người thiết kế hệ quan trắc. Liên hệ vị trí cảm biến với vị trí can thiệp (S1–B1 đỉnh, S2–B2 nút dầm – cột, S3–B3 giằng) |
| R2 | Đánh giá học máy | LORO; chấm theo bản ghi; chênh lệch số chiều đặc trưng giữa cấu hình (106 / 228 / 366); RF cố định có làm kết luận phụ thuộc mô hình không |
| R3 | Thống kê | Regret với 6 run; bootstrap theo bản ghi bỏ qua tương quan trong run; τb với 7 phần tử; phân biệt hiệu ứng thật với nhiễu fold |
| R4 | Đóng góp, định vị | So với tài liệu về bố trí, chọn cảm biến và đánh giá tính tổng quát giữa đợt đo. Liên hệ với khoảng trống A1/A2: một quyết định thiết kế cũng có phạm vi hiệu lực |
| ED | Biên tập viên | Tổng hợp; quyết định; điều kiện tối thiểu để nộp |

Báo cáo cho NCS viết tiếng Việt. Bản nộp quốc tế viết tiếng Anh; bản thảo hiện là tiếng Việt nên phải lập kế hoạch chuyển ngữ.

---

## 3. Ràng buộc

1. **Quy ước dữ liệu (tệp 00, mục 2):**
   - Dùng mã gốc CP2, CP3 trong toàn bài (bỏ "đợt 1/đợt 2" và mã nguồn CP1/CP2, hoặc chỉ giữ ở phụ lục đối chiếu).
   - Nhãn S0, B1, B2, B3 là **vị trí can thiệp, không có thứ tự**. Sửa cách gọi "trạng thái lành / ba trạng thái hư hỏng".
   - Không khẳng định tương tự động lực học của khung 1:10.
2. **Pipeline chuẩn (tệp 00, mục 3).** Bản thảo đang khớp: cửa sổ 400/200, chuẩn hóa theo từng cửa sổ, 25 đặc trưng mỗi kênh, chấm theo bản ghi. Kiểm thêm:
   - "Hệ số tương quan theo cặp kênh" có trùng với "tích trung bình theo cặp kênh" của Bài 1 không. Hai đại lượng tương đương khi kênh đã z-score; thống nhất tên gọi.
   - Kênh lực có thật sự bị loại không.
3. **Sở hữu kết quả (tệp 00 v1.1, mục 5):**
   - **1B sở hữu R6:** ổn định quyết định chọn cấu hình giữa đợt đo; regret; τb; ổn định theo seed so với theo đợt đo; chẩn đoán theo run và theo trạng thái.
   - 1B **không** sở hữu:
     - hiệu năng 4 mô hình ở cấu hình đầy đủ (R2, Bài 1);
     - so sánh mô hình × cấu hình (R7, 1C);
     - bộ dữ liệu (R1, Bài 1).
   - Con số RF của S123 ở CP2, CP3 trùng với Bài 1. Hoặc trích Bài 1, hoặc nêu rõ là dùng lại.
4. **Thứ tự nộp:** NCS muốn nộp 1B sớm. Nếu 1B nộp trước Bài 1:
   - mô tả dữ liệu ở mức đủ để tái lập;
   - dẫn Bài 1 là bản tiền in hoặc "under review";
   - không trình bày R2, R3 của Bài 1 như kết quả của 1B.

   NCS chọn cách xử lý ở Điểm dừng 1.
5. Không bịa số, trích dẫn, DOI. Hạng tạp chí kiểm trên trang tạp chí và SJR, ghi nguồn và ngày truy cập; không kiểm được thì `[CẦN KIỂM]`. Phân tích mới chỉ chạy sau khi giao thức được khóa và commit.
6. Không sửa tệp gốc. Sản phẩm ghi vào `03_PAPERS/PAPER_1B/review_YYYYMMDD/` (đường dẫn: [NCS XÁC NHẬN]).

---

## 4. Câu hỏi phản biện bắt buộc (tự trả lời ở Pha 1)

1. **Hiệu ứng trần.** Ở CP2, mọi cấu hình đạt ≥ 0,964 nên thứ hạng gần như ngẫu nhiên. Vậy "S2 đứng đầu ở CP2" có phải là một quyết định có ý nghĩa không? Regret A→B có phần lớn do trần không? Cần một mô hình so sánh rỗng: regret kỳ vọng khi chọn ngẫu nhiên trong các cấu hình đồng hạng.
2. **Chỉ hai đợt, một cặp chuyển.** Kết luận "không được bảo toàn" dựa trên đúng một cặp. Có mở rộng được sang CP1 qua các cấu hình chung S1, S2, S12 (thành ba cặp CP1↔CP2, CP1↔CP3, CP2↔CP3) không?
3. **Khoảng cách cảm biến – can thiệp.** Thứ hạng cấu hình có chỉ phản ánh cảm biến nào gần vị trí can thiệp không? Nếu đúng, có làm yếu hay làm mạnh thông điệp cho người thiết kế?
4. **Độ bất định.** Bootstrap theo bản ghi có làm KTC 0,099–0,229 hẹp quá không? Cần bootstrap theo khối run, hoặc hoán vị nhãn cấu hình.
5. **Phụ thuộc mô hình.** Kết luận chỉ cho RF. Một kiểm tra độ nhạy với một mô hình thứ hai có cần thiết không? Nếu làm, đó chỉ là kiểm tra độ bền; phần so sánh mô hình thuộc 1C.
6. **Kích thích.** Mỗi trạng thái có 3 kiểu kích thích mỗi run. Quyết định có đổi theo kiểu kích thích không? Đây có thể là một chiều ổn định thứ ba (seed → run → kích thích → đợt đo).
7. **"So what".** Viết một câu khuyến nghị cho người thiết kế hệ quan trắc rút từ bài. Ví dụ: chọn cấu hình theo regret lớn nhất nhỏ nhất (minimax) qua các đợt thay vì theo đỉnh của một đợt. Bài có đủ bằng chứng cho câu đó không?

---

## 5. Hướng đóng góp cần đánh giá (Pha 2)

Đánh giá từng hướng theo bốn tiêu chí: độ mới (so với tài liệu đã rà soát), độ chắc với dữ liệu hiện có, công sức, độ khớp với luận án.

| # | Câu chuyện | Phần mới có thể tuyên bố |
|---|---|---|
| D1 | **Giữ như hiện tại:** ổn định quyết định giữa hai đợt đo | Regret ở mức quyết định; ổn định theo seed khác ổn định theo đợt đo |
| D2 | **Quyết định thiết kế cũng có phạm vi hiệu lực:** một quyết định chọn cấu hình chỉ đúng trong điều kiện đã sinh ra nó. Đo phạm vi đó qua bốn mức seed → run → kích thích → đợt đo | Thang ổn định nhiều mức; nối trực tiếp với A2 của luận án; dễ viết thành câu chuyện tổng quát |
| D3 | **Quy tắc chọn bền vững:** so sánh "chọn theo đỉnh một đợt" với "chọn theo minimax regret / theo trung bình nhiều đợt" | Khuyến nghị có điều kiện cho thực hành, đo bằng regret ngoài đợt |
| D4 | **Ba cặp chuyển trên ba đợt:** thêm CP1 qua S1, S2, S12 | Tăng tính tổng quát từ 1 lên 3 cặp; cần kiểm ranh giới với 1C |

Đề xuất câu chuyện chính, câu chuyện phụ, tiêu đề và ba đóng góp. Mỗi đóng góp phải đo được bằng dữ liệu hiện có.

---

## 6. Quy trình – dừng ở mỗi ĐIỂM DỪNG

**Pha 0 – Kiểm kê và tái lập (không nhận xét).**
- Lập hồ sơ sự kiện: dữ liệu, pipeline, mọi con số chính kèm bảng hoặc hình nguồn.
- Đối chiếu từng con số với tệp kết quả: Khớp / Lệch / Không tìm thấy.
- Liệt kê chỗ lệch với tệp 00 và với Bài 1 (mã đợt, nhãn, tên đặc trưng, số liệu dùng chung).
- **Sản phẩm:** `P1B_0_kiem_ke_YYYYMMDD.md`. → **ĐIỂM DỪNG 0**

**Pha 1 – Phản biện.**
- R1–R4 viết báo cáo độc lập: Major/Minor, mỗi mục có vị trí, vấn đề, yêu cầu sửa, công sức S/M/L.
- ED tổng hợp, xếp mức Chặn / Nặng / Nhẹ, ra khuyến nghị.
- Kèm phương án xử lý thứ tự nộp với Bài 1 (ràng buộc 4).
- **Sản phẩm:** `P1B_1_phan_bien_YYYYMMDD.md`. → **ĐIỂM DỪNG 1**

**Pha 2 – Định vị đóng góp.**
- Đánh giá D1–D4 theo mục 5. Đề xuất câu chuyện chính.
- Kiểm tài liệu gần nhất (nếu tìm thêm thì ghi nhật ký truy vấn; `[CHƯA ĐỌC TOÀN VĂN]` khi cần).
- Viết 2–3 phương án tiêu đề tiếng Anh, tóm tắt mới (số chưa có để `[DATA-PENDING]`) và ba đóng góp.
- **Sản phẩm:** `P1B_2_dinh_vi_dong_gop_YYYYMMDD.md`. → **ĐIỂM DỪNG 2** (NCS chọn câu chuyện)

**Pha 3 – Gói phân tích bổ sung (khóa trước khi chạy).**
- Chỉ các phân tích phục vụ câu chuyện đã chọn, thuộc R6. Ví dụ:
  - mô hình so sánh rỗng cho hiệu ứng trần;
  - bootstrap hoặc hoán vị theo khối run;
  - ổn định theo kiểu kích thích;
  - ba cặp chuyển qua S1, S2, S12;
  - quy tắc chọn minimax;
  - kiểm tra độ nhạy với một mô hình thứ hai.
- Mỗi phân tích ghi: giả thuyết; thiết kế; tiêu chí đọc kết quả, viết trước khi chạy; công sức.
- Chạy sau khi NCS duyệt. Báo bảng trước/sau.
- **Sản phẩm:** `P1B_3_giao_thuc_va_ket_qua_YYYYMMDD.md`. → **ĐIỂM DỪNG 3**

**Pha 4 – Kế hoạch bản nộp.**
- Đề cương tiếng Anh; danh sách bảng, hình; kế hoạch sửa theo mục; bảng trả lời phản biện dự kiến.
- 3–5 tạp chí ứng viên, đã kiểm hoặc `[CẦN KIỂM]`.
- Việc của NCS: tác giả, CRediT, mô tả thí nghiệm còn trống, dữ liệu mở.
- **Sản phẩm:** `P1B_4_ke_hoach_nop_YYYYMMDD.md`. → **ĐIỂM DỪNG 4**

## 7. Báo cáo sau mỗi pha

Gồm 5 mục:
1. Đã làm (≤ 5 dòng).
2. Tệp đã tạo.
3. Tối đa 5 phát hiện, xếp theo mức chặn.
4. Câu hỏi cho NCS.
5. Việc kế tiếp.

## 8. Tự kiểm

- [ ] Mọi con số có nguồn; đã tái lập.
- [ ] Mã đợt CP2, CP3; nhãn không thứ tự; không gọi B1–B3 là "hư hỏng".
- [ ] Không có kết quả R1, R2, R7 trình bày như kết quả mới của 1B.
- [ ] Đóng góp đo được bằng dữ liệu hiện có hoặc đã ghi `[DATA-PENDING]`.
- [ ] Hạng tạp chí đã kiểm hoặc `[CẦN KIỂM]`.
- [ ] Đã dừng ở mỗi ĐIỂM DỪNG.

**Bắt đầu bằng Pha 0.**
