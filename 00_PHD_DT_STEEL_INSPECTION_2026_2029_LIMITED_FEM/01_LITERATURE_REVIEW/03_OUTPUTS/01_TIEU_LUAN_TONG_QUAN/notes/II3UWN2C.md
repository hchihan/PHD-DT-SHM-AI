# II3UWN2C — Hagedorn, Pauwels & König (2023) — [21]

Hagedorn P, Pauwels P, König M. Semantic rule checking of cross-domain building data in information containers for
linked document delivery using the shapes constraint language. *Automation in Construction* 156 (2023) 105106
(số bài báo 105106). DOI 10.1016/j.autcon.2023.105106. Nhận 12/09/2022, sửa 30/05/2023, chấp nhận 25/09/2023, trực
tuyến 12/10/2023 (tr. 1). Đã đối chiếu với trang đầu bài báo và trang bìa kho lưu trữ; khớp `matrix/doi_chieu_danh_muc.csv`
(dòng 21).

**Bản đã đọc:** bản **chính thức của nhà xuất bản** (Publisher's PDF / Version of Record) lấy từ kho lưu trữ TU/e
(trang bìa kho ghi giấy phép Taverne, ngày xuất bản 01/12/2023), tệp Zotero
`storage/89V4LD2T/Hagedorn et al. - 2023 - ...pdf`, 23 tr. PDF. Trang PDF 1 là trang bìa của kho; **trang bài báo = trang
PDF − 1** (tr. 1–22). **Số trang dưới đây là trang bài báo.** Trích văn bản bằng PyMuPDF; các Listing 1–5, A.1–B.2 là đồ
họa vector nên đã xem trực tiếp dưới dạng ảnh trang (Listing 1 tr. 7; Listing 2–3 tr. 11; A.1–A.2 tr. 17–18; B.1–B.2
tr. 19–20); Hình 10–12 (biểu đồ hộp) chỉ đọc qua chú thích và số liệu trong thân bài. Đọc toàn văn ngày 01/10/2026,
phiên T2-4.

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | II3UWN2C / [21] |
| Tier / Cụm | Tier 2 / Truy vết thông tin |
| Luận điểm | Có thể kiểm tra bằng SHACL không chỉ sự phù hợp lược đồ của một vật chứa thông tin ICDD (ISO 21597) mà cả **liên kết giữa các thực thể thuộc các miền dữ liệu khác nhau** (cấu kiện IFC ↔ công việc tiến độ) bên trong vật chứa; suy ra trước các thuộc tính liên kết trực tiếp (ontology ICDDL) giúp viết luật đơn giản hơn và kiểm nhanh hơn với tập dữ liệu lớn (tr. 1–2, 15–16). |
| Bằng chứng | Phép đo hiệu năng (benchmark) trên bốn vật chứa ICDD dữ liệu 4D (mô hình IFC + tiến độ MS-Project-XML), mỗi vật chứa ở ba kiểu liên kết (BinaryLink, DirectedBinaryLink, Directed1ToNLink), ba luật R1–R3 mỗi luật hai phiên bản (trên dữ liệu đã suy ra / dữ liệu gốc); đo thời gian suy ra và thời gian kiểm, 20 lần lặp (tr. 6–10, Bảng 2; tr. 10–16, Bảng 3–4, Hình 10–12). |
| Giới hạn | Xem mục 5. |
| Tác động K1/K2/K3 | K1: không liên quan trực tiếp (không có bằng chứng tình trạng; PROV-O chỉ dùng cho thời điểm bắt đầu/kết thúc công việc). K2: **thu hẹp về công cụ, không về khoảng trống** — kiểm được liên kết giữa thực thể của hai miền dữ liệu và so sánh khoảng thời gian bằng SHACL-SPARQL, nhưng liên kết là tĩnh, không có khoảng hiệu lực. K3: không liên quan (không có hành động, trạng thái, tác nhân). |
| Vị trí sử dụng | 3.5 (kiểm tra ràng buộc trên dữ liệu liên kết); 5.5 (SHACL là công cụ biểu diễn C1–C9; tiền lệ dạng luật); 5.7 (thiết kế kiểm chứng: phân biệt đo hiệu năng với đo độ nhạy phát hiện lỗi M2.1–M2.2); 5.6 (công cụ không phải AI: pySHACL — xem lưu ý mục 2). |
| Mức đã đọc | Toàn văn, kể cả phụ lục A–B (01/10/2026) |

## 1. Vấn đề và đối tượng

- (a) Trao đổi thông tin xuyên suốt vòng đời công trình ngày càng dùng vật chứa ICDD (ISO 21597-1, -2) để đóng gói và liên
  kết dữ liệu nhiều miền; nghiên cứu kiểm tra luật trong xây dựng chủ yếu nhắm vào sự tuân thủ của mô hình một miền (IFC),
  ít chú ý đến **liên kết giữa các miền** (tr. 1–2).
- (a) Tính đúng của liên kết là điều kiện để các bên diễn giải đúng quan hệ giữa dữ liệu do nhiều người cung cấp; ISO 29481
  (IDM) và MVD đảm bảo chất lượng cho từng mô hình IFC nhưng chưa áp cho dữ liệu liên kết trong ICDD (tr. 2).
- (a) Cấu trúc vật chứa (tr. 4, Hình 3): tệp chỉ mục `index.rdf` khai báo siêu dữ liệu và các tài liệu; **"phiên bản và
  nguồn gốc của dữ liệu trong vật chứa được chú thích"** ở đây; ba thư mục: tài nguyên ontology, tài liệu tải (payload
  documents: IFC, XML…), bộ ba tải (payload triples: linkset và dữ liệu RDF).
- (a) Linkset ontology có năm lớp liên kết (Link, BinaryLink, DirectedLink, Directed1ToNLink, DirectedBinaryLink); mỗi phần
  tử liên kết trỏ đúng một tài liệu và tùy chọn một định danh; ba loại định danh: StringBasedIdentifier,
  UriBasedIdentifier, QueryBasedIdentifier (bài không xét loại thứ ba) (tr. 4, Hình 4).
- (a) Năm câu hỏi nghiên cứu (tr. 2): RQ1 kiểm liên kết sâu giữa thực thể; RQ2 đơn giản hóa cấu trúc liên kết để viết luật;
  RQ3 dùng lược đồ linkset để suy ra quan hệ; RQ4 hiệu năng kiểm trên linkset đã suy ra so với gốc; RQ5 ảnh hưởng của cách
  viết shape, kiểu liên kết, kích thước linkset.
- Đối tượng dữ liệu: **dữ liệu thiết kế – lập tiến độ (4D)**, không có dữ liệu vận hành hay cảm biến (tr. 8).

## 2. Phương pháp: cách viết luật SHACL, ontology, công cụ

**Ba chiến lược kiểm (tr. 5, Hình 5).** V1 kiểm lược đồ ICDD bằng shape sinh từ ontology Container và Linkset (số lượng,
ràng buộc); V2 kiểm dữ liệu miền bằng shape sinh từ ontology miền (BOT, ifcOWL; đã có tiền lệ ở Oraskari và cs., Stolk &
McGlinn); **V3 kiểm liên kết**, là trọng tâm của bài.

**Suy ra thuộc tính liên kết (tr. 5–6, Listing 1 tr. 7).** Mỗi lớp liên kết của Linkset/ExtendedLinkset được chuyển thành
một `owl:ObjectProperty` trong ontology ICDDL (ví dụ `icddl:linkedBinary`), kèm luật `sh:SPARQLRule` (SHACL Advanced
Features) dạng CONSTRUCT: tìm hai phần tử liên kết, so định danh với thực thể RDF theo ba tổ hợp (chuỗi–chuỗi, chuỗi–URI,
URI–URI, nối bằng UNION), rồi tạo bộ ba quan hệ thuận và nghịch giữa hai thực thể. Sau suy ra, một liên kết nhị phân chỉ
cần hai bộ ba, trong khi cấu trúc linkset gốc cần ít nhất 15 bộ ba (tr. 15).

**Ba luật kiểm, độ phức tạp tăng dần (tr. 9).** Viết trước bằng ngôn ngữ tự nhiên, rồi mã hóa thành shape:

| Luật | Phát biểu (tr. 9) | Cách mã hóa | Nơi |
|---|---|---|---|
| R1 | Mỗi cấu kiện phải liên kết với ít nhất một công việc | V1: `sh:NodeShape`, `sh:targetClass bot:Element`, `sh:property` với `sh:alternativePath` qua các thuộc tính ICDDL, `sh:minCount 1`, `sh:class cto:Task` (SHACL Core). V2: `sh:SPARQLConstraint` duyệt cấu trúc linkset gốc, OPTIONAL + `FILTER(!bound(?task))` | Listing 2–3, tr. 11 |
| R2 | Các công việc gắn cùng một cấu kiện không được chồng lấn thời gian | `sh:SPARQLConstraint`; lấy hai công việc liên kết với `$this`, đọc `prov:startedAtTime`, `prov:endedAtTime`, `FILTER(!sameTerm(...))` và `FILTER((?start1 < ?end2) && (?start2 < ?end1))` | Listing A.1–A.2, tr. 17–18 |
| R3 | Công việc cho tường BTCT chịu lực không được kéo dài quá hệ số năng suất trung bình | `sh:SPARQLConstraint`; lọc `beo:Wall`, `props:loadBearing_simple true`, lấy thể tích; tính giờ thực hiện bằng `BIND`, chia cho thể tích, `FILTER(?hoursPerVolume > 2.5)` | Listing B.1–B.2, tr. 19–20 |

- (a) Các luật được tạo thủ công để kiểm tiến độ trên nền BIM và "được đánh giá cùng một đối tác công nghiệp"; biểu thức
  SPARQL được thử trên dữ liệu trước rồi mới đưa vào cấu trúc SHACL (tr. 9).
- (a) Mỗi luật có hai biến thể: trên dữ liệu đã suy ra (dùng tiền tố `icddl`) và trên dữ liệu gốc (tr. 9).

**Ontology dùng (tr. 8, Bảng 1).** ICDD Container và Linkset (ISO 21597-1), ExtendedLinkset (ISO 21597-2), ICDDL (mới, của
bài); BOT (cấu kiện, cấu trúc không gian); PROPS và BEO (thuộc tính mức L1 và loại cấu kiện sinh từ IFC); CTO (công việc thi
công); **PROV-O dùng để biểu diễn thời điểm bắt đầu và kết thúc của công việc** (tr. 8).

**Chuỗi công cụ (tr. 6–8).** TopBraid SHACL API cho Java bản 1.4.0 (trên Apache Jena 4.2.0) cho bước suy ra; jena-shacl
(Apache Jena 4.4.0) cho bước kiểm; JMH 1.35 để đo; OpenJDK 18.0.1.1, 24 GB RAM, Intel i7-10750H, Windows 11. Dữ liệu: mô
hình IFC2X3 xuất từ Revit 2020 (và tệp Duplex của buildingSMART), tiến độ từ Rillsoft Project 8.1 xuất MS-Project-XML, liên
kết tạo bằng DESITE BIM 2.8.7, chuyển vào ICDD qua ICDD REST API; IFC → RDF bằng IFC-to-LBD Converter, XML → RDF bằng bộ
chuyển MSPROJ-XML-to-LBD do tác giả viết (tr. 8). Dữ liệu, luật và mã nguồn công bố mở (tr. 2, 16).

- **[NCS]** Bài **không dùng pySHACL**; việc luận án dùng pySHACL (Python) là chuyển giao sang công cụ khác, không có căn cứ
  hiệu năng từ bài này. Bài tự nhấn mạnh kết quả chỉ áp cho bộ xử lý Jena đã dùng (tr. 14).

## 3. Ca nghiên cứu và đánh giá

**Dữ liệu (tr. 8–9, Bảng 2).** Bốn vật chứa: ① Garage (9 cấu kiện, 8 công việc), ② Apartment Building (93; 15), ③ Duplex
Building (147; 115), ④ Office Building (832; 55). Số liên kết nhị phân lần lượt 9, 93, 219, 959 (bộ ba: 266; 2.702; 6.356;
27.816); dùng Directed1ToNLink giảm số bộ ba 24 %, 49 %, 35 %, 49 %, trung bình 40 % (tr. 9).

**Thiết lập đo (tr. 7–8).** Ba lượt: (1) suy ra thuộc tính liên kết, (2) kiểm trên dữ liệu đã suy ra, (3) kiểm trên dữ liệu
gốc. Chế độ thời gian trung bình, 20 lần lặp, 5 lần khởi động JVM không tính; nạp dữ liệu trước khi đo; dừng đo trước khi ghi
báo cáo kiểm (tr. 8, 12).

**Kết quả suy ra (tr. 10–11, Bảng 3).** Ví dụ ① Garage: 15,104 ms (liên kết nhị phân); ④ Office: 2.507,041 ms (nhị phân),
601,849 ms (1-n). Số bộ ba suy ra: 18; 126; 336; 1.622, không tỷ lệ với số liên kết vì một số cấu kiện được liên kết
(ví dụ phần tử lỗ mở trong tường IFC) **không có trong dữ liệu RDF**, nên các liên kết đó không suy ra được (tr. 11).

**Kết quả kiểm (tr. 12–16, Hình 11–12, Bảng 4).**
- ① Garage, R1: 0,142 / 0,138 / 0,135 ms trên dữ liệu đã suy ra so với 1,088 / 1,095 / 0,998 ms trên dữ liệu gốc (tr. 12).
- Cách viết truy vấn quyết định thời gian: phiên bản đầu kết hợp đường thay thế và chuỗi đường vượt 60.000 ms ở ④ (quá
  thời hạn); viết lại bằng bộ ba thường giảm hơn 90 %, còn 2.251,192 ms (tr. 12). Truy cập phần tử liên kết bằng vị từ cụ
  thể thay cho biến giảm R2,V2 ở ④ (1-n) từ 717,161 ms xuống 135,359 ms (81 %) (tr. 14). [NCS] Bài viết "717, 161ms" và
  "135, 359ms" (dấu phẩy kèm khoảng trắng); đọc là phần thập phân theo ký hiệu tiếng Anh (717.161 ms), vì tác giả nói mọi
  thời gian kiểm không vượt 2,5 s (tr. 16); cần cẩn trọng khi dẫn.
- SHACL Core tiết kiệm 61,3 % thời gian so với SHACL-SPARQL cho R1 trên bốn tập đã suy ra; tác giả nhấn mạnh chỉ áp cho dữ
  liệu và bộ xử lý Jena này (tr. 14).
- Cộng cả thời gian suy ra thì lợi ích chỉ xuất hiện từ tập ③ trở lên (ví dụ R1 ở ③: chênh 120,00 ms > 104,88 ms thời gian
  suy ra); ở ① không có lợi (tr. 14–15).
- Thời gian kiểm không vượt 2,5 s trong toàn bộ phép đo, tác giả kết luận kiểm độ trễ thấp là khả thi khi suy ra liên kết
  trước (tr. 16).
- **Số vi phạm (Bảng 4, tr. 15):** R1: 0 / 30 / 39 / 1; R2: 0 / 0 / 0 / 0; R3: 0 / 0 / 7 / 0 (theo tập ①–④). Tác giả nêu
  vi phạm R1 có thể chỉ ra tiến độ chưa xong hoặc cấu kiện bị bỏ sót khi lập tiến độ (tr. 9).

**Khuyến nghị của tác giả (tr. 16):** khai thác SHACL cho nội dung vật chứa, không chỉ cho sự phù hợp vật chứa; ưu tiên SHACL
Core khi viết được; viết truy vấn càng cụ thể càng nhanh; định danh dạng chuỗi khó dùng với dữ liệu liên kết, nên dùng định
danh URI; chọn kiểu liên kết ảnh hưởng thời gian suy ra và kiểm.

## 4. Luận điểm chính

1. Kiểm liên kết giữa thực thể của các tài liệu khác miền trong vật chứa ICDD là khả thi bằng SHACL (RQ1; tr. 15).
2. Suy ra thuộc tính liên kết trực tiếp (ICDDL) bằng luật SHACL làm luật kiểm ngắn hơn và người viết luật không cần biết cấu
   trúc linkset (RQ2–RQ3; tr. 15–16).
3. Dữ liệu đã suy ra kiểm nhanh hơn; lợi ích ròng chỉ có với tập lớn hoặc khi chạy nhiều shape (RQ4; tr. 15–16).
4. Cách viết shape (Core hay SPARQL, độ cụ thể của truy vấn), kiểu liên kết và kích thước ảnh hưởng mạnh đến thời gian
   (RQ5; tr. 12, 14, 16).

## 5. Giới hạn

| ID | Loại | Giới hạn | Trang |
|---|---|---|---|
| L1 | (b) | Các luật được tạo cho phép đo, không áp được cho mọi việc lập tiến độ, mọi dự án, mọi giai đoạn; luật phức tạp hơn nằm ngoài phạm vi | tr. 9 |
| L2 | (b) | Không dùng chỉ mục RDF; cần nghiên cứu thêm với kho bộ ba có chỉ mục | tr. 7–8, 14 |
| L3 | (b) | Không nhằm so sánh các bộ xử lý SHACL; con số (ví dụ 61,3 %) chỉ áp cho dữ liệu và bộ xử lý Jena này | tr. 14, 16 |
| L4 | (b) | Chưa ước được ảnh hưởng của số vi phạm đến thời gian kiểm; cần nghiên cứu thêm | tr. 14 |
| L5 | (b) | QueryBasedIdentifier không xét vì thiếu ca ứng dụng; định danh dạng chuỗi chỉ dùng được với thuộc tính mức L1 | tr. 4, 6, 16 |
| L6 | (b) | Lợi ích của suy ra chỉ có với tập dữ liệu lớn hoặc để dễ viết luật; dữ liệu phải qua bước suy ra trước khi kiểm | tr. 16 |
| L7 | (b) | Hướng tiếp: suy luận RDFS/OWL, SHACL-js, so sánh các cài đặt khác, mở rộng cơ chế liên kết của ICDD, đánh giá các ca sử dụng khác | tr. 16 |
| L8 | [NCS] | Đánh giá là **hiệu năng** (thời gian), không phải **tính đúng** của việc phát hiện: không có lỗi gài sẵn, không có tập lỗi chuẩn, không báo độ nhạy hay báo động giả; Bảng 4 chỉ đếm vi phạm, không đối chiếu vi phạm nào là lỗi thật | tr. 9, 15 |
| L9 | [NCS] | Việc "đánh giá cùng đối tác công nghiệp" không được mô tả (ai, tiêu chí, kết quả) | tr. 9 |
| L10 | [NCS] | Dữ liệu thiết kế – tiến độ, tĩnh; liên kết không có khoảng hiệu lực hay lịch sử; phiên bản và nguồn gốc chỉ được nêu là chú thích trong `index.rdf`, không có luật nào kiểm chúng | tr. 4, 8 |
| L11 | [NCS] | Luật R3 tính số giờ bằng `DAY(end) − DAY(start)` nhân 8 cộng chênh giờ, phút; cách tính này chỉ đúng khi hai mốc cùng tháng và ngày làm việc 8 giờ (suy từ Listing B.1–B.2) | tr. 19–20 |
| L12 | [NCS] | Một số lỗi trình bày: shape của Listing A.2 vẫn mang tên `R2_V1`; luật R3 được đặt tên `R4_V1`, `R4_V2` trong Listing B.1–B.2; ghi "ISO 29157" (tr. 5) và "ISO 21587-1" (tr. 4) thay cho ISO 21597; số liệu "717, 161ms" có dấu phẩy gây nhầm | tr. 4, 5, 14, 18–20 |

## 6. Đoạn dùng được cho tiểu luận

| # | Ý (diễn đạt lại, không trích nguyên văn) | Trang | Loại | Dùng ở |
|---|---|---|---|---|
| D1 | Kiểm tra luật trong xây dựng chủ yếu nhắm vào mô hình một miền; liên kết giữa dữ liệu các miền ít được nghiên cứu | tr. 1–2 | (a) | 3.5 |
| D2 | Tính đúng của liên kết giữa dữ liệu do nhiều bên cung cấp là điều kiện để diễn giải đúng quan hệ giữa chúng | tr. 2 | (a) | 3.5, 5.5 |
| D3 | Phân ba cấp kiểm: lược đồ vật chứa, dữ liệu miền, liên kết giữa thực thể | tr. 5, Hình 5 | (a) | 5.5, 5.7 (khung cấp kiểm) |
| D4 | Luật "mỗi cấu kiện phải liên kết ít nhất một công việc" viết được bằng SHACL Core (`sh:minCount`, `sh:class`) | tr. 9, 11 | (a) | 5.5 (tiền lệ cho C1) |
| D5 | Ràng buộc so sánh khoảng thời gian giữa các thực thể liên kết (không chồng lấn) viết được bằng SHACL-SPARQL trên thuộc tính thời gian của PROV-O | tr. 9, 17–18 | (a) | 5.5 (tiền lệ kỹ thuật cho C3, C9) |
| D6 | Kiểm trên bốn vật chứa dữ liệu thật (đến 27.816 bộ ba) đều dưới 2,5 s | tr. 9, 16 | (a) | 5.7 (khả thi về chi phí tính toán) |
| D7 | Khuyến nghị dùng định danh URI thay cho định danh dạng chuỗi; ưu tiên SHACL Core | tr. 16 | (a) | 5.5 (chọn định danh) |
| D8 | Đánh giá của bài là hiệu năng, chưa phải độ nhạy phát hiện lỗi | tr. 9–16 | [NCS] | 5.7 (lý do luận án đo M2.1, M2.2 bằng lỗi gài mù) |

## 7. Liên hệ với ràng buộc C1–C9 của luận án

Mức: **có tiền lệ** = bài trình bày một luật SHACL cùng dạng; **tương tự** = bài có kỹ thuật dùng được, nhưng nội dung ràng
buộc khác; **không** = bài không có. Mọi đánh giá "tương tự" và "dùng được" là **[NCS]**.

| Ràng buộc | Mức | Căn cứ trong bài | Phần luận án phải tự làm |
|---|---|---|---|
| C1 không mồ côi | **Có tiền lệ** | R1: mỗi `bot:Element` phải có ít nhất một liên kết tới `cto:Task` (`sh:minCount 1`, `sh:class`), cả bản Core và bản SPARQL; vi phạm đếm được (Bảng 4) (tr. 9, 11, 15). Thêm: liên kết trỏ tới cấu kiện không có trong RDF được phát hiện gián tiếp ở bước suy ra (tr. 11), không thành luật | Áp cho EVIDENCE–COMPONENT, EVIDENCE–VALIDITY_SCOPE; luật cho liên kết "treo" (trỏ tới thực thể không tồn tại) |
| C2 ID duy nhất | Không | V1 (kiểm số lượng theo ontology chuẩn) chỉ được mô tả, không trình bày luật duy nhất hay đo (tr. 5) | Toàn bộ |
| C3 thời điểm quan trắc trong hiệu lực ánh xạ | **Tương tự** | R2 so sánh khoảng [`prov:startedAtTime`, `prov:endedAtTime`] của hai thực thể nối với cùng cấu kiện bằng `FILTER` trong `sh:SPARQLConstraint` (tr. 9; Listing A.1–A.2, tr. 17–18). R2 là kiểm **chồng lấn** giữa hai khoảng, C3 là kiểm **chứa** một thời điểm trong một khoảng | Đổi điều kiện thành `valid_from ≤ t ≤ valid_to` qua SENSOR_MAPPING; xử lý `valid_to` để trống (ánh xạ còn hiệu lực) |
| C4 khớp phiên bản mô hình | Không | Phiên bản và nguồn gốc được chú thích trong `index.rdf` (tr. 4); không có luật kiểm | Toàn bộ |
| C5 dùng ngoài phạm vi phải có lý do | Tương tự (yếu) | R3 là luật có điều kiện: chỉ áp khi cấu kiện là tường chịu lực, rồi kiểm một giá trị tính được (tr. 9; Listing B.1–B.2, tr. 19–20). Dạng "nếu A thì phải có B" mã hóa được theo cùng khuôn | Luật: nếu `within_scope = false` thì `justification` bắt buộc |
| C6 bước chuyển có căn cứ, đúng thẩm quyền | Không | Không có tác nhân, vai trò, thẩm quyền | Toàn bộ (tiền lệ khuôn ở [44]) |
| C7 bước chuyển hợp lệ theo máy trạng thái | Không | Không có trạng thái hay sự kiện chuyển | Toàn bộ |
| C8 bằng chứng cảm biến có OBS_CONTEXT, method_version | Tương tự | Kiểm sự có mặt và kiểu của thuộc tính bắt buộc bằng `sh:property` + `sh:minCount` + `sh:class` (Listing 2, tr. 11); không có dữ liệu cảm biến | Áp cho EVIDENCE loại cảm biến; luật có điều kiện theo `evidence_type` |
| C9 sự kiện chuyển trỏ tới phiên bản bằng chứng còn hiệu lực | Tương tự (một phần) | Kỹ thuật nối hai thực thể qua liên kết rồi so sánh thời điểm (R2, tr. 17–18) dùng được; không có phiên bản, không có quan hệ thay thế hay vô hiệu hóa | Luật kết hợp `prov:wasRevisionOf`/`prov:wasInvalidatedBy` với thời điểm của STATUS_EVENT |

**[NCS] Tóm lại:** bài là tiền lệ kỹ thuật cho việc **viết ràng buộc C1, C3, C5, C8, C9 bằng SHACL** trên dữ liệu liên kết
nhiều miền, gồm ràng buộc thời gian dạng so sánh khoảng (R2). Bài không có tiền lệ cho các ràng buộc về phiên bản (C4),
thẩm quyền (C6) và máy trạng thái (C7), vì dữ liệu của bài không có các khái niệm này. Bài cũng cho thấy chi phí tính toán
của kiểm SHACL ở quy mô hàng chục nghìn bộ ba là thấp (tr. 16), nhưng chưa đo khả năng phát hiện lỗi; đây là phần luận án
đo bằng M2.1–M2.2 với lỗi gài mù.

## 8. Kiểm phản chứng

| Ứng viên | Kết luận | Căn cứ |
|---|---|---|
| **UV-02** (nguồn gốc, phiên bản phương pháp, phạm vi hiệu lực của đầu ra phát hiện) | **Không giải quyết** | Không có đầu ra phát hiện hay dữ liệu đo. Nguồn gốc và phiên bản chỉ được nêu là chú thích ở mức vật chứa trong `index.rdf` (tr. 4); PROV-O chỉ dùng cho thời điểm bắt đầu, kết thúc công việc (tr. 8). Không đổi phát biểu đã thu hẹp của UV-02. |
| **UV-03** (ghép cảm biến – cấu kiện có thời hạn) | **Không giải quyết** (đóng góp công cụ cho phần còn lại) | Liên kết ICDD giữa thực thể hai miền là tĩnh, không có khoảng hiệu lực hay lịch sử (tr. 4–5, Hình 4; suy từ việc lược đồ linkset không có thuộc tính thời gian — [NCS]); không có cảm biến. Tuy vậy, bài cho thấy kiểm liên kết giữa thực thể khác miền (tr. 9–11) và so sánh khoảng thời gian trên thực thể liên kết (R2, tr. 17–18) viết được bằng SHACL-SPARQL. [NCS] Điều này **củng cố** đánh giá đã ghi ở UV-03: phần còn lại là một hồ sơ áp dụng và một ràng buộc (C3), và ràng buộc đó có tiền lệ kỹ thuật để cài đặt; không đổi phát biểu đã thu hẹp. |

## 9. Vị trí sử dụng trong tiểu luận v2

- 3.5: dẫn [21] cho nhận định liên kết giữa dữ liệu nhiều miền cần được kiểm và đã kiểm được bằng SHACL trên vật chứa ICDD
  (tr. 1–2, 15).
- 5.5: dẫn [21] như tiền lệ kỹ thuật khi trình bày C1–C9 bằng SHACL (C1 theo R1; ràng buộc thời gian theo R2); nêu rõ
  phần mới là nội dung ràng buộc (hiệu lực ánh xạ, phiên bản bằng chứng, thẩm quyền, máy trạng thái), không phải kỹ thuật
  SHACL.
- 5.7: dẫn [21] cho khả thi về chi phí tính toán (dưới 2,5 s; tr. 16); phân biệt với chỉ số tính đúng mà luận án đo.
- Không dẫn các con số thời gian chi tiết; không dẫn khuyến nghị về kiểu liên kết ICDD (ngoài phạm vi).
