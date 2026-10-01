# 82WQNDHU — Mitchell và cs. (2019)

Mitchell M, Wu S, Zaldivar A, Barnes P, Vasserman L, Hutchinson B, Spitzer E, Raji ID, Gebru T. Model cards for model
reporting. In: *Proceedings of the Conference on Fairness, Accountability, and Transparency* (FAT* '19), Atlanta,
29–31/01/2019. ACM, tr. 220–229. DOI 10.1145/3287560.3287596 (Crossref xác minh 01/10/2026).

**Bản đã đọc:** bản arXiv 1810.03993v2 (14/01/2019), tệp `pdf/82WQNDHU_Mitchell2019_arXiv.pdf` (10 tr., định dạng ACM giống
bản in; trang đầu ghi DOI của bản in). Đọc toàn văn ngày 01/10/2026, kiểm phản chứng UV-02, UV-07 (N-21, N-24). Bài được [53]
dẫn. **Trang dẫn dưới đây là trang PDF của bản arXiv**; quy đổi dự kiến tr. in = 219 + tr. PDF, cần đối chiếu bản in (N-04).

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | 82WQNDHU / mới (phanchung-GD2) |
| Tier / Cụm | Bổ sung phản chứng (không thuộc 30 key) / Độ tin cậy đánh giá |
| Luận điểm | Mô hình học máy khi phát hành nên kèm "thẻ mô hình" (model card) 1–2 trang, nêu chi tiết mô hình, mục đích sử dụng, yếu tố ảnh hưởng hiệu năng, chỉ số, dữ liệu đánh giá – huấn luyện, phân tích định lượng tách theo nhóm và điều kiện, cân nhắc đạo đức, lưu ý (tr. PDF 1–3, Hình 1). |
| Bằng chứng | Đề xuất khung tài liệu; hai thẻ mẫu (bộ phân loại nụ cười trên CelebA; bộ chấm điểm độc hại của Perspective API, phiên bản 1 và 5) (tr. PDF 6–8, Hình 2–3). Không có đánh giá thực nghiệm về hiệu quả của thẻ. |
| Giới hạn | Xem mục 3. |
| Tác động K1/K2/K3 | K1 (UV-02): giải quyết một phần — có tiền lệ cho **nội dung** phạm vi hiệu lực ở mức mô hình. K3 (UV-07): không liên quan trực tiếp. K2: không liên quan. |
| Vị trí sử dụng | 3.4 hoặc 3.5 (tiền lệ ghi phạm vi sử dụng ở mức mô hình); 5.5 (`VALIDITY_SCOPE`: "out-of-scope use cases", yếu tố thiết bị đo và môi trường); 5.6A (thẻ mô hình là một nguồn để cấp `method_version`). |
| Mức đã đọc | Toàn văn (01/10/2026), bản arXiv v2 |

## 1. Nội dung thẻ mô hình (a)

- **Chi tiết mô hình** (tr. PDF 3–4): người/tổ chức phát triển, ngày, **phiên bản** ("Which version of the model is it, and how
  does it differ from previous versions?"), loại mô hình, thuật toán, tham số, giấy phép.
- **Mục đích sử dụng** (tr. PDF 4): mục đích chính, người dùng chính và **trường hợp ngoài phạm vi** (out-of-scope uses), ví dụ
  "for use on black-and-white images only".
- **Yếu tố** (tr. PDF 4–5): nhóm, **thiết bị đo** (instrumentation — hiệu năng thay đổi theo phần cứng, thiết lập ghi), **môi
  trường** triển khai (ánh sáng, độ ẩm); phân biệt yếu tố liên quan và yếu tố đã được đánh giá.
- **Chỉ số** (tr. PDF 5): chỉ số hiệu năng, ngưỡng quyết định, **cách tính độ bất định và biến thiên** (độ lệch chuẩn, khoảng tin
  cậy; "average of 5 runs, 10-fold cross-validation").
- **Dữ liệu đánh giá, huấn luyện; phân tích định lượng** tách theo yếu tố, kèm khoảng tin cậy (tr. PDF 5–6).
- Thẻ Perspective API ghi "Not intended for fully automated moderation" (tr. PDF 8); hai phiên bản mô hình có kết quả khác hẳn,
  nên thẻ phải cập nhật theo mỗi lần phát hành (tr. PDF 6).

## 2. Đoạn dùng được cho tiểu luận

| Luận điểm trong tiểu luận | Trang (PDF arXiv) | Loại |
|---|---|---|
| Đã có đề xuất ghi phạm vi sử dụng của mô hình học máy, gồm trường hợp ngoài phạm vi, yếu tố thiết bị đo và môi trường | 4–5 | trực tiếp |
| Thẻ mô hình ghi phiên bản và cách ước lượng độ bất định của chỉ số | 3–5 | trực tiếp |
| Thẻ mô hình là tài liệu đi kèm **mô hình**, do người lập soạn; độ tin cậy phụ thuộc người lập | 9 | trực tiếp (TG) |
| Phạm vi hiệu lực của luận án gắn vào **từng** bằng chứng và được kiểm khi bằng chứng được dùng | — | diễn giải của NCS |

## 3. Giới hạn

- (b) Tính hữu ích và độ chính xác của thẻ dựa vào sự trung thực của người lập; khó chuẩn hóa đủ để ngăn trình bày sai lệch;
  thẻ chỉ là một công cụ minh bạch bên cạnh kiểm toán thuật toán của bên thứ ba (tr. PDF 9).
- (b) Dữ liệu đánh giá phù hợp cho phân tích tách nhóm chưa phổ biến (tr. PDF 3).
- **[NCS]** Thẻ ở mức **mô hình đã phát hành**, dạng văn bản cho người đọc; không có cơ chế gắn thẻ vào từng kết quả dự đoán, không
  có cách kiểm bằng máy rằng một lần sử dụng kết quả nằm trong phạm vi đã khai. Hướng tới mô hình về con người (thị giác máy, ngôn
  ngữ), không bàn dữ liệu đo kết cấu.

## 4. Kiểm phản chứng

- **UV-02 (nguồn gốc, phiên bản phương pháp, phạm vi hiệu lực của đầu ra phát hiện): giải quyết một phần.** Đã có tiền lệ cho
  **nội dung** cần ghi — phiên bản mô hình, trường hợp ngoài phạm vi, yếu tố thiết bị đo và môi trường, cách tính độ bất định
  (tr. PDF 3–5) — cùng chiều với phiếu thông tin mô hình của [53]. Phần không giải quyết: thẻ ở mức mô hình, là văn bản; không đi
  theo từng kết quả; không kiểm được khi kết quả được dùng (tr. PDF 9: phụ thuộc người lập).
- **UV-07 (xác nhận của chuyên gia với đầu ra AI): không giải quyết.** Thẻ không ghi lần xác nhận đầu ra nào; câu "Not intended
  for fully automated moderation" (tr. PDF 8) chỉ nêu ý định sử dụng có người kiểm, không nêu cách ghi.
