# CHƯƠNG 3. TỔNG QUAN VỀ DỮ LIỆU DAO ĐỘNG VÀ BẰNG CHỨNG TRẠNG THÁI

## 3.1. Dữ liệu dao động trong theo dõi trạng thái kết cấu

### 3.1.1. Theo dõi trạng thái kết cấu dựa trên dao động

Theo dõi trạng thái kết cấu dựa trên dao động (vibration-based structural health monitoring) dựa trên nguyên lý: thay đổi đặc trưng động lực học có thể phản ánh thay đổi trạng thái vật lý của kết cấu. Hướng này đã phát triển từ các phương pháp dựa trên đặc trưng động lực truyền thống tới học máy và học sâu; các tổng quan gần đây cho thấy khó khăn nằm ở cả việc chọn mô hình, cách kiểm chứng kết quả lẫn khả năng chuyển từ điều kiện kiểm soát ra thực tế \[13\].

Biến thiên môi trường và vận hành là yếu tố chi phối mạnh nhất. Sohn (2007) chỉ ra rằng biến đổi do nhiệt độ, tải trọng vận hành hoặc điều kiện sử dụng có thể có biên độ tương đương hoặc lớn hơn thay đổi do trạng thái kết cấu \[45\]; Keshmiry và cộng sự (2023) xác nhận vai trò của điều kiện môi trường và vận hành trong theo dõi trạng thái kết cấu và kiểm tra không phá hủy \[46\]. Hệ quả phương pháp là kết quả phân loại chỉ có ý nghĩa khi đi kèm bối cảnh tạo ra nó: điều kiện thu nhận, cấu hình cảm biến, trạng thái lắp đặt, đợt đo và điều kiện môi trường là một phần của ngữ cảnh diễn giải bằng chứng.

### 3.1.2. Theo dõi trạng thái liên kết bu lông trong khung thép

Liên kết bu lông đã được theo dõi bằng nhiều phương pháp, trong đó có dữ liệu dao động và học máy. Trên khung thép, trạng thái liên kết có thể được phân biệt trong phòng thí nghiệm bằng dữ liệu cảm biến và nhiều mô hình phân loại \[47\]–\[50\]. Dùng học máy hay học sâu để phân loại trạng thái liên kết bu lông vì vậy không mới; giá trị của một nghiên cứu mới nằm ở cách tổ chức thí nghiệm, định nghĩa đơn vị độc lập, cách chia dữ liệu, kiểm soát rò rỉ và phạm vi mà kết quả được kiểm chứng.

Bảng 3.1 đối chiếu một số nghiên cứu đại diện theo ba tiêu chí thường quyết định mức tin cậy của kết quả: đối tượng vật lý, cách chia dữ liệu và cấu hình cảm biến.

<span id="TLTQ_Bang_3_1" class="anchor"></span>Bảng 3.1. Một số nghiên cứu đại diện về đơn vị vật lý và cách đánh giá dữ liệu

| **Nghiên cứu** | **Đối tượng** | **Đơn vị vật lý** | **Cách chia dữ liệu** | **Cấu hình cảm biến** | **Hàm ý phương pháp** |
|:---|:---|:---|:---|:---|:---|
| Zhang và cộng sự (2020) \[47\] | Khung thép, liên kết bu lông | Bản ghi từ gia tốc kế | Không mô tả rõ phép chia theo đơn vị vật lý | Một cảm biến | Cho thấy tiền lệ về đối tượng nghiên cứu |
| Pal và cộng sự (2022) \[48\] | Khung thép phẳng một tầng, liên kết dầm – cột | Lần kích thích vật lý | Chia theo lần thử | Sáu cảm biến biến dạng | Cho thấy tầm quan trọng của mô tả rõ cấu trúc chia dữ liệu |
| Biswal và cộng sự (2022) \[49\] | Khung thép cổng một nhịp | Lần kích thích vật lý | Không xây dựng quy trình huấn luyện – kiểm tra hoàn chỉnh | Sáu gia tốc kế | Tiền lệ về trạng thái liên kết, không phải giao thức đánh giá |
| Parziale và cộng sự (2024) \[50\] | Khung thép quy mô lớn | Lần thu tín hiệu | Tạo cửa sổ trước rồi chia ngẫu nhiên các ảnh đầu vào | Cấu hình cảm biến cố định | Minh họa rủi ro khi cửa sổ từ cùng nguồn vật lý xuất hiện ở hai phía phép chia |
| Dadoulis và Manolis (2026) \[51\] | Dầm thép chịu khối lượng di động | Một lượt chuyển động | Huấn luyện trên mô phỏng, kiểm tra trên dữ liệu thí nghiệm | Ba nút gia tốc | Cho thấy cách đánh giá đóng góp cảm biến |
| Beleites và cộng sự (2013) \[14\] | Dữ liệu quang phổ ngoài lĩnh vực xây dựng | Người hiến/mẻ nuôi cấy | So sánh chia theo quan sát với chia theo nhóm nguồn | Không áp dụng | Cung cấp nguyên tắc về đơn vị độc lập |
| Wheat và cộng sự (2024) \[15\] | Bệ thử ổ lăn | Lần chạy, ngày đo, chi tiết vật lý | Giữ lại theo nhiều cấp nguồn vật lý | Hai vị trí gia tốc | Cho thấy cấp chia dữ liệu ảnh hưởng mạnh tới hiệu năng |

Bảng này cho thấy một bất đối xứng lặp lại: các nghiên cứu trên khung thép thường có số lần thử vật lý nhỏ hơn rất nhiều so với số cửa sổ tín hiệu tạo ra từ các lần thử đó. Số cửa sổ vì vậy không thể hiểu là cỡ mẫu độc lập. Đây là điểm nối giữa thí nghiệm dao động và thiết kế đánh giá thống kê, nơi phát sinh phần lớn các rủi ro phân tích ở mục 3.3.

### 3.1.3. Phân biệt bằng chứng trạng thái và chẩn đoán hư hỏng

Trong nghiên cứu này, đầu ra của một mô hình phân loại trên dữ liệu dao động được gọi là **bằng chứng trạng thái** (condition evidence). Bằng chứng này có thể gồm nhãn trạng thái, xác suất hoặc mức độ tin cậy, cùng bối cảnh đã tạo ra kết quả. Nó không được xem là kết luận trực tiếp về hư hỏng vật lý, mức độ nghiêm trọng hoặc chỉ số sức khỏe của cấu kiện.

Sự phân biệt này cần thiết vì nhãn và trạng thái vật lý không tương ứng một–một theo cả hai chiều. Theo chiều thứ nhất, nhãn phân loại phụ thuộc vào nhiều yếu tố ngoài trạng thái vật lý (cấu hình cảm biến, đợt thí nghiệm, điều kiện lắp đặt, đường cơ sở tham chiếu, phiên bản dữ liệu và chuỗi xử lý), nên thay đổi một yếu tố có thể làm đổi kết quả mà không có thay đổi vật lý tương ứng. Theo chiều ngược lại, dữ liệu dao động không đủ để xác định nguyên nhân của một thay đổi vật lý thực; tín hiệu còn chịu ảnh hưởng của điều kiện môi trường, vận hành, lắp đặt và lịch sử can thiệp. Dữ liệu dao động vì vậy cung cấp dấu hiệu thay đổi trạng thái; nguyên nhân phải được xác nhận bằng hoạt động kiểm tra phù hợp.

Từ đó, ba nguyên tắc được giữ nhất quán cho luận án:

> 1\. kết quả phòng thí nghiệm chỉ chứng minh khả năng phân biệt các trạng thái có kiểm soát trong phạm vi đã thí nghiệm;
>
> 2\. bất thường trong bằng chứng dao động dẫn tới yêu cầu kiểm tra, không dẫn trực tiếp tới kết luận hư hỏng;
>
> 3\. mô hình phân loại phòng thí nghiệm không được chuyển trực tiếp sang công trình thực để chẩn đoán khi chưa có bằng chứng xác nhận.

## 3.2. Cảm biến và chuỗi xử lý dữ liệu

### 3.2.1. Loại, số lượng và cấu hình cảm biến

Các nghiên cứu dùng nhiều loại và số lượng cảm biến, phổ biến nhất là gia tốc kế và cảm biến biến dạng, từ vài vị trí tới mạng đo nhiều điểm. Phần lớn dùng một cấu hình cố định và tập trung vào mô hình phân loại, ít đánh giá có kiểm soát ảnh hưởng của chính cấu hình đó.

Cấu hình cảm biến là một phần của điều kiện tạo bằng chứng: kết quả đạt được với một tổ hợp cảm biến không mặc nhiên giữ nguyên khi số lượng hay vị trí thay đổi. Wheat và cộng sự (2024) cho thấy vị trí cảm biến ảnh hưởng tới hiệu năng ngay trong một giao thức đánh giá giữ nguyên \[15\]; Dadoulis và Manolis (2026) định lượng đóng góp của từng kênh đo \[51\]. Trong luận án, cấu hình cảm biến giữ vai trò hỗ trợ cho Câu hỏi nghiên cứu 1 (đánh giá chất lượng bằng chứng dưới các cấu hình khác nhau); chương này không tìm “vị trí tối ưu” và không coi cấu hình cảm biến là trục nghiên cứu độc lập.

### 3.2.2. Tiền xử lý, phân đoạn và tạo đầu vào

Chuỗi xử lý dữ liệu dao động thường gồm cắt đoạn tín hiệu, lọc, chuẩn hóa, biến đổi miền tần số hoặc thời gian – tần số, rút đặc trưng hoặc tạo đầu vào trực tiếp cho mô hình học sâu. Hai khâu đặc biệt nhạy với kết quả đánh giá.

Khâu thứ nhất là phân đoạn tín hiệu. Khi một bản ghi được chia thành nhiều cửa sổ, các cửa sổ đó không phải quan sát độc lập nếu cùng xuất phát từ một lần thu vật lý; với cửa sổ chồng lấn, mức phụ thuộc còn lớn hơn vì chúng chia sẻ trực tiếp nhiều mẫu tín hiệu. Cửa sổ vì vậy là đơn vị tính toán, không mặc nhiên là đơn vị suy luận thống kê.

Khâu thứ hai là thứ tự giữa phép chia tập và các phép biến đổi có tham số học được. Nếu trung bình, độ lệch chuẩn, phép giảm chiều hoặc các tham số khác được ước lượng trên toàn bộ dữ liệu trước khi chia, thông tin của tập kiểm tra đã đi vào quá trình xây dựng mô hình. Amin và cộng sự (2026) cung cấp tiền lệ cho cách làm ngược lại: chia theo sự kiện vật lý trước, sau đó chỉ học các phép biến đổi từ phần huấn luyện \[52\]. Nguyên tắc rút ra: **chia dữ liệu theo đơn vị vật lý trước khi thực hiện các phép biến đổi có thể học từ dữ liệu**, và ước lượng mọi tham số tiền xử lý chỉ từ tập huấn luyện trong từng lượt đánh giá.

### 3.2.3. Học máy và học sâu như công cụ tạo bằng chứng

Các mô hình được sử dụng trong theo dõi trạng thái dao động trải rộng từ hồi quy logistic, máy véc-tơ hỗ trợ, rừng ngẫu nhiên tới mạng nơ-ron tích chập và nhiều kiến trúc học sâu khác. Trong nghiên cứu này, chúng được xem là **công cụ tạo bằng chứng**, không phải mục tiêu đóng góp thuật toán.

Hiệu năng của mô hình chỉ có ý nghĩa khi giao thức đánh giá đủ chặt. Wheat và cộng sự (2024) cho thấy chỉ cần đổi cấp phân tách dữ liệu là hiệu năng đo được trên cùng một bài toán rung động đã thay đổi mạnh; so sánh kiến trúc mô hình dưới một giao thức chưa kiểm soát đơn vị độc lập hoặc rò rỉ dữ liệu có thể cho kết luận không ổn định \[15\]. Câu hỏi phù hợp là “bằng chứng do mô hình tạo ra đáng tin trong phạm vi nào?”, chứ không phải “mô hình nào đạt điểm cao nhất?”. Trọng tâm vì thế dịch từ tối ưu thuật toán sang thiết kế thí nghiệm, giao thức đánh giá và phạm vi diễn giải.

## 3.3. Độ tin cậy của bằng chứng trạng thái

### 3.3.1. Đơn vị vật lý độc lập và lặp giả

Vấn đề đầu tiên của dữ liệu dao động là xác định đâu là **đơn vị vật lý độc lập**. Nhiều cửa sổ tạo ra từ cùng một bản ghi không làm tăng số lần thí nghiệm độc lập; nếu coi chúng như các quan sát hoàn toàn độc lập, cỡ mẫu biểu kiến có thể lớn hơn rất nhiều so với cỡ mẫu vật lý thực. Beleites và cộng sự (2013), trong một lĩnh vực khác (hóa phân tích, dữ liệu quang phổ), minh họa hiện tượng **lặp giả** (pseudoreplication): hàng nghìn quan sát ở cấp thấp không thay thế được số lượng hữu hạn các nguồn vật lý độc lập ở cấp cao. Nguyên tắc chuyển giao được sang dữ liệu dao động là cấp dùng cho suy luận phải phản ánh nguồn độc lập thực sinh ra dữ liệu \[14\].

Trong thí nghiệm dao động, cấu trúc dữ liệu thường có dạng phân cấp:

**Đợt thí nghiệm → lần lắp đặt / trạng thái lắp ráp → lần chạy hoặc lần thu → cửa sổ tín hiệu**

Cửa sổ tín hiệu nằm ở cấp thấp nhất và không phải đơn vị độc lập. Lần chạy hoặc lần thu thường là cấp vật lý phù hợp hơn cho đánh giá trong cùng một đợt; khi mục tiêu là kiểm tra khả năng chuyển giao qua lắp đặt hoặc qua đợt đo, cấp độc lập phải được nâng lên tương ứng. Chọn đúng đơn vị độc lập vì vậy quyết định trực tiếp phạm vi diễn giải của kết quả, ngoài ý nghĩa thống kê.

### 3.3.2. Rò rỉ dữ liệu và đánh giá theo nhóm

**Rò rỉ dữ liệu** (data leakage) xảy ra khi thông tin từ phần kiểm tra ảnh hưởng tới quá trình huấn luyện, khiến hiệu năng đo được cao hơn khả năng thực trên dữ liệu mới. Với dữ liệu dao động có cấu trúc phân cấp, rò rỉ xuất hiện qua ba đường tương ứng với ba cấp của cấu trúc đó.

Đường thứ nhất nằm ở cấp cửa sổ: tạo cửa sổ trước rồi chia ngẫu nhiên. Khi các cửa sổ từ cùng một bản ghi nằm ở cả tập huấn luyện và kiểm tra, mô hình có thể học đặc điểm riêng của bản ghi thay vì đặc điểm chung của trạng thái. Đường thứ hai nằm ở cấp chuỗi xử lý: tiền xử lý trên toàn bộ dữ liệu trước khi chia; cách kiểm soát là học mọi tham số tiền xử lý chỉ trên phần huấn luyện. Đường thứ ba, khó nhận ra nhất, nằm ở cấp cao hơn cấp đang được chia \[53\]. Wheat và cộng sự (2024) cho thấy ngay cả khi đã tách theo lần chạy, dữ liệu vẫn có thể chia sẻ cùng ngày đo hoặc cùng chi tiết vật lý \[15\]; Vieira và cộng sự (2026) cho thấy chỉ cần dùng cùng một chi tiết vật lý ở hai phía phép chia là hiệu năng đo được đã trở nên lạc quan \[20\].

Biện pháp tổng quát là **đánh giá theo nhóm** (grouped evaluation): toàn bộ dữ liệu phát sinh từ cùng một nguồn vật lý phải nằm trọn ở một phía của phép chia. Cấp nhóm được chọn theo câu hỏi nghiên cứu, không theo mức chặt chẽ hình thức: nếu câu hỏi chỉ yêu cầu khái quát sang lần chạy mới trong cùng đợt, nhóm ở cấp lần chạy là phù hợp; nếu câu hỏi yêu cầu chuyển sang đợt thí nghiệm mới, phải giữ lại toàn bộ đợt \[54\].

Rò rỉ dữ liệu đã được nhận diện rộng trong học máy nói chung và trong bảo trì theo tình trạng \[55\]. Kiểm soát rò rỉ vì vậy là điều kiện để kết quả có giá trị, không phải đóng góp mới.

### 3.3.3. Đánh giá giữ lại một lần chạy và giữ lại một đợt thí nghiệm

Luận án sử dụng hai giao thức đánh giá theo nhóm để trả lời hai câu hỏi khác nhau. **Đánh giá giữ lại một lần chạy** (Leave-One-Run-Out – LORO) giữ toàn bộ dữ liệu của một lần chạy làm tập kiểm tra và huấn luyện trên các lần chạy còn lại, qua đó đánh giá khả năng khái quát sang một lần chạy độc lập trong phạm vi cùng một đợt thí nghiệm. **Đánh giá giữ lại một đợt thí nghiệm** (Leave-One-Campaign-Out – LOCO) giữ toàn bộ dữ liệu của một đợt làm tập kiểm tra, và khắt khe hơn vì đợt mới có thể đi kèm tháo – lắp lại cảm biến, thay đổi trạng thái tiếp xúc, điều kiện môi trường cùng các yếu tố vận hành khác.

Mức khắt khe của LOCO có cơ sở vật lý. Brake, Schwingshackl và Reuß (2019) cho thấy quá trình lắp ráp và trạng thái tiếp xúc tạo biến thiên lớn trong kết cấu có liên kết \[18\]; Ramasso, de Oliveira Teloli và Marcel (2024) ghi nhận hiệu năng trong cùng đợt và trên đợt chưa thấy có thể chênh lệch rõ khi liên kết được tháo – lắp lại \[19\]; Da Silva và cộng sự (2024) minh họa khó khăn khi chuyển mô hình giữa các mẫu liên kết danh nghĩa tương tự nhau \[56\].

Hai giao thức trả lời hai câu hỏi tách biệt: LORO cho biết bằng chứng có khái quát sang một lần chạy mới trong cùng bối cảnh thí nghiệm hay không; LOCO cho biết bằng chứng có giữ giá trị khi chuyển sang đợt thí nghiệm khác hay không. Một kết quả LORO tốt không cho phép suy rộng sang đợt mới, càng không sang công trình thực. Một kết quả LOCO thấp không xóa giá trị của bằng chứng trong cùng đợt mà chỉ cho thấy phạm vi hiệu lực hẹp hơn. Cách đọc này quan trọng khi bằng chứng đi sang lớp quản lý thông tin, nơi người dùng thường không tiếp cận được giao thức đánh giá gốc.

Ở mức tổng quát hơn, dòng nghiên cứu theo dõi trạng thái theo quần thể đặt câu hỏi khi nào tri thức được phép chuyển giữa các kết cấu. Với nhóm kết cấu gần như đồng nhất, một dạng chung được xây cho cả nhóm và dùng cho thành viên thiếu dữ liệu \[57\]; với nhóm kết cấu dị thể, mỗi kết cấu được quy về đồ thị thuộc tính và mức tương đồng phải được đo trước khi bàn tới chuyển giao \[58\]. Khung này đặt ra điều kiện cho bước từ mô hình thu nhỏ sang công trình thực: phát biểu rõ mức tương đồng giữa hai kết cấu trước khi nói kết quả trên mô hình có ý nghĩa gì cho công trình. Luận án không chuyển bộ phân loại giữa hai đối tượng. Phần được chuyển là nguyên tắc tổ chức và truy vết bằng chứng, còn mức tương đồng vật lý được ghi nhận như một giới hạn của kết quả.

### 3.3.4. Các cơ chế đánh giá bổ trợ

Ngoài LORO và LOCO, bốn cơ chế bổ trợ giúp mô tả độ ổn định của bằng chứng. Lặp lại với nhiều hạt giống ngẫu nhiên tách được biến thiên do khởi tạo hoặc huấn luyện mô hình khỏi biến thiên do dữ liệu. Báo cáo độ bất định ở cấp đơn vị độc lập cho biết kết quả trung bình có ổn định qua các lần chạy hoặc các nhóm vật lý hay không. Kiểm định hoán vị tạo phân phối ngẫu nhiên thực nghiệm để đánh giá liệu hiệu năng quan sát được có vượt mức có thể xuất hiện do may rủi hay không \[59\], với lưu ý rằng trên dữ liệu có cấu trúc nhóm, phép hoán vị phải bảo toàn cấu trúc đơn vị độc lập. Cuối cùng, mức ngẫu nhiên thực nghiệm trở nên đặc biệt cần thiết khi số đơn vị kiểm tra nhỏ, vì mức ngẫu nhiên lý thuyết có thể không đủ để diễn giải hiệu năng trong các tập mẫu nhỏ \[60\].

Các thủ tục này là công cụ kiểm chứng, không phải khoảng trống nghiên cứu riêng; chúng giúp báo cáo bằng chứng kèm mức ổn định và mức chắc chắn phù hợp.

## 3.4. Nguồn gốc và phạm vi hiệu lực của bằng chứng trạng thái

### 3.4.1. Bằng chứng trạng thái như một bản ghi có bối cảnh

Nếu giá trị của một nhãn phụ thuộc vào nguồn thu, cấu hình cảm biến, phiên bản dữ liệu, chuỗi xử lý và giao thức đánh giá, thì nhãn đó không nên tồn tại như một con số tách rời. Nó cần được tổ chức thành một bản ghi mang đủ bối cảnh để người sử dụng hiểu được bằng chứng đã được tạo ra như thế nào và được phép dùng trong phạm vi nào.

Cần phân biệt hai mức độ tin cậy thường bị gộp làm một. Mức thứ nhất là độ tin cậy của một dự đoán riêng lẻ, thường là xác suất hậu nghiệm hoặc điểm số do mô hình sinh ra cho một mẫu; đại lượng này phụ thuộc vào cách hiệu chỉnh của mô hình và có thể cao ngay cả khi mô hình sai. Mức thứ hai là hiệu năng, độ bất định và phạm vi hiệu lực đã được kiểm chứng của chính mô hình sinh ra dự đoán đó, tức là kết quả đo được dưới một giao thức đánh giá xác định, trên các đơn vị vật lý độc lập và trong một phạm vi đã nêu rõ. Bản ghi Condition_Evidence_ID phải lưu cả hai mức và ghi rõ mức nào đang được dùng khi diễn giải: điểm tin cậy của một dự đoán không được đọc như mức tin cậy của bằng chứng, và mức tin cậy của bằng chứng chỉ có nghĩa trong phạm vi hiệu lực đã ghi.

Ở mức tối thiểu, một bản ghi bằng chứng trạng thái cần gắn với:

- nguồn thu dữ liệu, gồm đợt thí nghiệm và lần chạy;

- cấu hình cảm biến;

- phiên bản dữ liệu và chuỗi xử lý;

- giao thức đánh giá;

- độ bất định hoặc độ ổn định đã quan sát;

- phạm vi hiệu lực đã được kiểm chứng.

Danh mục này là hàm ý phương pháp rút ra từ các nghiên cứu đã tổng quan và từ thiết kế nghiên cứu, chưa phải lược đồ dữ liệu hoàn chỉnh; cấu trúc thực thể và quan hệ của bản ghi thuộc phần truy vết thông tin.

### 3.4.2. Phạm vi hiệu lực

**Phạm vi hiệu lực** mô tả nơi một bằng chứng đã được kiểm chứng là có giá trị: một kết quả có thể chỉ được xác lập trong cùng đợt thí nghiệm, hoặc có thể giữ được khi chuyển sang đợt khác. Phạm vi này không thể suy đoán từ một chỉ số hiệu năng tổng hợp mà phải gắn với giao thức đánh giá đã sử dụng.

Cách tiếp cận này thay đổi cách đọc cả kết quả dương lẫn kết quả âm. Kết quả tốt trong cùng đợt là bằng chứng có giá trị trong phạm vi đó, không mặc nhiên có giá trị ở hiện trường; kết quả chuyển giao kém giữa các đợt là thông tin về giới hạn của bằng chứng, không phải lý do loại bỏ kết quả trong cùng đợt. Ở công trình thực, phạm vi hiệu lực còn phụ thuộc điều kiện vận hành, môi trường và lịch sử can thiệp, nên dữ liệu hiện trường cần kèm bối cảnh về thời điểm thu, trạng thái vận hành, điều kiện môi trường và các thay đổi bảo trì liên quan.

### 3.4.3. Nguồn gốc dữ liệu và khả năng kiểm lại

**Nguồn gốc dữ liệu** (provenance) mô tả nguồn phát sinh, quá trình biến đổi và tác nhân liên quan tới một bản ghi. Đối với bằng chứng trạng thái, nguồn gốc trả lời các câu hỏi cụ thể: dữ liệu đến từ cảm biến nào, lần chạy nào, phiên bản nào, được xử lý bằng chuỗi nào và kết quả được tạo dưới giao thức đánh giá nào.

Yêu cầu này nối trực tiếp với quản lý tài sản. Khi bằng chứng hỗ trợ một yêu cầu kiểm tra, người quản lý cần truy ngược được từ hành động về nguồn kỹ thuật đã tạo ra nó; nếu bằng chứng mất thông tin về phạm vi hiệu lực hoặc nguồn gốc khi chuyển sang BIM hay hồ sơ kiểm tra, giá trị quản lý của nó giảm mạnh. Hàm ý chính của Chương 3 vì vậy là: **bằng chứng trạng thái phải được quản lý như một đối tượng thông tin có nguồn gốc và phạm vi hiệu lực**.

## 3.5. Tổng hợp chương

Dữ liệu dao động cùng các mô hình học máy và học sâu đã được sử dụng rộng để phân biệt trạng thái kết cấu và trạng thái liên kết bu lông trong điều kiện thí nghiệm. Việc áp dụng thêm một thuật toán phân loại mới vì vậy không phải trọng tâm khoa học của nghiên cứu này.

Trọng tâm nằm ở chất lượng của giao thức đánh giá, do bốn đặc điểm của dữ liệu dao động quy định: cấu trúc dữ liệu phân cấp; cửa sổ tín hiệu không phải đơn vị độc lập; tiền xử lý có thể gây rò rỉ nếu làm trước khi chia; khả năng khái quát phụ thuộc vào cấp vật lý được giữ lại. Các tiền lệ ở mục 3.3 đủ để xây dựng một giao thức đánh giá chặt chẽ trên nền bốn đặc điểm đó.

Từ góc nhìn của luận án, một kết quả phân loại chỉ trở thành **bằng chứng trạng thái** khi được gắn với nguồn thu, cấu hình cảm biến, phiên bản chuỗi xử lý, giao thức đánh giá, độ bất định và phạm vi hiệu lực. Bằng chứng đó không phải chẩn đoán hư hỏng và không tự động chuyển giao từ mô hình 1:10 sang công trình thực.

Chương 3 vì vậy đặt nền phương pháp cho Câu hỏi nghiên cứu 1 và Gói công việc 1: điều kiện để dữ liệu dao động tạo ra bằng chứng kiểm lại được và có phạm vi diễn giải rõ.

Đến đây, bằng chứng trạng thái đã được mô tả đầy đủ về mặt kỹ thuật nhưng chưa dùng được cho quản lý: nó còn phải gắn đúng cấu kiện, giữ các thuộc tính vừa nêu khi đi qua nhiều hệ thống, và cho phép truy ngược từ hồ sơ hay hành động về đúng căn cứ đã sinh ra chúng. Chương 4 xét những điều kiện đó.
