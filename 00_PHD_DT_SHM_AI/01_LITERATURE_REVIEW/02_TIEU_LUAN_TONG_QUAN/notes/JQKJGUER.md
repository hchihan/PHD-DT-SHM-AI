# JQKJGUER — Kapoor & Narayanan (2023) — [53]

Kapoor S, Narayanan A. Leakage and the reproducibility crisis in machine-learning-based science. *Patterns* 4: 100804.
DOI 10.1016/j.patter.2023.100804. Xuất bản trực tuyến 04/08/2023, số ra 08/09/2023 (tr. 1, 9).

**Bản đã đọc (QA nguồn, theo skill deep-read):** toàn văn bản PDF của nhà xuất bản, truy cập mở CC BY, tệp
`pdf/JQKJGUER_KapoorNarayanan2023.pdf` (13 tr. PDF; trang in 1–10 cộng tài liệu tham khảo; trang in = trang PDF − 1).
Trích văn bản bằng PyMuPDF; Hình 1 (bảng khảo sát 22 bài) và Hình 3 chỉ đọc qua chú thích và lời bàn. Phần phụ lục bổ sung
(model info sheet 21 câu hỏi, mục S1–S4) **không có trong tệp** và chưa đọc. Số trang dưới đây là trang in. Đọc ngày
01/10/2026, phiên T1-4.

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu (AUTHOR-STATED); **[NCS]** nhận định của NCS (READER-INFERRED).

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | JQKJGUER / [53] |
| Tier / Cụm | Tier 1 / Độ tin cậy đánh giá |
| Luận điểm | Rò rỉ dữ liệu (data leakage) là lỗi phổ biến của khoa học dựa trên học máy, làm hiệu năng bị đánh giá lạc quan; tác giả phân loại tám dạng rò rỉ và đề xuất "phiếu thông tin mô hình" (model info sheet) buộc người nghiên cứu lập luận rằng tập kiểm tra tách sạch, đặc trưng hợp lệ và tập kiểm tra lấy từ đúng phân bố mà khẳng định khoa học hướng tới (tr. 1, 3–6). |
| Bằng chứng | Khảo sát 22 bài tổng quan ở 17 lĩnh vực, cùng ghi nhận rò rỉ ở 294 bài, trình bày như cận dưới, không phải tổng quan hệ thống (tr. 2–3); nghiên cứu tái lập trong dự báo nội chiến: 12 bài có đủ mã và dữ liệu, 4 bài có lỗi rò rỉ, sau khi sửa thì mô hình học máy phức tạp không tốt hơn hồi quy logistic (tr. 6–8, Hình 3). |
| Giới hạn | Xem mục 5. |
| Tác động K1/K2/K3 | K1: mở rộng (căn cứ phương pháp rằng kết quả học máy cần kèm lập luận về đơn vị độc lập và phân bố áp dụng; và rằng chuẩn báo cáo hiện có không xử lý rò rỉ). K2, K3: không liên quan. |
| Vị trí sử dụng | 3.4 (độ tin cậy, kiểm soát rò rỉ); 5.6A.2 (đã trích); 1.3A/3.4.2 (phạm vi hiệu lực gắn với phân bố áp dụng); 5.7 (báo cáo bất định). |
| Mức đã đọc | Toàn văn (trừ phụ lục bổ sung) |

## Định tuyến (skill govern-phd-evidence)

```text
RQ: RQ1
WP: WP1
Chương: tiểu luận 3.4 (độ tin cậy của đánh giá); luận án: chương bằng chứng phòng thí nghiệm
Paper: Paper 1 (chỉ thiết kế đánh giá; không dùng kết quả Paper 1 trong tiểu luận)
Evidence Gate: G1 (theo bản đồ của skill; trạng thái Gate: Evidence is currently insufficient.)
Scope: Core (tiêu chí đánh giá)
Evidence type: Laboratory evidence (phương pháp đánh giá)
```

Không thuộc: WP2–WP4 (bài không bàn truy vết hay hành động). Thứ cấp: 5.5 (ý tưởng phiếu thông tin cho bằng chứng, xem mục F).

## 1. Câu hỏi nghiên cứu và đối tượng

- Câu hỏi: mức độ và dạng của các vấn đề tái lập do rò rỉ trong khoa học dùng học máy; cách phát hiện và ngăn (tr. 1–2).
- Phạm vi: "khoa học dựa trên học máy", tức dùng hiệu năng mô hình làm bằng chứng cho một khẳng định khoa học; tác giả
  tách khỏi nghiên cứu phương pháp học máy, ứng dụng kỹ thuật và cuộc thi mô hình (tr. 1, 3–4).
- Đối tượng kiểm chứng: dự báo nội chiến (khoa học chính trị). Không có dữ liệu kết cấu.

## 2. Phương pháp và kiến trúc thông tin

- Phân loại tám dạng rò rỉ (tr. 4–5): [L1] tách huấn luyện – kiểm tra không sạch (không có tập kiểm tra; tiền xử lý trên
  toàn bộ; chọn đặc trưng trên toàn bộ; bản ghi trùng); [L2] đặc trưng không hợp lệ (ví dụ đại diện của biến đích); [L3]
  tập kiểm tra không lấy từ phân bố mà khẳng định hướng tới (rò rỉ theo thời gian; **không độc lập giữa huấn luyện và
  kiểm tra**, ví dụ cùng đơn vị ở cả hai tập; thiên lệch chọn mẫu).
- Phiếu thông tin mô hình: 21 câu hỏi, gom thành ba lập luận bắt buộc: tách sạch, mọi đặc trưng hợp lệ, tập kiểm tra
  đúng phân bố (tr. 5–6). Lấy cảm hứng từ thẻ mô hình (model cards) của Mitchell và cs. 2019.
- Không có kiến trúc thông tin hay chuẩn dữ liệu.

## 3. Cách kiểm chứng

- Dữ liệu thật của các bài gốc; tái phân tích có mã công khai trên CodeOcean (tr. 9).
- Chỉ số: AUC, độ chính xác; kiểm định so sánh AUC làm trơn, khoảng tin cậy bootstrap (tr. 7).
- Đường cơ sở: hồi quy logistic của chính các bài gốc (tr. 7, Hình 3).
- Phiếu thông tin mô hình được thử trên bốn bài có lỗi: phát hiện được từng dạng rò rỉ đã gặp (tr. 7). Chưa thử trên các
  lĩnh vực khác.

## 4. Luận điểm chính

1. Rò rỉ có mặt trong mọi lĩnh vực đã có tổng quan về lỗi học máy; 294 bài bị ảnh hưởng là cận dưới (tr. 2–3).
2. Khi đơn vị (người, mẫu, họ protein) nằm ở cả tập huấn luyện và tập kiểm tra, hiệu năng đo được không đại diện cho
   khẳng định về đơn vị mới; cần chia theo khối hoặc theo cấu trúc phụ thuộc (tr. 4–5).
3. Biện pháp chống rò rỉ của cuộc thi và ứng dụng kỹ thuật không chuyển sang khoa học, vì người nghiên cứu có toàn bộ dữ
   liệu và khẳng định khoa học nhạy với khác biệt nhỏ (tr. 3–4).
4. Chuẩn báo cáo hiện có (checklist, thẻ mô hình) không xử lý rò rỉ; người nghiên cứu phải chịu nghĩa vụ chứng minh
   bằng lập luận tường minh (tr. 3, 5).
5. 9/12 bài có mã không kiểm định ý nghĩa hay định lượng bất định khi so sánh mô hình (tr. 7).

## 5. Giới hạn (bảng theo skill deep-read, mục D)

| ID | Trạng thái | Giới hạn / hướng | Vị trí | Khẳng định bị ảnh hưởng | Liên quan luận án |
|---|---|---|---|---|---|
| D1 | AUTHOR-STATED | Khảo sát là cận dưới, không phải tổng quan hệ thống; thuật ngữ khác nhau giữa các ngành làm khó tìm (L-DATA) | tr. 2–3 | Mức độ phổ biến | Không dùng con số 294 như tỷ lệ |
| D2 | AUTHOR-STATED | Phiếu thông tin mô hình không kiểm chứng được nếu thiếu tái lập tính toán; có thể tạo cảm giác an toàn sai; đòi hỏi chuyên môn học máy (L-REPORT) | tr. 6 | Hiệu quả của phiếu | Lý do phiếu phải đi kèm mã, dữ liệu, phiên bản |
| D3 | AUTHOR-STATED | Xử lý không độc lập khi chưa biết cấu trúc phụ thuộc là bài toán khó (L-METHOD) | tr. 5 | Cách chia dữ liệu | Đơn vị độc lập phải được xác định từ hiểu biết vật lý (lần lắp, đợt đo) |
| D4 | AUTHOR-STATED | Khái quát sang phân bố khác (dịch chuyển phân bố) là vấn đề mở; cách tốt nhất hiện nay là kiểm tra trên dữ liệu của phân bố muốn khẳng định (L-SCALE) | tr. 5 | Chuyển giao | Căn cứ cho phạm vi hiệu lực và cho 3.6 |
| D5 | READER-INFERRED | Ca kiểm chứng ở khoa học xã hội, dữ liệu bảng; chưa có ví dụ chuỗi thời gian hay tín hiệu đo (L-SCALE) | tr. 6–7 | Áp dụng cho SHM | Áp sang dao động bu lông là diễn giải |
| D6 | READER-INFERRED | Phiếu gắn với **mô hình** trong một bài báo, không gắn với từng kết quả được dùng về sau (L-TRACE) | tr. 5–6 | Truy vết | Gợi ý cho bản ghi bằng chứng (mục F) |

## 6. Điều bài KHÔNG xử lý, xét theo chuỗi của luận án

| Ý | Mức | Căn cứ |
|---|---|---|
| Nguồn gốc bằng chứng cảm biến | xử lý một phần (ở mức mô hình) | Phiếu thông tin ghi lập luận về dữ liệu và chia tập (tr. 5–6); không có bản ghi từng kết quả |
| Phạm vi hiệu lực của bằng chứng | xử lý một phần | Lập luận "tập kiểm tra đúng phân bố của khẳng định" (tr. 6) là phạm vi ở mức khẳng định; không gắn với từng kết quả |
| Quan hệ bằng chứng – cấu kiện có thời hạn | không xử lý | — |
| Trách nhiệm, thẩm quyền | không xử lý | Chỉ nói nghĩa vụ chứng minh thuộc người nghiên cứu (tr. 5) |
| Trạng thái hành động và lịch sử chuyển trạng thái | không xử lý | — |
| Truy ngược từ hành động về dữ liệu gốc | không xử lý | — |

## 7. Tác động tới K1/K2/K3 (bảng theo skill phd-gap-miner)

| Nguồn | Claim | Evidence | Loại | Gap | Gap-impact | Mức bảo vệ (đánh giá làm việc) | Allowed-usage-location |
|---|---|---|---|---|---|---|---|
| [53] | Chuẩn báo cáo học máy hiện có không xử lý rò rỉ | tr. 3, 5 (AUTHOR-STATED) | DATA / METHOD | K1 | WIDENS | không đổi từ một nguồn | 3.4; 5.2 (sau ĐD3) |
| [53] | Đơn vị chung giữa tập huấn luyện và kiểm tra là rò rỉ | tr. 4–5 (AUTHOR-STATED) | METHOD | K1 | WIDENS (căn cứ phương pháp) | như trên | 3.4; 1.3A |
| [53] | Phiếu thông tin mô hình là cách ghi lập luận về phạm vi | tr. 5–6 (AUTHOR-STATED) | — | K1 (UV-02) | NARROWS một phần: đã có khuôn báo cáo ở mức mô hình | như trên | 3.4; 5.5 (tiền lệ) |

## 8. Vị trí sử dụng trong tiểu luận v2

- 3.4: phân loại rò rỉ, đặc biệt L3.2 (không độc lập) và L3.3 (phân bố); nghĩa vụ lập luận của người nghiên cứu.
- 5.6A.2: đã trích cho đánh giá theo nhóm.
- 5.5: phiếu thông tin mô hình là tiền lệ cho phần "phạm vi hiệu lực" và "nguồn gốc" của bản ghi bằng chứng; nêu như
  kế thừa, không như đóng góp mới.
- Không dùng ví dụ nội chiến như căn cứ cho SHM; chỉ dùng phần phương pháp.

## F. Ý tưởng ứng viên (sàng lọc tám tiêu chí của skill deep-read)

| Ý tưởng | Giới hạn gốc | Fit | Evidence | Data | Method | Novelty | Boundary | Priority | Quyết định |
|---|---|---|---|---|---|---|---|---|---|
| Mở rộng phiếu thông tin mô hình thành **phiếu cho từng bản ghi bằng chứng** (lập luận về đơn vị, chia tập, phân bố áp dụng được lưu như trường của bản ghi, có phiên bản) | D2, D6 | PASS | PARTIAL ([53] + [19] + [18]) | PASS (dữ liệu WP1) | PARTIAL (cần tiêu chí đánh giá) | UNKNOWN (chưa kiểm thẻ mô hình Mitchell 2019, MLflow) | PASS | PASS (Gate 1–2) | ADD TO REVIEW |

## G. Claim → Evidence → Limitation → Next action

- **Claim:** Kết quả phân loại trên dữ liệu dao động chỉ dùng được như bằng chứng khi đi kèm lập luận tường minh về đơn vị
  độc lập và phân bố áp dụng.
- **Evidence:** [53] tr. 4–6 (phân loại rò rỉ, ba lập luận bắt buộc); cùng chiều với [18], [19] về lần lắp ráp.
- **Limitation:** [53] không thuộc lĩnh vực kết cấu; phiếu ở mức mô hình, chưa ở mức từng kết quả.
- **Next action:** kiểm phản chứng cho UV-02: thẻ mô hình (Mitchell và cs. 2019) và công cụ quản lý phiên bản mô hình
  (MLflow/DVC), trước khi coi "ghi phạm vi ở mức bản ghi" là phần còn thiếu. Gate gần hơn: G1 (thiết kế đánh giá).

## I. Bài học năm phút (TUTOR-EXPLANATION, dựa trên phần SOURCE-VERIFIED ở trên)

1. **Vấn đề:** nhiều ngành dùng học máy rồi báo cáo hiệu năng cao, nhưng con số đó thường bị thổi phồng vì thông tin của
   tập kiểm tra "lọt" vào lúc huấn luyện.
2. **Vì sao quan trọng:** khi hiệu năng là bằng chứng cho một khẳng định khoa học, con số sai dẫn tới kết luận sai; ở dự
   báo nội chiến, ưu thế của mô hình phức tạp biến mất khi sửa rò rỉ (tr. 7).
3. **Tác giả làm gì:** gom 22 bài tổng quan, phân loại tám dạng rò rỉ, đề xuất phiếu 21 câu hỏi, và tự tái lập 12 bài.
4. **Phát hiện:** rò rỉ có mặt ở mọi lĩnh vực đã được rà; lỗi hay gặp là tiền xử lý trên toàn bộ dữ liệu, đặc trưng là
   đại diện của biến đích, và chia tập không tôn trọng cấu trúc phụ thuộc.
5. **Không chứng minh:** tỷ lệ rò rỉ thực trong từng ngành; hiệu quả của phiếu ngoài bốn bài đã thử.
- **Áp vào luận án (THESIS-APPLICATION):** với khung thép bu lông, "đơn vị" là lần lắp ráp hoặc đợt đo (xem [18], [19]);
  nhiều cửa sổ cắt từ một lần đo rơi vào cả hai tập là đúng dạng L3.2. Phiếu của [53] gợi ý ghi lập luận này vào chính bản
  ghi bằng chứng.
