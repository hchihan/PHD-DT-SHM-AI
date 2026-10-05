# FINAL TECHNICAL PROOFREAD REPORT

Tệp: `xuat_ban/HO_CHI_HAN_TIEU_LUAN_TONG_QUAN_FINAL_PROOFREAD.docx`, dựng từ r11 ngày 03/10/2026.
- 69 trang, 85 tài liệu, 250 trường trích dẫn Zotero cùng một trường danh mục.
- Mục lục, danh mục bảng (20) và danh mục hình (4) đã cập nhật trong Word.
- KT1–KT3, RQ1–RQ3, mục tiêu, WP, đóng góp và phạm vi giữ nguyên.

Lệnh sửa trước/sau và script nằm ở `revision/HT18_final_scripts/`.

## Corrected

| # | Vị trí | Lỗi | Cách sửa |
|---|---|---|---|
| 1 | Danh mục [34] Nguyen 2024 (`4NQWJW3U`) | Năm lấy theo ngày đăng trực tuyến (12/2024), trong khi vol. 25, no. 2 in tháng 4/2025 | Năm sửa thành 2025 trên Zotero |
| 2 | Danh mục [54] Ashworth (`R4E6KWUP`) | Như trên: online 12/2022, vol. 41 no. 5/6 in 4/2023 | Sửa thành 2023 |
| 3 | Danh mục [63] Tavakoli (`F3ZIND76`) | Online 11/2023, vol. 13 no. 1 in 1/2024 | Sửa thành 2024 |
| 4 | Danh mục [85] Mosqueira-Rey (`73MBWFVJ`) | Online 8/2022, vol. 56 no. 4 in 4/2023 | Sửa thành 2023 |
| 5 | Toàn văn (bản Word) | Pandoc tự đổi ngoặc kép thẳng thành ngoặc cong | Tắt chức năng đổi dấu tự động (`-f markdown-smart` trong `xuat_ban/build.py`). Thân bài còn 0 ngoặc cong; danh mục tài liệu giữ ngoặc cong vì kiểu IEEE quy định |
| 6 | Dẫn nhập | Lần đầu dùng "song sinh số" trong thân bài chưa kèm thuật ngữ tiếng Anh | Thêm "(Digital Twin)" |
| 7 | 2.2.2 | "bằng chứng tình trạng" lệch thuật ngữ | Sửa thành "bằng chứng trạng thái" |
| 8 | Thuật ngữ | Thiếu định nghĩa "bản ghi kiểm tra", dễ lẫn với "hồ sơ kiểm tra"; "evidence gate" viết thường | Thêm dòng "Bản ghi kiểm tra (inspection record)", phân biệt với "hồ sơ kiểm tra"; sửa thành "Evidence Gate" |

## Verified

| Nhóm | Kết quả |
|---|---|
| 75 tài liệu có DOI | Đối chiếu tự động với Crossref: tiêu đề, tác giả đầu, số tác giả, nơi công bố, tập, số, trang hoặc số bài đều khớp. Sai lệch duy nhất là năm của 4 mục ở trên. Kết quả chi tiết: `crossref.json` |
| Trùng lặp | Không có DOI trùng, không có tiêu đề trùng |
| Trích dẫn ↔ danh mục | 85/85 mục được dẫn trong thân bài; không có số trích dẫn vượt danh mục; thứ tự IEEE theo lần xuất hiện đầu đúng với cả 250 trường |
| ISO 19650-3:2020 | Tên, năm, ISO đúng |
| ISO 55000:2024 | Tên "Asset management – Vocabulary, overview and principles", năm 2024, ISO; loại mục đổi sang tiêu chuẩn ở r9 |
| IFC4 ADD2 TC1 (4.0.2.1) | buildingSMART International, 10/2017 |
| IFC 4.3 | Được dẫn qua Bellon và cộng sự [48], không có mục chuẩn riêng; tên gọi đúng theo buildingSMART |
| BCF 3.0 | Tách hai nguồn BCF-XML và BCF-API (buildingSMART, 6/2021); câu về sự kiện đổi trạng thái dẫn BCF-API mục 3.9 |
| IDS | Được dẫn qua de Marco và cộng sự (2024); tiểu luận không nêu phiên bản IDS |
| SSN | W3C Recommendation 19/10/2017 |
| PROV-O | W3C Recommendation 30/4/2013; tác giả Lebo, Sahoo, McGuinness |
| Nghị định 207/2026/NĐ-CP | Số hiệu, tên, ngày ban hành 15/6/2026, hiệu lực 01/7/2026 khớp Cổng Thông tin điện tử Chính phủ (Hội đồng đã xác minh); văn bản không nêu số điều |
| Quyết định 258/QĐ-TTg | Số hiệu, ngày 17/3/2023, Thủ tướng Chính phủ, phê duyệt lộ trình áp dụng BIM (đối chiếu qua tra cứu web 03/10/2026) |
| Tham chiếu chéo | 51 mục có tiêu đề, 20 bảng, 4 hình; mọi "Mục x.y", "Bảng", "Hình" đều có đích; mọi bảng, hình đều được nhắc trong thân bài; chú thích đánh số liên tục trong từng chương |
| Trình bày | Không có gạch dài, khoảng trắng kép, dấu cách trước dấu câu hay ngoặc lệch. Cách viết 1:10, IFC 4.3, BCF 3.0, RQ1, KT1, Gate 1 thống nhất. Tên đề tài trên bìa giữ dấu "-" theo tên đã đăng ký |
| Thuật ngữ | "song sinh kỹ thuật số" chỉ ở tên đề tài; thân bài dùng "song sinh số". Các thuật ngữ bằng chứng trạng thái, nguồn gốc, độ bất định, phạm vi hiệu lực, đường cơ sở vận hành, mức ưu tiên, trạng thái xử lý, câu hỏi năng lực và cổng kiểm chứng được dùng nhất quán |

## Needs manual verification

| # | Nội dung | Lý do |
|---|---|---|
| 1 | 1.1.2: "Quyết định 258/QĐ-TTg ... yêu cầu chủ đầu tư các dự án thuộc lộ trình cập nhật mô hình phục vụ vận hành và bảo trì" | **NEEDS MANUAL VERIFICATION.** Số hiệu, ngày, cơ quan ban hành đã khớp, nhưng nội dung yêu cầu này chưa được đối chiếu với văn bản gốc trong vòng này |
| 2 | Mục [12] Nghị định 207/2026 – đường dẫn chinhphu.vn | **NEEDS MANUAL VERIFICATION.** Đường dẫn lấy từ ý kiến Hội đồng; trong phiên này máy không mở được văn bản gốc. Cần mở một lần để xác nhận liên kết còn hoạt động |
| 3 | Các trích dẫn kèm số trang, ví dụ [48] tr. 8–10, [49] tr. 3, 19–25, FHWA tr. 67–82 | **NEEDS MANUAL VERIFICATION.** Số trang lấy từ các phiên đọc sâu trước; vòng này không đối chiếu lại PDF |
| 4 | Bảng 3.2: ba đợt, sáu lần chạy lặp, hai rồi ba vị trí cảm biến, việc tháo – lắp giữa đợt chưa được ghi | **NEEDS MANUAL VERIFICATION.** Thông tin theo Paper 1 v9; NCS xác nhận dùng số đợt và số lần lặp (khác quyết định 15b trước đây) |
| 5 | Mục [14] bài báo về khu công nghiệp: các con số 478, 324, 68 nghìn ha | Đã kiểm nguyên văn ngày 01/10/2026 ở phiên trước; trang báo có thể thay đổi |

## Bridge added

Một đoạn 5 câu ở cuối Mục 3.4.3, ngay trước Mục 3.5. Đoạn này thay câu cũ về "ca kiểm thử quy tắc" để không lặp ý. Nội dung theo đúng bốn ý yêu cầu:
1. Thí nghiệm tạo môi trường có trạng thái can thiệp được kiểm soát, để đánh giá cách một kết quả từ dữ liệu dao động trở thành bằng chứng trạng thái có nguồn gốc, độ bất định và phạm vi hiệu lực.
2. Thí nghiệm không nhằm tạo bộ phân loại để đưa ra nhà xưởng.
3. Bản ghi bằng chứng được Mục tiêu 2 dùng làm ca thử, để kiểm ba thuộc tính có được giữ và truy vết qua cấu kiện liên kết BIM, bản ghi kiểm tra và lịch sử hành động hay không (trỏ Mục 4.6.3).
4. Ở hiện trường, mô hình, bộ phân loại và ngưỡng không được chuyển; chỉ kế thừa nguyên tắc tổ chức, đánh giá và sử dụng bằng chứng (trỏ Mục 3.5).

Đã đọc thử phương án đặt đoạn ở đầu Chương 4. Vị trí cuối 3.4.3 cho mạch tốt hơn, vì đoạn khép phần thí nghiệm ngay trước khi chuyển sang hiện trường.

## Visual review

Đã thêm **một hình**: Hình 4.2 "Ba kiểu quan hệ: cảm biến – cấu kiện, bằng chứng – cấu kiện và bản ghi kiểm tra – phát hiện thực tế".
- Vị trí: Mục 4.6.1, ngay sau đoạn mô tả ba kiểu quan hệ; được gọi trong văn bản.
- Phong cách giống Hình 1.1 và 4.1: Times New Roman, khung xám, khung nhấn xanh. Script vẽ: `figures/ve_hinh_4_2.py`.
- Lý do thêm: đây là điểm Hội đồng hỏi nhiều lần (vị trí cảm biến có phải vị trí hư hỏng không). Trước đó ý này chỉ nằm trong một đoạn văn.

Không thêm hình ưu tiên thứ hai, vì Bảng 1.2 đã thể hiện chuỗi kết quả phân loại → bằng chứng trạng thái → chẩn đoán hư hỏng.

## Scope check

- **Kết quả:** không có câu vượt phạm vi cần sửa.
- **Các cụm đã rà:** "chứng minh", "đảm bảo/bảo đảm", "chính xác", "tối ưu", "phát hiện hư hỏng", "chẩn đoán hư hỏng", "toàn bộ kết cấu", "quyết định tự động", "hoàn chỉnh".
- **Các chỗ còn xuất hiện** đều thuộc ba loại: mô tả nội dung của nguồn; câu giới hạn ở dạng phủ định; hoặc nhãn trong bảng phạm vi.
- **Bảy ranh giới vẫn giữ đúng chỗ:**
  - 1:10 không chứng minh tương tự động lực học: 1.5.1, Bảng 3.2, 5.7.
  - Không định lượng mức nới lỏng: Bảng 3.2, 5.7.
  - Bộ phân loại không chuyển ra hiện trường: 1.2.2, 3.4.3, 5.7.
  - Bất thường ở hiện trường không phải chẩn đoán hư hỏng: 5.7.
  - FEM chỉ danh nghĩa, chưa hiệu chuẩn: 5.7, Bảng 5.6.
  - Song sinh số là kiến trúc đích: 2.3, 5.7.
  - Quyết định cuối thuộc kỹ sư và người có thẩm quyền: 4.5, 5.8.
- **Gate:** không thêm chi tiết Gate.

## Kết luận

**READY TO SUBMIT AFTER MANUAL CHECK**

Năm mục ở phần "Needs manual verification" là các điểm NCS cần mở nguồn gốc kiểm một lần. Không mục nào làm thay đổi lập luận hay cấu trúc. Theo tiêu chí dừng, không sửa học thuật thêm nếu không có góp ý mới từ GVHD hoặc Hội đồng.
