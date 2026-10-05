# EMTIHHX4 — Çelik, Petri & Barati (2023) — [16]

Celik Y, Petri I, Barati M. Blockchain supported BIM data provenance for construction projects. *Computers in Industry*.
DOI 10.1016/j.compind.2022.103768 (nhận 17/05/2022, chấp nhận 15/08/2022; số tập và năm in theo
`matrix/doi_chieu_danh_muc.csv`).

**Bản đã đọc (QA nguồn):** toàn văn bản PDF trong kho Zotero, là **bản in thử** (trang đầu ghi "Computers in Industry xxx
(xxxx) xxx", có trang điểm nhấn và tóm tắt đồ họa); 18 tr. PDF, không có số trang tạp chí. **Số trang dưới đây là trang
PDF.** Trích văn bản bằng PyMuPDF; Hình 1–12 và phụ lục A (ảnh giao diện) chỉ đọc qua chú thích. Đọc ngày 01/10/2026,
phiên T1-4. Cần đối chiếu bản in trước khi dẫn trang.

Ký hiệu: (a) tác giả nói; (b) AUTHOR-STATED; **[NCS]** READER-INFERRED.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | EMTIHHX4 / [16] |
| Tier / Cụm | Tier 1 / Truy vết thông tin |
| Luận điểm | Trong dự án nhiều bộ môn, chuỗi khối (blockchain) có thể ghi nguồn gốc dữ liệu BIM ở mức đối tượng IFC (bộ môn, người, thao tác, thời điểm, phiên bản) một cách không sửa được, giúp tái dựng lịch sử thay đổi và tăng tin cậy giữa các bên (tr. 3, 8, 11–14). |
| Bằng chứng | Mẫu thử hợp đồng thông minh trên mạng thử Ethereum (Kovan) với mô hình IFC của một cầu đường cao tốc ở Anh (dự án Clouds-for-Coordination); kịch bản bốn bộ môn; đo chi phí gas và thời gian đào khối theo số thao tác, số lần cập nhật, số người (tr. 7–13, Bảng 1–4). |
| Giới hạn | Xem mục 5. |
| Tác động K1/K2/K3 | K2: thu hẹp một phần (nguồn gốc ở mức đối tượng BIM có định danh, phiên bản, người, thời điểm đã có tiền lệ). K1: mở rộng yếu (nguồn gốc chưa áp cho bằng chứng sinh từ dữ liệu đo). K3: không liên quan trực tiếp. |
| Vị trí sử dụng | 1.2.4 (đã trích); 1.4A (đã trích); 3.5 (nguồn gốc); 4.x và 5.5 (tiền lệ ghi nguồn gốc ở mức đối tượng). |
| Mức đã đọc | Toàn văn (bản in thử) |

## Định tuyến (skill govern-phd-evidence)

```text
RQ: RQ2
WP: WP2
Chương: tiểu luận 3.5 (nguồn gốc), 4.x; luận án: chương truy vết thông tin
Paper: Paper 2
Evidence Gate: G2 (trạng thái: Evidence is currently insufficient.)
Scope: Supporting (tiền lệ nguồn gốc dữ liệu BIM; chuỗi khối nằm ngoài phạm vi luận án)
Evidence type: Information traceability
```

Không thuộc: WP1 (không có học máy), WP3–WP4 (không có vận hành, hành động bảo trì).

## 1. Câu hỏi nghiên cứu và đối tượng

- Hai mục tiêu (tr. 4): đề xuất khung nguồn gốc dữ liệu BIM dùng chuỗi khối cho dự án nhiều bộ môn; minh họa tích hợp
  BIM – chuỗi khối trên một ca thực.
- Đối tượng: dữ liệu thiết kế của một **cầu đường cao tốc ở Anh** (giai đoạn thiết kế), các bộ môn kiến trúc, kết cấu, cơ
  điện, chủ đầu tư (tr. 7–10). Không có dữ liệu vận hành hay cảm biến.

## 2. Phương pháp và kiến trúc thông tin

- Bảy bước phương pháp: thu yêu cầu, tổng quan, tổng hợp, dựng môi trường thử, viết hợp đồng thông minh, giao diện web,
  trình bày kết quả (tr. 6, Hình 1).
- Bản ghi nguồn gốc sau mỗi cập nhật của một bộ môn (tr. 8): bộ (thao tác, thời điểm, mô hình, phiên bản, định danh đối
  tượng, chủ sở hữu). Mỗi bộ môn có định danh trên chuỗi khối; mã định danh người dùng được băm (tr. 6, 10).
- Hai hợp đồng: **provenance** (ghi bộ môn, đối tượng, thao tác, thời điểm, người, phiên bản) và **verification** (kiểm
  đối tượng do ai tạo hay sửa, thao tác và thời điểm, các phiên bản) (tr. 12).
- Xác thực: mã băm của tệp được đưa lên chuỗi khối; chủ đầu tư truy vấn để biết yêu cầu của hợp đồng đã được đáp ứng chưa
  (tr. 11).
- Chuẩn: IFC (tệp .ifc/.ifcXML, ISO 10303-21) (tr. 7). Không dùng PROV-O, SOSA, ISO 19650; nhắc môi trường dữ liệu chung
  như bối cảnh (tr. 4–5).

## 3. Cách kiểm chứng

- Dữ liệu thật về mô hình IFC của dự án; các thao tác là **kịch bản** do nhóm tác giả dựng (tr. 10, Bảng 1).
- Chỉ số: gas tiêu thụ, chi phí ETH, thời gian đào khối, theo số thao tác (5–30), số lần cập nhật (5–30), số người (5–30);
  lặp 5 lần mỗi cấu hình (tr. 12–13).
- Không có đường cơ sở so sánh (không so với môi trường dữ liệu chung không dùng chuỗi khối); không đo tính đúng hay đầy
  đủ của bản ghi nguồn gốc; không có người dùng thực đánh giá.

## 4. Luận điểm chính

1. Trong dự án nhiều bộ môn cần cơ chế xác định ưu tiên, nguồn gốc và mức phù hợp của thông tin, gồm định danh giao dịch
   đã đưa thông tin vào (tr. 3).
2. Bản ghi nguồn gốc ở mức đối tượng IFC cho biết ai cập nhật, khi nào, phiên bản nào, đối tượng được dùng ở đâu trong quá
   trình (tr. 11–12).
3. Chi phí ghi và kiểm nguồn gốc tăng gần tuyến tính theo số thao tác, số người, số lần cập nhật (tr. 12–13).
4. Ghi toàn bộ lịch sử dự án vào chuỗi khối ngăn mất dữ liệu và cho phép tái dựng các hoạt động theo nhiệm vụ (tr. 14).

## 5. Giới hạn (bảng theo skill deep-read, mục D)

| ID | Trạng thái | Giới hạn / hướng | Vị trí | Khẳng định bị ảnh hưởng | Liên quan luận án |
|---|---|---|---|---|---|
| D1 | AUTHOR-STATED | Cần phân tích và tối ưu khả năng mở rộng, hiệu năng của chuỗi khối theo kịch bản cụ thể; cần tích hợp với thiết bị IoT và đám mây (L-SCALE) | tr. 14 | Khả thi triển khai | IoT là phần bài chưa làm, đúng chỗ luận án cần |
| D2 | READER-INFERRED | Một dự án, giai đoạn thiết kế, thao tác do kịch bản dựng; chỉ đo chi phí, không đo chất lượng nguồn gốc (L-VALID) | tr. 10–13 | "Tăng tin cậy", "tránh mất dữ liệu" | Khẳng định lợi ích chưa được kiểm chứng |
| D3 | READER-INFERRED | Nguồn gốc ghi "ai, khi nào, thao tác gì" nhưng không ghi **vì sao** hay căn cứ; không có trạng thái phê duyệt (L-DECISION) | tr. 8, 11–12 | Giải trình | Liên quan K3 |
| D4 | READER-INFERRED | Không có khái niệm phạm vi hiệu lực hay chất lượng của dữ liệu được ghi; nguồn gốc là của tệp/đối tượng thiết kế (L-TRACE) | tr. 8, 12 | Áp cho bằng chứng tình trạng | Liên quan K1, K2 |
| D5 | READER-INFERRED | Một số lập luận dựa trên nguồn không phản biện (ví dụ con số 95 % dữ liệu bị mất khi bàn giao trích từ một tổ chức tư vấn) (L-REPORT) | tr. 5 | Bối cảnh | Không dẫn lại con số này |

## 6. Điều bài KHÔNG xử lý, xét theo chuỗi của luận án

| Ý | Mức | Căn cứ |
|---|---|---|
| Nguồn gốc bằng chứng cảm biến | không xử lý | Nguồn gốc của dữ liệu thiết kế BIM; IoT là hướng tiếp (tr. 14) |
| Phạm vi hiệu lực của bằng chứng | không xử lý | — |
| Quan hệ bằng chứng – cấu kiện có thời hạn | xử lý một phần | Lịch sử phiên bản của đối tượng IFC theo thời gian (tr. 11–12); không có bằng chứng |
| Trách nhiệm, thẩm quyền | xử lý một phần | Ghi bộ môn và người thực hiện, có thể cập nhật vai trò người dùng (tr. 11); không có thẩm quyền phê duyệt |
| Trạng thái hành động và lịch sử chuyển trạng thái | không xử lý | Lịch sử thao tác trên đối tượng, không có trạng thái |
| Truy ngược từ hành động về dữ liệu gốc | xử lý một phần | Truy được ai sửa đối tượng nào khi nào (tr. 11–12); không có hành động bảo trì |

## 7. Tác động tới K1/K2/K3 (bảng theo skill phd-gap-miner)

| Nguồn | Claim | Evidence | Loại | Gap | Gap-impact | Mức bảo vệ | Allowed-usage-location |
|---|---|---|---|---|---|---|---|
| [16] | Nguồn gốc ở mức đối tượng IFC (người, thời điểm, phiên bản) ghi được không sửa được | tr. 8, 11–12 (AUTHOR-STATED) | — | K2 | NARROWS một phần | không đổi từ một nguồn | 3.5; 5.5 (tiền lệ) |
| [16] | Nguồn gốc mới áp cho dữ liệu thiết kế; tích hợp IoT là việc sau | tr. 14 (AUTHOR-STATED) | FUTURE-WORK | K1 (UV-02) | WIDENS yếu | như trên | 3.5 |
| [16] | Bản ghi không có căn cứ hay phê duyệt | tr. 8 (READER-INFERRED) | SCOPE | K3 | NO_CHANGE (bài không nhằm việc này) | — | chỉ ghi vào nhật ký |

## 8. Vị trí sử dụng trong tiểu luận v2

- 1.2.4 và 1.4A (đã trích đúng ý: ghi nguồn gốc, tác nhân, thời điểm, phiên bản).
- 3.5 và 5.5: tiền lệ của nguồn gốc ở mức đối tượng; luận án kế thừa ý ghi người, thời điểm, phiên bản và mở rộng cho
  bằng chứng sinh từ dữ liệu đo.
- Không đưa chuỗi khối vào phạm vi luận án; không dẫn các con số chi phí gas.

## F. Ý tưởng ứng viên

| Ý tưởng | Giới hạn gốc | Fit | Evidence | Data | Method | Novelty | Boundary | Priority | Quyết định |
|---|---|---|---|---|---|---|---|---|---|
| Lưu **mã băm** của tệp dữ liệu đo và của mô hình trong bản ghi bằng chứng để định danh chính xác căn cứ đã dùng (không cần chuỗi khối) | D4 | PASS | PARTIAL ([16], [44]) | PASS | PASS | FAIL nếu coi là mới (đã có ở [44], [16]) — chỉ là kế thừa | PASS | PARTIAL | ADOPT NOW như **kế thừa** khi viết 5.5 (chờ NCS duyệt đề xuất ở `mapping/garcia2026.md` Phần D) |

## G. Claim → Evidence → Limitation → Next action

- **Claim:** Ghi nguồn gốc ở mức đối tượng BIM (người, thời điểm, phiên bản) đã có tiền lệ; luận án kế thừa và áp cho bằng
  chứng tình trạng.
- **Evidence:** [16] tr. 8, 11–12; cùng chiều [44] (mã băm, phiên bản tệp).
- **Limitation:** bản in thử, chỉ đo chi phí, một dự án giai đoạn thiết kế.
- **Next action:** đối chiếu bản in để có số trang; giữ [16] ở mức "tiền lệ" trong 3.5 và 5.5. Gate gần hơn: G2 (tiền lệ
  cho mô hình dữ liệu).

## I. Bài học năm phút (TUTOR-EXPLANATION)

1. **Vấn đề:** nhiều bộ môn cùng sửa một mô hình BIM; khi có tranh chấp, khó biết ai sửa gì, lúc nào.
2. **Vì sao quan trọng:** tin cậy và trách nhiệm giữa các bên phụ thuộc vào lịch sử thay đổi không bị chỉnh sửa.
3. **Tác giả làm gì:** viết hai hợp đồng thông minh ghi và kiểm lịch sử thao tác trên đối tượng IFC, chạy trên mạng thử
   Ethereum với mô hình cầu thật và kịch bản bốn bộ môn.
4. **Phát hiện:** ghi được và truy vấn được lịch sử; chi phí tăng theo số thao tác, người, lần cập nhật.
5. **Không chứng minh:** lợi ích về tin cậy hay giảm mất dữ liệu (không đo); vận hành; dữ liệu cảm biến.
- **Áp vào luận án (THESIS-APPLICATION):** ý "mỗi lần thay đổi đối tượng là một bản ghi có người, thời điểm, phiên bản" là
  khuôn cho sự kiện chuyển trạng thái và bản ghi bằng chứng; công nghệ chuỗi khối thì không cần.
