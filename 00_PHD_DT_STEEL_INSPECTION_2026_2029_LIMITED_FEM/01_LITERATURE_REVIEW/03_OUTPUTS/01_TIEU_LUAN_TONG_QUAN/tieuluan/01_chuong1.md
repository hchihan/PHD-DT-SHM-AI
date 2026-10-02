# CHƯƠNG 1. GIỚI THIỆU VÀ PHƯƠNG PHÁP TỔNG QUAN

## 1.1. Bối cảnh nghiên cứu

### 1.1.1. Bối cảnh vận hành nhà công nghiệp khung thép

Nhà công nghiệp khung thép được thiết kế và xây dựng trong một giai đoạn hữu hạn nhưng được khai thác, kiểm tra, sửa chữa và điều chỉnh trong nhiều năm. Khi công trình chuyển sang vận hành, người quản lý phải trả lời lặp lại các câu hỏi: cấu kiện nào cần chú ý, căn cứ nào cho thấy trạng thái đã thay đổi, lần kiểm tra gần nhất do ai thực hiện, kết quả lưu ở đâu và việc xử lý đang ở trạng thái nào. Đó trước hết là câu hỏi về tổ chức thông tin phục vụ quyết định, sau đó mới là câu hỏi về phép đo. Cơ sở lý luận về quản lý tài sản và quản lý thông tin vận hành, gồm vai trò của ISO 19650-3:2020 \[1\], được trình bày ở Chương 2.

Trong môi trường công nghiệp, yêu cầu quản lý thông tin trở nên rõ hơn vì trạng thái khai thác chịu đồng thời tác động của chế độ tải, thiết bị, điều kiện môi trường, thay đổi công năng, lịch sử can thiệp và quá trình lão hóa. Luận án xem các yếu tố này là bối cảnh quản lý tài sản cần được lưu giữ cùng dữ liệu và hồ sơ; chúng không được dùng để suy luận cơ chế hư hỏng từ một chỉ báo dao động riêng lẻ. Cách đặt vấn đề này giúp giữ trọng tâm ở tính liên tục, nguồn gốc và khả năng truy vết của thông tin thay vì giới hạn nghiên cứu theo một điều kiện địa lý cụ thể.

Trong nhà công nghiệp khung thép, trạng thái liên kết bu lông là đối tượng trực tiếp của theo dõi và kiểm tra (mục 1.2.2). Từ góc nhìn Quản lý xây dựng, câu hỏi không dừng ở việc tín hiệu có nhận biết được thay đổi của liên kết hay không. Khi một dấu hiệu thay đổi xuất hiện, cần biết dấu hiệu đó được biến thành bằng chứng ra sao, được giới hạn phạm vi sử dụng thế nào, gắn với cấu kiện nào và đi vào quy trình kiểm tra – bảo trì theo cách nào.

### 1.1.2. Chuyển đổi số trong quản lý vận hành

Cảm biến, mô hình thông tin công trình (BIM), chuẩn trao đổi dữ liệu IFC, cơ sở dữ liệu vận hành và song sinh số cho phép gắn dữ liệu kỹ thuật với ngữ cảnh của tài sản. Ở từng mắt xích, nền kỹ thuật đã tương đối rõ. Lược đồ IFC có thể được mở rộng để biểu diễn hệ theo dõi trạng thái và quan hệ giữa cảm biến với cấu kiện \[2\]. Dữ liệu vận hành có thể được tích hợp với mô hình số ở cấp công trình và khuôn viên \[3\]. Định danh toàn cục của đối tượng IFC có thể dùng để nối mô hình với cơ sở dữ liệu chuỗi thời gian \[4\], \[5\]. Trong các tài liệu đã rà soát, việc đưa dữ liệu cảm biến vào ngữ cảnh mô hình công trình đã có nhiều giải pháp.

Tuy vậy, tích hợp dữ liệu chưa bảo đảm truy vết thông tin. Trong vận hành, dữ liệu cảm biến nằm trong hệ thu nhận; hình học và thuộc tính cấu kiện nằm trong BIM; hồ sơ kiểm tra nằm trong biểu mẫu, cơ sở dữ liệu hoặc hệ quản lý bảo trì; lịch sử hành động có thể nằm ở một hệ thống khác. Sự phân tán này là lý do Kim và cộng sự (2018) phải xây một lớp ngữ nghĩa riêng để nối dữ liệu quản lý vận hành với đối tượng IFC \[6\]. Boje và cộng sự (2020) cho rằng mô hình thông tin tĩnh không đáp ứng được một hệ thống số vận hành cần dữ liệu động, ngữ nghĩa và khả năng liên thông \[7\].

Khoảng cách giữa có dữ liệu và có bằng chứng dùng được cho quản lý vẫn còn. Một cảnh báo có thể hiện đúng vị trí trên mô hình trong khi người quản lý không biết nó được tạo từ dữ liệu nào, bằng phiên bản xử lý nào, có giá trị trong phạm vi nào, cấu kiện liên quan đã được kiểm tra chưa và hành động tiếp theo đang ở trạng thái nào. Mức độ chuyển đổi số trong vận hành vì vậy nên được đo bằng khả năng duy trì quan hệ kiểm tra được giữa nguồn dữ liệu, bằng chứng, cấu kiện, hồ sơ và hành động, hơn là bằng khối lượng dữ liệu hay độ trực quan của giao diện.

### 1.1.3. Song sinh số như mục tiêu kiến trúc của nghiên cứu

Khái niệm song sinh số được dùng với nhiều mức năng lực khác nhau trong các nghiên cứu. Kritzinger và cộng sự (2018) phân biệt mô hình số, bóng số và song sinh số theo chiều và mức tự động của luồng dữ liệu giữa đối tượng vật lý với biểu diễn số \[8\]. Sepasgozar (2021) đưa sự phân biệt này vào môi trường xây dựng \[9\], còn Chen và cộng sự (2021) tiếp cận song sinh số trong quản lý tài sản bằng mô hình trưởng thành nhiều chiều \[10\]. Cả ba cách phân loại cùng cho thấy mức năng lực của một hệ thống phải được đánh giá trên các chức năng thực có, không suy ra từ tên gọi.

Việc nối BIM với cảm biến tự nó chưa đủ để gọi một hệ thống là song sinh số. Luận án dùng phân loại của \[8\] để khai báo mức tích hợp. Dữ liệu đi tự động từ công trình vào mô hình số, còn mọi tác động trở lại công trình đi qua quyết định của con người, nên hệ thống ở mức bóng số (digital shadow). Tên đề tài giữ cụm "song sinh số dựa trên dữ liệu" theo hướng kiến trúc, kèm khai báo này (mục 5.6.6). Trong kiến trúc đó, dữ liệu từ tài sản vật lý được tổ chức thành bằng chứng trạng thái có nguồn gốc và phạm vi hiệu lực. Bằng chứng được liên kết với cấu kiện trong BIM và với bản ghi kiểm tra. Trạng thái hành động kiểm tra – bảo trì được ghi trở lại hệ thống thông tin và trở thành bối cảnh cho các lần đánh giá sau. Nếu được sử dụng, mô hình phần tử hữu hạn là mô hình danh nghĩa, chưa hiệu chuẩn, dùng để tham chiếu và không dùng cho chẩn đoán hư hỏng (Mục 5.9.3). Dự báo tuổi thọ còn lại, bảo trì dự báo, suy luận suy giảm độ cứng và tự động tác động lên tài sản không thuộc mục tiêu hiện tại.

### 1.1.4. Bối cảnh quản lý bảo trì và mô hình thông tin công trình tại Việt Nam

Tại Việt Nam, bảo trì công trình xây dựng hiện được quy định chi tiết tại Nghị định số 207/2026/NĐ-CP ngày 15/6/2026 của Chính phủ, có hiệu lực từ ngày 01/7/2026 và thay thế Nghị định số 06/2021/NĐ-CP \[11\] \[CẦN KIỂM: điều khoản thay thế Nghị định 06/2021/NĐ-CP\]. Nghị định xác định quy trình bảo trì là tài liệu quy định trình tự, nội dung và chỉ dẫn thực hiện các công việc bảo trì. Nội dung chính của quy trình bảo trì gồm, cùng các nội dung khác, quy định đối tượng, phương pháp và tần suất kiểm tra công trình, và quy định về hồ sơ bảo trì cùng việc cập nhật thông tin vào hồ sơ này (Điều 34 \[CẦN KIỂM: số điều\]). Quan trắc phục vụ bảo trì được yêu cầu trong các trường hợp cụ thể: công trình có dấu hiệu lún, nghiêng, nứt hoặc bất thường khác có khả năng gây sập đổ; theo yêu cầu của chủ đầu tư, chủ sở hữu hoặc chủ quản lý sử dụng; và công trình thuộc danh mục phải quan trắc theo quy định chuyên ngành (Điều 37 \[CẦN KIỂM: số điều\]). Quan trắc vì vậy là yêu cầu theo từng trường hợp.

Về mô hình thông tin công trình, Quyết định số 258/QĐ-TTg ngày 17/3/2023 phê duyệt lộ trình áp dụng BIM. Theo lộ trình này, BIM là bắt buộc từ năm 2023 với công trình cấp I và cấp đặc biệt, và từ năm 2025 với công trình cấp II trở lên, thuộc các dự án đầu tư xây dựng mới sử dụng vốn đầu tư công, vốn nhà nước ngoài đầu tư công và đầu tư theo phương thức đối tác công tư \[12\]. Quyết định cũng yêu cầu chủ đầu tư các dự án áp dụng BIM theo lộ trình tổ chức cập nhật mô hình để phục vụ quản lý, vận hành và bảo trì công trình (Điều 1, khoản 3, điểm g).

Hai văn bản trên cho thấy hồ sơ bảo trì, thông tin kiểm tra và mô hình thông tin công trình đều là đối tượng quản lý đã có cơ sở pháp lý tại Việt Nam. Tiểu luận dùng chúng để đặt bài toán quản lý thông tin của luận án vào bối cảnh trong nước, không dùng để suy ra ngưỡng kỹ thuật và không coi song sinh số là yêu cầu pháp lý; cả hai văn bản đều không quy định về song sinh số.

## 1.2. Nhà công nghiệp khung thép liên kết bu lông

### 1.2.1. Quy mô và vai trò của nhà xưởng khung thép

Quy mô của các khu công nghiệp cho thấy khối lượng nhà xưởng cần được quản lý vận hành ở Việt Nam. Theo số liệu của Cục Đầu tư nước ngoài (Bộ Tài chính), đến khoảng tháng 11/2025 cả nước có 478 khu công nghiệp đã thành lập, trong đó 324 khu đã đi vào hoạt động với khoảng 68 nghìn ha đất công nghiệp \[@XM5ZUP99\]. Từ thực tế kiểm định, nghiên cứu sinh nhận thấy nhà khung thép liên kết bu lông là loại hình phổ biến trong các khu này; đây là nhận định của nghiên cứu sinh, chưa có thống kê chính thức về tỷ trọng. Ở phạm vi quốc tế, Saleem và Qureshi (2018) cho thấy nhà thép tiền chế dùng tiết diện được tạo hình theo nội lực, nhờ đó nhẹ hơn và kinh tế hơn khung thép dùng tiết diện cán nóng không đổi \[@J358BJ7Z\]. Hiệu quả kinh tế này giải thích vì sao loại hình được dùng rộng rãi; tiểu luận không dùng nguồn này làm căn cứ về tỷ trọng.

Với chủ đầu tư, nhà xưởng là tài sản phục vụ sản xuất. Torres-Barriuso và cộng sự (2025) nêu rằng bảo trì nhà công nghiệp cần thiết để công trình làm việc đúng chức năng và tránh gián đoạn cùng thiệt hại kinh tế, và bảo trì phòng ngừa có cấu trúc góp phần duy trì sản xuất liên tục \[@QMVQCEL5\] (tr. 1, 3). Giá trị của thông tin trạng thái vì vậy được đo bằng khả năng giúp người quản lý chọn đúng cấu kiện cần kiểm tra và đúng thời điểm can thiệp, để công trình an toàn mà sản xuất ít bị gián đoạn nhất.

### 1.2.2. Liên kết bu lông là đối tượng theo dõi trực tiếp

Trong khung nhà xưởng, nội lực giữa cột, kèo và các cấu kiện phụ được truyền qua liên kết bu lông, nên tình trạng của liên kết quyết định trực tiếp khả năng làm việc của khung. Tài liệu đã tổng quan chỉ ra ba nhóm yếu tố làm tình trạng này thay đổi trong vận hành.

Nhóm thứ nhất là nới lỏng. Gong và cộng sự (2022) định nghĩa nới lỏng là sự mất lực siết và xếp nới lỏng vào các dạng hư hỏng chủ yếu của mối ghép ren, ảnh hưởng tới tính toàn vẹn và độ tin cậy của sản phẩm. Nhóm tác giả cũng cho biết nới lỏng dưới dao động ngang là chủ đề được nghiên cứu rộng rãi \[@WP5WUUF9\]. Nhóm thứ hai là ăn mòn. Việt Nam nằm trong vùng nhiệt đới ẩm. Lien và cộng sự (2007) thử phơi mẫu mười năm tại 6–8 trạm và ghi nhận thời gian ẩm ướt rất dài trên cả nước, tốc độ ăn mòn thép các-bon ở cấp ăn mòn C3 tại hầu hết các trạm; ăn mòn thép mạ kẽm phụ thuộc chủ yếu vào nồng độ ion clorua, cao nhất ở vùng ven biển \[@SKCFNXPU\] (tr. 552, 557). Với bu lông mạ kẽm, Daniel và cộng sự (2023) nêu rằng khả năng bảo vệ của lớp kẽm suy giảm theo thời gian, làm lộ thép nền và rút ngắn tuổi thọ chi tiết ghép, đặc biệt trong môi trường công nghiệp và biển \[@IJGQYI7W\] (tr. 5177). Nhóm thứ ba là chính quá trình lắp ráp: Brake và cộng sự (2019) cho thấy trên mẫu thí nghiệm có mối nối bu lông, quy trình lắp ráp làm đặc trưng động lực thay đổi giữa các lần lắp nếu không được kiểm soát \[18\].

Theo đánh giá của phần tổng quan nghiên cứu này, ba nhóm bằng chứng trên dẫn tới một diễn giải cho nhà xưởng. Trạng thái của liên kết bu lông thay đổi theo thời gian, theo điều kiện môi trường và theo mỗi lần can thiệp, nên một nhận định về liên kết chỉ có giá trị khi kèm theo thời điểm, điều kiện và lần lắp ráp mà nó được tạo ra. Đây là lý do khái niệm bằng chứng trạng thái có phạm vi hiệu lực (mục 1.3) được đặt vào trung tâm của luận án.

### 1.2.3. Điều kiện vận hành và khó khăn kiểm tra

Nhà xưởng khác nhà dân dụng ở chỗ công trình chịu tác động của chính hoạt động sản xuất. Thiết bị nâng và máy móc tạo ra rung động vận hành; Ju và cộng sự (2020), khảo sát một nhà máy công nghệ cao, cho thấy rung do cầu trục di chuyển tập trung trong một dải tần nhất định và phụ thuộc vận tốc, gia tốc của cầu trục và độ gồ ghề của ray \[@38FMATHE\]. Nghiên cứu này xét rung ảnh hưởng thiết bị nhạy rung trên sàn; việc rung vận hành cùng loại xuất hiện trong dữ liệu quan trắc khung nhà xưởng là diễn giải của tiểu luận và được xét tiếp ở Chương 3.

Kiểm tra liên kết trong nhà xưởng cũng tốn kém. Torres-Barriuso và cộng sự (2025) mô tả việc kiểm tra kết cấu nhà công nghiệp là quá trình cần nhiều nhân công và phải tiếp cận vùng cao, hẹp hoặc nguy hiểm. Theo nhóm tác giả, việc kiểm tra còn cần thiết bị phụ trợ, biện pháp an toàn quy mô lớn, có khi phải dừng sản xuất, và các yếu tố này làm tăng chi phí kiểm tra \[@QMVQCEL5\] (tr. 3, 5). Nooralishahi và cộng sự (2021) nêu các thách thức tương tự cho cơ sở công nghiệp: quy mô lớn, khó tiếp cận và rủi ro sức khỏe cho người kiểm tra \[@2AZ7VZ5R\]. Từ đó, giá trị quản lý của dữ liệu quan trắc ở nhà xưởng nằm ở chỗ giúp khoanh vùng cấu kiện cần kiểm tra trước; kết luận về tình trạng vẫn được xác lập qua kiểm tra của kỹ sư.

### 1.2.4. Khách thể, đối tượng và phạm vi nghiên cứu

Khách thể nghiên cứu là nhà công nghiệp khung thép có liên kết bu lông trong giai đoạn vận hành. Đối tượng nghiên cứu gồm ba thành phần: trạng thái liên kết bu lông của kết cấu thép nhà công nghiệp, xét qua dữ liệu dao động; bằng chứng trạng thái tạo từ dữ liệu đó (Mục 1.3); và chuỗi bằng chứng – kiểm tra – hành động trong mô hình thông tin công trình.

Phạm vi không gian gồm phòng thí nghiệm và hai nhà xưởng khung thép đang khai thác. Trong phòng thí nghiệm, mô hình khung thép tỉ lệ 1:10 cho phép tạo trạng thái liên kết có kiểm soát để xác lập quy trình tạo bằng chứng (Mục tiêu 1). Mô hình này mô phỏng một nhà xưởng ở tỉnh Khánh Hòa. Mô hình BIM của nhà xưởng Khánh Hòa là nền để đánh giá mô hình thông tin (Mục tiêu 2), và hồ sơ kiểm định cũ của chính nhà xưởng này được mã hóa làm đối chứng B0 (Mục 5.5.2). Nhà xưởng thứ hai ở tỉnh Đắk Lắk (địa bàn tỉnh Phú Yên cũ), đã có mô hình BIM, là nơi chuỗi bằng chứng – kiểm tra – hành động được triển khai và kiểm chứng khả thi (Mục tiêu 3). Kết quả trên mô hình 1:10 được nối với nhà xưởng ở Đắk Lắk qua nguyên tắc tổ chức bằng chứng; luận án không khẳng định tương tự động lực học giữa hai kết cấu (Mục 3.4.3).

Phạm vi thời gian là giai đoạn vận hành của công trình. Dữ liệu phòng thí nghiệm gồm ba đợt thí nghiệm; quan trắc tại nhà xưởng kéo dài 3–6 tháng (Mục 5.5.2). Tài liệu về BIM và song sinh số được ưu tiên trong giai đoạn 2018–2026, còn tài liệu nền tảng về phương pháp được xét không phụ thuộc năm công bố (Mục 1.8.5).

Mức tích hợp của hệ thống là bóng số (Mục 1.1.3). Các hướng thuộc và không thuộc phạm vi nội dung được phân lớp ở Bảng 5.8 (Mục 5.9.1). Khi tiểu luận dùng tài liệu về cầu, kết cấu ngoài trời hay nhà máy công nghệ cao, phần bằng chứng được trích đúng đối tượng của nguồn, còn việc áp sang nhà xưởng được ghi rõ là diễn giải; phạm vi diễn giải được trình bày ở Mục 5.9.

## 1.3. Khái niệm bằng chứng trạng thái

Trong luận án này, bằng chứng trạng thái (condition evidence) là một nhận định về tình trạng của một cấu kiện, kèm nguồn tạo ra nhận định đó và phạm vi mà nhận định được phép sử dụng.

Nhận định đó có thể đến từ ba nguồn: mô hình chạy trên dữ liệu cảm biến, quan sát của kỹ sư khi kiểm tra, hoặc phép đo kiểm tra không phá hủy. Luận án tập trung vào bằng chứng từ dữ liệu dao động ở Gói công việc 1 (WP1), còn cấu trúc dữ liệu tiếp nhận cả ba loại (Mục 5.6.2).

Một ví dụ giả định về bằng chứng từ dữ liệu cảm biến giúp hình dung khái niệm. Cảm biến gia tốc gắn trên cột trục C3 của một nhà xưởng giả định ghi dao động khi cầu trục vận hành, và mô hình học máy gán cho một đoạn tín hiệu nhãn "lệch khỏi đường cơ sở vận hành". Nhãn này là kết quả phân loại. Nó trở thành bằng chứng trạng thái khi đi kèm ba thành phần. Thành phần thứ nhất là nguồn gốc (provenance): nhãn được tạo ra từ dữ liệu nào và bằng cách nào. Nguồn gốc bao gồm nguồn thu, cấu hình cảm biến, phiên bản dữ liệu – chuỗi xử lý và giao thức đánh giá; chi tiết ở Mục 3.5.1. Thành phần thứ hai là độ bất định: nhãn thay đổi ra sao khi phép đánh giá được lặp lại. Thành phần thứ ba là phạm vi hiệu lực (validity scope): nhận định đúng cho cột C3 trong các chế độ vận hành đã có mặt ở dữ liệu tham chiếu. Mọi giá trị và cấu hình trong ví dụ đều giả định.

Phạm vi hiệu lực được ghi rõ vì độ tin cậy của một kết quả phụ thuộc vào cách kết quả được đánh giá. Beleites và cộng sự (2013) phân biệt số quan sát tính toán với số đơn vị độc lập thực \[14\]. Wheat và cộng sự (2024) cho thấy hiệu năng đo được trên dữ liệu rung động thay đổi mạnh khi đổi cấp nguồn vật lý dùng để chia dữ liệu \[15\]. Phạm vi hiệu lực vì vậy ghi đơn vị suy luận và cách chia dữ liệu, cùng đợt lắp đặt, cấu hình cảm biến và điều kiện áp dụng (mục 3.5.2).

Bảng 1.1 đặt ba khái niệm cạnh nhau. Chẩn đoán hư hỏng là kết luận của kỹ sư sau khi kiểm tra cấu kiện; bằng chứng trạng thái là căn cứ mà kỹ sư dùng để quyết định kiểm tra và để đi tới kết luận đó.

<span id="TLTQ_Bang_1_1" class="anchor"></span>Bảng 1.1. Kết quả phân loại, bằng chứng trạng thái và chẩn đoán hư hỏng

| Khái niệm | Gồm những gì | Do ai hoặc cái gì tạo ra | Dùng để làm gì |
|---|---|---|---|
| Kết quả phân loại | Một giá trị cho một mẫu tín hiệu: nhãn, xác suất hoặc điểm số | Mô hình học máy | Là đầu vào để tạo bằng chứng trạng thái từ dữ liệu cảm biến |
| Bằng chứng trạng thái | Một nhận định về tình trạng cấu kiện (kết quả phân loại, ghi nhận quan sát hoặc số đo), gắn với cấu kiện, nguồn gốc, độ bất định và phạm vi hiệu lực | Mô hình trên dữ liệu cảm biến cùng chuỗi xử lý có phiên bản; kỹ sư quan sát khi kiểm tra; phép đo kiểm tra không phá hủy | Là căn cứ để kỹ sư quyết định kiểm tra và lập chẩn đoán, trong phạm vi hiệu lực đã ghi |
| Chẩn đoán hư hỏng | Kết luận về có hư hỏng hay không, vị trí, nguyên nhân và mức độ | Kỹ sư, sau khi kiểm tra cấu kiện | Là căn cứ để quyết định sửa chữa hoặc bảo trì |

Cấu trúc dữ liệu của bản ghi bằng chứng, gồm cả ba thành phần trên, được trình bày ở Mục 5.6.2.

## 1.4. Ba câu hỏi của người quản lý

Một kịch bản giả định cho thấy người quản lý cần gì ở thông tin. Trong một ca sản xuất của nhà xưởng thép, hệ thống ghi nhận dao động của cột trục C3 lệch khỏi đường cơ sở vận hành. Hệ thống tạo một bằng chứng trạng thái gắn với cột C3, ghi cảm biến, phiên bản phương pháp, độ bất định và điều kiện áp dụng. Kỹ sư A nhận bằng chứng, kiểm tra tại hiện trường và xác nhận một bu lông liên kết ở cột C3 bị lỏng. Kết quả kiểm tra được ghi thành bản ghi kiểm tra và liên kết với bằng chứng đã làm phát sinh kiểm tra. Trưởng phòng B, người có thẩm quyền, phê duyệt việc siết lại. Bu lông được siết, hành động được đóng. Sáu tháng sau, khu vực này xảy ra một sự cố. Người điều tra mở hành động, đọc được bản ghi kiểm tra của kỹ sư A, bằng chứng đã dẫn tới bản ghi đó và phạm vi mà bằng chứng được phép dùng, mà không phải hỏi lại từng người.

Kịch bản đặt ra ba câu hỏi mà người quản lý cần trả lời được ở mọi thời điểm. Cái gì bất thường, ở đâu? Tin được đến mức nào? Ai đã xử lý, dựa vào đâu?

Mỗi câu hỏi tương ứng với một phần của luận án. Câu hỏi thứ nhất cần liên kết giữa bằng chứng và cấu kiện, để bất thường được đặt vào đúng cột thay vì chỉ gắn với một cảm biến. Câu hỏi thứ hai cần nguồn gốc và phạm vi hiệu lực của bằng chứng, để mức tin cậy được đọc trong đúng điều kiện. Câu hỏi thứ ba cần bản ghi kiểm tra, các sự kiện chuyển trạng thái của hành động và thẩm quyền của người thực hiện. Tiền lệ cho từng phần của câu hỏi thứ ba được trình bày ở Mục 1.5.4. Mục 5.6.2 trình bày cấu trúc dữ liệu để trả lời ba câu hỏi này.

## 1.5. Vấn đề nghiên cứu

### 1.5.1. Vấn đề quản lý trung tâm

Vấn đề nghiên cứu xuất phát từ sự không liên tục giữa dữ liệu kỹ thuật và thông tin quản lý. Dữ liệu cảm biến, mô hình BIM, hồ sơ kiểm tra và lịch sử bảo trì có thể cùng tồn tại nhưng phân tán. Khi đó, một kết quả sinh từ dữ liệu cảm biến chưa chắc nối được, theo cách kiểm chứng được, với cấu kiện cụ thể, hồ sơ kiểm tra tương ứng và trạng thái của hành động tiếp theo. Vấn đề quản lý trung tâm của luận án được phát biểu như sau:

Thông tin giám sát, kiểm tra và bảo trì có thể tồn tại đồng thời nhưng thiếu một chuỗi truy vết bảo toàn được nguồn gốc và phạm vi hiệu lực của bằng chứng từ dữ liệu cảm biến tới cấu kiện, hồ sơ kiểm tra và trạng thái hành động.

Với người quản lý, một cảnh báo chỉ có giá trị khi trả lời được chuỗi câu hỏi: cảnh báo xuất phát từ cảm biến nào, cảm biến đó phục vụ cấu kiện nào, dữ liệu được thu trong điều kiện nào, kết quả được tạo bằng phiên bản xử lý và giao thức đánh giá nào, bằng chứng có hiệu lực tới đâu, cấu kiện đã được kiểm tra chưa, hồ sơ nào liên quan, ai đã rà soát và hành động hiện đang ở trạng thái nào. Nếu phải tra thủ công qua nhiều hệ thống mới trả lời được, khả năng giải trình và kiểm lại quyết định sẽ bị hạn chế.

Bài toán của luận án vì thế là xác định kết quả học máy dùng được trong phạm vi nào. Mô hình học máy và học sâu là công cụ tạo bằng chứng kỹ thuật. Câu hỏi khoa học là làm thế nào để bằng chứng đó được xác lập chất lượng, được giới hạn phạm vi sử dụng, được liên kết đúng đối tượng và được duy trì trong chuỗi thông tin quản lý.

Vấn đề này có hai mặt, ứng với hai khoảng trống ở Mục 5.2. Mặt thứ nhất là chất lượng và phạm vi hiệu lực của bằng chứng tạo từ dữ liệu dao động (Mục 1.5.2, KT1). Mặt thứ hai là việc giữ các thuộc tính đó khi bằng chứng đi qua cấu kiện và bản ghi kiểm tra tới hành động có căn cứ và thẩm quyền (Mục 1.5.3 và 1.5.4, KT2).

### 1.5.2. Từ kết quả phân loại đến bằng chứng trạng thái

Theo dõi trạng thái kết cấu bằng dữ liệu dao động đã có nền nghiên cứu rộng; riêng Jia và Li (2023) tổng hợp 337 công bố về học sâu trong lĩnh vực này \[13\]. Áp dụng thêm một mô hình phân loại cho dữ liệu khung thép vì vậy không tự tạo thành khoảng trống khoa học. Vấn đề nằm ở độ tin cậy của kết quả, bắt nguồn từ cấu trúc của dữ liệu dao động: rất nhiều cửa sổ tín hiệu có thể được cắt ra từ một số ít lần thu vật lý. Nếu coi các cửa sổ này là quan sát độc lập, hiệu năng sẽ bị đánh giá lạc quan. Các nguyên tắc liên quan (phân biệt số quan sát tính toán với số đơn vị độc lập thực \[14\]; ảnh hưởng của cấp nguồn vật lý dùng để chia dữ liệu \[15\]) đã nêu ở Mục 1.3 và được tổng hợp ở Mục 3.4.

Luận án kế thừa các nguyên tắc này từ \[14\], \[15\] để làm rõ một kết quả có thể được tin cậy trong phạm vi nào. Luận án dùng khái niệm bằng chứng trạng thái để chỉ kết quả tạo từ dữ liệu dao động cùng các thông tin cần để diễn giải nó: nguồn dữ liệu, cấu hình cảm biến, phiên bản chuỗi xử lý, giao thức đánh giá, độ bất định và phạm vi hiệu lực đã được kiểm chứng. Bằng chứng trạng thái khác với chẩn đoán hư hỏng. Một thay đổi của tín hiệu có thể do điều kiện môi trường, cách lắp đặt, lịch sử bảo trì hoặc một thay đổi vật lý thật. Bất thường từ dữ liệu vì vậy được dùng để kích hoạt kiểm tra, không dùng để tự động kết luận nguyên nhân hay mức độ hư hỏng. Yêu cầu này được phát biểu thành KT1 ở Mục 5.2.1.

### 1.5.3. Từ định danh cấu kiện đến truy vết thông tin

Ở lớp thông tin công trình, BIM và IFC là nền để liên kết dữ liệu với cấu kiện: hệ theo dõi trạng thái và quan hệ cảm biến – cấu kiện có thể được biểu diễn ngay trong lược đồ IFC \[2\], và định danh toàn cục có thể nối dữ liệu mô hình với chuỗi thời gian \[5\]. Các tiền lệ về liên kết BIM – hệ quản lý bảo trì, hồ sơ khiếm khuyết gắn cấu kiện và kiểm chứng quan hệ bằng ràng buộc ngữ nghĩa được trình bày ở mục 4.2–4.4. Luận án kế thừa các liên kết này (cảm biến – BIM, BIM – hệ quản lý bảo trì, hồ sơ khiếm khuyết – cấu kiện) từ các tiền lệ đó.

Điều cần xem xét là việc bảo toàn chất lượng của bằng chứng qua chuỗi. Sau khi được tạo, một bằng chứng mang theo nhãn trạng thái cùng nguồn gốc, phiên bản, điều kiện đánh giá và phạm vi hiệu lực; các thuộc tính này phải còn nguyên khi bằng chứng được liên kết với cấu kiện hoặc hồ sơ. Bấm được từ cảm biến tới cấu kiện là điều hướng. Truy vết đòi hỏi thêm hai điều: bản ghi kiểm tra truy ngược được tới đúng bằng chứng đã làm phát sinh nó, và quan hệ giữa các bản ghi ở hai hệ thống còn toàn vẹn khi dữ liệu thay đổi. Trọng tâm vì vậy chuyển từ kết nối dữ liệu sang truy vết có thể kiểm chứng. Trong luận án, khoảng hiệu lực của ánh xạ cảm biến – cấu kiện được xử lý như ràng buộc C3 của mô hình dữ liệu (Mục 5.2.3, Phụ lục B); việc truy ngược từ bản ghi kiểm tra về bằng chứng thuộc KT2.

### 1.5.4. Từ bằng chứng đến hỗ trợ hành động có thể giải trình

Hệ thống quản lý tài sản không dừng ở việc hiển thị trạng thái cấu kiện. Sau một dấu hiệu bất thường, người quản lý phải quyết định có kiểm tra hay không, ai chịu trách nhiệm, kết quả kiểm tra thay đổi nhận định ban đầu thế nào và hành động tiếp theo được ghi nhận ra sao. Từng phần của quá trình này đã có tiền lệ. Çelik và cộng sự (2023) ghi nguồn gốc dữ liệu, tác nhân, thời điểm và phiên bản trong trao đổi thông tin xây dựng \[16\]; Wu và cộng sự (2026) phát triển khung kiểm định công trình có chuyên gia tương tác và rà soát \[17\]; các tiền lệ về bản ghi sửa chữa, trạng thái hoàn thành và điều hướng giữa BIM với hệ quản lý bảo trì được trình bày ở mục 4.3 và mục 4.5. Luận án kế thừa các thành phần này (con người trong quy trình, bản ghi sửa chữa, trạng thái hoàn thành) từ các tiền lệ nêu trên.

Phần còn lại nằm ở khả năng giải trình của điểm nối từ bằng chứng tới hành động. Khi một hành động được đề xuất hoặc chuyển trạng thái, người quản lý cần truy ngược được tới căn cứ kỹ thuật đã dùng và biết căn cứ đó có hiệu lực trong phạm vi nào; lịch sử rà soát, vai trò, thời điểm và kết quả xử lý cũng phải tái dựng được. Phát biểu về điểm nối này giới hạn trong tập tài liệu đã rà soát (Mục 5.9.4). Điểm nối này được phát biểu thành KT2 ở Mục 5.2.2.

### 1.5.5. Chuỗi nghiên cứu

Từ các vấn đề trên, trục nghiên cứu được khóa thành một chuỗi duy nhất, trình bày ở Hình 1.1.

![](../TLTQ_28.09.2026/figures/Hinh_1_1_Chuoi_nghien_cuu_tong_the.png)
<!-- GĐ0: hình gốc vẽ bằng shape trong .docx; ảnh cắt từ PDF do Word xuất ngày 28/09/2026 -->

<span id="TLTQ_Hinh_1_1" class="anchor"></span>Hình 1.1. Chuỗi nghiên cứu tổng thể

Tương ứng với chuỗi này là một chuỗi định danh kỹ thuật:

*Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status*

Trong đó *Sensor_ID* xác định nguồn đo; *BIM_GUID* xác định cấu kiện trong mô hình thông tin; *Condition_Evidence_ID* xác định bản ghi bằng chứng trạng thái; *Inspection_Record_ID* xác định bản ghi kiểm tra; *Action_Status* biểu diễn trạng thái xử lý của hành động kiểm tra hoặc bảo trì. Các mã này thống nhất với kiến trúc dữ liệu của luận án (mục 5.6.2).

## 1.6. Sự cần thiết của nghiên cứu

Bốn lý do dưới đây gắn với hai khoảng trống và ba mục tiêu. Mục 1.6.1 ứng với KT1 và Mục tiêu 1, Mục 1.6.2 với KT2 và Mục tiêu 2, Mục 1.6.3 với Mục tiêu 3; Mục 1.6.4 giải thích việc định vị hệ thống ở mức bóng số.

### 1.6.1. Cần nâng chất lượng của kết quả phân loại thành chất lượng của bằng chứng

Số mô hình học máy và học sâu trong theo dõi trạng thái kết cấu đã lớn, nên giá trị khoa học của một nghiên cứu mới nằm ở cách kết quả được tạo ra và kiểm chứng. Các nghiên cứu về kết cấu có liên kết cho thấy lý do: đáp ứng của kết cấu chịu ảnh hưởng mạnh của quá trình lắp ráp và trạng thái tiếp xúc \[18\]; dữ liệu từ một đợt thí nghiệm mới sau tháo – lắp lại có thể tạo thành một miền dữ liệu khác \[19\]; cách phân bổ đơn vị vật lý giữa tập huấn luyện và tập kiểm tra có thể làm thay đổi mạnh kết quả đánh giá \[20\].

Bằng chứng kỹ thuật vì vậy phải mang theo điều kiện và giới hạn của chính nó. Nếu khả năng chuyển giao sang một đợt đo mới chưa được chứng minh, kết quả vẫn giữ giá trị trong phạm vi đã kiểm chứng. Cách hiểu này khớp với nhu cầu quản lý: người ra quyết định cần một nhãn kèm mức độ chắc chắn và bối cảnh sử dụng của nhãn đó.

### 1.6.2. Cần chuyển từ tích hợp phần mềm sang truy vết có thể kiểm tra

Các nghiên cứu đã cho thấy cảm biến có thể nối với BIM, hồ sơ kiểm tra có thể gắn với cấu kiện và tài sản có thể được đồng bộ sang hệ quản lý bảo trì. "Kết nối được" vì vậy không còn đủ để định vị đóng góp. Cần kiểm tra xem các quan hệ có đúng, đủ và bền vững hay không, và điều này cũng đã khả thi: ràng buộc ngữ nghĩa có thể phát hiện vi phạm trong các liên kết xuyên miền \[21\]; lược đồ IFC mở rộng có thể được kiểm tra bằng các trường hợp cố ý vi phạm quy tắc \[2\].

Câu hỏi đặt ra vì thế chuyển từ "Hệ thống có liên kết được không?" sang "Hệ thống có chứng minh được rằng bằng chứng liên kết đúng với cấu kiện, hồ sơ và trạng thái hành động, đồng thời phát hiện được khi chuỗi bị thiếu hoặc sai hay không?". Đây là bước chuyển từ trình diễn tích hợp sang kiểm chứng thông tin.

Ở Việt Nam, Nghị định 207/2026/NĐ-CP yêu cầu quy trình bảo trì quy định hồ sơ bảo trì và việc cập nhật thông tin vào hồ sơ này, còn Quyết định 258/QĐ-TTg yêu cầu cập nhật mô hình BIM phục vụ vận hành và bảo trì (Mục 1.1.4). Theo đánh giá của phần tổng quan nghiên cứu này, hai yêu cầu đó tạo nhu cầu ghi được căn cứ của từng quyết định kiểm tra – bảo trì trong hồ sơ số.

### 1.6.3. Cần phân biệt bằng chứng phòng thí nghiệm với khả năng áp dụng trong bối cảnh thực tế

Trên công trình đang vận hành, dữ liệu hư hỏng có nhãn thường khó thu đủ để kiểm chứng trực tiếp một bộ phân loại huấn luyện trong phòng thí nghiệm; điều kiện môi trường, cách lắp đặt, lịch sử bảo trì và cấu trúc thực tế cũng khác mô hình thu nhỏ. Vì vậy, định hướng nghiên cứu không giả định khả năng chuyển trực tiếp bộ phân loại từ khung thép 1:10 sang công trình thực.

Phần có thể chuyển từ phòng thí nghiệm sang bối cảnh thực tế là nguyên tắc tổ chức bằng chứng: bằng chứng phải có định danh, nguồn gốc, bối cảnh, phạm vi hiệu lực và quan hệ với cấu kiện. Ở cấp tổng quan, yêu cầu này được dùng để xác lập ranh giới phương pháp: dữ liệu vận hành có thể hỗ trợ nhận biết biến đổi và kích hoạt kiểm tra, nhưng không tự động trở thành nhãn hư hỏng. Khả năng áp dụng của khung trên một nhà xưởng thật được kiểm chứng ở Mục tiêu 3 của luận án (Mục 5.3.3).

### 1.6.4. Cần một kiến trúc song sinh số bám theo quá trình quản lý

Song sinh số chỉ có ý nghĩa với luận án khi nó giúp duy trì liên hệ giữa tài sản vật lý, thông tin số và lịch sử quản lý. Các khung phân loại và mô hình trưởng thành yêu cầu năng lực của một hệ thống số được xác định rõ, không suy ra từ tên gọi \[8\]–\[10\]. Các yêu cầu về dữ liệu động và ngữ nghĩa \[7\], về khả năng nối dữ liệu thời gian với IFC \[5\] và về vai trò của con người khi rà soát kết quả số \[17\] cũng đã được đặt ra.

Luận án kế thừa các tiền lệ này và tập trung vào một câu hỏi quản lý: một bằng chứng trạng thái có được duy trì tới bản ghi kiểm tra và trạng thái hành động theo cách truy lại và giải trình được hay không. Mức tích hợp được khai báo ở Mục 1.1.3; năng lực đạt được được đánh giá sau khi triển khai trên nhà xưởng (Mục 5.6.6).

## 1.7. Mục tiêu và phạm vi của Tiểu luận tổng quan

### 1.7.1. Mục tiêu tổng quát

Mục tiêu của Tiểu luận tổng quan là hệ thống hóa và tổng hợp có chọn lọc cơ sở lý luận cùng bằng chứng nghiên cứu liên quan. Các nội dung đó xác lập nền khoa học cho việc phát triển khung song sinh số dựa trên dữ liệu phục vụ giám sát trạng thái và hỗ trợ kiểm tra – bảo trì nhà công nghiệp khung thép, với mức tích hợp khai báo ở Mục 1.1.3. Trọng tâm của Tiểu luận là tính liên tục của chuỗi thông tin từ dữ liệu dao động tới bằng chứng trạng thái, cấu kiện trong mô hình thông tin, hồ sơ kiểm tra và trạng thái hành động.

### 1.7.2. Mục tiêu cụ thể

Tiểu luận thực hiện năm mục tiêu cụ thể:

1\. Hệ thống hóa cơ sở về quản lý tài sản, quản lý thông tin vận hành, BIM, IFC và song sinh số có liên quan trực tiếp tới kiểm tra – bảo trì công trình.

2\. Tổng hợp bằng chứng nghiên cứu về dữ liệu dao động và điều kiện cần để một kết quả phân loại có thể được xem là bằng chứng trạng thái có phạm vi hiệu lực rõ.

3\. Tổng hợp các nghiên cứu về liên kết cảm biến – BIM, hồ sơ kiểm tra, định danh, nguồn gốc dữ liệu, kiểm chứng quan hệ và hỗ trợ hành động có người rà soát.

4\. Phân biệt những nội dung các nghiên cứu đã giải quyết với những điểm nối còn thiếu, tránh xây dựng khoảng trống bằng các tuyên bố thiếu vắng rộng.

5\. Tạo cơ sở để Chương 5 tổng hợp khoảng trống, xác lập các câu hỏi nghiên cứu, kiến trúc nghiên cứu và thiết kế kiểm chứng của luận án.

Tiểu luận trình bày thiết kế và công cụ của thực nghiệm; kết quả thực nghiệm được báo cáo trong các bài báo chuyên đề của luận án.

### 1.7.3. Đối tượng tổng quan

Đối tượng tổng quan gồm các nghiên cứu và tài liệu chuẩn thuộc bốn nhóm gắn với chuỗi nghiên cứu: (1) quản lý tài sản, quản lý thông tin giai đoạn vận hành và song sinh số trong môi trường xây dựng; (2) theo dõi trạng thái bằng dữ liệu dao động, cách tổ chức và đánh giá bằng chứng trạng thái; (3) BIM, IFC, định danh cấu kiện và liên kết dữ liệu cảm biến với mô hình thông tin; (4) hồ sơ kiểm tra – bảo trì, nguồn gốc dữ liệu, kiểm chứng quan hệ, khả năng truy vết và hỗ trợ hành động có con người rà soát.

Khách thể, đối tượng và phạm vi nghiên cứu của luận án được nêu ở Mục 1.2.4. Áp các nguyên tắc về quản trị bằng chứng, định danh và truy vết cho loại kết cấu và tài sản công trình khác là hướng phát triển sau luận án (Mục 5.9.1).

### 1.7.4. Phạm vi của Tiểu luận tổng quan

Tiểu luận rà soát tài liệu thuộc bốn mắt xích của chuỗi nghiên cứu: quản lý tài sản và song sinh số trong vận hành; dữ liệu dao động và bằng chứng trạng thái; BIM/IFC, định danh và truy vết cấp cấu kiện; hồ sơ kiểm tra, khả năng áp dụng trong bối cảnh thực tế và hỗ trợ hành động. Học máy, học sâu, nguồn gốc dữ liệu, khả năng liên thông và con người trong vòng lặp được rà soát ở vai trò hỗ trợ.

Ngoài phạm vi hiện tại là các hướng như chẩn đoán hư hỏng hiện trường khi chưa có kiểm tra xác nhận, dự báo tuổi thọ còn lại, bảo trì dự báo, suy luận suy giảm độ cứng, tối ưu hóa vị trí cảm biến và bảo trì tự động. Bảng phân lớp phạm vi đầy đủ của luận án, gồm cả nhóm hướng nghiên cứu sau luận án, được trình bày ở Mục 5.9.1.

### 1.7.5. Bốn loại bằng chứng

Luận án phân biệt bốn loại bằng chứng: bằng chứng phòng thí nghiệm, bằng chứng truy vết thông tin, bằng chứng về khả năng áp dụng trong bối cảnh thực tế và bằng chứng hỗ trợ quyết định quản lý. Mỗi loại được dùng cho kết luận cùng loại; ranh giới của từng loại được trình bày ở Mục 5.9.2.

Quy tắc chung được giữ nhất quán là:

Bất thường trong dữ liệu vận hành dẫn tới xem xét và kiểm tra, không dẫn trực tiếp tới kết luận hư hỏng.

## 1.8. Phương pháp thực hiện tổng quan

### 1.8.1. Cách tiếp cận

Tiểu luận sử dụng tổng quan tài liệu theo chủ đề có cấu trúc (structured thematic literature review), khác với tổng quan hệ thống (systematic literature review) và phân tích thư mục định lượng. Vấn đề nghiên cứu đi qua nhiều miền kiến thức: quản lý tài sản, BIM/IFC, song sinh số, theo dõi trạng thái bằng dao động, học máy, nguồn gốc dữ liệu, quản lý hồ sơ kiểm tra và hỗ trợ hành động. Mục tiêu vì thế là xác định các tiền lệ và giới hạn ảnh hưởng trực tiếp tới chuỗi nghiên cứu.

Quá trình tổng hợp tuân theo ba nguyên tắc. Thứ nhất, tài liệu được tổ chức theo mắt xích của chuỗi nghiên cứu thay vì theo tên công nghệ. Thứ hai, các nghiên cứu trọng yếu được đọc và tổng hợp theo cấu trúc luận điểm, bằng chứng, giới hạn và hàm ý nghiên cứu. Thứ ba, mọi phát biểu về khoảng trống phải được kiểm tra bằng nguồn phản biện hoặc tiền lệ gần nhất trước khi được giữ lại. Nguồn tài liệu, chiến lược khảo sát, quy trình sàng lọc, tiêu chí lựa chọn và cách đánh giá chất lượng bằng chứng được trình bày ở mục 1.8.5.

### 1.8.2. Các nhóm chủ đề

Tập tài liệu được tổ chức thành chín nhóm bám theo chuỗi nghiên cứu: quản lý tài sản và thông tin trong giai đoạn vận hành; BIM, IFC, mô hình thông tin tài sản và định danh cấu kiện; song sinh số cùng các khung đánh giá mức năng lực; dữ liệu dao động và theo dõi trạng thái liên kết; đơn vị vật lý độc lập, rò rỉ dữ liệu và khả năng chuyển giao; liên kết cảm biến – BIM và dữ liệu chuỗi thời gian; hồ sơ kiểm tra, khiếm khuyết, sửa chữa và hệ quản lý bảo trì; nguồn gốc dữ liệu, kiểm chứng quan hệ và lịch sử thông tin; con người trong vòng lặp và hỗ trợ hành động kiểm tra – bảo trì. Cách phân nhóm này tránh gom những tài liệu rất khác nhau vào các nhãn quá rộng như "trí tuệ nhân tạo", "BIM" hay "song sinh số". Trong ma trận 29 tài liệu đọc sâu, chín nhóm này được gom thành năm cụm: song sinh số; theo dõi trạng thái – liên kết bu lông – biến đổi môi trường và vận hành; độ tin cậy của đánh giá; truy vết thông tin; giá trị của thông tin cho quyết định.

### 1.8.3. Kiểm soát mức bằng chứng của nguồn tài liệu

Kết luận rút từ một nghiên cứu chỉ được dùng ở đúng mức mà nghiên cứu đó kiểm chứng. Nghiên cứu liên kết cảm biến với BIM cho thấy liên kết đó; sự tồn tại của hồ sơ kiểm tra cần bằng chứng riêng. Hồ sơ sửa chữa khác với lịch sử trạng thái, và sự tham gia của con người vào quy trình khác với việc vai trò, thẩm quyền và trách nhiệm được biểu diễn thành dữ liệu. Điều hướng hai chiều trên giao diện khác với toàn vẹn hai chiều của quan hệ dữ liệu; kết quả phòng thí nghiệm khác với khả năng chẩn đoán trong bối cảnh sử dụng thực. Khi bằng chứng không đủ cho một phát biểu, phát biểu đó được ghi là chưa đủ bằng chứng.

### 1.8.4. Cách xử lý khoảng trống nghiên cứu

Khoảng trống được xác lập bằng phép trừ tiền lệ, qua ba bước: xác định nội dung các nghiên cứu đã giải quyết; tìm các nghiên cứu gần nhất có khả năng phản biện nhận định còn thiếu; chỉ giữ phần còn lại sau khi đã trừ các tiền lệ đó. Cách đối chiếu với nghiên cứu gần nhất được mô tả chi tiết ở mục 1.8.5.

Kết quả rà soát cho thấy các thành phần kỹ thuật chính đều đã có tiền lệ, từ phân loại trạng thái bằng dữ liệu dao động, kiểm soát rò rỉ và đánh giá theo nhóm, tới liên kết cảm biến – BIM, BIM – hệ quản lý bảo trì, hồ sơ khiếm khuyết, định danh, nguồn gốc dữ liệu, kiểm chứng quan hệ và con người trong quy trình. Phần còn thiếu nằm ở các điểm nối giữa những thành phần đó. Sau khi đối chiếu tiền lệ, tiểu luận giữ lại hai khoảng trống, phát biểu ở Mục 5.2: KT1 về phạm vi hiệu lực của bằng chứng trạng thái, gồm vế đánh giá (A1) và vế khai báo (A2); KT2 về đường đi từ bằng chứng tới hành động có căn cứ và thẩm quyền. Yêu cầu giữ nguyên các thuộc tính của bằng chứng khi đi qua chuỗi truy vết được xử lý như một ràng buộc của mô hình dữ liệu (Mục 5.2.3).

### 1.8.5. Nguồn tài liệu, chiến lược khảo sát và quy trình lựa chọn nghiên cứu

Mục này mô tả nguồn tài liệu, cách tìm, cách sàng lọc và cách đánh giá chất lượng bằng chứng.

**a) Nguồn tài liệu và phạm vi khảo sát**

Nguồn tài liệu được xem xét gồm các bài báo khoa học đăng trên tạp chí quốc tế có phản biện, bài báo hội nghị khoa học, các công trình tổng quan, tiêu chuẩn kỹ thuật và tài liệu chính thức của các tổ chức chuyên ngành có liên quan.

Việc khảo sát tập trung vào các nghiên cứu thuộc lĩnh vực Quản lý xây dựng, quản lý tài sản công trình, quản lý thông tin trong giai đoạn vận hành, BIM/IFC, song sinh số (Digital Twin), theo dõi trạng thái kết cấu (SHM), phân tích dữ liệu dao động, truy vết thông tin và hỗ trợ kiểm tra – bảo trì.

Các tài liệu được tổ chức theo chín nhóm chủ đề đã xác định tại mục 1.8.2, bám sát các mắt xích của chuỗi nghiên cứu, thay vì phân loại riêng biệt theo từng công nghệ.

Đối với các nghiên cứu về BIM, Digital Twin và quản lý thông tin công trình, tài liệu được ưu tiên khảo sát trong giai đoạn 2018–2026 nhằm phản ánh sự phát triển gần đây của lĩnh vực. Các nghiên cứu có tính nền tảng về phương pháp đánh giá mô hình, kiểm soát rò rỉ dữ liệu, lý thuyết quản lý tài sản và các tiêu chuẩn liên quan được xem xét không phụ thuộc vào thời điểm công bố.

Ngoài nhà công nghiệp khung thép, khảo sát xét cả các nghiên cứu trên cầu, công trình dân dụng và loại tài sản xây dựng khác khi phương pháp hoặc kết quả của chúng liên quan trực tiếp đến bài toán quản lý thông tin, truy vết bằng chứng và hỗ trợ kiểm tra – bảo trì.

**b) Chiến lược khảo sát và tìm kiếm tài liệu**

Chiến lược tìm kiếm được xây dựng theo từng nhóm chủ đề, sử dụng các tổ hợp từ khóa tiếng Anh phản ánh đối tượng nghiên cứu, phương pháp và nội dung cần kiểm chứng.

Các nhóm từ khóa chính bao gồm:

- Quản lý tài sản và thông tin vận hành: asset management, facility management, operation and maintenance, asset information management.

- BIM và song sinh số: Building Information Modeling, Industry Foundation Classes, Digital Twin, BIM-enabled asset management.

- Theo dõi trạng thái kết cấu: structural health monitoring, vibration-based condition monitoring, bolted steel connections.

- Chất lượng bằng chứng và đánh giá mô hình: data leakage, grouped evaluation, independent experimental units, cross-campaign generalization, transferability.

- Truy vết và quản lý hồ sơ: information traceability, data provenance, IFC GlobalId, inspection records, maintenance records, semantic validation.

Các tổ hợp từ khóa được điều chỉnh theo từng nhóm nội dung nhằm tìm kiếm cả những nghiên cứu trực tiếp giải quyết bài toán và các nghiên cứu có phương pháp hoặc kết quả có thể sử dụng để đối chiếu, phản biện.

Một phần tài liệu ứng viên được gợi ý qua công cụ tìm kiếm học thuật có dùng trí tuệ nhân tạo (Consensus). Mỗi ứng viên được kiểm tên bài, tác giả, năm và DOI qua Crossref, nhập vào thư viện Zotero và chỉ được trích sau khi đọc ít nhất phần tóm tắt; mức đã đọc của từng tài liệu được ghi trong ma trận tài liệu.

Bên cạnh tìm kiếm theo từ khóa, quá trình khảo sát còn xem xét danh mục tài liệu tham khảo của các công trình trọng yếu và những nghiên cứu có liên quan được trích dẫn trong các công trình đó. Cách tiếp cận này nhằm nhận diện các nghiên cứu nền tảng, các phương pháp đã được xác lập và những tiền lệ gần với vấn đề nghiên cứu của luận án.

Đối với các phát biểu về khoảng trống nghiên cứu, việc khảo sát được thực hiện theo hướng tìm kiếm những công trình có khả năng phản biện hoặc thu hẹp phát biểu đó, thay vì chỉ lựa chọn các tài liệu ủng hộ định hướng nghiên cứu ban đầu.

**c) Quy trình sàng lọc và lựa chọn tài liệu**

Quá trình lựa chọn tài liệu được tổ chức theo năm bước.

Bước 1 – Thu thập và phân loại sơ bộ. Các tài liệu được thu thập theo nhóm chủ đề, xác định thông tin thư mục và phân loại sơ bộ theo mức độ liên quan đến vấn đề nghiên cứu.

Bước 2 – Kiểm tra và loại bỏ tài liệu trùng lặp. Các bản ghi được đối chiếu theo DOI, tên công trình, tác giả và năm công bố. Trường hợp một nghiên cứu có nhiều phiên bản công bố, ưu tiên sử dụng phiên bản đầy đủ và phù hợp nhất với nội dung cần phân tích.

Bước 3 – Sàng lọc theo tiêu đề và tóm tắt. Tài liệu được xem xét dựa trên mức độ liên quan đến các câu hỏi nghiên cứu, đối tượng nghiên cứu và các mắt xích trong chuỗi bằng chứng – truy vết – hỗ trợ hành động. Những công trình chỉ có sự tương đồng về từ khóa nhưng không đóng góp trực tiếp vào nội dung tổng quan được loại khỏi tập tài liệu phân tích trọng tâm.

Bước 4 – Đọc và đánh giá nội dung nghiên cứu. Các công trình được giữ lại được xem xét sâu hơn về mục tiêu, phương pháp, dữ liệu sử dụng, thiết kế kiểm chứng, kết quả và giới hạn nghiên cứu. Đối với các tài liệu trọng yếu, việc đánh giá tập trung vào phương pháp và kết quả được trình bày trong toàn văn, không chỉ dựa trên nội dung tóm tắt hoặc kết luận của tác giả.

Bước 5 – Tổng hợp và tổ chức bằng chứng. Các tài liệu phù hợp được đưa vào ma trận tổng hợp bằng chứng (Evidence Matrix) theo từng nhóm chủ đề và mắt xích của chuỗi nghiên cứu. Ma trận phân biệt nội dung đã được kiểm chứng, giới hạn của nghiên cứu và những vấn đề được tác giả đề xuất nhưng chưa có kết quả kiểm chứng tương ứng.

Tiêu chí lựa chọn ưu tiên các công trình có nội dung liên quan trực tiếp đến ít nhất một mắt xích của chuỗi nghiên cứu, trình bày rõ phương pháp và cung cấp bằng chứng có thể đánh giá được. Các tiêu chuẩn và tài liệu chính thức của tổ chức chuyên ngành được sử dụng để xác lập cơ sở khái niệm, yêu cầu thông tin và nguyên tắc kỹ thuật liên quan.

Chỉ những tài liệu đủ thông tin để đánh giá phương pháp và kết quả được dùng làm căn cứ chính để xác lập tính mới hay khoảng trống nghiên cứu.

**d) Đánh giá chất lượng và tổng hợp bằng chứng nghiên cứu**

Chất lượng bằng chứng được xem xét dựa trên sự phù hợp giữa mục tiêu nghiên cứu, phương pháp, loại dữ liệu sử dụng và kết luận được công bố.

Việc đánh giá tập trung vào ba nội dung:

Thứ nhất, xác định loại bằng chứng được sử dụng, bao gồm dữ liệu phòng thí nghiệm, dữ liệu hiện trường, dữ liệu mô phỏng hoặc các trường hợp kiểm chứng mô hình thông tin và quan hệ dữ liệu.

Thứ hai, xem xét quy mô, điều kiện và phạm vi kiểm chứng của từng nghiên cứu, đặc biệt là mức độ phù hợp giữa đối tượng được khảo sát và đối tượng nghiên cứu của luận án.

Thứ ba, phân biệt kết quả đã được kiểm chứng bằng dữ liệu với các đề xuất phương pháp, giả thuyết hoặc định hướng phát triển chưa được kiểm chứng.

Các nghiên cứu sử dụng dữ liệu mô phỏng hoặc trường hợp thử nghiệm giới hạn vẫn được xem xét khi cung cấp cơ sở lý thuyết hoặc phương pháp phù hợp. Tuy nhiên, bằng chứng từ các nghiên cứu này không được sử dụng để suy rộng trực tiếp về hiệu quả triển khai hoặc khả năng áp dụng trong điều kiện công trình thực.

Đối với từng khoảng trống nghiên cứu, các công trình có nội dung gần nhất được đối chiếu về mục tiêu, đối tượng, phương pháp, dữ liệu, kết quả và giới hạn. Những thành phần đã được nghiên cứu trước giải quyết được ghi nhận rõ; phần nghiên cứu còn lại chỉ được xác lập sau khi xem xét những tiền lệ có khả năng phản biện.

Quá trình tổng hợp tuân theo cấu trúc: luận điểm → bằng chứng → giới hạn → hàm ý nghiên cứu, qua đó hình thành cơ sở cho việc xác lập các câu hỏi nghiên cứu và thiết kế kiểm chứng của luận án.

Các tài liệu được giữ lại được tổ chức trong ma trận tổng hợp bằng chứng (Evidence Matrix), ghi cho mỗi nguồn nhóm chủ đề, mắt xích của chuỗi nghiên cứu, loại dữ liệu, phương pháp, nội dung đã được chính nghiên cứu kiểm chứng, giới hạn và khoảng trống mà nguồn đó góp phần xác lập hoặc thu hẹp. Ma trận được lưu thành tài liệu làm việc kèm theo, không đưa vào thân tiểu luận để giữ mạch lập luận.

**e) Giới hạn của phương pháp tổng quan**

Do phạm vi nghiên cứu liên quan đến nhiều lĩnh vực và sử dụng các nhóm tài liệu có đặc điểm phương pháp khác nhau, kết quả tổng quan không nhằm khẳng định đã bao phủ toàn bộ các công bố quốc tế liên quan.

Các phát biểu về khoảng trống nghiên cứu được giới hạn trong phạm vi tập tài liệu đã khảo sát và đối chiếu. Khi xuất hiện nghiên cứu có kết quả tương đương hoặc trực tiếp giải quyết vấn đề đã xác định, phát biểu về khoảng trống cần được xem xét và điều chỉnh phù hợp.

Nhật ký tìm kiếm có ngày thực hiện, chuỗi truy vấn nguyên văn và số bản ghi ở từng bước sàng lọc chưa được lưu đầy đủ; vì vậy tiểu luận không báo cáo sơ đồ dòng chảy tài liệu theo mẫu PRISMA. Danh mục tài liệu tham khảo gồm các nguồn được trích dẫn trong tiểu luận.

## 1.9. Mục tiêu, câu hỏi nghiên cứu và kiến trúc của luận án

### 1.9.1. Mục tiêu và câu hỏi nghiên cứu

Từ hai khoảng trống tổng hợp ở mục 5.2, luận án có ba mục tiêu, mỗi mục tiêu ứng với một câu hỏi nghiên cứu; phát biểu đầy đủ ở mục 5.3–5.4 và ma trận mục tiêu – câu hỏi – gói công việc – bài báo ở mục 5.5. Câu hỏi 1 đo mức chênh lệch giữa đánh giá cùng lần chạy và hai mức đánh giá theo đơn vị độc lập, giữ lại lần chạy và giữ lại đợt thí nghiệm, cho phân loại trạng thái liên kết bu lông trên khung thép 1:10, và khai báo phạm vi hiệu lực của từng kết quả. Câu hỏi 2 đánh giá một mô hình thông tin mở rộng IFC 4.3 và BCF 3.0 bằng tầng bằng chứng và tầng trách nhiệm, so với hồ sơ kiểm định hiện hành và với mô hình chỉ dùng chuẩn sẵn có. Câu hỏi 3 kiểm khả năng vận hành của chuỗi bằng chứng – hành động trên một nhà xưởng khung thép thật có BIM. Câu hỏi 1 ứng với vế A1 và phần khai báo của vế A2 thuộc KT1; Câu hỏi 2 ứng với KT2 và phần kiểm tại lần sử dụng của vế A2; Câu hỏi 3 kiểm hai khoảng trống trong điều kiện áp dụng. Cả ba câu hỏi phục vụ kiểm chứng luận đề ở Mục 5.3.1.

Mỗi câu hỏi cần một loại bằng chứng riêng, và kết quả của câu trước không dùng thay cho câu sau. Cảm biến, xử lý tín hiệu, học máy và BIM là công cụ tạo và tổ chức thông tin phục vụ quản lý.

### 1.9.2. Bốn lớp và chuỗi định danh

Kiến trúc nghiên cứu gồm bốn lớp, tương ứng với bốn loại bằng chứng ở mục 1.7.5: bằng chứng phòng thí nghiệm, truy vết thông tin, khả năng áp dụng trong bối cảnh thực tế và hỗ trợ quyết định quản lý. Các lớp kế tiếp nhau và không dùng thay cho nhau. Lớp 1 ứng với Mục tiêu 1, Lớp 2 với Mục tiêu 2, Lớp 3 với Mục tiêu 3; Lớp 4 dùng kết quả của Mục tiêu 2 và 3. Quan hệ một – một là giữa mục tiêu và câu hỏi nghiên cứu; bốn lớp là bốn loại bằng chứng mà ba mục tiêu tạo ra.

Chuỗi định danh lõi là *Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status*. *FEM_Node_ID*, nếu được dùng, chỉ là siêu dữ liệu tùy chọn của mô hình tham chiếu danh nghĩa và không nằm trong chuỗi bắt buộc.

*Chuỗi này là cách trình bày cho người đọc. Mô hình dữ liệu của luận án là một đồ thị sáu thực thể, trong đó sự kiện chuyển trạng thái là thực thể bắt buộc và trạng thái xử lý hiện thời được suy ra từ chuỗi sự kiện (mục 5.6.2).*

Nội dung đầy đủ của bốn lớp, nghĩa vụ kiểm chứng của từng mắt xích, thang kiểm chứng và quan hệ giữa luồng dữ liệu với luồng trách nhiệm được trình bày ở Chương 5, mục 5.6.

### 1.9.3. Định vị bóng số trong kiến trúc

Khung nghiên cứu duy trì mối liên hệ có cập nhật giữa tài sản vật lý, biểu diễn số, bằng chứng trạng thái, bản ghi kiểm tra và trạng thái hành động. Mức tích hợp của hệ thống được khai báo ở Mục 1.1.3; các khung của Sepasgozar (2021) và Chen và cộng sự (2021) được dùng để đánh giá năng lực đạt được sau triển khai \[9\], \[10\]. Chức năng nằm ngoài phạm vi luận án không được bổ sung chỉ để đạt mức phân loại cao hơn (mục 5.6.6).

## 1.10. Cấu trúc của Tiểu luận tổng quan

Tiểu luận gồm năm chương, đi từ nền quản lý tới bằng chứng kỹ thuật, truy vết thông tin và định hướng nghiên cứu.

Chương 1 (Giới thiệu và phương pháp tổng quan) trình bày bối cảnh, vấn đề quản lý trung tâm, sự cần thiết, mục tiêu, phạm vi, phương pháp tổng quan, mục tiêu và câu hỏi nghiên cứu của luận án và kiến trúc tổng thể ở mức giới thiệu.

Chương 2 (Tổng quan về quản lý tài sản và song sinh số trong giai đoạn vận hành) xây dựng nền lý luận về quản lý tài sản, thông tin vận hành, BIM/IFC, định danh cấu kiện, song sinh số, khả năng liên thông, nguồn gốc dữ liệu và con người trong vòng lặp; chương giải thích vì sao BIM/IFC mới là điều kiện nền, chưa tự tạo ra khả năng truy vết.

Chương 3 (Tổng quan về dữ liệu dao động và bằng chứng trạng thái) tập trung vào điều kiện để một kết quả từ dữ liệu dao động trở thành bằng chứng có thể kiểm lại, qua các nội dung về đơn vị vật lý độc lập, rò rỉ dữ liệu, đánh giá theo nhóm, khả năng chuyển giao, độ bất định, nguồn gốc và phạm vi hiệu lực.

Chương 4 (Tổng quan về truy vết bằng chứng và hỗ trợ kiểm tra – bảo trì) tổng quan các nghiên cứu về tích hợp cảm biến – BIM, hồ sơ kiểm tra và sửa chữa, định danh, nguồn gốc dữ liệu, kiểm chứng quan hệ, khả năng áp dụng trong bối cảnh thực tế, con người trong vòng lặp và trạng thái hành động.

Chương 5 (Tổng hợp khoảng trống và định hướng nghiên cứu) tổng hợp những nội dung đã được giải quyết, phát biểu hai khoảng trống còn lại, rồi trình bày luận đề trung tâm, ba mục tiêu và ba câu hỏi nghiên cứu, ma trận mục tiêu – gói công việc – bài báo – thiết kế kiểm chứng, kiến trúc bóng số dựa trên dữ liệu, công cụ trí tuệ nhân tạo, đóng góp dự kiến, phạm vi và định hướng nghiên cứu tiếp theo.

Chương 2 bắt đầu từ lớp ngoài cùng của chuỗi: bối cảnh quản lý tài sản đặt ra yêu cầu gì đối với thông tin vận hành, và BIM/IFC cùng song sinh số đáp ứng được tới đâu.
