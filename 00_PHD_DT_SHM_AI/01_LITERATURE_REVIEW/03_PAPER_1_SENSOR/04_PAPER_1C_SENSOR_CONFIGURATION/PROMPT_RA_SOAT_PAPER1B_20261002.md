> **ĐÃ THAY THẾ (02/10/2026).** Không dùng tệp này. Bản này gộp nhầm 1B với bài cấu hình cảm biến. Dùng `PROMPT_PHAN_BIEN_PAPER1B_ON_DINH_QUYET_DINH_20261002.md` (1B) và `PROMPT_PHAN_BIEN_PAPER1C_CAU_HINH_CAM_BIEN_20261002.md` (1C).

# PROMPT – Rà soát và khởi động Paper 1B (cấu hình cảm biến), ưu tiên nộp trước

> Dùng cho Claude Code tại thư mục gốc luận án `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM`. Nên bật Zotero MCP.
> Lập ngày 02/10/2026. Văn bản dùng chung:
> - "tệp 00": `00_DONG_BO_PIPELINE_VA_PHAN_VUNG_KET_QUA.md`
> - `CLAUDE.md`
> - "prompt Bài 1": `PROMPT_PHAN_BIEN_PAPER1_Q1_20261002.md`
>
> NCS quyết định ưu tiên Paper 1B vì đánh giá là kết quả tốt. Prompt này kiểm xem "kết quả tốt" có giữ được dưới giao thức chuẩn không. Sau đó đưa bài đến bản nộp được.

---

## 1. Paper 1B là gì (theo tài liệu hiện có)

- Theo `04_PAPER_1B_SENSOR_CONFIGURATION/README.md`, mục tiêu của 1B gồm:
  - tập con cảm biến, số lượng và thành phần cảm biến;
  - mức giữ hiệu năng (performance retention) và lợi ích biên (marginal benefit);
  - độ bền vững giữa run và giữa campaign.
- Vị trí: phạm vi hỗ trợ cho RQ1/WP1, không có RQ hay Gate riêng.
- Giao thức hợp lệ do Bài 1 (1A) sở hữu.
- Hai bản thảo đang ứng với phạm vi này (tệp 00 gọi là BT-A và BT-B):

| Mã | Bản thảo | Dữ liệu | Giao thức | Kết quả nổi bật (theo bản thảo, chưa kiểm) |
|---|---|---|---|---|
| BT-A | `PAPER_DRAFTING/Q2_Paper 2_Uncertainty.pdf` (tiếng Việt). "Tính ổn định của quyết định chọn cấu hình cảm biến giữa hai campaign đo" | CP2, CP3; 7 tập con S1…S123; RF | LORO 5/1, 5 seed, chấm theo bản ghi, bootstrap, regret, Kendall τb | Regret A→B = 0,159 (KTC 95 % 0,099–0,229); S2 tốt nhất ở CP2 nhưng kém nhất ở CP3 |
| BT-B | `PAPER_DRAFTING/Q3_Paper3_Sensor_Configuration (10.06).docx` (tiếng Anh) | 72 recording (nhiều khả năng là CP1); S1, S2, S12; RF, SVM, LR, 1D-CNN | Một lần chia cố định, chấm theo cửa sổ, 1 kênh mỗi cảm biến, cửa sổ 1.024 | 1D-CNN tăng từ 0,641 (S1) lên 0,841 (S12); DSI có thứ tự, R = 0,953 |

**Cảnh báo cần kiểm ngay** (từ README 13/09 và tài liệu G1):
- Khối tập con cũ (ResNet1D, 17 cấu hình × 30 lần chia, **một seed**) **không tách được** hiệu ứng cấu hình khỏi nhiễu fold ở CP2, CP3.
- Câu "cấu hình cảm biến ảnh hưởng ngang hoặc hơn chọn thuật toán" **chưa được bằng chứng hỗ trợ**, đang chờ thầy quyết định (mục C-02 trong `01_CURRENT_CONTROL/PAPER1_SCIENCE_LOCK_PROJECT_SYNC_REPORT_20260913.md`). BT-B lại đưa ý này vào highlight.
- BT-B dùng pipeline khác pipeline chuẩn: chấm theo cửa sổ, một lần chia, chuẩn hóa theo tập train, 1 kênh. BT-B còn coi nhãn là có thứ tự (DSI) và khẳng định tương tự động lực học. Cả hai điều này trái với Bài 1 và tệp 00 mục 2.

**Vì vậy "kết quả tốt" của BT-B chưa được dùng làm căn cứ** cho tới khi chạy lại theo pipeline chuẩn. Kết quả của BT-A được làm theo pipeline gần chuẩn, nên là ứng viên mạnh hơn cho lõi của 1B.

---

## 2. Vai trò

Bạn vừa là **hội đồng phản biện** (giọng gắt, có căn cứ, chỉ dòng cụ thể), vừa là **trợ lý thực thi** đưa 1B đến bản nộp được.

Hội đồng gồm:
- **R1** – SHM và thiết kế hệ cảm biến;
- **R2** – học máy và rò rỉ dữ liệu;
- **R3** – thống kê: nhiễu fold so với hiệu ứng thật, bootstrap, kiểm định;
- **R4** – đóng góp và định vị so với tài liệu về chọn cấu hình, bố trí cảm biến;
- **ED** – biên tập viên tổng hợp.

Báo cáo cho NCS viết tiếng Việt. Bản thảo nộp quốc tế viết tiếng Anh.

---

## 3. Nguồn phải đọc (toàn bộ; tệp dài đọc theo phần)

1. Hai bản thảo BT-A, BT-B ở trên. Tìm thêm tệp nguồn của BT-A (.docx, .tex) và mã, kết quả của tác giả xử lý AI. Không có thì ghi `MISSING`.
2. Thư mục `03_OUTPUTS/04_PAPER_1B_SENSOR_CONFIGURATION/`: `README.md`, `P1SC_OUTLINE_AND_IT_CHECKLIST.docx`, `P1SC_Q3_MONITORING_PLANNING_OUTLINE_AND_IT_TASKS.docx`.
3. `01_CURRENT_CONTROL/PAPER1_SCIENCE_LOCK_PROJECT_SYNC_REPORT_20260913.md` (mục C-02); kết luận kỹ thuật 07/09/2026 về khối tập con. Không thấy thì ghi `MISSING`.
4. Bài 1 v8 (`PAPER_DRAFTING/Q1_PAPER1_v8_…docx`): mô tả dữ liệu, pipeline, các bảng có chung số liệu với 1B.
5. Tệp 00: mục 2 (quy ước), mục 3 (pipeline chuẩn), mục 5 (ma trận sở hữu R1–R7).
6. Dữ liệu, mã: `02_DATA_CODE_AND_EXPERIMENTS/`. Gồm registry 216 recording, cấu hình chạy, kết quả từng fold và từng seed của BT-A, BT-B và khối tập con 07/09. Chưa kết nối thì ghi `MISSING` và dừng ở phần cần số.
7. Ghi chú tài liệu liên quan trong `notes/` (ví dụ [15], [14], [53], [48], Eraliev 2022). Tài liệu về bố trí, chọn cấu hình cảm biến nếu tìm thêm: ghi nhật ký truy vấn; chưa đọc toàn văn thì gắn `[CHƯA ĐỌC TOÀN VĂN]`.

---

## 4. Ràng buộc

1. **MT1 là tối thượng; giao thức do Bài 1 sở hữu.** 1B dùng pipeline chuẩn ở tệp 00 mục 3:
   - cửa sổ 400/200, chuẩn hóa theo từng cửa sổ;
   - 25 đặc trưng mỗi kênh, 4 kênh mỗi cảm biến;
   - chấm theo bản ghi;
   - đánh giá theo nhóm (LORO; LOCO khi so giữa các campaign).

   Muốn lệch bước nào thì phải nêu lý do và có NCS duyệt.
2. **Quy ước dữ liệu (tệp 00 mục 2):**
   - Campaign: CP1–CP3. Không dùng A/B.
   - Nhãn: S0, B1, B2, B3, không có thứ tự. Bỏ DSI có thứ tự.
   - Cấu hình: S12 dùng chung ba campaign; S3 chỉ có ở CP2, CP3.
   - Không khẳng định tương tự động lực học của khung 1:10.
3. **Ma trận sở hữu (tệp 00 mục 5):**
   - 1B sở hữu R6 (tập con, regret, τb, ổn định theo seed so với theo campaign) và R7 (cấu hình × thuật toán ở CP1).
   - 1B **không** trình bày làm kết quả mới các phần: R1 (bộ dữ liệu), R2 (hiệu năng 4 mô hình ở cấu hình đầy đủ), R3 (chênh lệch cùng lần chạy so với LORO/LOCO), R4 (LOCO trên S12), R5. Các phần này trích Bài 1.
   - Nếu 1B nộp trước Bài 1: Bài 1 phải có bản tiền in, hoặc 1B mô tả dữ liệu ở mức tối thiểu và dẫn "manuscript under review". NCS chọn cách (mục 6, Pha 1).
4. **Không dùng câu "cấu hình chi phối hơn thuật toán"** ở dạng khẳng định, trừ khi phân tích đã khóa trước cho thấy điều đó và thầy đã duyệt mục C-02.
5. **Không bịa số liệu, trích dẫn, DOI.** Số lấy từ bản thảo hoặc tệp kết quả, ghi nơi lấy. Phân tích chưa chạy ghi `[DATA-PENDING]`.
6. **Khóa trước khi chạy:** giao thức, danh sách cấu hình, thước đo, tiêu chí "kết quả giữ được" phải được commit trước lần chạy lại đầu tiên.
7. **Không sửa tệp gốc.** Sản phẩm ghi vào `03_PAPERS/PAPER_1B/review_YYYYMMDD/` (đường dẫn: [NCS XÁC NHẬN]).
8. **Tác giả:** NCS chốt danh sách tác giả và vai trò theo CRediT. Nguyễn Quang Vinh là IT hỗ trợ xử lý AI. Prompt không tự quyết thứ tự tác giả.
9. Hạng Q, phạm vi, giới hạn độ dài của tạp chí: kiểm trên trang tạp chí và SJR, ghi nguồn và ngày truy cập. Không kiểm được thì ghi `[CẦN KIỂM]`.

---

## 5. Câu hỏi bắt buộc phản biện phải tự trả lời

**R1 – SHM:**
- S1, S2, S3 đặt ở ba vùng ứng với ba vị trí can thiệp B1, B2, B3. Khi đó "cảm biến nào tốt" có phải chỉ là "cảm biến nào gần chỗ can thiệp"? Nếu đúng, kết luận có còn giá trị cho người thiết kế hệ quan trắc không?
- Ba kiểu kích thích (BEAT_L1, BEAT_L2, WHITE NOISE) có làm đổi thứ hạng cấu hình không?

**R2 – Học máy:**
- BT-B chấm theo cửa sổ, một lần chia, chuẩn hóa theo train. Con số 0,641 → 0,841 còn lại bao nhiêu khi chạy theo pipeline chuẩn?
- So sánh 7 cấu hình có số chiều đặc trưng khác nhau (106 / 228 / 366): đã kiểm hiệu ứng số chiều chưa?

**R3 – Thống kê:**
- Với 6 run mỗi campaign, chênh lệch giữa các cấu hình có vượt nhiễu fold và seed không? Đây đúng là chỗ khối 07/09 thất bại.
- Bootstrap theo recording bỏ qua biến động giữa run (BT-A tự nêu). Cần bootstrap hoặc hoán vị theo khối run.
- τb = −0,066 với 7 cấu hình có ý nghĩa gì?

**R4 – Đóng góp:**
- Viết một câu "người thiết kế hệ quan trắc biết thêm điều gì". Câu nào đứng được hơn:
  - "quyết định chọn cấu hình rút từ một campaign không được bảo toàn ở campaign khác" (BT-A);
  - hay "thêm cảm biến hơn đổi thuật toán" (BT-B)?

**ED:**
- 1B nên là một bài (gộp BT-A và BT-B) hay hai bài? Mục 6, Pha 1 có ba phương án.

---

## 6. Quy trình – dừng ở mỗi ĐIỂM DỪNG

### Pha 0 – Kiểm kê và tái lập số (không nhận xét)
- Liệt kê mọi tệp của 1B (bản thảo, nguồn, mã, kết quả) kèm ngày sửa.
- Lập hồ sơ sự kiện cho BT-A, BT-B và khối tập con 07/09: dữ liệu, pipeline, giao thức, mọi con số chính kèm nguồn.
- **Tái lập:** đối chiếu từng con số chính trong bản thảo với tệp kết quả gốc. Ghi Khớp / Lệch / Không tìm thấy.
- Đối chiếu với tệp 00 mục 2, 3, 5. Liệt kê điểm lệch, gồm cả số liệu dùng chung với Bài 1 (ví dụ RF S123 CP3: 0,875 ở Bài 1, 0,889 ở BT-A).
- **Sản phẩm:** `P1B_0_kiem_ke_tai_lap_YYYYMMDD.md`. → **ĐIỂM DỪNG 0**

### Pha 1 – Phản biện và chọn phương án
- R1–R4 viết báo cáo: Major/Minor, mỗi mục có vị trí, vấn đề, yêu cầu sửa, công sức (S/M/L), cần dữ liệu mới hay không.
- ED tổng hợp, xếp mức Chặn / Nặng / Nhẹ, và đánh giá **ba phương án**:

| Phương án | Nội dung | Gợi ý đánh giá |
|---|---|---|
| A | 1B = BT-A làm lõi. Thêm CP1 qua cấu hình chung S12 và các tập con S1, S2. Bỏ BT-B hoặc hoãn | Giao thức gần chuẩn, kết quả có khoảng tin cậy, ít việc nhất |
| B | Gộp BT-A + BT-B thành một bài: ổn định quyết định cấu hình (giữa run, campaign, kích thích) và tương tác cấu hình × thuật toán, chạy lại theo pipeline chuẩn | Bài mạnh hơn, nhưng phải chạy lại BT-B; cần sửa tệp 00 (gộp R6, R7) |
| C | Giữ hai bài riêng | Rủi ro chồng lấn và "cắt lát"; tốn công nhất |

- Ghi rõ phương án được đề xuất và lý do. Ghi cách xử lý thứ tự nộp với Bài 1 (ràng buộc 3).
- **Sản phẩm:** `P1B_1_phan_bien_va_phuong_an_YYYYMMDD.md`. → **ĐIỂM DỪNG 1** (NCS chọn phương án; nếu chọn B thì sửa tệp 00)

### Pha 2 – Kiểm "kết quả tốt" dưới giao thức chuẩn
- Viết giao thức chạy lại, khóa trước. Nội dung tối thiểu:
  - cấu hình theo phương án đã chọn;
  - mô hình: RF bắt buộc; các mô hình khác tùy phương án;
  - LORO trong campaign; với so sánh giữa campaign, dùng S12 và các tập con có ở cả hai campaign;
  - ≥ 5 seed;
  - bootstrap hoặc hoán vị theo khối run;
  - **tiêu chí "kết quả giữ được"**: ví dụ dấu của chênh lệch không đổi, và khoảng tin cậy không chứa 0.
- Chạy (nếu mã và dữ liệu sẵn có). Báo bảng trước/sau cho từng con số chính của bản thảo.
- Nếu kết quả không giữ được thì nói thẳng, và đề xuất câu hỏi nghiên cứu còn đứng được.
- **Sản phẩm:** `P1B_2_giao_thuc_va_ket_qua_kiem_YYYYMMDD.md` kèm bảng CSV. → **ĐIỂM DỪNG 2**

### Pha 3 – Khai phá thêm trên dữ liệu sẵn có (chỉ phân tích thuộc R6, R7)
Lập danh mục ứng viên. Mỗi dòng ghi: câu hỏi; dữ liệu; thiết kế; giá trị cho bài; công sức; rủi ro; chủ sở hữu theo tệp 00. Gợi ý để đánh giá:
- **Retention và lợi ích biên:** hiệu năng giữ được khi bớt cảm biến; lợi ích của cảm biến thứ hai, thứ ba; theo trạng thái.
- **Ổn định quyết định ở ba mức:** seed → run → campaign; thêm mức kiểu kích thích.
- **Bóc tách khoảng cách:** cảm biến – vị trí can thiệp (trả lời câu R1) bằng ma trận cấu hình × trạng thái.
- **Kiểm soát số chiều đặc trưng:** chọn số đặc trưng bằng nhau giữa các cấu hình.
- **Kênh trục:** x, y, z so với tổng hợp, nếu không chạm R2 của Bài 1.
- **Câu hỏi thiết kế:** cấu hình nào cho regret nhỏ nhất qua mọi campaign (cấu hình "an toàn"), trình bày như khuyến nghị có điều kiện.

Phân tích chạm R1–R5 hoặc R11 thì tách thành đề xuất đổi ma trận.

- **Sản phẩm:** `P1B_3_tiem_nang_YYYYMMDD.md`. → **ĐIỂM DỪNG 3**

### Pha 4 – Kế hoạch bản nộp
- Đề cương bài bằng tiếng Anh: 2–3 phương án tiêu đề; tóm tắt; 3 đóng góp; cấu trúc mục; danh sách bảng, hình. Chỉ dùng số đã kiểm ở Pha 2; số mới để `[DATA-PENDING]`.
- 3–5 tạp chí ứng viên. Hạng và phạm vi đã kiểm có nguồn, hoặc `[CẦN KIỂM]`.
- Kế hoạch sửa theo mục. Bảng trả lời phản biện dự kiến (Chặn/Nặng → cách xử lý).
- Việc của NCS: chốt tác giả, CRediT, bản tiền in Bài 1 (nếu cần), quyền dùng dữ liệu.
- **Sản phẩm:** `P1B_4_ke_hoach_nop_YYYYMMDD.md`. → **ĐIỂM DỪNG 4**

---

## 7. Báo cáo sau mỗi pha

1. Đã làm gì (≤ 5 dòng).
2. Tệp đã tạo.
3. Tối đa 5 phát hiện, xếp theo mức chặn.
4. Câu hỏi cần NCS quyết định.
5. Việc kế tiếp.

## 8. Tự kiểm

- [ ] Mọi con số có nguồn; đã ghi Khớp / Lệch khi tái lập.
- [ ] Không còn A/B, DSI có thứ tự, tương tự động lực học, chấm theo cửa sổ trong đề xuất.
- [ ] Không có kết quả R1–R5 của Bài 1 được trình bày như kết quả mới của 1B.
- [ ] Câu "cấu hình chi phối hơn thuật toán" không xuất hiện ở dạng khẳng định khi chưa có căn cứ.
- [ ] Hạng tạp chí đã kiểm hoặc ghi `[CẦN KIỂM]`.
- [ ] Đã dừng ở mỗi ĐIỂM DỪNG.

**Bắt đầu bằng Pha 0.**
