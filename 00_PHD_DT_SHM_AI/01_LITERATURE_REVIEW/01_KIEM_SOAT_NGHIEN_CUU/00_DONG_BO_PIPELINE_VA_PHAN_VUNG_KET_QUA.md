# 00 – Đồng bộ pipeline và phân vùng kết quả

**Phiên bản:** v1.2 – 02/10/2026 (cập nhật sau P1R4, NCS "DUYỆT HẾT"). Trước đó: v1.1 – 02/10/2026. v1.0 lập theo Q6 ở ĐIỂM DỪNG 1; v1.1 đổi mã bài theo cách gọi của NCS (1A, 1B, 1C) và đặt lại phạm vi 1C theo ý định NCS nêu ngày 02/10.

**Lưu ý ký hiệu:** từ v1.1, các bài được gọi là **1A, 1B, 1C, 2**. Không dùng "B1" cho bài báo nữa, để tránh trùng với đối chứng B1 (MT2) và trạng thái B1 (can thiệp vùng đỉnh).

**Căn cứ:**
- Quyết định của NCS ngày 02/10/2026 (Q1–Q6, tài liệu G1).
- `tieuluan/` và `revision/GD3b_khoang_trong_va_muc_tieu.md` (mức ưu tiên cao nhất).
- `CLAUDE.md` mục 2, 2A, 8, 13.
- Ba bản thảo trong `PAPER_DRAFTING/`.

**Quy ước nhãn:** [ĐÃ CÓ] = có trong tài liệu; [ĐỀ XUẤT] = cố vấn đề xuất, chờ NCS duyệt; [NCS XÁC NHẬN] = cần NCS điền hoặc xác nhận.

**Nguyên tắc gốc:**
1. **MT1 là tối thượng.** Mọi bài dùng dữ liệu phòng thí nghiệm điều chỉnh theo pipeline và quy ước của MT1 (Bài 1).
2. **Mỗi kết quả chỉ là kết quả mới trong một bài.** Bài khác dùng lại kết quả đó thì phải trích bài sở hữu, không trình bày như kết quả mới.

---

## 1. Danh mục bài báo

Cam kết với trường và với tiểu luận là 2 bài (Bài 1, Bài 2). Đó là mức tối thiểu để đủ điều kiện tốt nghiệp. Các bài bổ trợ có thể nhiều hơn và không ghi vào tiểu luận (Q1).

| Mã | Bài | Mục tiêu | Loại | Bản thảo hiện có | Trạng thái |
|---|---|---|---|---|---|
| **1A** (Bài 1) | Bằng chứng trạng thái có phạm vi hiệu lực: đánh giá theo đơn vị độc lập trên khung thép 1:10 | MT1 | Cam kết (tiểu luận) | `PAPER1_v9_SHM_20261002.docx` (thư mục `02_PAPER_1A_GATE1_EVIDENCE_CONDITION`; gốc v8.1) | v9 viết xong 02/10/2026, chờ NCS duyệt; khung P1-S1 |
| **2** (Bài 2) | Mô hình thông tin truy vết bằng chứng → hành động, mở rộng IFC 4.3 + BCF 3.0, so với B0 và B1 | MT2 (+MT3 minh họa) | Cam kết (tiểu luận) | Chưa có. Hồ sơ ở `05_PAPER_2_TRACEABILITY/`, prompt `PROMPT_KHOI_DONG_PAPER2_v2_20261002.md` | Pha 0 |
| **1B** | Tính ổn định của quyết định chọn cấu hình cảm biến giữa các đợt đo | Bổ trợ cho RQ1 (quyết định thiết kế cũng có phạm vi hiệu lực) | Bổ trợ | `04_PAPER_1B_SENSOR_CONFIGURATION/P1B_main_ban_NCS_gui_20261002.pdf` (mới hơn `Q2_Paper 2_Uncertainty.pdf`) | Gần hoàn chỉnh; prompt `PROMPT_PHAN_BIEN_PAPER1B_ON_DINH_QUYET_DINH_20261002.md` |
| **1C** | Tác động của cấu hình 1, 2, 3 cảm biến lên các mô hình AI, qua ba đợt đo | Bổ trợ cho RQ1 (cấu hình là thành phần của phạm vi) | Bổ trợ | `Q3_Paper3_Sensor_Configuration (10.06).docx` (bản cũ, giao thức không dùng được) | Thiết kế lại; prompt `PROMPT_PHAN_BIEN_PAPER1C_CAU_HINH_CAM_BIEN_20261002.md` |
| **1D** | OMA và FEM giải thích | Bổ trợ (bối cảnh vật lý của MT1) | Bổ trợ | Chưa có (dự kiến) | Hoãn |

Ghi chú về tên gọi [ĐỀ XUẤT]:
- Không dùng "Paper 2", "Paper 3" cho các bài bổ trợ, để tránh nhầm với Bài 2 của luận án.
- Tên tệp trong `PAPER_DRAFTING/` có thể giữ nguyên; trong văn bản điều hành dùng mã ở bảng trên.

---

## 2. Quy ước dữ liệu chung (bắt buộc cho 1A, 1B, 1C, 1D)

| Hạng mục | Quy ước | Nguồn |
|---|---|---|
| Campaign | **CP1, CP2, CP3**. Không dùng A/B hay CP4 (CP4 đã bỏ) | 1A v8 [ĐÃ CÓ]; quyết định phạm vi 10/2026 |
| Quy mô | 18 run (RUN001–018), 216 recording (72 mỗi campaign), 100 Hz. **Phiên đo lặp 22/07/2026 (53 recording S0/B1/B2) không thuộc bộ dữ liệu, không dùng** | 1A v8 [ĐÃ CÓ]; NCS 02/10/2026 |
| Thứ bậc đơn vị (v1.2) | recording ⊂ **lần lặp (RUN)** ⊂ **lần thiết lập trạng thái** ⊂ campaign. RUN là lần lặp liên tiếp trong cùng ô trạng thái × kích thích (trung vị 127 s); CP1: 2 lần thiết lập/trạng thái (trùng họ kích thích), CP2: 1, CP3: 2 (hai lượt) | E1, P1_V9_POSTHOC |
| Độ phân giải tín hiệu (v1.2) | CSV gốc PASCO ghi 1 chữ số thập phân: bước lượng tử 0,1 m/s². Mọi bài dùng dữ liệu này phải báo | E5 |
| Trạng thái | **S0** tham chiếu; **B1** can thiệp vùng đỉnh (apex); **B2** can thiệp nút dầm – cột; **B3** can thiệp liên kết giằng. Nhãn chỉ vị trí can thiệp, **không có thứ tự**, không là thang mức hư hỏng | 1A v8 [ĐÃ CÓ] |
| Cảm biến | S1 vùng đỉnh, S2 nút dầm – cột (CP1–CP3); S3 vùng giằng – cột (chỉ CP2, CP3). PASCO PS-3223, 4 kênh mỗi cảm biến | 1A v8 [ĐÃ CÓ] |
| Cấu hình dùng chung | **S12** dùng chung cho cả ba campaign. **Ngoại lệ v1.2:** kết quả chéo đợt của 1A dùng **S123 cho CP2↔CP3** (cấu hình chung của hai đợt này, theo đầu ra IT đã chạy); CP1 không vào so sánh chéo | Q4c [ĐÃ CÓ]; NCS duyệt 02/10/2026 (P1R4 (b)) |
| Cấu hình trong từng campaign | 1A giữ phân tích S12 (CP1) và S123 (CP2, CP3) | Q4c [ĐÃ CÓ] |
| Khung 1:10, BIM 1:1 và nhà xưởng hiện trường | Khung 1:10 mô phỏng một nhà xưởng thật ở tỉnh Khánh Hòa; BIM 1:1 của nhà xưởng này dùng cho MT2 (Bài 2). Nhà xưởng hiện trường của MT3 ở tỉnh Đắk Lắk (địa bàn Phú Yên cũ), là công trình khác. Khung 1:10 và BIM 1:1 chỉ nối qua tương ứng thông tin (Physical_Identity = FALSE). Không khẳng định tương tự động lực học khi chưa kiểm | Q4b; 1A v8 [ĐÃ CÓ] |
| Kết quả 1A trước khi Gate 1 ký | Mức CANDIDATE | Prompt Paper 2 [ĐÃ CÓ] |

---

## 3. Pipeline chuẩn (gọi tắt `shm-core`)

**Pipeline chuẩn là pipeline của 1A v8.** Repo và commit: [NCS XÁC NHẬN]. Mọi kết quả phải ghi `method_version` (git commit) theo CLAUDE.md QĐ 6.

| Bước | Chuẩn | 1A v8 | 1B | 1C (bản cũ 10.06) |
|---|---|---|---|---|
| Cắt cửa sổ | 400 mẫu, bước 200 | ✔ | ✔ | ✘ 1.024/256 |
| Chuẩn hóa | z-score theo từng cửa sổ | ✔ | ✔ | ✘ theo tập train |
| Đặc trưng | 25 đặc trưng/kênh + tích trung bình theo cặp kênh | ✔ | ✔ (gọi là "hệ số tương quan", cần sửa tên) | ✘ ~140/kênh |
| Kênh | 4 kênh mỗi cảm biến | ✔ | ✔ | ✘ 1 kênh |
| Mô hình chuẩn | RF, SVM-RBF, 1D-CNN, ResNet1D | ✔ | Chỉ RF (chấp nhận được) | ✘ có LR, thiếu ResNet1D |
| Đơn vị chấm điểm | Theo bản ghi | ✔ | ✔ | ✘ theo cửa sổ |
| Đánh giá | **Cùng lần chạy (mốc) + LORO = giữ lại toàn bộ một lần chạy** (v1.4, thay v1.2) + LOCO; bootstrap theo cụm run; hoán vị có giới hạn (khối trạng thái trong run); biến thiên theo seed và ứng viên | ✔ v9 (LORO + LOCO CP2↔CP3 cho 4 mô hình; RF/SVM bằng mô hình đã lưu, E10) | LORO 5/1 + bootstrap | ✘ một lần chia |
| Siêu tham số | Chọn trong vùng không chứa run test | ✘ 15/18 fold vi phạm (1A tự nêu) | Cố định | — |

**Quy tắc:** bài bổ trợ được thêm phân tích riêng (regret, Kendall τb, bootstrap…) nhưng không đổi các bước 1–6. Muốn đổi bước nào thì ghi vào sổ thay đổi (mục 7) và có NCS duyệt.

---

## 4. Việc 1A phải bổ sung để đủ tiêu chí MT1 (Q5: bài điều chỉnh theo MT1)

| # | Việc | Căn cứ |
|---|---|---|
| 1A-1 | Chạy đánh giá **cùng lần chạy** làm mốc; báo chênh lệch của LORO và LOCO so với mốc này | GD3b MT1 (c); CLAUDE.md QĐ 13 |
| 1A-2 | **LOCO đầy đủ** cho cả 4 mô hình, trên cấu hình chung S12, cả ba campaign | CLAUDE.md QĐ 4; Q4c |
| 1A-3 | Kiểm định hoán vị cho kết quả chính; RF, SVM chạy ≥ 3 seed | CLAUDE.md QĐ 4 |
| 1A-4 | Xử lý phụ thuộc siêu tham số: chọn lại trong vùng không chứa run test, hoặc tách thành phân tích nhạy | 1A v8 tự nêu |
| 1A-5 | Ghi mỗi kết quả thành bản ghi `EVIDENCE` có `method_version`, `uncertainty`, phạm vi (`inference_unit`, `data_split`, `install_batch`) | GD3b MT1 (d) |
| 1A-6 | Tổng quan nêu [19] Ramasso 2025 và [15] Wheat 2024 là tiền lệ gần nhất | GD3b, CLAUDE.md QĐ 13 |
| 1A-7 (v1.2) | Báo mức đủ của tín hiệu (độ phân giải, số mức, cửa sổ hằng) | P1R2 C1; E5 |
| 1A-8 (v1.2) | Báo các đường thông tin không phải kết cấu (độ lệch tĩnh, thứ tự đo) | P1R2 C2; E6, E7 |
| 1A-9 (v1.2) | Công bố dữ liệu và mã (DOI), commit 360c79f, giao thức hậu kiểm | P1R2 N9 |

**Trạng thái trong v9 (02/10/2026):** 1A-1 **chưa đạt**: v9 dùng thứ bậc đơn vị (LORO = trong lần thiết lập) so với LOCO, chưa chạy mốc cùng lần chạy. **NCS quyết định 02/10/2026 (v1.4): Bài 1 chạy thêm mốc đánh giá cùng lần chạy; LORO định nghĩa lại là giữ lại toàn bộ một lần chạy, khớp tiểu luận (thuật ngữ, 3.4.3, Bảng 5.4).** 1A-2 một phần (CP2↔CP3, S123, 4 mô hình); 1A-3 hoán vị có giới hạn ✔, RF/SVM vẫn 1 seed (bù bằng E3); 1A-4 nêu và lập luận hướng bảo thủ; 1A-5 ✔ (Phụ lục B); 1A-6 ✔; 1A-7, 1A-8 ✔; 1A-9 chờ NCS chọn kho DOI.

---

## 5. Ma trận sở hữu kết quả

Ô **M** = kết quả mới của bài đó. Ô **T** = trích từ bài sở hữu. Ô trống = không dùng.

| Kết quả | 1A | 2 | 1B | 1C | 1D |
|---|---|---|---|---|---|
| R1. Bộ dữ liệu CP1–CP3 (mô tả, registry, SHA-256) | **M** | T | T | T | T |
| R2. Hiệu năng 4 mô hình ở cấu hình đầy đủ trong từng đợt: S12 (CP1), S123 (CP2, CP3), LORO | **M** | | T (RF S123 làm mốc) | T (điểm mốc) | |
| R3. Chênh lệch cùng lần chạy so với LORO và LOCO | **M** | | | | |
| R4. LOCO / chuyển giao giữa đợt (v1.2: CP2↔CP3 trên S123) | **M** | | T | T | |
| R4b (v1.2). Mức đủ tín hiệu, độ lệch tĩnh, thứ tự đo; độ tin cậy trong/ngoài phạm vi (E5–E8) | **M** | T | T | T | |
| R5. Bản ghi `EVIDENCE` có phạm vi của các kết quả R2–R4 | **M** | T (đầu vào chèn lỗi) | | | |
| R6. Ổn định **quyết định chọn cấu hình** (RF, 7 tập con ở CP2, CP3; mở rộng qua S1, S2, S12 nếu duyệt): selection regret, Kendall τb, ổn định theo seed / run / kích thích / đợt, quy tắc chọn bền vững | | | **M** | T (số RF tập con) | |
| R7. **Tác động của cấu hình 1, 2, 3 cảm biến lên các mô hình AI** (RF, SVM-RBF, 1D-CNN, ResNet1D): tương tác mô hình × cấu hình; mức giữ hiệu năng và lợi ích biên; phủ vị trí so với số lượng; qua ba đợt trên {S1, S2, S12} và trong CP2, CP3 cho cấu hình có S3; LOCO trên S1, S2 theo từng mô hình | | | | **M** | |
| R8. Mô hình thông tin 6 thực thể, 5 ràng buộc, script | | **M** | | | |
| R9. M1–M4 so với B0 và B1 trên BIM nhà xưởng thật | | **M** | | | |
| R10. Dữ liệu hiện trường MT3, kịch bản C3 | | M (minh họa, nếu kịp) / chương luận án | | | |
| R11. Dạng dao động (OMA), so sánh với FEM danh nghĩa | | | | | **M** |

**Ranh giới 1B – 1C (cùng dữ liệu, khác câu hỏi):**
- 1B hỏi về **quyết định**: cấu hình được chọn ở đợt này có còn đúng ở đợt khác không (RF cố định làm công cụ đo). Thước đo: regret, thứ hạng.
- 1C hỏi về **mô hình**: số và tổ hợp cảm biến tác động thế nào lên từng họ mô hình AI. Thước đo: hiệu năng, mức giữ hiệu năng, tương tác.
- Số RF trên các tập con ở CP2, CP3 xuất hiện ở cả hai bài: 1B sở hữu, 1C trích. Nếu 1B dùng thêm mô hình thứ hai, đó chỉ là kiểm tra độ bền, không là so sánh mô hình.

**Các điểm phải sửa để ma trận đúng:**
- **1B:** dùng mã gốc CP2, CP3 (bản thảo gọi "đợt 1, đợt 2" và mã nguồn "CP1, CP2"). Nhãn B1–B3 là vị trí can thiệp, không gọi là "trạng thái hư hỏng". Bảng S123 dùng làm nền phải trích 1A (R2). Nếu 1B nộp trước 1A: chỉ trình bày R6, R2 dẫn dạng bản tiền in hoặc "under review" [NCS XÁC NHẬN].
- **1B, tác giả:** Nguyễn Quang Vinh là IT hỗ trợ xử lý AI (Q2). Danh sách tác giả, CRediT và quyền dùng dữ liệu cần NCS chốt trước khi nộp [NCS XÁC NHẬN].
- **1C:** thiết kế lại theo pipeline chuẩn. Bỏ tuyên bố "labeled dataset" (R1 thuộc 1A). Bỏ DSI có thứ tự. Bỏ câu về tương tự động lực học. Bỏ lộ trình "Paper 2 FEM-updated DSI / Paper 3 Lab-to-Field". CP1 không có S3: cấu hình 3 cảm biến chỉ ở CP2, CP3.
- **1B và 1C:** kết luận về cấu hình không được mâu thuẫn; mỗi bài nêu rõ phạm vi đợt và mô hình của mình.

---

## 6. Phụ thuộc giữa các bài

- 1A → 2: Bài 2 cần tập `EVIDENCE` có phạm vi đã biết (R5). Dùng được ngay khi giao thức 1A đã khóa, không cần chờ 1A được nhận (GD3b D7).
- 1A → 1B, 1C: cần R1, R2 đã công bố, hoặc ít nhất đã nộp hay có bản tiền in, để trích.
- 1B → 1C: 1C trích số RF tập con của 1B (R6). Nộp 1C sau 1B, hoặc cùng lúc kèm bản tiền in.
- 2 → MT3: cần schema và script trước kịch bản C3.
- 1D không chặn bài nào.

---

## 7. Sổ thay đổi

| Ngày | Thay đổi | Người duyệt |
|---|---|---|
| 02/10/2026 | v1.4: LORO = giữ lại toàn bộ một lần chạy (bỏ định nghĩa "trong lần thiết lập" của v1.2); Bài 1 chạy thêm mốc đánh giá cùng lần chạy (1A-1) | NCS quyết định trong phiên hoàn thiện tiểu luận |
| 02/10/2026 | v1.3: mục 2 tách hai nhà xưởng: khung 1:10 và BIM 1:1 của MT2 ở Khánh Hòa; nhà xưởng hiện trường MT3 ở Đắk Lắk (Phú Yên cũ) | NCS xác nhận trong phiên hoàn thiện tiểu luận |
| 02/10/2026 | Lập v1.0 | NCS duyệt lập (Q6); nội dung chờ NCS duyệt |
| 02/10/2026 | v1.2: (a) LORO = giữ lại lần lặp (trong lần thiết lập); (b) chéo đợt CP2↔CP3 dùng S123; (c) thêm 1A-7, 1A-8, 1A-9 và R4b; (d) không dùng 53 recording ngày 22/07. Bản thảo 1A = v9 | NCS duyệt ("DUYỆT HẾT", P1R4) |
| 02/10/2026 | v1.1: đổi mã bài sang 1A, 1B, 1C, 1D, 2; 1B = bản `main.pdf` (ổn định quyết định); 1C = cấu hình 1, 2, 3 cảm biến × mô hình AI qua ba đợt (theo ý định NCS); viết lại R6, R7, ranh giới 1B – 1C, phụ thuộc | NCS nêu phạm vi 1B, 1C; ma trận chờ NCS duyệt |
