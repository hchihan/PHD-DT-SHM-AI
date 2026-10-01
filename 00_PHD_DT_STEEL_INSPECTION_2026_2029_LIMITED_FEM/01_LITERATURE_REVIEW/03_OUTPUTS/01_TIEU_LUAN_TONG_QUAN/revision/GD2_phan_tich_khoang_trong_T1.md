# Phân tích khoảng trống làm việc sau khi đọc Tier 1 (GĐ2)

Lập ngày 01/10/2026, sau phiên T1-4. **Đây là phân tích làm việc, không chốt khoảng trống** (CLAUDE.md mục 2.9, 11;
chốt ở Điểm duyệt 3). K1–K3 là giả thuyết làm việc.

Nguồn đã đọc toàn văn: 11/12 tài liệu Tier 1 — [8], [7], [3], [2], [44], [22], [18], [19], [53], [16], [17]; chưa đọc [35]
Bellon (PDF mới có). Chuẩn đã đối chiếu: BCF 3.0, IFC4 ADD2 TC1 (một số thực thể), COBie 2.4 (NBIMS-US V3 chương 4.2),
SSN/SOSA (Khuyến nghị W3C 2017). Tier 2 đọc một phần trước đây: Figueiredo 2011, Hughes 2022, [45], [56] (ghi chú trong
`notes/`). Chi tiết từng căn cứ ở `revision/GD2_nhat_ky_khoang_trong.md`.

## 1. Cách dùng các skill PhD trong phân tích này

| Skill | Phần đã dùng | Phần không dùng, lý do |
|---|---|---|
| deep-read-phd-papers | QA nguồn; định tuyến; bảng giới hạn có nhãn AUTHOR-STATED / READER-INFERRED và mã L-…; sàng lọc ý tưởng tám tiêu chí; Claim → Evidence → Limitation → Next action; bài học năm phút; tổng hợp liên tài liệu (mục H dưới đây) | Không chạy MinerU (văn bản trích bằng PyMuPDF, đã ghi trong từng ghi chú); không dùng chuỗi định danh tuyến tính của skill thay cho schema đồ thị đã khóa |
| phd-gap-miner | Bảng Claim → Evidence → Limitation → Gap-impact → Allowed-usage-location; thang mức bảo vệ (STRONG / NARROW_BUT_DEFENSIBLE / WEAK / NOT_DEFENSIBLE); quy tắc một nguồn chỉ là một điểm dữ liệu; rà cơ hội mở rộng (mục 4) | Không ghi vào tệp kiểm toán "KHÔNG NỘP" bên ngoài dự án; không dùng câu chữ "khoảng trống đã khóa" của skill làm chuẩn chấm (theo chỉ đạo của NCS ở phiên T1-1) |
| govern-phd-evidence | Khối định tuyến bắt buộc; phân lớp bằng chứng; tường lửa phạm vi; ghi "Evidence is currently insufficient." khi thiếu nguồn hiện hành | Không đọc được các tệp quản trị của luận án (Charter, ADR, CURRENT_STATUS) trong phiên này; trạng thái Gate để là chưa đủ bằng chứng |

## 2. Tổng hợp liên tài liệu (mục H của skill deep-read)

| Ứng viên | Tài liệu ủng hộ (trước 2025 in đậm) | Tài liệu thu hẹp / phản chứng | Đích trong luận án | Sức mạnh bằng chứng | Cần kiểm thêm | Quyết định |
|---|---|---|---|---|---|---|
| UV-01 Hành động và lần đổi trạng thái không nối ngược về bằng chứng cùng phạm vi | **[3]**, **[7]**, **[22]** (nhu cầu), [44] | BCF 3.0, IFC4, COBie 2.4, [44] (đã kiểm) | K3; 5.5; 4.5.4 | Trung bình: phần biểu diễn trạng thái, phê duyệt, lịch sử đã có chuẩn; phần còn lại hẹp | CMMS; ISO 19650-3 (không truy cập được); [35] | ADD TO REVIEW |
| UV-02 Từng kết quả từ dữ liệu đo chưa mang nguồn gốc, phiên bản phương pháp, phạm vi | **[3]**, **[7]**, **[53]**, **[16]** | [16] (nguồn gốc mức đối tượng), [44] (mức tệp), [53] (phiếu mức mô hình), SSN (một phần) | K1; 3.5; 5.5 | Trung bình: bốn căn cứ trước 2025, phần còn lại rõ (mức "từng kết quả") | PROV-O; MLflow/DVC; thẻ mô hình (chưa có trong Zotero) | ADD TO REVIEW |
| UV-03 Ánh xạ cảm biến – cấu kiện thiếu khoảng hiệu lực được quy định và ràng buộc thời gian | **[3]**, **[7]**, **[2]** | [2], [3], SSN Deployment, IFC4 (đã kiểm) | K2; ràng buộc C3; 4.x; 5.5 | Đủ điều kiện hình thức; phần còn lại nhỏ (hồ sơ áp dụng + ràng buộc) | [35] | Đề xuất **hạ thành yêu cầu của mô hình dữ liệu** thay vì khoảng trống độc lập (chờ NCS) |
| UV-04 Thiếu phân loại DM/DS/DT cho kiểm tra – bảo trì có người quyết định | **[8]**, **[7]** | — | Định vị 2.3 | Thấp; là câu hỏi khái niệm | [10], Sepasgozar 2021 | DEFER (chỉ định vị) |
| UV-05 Thiếu nhãn hiện trường; nhãn đến từ kiểm tra | **[3]**, [19], [17]; 5.6A: Bull 2022, Wang & Cha 2021, [57] | Hughes 2022, Bull 2022 (đề xuất cách lấy nhãn từ kiểm tra) | 3.6; 5.6A; WP3 | Cao về hiện tượng; thấp về "khoảng trống" vì đã có hướng giải | Đọc đủ [57]; Hughes bản in | Giữ làm **luận điểm bối cảnh** cho 3.6, không làm khoảng trống |
| UV-06 Lần lắp ráp hoặc can thiệp bảo trì là ranh giới phạm vi hiệu lực | **[18]**, **[53]** (phương pháp chung), **[56]** (đọc một phần), [19] | [19] (đánh giá để riêng đợt đo đã làm cho mối nối bu lông bằng phát xạ âm) | K1; 1.3A; 3.4; 3.6 | Trung bình; phản chứng chưa kiểm | [57], Gardner 2021 phần III, Cross 2011, các nghiên cứu theo dõi dài hạn sau bảo trì | ADD TO REVIEW |
| UV-07 Xác nhận của chuyên gia đối với đầu ra AI là tín hiệu học, chưa là bản ghi trách nhiệm | **[3]**, **[7]**, **Hughes 2022**, [17] | IfcApproval, [44] (biểu diễn phê duyệt đã có) | K3; 5.6A; WP4 | Trung bình; có nguy cơ thu hẹp mạnh khi kiểm tài liệu học máy có người trong vòng | Tài liệu human-in-the-loop; thẻ mô hình | ADD TO REVIEW |

Lưu ý của skill: "các tài liệu đã đọc không báo cáo X" khác với "chưa ai làm X". Mọi dòng trên là phát biểu trong phạm vi
tập tài liệu đã đọc.

## 3. Mức bảo vệ làm việc của K1–K3 (thang của skill phd-gap-miner)

Đây là **lần đánh giá đầu tiên** trong dự án, không có mức trước để so; quy tắc "không hạ quá một mức từ một nguồn" áp
cho các lần sau.

| Giả thuyết | Nguồn thu hẹp (độc lập) | Phần còn lại sau khi trừ tiền lệ | Mức làm việc | Ghi chú |
|---|---|---|---|---|
| **K1** Xác lập chất lượng và phạm vi hiệu lực của bằng chứng trạng thái | [19] (đánh giá để riêng đợt đo cho mối nối bu lông, phát xạ âm), [56] (thích nghi miền giữa các dầm bu lông), [53] (phiếu báo cáo mức mô hình) — 3 nguồn | (a) dữ liệu **dao động** trên **khung thép** có kiểm soát rò rỉ tường minh theo lần lắp ráp; (b) phạm vi hiệu lực được ghi ở mức **từng** bằng chứng và đi theo nó | NARROW_BUT_DEFENSIBLE | [19] thu hẹp mạnh vế "đánh giá trên đơn vị độc lập": cần đọc [48] Pal 2022 và các bài dao động bu lông Tier 2 để biết vế (a) còn đứng không |
| **K2** Bảo toàn chất lượng bằng chứng trong truy vết cấp cấu kiện | [2], [3], SSN, IFC4, [16], [44] — 6 nguồn | Khoảng hiệu lực bắt buộc của ánh xạ và **thuộc tính chất lượng của bằng chứng tình trạng** (nguồn gốc, phạm vi) được giữ khi đi qua các liên kết | NARROW_BUT_DEFENSIBLE, có nguy cơ thành WEAK ở vế "ánh xạ" | Vế "ánh xạ có thời hạn" (UV-03) còn rất mỏng; vế "giữ chất lượng bằng chứng" là phần chính còn lại |
| **K3** Từ bằng chứng đến hành động | BCF 3.0, IFC4, COBie 2.4, [44] — 4 nguồn | Quan hệ định kiểu từ hành động và từng bước chuyển trạng thái về bản ghi sử dụng bằng chứng cùng phạm vi hiệu lực; ghi lần xác nhận đầu ra AI như bản ghi trách nhiệm (UV-07) | NARROW_BUT_DEFENSIBLE | Trạng thái, phê duyệt, lịch sử, thẩm quyền theo vai trò đều đã có ở các chuẩn; phần còn lại là **liên kết**, không phải **thành phần** |

Kết luận làm việc: cả ba giả thuyết **đứng được ở mức hẹp**; phần còn lại của cả ba hội tụ về cùng một điểm: **bằng chứng
tình trạng là một bản ghi mang nguồn gốc và phạm vi hiệu lực, và các liên kết tới cấu kiện, kiểm tra, hành động phải giữ
các thuộc tính đó**. [NCS] Điều này khớp với luận điểm trung tâm ở CLAUDE.md mục 1 và gợi ý rằng ở GĐ3 có thể phát biểu
ba khoảng trống quanh một trục chung thay vì ba trục rời.

## 4. Rà cơ hội mở rộng (opportunity radar của skill phd-gap-miner; không đổi phạm vi luận án)

| Nguồn | Loại cơ hội | Mô tả | Vì sao ngoài phạm vi hiện tại | Số nguồn | Điều kiện khả thi |
|---|---|---|---|---|---|
| [53] + schema | METHODOLOGICAL_COMBINATION | "Phiếu thông tin" cho từng bản ghi bằng chứng: lập luận về đơn vị, chia tập, phân bố áp dụng thành trường bắt buộc, có phiên bản | **Có thể nằm trong phạm vi** (5.5, 5.7); NCS quyết định | 2 ([53], [19]) | Kiểm thẻ mô hình, MLflow/DVC trước |
| [19] | TOOLING_OR_DATASET_REUSE | Bộ dữ liệu ORION-AE công khai (5 đợt đo sau tháo – lắp) để thử cách ghi phạm vi hiệu lực theo đợt lắp | Dữ liệu phát xạ âm, dầm nhôm; WP1 dùng dao động khung thép | 1 | Chỉ dùng như ví dụ đối chiếu |
| [16] + [44] | METHODOLOGICAL_COMBINATION | Mã băm của tệp dữ liệu và mô hình làm định danh căn cứ của bằng chứng | Chuỗi khối ngoài phạm vi; mã băm thì không | 2 | Đã nêu ở `mapping/garcia2026.md` Phần D |
| [17] | CROSS_DOMAIN_TRANSFER | Ghi nhật ký tương tác của chuyên gia như nguồn gốc (tr. 6) | Thiết kế giao diện, HCI ngoài phạm vi | 1 | Một nguồn, theo dõi |
| [3], [7], Hughes 2022, [17] | TAXONOMY_PRESSURE | "Xác nhận của con người đối với đầu ra AI" lặp lại ở bốn nguồn nhưng không khớp gọn K1–K3 (nằm giữa K3 và nguyên tắc AI của 5.6A) | Cần NCS quyết định có thành khoảng trống riêng, gộp vào K3, hay chỉ là yêu cầu thiết kế | 4 | Kiểm phản chứng UV-07 trước |

## 5. Xung đột phát hiện khi áp các skill (ghi nhận, không tự hợp nhất)

| Mã | Xung đột | Nguồn theo | Xử lý |
|---|---|---|---|
| X-01 | Skill govern-phd-evidence và deep-read dùng chuỗi định danh tuyến tính và ghi "không thêm Status_Event_ID như thành phần bắt buộc"; CLAUDE.md (NCS duyệt) dùng schema đồ thị có thực thể `STATUS_EVENT` | CLAUDE.md mục 2.7, 8 (quyết định dự án tiểu luận) | Theo CLAUDE.md; báo NCS để đồng bộ lại skill |
| X-02 | Bản đồ của skill định tuyến theo chương luận án C4–C7 và Gate G1–G7; tiểu luận dùng số mục riêng | CLAUDE.md mục 6.3 | Ghi cả hai trong khối định tuyến của ghi chú |
| X-03 | Câu chữ "Gap 2" của skill (chuỗi định danh từ bằng chứng tới cấu kiện và hồ sơ) khác K2 trong bản tiểu luận ("bảo toàn chất lượng bằng chứng trong truy vết cấp cấu kiện") | Bản tiểu luận mục 5.2 | Dùng câu chữ của tiểu luận; khoảng trống chốt ở ĐD3 |
| X-04 | Skill yêu cầu đọc trạng thái Gate từ `CURRENT_STATUS_AND_NEXT_DIRECTION.md`; tệp không được đọc trong phiên | — | Ghi "Evidence is currently insufficient." ở mọi ô trạng thái Gate |

## 6. Việc tiếp theo đề xuất

1. Hoàn tất T1-1: đọc [35] Bellon (PDF đã có) và lập `mapping/bellon2025.md`; kiểm [35] như phản chứng cho UV-01, UV-03.
2. Phiên Tier 2 ưu tiên theo khoảng trống: [48] Pal 2022, [56] Da Silva (đọc đủ), [57] Bull 2021 để kiểm vế (a) của K1 và
   UV-06; sau đó [45], Figueiredo (đọc đủ phần kết quả).
3. Kiểm phản chứng còn treo: CMMS (UV-01), PROV-O và MLflow/DVC (UV-02), tài liệu học máy có người trong vòng (UV-07).
   Thẻ mô hình (Mitchell 2019) cần NCS quyết định có nhập Zotero không.
4. NCS quyết định: (a) UV-03 hạ thành yêu cầu mô hình dữ liệu; (b) UV-05 chỉ là luận điểm bối cảnh; (c) UV-07 tách riêng
   hay gộp K3; (d) có tính [22] là căn cứ của UV-01 không.
