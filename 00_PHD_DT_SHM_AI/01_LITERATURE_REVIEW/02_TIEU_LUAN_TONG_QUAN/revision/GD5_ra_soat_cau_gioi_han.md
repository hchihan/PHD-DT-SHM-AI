# Rà soát lại danh sách câu giới hạn (GĐ5, 02/10/2026)

Đầu vào: `revision/danh_sach_cau_gioi_han.csv` (80 câu, lập 29/09/2026, commit c6bf754). Quét lại toàn văn `tieuluan/`
hiện tại (trừ chú thích ẩn và `99_tailieu.md`) theo cùng năm cụm từ của CLAUDE.md 4.5 ("không phải", "không chứng minh",
"không thay thế", "không đồng nghĩa", "không đủ"); ghép với danh sách cũ theo độ giống câu, rồi kiểm tay.
Sản phẩm: `revision/danh_sach_cau_gioi_han_v2.csv` (52 dòng, cột `loai_de_xuat`, `xu_ly`, `cau_de_xuat`, `stt_cu`).
**Chưa sửa câu nào trong `tieuluan/`**; chỉ sửa sau khi NCS duyệt danh sách v2.

## 1. So với bản 29/09

| | Số câu |
|---|---|
| Danh sách cũ | 80 |
| Đã mất khỏi văn bản do các phiên đồng bộ 01–02/10 (chủ yếu Chương 5: 5.2–5.7, 5.9 viết lại; Dẫn nhập viết lại; 1.7 rút gọn; 4.5.3, 4.5.4) | 35 (Ch.5: 28; Ch.1: 2; Ch.4: 3; Ch.3: 1; Dẫn nhập: 1) |
| Còn trong văn bản (giữ nguyên hoặc sửa nhẹ) | 46 |
| Mới xuất hiện | 6 (trong đó 3 là kết quả quét nhầm, đề xuất bỏ) |
| **Danh sách v2** | **52**, sau khi bỏ quét nhầm và câu thuật lại nguồn: **43 câu cần quyết định** |

Mật độ câu giới hạn trong thân bài đã giảm đáng kể nhờ các phiên đồng bộ; phần còn lại tập trung ở Ch.1 (13), Ch.3 (14), Ch.4 (9), Ch.5 (11, trong đó 5 câu đã ở mục giới hạn 5.8).

## 2. Đề xuất theo loại

| Loại | Số | Xử lý đề xuất |
|---|---|---|
| A – phân định khái niệm | 23 | 5 câu giữ dạng phân định (Ch.1: 2; Ch.2: 1; Ch.3: 2; Ch.4: 1, trong giới hạn 3–4 câu mỗi chương), 1 câu ở mục 5.8 giữ; 17 câu viết lại khẳng định (phần lớn chỉ bỏ vế "không phải …" ở cuối câu) |
| B – tự hạ đóng góp | 11 | 6 câu chuyển thành câu kế thừa có dẫn nguồn; 4 ô bảng 5.1 đổi "Không phải khoảng trống" thành "Đã có tiền lệ"; 1 câu xóa (3.5, câu sau đã nêu trọng tâm) |
| C – giới hạn kết luận | 12 | 4 câu ở mục 5.8.2 giữ (đúng chỗ); 2 câu xóa khỏi thân bài, thay câu trỏ 5.8; 6 câu viết lại khẳng định (trong đó 1.4.2 giữ tại chỗ vì là cam kết QĐ 2, viết theo hướng "tiểu luận trình bày thiết kế, kết quả thuộc bài báo chuyên đề") |
| – không cần sửa | 6 | 3 quét nhầm ("không phải hỏi lại", "không đủ nhãn"); 3 câu thuật lại nguồn ([14], [60], [67]) |

Câu A giữ dạng phân định (đề xuất): 1.1.2 "tích hợp dữ liệu không đồng nghĩa với truy vết thông tin"; 1.6.3 nguyên tắc
"Bằng chứng hiện tại chưa đủ"; 2.2.3 hồ sơ là bản ghi, không phải thuộc tính tĩnh; 3.1.3 dữ liệu dao động không đủ để xác
định nguyên nhân; 3.3.1 cửa sổ không phải đơn vị độc lập; 4.2.2 quan hệ cảm biến – cấu kiện khác quan hệ bằng chứng – cấu kiện.

## 3. Ngoài phạm vi quét
- Quét chỉ theo năm cụm từ của CLAUDE.md 4.5; các câu phủ định dùng từ khác ("chưa", "không dùng", "không nhằm") không
  được liệt kê. Nếu NCS muốn, có thể mở rộng ở phiên sửa.
- Mục 5.8 hiện có các câu "Nó không chứng minh …" (5.8.2). Theo 4.5, đây là đúng chỗ; có thể đổi giọng sang "được xác lập
  trong phạm vi …" khi đánh số lại mục.
