# GĐ3: Hai khoảng trống và ba mục tiêu (bản nháp chờ NCS duyệt, gửi thầy)

Lập ngày 01/10/2026 theo `revision/prompt_GD3_khoang_trong_muc_tieu.md` và CLAUDE.md (commit `5bd3eb2`) mục 2 (QĐ 9–11), 2A, 8.
Nguồn: `revision/GD2_nhat_ky_khoang_trong.md` (UV-01 – UV-08), `notes/`. Không đọc thêm tài liệu trong phiên này.
Ký hiệu loại căn cứ: TG = tác giả tự nêu; [NCS] = nhận định của NCS từ việc tài liệu không xử lý một ý.
Trang của Mitchell 2019 theo bản arXiv, của Maes 2022 theo bản postprint (đối chiếu bản in ở GĐ6, N-04).

## Bảng kiểm (Bước 2)

### Kiểm theo ứng viên

| Ứng viên | Vào | Căn cứ độc lập trước 2025 (theo nhóm tác giả, kèm trang) | Tỉ trọng nguồn 2025–2026 | Còn "chưa kiểm"? | Phát biểu đã thu hẹp (1 câu) |
|---|---|---|---|---|---|
| UV-02 | G-A | 4: [3] tr. 5, 13–14 ([NCS]); [7] tr. 9, 11 (TG); [53] tr. 3, 5 (TG); [16] tr. PDF 14 (TG) | 0/4 | Không (thẻ mô hình, PROV-O, MLflow/DVC, SSN đã kiểm 01/10) | Nguồn gốc và phiên bản phương pháp cho từng kết quả đã biểu diễn được; phạm vi hiệu lực và độ bất định chưa là thành phần bắt buộc, kiểm được bằng máy, gắn vào từng bằng chứng và được kiểm tại lần sử dụng. |
| UV-06 | G-A | 4: [18] tr. 283, 292 (TG); Maes 2022 `2ZJSENQU` tr. 6, 20 (TG, hiện trường, cùng chiều); [53] tr. 4–5 (TG, phương pháp chung); [56] tr. 011102-1, -4 (TG, gián tiếp) | 1/5 ([19]; cùng nhóm Teloli với [56], không tính thêm) | Không (Maes 2022 đã kiểm 01/10) | Lần lắp ráp và lần can thiệp chưa được ghi như thành phần bắt buộc của phạm vi hiệu lực, gắn sự kiện có thời điểm, để kiểm bằng máy bằng chứng nào còn dùng được sau can thiệp. |
| UV-01 | G-B | 3: [3] tr. 6, 13–14 (TG một phần + [NCS]); [7] tr. 10, 12 (TG + [NCS]); [22] tr. 192 (TG, căn cứ nhu cầu, gián tiếp) | 1/4 ([44]) | Không theo nghĩa quy tắc 7.4, nhưng hai mục ở mức nguồn thứ cấp: CMMS qua [29] tr. 7, 11 và mô tả của [35] tr. 3 (N-20 (a)); ISO 19650-3 không truy cập được, đối chiếu qua [44] | Bằng chứng có nguồn gốc và phạm vi hiệu lực chưa đi vào chuỗi kiểm tra – cấu kiện – hành động; từng lần đổi trạng thái của hành động chưa là sự kiện có căn cứ và thẩm quyền. |
| UV-05 | G-B | 3: [3] tr. 2–3, 13 (TG); nhóm Sheffield – Los Alamos: Bull 2022 `87NKU5IS` tr. 1–4, Hughes 2022 `Z9RD5DMZ` tr. 1–2, 7, Worden 2007 `MCNRW6F5` tr. 1647–1651 (TG, tính một); Wang & Cha 2021 `TDRPDWJE` tr. 2, 20 (TG) | 2/5 ([19], [17]) | Không | Nhãn sinh từ kiểm tra thực ở công trình vận hành, mang độ bất định của kiểm tra, chưa được ghi như bản ghi gắn phép đo đã kích hoạt kiểm tra và cấu kiện. |
| UV-07 | G-B | 4: [3] tr. 4, 13 ([NCS]); [7] tr. 12 (TG); Hughes 2022 tr. 2, 7, 27–28 (TG); Mosqueira-Rey 2023 `73MBWFVJ` tr. 3006, 3012, 3039–3040 (TG mô tả, cùng chiều) | 1/5 ([17]) | Không | Khuôn trách nhiệm – phê duyệt chưa được áp cho từng đầu ra AI, để một lần xác nhận của kỹ sư được ghi đồng thời là bản ghi trách nhiệm và nhãn hiện trường có độ bất định. |
| UV-03 | Yêu cầu của schema (C3) | 3 ([3], [7], [2]) | — | Không | Khoảng hiệu lực bắt buộc trên quan hệ cảm biến – cấu kiện và ràng buộc thời điểm đo nằm trong khoảng đó; tiền lệ SSN `Deployment`, [2], [42], [21]. |
| UV-08 | Luận điểm 3.2; nội dung `applicable_conditions`, `obs_context` | 3 nhóm cho hiện tượng EOV chung ([45]; Worden 2007 + Figueiredo 2011; Cawley 2018); riêng nhà xưởng: Ju 2020 (hiện tượng) + [NCS] | — | Hu 2023 kiểm ở mức tóm tắt (truy cập đóng) | Trạng thái cầu trục và nhiệt độ phải là trường của bối cảnh quan trắc; hiệu quả phát hiện khi có cầu trục thuộc kiểm chứng MT3, không là khoảng trống riêng. |
| UV-04 | Định vị ở 2.3 | 2 ([8], [7]) | — | Không | Luận án khai báo mức bóng số (DS) theo [8]; thang trưởng thành [10], Papic 2019 đo năng lực tổ chức, không đo một hệ. |

### Kiểm ở cấp khoảng trống

| Tiêu chí | G-A | G-B |
|---|---|---|
| (i) ≥ 3 căn cứ độc lập ngoài nhóm 2025–2026 | Đạt: 7 nhóm ([3], [7], [53], [16], [18], Maes 2022, [56] gián tiếp). Loại trừ căn cứ dùng chung với G-B ([3], [7]) vẫn còn 5. | Đạt: 6 nhóm ([3], [7], [22], Sheffield – Los Alamos, Wang & Cha, Mosqueira-Rey). Loại trừ [3], [7] vẫn còn 4. |
| (ii) Không còn "chưa kiểm" | Đạt. Một mục nội dung (UV-08, Hu 2023) chỉ ở mức tóm tắt. | **Đạt có điều kiện:** CMMS đối chiếu qua nguồn thứ cấp ([29]; mô tả của [35] về Chen 2018, Condotta 2023); ISO 19650-3 không truy cập được, đối chiếu qua [44] (nguồn 2026). Hai mục này ghi đúng như vậy, không tính là đã đọc bản gốc. |
| (iii) Mọi trang dẫn có trong `notes/` | Đạt (đã dò từng trang trong `notes/`). Trang Mitchell (arXiv) và Maes (postprint) cần đối chiếu bản in ở GĐ6. | Đạt (đã dò). |

Chỗ không đạt hoặc cần NCS lưu ý:
1. Căn cứ [22] của UV-01 vẫn mang dấu "CẦN NCS KIỂM" (chỉ là căn cứ về nhu cầu). Ở cấp G-B không cần [22] để đủ ngưỡng.
2. N-12 (a)–(c) còn mở; không ảnh hưởng ngưỡng vì [28], [14]–[15], [42] không được đếm.
3. Phần lớn căn cứ của vế "chưa được ghi" là loại [NCS] (suy từ phần tài liệu không mô tả). Căn cứ TG trực tiếp cho G-A là [7] tr. 9, 11, [53] tr. 3, 5, [16] tr. PDF 14; cho G-B là [7] tr. 12, Hughes tr. 27–28. Cách viết ở Phần D giữ tách bạch hai loại này.
4. Ba tiền lệ bắt buộc nêu chưa có bản ghi Zotero để trích: IFC4 ADD2 TC1 (gồm `IfcApproval`), Khuyến nghị W3C SSN (mục 5.1 `ssn-system:Condition`; [61], [62] là bài báo, chưa đọc), tài liệu MLflow/DVC. Phần D đánh dấu `[CẦN NGUỒN]` tại các chỗ này; MLflow/DVC không đưa vào tiểu luận (CLAUDE.md 6.2 đã bỏ khỏi 5.6A).

## Phần A. Hai khoảng trống

### G-A. Bằng chứng trạng thái có phạm vi hiệu lực

Phát biểu. Trong các tài liệu đã rà soát, kết quả rút từ dữ liệu dao động của kết cấu có liên kết bu lông chưa được ghi thành bằng chứng trạng thái mang bắt buộc nguồn gốc, phiên bản phương pháp, độ bất định và phạm vi hiệu lực (đơn vị đánh giá, lần lắp ráp – can thiệp, điều kiện vận hành), ở dạng kiểm được bằng máy khi bằng chứng được dùng.

Phần đã được giải quyết. Từ vựng nguồn gốc cho từng thực thể đã có trong PROV-O [69]: một kết quả là `prov:Entity` sinh bởi một `prov:Activity` có thời điểm, theo một `prov:Plan` gắn qua `prov:qualifiedAssociation` (mục 3.1, 3.3, 4). SSN có `ssn-system:Condition` để khai điều kiện mà năng lực đo của cảm biến có hiệu lực (Khuyến nghị W3C, mục 5.1). Thẻ mô hình của Mitchell và cs. (`82WQNDHU`, tr. PDF 3–5) và phiếu thông tin mô hình của [53] (tr. 5–6) khai phiên bản, trường hợp ngoài phạm vi, yếu tố thiết bị đo và môi trường ở mức mô hình. MLflow và DVC cấp phiên bản và dòng dõi cho mô hình và tệp đầu ra (tài liệu chính thức).

Phần còn thiếu. Các tiền lệ trên khai phạm vi ở mức mô hình hoặc cảm biến, dạng văn bản hay từ vựng tùy chọn. Phần chưa thấy là phạm vi hiệu lực và độ bất định như trường bắt buộc của từng bằng chứng, có lần lắp ráp – can thiệp là thành phần, và được kiểm khi bằng chứng được dùng (C5, C9).

Căn cứ (chi tiết trang ở Bảng kiểm, nội dung ở Phần D 5.2.1). Bằng chứng (TG): [18] tr. 283; [56] tr. 011102-4; Maes 2022 tr. 6, 20; [53] tr. 3, 5; [7] tr. 9, 11; [16] tr. PDF 14. Diễn giải ([NCS]): [3] tr. 13–14 không mô tả phiên bản thuật toán hay điều kiện áp dụng. Dữ liệu ngược chiều một phần: một lần siết lại trong phòng thí nghiệm không làm mất hiệu lực bộ phân loại ([48] tr. 9–10), nên phát biểu dùng "phải ghi để kiểm được", không dùng "luôn làm mất hiệu lực".

Vì sao quan trọng. Người quản lý kiểm tra – bảo trì nhà xưởng cần trả lời "tin được đến mức nào?" trước khi điều kỹ sư lên kiểm tra một liên kết. Diễn giải: một kết quả không kèm phạm vi hiệu lực có thể được dùng tiếp sau khi bu lông đã siết lại hay cấu kiện đã thay, và khi đó quyết định kiểm tra dựa trên một đường cơ sở không còn đúng. Với nhà xưởng có cầu trục, điều kiện vận hành (cờ cầu trục, nhiệt độ) phải nằm trong phạm vi đó (UV-08).

Mục tiêu đáp ứng: MT1 (tạo bằng chứng có phạm vi), MT2 (trường bắt buộc và ràng buộc C5, C9), MT3 (áp dụng ở hiện trường).

### G-B. Từ bằng chứng đến hành động có trách nhiệm

Phát biểu. Trong các tài liệu đã rà soát, chuỗi kiểm tra – cấu kiện – hành động đã có chuẩn biểu diễn, nhưng bằng chứng có phạm vi hiệu lực (cảm biến, NDT) chưa đi vào chuỗi đó, và mỗi lần đổi trạng thái của hành động, kể cả lần kỹ sư xác nhận một đầu ra AI, chưa được ghi thành sự kiện có căn cứ, vai trò người thực hiện và bước xác minh sau sửa chữa.

Phần đã được giải quyết. [35] biểu diễn chuỗi lần kiểm tra → hư hỏng → cấu kiện → nhiệm vụ bảo trì → chi phí bằng thực thể chuẩn IFC 4.3 cho phát hiện bằng mắt (tr. 3, 5–7). IFC4 có yêu cầu hành động, lệnh bảo trì và nhiệm vụ có trường trạng thái, cùng `IfcApproval` ghi người, thời điểm và trạng thái phê duyệt. BCF 3.0 (`K5SGFIGW`) có trạng thái vấn đề gắn cấu kiện và dịch vụ sự kiện ghi ngày, người, loại thay đổi (BCF-API mục 3.9). [44] áp bước chuyển có gói bằng chứng, vai trò tách biệt cho gói thông tin bàn giao (tr. 3, 12, 19–25).

Phần còn thiếu. Trạng thái của [35] chỉ gắn hư hỏng (`ACTIVE`/`OUTDATED`/`REPAIRED`, tr. 9–10); IFC4 chỉ giữ giá trị hiện tại; sự kiện BCF ghi loại và giá trị mới, không ghi căn cứ. Phần chưa thấy là sự kiện chuyển trạng thái của hành động trỏ về bản ghi sử dụng bằng chứng (C6, C9), và một lần xác nhận đầu ra AI được ghi đồng thời là bản ghi trách nhiệm và nhãn hiện trường có độ bất định.

Căn cứ (chi tiết ở Bảng kiểm và Phần D 5.2.2). Bằng chứng (TG): [7] tr. 12; Hughes 2022 tr. 7, 27–28; Bull 2022 tr. 1–2, 4; Wang & Cha 2021 tr. 2, 20; Mosqueira-Rey 2023 tr. 3006, 3012, 3040; [22] tr. 192 (căn cứ nhu cầu). Diễn giải ([NCS]): chuỗi của [3] dừng ở cảnh báo và hỗ trợ quyết định (tr. 6, 13–14). CMMS đối chiếu ở mức nguồn thứ cấp qua [29] tr. 7, 11.

Vì sao quan trọng. Câu hỏi "ai đã xử lý, dựa vào đâu?" của người quản lý chỉ trả lời được khi mỗi bước chuyển trạng thái giữ người, vai trò, thời điểm và bằng chứng đã dùng. Diễn giải: trong kiểm định an toàn, khi xảy ra sự cố sau một lần sửa chữa, đơn vị quản lý cần truy ngược quyết định "siết lại" về bằng chứng và người phê duyệt; hồ sơ hiện hành (B0) ghi kết quả cuối, không ghi chuỗi đó.

Mục tiêu đáp ứng: MT2 (tầng trách nhiệm, C6, C9, logic bốn mức), MT3 (kịch bản cột C3 đầu cuối, nhãn hiện trường từ 1–2 đợt kiểm tra).

## Phần B. Ba mục tiêu

### MT1. Bằng chứng trạng thái liên kết bu lông có phạm vi hiệu lực (phòng thí nghiệm)

1. Mục tiêu: định lượng hiệu năng của bốn mô hình (RF, SVM-RBF, 1D-CNN, ResNet1D) phân biệt trạng thái liên kết bu lông có kiểm soát trên khung thép 1:10 khi đánh giá theo đơn vị độc lập, và khai báo phạm vi hiệu lực cho từng kết quả.
2. RQ1: Khi giữ lại cả lần chạy trong đánh giá, bốn mô hình phân biệt các trạng thái liên kết ở mức nào, chênh lệch bao nhiêu so với đánh giá cùng lần chạy, và mỗi kết quả được phép dùng trong phạm vi nào?
3. Nội dung: (a) xác định đơn vị độc lập (lần chạy, đợt) trên dữ liệu ba đợt; (b) huấn luyện RF, SVM-RBF trên đặc trưng thủ công miền thời gian – tần số và 1D-CNN, ResNet1D trên tín hiệu chuẩn hóa; (c) đánh giá theo nhóm giữ lại cả lần chạy, chấm điểm theo bản ghi, kiểm định hoán vị, báo cáo biến thiên theo seed và fold; (d) ghi mỗi kết quả thành bản ghi `EVIDENCE` có `method_version` (git commit), `uncertainty`, phạm vi (`inference_unit`, `data_split`, `install_batch`).
4. Dữ liệu và tài sản: dữ liệu ba đợt thí nghiệm; schema rút gọn (thực thể `EVIDENCE`).
5. Tiêu chí hoàn thành: hiệu năng theo đơn vị độc lập kèm biến thiên seed – fold và p hoán vị; chênh lệch so với đánh giá cùng lần chạy; mọi kết quả trong bài có khai báo phạm vi hiệu lực.
6. Sản phẩm: Bài 1 (Q2/Q3, SHM – đo lường); chương MT1 của luận án.
7. Rủi ro: ba đợt cho ít đơn vị độc lập, khoảng tin cậy rộng. Giảm: báo cáo số đơn vị, khoảng tin cậy và kiểm định hoán vị; giới hạn tuyên bố trong phạm vi đã khai; luận điểm của bài là giao thức đánh giá và khai báo phạm vi, không phụ thuộc mô hình nào thắng.

### MT2. Mô hình thông tin truy vết bằng chứng → hành động

1. Mục tiêu: xây dựng mô hình thông tin 6 thực thể, 5 ràng buộc (C1, C3, C5, C6, C9) mở rộng IFC 4.3 của [35] và BCF 3.0, và đo M1–M4 so với B0 trên BIM nhà xưởng thật.
2. RQ2: So với hồ sơ kiểm định hiện hành (B0), mô hình thông tin mở rộng IFC 4.3 – BCF 3.0 bằng tầng bằng chứng và tầng trách nhiệm thay đổi M1–M4 ở mức nào?
3. Nội dung: (a) đặc tả 6 thực thể, ánh xạ sang IFC 4.3 ([35]) và BCF 3.0, kèm một bảng ánh xạ khái niệm sang SOSA/SSN, PROV-O; (b) viết script Python kiểm 5 ràng buộc và logic bốn mức `priority_level` bằng luật; (c) mã hóa tay 20–30 hồ sơ kiểm định cũ làm B0; (d) khóa trước danh sách khoảng 30 lỗi do người thứ ba chèn mù và câu hỏi truy ngược, rồi đo M1–M4 trên BIM nhà xưởng thật với bằng chứng từ MT1.
4. Dữ liệu và tài sản: schema rút gọn; BIM nhà xưởng thật; hồ sơ kiểm định cũ làm B0; bằng chứng có phạm vi đã biết từ MT1 (dùng để chèn ca dùng ngoài phạm vi).
5. Tiêu chí hoàn thành: M1 tỉ lệ bản ghi đủ thuộc tính bắt buộc; M2 tỉ lệ lỗi chèn mù script bắt được; M3 thời gian hoặc số bước trả lời ba câu hỏi của người quản lý; M4 số phút mỗi bản ghi; cả bốn so với B0.
6. Sản phẩm: Bài 2 (Q2, tin học xây dựng); chương MT2 của luận án.
7. Rủi ro: hồ sơ B0 không đồng nhất về mẫu và mức chi tiết, làm so sánh M1, M3 thiên lệch. Giảm: khóa quy tắc mã hóa trước khi mã hóa, ghi trường nào B0 không có thay vì suy ra, báo cáo M1–M4 theo từng loại hồ sơ.

### MT3. Triển khai và kiểm chứng khả thi trên nhà xưởng thật

1. Mục tiêu: triển khai chuỗi bằng chứng → hành động của MT2 trên một nhà xưởng khung thép có BIM (6–10 cảm biến ở liên kết đại diện, quan trắc 3–6 tháng) và kiểm chứng khả thi bằng kịch bản cột C3 đầu cuối.
2. RQ3: Trên một nhà xưởng thật, chuỗi bằng chứng → hành động có thu đủ dữ liệu, giữ đúng ánh xạ cảm biến – cấu kiện, truy ngược được kịch bản cột C3 hay không, và với chi phí ghi nhận bao nhiêu?
3. Nội dung: (a) lắp cảm biến, ghi `SENSOR_MAPPING` có `valid_from`, `valid_to`, `install_record_ref`; (b) lập đường cơ sở vận hành; Autoencoder sinh bằng chứng cảm biến, bù tối thiểu bằng hồi quy nhiệt độ và cờ cầu trục chạy/dừng; (c) 1–2 đợt kiểm tra thật, kết quả của kỹ sư ghi làm nhãn hiện trường và `INSPECTION_RECORD`; (d) chạy kịch bản cột C3 đầu cuối, đo M3, M4.
4. Dữ liệu và tài sản: BIM nhà xưởng thật; cam kết lắp cảm biến; schema rút gọn.
5. Tiêu chí hoàn thành (CLAUDE.md 2A): tỉ lệ dữ liệu về đủ; ánh xạ cảm biến – cấu kiện đúng (C3 qua, đối chiếu thực địa); kịch bản C3 truy ngược được (M3); chi phí ghi nhận (M4). MT3 chỉ tuyên bố khả thi và truy vết, không tuyên bố hiệu năng phát hiện hư hỏng ở hiện trường.
6. Sản phẩm: chương MT3 của luận án; phần hiện trường của Bài 2 nếu kịp, hoặc bài hội nghị (không bắt buộc).
7. Rủi ro: quan trắc ngắn hơn dự kiến. Giảm: thời gian ngắn vẫn đủ cho tuyên bố khả thi và truy vết (dữ liệu về, ánh xạ, kịch bản C3, chi phí); Bài 2 kiểm chứng bằng BIM, B0 và dữ liệu MT1 nên không phụ thuộc MT3.

## Phần C. Ma trận

| Khoảng trống | Mục tiêu | RQ | Bài báo | Chương luận án | Chỉ số / kết quả đo |
|---|---|---|---|---|---|
| G-A | MT1 | RQ1 | Bài 1 | Chương MT1 | Hiệu năng theo đơn vị độc lập; chênh lệch so với cùng lần chạy; khai báo phạm vi |
| G-B (+G-A) | MT2 | RQ2 | Bài 2 | Chương MT2 | M1, M2, M3, M4 so với B0 |
| G-A, G-B (áp dụng) | MT3 | RQ3 | Bài 2 (phần hiện trường, nếu kịp) | Chương MT3 | Dữ liệu về đủ; ánh xạ đúng (C3); M3 kịch bản cột C3; M4 |

Số chương của luận án chưa đánh số; ghép ở tháng 7–9 theo CLAUDE.md mục 13.

## Phần D. Văn bản đề xuất thay mục 5.2 và mục RQ (chờ NCS duyệt, chưa chèn vào `tieuluan/`)

### 5.2. Hai khoảng trống nghiên cứu

#### 5.2.1. Khoảng trống A – Bằng chứng trạng thái có phạm vi hiệu lực

Kết quả rút từ dữ liệu dao động của kết cấu có liên kết bu lông phụ thuộc lần lắp ráp và mẫu kết cấu. Sau mỗi lần lắp lại khi bảo trì, phần lớn dữ liệu đáp ứng đã thu mất tác dụng cho theo dõi trạng thái \[18\]; bộ phân loại học trên một mẫu dầm không phân loại được dữ liệu của mẫu khác \[56\]. Trên cầu thép KW51, sau khi liên kết bu lông được gia cường giữa thời gian theo dõi, mô hình huấn luyện trên dữ liệu trước can thiệp không còn đại diện cho trạng thái bình thường \[@2ZJSENQU\]. Đánh giá vì vậy phải tách theo đơn vị độc lập và nêu rõ phân bố mà kết quả hướng tới \[53\].

Từ vựng ghi nguồn gốc cho từng kết quả đã có trong PROV-O \[69\]; SSN có khái niệm điều kiện mà năng lực đo của cảm biến có hiệu lực \[CẦN NGUỒN: Khuyến nghị W3C SSN, mục 5.1\]; thẻ mô hình \[@82WQNDHU\] và phiếu thông tin mô hình \[53\] khai phiên bản và trường hợp ngoài phạm vi ở mức mô hình. Trong các tài liệu đã rà soát, phạm vi hiệu lực chưa là trường bắt buộc của từng bằng chứng, có lần lắp ráp – can thiệp và điều kiện vận hành làm thành phần, và được kiểm khi bằng chứng được dùng. Các khung song sinh số cho công trình đã đọc xuất cảnh báo không kèm phiên bản thuật toán hay điều kiện áp dụng \[3\] và tự nêu rằng tính hợp lệ của dự đoán còn cần kiểm chứng \[7\]. Với nhà xưởng, trạng thái vận hành của cầu trục thuộc phạm vi này (Mục 3.2).

#### 5.2.2. Khoảng trống B – Từ bằng chứng đến hành động có trách nhiệm

Chuỗi lần kiểm tra – hư hỏng – cấu kiện – nhiệm vụ bảo trì đã được biểu diễn bằng thực thể chuẩn IFC 4.3 cho phát hiện bằng mắt \[35\]. IFC4 có lệnh bảo trì có trạng thái và phê duyệt ghi người, thời điểm \[CẦN NGUỒN: IFC4 ADD2 TC1\]; BCF 3.0 ghi trạng thái vấn đề gắn cấu kiện và sự kiện đổi trạng thái \[@K5SGFIGW\]; bước chuyển có gói bằng chứng và vai trò tách biệt đã được áp cho gói thông tin bàn giao \[44\]. Trạng thái trong \[35\] gắn với hư hỏng, không gắn với hành động; sự kiện BCF ghi giá trị mới, không ghi căn cứ.

Ở phía dữ liệu đo, chuỗi của các khung song sinh số đã đọc dừng ở cảnh báo và hỗ trợ quyết định \[3\], hoặc yêu cầu người dùng xác nhận mà không nêu cách ghi lần xác nhận \[7\]. Nhãn ở công trình vận hành phải lấy từ kiểm tra, vốn tốn kém và có thể sai \[@87NKU5IS\], \[@Z9RD5DMZ\]; xác nhận của chuyên gia thường được dùng làm nhãn hay dữ liệu huấn luyện \[@73MBWFVJ\]. Bảo trì nhà công nghiệp thép cần hồ sơ hư hỏng cập nhật liên tục để theo dõi khắc phục \[22\], trong khi dữ liệu bảo trì nằm ở các hệ CMMS riêng rẽ \[29\]. Trong các tài liệu đã rà soát, bằng chứng có phạm vi hiệu lực chưa đi vào chuỗi kiểm tra – cấu kiện – hành động, và mỗi lần đổi trạng thái của hành động, kể cả lần kỹ sư xác nhận một đầu ra AI, chưa được ghi thành sự kiện có căn cứ, vai trò người thực hiện và bước xác minh sau sửa chữa.

Hai khoảng trống nối với nhau qua bản ghi sử dụng bằng chứng: khoảng trống A xác định bằng chứng nào còn dùng được, khoảng trống B xác định việc dùng đó được ghi và giải trình ra sao.

### 5.4. Câu hỏi nghiên cứu

RQ1 (MT1). Khi giữ lại cả lần chạy trong đánh giá, bốn mô hình RF, SVM-RBF, 1D-CNN và ResNet1D phân biệt các trạng thái liên kết bu lông có kiểm soát trên khung thép 1:10 ở mức nào, chênh lệch bao nhiêu so với đánh giá cùng lần chạy, và mỗi kết quả được dùng trong phạm vi nào?

RQ2 (MT2). So với hồ sơ kiểm định hiện hành, mô hình thông tin mở rộng IFC 4.3 \[35\] và BCF 3.0 bằng tầng bằng chứng và tầng trách nhiệm thay đổi bốn chỉ số (đủ thuộc tính bắt buộc, phát hiện lỗi chèn mù, truy ngược, chi phí ghi nhận) ở mức nào?

RQ3 (MT3). Trên một nhà xưởng khung thép thật có BIM, chuỗi bằng chứng – hành động có thu đủ dữ liệu, giữ đúng ánh xạ cảm biến – cấu kiện và truy ngược được một kịch bản kiểm tra – xử lý đầu cuối không, với chi phí ghi nhận bao nhiêu?
