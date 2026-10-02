# CHƯƠNG 4. TỔNG QUAN VỀ TRUY VẾT BẰNG CHỨNG VÀ HỖ TRỢ KIỂM TRA – BẢO TRÌ

## 4.1. Ranh giới khái niệm của truy vết trong quản lý tài sản

### 4.1.1. Từ hiển thị dữ liệu đến truy vết bằng chứng

Chương 2 cho thấy BIM và IFC cung cấp nền định danh và ngữ cảnh tài sản nhưng không tự tạo ra chuỗi thông tin vận hành. Chương 3 cho thấy một kết quả phân loại từ dữ liệu dao động chỉ là bằng chứng trạng thái khi đi kèm nguồn gốc, điều kiện tạo lập và phạm vi hiệu lực đã kiểm chứng. Từ hai tiền đề đó, Chương 4 xét câu hỏi ở lớp thông tin: bằng chứng kỹ thuật được liên kết với cấu kiện, hồ sơ kiểm tra và trạng thái hành động theo cách nào để người quản lý truy xuất và kiểm lại được căn cứ của một quyết định.

Trong các nghiên cứu, liên kết, tích hợp, trực quan hóa và truy vết đôi khi được dùng gần nhau nhưng ứng với các mức năng lực khác nhau. Để tránh phóng đại ý nghĩa của các triển khai đã có, chương này phân biệt bốn mức (Bảng 4.1).

<span id="TLTQ_Bang_4_1" class="anchor"></span>Bảng 4.1. Phân biệt các mức liên kết thông tin trong quản lý tài sản

| **Mức** | **Nội dung** | **Điều chưa được chứng minh chỉ từ mức này** |
|:---|:---|:---|
| Tích hợp cảm biến – BIM | Dữ liệu hoặc siêu dữ liệu cảm biến được liên kết với đối tượng trong mô hình | Hồ sơ kiểm tra, lịch sử hành động hoặc khả năng kiểm lại nguồn của một quyết định |
| Trực quan hóa trên BIM | Giá trị, cảnh báo hoặc trạng thái được hiển thị trên mô hình | Tính toàn vẹn của quan hệ dữ liệu bên dưới |
| Liên kết hồ sơ – cấu kiện | Hồ sơ kiểm tra, khiếm khuyết hoặc sửa chữa được gắn với cấu kiện | Khả năng truy ngược toàn bộ chuỗi về bằng chứng ban đầu |
| Truy vết bằng chứng – hành động | Bằng chứng, cấu kiện, hồ sơ và trạng thái hành động được nối bằng các quan hệ có thể kiểm tra | Độ chính xác kỹ thuật của bằng chứng đầu vào |

Cột thứ ba của bảng là phần có ý nghĩa nhất đối với quản lý tài sản, vì nó chỉ ra điều mà mỗi mức *không* chứng minh. Một cảnh báo xuất hiện đúng vị trí trên mô hình chưa cho biết cảnh báo đó được tạo từ dữ liệu nào, bằng quy trình nào hoặc đã dẫn tới hồ sơ kiểm tra nào; một hồ sơ được gắn với cấu kiện chưa tự động cho biết hành động sau đó đã được ai rà soát, có hoàn thành hay không và căn cứ của nó là gì.

Trong chương này, **truy vết** là khả năng duy trì và truy xuất quan hệ giữa các bản ghi qua thời gian và qua hệ thống, để người dùng đi được từ một bằng chứng tới đối tượng liên quan và từ một hồ sơ hay trạng thái hành động truy ngược về căn cứ ban đầu.

### 4.1.2. Cấu kiện, bằng chứng, hồ sơ và hành động là các thực thể khác nhau

Nguyên tắc đầu tiên là không đồng nhất các loại thông tin khác nhau thành thuộc tính của cùng một đối tượng. Cấu kiện là đối tượng vật lý hoặc đối tượng số đại diện cho tài sản; cảm biến là nguồn thu dữ liệu; bằng chứng trạng thái là kết quả của một quá trình xử lý và đánh giá dữ liệu; hồ sơ kiểm tra là bản ghi nghiệp vụ được tạo tại một thời điểm bởi một người hoặc đơn vị có trách nhiệm; hành động là một quá trình quản lý có trạng thái thay đổi theo thời gian.

Các thực thể này phải tách riêng để giữ lịch sử. Cảm biến có thể được tháo hoặc chuyển vị trí, nhưng bằng chứng tạo trước đó vẫn phải tồn tại và truy được tới cấu kiện tại thời điểm ghi; hồ sơ kiểm tra có thể được cập nhật hoặc đóng sau khi hành động hoàn thành mà không làm thay đổi cấu kiện. Nếu gộp bốn loại thông tin thành thuộc tính của cùng một đối tượng, mỗi thay đổi ở một loại sẽ ghi đè lịch sử của các loại còn lại. Các hệ thống quản lý tài sản dựa trên BIM cũng đi theo hướng này, tổ chức dữ liệu vận hành và hồ sơ bảo trì thành bản ghi có quan hệ với đối tượng mô hình \[6\], \[34\], \[36\].

## 4.2. Tích hợp cảm biến với BIM và IFC

### 4.2.1. Các cách liên kết cảm biến với cấu kiện

Liên kết dữ liệu cảm biến với BIM đã được thực hiện theo hai hướng chính và không còn là vấn đề mới.

Hướng thứ nhất là mở rộng chính lược đồ dữ liệu. Theiler và Smarsly (2018) mở rộng IFC để mô hình hóa nút cảm biến, mạng cảm biến và quan hệ của hệ theo dõi trạng thái với cấu kiện chịu lực, cho thấy cảm biến có thể được biểu diễn ở cấp lược đồ thay vì chỉ được đặt như ký hiệu trên giao diện \[2\]. Hướng thứ hai là duy trì một lớp ánh xạ giữa hệ cảm biến và mô hình, với các biến thể khác nhau về kỹ thuật nền: cấu trúc dữ liệu liên kết để nối trạng thái hệ tự động hóa tòa nhà với ngữ cảnh BIM \[26\], ánh xạ giữa các hệ định danh để tích hợp BIM với dữ liệu thiết bị \[4\], hoặc dùng *GlobalId* của IFC làm khóa nối tới cơ sở dữ liệu chuỗi thời gian \[5\].

Cả hai hướng cho thấy dữ liệu thời gian thực hoặc dữ liệu lịch sử truy xuất được theo ngữ cảnh cấu kiện nếu có cơ chế định danh và ánh xạ phù hợp. Đây là điều kiện cần cho hệ thống quản lý tài sản dựa trên dữ liệu, nhưng chưa phải điều kiện đủ (mục 4.2.2).

Ở lớp biểu diễn quan trắc, W3C và OGC đã chuẩn hóa từ vựng SOSA và SSN cho cảm biến, quy trình đo, quan trắc và kết quả \[61\], \[62\]. Một quan trắc trong từ vựng này mang sẵn sensor tạo ra nó, thuộc tính được quan trắc, quy trình áp dụng, thời điểm đo và thời điểm có kết quả. Tài liệu đã rà soát cho thấy các nghiên cứu liên kết cảm biến với mô hình công trình thường mở rộng lược đồ IFC hoặc dựng cấu trúc riêng, ít khi neo vào từ vựng quan trắc chuẩn. SSN còn có khái niệm triển khai (`ssn:Deployment`): một hay nhiều hệ được triển khai cho một mục đích, có thể trên một nền tảng, ví dụ cảm biến nhiệt gắn trên tường; phần quy định của khái niệm này chưa có thuộc tính thời gian, và các ví dụ không quy định ghi thời điểm triển khai bằng cách ghép với PROV-O hoặc OWL-Time \[@GHAZGWUN\]. Cùng với việc gán cảm biến cho cấu kiện trong IFC của \[2\], đây là tiền lệ trực tiếp cho ánh xạ cảm biến – cấu kiện. Luận án dùng các khái niệm này để đối chiếu, trình bày bằng một bảng ánh xạ (Phụ lục A, Bảng A.3), và bổ sung khoảng hiệu lực bắt buộc của ánh xạ, ràng buộc thời điểm đo nằm trong khoảng đó (ràng buộc C3), cùng các thuộc tính về giao thức đánh giá và phạm vi hiệu lực của bằng chứng.

### 4.2.2. Liên kết cảm biến không đồng nghĩa với liên kết bằng chứng

Dù cảm biến có thể được gắn với cấu kiện, **quan hệ cảm biến – cấu kiện** và **quan hệ bằng chứng – cấu kiện** không phải một. Quan hệ thứ nhất mô tả nguồn đo cùng vị trí hoặc đối tượng mà cảm biến phục vụ, và có thể thay đổi khi cảm biến được tháo, thay thế hoặc tái bố trí. Quan hệ thứ hai gắn với một bản ghi được tạo tại một thời điểm từ một tập dữ liệu cụ thể; sau khi được tạo, bằng chứng phải giữ được liên hệ với nguồn dữ liệu và cấu kiện liên quan kể cả khi cấu hình cảm biến sau đó thay đổi.

Quan hệ Sensor_ID → BIM_GUID vì vậy chỉ biểu diễn ánh xạ giữa nguồn đo và cấu kiện liên quan. Quan hệ này cho biết nguồn đo phục vụ cấu kiện nào; một bất thường trong tín hiệu có thể đến từ cấu kiện lân cận, điều kiện môi trường hoặc thay đổi vận hành; cảm biến cũng có thể được di chuyển, thay thế hoặc hiệu chuẩn lại trong quá trình khai thác. Mô hình truy vết vì vậy phải phân biệt bốn nội dung: ánh xạ cảm biến với cấu kiện; bối cảnh của phép đo hoặc quan trắc; liên hệ giữa bằng chứng trạng thái với cấu kiện; và căn cứ cùng phạm vi hiệu lực của chính liên hệ đó. Mỗi ánh xạ còn phải có thời gian hiệu lực, phiên bản mô hình tương ứng và lịch sử thay đổi vị trí cảm biến, để một bằng chứng cũ không bị đọc theo một ánh xạ mới. Luận án không suy ra vị trí hư hỏng từ vị trí cảm biến và không dùng mô hình phần tử hữu hạn để chứng minh nguyên nhân hư hỏng.

Với dữ liệu dao động, một cấu kiện có thể có nhiều lần đo, nhiều cấu hình cảm biến và nhiều phiên bản xử lý. Nếu hệ thống chỉ lưu quan hệ “cảm biến này thuộc cấu kiện này”, người quản lý không biết một kết quả cụ thể được tạo từ lần đo nào hay bằng quy trình nào. Lớp quản lý bằng chứng vì vậy cần một bản ghi trung gian có định danh và nguồn gốc riêng.

### 4.2.3. Định danh và tính liên tục qua hệ thống

IFC cung cấp *GlobalId* như một nền định danh cho đối tượng mô hình. Khi các hệ thống bên ngoài dùng định danh này hoặc duy trì một ánh xạ ổn định tới nó, dữ liệu từ cảm biến, cơ sở dữ liệu hoặc hệ quản lý bảo trì có thể được kết nối với cùng một cấu kiện.

Nhưng tính duy nhất bên trong một mô hình không tự bảo đảm tính liên tục của định danh qua mọi phiên bản và mọi công cụ. Các nghiên cứu về so sánh mô hình, quản lý phiên bản và thay đổi đối tượng BIM cho thấy sự thay đổi mô hình có thể làm phát sinh vấn đề nhận dạng cùng một tài sản qua thời gian \[33\]. Yêu cầu thực hành rút ra là hệ thống vận hành phải quản lý quan hệ giữa các hệ định danh thay vì giả định một mã duy nhất luôn ổn định trong mọi hoàn cảnh; khi cần, một mã tài sản nghiệp vụ có thể tồn tại song song với *GlobalId* của mô hình IFC và định danh của cảm biến.

Các nghiên cứu này tạo một nền tương đối rõ: **BIM/IFC có thể làm neo ngữ cảnh cho dữ liệu cảm biến, nhưng tính liên tục của bằng chứng đòi hỏi thêm một lớp quản lý bản ghi và quan hệ theo thời gian**.

## 4.3. BIM trong quản lý hồ sơ kiểm tra và bảo trì

### 4.3.1. Từ biểu diễn khiếm khuyết đến hồ sơ kiểm tra có cấu trúc

Nhiều nghiên cứu dùng BIM để biểu diễn dữ liệu kiểm tra, khiếm khuyết và bảo trì, và hướng này đã thay đổi theo thời gian. Một hướng gắn thông tin tình trạng hoặc khiếm khuyết vào đối tượng mô hình, chẳng hạn mô hình hóa khiếm khuyết cùng quan hệ của chúng với cấu kiện và hành động bảo trì \[64\]. BIM khi đó là một lớp ngữ cảnh: dữ liệu kiểm tra được tổ chức theo vị trí và cấu kiện thay vì nằm trong báo cáo rời.

Một thuộc tính khiếm khuyết gắn vào cấu kiện tuy vậy vẫn khác với một **hồ sơ kiểm tra** có định danh, ngày tạo, người thực hiện, kết quả, trạng thái và lịch sử riêng. Các hệ thống phát triển sau đó tiến gần hơn tới logic hồ sơ theo hai cách bổ sung nhau: liên kết dữ liệu công việc quản lý vận hành với đối tượng IFC \[6\], và xây dựng hệ thống bảo trì cầu xuất phát từ yêu cầu của các bên sử dụng \[66\]. Điểm chung là dữ liệu kiểm tra có thể được tổ chức thành cấu trúc phục vụ vận hành, không chỉ để trực quan hóa trên mô hình.

Lin và cộng sự (2025) cập nhật hình học cấu kiện trong tệp IFC từ dữ liệu quét laser cho một khung thép gồm 218 cấu kiện, đưa sai lệch khoảng cách trung bình từ 17,50 mm xuống 4,00 mm. Nghiên cứu này cho thấy thông tin hiện trường ghi ngược được vào mô hình ở cấp cấu kiện. Nội dung được ghi là tọa độ trục, không phải hồ sơ kiểm tra có người chịu trách nhiệm, trạng thái xử lý và phạm vi hiệu lực của bằng chứng \[67\].

### 4.3.2. Hồ sơ khiếm khuyết, sửa chữa và trạng thái hoàn thành

Li và cộng sự (2023) cung cấp một ví dụ rõ về quản lý khiếm khuyết và sửa chữa dựa trên BIM: hệ thống sử dụng mã khiếm khuyết, liên kết với vị trí cấu kiện, lưu dữ liệu kiểm tra và bản ghi sửa chữa, đồng thời duy trì trạng thái hoàn thành \[34\].

Kết quả này có hai mặt. Việc tạo bản ghi khiếm khuyết hoặc sửa chữa gắn với cấu kiện đã có tiền lệ trực tiếp, nên một nghiên cứu mới không thể coi “đưa hồ sơ kiểm tra vào BIM” là đóng góp chính. Mặt khác, một trạng thái hiện tại như “đã hoàn thành” chưa tương đương với lịch sử trạng thái: người quản lý có thể cần biết hồ sơ được tạo khi nào, ai rà soát, ai chuyển trạng thái, hành động nào được thực hiện và dựa trên bằng chứng nào. Đó là khác biệt giữa một **trường trạng thái** và một **chuỗi sự kiện quản lý**.

### 4.3.3. Liên kết BIM với hệ quản lý bảo trì

Việc đưa BIM vào hệ quản lý bảo trì có hỗ trợ máy tính (Computerized Maintenance Management System – CMMS) cũng đã được nghiên cứu. Piras và cộng sự (2026) trình bày phương pháp tích hợp BIM với CMMS bằng chuẩn mở, trong đó *GlobalId* được duy trì khi tài sản từ BIM được đăng ký vào hệ quản lý bảo trì; khả năng điều hướng giữa danh sách tài sản và mô hình cho thấy định danh có thể giúp duy trì quan hệ qua ranh giới hệ thống \[36\].

Các nghiên cứu này chuyển trọng tâm từ một mô hình đơn lẻ sang **hệ sinh thái thông tin tài sản**. Trong vận hành, BIM hiếm khi là hệ duy nhất: dữ liệu cảm biến, công việc bảo trì, kiểm tra và tài liệu thường nằm ở các nền tảng khác nhau, nên liên kết xuyên hệ thống quan trọng hơn việc dồn mọi dữ liệu vào một tệp mô hình.

Điều hướng hai chiều trên giao diện và cập nhật dữ liệu hai chiều vẫn chưa phải truy vết bằng chứng theo nghĩa quản lý. Người dùng có thể đi từ BIM sang CMMS rồi quay lại mà vẫn không biết một yêu cầu kiểm tra được sinh ra từ bằng chứng nào, hoặc bằng chứng đó có hiệu lực tới đâu.

### 4.3.4. Từ hồ sơ gắn cấu kiện đến chuỗi thông tin có thể kiểm lại

Các nghiên cứu về kiểm tra – bảo trì đã chứng minh ba năng lực:

> 1\. dữ liệu khiếm khuyết và kiểm tra có thể được gắn với cấu kiện BIM;
>
> 2\. hồ sơ sửa chữa và trạng thái công việc có thể được số hóa;
>
> 3\. định danh có thể được duy trì khi thông tin đi giữa BIM và hệ quản lý bảo trì.

Ba năng lực này là nền cần thiết nhưng chưa đáp ứng yêu cầu về nguồn gốc và khả năng kiểm lại. Để trở thành mắt xích của chuỗi bằng chứng, hồ sơ kiểm tra cần quan hệ tường minh với căn cứ đã làm phát sinh hoạt động kiểm tra và với trạng thái xử lý sau đó. Việc cần làm là tổ chức các bản ghi thành quan hệ truy vấn được theo thời gian.

## 4.4. Định danh, nguồn gốc dữ liệu và kiểm chứng quan hệ

### 4.4.1. Nguồn gốc dữ liệu

Nguồn gốc dữ liệu (provenance) mô tả một bản ghi được tạo từ đâu, qua quá trình nào và bởi tác nhân nào. Các mô hình chuẩn như PROV-DM và PROV-O đã cung cấp từ vựng tổng quát cho thực thể, hoạt động, tác nhân và các quan hệ sinh ra, sử dụng hoặc phái sinh \[68\], \[69\], còn PAV bổ sung các khái niệm về tác giả, người đóng góp, phiên bản và dấu thời gian \[70\].

Trong xây dựng, nguồn gốc dữ liệu đã được dùng để tăng khả năng giải trình của trao đổi thông tin: ghi lại nguồn và lịch sử của dữ liệu BIM \[16\], kết hợp Song sinh số với blockchain để hỗ trợ chia sẻ thông tin có trách nhiệm giải trình \[71\], hoặc đặt nguồn gốc dữ liệu trong bối cảnh dữ liệu Song sinh số cho quản lý tài sản \[43\]. Luận án kế thừa khái niệm nguồn gốc dữ liệu từ các nghiên cứu trên; với kiểm tra – bảo trì, giá trị của nó nằm ở việc áp dụng vào bản ghi vận hành: bằng chứng nào tạo ra yêu cầu kiểm tra, hồ sơ nào sinh ra sau kiểm tra và hành động nào được ghi nhận sau đó.

Trong đo lường, White (2025) ánh xạ lược đồ chứng chỉ hiệu chuẩn số sang PROV: phòng hiệu chuẩn là prov:Organization, kỹ thuật viên và người phê duyệt là prov:Person phân biệt bằng prov:role, hiệu chuẩn và phê duyệt là hai activity riêng có thời điểm bắt đầu, thời điểm kết thúc và vị trí thực hiện. Cách làm này cho thấy từ vựng nguồn gốc đủ để ghi lại vai trò và trình tự phê duyệt của một chuỗi bằng chứng đo, với mục đích để bên kiểm toán xác minh quy trình \[72\].

### 4.4.2. Phiên bản và lịch sử thông tin

Thông tin vận hành thay đổi liên tục: dữ liệu cảm biến được bổ sung, mô hình BIM được cập nhật, hồ sơ kiểm tra được tạo mới, trạng thái công việc chuyển đổi. Nếu hệ thống không quản lý phiên bản hoặc thời điểm của các thay đổi, một bản ghi cũ sẽ mất bối cảnh.

Yêu cầu phiên bản xuất hiện đồng thời ở ba phía của chuỗi. Ở phía bằng chứng, người sử dụng cần biết phiên bản dữ liệu, chuỗi xử lý và giao thức đánh giá. Ở phía BIM, cần biết bằng chứng đã được liên kết với mô hình hoặc cấu kiện nào và tại thời điểm nào. Ở phía hồ sơ, cần duy trì lịch sử tạo, rà soát và cập nhật. Truy vết trong quản lý tài sản vì vậy là truy vết **theo thời gian**, không chỉ là truy vấn quan hệ tại trạng thái hiện tại.

### 4.4.3. Kiểm chứng quan hệ và dữ liệu không hợp lệ

Một chuỗi dữ liệu có thể tồn tại về mặt cấu trúc nhưng vẫn sai về quan hệ: một hồ sơ tham chiếu tới cấu kiện không tồn tại, một bằng chứng thiếu nguồn cảm biến, hoặc một liên kết ngược không tương ứng với liên kết thuận.

Các nghiên cứu về kiểm tra quy tắc BIM và dữ liệu ngữ nghĩa cho thấy các quan hệ như vậy kiểm chứng được bằng ràng buộc có thể thực thi. Lee, Eastman và Solihin (2021) nghiên cứu quy tắc và quá trình xác nhận dữ liệu BIM phục vụ trao đổi \[32\]; Hagedorn, Pauwels và König (2023) dùng ngôn ngữ ràng buộc SHACL để kiểm tra quan hệ xuyên miền giữa dữ liệu công trình và tác vụ, đồng thời phát hiện các trường hợp vi phạm \[21\]. Về phương pháp, Theiler và Smarsly (2018) kiểm tra lược đồ mở rộng cho hệ theo dõi trạng thái bằng các trường hợp dữ liệu không hợp lệ tạo có chủ ý \[2\]. Một mô hình dữ liệu cần chứng minh cả hai điều: trường hợp đúng chạy được, và các trường hợp sai quan trọng bị phát hiện.

Với quản lý tài sản, đây là bước chuyển từ **trình diễn hệ thống** sang **kiểm chứng cấu trúc thông tin**. Một giao diện đẹp hay một truy vấn chạy được chưa chứng minh toàn bộ quan hệ được bảo toàn; cần kiểm tra ràng buộc về tồn tại định danh, tính duy nhất, quan hệ bắt buộc, liên kết thuận – nghịch và tính đầy đủ của các trường nguồn gốc.

Trong thực hành openBIM, Information Delivery Specification (IDS) của buildingSMART đang thay thế mvdXML để mô tả yêu cầu thông tin dưới dạng máy đọc được và kiểm tra tự động mô hình theo yêu cầu đó \[73\]. Các đánh giá công cụ cho thấy cơ chế này đã dùng được trong dự án thực nhưng còn vướng ở mặt phân loại, biểu thức chính quy và cách báo lỗi \[74\]. Hai cơ chế kiểm chứng vì vậy trả lời hai câu hỏi khác nhau: IDS kiểm tra một cấu kiện có đủ thuộc tính yêu cầu hay không, còn ràng buộc ngữ nghĩa kiểm tra các quan hệ giữa bằng chứng, cấu kiện, hồ sơ và hành động có đúng hay không. Luận án kiểm tính toàn vẹn của chuỗi truy vết bằng năm ràng buộc viết bằng Python (Phụ lục B); dùng IDS cho yêu cầu thông tin ở cấp cấu kiện là hướng mở rộng (Bảng 5.7).

### 4.4.4. Truy vấn hai chiều và truy vết hai chiều

Từ đó cần phân biệt tiếp **điều hướng hai chiều** với **truy vết hai chiều có kiểm chứng**. Điều hướng hai chiều cho phép người dùng từ đối tượng A mở đối tượng B rồi quay lại A; năng lực này hữu ích về giao diện và đã có tiền lệ trong tích hợp BIM – CMMS. Truy vết hai chiều đòi hỏi mạnh hơn: quan hệ ở hai phía phải cùng biểu diễn một liên hệ có định danh và có thể được kiểm tra. Nếu một bản ghi ở hệ này bị xóa hoặc thay đổi mà hệ kia không phản ánh, điều hướng vẫn có thể tồn tại ở một phía trong khi chuỗi thông tin đã không còn toàn vẹn.

Tiêu chí cho truy vết vì vậy gồm cả khả năng kiểm tra tính nhất quán và phát hiện liên kết bị đứt, ngoài việc người dùng bấm được từ A sang B.

## 4.5. Khả thi hiện trường và hỗ trợ hành động kiểm tra – bảo trì

### 4.5.1. Khả thi triển khai khác với chẩn đoán hiện trường

Các nghiên cứu theo dõi dài hạn trên công trình thực cho thấy cảm biến triển khai được và dữ liệu động lực học thu được trong thời gian dài: hệ quan trắc trên một tòa nhà khung thép \[23\], đường cơ sở phụ thuộc nhiệt độ cho dữ liệu theo dõi dài hạn \[75\], xử lý dữ liệu dài hạn trong điều kiện biến thiên môi trường và dữ liệu thiếu \[76\].

Những nghiên cứu này chứng minh **khả thi triển khai**, chưa chứng minh khả năng chẩn đoán. Trên công trình đang khai thác, nhãn hư hỏng được xác nhận độc lập thường hiếm, điều kiện vận hành thay đổi và can thiệp bảo trì tạo thêm biến thiên. Cần tách hai câu hỏi: hệ thống có lắp đặt, thu dữ liệu và duy trì đường cơ sở được không; và dữ liệu đó có đủ căn cứ để kết luận một dạng hư hỏng cụ thể không. Một nghiên cứu có thể trả lời tốt câu thứ nhất mà chưa trả lời được câu thứ hai. Với quản lý tài sản, khả thi triển khai vẫn có giá trị riêng vì nó cho thấy nguồn dữ liệu và chuỗi hồ sơ vận hành được trong bối cảnh thật.

### 4.5.2. Đường cơ sở vận hành và bối cảnh hiện trường

Khi không đủ nhãn hư hỏng, đường cơ sở vận hành trở thành công cụ chính: dữ liệu mô tả trạng thái vận hành bình thường và giúp theo dõi các thay đổi cần xem xét, thay vì yêu cầu hệ thống nhận diện một lớp hư hỏng cụ thể.

Đường cơ sở không tách được khỏi bối cảnh. Nhiệt độ, độ ẩm, chế độ tải, thay đổi thiết bị và lịch sử bảo trì đều có thể làm thay đổi tín hiệu. Các biến này phải được ghi như bối cảnh của dữ liệu và không được mặc nhiên diễn giải thành hư hỏng. Với nhà công nghiệp khung thép, ý nghĩa quản lý của đường cơ sở là tạo tham chiếu để nhận biết biến đổi cần rà soát và hỗ trợ tổ chức thông tin cho quy trình kiểm tra.

### 4.5.3. Con người trong vòng lặp

Các quy trình kiểm tra và bảo trì đã có nhiều tiền lệ đưa con người vào các bước rà soát, xác nhận hoặc phê duyệt: người quản lý tham gia rà soát và kiểm tra kết quả sửa chữa \[78\], và quản trị con người cùng quan hệ giữa tài sản, tình trạng và công việc như thành phần của quản lý bảo trì thông minh \[29\]. Wu, El-Assady và De Wolf (2026) tiếp cận theo hướng tương tác, với một khung kết hợp thu thập dữ liệu, dự đoán, tương tác, trực quan hóa và rà soát chuyên gia \[17\].

Luận án kế thừa việc đưa con người vào quy trình kiểm tra – bảo trì từ các nghiên cứu trên. Với khả năng giải trình, điều cần xét thêm là **vai trò của con người có được ghi lại trong dữ liệu hay không**: hệ thống quản lý cần biết ai đã rà soát, khi nào, kết quả rà soát là gì và trạng thái sau rà soát thay đổi ra sao.

### 4.5.4. Mức ưu tiên, trạng thái xử lý và lịch sử chuyển trạng thái

Thông tin về một hành động kiểm tra – bảo trì gồm hai trục khác nhau. **Mức ưu tiên** (priority level) cho biết bằng chứng đề nghị mức chú ý nào đối với cấu kiện, theo thang Bình thường → Theo dõi → Kiểm tra → Kiểm tra ưu tiên. **Trạng thái xử lý** (action status) cho biết hành động đang ở bước nào, theo thang Mở → Đang xử lý → Hoàn thành → Đã xác minh. Hai trục thay đổi theo những căn cứ khác nhau: mức ưu tiên đổi khi có bằng chứng mới, theo luật minh bạch của lớp hỗ trợ hành động; trạng thái xử lý đổi khi người có vai trò tiếp nhận, thực hiện hoặc xác minh công việc. Một hành động có thể ở mức Kiểm tra ưu tiên mà vẫn đang Mở, và một hành động đã Hoàn thành vẫn cần bước Đã xác minh sau sửa chữa. Trong IFC4, trường trạng thái của yêu cầu hành động là nhãn tự do với các ví dụ như Hold, NoAction, Schedule, Urgent \[@63XPSMIR\]; theo nhận định của nghiên cứu sinh, các ví dụ này trộn mức khẩn cấp với bước xử lý trong cùng một trường, nên luận án tách thành hai trường riêng.

Các hệ thống bảo trì thường dùng trường trạng thái để theo dõi tiến độ, và đây là nền cần thiết. Từ góc độ truy vết, trạng thái hiện tại chưa mô tả được lịch sử: một bản ghi "đã hoàn thành" không tự cho biết ai đã xác nhận, vào thời điểm nào, theo tiêu chí nào và dựa trên bằng chứng trước – sau nào.

Hai tiền lệ cho thấy lịch sử chuyển trạng thái biểu diễn được. BCF-API 3.0 sinh một sự kiện có ngày, tác giả và giá trị mới mỗi khi trạng thái của vấn đề thay đổi \[@K5SGFIGW\] (mục 2.2.3). García và cộng sự (2026), với gói thông tin bàn giao trong môi trường dữ liệu chung, coi bước chuyển từ chia sẻ sang công bố là một sự kiện được quản trị, có gói bằng chứng, bản ghi quyết định, vai trò tách biệt và hai cấp ký xác nhận \[44\] (tr. 3, 19–25). Luận án kế thừa khuôn "bước chuyển có bằng chứng và đúng thẩm quyền" của \[44\] và áp cho hành động kiểm tra – bảo trì dựa trên bằng chứng tình trạng: mỗi lần chuyển trạng thái xử lý là một sự kiện ghi thời điểm, vai trò người thực hiện, bản ghi sử dụng bằng chứng làm căn cứ và lý do; trạng thái hiện thời được suy ra từ sự kiện mới nhất. Các bước chuyển được phép và vai trò tương ứng được nêu ở Phụ lục A (Bảng A.2), ràng buộc kiểm tự động ở Phụ lục B (C6, C9).

### 4.5.5. Hỗ trợ quyết định thay vì quyết định tự động

Trong quản lý tài sản, hệ thống số có thể hỗ trợ lựa chọn hành động bằng cách tổng hợp dữ liệu và trình bày căn cứ, nhưng quyết định kiểm tra hoặc bảo trì vẫn phải phụ thuộc vào vai trò có trách nhiệm. Điều này đặc biệt đúng khi bằng chứng đầu vào có phạm vi hiệu lực hạn chế: một kết quả từ dữ liệu dao động có thể cho thấy thay đổi so với đường cơ sở hoặc trạng thái tham chiếu, nhưng người quản lý còn cần xem bối cảnh, hồ sơ trước đó và thông tin kiểm tra trước khi quyết định hành động.

Giá trị của hệ thống nằm ở việc làm cho quyết định **minh bạch, có căn cứ và có thể truy ngược**, trong khi người ra quyết định vẫn là con người. Cách tiếp cận này phù hợp với quản lý tài sản khi dữ liệu hư hỏng hiện trường hạn chế.

Trong lý thuyết quyết định, giá trị của thông tin quan trắc được lượng hóa bằng phân tích Bayes tiền hậu nghiệm, và kế hoạch kiểm tra theo rủi ro dùng chính lượng này để chọn thời điểm và nội dung kiểm tra \[79\]. Luận án không giải bài toán tối ưu kế hoạch kiểm tra và không lượng hóa chi phí vòng đời. Khung giá trị thông tin được nêu ở đây như căn cứ lý thuyết cho lớp hỗ trợ hành động: mức ưu tiên kiểm tra là một đề xuất có căn cứ để người có trách nhiệm rà soát, và việc hiệu chỉnh ngưỡng chuyển mức bằng dữ liệu chi phí cùng rủi ro thuộc bước phát triển sau luận án.

## 4.6. Tổng hợp các dòng nghiên cứu và hàm ý cho Tiểu luận

Các nghiên cứu tổng quan trong Chương 4 cho thấy nhiều thành phần của chuỗi quản lý thông tin đã được giải quyết riêng lẻ. Liên kết cảm biến với BIM đã có giải pháp ở cấp lược đồ, ánh xạ định danh và cơ sở dữ liệu. Hồ sơ kiểm tra, khiếm khuyết và sửa chữa đã được gắn với cấu kiện trong nhiều hệ thống dựa trên BIM. Định danh, nguồn gốc dữ liệu và kiểm tra ràng buộc đều đã có nền phương pháp. Triển khai cảm biến dài hạn trên công trình thực và đưa con người vào quy trình kiểm tra – bảo trì cũng đã có nhiều tiền lệ. Bảng 4.2 tổng hợp các dòng nghiên cứu này cùng hàm ý của từng dòng cho chuỗi thông tin quản lý.

<span id="TLTQ_Bang_4_2" class="anchor"></span>Bảng 4.2. Tổng hợp các dòng nghiên cứu chính

| **Dòng nghiên cứu** | **Các nghiên cứu đã chứng minh** | **Hàm ý đối với chuỗi thông tin quản lý** |
|:--:|:---|:---|
| Tích hợp cảm biến – BIM | Có thể nối dữ liệu hoặc thiết bị với cấu kiện thông qua lược đồ hoặc định danh | Cần phân biệt quan hệ cảm biến – cấu kiện với quan hệ bằng chứng – cấu kiện |
| BIM cho kiểm tra và khiếm khuyết | Hồ sơ và khiếm khuyết có thể gắn với cấu kiện | Hồ sơ nên được xem là bản ghi có lịch sử riêng, không chỉ là thuộc tính |
| BIM – CMMS | Định danh có thể được duy trì qua ranh giới hệ thống | Điều hướng liên hệ thống chưa tự chứng minh tính toàn vẹn của chuỗi |
| Nguồn gốc dữ liệu | Có từ vựng và mô hình ghi nguồn, tác nhân, phiên bản | Bằng chứng kỹ thuật cần giữ được nguồn gốc khi đi vào hồ sơ quản lý |
| Kiểm chứng quan hệ | Có thể dùng quy tắc và ràng buộc để phát hiện dữ liệu sai | Truy vết cần tiêu chí kiểm tra chứ không chỉ trình diễn đường truy vấn đúng |
| Quan trắc hiện trường | Hệ cảm biến và đường cơ sở dài hạn có thể triển khai | Khả thi hiện trường phải tách khỏi chẩn đoán hư hỏng |
| Con người trong vòng lặp | Rà soát và phê duyệt đã xuất hiện trong quy trình | Vai trò, thời điểm và kết quả rà soát cần có khả năng truy lại |
| Trạng thái công việc | Hệ thống có thể lưu trạng thái và bản ghi sửa chữa | Cần phân biệt trạng thái hiện tại với lịch sử sự kiện |
| Biểu diễn quan trắc theo chuẩn mở | Từ vựng SOSA và SSN của W3C và OGC mô tả cảm biến, quy trình đo, quan trắc và kết quả | Khái niệm của bản ghi bằng chứng cần đối chiếu được với lớp quan trắc chuẩn (Phụ lục A, Bảng A.3); giao thức đánh giá và phạm vi hiệu lực nằm ngoài phạm vi của từ vựng này |
| Yêu cầu thông tin máy đọc được | Information Delivery Specification mô tả và kiểm tra yêu cầu thông tin ở cấp cấu kiện, đã dùng được trong dự án thực | Kiểm tra thuộc tính của một cấu kiện khác với kiểm tra quan hệ giữa bằng chứng, cấu kiện, hồ sơ và hành động |
| Giá trị thông tin và kế hoạch kiểm tra theo rủi ro | Lợi ích của thông tin quan trắc lượng hóa được bằng phân tích Bayes tiền hậu nghiệm, dùng để chọn thời điểm và nội dung kiểm tra | Lớp hỗ trợ hành động cần căn cứ lý thuyết cho mức ưu tiên; luận án dừng ở đề xuất có người rà soát, không tối ưu chi phí vòng đời |

Các thành phần kỹ thuật này đã tương đối trưởng thành nhưng thường được phát triển trong những hệ thống hoặc cho những mục tiêu riêng. Khi đánh giá một kiến trúc quản lý tài sản, cần xem cả việc từng thành phần có tồn tại hay không lẫn việc quan hệ giữa chúng có được duy trì và kiểm lại hay không.

Chương 4 không tự xác lập danh sách khoảng trống riêng; chương cung cấp **bằng chứng từ các nghiên cứu hiện có** cho ba nhận định sẽ được tổng hợp ở Chương 5:

- bằng chứng kỹ thuật cần giữ được nguồn gốc và phạm vi hiệu lực khi đi vào hệ thống thông tin;

- liên kết cảm biến, BIM và hồ sơ đã có tiền lệ, nên giá trị nghiên cứu nằm ở tính liên tục và khả năng kiểm chứng của quan hệ chứ không ở bản thân việc tích hợp;

- hỗ trợ hành động duy trì căn cứ và lịch sử rà soát; quyết định thuộc người có trách nhiệm.

Đến đây, ba chương nền đã hoàn tất. Việc còn lại là một phép trừ: đặt những gì các nghiên cứu đã giải quyết cạnh nhau, xác định phần thực sự còn lại sau khi trừ các tiền lệ, và kiểm tra phần còn lại có đủ để bảo vệ được hay không. Đó là nội dung của Chương 5.
