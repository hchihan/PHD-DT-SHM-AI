# HT12 — Kế hoạch rà soát tiểu luận r6 và slide bảo vệ (chờ NCS duyệt)

Ngày lập: 03/10/2026. Trạng thái: **kế hoạch, chưa sửa tệp nào**.

**Đối tượng rà soát**
- Tiểu luận: `xuat_ban/HO_CHI_HAN_TIEU_LUAN_TONG_QUAN_20261003_r6.docx`. Nguồn là `tieuluan/*.md`, trùng với r6; chưa có thay đổi nào sau khi xuất.
- Slide: `BAO_CAO_TLTQ_02102026.pptx`, 19 slide. Bản này dựng trước r4–r6.

**Góp ý dùng làm căn cứ**
- Năm nhóm ưu tiên trong yêu cầu của NCS ngày 03/10/2026.
- Báo cáo phản biện Paper 2 trong dự án: `05_PAPER_2_TRACEABILITY/P2A_audit_20261002/P2A_1_phan_bien_20261002.md` (gọi tắt là P2A). Báo cáo này hội tụ với ưu tiên 1–2. **NCS xác nhận có dùng P2A làm căn cứ hay không** (câu hỏi Q0).

**Nguyên tắc**
- Không thêm nguồn, không tạo kết quả, không tự đặt luật mới.
- Mọi điều chỉnh thiết kế (schema, chỉ số, luật dùng bằng chứng) là quyết định của NCS, ghi ở cột "Cần NCS xác nhận".
- Tiểu luận là báo cáo tổng quan. Chi tiết đặc tả của Paper 2 (giao thức 5 vai, niêm phong SHA-256, khoảng Clopper–Pearson) giữ ở hồ sơ Paper 2; tiểu luận chỉ nêu nguyên tắc trong 2–4 câu.

**Mức độ sửa**
- **L** – logic nghiên cứu: đụng thiết kế, cần NCS quyết định.
- **D** – diễn đạt: biên tập được ngay.
- **T** – trình bày: slide, bảng, hình.

---

## 1. Bảng công việc

| Mã | Ưu tiên | Câu hội đồng có thể hỏi | Vị trí trong r6 / slide | Nội dung đang có | Cách sửa đề xuất | Bằng chứng cần kiểm | Mức | Cần NCS xác nhận |
|---|:--:|---|---|---|---|---|:--:|---|
| R2-1 | 1 | "Cảm biến đặt ở cột C3 thì bằng chứng nói hư hỏng nằm ở C3 à?" | 1.3 đoạn kịch bản ("tạo một bằng chứng trạng thái gắn với cột C3"); 4.2 đoạn 2; 4.6.1; A.1 dòng EVIDENCE (`BIM_GUID` n:m); slide 5, 15 | Quan hệ bằng chứng – cấu kiện chưa định nghĩa nghĩa. Riêng 4.2 có một câu "bất thường có thể đến từ cấu kiện lân cận" | Định nghĩa: liên kết bằng chứng – cấu kiện là **cấu kiện/khu vực mà nguồn đo giám sát** (vùng đề nghị kiểm tra). **Vị trí hư hỏng** chỉ được xác lập trong bản ghi kiểm tra (`finding`). Sửa câu kịch bản 1.3 thành "bằng chứng gắn với khu vực cột C3 mà cảm biến giám sát". Thêm 1 câu vào 4.6.1 và chú thích A.1 | [2] (quan hệ cảm biến – cấu kiện), câu sẵn có ở 4.2; không cần nguồn mới | L + D | D1: nghĩa của quan hệ n:m |
| R2-2 | 1 | "Từ lúc có cảnh báo đến lúc mở hồ sơ kiểm tra, dữ liệu nào ghi lại việc đề nghị kiểm tra?" | 4.5 (hai trục); 4.6.1; A.1 dòng ACTION (bắt buộc `Inspection_Record_ID`); A.2 bước "(tạo) → Mở, căn cứ bản ghi kiểm tra"; B.1 C1 | ACTION chỉ được tạo sau khi đã có bản ghi kiểm tra. Mức ưu tiên nằm trên ACTION. Bước "cảnh báo → đề nghị kiểm tra" vì vậy **không có bản ghi** | Phương án a: cho ACTION có `action_type` ∈ {kiểm tra, can thiệp}; hành động kiểm tra tạo từ một bản ghi sử dụng bằng chứng, trước khi có bản ghi kiểm tra (trùng P2A ĐX6). Phương án b: giữ schema, viết rõ đề nghị kiểm tra là mức ưu tiên tính từ bằng chứng và chưa thành hành động, ghi là giới hạn. Kèm một hình trình tự 5 bước: cảnh báo → đề nghị kiểm tra → bản ghi kiểm tra → quyết định → xác minh | P2A §3.2 N3, §5 ĐX6; A.2 hiện có | **L** | D2: chọn a hay b |
| R2-3 | 1 | "Bằng chứng ngoài phạm vi thì xử lý thế nào: bỏ, cảnh báo hay vẫn dùng?" | 4.6.1 (đoạn 5 ràng buộc); A.1 EVIDENCE_USE; B.1 C5 và câu "đợt lắp đặt đổi khi … Đã xác minh"; slide 14 ("trong phạm vi? nếu không, lý do?") | C5 chỉ đòi có lý do. Chưa có quy định bằng chứng ngoài phạm vi được làm căn cứ cho bước nào. Mốc đổi đợt lắp đặt đặt ở "Đã xác minh", tạo cửa sổ phạm vi sai giữa Hoàn thành và Đã xác minh (P2A N2) | Nêu ba lựa chọn để NCS chọn, **không tự đặt luật**: (i) giữ C5 như hiện tại; (ii) ngoài phạm vi chỉ được dùng để đề nghị kiểm tra, không làm căn cứ cho Hoàn thành hoặc Đã xác minh; (iii) như (ii) và thêm `within_scope` ba trị TRUE/FALSE/UNKNOWN, UNKNOWN xử lý như FALSE (P2A B3). Riêng mốc đợt lắp đặt: chuyển sang sự kiện Đang xử lý → Hoàn thành của hành động can thiệp (P2A ĐX2) | P2A B3, N2, ĐX2, ĐX6 | **L** | D3: chọn (i), (ii) hoặc (iii); duyệt ĐX2 |
| R2-4 | 1 | "'Ai đã xử lý' mà chỉ ghi vai trò, không ghi người?" | 1.3 câu hỏi 3; A.1 `inspector_role`, `actor_role`; slide 4/5 | Chỉ ghi vai trò. P2A N1: yếu hơn [35] và BCF ở chỗ ghi "ai" | Phương án a: thêm `actor_ref` (mã người, mã tổ chức; không lưu tên) và vế "người xác minh ≠ người thực hiện" (ĐX1). Phương án b: sửa câu hỏi 3 thành "vai trò nào đã xử lý, dựa vào đâu" và ghi giới hạn | P2A N1, ĐX1; [35] tr. 9; BCF 3.0 | L | D4 |
| R2-5 | 2 | "B1 có được dựng hết khả năng của IFC/BCF không, hay dựng yếu để mô hình đề xuất thắng?" | 4.6.2 bước 4 ("B1 … chỉ dùng IFC 4.3 theo [35] cùng BCF 3.0, chưa có tầng…"); Bảng B.2 (B1 "Không" ở C3, C5, C9); slide 15, 17 (câu xin góp ý 2) | B1 mô tả bằng phần thiếu. Bảng B.2 cho thấy kết quả B1 ở ba nhóm lỗi đã được định trước | Mô tả B1 bằng **những gì nó có**: quy ước ACTIVE/OUTDATED/REPAIRED và `IfcOwnerHistory` theo [35]; `IfcSensor` và `IfcRelAssignsToProduct` theo [2]; `IfcApproval`; sự kiện đổi trạng thái của BCF 3.0. B1 chạy phiên bản rút gọn của các ràng buộc trên chính trường của nó (C3′, C6′, C9′). B.2 thêm cột "biểu diễn được trong B1". Trong tiểu luận chỉ cần 3–4 câu ở 4.6.2 và chỉnh B.2 | [35] tr. 4–10; [@K5SGFIGW] BCF 3.0; [@63XPSMIR] IFC4; P2A B5 (điểm BCF-API ghi [CẦN KIỂM]) | **L** | D5 |
| R2-6 | 2 | "Lỗi chèn được đặt tên theo ràng buộc thì mô hình đề xuất bắt được gần 100 % là hiển nhiên?" | 4.6.2 bước 5; 5.5 Bảng 5.3; Bảng 5.4 lớp V2; Bảng 5.5; B.2 | M2 so với B1 dễ bị xem là vòng tròn (P2A B1) | Trong tiểu luận, nói ở mức nguyên tắc: (1) phép so với B1 trước hết là **phân tích** loại lỗi nào chuyển từ "không biểu diễn được" sang "kiểm được bằng máy"; (2) M2 thực nghiệm xác nhận phân tích đó; (3) lỗi chèn lấy từ nguồn độc lập với ràng buộc, có báo cả tỉ lệ báo sai trên bản ghi hợp lệ (ĐX3). Chi tiết vai, niêm phong giữ ở hồ sơ Paper 2 | P2A B1, B6, ĐX3, câu tiếng Anh số 5 | **L** | D5 (gộp): duyệt ba tầng kết quả và ĐX3 (đổi định nghĩa M2 đã khóa) |
| R2-7 | 2 | "Anh mở rộng lược đồ IFC hay chỉ lưu SQLite rồi xuất ra?" | 4.6.1 ("phần mở rộng của mô hình IFC 4.3 của [35]"); 4.6.2 bước 2; 4.7; 5.3 MT2 ("mở rộng mô hình IFC 4.3"); Bảng 5.2 ("Mô hình sáu thực thể"); Bảng 5.5 dòng 3; A.3 câu dẫn; slide 14–15 | Gọi là "mở rộng IFC 4.3" và dùng "sáu thực thể" như đóng góp, trong khi dữ liệu lưu SQLite và chỉ xuất ra IFC | Đổi tên: "**lớp dữ liệu bằng chứng – trách nhiệm liên thông với IFC 4.3 và BCF 3.0 qua ánh xạ xuất**", không sửa chuẩn. Phần mới chỉ gồm hai điểm: phạm vi hiệu lực bắt buộc, kiểm tại lần dùng; quan hệ định kiểu từ bước chuyển trạng thái tới bản ghi sử dụng bằng chứng. Bỏ "sáu thực thể" khỏi cột đóng góp và kết quả | P2A §1, B4, câu tiếng Anh 1–2; García 2026b **chưa đọc** nên phát biểu giữ "trong tài liệu đã rà soát" | L + D | D6: câu chữ tên gọi |
| R2-8 | 2 | "Xuất ra IFC/BCF rồi đọc lại có mất thông tin không? Truy ngược làm bằng gì?" | 4.6.2 (IfcOpenShell đọc/ghi); 4.4 (IDS là hướng mở rộng); A.3 | Không có phép thử xuất – nhập; truy ngược chỉ đo bằng M3 | Mô tả **phép thử khứ hồi** SQLite → IFC/BCF → đọc lại bằng IfcOpenShell, báo tỉ lệ trường giữ được, như một **kiểm tra kỹ thuật** (không thêm chỉ số). Truy ngược ba câu hỏi chạy trên dữ liệu sau khứ hồi. Hồ sơ xuất dạng IDS vẫn là hướng mở rộng | P2A B4 | L | D6 (gộp): coi khứ hồi là kiểm tra kỹ thuật, không phải chỉ số M5 |
| R2-9 | 2 | "Bằng chứng khung 1:10 gắn lên BIM nhà xưởng 1:1 thì lúc nào cũng ngoài phạm vi, vậy C5 thử được gì?" | 4.6.2 bước 3 ("tập bằng chứng có phạm vi hiệu lực đã biết từ Mục tiêu 1"); 3.4.3 câu cuối; 5.4 đoạn cuối | Chưa có ngữ cảnh mà `within_scope` thực sự biến thiên (P2A B2) | Phương án a: dựng thêm mô hình thông tin của chính khung 1:10, mỗi lần lắp là một đợt lắp đặt (ĐX4). Phương án b: lập đợt lắp đặt của cấu kiện nhà xưởng từ lịch sử siết lại trong hồ sơ B0. Cả hai phương án đều tách C5-a (thiếu lý do) và C5-b (sai giá trị phạm vi) | P2A B2, ĐX4; 3.4.1 (giữa các đợt có tháo – lắp lại) | **L** | D7 |
| R1-1 | 3 | "Đợt sau đổi cảm biến và dạng kích động thì chênh lệch LOCO do tháo – lắp hay do đổi cấu hình?" | 3.4.1 đoạn 3 ("dạng kích động và cấu hình cảm biến có thể thay đổi"); 3.4.3; 3.2.4; 5.4 RQ1 | Cho phép đổi cấu hình giữa các đợt nhưng chưa khóa điều kiện để kết quả LOCO so sánh được | Khóa ba điều kiện so sánh LOCO: chỉ dùng kênh cảm biến có ở mọi đợt được so; cùng loại kích động; đợt bổ sung chỉ vào phép LOCO chính khi thỏa hai điều kiện trên, còn lại báo như một tầng phạm vi riêng. Viết vào 3.4.3 (2 câu) và khai báo ở trường phạm vi | 3.2.4 ([15]: vị trí cảm biến làm đổi hiệu năng); thiết kế Gate 1. Không đưa số liệu Paper 1 | **L** | D8 |
| R1-2 | 3 | "Độ bất định của một dự đoán khác gì biến thiên theo seed/fold?" | 1.3 (định nghĩa độ bất định "nhãn thay đổi ra sao khi đánh giá được lặp lại"); 3.3 (hai mức tin cậy); 3.4.3 ("biến thiên … vào trường độ bất định ở mức giao thức"); A.1 `uncertainty`; slide 5 ("Độ tin cậy") | Phân biệt đã có ở 3.3 nhưng 1.3 định nghĩa độ bất định theo một mức, A.1 chỉ có một trường, slide dùng chữ "độ tin cậy" | Phương án a (không đổi schema): xác suất của từng dự đoán ghi ở trường giá trị; trường độ bất định chỉ ghi biến thiên giao thức. Sửa 1.3, 3.4.3, A.1 và slide cho cùng một cách gọi. Phương án b: tách `uncertainty` thành hai trường con | 3.3 hiện có; P2A N6 (`evidence_level`) | D (a) / L (b) | D9 |
| R3-1 | 4 | "Truy ngược kịch bản C3 là kịch bản giả, vậy RQ3 kết luận được gì về hiện trường?" | 3.5 đoạn 3; 5.4 RQ3; Bảng 5.2 dòng KT3; Bảng 5.4 lớp V3; slide 15 | Kịch bản ghi tách với bản ghi kiểm tra thật, nhưng RQ3 chưa nói căn cứ chính là gì. Chưa có phương án khi 3–6 tháng không có bất thường thật | RQ3 nói rõ: căn cứ chính là dữ liệu thật, ánh xạ thật và 1–2 đợt kiểm tra thật. Kịch bản giả định chỉ kiểm khả năng truy ngược của chuỗi, được đánh dấu "giả định" trong dữ liệu. Nếu không có bất thường thật, báo truy ngược trên đợt kiểm tra định kỳ thật và ghi giới hạn | 3.5 hiện có; CLAUDE.md §2A (MT3 chỉ khả thi và truy vết) | L + D | D10 |
| R3-2 | 4 | "Anh có dùng bộ phân loại 1:10 ở nhà xưởng không?" | 1.2.4 đoạn "Khoảng cách giữa phòng thí nghiệm và hiện trường", câu cuối ("bộ phân loại và ngưỡng chỉ được dùng ở hiện trường sau khi kiểm tra phạm vi hiệu lực"); 3.2.2 đoạn cuối; slide 12 | Câu ở 1.2.4 ngầm cho phép dùng, trái với slide 12 ("không chuyển") | Sửa thành: luận án không dùng bộ phân loại và ngưỡng của mô hình 1:10 ở nhà xưởng; ở hiện trường, bằng chứng tạo bằng phát hiện bất thường so với đường cơ sở của chính công trình (Mục 3.5) | Không cần nguồn mới | D | Không |
| R3-3 | 4 | "MT3 kiểm chứng được những gì của chuỗi?" | 3.5 đoạn 3; 3.6; 5.7 | Đã nói "khả năng vận hành", nhưng chưa nói rõ không đánh giá hiệu năng autoencoder và bù nhiệt độ | Thêm một câu vào 5.7: MT3 kiểm việc thu, ghi và truy vết của chuỗi; hiệu năng phát hiện của autoencoder và bù nhiệt độ – cầu trục là hướng sau luận án | CLAUDE.md §2A | D | Không |
| C-1 | 5 | "Mô hình có mấy thực thể?" | 4.6.1 ("sáu thực thể"); Bảng 5.2; A.1 (SENSOR và SENSOR_MAPPING; quan hệ EVIDENCE_USE); slide 14 (sơ đồ 6 ô) | Đọc A.1 dễ đếm ra 7–8 bảng | Viết thống nhất "sáu thực thể và quan hệ sử dụng bằng chứng"; nếu duyệt R2-7 thì bỏ con số khỏi phần đóng góp | A.1 | D | Không |
| C-2 | 5 | "30 tài liệu đọc sâu hay 29 đọc toàn văn?" | 1.5.2 ("30 key đọc sâu (12 đọc toàn văn và 18 đọc có trọng tâm)"); Khai báo AI ("29/30 đọc toàn văn"); Dẫn nhập; slide 6 phễu ("45 ứng viên → nhận 22", "29 đọc toàn văn") | Mâu thuẫn: 12 đọc toàn văn (1.5.2) với 29 đọc toàn văn (Khai báo AI). Slide còn số 45/22 mà r6 đã bỏ | Một công thức dùng chung: "84 tài liệu được trích dẫn; 30 tài liệu key (12 dự kiến đọc toàn văn, 18 đọc có trọng tâm), thực tế 29/30 đã đọc toàn văn". Bỏ số 45/22 khỏi slide hoặc đưa lại vào r6 (NCS chọn) | CLAUDE.md §7, bao_cao_GD1 | D | D11 |
| C-3 | 5 | "Phạm vi hiệu lực gồm những gì?" | Thuật ngữ; 1.3; 3.3 đoạn 2; A.1 (`scope.*`); B.1 C5 (chỉ đợt lắp đặt và điều kiện vận hành) | Bốn nơi định nghĩa khác nhau; C5 chỉ kiểm hai thành phần | Một định nghĩa vận hành ở Thuật ngữ và 1.3: bộ ⟨đơn vị suy luận, cách chia dữ liệu, đợt lắp đặt, điều kiện áp dụng, cấu hình cảm biến⟩; các mục khác trỏ về. Ghi rõ thành phần nào C5 kiểm bằng máy, thành phần nào chỉ khai báo | P2A B3, N6 | D (+L nếu đổi C5) | D12 |
| C-4 | 5 | "Hệ thống của anh là song sinh số hay bóng số?" | r6: 1.1.2, 2.4, 5.7, 5.8 (mục tiêu kiến trúc); slide 16 ("Luận án đạt được: Bóng số") và slide 17 câu xin góp ý 3 | Slide trái với quyết định 03/10 | Slide 16 viết theo r6: mục tiêu kiến trúc, năng lực thực tế đánh giá sau triển khai; bỏ nhãn "đạt được: bóng số"; thay câu xin góp ý 3 | CLAUDE.md QĐ 15 | T | Không |
| C-5 | 5 | "Điều 34, 37 của Nghị định 207/2026 nói gì?" | 1.1.3 (3 thẻ [CẦN KIỂM] trong Markdown, đã gỡ khỏi docx); 1.2.4 câu "quan trắc chỉ là yêu cầu theo từng trường hợp"; slide 7 | Điều khoản chưa đối chiếu văn bản chính thức | Đối chiếu văn bản gốc trước buổi bảo vệ; nếu chưa đối chiếu được thì bỏ số điều, chỉ giữ nội dung chung kèm nguồn | Văn bản NĐ 207/2026 (NCS cung cấp) | D | NCS cung cấp văn bản |
| C-6 | 5 | "Ba câu hỏi người quản lý do ai đặt? Đã xác nhận chưa?" | 1.3; 4.6.2 ("bộ câu hỏi được xác nhận với người quản lý" – viết như việc đã làm) | Câu ở 4.6.2 dùng thì đã làm (P2A n4); câu hỏi do NCS đặt (P2A N9) | Đổi sang thì dự kiến: "sẽ được xác nhận qua phỏng vấn trước khi khóa"; 1.3 ghi ba câu hỏi là khung đề xuất của luận án | P2A N9, n4; QĐ 12 (phỏng vấn cần thầy duyệt) | D | Không |
| C-7 | 5 | "Thuật ngữ 'độ tin cậy' trên slide và 'độ bất định' trong tiểu luận có phải một?" | Slide 5, 13; r6 1.3, 3.3 | Hai cách gọi | Thống nhất theo R1-2 | – | T | Theo D9 |
| C-8 | 5 | "'Nghiên cứu thiết kế' theo khung nào?" | 5.5 đoạn 1, Bảng 5.3 | Gọi tên phương pháp mà không dẫn khung | Giữ cách mô tả trình tự ("xây dựng mô hình rồi đánh giá so với đối chứng"), bỏ nhãn; hoặc ghi [CẦN NGUỒN] nếu NCS muốn giữ nhãn | P2A n6 | D | Giữ nhãn hay không |
| C-9 | 5 | "Phạm vi 'ven biển' của đề tài?" | r6 và slide: 0 lần; charter (bản trong git): có trong tên đề tài | Tiểu luận và slide đã bỏ theo yêu cầu NCS ngày 02/10 | Chỉ kiểm lại khi xuất bản; tên đề tài đăng ký là việc hành chính, ngoài phạm vi sửa | – | – | Không |
| C-10 | 5 | Số liệu, trích dẫn trên slide có khớp r6 không | Slide 3 (478/324/68 nghìn ha, "Hiếu Phương, 2025"), slide 7 (24 %), slide 15 (3 cảm biến, 3–6 tháng) | Năm của bài Hiếu Phương chưa có trong danh mục r6 | Kiểm năm xuất bản của [XM5ZUP99]; đối chiếu từng con số slide với câu tương ứng trong r6 | Zotero XM5ZUP99 | D | Không |

---

## 2. Chi tiết theo Claim → Evidence → Limitation → Next action

### Ưu tiên 1 — Logic lõi RQ2

**R2-1. Vị trí cảm biến và vị trí hư hỏng**
- *Claim:* Bằng chứng từ cảm biến chỉ đề nghị kiểm tra một khu vực giám sát; vị trí và nguyên nhân hư hỏng do kỹ sư xác lập.
- *Evidence:* 4.2 đoạn 2 đã có câu này. A.1 cho EVIDENCE n:m COMPONENT. [2] mô hình hóa quan hệ hệ theo dõi – cấu kiện.
- *Limitation:* Không có nguồn trong r6 về cách xác định vùng giám sát của một cảm biến trên khung nhà xưởng. Vùng này được xác định bằng khảo sát ở MT3, là quyết định thực hiện.
- *Next action:* Sau khi chốt D1: sửa 1.3, 4.6.1, chú thích A.1, slide 5 và slide 15. Biên tập thuần, không đổi schema.

**R2-2. Đường đi cảnh báo → đề nghị kiểm tra → hồ sơ → quyết định → xác minh**
- *Claim:* Chuỗi phải ghi được cả bước đề nghị kiểm tra, nếu không thì câu "ai quyết định kiểm tra, dựa vào đâu" mất căn cứ.
- *Evidence:* A.1 buộc ACTION có `Inspection_Record_ID`. A.2 bắt đầu từ "(tạo) → Mở, căn cứ bản ghi kiểm tra". P2A ĐX6 đề xuất `action_type`.
- *Limitation:* Phương án a đổi Bảng A.1, A.2 đã khóa. Phương án b giữ schema nhưng phải nêu thành giới hạn.
- *Next action:* NCS chốt D2. Sau đó thêm hình trình tự 5 bước ở 4.6.1, cập nhật A.1, A.2 (nếu chọn a), và vẽ slide tương ứng.

**R2-3. Bằng chứng ngoài phạm vi hiệu lực**
- *Claim:* Cần nói rõ bằng chứng ngoài phạm vi được dùng tới đâu và khi nào phạm vi của một cấu kiện thay đổi.
- *Evidence:* B.1 C5 và câu về đợt lắp đặt; P2A B3 (vị từ `within_scope` chưa kiểm được bằng máy), N2 (cửa sổ phạm vi sai), ĐX2.
- *Limitation:* Mọi luật dùng bằng chứng là quyết định thiết kế; kế hoạch chỉ nêu phương án.
- *Next action:* NCS chốt D3. Sửa 4.6.1 (1–2 câu), B.1 (C5 và mốc đợt lắp đặt), slide 14.

**R2-4. "Ai đã xử lý"**
- *Claim:* Ghi vai trò chưa trả lời được câu hỏi "ai".
- *Evidence:* P2A N1, ĐX1; [35] tr. 9 dùng `IfcOwnerHistory`.
- *Limitation:* Thêm `actor_ref` là đổi A.1. Không thêm thì phải hạ câu hỏi 3.
- *Next action:* NCS chốt D4. Sửa 1.3, A.1, B.1 C6, slide 4/5.

### Ưu tiên 2 — Tính công bằng và tính mới của RQ2

**R2-5, R2-6. Đối chứng B1 và cách đọc M2**
- *Claim:* So sánh với B1 chỉ có giá trị khi B1 dùng hết khả năng của chuẩn, và kết quả không được định sẵn bởi cách đặt tên lỗi.
- *Evidence:* Bảng B.2 hiện tại (B1 "Không" ở C3, C5, C9). P2A B1, B5, ĐX3. [35] tr. 4–10; BCF 3.0; IFC4.
- *Limitation:* Mô hình sự kiện của BCF-API ghi [CẦN KIỂM] trong P2A, cần đối chiếu văn bản chuẩn. ĐX3 đổi định nghĩa M2 đã khóa.
- *Next action:* NCS chốt D5. Sửa 4.6.2 (3–4 câu B1, 2–3 câu cách đọc kết quả), Bảng B.2 (thêm cột), Bảng 5.4 lớp V2, Bảng 5.5, slide 15 và slide 17.

**R2-7, R2-8. Tên gọi đóng góp và phép thử khứ hồi**
- *Claim:* Đóng góp là lớp dữ liệu liên thông có ánh xạ xuất, không phải lược đồ IFC mới. Phép thử khứ hồi cho thấy ánh xạ xuất giữ được những trường nào.
- *Evidence:* A.3 ("lưu SQLite và xuất IFC"); P2A §1, B4.
- *Limitation:* García 2026b chưa đọc, nên mọi câu về tính mới phải giữ khung "trong tài liệu đã rà soát". Phép thử khứ hồi chưa có trong thiết kế khóa.
- *Next action:* NCS chốt D6. Sửa 4.6.1, 4.6.2, 4.7, 5.3, Bảng 5.2, Bảng 5.5, A.3, slide 14 và 15.

**R2-9. Ngữ cảnh để `within_scope` biến thiên**
- *Claim:* Cần ít nhất một ngữ cảnh mà bằng chứng lúc trong, lúc ngoài phạm vi; nếu không, nhóm lỗi C5 suy biến.
- *Evidence:* P2A B2, ĐX4; 3.4.1 xác nhận giữa các đợt có tháo – lắp lại.
- *Limitation:* Phương án a cần dựng thêm mô hình thông tin cho khung 1:10. Phương án b phụ thuộc chất lượng lịch sử can thiệp trong hồ sơ B0.
- *Next action:* NCS chốt D7. Sửa 4.6.2 bước 3, 3.4.3 câu cuối, 5.4 đoạn cuối.

### Ưu tiên 3 — Gate 1 / RQ1

**R1-1. Điều kiện so sánh LOCO**
- *Claim:* Chênh lệch LOCO chỉ diễn giải được là hiệu ứng tháo – lắp khi cấu hình cảm biến và dạng kích động tương thích giữa các đợt.
- *Evidence:* 3.2.4 ([15]: vị trí cảm biến làm đổi hiệu năng); 3.4.1 cho phép đổi cấu hình.
- *Limitation:* Không đưa dữ liệu hay kết quả của Paper 1 vào tiểu luận (QĐ 2).
- *Next action:* NCS chốt D8. Sửa 3.4.1 (1 câu), 3.4.3 (2 câu), Bảng 5.4 lớp V1, slide 13.

**R1-2. Hai mức tin cậy**
- *Claim:* Xác suất của một dự đoán và biến thiên của giao thức đánh giá là hai đại lượng khác nhau, phải ghi ở hai chỗ khác nhau.
- *Evidence:* 3.3 đã phân biệt; 3.4.3 đã gán biến thiên vào trường độ bất định; A.1 có `value` và `uncertainty`.
- *Limitation:* Phương án b đổi A.1.
- *Next action:* NCS chốt D9. Phương án a chỉ là biên tập: sửa 1.3, 3.4.3, Thuật ngữ, A.1 (chú thích), slide 5 và 13.

### Ưu tiên 4 — RQ3 và giới hạn kết luận

**R3-1. Dữ liệu thật và kịch bản giả định**
- *Claim:* Kết luận của RQ3 dựa trên dữ liệu và hồ sơ thật; kịch bản giả định chỉ là phép thử truy ngược.
- *Evidence:* 3.5 đoạn 3; CLAUDE.md §2A.
- *Limitation:* Nếu trong 3–6 tháng không có bất thường, không có hồ sơ thật nào phát sinh từ cảnh báo.
- *Next action:* NCS chốt D10. Sửa 5.4 RQ3, Bảng 5.2, Bảng 5.4 lớp V3, 3.5, slide 15.

**R3-2, R3-3. Không chuyển bộ phân loại; giới hạn của MT3**
- *Claim:* Ở hiện trường không dùng bộ phân loại hay ngưỡng của mô hình 1:10, và MT3 không đánh giá hiệu năng phát hiện.
- *Evidence:* 3.2.2 đoạn cuối; slide 12; CLAUDE.md §2A.
- *Limitation:* Không có.
- *Next action:* Biên tập ngay: 1.2.4 (1 câu), 5.7 (1 câu).

### Ưu tiên 5 — Nhất quán (C-1 đến C-10)

- *Claim:* Các con số, thuật ngữ và định vị phải trùng nhau giữa r6 và slide.
- *Evidence:* Bảng công việc ở mục 1.
- *Limitation:* C-5 cần văn bản Nghị định 207/2026 gốc; C-10 cần kiểm Zotero.
- *Next action:* Biên tập sau cùng, khi các quyết định thiết kế đã chốt, để không phải sửa hai lần.

---

## 3. Thứ tự thực hiện đề xuất

1. **Bước 0 — NCS chốt quyết định** (mục 4). Các việc biên tập thuần (R3-2, R3-3, C-1, C-2, C-6, C-8) có thể làm ngay, không cần chờ.
2. **Bước 1 — Sửa r6 phần logic RQ2:** R2-1 đến R2-9 trên `04_chuong4.md` (4.2, 4.5, 4.6) và `phuluc.md` (A.1, A.2, A.3, B.1, B.2), cùng câu liên quan ở 1.3. Mỗi lần sửa ghi trước/sau.
3. **Bước 2 — Sửa r6 phần RQ1, RQ3:** R1-1, R1-2 ở 3.4; R3-1, R3-2, R3-3 ở 1.2.4, 3.5, 5.4, 5.7.
4. **Bước 3 — Đồng bộ Chương 5 và phần đầu:** Bảng 5.2–5.5, 5.3, 5.4; Thuật ngữ; Dẫn nhập; C-1 đến C-10.
5. **Bước 4 — Xuất r7:** chạy `xuat_ban/build.py`, cập nhật mục lục, kiểm 84 tài liệu, kiểm tự động trích dẫn không thiếu và không thêm.
6. **Bước 5 — Đồng bộ PPTX:** slide 4/5 (vị trí cảm biến, ba câu hỏi), 6 (phễu), 7 (pháp lý), 12 (ba công trình), 13 (LOCO, độ bất định), 14 (hình trình tự, ngoài phạm vi), 15 (B1, tên gọi, RQ3), 16 (song sinh số), 17 (xin góp ý), 18 (đóng góp).
7. **Bước 6 — Kiểm chéo** theo tiêu chí ở mục 5, rồi ghi `revision/changelog.md`.

---

## 4. Các quyết định NCS cần chốt

| Mã | Câu hỏi | Khuyến nghị |
|---|---|---|
| Q0 | Có dùng P2A làm căn cứ cho kế hoạch này không? | Có. P2A là phản biện nội bộ của chính thiết kế MT2 |
| D1 | Quan hệ bằng chứng – cấu kiện có nghĩa là "khu vực giám sát, đề nghị kiểm tra", không phải vị trí hư hỏng? | Có. Biên tập thuần |
| D2 | Ghi bước đề nghị kiểm tra: (a) ACTION có `action_type`, hành động kiểm tra tạo trước bản ghi kiểm tra; (b) để ngoài mô hình, ghi giới hạn | a |
| D3 | Bằng chứng ngoài phạm vi: (i) giữ C5; (ii) chỉ dùng để đề nghị kiểm tra; (iii) (ii) cộng `within_scope` ba trị. Duyệt mốc đổi đợt lắp đặt (ĐX2)? | iii + ĐX2 |
| D4 | Thêm `actor_ref` (ĐX1) hay hạ câu hỏi 3 xuống mức vai trò? | Thêm `actor_ref` |
| D5 | Đặc tả B1 dùng hết chuẩn; kết quả MT2 báo ba tầng; M2 có tỉ lệ báo sai (ĐX3) | Duyệt cả ba |
| D6 | Tên gọi "lớp dữ liệu bằng chứng – trách nhiệm liên thông với IFC 4.3 và BCF 3.0 qua ánh xạ xuất"; phép thử khứ hồi là kiểm tra kỹ thuật, không phải chỉ số mới | Duyệt |
| D7 | Ngữ cảnh `within_scope` biến thiên: (a) mô hình thông tin của khung 1:10; (b) lịch sử siết lại trong hồ sơ B0 | a |
| D8 | Điều kiện so sánh LOCO: kênh cảm biến chung, cùng loại kích động; đợt không đạt điều kiện báo thành tầng riêng | Duyệt |
| D9 | Hai mức tin cậy: (a) giữ schema, xác suất ở trường giá trị; (b) tách trường | a |
| D10 | RQ3: căn cứ chính là dữ liệu và hồ sơ thật; kịch bản giả định được đánh dấu; xử lý khi không có bất thường thật | Duyệt |
| D11 | Công thức số tài liệu; giữ hay bỏ số 45/22 ở slide | Bỏ 45/22 ở slide, giữ "84 / 30 / 29" |
| D12 | Một định nghĩa vận hành của phạm vi hiệu lực, ghi rõ thành phần nào được kiểm bằng máy | Duyệt |

Ngoài ra NCS cần cung cấp: văn bản Nghị định 207/2026 (C-5), và năm xuất bản của bài Hiếu Phương (C-10).

---

## 5. Tiêu chí kiểm tra hai tệp sau khi sửa

**Logic RQ2**
- Có một hình hoặc đoạn mô tả đủ 5 bước: cảnh báo → đề nghị kiểm tra → bản ghi kiểm tra → quyết định → xác minh. Mỗi bước có bản ghi và vai trò tương ứng trong A.1, A.2.
- Không câu nào ngầm coi vị trí cảm biến là vị trí hư hỏng.
- Có quy định rõ cho bằng chứng ngoài phạm vi, trùng nhau giữa 4.6, B.1 và slide.
- B1 được mô tả bằng những gì nó có. B.2 có cột "biểu diễn được trong B1". Không câu nào hứa mô hình đề xuất chắc chắn vượt B1.

**Tính mới, thuật ngữ, định vị**
- Không còn "mở rộng lược đồ IFC" hay "sáu thực thể là đóng góp".
- Phát biểu tính mới chỉ gồm hai điểm và giữ khung "trong tài liệu đã rà soát".
- Một định nghĩa phạm vi hiệu lực, các mục khác trỏ về.
- "Độ bất định" và "xác suất dự đoán" dùng đúng một nghĩa ở r6 và slide.
- Song sinh số là mục tiêu kiến trúc ở cả hai tệp; không còn nhãn "đạt được: bóng số".

**RQ1, RQ3**
- RQ1 có điều kiện so sánh LOCO. Không có số liệu hay kết quả của Paper 1.
- RQ3 tách dữ liệu thật với kịch bản giả định. Không câu nào hàm ý chuyển bộ phân loại hay ngưỡng ra nhà xưởng, hoặc đã kiểm chứng hiệu năng phát hiện ở hiện trường.

**Số liệu, trích dẫn**
- Mọi con số trên slide trùng với r6: 84/30/29; 478/324/68 nghìn ha; 24 %; 20–30 hồ sơ; khoảng 30 lỗi; 3 cảm biến; 3–6 tháng.
- Trích dẫn trên slide có trong danh mục r6.
- r7 vẫn đủ 84 tài liệu; kiểm tự động không thiếu, không thêm trích dẫn so với r6.
- Không còn thẻ [CẦN KIỂM] chưa xử lý về Nghị định 207/2026 trong phần sẽ trình bày.

**Ngôn ngữ cho buổi bảo vệ chuyên đề**
- Mọi kết quả chưa làm đều viết ở thì dự kiến.
- Đóng góp ghi "dự kiến, nếu kiểm chứng ủng hộ".
- Không có câu "đầu tiên", "chưa ai nghiên cứu".
- Chi tiết đặc tả của Paper 2 không đưa vào thân tiểu luận quá 2–4 câu mỗi chỗ.
