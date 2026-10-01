# NUTL57KJ — Bellon, Martins, Franco de Carvalho, de Souza, Ribeiro, César Júnior & de Oliveira (2025) — [35]

Bellon FG và cs. IFC framework for inspection and maintenance representation in facility management. *Automation in
Construction* 174: 106157. DOI 10.1016/j.autcon.2025.106157. Nhận 24/09/2024, chấp nhận 25/03/2025, trực tuyến 02/04/2025 (tr. 1).

**Bản đã đọc:** toàn văn bản PDF của nhà xuất bản (19 tr., tệp đính kèm trong kho Zotero), gồm thân bài tr. 1–18 và danh
mục tài liệu tr. 18–19. Hình chỉ đọc qua chú thích và phần lời mô tả; Bảng 1–3 đọc đủ. Số trang là trang in, trùng trang
PDF. Đọc ngày 01/10/2026, phiên T1-1. Tài liệu năm 2025: không dùng làm căn cứ chính cho một khoảng trống (CLAUDE.md 4.1).

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | NUTL57KJ / [35] |
| Tier / Cụm | Tier 1 / Truy vết thông tin |
| Luận điểm | Chỉ với thực thể chuẩn của IFC 4.3 ADD2, không mở rộng lược đồ, có thể biểu diễn liền một mạch kiểm tra → hư hỏng → cấu kiện bị hư hỏng → nhiệm vụ bảo trì (ba cấp) → chi phí, để trao đổi giữa các phần mềm và các bên (tr. 3, 5–7, 17). |
| Bằng chứng | Ứng dụng Python + IfcOpenShell sinh tệp IFC từ JSON; ca 1 tổng quát (3 cấu kiện, 3 lần kiểm tra, 7 bản ghi hư hỏng) đạt cả bốn nhóm kiểm của dịch vụ kiểm IFC của buildingSMART (tr. 10, 12–14); ca 2 cầu Coimbra I với 10 hư hỏng thật từ cơ sở dữ liệu của DNIT, xuất IFC4 và IFC4.3, mở trên 8 phần mềm: chỉ 2 hiển thị đủ bảo trì và chi phí (tr. 14–18, Bảng 2–3). |
| Giới hạn | Xem mục 5. |
| Tác động K1/K2/K3 | K3: thu hẹp (quan hệ định kiểu kiểm tra → hư hỏng → nhiệm vụ bảo trì đã có bằng thực thể chuẩn, cho phát hiện bằng mắt). K2: thu hẹp một phần (hư hỏng gắn cấu kiện bằng quan hệ chuẩn). K1: không liên quan trực tiếp; trạng thái "active/outdated/repaired" của hư hỏng là một tương tự xa. |
| Vị trí sử dụng | 2.2 (IFC cho kiểm tra – bảo trì); 4.5 và 5.5 (tiền lệ ràng buộc IFC cho kiểm tra – hư hỏng – bảo trì); Phụ lục ánh xạ. |
| Mức đã đọc | Toàn văn (01/10/2026) |

## 1. Câu hỏi nghiên cứu và đối tượng

- Câu hỏi (tr. 1, 3): lược đồ IFC có thể chuẩn hóa biểu diễn dữ liệu kiểm tra, hư hỏng, bảo trì và chi phí bảo trì ra
  sao, để bảo đảm nhất quán ngữ nghĩa và khả năng trao đổi giữa phần mềm.
- Khoảng trống tác giả nêu (tr. 3): chưa có cách tiếp cận IFC tổng thể nối liền dữ liệu kiểm tra, đánh giá hư hỏng, hành
  động bảo trì và phân tích chi phí; các nghiên cứu trước chủ yếu cho cầu và tập trung vào mô hình hóa hư hỏng (Bảng 1, tr. 2).
- Đối tượng: tổng quát "facility" (`IfcFacility`), áp được cho nhà, cầu, đường (tr. 4). Ca thật là cầu bê tông cốt thép
  (tr. 14). Tác giả nêu khả năng dùng cho nhà công nghiệp (tr. 1, 18) nhưng không có ca nhà công nghiệp. Giai đoạn: vận
  hành – bảo trì; nguồn dữ liệu là hồ sơ kiểm tra bằng mắt.

## 2. Phương pháp và kiến trúc thông tin

- **Chỉ dùng thực thể chuẩn** của IFC 4.3 ADD2, không mở rộng, để giữ khả năng trao đổi (tr. 3, 17). Ba nhóm biểu diễn:
  cấu trúc không gian, quá trình, chi phí (tr. 3).
- **Không gian** (tr. 4–5): `IfcSite`, `IfcFacility` (hoặc lớp con như `IfcBuilding`, `IfcBridge`); cấu kiện là lớp con
  của `IfcElement`, chứa trong công trình qua `IfcRelContainedInSpatialStructure`. Phân rã công trình nằm ngoài phạm vi.
- **Hư hỏng** (tr. 4–5): `IfcSurfaceFeature` với `PredefinedType = DEFECT`; loại hư hỏng ghi ở `ObjectType`; số đo và
  trạng thái ghi trong một bộ thuộc tính (property set). Mô hình hóa chi tiết hư hỏng nằm ngoài phạm vi; thực thể chỉ là
  "chỗ giữ" cho biểu diễn chi tiết hơn.
- **Hư hỏng – cấu kiện** (tr. 5): `IfcRelAdheresToElement`, quan hệ phân cấp, không vòng, **mỗi bản ghi hư hỏng chỉ gắn
  một cấu kiện**; hư hỏng trên nhiều cấu kiện phải chia thành nhiều phần.
- **Quá trình** (tr. 5–6): cây `IfcTask` lồng bằng `IfcRelNests`; nhiệm vụ tổng khai báo vào `IfcProject` bằng
  `IfcRelDeclares`. Nhánh kiểm tra (`PredefinedType = INSPECTION`) gồm từng lần kiểm tra toàn công trình. Nhánh bảo trì
  (`MAINTENANCE`) có ba cấp phân biệt bằng `ObjectType`: cấp công trình (một đợt can thiệp), cấp hư hỏng (gom các việc sửa
  một hư hỏng), cấp hoạt động (việc thực làm, có khối lượng và đơn giá).
- **Chi phí** (tr. 6): cây `IfcCostItem` lồng bằng `IfcRelNests` (cấp loại, lần, từng khoản), `IfcCostValue`,
  `IfcQuantityArea`/`IfcQuantityVolume`; `IfcCostSchedule` chủ yếu để hiển thị.
- **Luồng thông tin** (tr. 6–7, Hình 4), dùng các quan hệ gán:
  - công trình → nhiệm vụ kiểm tra gốc: `IfcRelAssignsToProcess`;
  - lần kiểm tra → hư hỏng: `IfcRelAssignsToProduct` (hư hỏng là **sản phẩm** của lần kiểm tra; "bảo đảm mỗi hư hỏng gắn
    với lần kiểm tra đã phát hiện nó");
  - lần kiểm tra → tài liệu: `IfcRelAssociatesDocument`;
  - hư hỏng → nhiệm vụ bảo trì cấp hư hỏng: `IfcRelAssignsToProcess` (mỗi hư hỏng gán một nhiệm vụ sửa);
  - nhiệm vụ cấp hoạt động → khoản chi phí: `IfcRelAssignsToControl`.
- **Phần cài đặt** (tr. 7–10): ứng dụng Python dùng IfcOpenShell, đầu vào JSON (công trình, cấu kiện, các lần kiểm tra
  có người kiểm tra, cấu kiện hư hỏng, hư hỏng, tài liệu; các lần bảo trì có ngày giờ) và tệp IFC có sẵn nếu có.
  - Người kiểm tra: `IfcPerson`, `IfcActor`, gán vào lần kiểm tra bằng `IfcRelAssignsToActor`, ghi là phần bổ sung ngoài
    khung gốc (tr. 9).
  - Mỗi lần sửa tệp có sẵn tạo một `IfcOwnerHistory` mới "để theo dõi mọi thay đổi" (tr. 9).
  - **Trạng thái hư hỏng** (tr. 9–10): mỗi lần kiểm tra tạo bản ghi hư hỏng mới. Bản ghi mới nhất của cùng một hư hỏng là
    `ACTIVE`, các bản trước là `OUTDATED`; sau một lần bảo trì, mọi hư hỏng báo trước đó được đặt `REPAIRED`. Tác giả ghi
    rõ đây là quy ước đơn giản hóa, có thể điều chỉnh. Hư hỏng được nhận là "cùng một" qua **tên** trùng nhau giữa các lần
    kiểm tra (tr. 12).
  - Một mô hình tham số sinh nhiệm vụ bảo trì cấp hư hỏng và cấp hoạt động theo loại và số đo hư hỏng, rồi tính khối lượng
    và chi phí (tr. 10).
- Không dùng: `IfcActionRequest`, `IfcProjectOrder`, `IfcApproval`, thuộc tính `Status` của `IfcTask`, `IfcRelSequence`
  (tr. 17 nêu `IfcRelSequence` là hướng mở rộng). Không có cảm biến hay dữ liệu quan trắc. [NCS] Điều "không dùng" là
  nhận định từ việc bài không nêu.

## 3. Cách kiểm chứng

- **Kiểm hợp lệ tệp** (tr. 10–11): mô-đun kiểm của IfcOpenShell trong lúc phát triển; sau đó dịch vụ kiểm IFC của
  buildingSMART với bốn nhóm: cú pháp STEP, lược đồ IFC, luật chuẩn IFC (ba nhóm bắt buộc), thực hành ngành (chỉ cảnh báo).
- **Ca 1 – tổng quát** (tr. 11–14): dữ liệu giả định, không có hình học; 3 cấu kiện, 2 có hư hỏng, 3 lần kiểm tra, một hư
  hỏng lớn dần qua các lần; giai đoạn 1 không có bảo trì, giai đoạn 2 có một lần bảo trì sau mọi lần kiểm tra. Kết quả:
  7 bản ghi hư hỏng (2 `OUTDATED`, 5 `ACTIVE`); tệp giai đoạn 2 đạt mọi nhóm kiểm (Hình 15). Xem trên Blender/Bonsai.
- **Ca 2 – áp dụng** (tr. 14–17): cầu Coimbra I (Minas Gerais), mô hình hoàn công từ quét laser, dựng trên Revit; 10 hư hỏng
  thật từ cơ sở dữ liệu cầu của DNIT (Bảng 2: loại, kích thước, đơn vị, cấu kiện). Xuất IFC4 và IFC4.3; hư hỏng biểu diễn
  bằng khối lập phương tại trọng tâm cấu kiện. Mở trên 8 phần mềm (Bảng 3).
  - Khác biệt IFC4 so với IFC4.3 ảnh hưởng khung (tr. 15): IFC4 không có `IfcRelAdheresToElement` (thay bằng
    `IfcRelAggregates`), bắt buộc `IfcBuilding`, thiếu kiểu định sẵn `INSPECTION` của `IfcTask` và `DEFECT` của `IfcSurfaceFeature`.
  - Kết quả (tr. 17, Bảng 3): Bonsai và KITModelViewer hiển thị đủ cả hai phiên bản; usBIM.browser thấy quan hệ ngược tới
    lần kiểm tra và nhiệm vụ bảo trì nhưng không hiển thị trực tiếp quá trình; Navisworks, Trimble Connect chỉ đọc tốt IFC4;
    BimCollab ZOOM, Primus, Solibri không nhận `IfcRelAdheresToElement` và không hiển thị bảo trì, chi phí.
- Không có kiểm chứng với người dùng, không đo thời gian hay độ đầy đủ truy vết, không so với thực hành hiện hành. "No
  data was used" (tr. 18, mục dữ liệu).

## 4. Luận điểm chính

1. Thực thể chuẩn của IFC 4.3 ADD2 đủ để biểu diễn mạch kiểm tra – hư hỏng – bảo trì – chi phí mà không cần mở rộng lược
   đồ; cách chia cấp có thể điều chỉnh mà không đổi ngữ nghĩa chung (tr. 3, 17).
2. Gắn hư hỏng với **lần kiểm tra đã phát hiện nó** và với **nhiệm vụ bảo trì sửa nó** bằng quan hệ gán định kiểu giúp
   người chỉ có tệp IFC cũng đọc được luồng thông tin (tr. 6–7).
3. Tệp hợp lệ về lược đồ chưa đủ: đa số phần mềm phổ biến không hiển thị quá trình và chi phí, và đổi giữa IFC4 và IFC4.3
   làm thay đổi mức thông tin đọc được (tr. 17–18).
4. IFC cho phép chia sẻ thông tin kiểm tra – bảo trì giàu ngữ nghĩa giữa các bên mà không mở cơ sở dữ liệu riêng, hữu ích
   khi quản lý cơ sở vật chất và bảo trì do các bên khác nhau làm (tr. 18).

### Bài có khái niệm bằng chứng tình trạng công trình không?

**Một phần, chỉ cho phát hiện bằng mắt.** Hư hỏng (`IfcSurfaceFeature` DEFECT) là một nhận định về tình trạng cấu kiện,
gắn với cấu kiện và với lần kiểm tra tạo ra nó (tr. 5, 7); có số đo và một trạng thái theo thời gian (`ACTIVE`,
`OUTDATED`, `REPAIRED`; tr. 9–10). Không có độ bất định, phương pháp, phạm vi hiệu lực hay nguồn từ cảm biến, NDT. Người
kiểm tra được ghi (tr. 9) nhưng người đánh giá, phê duyệt hành động thì không.

## 5. Giới hạn

**(b) Tác giả tự nêu:**
- Cần áp dụng trên nhiều trường hợp thật với bộ dữ liệu đầy đủ, gắn với các hệ quản lý cơ sở vật chất đã vận hành ở nhiều
  khu vực (tr. 18).
- Cần tích hợp với công nghệ thu thập dữ liệu tự động như IoT và song sinh số (tr. 1, 18).
- Phần lớn phần mềm không hiển thị quá trình và chi phí; nguyên nhân chưa xác định được vì mã nguồn đóng (tr. 18).
- Mức thông tin đọc được thay đổi giữa IFC4 và IFC4.3; cần thử với mô hình từ nhiều phần mềm và nhiều phiên bản IFC (tr. 18).
- Mô hình tham số sinh nhiệm vụ bảo trì chỉ để minh họa; ứng dụng thật cần mô hình dựa trên dữ liệu gắn loại và kích thước
  hư hỏng với dịch vụ bảo trì (tr. 17).
- Quy ước trạng thái `ACTIVE`/`OUTDATED`/`REPAIRED` và giả định "mọi hư hỏng báo trước một lần bảo trì đều đã được sửa" là
  đơn giản hóa (tr. 9–10).
- Mô hình hóa hư hỏng và phân rã công trình nằm ngoài phạm vi (tr. 4).

**[NCS] nhận định:**
- Hư hỏng được nhận diện qua các lần kiểm tra bằng **tên**, không có định danh bền của hư hỏng (tr. 12); trạng thái là giá
  trị thuộc tính bị ghi đè theo quy ước, không phải lịch sử sự kiện có người, thời điểm, căn cứ.
- Bước "đã sửa" được suy ra từ việc có một lần bảo trì, không có kiểm tra xác minh sau sửa.
- Không có thẩm quyền và phê duyệt: chỉ người kiểm tra được gán; không có ai quyết định đưa hư hỏng vào bảo trì.
- Kiểm chứng là kiểm tính hợp lệ của tệp và khả năng hiển thị; chưa có đánh giá khả năng truy vết hay giá trị cho người
  quản lý. Mẫu thật nhỏ (10 hư hỏng, một cầu).
- Nhận định "áp được cho nhà công nghiệp" (tr. 1, 18) chưa có ca kiểm chứng; không dùng [35] làm căn cứ cho luận điểm về
  nhà công nghiệp.

## 6. Điều bài KHÔNG xử lý, xét theo chuỗi của luận án

| Ý | Mức | Căn cứ |
|---|---|---|
| Nguồn gốc bằng chứng cảm biến | không xử lý | Không có cảm biến; IoT là việc sau (tr. 18) |
| Phạm vi hiệu lực của bằng chứng | không xử lý; có tương tự xa | Trạng thái `OUTDATED` đánh dấu bản ghi đã bị bản mới thay (tr. 9); đó là hiệu lực theo thời gian, không phải điều kiện áp dụng |
| Quan hệ bằng chứng – cấu kiện có thời hạn | không xử lý | `IfcRelAdheresToElement` là quan hệ phân cấp tĩnh, một hư hỏng – một cấu kiện (tr. 5) |
| Trách nhiệm, thẩm quyền | xử lý một phần | Người kiểm tra gán qua `IfcRelAssignsToActor` (tr. 9); không có phê duyệt, không có người quyết định bảo trì |
| Trạng thái hành động và lịch sử chuyển trạng thái | xử lý một phần, cho hư hỏng | Trạng thái hư hỏng theo quy ước (tr. 9–10); nhiệm vụ bảo trì không có trạng thái; không có sự kiện chuyển trạng thái |
| Truy ngược từ hành động về dữ liệu gốc | **có xử lý**, cho phát hiện bằng mắt | Nhiệm vụ bảo trì ← hư hỏng ← lần kiểm tra ← tài liệu; chi phí ← nhiệm vụ (tr. 6–7; kiểm trên KITModelViewer, tr. 17, Hình 20) |

## 7. Tác động tới K1/K2/K3

- **K3: thu hẹp.** Quan hệ định kiểu từ nhiệm vụ bảo trì về hư hỏng và về lần kiểm tra đã phát hiện hư hỏng **đã có** trong
  IFC 4.3 bằng thực thể chuẩn và đã được kiểm hợp lệ (tr. 6–7, 14). Như vậy phần "nối hành động về phát hiện tình trạng"
  của UV-01 không còn mới với **phát hiện bằng mắt**. Phần còn lại cho luận án: căn cứ là bằng chứng có nguồn gốc và
  phạm vi hiệu lực (gồm bằng chứng cảm biến, NDT); trạng thái và lịch sử chuyển trạng thái của **hành động** kèm căn cứ và
  thẩm quyền; bước xác minh sau sửa. Tác giả tự để IoT, song sinh số và hệ quản lý cơ sở vật chất thật cho công việc sau (tr. 18).
- **K2: thu hẹp một phần.** Hư hỏng gắn cấu kiện và lần kiểm tra bằng quan hệ chuẩn; truy vết hai chiều xem được trên phần
  mềm (tr. 17). Không có quan hệ cảm biến – cấu kiện; không kiểm sự bảo toàn chất lượng bằng chứng.
- **K1: không liên quan trực tiếp.**

## 8. Vị trí sử dụng trong tiểu luận v2

- 2.2: IFC 4.3 có thực thể chuẩn đủ cho mạch kiểm tra – hư hỏng – bảo trì – chi phí; hạn chế hiển thị giữa các phần mềm.
- 4.5 và 5.5: tiền lệ bắt buộc nêu cho ràng buộc IFC của bản ghi kiểm tra, hư hỏng và hành động (`IfcRelAssignsToProduct`,
  `IfcRelAdheresToElement`, `IfcRelAssignsToProcess`); nêu cùng [2] và [44]. Lưu ý thiết kế: `IfcRelAdheresToElement` chỉ cho
  một cấu kiện mỗi bản ghi, khác quan hệ n:m giữa EVIDENCE và COMPONENT của schema (xem `mapping/bellon2025.md` Phần D).
- Không dùng làm căn cứ chính cho khoảng trống (2025); không dùng cho luận điểm về nhà công nghiệp.
- Bảng ánh xạ: `mapping/bellon2025.md`.
