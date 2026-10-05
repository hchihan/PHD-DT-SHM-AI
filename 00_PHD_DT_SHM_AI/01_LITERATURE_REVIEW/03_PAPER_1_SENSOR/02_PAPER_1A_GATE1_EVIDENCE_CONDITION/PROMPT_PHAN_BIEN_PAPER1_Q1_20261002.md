# PROMPT – Phản biện gắt Bài 1 (MT1) để nâng lên tầm Q1, và khai phá dữ liệu sẵn có

> Dùng cho Claude Code tại thư mục gốc luận án `00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM`. Nên bật Zotero MCP.
> Lập ngày 02/10/2026. Văn bản dùng chung: `00_DONG_BO_PIPELINE_VA_PHAN_VUNG_KET_QUA.md` (gọi tắt "tệp 00"), `revision/GD3b_khoang_trong_va_muc_tieu.md` (gọi tắt "GD3b"), `CLAUDE.md`.

---

## 1. Vai trò

Bạn đóng vai **hội đồng phản biện năm người** của một tạp chí SHM hạng cao. Năm người làm việc độc lập, sau đó biên tập viên tổng hợp:

| Mã | Vai | Soi điều gì |
|---|---|---|
| R1 | Chuyên gia SHM dao động, liên kết bu lông | Thiết kế thí nghiệm; tính đại diện của khung 1:10; trạng thái liên kết; ảnh hưởng của kích thích và môi trường; ý nghĩa vật lý của kết quả |
| R2 | Chuyên gia học máy, rò rỉ dữ liệu, đánh giá | Cách chia dữ liệu; rò rỉ (cửa sổ, chuẩn hóa, siêu tham số); đơn vị độc lập; so sánh mô hình công bằng hay không |
| R3 | Nhà thống kê | Cỡ mẫu thật (số run, số campaign); kiểm định hoán vị và giả định hoán đổi; khoảng bất định; nhiều phép so sánh |
| R4 | Phản biện "đóng góp và định vị" | Bài mới ở đâu so với [19] Ramasso 2025, [15] Wheat 2024, [18], [14], [53], [56], [48], Eraliev 2022; câu hỏi "so what?" cho người làm SHM |
| R5 | Phản biện tái lập | Dữ liệu, mã, registry, SHA-256, `method_version`; người khác có chạy lại ra đúng số không |
| ED | Biên tập viên | Tổng hợp; ra quyết định (reject / major / minor); nêu điều kiện tối thiểu để vào vòng phản biện ở Q1 |

**Giọng phản biện:** gắt, cụ thể, có căn cứ. Mỗi nhận xét phải chỉ dòng hoặc mục trong bản thảo, nói vì sao đó là vấn đề, và cần gì để sửa. Không khen chung chung. Không nhận xét về câu chữ khi lỗi nội dung chưa được nêu hết.

**Ngôn ngữ:** báo cáo cho NCS viết tiếng Việt. Câu đề xuất chèn vào bản thảo viết tiếng Anh học thuật.

---

## 2. Nguồn phải đọc (đọc toàn bộ; tệp dài thì đọc theo phần)

**Bản thảo:**
1. `01_LITERATURE_REVIEW/03_OUTPUTS/01_TIEU_LUAN_TONG_QUAN/PAPER_DRAFTING/Q1_PAPER1_v8_SHM_pre_SUBMISSION_13.09.2026.docx` – bản chính.
2. `03_OUTPUTS/03_PAPER_1A_GATE1/pptx/Paper 1.md/`:
   - `PAPER1_v8.1_SHM_RISK_REDUCED.docx`; ghi rõ khác v8 ở đâu và bản nào mới hơn;
   - các tệp `…CHANGELOG`, `…COMPLIANCE_CHECK`, `…PRE_SUBMISSION_AUDIT`, `…NEW_REFERENCE_AUDIT`;
   - `LITERATURE_GAPS_FOR_PAPER1.md`, `CEI_SCIENTIFIC_BASIS_…`, `GATE3_SCIENTIFIC_BASIS_…`, `PAPER1_SOURCE_AND_RESULT_TRACEABILITY_MATRIX_…csv`.

**Căn cứ điều hành:**
3. Tệp 00: mục 2 (quy ước dữ liệu), mục 3 (pipeline chuẩn), mục 4 (B1-1 đến B1-6), mục 5 (ma trận sở hữu kết quả).
4. GD3b phần MT1 và A1; `CLAUDE.md` Quyết định 4, 13.

**Tài liệu gần nhất:** ghi chú trong `notes/`:
- `RWHW6F9I` [19];
- `RG9FMT8Y` [15];
- `VPFBB9SG` [18];
- `L97BIAI3` [14];
- `JQKJGUER` [53];
- `IW7JBB3E` [56];
- `SL6IEB2E` [48];
- `VVBGM9EN` Eraliev 2022;
- `2ZJSENQU` Maes 2022.

**Dữ liệu và mã:** `02_DATA_CODE_AND_EXPERIMENTS/`. Gồm registry 216 recording, kết quả từng fold, cấu hình chạy.
- Thư mục chưa được kết nối thì ghi `MISSING` và dừng ở phần cần dữ liệu. Không suy đoán số.

**Tạp chí:** đích dự kiến là *Structural Health Monitoring* (SAGE).
- Hạng Q, phạm vi bài nhận và giới hạn độ dài: kiểm trên trang tạp chí và SJR, ghi nguồn và ngày truy cập. Không kiểm được thì ghi `[CẦN KIỂM]`.
- Đề xuất thêm 2–3 tạp chí dự phòng, cũng phải kiểm như trên.

---

## 3. Ràng buộc (không vi phạm)

1. **MT1 là tối thượng.** Bài phải đạt tiêu chí MT1: chênh lệch giữa đánh giá cùng lần chạy và LORO, LOCO; khai báo phạm vi hiệu lực cho từng kết quả. Bài điều chỉnh theo MT1, không điều chỉnh MT1 theo bài.
2. **Ma trận sở hữu kết quả (tệp 00, mục 5).** B1 sở hữu R1–R5.
   - Không đưa vào B1 làm kết quả mới các phần sau: R6 (7 tập con cảm biến, regret, τb – thuộc BT-A); R7 (cấu hình × thuật toán trên CP1 – thuộc BT-B); R11 (OMA – FEM – thuộc BT-C).
   - Phân tích nào chạm ranh giới thì tách thành **đề xuất đổi ma trận**, kèm lý do, chờ NCS duyệt.
3. **Không bịa số liệu, trích dẫn, DOI.** Mọi con số lấy từ bản thảo hoặc tệp kết quả, ghi rõ nơi lấy. Phân tích chưa chạy chỉ được mô tả là kế hoạch, kèm `[DATA-PENDING]`.
4. **Định vị khoảng trống A1 theo GD3b.** [19] đã định lượng chênh lệch cho phát xạ âm trên dầm nhôm; [15] cho ổ trục. Phần mới của B1 là ba điều cộng lại: dao động trên khung thép nhiều liên kết, bốn mô hình, khai báo phạm vi.
   - Không dùng "đầu tiên", "chưa ai".
   - Có tìm thêm tài liệu thì ghi nhật ký truy vấn (công cụ, chuỗi tìm, ngày). Nguồn chưa đọc toàn văn gắn `[CHƯA ĐỌC TOÀN VĂN]`.
5. **Quy ước dữ liệu (tệp 00, mục 2):**
   - Campaign: CP1–CP3.
   - Nhãn: S0, B1, B2, B3, không có thứ tự.
   - Cấu hình: S12 dùng chung cho ba campaign; S123 chỉ phân tích trong CP2, CP3.
   - Không khẳng định tương tự động lực học của khung 1:10.
6. **Không sửa tệp gốc.** Mọi sản phẩm ghi vào `03_PAPERS/PAPER_1/review_YYYYMMDD/` (đường dẫn: [NCS XÁC NHẬN]). Bản thảo mới có hậu tố phiên bản.
7. **Khóa trước khi chạy.** Phân tích mới chỉ chạy sau khi NCS duyệt danh sách (Pha 3). Giao thức được ghi và commit trước lần chạy đầu. Không chọn phân tích sau khi đã thấy kết quả.

---

## 4. Quy trình – dừng ở mỗi ĐIỂM DỪNG

### Pha 0 – Kiểm kê (không nhận xét)
- Liệt kê mọi phiên bản bản thảo, ngày sửa, khác biệt chính. Chốt bản dùng để phản biện.
- Trích "hồ sơ sự kiện" của bài thành bảng: câu hỏi; dữ liệu (campaign, run, recording, cửa sổ, kênh, cấu hình); pipeline; mô hình; giao thức; mọi con số chính, kèm bảng hoặc dòng nguồn; đóng góp tuyên bố; giới hạn tự nêu.
- Đối chiếu hồ sơ sự kiện với tệp 00 mục 2–4. Liệt kê các điểm lệch.
- **Sản phẩm:** `P1R0_kiem_ke_YYYYMMDD.md`. → **ĐIỂM DỪNG 0**

### Pha 1 – Phản biện độc lập (R1–R5)
Mỗi người viết một báo cáo theo mẫu tạp chí. Trước khi viết, mỗi người phải **tự trả lời** các câu bắt buộc ở mục 5.

Mỗi báo cáo gồm:
- Tóm tắt bài trong 3 câu, theo cách người phản biện hiểu.
- **Major issues**, đánh số. Mỗi mục ghi: vị trí; vấn đề; vì sao ảnh hưởng tới kết luận; yêu cầu sửa; ước lượng công sức (S / M / L) và có cần dữ liệu mới không.
- **Minor issues.**
- Khuyến nghị: reject / major / minor, kèm lý do.

→ **ĐIỂM DỪNG 1** (gửi năm báo cáo, chưa tổng hợp)

### Pha 2 – Tổng hợp của biên tập viên và khoảng cách tới Q1
- Gộp các nhận xét trùng. Xếp hạng theo mức chặn: **Chặn** (không sửa thì bị từ chối), **Nặng**, **Nhẹ**.
- Lập **bảng khoảng cách tới Q1**: tiêu chí (tính mới; độ chặt của đánh giá; tính tổng quát; tái lập; ý nghĩa cho người làm SHM; trình bày) × hiện trạng × yêu cầu Q1 × việc cần làm × công sức × phụ thuộc dữ liệu.
- Đối chiếu với B1-1 đến B1-6 (tệp 00, mục 4). Nêu việc nào trùng, việc nào mới phát sinh.
- Đánh giá thẳng: với dữ liệu hiện có (3 campaign, 18 run), bài đạt được mức nào; phần nào chỉ đạt khi có dữ liệu mới.
- **Sản phẩm:** `P1R2_tong_hop_va_khoang_cach_Q1_YYYYMMDD.md`. → **ĐIỂM DỪNG 2**

### Pha 3 – Khai phá tiềm năng dữ liệu sẵn có
Lập danh mục **phân tích ứng viên chạy được trên dữ liệu hiện có**. Mỗi ứng viên là một dòng, gồm:
- câu hỏi nó trả lời;
- dữ liệu dùng;
- thiết kế (đơn vị độc lập, đối chứng, thống kê);
- giá trị cho Q1 (cao / trung bình / thấp) và vì sao;
- công sức;
- rủi ro rò rỉ hoặc diễn giải sai;
- **chủ sở hữu theo tệp 00** (B1, hay chạm BT-A / BT-B / BT-C).

Các hướng **gợi ý để đánh giá, không bắt buộc**:
- **Định lượng mức lạc quan (lõi A1):**
  - cùng lần chạy → LORO → LOCO, cho 4 mô hình trên S12, cả ba campaign;
  - so thêm với chia ngẫu nhiên theo cửa sổ, để có thang "thổi phồng" đầy đủ.
- **Đường cong học** theo số run huấn luyện (1…5): kết quả phụ thuộc cỡ mẫu thật ra sao.
- **Đơn vị độc lập theo kiểu kích thích** (nếu mỗi run có nhiều kiểu kích thích): giữ lại một kiểu kích thích, xem như một chiều của phạm vi hiệu lực.
- **Giải thích sự sụt giảm ở CP3:**
  - đo độ dịch chuyển phân bố giữa các campaign (ví dụ MMD, khoảng cách phổ);
  - nối với khác biệt về giao thức đo đã biết;
  - không suy ra quan hệ nhân quả.
- **Độ bất định và phạm vi hiệu lực ở mức từng dự đoán:** hiệu chỉnh xác suất (calibration), dự đoán phù hợp (conformal) theo nhóm run hoặc campaign, cờ "ngoài phạm vi". Đây là cầu nối sang trường `uncertainty` và `scope` của `EVIDENCE` (MT2).
- **Nested CV cho siêu tham số:** xử lý vi phạm 15/18 fold mà bản thảo tự nêu.
- **Kiểm định hoán vị theo khối** (hoán vị nhãn ở mức run hoặc recording), kèm bàn về giả định hoán đổi.
- **Xuất bản ghi `EVIDENCE`** cho mỗi kết quả, làm phụ lục hoặc dữ liệu bổ sung.
- **Bộ dữ liệu mở và registry:** công bố dữ liệu kèm bài (hoặc Data in Brief riêng – cân nhắc vì R1 thuộc B1).

Sau danh mục, đề xuất **gói tối thiểu cho Q1**: số ít phân tích có giá trị cao nhất trên công sức. Kèm thứ tự chạy và tiêu chí dừng.

Phân tích nào chạm R6, R7, R11 thì ghi riêng thành **đề xuất đổi ma trận**.

- **Sản phẩm:** `P1R3_tiem_nang_du_lieu_YYYYMMDD.md` và bảng `P1R3_ung_vien_phan_tich.csv`. → **ĐIỂM DỪNG 3** (NCS chọn gói, rồi khóa giao thức)

### Pha 4 – Kế hoạch sửa và đề cương v9
- Kế hoạch sửa theo từng mục của bài: Title, Abstract, Introduction, Related work, Method, Results, Discussion, Limitations, Data/Code availability.
  - Với mỗi mục ghi: nhận xét được xử lý; việc cần làm; phân tích từ gói đã chọn; `[DATA-PENDING]` ở chỗ cần số.
- Viết lại tiêu đề (2–3 phương án), tóm tắt và danh sách đóng góp bằng tiếng Anh, chỉ dùng số đã có. Số mới để placeholder.
- Bảng **trả lời phản biện dự kiến**: nhận xét Chặn/Nặng → cách xử lý → vị trí sửa.
- **Sản phẩm:** `P1R4_ke_hoach_sua_v9_YYYYMMDD.md`. → **ĐIỂM DỪNG 4**

Pha chạy phân tích và viết bản v9 là phiên riêng, chỉ bắt đầu khi NCS duyệt Pha 4.

---

## 5. Câu hỏi bắt buộc cho phản biện (tự trả lời ở Pha 1)

**R1 – SHM:**
- Bốn trạng thái là can thiệp ở bốn vị trí khác nhau. Bài đang phân loại "trạng thái liên kết" hay "vị trí can thiệp"? Điều đó ảnh hưởng gì tới ý nghĩa SHM?
- Không có số liệu lực siết hay mô-men xoắn. Vậy "trạng thái" được định nghĩa và tái lập thế nào?
- Khung 1:10 đại diện cho điều gì? Giới hạn ngoại suy có được nói đủ và đúng chỗ không?
- Kích thích, nhiệt độ, thời điểm đo khác nhau giữa campaign có được ghi lại không?

**R2 – Học máy:**
- Đâu là đơn vị độc lập thật: run, recording hay campaign? 6 run mỗi campaign có đủ để nói về hiệu năng không?
- Chuẩn hóa theo từng cửa sổ, chọn siêu tham số, chọn ứng viên theo validation: còn đường rò rỉ nào chưa đóng?
- So sánh RF / SVM (1 seed, không tinh chỉnh) với học sâu (3 seed, có phát triển siêu tham số trước) có công bằng không?
- Chấm theo bản ghi bằng trung bình xác suất cửa sổ có làm khuếch đại hiệu năng không?

**R3 – Thống kê:**
- Khoảng bất định của Macro-F1 với 18 recording kiểm tra mỗi fold là bao nhiêu?
- Giả định hoán đổi của kiểm định hoán vị có hợp lý khi recording trong cùng run phụ thuộc nhau?
- Có hiệu chỉnh cho nhiều phép so sánh không?

**R4 – Đóng góp:**
- Viết một câu "điều người làm SHM biết sau khi đọc bài mà trước đó chưa biết". Câu đó có đứng được trước [19] và [15] không?
- Nếu hiện tại chưa đứng được, thì phân tích nào ở Pha 3 làm nó đứng được?

**R5 – Tái lập:**
- Người ngoài có tải được dữ liệu, mã, cấu hình, và chạy lại ra Bảng 4 không?
- Còn ba điểm nguồn gốc dữ liệu chưa kiểm mà bản thảo tự nêu. Đó là những điểm nào, và ảnh hưởng gì?

---

## 6. Định dạng báo cáo sau mỗi pha

1. Đã làm gì (≤ 5 dòng).
2. Tệp đã tạo (đường dẫn).
3. Phát hiện quan trọng nhất: tối đa 5 dòng, xếp theo mức chặn.
4. Câu hỏi cần NCS quyết định.
5. Việc kế tiếp.

## 7. Tự kiểm

- [ ] Mọi nhận xét chỉ dòng hoặc mục cụ thể, kèm yêu cầu sửa.
- [ ] Mọi con số có nguồn (bảng, dòng, tệp kết quả). Không có số mới tự tạo.
- [ ] Hạng Q và phạm vi tạp chí đã kiểm có nguồn, hoặc ghi `[CẦN KIỂM]`.
- [ ] Không có kết quả của BT-A, BT-B, BT-C bị kéo vào B1 mà chưa có đề xuất đổi ma trận.
- [ ] Quy ước nhãn, campaign, cấu hình khớp tệp 00.
- [ ] Đã dừng ở mỗi ĐIỂM DỪNG.

**Bắt đầu bằng Pha 0.**
