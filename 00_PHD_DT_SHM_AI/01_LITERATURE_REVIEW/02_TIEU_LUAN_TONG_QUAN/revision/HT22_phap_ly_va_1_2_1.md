# HT22 — Viết lại 1.1.2 (pháp lý) và đoạn đầu 1.2.1 (04/10/2026)

Bản Word: `xuat_ban/HO_CHI_HAN_TIEU_LUAN_TONG_QUAN_FINAL_ASSET_RATIONALE_r3.docx` (71 trang, 90 tài liệu, mục lục đã cập nhật).
Slide: `BAO_CAO_TLTQ_FINAL_20261004_r3.pptx` (slide 3, 4, 6 đồng bộ; script `revision/HT21_slide_scripts/patch_ht22.py`).
So với r2 (chuẩn hóa số trích dẫn): chỉ khác ở 1.1.2, đoạn đầu và đầu đoạn hai của 1.2.1, số tài liệu ở 1.5.2.

**Thay đổi so với quyết định cũ.** CLAUDE.md QĐ 16(m) chỉ cho nêu số hiệu, tên, ngày, hiệu lực của Nghị định 207/2026, không nêu số điều, vì
khi đó chưa đối chiếu được văn bản gốc. Lần này đã đọc trực tiếp bản PDF có chữ ký trong Zotero (`R5P8K8CG`, bản quét, đọc bằng
ảnh trang 46–48) và toàn văn Thông tư 32/2026 (`HNY4EZVB`), nên số điều được nêu. Cần NCS duyệt để thay QĐ 16(m).

## 1. Nguồn đã đọc

| Nguồn | Phần đã đọc | Dùng cho |
|---|---|---|
| NĐ 207/2026/NĐ-CP [11] (`R5P8K8CG`) | Điều 36 (tr. 46), Điều 37 (tr. 47), Điều 38 khoản 1–3 (tr. 48) | Kiểm tra (Đ36 k2; Đ38 k2: trực quan, số liệu quan trắc thường xuyên nếu có, thiết bị chuyên dụng); ba trường hợp quan trắc (Đ37 k1); phân tích, so giới hạn (Đ37 k2); hồ sơ bảo trì (Đ38 k1) |
| TT 32/2026/TT-BXD (`HNY4EZVB`, mới trích) | Toàn văn 7 trang | Đ3 k1: đề cương quan trắc thi công gồm phương pháp phân tích, xử lý số liệu; Đ6 k3: nội dung quan trắc phục vụ bảo trì (phạm vi, thông số ví dụ nghiêng, lún, nứt, võng, chuyển vị, giới hạn, thời gian, chu kỳ); Phụ lục: nhà, kết cấu nhịp lớn dạng khung thuộc danh mục khi ở cấp đặc biệt |
| TCVN 9360:2024 (`EAFCGACH`, mới) | Trang mô tả trên cổng VSQI (tên, phạm vi, hiệu lực) | Ví dụ phương pháp đo đã tiêu chuẩn hóa (độ lún, đo cao hình học) |
| TCVN 9399:2012 (`T2X2CV6F`, mới) | Trang mô tả trên cổng VSQI | Ví dụ phương pháp đo đã tiêu chuẩn hóa (chuyển dịch ngang, trắc địa) |
| Qin và cs. 2024 (`S96MXF6A`) | Toàn văn, tr. 1–2 | 1.2.1: công năng, phần lớn quỹ công trình; thiệt hại lũ 2022 (>1 tỷ AUD cho nhà thương mại, công nghiệp; số liệu tác giả dẫn lại) |
| Hemker và cs. 2019 [22] | Toàn văn, tr. 187 | 1.2.1: hư hỏng phát hiện muộn có thể làm suy giảm nghiêm trọng năng lực làm việc của nhà máy |

Bỏ khỏi văn bản: số liệu khu công nghiệp của Cục Đầu tư nước ngoài (`XM5ZUP99`, bài báo Hiếu Phương), theo yêu cầu NCS. Mục Zotero giữ nguyên.

## 2. Phát biểu là nhận định của tiểu luận (đã gắn nhãn trong văn bản)

- Với nhà công nghiệp khung thép không thuộc cấp đặc biệt, quan trắc phục vụ bảo trì thực hiện theo trường hợp; kiểm tra trực quan định kỳ vẫn là hình thức chính. Suy từ Đ37 k1 NĐ 207 và Phụ lục TT 32; cấp công trình của từng nhà xưởng chưa được xác định trong tiểu luận.
- Trong các văn bản đã rà soát, chưa có hướng dẫn phương pháp cho quan trắc dao động, cho việc dùng số liệu quan trắc làm căn cứ kiểm tra, hay cho việc ghi liên kết quan trắc – cấu kiện – hành động. Phạm vi rà soát: NĐ 207/2026, TT 32/2026, hai TCVN trắc địa nêu trên, TCVN 9381:2012 đã có. Chưa rà toàn bộ danh mục TCVN.
- Nhà công nghiệp khung thép gắn trực tiếp với sản xuất và lưu trữ hàng hóa, nên hậu quả sự cố gồm cả thời gian gián đoạn.

## 3. Việc còn mở

1. NCS duyệt câu chữ 1.1.2, 1.2.1 và việc thay QĐ 16(m).
2. Nếu cần khẳng định mạnh hơn về việc "chưa có tiêu chuẩn phương pháp quan trắc dao động", cần rà danh mục TCVN trên VSQI theo từ khóa (dao động, rung, quan trắc kết cấu); hiện chỉ phát biểu trong phạm vi văn bản đã rà.
3. Sau khi duyệt: cập nhật changelog, CLAUDE.md (QĐ 16(m), (n): 90 tài liệu), commit đúng tệp.
