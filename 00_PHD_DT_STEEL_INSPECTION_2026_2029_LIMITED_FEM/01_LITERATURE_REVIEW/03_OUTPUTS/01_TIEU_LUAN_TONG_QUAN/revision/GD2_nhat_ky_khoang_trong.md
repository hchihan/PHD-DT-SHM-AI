# Nhật ký ứng viên khoảng trống — Giai đoạn 2

Tạo ngày 30/09/2026 (phiên T1-3). Đây là nhật ký **làm việc**; khoảng trống chỉ được chốt ở Giai đoạn 3 (Điểm duyệt 3).
Mọi ứng viên là giả thuyết, chưa phải kết luận.

Quy ước:
- **K1** = xác lập chất lượng và phạm vi hiệu lực của bằng chứng trạng thái; **K2** = bảo toàn chất lượng bằng chứng
  trong truy vết cấp cấu kiện; **K3** = từ bằng chứng đến hành động (theo mục 5.2 của bản gốc). Đây là các giả thuyết
  làm việc.
- Căn cứ được đếm là **độc lập** khi thuộc các nhóm tác giả khác nhau và đã được đọc toàn văn hoặc đúng phần liên quan.
  Ngưỡng của Giai đoạn 3: mỗi khoảng trống cần từ 3 căn cứ, trong đó không thuộc nhóm 2025–2026 (CLAUDE.md 4.1).
- Loại căn cứ: **TG** = tác giả tự nêu; **NCS** = nhận định của NCS từ việc bài không xử lý một ý; ghi rõ khi lẫn.
- **Phản chứng đã kiểm** (quy tắc thêm ngày 30/09/2026, CLAUDE.md mục 7.4): nguồn, chuẩn hoặc hệ thống có thể đã giải quyết vấn đề
  (ví dụ CMMS, BCF 3.0, IFC Monitor [2], ISO 19650); ghi kết quả đối chiếu kèm trang, hoặc "chưa kiểm".
- **Phát biểu đã thu hẹp:** phát biểu sau khi trừ phần đã được giải quyết.
- Một ứng viên chỉ được đưa vào GĐ3 khi trường "Phản chứng đã kiểm" không còn mục nào ghi "chưa kiểm".
- Nguồn đã đọc toàn văn đến hết phiên T1-3: [8], [7], [3] (30/09/2026). Phiên T1-2 (01/10/2026): [22], [18], [19] đọc toàn văn ([19] bản tiền in arXiv). Phiên T1-4 (01/10/2026): [53], [16] (bản in thử), [17] đọc toàn văn. Phiên T1-1 (30/09/2026): [2], [44] đọc toàn văn; [35] đọc toàn văn ngày 01/10/2026 (T1-1 hoàn tất). Tài liệu chính thức đã đọc để kiểm phản chứng: BCF 3.0 (BCF-XML, BCF-API), IFC4 ADD2 TC1 (các thực thể nêu ở UV-01, UV-03), COBie 2.4 (NBIMS-US V3 chương 4.2), SSN/SOSA (Khuyến nghị W3C 2017). ISO 19650-3 không truy cập được. Phiên T1-1 (ba tiền lệ [2], [35], [44]) đã
  hoàn tất ngày 01/10/2026. Phiên T2-1 (01/10/2026): Worden 2007 `MCNRW6F5`, Cawley 2018 `EBB69J4F`, Ju 2020 `38FMATHE`
  đọc toàn văn; [45] Sohn 2007 và Figueiredo 2011 `23TBQTIP` đọc bổ sung, nay là toàn văn. Căn cứ đã dùng ở 5.6A (Bull 2022,
  Hughes 2022, Wang & Cha 2021, Figueiredo 2011) đã đưa vào UV-02 và UV-05 ngày 01/10/2026, dựa trên `notes/`; [57] Bull 2021
  chưa có ghi chú đọc nên chưa đưa vào.
- **Quy ước đếm nhóm tác giả (thêm 01/10/2026):** Worden 2007, Figueiredo 2011, Bull 2022, Hughes 2022 cùng nhóm Sheffield –
  Los Alamos (chung Worden, Farrar hoặc Bull); khi đếm căn cứ độc lập, các bài này tính là **một** nhóm.

## Bảng tóm tắt

| Mã | Phát biểu | K | Số căn cứ độc lập hiện có | Năm các căn cứ | Ghi chú |
|---|---|---|---|---|---|
| UV-01 | Hành động và lần đổi trạng thái không nối ngược được về bằng chứng tình trạng cùng phạm vi hiệu lực (đã thu hẹp) | K3 | 4 ([3], [7], [22], [44]); 3 trước 2025 ([22] chỉ là căn cứ về nhu cầu) | 2020, 2020, 2019, 2026 | Đủ số căn cứ nếu NCS chấp nhận [22]; [35] đã kiểm (01/10, thu hẹp thêm); còn CMMS chưa kiểm, ISO 19650-3 không truy cập được |
| UV-02 | Đầu ra phát hiện bất thường trong khung song sinh cho công trình chưa được ghi cùng nguồn gốc xử lý, phiên bản phương pháp và phạm vi hiệu lực | K1 | 4 ([3], [7], [53], [16]) | 2020, 2020, 2023, 2023 | Phản chứng kiểm một phần ([44], SSN, [16], [53]); còn PROV-O, MLflow/DVC, thẻ mô hình; T2-1 thêm căn cứ về **nội dung** phạm vi hiệu lực ([45], Figueiredo, Worden, Cawley, Wang & Cha), không tính vào phần "chưa được ghi" |
| UV-03 | Ánh xạ cảm biến – cấu kiện thiếu cách ghép được quy định về thời hạn hiệu lực và ràng buộc thời gian (đã thu hẹp) | K2 | 3 ([3], [7], [2]) | 2020, 2020, 2018 | **Đủ điều kiện hình thức vào GĐ3**; phần còn lại nhỏ, nên xem là yêu cầu của mô hình dữ liệu; [35] đã kiểm (không có cảm biến, không đổi kết luận) |
| UV-04 | Thiếu phân loại mức tích hợp DM/DS/DT áp cho kiểm tra – bảo trì kết cấu công trình có con người ra quyết định | mới (định vị) | 2 ([8], [7]) | 2018, 2020 | Chỉ phục vụ định vị ở 2.3, không dự kiến thành khoảng trống |
| UV-05 | Ở công trình đang vận hành thiếu dữ liệu có nhãn về bất thường; nhãn phụ thuộc đánh giá con người | mới (nhãn hiện trường; liên quan L2.3, 5.6A) | 5 nhóm ([3], nhóm Sheffield – Los Alamos: Bull 2022 + Hughes 2022 + Worden 2007, Wang & Cha 2021, [19], [17]); 3 trước 2025 | 2020, 2007–2022, 2021, 2025, 2026 | Đã nhập căn cứ 5.6A (01/10); phản chứng kiểm một phần (Hughes, Bull 2022); còn [57] và SHM theo quần thể chưa kiểm |
| UV-06 | Lần lắp ráp hoặc can thiệp bảo trì là ranh giới phạm vi hiệu lực của bằng chứng từ mối nối bu lông | K1 | 4 ([18], [53], [56], [19]); 3 trước 2025 | 2019, 2023, 2024, 2025 | Phản chứng chưa kiểm; [56] mới đọc một phần |
| UV-07 | Xác nhận của chuyên gia đối với đầu ra AI là tín hiệu học, chưa là bản ghi trách nhiệm | K3 (+5.6A) | 4 ([3], [7], Hughes 2022, [17]); 3 trước 2025 | 2020, 2020, 2022, 2026 | Mới (T1-4); phản chứng kiểm một phần (IfcApproval, [44]) |
| UV-08 | Ảnh hưởng của rung vận hành (cầu trục, máy móc) lên phát hiện suy giảm liên kết trong nhà xưởng khung thép chưa được nghiên cứu bằng dữ liệu hiện trường (đã thu hẹp) | mới (K1 – điều kiện áp dụng; L2.2) | 3 nhóm trước 2025 cho hiện tượng EOV chung ([45], nhóm Worden/Figueiredo, Cawley); cho riêng nhà xưởng: chỉ [NCS] + Ju 2020 (hiện tượng) | 2007, 2007–2011, 2018, 2020 | Mới (T2-1); phản chứng kiểm ở mức Zotero + 3 truy vấn Consensus (chỉ tóm tắt); Hu 2023, Eraliev 2022 chưa đọc toàn văn → chưa đủ điều kiện |

Tình trạng phản chứng (30/09/2026, sau phiên T1-1): UV-03 đã kiểm hết các phản chứng liệt kê ([2], [3], IFC4, SSN/SOSA). UV-01 đã kiểm BCF 3.0, IFC4, COBie 2.4, [44]; còn CMMS chưa kiểm, ISO 19650-3 không truy cập được, [35] chờ PDF. UV-02 kiểm một phần. UV-04, UV-05 chưa kiểm. Đủ điều kiện hình thức vào GĐ3 (ba căn cứ độc lập, không phụ thuộc 2025–2026, không còn "chưa kiểm"): chỉ UV-03. Cập nhật 01/10/2026 (T1-4): thêm UV-07; UV-02 có 4 căn cứ trước 2025 nhưng còn PROV-O, MLflow/DVC, thẻ mô hình chưa kiểm; UV-06 có 3 căn cứ trước 2025 (một đọc chưa đủ). Vẫn chỉ UV-03 đủ điều kiện hình thức. Đánh giá mức bảo vệ của K1–K3 theo thang của skill phd-gap-miner: `revision/GD2_phan_tich_khoang_trong_T1.md`. Cập nhật 01/10/2026 (T2-1): UV-02 và UV-05 nhập căn cứ 5.6A; UV-05 kiểm một phần (Hughes 2022, Bull 2022), còn [57] chưa kiểm; tạo UV-08 (nhiễu vận hành nhà xưởng), phản chứng mới kiểm ở mức tóm tắt. Ứng viên đủ điều kiện hình thức vào GĐ3 vẫn chỉ có UV-03. Cập nhật 01/10/2026 (T1-1, [35] Bellon): UV-01 thu hẹp thêm vì chuỗi định kiểu lần kiểm tra → hư hỏng → cấu kiện → nhiệm vụ bảo trì → chi phí đã có bằng thực thể chuẩn IFC 4.3 cho phát hiện bằng mắt; UV-01 còn CMMS chưa kiểm. UV-03: [35] không có cảm biến, kết luận giữ nguyên. Cập nhật 01/10/2026 (T1-2): thêm UV-06 (chưa kiểm phản chứng); UV-01 có căn cứ thứ ba trước 2025 ([22], chờ NCS chấp nhận) nhưng vẫn còn mục "chưa kiểm".

## UV-01 — Chuỗi cảnh báo → hành động

- **Phát biểu:** Trong các khung song sinh số đã đọc, chuỗi từ phát hiện bất thường đến hành động bảo trì dừng ở cảnh
  báo và hỗ trợ quyết định của con người, không được ghi thành trạng thái xử lý và lịch sử chuyển trạng thái có thể
  truy ngược.
- **Căn cứ:**
  - Lu và cs. 2020 [3], tr. 6 (Hình 4: kết thúc ở báo cáo – sửa chữa), tr. 13–14 (mục đích là hỗ trợ quyết định; Hình 18
    chỉ hiển thị cảnh báo), tr. 5–6 (chỉ ra IFC4 thiếu giá trị `IfcChangeActionEnum` cho FM và đề xuất
    `IfcInspectionHistory`, `IfcMaintenanceHistory`, nhưng ca nghiên cứu không dùng chúng).
  - Boje và cs. 2020 [7], tr. 12 (cảnh báo và khuyến nghị "cần người dùng xác nhận và cho phép"; không nêu mô hình ghi lại
    xác nhận), tr. 10 (Bảng 2: "chấp hành" là một khả năng, không có trạng thái hành động).
- **Loại căn cứ:** TG một phần ([3] tr. 5 tự nêu IFC4 thiếu thực thể; [7] tr. 12 tự nêu cần kiểm chứng AI trước khi
  chuyển tác vụ) + **NCS** (việc chuỗi không có trạng thái xử lý là suy từ phần bài không mô tả).
- **Liên quan:** K3.
- **Ghi chú:** đối tượng của [3] là bơm HVAC, của [7] là công trường thi công; không trực tiếp là kết cấu thép vận hành.
- **Phản chứng đã kiểm:**
  - Hệ quản lý bảo trì trên máy tính (CMMS), quản lý lệnh công việc có trạng thái: **chưa kiểm** trên nguồn chuyên về CMMS. Căn cứ gián tiếp đã có: [3] tr. 1 ghi CMMS lưu lệnh công việc hằng ngày, hồ sơ lịch sử, yêu cầu dịch vụ và thông tin bảo trì; [3] tr. 4 ghi CMMS lưu yêu cầu dịch vụ và lệnh công việc xử lý yêu cầu. Trạng thái hành động vì vậy nhiều khả năng đã được theo dõi ở CMMS.
    - *Cập nhật 01/10/2026:* hai nguồn chuyên về BIM – bảo trì mà [35] dẫn (tham khảo 31, 33) đã xác minh DOI qua Crossref và nhập Zotero (TL-Key/Bổ sung, tag `GD2-phanchung`): Chen và cs. 2018 `QZ7E3HDV` (lịch tự động cho lệnh công việc bảo trì, mở rộng IFC với thực thể quá trình và điều khiển bảo trì; theo mô tả của [35] tr. 3) và Condotta & Scanagatta 2023 `QBTTSBTH` (tích hợp BIM với phần mềm CMMS qua phân loại cơ sở dữ liệu; theo mô tả của [35] tr. 3). **Chưa đọc được bản gốc:** Chen 2018 không có bản truy cập mở; Condotta 2023 có bản nộp trên kho của IUAV, chờ NCS đồng ý tải. Mô tả trong ngoặc là lời của [35], chưa đối chiếu với bản gốc. Trạng thái mục CMMS: **chưa kiểm** (đã có nguồn, chờ PDF).
  - BCF 3.0 (`K5SGFIGW`): **đã kiểm 30/09/2026**. Nguồn đọc: tài liệu kỹ thuật BCF-XML 3.0 và BCF-API 3.0 trên kho GitHub của buildingSMART (nhánh `release_3_0`); đặc tả không đánh số trang nên dẫn theo tên mục.
    - *Trạng thái:* mỗi vấn đề (Topic) bắt buộc có `TopicStatus` và `TopicType`, giá trị lấy từ danh sách định sẵn của dự án (BCF-XML, mục Topic). Có thêm `Priority`, `DueDate`, `Stage`, `AssignedTo` (tùy chọn).
    - *Người tạo, thời điểm:* `CreationAuthor`, `CreationDate` bắt buộc; `ModifiedAuthor`, `ModifiedDate` chỉ giữ lần sửa cuối (BCF-XML, mục Topic).
    - *Bình luận:* mỗi bình luận có `Date`, `Author`, nội dung và có thể trỏ tới một góc nhìn; mục đích là ghi lại trao đổi giữa các bên (BCF-XML, mục Comment).
    - *Liên kết cấu kiện:* qua góc nhìn (viewpoint), cấu kiện được chọn mang `IfcGuid` (BCF-XML, mục Components, Component). Phần đầu tệp còn cho phép trỏ tới `IfcProject` và phần tử không gian. Vấn đề **không** có trường riêng trỏ thẳng tới cấu kiện; liên kết đi qua góc nhìn.
    - *Lịch sử chuyển trạng thái:* BCF-API 3.0 có dịch vụ sự kiện của vấn đề (mục 3.9): mỗi lần tạo hoặc sửa sinh sự kiện có `date`, `author`, loại sự kiện (trong đó có `status_updated`, `assigned_to_updated`) và giá trị mới, nhằm giữ lịch sử đầy đủ. Lịch sử này chỉ có ở BCF-API; tệp BCF-XML không mang theo.
    - *Thẩm quyền:* BCF-API cho phép máy chủ giới hạn hành động theo người dùng, kể cả các giá trị trạng thái mà người dùng được chọn (mục 1.2, 3.1.5). Đây là quyền thao tác trên hệ thống; không có khái niệm vai trò chuyên môn hay thẩm quyền phê duyệt.
    - *Liên kết ra ngoài:* `ReferenceLink` (ví dụ tới hệ quản lý yêu cầu công việc), `DocumentReferences`, `BimSnippet`, `RelatedTopic` (BCF-XML, các mục cùng tên). Đây là liên kết tự do, không định kiểu.
    - **Kết quả đối chiếu:** BCF 3.0 **đã giải quyết** phần "trạng thái vấn đề gắn cấu kiện, ai tạo, khi nào, ai đổi trạng thái" của UV-01. Phần BCF **không có**: khái niệm bằng chứng và quan hệ định kiểu từ vấn đề về bằng chứng đã làm phát sinh nó; nguồn gốc, độ bất định, phạm vi hiệu lực; căn cứ của từng lần đổi trạng thái (sự kiện chỉ ghi loại và giá trị); máy trạng thái quy định bước chuyển hợp lệ; thẩm quyền theo vai trò chuyên môn. [NCS] Các điểm "không có" là nhận định từ việc đặc tả không nêu.
    - **Hệ quả với schema (NCS):** sự kiện chuyển trạng thái và danh sách trạng thái có tiền lệ trực tiếp ở BCF-API 3.0; mục 2.2 và 5.5 cần nêu BCF như tiền lệ, và phần mới của luận án thu về quan hệ giữa sự kiện với bản ghi sử dụng bằng chứng.
  - ISO 19650-3 [1]: **không truy cập được** (30/09/2026). Lý do: toàn văn là tài liệu trả phí, không có trong Zotero hay thư mục dự án; bản xem trước trên nền tảng trực tuyến của ISO đòi chấp nhận điều khoản sử dụng trước khi mở, việc này cần NCS tự làm. Không suy đoán nội dung. Thông tin gián tiếp từ [44]: bộ ISO 19650 cho khung vai trò, trách nhiệm và trạng thái WIP–Shared–Published (tr. 3, 6) nhưng không quy định cổng kiểm tính toán được hay gói bằng chứng tối thiểu ở mức tệp (tr. 9, Bảng 2); chuyển từ ISO 19650-2 sang 19650-3 thường không liên tục (tr. 3, 23). Đây là nhận định của [44], chưa đối chiếu với chính tiêu chuẩn.
  - IFC4 (tài liệu IFC4 ADD2 TC1 của buildingSMART, dẫn theo tên thực thể): **đã kiểm 30/09/2026**.
    - `IfcActionRequest`: yêu cầu hành động, gồm cả báo hỏng cho bảo trì; có `Status` (nhãn tự do, ví dụ Hold, NoAction, Schedule, Urgent); lồng được các yêu cầu tiếp theo; gán người yêu cầu và người thực hiện; gắn phê duyệt qua `IfcRelAssociatesApproval`.
    - `IfcProjectOrder` với loại `MAINTENANCEWORKORDER`: lệnh công việc bảo trì, có `Status` (ví dụ PLANNED, REQUESTED, APPROVED, ISSUED, STARTED, DELAYED, DONE). IFC4 không có thực thể tên IfcWorkOrder.
    - `IfcTask`: có `Status` (ví dụ chưa bắt đầu, đã bắt đầu, hoàn thành); liên hệ với lệnh công việc qua `IfcRelAssignsToControl`. `IfcWorkPlan`: kế hoạch gồm các lịch và nhiệm vụ, cho cả quản lý vận hành.
    - `IfcApproval`: trạng thái phê duyệt, thời điểm, người đề nghị và người phê duyệt; phê duyệt nhiều cấp có thứ tự.
    - Quan hệ tới cấu kiện: qua quan hệ gán chung (`IfcRelAssignsToControl`, `IfcRelAssignsToProduct`); mục mô tả `IfcActionRequest` chỉ nêu gán tác nhân, không nêu gán cấu kiện.
    - Lịch sử: `Status` chỉ là giá trị hiện tại; `IfcOwnerHistory` ghi rõ chỉ lưu lần sửa cuối. Không có lịch sử chuyển trạng thái.
    - Dữ liệu quan trắc: `IfcPerformanceHistory` ghi dữ liệu đo theo thời gian từ hệ tự động hóa tòa nhà, gán cho sản phẩm, nhóm, quá trình (ví dụ sự kiện cảnh báo được nêu và xác nhận). `IfcRelAssignsToControl` loại trừ việc gán một điều khiển cho một điều khiển khác, và cả yêu cầu lẫn lịch sử hiệu năng đều là lớp con của `IfcControl`. [NCS] Vì vậy không có quan hệ định kiểu từ yêu cầu hay lệnh công việc về dữ liệu quan trắc làm căn cứ.
    - **Kết quả:** IFC4 **đã giải quyết** phần "yêu cầu, lệnh bảo trì, nhiệm vụ có trạng thái, phê duyệt có người và thời điểm". **Không có**: lịch sử chuyển trạng thái, khái niệm bằng chứng tình trạng và phạm vi hiệu lực, quan hệ định kiểu từ hành động về căn cứ quan trắc.
  - COBie 2.4 (NBIMS-US V3, chương 4.2; số trang theo tệp của NIBS): **đã kiểm 30/09/2026**.
    - Bảng Job: công việc vận hành, bảo trì, kiểm tra gắn với **loại** thiết bị (`Job.TypeName`), không gắn cấu kiện cụ thể; `Job.Status` mặc định "Not Yet Started", "Started", "Completed"; `Job.Category` có "Inspection" (tr. 39–40, 113). Có `CreatedBy`, `CreatedOn` (tr. 228).
    - Bảng Issue: vấn đề tham chiếu tới một hay hai dòng của bảng khác (nên gắn được cấu kiện); có loại, rủi ro, khả năng, tác động, người phụ trách, biện pháp giảm thiểu (tr. 44–45); **không có trường trạng thái**. Bảng Issue nằm ngoài phạm vi bắt buộc của trao đổi cho quản lý cơ sở vật chất (tr. 229).
    - **Kết quả:** COBie có trạng thái công việc ở mức loại thiết bị và vấn đề gắn đối tượng; không có lịch sử, không có căn cứ quan trắc. Là định dạng bàn giao, không phải hồ sơ vận hành.
  - [44] García 2026: **đã kiểm 30/09/2026** (đọc toàn văn). Bước chuyển trạng thái có gói bằng chứng, bản ghi quyết định, vai trò tách biệt và vòng NCR/BCF (tr. 3, 12, 19–25). Đây là **tiền lệ trực tiếp** của khuôn "bước chuyển có căn cứ và đúng thẩm quyền", áp cho tệp IFC bàn giao; không có bằng chứng tình trạng công trình.
  - [35] Bellon 2025 (*Autom. Constr.* 174: 106157): **đã kiểm 01/10/2026**, đọc toàn văn (tr. 1–18).
    - *Chuỗi định kiểu bằng thực thể chuẩn IFC 4.3 ADD2, không mở rộng* (tr. 3, 5–7, Hình 4): lần kiểm tra là `IfcTask` loại `INSPECTION`; hư hỏng là `IfcSurfaceFeature` loại `DEFECT`, là **sản phẩm** của lần kiểm tra qua `IfcRelAssignsToProduct`; hư hỏng gắn **một** cấu kiện qua `IfcRelAdheresToElement`; hư hỏng gán cho nhiệm vụ bảo trì cấp hư hỏng qua `IfcRelAssignsToProcess`; nhiệm vụ cấp hoạt động gắn khoản chi phí `IfcCostItem` qua `IfcRelAssignsToControl`; tài liệu gắn lần kiểm tra qua `IfcRelAssociatesDocument`.
    - *Kiểm chứng:* tệp đạt cả bốn nhóm kiểm của dịch vụ kiểm IFC của buildingSMART (tr. 10, 14, Hình 15); ca cầu thật với 10 hư hỏng từ cơ sở dữ liệu DNIT; truy ngược từ hư hỏng tới lần kiểm tra và nhiệm vụ bảo trì xem được trên KITModelViewer và usBIM.browser (tr. 17, Hình 17, 20).
    - *Trạng thái:* chỉ có trạng thái của **hư hỏng** theo quy ước `ACTIVE`/`OUTDATED`/`REPAIRED`, ghi trong thuộc tính; "đã sửa" được gán cho mọi hư hỏng báo trước một lần bảo trì; tác giả ghi là đơn giản hóa (tr. 9–10). Nhiệm vụ bảo trì không có trạng thái; không có sự kiện chuyển trạng thái, phê duyệt hay vai trò ngoài người kiểm tra (`IfcRelAssignsToActor`, tr. 9). [NCS] Các điểm "không có" là nhận định từ việc bài không nêu.
    - *Nguồn của phát hiện:* kiểm tra bằng mắt; không có cảm biến, NDT, độ bất định hay phạm vi hiệu lực. Tác giả tự nêu tích hợp IoT, song sinh số và hệ quản lý cơ sở vật chất thật là việc sau (tr. 1, 18).
    - **Kết quả đối chiếu:** [35] **đã giải quyết** phần "quan hệ định kiểu nối hành động bảo trì về phát hiện tình trạng và về lần kiểm tra đã tạo ra phát hiện", cho phát hiện bằng mắt, bằng thực thể IFC chuẩn. **Không có:** bằng chứng cảm biến hoặc NDT có nguồn gốc và phạm vi hiệu lực; trạng thái và lịch sử chuyển trạng thái của hành động; căn cứ và thẩm quyền của bước chuyển; kiểm tra xác minh sau sửa.
- **Phát biểu đã thu hẹp (sau khi kiểm BCF 3.0, IFC4, COBie 2.4, [44], [35]; còn chờ CMMS; ISO 19650-3 không truy cập được):** yêu cầu, lệnh bảo trì, vấn đề gắn cấu kiện, trạng thái, phê duyệt và lịch sử đổi trạng thái đều đã có chuẩn biểu diễn (IFC4, BCF 3.0, COBie); chuỗi định kiểu lần kiểm tra → phát hiện bằng mắt → cấu kiện → nhiệm vụ bảo trì → chi phí đã được biểu diễn bằng thực thể chuẩn IFC 4.3 [35]; và khuôn "bước chuyển có bằng chứng và đúng thẩm quyền" đã được thử cho gói thông tin bàn giao [44]. Phần chưa thấy ở các nguồn đã kiểm là: (i) bằng chứng tình trạng có nguồn gốc và phạm vi hiệu lực, gồm bằng chứng từ cảm biến và kiểm tra không phá hủy, đi vào cùng chuỗi đó; (ii) từng lần đổi trạng thái của **hành động** được ghi thành sự kiện có căn cứ trỏ về bằng chứng đã dùng và có thẩm quyền của người thực hiện.
- **Căn cứ bổ sung (01/10/2026, T1-2):** Hemker và cs. 2019 [22], tr. 192 (tác giả tự nêu nhu cầu hồ sơ hư hỏng đầy đủ, cập nhật liên tục để khắc phục đúng thứ tự ưu tiên và theo dõi giai đoạn, tiến độ khắc phục; không có mô hình), tr. 189 (lưu đồ kiểm tra – khắc phục và ba cấp kiểm tra theo trình độ). Đây là căn cứ về **nhu cầu** từ thực hành nhà công nghiệp thép, không phải căn cứ rằng các hệ hiện có không đáp ứng; tính là căn cứ độc lập thứ ba trước 2025 với mức "TG, gián tiếp". CẦN NCS KIỂM cách tính này.
- **Căn cứ bổ sung (01/10/2026, T1-1):** [35] tr. 1, 18 (tác giả tự nêu: tích hợp IoT và song sinh số, áp dụng với hệ quản lý cơ sở vật chất thật là việc sau; TG). Tài liệu 2025, không tính vào ngưỡng ba căn cứ trước 2025.
- **Căn cứ bổ sung (30/09/2026, T1-1):** [44] tr. 3–4, 23 (tác giả tự nêu khoảng đứt giữa bàn giao và quản lý trong vận hành), tr. 34 (gắn với quản lý vận hành là việc để lại). Tài liệu 2026, không tính vào ngưỡng ba căn cứ trước 2025.

## UV-02 — Nguồn gốc, phiên bản phương pháp, phạm vi hiệu lực của đầu ra phát hiện

- **Phát biểu:** Đầu ra phát hiện bất thường và dự đoán trong các khung song sinh số công trình chưa được ghi như một
  bản ghi có nguồn gốc xử lý, phiên bản phương pháp và phạm vi hiệu lực.
- **Căn cứ:**
  - [3], tr. 5 (Hình 3: dữ liệu thô có Sensor_ID, Sensor_Timestamp), tr. 13–14 (đầu ra là điểm thay đổi và cảnh báo hiển
    thị; không mô tả phiên bản thuật toán, tham số hay điều kiện áp dụng). Đối chiếu ngữ cảnh vận hành để lọc điểm thay
    đổi (tr. 6) là xử lý một phần.
  - [7], tr. 9 (độ tin cậy dữ liệu nguồn là mối quan ngại; cần phân biệt dữ liệu cảm biến thật và mô phỏng; tính hợp lệ
    của dự đoán cần kiểm chứng), tr. 11 (kiểm chứng tính đúng và đủ của dữ liệu còn khó). Tìm trong văn bản: không có
    provenance, traceability, accountability, audit.
- **Căn cứ bổ sung (01/10/2026, T1-4):** Kapoor & Narayanan 2023 [53], tr. 3, 5 (chuẩn báo cáo học máy hiện có, kể cả checklist và thẻ mô hình, không xử lý rò rỉ; người nghiên cứu phải lập luận tường minh về tách tập, đặc trưng và phân bố áp dụng; TG). Çelik và cs. 2023 [16], tr. PDF 14 (tích hợp với thiết bị IoT là việc sau; nguồn gốc mới áp cho dữ liệu thiết kế BIM; TG).
- **Loại căn cứ:** TG ([7] tr. 9, 11; [53] tr. 3, 5; [16] tr. 14) + **NCS** (không có cơ chế ghi nguồn gốc/phạm vi là suy từ phần bài không xử lý).
- **Liên quan:** K1.
- **Ghi chú:** cần đối chiếu với [18], [45], Figueiredo 2011 (Tier 2) về phạm vi hiệu lực phụ thuộc điều kiện huấn luyện.
- **Phản chứng đã kiểm:**
  - [44] García 2026: đã kiểm. Có nguồn gốc của **tệp** bàn giao (phiên bản, tác giả, phần mềm xuất, mã băm; tr. 17–20) và đường cơ sở yêu cầu có phiên bản (tr. 25–27); không có nguồn gốc của kết quả phân tích dữ liệu đo.
  - SSN/SOSA (Khuyến nghị W3C 19/10/2017): kiểm một phần. `sosa:Observation` có cảm biến tạo ra, thủ tục đã dùng, thời điểm hiện tượng và thời điểm kết quả (mục 4.3); phần căn chỉnh với PROV-O có sẵn (mục 6.5). Chưa kiểm cách ghi phiên bản thuật toán và phạm vi áp dụng.
  - [16] Çelik 2023: **đã kiểm 01/10/2026** (toàn văn, bản in thử). Có bản ghi nguồn gốc ở mức đối tượng IFC: thao tác, thời điểm, mô hình, phiên bản, định danh đối tượng, chủ sở hữu; hợp đồng kiểm tra ai tạo/sửa đối tượng nào, khi nào, phiên bản nào (tr. PDF 8, 11–12). Không có phạm vi hiệu lực; không áp cho dữ liệu đo.
  - [53] Kapoor & Narayanan 2023: **đã kiểm 01/10/2026**. Phiếu thông tin mô hình (21 câu hỏi) ghi lập luận về tách tập, đặc trưng hợp lệ, phân bố áp dụng (tr. 5–6), có phiên bản; ở mức mô hình trong một bài báo, không gắn từng kết quả được dùng về sau. Phụ lục chứa mẫu phiếu chưa đọc.
  - Thẻ mô hình (model cards, Mitchell và cs. 2019, được [53] dẫn): **chưa kiểm**; tài liệu chưa có trong Zotero, không được trích khi chưa nhập.
  - PROV-O [69], công cụ quản lý phiên bản mô hình (MLflow/DVC): **chưa kiểm**.
- **Phát biểu đã thu hẹp (đề xuất, chờ kiểm PROV-O, MLflow/DVC, thẻ mô hình):** nguồn gốc ở mức đối tượng hay tệp ([16], [44]) và lập luận về phạm vi ở mức mô hình ([53]) đã có tiền lệ; phần chưa thấy là một bản ghi cho **từng** kết quả sinh từ dữ liệu đo, mang cùng lúc nguồn gốc xử lý, phiên bản phương pháp và phạm vi hiệu lực, và đi theo kết quả đó khi nó được dùng về sau.
- **Căn cứ bổ sung về nội dung phạm vi hiệu lực (01/10/2026, căn cứ 5.6A và T2-1):** các nguồn sau cho thấy đầu ra phát hiện chỉ có nghĩa trong điều kiện của dữ liệu tham chiếu, tức là phạm vi hiệu lực là **cần**; chúng **không** nói gì về việc ghi hay không ghi phạm vi, nên không tính vào số căn cứ của phát biểu "chưa được ghi".
  - Figueiredo và cs. 2011 `23TBQTIP`, tr. 571 (không bảo đảm hiệu quả với điều kiện chưa có trong huấn luyện; TG); tr. 569–570 (ngưỡng và thuật toán là một điểm đánh đổi báo động giả – bỏ sót; TG).
  - Sohn 2007 [45], tr. 553 (sai số AANN tăng với bất kỳ tín hiệu chưa ghi vào mạng, không riêng hư hỏng; TG), tr. 548 (chuẩn hóa là riêng từng công trình; TG), tr. 557 (dữ liệu huấn luyện phải phủ dải rộng điều kiện; TG).
  - Worden và cs. 2007 `MCNRW6F5`, tr. 1642–1647 (mọi phát hiện là so sánh với đường cơ sở; đường cơ sở dịch chuyển gây báo sai; TG).
  - Cawley 2018 `EBB69J4F`, tr. 13–15 (cần POD và tỉ lệ báo động giả kiểm chứng trong điều kiện vận hành; TG).
  - Wang & Cha 2021 `TDRPDWJE`, bản thảo tác giả tr. 2, 20 (mỗi công trình có điều kiện biên và vật liệu riêng; TG), tr. 21 (định vị, định lượng khó khi huấn luyện thiếu thông tin hư hỏng; TG).
- **Số căn cứ độc lập:** 4 ([3] 2020, [7] 2020, [53] 2023, [16] 2023); trước 2025: 4.

## UV-03 — Ghép cảm biến – cấu kiện có thời hạn

- **Phát biểu:** Việc gắn dữ liệu cảm biến với đối tượng BIM, khi có, được thực hiện bằng bảng ghép hoặc tương đương
  mà không có thời hạn hiệu lực và lịch sử thay đổi ghép.
- **Căn cứ:**
  - [7], tr. 7 (các nghiên cứu cảm biến trong xây dựng **không xử lý việc căn chỉnh dữ liệu cảm biến với chính mô hình BIM**),
    tr. 2 (dữ liệu từ nhiều nguồn phải được đối chiếu với BIM ở mức đối tượng và nhất quán theo thời gian).
  - [3], tr. 6, 10 (Hình 7, 11: bảng ghép GUID ↔ ID nguồn dữ liệu; chỉ bảng ghép cần bảo trì); không nêu thời hạn hiệu
    lực hoặc cách xử lý khi cảm biến được thay hay dời.
- **Loại căn cứ:** TG ([7] tr. 7 tự nêu chưa giải quyết) + **NCS** (không thời hạn hiệu lực là suy từ [3]).
- **Liên quan:** K2.
- **Căn cứ bổ sung (30/09/2026):** Theiler & Smarsly 2018 [2], tr. 58–60, 63 (quan hệ tĩnh, không thuộc tính thời gian; NCS), tr. 64 (động lực học của hệ quan trắc chưa mô tả được; TG).
- **Ghi chú:** [3] là **tiền lệ** cho việc ghép; điểm còn thiếu là thời hạn và lịch sử. Đã đối chiếu [2] (IFC Monitor)
  và [35] ở phiên T1-1 (xem phản chứng).
- **Phản chứng đã kiểm:**
  - [3] Lu 2020: đã kiểm. Có bảng ghép GUID ↔ ID nguồn dữ liệu (tr. 6, 10); không có thời hạn hiệu lực hay lịch sử thay đổi ghép.
  - [2] IFC Monitor (Theiler & Smarsly 2018, *Adv. Eng. Inform.* 37: 54–65): **đã kiểm 30/09/2026**, đọc toàn văn thân bài (tr. 54–64).
    - Quan hệ cảm biến – cấu kiện: nút cảm biến (`IfcSensorNode`) được tham chiếu ngữ nghĩa tới cấu kiện bằng `IfcRelAssignsToProduct`; mạng cảm biến nối với phần tử không gian (tầng) bằng `IfcRelServicesBuildings` (tr. 56, 59, 63; Listing 4).
    - Thời hạn hiệu lực: **không xử lý**. Ba thực thể mới (`IfcSensorNode`, `IfcSensorNetwork`, `IfcSHMSystem`) và kiểu liệt kê cấu trúc mạng không có thuộc tính thời gian; các quan hệ dùng lại của IFC được mô tả như quan hệ tĩnh (tr. 58–60, Hình 4, Listing 1). Tìm trong văn bản không có thuộc tính ngày lắp, ngày gỡ hay khoảng hiệu lực. [NCS] nhận định từ việc bài không nêu.
    - Bài đặt mục tiêu hỗ trợ lập hồ sơ và theo dõi thay đổi của hệ quan trắc trong vòng đời vận hành (tr. 55) nhưng không trình bày cơ chế; ca kiểm chứng là một hệ mẫu trên khung nhôm bốn tầng trong phòng thí nghiệm, mô hình hóa tại một thời điểm (tr. 61–63).
    - Tác giả tự nêu: động lực học của hệ quan trắc chưa mô tả được đầy đủ bằng các cách mô hình hóa trên nền IFC hiện có, để cho công việc sau (tr. 64).
    - **Kết quả đối chiếu:** [2] giải quyết phần "biểu diễn quan hệ cảm biến – cấu kiện trong IFC"; **không** giải quyết thời hạn hiệu lực và lịch sử thay đổi ghép. Có một căn cứ tác giả tự nêu (tr. 64).
  - IFC4 (tài liệu IFC4 ADD2 TC1 của buildingSMART): **đã kiểm 30/09/2026**. `IfcOwnerHistory` ghi người và ứng dụng sở hữu, ngày tạo, và **chỉ lần sửa cuối** (mô tả thuộc tính `OwnerHistory` của `IfcRoot` ghi rõ chỉ lưu lần sửa cuối); không có khoảng hiệu lực. `IfcRelAssigns` và các lớp con là liên kết hai chiều giữa các đối tượng, không có thuộc tính thời gian. `IfcRelAssignsToProduct` gán đối tượng cho sản phẩm; các tên dùng được gợi ý là 'Context' và 'View'. **Kết quả:** IFC4 không biểu diễn khoảng hiệu lực hay lịch sử của quan hệ cảm biến – cấu kiện.
  - SSN/SOSA [61]–[62] (Khuyến nghị W3C "Semantic Sensor Network Ontology", 19/10/2017, dẫn theo số mục): **đã kiểm 30/09/2026**.
    - `ssn:Deployment` mô tả việc triển khai một hay nhiều hệ cho một mục đích, có thể trên một nền tảng; ví dụ của đặc tả là cảm biến nhiệt gắn trên tường (mục 4.9.2.6). Quan hệ: `ssn:deployedSystem`, `ssn:deployedOnPlatform`, `ssn:forProperty`; thêm `sosa:hosts`/`sosa:isHostedBy` giữa nền tảng và cảm biến.
    - Thời gian triển khai: phần quy định của `ssn:Deployment` **không có thuộc tính thời gian**. Ví dụ B.11 (không quy định) gắn `prov:startedAtTime` vào một lần triển khai; các ví dụ khác dùng khoảng thời gian OWL-Time cho quan trắc. Vậy "cảm biến lắp trên cấu kiện X trong khoảng T" **biểu diễn được** bằng cách ghép SSN với PROV-O hoặc OWL-Time, nhưng đặc tả không chuẩn hóa cách ghép.
    - Thời gian quan trắc: `sosa:phenomenonTime`, `sosa:resultTime` (mục 4.3.2).
    - Ràng buộc: [NCS] đặc tả không có tiên đề hay luật nào kiểm thời điểm quan trắc nằm trong khoảng triển khai; đây là nhận định từ việc đặc tả không nêu.
    - **Kết quả:** SSN **đã có** khái niệm tương ứng với ánh xạ cảm biến – cấu kiện có thời hạn (Deployment trên Platform), là tiền lệ trực tiếp. Phần chưa có: thuộc tính thời gian được quy định, và ràng buộc nhất quán thời gian.
  - [35] Bellon 2025: **đã kiểm 01/10/2026** (toàn văn). Không có cảm biến hay quan hệ cảm biến – cấu kiện. Quan hệ hư hỏng – cấu kiện (`IfcRelAdheresToElement`) là quan hệ phân cấp tĩnh, mỗi hư hỏng một cấu kiện, không có thuộc tính thời gian (tr. 5). Mỗi lần sửa tệp tạo một `IfcOwnerHistory` mới (tr. 9), tức chỉ ghi lần sửa, không ghi khoảng hiệu lực của quan hệ. **Kết quả:** không xử lý UV-03; không đổi phát biểu đã thu hẹp.
- **Phát biểu đã thu hẹp (sau khi kiểm [2], [3], IFC4, SSN/SOSA, [35]; mọi phản chứng đã liệt kê đều đã kiểm):** quan hệ cảm biến – cấu kiện đã biểu diễn được trong IFC (IFC Monitor, bảng ghép GUID – ID), và khái niệm triển khai cảm biến trên nền tảng đã có trong SSN, ghép được với thời gian của PROV-O hoặc OWL-Time. Phần chưa có là một cách ghép được quy định giữa hai phía (cấu kiện IFC làm nền tảng, khoảng hiệu lực bắt buộc, lịch sử lắp – dời – thay – hiệu chuẩn) cùng ràng buộc kiểm thời điểm quan trắc nằm trong khoảng hiệu lực của ánh xạ.
- **[NCS] Đánh giá:** sau khi trừ tiền lệ, phần còn lại là một hồ sơ áp dụng (profile) và một ràng buộc, quy mô nhỏ. Nên coi UV-03 là một yêu cầu của mô hình dữ liệu (ràng buộc C3) hơn là một khoảng trống độc lập; [35] đã đọc (01/10/2026): không xử lý cảm biến, đánh giá này giữ nguyên.

## UV-04 — Định vị mức tích hợp DM/DS/DT cho kiểm tra – bảo trì

- **Phát biểu:** Chưa có phân loại mức tích hợp DM/DS/DT gắn với các khung có con người ra quyết định cho kiểm tra –
  bảo trì kết cấu công trình.
- **Căn cứ:**
  - Kritzinger và cs. 2018 [8], tr. 1020 (chưa có định nghĩa chung; cần mô hình tham chiếu theo lĩnh vực và các ca nghiên
    cứu); phạm vi bài là sản xuất (tr. 1018).
  - [7], tr. 12–13 (thang ba thế hệ cho song sinh số xây dựng, thế hệ 2 có xác nhận của người dùng).
- **Loại căn cứ:** TG ([8] tr. 1020) + **NCS** (việc chưa có phân loại cho kiểm tra – bảo trì kết cấu là suy từ phạm vi hai bài).
- **Liên quan:** mới, chỉ phục vụ **định vị** (mục 2.3 và câu khai báo mức DS ở Dẫn nhập). **[NCS]** Không nên phát triển
  thành khoảng trống của luận án: đây là câu hỏi khái niệm, không phải điều luận án kiểm chứng.
- **Phản chứng đã kiểm:** **chưa kiểm**. Cần đối chiếu [10] Chen 2021 (mô hình trưởng thành theo Gemini Principles) và Sepasgozar 2021 [9].
- **Phát biểu đã thu hẹp:** chưa có; ứng viên chỉ dùng để định vị.

## UV-05 — Thiếu nhãn hư hỏng ở hiện trường

- **Phát biểu:** Ở công trình đang vận hành, khó có dữ liệu có nhãn về bất thường; phân biệt bình thường – bất thường phụ
  thuộc nhiều vào đánh giá của con người, nên nhãn cần đến từ kiểm tra.
- **Căn cứ:** [3], tr. 2 (dữ liệu có nhãn tốt thường không sẵn có ở môi trường xây dựng), tr. 3 (khó phân biệt điều
  kiện bình thường và bất thường, hiện phụ thuộc đánh giá của con người), tr. 13 (huấn luyện bộ phân loại một lớp cần dữ
  liệu lớn ở nhiều điều kiện bình thường, không thực tế).
- **Loại căn cứ:** TG.
- **Liên quan:** mới (nhãn hiện trường, vòng lặp kiểm tra tạo nhãn). Trong GD1 đây là luận điểm L2.3 ("thiếu dữ liệu hư
  hỏng có nhãn ở hiện trường"), đã có nguồn ở 5.6A (Bull 2022, Wang & Cha 2021, [57]) mà chưa đưa vào nhật ký này.
- **Căn cứ bổ sung (01/10/2026, T1-2):** Ramasso và cs. 2025 [19] (bản tiền in arXiv), tr. 15 (thêm dần nhãn của đợt kiểm tra để mô phỏng việc các đợt kiểm tra định kỳ cho phép gán nhãn dữ liệu đã thu; độ chính xác tăng theo lượng nhãn), tr. 14, 21 (nhãn đặt bằng cờ-lê lực có bất định; tác giả tự nêu). Loại: TG. Tài liệu nhóm 2025.
- **Căn cứ bổ sung (01/10/2026, T1-4):** Wu và cs. 2026 [17], tr. 4 (gán nhãn tương tác và học chủ động để bù việc thiếu dữ liệu có nhãn, đưa tri thức chuyên gia vào xác nhận; TG), tr. 10 (LFW1: cải thiện mô hình khi phản hồi ít là giới hạn; TG). Tài liệu 2026; đối tượng là kiểm kê tái sử dụng.
- **Ghi chú:** đối tượng của [3] là bơm HVAC; chỉ dùng như căn cứ cùng chiều.
- **Căn cứ bổ sung (01/10/2026, căn cứ 5.6A, dựa trên `notes/`):**
  - Bull và cs. 2022 `87NKU5IS`, tr. 3–4 (học không giám sát chỉ cho phát hiện điểm mới; định vị, phân loại, đánh giá cần nhãn; TG), tr. 1–2 (kiểm tra của chuyên gia tốn kém, dùng để gán nhãn; TG), tr. 4 (không thể kiểm tra lại trạng thái ở thời điểm đã qua; TG).
  - Hughes và cs. 2022 `Z9RD5DMZ` (tiền in arXiv v2), tr. 1–2, 7 (hỏi nhãn = kiểm tra; nhãn do kỹ sư cung cấp; TG).
  - Wang & Cha 2021 `TDRPDWJE` (bản thảo tác giả), tr. 2, 20 (khó thu đủ dữ liệu hư hỏng của công trình; TG).
  - Worden và cs. 2007 `MCNRW6F5`, tr. 1647–1651 (tiên đề III: loại và mức độ hư hỏng cần học có giám sát; TG).
  - [57] Bull 2021 `W7AEKRT8`, tr. 1, 3 (một công trình riêng lẻ hiếm có dữ liệu và nhãn phủ đủ điều kiện; TG), tr. 11, 15 (nhãn đường cong công suất gán "phần nào chủ quan" theo phán đoán kỹ thuật; TG). Đọc toàn văn T2-2 (01/10/2026). Cùng nhóm Sheffield – Los Alamos, không tăng số căn cứ độc lập.
- **Số căn cứ độc lập (quy ước nhóm tác giả):** [3] 2020; nhóm Sheffield – Los Alamos (Bull 2022, Hughes 2022, Worden 2007) tính một; Wang & Cha 2021; [19] 2025; [17] 2026. Trước 2025: 3.
- **Phản chứng đã kiểm:**
  - Hughes 2022 `Z9RD5DMZ` (học chủ động theo rủi ro): **đã kiểm 01/10/2026** theo ghi chú có sẵn (đọc mục 1–4, 6–8). Đã đề xuất cơ chế lấy nhãn bằng kiểm tra có chọn lọc theo giá trị thông tin cho quyết định (tr. 1, 7). Giới hạn tác giả tự nêu: biết trước số lớp, giả định kiểm tra cho thông tin hoàn hảo, quyết định nhị phân (tr. 27–28). Dữ liệu cầu Z24 với nhãn định sẵn.
  - Bull 2022 `87NKU5IS` (quản lý kiểm tra theo lý thuyết thông tin): **đã kiểm 01/10/2026** theo ghi chú có sẵn (đọc mục 1, 2, 7, 8; lướt 3–6). Đề xuất truy vấn kiểm tra cho các phép đo giàu thông tin, thêm lớp mới khi kiểm tra phát hiện (tr. 1–2). Nhãn trong ví dụ hiện trường lấy theo quy ước nghiên cứu trước (tr. 15).
  - [57] Bull 2021 `W7AEKRT8`: **đã kiểm 01/10/2026 (toàn văn)** — giải quyết một phần: nêu việc thiếu nhãn và giảm nhu cầu nhãn bằng cách chuyển mô hình trạng thái bình thường giữa các thành viên quần thể (tr. 1, 3, 11). Không có: nhãn từ kiểm tra thực, độ bất định của nhãn, người gán nhãn. Phát biểu thu hẹp giữ nguyên.
  - [56] Da Silva 2024 `IW7JBB3E`: **đã kiểm 01/10/2026 (toàn văn)** — giải quyết một phần phát biểu gốc (chuyển giao nhãn từ kết cấu nguồn có nhãn bằng thích nghi miền, tr. 011102-1, -5); không giải quyết phát biểu thu hẹp: nhãn đặt bằng cờ-lê lực trong PTN, nhãn đích đã biết và dùng để đánh giá.
  - SHM theo quần thể phần III (Gardner 2021): **chưa kiểm** (chưa có trong Zotero).
- **Phát biểu đã thu hẹp (đề xuất; [57], [56] đã kiểm, còn Gardner 2021):** việc thiếu nhãn ở hiện trường và việc lấy nhãn bằng kiểm tra có chọn lọc đã được nêu và mô hình hóa (Bull 2022, Hughes 2022), trên dữ liệu cầu với nhãn giả định và giả định kiểm tra hoàn hảo. Phần chưa thấy: nhãn sinh từ kiểm tra thực ở công trình đang vận hành, mang độ bất định của kiểm tra, được ghi như một bản ghi gắn với phép đo đã kích hoạt kiểm tra và với cấu kiện. [NCS] Phần này gần với UV-07 và K3; khi chốt ở GĐ3 có thể gộp.

## UV-06 — Lần lắp ráp hoặc can thiệp bảo trì là ranh giới phạm vi hiệu lực của bằng chứng từ mối nối bu lông

- **Phát biểu:** Với kết cấu có mối nối bu lông, kết quả rút ra từ dữ liệu dao động hoặc phát xạ âm phụ thuộc lần lắp ráp (bề mặt tiếp xúc, thứ tự siết, mài mòn tích lũy); sau một lần tháo – lắp hay siết lại, bằng chứng và dữ liệu tham chiếu trước đó không còn đương nhiên dùng được, nhưng các nghiên cứu không biến điều này thành ranh giới được ghi của phạm vi hiệu lực.
- **Căn cứ:**
  - Brake và cs. 2019 [18], tr. 283 (sau mỗi lần lắp lại khi bảo trì, phần lớn dữ liệu đáp ứng đã thu mất tác dụng cho theo dõi trạng thái; TG), tr. 292 (kết quả phụ thuộc quy trình lắp ráp; TG), tr. 293 (mài mòn làm tần số giảm vĩnh viễn; TG), tr. 302–303 (tính chất mối nối phụ thuộc kết cấu xung quanh; TG).
  - Ramasso và cs. 2025 [19] (tiền in), tr. 4–5, 20 (mỗi đợt sau tháo – lắp là một hệ mới; TG), tr. 2, 12–14 (đánh giá cùng đợt cho kết quả lạc quan; độ chính xác giảm mạnh khi kiểm tra trên đợt chưa thấy; TG).
  - Da Silva và cs. 2024 [56], tr. 011102-1 ("tend to fail when used in other similar bolted structures"), tr. 011102-4 (bộ phân loại học trên Dầm #2 "fails to classify" dữ liệu Dầm #1 trong không gian đặc trưng gốc), Hình 8 tr. 011102-7; TG. **Đã đọc toàn văn T2-2 (01/10/2026), sửa trang.** Lưu ý: thất bại xảy ra giữa **hai mẫu dầm** (khác do chế tạo, mài mòn; tr. -3, -7–8), không phải giữa hai lần lắp của cùng một dầm; tám đợt tháo – lắp của mỗi dầm bị gộp vào một miền (tr. -3). Với ý "lần lắp ráp" đây là căn cứ **gián tiếp**.
  - Pal và cs. 2022 [48], tr. 9–10: ca UD-C (siết lại toàn bộ sau các ca lỏng) được xếp đúng vào lớp siết chặt 60/60 — **dữ liệu ngược chiều một phần**: một lần siết lại không làm mất hiệu lực của bộ phân loại trong ca này (cùng khung, PTN, siết bằng tay). [NCS] Khi chốt ở GĐ3, viết theo hướng "lần lắp ráp – can thiệp phải được ghi để kiểm được hiệu lực", không viết "luôn làm mất hiệu lực".
  - Kapoor & Narayanan 2023 [53], tr. 4–5 (L3.2: đơn vị chung giữa tập huấn luyện và kiểm tra là rò rỉ, trừ khi khẳng định hướng tới phân bố có cùng cấu trúc phụ thuộc; L3.3: kiểm tra phải lấy từ phân bố mà khẳng định hướng tới; TG, căn cứ phương pháp chung, không riêng mối nối bu lông).
  - Hemker và cs. 2019 [22], tr. 191 (một thay đổi nhỏ ở dầm cầu trục làm đánh giá mỏi ban đầu mất giá trị; [NCS] tương tự về ý, khác loại bằng chứng). Không tính vào số căn cứ.
- **Loại căn cứ:** TG về hiện tượng vật lý ([18], [19], [56]); [NCS] về việc chưa được ghi thành ranh giới phạm vi hiệu lực.
- **Liên quan:** K1 (phạm vi hiệu lực: đợt lắp đặt, đơn vị suy luận). Gần với UV-02; tách riêng vì UV-02 nói về việc **ghi** nguồn gốc và phạm vi, còn UV-06 nói về **nội dung** của phạm vi (lần lắp ráp, can thiệp).
- **Ghi chú T2-1 (01/10/2026):** Figueiredo 2011 `23TBQTIP` xếp giảm độ cứng cột vào nhóm "chưa hư hỏng" để mô phỏng biến động vận hành – môi trường, còn hư hỏng là phi tuyến va chạm (tr. 565, Bảng 1). [NCS] Một suy giảm liên kết chỉ làm giảm độ cứng (không va đập) vì vậy dễ bị coi là biến động bình thường; điều này củng cố việc phải ghi trạng thái lắp ráp và can thiệp vào phạm vi hiệu lực. Không tính là căn cứ.
- **Số căn cứ độc lập:** 4 ([18] 2019, [53] 2023 (phương pháp chung), [56] 2024 gián tiếp, [19] 2025); trước 2025: 3, trong đó [56] là gián tiếp (giữa các mẫu kết cấu, không giữa các lần lắp). Có một dữ liệu ngược chiều một phần ([48]).
- **Phản chứng đã kiểm:** **một phần** (cập nhật 01/10/2026: đã kiểm Cross 2011, [57], [56], [48] — đều không giải quyết; còn **chưa kiểm**: phần III Gardner 2021, nghiên cứu theo dõi dài hạn sau bảo trì). Danh sách ban đầu: SHM theo quần thể [57] Bull 2021 và phần III (Gardner 2021), thích nghi miền [56]; bù EOV và đồng liên kết (Cross 2011); phát hiện thay đổi đường cơ sở sau bảo trì trong các nghiên cứu theo dõi dài hạn.
  - *[57] Bull 2021 `W7AEKRT8` — đã kiểm 01/10/2026 (toàn văn):* không giải quyết. Thay đổi do người vận hành can thiệp hay bảo trì được đưa vào mô hình trạng thái bình thường (tr. 11, 17), không coi lần can thiệp là ranh giới phạm vi hiệu lực.
  - *[56] Da Silva 2024 `IW7JBB3E` — đã kiểm 01/10/2026 (toàn văn):* không giải quyết; thích nghi miền xử lý khác biệt giữa các kết cấu, các đợt tháo – lắp bị gộp vào miền, không được ghi thành ranh giới.
  - *[48] Pal 2022 `SL6IEB2E` — đã kiểm 01/10/2026 (toàn văn):* không giải quyết; có dữ liệu ngược chiều một phần (xem Căn cứ).
  - *Cross 2011 `KPWFC4PI` — đã kiểm 01/10/2026 (toàn văn):* không giải quyết. Bài chỉ yêu cầu tập huấn luyện là trạng thái bình thường (tr. 2728), không bàn lần lắp ráp hay can thiệp. Theo tr. 2715, mọi sự kiện đổi quan hệ giữa các biến đều làm phần dư mất tính dừng; [NCS] một lần siết lại cũng có thể làm vậy, nên sau can thiệp phải ghi sự kiện và lập lại tập huấn luyện — củng cố UV-06, không tính là căn cứ. Các mục còn lại vẫn **chưa kiểm**.
- **Phát biểu đã thu hẹp:** chưa có; chờ kết quả kiểm.

## UV-07 — Xác nhận của chuyên gia đối với đầu ra AI được dùng làm tín hiệu học, chưa được ghi như bản ghi trách nhiệm

- **Phát biểu:** Trong các khung người – AI đã đọc, chuyên gia xác nhận hay sửa đầu ra của mô hình, nhưng lần xác nhận đó được dùng làm nhãn hoặc phản hồi để học lại, hoặc chỉ là một bước quy trình; chưa thấy nó được ghi như một bản ghi có vai trò, thẩm quyền, thời điểm và căn cứ, gắn với đầu ra đã được xác nhận.
- **Căn cứ:**
  - Wu và cs. 2026 [17], tr. 6–7 (điểm rà soát cuối trước khi dùng cho bước sau; phản hồi của người tinh chỉnh mô hình), tr. 9 (cơ sở dữ liệu giữ dự đoán ban đầu và đã sửa); không có ghi vai trò, thẩm quyền ([NCS]).
  - Boje và cs. 2020 [7], tr. 12 (thế hệ 2 cần người dùng xác nhận và cho phép; không nêu cách ghi; TG + [NCS]).
  - Hughes và cs. 2022 `Z9RD5DMZ` (tiền in arXiv v2), tr. 2, 7 (hỏi nhãn được ánh xạ thành việc kiểm tra; nhãn là thông tin do kỹ sư cung cấp), tr. 27–28 (giả định kiểm tra cho thông tin hoàn hảo trong khi kiểm tra có thể có sai sót của con người; TG).
  - Lu và cs. 2020 [3], tr. 4, 13 (người quản lý FM là người quyết định, quy trình DT không có bước ghi quyết định; [NCS]).
- **Loại căn cứ:** TG ([7] tr. 12; Hughes tr. 27–28) + **NCS** (việc không ghi thành bản ghi trách nhiệm là suy từ phần bài không mô tả).
- **Liên quan:** K3, và nguyên tắc "AI tạo bằng chứng, con người quyết định" của 5.6A. Gần UV-01 (chuỗi hành động); tách riêng vì UV-07 nói về **lần xác nhận đầu ra AI**, còn UV-01 nói về **hành động bảo trì và trạng thái của nó**. NCS có thể gộp khi chốt ở GĐ3.
- **Số căn cứ độc lập:** 4 ([3] 2020, [7] 2020, Hughes 2022, [17] 2026); trước 2025: 3.
- **Phản chứng đã kiểm:**
  - IFC4 `IfcApproval` (đã kiểm ở UV-01, 30/09/2026): có trạng thái phê duyệt, thời điểm, người đề nghị và người phê duyệt, gắn được vào mọi đối tượng IFC. [NCS] Về hình thức đã biểu diễn được "ai phê duyệt cái gì, khi nào"; chưa thấy nó được áp cho đầu ra của mô hình học máy.
  - [44] García 2026 (đã kiểm): ký xác nhận theo vai trò, tách nhiệm vụ, cho gói thông tin bàn giao (tr. 21–25).
  - Tài liệu về học máy có người trong vòng (human-in-the-loop) và về thẻ mô hình: **chưa kiểm**.
- **Phát biểu đã thu hẹp:** chưa có; chờ kiểm. Dự kiến: biểu diễn phê duyệt đã có (IFC4, [44]); phần còn thiếu có thể chỉ là việc **áp** khuôn phê duyệt cho đầu ra AI và tách nó khỏi việc dùng làm nhãn.

## UV-08 — Nhiễu vận hành nhà xưởng (cầu trục, máy móc) và phát hiện suy giảm liên kết

- **Phát biểu dự kiến (NCS giao 01/10/2026):** ảnh hưởng của rung vận hành (cầu trục, máy móc) lên phát hiện suy giảm liên kết trong nhà xưởng khung thép chưa được nghiên cứu.
- **Căn cứ (về hiện tượng chung, tác giả nói):**
  - Sohn 2007 [45], tr. 541 (điều kiện vận hành gồm tải môi trường, tốc độ vận hành, tải khối lượng), tr. 543–544 (khác biệt do tải khối lượng vận hành lớn hơn nhiều khác biệt do hư hỏng ở tàu lượn), tr. 548 (chuẩn hóa là riêng từng công trình), tr. 557–558 (cần thử trên công trình thật; điều kiện vận hành bất thường gây hiệu ứng giống hư hỏng). TG.
  - Worden và cs. 2007 `MCNRW6F5`, tr. 1652–1654 (tiên đề IVb). Figueiredo và cs. 2011 `23TBQTIP`, tr. 561–562, 571. TG; cùng nhóm tác giả, tính là một.
  - Cawley 2018 `EBB69J4F`, tr. 4 (tần số dạng thấp nhạy khối lượng, điều kiện biên hơn hư hỏng cục bộ), tr. 9 (trừ đường cơ sở khó trong môi trường công nghiệp), tr. 14–15 (thiếu kiểm chứng trên kết cấu thật trong môi trường vận hành). TG.
- **Căn cứ (về nguồn rung trong nhà máy):** Ju và cs. 2020 `38FMATHE`, tr. 7–11 (rung do cầu trục 15–35 Hz, phụ thuộc vận tốc, gia tốc, độ gồ ghề ray, vị trí). TG về hiện tượng; bài **không** bàn phát hiện hư hỏng (tr. 1–13). Đối tượng là nhà máy công nghệ cao, cầu trục chạy trên sàn.
- **Loại căn cứ:** TG cho hiện tượng EOV chung; **[NCS]** cho việc áp sang nhà xưởng có cầu trục và cho nhận định "chưa được nghiên cứu".
- **Liên quan:** K1 (điều kiện áp dụng, đường cơ sở vận hành, bối cảnh quan trắc gồm trạng thái cầu trục); L2.2 (mục 3.2); WP3 (bù EOV, Autoencoder).
- **Số căn cứ độc lập:** cho hiện tượng EOV chung: 3 nhóm trước 2025 ([45] 2007; Worden 2007 + Figueiredo 2011; Cawley 2018). Cho riêng nhà xưởng có cầu trục: chưa có căn cứ của tác giả nào; chỉ có Ju 2020 (hiện tượng) và nhận định của NCS.
- **Phản chứng đã kiểm (01/10/2026):**
  - *Zotero* (tìm trong tiêu đề và tóm tắt: crane, industrial building, factory, factories, operational vibration, portal frame, industrial steel, warehouse, workshop, operational variab, environmental and operational): không có nghiên cứu SHM nào trên nhà công nghiệp có cầu trục. Có: Ju 2020 (và bản trùng `N4BZUNIL`); Hemker 2019 [22] (bảo trì nhà thép công nghiệp, không SHM); Eraliev và cs. 2022 `VVBGM9EN` (bu lông đế động cơ, xem dưới); các nguồn EOV chung ([45], `9RSPTNJE`, `ESQIRHVE` Keshmiry 2023, `KPWFC4PI` Cross 2011, `L56P7RAF`).
  - *Consensus* (3 truy vấn: "crane-induced vibration structural health monitoring industrial building"; "operational variability damage detection factory steel structure"; "bolt loosening detection under operational vibration steel frame"). Ứng viên phản chứng, **chỉ đọc tóm tắt**, DOI đã xác minh qua Crossref; **chưa nhập Zotero**:

    | Tác giả, năm | Nguồn | DOI | Nội dung theo tóm tắt (1 câu) | Liên quan |
    |---|---|---|---|---|
    | Hu và cs., 2023 | *Int. J. Struct. Stab. Dyn.* 24(19): 2450217 | 10.1142/s0219455424502171 | Nhận dạng hư hỏng dầm cầu trục dưới tải di động bằng biến đổi wavelet thực nghiệm và autoencoder thưa, kiểm chứng bằng thí nghiệm nứt dầm. | Gần nhất: phát hiện hư hỏng khi có tải cầu trục, nhưng là dầm cầu trục, vết nứt, thí nghiệm |
    | Van Wittenberghe và cs., 2024 | *Procedia Struct. Integr.* 57: 95–103 | 10.1016/j.prostr.2024.03.012 | SHM cho chính cầu trục (12,5 t) bằng biến dạng kèm dữ liệu vận hành (vị trí xe con, tải móc) để tính mỏi và phát hiện bất thường. | Dùng dữ liệu vận hành làm bối cảnh; đối tượng là cầu trục, không phải nhà |
    | Li và cs., 2022 | *J. Build. Eng.* 58: 105018 | 10.1016/j.jobe.2022.105018 | Đo hiện trường cho thấy cầu trục xưởng lân cận kích động ở 3,6 Hz trùng tần số riêng của nhà văn phòng, gây cộng hưởng. | Hiện tượng rung do cầu trục, tiện nghi; không phát hiện hư hỏng |
    | He, 2019 | *Environ. Sci. Pollut. Res.* 26(36): 36515–36537 | 10.1007/s11356-019-06759-7 | Đo hiện trường rung và tiếng ồn do cầu trục dầm trong hai tòa nhà trên đề-pô, mức rung nhạy với vận tốc chạy hơn tải. | Hiện tượng; không phát hiện hư hỏng |
    | Zolina, 2017 | *Vestnik MGSU* (12): 1352–1360 | 10.22227/1997-0935.2017.12.1352-1360 | Đánh giá ảnh hưởng tải cầu trục đến an toàn nhà công nghiệp bằng thí nghiệm tỉ lệ thật và phương pháp xác suất; dao động khi cầu trục chạy lệch lớn hơn khi xe con giảm tốc. | Nhà công nghiệp có cầu trục; đánh giá kết cấu, không phải SHM dữ liệu |
    | Valdez và cs., 2024 | *Struct. Health Monit.* 24(5): 2941–2957 | 10.1177/14759217241268522 | Phát hiện lỏng bu lông ở chân đế dạng giàn của tua-bin gió trên mô hình thu nhỏ bằng PCA và khoảng cách Mahalanobis chỉ cần dữ liệu trạng thái lành. | Lỏng bu lông, học từ trạng thái lành; PTN, không có vận hành nhà xưởng |
    | Kullaa, 2011 | *Mech. Syst. Signal Process.* 25(8): 2976–2989 | 10.1016/j.ymssp.2011.05.017 | Phân biệt ảnh hưởng môi trường – vận hành, lỗi cảm biến và hư hỏng, với giả định dữ liệu huấn luyện đã chứa các điều kiện môi trường – vận hành. | Phương pháp chung; nguồn cho UV-02/K1 |

    Có sẵn trong Zotero, liên quan: Eraliev và cs. 2022 `VVBGM9EN` (*Sensors*, 10.3390/s22031210): theo tóm tắt, phát hiện lỏng bu lông đế động cơ ở ba tốc độ vận hành bằng học máy, cấp máy móc. Chưa đọc toàn văn.
  - **Kết quả (ở mức tóm tắt):** không thấy nghiên cứu nào xử lý trực tiếp phát hiện suy giảm liên kết trong nhà khung thép có cầu trục bằng dữ liệu hiện trường. Gần nhất: Hu 2023 (hư hỏng dầm cầu trục dưới tải di động, thí nghiệm) và Eraliev 2022 (lỏng bu lông dưới nhiều tốc độ vận hành, máy). **Chưa kiểm toàn văn** Hu 2023 và Eraliev 2022; 3 truy vấn không phải tìm kiếm có hệ thống.
- **Phát biểu đã thu hẹp (đề xuất):** việc biến đổi môi trường – vận hành che lấp hư hỏng đã được xác lập chung ([45], Worden 2007, Figueiredo 2011, Cawley 2018); rung do cầu trục đã được đo trong nhà máy và tòa nhà vì tiện nghi và rung vi mô (Ju 2020; He 2019, Li 2022, Zolina 2017 theo tóm tắt); phát hiện hư hỏng dưới tải cầu trục đã được thử cho chính dầm cầu trục trong thí nghiệm (Hu 2023, theo tóm tắt). Phần chưa thấy: phát hiện suy giảm **liên kết** của **khung nhà** công nghiệp khi trạng thái cầu trục và máy móc là một phần của đường cơ sở vận hành, bằng dữ liệu hiện trường.
- **[NCS] Đánh giá tiềm năng thành K4:** thấp. Phần còn lại là khoảng trống **ứng dụng** ("chưa làm cho loại công trình này"), mà sự hiếm không đồng nghĩa với tính mới; căn cứ riêng cho nhà xưởng hiện chỉ là nhận định của NCS. Đề xuất giữ làm (i) luận điểm của 3.2 (L2.2) và (ii) yêu cầu nội dung của K1: bối cảnh quan trắc và điều kiện áp dụng phải ghi trạng thái cầu trục, máy móc; kiểm chứng ở WP3. NCS quyết định.
