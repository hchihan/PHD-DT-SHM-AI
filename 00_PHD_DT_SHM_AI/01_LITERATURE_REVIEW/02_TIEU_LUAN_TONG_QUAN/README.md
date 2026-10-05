# Tiểu luận tổng quan – NCS Hồ Chí Hân (bản chốt 04/10/2026)

"Tổng quan về hệ thống song sinh kỹ thuật số dựa trên dữ liệu trong giám sát trạng thái và hỗ trợ kiểm tra – bảo trì công trình công nghiệp khung thép". Ngành Quản lý xây dựng.

## Bản chốt

| Tệp | Nội dung |
|---|---|
| `00_BAN_CHOT/HO_CHI_HAN_TIEU_LUAN_TONG_QUAN_BAN_CHOT_20261004.docx` | Báo cáo, 71 trang, 90 tài liệu, trích dẫn là trường Zotero (Refresh được trong Word) |
| `00_BAN_CHOT/BAO_CAO_TLTQ_BAN_CHOT_20261004.pptx`, `.pdf` | Slide báo cáo, 20 slide, có ghi chú thuyết trình |

Các bản trung gian (r9, r11, FINAL_PROOFREAD, ASSET_RATIONALE r1–r3, slide các vòng) nằm ở `_luu_tru/`, không đưa vào Git.

## Cấu trúc

| Thư mục | Vai trò |
|---|---|
| `tieuluan/` | **Nguồn duy nhất** của bản Word: Markdown theo chương (`00_bia.md` … `05_chuong5.md`, `phuluc.md`) |
| `xuat_ban/build.py` | Dựng bản Word từ `tieuluan/`: đánh số IEEE theo thứ tự xuất hiện, lấy danh mục từ Zotero, chèn trường Zotero |
| `xuat_ban/zotero_cache.json`, `danh_muc_Zotero.csv` | Bộ đệm CSL-JSON và danh mục do `build.py` sinh |
| `matrix/doi_chieu_danh_muc.csv` | Ánh xạ số cũ ↔ khóa Zotero, ghi chú mức đã đọc của từng nguồn |
| `figures/` | Hình và script vẽ (`ve_hinh.py`, `ve_hinh_4_2.py`) |
| `notes/`, `mapping/` | Ghi chú đọc sâu tài liệu key; bảng ánh xạ tiền lệ |
| `revision/` | Nhật ký (`changelog.md`), biên bản từng vòng, script sửa slide (`HT19_…`, `HT20_…`, `HT21_slide_scripts/`) |
| `pdf/` | PDF tài liệu (liên kết Zotero, không vào Git) |
| `HO_CHI_HAN_TIEU_LUAN_TONG_QUAN_23092026_HOANTHIEN.docx` | Bản gốc, dùng làm mẫu định dạng cho `build.py`; không sửa |
| `CLAUDE.md` | Quy tắc làm việc và các quyết định đã khóa (QĐ 1–17) |

## Dựng lại bản Word

Yêu cầu: Python 3, `pandoc`, Zotero đang chạy (API cục bộ `localhost:23119`).

```bash
python xuat_ban/build.py TEN_TEP_XUAT
```

Sau đó mở tệp trong Word, cập nhật mục lục (chuột phải → Update Field) hoặc chạy lại bước cập nhật mục lục bằng PowerShell như các phiên trước.

Quy tắc:
- Trích dẫn trong Markdown: `\[n\]` (số cũ) hoặc `\[@KHOAZOTERO\]`. Không sửa tay số IEEE.
- Nguồn mới: nhập Zotero trước, thêm một dòng `so_cu = moi` vào `matrix/doi_chieu_danh_muc.csv`.
- **Nếu sửa trực tiếp trong Word, phải đưa sửa đổi về `tieuluan/` trước khi dựng lại**, nếu không bản dựng mới sẽ ghi đè. Cách kiểm: so văn bản hai bản `.docx` (xem cách làm trong `revision/changelog.md`, phiên 04/10).

## Slide

Bộ slide được sửa qua nhiều vòng bằng python-pptx trên tệp của vòng trước, xen kẽ với sửa tay của NCS, nên chuỗi script trong `revision/HT21_slide_scripts/` **không dựng lại được từ đầu**. Để sửa tiếp, mở thẳng bản chốt trong `00_BAN_CHOT/`. Các công cụ dùng lại được:
- `pptx_kit.py`: hàm vẽ ô, mũi tên, bảng màu của bộ slide.
- `overflow_check.ps1`: đo chữ tràn bằng PowerPoint (`-src tệp.pptx -outCsv kết_quả.csv`).
- `fonts_r5.py`: chuẩn hóa cỡ chữ (thân bài 16pt, trích dẫn 12pt, tiêu đề 26pt).

Quy ước hiển thị: thân bài 16pt (tối thiểu 14pt ở ô dày), trích dẫn và chú thích 12pt nghiêng xám, tiêu đề 26pt.

## Việc còn mở

- Bản giải trình tiếp thu góp ý (`xuat_ban/HO_CHI_HAN_GIAI_TRINH_TIEP_THU_GOP_Y_20261002.docx`) là bản 02/10, chưa cập nhật theo các vòng sau.
- Slide 15 ghi "nhiều đợt" trong khi Bảng 3.2 ghi ba đợt; slide 13 mô tả dữ liệu Bước 2 khác 4.6.3 (sửa tay của NCS, giữ nguyên).
