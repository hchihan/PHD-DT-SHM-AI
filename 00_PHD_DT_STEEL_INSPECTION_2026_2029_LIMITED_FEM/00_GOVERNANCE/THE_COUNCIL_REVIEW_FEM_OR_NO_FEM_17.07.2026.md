# THE COUNCIL REVIEW — FEM OR NO FEM
**Đối tượng đánh giá:** BaoCao_NCS_T7.2026_HoChiHan (UPDATED) + Outline luận án hiện hành
**Câu hỏi trung tâm:** Loại RSAP/FEM khỏi trục nghiên cứu chính làm luận án yếu đi, hay giúp luận án phù hợp ngành Quản lý xây dựng (QLXD) và giảm rủi ro bảo vệ?
**Ngày lập:** 17/07/2026

---

# PHẦN 1 — KẾT LUẬN ĐIỀU HÀNH

**Khuyến nghị: PHƯƠNG ÁN B — hạ FEM xuống vai trò công cụ hỗ trợ giới hạn, đồng thời tiếp nhận gần như toàn bộ kiến trúc không-FEM đang đề xuất (Mục 8 của đề bài) làm khung xương luận án.**

Lý do loại A: Giữ FEM là trục lõi buộc luận án phải vượt qua một Evidence Gate "baseline FEM đã hiệu chuẩn với tiêu chí chấp nhận" (đang ghi ở Mốc 3 và Chương 5 của báo cáo). Đây là một dự án Kỹ thuật kết cấu thu nhỏ: hiệu chỉnh mô hình khung 1:10 với liên kết bu lông đòi hỏi thí nghiệm modal độc lập (EMA), định lượng độ cứng liên kết, MAC, và đặc biệt là **luật đồng dạng (similitude) để chuyển từ 1:10 sang công trình thực** — điểm mà một hội đồng có chuyên gia kết cấu gần như chắc chắn sẽ khai thác và luận án khó trả lời trọn vẹn trong thời gian còn lại. FEM lõi cũng kéo đóng góp lệch khỏi ngành QLXD.

Lý do loại C: Loại FEM hoàn toàn tạo ra ba mâu thuẫn không cần thiết: (1) Báo cáo Paper 1 đã công khai hứa "Paper 2 dùng FEM giải thích các nhầm lẫn class" — hai anomaly (BCJ sụp đổ dưới S2; nhầm lẫn Apex↔BCJ) sẽ thành câu hỏi mồ côi; (2) Đề tài cấp tỉnh cam kết sản phẩm có "FEM tham chiếu" và "cảm biến tại vị trí tối ưu theo diễn giải cơ học" — NCS không thể vừa nói FEM vô dụng trong luận án vừa bán FEM cho tỉnh; (3) mất cơ sở kỹ thuật rẻ nhất để biện minh vị trí đặt cảm biến hiện trường. C tiết kiệm rất ít so với B nhưng bỏ đi một tài sản phòng thủ giá thấp.

**Phương án B cụ thể:** FEM là **mô hình tham chiếu danh nghĩa (nominal), không hiệu chuẩn, không có RQ riêng, không có chương riêng, không có Paper riêng, không là Evidence Gate**. FEM chỉ được dùng để: (i) biện minh sơ bộ vị trí đặt cảm biến hiện trường; (ii) minh họa vị trí cấu kiện; (iii) nêu giả thuyết cơ học định tính cho các anomaly của Paper 1 trong phần Discussion/Limitation. Chuỗi định danh lõi bỏ FEM_Node_ID: **Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status**; ánh xạ FEM node là metadata tùy chọn.

**Rủi ro lớn nhất của B: "FEM xác sống".** Chỉ cần FEM xuất hiện, một phản biện kết cấu có thể hỏi "mô hình đã hiệu chuẩn chưa, MAC bao nhiêu?". Nếu NCS trả lời lấp lửng, B sụp thành A với đầy đủ rủi ro của A.

**Điều kiện để B đứng vững:** (1) Ngôn ngữ kỷ luật tuyệt đối — mọi lần nhắc FEM đều kèm "nominal, uncalibrated, reference-only, not used for damage diagnosis"; (2) FEM chỉ xuất hiện trong một tiểu mục phương pháp và phần Limitation, không xuất hiện trong tên RQ/chương/Paper/Evidence Gate; (3) danh mục Prohibited claims được viết thành văn (Phần 5); (4) sự đồng thuận bằng văn bản của cả hai thầy hướng dẫn trước khi nộp chuyên đề tổng quan tháng 7/2026.

---

# PHẦN 2 — Ý KIẾN ĐỘC LẬP CỦA TỪNG THÀNH VIÊN

## 2.1. Chuyên gia Quản lý xây dựng & quản lý tài sản công trình

- **Claim:** Đóng góp bảo vệ được của luận án này nằm ở *quy trình quản lý thông tin và hỗ trợ quyết định kiểm tra*, không nằm ở mô hình cơ học. FEM lõi làm loãng định vị ngành.
- **Evidence:** Chính hội đồng trước đã yêu cầu "làm nổi bật ngành QLXD" (slide góp ý, nhóm 1). Tên đề tài mới đã chuyển sang "Data-informed... Inspection-Maintenance Support". NĐ 207/2026 và TT 32/2026 đặt yêu cầu về *hồ sơ bảo trì và quan trắc* — đúng địa hạt quản lý, không yêu cầu FEM hiệu chuẩn.
- **Limitation:** Không nắm quy chế đào tạo cụ thể của cơ sở về mức độ nội dung kỹ thuật bắt buộc trong luận án QLXD — *insufficient evidence*.
- **Recommendation:** Chọn B. Đưa toàn bộ ngôn ngữ luận án về trục "evidence → traceability → inspection decision". Đồng thuận với chuyên gia 2 và 5; bất đồng nhẹ với chuyên gia 4 về mức giữ lại FEM.

## 2.2. Chuyên gia Digital Twin / BIM / quản lý thông tin công trình

- **Claim:** Digital Twin không bắt buộc phải có FEM. Một DT ở mức trưởng thành "descriptive–diagnostic" (mô tả – hỗ trợ chẩn đoán ở cấp quản lý) với dữ liệu cảm biến + BIM + hồ sơ kiểm tra là hợp lệ trong tài liệu, miễn là luận án **tự định nghĩa rõ mức trưởng thành và không tuyên bố predictive**.
- **Evidence:** Chuỗi định danh Sensor_ID → BIM_GUID là ánh xạ trực tiếp, không cần FEM_Node_ID làm trung gian về mặt logic dữ liệu; FEM_Node_ID trong báo cáo hiện tại thực chất là một pivot *tùy chọn*, không phải mắt xích bắt buộc. TCVN 14177:2024 (định danh tài sản) đã được đề tài tỉnh viện dẫn — đủ nền cho mô hình dữ liệu.
- **Limitation:** Một bộ phận reviewer quốc tế vẫn đồng nhất DT với physics-based model; rủi ro tranh cãi thuật ngữ tồn tại ở cả B lẫn C.
- **Recommendation:** B hoặc C đều chấp nhận được về mặt DT; nghiêng B vì FEM danh nghĩa giúp trả lời câu hỏi "vì sao đặt cảm biến ở đó" mà không tốn thêm chi phí kiểm chứng. Yêu cầu bắt buộc: chương khung nghiên cứu phải có một mục "Định nghĩa và mức trưởng thành Digital Twin trong luận án này".

## 2.3. Chuyên gia giám sát trạng thái bằng dữ liệu dao động

- **Claim:** Giá trị khoa học chắc chắn nhất hiện có của luận án là Paper 1 (sensor configuration dominates architecture; run-aware protocol). Mọi quyết định kiến trúc phải bảo vệ tài sản này trước, và không được để tranh luận FEM che khuất hai việc đang chặn Paper 1.
- **Evidence:** LORO cross-validation chưa chạy; chế độ cảm biến của ResNet1D chưa xác nhận — nhưng slide Paper 1 vẫn liệt kê ResNet1D trong danh sách mô hình so sánh. Đây là rủi ro trình bày ngay trong báo cáo hiện tại, độc lập với câu hỏi FEM.
- **Limitation:** Không đánh giá được liệu dữ liệu 6 runs có đủ cho LORO ổn định — kết quả LORO sẽ quyết định.
- **Recommendation:** Ủng hộ B/C như nhau về mặt tín hiệu; nhưng cảnh báo: nếu loại FEM (C), hai anomaly của Paper 1 phải được đóng khung lại thành "open question / limitation", tuyệt đối không hứa cơ chế giải thích ở Paper nào nữa. Với B, được phép nêu *giả thuyết định tính* từ mô hình danh nghĩa, có nhãn "hypothesis, not confirmed".

## 2.4. Chuyên gia kết cấu thép & FEM (phản biện rủi ro kỹ thuật)

- **Claim (bất đồng một phần với hội đồng):** Loại FEM hoàn toàn là vứt bỏ ngôn ngữ cơ học tối thiểu mà một luận án về kết cấu thép — dù thuộc ngành QLXD — vẫn nên có. Nhưng giữ FEM *lõi* thì tôi, trong vai phản biện, sẽ đánh sập được.
- **Evidence (vì sao A sập):** (1) Hiệu chuẩn khung 1:10 liên kết bu lông cần EMA độc lập + model updating; báo cáo chưa có kế hoạch EMA. (2) "Suy giảm độ cứng tương đương" mô phỏng nới lỏng bu lông là giả định cần biện minh bằng dữ liệu siết lực — chưa có. (3) Similitude động lực học 1:10 → nhà thực (trọng lực không scale, tỷ số cản khác, liên kết không đồng dạng) là câu hỏi không có câu trả lời gọn trong khuôn khổ này. (4) Kinh nghiệm từ hồ sơ Rapexco: ngay ở công trình thực, mô hình ETABS cũng chỉ dám nhận là "mô hình đại diện, không phải đo kiểm" — tức chính nhóm nghiên cứu đã biết giới hạn này.
- **Limitation:** Thành phần hội đồng bảo vệ thực tế chưa biết — *insufficient evidence*; mức độ khắt khe là dự phóng từ nhận xét của thầy hướng dẫn.
- **Recommendation:** B, dứt khoát không A, và phản đối C. FEM danh nghĩa (mô hình thiết kế, không hiệu chuẩn) dùng cho sensor placement là thực hành công nghiệp bình thường, dễ bảo vệ: "chúng tôi dùng mô hình thiết kế để chọn vị trí đo, như mọi đơn vị tư vấn quan trắc vẫn làm; chúng tôi không tuyên bố chẩn đoán từ mô hình."

## 2.5. Chuyên gia phương pháp nghiên cứu & chiến lược công bố

- **Claim:** Cấu trúc 3-paper không FEM là *hoàn thành được* và đủ cho luận án; điểm yếu duy nhất là Paper 2 thay thế có nguy cơ bị chê "system integration". Nguy cơ này khắc phục được bằng thiết kế kiểm chứng, không cần FEM.
- **Evidence:** Paper 1 độc lập với FEM. Paper 3 (field feasibility) độc lập với FEM. Chỉ Paper 2 đổi bản chất: từ FEM-interpretation sang traceability framework — thể loại này có đường công bố thật ở Automation in Construction, ITcon, Buildings, JCSHM *nếu* có mô hình dữ liệu hình thức + tiêu chí đánh giá + kiểm chứng kịch bản (chi tiết Phần 6).
- **Limitation:** Xác suất chấp nhận ở tạp chí Q1/Q2 của Paper 2 mới thấp hơn Paper 2 FEM làm *tốt* — nhưng Paper 2 FEM làm tốt là giả định phi thực tế với nguồn lực hiện có; so sánh đúng phải là "Paper 2 traceability khả thi" vs "Paper 2 FEM rủi ro cao trễ 12 tháng".
- **Recommendation:** B (C cũng chấp nhận được về công bố). Ưu tiên tuyệt đối: khóa LORO + ResNet1D trước, quyết định kiến trúc sau đó một tuần cũng không muộn — nhưng chuyên đề tổng quan deadline T7/2026 buộc phải chốt kiến trúc ngay, nên chốt B bây giờ.

**Điểm đồng thuận:** Không ai chọn A. Cả 5 đồng ý FEM không được là Evidence Gate, không có chương/Paper riêng.
**Điểm bất đồng:** Chuyên gia 4 phản đối C (mất ngôn ngữ cơ học tối thiểu); chuyên gia 2 và 5 coi B/C tương đương và nghiêng B chỉ vì chi phí thấp; chuyên gia 1 nghiêng B vì tính nhất quán với đề tài tỉnh.

---

# PHẦN 3 — MA TRẬN SO SÁNH BA PHƯƠNG ÁN

Thang 1–5 (5 = tốt nhất / rủi ro thấp nhất).

| Tiêu chí | A (FEM lõi) | B (FEM hỗ trợ) | C (loại FEM) | Giải thích ngắn |
|---|---|---|---|---|
| Phù hợp ngành QLXD | 2 | 4 | 5 | A kéo trọng tâm sang kỹ thuật kết cấu; C thuần quản lý; B gần C |
| Tính mới | 3 | 4 | 3 | FEM 1:10 hiệu chuẩn là đóng góp incremental trong SE; B/C dồn tính mới vào chuỗi evidence→traceability→decision; C mất lớp diễn giải nên khó phân biệt với tích hợp phần mềm hơn B |
| Chuỗi bằng chứng | 4 | 4 | 3 | A đầy đủ nhưng mắt xích FEM mong manh; B giữ liên tục nhờ giả thuyết cơ học định tính; C có khoảng trống "vì sao tin cảnh báo chỉ đúng cấu kiện đó" |
| Khả năng kiểm chứng | 2 | 4 | 4 | Tiêu chí chấp nhận FEM (MAC, sai số tần số) của A rất khó đạt và phải công bố trước; B/C chỉ kiểm chứng những gì đo được |
| Rủi ro kỹ thuật (bị phản biện sâu) | 1 | 4 | 4 | A mở toàn bộ mặt trận EMA/MAC/similitude; B còn rủi ro "FEM xác sống" nhưng kiểm soát được bằng ngôn ngữ; C còn rủi ro "DT không physics?" |
| Tính khả thi | 2 | 4 | 5 | A thêm ~9–12 tháng công việc kiểm chứng; B thêm gần như 0; C bớt việc viết lại vài tài liệu |
| Tính thống nhất luận án | 3 | 4 | 4 | Chương FEM của A dễ thành ốc đảo; B/C có trục duy nhất evidence→traceability→decision |
| Tính hợp lệ Digital Twin | 5 | 4 | 3 | A dễ bảo vệ chữ "twin" nhất; B có physics tham chiếu; C phải tự định nghĩa mức trưởng thành DT và chịu tranh cãi thuật ngữ |
| Khả năng công bố (3 bài độc lập) | 3 | 4 | 3 | Paper 2 FEM của A chịu chuẩn cao của tạp chí kết cấu; Paper 2 traceability của C rủi ro "integration"; B cho phép Paper 2 traceability có thêm mục thảo luận cơ học định tính làm dày đóng góp |
| Giá trị ứng dụng | 3 | 4 | 4 | Doanh nghiệp cần hồ sơ số + quy trình kiểm tra, không cần FEM hiệu chuẩn; B khớp đúng sản phẩm "FEM tham chiếu" của đề tài tỉnh |
| **Tổng** | **28** | **40** | **38** | |

**Giải thích các chênh lệch lớn:**
- *Khả năng kiểm chứng & Rủi ro kỹ thuật (A=2/1 vs B,C=4):* đây là hai tiêu chí quyết định. A tự đặt ra nghĩa vụ chứng minh (calibration acceptance) mà dữ liệu và thời gian hiện tại không gánh nổi; B và C chỉ tuyên bố những gì kiểm chứng được.
- *Chuỗi bằng chứng & Tính hợp lệ DT (C=3 vs B=4):* khác biệt duy nhất khiến B thắng C. Không có bất kỳ lớp cơ học nào, C phải trả lời "vì sao đặt cảm biến ở vị trí này" và "twin của cái gì" chỉ bằng lập luận quản lý — làm được nhưng mỏng hơn.
- *Tính khả thi (C=5 vs B=4):* chênh 1 điểm vì B đòi kỷ luật ngôn ngữ và một tiểu mục phương pháp; chi phí nhỏ, không phải lý do chọn C.

---

# PHẦN 4 — RED TEAM REVIEW

## 4.1. Mười câu hỏi đánh phương án GIỮ FEM (A)

1. Mô hình FEM của khung 1:10 đã được hiệu chuẩn bằng thí nghiệm modal độc lập nào? MAC và sai số tần số từng mode là bao nhiêu, tiêu chí chấp nhận công bố ở đâu, trước hay sau khi có kết quả?
2. Độ cứng xoay của liên kết bu lông trong mô hình lấy từ đâu — đo, tra bảng, hay giả định? Sai số của giả định đó lan truyền thế nào vào kết luận?
3. Điều kiện biên chân khung 1:10 (ngàm/khớp/semi-rigid) được xác nhận bằng gì?
4. Anh mô phỏng "nới lỏng liên kết" bằng suy giảm độ cứng tương đương — căn cứ thực nghiệm nào cho hàm ánh xạ giữa lực siết bu lông và độ cứng tương đương?
5. Khối lượng cảm biến và dây dẫn chiếm bao nhiêu phần trăm khối lượng mô hình 1:10, đã hiệu chỉnh added-mass chưa?
6. Luật đồng dạng nào cho phép chuyển kết luận động lực học từ 1:10 sang nhà 25×80 m? Trọng lực, tỷ số cản và ứng xử liên kết có đồng dạng không?
7. Nếu FEM và dữ liệu đo mâu thuẫn, cái nào thắng, và quy tắc đó viết ở chương nào?
8. Ngành đào tạo là QLXD — đóng góp FEM này khác gì hàng trăm bài model-updating đã có trong Kỹ thuật kết cấu?
9. Evidence Gate "baseline FEM với tiêu chí chấp nhận" — nếu không đạt tiêu chí sau 6 tháng thì kế hoạch dự phòng của luận án là gì?
10. Chi phí thời gian của WP2 chiếm bao nhiêu phần trăm thời gian PhD còn lại, và Paper 1 đã xong LORO chưa mà chuyển nguồn lực sang FEM?

## 4.2. Mười câu hỏi đánh phương án LOẠI FEM (C)

1. Không có mô hình cơ học, anh dựa vào đâu để nói cảnh báo từ cảm biến X liên quan đến cấu kiện Y chứ không phải cấu kiện bên cạnh?
2. Vị trí đặt cảm biến ở công trình thực được chọn bằng tiêu chí gì — kinh nghiệm, tiện thi công, hay có cơ sở kỹ thuật?
3. Báo cáo Paper 1 của chính anh hứa Paper 2 dùng FEM giải thích nhầm lẫn Apex↔BCJ; giờ ai giải thích, hay anomaly bị bỏ rơi?
4. "Digital Twin" mà không có bất kỳ mô hình vật lý nào — anh định nghĩa twin thế nào để phân biệt với một cơ sở dữ liệu quan trắc có gắn BIM?
5. Đề tài cấp tỉnh của chính anh liệt kê sản phẩm "FEM tham chiếu" và "cảm biến tại vị trí tối ưu theo diễn giải cơ học" — luận án loại FEM thì ai làm phần đó, và tính nhất quán học thuật của NCS ở đâu?
6. Paper 2 mới về traceability khác gì một bài tích hợp Revit + database mà một kỹ sư phần mềm làm trong ba tháng?
7. Đơn vị phân tích của Paper 2 là gì, và biến đo lường nào cho phép nói framework "tốt hơn" hiện trạng?
8. Bốn mức Normal–Watch–Inspect–Priority Inspection được ngưỡng hóa bằng gì khi không có lớp diễn giải cơ học nào đứng giữa tín hiệu và hành động?
9. Không FEM, chương tổng quan vẫn viết khoảng trống "chưa có chuỗi dao động–FEM–BIM–hành động" (slide Chương 2) — anh sửa khoảng trống nghiên cứu hay sửa luận án cho khớp?
10. Nếu hội đồng có chuyên gia kết cấu hỏi một câu cơ học sơ đẳng về khung thép mà luận án không có lấy một mô hình tham chiếu, ấn tượng để lại là gì?

## 4.3. Phương án nào rủi ro bảo vệ thấp hơn?

**B thấp nhất.** A chịu 10 câu hỏi mục 4.1 mà phần lớn *không có câu trả lời tốt trong nguồn lực hiện tại*. C chịu 10 câu hỏi mục 4.2 — trong đó câu 1, 2, 3, 5 trả lời khá gượng. B vô hiệu hóa gần hết cả hai danh sách: các câu 4.1 được trả lời bằng "FEM trong luận án là mô hình tham chiếu danh nghĩa, không hiệu chuẩn, không dùng để chẩn đoán — do đó các yêu cầu MAC/EMA không áp dụng"; các câu 4.2 (1, 2, 3, 5) được trả lời bằng chính mô hình danh nghĩa đó. Câu hỏi nguy hiểm duy nhất còn lại với B là "đã có FEM sao không hiệu chuẩn luôn?" — trả lời chuẩn: "vì hiệu chuẩn không phục vụ câu hỏi nghiên cứu QLXD nào của luận án, và tuyên bố của chúng tôi không vượt quá mức danh nghĩa."

---

# PHẦN 5 — KIẾN TRÚC NGHIÊN CỨU KHUYẾN NGHỊ (B trên khung xương không-FEM)

| Thành phần | Nội dung khuyến nghị |
|---|---|
| **Central thesis statement** | Một khung Digital Twin dựa trên dữ liệu — tổ chức, liên kết và truy vết bằng chứng trạng thái từ dữ liệu dao động đến cấu kiện BIM và hồ sơ kiểm tra — có thể hỗ trợ lựa chọn hành động kiểm tra–bảo trì nhà công nghiệp khung thép một cách minh bạch và kiểm chứng được, ngay cả khi dữ liệu hư hỏng hiện trường hạn chế; mô hình FEM danh nghĩa chỉ đóng vai trò tham chiếu bố trí cảm biến, không phải nguồn chẩn đoán. |
| **Mục tiêu tổng quát** | Phát triển và kiểm chứng khung DT dựa trên dữ liệu cho giám sát trạng thái và hỗ trợ kiểm tra–bảo trì nhà công nghiệp khung thép, trên cơ sở mô hình thí nghiệm 1:10 và nghiên cứu trường hợp công trình thực. |
| **Mục tiêu cụ thể** | (1) Tạo bằng chứng trạng thái đáng tin cậy từ dữ liệu dao động lab với giao thức run-aware/LORO; (2) Xây dựng và hình thức hóa mô hình dữ liệu truy vết Sensor–BIM–Inspection; (3) Kiểm chứng tính khả thi truy vết và hỗ trợ kiểm tra tại công trình thực; (4) Tổng hợp thành logic 4 mức hành động. |
| **RQ1** | Giữ như đề xuất Mục 8: dữ liệu dao động 1:10 + cấu hình cảm biến tạo bằng chứng phân biệt trạng thái liên kết đáng tin cậy như thế nào? (thêm cụm "dưới giao thức chống rò rỉ run-aware") |
| **RQ2** | Giữ như đề xuất: bằng chứng trạng thái được tổ chức và liên kết với cấu kiện BIM và hồ sơ kiểm tra như thế nào để bảo đảm khả năng truy vết? (không nhắc FEM) |
| **RQ3** | Giữ như đề xuất: khung DT hỗ trợ lựa chọn và ghi nhận hành động kiểm tra tại công trình thực như thế nào trong điều kiện dữ liệu hư hỏng hiện trường hạn chế? |
| **WP1–WP4** | WP1 Lab vibration evidence (gồm LORO + xác nhận ResNet1D); WP2 BIM–Sensor–Inspection traceability (gồm thiết kế mô hình dữ liệu + tiêu chí đánh giá); WP3 Field feasibility & inspection support (gồm bố trí cảm biến có tham chiếu FEM danh nghĩa); WP4 Decision-support synthesis (4 mức hành động, case scenarios). |
| **Chương luận án** | C1 Mở đầu; C2 Tổng quan & khoảng trống (viết lại khoảng trống: "chưa có chuỗi truy vết đầy đủ *dao động → bằng chứng → cấu kiện BIM → hồ sơ kiểm tra → hành động*"); C3 Khung nghiên cứu & thiết kế kiểm chứng (gồm mục "Định nghĩa & mức trưởng thành DT" và tiểu mục "Vai trò giới hạn của mô hình FEM danh nghĩa"); C4 Lab evidence (Paper 1); C5 Traceability framework (Paper 2); C6 Field feasibility (Paper 3); C7 Decision-support framework (Paper 4/stretch); C8 Kết luận. *Không còn chương FEM.* |
| **Paper 1** | Giữ tên hiện tại (Run-Aware Evaluation...). Không đưa ResNet1D vào bản thảo cho tới khi xác nhận sensor mode; LORO là điều kiện nộp bài. |
| **Paper 2** | Xem Phần 6 — traceability framework, tên đề xuất ở đó. |
| **Paper 3** | Field Feasibility of a Data-Informed Digital Twin Framework for Condition-Based Inspection Support of an Industrial Steel Building (giữ như đề xuất). |
| **Evidence Gates** | G1: metadata khóa + LORO hoàn thành + ResNet1D mode xác nhận → nộp Paper 1. G2: mô hình dữ liệu truy vết v1 + bộ tiêu chí đánh giá công bố trước. G3: case study truy vết lab end-to-end đạt các tiêu chí G2. G4: bố trí cảm biến hiện trường + baseline vận hành + tối thiểu 3 kịch bản truy vết hiện trường. G5: case scenarios 4 mức hành động được chuyên gia/quản lý cơ sở đánh giá. *Không còn gate "FEM hiệu chuẩn".* |
| **Validation ladder** | V1 Lab validity (trạng thái kiểm soát phân biệt được, lặp lại qua LORO); V2 Traceability validity (chuỗi định danh đi hai chiều cảnh báo↔cấu kiện↔hồ sơ, đo bằng tiêu chí Phần 6); V3 Field feasibility (triển khai được, dữ liệu về, truy vết chạy trên công trình thực); V4 Decision validity (khuyến nghị minh bạch, giải thích được, được người quản lý cơ sở xác nhận hợp lý). |
| **Allowed claims** | "Bằng chứng trạng thái từ lab phân biệt được các trạng thái liên kết kiểm soát"; "cấu hình cảm biến ảnh hưởng mạnh hơn lựa chọn kiến trúc mô hình"; "khung truy vết liên kết được cảnh báo với cấu kiện và hồ sơ kiểm tra, kiểm chứng qua kịch bản"; "khung khả thi triển khai tại công trình thực"; "FEM danh nghĩa cung cấp tham chiếu bố trí cảm biến". |
| **Prohibited claims** | Chẩn đoán hư hỏng hiện trường khi chưa kiểm tra xác nhận; suy luận lực siết bu lông hoặc mức suy giảm độ cứng thực từ FEM; mọi tuyên bố dựa trên FEM đã hiệu chuẩn; chuyển kết luận định lượng 1:10 → công trình thực; severity/DSI ordinal; predictive maintenance/RUL; AI vượt trội chung; Health Index trọng số. |

---

# PHẦN 6 — ĐÁNH GIÁ PAPER 2 THAY THẾ

**Kết luận: đủ mạnh để công bố quốc tế NẾU và CHỈ NẾU được thiết kế như một nghiên cứu có mô hình dữ liệu hình thức và kiểm chứng đo được — không phải bản mô tả hệ thống.**

- **Research gap:** Các nghiên cứu Sensor–IFC/BIM-to-FEM hiện có (nhóm tài liệu Rio, Gradišar & Dolenc, Fawad, Zou đã rà soát trong báo cáo) tập trung vào tích hợp dữ liệu cảm biến vào BIM, nhưng thiếu (a) chuỗi định danh đi trọn từ *bằng chứng trạng thái đã kiểm soát rò rỉ* đến *hồ sơ kiểm tra và trạng thái hành động*, và (b) bộ tiêu chí đánh giá khả năng truy vết có thể tái lập. Khoảng trống là *evidence-to-action traceability*, không phải sensor-to-BIM integration.
- **Đơn vị phân tích:** một "traceability instance" — bộ ba (bằng chứng trạng thái, cấu kiện BIM, hồ sơ/hành động kiểm tra) và các truy vấn hai chiều trên đó.
- **Dữ liệu đầu vào:** bằng chứng trạng thái từ Paper 1 (lab, có nhãn); mô hình BIM khung 1:10 và công trình thực; hồ sơ kiểm tra mẫu; định danh tài sản theo TCVN 14177:2024/ISO 19650.
- **Mô hình dữ liệu:** schema hình thức hóa (lớp thực thể, quan hệ, ràng buộc định danh) trên nền IFC + bảng ánh xạ Sensor_ID→BIM_GUID→Condition_Evidence_ID→Inspection_Record_ID→Action_Status; triển khai tham chiếu (graph database hoặc quan hệ) chỉ là instrument, không phải đóng góp.
- **Phương pháp kiểm chứng:** (1) competency questions — bộ câu truy vấn nghiệp vụ định nghĩa trước ("cảnh báo E xuất phát từ cảm biến nào, cấu kiện nào, lần kiểm tra gần nhất khi nào, hành động đang ở trạng thái gì?"); (2) kịch bản truy vết end-to-end trên lab case và field case; (3) round-trip test cảnh báo→cấu kiện→hồ sơ→cảnh báo.
- **Tiêu chí đánh giá:** tỷ lệ competency questions trả lời đúng/đủ; tính toàn vẹn định danh (không mồ côi, không trùng); tính đầy đủ chuỗi (mọi evidence đều truy được về cấu kiện và ngược lại); chi phí thao tác so với quy trình hồ sơ phân tán hiện trạng (đo bằng số bước/thời gian trong kịch bản).
- **Đóng góp khoa học:** một mô hình dữ liệu truy vết được hình thức hóa + bộ tiêu chí đánh giá tái lập được cho lớp bài toán evidence-to-inspection trong quản lý tài sản nhà công nghiệp thép — generalizable vượt khỏi case study.
- **Nguy cơ "system integration" và cách hóa giải:** nguy cơ có thật nếu bài viết theo lối "chúng tôi kết nối Revit với database". Hóa giải: đặt competency questions và tiêu chí *trước* khi triển khai (pre-registered), trình bày schema như đóng góp chính, demo chỉ là kiểm chứng; thêm mục thảo luận giới hạn nêu rõ những gì framework *không* làm (không chẩn đoán, không severity).
- **Tên Paper 2 đề xuất:** *A Verifiable Component-Level Traceability Framework Linking Vibration-Based Condition Evidence to BIM Objects and Inspection Records for Industrial Steel Buildings.* (Từ khóa "verifiable" và "component-level" là hai điểm phân biệt với nhóm sensor-integration.)
- Tạp chí mục tiêu theo thứ tự: Automation in Construction (tham vọng), Journal of Information Technology in Construction (ITcon), Buildings (MDPI), Journal of Civil Structural Health Monitoring.

---

# PHẦN 7 — DANH SÁCH THAY ĐỔI TRONG BÁO CÁO HIỆN TẠI

(Số trang theo thứ tự slide trong PDF.)

| Trang | Nội dung hiện tại | Giữ / Sửa / Xóa | Nội dung thay thế |
|---|---|---|---|
| 3 | Chuỗi thống nhất: "Dữ liệu rung động → AI/cảnh báo → **RSAP/FEM diễn giải** → BIM truy vết → khuyến nghị"; RQ (ii) "diễn giải RSAP/FEM"; "Paper 2 FEM & Suy giảm liên kết" | Sửa | Chuỗi: "Dữ liệu rung động → bằng chứng trạng thái → liên kết cấu kiện BIM & hồ sơ kiểm tra → truy vết → khuyến nghị kiểm tra–bảo trì". RQ (ii) → tổ chức & truy vết bằng chứng. Paper 2 → BIM–Sensor Traceability |
| 4 | Bảng đổi tên đề tài (Data-informed, Framework, Condition Monitoring, Industrial Steel Buildings) | Giữ | Không nhắc FEM — đã tương thích B |
| 5 | Outline: Chương 5 "RSAP/FEM và diễn giải cơ học (Paper 2)"; Chương 6 "BIM-FEM-Sensor... FEM_Node_ID (Paper 3)" | Sửa | C5 → "Khung truy vết BIM–Sensor–Inspection (Paper 2)"; C6 → "Kiểm chứng khả thi hiện trường (Paper 3)"; bỏ FEM_Node_ID khỏi ánh xạ lõi; thêm ghi chú "FEM danh nghĩa: tiểu mục trong C3" |
| 6 | Chuyên đề tổng quan: sơ đồ có hộp "Diễn giải FEM"; định vị ngành ghi "Cảm biến, FEM, BIM và AI là công cụ hỗ trợ" | Sửa | Bỏ hộp "Diễn giải FEM" khỏi chuỗi chính; câu định vị giữ nguyên nhưng thêm "(FEM: tham chiếu danh nghĩa, không hiệu chuẩn)" |
| 7 | RQ2→WP2→Paper 2 "Baseline FEM... diễn giải nới lỏng"; Mốc 3 "baseline FEM với tiêu chí chấp nhận" | Sửa | RQ2→WP2→Paper 2: mô hình dữ liệu truy vết + case study; Mốc 3 → "mô hình dữ liệu & tiêu chí truy vết v1". Xóa mọi Evidence Gate FEM |
| 8 | Bảng khoảng trống: hàng "Bằng chứng tình trạng → diễn giải FEM... Cần baseline FEM khỏe mạnh" | Sửa | Thu hàng này thành nguồn tham khảo phụ (bối cảnh), chuyển khoảng trống chính sang "evidence-to-action traceability"; giữ 3 hàng còn lại |
| 9 | Gantt: WP2 "Diễn giải cơ học bằng RSAP/FEM"; pha "Kiểm chứng FEM"; Paper 2 "FEM & Sensor Sensitivity" | Sửa | WP2 → "Thiết kế & kiểm chứng mô hình dữ liệu truy vết"; pha → "Truy vết BIM–Sensor"; Paper 2 đổi tên; thời gian giải phóng từ FEM dồn cho LORO + field |
| 10 | Đề tài tỉnh: Sản phẩm "…FEM tham chiếu…" | Giữ (có điều kiện) | Giữ "FEM tham chiếu" vì là sản phẩm ứng dụng của nhiệm vụ tỉnh, tương thích B; thêm chú thích nội bộ: FEM tham chiếu = mô hình thiết kế, không hiệu chuẩn, không dùng chẩn đoán (giữ firewall PhD/tỉnh) |
| 11 | Kiến trúc thí điểm: "FEM tham chiếu (diễn giải cơ học tham chiếu, xác định vị trí cảm biến…)"; "Cảm biến tại vị trí tối ưu theo diễn giải cơ học" | Sửa nhẹ | Đổi "tối ưu" → "được lựa chọn có tham chiếu mô hình thiết kế" (tránh nghĩa vụ chứng minh optimality); phần còn lại giữ |
| 12 | Lộ trình phát triển: gói thương mại "truy vết sensor–BIM–FEM" | Sửa nhẹ | "truy vết sensor–BIM (FEM tham chiếu khi có hồ sơ)" |
| 13 | Kết luận: "Dữ liệu NCS: Lab → **FEM** → BIM-linked traceability → inspection support" | Sửa | "Lab → condition evidence → BIM-linked traceability → field feasibility → inspection support" |
| 14 | Paper 1: mục tiêu cụ thể liệt kê **ResNet1D**; "đề xuất CEI thay cho DSI" | Sửa | Giữ CEI-thay-DSI (đúng hướng đã chốt). ResNet1D: đánh dấu "pending — chờ xác nhận sensor mode", không đưa số liệu vào bản thảo |
| 15 | Paper 1: "Kết luận & hướng sang Paper 2: Paper 2 sẽ dùng FEM, độ cứng tương đương và độ nhạy sensor để giải thích… Physics-informed Condition Evidence" | Sửa | "Các nhầm lẫn class (Apex↔BCJ; BCJ dưới S2) được ghi nhận là giả thuyết mở; Paper 2 chuyển trọng tâm sang truy vết bằng chứng đến cấu kiện BIM và hồ sơ kiểm tra. Giả thuyết cơ học được thảo luận định tính (mô hình danh nghĩa) trong Limitation" — xóa cụm "Physics-informed Condition Evidence" |

---

# PHẦN 8 — PHÁN QUYẾT CUỐI CÙNG

## **VERDICT B — RETAIN FEM ONLY AS A LIMITED SUPPORTING TOOL**

(Tiếp nhận kiến trúc không-FEM ở Mục 8 của đề bài làm khung xương; FEM tồn tại duy nhất như mô hình tham chiếu danh nghĩa trong một tiểu mục phương pháp và phần Limitation.)

**Năm hành động tiếp theo theo thứ tự ưu tiên:**

1. **Trình verdict B cho cả hai thầy hướng dẫn và xin xác nhận bằng văn bản** (email tóm tắt 1 trang: chuỗi bằng chứng mới, vai trò giới hạn của FEM, danh mục Prohibited claims) — trước khi nộp chuyên đề tổng quan deadline T7/2026.
2. **Hoàn thành LORO trên 6 runs và xác nhận sensor mode của ResNet1D** — vẫn là nút chặn kỹ thuật số 1 của toàn luận án, độc lập với quyết định FEM; không viết tiếp bản thảo Paper 1 trước khi xong.
3. **Viết lại chuỗi bằng chứng và chuỗi định danh** (bỏ FEM_Node_ID khỏi lõi) đồng loạt trong: outline luận án, chuyên đề tổng quan, slide báo cáo, hồ sơ đề tài tỉnh (chỉ phần thuyết minh liên quan, giữ nguyên sản phẩm "FEM tham chiếu").
4. **Thiết kế Paper 2 mới theo Phần 6:** chốt competency questions và bộ tiêu chí truy vết *trước* khi triển khai bất kỳ schema/demo nào (pre-registered), để chặn nguy cơ "system integration".
5. **Cập nhật Gantt:** đổi pha "Kiểm chứng FEM" thành "Truy vết BIM–Sensor"; dồn thời gian giải phóng cho WP3 hiện trường — kèm điều kiện tiên quyết đã treo từ lâu: **ký thỏa thuận hợp tác chính thức với đơn vị công trình thực trước khi lắp bất kỳ cảm biến nào**.

---

**Ghi chú "insufficient evidence" (không suy diễn thêm):** (1) quy chế đào tạo của cơ sở về yêu cầu nội dung kỹ thuật trong luận án QLXD; (2) thành phần thực tế của hội đồng bảo vệ; (3) sensor mode của ResNet1D; (4) độ ổn định LORO trên 6 runs; (5) tình trạng ký kết thỏa thuận tiếp cận công trình thực. Các mục này phải được xác nhận bằng nguồn chính thức, không được giả định trong bất kỳ tài liệu nào tiếp theo.
