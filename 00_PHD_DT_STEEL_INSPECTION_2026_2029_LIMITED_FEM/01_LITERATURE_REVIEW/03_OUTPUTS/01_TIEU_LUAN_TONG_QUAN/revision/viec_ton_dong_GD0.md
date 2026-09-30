# Việc tồn đọng sau Giai đoạn 0

Cập nhật: 29/09/2026. Nguồn: `matrix/doi_chieu_danh_muc.csv`, bản sao chỉ-đọc `zotero.sqlite` (29/09/2026).

## 1. Bảy tài liệu key thiếu PDF

Cần có PDF toàn văn trong Zotero trước Giai đoạn 2 (đọc sâu).

| Số cũ | Tài liệu | Tier | Khóa Zotero | DOI |
|---|---|---|---|---|
| [22] | Hemker và cs. (2019), Building Maintenance Management for Steel Structures in Industrial Facilities | 1 | B2JXAM9M | 10.1002/cepa.1045 |
| [35] | Bellon và cs. (2025), IFC framework for inspection and maintenance representation in facility management | 1 | NUTL57KJ | 10.1016/j.autcon.2025.106157 |
| [53] | Kapoor & Narayanan (2023), Leakage and the reproducibility crisis in machine-learning-based science | 1 | JQKJGUER | 10.1016/j.patter.2023.100804 |
| [28] | Kamariotis và cs. (2023), A framework for quantifying the value of vibration-based SHM | 2 | AESHHWVZ | 10.1016/j.ymssp.2022.109708 |
| [42] | Ramonell và cs. (2023), Knowledge graph-based data integration system for digital twins of built assets | 2 | DWT957YI | 10.1016/j.autcon.2023.105109 |
| [57] | Bull và cs. (2021), Foundations of population-based SHM, Part I | 2 | W7AEKRT8 | 10.1016/j.ymssp.2020.107141 |
| [80] | T. Bull và cs. (2025), Probabilistic digital-twin-informed risk-based inspection planning for offshore wind turbine structures | 2 | 5D5H5XGK | 10.1177/14759217251316199 |

DOI lấy từ cột `doi` của `matrix/doi_chieu_danh_muc.csv` (tức danh mục tài liệu của tiểu luận).

## 2. Bản ghi trùng trong Zotero (CHƯA gộp)

Đề xuất giữ bản đang được trích trong tệp .docx gốc, để không làm hỏng field Zotero của tiểu luận.

### [68] PROV-DM (2 bản)

| Khóa | Loại | Ngày thêm | Collection | Ghi chú/đính kèm | Được trích trong .docx | Đề xuất |
|---|---|---|---|---|---|---|
| B8QZMS77 | journalArticle | 03/08/2026 | PAPER2_G2G3_MASTER_15092026 | 7 ghi chú, 11 tag | Có | **Giữ (bản chính)** |
| M8AI7TWT | report | 20/09/2026 | TIEU_LUAN_TONG_QUAN_bo_sung_20260919; RQ3/WP3/Paper 3/Gate 4 | 0 | Không | Gộp vào B8QZMS77 |

### [69] PROV-O (4 bản)

| Khóa | Loại | Ngày thêm | Collection | Ghi chú/đính kèm | Được trích trong .docx | Đề xuất |
|---|---|---|---|---|---|---|
| FJJAV9T4 | journalArticle | 03/08/2026 | PAPER2_G2G3_MASTER_15092026 | 7 ghi chú, 12 tag (có `Chuẩn`) | Có | **Giữ (bản chính)** |
| TMZJ5PYK | webpage | 03/08/2026 | PAPER2_G2G3_MASTER_15092026 | 1 đính kèm | Không | Gộp vào FJJAV9T4 (giữ tệp đính kèm) |
| 3XFEVIGR | report | 20/09/2026 | TIEU_LUAN_TONG_QUAN_bo_sung_20260919; RQ3/WP3/Paper 3/Gate 4 | 0 | Không | Gộp vào FJJAV9T4 |
| PQUX27P4 | attachment (độc lập) | 03/08/2026 | — | — | Không | Không phải bản ghi thư mục; chuyển thành tệp đính kèm của FJJAV9T4 hoặc để nguyên |

Lưu ý sau khi gộp: hai bản giữ lại đang có loại `journalArticle`, trong khi PROV-DM và PROV-O là
khuyến nghị W3C. Nên đổi loại sang `report` (hoặc `document`) để danh mục IEEE ở GĐ6 hiển thị đúng.
Việc gộp làm trong Zotero desktop (Duplicate Items → Merge), chọn bản chính như trên; sau đó
Refresh trong Word nếu có hỏi.

## 3. [11] Nghị định 207/2026/NĐ-CP

Văn bản pháp luật, không có DOI, nên không xác minh được qua Crossref. NCS tự đối chiếu với
Công báo hoặc cơ sở dữ liệu văn bản pháp luật quốc gia (số hiệu, ngày ban hành, ngày hiệu lực,
các điều được trích: 34, 37) rồi cập nhật cột `trang_thai_xuat_ban` trong `doi_chieu_danh_muc.csv`.

## 4. Việc khác

- [80] T. Bull và cs.: sửa năm danh mục 2025 → 2026 theo bản in (khi đánh số lại ở GĐ6).
- [17] Wu và cs.: danh mục đã ghi 2026, khớp bản in; không cần sửa.
- Tag K1, K2, K3, Đối tượng: gắn trong Giai đoạn 2, khi đọc sâu từng tài liệu.
- Collection đích của GĐ1: `TL-Key/Bổ sung` (TKVJVWDZ). Kiểm tra 30/09/2026 trên bản sao CSDL Zotero (lưu 29/09 15:03): không có collection `00_TLTQ/05_Bo_sung_GD1`.
- Chỉ 3/84 bản ghi có citation key; cân nhắc cài Better BibTeX trước GĐ6.

## 5. Chờ PDF (mục 5.6A, cập nhật 29/09/2026)

| Tài liệu | Khóa Zotero | Tình trạng | Việc cần làm khi có tệp trong `pdf/` |
|---|---|---|---|
| Cross, Worden & Chen (2011), Proc. R. Soc. A 467: 2712–2732 | KPWFC4PI | Truy cập đóng; không có bản lưu trữ mở | Đọc phần phương pháp; chỉnh câu về đồng liên kết ở 5.6A.3; cập nhật `notes/KPWFC4PI.md` và cột `muc_da_doc` |
| Ghazimoghadam & Hosseinzadeh (2024), Measurement 229: 114410 | G98ZWHKW | ScienceDirect chặn bằng CAPTCHA; không có bản lưu trữ mở | Đọc phần phương pháp; chỉnh câu về autoencoder và bu lông nới lỏng ở 5.6A.3; cập nhật `notes/G98ZWHKW.md` và cột `muc_da_doc` |
| Hughes và cs. (2022), bản in MSSP 167: 108569 | Z9RD5DMZ | Đã có bản tiền in arXiv v2; bản in truy cập đóng | Đối chiếu bản in với bản tiền in; cập nhật số trang trong `revision/5_6A_luan_diem_nguon.csv` và `notes/Z9RD5DMZ.md` |

Lưu tệp với tên bắt đầu bằng khóa Zotero (ví dụ `pdf/KPWFC4PI_Cross2011.pdf`) và liên kết vào Zotero dạng linked file.
