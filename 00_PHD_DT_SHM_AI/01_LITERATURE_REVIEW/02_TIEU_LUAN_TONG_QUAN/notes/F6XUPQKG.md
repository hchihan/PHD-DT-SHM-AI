# F6XUPQKG — Wu, El-Assady & De Wolf (2026) — [17]

Wu P-Y, El-Assady M, De Wolf C. A unified intelligence-augmented framework for building audits via physical and virtual
inspection. *Expert Systems With Applications* 302 (2026): 130514. DOI 10.1016/j.eswa.2025.130514. Nhận 04/08/2025,
chấp nhận 17/11/2025, trực tuyến 26/11/2025 (tr. 1).

**Bản đã đọc (QA nguồn):** toàn văn bản PDF của nhà xuất bản trong kho Zotero (truy cập mở CC BY, 12 tr. = tr. 1–12 của
bài). Hình 1–10 chỉ đọc qua chú thích và lời bàn. Tài liệu bổ sung trực tuyến chưa đọc. Đọc ngày 01/10/2026, phiên T1-4.
**Tài liệu nhóm 2026**: không làm căn cứ chính cho khoảng trống (CLAUDE.md 4.1).

Ký hiệu: (a) tác giả nói; (b) AUTHOR-STATED; **[NCS]** READER-INFERRED.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | F6XUPQKG / [17] |
| Tier / Cụm | Tier 1 / Truy vết thông tin (đề xuất; có thể xếp "Giá trị quyết định"; CẦN NCS KIỂM) |
| Luận điểm | Kiểm định công trình (trước phá dỡ, trước cải tạo) có thể được tổ chức thành chuỗi sáu mô-đun (truy xuất, ghi nhận hiện trạng, dự đoán, tương tác, trực quan hóa, tổng hợp) trong đó mô hình học máy đề xuất và chuyên gia sửa, xác nhận qua vòng phản hồi (tr. 1–2, 5–6). |
| Bằng chứng | Tổng quan phạm vi (25 bài từ Scopus và tài liệu xám), phỏng vấn 4 đại diện ngành, đồng thiết kế với 12 nhà nghiên cứu, ánh xạ 3 ứng dụng hiện có và 3 kịch bản, nghiên cứu người dùng chuyên gia với 8 công ty ở Thụy Sĩ (tr. 2–3, 9–10). Chưa có mẫu thử phần mềm; mẫu thử để cho bài sau (tr. 2, 9). |
| Giới hạn | Xem mục 5. |
| Tác động K1/K2/K3 | K3: mở rộng yếu (xác nhận của chuyên gia là bước trong quy trình và tín hiệu học, không là bản ghi trách nhiệm). K2: thu hẹp yếu (tác giả nêu định danh duy nhất và quản lý phiên bản cho cấu kiện là thiết yếu). K1: không liên quan trực tiếp. |
| Vị trí sử dụng | 1.2.4 và 1.4A (đã trích); 5.6A (khuôn người trong vòng, học chủ động có chuyên gia); 3.6 (nhãn từ chuyên gia). |
| Mức đã đọc | Toàn văn |

## Định tuyến (skill govern-phd-evidence)

```text
RQ: RQ3
WP: WP4 (hỗ trợ hành động có con người rà soát); thứ cấp WP3 (vòng lặp kiểm tra tạo nhãn)
Chương: tiểu luận 5.6A, 3.6; luận án: chương hỗ trợ quyết định
Paper: Evidence is currently insufficient. (chưa rõ bài báo đích của WP4 trong tiểu luận)
Evidence Gate: G5 theo bản đồ của skill (trạng thái: Evidence is currently insufficient.)
Scope: Supporting (khuôn người – AI; đối tượng là kiểm kê vật liệu cho tái sử dụng, không phải an toàn kết cấu)
Evidence type: Management decision support
```

Không thuộc: WP1 (không có phân loại dao động), WP2 (không có mô hình dữ liệu hình thức).

## 1. Câu hỏi nghiên cứu và đối tượng

- Vấn đề: kiểm định công trình hiện chủ yếu thủ công, tốn thời gian, dữ liệu phân mảnh và thiếu chuẩn hóa (tr. 1).
- Đối tượng: **kiểm định trước phá dỡ hoặc cải tạo** để kiểm kê vật liệu tái sử dụng, chất nguy hại; bối cảnh xây dựng tuần
  hoàn ở Thụy Sĩ và EU (tr. 1, 3–5). Không phải kiểm định an toàn kết cấu.
- Dữ liệu: tài liệu thiết kế, ảnh, video, đám mây điểm từ kính Aria, hồ sơ cải tạo (tr. 5, 8–9).

## 2. Phương pháp và kiến trúc thông tin

- Năm nguyên tắc thiết kế "5A": thích ứng, dễ tiếp cận, chi phí thấp, tăng tốc, đồng bộ (tr. 5).
- Chuỗi R²PIVS sáu mô-đun (tr. 5–6, Hình 3). Ở mô-đun trực quan hóa: chuyên gia so dự đoán với tài liệu thiết kế và hiện
  trạng; trường hợp bất định được gắn cờ để gán nhãn và đưa vào học chủ động (tr. 6).
- Ba kịch bản học máy: đo hình học (SceneScript, EFM3D), đánh giá trực quan (mô hình ngôn ngữ – thị giác), ước lượng chất
  nguy hại (RAG trên đồ thị tri thức) (tr. 7–9). Mỗi kịch bản có "điểm rà soát" xác minh cuối cùng trước khi dùng cho bước
  sau (tr. 7).
- Thông tin: cơ sở dữ liệu đa phương thức lưu dữ liệu thô, dự đoán ban đầu và đã sửa, bảo đảm truy vết (tr. 9); chuyên gia
  nêu cần quản lý phiên bản chặt và định danh duy nhất cho cấu kiện, tích hợp với Revit/Archicad (tr. 6). Gắn mã eBKP,
  chuẩn SwissInv (tr. 10).

## 3. Cách kiểm chứng

- Không có mẫu thử chạy được; kiểm chứng bằng **đánh giá ý kiến chuyên gia** về sơ đồ ứng dụng (8 công ty; trình bày 15 phút,
  thảo luận 15 phút, khảo sát trực tuyến có câu hỏi mở và thang Likert) (tr. 3, 9–10).
- Kết quả định tính: mọi chuyên gia đánh giá cao cấu trúc mô-đun; ba phần tư coi là giải pháp mở rộng được; một nửa đồng ý
  hỗ trợ hợp tác chi phí thấp; 5/7 cho rằng đáp ứng trao đổi dữ liệu chuẩn hóa (tr. 10). Mẫu số không thống nhất (8 công ty,
  có câu 7 người trả lời).
- Không có đường cơ sở, không có chỉ số hiệu năng, không đo thời gian hay chất lượng kiểm kê.

## 4. Luận điểm chính

1. Kiểm định công trình hiện thủ công, phi chuẩn hóa, dữ liệu không nhất quán (tr. 1, 3–4).
2. Hệ người – AI kết hợp (mixed-initiative), với gán nhãn tương tác và học chủ động, giải quyết được việc thiếu dữ liệu có
   nhãn và đưa tri thức chuyên gia vào xác nhận (tr. 4).
3. Tương tác người trong vòng hỗ trợ giám sát của con người và tạo tin cậy vào dự đoán, điều cần cho triển khai thực (tr. 2).
4. Quản lý phiên bản và định danh duy nhất cho cấu kiện là thiết yếu khi dữ liệu đa phương thức (tr. 6).

## 5. Giới hạn (bảng theo skill deep-read, mục D)

| ID | Trạng thái | Giới hạn / hướng | Vị trí | Khẳng định bị ảnh hưởng | Liên quan luận án |
|---|---|---|---|---|---|
| D1 | AUTHOR-STATED | LFW1: hiệu năng khi phản hồi ít; các cơ chế mức trung cần nhiều phản hồi có nhãn, khó cải thiện ngay lúc đầu (L-DATA) | tr. 10 | Vòng học từ chuyên gia | Cùng chiều UV-05 |
| D2 | AUTHOR-STATED | LFW2: biểu diễn và trực quan hóa dữ liệu đa phương thức ở nhiều mức không gian còn khó (L-METHOD) | tr. 10 | Chất lượng phản hồi | — |
| D3 | AUTHOR-STATED | LFW3: khung thiết kế cho công trình hiện hữu thường thiếu BIM; tích hợp BIM là hướng tiếp (L-TRACE) | tr. 10–11 | Truy vết cấp cấu kiện | Liên quan K2 |
| D4 | AUTHOR-STATED | Mẫu thử và thử nghiệm để cho bài sau; tác giả không được phép chia sẻ dữ liệu (L-VALID, L-REPORT) | tr. 2, 9, 11 | Mọi khẳng định hiệu quả | Khung chưa kiểm chứng vận hành |
| D5 | READER-INFERRED | Kiểm chứng bằng ý kiến 8 công ty, cùng một quốc gia, một nửa đã tham gia phỏng vấn trước (L-VALID) | tr. 3, 10 | "Hứa hẹn", "mở rộng được" | Bằng chứng yếu |
| D6 | READER-INFERRED | Xác nhận của chuyên gia được dùng làm phản hồi để tinh chỉnh mô hình; "điểm rà soát" không có bản ghi ai xác nhận, căn cứ nào, trạng thái gì (L-DECISION) | tr. 6–7, 9 | Giải trình | Căn cứ cho UV-07 |

## 6. Điều bài KHÔNG xử lý, xét theo chuỗi của luận án

| Ý | Mức | Căn cứ |
|---|---|---|
| Nguồn gốc bằng chứng cảm biến | xử lý một phần | Lưu dữ liệu thô, dự đoán ban đầu và đã sửa để truy vết (tr. 9); dữ liệu hành vi tương tác có thể cho thấy mẫu nguồn gốc (tr. 6); không có cấu trúc |
| Phạm vi hiệu lực của bằng chứng | không xử lý | Có gắn cờ trường hợp bất định (tr. 6), không có phạm vi |
| Quan hệ bằng chứng – cấu kiện có thời hạn | không xử lý | Chỉ nêu cần định danh duy nhất và phiên bản (tr. 6) |
| Trách nhiệm, thẩm quyền | xử lý một phần | Có điểm rà soát của người (tr. 7); không ghi vai trò, thẩm quyền |
| Trạng thái hành động và lịch sử chuyển trạng thái | không xử lý | — |
| Truy ngược từ hành động về dữ liệu gốc | xử lý một phần | Cơ sở dữ liệu giữ đầu vào, dự đoán và kết quả sửa (tr. 9); không có hành động |

## 7. Tác động tới K1/K2/K3 (bảng theo skill phd-gap-miner)

| Nguồn | Claim | Evidence | Loại | Gap | Gap-impact | Mức bảo vệ | Allowed-usage-location |
|---|---|---|---|---|---|---|---|
| [17] | Xác nhận của chuyên gia là tín hiệu học và bước quy trình, không phải bản ghi trách nhiệm | tr. 6–7, 9 (READER-INFERRED) | SCOPE | K3 (UV-07) | WIDENS (ứng viên) | không đổi; tài liệu 2026 | 5.6A; 5.2 sau ĐD3 |
| [17] | Định danh duy nhất và phiên bản cho cấu kiện là thiết yếu | tr. 6 (AUTHOR-STATED, ý kiến chuyên gia) | — | K2 | NO_CHANGE (nêu nhu cầu, không giải pháp) | — | 4.x |
| [17] | Thiếu nhãn; học chủ động với chuyên gia | tr. 4, 10 (AUTHOR-STATED) | DATA | UV-05 | WIDENS | — | 3.6; 5.6A.3 |

## 8. Vị trí sử dụng trong tiểu luận v2

- 1.2.4 và 1.4A (đã trích đúng ý: khung kiểm định có chuyên gia tương tác và rà soát).
- 5.6A: khuôn "AI đề xuất, chuyên gia sửa và xác nhận"; học chủ động có chuyên gia (ghi rõ đối tượng là kiểm kê tái sử dụng).
- Không dùng làm căn cứ hiệu quả (chưa có mẫu thử); không dùng làm căn cứ chính cho khoảng trống (2026).

## F. Ý tưởng ứng viên

| Ý tưởng | Giới hạn gốc | Fit | Evidence | Data | Method | Novelty | Boundary | Priority | Quyết định |
|---|---|---|---|---|---|---|---|---|---|
| Ghi mỗi lần chuyên gia xác nhận hay sửa đầu ra AI thành **bản ghi có vai trò, thời điểm, căn cứ**, tách khỏi việc dùng phản hồi đó làm nhãn | D6 | PASS | PARTIAL ([17], [7], Hughes 2022) | PASS | PARTIAL | UNKNOWN (chưa kiểm phản chứng) | PASS | PASS (G5) | ADD TO REVIEW (UV-07) |

## G. Claim → Evidence → Limitation → Next action

- **Claim:** Khung người – AI cho kiểm định đã đặt chuyên gia vào vòng xác nhận, nhưng xác nhận được dùng để học, chưa được
  ghi như bản ghi trách nhiệm.
- **Evidence:** [17] tr. 6–7, 9; cùng chiều [7] tr. 12, Hughes 2022 tr. 2, 27–28.
- **Limitation:** [17] chưa có mẫu thử, đối tượng là kiểm kê tái sử dụng; nhận định là READER-INFERRED.
- **Next action:** kiểm phản chứng UV-07 trong IFC4 (`IfcApproval`), BCF-API, [44] (phê duyệt theo vai trò) và tài liệu về
  học máy có người trong vòng. Gate gần hơn: G5 (logic hỗ trợ hành động có người rà soát).

## I. Bài học năm phút (TUTOR-EXPLANATION)

1. **Vấn đề:** kiểm kê vật liệu trước phá dỡ làm thủ công, chậm, dữ liệu không thống nhất.
2. **Vì sao quan trọng:** tái sử dụng cấu kiện cần dữ liệu đúng về kích thước, tình trạng, chất nguy hại.
3. **Tác giả làm gì:** từ tổng quan, phỏng vấn, đồng thiết kế, đề ra chuỗi sáu mô-đun trong đó AI đo, phân loại, ước lượng
   còn chuyên gia sửa và xác nhận; hỏi ý kiến 8 công ty về sơ đồ ứng dụng.
4. **Phát hiện:** chuyên gia ủng hộ cấu trúc mô-đun và nhu cầu dữ liệu chuẩn hóa.
5. **Không chứng minh:** khung chạy được và hiệu quả (chưa có mẫu thử); không bàn trách nhiệm pháp lý của người xác nhận.
- **Áp vào luận án (THESIS-APPLICATION):** khuôn người trong vòng giống nguyên tắc "AI tạo bằng chứng, con người quyết định"
  của 5.6A; phần luận án cần thêm là ghi lại lần xác nhận như một sự kiện có thẩm quyền và căn cứ, không chỉ như dữ liệu học.
