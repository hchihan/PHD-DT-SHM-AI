# HT0 – Chẩn đoán Tiểu luận tổng quan (Pha 0, không sửa tệp)

Ngày: 02/10/2026. Theo `PROMPT_HOAN_THIEN_TIEU_LUAN_20261002.md`, Pha 0.
Đầu vào đã đọc hết: 10 tệp `tieuluan/` (bản lưu 02/10, 11:0x), `CLAUDE.md` (toàn bộ), `revision/GD3b_khoang_trong_va_muc_tieu.md`,
`danh_sach_cau_gioi_han_v2.csv`, `GD5_ra_soat_cau_gioi_han.md`, `GD5_ra_soat_tai_lieu_cau.md`, `nhap_khai_bao_AI_tao_sinh.md`,
`thieu_toan_van.md`, `L1_1_so_lieu_KCN_da_kiem.md`, `matrix/doi_chieu_danh_muc.csv`, `matrix/literature_matrix.csv`.
**Không có trong thư mục được cấp:** tài liệu G1 (danh sách N1–N13 gốc) và `../00_DONG_BO_PIPELINE_VA_PHAN_VUNG_KET_QUA.md`
(nằm ở `03_OUTPUTS/`, ngoài quyền truy cập). Danh sách N1–N17 kiểm theo bảng trong prompt.

Quy ước: **Đạt** · **Yếu** (có nhưng chưa rõ, rải rác hoặc chưa đủ tiêu chí) · **Thiếu** · **Mâu thuẫn** (hai chỗ nói khác nhau).
Số dòng theo tệp hiện hành.

---

## 1. Tóm tắt

1. Nội dung lõi đã đúng hướng khóa 01–02/10: hai khoảng trống (5.2), ba mục tiêu (5.3.3), ba RQ (5.4), B0/B1, schema 6 thực thể – 5 ràng buộc (Phụ lục A, B), không có kết quả Paper 1, không còn K1–K3/UV-xx.
2. Điểm yếu lớn nhất nằm ở **Chương 1**: 1.5 và 1.6 vẫn chia vấn đề thành ba – bốn mạch (bằng chứng; định danh – truy vết; hành động; song sinh số), là dấu vết của ba khoảng trống cũ, nên 1.8.4 còn ghi "Ba khoảng trống". T1 chưa có một câu luận đề nhất quán từ Dẫn nhập tới 5.3.
3. **T3 và T4 thiếu bảng tổng hợp** mà tiêu chí yêu cầu: chưa có bảng RQ – phương pháp – dữ liệu – chỉ số – đối chứng – kế thừa – khác tiền lệ; 5.8 chưa tách đóng góp khoa học và thực tiễn; M1–M4 chưa được gọi tên trong thân bài.
4. Có **4 mâu thuẫn nội dung mới** cần xử lý trước Pha 2: định nghĩa bằng chứng trạng thái ở 3.1.3 trái với 1.3; Ch.4 và Bảng thuật ngữ nói luận án dùng IDS/SHACL/SOSA trong khi §8 khóa script Python, không RDF; 3.3.1 gán "cấu hình cảm biến" cho RQ1; 5.9.4 nói "đang tiếp tục rà soát" trái QĐ 11.
5. N1–N17: còn 13, đã xử lý 3 (N10, N16, N17), xử lý một phần 1 (N12). Bổ sung 20 lỗi mới (N18–N37).

---

## 2. Ma trận bốn trục

### T1. Mục đích nghiên cứu

| Vị trí | Đánh giá | Dẫn chứng |
|---|---|---|
| Dẫn nhập | Yếu | Có tình huống C3, hai khoảng trống, ba mục tiêu (dòng 15–17); **không có câu luận đề**. "Cho ai" chỉ ngầm qua "người điều tra". |
| 1.4 | Đạt | Ba câu hỏi của người quản lý, nối với ba phần của luận án (dòng 87–89). |
| 1.5 | Mâu thuẫn | 1.5.1 phát biểu "vấn đề quản lý trung tâm" theo trục truy vết (dòng 97); 1.5.2, 1.5.3, 1.5.4 là ba mạch vấn đề, trong đó 1.5.3 (định danh – truy vết) là K2 cũ đã hạ thành ràng buộc C3 (QĐ 9). Không nhắc hai khoảng trống. |
| 1.6 | Yếu | Bốn "sự cần thiết" (1.6.1–1.6.4) không ánh xạ vào hai khoảng trống; 1.6.3 đẩy kiểm chứng hiện trường sang "các chuyên đề tiếp theo", trong khi MT3 thuộc luận án. |
| 1.8.4 | Mâu thuẫn | "Ba khoảng trống được phản biện và phát biểu chính thức tại Chương 5" (dòng 226) – N1. |
| 1.9 | Yếu | RQ1–RQ3 tóm đúng (dòng 320); nhưng 1.9.2 "bốn lớp" ứng với "bốn loại bằng chứng" (dòng 326) làm đứt quan hệ 1:1 MT–RQ. |
| 5.2 | Đạt | Hai khoảng trống, mỗi khoảng trống có: đã giải quyết – còn chưa chắc – vì sao cần – nghiên cứu này kiểm gì (khớp GĐ3b Phần D). Nhãn trong văn bản là "Khoảng trống A/B"; vế A1/A2 chỉ gọi "vế thứ nhất/thứ hai" (dòng 77) – xem N28. |
| 5.3 | Đạt / Yếu | Luận đề 5.3.1 (dòng 103) khớp luận điểm trung tâm của CLAUDE §1. Bảng MT 5.3.3 nối MT1↔A, MT2↔B(+A), MT3↔A,B. Chưa nói rõ A2 chia giữa MT1 (khai báo) và MT2 (kiểm tại lần dùng), dù 5.2.1 dòng 81 đã ngầm nêu. |
| 5.11 | Yếu | Câu kết "Quản lý, liên kết và truy vết thông tin…" (dòng 401) là câu định vị khác với luận đề 5.3.1. |

**Kết luận T1: Yếu.** Cần một câu luận đề dùng nguyên văn (hoặc rút gọn cố định) ở Dẫn nhập, 1.5 hoặc 1.9, 5.3.1, 5.11; viết lại 1.5 theo hai khoảng trống.

### T2. Đối tượng và phạm vi

| Vị trí | Đánh giá | Dẫn chứng |
|---|---|---|
| 1.2 (tiêu đề), 1.2.4 | Yếu | "Đối tượng nghiên cứu: nhà công nghiệp khung thép liên kết bu lông" – thực chất là **khách thể**. Đối tượng theo tiêu chí (liên kết bu lông, bằng chứng trạng thái, chuỗi bằng chứng – hành động) chưa được nêu thành một câu. 1.2.4 thêm "một tầng" – chỉ xuất hiện ở đây. |
| Khách thể | Thiếu | Không có từ "khách thể" ở đâu. |
| Phạm vi không gian – thời gian | Thiếu | Rải rác: Việt Nam (1.1.4, B0), một nhà xưởng (MT3), 3–6 tháng (5.5.2), tài liệu 2018–2026 (1.8.5). Không có chỗ nêu gộp. |
| 1.3 vs 3.1.3 | **Mâu thuẫn** | 1.3: bằng chứng là nhận định từ ba nguồn (mô hình, kỹ sư, NDT), khác kết quả phân loại (Bảng 1.1). 3.1.3 dòng 33: "đầu ra của một mô hình phân loại … được gọi là bằng chứng trạng thái". |
| 1.7.3 | Yếu | Tách "đối tượng tổng quan" và "đối tượng ứng dụng" – đúng ý, nhưng thêm một cách gọi thứ ba. |
| Mức tích hợp (bóng số) | Mâu thuẫn với tiêu chí "nêu một lần" | Khai báo lặp ở Dẫn nhập, 1.1.3, 1.6.4, 1.7.1, 1.9.3, 2.5, 5.3.2, 5.6.6, 5.11 (9 chỗ), câu chữ gần như nhau. Nội dung không mâu thuẫn. |
| 5.9.1 (Bảng 5.5) | Đạt | Phân lớp phạm vi rõ; khớp 1.7.4. |
| Phụ lục A | Đạt | 6 thực thể, trường bắt buộc, EVIDENCE_USE, Bảng A.3, A.4; khớp CLAUDE §8. |

**Kết luận T2: Yếu (có một mâu thuẫn định nghĩa).** Đề xuất một tiểu mục "Đối tượng, khách thể và phạm vi" ở 1.2.4 hoặc 1.7, các nơi khác trỏ về.

### T3. Sự tương thích của phương pháp

| Vị trí | Đánh giá | Dẫn chứng |
|---|---|---|
| 1.8 (phương pháp tổng quan) | Yếu | Tổng quan theo chủ đề có cấu trúc, tự nhận không PRISMA (dòng 314) – trung thực. Nhưng: (a) 1.8.2 "chín nhóm chủ đề" khác 5 cụm của ma trận (CLAUDE 7.4); (b) 1.8.5 không nhắc việc dùng Consensus để gợi ý tài liệu, trong khi bản khai báo AI có nêu; (c) 1.8.5 dài 2.619 từ, lặp 1.8.1 và 5.9.4. |
| 3.4 | Yếu | LORO, LOCO, đánh giá theo nhóm, kiểm định hoán vị có căn cứ đầy đủ. **"Đánh giá cùng lần chạy"** – mốc đối chứng của A1 – không được định nghĩa ở 3.4 hay Bảng thuật ngữ; chỉ xuất hiện từ 5.2. |
| 3.3.1 | Mâu thuẫn | "cấu hình cảm biến giữ vai trò hỗ trợ cho RQ1 (đánh giá … dưới các cấu hình khác nhau)" (dòng 85) – RQ1/MT1 không có biến cấu hình cảm biến. |
| 5.4–5.5 | Yếu | RQ1 ↔ cùng lần chạy/LORO/LOCO, ba đợt, seed/fold, hoán vị: có. **Chỉ số hiệu năng của RQ1 chưa được gọi tên.** RQ2 ↔ lỗi chèn mù, B0, B1: có; **M1–M4 không được gọi tên trong thân bài** (5.5.2 Bước 2 chỉ ghi "bốn chỉ số"). RQ3 ↔ Bước 4 có kịch bản đầu cuối nhưng không nối tên với kịch bản cột C3 của 1.4. |
| 5.7 | Đạt | Vai trò AI theo gói, lý do đổi từ phân loại sang phát hiện bất thường lập luận bằng tài liệu (5.7.3), không dùng kết quả Paper 1. |
| Ch.4, Bảng thuật ngữ | **Mâu thuẫn** | 4.4.3 dòng 118: "Luận án dùng cơ chế thứ nhất (IDS) … và cơ chế thứ hai (ràng buộc ngữ nghĩa)"; Bảng 4.2 dòng 178: "Bản ghi bằng chứng nên đặt trên lớp quan trắc chuẩn"; thuật ngữ: SHACL "Luận án dùng để kiểm chứng", SOSA "Luận án đặt bản ghi bằng chứng trên lớp này". CLAUDE §8 và A.5, B.1: script Python trên SQLite, không RDF/SHACL, ánh xạ SOSA/SSN chỉ bằng một bảng. |
| Phụ lục B | Đạt | C1, C3, C5, C6, C9 phát biểu kiểm được; Bảng B.2 nối nhóm lỗi – ràng buộc – B0/B1; B.3 nêu tiền lệ [21], [44]. |
| Bảng tổng hợp "vì sao phù hợp – kế thừa – khác tiền lệ" | Thiếu | Nội dung rải ở 5.8.1 ([19], [15]), 5.8.2, 2.2.3, B.3; chưa có một bảng hay đoạn gom. |

**Kết luận T3: Yếu.** Cần bảng RQ – phương pháp – dữ liệu – chỉ số – đối chứng – kế thừa từ – khác tiền lệ ở 5.5 (đề xuất trong Pha 2).

### T4. Đóng góp khoa học và thực tiễn

| Vị trí | Đánh giá | Dẫn chứng |
|---|---|---|
| 5.8 | Yếu | Chia theo mục tiêu (5.8.1 thực nghiệm – phương pháp; 5.8.2 artefact; 5.8.3 khả thi; 5.8.4 ngành), **chưa tách khoa học / thực tiễn**. Nội dung cần có đều đã có: A1 (5.8.1), A2 + G-B đo bằng chênh lệch với B1 (5.8.2 dòng 322), B0 là đóng góp bối cảnh Việt Nam (dòng 322), MT3 (5.8.3). |
| 5.8.1 | Mâu thuẫn nhỏ | "bốn họ mô hình" (dòng 307) – N3. |
| Bảng 5.1 | Đạt | Cột "phần còn lại" khớp hai khoảng trống. Bốn dòng cuối (SOSA, IDS, quần thể, VoI) nêu "phần còn lại" không thuộc MT nào – xem N19. |
| 5.2 | Đạt | Ghi "Sau nghiên cứu, người quản lý có …" ở cuối mỗi khoảng trống. |
| Từ tuyệt đối | Yếu | "bác bỏ mọi tuyên bố về tính mới" (5.1.3 dòng 27); "đã là bài toán có lời giải" (1.1.2 dòng 15). |

**Kết luận T4: Yếu (cấu trúc, không phải nội dung).** Đề xuất Bảng "Đóng góp khoa học – Đóng góp thực tiễn" ở 5.8 trong Pha 2.

### Trục phụ

| Trục | Đánh giá | Dẫn chứng |
|---|---|---|
| Tính cấp thiết (1.6) | Yếu | Chưa nối với bối cảnh Việt Nam (1.1.4: NĐ 207/2026 yêu cầu hồ sơ bảo trì; QĐ 258 yêu cầu cập nhật BIM cho vận hành) và chưa nối với hai khoảng trống. |
| Câu hỏi nghiên cứu (5.4) | Đạt | Ba RQ đo được, có đối chứng; 5.4.4 logic kế tiếp. Thiếu tên chỉ số RQ1 (xem T3). |
| Cấu trúc luận án dự kiến (1.10, 5.10) | Thiếu | 1.10 chỉ mô tả cấu trúc tiểu luận. Cấu trúc luận án (5 chương theo ba mục tiêu, CLAUDE §13) chỉ có một câu ở ghi chú Bảng 5.2. |

---

## 3. Kiểm lại N1–N17

| Mã | Trạng thái | Kiểm thực tế |
|---|---|---|
| N1 | **Còn** | ch1:226 "Ba khoảng trống"; ch5:367 "Ba khoảng trống nghiên cứu trong tập tài liệu đã kiểm chứng". Đúng vị trí. Gốc rễ: 1.5 còn ba mạch (xem T1). |
| N2 | **Còn** | thuatngu:58 `Action_Status` = "Bình thường, Theo dõi, Kiểm tra, Kiểm tra ưu tiên". Thiếu dòng `priority_level`. |
| N3 | **Còn** | ch5:268 "Họ mô hình thứ nhất … Họ thứ hai"; ch5:307 "bốn họ mô hình". |
| N4 | **Còn** | ch1:69 "đợt lắp đặt"; ch3:109 "Đợt thí nghiệm → lần lắp đặt / trạng thái lắp ráp → lần chạy hoặc lần thu → cửa sổ"; ch5:270 "điểm được chấm theo bản ghi"; PL:57 "đợt lắp đặt (lần lắp ráp hoặc lần can thiệp gần nhất)". Bốn cách gọi: đợt lắp đặt / lần lắp đặt / lần lắp ráp / `install_batch`. Bảng thuật ngữ chưa có mục nào. Thêm "đánh giá cùng lần chạy" (N29). |
| N5 | **Còn** | ch5:286, ch5:298 "đường cơ sở B0"; PL:69 tiêu đề "Đường cơ sở B0 và đối chứng B1". |
| N6 | **Còn** | Không có "M1"–"M4" trong Ch.5; PL:7 "chỉ số M1 (Mục 5.5)"; PL:126, 136 dùng M2. |
| N7 | **Còn** | PL: Bảng A.1, A.3, A.4, B.1, B.2 (không có A.2); tiểu mục A.3 là "Định nghĩa" nhưng Bảng A.3 nằm ở A.4 – dễ nhầm. ch5:216 "(Mục 5.6.2)" nằm trong 5.6.2. |
| N8 | **Còn** (đúng số) | 84 số cũ: không trích [63], [65], [77], [80], [84]; 33 khóa `@KEY` chưa có trong `99_tailieu.md`. `99_tailieu.md` lưu 27/09, chưa cập nhật. |
| N9 | **Còn** | ch3:127 "Ramasso … (2024)" – danh mục và `doi_chieu` ghi 2025 (trực tuyến 2024). ch2:34 "Kamariotis và cộng sự (2022)" – danh mục, `doi_chieu`, CLAUDE 7.2 ghi 2023. |
| N10 | **Đã xử lý** | Không còn K1–K3, UV-xx. Lưu ý: văn bản dùng "Khoảng trống A/B", không dùng "G-A/G-B", và không gắn nhãn A1/A2 (N28). |
| N11 | **Còn** | `[CẦN NGUỒN: IFC4 ADD2 TC1]` ch2:58, ch4:148, ch5:85; `[CẦN NGUỒN: Khuyến nghị W3C SSN]` ch4:40, ch5:77, PL:95, 96, 140. Chưa nhập Zotero (`thieu_toan_van.md` mục D). |
| N12 | **Một phần** | KCN (ch1:39): đã kiểm nguyên văn `XM5ZUP99` (`L1_1_so_lieu_KCN_da_kiem.md`); còn thiếu ngày truy cập trong danh mục (khóa chưa vào `99_tailieu`). NĐ 207/2026 (ch1:29): NCS xác nhận hiệu lực (changelog phiên 01/10 (7)); mục [11] không có ngày ban hành, nơi đăng, URL, ngày truy cập; nội dung Điều 34, 37 chưa có ghi chú đối chiếu nguyên văn trong `revision/`. |
| N13 | **Còn** | thuatngu:10 "tính bền vững của nó là vấn đề nghiên cứu ở Mục 2.2.4"; 2.2.4 trình bày như giới hạn. |
| N14 | **Còn** | ch5:25 "Seiß và cộng sự (2025) dùng trực tiếp định danh IFC để gắn hồ sơ kiểm tra với cấu kiện \[82\]". |
| N15 | **Còn** | ch5:278 câu Ghazimoghadam `G98ZWHKW` ở mức chi tiết ("phát hiện bu lông liên kết bị nới lỏng trên kết cấu phòng thí nghiệm"); PDF chưa có. |
| N16 | **Đã xử lý** | 2.1.1 dòng 11 chỉ nêu tên, phạm vi, ấn bản; có chú thích ẩn dòng 12. |
| N17 | **Đã xử lý** trong văn bản | 4.3.1 còn [64], [66]; 4.5.3 còn [78]; [63], [65], [77] đã bỏ khỏi thân bài, còn trong danh mục (gộp vào N8). Ý [78] ở 4.5.3 "rà soát kết quả sửa chữa" chưa kiểm toàn văn (GD5). |

---

## 4. Lỗi mới tìm thấy (N18–N37)

| Mã | Lỗi | Vị trí | Nhóm Pha |
|---|---|---|---|
| N18 | Định nghĩa bằng chứng trạng thái = đầu ra mô hình phân loại, trái 1.3 và Bảng 1.1 | ch3:33 | P1 thuật ngữ |
| N19 | Văn bản nói luận án dùng IDS, SHACL, đặt bản ghi trên SOSA – trái §8 (script Python, SQLite, không RDF) | ch4:118; ch4:178 (Bảng 4.2); thuatngu:23, 28; Bảng 5.1 dòng 64–65 | P1 / P2-T3 |
| N20 | "Cấu hình cảm biến hỗ trợ RQ1 … dưới các cấu hình khác nhau" – ngoài MT1 | ch3:85 | P2-T3 |
| N21 | "đang tiếp tục rà soát" trái QĐ 11; câu "Ba khoảng trống … trong tập tài liệu đã kiểm chứng" thiếu vị ngữ | ch5:367 | P1 |
| N22 | Đường dẫn hình `../figures/…` không tồn tại (hình nằm ở `TLTQ_28.09.2026/figures/`); bốn hình vẽ trước khi khóa schema 01/10, cần kiểm khớp 6 thực thể | ch1:125; ch5:209, 222, 317 | P1 đánh số |
| N23 | Bảng không số (bảng MT ở 5.3.3); Bảng 2.1, 4.2, 5.1–5.5 không được nhắc trong văn bản trước khi xuất hiện; kiểu chú thích bảng không đồng nhất (`*Bảng 1.1*` vs `<span>`) | ch5:129; ch2:86; ch4:166; ch5:51, 173, 239, 290, 338 | P1 đánh số |
| N24 | Bảng thuật ngữ thiếu: BCF, IFC 4.3, bóng số (DS/DT/DM), B0, B1, M1–M4, đánh giá cùng lần chạy, EOV, autoencoder, `priority_level`, `STATUS_EVENT`, `EVIDENCE_USE`, RQ/WP/MT. "Hồ sơ kiểm tra" (thuật ngữ, Ch.1, 4, 5) và "bản ghi kiểm tra" (Phụ lục) dùng lẫn cho `INSPECTION_RECORD` | thuatngu | P1 thuật ngữ |
| N25 | Khai báo bóng số lặp 9 chỗ (T2 yêu cầu nêu một lần) | xem T2 | P2-T2 |
| N26 | 1.8.2 "chín nhóm" ≠ 5 cụm của ma trận; 1.8.5 không nêu dùng Consensus | ch1:216, 228–314 | P2-T3 |
| N27 | Ngôi viết lẫn: "Tiểu luận" (40), "luận án" (66), "nghiên cứu này" (11), "Nghiên cứu" (9), "nghiên cứu sinh" (5) | toàn văn | P3 |
| N28 | Nhãn khoảng trống: văn bản "Khoảng trống A/B", "vế thứ nhất/thứ hai"; CLAUDE và prompt dùng G-A (A1, A2), G-B | ch5:73–95, 107–111, 131–133; Dẫn nhập | P1 thuật ngữ (cần NCS chọn) |
| N29 | "Đánh giá cùng lần chạy" chưa định nghĩa ở 3.4 – là mốc đối chứng của A1 | ch3 3.4.3; ch5 | P2-T3 |
| N30 | Lỗi nhỏ: câu hỏng ngữ pháp 1.6.4 ("vai trò của con người … mà Wu và cộng sự cũng đã được đặt ra"); thiếu dấu chấm sau \[41\]; "**.**" thừa; "máy vectơ/máy véc-tơ"; "mạng phần dư/mạng dư" | ch1:158, 348; ch2:102; ch5:123, 268 | P1 |
| N31 | \[23\] UCLA Factor Building (nhà văn phòng) đặt trong đoạn về nhà công nghiệp – CLAUDE 4.1 cấm làm căn cứ cho luận điểm nhà công nghiệp | ch2:16 (ch4:130 dùng đúng vai trò khả thi) | P1 nguồn |
| N32 | Từ tuyệt đối | ch1:15; ch5:27 | P3 |
| N33 | Khai báo AI: chưa chèn; còn ô trống tên công cụ; câu "mọi trích dẫn đều được đối chiếu với bản gốc" hiện chưa đúng – `thieu_toan_van.md`: \[1\] ISO 19650-3 chưa đọc (trích ở Ch.1, 2, 5), 7 nguồn mức tóm tắt (A), 14 bài chưa có PDF (B) | `revision/nhap_khai_bao_AI_tao_sinh.md` | P4 (chuẩn bị từ P1) |
| N34 | Lặp ý: Beleites/Wheat (1.3, 1.5.2, 3.4, 5.1.2); Çelik/Wu (1.4, 1.5.4, 1.6.4, 2.3.3, 5.1.3); FEM danh nghĩa (1.1.3, 1.7.4, 2.4, 5.9.3); "bất thường → kiểm tra" (1.7.5, 3.1.3, 5.8.2, 5.9.2, 5.10.3); "tổng quan theo chủ đề có cấu trúc, không tự nhận…" (1.8.1, 1.8.5e, 5.9.4) | nhiều chỗ | P3 |
| N35 | Câu giới hạn: danh sách v2 có 52 dòng, 40 "giữ nguyên" chưa xử lý; Ch.1 có 7 câu loại A (> 3–4); 1.7.5, 1.8.3, 3.1.3 dày câu "chỉ chứng minh / không chứng minh" | `danh_sach_cau_gioi_han_v2.csv` | P3 (sau NCS duyệt v2) |
| N36 | Chưa gọi tên chỉ số hiệu năng của RQ1 | 5.3.3, 5.4.1, 5.5.2 | P2-T3 (câu hỏi NCS) |
| N37 | Thiếu cấu trúc luận án dự kiến | 1.10, 5.10 | P2 trục phụ |

---

## 5. Số từ so với giới hạn (CLAUDE 6.0)

Đếm theo khoảng trắng (cùng cách Word đếm cho tiếng Việt), bỏ chú thích ẩn.

| Phần | Số từ | Giới hạn | Nhận xét |
|---|---:|---|---|
| Dẫn nhập | 1.048 | "ngắn" | Được |
| Ch.1 | 10.528 | – | 1.8 = 2.619 (dài nhất, lặp nhiều); 1.1 = 1.567; 1.5 = 1.394 |
| 1.2 Đối tượng | 1.147 | ≤ 1.500 | Đạt |
| Ch.2 | 5.123 | – | |
| Ch.3 | 5.981 | – | |
| 3.2 Hạn chế quan trắc | 1.510 | ≤ 1.500 | Vượt nhẹ |
| Ch.4 | 6.221 | – | |
| Ch.5 | 10.548 | – | |
| 5.2 Khoảng trống | 1.052 | ≤ 1.500 (≤ 2 trang) | Đạt |
| 5.5 Kiểm chứng | 791 | ~1 trang | Hơi dài nếu tính cả Bảng 5.2 |
| 5.6 Schema | 1.342 | ≤ 1.500 | Đạt |
| 5.7 Công cụ AI | 1.764 | ≤ 1.500 (đã duyệt 1.691) | Vượt |
| Phụ lục | 2.439 | – | |
| **Tổng thân bài** | **≈ 41.900** | | |

Câu dài (> 45 âm tiết, xấp xỉ > 30 từ): Ch.1 64/294 câu; Ch.2 41/128; Ch.3 41/160; Ch.4 37/152; Ch.5 52/260. Ch.2 có tỉ lệ cao nhất (32 %).

---

## 6. Đề xuất thứ tự cho Pha 1 (mỗi phiên một nhóm)

1. **Thuật ngữ:** N2, N4, N13, N18, N24, N28 (+ dòng SHACL/SOSA của N19 trong thuật ngữ).
2. **Tham chiếu và đánh số:** N1, N5, N6 (chỉ phần tham chiếu), N7, N21, N22, N23, N30.
3. **Danh mục và nguồn:** N8, N9, N11, N12, N14, N15, N31.
N3, N6 (định nghĩa M1–M4), N19 (Ch.4, Bảng 5.1), N20, N25, N26, N29, N36, N37 để sang Pha 2 vì đụng nội dung trục.

---

## 7. Câu hỏi cho NCS (trước Pha 1)

1. **Nhãn khoảng trống (N28):** dùng "G-A (A1, A2), G-B" trong văn bản, hay giữ "Khoảng trống A/B" và chỉ thêm nhãn "A1 – đánh giá", "A2 – khai báo"?
2. **IDS (N19):** 4.4.3 nói luận án dùng IDS cho yêu cầu thông tin cấp cấu kiện. Bỏ câu này (theo §8) hay giữ IDS làm hướng mở rộng?
3. **Chỉ số RQ1 (N36):** chỉ số hiệu năng nào được khóa cho Bài 1 (ví dụ độ chính xác cân bằng, F1 macro)? Tiểu luận chỉ cần gọi tên, không thêm chỉ số mới.
4. **Ngôi viết (N27):** câu nhận định cá nhân giữ "nghiên cứu sinh nhận thấy" (1.2.1, 2.2.3, 4.5.4) hay đổi thành "theo đánh giá của nghiên cứu này"?
5. **"Một tầng" (1.2.4):** giữ làm giới hạn khách thể, hay bỏ?
6. **Hình (N22):** NCS muốn sửa đường dẫn trỏ `TLTQ_28.09.2026/figures/` hay chuyển hình về `figures/` ở gốc dự án như CLAUDE §5?
7. **Tài liệu G1** và `00_DONG_BO_PIPELINE_…md`: nếu cần đối chiếu, xin cấp thêm quyền thư mục `03_OUTPUTS` hoặc chép hai tệp vào `revision/`.

---

## 8. Ghi nhận cho danh sách "Chuyển sang luận án" (dự kiến, chưa soạn chính thức)

- Toàn văn ISO 19650-3:2020 \[1\] và ISO 55000:2024 (`8PB7EN2E`) – chưa tiếp cận; tiểu luận dẫn ở mức tên, phạm vi.
- IFC4 ADD2 TC1, Khuyến nghị W3C SSN – nhập Zotero dạng tài liệu chuẩn (có thể làm trong tiểu luận nếu NCS mở trang thủ công).
- Toàn văn Ghazimoghadam 2024 (`G98ZWHKW`) và 7 nguồn mức tóm tắt ở `thieu_toan_van.md` mục A.
- Tìm kiếm có hệ thống, nhật ký truy vấn, PRISMA (1.8.5e).
- Phản chứng N-20 – N-25 ở mức toàn văn; phỏng vấn người quản lý (bằng chứng nhu cầu cho G-B); hồ sơ kiểm định thật cho nhận định về B0.

---

*Pha 0 không sửa tệp nào trong `tieuluan/`. Dừng ở ĐIỂM DỪNG 0, chờ NCS duyệt ma trận, danh sách N1–N37 và trả lời mục 7.*

---

## 9. Bổ sung sau ĐIỂM DỪNG 0 (02/10/2026, lần 2)

### 9.1. Quyết định của NCS cho mục 7

| # | Câu hỏi | Quyết định | Áp dụng ở |
|---|---|---|---|
| 1 | Nhãn khoảng trống (N28) | NCS chọn "G1 – G2 – G3". **Chờ làm rõ** (xem 9.3) | — |
| 2 | IDS (N19) | Giữ IDS làm **hướng mở rộng**; 4.4.3 bỏ câu "Luận án dùng cơ chế thứ nhất…", chuyển ý vào Bảng 5.5 (hướng phát triển) | Pha 1 nhóm 1; Pha 2-T3 |
| 3 | Chỉ số RQ1 (N36) | Nêu **ở mức sơ bộ**: "chỉ số hiệu năng phân loại chấm theo bản ghi; chỉ số cụ thể được khóa trong Bài 1", không nêu tên chỉ số | Pha 2-T3 |
| 4 | Ngôi viết (N27) | Câu nhận định dùng **"theo đánh giá của phần tổng quan nghiên cứu này"**; thay "nghiên cứu sinh nhận thấy", "theo nhận định của nghiên cứu sinh", "Theo đánh giá của nghiên cứu này" | Pha 3 (5 chỗ "nghiên cứu sinh": 1.2.1 ×2, Dẫn nhập, 2.2.3, 4.5.4; 1 chỗ "Theo đánh giá của nghiên cứu này": 5.2.2) |
| 5 | "Một tầng" | **Bỏ** ở 1.2.4 | Pha 1 nhóm 1 |
| 6 | Thư mục `03_OUTPUTS` | Đã cấp; đã đọc `00_DONG_BO_PIPELINE_VA_PHAN_VUNG_KET_QUA.md` và `PROMPT_KHOI_DONG_PROJECT_DINH_HUONG_LUAN_AN.md` | 9.2 |

Lưu ý về câu ngôi viết dùng cho Dẫn nhập và 1.2.1: hai câu đó nói về **nhận định từ thực tế kiểm định** của NCS (CLAUDE 7.5), không phải từ tổng quan. Đổi thành "theo đánh giá của phần tổng quan nghiên cứu này" sẽ gán sai nguồn của nhận định. Đề xuất giữ cho hai câu này dạng "từ thực tế kiểm định, …", các câu còn lại theo quyết định 4. Chờ NCS xác nhận.

### 9.2. Kết quả tìm trong `03_OUTPUTS`

**Tài liệu G1 không có trong `03_OUTPUTS`** (đã liệt kê cả 6 thư mục con; tìm thêm trên Google Drive theo tên `G1_ban_do_tai_lieu` – không có). Theo `PROMPT_KHOI_DONG_PROJECT_…md` mục 3, G1 là sản phẩm Giai đoạn 1 của project định hướng luận án, có thể nằm trong project hoặc tài liệu Claude khác. Pha 1 vẫn làm được theo bảng N1–N17 của prompt.

Điểm mới từ `00_DONG_BO_…md` (v1.0, 02/10) ảnh hưởng tiểu luận:

| Điểm | Nội dung ở tệp 00 | Hệ quả cho tiểu luận |
|---|---|---|
| Q1 | Bài bổ trợ BT-A, BT-B (cấu hình cảm biến) "bổ trợ cho RQ1" nhưng **không ghi vào tiểu luận** | Cập nhật N20: câu 3.3.1 dòng 85 đang ngầm nhắc nội dung của BT-A/BT-B. Sửa thành "cấu hình cảm biến là một thành phần của phạm vi hiệu lực" (khớp `obs_context`), bỏ vế "hỗ trợ cho RQ1 … dưới các cấu hình khác nhau" |
| Nguyên tắc 1 | MT1 là tối thượng | Không cần đưa vào tiểu luận; giữ thứ tự MT1 → MT2 → MT3 như hiện có |
| Mục 2 | Khung 1:10 mô phỏng chính nhà xưởng có BIM 1:1; hai bên chỉ nối qua tương ứng thông tin, không khẳng định tương tự động lực học | Bổ sung cho T2: 1.2.4 nên nói rõ quan hệ hai đối tượng theo câu này; khớp 3.4.3 (mức tương đồng là giới hạn) |
| Mục 2 | Nhãn trạng thái thí nghiệm S0, B1, B2, B3; tên bài "B1", "B2" | **Va chạm tên** với đối chứng B0, B1 của tiểu luận. Tiểu luận hiện không dùng S0–B3 và gọi bài là "Bài báo 1, 2" – giữ nguyên, không đưa các mã này vào |
| Mục 4, B1-6 | Tổng quan nêu [19] **Ramasso 2025** và [15] Wheat 2024 là tiền lệ gần nhất | Xác nhận N9: sửa 3.4.3 thành 2025; 5.8.1 đã nêu đủ hai tiền lệ |
| Mục 3 | Đánh giá chuẩn = cùng lần chạy (mốc) + LORO + LOCO, chấm theo bản ghi | Khớp 5.4.1, 5.5.2, 5.7.2. Củng cố N29: cần định nghĩa "đánh giá cùng lần chạy" ở 3.4 và Bảng thuật ngữ |

### 9.3. Câu hỏi còn mở về nhãn khoảng trống

"G1 – G2 – G3" (ba nhãn) gặp hai vướng:
1. **Số khoảng trống:** CLAUDE QĐ 9, 13 và prompt mục 4 khóa *hai* khoảng trống (G-A gồm A1, A2; G-B). Ba nhãn sẽ đọc thành ba khoảng trống, đúng lỗi N1 đang sửa.
2. **Trùng tên:** G1–G7 đã là mã góp ý của thầy (CLAUDE §3, bản giải trình ở Pha 4) và "tài liệu G1" của project định hướng.

Nếu ý NCS là G1 = A1 (đánh giá), G2 = A2 (khai báo), G3 = G-B, nội dung vẫn giữ nhưng hai vướng trên vẫn còn. Chờ NCS chọn trước khi chạy Pha 1 nhóm 1.
