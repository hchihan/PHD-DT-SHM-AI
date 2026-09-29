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
