# CHƯƠNG 3. TỔNG QUAN VỀ DỮ LIỆU DAO ĐỘNG VÀ BẰNG CHỨNG TRẠNG THÁI

## 3.1. Dữ liệu dao động trong theo dõi trạng thái kết cấu

### 3.1.1. Theo dõi trạng thái kết cấu dựa trên dao động

Theo dõi trạng thái kết cấu dựa trên dao động (vibration-based structural health monitoring) dựa trên nguyên lý: thay đổi đặc trưng động lực học có thể phản ánh thay đổi trạng thái vật lý của kết cấu. Hướng này đã phát triển từ các phương pháp dựa trên đặc trưng động lực truyền thống tới học máy và học sâu. Các tổng quan gần đây cho thấy khó khăn nằm ở cả việc chọn mô hình, cách kiểm chứng kết quả lẫn khả năng chuyển từ điều kiện kiểm soát ra thực tế \[13\].

Biến thiên môi trường và vận hành là yếu tố chi phối mạnh nhất. Sohn (2007) chỉ ra rằng biến đổi do nhiệt độ, tải trọng vận hành hoặc điều kiện sử dụng có thể có biên độ tương đương hoặc lớn hơn thay đổi do trạng thái kết cấu \[45\]. Keshmiry và cộng sự (2023) xác nhận vai trò của điều kiện môi trường và vận hành trong theo dõi trạng thái kết cấu và kiểm tra không phá hủy \[46\]. Hệ quả phương pháp là kết quả phân loại chỉ có ý nghĩa khi đi kèm bối cảnh tạo ra nó. Điều kiện thu nhận, cấu hình cảm biến, trạng thái lắp đặt, đợt đo và điều kiện môi trường là một phần của ngữ cảnh diễn giải bằng chứng.

### 3.1.2. Theo dõi trạng thái liên kết bu lông trong khung thép

Liên kết bu lông đã được theo dõi bằng nhiều phương pháp, trong đó có dữ liệu dao động và học máy. Trên khung thép, trạng thái liên kết có thể được phân biệt trong phòng thí nghiệm bằng dữ liệu cảm biến và nhiều mô hình phân loại \[47\]–\[50\]. Luận án vì vậy kế thừa việc dùng học máy và học sâu để phân loại trạng thái liên kết bu lông. Giá trị của một nghiên cứu mới nằm ở cách tổ chức thí nghiệm, định nghĩa đơn vị độc lập, cách chia dữ liệu, kiểm soát rò rỉ và phạm vi mà kết quả được kiểm chứng.

Bảng 3.1 đối chiếu một số nghiên cứu đại diện theo ba tiêu chí thường quyết định mức tin cậy của kết quả: đối tượng vật lý, cách chia dữ liệu và cấu hình cảm biến.

<span id="TLTQ_Bang_3_1" class="anchor"></span>Bảng 3.1. Một số nghiên cứu đại diện về đơn vị vật lý và cách đánh giá dữ liệu

| Nghiên cứu | Đối tượng | Đơn vị vật lý | Cách chia dữ liệu | Cấu hình cảm biến | Hàm ý phương pháp |
|:---|:---|:---|:---|:---|:---|
| Zhang và cộng sự (2020) \[47\] | Khung thép, liên kết bu lông | Bản ghi từ gia tốc kế | Không mô tả rõ phép chia theo đơn vị vật lý | Một cảm biến | Cho thấy tiền lệ về đối tượng nghiên cứu |
| Pal và cộng sự (2022) \[48\] | Khung thép phẳng một tầng, liên kết dầm – cột | Lần kích thích vật lý | Chia theo lần thử | Sáu cảm biến biến dạng | Cho thấy tầm quan trọng của mô tả rõ cấu trúc chia dữ liệu |
| Biswal và cộng sự (2022) \[49\] | Khung thép cổng một nhịp | Lần kích thích vật lý | Không xây dựng quy trình huấn luyện – kiểm tra hoàn chỉnh | Sáu gia tốc kế | Tiền lệ về trạng thái liên kết |
| Parziale và cộng sự (2024) \[50\] | Khung thép quy mô lớn | Lần thu tín hiệu | Tạo cửa sổ trước rồi chia ngẫu nhiên các ảnh đầu vào | Cấu hình cảm biến cố định | Minh họa rủi ro khi cửa sổ từ cùng nguồn vật lý xuất hiện ở hai phía phép chia |
| Dadoulis và Manolis (2026) \[51\] | Dầm thép chịu khối lượng di động | Một lượt chuyển động | Huấn luyện trên mô phỏng, kiểm tra trên dữ liệu thí nghiệm | Ba nút gia tốc | Cho thấy cách đánh giá đóng góp cảm biến |
| Beleites và cộng sự (2013) \[14\] | Dữ liệu quang phổ ngoài lĩnh vực xây dựng | Người hiến/mẻ nuôi cấy | So sánh chia theo quan sát với chia theo nhóm nguồn | Không áp dụng | Cung cấp nguyên tắc về đơn vị độc lập |
| Wheat và cộng sự (2024) \[15\] | Bệ thử ổ lăn | Lần chạy, ngày đo, chi tiết vật lý | Giữ lại theo nhiều cấp nguồn vật lý | Hai vị trí gia tốc | Cho thấy cấp chia dữ liệu ảnh hưởng mạnh tới hiệu năng |

Bảng này cho thấy một bất đối xứng lặp lại: các nghiên cứu trên khung thép thường có số lần thử vật lý nhỏ hơn rất nhiều so với số cửa sổ tín hiệu tạo ra từ các lần thử đó. Số cửa sổ vì vậy không thể hiểu là cỡ mẫu độc lập. Đây là điểm nối giữa thí nghiệm dao động và thiết kế đánh giá thống kê, nơi phát sinh phần lớn các rủi ro phân tích ở mục 3.4.

### 3.1.3. Phân biệt bằng chứng trạng thái và chẩn đoán hư hỏng

Theo định nghĩa ở Mục 1.3, đầu ra của một mô hình phân loại trên dữ liệu dao động là kết quả phân loại; kết quả đó trở thành bằng chứng trạng thái (condition evidence) khi được ghi kèm nguồn gốc, độ bất định và phạm vi hiệu lực. Ở chương này, bằng chứng trạng thái được xét cho nguồn dữ liệu dao động: nhãn trạng thái, xác suất hoặc điểm số, cùng bối cảnh đã tạo ra kết quả. Kết luận về hư hỏng vật lý, mức độ nghiêm trọng hoặc chỉ số sức khỏe của cấu kiện thuộc về kiểm tra của kỹ sư.

Sự phân biệt này cần thiết vì nhãn và trạng thái vật lý không tương ứng một–một theo cả hai chiều. Theo chiều thứ nhất, nhãn phân loại phụ thuộc vào nhiều yếu tố ngoài trạng thái vật lý: cấu hình cảm biến, đợt thí nghiệm, điều kiện lắp đặt, đường cơ sở tham chiếu, phiên bản dữ liệu và chuỗi xử lý. Thay đổi một yếu tố có thể làm đổi kết quả mà không có thay đổi vật lý tương ứng. Theo chiều ngược lại, dữ liệu dao động một mình chưa xác định được nguyên nhân của một thay đổi vật lý thực; tín hiệu còn chịu ảnh hưởng của điều kiện môi trường, vận hành, lắp đặt và lịch sử can thiệp. Dữ liệu dao động vì vậy cung cấp dấu hiệu thay đổi trạng thái; nguyên nhân phải được xác nhận bằng hoạt động kiểm tra phù hợp.

Từ đó, luận án giữ quy tắc chung ở Mục 1.7.5: bất thường trong bằng chứng dao động dẫn tới yêu cầu kiểm tra. Kết quả phòng thí nghiệm được dùng trong phạm vi đã thí nghiệm, và bộ phân loại chỉ được áp sang công trình thực sau khi kiểm tra phạm vi hiệu lực (Mục 5.9.2).

## 3.2. Hạn chế của quan trắc hiện tại với công trình công nghiệp

Ở nhà xưởng khung thép, thông tin về tình trạng liên kết hiện đến từ hai đường: kiểm tra trực quan định kỳ của kỹ sư và quan trắc bằng cảm biến. Mục này tổng hợp giới hạn của từng đường khi áp cho công trình công nghiệp, rồi xét điều kiện để bằng chứng tạo ra trong phòng thí nghiệm được dùng ở hiện trường. Nhiều nguồn dưới đây nghiên cứu cầu hoặc kết cấu ngoài trời; phần bằng chứng được trích đúng đối tượng của nguồn, còn việc áp sang nhà xưởng được ghi là diễn giải.

### 3.2.1. Kiểm tra trực quan: kết quả phụ thuộc người kiểm tra

Kiểm tra trực quan là phương pháp chủ đạo trong thực hành kiểm tra công trình. Nghiên cứu của Cục Đường bộ Liên bang Hoa Kỳ (FHWA) với 49 kiểm tra viên trên các cầu thử nghiệm cho thấy phương pháp này mang tính chủ quan cao. Chỉ khoảng 68 % điểm tình trạng nằm trong phạm vi ±1 điểm quanh giá trị trung bình \[@23ZIDHJX\] (tr. 67, 71, 82). Trong nhiệm vụ kiểm tra chi tiết một cầu thép, tỷ lệ phát hiện đúng các liên kết bu lông có đai ốc hở ít nhất 4 mm chỉ là 24 % \[@23ZIDHJX\] (tr. 78). Cùng nghiên cứu đó, Phares và cộng sự (2004) ghi nhận điểm tình trạng, ghi chú hiện trường và ảnh đều biến thiên lớn giữa các kiểm tra viên, và khuyết tật quan trọng nhiều khi không được ghi lại trong hồ sơ \[@IB6Q2FEH\] (tr. 403, 408, 412–413).

Theo đánh giá của phần tổng quan nghiên cứu này, kết quả trên dẫn tới hai diễn giải cho nhà xưởng. Khuyết tật bu lông trong nghiên cứu trên là loại nhìn thấy được. Mất lực siết không kèm dấu hiệu hình học còn khó phát hiện bằng mắt hơn, trong khi liên kết nhà xưởng thường nằm trên cao và việc tiếp cận tốn kém (mục 1.2.3). Kết quả kiểm tra của con người cũng có độ bất định và phụ thuộc người thực hiện. Vì vậy bản ghi kiểm tra cần mang thông tin về người kiểm tra, thời điểm và độ bất định của phát hiện, như các trường của bản ghi kiểm tra ở Phụ lục A.

### 3.2.2. Quan trắc cảm biến: chi phí và mật độ đo

Cawley (2018) so sánh bốn nhóm theo dõi và chỉ ra rằng số cảm biến cần để phủ toàn kết cấu tăng mạnh khi chuyển từ theo dõi toàn cục sang theo dõi cục bộ. Theo dõi cục bộ mọi vị trí cần thiết thường quá đắt, nên kiểm tra không phá hủy định kỳ hiệu quả hơn \[@EBB69J4F\] (tr. 2, Bảng 1; tr. 10–11). Quan trắc phải cạnh tranh với kiểm tra định kỳ hay thay thế theo kế hoạch, thông tin thêm phải đáng với chi phí, và chi phí cần tính đủ gồm bảo trì hệ đo và xử lý dữ liệu lặp lại \[@EBB69J4F\] (tr. 12). Worden và cộng sự (2007) cũng xếp chi phí vào các yếu tố quyết định khi chọn phần cứng \[@MCNRW6F5\] (tr. 1656).

Nhà xưởng có nhiều liên kết bu lông cùng loại phân bố trên toàn khung. Theo đánh giá của phần tổng quan nghiên cứu này, quan trắc dày đặc mọi liên kết của loại tài sản này khó có cơ sở kinh tế. Hướng khả thi là đặt số ít cảm biến ở các liên kết đại diện và dùng tín hiệu để khoanh vùng cấu kiện cần kiểm tra. Luận án vì vậy ghi nhận chi phí như một kết quả đo của Mục tiêu 3, thay vì giả định trước.

### 3.2.3. Biến đổi vận hành và môi trường trong nhà xưởng

Mục 3.1.1 đã nêu biến đổi môi trường – vận hành là yếu tố chi phối mạnh nhất. Các nguồn đã đọc cho thấy rõ hơn cơ chế của nó. Sohn (2007) dẫn ví dụ tàu lượn, nơi khác biệt đặc trưng động lực do tải hành khách lớn hơn nhiều so với khác biệt do hư hỏng bánh xe. Tác giả coi chuẩn hóa dữ liệu theo điều kiện vận hành là một trở ngại chính khi triển khai \[45\] (tr. 539–540, 543–544, 557). Tiên đề IVb của Worden và cộng sự (2007) phát biểu rằng nếu không có trích chọn đặc trưng thông minh, độ nhạy của phép đo với hư hỏng càng cao thì độ nhạy với thay đổi điều kiện vận hành – môi trường càng cao \[@MCNRW6F5\] (tr. 1652–1654). Figueiredo và cộng sự (2011) làm trên khung nhôm ba tầng lắp bu lông trong phòng thí nghiệm, với biến đổi vận hành – môi trường mô phỏng. Nhóm tác giả cho thấy biến đổi này có thể che lấp đặc trưng do hư hỏng và so sánh các thuật toán học mô hình trạng thái bình thường để tách hai loại thay đổi \[@23TBQTIP\] (tr. 561–562, 564, 571). Cawley (2018) cũng nêu rằng tần số các dạng dao động thấp nhạy với điều kiện biên, khối lượng và nhiệt độ hơn với hư hỏng cục bộ \[@EBB69J4F\] (tr. 4, 9).

Trong nhà xưởng, nguồn biến đổi vận hành gồm cầu trục, máy móc và chu kỳ nhiệt theo ca sản xuất và theo mùa. Ju và cộng sự (2020) cho thấy rung do cầu trục di chuyển trong một nhà máy công nghệ cao phụ thuộc vận tốc, gia tốc và độ gồ ghề ray \[@38FMATHE\]. Nghiên cứu này xét rung sàn. Việc rung cầu trục che lấp tín hiệu liên kết trong khung nhà xưởng là đánh giá của phần tổng quan nghiên cứu này, và chưa có nguồn đã đọc kiểm chứng trực tiếp. Từ đó, đường cơ sở vận hành của nhà xưởng cần ghi kèm trạng thái cầu trục và nhiệt độ, và luận án dùng hồi quy theo nhiệt độ cùng cờ cầu trục chạy/dừng làm mức bù tối thiểu (Mục 5.7.3).

### 3.2.4. Cầu nối phòng thí nghiệm – hiện trường

Các mục 3.4 và 3.5 xác lập điều kiện để kết quả phòng thí nghiệm trở thành bằng chứng có phạm vi hiệu lực. Tiểu mục này xét điều gì ngăn bằng chứng đó được dùng nguyên ở nhà xưởng. Cawley (2018) nhận xét nhiều nghiên cứu làm trên dầm, tấm đơn giản trong phòng thí nghiệm, trong khi vấn đề thực chỉ lộ ra trên kết cấu thật với biến đổi môi trường thực \[@EBB69J4F\] (tr. 14–15); Sohn (2007) cũng ghi nhận thành công trên mô hình thu nhỏ và mẫu thí nghiệm chưa bảo đảm hiệu quả ở hiện trường \[45\] (tr. 539–540, 558).

Bốn nhóm bằng chứng cho thấy bộ phân loại học ở phòng thí nghiệm khó chuyển nguyên sang nhà xưởng. Thứ nhất, nhãn hiện trường đến từ kiểm tra của chuyên gia nên hiếm và đắt; thiếu nhãn, học không giám sát dừng ở bậc phát hiện bất thường trong phân cấp của Rytter \[@87NKU5IS\]. Mỗi công trình còn có điều kiện biên và vật liệu riêng \[@TDRPDWJE\], và dữ liệu đo phủ đủ các điều kiện vận hành và hư hỏng của một công trình hiếm khi có sẵn \[57\]. Thứ hai, ở kết cấu có mối nối, quy trình lắp ráp quyết định độ lặp lại; thiếu kiểm soát lắp ráp, độ bất định đo được có thể lớn hơn độ dịch tần số do phi tuyến của mối nối \[18\]. Thứ ba, biến đổi môi trường – vận hành có thể che lấp thay đổi do hư hỏng, nên dữ liệu huấn luyện phải phủ dải điều kiện rộng \[45\]. Thứ tư, bộ phân loại lực siết học trên một dầm liên kết bu lông đã thất bại khi áp trực tiếp sang dầm tương tự \[56\]. Câu hỏi khi nào tri thức được chuyển giữa các kết cấu được xét ở Mục 3.4.3 \[57\].

Phần chuyển được từ phòng thí nghiệm sang hiện trường vì vậy là nguyên tắc tổ chức bằng chứng và giao thức đánh giá. Bộ phân loại và ngưỡng của mô hình 1:10 chỉ được dùng ở hiện trường sau khi kiểm tra phạm vi hiệu lực. Cách luận án đổi vai công cụ AI ở hiện trường dựa trên bốn nhóm bằng chứng này được trình bày ở Mục 5.7.3.

### 3.2.5. Hàm ý cho luận án

Bốn giới hạn trên cùng dẫn tới một yêu cầu. Ở nhà xưởng, cả kết quả kiểm tra của kỹ sư lẫn tín hiệu cảm biến đều cần được ghi thành bằng chứng mang nguồn gốc, độ bất định và phạm vi hiệu lực, gắn với cấu kiện và với hành động xử lý. Cảm biến có giá trị nhất khi khoanh vùng cấu kiện cần kiểm tra trước; kiểm tra của kỹ sư xác lập tình trạng và tạo nhãn hiện trường cho các lần đánh giá sau. Cách tổ chức các bằng chứng này thành đối tượng thông tin được trình bày ở mục 3.5 và Chương 4.

## 3.3. Cảm biến và chuỗi xử lý dữ liệu

### 3.3.1. Loại, số lượng và cấu hình cảm biến

Các nghiên cứu dùng nhiều loại và số lượng cảm biến, phổ biến nhất là gia tốc kế và cảm biến biến dạng, từ vài vị trí tới mạng đo nhiều điểm. Phần lớn dùng một cấu hình cố định và tập trung vào mô hình phân loại, ít đánh giá có kiểm soát ảnh hưởng của chính cấu hình đó.

Cấu hình cảm biến là một phần của điều kiện tạo bằng chứng: kết quả đạt được với một tổ hợp cảm biến không mặc nhiên giữ nguyên khi số lượng hay vị trí thay đổi. Wheat và cộng sự (2024) cho thấy vị trí cảm biến ảnh hưởng tới hiệu năng ngay trong một giao thức đánh giá giữ nguyên \[15\]; Dadoulis và Manolis (2026) định lượng đóng góp của từng kênh đo \[51\]. Trong luận án, cấu hình cảm biến là một thành phần của phạm vi hiệu lực và được ghi vào bối cảnh quan trắc của mỗi bằng chứng (Phụ lục A). Tối ưu vị trí cảm biến nằm ngoài phạm vi luận án (Mục 5.9.1).

### 3.3.2. Tiền xử lý, phân đoạn và tạo đầu vào

Chuỗi xử lý dữ liệu dao động thường gồm cắt đoạn tín hiệu, lọc, chuẩn hóa, biến đổi miền tần số hoặc thời gian – tần số, rút đặc trưng hoặc tạo đầu vào trực tiếp cho mô hình học sâu. Hai khâu đặc biệt nhạy với kết quả đánh giá.

Khâu thứ nhất là phân đoạn tín hiệu. Khi một bản ghi được chia thành nhiều cửa sổ, các cửa sổ cùng xuất phát từ một lần thu vật lý thuộc cùng một đơn vị độc lập (mục 3.4.1). Với cửa sổ chồng lấn, mức phụ thuộc còn lớn hơn vì chúng chia sẻ trực tiếp nhiều mẫu tín hiệu. Cửa sổ vì vậy là đơn vị tính toán, không mặc nhiên là đơn vị suy luận thống kê.

Khâu thứ hai là thứ tự giữa phép chia tập và các phép biến đổi có tham số học được. Nếu trung bình, độ lệch chuẩn, phép giảm chiều hoặc các tham số khác được ước lượng trên toàn bộ dữ liệu trước khi chia, thông tin của tập kiểm tra đã đi vào quá trình xây dựng mô hình. Amin và cộng sự (2026) cung cấp tiền lệ cho cách làm ngược lại: chia theo sự kiện vật lý trước, sau đó chỉ học các phép biến đổi từ phần huấn luyện \[52\]. Nguyên tắc rút ra là chia dữ liệu theo đơn vị vật lý trước khi thực hiện các phép biến đổi có thể học từ dữ liệu, và ước lượng mọi tham số tiền xử lý chỉ từ tập huấn luyện trong từng lượt đánh giá.

### 3.3.3. Học máy và học sâu như công cụ tạo bằng chứng

Các mô hình được sử dụng trong theo dõi trạng thái dao động trải rộng từ hồi quy logistic, máy véc-tơ hỗ trợ, rừng ngẫu nhiên tới mạng nơ-ron tích chập và nhiều kiến trúc học sâu khác. Trong nghiên cứu này, chúng là công cụ tạo bằng chứng, kế thừa từ các nghiên cứu ở mục 3.1.2.

Hiệu năng của mô hình chỉ có ý nghĩa khi giao thức đánh giá đủ chặt. Wheat và cộng sự (2024) cho thấy chỉ cần đổi cấp phân tách dữ liệu là hiệu năng đo được trên cùng một bài toán rung động đã thay đổi mạnh. So sánh kiến trúc mô hình dưới một giao thức chưa kiểm soát đơn vị độc lập hoặc rò rỉ dữ liệu có thể cho kết luận không ổn định \[15\]. Câu hỏi phù hợp là bằng chứng do mô hình tạo ra đáng tin trong phạm vi nào. Trọng tâm vì thế dịch từ tối ưu thuật toán sang thiết kế thí nghiệm, giao thức đánh giá và phạm vi diễn giải.

## 3.4. Độ tin cậy của bằng chứng trạng thái

### 3.4.1. Đơn vị vật lý độc lập và lặp giả

Vấn đề thứ nhất của dữ liệu dao động là xác định đâu là đơn vị vật lý độc lập. Nhiều cửa sổ tạo ra từ cùng một bản ghi không làm tăng số lần thí nghiệm độc lập. Nếu coi chúng như các quan sát hoàn toàn độc lập, cỡ mẫu biểu kiến có thể lớn hơn rất nhiều so với cỡ mẫu vật lý thực. Beleites và cộng sự (2013) minh họa hiện tượng lặp giả (pseudoreplication) trong một lĩnh vực khác, hóa phân tích với dữ liệu quang phổ. Hàng nghìn quan sát ở cấp thấp vẫn chỉ đại diện cho số lượng hữu hạn các nguồn vật lý độc lập ở cấp cao. Nguyên tắc chuyển giao được sang dữ liệu dao động là cấp dùng cho suy luận phải phản ánh nguồn độc lập thực sinh ra dữ liệu \[14\].

Trong thí nghiệm dao động, cấu trúc dữ liệu thường có dạng phân cấp:

Đợt thí nghiệm → đợt lắp đặt (trạng thái lắp ráp) → lần chạy → bản ghi → cửa sổ tín hiệu

Cửa sổ tín hiệu nằm ở cấp thấp nhất và là đơn vị tính toán. Lần chạy thường là cấp vật lý phù hợp hơn cho đánh giá trong cùng một đợt; khi mục tiêu là kiểm tra khả năng chuyển giao qua đợt lắp đặt hoặc qua đợt thí nghiệm, cấp độc lập phải được nâng lên tương ứng. Chọn đúng đơn vị độc lập vì vậy quyết định trực tiếp phạm vi diễn giải của kết quả, ngoài ý nghĩa thống kê.

### 3.4.2. Rò rỉ dữ liệu và đánh giá theo nhóm

Rò rỉ dữ liệu (data leakage) xảy ra khi thông tin từ phần kiểm tra ảnh hưởng tới quá trình huấn luyện, khiến hiệu năng đo được cao hơn khả năng thực trên dữ liệu mới. Với dữ liệu dao động có cấu trúc phân cấp, rò rỉ xuất hiện qua ba đường tương ứng với ba cấp của cấu trúc đó.

Đường thứ nhất nằm ở cấp cửa sổ: tạo cửa sổ trước rồi chia ngẫu nhiên. Khi các cửa sổ từ cùng một bản ghi nằm ở cả tập huấn luyện và kiểm tra, mô hình có thể học đặc điểm riêng của bản ghi thay vì đặc điểm chung của trạng thái. Đường thứ hai nằm ở cấp chuỗi xử lý: tiền xử lý trên toàn bộ dữ liệu trước khi chia; cách kiểm soát là học mọi tham số tiền xử lý chỉ trên phần huấn luyện. Đường thứ ba, khó nhận ra nhất, nằm ở cấp cao hơn cấp đang được chia \[53\]. Wheat và cộng sự (2024) cho thấy ngay cả khi đã tách theo lần chạy, dữ liệu vẫn có thể chia sẻ cùng ngày đo hoặc cùng chi tiết vật lý \[15\]. Vieira và cộng sự (2026) cho thấy chỉ cần dùng cùng một chi tiết vật lý ở hai phía phép chia là hiệu năng đo được đã trở nên lạc quan \[20\].

Biện pháp tổng quát là đánh giá theo nhóm (grouped evaluation): toàn bộ dữ liệu phát sinh từ cùng một nguồn vật lý phải nằm trọn ở một phía của phép chia. Cấp nhóm được chọn theo câu hỏi nghiên cứu, không theo mức chặt chẽ hình thức. Nếu câu hỏi chỉ yêu cầu khái quát sang lần chạy mới trong cùng đợt, nhóm ở cấp lần chạy là phù hợp; nếu câu hỏi yêu cầu chuyển sang đợt thí nghiệm mới, phải giữ lại toàn bộ đợt \[54\].

Rò rỉ dữ liệu đã được nhận diện rộng trong học máy nói chung và trong bảo trì theo tình trạng \[55\]. Luận án kế thừa yêu cầu kiểm soát rò rỉ từ các nghiên cứu này như điều kiện để kết quả có giá trị.

### 3.4.3. Đánh giá giữ lại một lần chạy và giữ lại một đợt thí nghiệm

Mốc so sánh của luận án là đánh giá cùng lần chạy (within-run evaluation): tập huấn luyện và tập kiểm tra được chia bên trong cùng các lần chạy, nên dữ liệu kiểm tra có thể đến từ lần chạy đã có trong huấn luyện. Hai nghiên cứu đã rà soát cho bài toán phân loại liên kết bu lông trên khung thép chia tập trong cùng lần lắp ráp hoặc cùng bản ghi \[48\], \[@VVBGM9EN\] (Mục 5.2.1). Chênh lệch giữa mốc này và hai giao thức dưới đây là đại lượng mà vế A1 của KT1 cần đo.

Luận án sử dụng hai giao thức đánh giá theo nhóm để trả lời hai câu hỏi khác nhau. Đánh giá giữ lại một lần chạy (Leave-One-Run-Out – LORO) giữ toàn bộ dữ liệu của một lần chạy làm tập kiểm tra và huấn luyện trên các lần chạy còn lại. Giao thức này đánh giá khả năng khái quát sang một lần chạy độc lập trong phạm vi cùng một đợt thí nghiệm. Đánh giá giữ lại một đợt thí nghiệm (Leave-One-Campaign-Out – LOCO) giữ toàn bộ dữ liệu của một đợt làm tập kiểm tra. Giao thức này khắt khe hơn vì đợt mới có thể đi kèm tháo – lắp lại cảm biến, thay đổi trạng thái tiếp xúc, điều kiện môi trường cùng các yếu tố vận hành khác.

Mức khắt khe của LOCO có cơ sở vật lý. Brake, Schwingshackl và Reuß (2019) cho thấy quá trình lắp ráp và trạng thái tiếp xúc tạo biến thiên lớn trong kết cấu có liên kết \[18\]. Ramasso, de Oliveira Teloli và Marcel (2025) ghi nhận hiệu năng trong cùng đợt và trên đợt chưa thấy có thể chênh lệch rõ khi liên kết được tháo – lắp lại \[19\]. Da Silva và cộng sự (2024) minh họa khó khăn khi chuyển mô hình giữa các mẫu liên kết danh nghĩa tương tự nhau \[56\].

Hai giao thức trả lời hai câu hỏi tách biệt. LORO cho biết bằng chứng có khái quát sang một lần chạy mới trong cùng bối cảnh thí nghiệm hay không, còn LOCO cho biết bằng chứng có giữ giá trị khi chuyển sang đợt thí nghiệm khác hay không. Kết quả LORO có giá trị trong cùng bối cảnh thí nghiệm; dùng cho đợt mới cần kết quả LOCO, và dùng cho công trình thực cần kiểm chứng riêng. Một kết quả LOCO thấp vẫn giữ giá trị của bằng chứng trong cùng đợt và cho thấy phạm vi hiệu lực hẹp hơn. Cách đọc này quan trọng khi bằng chứng đi sang lớp quản lý thông tin, nơi người dùng thường không tiếp cận được giao thức đánh giá gốc.

Ở mức tổng quát hơn, dòng nghiên cứu theo dõi trạng thái theo quần thể đặt câu hỏi khi nào tri thức được phép chuyển giữa các kết cấu. Với nhóm kết cấu gần như đồng nhất, một dạng chung được xây cho cả nhóm và dùng cho thành viên thiếu dữ liệu \[57\]. Với nhóm kết cấu dị thể, mỗi kết cấu được quy về đồ thị thuộc tính và mức tương đồng phải được đo trước khi bàn tới chuyển giao \[58\]. Khung này đặt ra điều kiện cho bước từ mô hình thu nhỏ sang công trình thực: phát biểu rõ mức tương đồng giữa hai kết cấu trước khi nói kết quả trên mô hình có ý nghĩa gì cho công trình. Phần luận án chuyển từ mô hình 1:10 sang công trình là nguyên tắc tổ chức và truy vết bằng chứng, còn mức tương đồng vật lý được ghi nhận như một giới hạn của kết quả (Mục 3.2.4).

### 3.4.4. Các cơ chế đánh giá bổ trợ

Ngoài LORO và LOCO, bốn cơ chế bổ trợ giúp mô tả độ ổn định của bằng chứng. Lặp lại với nhiều hạt giống ngẫu nhiên tách được biến thiên do khởi tạo hoặc huấn luyện mô hình khỏi biến thiên do dữ liệu. Báo cáo độ bất định ở cấp đơn vị độc lập cho biết kết quả trung bình có ổn định qua các lần chạy hoặc các nhóm vật lý hay không. Kiểm định hoán vị tạo phân phối ngẫu nhiên thực nghiệm để đánh giá liệu hiệu năng quan sát được có vượt mức có thể xuất hiện do may rủi hay không \[59\]. Trên dữ liệu có cấu trúc nhóm, phép hoán vị phải bảo toàn cấu trúc đơn vị độc lập. Cuối cùng, mức ngẫu nhiên thực nghiệm đặc biệt cần thiết khi số đơn vị kiểm tra nhỏ, vì mức ngẫu nhiên lý thuyết có thể dẫn tới diễn giải sai hiệu năng trong các tập mẫu nhỏ \[60\].

Các thủ tục này là công cụ kiểm chứng, kế thừa từ \[59\], \[60\]; chúng giúp báo cáo bằng chứng kèm mức ổn định và mức chắc chắn phù hợp.

## 3.5. Nguồn gốc và phạm vi hiệu lực của bằng chứng trạng thái

### 3.5.1. Bằng chứng trạng thái như một bản ghi có bối cảnh

Nếu giá trị của một nhãn phụ thuộc vào nguồn thu, cấu hình cảm biến, phiên bản dữ liệu, chuỗi xử lý và giao thức đánh giá, thì nhãn đó không nên tồn tại như một con số tách rời. Nó cần được tổ chức thành một bản ghi mang đủ bối cảnh để người sử dụng hiểu được bằng chứng đã được tạo ra như thế nào và được phép dùng trong phạm vi nào.

Cần phân biệt hai mức độ tin cậy thường bị gộp làm một. Mức thứ nhất là độ tin cậy của một dự đoán riêng lẻ, thường là xác suất hậu nghiệm hoặc điểm số do mô hình sinh ra cho một mẫu. Đại lượng này phụ thuộc vào cách hiệu chỉnh của mô hình và có thể cao ngay cả khi mô hình sai. Mức thứ hai là hiệu năng, độ bất định và phạm vi hiệu lực đã được kiểm chứng của chính mô hình sinh ra dự đoán đó. Đó là kết quả đo được dưới một giao thức đánh giá xác định, trên các đơn vị vật lý độc lập và trong một phạm vi đã nêu rõ. Bản ghi Condition_Evidence_ID phải lưu cả hai mức và ghi rõ mức nào đang được dùng khi diễn giải. Điểm tin cậy của một dự đoán không được đọc như mức tin cậy của bằng chứng, và mức tin cậy của bằng chứng chỉ có nghĩa trong phạm vi hiệu lực đã ghi.

Ở mức tối thiểu, một bản ghi bằng chứng trạng thái cần gắn với:

- nguồn thu dữ liệu, gồm đợt thí nghiệm và lần chạy;

- cấu hình cảm biến;

- phiên bản dữ liệu và chuỗi xử lý;

- giao thức đánh giá;

- độ bất định hoặc độ ổn định đã quan sát;

- phạm vi hiệu lực đã được kiểm chứng.

Danh mục này là hàm ý phương pháp rút ra từ các nghiên cứu đã tổng quan và từ thiết kế nghiên cứu. Cấu trúc thực thể và quan hệ đầy đủ của bản ghi được trình bày ở Mục 5.6.2 và Phụ lục A.

### 3.5.2. Phạm vi hiệu lực

Phạm vi hiệu lực mô tả nơi một bằng chứng đã được kiểm chứng là có giá trị: một kết quả có thể chỉ được xác lập trong cùng đợt thí nghiệm, hoặc có thể giữ được khi chuyển sang đợt khác. Phạm vi này không thể suy đoán từ một chỉ số hiệu năng tổng hợp mà phải gắn với giao thức đánh giá đã sử dụng.

Cách tiếp cận này thay đổi cách đọc cả kết quả dương lẫn kết quả âm. Kết quả tốt trong cùng đợt là bằng chứng có giá trị trong phạm vi đó; dùng ở hiện trường cần kiểm chứng riêng. Kết quả chuyển giao giữa các đợt cho biết phạm vi hiệu lực của bằng chứng, và kết quả trong cùng đợt vẫn được giữ trong phạm vi của nó. Ở công trình thực, phạm vi hiệu lực còn phụ thuộc điều kiện vận hành, môi trường và lịch sử can thiệp. Dữ liệu hiện trường vì vậy cần kèm bối cảnh về thời điểm thu, trạng thái vận hành, điều kiện môi trường và các thay đổi bảo trì liên quan.

### 3.5.3. Nguồn gốc dữ liệu và khả năng kiểm lại

Nguồn gốc dữ liệu (provenance) mô tả nguồn phát sinh, quá trình biến đổi và tác nhân liên quan tới một bản ghi. Đối với bằng chứng trạng thái, nguồn gốc trả lời các câu hỏi cụ thể: dữ liệu đến từ cảm biến nào, lần chạy nào, phiên bản nào, được xử lý bằng chuỗi nào và kết quả được tạo dưới giao thức đánh giá nào.

Yêu cầu này nối trực tiếp với quản lý tài sản. Khi bằng chứng hỗ trợ một yêu cầu kiểm tra, người quản lý cần truy ngược được từ hành động về nguồn kỹ thuật đã tạo ra nó. Nếu bằng chứng mất thông tin về phạm vi hiệu lực hoặc nguồn gốc khi chuyển sang BIM hay hồ sơ kiểm tra, giá trị quản lý của nó giảm mạnh. Hàm ý chính của Chương 3 vì vậy là bằng chứng trạng thái phải được quản lý như một đối tượng thông tin có nguồn gốc và phạm vi hiệu lực.

## 3.6. Tổng hợp chương

Dữ liệu dao động cùng các mô hình học máy và học sâu đã được sử dụng rộng để phân biệt trạng thái kết cấu và trạng thái liên kết bu lông trong điều kiện thí nghiệm.

Ở công trình công nghiệp, quan trắc hiện tại gặp bốn giới hạn (mục 3.2). Kiểm tra trực quan phụ thuộc người kiểm tra, quan trắc dày đặc khó có cơ sở kinh tế, biến đổi vận hành và môi trường có thể che lấp thay đổi do hư hỏng, và bộ phân loại học ở phòng thí nghiệm khó chuyển nguyên sang hiện trường. Phần chuyển được từ phòng thí nghiệm sang hiện trường là nguyên tắc tổ chức bằng chứng và giao thức đánh giá.

Trọng tâm nằm ở chất lượng của giao thức đánh giá, do bốn đặc điểm của dữ liệu dao động quy định. Đó là cấu trúc dữ liệu phân cấp; cửa sổ tín hiệu thuộc về đơn vị vật lý tạo ra nó; tiền xử lý có thể gây rò rỉ nếu làm trước khi chia; khả năng khái quát phụ thuộc vào cấp vật lý được giữ lại. Các tiền lệ ở mục 3.4 đủ để xây dựng một giao thức đánh giá chặt chẽ trên nền bốn đặc điểm đó.

Từ góc nhìn của luận án, một kết quả phân loại chỉ trở thành bằng chứng trạng thái khi được gắn với nguồn thu, cấu hình cảm biến, phiên bản chuỗi xử lý, giao thức đánh giá, độ bất định và phạm vi hiệu lực. Phạm vi diễn giải của bằng chứng được trình bày ở Mục 5.9.

Chương 3 vì vậy đặt nền phương pháp cho Câu hỏi nghiên cứu 1 và Gói công việc 1: điều kiện để dữ liệu dao động tạo ra bằng chứng kiểm lại được và có phạm vi diễn giải rõ.

Đến đây, bằng chứng trạng thái đã được mô tả đầy đủ về mặt kỹ thuật nhưng chưa dùng được cho quản lý. Bằng chứng còn phải gắn đúng cấu kiện, giữ các thuộc tính vừa nêu khi đi qua nhiều hệ thống, và cho phép truy ngược từ hồ sơ hay hành động về đúng căn cứ đã sinh ra chúng. Chương 4 xét những điều kiện đó.
