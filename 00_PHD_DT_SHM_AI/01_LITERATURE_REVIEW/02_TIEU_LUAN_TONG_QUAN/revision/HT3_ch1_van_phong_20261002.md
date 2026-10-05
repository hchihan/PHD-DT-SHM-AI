# HT3 – Pha 3, Chương 1: Biên tập văn phong (02/10/2026)

Theo prompt mục 6 và skill `strict-writing-discipline`. Giữ nguyên trích dẫn, số liệu, thuật ngữ; không đổi nghĩa; không thêm tài liệu. Kèm hai quyết định NCS: LORO = giữ lại toàn bộ một lần chạy; Bài 1 chạy thêm mốc cùng lần chạy (đã ghi vào `00_DONG_BO_PIPELINE…` bản v1.4).

## 1. Số đo trước / sau
| Chỉ tiêu | Trước | Sau |
|---|---:|---:|
| Số từ (bỏ chú thích ẩn) | 11.327 | 10.893 |
| Câu > 45 âm tiết | 69 | 54 |
| Câu > 60 âm tiết | 29 | 15 |
| Bôi đậm trong văn xuôi | 35 | 0 (còn 5 nhãn a)–e) ở 1.8.5, dùng như tiêu đề nhỏ) |
| Cụm câu giới hạn (năm cụm CLAUDE 4.5 và "chưa đủ", "không tự") | 21 | 6 (1 quét nhầm "không phải hỏi lại"; còn khoảng 4 câu loại A, đúng giới hạn 3–4) |
| Ngoặc kép cong | 12 | 0 |

## 2. Nhóm thay đổi
| Nhóm | Số chỗ (tính theo lệnh sửa) |
|---|---:|
| bôi đậm | 18 |
| tách câu | 13 |
| bôi đậm 1.10 | 5 |
| giới hạn A | 4 |
| lặp ý | 3 |
| giới hạn B | 3 |
| ngôi | 2 |
| giới hạn C | 2 |
| lặp ý (1.8.1) | 2 |
| lặp ý (đã ở 1.1.3 | 1 |
| 5.9.3) | 1 |
| giới hạn A/C | 1 |
| từ cấm | 1 |
| câu dài | 1 |
| từ cấm (không chỉ … mà còn) | 1 |

Ghi chú:
- Câu dài còn lại chủ yếu là câu liệt kê theo nguồn (trích Nghị định 207/2026 ở 1.1.4; danh sách câu hỏi ở 1.5.1; danh mục nhóm chủ đề ở 1.7.3, 1.8.2), giữ để không cắt rời nội dung trích.
- Bỏ ba đoạn lặp: câu Çelik/Wu ở 1.4 (giữ ở 1.5.4); câu Beleites/Wheat ở 1.5.2 (giữ ở 1.3, 3.4); câu FEM ở 1.7.4 (giữ ở 1.1.3, 5.9.3); hai đoạn mở 1.8.5 và đoạn đầu 1.8.5e (trùng 1.8.1).
- 1.7.5 rút từ bốn câu "chỉ chứng minh" xuống hai câu, trỏ 5.9.2. 1.8.3 viết lại dạng "A khác B" thay cho năm câu "không tự chứng minh".
- 1.10: tên chương bỏ bôi đậm, đặt trong ngoặc.
- "Tiểu luận rút ra một diễn giải" (1.2.2) → "Theo đánh giá của phần tổng quan nghiên cứu này"; "Nghiên cứu xem" (1.1.1) → "Luận án xem". Câu "Từ thực tế kiểm định…" (1.2.1) giữ theo quyết định NCS.

## 3. Ví dụ trước / sau
| Nhóm | Trước | Sau |
|---|---|---|
| tách câu | Ở từng mắt xích, nền kỹ thuật đã tương đối rõ: lược đồ IFC có thể được mở rộng để biểu diễn hệ theo dõi trạng thái và quan hệ giữa cảm biến với cấu kiện \[2\]; dữ liệu vận hành có thể được tích hợp với mô hình số ở cấp công trình và khuôn viên \[3\]; định danh toàn cục của đối tượng IFC có thể dùng để nối mô hình với cơ sở dữ liệu chuỗi thời gian \[4\], \[5\]. | Ở từng mắt xích, nền kỹ thuật đã tương đối rõ. Lược đồ IFC có thể được mở rộng để biểu diễn hệ theo dõi trạng thái và quan hệ giữa cảm biến với cấu kiện \[2\]. Dữ liệu vận hành có thể được tích hợp với mô hình số ở cấp công trình và khuôn viên \[3\]. Định danh toàn cục của đối tượng IFC có thể dùng để nối mô hình với cơ sở dữ liệu chuỗi thời gian \[4\], \[5\]. |
| lặp ý |  Phần thứ ba đã có tiền lệ từng phần: Çelik và cộng sự (2023) ghi nguồn gốc dữ liệu, tác nhân, thời điểm và phiên bản trong trao đổi thông tin xây dựng \[16\], còn Wu và cộng sự (2026) xây dựng khung kiểm định công trình có chuyên gia tương tác và rà soát \[17\]. |  Tiền lệ cho từng phần của câu hỏi thứ ba được trình bày ở Mục 1.5.4. |
| giới hạn A | Tuy vậy, **tích hợp dữ liệu không đồng nghĩa với truy vết thông tin**. | Tuy vậy, tích hợp dữ liệu chưa bảo đảm truy vết thông tin. |
| giới hạn B | Những nguyên tắc này không mới; giá trị của chúng là làm rõ **một kết quả có thể được tin cậy trong phạm vi nào**. Luận án dùng khái niệm **bằng chứng trạng thái** | Luận án kế thừa các nguyên tắc này từ \[14\], \[15\] để làm rõ một kết quả có thể được tin cậy trong phạm vi nào. Luận án dùng khái niệm bằng chứng trạng thái |
| giới hạn C |  Ở giai đoạn tổng quan, **bằng chứng chưa đủ để khẳng định sự vắng mặt phổ quát** của một chuỗi như vậy trong các nghiên cứu quốc tế. Phạm vi của phát biểu này được trình bày ở Mục 5.9.4. |  Phát biểu về điểm nối này giới hạn trong tập tài liệu đã rà soát (Mục 5.9.4). |

## 4. Danh sách đầy đủ
47 lệnh sửa, xem `revision/HT3_ch1_edits.json` (trước/sau nguyên văn).

## 5. Việc còn mở
- Chương 2–5, Dẫn nhập, Phụ lục: biên tập ở các phiên sau.
- Hình 1.1 còn ô "Hồ sơ kiểm tra" (nhãn cũ).

ĐIỂM DỪNG 3 – Chương 1.
