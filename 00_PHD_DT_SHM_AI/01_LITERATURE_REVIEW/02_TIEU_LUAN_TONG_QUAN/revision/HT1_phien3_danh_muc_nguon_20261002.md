# HT1 – Pha 1, phiên 3: Danh mục và nguồn (02/10/2026)

Phạm vi: N8, N9, N11, N12, N14, N15, N31.
Zotero ban đầu không chạy; NCS mở lại, phần N8 (33 khóa) và N11 (hai chuẩn) đã làm xong ở lượt sau.

## 1. Đã làm
| Mã | Kết quả |
|---|---|
| N9 | Ramasso (2024) → (2025) ở 3.4.3; Kamariotis (2022) → (2023) ở 2.1.3. Danh mục [19], [28] đã đúng năm (khớp `doi_chieu_danh_muc.csv`, Crossref). |
| N12 | NĐ 207/2026: đã kiểm trên thuvienphapluat.vn ngày 02/10/2026 – tên đầy đủ, ngày ban hành 15/6/2026, hiệu lực 01/7/2026 **khớp văn bản**. **Không kiểm được** số Điều 34, 37 và việc thay thế NĐ 06/2021 (trang chỉ hiện trích đoạn; trích đoạn nhắc "Điều 36" liên quan quan trắc phục vụ bảo trì). Đã gắn `[CẦN KIỂM]` ở ba chỗ (1.1.4) và bổ sung ngày ban hành, hiệu lực, URL, ngày truy cập cho mục [11]. Nên thay URL bằng bản trên Cổng văn bản Chính phủ khi NCS mở được. KCN (`XM5ZUP99`): số liệu đã kiểm nguyên văn 01/10/2026; ngày truy cập sẽ ghi khi đưa khóa vào danh mục (chờ Zotero). |
| N14 | Câu [82] Seiß sửa theo `notes/JTF8EM7Y.md` (tr. 9–11): đối tượng là lần kiểm tra theo kế hoạch trong thi công, định danh lấy từ IFC sau khi chuyển sang RDF. |
| N15 | Câu Ghazimoghadam rút về đúng nội dung tóm tắt (`notes/G98ZWHKW.md`), bỏ chi tiết "trên kết cấu phòng thí nghiệm"; thêm chú thích ẩn "mức tóm tắt". Đưa vào danh sách chuyển sang luận án (toàn văn). |
| N31 | Câu [23] ở 2.1.1 ghi rõ UCLA Factor Building là tòa nhà văn phòng; việc áp cho nhà công nghiệp ghi là diễn giải (CLAUDE 4.1). |
| N8 (một phần) | Bỏ [63], [65], [77], [80], [84] khỏi danh mục (không còn được trích; [63], [65], [77] theo quyết định 02/10; [80] bỏ ở GĐ2; [84] Mariniello 2025 chưa từng được trích). Năm mục chuyển vào chú thích ẩn cuối `99_tailieu.md`; số thứ tự để trống đến GĐ6. |

## 2. Phần làm sau khi Zotero chạy
- **N8 xong:** `99_tailieu.md` thêm mục "Tài liệu bổ sung (trích bằng khóa Zotero, đánh số theo IEEE ở GĐ6)" gồm 35 mục (33 khóa cũ + 2 chuẩn mới), xuất từ Zotero kiểu IEEE. Mục `XM5ZUP99` ghi tên tạp chí, ngày đăng 16/11/2025 và ngày truy cập 01/10/2026 (theo trường "accessed" trong Zotero). Kiểm bằng script: mọi số `\[n\]` và mọi khóa `\[@KEY\]` trong thân bài đều có trong danh mục, không còn mục thừa.
- **N11 xong:** nhập vào Zotero, collection `TL-Key/Bổ sung`, tag `TLTQ:Chuan`, `N11`:
  - `GHAZGWUN` – W3C, *Semantic Sensor Network Ontology*, Khuyến nghị W3C 19/10/2017; biên tập A. Haller, K. Janowicz, S. Cox, D. Le Phuoc, K. Taylor, M. Lefrançois. Kiểm trang đặc tả 02/10/2026; mục 5.1 có `ssn-system:Condition`, khớp câu ở 5.2.1.
  - `63XPSMIR` – buildingSMART International, *IFC4 ADD2 TC1* (4.0.2.1), 10/2017, tương đương ISO 16739-1:2018. Kiểm trang danh mục phiên bản IFC 02/10/2026.
  - Thay 8 chỗ `[CẦN NGUỒN]`: IFC4 ở 2.2.3, 4.5.4, 5.2.2; SSN ở 4.2.1, 5.2.1 ("(mục 5.1)"), Phụ lục A (2 ô Bảng A.3), B.3. Thêm 2 dòng `so_cu = moi` vào `matrix/doi_chieu_danh_muc.csv`.

### Phát hiện cần NCS xử lý trong Zotero
1. **Bốn tài liệu đang được trích nằm trong Thùng rác (Trash) của Zotero:** `69U5H3TZ` He 2016 (5.7.2), `8IMKCTE5` Graybeal 2002 (3.2.1), `J7FAWJ8I` Phares 2004 (3.2.1), `KPWFC4PI` Cross 2011 (5.7.3). Danh mục hiện lấy thông tin từ BibTeX của chính bản ghi trong Thùng rác. Cần **khôi phục** bốn mục này trước khi chạy script đánh số lại ở GĐ6, nếu không chúng sẽ rơi khỏi danh mục.
2. Hai mục mới (`GHAZGWUN`, `63XPSMIR`) được ghi qua Zotero web API; API cục bộ chưa thấy (lỗi 404) lúc kiểm. Cần Zotero đồng bộ (Sync) rồi kiểm lại hai mục có trong `TL-Key/Bổ sung`.
3. Thông tin thư mục còn thiếu trong Zotero (sửa ở GĐ6, không sửa tay danh mục): He 2016 thiếu tên hội nghị (CVPR); Mitchell 2019 thiếu tên kỷ yếu (FAT* '19); Torres-Barriuso 2025 thiếu tập, số bài; IFC4 ADD2 TC1 ghi kiểu trang web.
4. [61], [62] (SOSA/SSN bài báo) vẫn trích ở 4.2.1 cùng với `GHAZGWUN`. CLAUDE.md §12 ghi dự định chuyển hẳn sang Khuyến nghị W3C; giữ cả hai đến khi NCS quyết.

## 3. Trước / sau
| Mã | Tệp | Trước | Sau |
|---|---|---|---|
| N9 | `03_chuong3.md` | Ramasso, de Oliveira Teloli và Marcel (2024) | Ramasso, de Oliveira Teloli và Marcel (2025) |
| N9 | `02_chuong2.md` | Kamariotis và cộng sự (2022) | Kamariotis và cộng sự (2023) |
| N14 | `05_chuong5.md` | Seiß và cộng sự (2025) dùng trực tiếp định danh IFC để gắn hồ sơ kiểm tra với cấu kiện \[82\]. | Seiß và cộng sự (2025) nối các lần kiểm tra theo kế hoạch trong thi công với cấu kiện qua định danh cấu kiện lấy từ mô hình IFC sau khi chuyển sang RDF \[82\]. |
| N15 | `05_chuong5.md` | Ghazimoghadam và Hosseinzadeh (2024) cũng học từ trạng thái chưa hư hỏng và phát hiện bu lông liên kết bị nới lỏng trên kết cấu phòng thí nghiệm \[@G98ZWHKW\]. | Ghazimoghadam và Hosseinzadeh (2024) cũng huấn luyện autoencoder chỉ với dữ liệu trạng thái chưa hư hỏng và phát hiện được hư hỏng nhỏ dạng bu lông liên kết bị nới lỏng \[@G98ZWHKW\].<!-- N15: câu viết ở mức tóm tắt bài báo; chưa có toàn văn (notes/G98ZWHKW.md). --> |
| N31 | `02_chuong2.md` | Ở phía kỹ thuật, quan trắc dài hạn đã chứng minh khả năng thu dữ liệu động lực học liên tục trên kết cấu thép ở quy mô công trình thực, điển hình là hệ thống trên UCLA Factor Building \[23\]. | Ở phía kỹ thuật, quan trắc dài hạn đã thu được dữ liệu động lực học liên tục trên kết cấu thép ở quy mô công trình thực, ví dụ hệ thống trên UCLA Factor Building, một tòa nhà văn phòng khung thép \[23\]; việc áp kết quả này cho nhà công nghiệp là diễn giải của tiểu luận. |
| N12 | `01_chuong1.md` | thay thế Nghị định số 06/2021/NĐ-CP \[11\]. | thay thế Nghị định số 06/2021/NĐ-CP \[11\] \[CẦN KIỂM: điều khoản thay thế Nghị định 06/2021/NĐ-CP\]. |
| N12 | `01_chuong1.md` | (Điều 34) | (Điều 34 \[CẦN KIỂM: số điều\]) |
| N12 | `01_chuong1.md` | (Điều 37) | (Điều 37 \[CẦN KIỂM: số điều\]) |
| N12 | `99_tailieu.md` | bảo trì công trình xây dựng,” 207/2026/NĐ-CP. | bảo trì công trình xây dựng,” Nghị định số 207/2026/NĐ-CP, ban hành ngày 15/6/2026, hiệu lực từ ngày 01/7/2026. \[Online\]. Available: https://thuvienphapluat.vn/van-ban/Xay-dung-Do-thi/Nghi-dinh-207-2026-ND-CP-huong-dan-Luat-Xay-dung-quan-ly-chat-luong-thi-cong-xay-dung-701883.aspx (truy cập ngày 02/10/2026). |
| N8 | `99_tailieu.md` | \[63\] D. Isailović, V. Stojanovic, M. Trapp, R. Richter, R.; \[65\] A. G. Mohamed, A. Khaled, and I. S. Abotaleb, “A Brid; \[77\] R. Sacks *et al.*, “SeeBridge as next generation brid; \[80\] T. Bull *et al.*, “Probabilistic digital-twin-informe; \[84\] G. Mariniello, C. Gragnaniello, and D. Asprone, “Enha | chuyển vào chú thích ẩn cuối tệp |

## 4. Trích dẫn mới
`\[@GHAZGWUN\]` (W3C SSN) và `\[@63XPSMIR\]` (IFC4 ADD2 TC1), đều đã có trong Zotero và trong `doi_chieu_danh_muc.csv`.

## 5. Bổ sung danh sách "Chuyển sang luận án"
- Toàn văn Ghazimoghadam & Hosseinzadeh 2024 (`G98ZWHKW`).
- Số điều của NĐ 207/2026 về quy trình bảo trì và quan trắc; điều khoản thay thế NĐ 06/2021 (nếu không kiểm được trước khi chốt).
- [84] Mariniello 2025: không dùng trong tiểu luận; cân nhắc nêu ở Bài 2 (đã có `10_NOVELTY_CHECK_B_MARINIELLO_2025.md` trong hồ sơ Paper 2).

ĐIỂM DỪNG 1 (phiên 3). Pha 1 hoàn tất; bước kế tiếp là Pha 2 (bốn trục T1 → T4).
