# Changelog — Tiểu luận tổng quan v2 (nhánh `revision-v2`)

## Giai đoạn 0 – thiết lập (28/09/2026)

### Bước 1 – Thiết lập dự án
- Thư mục nằm trong repo Git có sẵn (`03_RESEARCH/01_PHD_DT_AI_AM`), nên không `git init`. Tạo nhánh `revision-v2` từ `master` (commit 076b899).
- Tạo thư mục `tieuluan/`, `matrix/`, `notes/`, `mapping/`, `revision/`, `figures/`.

### Bước 2 – Chuyển tiểu luận sang Markdown
- Nguồn: `HO_CHI_HAN_TIEU_LUAN_TONG_QUAN_23092026_HOANTHIEN.docx` (không sửa, không xóa).
- Công cụ: pandoc (GFM, không ngắt dòng). Tách thành `00_dau.md` (bìa, mục lục, danh mục bảng/hình, thuật ngữ, Dẫn nhập), `01_chuong1.md` … `05_chuong5.md`, `99_tailieu.md`.
- Kiểm tra đối chiếu với .docx:
  - Đề mục: 7 cấp 1, 35 cấp 2, 106 cấp 3 — khớp.
  - Bảng: 12 (4 bảng thuật ngữ + 8 bảng thân bài 2.1, 3.1, 4.1, 4.2, 5.1–5.4) — khớp; không bảng nào lệch cột.
  - Chú thích: 8 chú thích bảng + 4 chú thích hình — khớp.
  - Tài liệu tham khảo: 84 mục [1]–[84] — khớp.
  - Số từ: 40.214 (docx) / 40.190 (md); chênh 24 từ do ký hiệu thoát và neo liên kết.
  - Không có ký tự lỗi, không còn mã field Zotero.
- Mất định dạng:
  - Bốn hình vẽ bằng shape (Hình 1.1, 5.1, 5.2, 5.3) pandoc không chuyển. Đã cắt ảnh từ PDF do Word xuất, lưu `figures/Hinh_*.png`, chèn dòng ảnh ngay trước chú thích (kèm ghi chú HTML). Không đổi chữ nào của văn bản.
  - Liên kết số trang trong mục lục và danh mục bảng/hình trở thành liên kết neo; số trang không còn ý nghĩa trong Markdown.
  - Chữ đậm, nghiêng và chỉ số trích dẫn `\[n\]` giữ nguyên.
- Lỗi có sẵn trong bản gốc (ghi nhận, không sửa): mục 1.1.4, câu về QĐ 258/QĐ-TTg kết thúc bằng trích dẫn lặp "[12], [12], [12]".

### Bước 3 – Đối chiếu danh mục với Zotero (28/09/2026)
- Tạo collection `TL-Key` (PRGXUPFZ) với `Tier1` (H86TEIR4), `Tier2` (WVXRDFTI), `Bổ sung` (TKVJVWDZ, đang trống).
- Đối chiếu 84 tài liệu theo DOI, sau đó theo tiêu đề, trên bản sao chỉ-đọc của `zotero.sqlite`: 84/84 có trong Zotero, 60/84 có PDF. Kết quả: `matrix/doi_chieu_danh_muc.csv` (phân cách `|`, UTF-8 BOM).
- Gán Tier theo CLAUDE.md 7.1–7.2: 12 tài liệu vào `Tier1`, 15 vào `Tier2`. Gắn tag `Chuẩn` cho [1] ISO 19650-3, [61] SOSA, [62] SSN, [69] PROV-O.
- Tag K1, K2, K3, Đối tượng chưa tồn tại: Zotero chỉ tạo tag khi gắn vào tài liệu, và CLAUDE.md chưa quy định tài liệu nào mang các tag này.
- Tài liệu 2025–2026 (19 mục): kiểm tra DOI qua Crossref. 18 mục "chính thức" (có tập và trang/số bài); [11] NĐ 207/2026/NĐ-CP "không xác minh được" (không có DOI).
- Không nhập tài liệu mới vào Zotero; không sửa siêu dữ liệu tài liệu.
- Phát hiện cần NCS xử lý:
  - [17] Wu và cs. và [80] T. Bull và cs.: năm trong danh mục khác năm bản in (xem cột ghi_chu).
  - [68] PROV-DM có 2 bản ghi trùng trong Zotero; [69] PROV-O có 4 bản ghi trùng.
  - 7 tài liệu Tier1/Tier2 chưa có PDF: [22] Hemker, [28] Kamariotis, [35] Bellon, [42] Ramonell, [53] Kapoor & Narayanan, [57] Bull 2021, [80] Bull 2025.
  - Chỉ 3/84 bản ghi có citation key; cột `citekey` dùng dạng `zotero:<item key>` cho các mục còn lại.

## Phiên 29/09/2026 – bốn việc kỹ thuật

### Việc 1 – Tách 00_dau.md
- Tách thành `00_bia.md` (trang bìa), `00_thuatngu.md` (Giải thích thuật ngữ, nguyên văn), `00_dannhap.md` (từ "# DẪN NHẬP" đến hết).
- Xóa mục lục, danh mục bảng, danh mục hình (326 dòng, toàn bộ là dòng liên kết neo và 3 dòng tiêu đề danh mục); sẽ tạo lại khi xuất Word ở GĐ6.
- Kiểm tra: ghép 3 tệp mới với phần đã xóa trùng khớp từng ký tự với `00_dau.md`. Số câu theo từng phần: bìa 1, thuật ngữ 21, dẫn nhập 27 (tổng 49). 12 thẻ `<span id="TLTQ_...">` trong các chương giữ nguyên.
- Đã xóa `00_dau.md`.

### Việc 2 – CLAUDE.md mục 4.4 "Quy ước trích dẫn"
- Thêm mục 4.4 (số cũ `\[n\]` giữ đến hết GĐ5; tài liệu mới dạng `\[@KHÓA_ZOTERO\]`; dòng mới trong `doi_chieu_danh_muc.csv` với `so_cu = "moi"`; đánh số lại theo IEEE ở GĐ6; không sửa tay số trích dẫn).
- Cập nhật mục 5 (cấu trúc thư mục) theo tên tệp mới của phần đầu.
- Đưa CLAUDE.md vào Git (trước đó chưa được theo dõi).

### Việc 3 – CLAUDE.md mục 4.5 "Viết về giới hạn" và danh sách câu
- Thêm mục 4.5 (phân loại A/B/C, giọng văn khẳng định; là việc của GĐ5).
- Lập `revision/danh_sach_cau_gioi_han.csv`: 80 câu chứa "không chứng minh / không phải / không thay thế / không đồng nghĩa / không đủ" trong phần thuật ngữ, dẫn nhập và 5 chương (kể cả ô bảng).
- Nhãn đề xuất: A 43, B 13, C 24. Nhãn tự động được rà tay; 8 câu đổi nhãn, 7 câu có ghi chú (câu thuật lại kết quả tài liệu hoặc ô bảng — đề xuất giữ nguyên).
- Loại A vượt hạn mức 3–4 câu/chương ở Ch.1 (7), Ch.3 (8), Ch.4 (6), Ch.5 (18); cần NCS chọn câu giữ.
- Chưa sửa câu nào trong tiểu luận.

### Việc 4 – Tồn đọng GĐ0
- Sửa lỗi trích lặp ở mục 1.1.4 (`01_chuong1.md`): "\[12\], \[12\], \[12\]" → "\[12\]". Đây là thay đổi duy nhất trong văn bản tiểu luận ở phiên này.
- `doi_chieu_danh_muc.csv`: điền "không áp dụng (trước 2025)" cho 65 dòng trống ở cột `trang_thai_xuat_ban`; ghi chú [80] "cần sửa năm danh mục 2025 → 2026 theo bản in"; cập nhật ghi chú [12].
- Lập `revision/viec_ton_dong_GD0.md`: 7 tài liệu key thiếu PDF; bản ghi trùng [68] (2) và [69] (4) kèm đề xuất bản giữ lại (bản đang được trích trong .docx: B8QZMS77, FJJAV9T4), chưa gộp; [11] chờ NCS đối chiếu văn bản pháp luật.
- Chưa lưu `revision/nhap_5_8_pham_vi_ap_dung.md`: yêu cầu không kèm nội dung bản nháp.
- Cập nhật bảng Trạng thái tiến độ trong CLAUDE.md.

## Phiên 29/09/2026 (2) – chuẩn bị nguồn cho mục Công cụ AI (5.6A)

### Việc 0 – Lưu bản nháp mục 5.8
- Lưu nguyên văn bản nháp NCS cung cấp vào `revision/nhap_5_8_pham_vi_ap_dung.md` (7 đoạn). Chưa chèn vào Chương 5.

### Việc 1 – Kiểm kê Zotero các tài liệu phương pháp
- `revision/nguon_5_6A_kiem_ke.csv`: 9 tài liệu. DOI của 7 tài liệu mới được xác minh qua Crossref (tác giả đầu, tạp chí, tập, trang, năm khớp mô tả trong yêu cầu).
- Có trong Zotero (kèm PDF): Kiranyaz và cs. 2021 (IU5KZQEA), Avci và cs. 2021 (QUGY4928), Sohn 2007 [45] (MANJDQEZ), Keshmiry và cs. 2023 [46] (ESQIRHVE).
- Chưa có trong Zotero: Breiman 2001, Cortes & Vapnik 1995, He và cs. 2016 (CVPR, không có số tập), Varma & Simon 2006, Vabalas và cs. 2019.
- Chỉ dùng làm nguồn phương pháp; không lấy kết quả Paper 1.

### Việc 2 – Tìm và xác minh ứng viên G1–G6
- Consensus: 17 truy vấn (G1 3, G2 3 + 1 truy vấn kiểm gợi ý Figueiredo, G3 3, G4 3, G5 2, G6 2). Mỗi nhóm giữ tối đa 5 ứng viên.
- `revision/nguon_5_6A_ung_vien.csv`: 29 ứng viên; cả 29 được Crossref xác minh (tiêu đề, tác giả, năm, tạp chí, tập/trang, DOI). Không ứng viên nào bị loại vì không xác minh được.
- Các gợi ý của NCS đều khớp Crossref: Pathirage 2018, Figueiredo 2011, Cross/Worden/Chen 2011, Bull 2018 và 2019, Wang/Yan/Oates 2017, Abdeljaber 2017.
- Năm theo Crossref khác Consensus ở 5 bài (Wang & Cha, Shang, Maes, Hughes, Ismail Fawaz); CSV dùng năm Crossref.
- Đề xuất: 16 nhận (13 cần nhập Zotero; 3 đã có: Kiranyaz, Avci; Pal [48] để dự phòng), 13 dự phòng. Đánh giá dựa trên tóm tắt, chưa đọc toàn văn.
- Không nhập Zotero, không sửa chương.
