# R1 – Phản biện openBIM (IFC 4.3, BCF 3.0, IDS, mvdXML) – Paper 2 (MT2), Pha 1

Người viết: R1 (vai openBIM). Ngày 02/10/2026. Báo cáo độc lập.

Quy ước nhãn:
- **TG** kèm trang: điều tài liệu nguồn nói (trang theo ghi chú `src/NUTL57KJ.md`, `src/bellon2025.md`…).
- **[R1]**: nhận định của phản biện này.
- **[CẦN KIỂM: …]**: điều về chuẩn mà R1 nêu theo hiểu biết chuyên môn nhưng tài liệu trong `src/` không chứa; Pha 2 phải đối chiếu với văn bản chuẩn trước khi dùng trong bản thảo.

Tệp đã đọc: `NUTL57KJ.md`, `bellon2025.md` (toàn bộ); `garcia2026.md`, `theiler2018.md` (toàn bộ); `phuluc.md` (toàn bộ, gồm A.1, A.3, B.2); `CLAUDE.md` mục 2, 2A, 6.1, 8; `GD3b` mục G-B, MT2, 5.2.2, Phần F; `05_chuong5.md` 5.1.3, 5.2.2, 5.4.2, 5.5.2, 5.6.2, 5.6.5, 5.8.2; `gate2_3_data_model_v0.2.md` (toàn bộ); `OUTLINE_BIEN_TAP_24092026.md` (mục đóng góp, 2, 4); `MANUSCRIPT_OUTLINE_24092026.md` (khung lập luận, mục 2, 4, 5.2, 5.6); `P2A_0_kiem_toan_thu_muc_20261002.md` mục 1, 4, 5, 6; `04_chuong4.md` 4.5.3–4.5.4 (tham khảo).

---

## 1. Tóm tắt nhận định

- [R1] Sau khi trừ phần [35] và BCF 3.0 đã làm được, phần mới thật sự hẹp: (i) hợp đồng phạm vi hiệu lực của bằng chứng, kiểm tại lần dùng (`scope.*`, `uncertainty`, `method_version`, `within_scope`, `justification`); (ii) khoảng hiệu lực bắt buộc của ánh xạ cảm biến – cấu kiện; (iii) quan hệ định kiểu từ sự kiện chuyển trạng thái tới bản ghi sử dụng bằng chứng; (iv) ba ràng buộc thời gian – phạm vi (C3, C5, C9). Trong 41 trường – quan hệ, 13 mới hẳn và 11 mới một phần (Mục 4a).
- [R1] Phần còn lại (định danh, gắn cấu kiện, lần kiểm tra, nhiệm vụ, trạng thái, tác giả – thời điểm sự kiện, ưu tiên) đã có trong [35], BCF 3.0 hoặc thực thể IFC4/4.3 khác. ĐG1 như đang viết ("mô hình 6 thực thể mở rộng IFC 4.3 + BCF 3.0") sẽ bị đọc là tuyên bố quá mức.
- [R1] "Mở rộng IFC 4.3" chưa có cơ chế cụ thể: không Pset, không IfcRel, không IDS, không hồ sơ xuất. Thực tế là lớp SQLite có ánh xạ xuất (Phụ lục A.3, câu cuối). Mức tuyên bố phải hạ cho khớp.
- [R1] Đặc tả B1 hiện có ba chỗ dễ làm B1 yếu vô ý: mâu thuẫn "tắt C6, C9" với Bảng B.2; không nói B1 dùng tệp BCF hay sự kiện BCF-API; không nói B1 chứa bằng chứng cảm biến bằng thực thể nào. Ngoài ra, B1 làm được một phần C9 bằng quy ước ACTIVE/OUTDATED của [35], nhưng Bảng B.2 ghi "Không".
- [R1] Xuất bằng chứng cảm biến/AI thành `IfcSurfaceFeature` DEFECT là sai ngữ nghĩa (biến suy luận thành "hư hỏng vật thể"). Ngoài ra, quy tắc "mỗi cặp một `IfcRelAdheresToElement`" buộc phải nhân bản đối tượng bằng chứng.
- **Khuyến nghị sơ bộ: Major revision.** Thiết kế cứu được mà không đổi phạm vi khóa, nếu (1) viết lại ĐG1 theo bảng nguồn gốc từng trường, (2) đặc tả hồ sơ xuất IFC/BCF, (3) khóa lại đặc tả B1 theo M3–M4 dưới đây.

## 2. Major

### M1. Đóng góp ĐG1 chưa tách khỏi phần [35] và BCF 3.0 đã làm được

- **Vị trí:** ĐG1 trong `/home/claude/p2/agents/BRIEF.md` ("ĐG1 mô hình 6 thực thể mở rộng IFC4.3+BCF3.0") và `P2A_0` Đ10; `05_chuong5.md` 5.8.2 đoạn 1; `CLAUDE.md` mục 8 "Định vị"; `GD3b` MT2 mục 1.
- **Vấn đề:**
  - TG: [35] đã biểu diễn liền mạch lần kiểm tra → hư hỏng → cấu kiện → nhiệm vụ bảo trì → chi phí bằng thực thể chuẩn IFC 4.3 ADD2, không mở rộng lược đồ (tr. 3, 5–7, 17). [35] có cả người kiểm tra (`IfcActor`, `IfcRelAssignsToActor`, tr. 9) và vết sửa tệp (`IfcOwnerHistory`, tr. 9).
  - TG: theo `04_chuong4.md` 4.5.4, BCF-API 3.0 sinh sự kiện có ngày, tác giả và giá trị mới khi trạng thái vấn đề đổi.
  - [R1] Bảng phân loại ở Mục 4a cho thấy: trong 41 trường – quan hệ của Bảng A.1 (cả `EVIDENCE_USE`), 13 mới hẳn. Trong 13 trường đó, 9 dồn ở `EVIDENCE.scope/uncertainty/method_version`, `EVIDENCE_USE.within_scope/justification` và `STATUS_EVENT.evidence_ref`. Các thực thể COMPONENT, INSPECTION_RECORD, ACTION gần như không có trường mới.
  - [R1] Gọi "sáu thực thể" là đóng góp thì cộng cả phần đã có vào phần mới. Phản biện sẽ hỏi đúng chỗ này, nhất là khi [35] cùng tạp chí đích (Automation in Construction 174, tr. 1).
- **Vì sao quan trọng:** tạp chí hạng cao loại bài mà đóng góp chính đã có trong một bài cùng tạp chí một năm trước. Không có bảng tách bạch thì người đọc không tin con số "chênh lệch so với B1".
- **Yêu cầu sửa (kiểm được):**
  1. Đưa vào bài một bảng "nguồn gốc từng trường" như Mục 4a: mỗi trường xếp *có sẵn ở [35] / BCF 3.0 / IFC4–4.3 khác / mới*, kèm trang hoặc mục chuẩn.
  2. Viết lại ĐG1 theo các dòng "mới" của bảng (gợi ý ở Mục 7, câu 1–2). Phần có sẵn ghi là "nền", có trích [35] và BCF.
  3. Không dùng số "6 thực thể" làm đơn vị đóng góp trong Abstract hay Highlights.
- **Công sức:** S. **Mức:** Chặn.

### M2. "Mở rộng IFC 4.3" chưa có cơ chế, nên mức tuyên bố không khớp với cách cài đặt

- **Vị trí:** `phuluc.md` A.3 câu cuối ("luận án lưu dữ liệu bằng SQLite và xuất IFC"); `CLAUDE.md` mục 8 ("mở rộng trên nền IFC 4.3 của [35]… Không dựng mô hình song song"; "Công cụ: Python, IfcOpenShell, SQLite hoặc JSON"); `05_chuong5.md` 5.8.2.
- **Vấn đề:**
  - [R1] Có hai cách đọc trái nhau. `CLAUDE.md` mục 8 nói "không dựng mô hình song song", còn A.3 nói nơi lưu chính là SQLite và chỉ xuất ra IFC.
  - [R1] Không tài liệu nào chỉ ra trường mới nằm ở đâu trong IFC: bộ thuộc tính (Pset) tự định nghĩa, quan hệ chuẩn (`IfcRel*`), hay thực thể ngoài lược đồ. Cũng không có hồ sơ xuất (export profile) hay tệp IDS mô tả phần mở rộng.
  - [R1] `EVIDENCE_USE` là quan hệ có thuộc tính (`used_at`, `within_scope`, `justification`). Trong IFC, quan hệ (`IfcRelationship`) không mang được bộ thuộc tính. [CẦN KIỂM: IFC 4.3 ADD2, `IfcRelDefinesByProperties.RelatedObjects` chỉ nhận `IfcObjectDefinition`]. Vì vậy phần lõi của ĐG2 không thể là "IFC mở rộng" nếu không vật hóa quan hệ thành đối tượng. Tài liệu chưa nêu điều này.
- **Vì sao quan trọng:** phản biện openBIM sẽ tìm lược đồ EXPRESS, Pset hoặc IDS. Nếu chỉ thấy cơ sở dữ liệu SQLite thì bài bị xếp vào loại "IFC-washing", tức gắn nhãn IFC cho một cơ sở dữ liệu riêng.
- **Yêu cầu sửa:**
  1. Chọn và ghi mức tuyên bố: "lớp dữ liệu bằng chứng – trách nhiệm có ánh xạ xuất sang IFC 4.3 ADD2 và BCF 3.0". Bỏ cách nói "lược đồ IFC mở rộng" (lý do ở Mục 4c).
  2. Đặc tả hồ sơ xuất. Với mỗi trường: thực thể IFC hoặc phần tử BCF đích; tên Pset tự định nghĩa (không dùng tiền tố `Pset_`, vì tiền tố này dành cho buildingSMART [CẦN KIỂM]); kiểu thuộc tính; và mất gì khi xuất.
  3. Viết hồ sơ xuất thành một tệp IDS. Kiểm tệp xuất bằng IDS và bằng dịch vụ kiểm IFC của buildingSMART, cùng bốn nhóm kiểm như [35] (TG tr. 10–11).
  4. Làm phép thử khứ hồi: SQLite → IFC/BCF → đọc lại bằng IfcOpenShell → so từng trường. Báo tỉ lệ trường giữ được.
- **Công sức:** M. **Mức:** Chặn.

### M3. Định nghĩa B1 tự mâu thuẫn ở C6, C9 và thiếu ba quyết định dựng

- **Vị trí:** `CLAUDE.md` mục 8 "Đối chứng" ("cùng script (tắt các ràng buộc C5, C6, C9 và các trường mới)"); `phuluc.md` Bảng B.2 (B1 ở C6 là "Một phần (BCF ghi người và loại thay đổi…)"); `GD3b` F-1 "Rủi ro thêm"; `05_chuong5.md` 5.5.2 bước 2.
- **Vấn đề:**
  1. [R1] Nếu tắt hẳn C6 cho B1 thì B1 bắt được 0 lỗi C6. Như vậy cột B1 ở Bảng B.2 ("Một phần") không bao giờ được đo. Hai nguồn hiệu lực cao nói hai điều khác nhau.
  2. [R1] "BCF 3.0" không nói rõ là tệp BCF hay BCF-API 3.0. TG: `04_chuong4.md` 4.5.4 và `GD3b` (dòng "có căn cứ") đều dẫn **BCF-API** cho sự kiện. [CẦN KIỂM: tệp bcfzip 3.0 chỉ giữ `ModifiedDate/ModifiedAuthor` lần sửa cuối của Topic cùng các Comment, không có danh sách sự kiện]. Nếu B1 được dựng bằng tệp bcfzip thì B1 mất lịch sử trạng thái, và lỗi đó nằm ở cách dựng chứ không ở chuẩn.
  3. [R1] B1 = "[35] + BCF" mà [35] không có cảm biến (TG tr. 18; `bellon2025.md` Phần A, SENSOR "không có"). Đặc tả không nói bằng chứng MT1 vào B1 dưới dạng nào: `IfcSurfaceFeature` DEFECT? Có `IfcSensor` + `IfcRelAssignsToProduct` như [2] (TG `theiler2018.md` Phần A) không? Nếu B1 không có cảm biến thì mọi lỗi nhóm C3 "không phát hiện" là do dựng, không phải do chuẩn.
  4. [R1] Một lần kiểm tra trong [35] là một đợt kiểm tra cả công trình (TG tr. 5). INSPECTION_RECORD của luận án là một lần kiểm tra một cấu kiện (`phuluc.md` A.1). B1 phải được phép lồng `IfcTask` INSPECTION theo cấu kiện bằng `IfcRelNests`. TG: [35] tự nói cách chia cấp điều chỉnh được (tr. 3, 17).
  5. [R1] Ở B1, hành động nằm ở `IfcTask` MAINTENANCE ([35]) hay ở Topic của BCF? Hai thứ nối với nhau bằng gì? Nếu không nối thì chuỗi B1 gãy do dựng.
- **Vì sao quan trọng:** `GD3b` F-1 đã nêu rủi ro "B1 bị dựng yếu một cách vô ý". Đây đúng là chỗ phản biện sẽ tấn công nếu B1 thua ở mọi nhóm lỗi.
- **Yêu cầu sửa (đưa vào đặc tả B1, khóa trước khi đo):**
  - Thay "tắt C6, C9" bằng "chạy C6′, C9′". Đây là phiên bản của C6, C9 chỉ dùng trường B1 có (Mục 4b, bảng B1-1).
  - B1 dùng mô hình sự kiện của BCF-API 3.0, tức sự kiện của topic và của comment. Nếu không dựng máy chủ thì giả lập đúng các trường sự kiện của BCF-API.
  - B1 có `IfcSensor` và `IfcRelAssignsToProduct` theo [2]. Bằng chứng cảm biến vào B1 theo cùng khuôn DEFECT + Pset của [35] (tr. 4–5).
  - Nêu rõ cách nối Topic BCF ↔ `IfcTask` (tham chiếu GUID hoặc liên kết tài liệu) và nguồn sự thật của trạng thái hiện thời.
  - Thêm trường "biểu diễn được trong B1? có/không" cho mỗi lỗi chèn. Báo riêng "không biểu diễn được" và "biểu diễn được nhưng không bắt được".
- **Công sức:** M. **Mức:** Chặn.

### M4. B1 làm được một phần C9 và C3. Bảng B.2 đang ghi "Không"

- **Vị trí:** `phuluc.md` Bảng B.2 dòng C3 và C9; `bellon2025.md` Phần A dòng VALIDITY_SCOPE và Phần D.3.
- **Vấn đề:**
  - TG: [35] tạo bản ghi hư hỏng mới cho mỗi lần kiểm tra. Bản mới nhất là `ACTIVE`, các bản trước là `OUTDATED`; sau bảo trì, các bản đều thành `REPAIRED`. Hư hỏng "cùng một" được nhận qua tên (tr. 9–10, 12).
  - [R1] B1 vì vậy có đủ dữ kiện để làm C9′ (Mục 4b):
    - bản ghi chỉ thêm, không ghi đè, nên `CreationDate` trong `IfcOwnerHistory` của bản mới là thời điểm bản cũ bị thay [CẦN KIỂM: `CreationDate` không đổi khi đối tượng bị sửa];
    - sự kiện BCF có ngày;
    - Topic hoặc Comment có thể trỏ GlobalId của bản ghi DEFECT.
  - [R1] Phép kiểm C9′ là: "tại ngày của sự kiện, đã có bản ghi DEFECT cùng tên, tạo muộn hơn bản đang được trỏ chưa?". Phép kiểm này bắt được lỗi C9 với bằng chứng nhận diện được, và hỏng khi tên không duy nhất.
  - [R1] Tương tự, nếu B1 giữ chuỗi tệp IFC theo phiên bản (một CDE theo ISO 19650 làm vậy; `garcia2026.md` Phần A dòng MODEL_VERSION), thì C3′ làm được: tra ánh xạ cảm biến của phiên bản IFC đang hiệu lực tại thời điểm đo. Cách này kém chính xác hơn khoảng hiệu lực thật.
  - [R1] Chỉ có C5 là B1 không thể làm được, vì không có trường phạm vi. Đây đúng là phần mới.
- **Vì sao quan trọng:** nếu B1 ghi "Không" mà phản biện chỉ ra cách làm C9′ thì toàn bộ chênh lệch M2 ở nhóm "phiên bản" bị nghi là do dựng B1 yếu.
- **Yêu cầu sửa:** sửa Bảng B.2 thành "Một phần (C9′, C3′; điều kiện: …)", cài C9′, C3′ vào script B1 và khóa trước khi đo. Kết quả M2 ở hai nhóm này mới là phần chênh lệch có ý nghĩa thực nghiệm.
- **Công sức:** S–M. **Mức:** Nặng.

### M5. Chênh lệch M2 so với B1 ở nhóm C5 là hiển nhiên theo thiết kế, giống M1 so với B0

- **Vị trí:** `CLAUDE.md` mục 8 dòng M2 ("trọng tâm… C5, C9"); `05_chuong5.md` 5.4.2, 5.8.2 đoạn cuối; `GD3b` MT2 mục 5.
- **Vấn đề:**
  - [R1] B1 theo định nghĩa không có trường phạm vi, nên tỉ lệ bắt lỗi C5 của B1 bằng 0 do cấu trúc, trước mọi phép đo. Đây là cùng loại lập luận mà tài liệu đã tự áp cho M1 so với B0 ("hiển nhiên theo thiết kế"), nhưng chưa áp cho M2 so với B1.
  - [R1] Phần thực nghiệm thật của M2 là: tỉ lệ bắt và tỉ lệ dương tính giả của mô hình đề xuất trước lỗi chèn mù; các nhóm mà B1 có năng lực một phần (C1, C3′, C6′, C9′).
- **Vì sao quan trọng:** phản biện sẽ gọi so sánh C5 với B1 là "so với chính định nghĩa của mình".
- **Yêu cầu sửa:**
  - Trong bài, tách M2 thành hai phần: (a) khả năng biểu diễn, phân tích được trước khi đo (bảng có/không theo thiết kế); (b) hiệu năng phát hiện đo được (recall và dương tính giả trên bản ghi hợp lệ), theo từng nhóm.
  - Chỉ dùng (b) và các nhóm có C*′ để quy đóng góp. Với C5, đóng góp là "biểu diễn được và kiểm được", không phải "tỉ lệ cao hơn B1".
- **Công sức:** S. **Mức:** Nặng.

### M6. Ánh xạ sang IFC ở Bảng A.3 lệch với đồ thị Bảng A.1 và nhầm chiều ngữ nghĩa

- **Vị trí:** `phuluc.md` Bảng A.3 dòng "Bản ghi kiểm tra → bằng chứng", "Bằng chứng → hành động", "Trạng thái và sự kiện của hành động"; Bảng A.1 (`ACTION.Inspection_Record_ID`); `CLAUDE.md` mục 8 "Định vị".
- **Vấn đề:**
  1. TG: ở [35], `IfcRelAssignsToProduct` nghĩa là hư hỏng là **sản phẩm** của lần kiểm tra (tr. 6–7). [R1] Với bằng chứng cảm biến, lần kiểm tra **dùng** bằng chứng (`EVIDENCE_USE`), tức là đầu vào. Cột PROV của chính Bảng A.3 đã tách `prov:wasGeneratedBy` và `prov:used`, nhưng cột IFC dùng một quan hệ cho cả hai. Với chiều "dùng", khuôn đúng của [35] là `IfcRelAssignsToProcess`: [35] đã dùng quan hệ này cho hư hỏng → nhiệm vụ (tr. 7).
  2. [R1] Bảng A.3 ánh xạ quan hệ "bằng chứng → hành động", nhưng Bảng A.1 không có quan hệ này. ACTION trỏ tới `Inspection_Record_ID`. Khi xuất IFC thì quan hệ nào được sinh: hư hỏng do kỹ sư xác nhận → `IfcTask` MAINTENANCE như [35], hay lần kiểm tra → nhiệm vụ? Tài liệu chưa nói.
  3. [R1] ACTION có hai biểu diễn: `IfcTask` MAINTENANCE ([35]) và Topic của BCF (dòng cuối A.3). Không nói bên nào giữ `Action_Status`. [CẦN KIỂM: `IfcTask.Status` và `IfcTask.Priority` có trong IFC4/4.3]. Nếu cả hai cùng có trạng thái thì phải có quy tắc đồng bộ, nếu không chính phép xuất sẽ sinh lỗi "trạng thái không khớp".
- **Vì sao quan trọng:** phản biện openBIM đọc Bảng A.3 trước tiên. Một quan hệ sai chiều làm mất uy tín của cả phần "bám chuẩn".
- **Yêu cầu sửa:** tách dòng "Bản ghi kiểm tra → bằng chứng" thành hai dòng: *sinh ra* (quan sát, NDT: `IfcRelAssignsToProduct`) và *dùng* (cảm biến: `IfcRelAssignsToProcess`, bằng chứng là đầu vào của `IfcTask` INSPECTION). Thay dòng "Bằng chứng → hành động" bằng quan hệ có thật trong A.1. Chọn một nguồn sự thật cho trạng thái hiện thời: đề xuất BCF-API, với `IfcTask.Status` chỉ là bản sao khi xuất. Ghi quy tắc này vào hồ sơ xuất (M2).
- **Công sức:** S. **Mức:** Nặng.

### M7. Xuất bằng chứng cảm biến/AI thành `IfcSurfaceFeature` DEFECT là sai ngữ nghĩa và buộc phải nhân bản bằng chứng

- **Vị trí:** `CLAUDE.md` mục 8 ("khi xuất IFC tách mỗi cặp thành một `IfcRelAdheresToElement`"); `phuluc.md` A.3 dòng "Bằng chứng → cấu kiện"; `bellon2025.md` Phần D.2.
- **Vấn đề:** xem trả lời đầy đủ ở Mục 4d. Tóm tắt:
  - (i) DEFECT khẳng định có một hư hỏng vật thể trên bề mặt. Điều này trái với `05_chuong5.md` 5.8.2: "kết luận hư hỏng do kỹ sư đưa ra sau kiểm tra".
  - (ii) Một `IfcSurfaceFeature` chỉ bám tối đa một cấu kiện [CẦN KIỂM: thuộc tính ngược `AdheresToElement` SET [0:1]]. Vì vậy "mỗi cặp một quan hệ" thực chất là nhân bản đối tượng bằng chứng, làm vỡ định danh `Condition_Evidence_ID`.
  - (iii) Quan hệ bám dính buộc vòng đời bằng chứng vào cấu kiện chủ, trong khi bằng chứng phải sống qua lần thay bu lông (`install_batch`).
- **Vì sao quan trọng:** đây là điểm kỹ thuật mà phản biện IFC kiểm được ngay trên tệp xuất.
- **Yêu cầu sửa (trong phạm vi khóa):**
  - Ghi rõ: xuất một `IfcSurfaceFeature` cho mỗi cặp (bằng chứng, cấu kiện); mọi bản sao mang cùng `Condition_Evidence_ID` trong Pset và được gom bằng `IfcGroup` + `IfcRelAssignsToGroup`.
  - Đặt `ObjectType` phân biệt "SensorEvidence" với "Defect".
  - Nêu giới hạn ngữ nghĩa trong bài.
  - Phương án tốt hơn (dùng `IfcPerformanceHistory` hoặc `IfcRelAssociatesDocument` cho bằng chứng cảm biến) đổi quyết định đã khóa, nên để ở Mục 6, đề xuất P2.
- **Công sức:** S (trong phạm vi) / M (phương án Mục 6). **Mức:** Nặng.

### M8. Thiếu định danh người thực hiện: mô hình đề xuất ghi "ai" kém hơn [35] và BCF

- **Vị trí:** `phuluc.md` Bảng A.1: `INSPECTION_RECORD.inspector_role`, `STATUS_EVENT.actor_role`. Không có `actor_id` hay `inspector_id`.
- **Vấn đề:**
  - TG: [35] gán người kiểm tra là `IfcPerson`/`IfcActor` (tr. 9). TG: sự kiện BCF-API ghi tác giả (`04_chuong4.md` 4.5.4).
  - [R1] Mô hình đề xuất chỉ ghi vai trò, nên với câu hỏi 3 của người quản lý ("ai đã xử lý") nó trả lời được ít hơn B1. M3 có thể nghiêng về B1 ở câu này.
  - [R1] Không có định danh người thì không kiểm được tách nhiệm vụ (người tạo bằng chứng ≠ người phê duyệt). TG: tách nhiệm vụ là điểm [44] có (`garcia2026.md` Phần D.1, tr. 23).
- **Vì sao quan trọng:** tầng "trách nhiệm" mà không ghi người chịu trách nhiệm là điểm yếu dễ thấy.
- **Yêu cầu sửa:** thêm `actor_ref` (trỏ `IfcPersonAndOrganization` hoặc tác giả BCF) vào `STATUS_EVENT` và `INSPECTION_RECORD`, và giữ `*_role` để kiểm C6. Đây là đổi Bảng A.1 đã khóa, nên để ở Mục 6, đề xuất P1. Nếu NCS không duyệt thì phải ghi giới hạn và giải thích (ví dụ quyền riêng tư) trong bài.
- **Công sức:** S. **Mức:** Nặng.

### M9. Định danh cấu kiện qua các phiên bản mô hình chưa được xác định, ảnh hưởng nhóm lỗi định danh của cả hai nhánh

- **Vị trí:** `phuluc.md` A.1: `COMPONENT` (`BIM_GUID`, `model_version`); `EVIDENCE.BIM_GUID` và `INSPECTION_RECORD.BIM_GUID` không kèm `model_version`. So với `gate2_3_data_model_v0.2.md` A.1 "Nguyên tắc neo" và D2 (neo kép `Prototype_Component_ID` + `Binding_ID`).
- **Vấn đề:**
  - [R1] Nếu khóa của COMPONENT là (`BIM_GUID`, `model_version`) thì tham chiếu chỉ bằng `BIM_GUID` từ EVIDENCE là mơ hồ. Nếu khóa chỉ là `BIM_GUID` thì `model_version` ở COMPONENT vô nghĩa.
  - [R1] GlobalId không chắc bền qua các lần xuất. TG: hồ sơ cũ ghi 8 cặp tham số IfcGUID trùng trong Revit, còn exporter gán GlobalId mới (`MANUSCRIPT_OUTLINE` Đoạn 1.4). Hồ sơ cũ tự ghi mức NGHI NGỜ (`P2A_0` mục 5.3).
  - [R1] C1 chỉ kiểm "trỏ tới cấu kiện tồn tại". C1 không bắt được trường hợp một GlobalId bị gán cho cấu kiện khác ở phiên bản mới.
- **Vì sao quan trọng:** phản biện openBIM biết GlobalId của Revit không ổn định. Nếu bài không nói cách neo thì nhóm lỗi "định danh – liên kết" bị coi là thiết kế hở.
- **Yêu cầu sửa:**
  - Ghi rõ khóa của COMPONENT.
  - Thêm `model_version` vào mọi tham chiếu `BIM_GUID`, hoặc nêu quy tắc "tham chiếu theo phiên bản hiện hành tại `created_at`".
  - Áp cùng quy tắc cho B1.
  - Nếu cần thêm trường thì để ở Mục 6, đề xuất P3.
- **Công sức:** S. **Mức:** Nặng.

### M10. Tiền lệ IFC4 "bắt buộc nêu" chưa có nguồn và nằm ngoài B1, nên B1 dễ bị gọi là "người rơm"

- **Vị trí:** `CLAUDE.md` 6.1 (IFC4: `IfcActionRequest`, `IfcProjectOrder`, `IfcTask`, `IfcApproval`, `IfcPerformanceHistory` là tiền lệ bắt buộc nêu); `05_chuong5.md` 5.2.2 và `GD3b` 5.2.2 (`[CẦN NGUỒN: IFC4 ADD2 TC1]`); định nghĩa B1 ở `CLAUDE.md` mục 8.
- **Vấn đề:**
  - TG: tài liệu tự khẳng định IFC4 có lệnh bảo trì có trạng thái và phê duyệt ghi người, thời điểm (5.2.2). Nhưng B1 chỉ gồm "[35] + BCF". TG: [35] không dùng `IfcApproval`, `IfcActionRequest` hay `Status` của `IfcTask` (`NUTL57KJ.md` mục 2, cuối, là nhận định của NCS).
  - [R1] Phản biện sẽ hỏi: phê duyệt của trưởng phòng B trong kịch bản C3 ghi được bằng `IfcApproval` cùng `IfcRelAssociatesApproval` [CẦN KIỂM: thuộc tính `GivingApproval`, `TimeOfApproval`, `Status`]. Vậy vì sao B1 không có?
  - [R1] Câu khẳng định về IFC4 vẫn chưa có nguồn.
- **Vì sao quan trọng:** chênh lệch ở nhóm C6 dễ bị quy cho việc B1 bỏ thực thể chuẩn.
- **Yêu cầu sửa (trong phạm vi):**
  - Thêm vào bài một bảng phân tích (không đo) "thực thể IFC4/4.3 chưa dùng trong B1 → nhóm lỗi nó có thể giúp bắt". Kết luận phần vẫn thiếu: căn cứ trỏ về bằng chứng có phạm vi.
  - Bổ sung nguồn IFC 4.3 ADD2 (ISO 16739-1) [CẦN NGUỒN] trước khi viết 2.2.
  - Dựng thêm biến thể B1+ có `IfcApproval` là đổi phạm vi, nên để ở Mục 6, đề xuất P4.
- **Công sức:** S (bảng) / M (B1+). **Mức:** Nặng.

## 3. Minor

- **m1. Phiên bản bộ luật ưu tiên không có trường.**
  - *Vị trí:* `phuluc.md` A.4 đoạn cuối ("bộ luật… có phiên bản, để mỗi mức ưu tiên truy được về luật đã áp dụng") so với Bảng A.1 (`ACTION` không có trường phiên bản luật).
  - *Sửa:* thêm `priority_rule_version` (đổi Bảng A.1, nên để ở Mục 6, P6). Nếu không thêm được thì bỏ câu khẳng định. TG: `garcia2026.md` Phần D.2 cũng đề xuất trường này.
  - *Công sức:* S.
- **m2. C6 không kiểm tính liên tục của chuỗi trạng thái.**
  - *Vị trí:* `phuluc.md` B.1, C6 chỉ kiểm `from_to` có trong Bảng A.2.
  - *Vấn đề:* [R1] Lỗi "from ≠ to của sự kiện liền trước" không bị bắt. Hồ sơ cũ có luật này (`gate2_3` R11c). TG: BCF-API chỉ ghi giá trị mới (`GD3b` dòng "có căn cứ").
  - *Sửa:* gộp R11c vào C6, hoặc lưu `from` suy ra. Trong phạm vi.
  - *Công sức:* S.
- **m3. Chưa khai báo phiên bản IFC chung cho mọi nhánh.**
  - *Vị trí:* bài chưa khai báo phiên bản IFC dùng chung cho B1 và mô hình đề xuất.
  - *Vấn đề:* TG: IFC4 không có `IfcRelAdheresToElement`, kiểu INSPECTION và DEFECT; IFC4 phải thay bằng `IfcRelAggregates` ([35] tr. 15).
  - *Sửa:* khóa IFC4X3_ADD2 cho mọi nhánh. Ghi cách xuất từ Revit và kiểm GlobalId bằng IfcOpenShell. Hồ sơ cũ (`MANUSCRIPT_OUTLINE` 5.2) đã ghi IFC4X3_ADD2.
  - *Công sức:* S.
- **m4. Không đo khả năng trao đổi bằng phần mềm xem.**
  - *Vấn đề:* TG: [35] Bảng 3, tr. 17: chỉ 2/8 phần mềm hiển thị đủ quá trình và chi phí.
  - *Sửa:* M3 (truy ngược) đo trên IfcOpenShell và truy vấn BCF cho cả hai nhánh, như `bellon2025.md` Phần D.5 đã ghi. Không tuyên bố "trao đổi được giữa phần mềm" nếu không thử.
  - *Công sức:* S.
- **m5. Đích của bằng chứng về liên kết bu lông.**
  - *Vấn đề:* [R1] Bằng chứng nói về một liên kết (cột – kèo) nên tự nhiên thành n:m với các thanh. Nếu BIM có mô hình liên kết hoặc bu lông [CẦN KIỂM: BIM nhà xưởng có `IfcMechanicalFastener`, `IfcElementAssembly` hoặc `IfcRelConnectsWithRealizingElements` không], thì đích 1:1 là cụm liên kết. Đích này khớp [35] và giảm việc nhân bản ở M7.
  - *Sửa:* ghi lựa chọn đích (thanh hay cụm liên kết) trong hồ sơ xuất.
  - *Công sức:* S.
- **m6. Kết quả kiểm tra "không thấy hư hỏng" không có chỗ trong IFC.**
  - *Vấn đề:* [R1] Bước Hoàn thành → Đã xác minh cần bản ghi kiểm tra sau sửa chữa cho kết quả "đạt". Theo khuôn [35], kết quả âm không có đối tượng IFC, vì hư hỏng chỉ tồn tại khi có phát hiện (tr. 5, 7).
  - *Sửa:* đặc tả cách xuất kết quả âm, ví dụ `IfcTask` INSPECTION có Pset kết quả, sắp sau nhiệm vụ bảo trì bằng `IfcRelSequence`. TG: [35] tr. 17 tự nêu `IfcRelSequence` là hướng mở rộng. Áp cùng cách cho B1.
  - *Công sức:* S.
- **m7. Dùng IDS cho M1 ở cả hai nhánh.**
  - *Vấn đề:* [R1] M1 (đủ thuộc tính) kiểm được bằng IDS trên tệp xuất của cả B1 và mô hình đề xuất. Cách này cho M1 một công cụ chuẩn, độc lập với script của tác giả.
  - *Vấn đề:* [R1] IDS không diễn đạt được C3, C5, C9: chúng so thời gian giữa nhiều đối tượng và tính `within_scope` tại `used_at` [CẦN KIỂM: IDS 1.0, các facet và quan hệ `PartOf`]. Đó là lý do chính đáng để dùng script Python, và nên viết thẳng điều này trong bài.
  - *Vấn đề:* [R1] mvdXML diễn đạt được đường quan hệ nhưng cũng không có phép so thời gian giữa đối tượng [CẦN KIỂM]. Chỉ cần một câu trong bài.
  - *Công sức:* S.
- **m8. Nhập nhằng "BCF 3.0" và "BCF-API 3.0".**
  - *Vị trí:* `phuluc.md` B.2 ("BCF ghi người và loại thay đổi"), `05_chuong5.md` 5.2.2 ("BCF 3.0 ghi… sự kiện đổi trạng thái") so với `04_chuong4.md` 4.5.4 (BCF-API).
  - *Sửa:* thống nhất "BCF 3.0 (định dạng) và BCF-API 3.0 (sự kiện)". Trích dẫn hai văn bản riêng [CẦN NGUỒN: đặc tả BCF-API 3.0, nếu `K5SGFIGW` chỉ là định dạng].
  - *Công sức:* S.
- **m9. Ghi rõ phép thử khứ hồi chỉ là kiểm thử đơn vị.**
  - *Vấn đề:* [R1] Phép thử khứ hồi (M2-4) và phép kiểm hợp lệ tệp xuất là kiểm thử đơn vị. Không được báo cáo như kết quả. Đây là cùng nguyên tắc với cảnh báo 16/16 ở `gate2_3` A.5.
  - *Công sức:* S.

## 4. Trả lời các câu hỏi bắt buộc

### (a) Sau khi bỏ phần [35] và BCF 3.0 đã làm được, còn lại gì là mới

Xếp loại:
- **[35]**: có sẵn trong khung của Bellon 2025 (trang theo `NUTL57KJ.md`).
- **BCF**: có sẵn ở BCF 3.0 / BCF-API 3.0 (căn cứ trong `src/`: `04_chuong4.md` 4.5.4, `GD3b` dòng "có căn cứ", `phuluc.md` B.2).
- **IFC khác**: có sẵn bằng thực thể IFC4/4.3 mà [35] không dùng. Chỉ những thực thể được tài liệu nêu mới ghi TG (`CLAUDE.md` 6.1; [2] qua `theiler2018.md`). Các thực thể khác ghi [CẦN KIỂM].
- **Mới**: không có tương ứng trong [35], BCF hay IFC theo các tài liệu đã đọc. Có thể có tiền lệ ngoài openBIM (SSN, PROV, [44]).
- **Một phần**: cơ chế có sẵn, nội dung hoặc bản số mới.

Mọi xếp loại là nhận định [R1]. Căn cứ ghi ở cột 4.

| # | Trường / quan hệ (Bảng A.1) | Xếp loại | Căn cứ | Ghi chú [R1] |
|---|---|---|---|---|
| 1 | COMPONENT.`BIM_GUID` | [35] | TG tr. 4 (lớp con `IfcElement`, GlobalId) | |
| 2 | COMPONENT.`model_version` | [35] một phần / IFC khác | TG tr. 8–9 (`IfcOwnerHistory` mới mỗi lần sửa); [44] gói có phiên bản và mã băm (`garcia2026.md` A) | Không mới. Khóa chưa rõ (M9) |
| 3 | SENSOR.`Sensor_ID` | IFC khác ([2]) | TG `theiler2018.md` A (`IfcSensor`, `IfcSensorNode`) | [2] là mở rộng lược đồ; `IfcSensor` có trong IFC4 [CẦN KIỂM: kiểu gia tốc kế trong IFC 4.3] |
| 4 | SENSOR_MAPPING (`Sensor_ID`, `BIM_GUID`) | IFC khác ([2]) | TG `theiler2018.md` A (`IfcRelAssignsToProduct`, tr. 59, 63) | |
| 5 | SENSOR_MAPPING.`valid_from`, `valid_to` | **Mới** (với IFC/BCF) | TG `phuluc.md` A.3 ("Không có trường thời hạn"); tiền lệ SSN `Deployment` (`CLAUDE.md` 6.1) | Phần mới của C3 |
| 6 | SENSOR_MAPPING.`install_record_ref` | [35] (khuôn) | TG tr. 6–7 (`IfcRelAssociatesDocument` cho tài liệu của lần kiểm tra) | Mới chỉ ở chỗ bắt buộc |
| 7 | EVIDENCE.`Condition_Evidence_ID` | [35] | TG tr. 4–5 (GlobalId của `IfcSurfaceFeature`) | [35] nhận "cùng một hư hỏng" qua tên (tr. 12); định danh bản ghi thì có |
| 8 | EVIDENCE.`evidence_type` | Một phần ([35]) | TG tr. 4–5 (loại ở `ObjectType`) | Cơ chế có; giá trị "cảm biến/NDT" mới |
| 9 | EVIDENCE.`BIM_GUID` n:m | Một phần ([35]) | TG tr. 5 (một hư hỏng – một cấu kiện) | Bản số n:m mới; xung đột khi xuất (M7, 4d) |
| 10 | EVIDENCE.`Sensor_ID` (bằng chứng → cảm biến) | **Mới** (quan hệ) | [35] không có cảm biến (TG tr. 18); [2] không có bằng chứng (`theiler2018.md` A) | Thực thể có sẵn ở [2], quan hệ thì không |
| 11 | EVIDENCE.`value` | [35] | TG tr. 4–5 (số đo trong bộ thuộc tính) | |
| 12 | EVIDENCE.`uncertainty` | **Mới** | `bellon2025.md` A ("không có `value`/`uncertainty`… theo nghĩa của schema") | Cơ chế Pset có; nội dung mới [CẦN KIỂM: `IfcPropertyBoundedValue` dùng cho khoảng] |
| 13 | EVIDENCE.`method_version` | **Mới** | TG `phuluc.md` A.3 ("Phiên bản phương pháp – Không có") | Tiền lệ PROV `Plan` |
| 14–17 | EVIDENCE.`scope.inference_unit`, `.data_split`, `.install_batch`, `.applicable_conditions` | **Mới** (4 trường) | `bellon2025.md` A (VALIDITY_SCOPE "không có, tương tự xa"); `theiler2018.md` A ("không có") | Lõi G-A/A2 |
| 18 | EVIDENCE.`obs_context` | Một phần ([35] + [2]) | TG tr. 5, 8–9 (lần kiểm tra có ngày giờ); `theiler2018.md` A (OBS_CONTEXT một phần: cấu hình mạng) | Nhiệt độ, cờ cầu trục mới [CẦN KIỂM: `IfcTimeSeries` có `StartTime`/`EndTime`/`DataOrigin`] |
| 19 | EVIDENCE.`created_at` | [35] / IFC lõi | TG tr. 9 (`IfcOwnerHistory`) | `CreationDate` [CẦN KIỂM] |
| 20 | EVIDENCE.`revision_of` | **Mới** (quan hệ tường minh) | TG tr. 9–10 (`OUTDATED` là ghi đè theo quy ước); `phuluc.md` A.3 ("Không có") | Tương tự xa ở [35]; B1 làm C9′ được một phần (4b) |
| 21 | INSPECTION_RECORD.`Inspection_Record_ID` | [35] | TG tr. 5 (`IfcTask` INSPECTION) | Khác độ mịn: [35] là đợt kiểm tra cả công trình |
| 22 | INSPECTION_RECORD.`BIM_GUID` | [35] (khuôn) | TG tr. 6–7 (công trình → kiểm tra bằng `IfcRelAssignsToProcess`; gián tiếp qua hư hỏng) | |
| 23 | INSPECTION_RECORD.`inspector_role` | [35] một phần | TG tr. 9 (`IfcPerson`, `IfcActor`, `IfcRelAssignsToActor`) | [35] ghi **người**, schema chỉ ghi **vai trò** (M8). Vai trò: `IfcActorRole` [CẦN KIỂM] |
| 24 | INSPECTION_RECORD.`inspected_at` | [35] | TG tr. 8–9 (lần kiểm tra có ngày giờ) | |
| 25 | INSPECTION_RECORD.`finding` | [35] một phần | TG tr. 5, 7 (hư hỏng là sản phẩm của lần kiểm tra) | Kết quả âm không biểu diễn (m6) |
| 26 | INSPECTION_RECORD.`finding_uncertainty` | **Mới** | `bellon2025.md` B.2 ("không có độ bất định") | |
| 27 | EVIDENCE_USE (lần kiểm tra **dùng** bằng chứng) | Một phần ([35] khuôn ngược chiều) | TG tr. 7 (`IfcRelAssignsToProduct` = sinh ra; `IfcRelAssignsToProcess` = đầu vào nhiệm vụ) | Quan hệ "dùng" biểu diễn được bằng khuôn `AssignsToProcess` (M6) |
| 28 | EVIDENCE_USE.`used_at` | Một phần (IFC lõi) | [R1] `OwnerHistory.CreationDate` của chính đối tượng quan hệ [CẦN KIỂM] | Có thời điểm tạo quan hệ, không có ngữ nghĩa "lần dùng" |
| 29 | EVIDENCE_USE.`within_scope` | **Mới** | `bellon2025.md` A (EVIDENCE_USE: "không có kiểm trong/ngoài phạm vi"); `garcia2026.md` A (như trên) | Lõi ĐG2 |
| 30 | EVIDENCE_USE.`justification` | **Mới** | như trên | Lõi ĐG2 |
| 31 | ACTION.`Action_ID` | [35] + BCF + IFC khác | TG tr. 5–6 (`IfcTask` MAINTENANCE); BCF Topic; `CLAUDE.md` 6.1 (`IfcActionRequest`, `IfcProjectOrder`) | |
| 32 | ACTION.`Inspection_Record_ID` | [35] (gián tiếp) | TG tr. 7 (hư hỏng → nhiệm vụ; hư hỏng ← lần kiểm tra) | |
| 33 | ACTION.`priority_level` | BCF / IFC khác | `bellon2025.md` A ("không có `priority_level`"); [CẦN KIỂM: phần tử `Priority` của Topic BCF 3.0; `IfcTask.Priority`] | Trường có sẵn. Luật bốn mức có phiên bản là phần riêng (m1) |
| 34 | ACTION.`Action_Status` (suy ra) | BCF / IFC khác | TG `04_chuong4.md` 4.5.4 (trạng thái vấn đề BCF; `Status` của yêu cầu hành động IFC4 là nhãn tự do [CẦN NGUỒN: IFC4 ADD2 TC1]) | "Suy ra từ sự kiện mới nhất" là lựa chọn thiết kế, không phải điểm mới |
| 35 | STATUS_EVENT.`Status_Event_ID` | BCF (sự kiện) | TG `04_chuong4.md` 4.5.4 | |
| 36 | STATUS_EVENT.`Action_ID` | BCF | như trên (sự kiện thuộc một Topic) | |
| 37 | STATUS_EVENT.`from_to` | BCF một phần | TG `GD3b` (sự kiện ghi "loại và giá trị mới") | `from` suy ra từ sự kiện trước (m2) |
| 38 | STATUS_EVENT.`timestamp` | BCF | TG `04_chuong4.md` 4.5.4 ("ngày") | |
| 39 | STATUS_EVENT.`actor_role` + kiểm vai trò được phép (Bảng A.2) | Một phần (BCF: tác giả; [44]: vai trò, RACI) | TG `04_chuong4.md` 4.5.4 ("tác giả"); `garcia2026.md` A (AGENT "đủ") | Áp khuôn [44] cho hành động bảo trì là phần mới (`CLAUDE.md` 6.1) |
| 40 | STATUS_EVENT.`evidence_ref` → EVIDENCE_USE | **Mới** | TG `CLAUDE.md` 6.1 ("phần mới… là quan hệ giữa sự kiện chuyển trạng thái với bản ghi sử dụng bằng chứng"); `GD3b` ("không ghi căn cứ") | Lõi ĐG3 |
| 41 | STATUS_EVENT.`reason` | BCF một phần | [R1] Comment BCF có văn bản, tác giả, ngày [CẦN KIỂM: BCF 3.0 markup, Comment] | Comment không gắn định kiểu với sự kiện |

**Đếm [R1]:** 41 trường – quan hệ. Mới hẳn **13**: #5, 10, 12, 13, 14–17, 20, 26, 29, 30, 40. Một phần **11**. Có sẵn **17**.

Trong 13 trường mới, 9 nằm ở hợp đồng phạm vi và tầng trách nhiệm (#12–17, 29, 30, 40). Bốn trường còn lại:
- #5: thời hạn ánh xạ;
- #10: bằng chứng → cảm biến;
- #20: bản ghi thay thế;
- #26: độ bất định của kiểm tra.

Ngoài Bảng A.1, phần mới còn có:
- Bảng A.2 (danh sách bước chuyển và vai trò được phép, áp cho hành động bảo trì). Khuôn này có tiền lệ ở [44] cho gói thông tin.
- Ràng buộc C3, C5, C9 (kiểm thời gian và phạm vi tại lần dùng).
- Quy tắc "đợt lắp đặt hiện hành đổi khi can thiệp được xác minh" (`phuluc.md` B.1).

**Kết luận (a) [R1]:**
- COMPONENT, INSPECTION_RECORD, ACTION là **nền đã có**. Bài nên trình bày chúng như hồ sơ áp dụng [35] + BCF cho nhà thép, không phải đóng góp.
- Đóng góp nằm ở ba điểm:
  - **hợp đồng bằng chứng có phạm vi**: #12–17 cộng #29–30, kiểm bằng C5;
  - **căn cứ định kiểu của bước chuyển**: #40 cộng Bảng A.2, kiểm bằng C6;
  - **tính toàn vẹn theo thời gian**: #5, #20, kiểm bằng C3, C9.

### (b) B1 có thể bị dựng yếu vô ý không?

**Có, ở ít nhất bảy điểm.** Điểm nêu trong câu hỏi trước tiên.

**b.1. `IfcOwnerHistory`: hai câu nói về hai việc khác nhau, không mâu thuẫn.**
- TG: `NUTL57KJ.md` (tr. 9): ứng dụng của [35] tạo một `IfcOwnerHistory` **mới** cho mỗi lần sửa tệp có sẵn, "để theo dõi mọi thay đổi". Đây là **cách cài đặt** của [35].
- TG: `bellon2025.md` A dòng MODEL_VERSION ghi "Theo IFC, chỉ giữ lần sửa cuối (xem nhật ký UV-03, IFC4)". Đây là **ngữ nghĩa của chuẩn**.
- [R1] Mỗi đối tượng `IfcRoot` trỏ tới tối đa một `IfcOwnerHistory`. Đối tượng đó ghi lúc tạo và **lần sửa cuối** (`ChangeAction`, `LastModifiedDate`, `LastModifyingUser`) [CẦN KIỂM: IFC 4.3 ADD2, `IfcOwnerHistory`; từ IFC4, `OwnerHistory` là tùy chọn].
- [R1] Ghép hai câu lại:
  - Tệp của [35] tích lũy nhiều `IfcOwnerHistory`, mỗi phiên sửa một bản.
  - Nhưng với **từng đối tượng**, chỉ còn vết của lần sửa cuối. Khi một bộ thuộc tính bị đổi `ACTIVE` → `OUTDATED` → `REPAIRED`, ai đổi và lúc nào ở bước giữa bị mất. Cụ thể là `IfcPropertySet` (một `IfcRoot`) được gán `OwnerHistory` mới; còn `IfcProperty` thì không có `OwnerHistory`.
  - Riêng các bản ghi chỉ thêm (mỗi lần kiểm tra một DEFECT mới, TG tr. 9) giữ được `CreationDate` của chính nó.
- **B1 công bằng phải:**
  1. Cài đúng cách của [35]: mỗi phiên ghi một `IfcOwnerHistory` mới, có `ChangeAction`, ngày, `IfcPersonAndOrganization` của người sửa. Không bỏ trống `OwnerHistory` vì "IFC4.3 cho phép tùy chọn".
  2. Giữ mọi bản ghi DEFECT theo kiểu chỉ thêm, như [35] làm.
  3. Được phép giữ chuỗi tệp IFC theo phiên bản (mỗi giai đoạn một tệp, như ca 1 của [35] có hai giai đoạn, TG tr. 11–14). B1 không bị giới hạn ở một tệp ghi đè.
- Nếu B1 dựng theo câu "chỉ giữ lần sửa cuối" mà bỏ (1)–(3) thì B1 yếu hơn chính [35].

**b.2. Trạng thái `ACTIVE/OUTDATED/REPAIRED` của [35] làm được một phần C9.** Xem M4. Phép kiểm C9′:
- **Dữ kiện:** sự kiện BCF có ngày (TG `04_chuong4.md` 4.5.4); Topic hoặc Comment trỏ GlobalId của bản ghi DEFECT làm căn cứ.
- **Phép kiểm:** tồn tại một DEFECT cùng `Name`, có `CreationDate` sớm hơn ngày sự kiện và muộn hơn `CreationDate` của bản được trỏ hay không?
- **Giới hạn:**
  - nhận diện qua tên (TG tr. 12);
  - chỉ bắt được khi Topic có trỏ GUID;
  - quy ước `REPAIRED` ghi đè làm mất thời điểm `OUTDATED` (TG tr. 9–10).
- Đó vẫn là "Một phần", không phải "Không" như Bảng B.2.

**b.3. BCF: tệp hay API.**
- TG: `04_chuong4.md` 4.5.4: BCF-API 3.0 sinh một sự kiện có ngày, tác giả, giá trị mới mỗi khi trạng thái đổi.
- TG: `GD3b` (G-B, dòng "có căn cứ"): sự kiện ghi loại và giá trị mới, không ghi căn cứ (BCF-API mục 3.9).
- Tài liệu **không** nói gì về Comment.
- [R1] Comment BCF có văn bản, tác giả, ngày, có thể trỏ một góc nhìn chứa GUID; Topic có tham chiếu tài liệu [CẦN KIỂM: BCF 3.0 markup.xsd `Comment`, `DocumentReferences`; BCF-API 3.0 sự kiện của comment].
- **B1 công bằng:** dùng mô hình sự kiện của BCF-API, không dùng bcfzip trơn. Mỗi lần đổi trạng thái kèm một Comment ghi lý do và trỏ bằng chứng (GUID DEFECT hoặc tài liệu). Khi đó B1 kiểm được "có lý do không rỗng" và "có trỏ một căn cứ".
- **Điều B1 vẫn không làm được:** Comment không gắn định kiểu với sự kiện, chỉ ghép được theo thời gian và tác giả; và không có cờ trong/ngoài phạm vi. Đây mới là phần mới (#40).

**b.4. Vai trò và phê duyệt.**
- TG: [35] gán người kiểm tra bằng `IfcActor` (tr. 9).
- [R1] `IfcActor` mang vai trò qua `IfcActorRole` [CẦN KIỂM].
- [R1] BCF-API có cấu hình quyền theo người dùng [CẦN KIỂM: BCF-API 3.0, `authorization`, danh sách trạng thái người dùng được đặt].
- **B1 công bằng:**
  - có bảng người → vai trò bằng `IfcActor`/`IfcActorRole`;
  - được dùng Bảng A.2 làm danh sách bước chuyển được phép. Bảng A.2 là quy tắc nghiệp vụ, không phải thực thể mới; có thể cấu hình trong BCF-API ở mức người dùng.
- Khi đó C6′ = kiểm (tác giả sự kiện → vai trò) có thuộc vai trò được phép, và có Comment lý do. Phần C6 mà B1 không làm được là `evidence_ref` trỏ tới bản ghi sử dụng bằng chứng.
- `IfcApproval` cho bước "phê duyệt" là thực thể IFC4 chuẩn mà B1 hiện không gồm (M10).

**b.5. Bằng chứng cảm biến trong B1.**
- [R1] [35] không có cảm biến. Nếu B1 không có `IfcSensor` cùng `IfcRelAssignsToProduct` như [2] (TG `theiler2018.md` A), thì lỗi nhóm C3 "không phát hiện" là do dựng.
- **B1 công bằng:** có ánh xạ cảm biến không thời hạn như [2]. Nếu giữ chuỗi tệp IFC theo phiên bản thì C3′ = tra ánh xạ trong phiên bản IFC hiện hành tại thời điểm đo.

**b.6. Độ mịn và nối IFC – BCF.**
- TG: lần kiểm tra của [35] là cấp công trình (tr. 5); hành động là `IfcTask` MAINTENANCE ba cấp (tr. 5–6).
- B1 phải được phép:
  - lồng `IfcTask` INSPECTION theo cấu kiện (TG tr. 3, 17: chia cấp điều chỉnh được);
  - nối Topic BCF với `IfcTask` bằng một khóa ghi trong đặc tả.
- Không có hai điều này thì C1 của B1 báo "mồ côi" giả.

**b.7. Lỗi chèn không biểu diễn được và tính tương đương của truy vấn.**
- [R1] Lỗi "dùng ngoài phạm vi" không có trường để chèn vào B1. Nếu đếm nó là "B1 không phát hiện" thì gộp hai việc khác nhau. Cần cột "biểu diễn được trong B1".
- [R1] M3 (truy ngược) và M4 (phút/bản ghi): truy vấn B1 (IfcOpenShell + BCF) và truy vấn mô hình đề xuất (SQLite) phải do cùng người viết, khóa trước, đếm "bước" theo định nghĩa không phụ thuộc kho lưu. Nếu không, M3 nghiêng về SQLite chỉ vì kho dễ truy vấn hơn.

**Bảng B1-1. Năng lực của B1 công bằng theo từng ràng buộc (đề xuất thay cột B1 ở Bảng B.2)**

| Ràng buộc | Dữ kiện B1 có | Phép kiểm B1 (C*′) | Phần chỉ mô hình đề xuất có |
|---|---|---|---|
| C1 | GUID, quan hệ IFC ([35]), GUID trong Topic BCF | C1′ = C1 (giữ nguyên) | — |
| C3 | `IfcSensor` + `IfcRelAssignsToProduct` ([2]); chuỗi tệp IFC theo phiên bản | C3′: ánh xạ trong phiên bản IFC hiện hành tại thời điểm đo | Khoảng hiệu lực chính xác (`valid_from/to`), `install_record_ref` bắt buộc |
| C5 | Không | Không biểu diễn được | Toàn bộ (#12–17, #29–30) |
| C6 | Sự kiện BCF-API (ngày, tác giả, giá trị mới); Comment; `IfcActorRole`; Bảng A.2 làm cấu hình | C6′: bước chuyển trong danh sách, tác giả đúng vai trò, có Comment | `evidence_ref` định kiểu trỏ `EVIDENCE_USE` |
| C9 | DEFECT chỉ thêm; `CreationDate`; tên trùng; GUID trong Topic | C9′: có bản DEFECT mới hơn cùng tên trước ngày sự kiện | `revision_of` tường minh; căn cứ trỏ đúng bản ghi; không dựa vào tên |

### (c) Pset, IfcRel* hay thực thể ngoài IFC? Tương thích ngược? Mức tuyên bố đóng góp

**Ba cơ chế và giới hạn của từng cơ chế [R1]:**

| Cơ chế | Dùng cho | Tương thích ngược | Giới hạn |
|---|---|---|---|
| Pset tự định nghĩa trên đối tượng có sẵn (tên không mang tiền tố `Pset_` [CẦN KIỂM]) | Trường giá trị của EVIDENCE: `value`, `uncertainty`, `method_version`, `scope.*`, `obs_context`, `evidence_type`, `revision_of` (dạng chuỗi ID); `priority_level` | Có. Hợp lệ lược đồ; phần lớn phần mềm đọc Pset. TG: [35] dùng đúng cách này cho số đo và trạng thái (tr. 4–5) | Không có kiểu tham chiếu giữa đối tượng an toàn, nên ID chỉ là chuỗi. Không gắn được vào quan hệ |
| Quan hệ chuẩn `IfcRel*` | Bằng chứng ↔ cấu kiện, lần kiểm tra ↔ bằng chứng, lần kiểm tra ↔ hành động, tác nhân | Có, ở mức lược đồ. TG: nhiều phần mềm không đọc `IfcRelAdheresToElement` và phần quá trình ([35] tr. 17, Bảng 3) | Quan hệ không có thuộc tính, không có thời hạn. Không biểu diễn được `EVIDENCE_USE.within_scope/justification/used_at`, `SENSOR_MAPPING.valid_from/to`, `STATUS_EVENT.evidence_ref` |
| Thực thể mới trong lược đồ (kiểu IFC Monitor [2]) | Có thể biểu diễn tất cả | **Không.** Công cụ chuẩn không đọc. TG: [35] cố ý tránh để giữ khả năng trao đổi (tr. 3, 17) | Trái phạm vi khóa (công cụ Python + SQLite, `CLAUDE.md` mục 8) |
| Bảng SQLite song song, xuất IFC/BCF | Tất cả, kể cả quan hệ có thuộc tính và thời hạn | Tệp xuất tương thích nếu chỉ dùng hai cơ chế đầu | Xuất ra mất dữ liệu. Ràng buộc chỉ chạy trên SQLite |

**Khuyến nghị [R1]:**
- Kiến trúc thực tế là hàng cuối: SQLite là nơi lưu chính và nơi chạy C1–C9; xuất IFC 4.3 ADD2 bằng hai cơ chế đầu, cộng BCF-API 3.0 cho sự kiện.
- Đây cũng là cách A.3 đã viết ("luận án lưu dữ liệu bằng SQLite và xuất IFC").
- Thứ đi qua IFC mà không mất:
  - định danh;
  - gắn cấu kiện;
  - các trường giá trị của bằng chứng (Pset);
  - chuỗi lần kiểm tra → nhiệm vụ.
- Thứ **không** đi qua IFC mà không mất:
  - `EVIDENCE_USE` có thuộc tính;
  - khoảng hiệu lực của ánh xạ;
  - căn cứ định kiểu của sự kiện. Với BCF, sự kiện có lược đồ cố định, nên `evidence_ref` chỉ xuống được Comment ở dạng văn bản hoặc đường dẫn.
- Nếu muốn giữ các thứ đó trong IFC thì phải vật hóa quan hệ thành đối tượng (ví dụ một `IfcControl` con hoặc một tài liệu), và việc này làm mất ngữ nghĩa [CẦN KIỂM: `IfcControl` là lớp trừu tượng]. Nên ghi là giới hạn, không làm.

**Mức tuyên bố:** "lớp dữ liệu bằng chứng – trách nhiệm có ánh xạ xuất sang IFC 4.3 ADD2 và BCF 3.0", **không** phải "lược đồ IFC mở rộng". Lý do:
1. Không có thay đổi lược đồ EXPRESS.
2. Phần mới (Mục 4a) chính là phần không biểu diễn được bằng quan hệ IFC.
3. Gọi là "mở rộng lược đồ" sẽ bị đối chiếu với [2], vốn là mở rộng lược đồ thật (`theiler2018.md` A), và với [35], vốn chủ đích không mở rộng.

**Hệ quả cho cách viết ĐG1:**
- ĐG1 không còn là "mô hình 6 thực thể mở rộng IFC4.3 + BCF3.0". ĐG1 gồm ba thứ:
  - một **đặc tả thông tin** (bảng nguồn gốc từng trường, Mục 4a);
  - một **hồ sơ xuất** (ánh xạ trường → thực thể IFC/BCF, tên Pset, viết thành tệp IDS);
  - một **phép thử khứ hồi** báo tỉ lệ trường giữ được khi xuất.
- Câu tiếng Anh ở Mục 7.
- `CLAUDE.md` mục 8 "Không dựng mô hình song song" nên đọc là "không dựng mô hình **khái niệm** song song: dùng lại thực thể và quan hệ của [35]/BCF làm khung". Việc lưu song song bằng SQLite thì giữ. Nếu NCS đồng ý cách đọc này thì cần sửa câu chữ (Mục 6, đề xuất P5).
- Kiểm chứng cho ĐG1 gồm:
  - tệp xuất đạt dịch vụ kiểm IFC của buildingSMART (như [35], TG tr. 10–11);
  - tệp xuất đạt IDS của hồ sơ xuất;
  - tỉ lệ khứ hồi.
- Các kiểm chứng này áp cho cả B1, nên cũng xác nhận B1 hợp lệ.

### (d) EVIDENCE n:m COMPONENT xuất thành nhiều `IfcRelAdheresToElement`: vấn đề ngữ nghĩa

TG trong tài liệu:
- [35] dùng `IfcSurfaceFeature` với `PredefinedType = DEFECT` làm "chỗ giữ" cho hư hỏng. Loại ở `ObjectType`, số đo trong bộ thuộc tính (tr. 4–5).
- `IfcRelAdheresToElement` là quan hệ phân cấp, không vòng, mỗi bản ghi hư hỏng chỉ gắn một cấu kiện. Hư hỏng trên nhiều cấu kiện phải chia thành nhiều phần (tr. 5).
- Ở ca cầu, hư hỏng được vẽ thành khối lập phương tại trọng tâm cấu kiện (tr. 14–15).
- `CLAUDE.md` mục 8: "khi xuất IFC tách mỗi cặp thành một `IfcRelAdheresToElement`".

Vấn đề [R1]:
1. **Sai loại đối tượng.**
   - `IfcSurfaceFeature` là một đặc điểm vật lý trên bề mặt cấu kiện (lớp con của `IfcFeatureElement`, thuộc `IfcElement`, có vị trí và hình dạng) [CẦN KIỂM: định nghĩa trong IFC 4.3 ADD2].
   - Bằng chứng cảm biến/AI về lực siết bu lông thì khác: không nằm trên bề mặt, không phải vật thể; nó là một **suy luận** có xác suất và phạm vi, có thể là kết quả âm ("không lệch khỏi đường cơ sở").
   - Xuất nó thành DEFECT tức là khẳng định "có hư hỏng tại đây". Điều đó trái nguyên tắc "AI tạo bằng chứng, con người quyết định" (`CLAUDE.md` mục 2, QĐ 6) và trái 5.8.2 ("kết luận hư hỏng do kỹ sư đưa ra sau kiểm tra").
   - Phần mềm xem sẽ vẽ nó như một hư hỏng.
2. **Bản số buộc nhân bản.**
   - Một `IfcSurfaceFeature` chỉ bám tối đa một cấu kiện [CẦN KIỂM: thuộc tính ngược `AdheresToElement` SET [0:1]]. Một quan hệ thì gom được nhiều đặc điểm vào **một** cấu kiện.
   - Vậy "mỗi cặp một `IfcRelAdheresToElement`" chỉ hợp lệ nếu sinh **một `IfcSurfaceFeature` cho mỗi cặp**. Như thế một `Condition_Evidence_ID` thành n GlobalId.
   - Hệ quả trên tệp xuất:
     - đếm bằng chứng bị nhân n;
     - `revision_of` phải lặp n lần;
     - một sự kiện trỏ "bằng chứng" phải chọn một trong n bản;
     - C1/C9 chạy trên tệp xuất (nếu có ai chạy) cho kết quả khác chạy trên SQLite.
   - Nếu dùng một đối tượng với n quan hệ thì tệp vi phạm lược đồ.
3. **Vòng đời gắn sai.**
   - Quan hệ bám dính là quan hệ phụ thuộc: đặc điểm thuộc về cấu kiện chủ.
   - Bằng chứng phải sống qua lần thay hay siết bu lông (đợt lắp đặt đổi, `phuluc.md` B.1, đoạn cuối) và qua phiên bản mô hình mới. Gắn bám dính khiến công cụ có thể xóa bằng chứng khi xóa hay thay cấu kiện [CẦN KIỂM: hành vi của công cụ khi xóa đối tượng chủ].
4. **Quan hệ với lần kiểm tra bị đảo** (M6): bằng chứng cảm biến là đầu vào của lần kiểm tra, không phải sản phẩm.

Đề xuất:
- **Trong phạm vi khóa:**
  - Giữ `IfcSurfaceFeature` DEFECT + `IfcRelAdheresToElement` chỉ cho (i) bằng chứng loại quan sát và NDT và (ii) phát hiện đã được kỹ sư xác nhận (`finding = defect_confirmed`). Đây đúng là phạm vi [35] kiểm chứng.
  - Với bằng chứng cảm biến, nếu vẫn phải dùng `IfcSurfaceFeature`:
    - đặt `ObjectType = "SensorEvidence"`;
    - không có hình dạng;
    - Pset ghi `Condition_Evidence_ID` chung;
    - gom n bản bằng `IfcGroup`;
    - ghi giới hạn ngữ nghĩa trong bài.
  - Cân nhắc đích là cụm liên kết hoặc bu lông để bản số về 1:1 (m5).
- **Ngoài phạm vi khóa (Mục 6, P2):** xuất bằng chứng cảm biến thành đối tượng thông tin, không phải đối tượng vật lý.
  - `IfcPerformanceHistory` gắn cấu kiện bằng `IfcRelAssignsToControl`. Quan hệ này nhận nhiều đối tượng, nên giải được n:m mà không nhân bản [CẦN KIỂM].
  - TG: `CLAUDE.md` 6.1 đã nêu `IfcPerformanceHistory` là tiền lệ bắt buộc cho dữ liệu đo theo thời gian.
  - Hoặc dùng `IfcDocumentReference` cùng `IfcRelAssociatesDocument` [CẦN KIỂM: `IfcDocumentInformation` có `ValidFrom`, `ValidUntil`, `Revision`, `Status`, có thể gần với phạm vi và thay thế].

## 5. Đáng giữ / nên bỏ từ hồ sơ cũ (lớp 2), góc nhìn openBIM

**Đáng giữ:**
- Đối chiếu tham số IfcGUID của Revit với GlobalId của tệp IFC xuất thật, đọc độc lập bằng IfcOpenShell.
  - Nguồn: `OUTLINE_BIEN_TAP` 1.3, 4.1; `MANUSCRIPT_OUTLINE` 4.1, 5.6; `gate2_3` CQ12, R14–R15.
  - Dùng cho: M9 và nhóm lỗi định danh.
  - Lưu ý: 8 cặp trùng vẫn ở mức NGHI NGỜ (`P2A_0` mục 5.3).
- Sổ phiên bản IFC kèm SHA-256 và phiên bản trình xuất (`MANUSCRIPT_OUTLINE` 5.2). Dùng làm nền cho `model_version` và cho chuỗi tệp IFC của B1 (b.1, b.5). Số liệu cần truy về dữ liệu gốc.
- Nguyên tắc neo kép (`gate2_3` A.1, D2): cấu kiện logic cộng cấu kiện trong một phiên bản. Dùng để giải M9.
- Tệp IDS `gate2_baseline_IFC4X3_ADD2.ids` (`gate2_3` A.1, dòng "Yêu cầu thông tin ở cấp cấu kiện vẫn kiểm bằng IDS"). Dùng làm điểm xuất phát cho hồ sơ xuất (M2, m7). `P2A_0_phuluc_B2` mục 23 ghi tệp này không có trong thư mục; cần tìm lại.
- Câu "Phạm vi áp dụng là thuộc tính của bằng chứng, không phải thuộc tính của tệp IFC" (`OUTLINE_BIEN_TAP` 4.4). Câu này hợp với kết luận ở Mục 4c.
- Câu "Việc sử dụng SHACL hoặc RDF không phải đóng góp mới…" (`OUTLINE_BIEN_TAP` 4.6). Viết lại cho Python, IDS và IfcOpenShell.
- Các cột của bảng so sánh tám tiêu chí (`MANUSCRIPT_OUTLINE` 2.6, Bảng 1). Giữ cấu trúc, điền lại dòng Bellon theo toàn văn (`NUTL57KJ.md`).

**Nên bỏ:**
- SHACL, chuyển CSV → RDF, namespace w3id (`gate2_3` D1, D4; `MANUSCRIPT_OUTLINE` 4.6, 5.6). Trái phạm vi khóa và không cần cho openBIM.
- Bảng "Tái sử dụng chuẩn" ánh xạ thực thể sang `sosa:`/`prov:` như kiểu dữ liệu (`gate2_3` A.1). Chỉ giữ một bảng đối chiếu khái niệm (A.3).
- Dòng Bellon "(tóm tắt)" toàn ô `[CẦN BỔ SUNG]`, cùng câu "chỉ đọc được tóm tắt" (`MANUSCRIPT_OUTLINE` 2.3, 2.6). Đã lỗi thời.
- Câu "ACTION chỉ ở mức thuộc tính hỗ trợ… không trình bày máy trạng thái" (`MANUSCRIPT_OUTLINE` 4.2). Trái G-B.
- Máy trạng thái 9 trạng thái (`gate2_3` A.2.6). Bảng A.2 thay thế.
- Mọi cách nói ngầm "trao đổi được qua phần mềm BIM" khi chưa thử (m4).

## 6. Đề xuất ngoài phạm vi khóa – chờ NCS duyệt

| Mã | Đề xuất | Lý do | Chi phí |
|---|---|---|---|
| P1 | Thêm `actor_ref` (người thực hiện) vào `STATUS_EVENT` và `inspector_ref` vào `INSPECTION_RECORD` (Bảng A.1) | M8: nếu không thêm, mô hình đề xuất ghi "ai" kém hơn [35] (tr. 9) và BCF; không kiểm được tách nhiệm vụ ([44], `garcia2026.md` D.1) | S |
| P2 | Xuất bằng chứng cảm biến/AI thành `IfcPerformanceHistory` + `IfcRelAssignsToControl` (hoặc tài liệu liên kết), thay cho `IfcSurfaceFeature` DEFECT + `IfcRelAdheresToElement`. Giữ DEFECT cho quan sát, NDT và phát hiện đã xác nhận | M7, Mục 4d: đúng ngữ nghĩa, giải n:m mà không nhân bản; đổi quyết định 01/10 ở `CLAUDE.md` mục 8 | M |
| P3 | Ghi `model_version` kèm mọi tham chiếu `BIM_GUID`, hoặc khôi phục neo kép (`gate2_3` D2) | M9 | S |
| P4 | Thêm biến thể **B1+** = B1 + thực thể IFC4/4.3 chuẩn mà [35] không dùng (`IfcApproval`, `IfcTask.Status/Priority`, `IfcActorRole`); báo M2 cho B1 và B1+ | M10: chặn lời phê bình "người rơm"; chênh lệch so với B1+ là chênh lệch so với toàn bộ chuẩn | M |
| P5 | Sửa câu `CLAUDE.md` mục 8 "Không dựng mô hình song song" thành "không dựng mô hình khái niệm song song; dữ liệu lưu ở SQLite và xuất IFC/BCF theo hồ sơ xuất" | M2: hết mâu thuẫn với `phuluc.md` A.3 | S |
| P6 | Thêm `priority_rule_version` vào ACTION (cùng đề xuất `garcia2026.md` D.2 đang chờ) | m1 | S |

## 7. Câu tiếng Anh đề xuất cho bản thảo

1. "We do not propose a new IFC schema. The inspection–defect–element–task chain is represented with standard IFC 4.3 ADD2 entities following Bellon et al. [35], and issue status and status-change events follow BCF 3.0 and BCF-API 3.0; Table X classifies every field of the proposed model as inherited from [35], inherited from BCF, available in other IFC 4.3 entities, or new."
2. "The contribution is an evidence-and-responsibility layer, stored and checked outside the exchange format and exported to IFC 4.3 ADD2 through standard relationships and custom property sets specified in an IDS file. Its new elements are a mandatory validity scope for each evidence record, checked at the time of use, and a typed link from each action status change to the evidence-use record that justified it."
3. "IDS can verify the presence and value range of the exported properties, but it cannot express constraints that compare timestamps across objects, such as whether a measurement fell within the validity interval of a sensor–element mapping (C3) or whether the cited evidence had been superseded before a status change (C9); these constraints are therefore implemented as queries over the authoritative store."
4. "Baseline B1 was built to the best capability of the standards: owner-history records were written for every edit as in [35], defect records were appended rather than overwritten, BCF-API events and comments were used for status history, and reduced checks (C3′, C6′, C9′) were run wherever B1 contains the necessary fields. Errors that cannot be represented in B1 are reported separately from errors that B1 represents but misses."
5. "Sensor-derived evidence is an inference about condition, not a physical surface feature. We therefore export it as [an information object / a non-geometric surface feature typed 'SensorEvidence'] and reserve IfcSurfaceFeature with PredefinedType DEFECT for defects confirmed by an inspecting engineer."
