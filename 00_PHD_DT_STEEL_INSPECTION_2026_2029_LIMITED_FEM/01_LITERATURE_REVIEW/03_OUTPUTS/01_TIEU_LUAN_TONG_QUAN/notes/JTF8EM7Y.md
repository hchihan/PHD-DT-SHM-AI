# JTF8EM7Y — Seiß, Zheng, Melzner, Wium & Seppänen (2025) — [82]

Seiß S, Zheng Y, Melzner J, Wium J, Seppänen O. Ontology-based representation of quality assurance and inspection
planning in construction. *Automation in Construction* 177 (2025) 106268. DOI 10.1016/j.autcon.2025.106268.

**Thông tin thư mục đã đối chiếu trên tr. 1 của PDF:** tiêu đề, 5 tác giả (Bauhaus-Universität Weimar; Aalto
University; Stellenbosch University), tạp chí *Automation in Construction*, tập 177, số bài 106268, năm 2025, DOI như
trên. Nhận bài 01/10/2024, nhận bản sửa 02/05/2025, chấp nhận 05/05/2025, trực tuyến 20/06/2025; truy cập mở CC BY.
**Trạng thái xuất bản:** bản chính thức của nhà xuất bản (version of record): đã có tập và số bài, chân trang ghi
"Automation in Construction 177 (2025) 106268" và đánh số trang 1–17. Không phải bản "in press" hay bản chấp nhận.
Khớp với `matrix/doi_chieu_danh_muc.csv` dòng [82].

**Bản đã đọc:** PDF nhà xuất bản trong Zotero (`storage/JM8S8UTE`), 19 tr. (tr. 1–17 thân bài và đầu danh mục tham khảo;
tr. 17–19 danh mục tham khảo). Trang dẫn dưới đây là trang in của tạp chí (trùng số trang PDF). Đọc toàn văn thân bài
(mục 1–9, Bảng 1–8, Listing 1–5); các hình 4, 7, 9 đọc trực tiếp trên ảnh trang; các hình 1–3, 5, 6, 8, 10–12 đọc qua
chú thích và lời dẫn. Danh mục tham khảo chỉ lướt. Đọc ngày 01/10/2026, phiên T2-4. Tài liệu năm 2025: không dùng làm
căn cứ chính cho một khoảng trống (CLAUDE.md 4.1).

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | JTF8EM7Y / [82] |
| Tier / Cụm | Tier 2 / Truy vết thông tin |
| Luận điểm | Lập kế hoạch kiểm tra chất lượng trong thi công cần một biểu diễn hình thức tích hợp thông tin hợp đồng, thiết kế/BIM, tiến độ, tổ chức, quy chuẩn và dữ liệu chất lượng; tác giả đề xuất ontology mô-đun OCQA (OWL), dựa trên DiCon và thuật ngữ ISO 9000/9001, DIN 55350, để mô tả kế hoạch kiểm tra và cung cấp tri thức lập kế hoạch (tr. 1–2, 5–7). |
| Bằng chứng | Phát triển theo phương pháp Linked Open Terms (LOT) (tr. 3–4); kiểm nhất quán bằng Pellet và OOPS! (tr. 9); đánh giá theo tiêu chí (tr. 9); đánh giá theo nhiệm vụ bằng câu hỏi năng lực (CQ) và truy vấn SPARQL trên dữ liệu thật của một công trình (công tác láng nền – screed, nhà thầu DEKO) (tr. 9–14); hai buổi phỏng vấn nhóm tập trung với 5 và 6 chuyên gia (tr. 4, 15–16). Không có chỉ số định lượng về hiệu năng. |
| Giới hạn | Xem mục 7. |
| Tác động K1/K2/K3 | K1: không thu hẹp (giá trị thực đo không mang độ bất định hay phạm vi hiệu lực; có tiền lệ căn chỉnh quan sát/đo với SOSA). K2: không thu hẹp (liên kết lần kiểm tra – cấu kiện tĩnh, không có thời hạn). K3: thu hẹp nhẹ ở phía **kiểm tra** (người chịu trách nhiệm, nhãn trạng thái kế hoạch), không chạm phía **hành động** và lịch sử chuyển trạng thái. |
| Vị trí sử dụng | 3.5 (ontology cho hồ sơ kiểm tra, căn chỉnh SOSA); 4.5 (biểu diễn lần kiểm tra – cấu kiện – người chịu trách nhiệm, giai đoạn thi công); 5.5 (tiền lệ cho `INSPECTION_RECORD` và cặp giá trị yêu cầu – giá trị thực đo; căn chỉnh khi xuất RDF). |
| Mức đã đọc | Toàn văn thân bài (01/10/2026) |

## 1. Câu hỏi và đối tượng

- (a) Ba thách thức (tr. 1): thông tin lập kế hoạch kiểm tra không đồng nhất, phải đồng bộ với tiến độ thực; kế hoạch
  riêng cho dự án đòi nhiều đặc trưng kiểm tra từ nhiều hệ thông tin; tri thức lập kế hoạch phụ thuộc hợp đồng, tổ chức,
  quy chuẩn và kinh nghiệm ngầm.
- (a) Thực hành hiện hành dùng danh mục kiểm tra (checklist) chung, không riêng cho dự án; thiếu lập kế hoạch chi phí,
  nguồn lực, trách nhiệm, lịch kiểm tra (tr. 1); nhóm chuyên gia xác nhận điều này (tr. 15, Bảng 8, câu 1).
- (a) Theo ISO 9000, "kiểm tra" (inspection) được xếp dưới khái niệm "xác định" (determination); kế hoạch kiểm tra
  là kết quả chính của lập kế hoạch kiểm tra (tr. 2).
- **Giai đoạn:** (a) mục đích của ontology là "lập kế hoạch kiểm tra trong **thi công**" (tr. 5, Purpose); người dùng
  cuối là quản lý thi công, kiến trúc sư, kế hoạch viên, đội trưởng, công nhân, nhà cung cấp ở giai đoạn chuẩn bị và
  thi công (tr. 5). Quản lý tài sản và quản lý cơ sở vật chất chỉ được nêu là lĩnh vực **có thể** áp dụng sau (tr. 16,
  mục 8.2). **[NCS]** Bài không bàn kiểm tra – bảo trì trong vận hành.
- Đối tượng ca nghiên cứu: công tác láng nền (screed) của một công trình nhà ở Đức, chọn vì là công tác hoàn thiện,
  nơi xuất hiện nhiều lỗi thi công nhất (tr. 9). Không có kết cấu thép, không có cảm biến trong ca nghiên cứu.

## 2. Khoảng trống tác giả nêu (tổng quan liên quan)

- (a) Các cách lập kế hoạch kiểm tra dựa trên BIM/IFC trước đây cho ra danh mục chuẩn hóa, không cá thể hóa theo cấu
  kiện; Kim và cs. ghi lần kiểm tra và kết quả trong phần mở rộng IFC; Ding và cs. mở rộng IFC để trao đổi kế hoạch và
  lần kiểm tra đã thực hiện (tr. 2–3). Mở rộng IFC cho tri thức kiểm tra đòi mở rộng lớn; mở rộng ifcOWL sẽ thành
  ontology nguyên khối khó bảo trì (tr. 3).
- (a) Bốn ontology kiểm tra chất lượng trước đó (C3R², CQIE, Martinez và cs., HCI) được đánh giá theo bộ tiêu chí ở
  Bảng 1 (tr. 4): không ontology nào biểu diễn **quá trình thi công thực tế**, vì thiếu khái niệm **trạng thái hoạt
  động**, **theo dõi thực thể thay đổi theo thời gian** và thông tin đa ngữ cảnh như đồ thị có tên (named graphs) cho
  kế hoạch – thực tế (tr. 3); không dùng thuật ngữ theo chuẩn chất lượng; đều nguyên khối; đều chưa công bố theo chuẩn
  Web ngữ nghĩa (tr. 3–4).

## 3. Thiết kế ontology

### 3.1 Phương pháp và yêu cầu

- (a) LOT gồm đặc tả yêu cầu, hiện thực, công bố, bảo trì; bước 1.3 bổ sung thu thập tri thức miền theo METHONTOLOGY
  (tr. 3–4, Hình 2). Ý niệm hóa kết hợp từ trên xuống (chuẩn, tài liệu kỹ thuật, ontology có sẵn) và từ dưới lên (dữ
  liệu của doanh nghiệp) (tr. 4).
- (a) Tài liệu đặc tả yêu cầu (ORSD) (tr. 5): phạm vi gồm lần kiểm tra, kế hoạch kiểm tra và các thực thể liên quan
  (tác nhân, thiết bị, quy trình, chuẩn, chi phí, chỉ dẫn, xác suất hư hỏng); hai ca sử dụng (mô tả kế hoạch kiểm tra;
  cung cấp tri thức lập kế hoạch); sáu yêu cầu phi chức năng (độ phủ, nhất quán, dễ dùng, rõ ràng, tái sử dụng – mở
  rộng, tin cậy – minh bạch). Ngôn ngữ OWL, soạn bằng Protégé.
- (a) Yêu cầu chức năng ở dạng CQ (tr. 5, Bảng 2): ca 1 có 5 CQ (thực thể liên quan của một lần kiểm tra; liên kết
  giữa các lần kiểm tra và với tiến độ; ngày bắt đầu – kết thúc; loại kiểm tra; đặc trưng được kiểm); ca 2 có 4 CQ
  (loại kiểm tra nào gán được/được yêu cầu cho một hoạt động, cấu kiện, vị trí; thực thể cần cho một loại kiểm tra;
  ràng buộc thời gian; đặc trưng kiểm được). **Không CQ nào hỏi về kết quả, quyết định chấp nhận, xử lý không phù hợp
  hay lịch sử.** [NCS, từ việc đọc Bảng 2]

### 3.2 Kiến trúc mô-đun (tr. 6–8, Hình 3)

- (a) Sáu miền tri thức: hợp đồng (BOQ), tài liệu thi công (bản vẽ, BIM, tiến độ), tổ chức (trách nhiệm, thiết bị), tài
  liệu kỹ thuật (chuẩn, hướng dẫn), dữ liệu chất lượng (lần kiểm tra và hư hỏng ở dự án trước, phương pháp, thiết bị),
  tài liệu kế hoạch kiểm tra (tr. 6).
- (a) Mô-đun: **lõi** (`ocqa:`); **danh mục** (`ocqa-cat:` xác suất hư hỏng, năng suất, đơn giá); **quy chuẩn**
  (`ocqa-reg:Regulation` với lớp con `Norm`, `Standard`, `Guideline`); **hợp đồng** (`ocqa-con:PerformanceDescription`,
  `BOQ`, `BOQItem`, `FunctionalPerformanceDescription`, `GeneralTerms`, `GeneralTechnicalTerms`, quan hệ
  `ocqa-con:requiredby`); **luật**; và **mở rộng theo công tác** (ví dụ `ocqa-screed:`) bằng `rdfs:subClassOf`
  (tr. 6–8, Hình 5, 6). Mô-đun danh mục và luật không trình bày trong bài, xem tài liệu trực tuyến (tr. 7).

### 3.3 Mô-đun lõi (tr. 7, Hình 4)

- (a) `ocqa:Inspection` là lớp con của `ocqa:Determination` (theo ISO 9000), cùng cấp với `ocqa:Measurement` và
  `ocqa:Observation`; đồng thời là lớp con của `dicp:Activity` (DiCon), nên có ngày bắt đầu, kết thúc và thời lượng như
  một hoạt động, và tham gia tiến độ (tr. 7).
- (a) Một lần kiểm tra gán được với `dice:Location`, `dice:BuildingObject`, `dice:Agent`, `dice:Equipment`,
  `dicp:Activity` (tr. 7). Theo Hình 4: `ocqa:InspectionPlan` —`ocqa:hasInspection`→ `ocqa:Inspection`;
  `ocqa:hasSubInspection`; `ocqa:hasInspectionEquipment` → `ocqa:InspectionEquipment`;
  `ocqa:hasInspectionProcedure` → `ocqa:InspectionProcedure`; `ocqa:Inspector` —`dica:isResponsiblefor`→
  `ocqa:Inspection`; `ocqa-reg:requiredby` → `ocqa-reg:Regulation`; `ocqa-cat:hasFeature` → `ocqa-cat:Feature`.
- (a) **Đặc trưng kiểm tra và giá trị:** `ocqa:Characteristic` (lớp con của `dicv:Property`) gắn với cả đối tượng được
  kiểm và lần kiểm tra; trỏ tới `ocqa:AssignedCharacteristicValue` (giá trị yêu cầu, do quy chuẩn hay thực thể khác đặt
  ra) và `ocqa:ActualCharacteristicValue` (giá trị thực xác định được). So sánh hai giá trị để xác định sự phù hợp được
  thực hiện bằng luật chuẩn hóa qua ngôn ngữ truy vấn hoặc luật (tr. 7). Khái niệm so sánh trực tiếp này được bổ sung
  sau góp ý của nhóm chuyên gia (tr. 15, Bảng 8, câu 4).
- (a) **Trạng thái:** trong ca nghiên cứu, lần kiểm tra mang `ocqa:hasStatus` "planned" và cấu kiện mang
  `ocqa:hasInspectionStatus` "to be inspected" (tr. 11, Bảng 4 câu 10, Listing 1 dòng 19–20, Hình 9). Theo Hình 9
  (tr. 12), cả hai là giá trị chữ (literal). **[NCS]** Bài không định nghĩa danh sách giá trị trạng thái, máy trạng thái,
  hay sự kiện chuyển trạng thái; trạng thái chỉ là một giá trị hiện tại.

### 3.4 Căn chỉnh với ontology bên ngoài (tr. 9, Hình 7)

- (a) **Cấu kiện, không gian:** dùng `dicp:hasObject` của DiCon để nối `ocqa:Inspection` với vùng hay cấu kiện của BOT
  (`bot:Zone`, `bot:Element`) hoặc ifcOWL (`ifc:IfcElement`) (tr. 9).
- (a) **Thời gian:** dùng Ontology for Property Management (OPM) và mô-đun biến – ngữ cảnh của DiCon để biểu diễn thay
  đổi của thực thể theo thời gian (tr. 9). **[NCS]** Chỉ nêu ở mức căn chỉnh; ca nghiên cứu không minh họa thay đổi theo
  thời gian hay lịch sử trạng thái.
- (a) **Cảm biến:** căn chỉnh với SSN, SOSA và SAREF; `sosa:Observation` và `saref:Measurement` được ánh xạ tới
  `ocqa:Observation` và `ocqa:Measurement` (tr. 9). Theo Hình 7 (tr. 9; NCS đọc trên hình, không phân biệt chắc kiểu
  tiên đề của từng mũi tên): có quan hệ `ocqa:hasSensor` tới `sosa:Sensor`; `ocqa:InspectionProcedure` nối
  `sosa:Procedure`; `ocqa:ActualCharacteristicValue` nối `sosa:Result`; `ocqa:InspectionEquipment` nối `sosa:Sampler`;
  ngoài ra `dice:Entity` nối `BFO:Entity`.
- (a) **Tổ chức:** `ocqa:Inspector` căn chỉnh với `foaf:Person`, `foaf:Organization` (tr. 9).
- (a) Có mô hình căn chỉnh tự động dựa trên BERT (theo BERTMap), nhưng nằm ngoài phạm vi bài (tr. 9).
- **[NCS]** Tìm trong thân bài không thấy PROV-O, SHACL, IFC `IfcApproval`, BCF; không có khái niệm nguồn gốc, phiên bản
  phương pháp, độ bất định hay phạm vi hiệu lực.

## 4. Lần kiểm tra được nối với cấu kiện và với quyết định, hành động như thế nào

- **Với cấu kiện:** (a) lần kiểm tra 42015 trỏ tới đối tượng láng nền có UUID `2EXbspDnzBfQetvaNkppij` qua
  `dicp:hasObject` (tr. 10–11, Bảng 4 câu 1, Listing 1 dòng 3, Hình 9); mô hình BIM ở dạng IFC được chuyển sang RDF bằng
  bộ chuyển IFC2LBD (tr. 10). Vị trí được suy từ vị trí của cấu kiện (tầng 1, phân khu 2) (tr. 11). Quan hệ là một –
  một trong ví dụ; không có thời hạn hiệu lực. [NCS cho hai ý cuối]
- **Với yêu cầu và căn cứ:** (a) chuỗi "vì sao phải kiểm": lần kiểm tra —`requiredby`→ DIN 18202 ←`references`— DIN 18560
  ←`contract`— hạng mục BOQ 3310.25.5.24; giá trị yêu cầu: sai lệch cao độ tối đa 0,6 cm trên chiều dài đo 200 cm; đo lặp
  3 lần do có thể có sai số đo (tr. 10–11, Bảng 4, Listing 1).
- **Với tiến độ:** (a) hoạt động láng nền 14545 đứng trước lần kiểm tra, thuộc Takt5; khoảng thời gian sớm nhất – muộn
  nhất 2022-08-01 đến 2022-08-15 (tr. 10–11); ở ca 2, luật SPARQL CONSTRUCT suy ra khung thời gian của lần kiểm tra
  42016 từ hoạt động trước – sau, cộng 3 ngày khô (tr. 14, Listing 4).
- **Với người:** (a) Inspector01, thuộc DEKO, `dica:isResponsiblefor` lần kiểm tra (tr. 11, Listing 1 dòng 17–18).
- **Với quyết định, hành động:** (a) quyết định được nói tới là **quyết định lập kế hoạch** của người lập kế hoạch (chọn
  loại kiểm tra, chọn quy trình đo bằng thước thủy thay vì lưới cao độ) (tr. 13–14). Bài nêu chung rằng OCQA có thể
  "hỗ trợ ra quyết định liên quan đến kiểm tra" (tr. 16). **[NCS]** Không có lớp cho kết luận phù hợp/không phù hợp, báo
  cáo không phù hợp, biện pháp khắc phục, phê duyệt hay chấp nhận; không có quan hệ từ kết quả kiểm tra sang hành động.
- **Lần kiểm tra đã thực hiện:** (a) dữ liệu đầu vào có "kế hoạch kiểm tra gồm các lần kiểm tra đã lập và đã thực hiện"
  (tr. 10). **[NCS]** Các truy vấn trình bày chỉ dùng lần kiểm tra ở trạng thái "planned"; bài không cho ví dụ giá trị
  thực đo (`ActualCharacteristicValue`) hay kết quả phù hợp.

## 5. Thẩm quyền, phê duyệt, trạng thái

| Ý | Có trong bài? | Căn cứ |
|---|---|---|
| Người chịu trách nhiệm lần kiểm tra | Có | `dica:isResponsiblefor`, `ocqa:Inspector` ↔ `foaf:Person` (tr. 7, 9, 11) |
| Tổ chức của người kiểm tra | Có | `dica:isOrganizationPartOf` (tr. 11, Listing 1) |
| Vai trò, thẩm quyền phê duyệt, tách nhiệm vụ | Không | [NCS] không thấy trong thân bài và hình |
| Trạng thái lần kiểm tra / cấu kiện | Có, dạng nhãn | "planned", "to be inspected" (tr. 11, Hình 9) |
| Danh sách trạng thái, bước chuyển hợp lệ, sự kiện chuyển trạng thái, người – thời điểm đổi trạng thái | Không | [NCS]; OPM/DiCon được nêu cho thay đổi theo thời gian (tr. 9) nhưng không minh họa |

## 6. Ca nghiên cứu và đánh giá

- (a) Dữ liệu thật của DEKO: BIM, tiến độ, kế hoạch kiểm tra, mẫu kiểm tra, BOQ dạng X83 (chuyển CSV bằng iTWO 4.0);
  ánh xạ thủ công sang khái niệm OCQA, sinh dữ liệu RDF bằng R2RML trong Stardog; IFC chuyển bằng IFC2LBD (tr. 10, Hình 8).
- (a) **Ca 1 – truy vấn thông tin:** một truy vấn SPARQL (Listing 1) trả lời các CQ riêng cho lần kiểm tra 42015; Bảng 4
  liệt kê 12 câu hỏi – trả lời, đánh số 1–11 (số 8 lặp hai lần) (tr. 11). Kết quả hiển thị trên công cụ mẫu gồm bộ dựng
  truy vấn Sparnatural, bảng/đồ thị, trình xem BIM và tiến độ (tr. 11–12, Hình 10).
- (a) **Ca 2 – tri thức hỗ trợ lập kế hoạch:** 5 CQ (Bảng 5, tr. 13); suy luận bằng bộ suy luận của Stardog xếp lần kiểm
  tra 42016 vào lớp kiểm tra sau láng nền nhờ tiên đề (Bảng 6); truy vấn ra loại kiểm tra (độ phẳng, độ ẩm, cao độ), chuẩn
  yêu cầu (DIN 18202), khung thời gian 2022-08-08 đến 2022-08-22, quy trình và thiết bị (tr. 13–15, Bảng 5–7, Listing 2–5).
- (a) Kiểm nhất quán: Pellet và OOPS! cho kết quả ontology nhất quán và mạch lạc (tr. 9). Đánh giá theo tiêu chí về độ
  rõ và khả năng mở rộng (tr. 9). Nhóm tập trung (11/2022): đánh giá tốt tính minh bạch, thuật ngữ, độ phủ; nhưng độ
  phức tạp và linh hoạt của ontology bị xem là điểm yếu vì thiếu chuẩn chi tiết cho kiểm tra (tr. 15–16, Bảng 8 câu 8).
- **[NCS]** Không có chỉ số định lượng (độ phủ CQ dưới dạng tỉ lệ, thời gian truy vấn, độ đúng), không có ca dữ liệu sai,
  không so với thực hành hiện hành. Câu hiện có ở `tieuluan/05_chuong5.md` ("bài báo không thử một trường hợp dữ liệu
  sai nào \[82\]") khớp với bản đã đọc.

## 7. Giới hạn

**(b) Tác giả tự nêu (tr. 16–17, mục 8.3):**
- Không có ontology tốt nhất; cần cải tiến, bảo trì liên tục qua GitHub.
- Trích xuất và chuyển đổi tri thức làm thủ công, hạn chế khả năng mở rộng; căn chỉnh tự động bằng LLM/BERT cần đánh giá
  thêm về độ chính xác và khả năng mở rộng.
- Chưa dùng OCQA để tự động suy ra kế hoạch kiểm tra.
- Thiếu giải pháp tự động tổng quát để tạo dữ liệu thể hiện: BIM chuyển RDF dễ, nhưng tiến độ và kế hoạch kiểm tra không
  có định dạng chuẩn; dùng R2RML viết tay.
- Đánh giá theo nhiệm vụ chỉ cho công tác láng nền (có đánh giá khác cho cách nhiệt và an toàn giàn giáo ở bài khác); suy
  luận dựa trên truy vấn SPARQL định sẵn, cần công sức để định sẵn cho ca khác.
- Không được phép chia sẻ dữ liệu ca nghiên cứu (tr. 17, Data availability).

**[NCS] nhận định:**
- Phạm vi là **đảm bảo chất lượng trong thi công**, trọng tâm là **lập kế hoạch** kiểm tra; vận hành – bảo trì chỉ là
  hướng áp dụng được nêu (tr. 16).
- Kết quả kiểm tra được biểu diễn tối thiểu (giá trị thực so với giá trị yêu cầu); không có nguồn gốc của giá trị thực,
  độ bất định (dù có yêu cầu đo lặp 3 lần vì sai số đo, tr. 11), hay phạm vi hiệu lực.
- Căn chỉnh SOSA/SSN được khai báo nhưng ca nghiên cứu không có cảm biến.
- Đánh giá định tính, một công tác, một nhà thầu, dữ liệu không công khai; nhóm tập trung do chính nhóm tác giả tổ chức.
- Tài liệu 2025 (đã xuất bản chính thức): dùng được làm tiền lệ, không làm căn cứ chính cho khoảng trống.

## 8. Đoạn dùng được cho tiểu luận

| # | Nội dung (diễn đạt lại, không trích nguyên văn) | Trang | Loại | Mục dùng |
|---|---|---|---|---|
| 1 | OCQA biểu diễn lần kiểm tra như một hoạt động trong tiến độ, nối với cấu kiện (BOT/ifcOWL), vị trí, người chịu trách nhiệm, thiết bị, quy trình và quy chuẩn yêu cầu | 7, 9 | Bằng chứng | 3.5, 4.5 |
| 2 | Cặp giá trị yêu cầu – giá trị thực đo của một đặc trưng kiểm tra cho phép xác định sự phù hợp bằng luật truy vấn | 7 | Bằng chứng | 5.5 (tiền lệ cho trường `value` của bản ghi kiểm tra) |
| 3 | Quan sát và đo được đặt dưới khái niệm "xác định" theo ISO 9000 và căn chỉnh với SOSA/SSN, SAREF | 7, 9 | Bằng chứng | 3.5, 5.5 (ánh xạ chuẩn) |
| 4 | Các ontology kiểm tra trước đó thiếu khái niệm trạng thái hoạt động và theo dõi thực thể thay đổi theo thời gian | 3, 4 (Bảng 1) | Bằng chứng (nhận định của [82] về tài liệu khác) | 3.5 |
| 5 | Trong thực hành thi công, kiểm tra thường dựa vào danh mục chung, thiếu kế hoạch về trách nhiệm, nguồn lực và lịch | 1, 15 | Bằng chứng (giai đoạn thi công) | 4.5 (bối cảnh chung) |
| 6 | Phạm vi của OCQA là lập kế hoạch kiểm tra trong thi công; quản lý tài sản và cơ sở vật chất là lĩnh vực áp dụng tiềm năng | 5, 16 | Bằng chứng | 3.5, 5.5 (định vị phần mới) |
| 7 | Trạng thái lần kiểm tra chỉ là nhãn hiện tại, không có lịch sử chuyển trạng thái hay phê duyệt | 11, Hình 9 | Diễn giải [NCS] | 5.5 (sau khi NCS duyệt) |

Lưu ý cho câu hiện có ở `tieuluan/05_chuong5.md` (dòng 25): "Seiß và cộng sự (2025) dùng trực tiếp định danh IFC để gắn
hồ sơ kiểm tra với cấu kiện \[82\]". Bản đọc cho thấy định danh là UUID của cấu kiện sau khi chuyển IFC sang RDF bằng
IFC2LBD, nối qua `dicp:hasObject` (tr. 9–11); và đối tượng được nối là **lần kiểm tra theo kế hoạch** (trạng thái
"planned"), chưa phải hồ sơ kết quả. **[NCS]** Đề xuất sửa "hồ sơ kiểm tra" thành "lần kiểm tra trong kế hoạch kiểm tra
chất lượng thi công" ở GĐ5; chờ NCS quyết.

## 9. Ánh xạ với schema của luận án (CLAUDE.md §8)

| Thực thể luận án | OCQA | Mức | Trang | Ghi chú |
|---|---|---|---|---|
| `INSPECTION_RECORD` | `ocqa:Inspection` (lớp con của `ocqa:Determination` và `dicp:Activity`), trong `ocqa:InspectionPlan` | Tương đương một phần | 7, 11 | Về ý là lần kiểm tra **theo kế hoạch** trong thi công; có thời gian, người, quy trình, thiết bị, yêu cầu; kết quả chỉ ở `ActualCharacteristicValue`. [NCS] |
| `EVIDENCE` (value) | `ocqa:ActualCharacteristicValue` so với `ocqa:AssignedCharacteristicValue`; `ocqa:Observation`, `ocqa:Measurement` (↔ `sosa:Observation`, `saref:Measurement`) | Tương đương một phần | 7, 9 | Có giá trị và căn chỉnh SOSA; **không có** `uncertainty`, `method_version`, nguồn gốc; không phân loại cảm biến / quan sát / NDT. [NCS] |
| `VALIDITY_SCOPE` | — | Không có | — | Gần nhất là khung thời gian và điều kiện tiên quyết của lần kiểm tra (tr. 11, 14) — điều kiện để **thực hiện** kiểm tra, không phải phạm vi được **dùng** kết quả. [NCS] |
| `OBS_CONTEXT` | `ocqa:InspectionProcedure`, `ocqa:InspectionEquipment`, tần suất đo (`ocqa:hasMeasurementFrequency`) | Tương đương một phần | 7, 11 | Mô tả cách đo, không có đợt quan trắc hay cấu hình cảm biến. [NCS] |
| `COMPONENT` | `dice:BuildingObject`, `bot:Element`, `ifc:IfcElement` qua `dicp:hasObject` | Có | 7, 9, 11 | Không có `model_version`. [NCS] |
| `SENSOR`, `SENSOR_MAPPING` | `ocqa:hasSensor` → `sosa:Sensor` (Hình 7) | Có lớp, không có ánh xạ có thời hạn | 9 | Không có `valid_from`/`valid_to`. [NCS] |
| `EVIDENCE_USE` | — | Không có | — | [NCS] |
| `ACTION` (priority_level, Action_Status) | — | Không có | — | `ocqa-cat:` có xác suất hư hỏng làm chỉ báo mức quan trọng của lần kiểm tra (tr. 11), không phải mức ưu tiên của hành động. [NCS] |
| `STATUS_EVENT` | — (chỉ nhãn `ocqa:hasStatus`, `ocqa:hasInspectionStatus`) | Không có | 11 | OPM/DiCon được nêu cho thay đổi theo thời gian (tr. 9), không minh họa. [NCS] |
| `AGENT` (role, authority) | `ocqa:Inspector` ↔ `foaf:Person`; `dica:isResponsiblefor`; `dice:Organization` | Có `AGENT` và trách nhiệm thực hiện; không có `authority` | 7, 9, 11 | Không có vai trò phê duyệt. [NCS] |
| `MODEL_VERSION` | — | Không có | — | [NCS] |
| Ràng buộc C1–C9 | Kiểm nhất quán OWL (Pellet, OOPS!); tiên đề phân loại kiểm tra | Không tương đương | 9, 13 | Tiên đề dùng để **phân loại** lần kiểm tra (Bảng 6, 7), không để kiểm ràng buộc dữ liệu như C1–C9; không dùng SHACL. [NCS] |

**[NCS] Hệ quả cho 5.5:** OCQA có thể là ontology để **căn chỉnh** phía `INSPECTION_RECORD` khi xuất RDF (cặp giá trị
yêu cầu – thực đo; `ocqa:Observation`/`Measurement` ↔ SOSA; người kiểm tra ↔ FOAF), tương tự cách [35] dùng IFC 4.3 cho
phía IFC. Phần luận án bổ sung so với OCQA: tầng bằng chứng (nguồn gốc, độ bất định, phạm vi hiệu lực, ánh xạ cảm biến
có thời hạn), tầng trách nhiệm (hành động, sự kiện chuyển trạng thái có căn cứ và thẩm quyền), và giai đoạn vận hành.

## 10. Kiểm phản chứng

### UV-01 — Chuỗi cảnh báo → hành động

- **Kết luận: không giải quyết** phần đã thu hẹp (i) và (ii) của UV-01.
- Căn cứ: OCQA dừng ở lần kiểm tra theo kế hoạch trong thi công; trạng thái là nhãn hiện tại "planned" / "to be
  inspected" (tr. 11, Hình 9); không có lớp hành động khắc phục – bảo trì, không có sự kiện chuyển trạng thái, không có
  phê duyệt hay thẩm quyền (mục 3–5 ở trên, [NCS] từ việc bài không nêu); giá trị thực đo không có nguồn gốc hay phạm vi
  hiệu lực (tr. 7). Theo dõi thay đổi theo thời gian chỉ được khai báo qua OPM/DiCon (tr. 9).
- Phần OCQA **đã có** (bổ sung vào danh sách phản chứng, không làm thu hẹp thêm): biểu diễn ontology cho lần kiểm tra
  gắn cấu kiện (BOT/ifcOWL), người chịu trách nhiệm, quy chuẩn yêu cầu và cặp giá trị yêu cầu – thực đo, ở giai đoạn thi
  công (tr. 7, 9–11).
- Đề xuất ghi vào nhật ký UV-01 [NCS]: "[82] Seiß 2025 (*Autom. Constr.* 177: 106268), đã kiểm 01/10/2026, toàn văn:
  không giải quyết; ontology OCQA biểu diễn lần kiểm tra theo kế hoạch trong thi công gắn cấu kiện, người chịu trách nhiệm
  và giá trị yêu cầu – thực đo; trạng thái chỉ là nhãn; không có hành động, sự kiện chuyển trạng thái, phê duyệt (tr. 7,
  9, 11)." Phát biểu đã thu hẹp của UV-01 giữ nguyên.
- Căn cứ nhu cầu cùng chiều (TG): [82] nhận định các ontology kiểm tra trước đó thiếu khái niệm trạng thái hoạt động và
  theo dõi thực thể thay đổi theo thời gian (tr. 3). Tài liệu 2025, không tính vào ngưỡng ba căn cứ trước 2025.

### UV-07 — Xác nhận của chuyên gia đối với đầu ra AI

- **Kết luận: không giải quyết; ngoài phạm vi.** OCQA không có đầu ra của mô hình học máy về tình trạng công trình cần
  chuyên gia xác nhận. AI duy nhất trong bài là mô hình BERT căn chỉnh ontology, nằm ngoài phạm vi bài (tr. 9) và được tác
  giả nêu là cần đánh giá thêm (tr. 16). Không có bản ghi phê duyệt (mục 5). Không làm thay đổi trạng thái UV-07; mục
  "học máy có người trong vòng / thẻ mô hình" vẫn **chưa kiểm**.

## 11. Tác động tới K1/K2/K3

- **K1: không thu hẹp.** Giá trị thực đo của lần kiểm tra không mang nguồn gốc, độ bất định hay phạm vi hiệu lực (tr. 7).
  Ghi nhận: OCQA đã căn chỉnh quan sát/đo với SOSA/SSN (tr. 9) — là tiền lệ về cách ánh xạ, cùng hướng với ánh xạ SOSA/SSN
  của luận án.
- **K2: không thu hẹp.** Liên kết lần kiểm tra – cấu kiện qua `dicp:hasObject` không có thời hạn; cảm biến chỉ có ở mức
  lớp căn chỉnh (tr. 9, 11).
- **K3: thu hẹp nhẹ ở phía kiểm tra.** Người chịu trách nhiệm lần kiểm tra và nhãn trạng thái đã có biểu diễn ontology
  cho giai đoạn thi công (tr. 7, 11). Không chạm phía hành động, căn cứ và thẩm quyền của bước chuyển.

## 12. Có nên thành "tiền lệ bắt buộc nêu" (CLAUDE.md 6.1)? — khuyến nghị [NCS]

**Khuyến nghị: nên nêu bắt buộc ở 5.5 (và nhắc ở 3.5), ở vai trò hẹp hơn BCF 3.0, IFC4, [35], [44].** Lý do: luận án
ánh xạ bằng chứng sang SOSA/SSN và dùng đồ thị RDF; OCQA là ontology kiểm tra chất lượng xây dựng đã công bố (w3id.org/ocqa,
tr. 17), đã căn chỉnh `ocqa:Observation`/`Measurement` với SOSA/SAREF và cấu kiện với BOT/ifcOWL (tr. 9). Người phản biện
có thể hỏi vì sao không tái sử dụng OCQA. Cách nêu đề xuất: `INSPECTION_RECORD` của luận án căn chỉnh với
`ocqa:Inspection` và cặp giá trị yêu cầu – thực đo khi xuất RDF; phần mới là tầng bằng chứng (nguồn gốc, độ bất định,
phạm vi hiệu lực, ánh xạ cảm biến có thời hạn), tầng trách nhiệm (hành động, sự kiện chuyển trạng thái có căn cứ và thẩm
quyền) và giai đoạn vận hành – bảo trì. Không dùng [82] làm tiền lệ cho K3 hay C6. Chờ NCS quyết định có thêm vào 6.1.
