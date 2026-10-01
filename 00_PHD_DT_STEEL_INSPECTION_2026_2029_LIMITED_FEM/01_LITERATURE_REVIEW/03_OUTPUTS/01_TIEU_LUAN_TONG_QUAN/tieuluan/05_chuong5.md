# CHƯƠNG 5. TỔNG HỢP KHOẢNG TRỐNG VÀ ĐỊNH HƯỚNG NGHIÊN CỨU

## 5.1. Tổng hợp những nội dung đã được giải quyết

### 5.1.1. Từ quản lý tài sản đến yêu cầu duy trì tính liên tục của thông tin

Các chương trước cho thấy quản lý nhà công nghiệp khung thép trong giai đoạn vận hành không thiếu dữ liệu theo nghĩa tuyệt đối. Dữ liệu tồn tại ở nhiều lớp: tín hiệu cảm biến trong hệ thu nhận; hình học và thuộc tính cấu kiện trong mô hình thông tin công trình; hồ sơ kiểm tra trong biểu mẫu hoặc hệ quản lý bảo trì; lịch sử xử lý trong các hệ thống quản lý công việc.

Chương 2 cho thấy quản lý tài sản trong giai đoạn vận hành đòi hỏi thông tin phải được tổ chức theo tài sản, có ngữ cảnh và duy trì được theo thời gian. ISO 19650-3:2020 cung cấp nền cho quản lý thông tin ở giai đoạn này, nhưng chuẩn hóa thông tin không tự động tạo ra chuỗi truy vết giữa dữ liệu kỹ thuật, cấu kiện, hồ sơ và hành động \[1\].

Ở phía mô hình thông tin, IFC cung cấp nền trao đổi và định danh đối tượng, và các nghiên cứu đã nối dữ liệu vận hành với đối tượng IFC theo nhiều cách (mục 2.2.2 và mục 5.1.3). Luận án vì vậy không đặt khoảng trống ở việc “có BIM”, “có cảm biến” hay “đưa dữ liệu lên mô hình”.

Điểm cần giải quyết nằm sâu hơn: **khi một kết quả kỹ thuật đã được xác lập chất lượng và phạm vi hiệu lực, các thuộc tính đó có được bảo toàn khi kết quả đi vào chuỗi thông tin quản lý hay không**.

### 5.1.2. Dữ liệu dao động và các phương pháp đánh giá 

Chương 3 cho thấy dữ liệu dao động, học máy và học sâu đã được dùng rộng trong theo dõi trạng thái kết cấu; riêng Jia và Li (2023) tổng hợp 337 công bố về học sâu trong lĩnh vực này \[13\].

Các nguyên tắc phương pháp về đánh giá cũng không mới và bao phủ gần hết các rủi ro của một thí nghiệm dao động: phân biệt số quan sát tính toán với số đơn vị độc lập thực \[14\]; ảnh hưởng của cấp nguồn vật lý dùng để phân tách dữ liệu \[15\]; chia theo sự kiện vật lý trước rồi mới học các phép biến đổi từ phần huấn luyện \[52\]; rò rỉ còn tồn tại khi cùng một chi tiết vật lý xuất hiện ở cả hai phía phép chia \[20\]; suy giảm khả năng chuyển giao khi giữ lại một đợt thí nghiệm chưa thấy sau tháo – lắp lại \[19\].

Kiểm soát rò rỉ dữ liệu, đánh giá theo nhóm, giữ lại đơn vị vật lý, giữ lại đợt thí nghiệm và kiểm định mức ngẫu nhiên vì vậy đều không phải kỹ thuật mới \[53\], \[54\]. Giá trị nghiên cứu nằm ở việc dùng chúng để xác định **một kết quả có thể được tin cậy trong phạm vi nào**, và đầu ra cần được quản lý như **bằng chứng trạng thái** gắn với nguồn gốc và điều kiện đánh giá.

### 5.1.3. Liên kết cảm biến, BIM, hồ sơ kiểm tra và quản lý bảo trì 

Chương 4 cho thấy lớp giữa của chuỗi nghiên cứu cũng đã có tiền lệ trực tiếp ở cả bốn mắt xích. Cảm biến hoặc dữ liệu cảm biến có thể được liên kết với ngữ cảnh cấu kiện \[2\], \[4\], \[5\]. Mã khiếm khuyết, vị trí cấu kiện, dữ liệu kiểm tra, bản ghi sửa chữa và trạng thái hoàn thành có thể được tổ chức trong cùng một hệ thống \[34\]. Định danh IFC có thể được duy trì khi tài sản từ BIM được đăng ký sang hệ quản lý bảo trì \[36\]. Các liên kết xuyên miền có thể được kiểm tra bằng ràng buộc ngữ nghĩa có thể thực thi \[21\]. Nguồn gốc dữ liệu và trách nhiệm giải trình cũng đã có nền phương pháp, từ việc ghi tác nhân, thời điểm và phiên bản trong trao đổi thông tin xây dựng \[16\] tới việc đưa chuyên gia vào quá trình tương tác và rà soát kết quả \[17\]. Lorvão Antunes và cộng sự (2024) nối dữ liệu quan trắc với cấu kiện kết cấu và định danh IFC trên ba dự án thí điểm đường cao tốc \[81\]. Seiß và cộng sự (2025) dùng trực tiếp định danh IFC để gắn hồ sơ kiểm tra với cấu kiện \[82\]. Kim và cộng sự (2018) và Wan và cộng sự (2019) gắn hồ sơ bảo trì, kiểm tra với cấu kiện trên dữ liệu thực \[6\], \[78\]. Oraskari, Senthilvel và Beetz (2021) dùng ràng buộc SHACL để phát hiện đối tượng mất đối ứng định danh \[83\]. Borkowski và cộng sự (2026) đề xuất một định danh bền vững cho cấu kiện qua các giai đoạn vòng đời \[33\].

Các tiền lệ này bác bỏ mọi tuyên bố về tính mới dựa trên từng thành phần riêng lẻ. Luận án không xem các nội dung sau là đóng góp mới tự thân:

- liên kết cảm biến với BIM;

- sử dụng định danh IFC;

- đưa hồ sơ kiểm tra hoặc sửa chữa vào hệ thống số;

- điều hướng giữa BIM và hệ quản lý bảo trì;

- ghi nguồn gốc dữ liệu;

- sử dụng các quy tắc kiểm tra dữ liệu;

- đưa con người vào quy trình rà soát;

- dùng câu hỏi nghiệp vụ và phép kiểm tra đạt/không đạt khi đứng riêng;

- duy trì định danh cấu kiện qua các giai đoạn vòng đời khi đứng riêng.

Phần còn lại nằm ở **cách các thành phần đã tồn tại được nối thành một chuỗi trong đó chất lượng và phạm vi hiệu lực của bằng chứng được bảo toàn tới hồ sơ và trạng thái hành động**.

### 5.1.4. Ranh giới giữa nội dung đã có và phần nghiên cứu còn lại

<span id="TLTQ_Bang_5_1" class="anchor"></span>Bảng 5.1. Tổng hợp nội dung đã được xác lập và phần còn lại của nghiên cứu

| **Nội dung** | **Đã được xác lập** | **Phần còn lại trong phạm vi luận án** |
|:---|:---|:---|
| Dữ liệu dao động cho theo dõi trạng thái | Có nền nghiên cứu rộng | Không phải khoảng trống |
| Học máy và học sâu cho phân loại | Đã được áp dụng rộng | Không phải khoảng trống thuật toán |
| Đơn vị độc lập, đánh giá theo nhóm, kiểm soát rò rỉ | Các nguyên tắc đã được xác lập | Kết hợp và báo cáo đồng thời phạm vi hiệu lực trên đúng bài toán dao động của khung thép liên kết bu lông |
| Liên kết cảm biến với BIM/IFC | Có nhiều tiền lệ | Không phải khoảng trống |
| BIM – hệ quản lý bảo trì – hồ sơ khiếm khuyết/sửa chữa | Đã có các trường hợp triển khai | Không phải khoảng trống |
| Định danh và kiểm tra quan hệ | Đã có tiền lệ về lược đồ, đồ thị và ràng buộc | Duy trì tính liên tục của chuỗi cùng nguồn gốc và phạm vi hiệu lực của bằng chứng |
| Nguồn gốc dữ liệu | Có mô hình và từ vựng nền | Gắn với bản ghi bằng chứng trạng thái và bảo toàn tới hồ sơ/hành động |
| Con người trong quy trình | Có nhiều tiền lệ | Ghi được căn cứ, vai trò, lịch sử xử lý và trạng thái hành động trong cùng chuỗi |
| Song sinh số trong vận hành tài sản | Có nhiều mô hình khái niệm và trường hợp tích hợp | Đánh giá mức năng lực thực tế của khung sau nghiên cứu trường hợp |
| Biểu diễn quan trắc theo chuẩn mở | Đã có chuẩn SOSA và SSN | Gắn giao thức đánh giá và phạm vi hiệu lực vào bản ghi quan trắc |
| Yêu cầu thông tin và kiểm tra tuân thủ | Đã có cơ chế Information Delivery Specification cùng công cụ | Kết hợp kiểm tra thuộc tính cấu kiện với kiểm tra quan hệ của chuỗi bằng chứng |
| Chuyển giao tri thức giữa các kết cấu | Đã có khung theo quần thể cho nhóm đồng nhất và nhóm dị thể | Phát biểu mức tương đồng khi dùng kết quả mô hình thu nhỏ để nói về công trình thực |
| Giá trị thông tin và kiểm tra theo rủi ro | Đã có khung quyết định Bayes cho kế hoạch kiểm tra | Neo mức ưu tiên kiểm tra vào căn cứ rà soát được; hiệu chỉnh ngưỡng bằng dữ liệu chi phí thuộc bước sau luận án |

Cột thứ ba cho thấy ở mọi dòng, phần còn lại là một yêu cầu về *quan hệ* hoặc *sự bảo toàn thuộc tính*, không phải một thành phần công nghệ còn thiếu. Các khoảng trống của luận án nằm tại **các điểm nối giữa những thành phần đã có tiền lệ**.

## 5.2. Hai khoảng trống nghiên cứu

### 5.2.1. Khoảng trống A – Bằng chứng trạng thái có phạm vi hiệu lực

Một kết quả rút từ dữ liệu dao động của kết cấu có liên kết bu lông chỉ có nghĩa trong điều kiện đã tạo ra nó. Sau mỗi lần lắp lại khi bảo trì, phần lớn dữ liệu đáp ứng đã thu mất tác dụng cho theo dõi trạng thái \[18\]. Trên cầu thép KW51, sau khi liên kết bu lông được gia cường, mô hình huấn luyện trên dữ liệu trước can thiệp không còn đại diện cho trạng thái bình thường \[@2ZJSENQU\]. Ở phía đánh giá, chia dữ liệu theo đơn vị thấp hơn đơn vị độc lập làm con số hiệu năng lạc quan \[14\], \[15\], \[53\]. Với phát xạ âm trên dầm nhôm nối bu lông, độ chính xác giảm mạnh khi kiểm tra trên một lần lắp chưa thấy \[19\].

Điều còn chưa chắc gồm hai vế. Vế thứ nhất là mức lạc quan đó lớn đến đâu đối với phân loại dựa trên dao động của liên kết bu lông trong khung thép: các nghiên cứu đã rà soát cho bài toán này chia tập trong cùng lần lắp ráp hoặc cùng bản ghi \[48\], \[@VVBGM9EN\], nên không báo được chênh lệch. Vế thứ hai là cách ghi để biết khi nào một kết quả còn dùng được. Từ vựng nguồn gốc cho từng kết quả đã có trong PROV-O \[69\]; SSN có khái niệm điều kiện mà năng lực đo của cảm biến có hiệu lực \[CẦN NGUỒN: Khuyến nghị W3C SSN, mục 5.1\]; thẻ mô hình \[@82WQNDHU\] và phiếu thông tin mô hình \[53\] khai phạm vi ở mức mô hình, do người lập soạn. Trong các tài liệu đã rà soát, phạm vi hiệu lực và độ bất định chưa là trường bắt buộc của từng bằng chứng, có lần lắp ráp – can thiệp và điều kiện vận hành làm thành phần, và chưa được kiểm tại lần sử dụng.

Các điều kiện đó cần thiết vì hiệu lực sau can thiệp không đoán trước được: có trường hợp mất \[18\], \[@2ZJSENQU\], có trường hợp một lần siết lại vẫn được phân loại đúng \[48\], nên chỉ kiểm được khi bằng chứng được dùng. Mô hình học từ trạng thái bình thường cũng không bảo đảm với điều kiện vận hành chưa có trong huấn luyện \[@23TBQTIP\], \[45\]. Với nhà xưởng có cầu trục, điều kiện vận hành thuộc phạm vi này (Mục 3.2).

Nghiên cứu này kiểm hai điều: mức chênh lệch giữa đánh giá cùng lần chạy và hai mức đánh giá theo đơn vị độc lập, giữ lại lần chạy và giữ lại đợt thí nghiệm, trên khung thép thu nhỏ (Mục tiêu 1), và khả năng kiểm bằng máy việc dùng bằng chứng ngoài phạm vi (Mục tiêu 2). Sau nghiên cứu, người quản lý có một con số về mức lạc quan của cách đánh giá thường gặp, và một bản ghi bằng chứng mang phạm vi để trả lời câu hỏi "tin được đến mức nào?".

### 5.2.2. Khoảng trống B – Từ bằng chứng đến hành động có trách nhiệm

Chuỗi lần kiểm tra – hư hỏng – cấu kiện – nhiệm vụ bảo trì đã được biểu diễn bằng thực thể chuẩn IFC 4.3 cho phát hiện bằng mắt \[35\]. IFC4 có lệnh bảo trì có trạng thái và phê duyệt ghi người, thời điểm \[CẦN NGUỒN: IFC4 ADD2 TC1\]; BCF 3.0 ghi trạng thái vấn đề gắn cấu kiện và sự kiện đổi trạng thái \[@K5SGFIGW\]; bước chuyển có gói bằng chứng và vai trò tách biệt đã được áp cho gói thông tin bàn giao \[44\].

Điều còn chưa chắc nằm ở chỗ nối dữ liệu đo với hành động. Chuỗi của các khung song sinh số đã đọc dừng ở cảnh báo và hỗ trợ quyết định \[3\], hoặc yêu cầu người dùng xác nhận mà không nêu cách ghi lần xác nhận \[7\]. Xác nhận của chuyên gia thường được dùng làm nhãn hay dữ liệu huấn luyện, và nhãn có thể sai \[@73MBWFVJ\], \[@Z9RD5DMZ\]. Trạng thái trong \[35\] gắn với hư hỏng và được gán "đã sửa" khi có lần bảo trì. Trong các tài liệu đã rà soát, bằng chứng có phạm vi hiệu lực chưa đi vào chuỗi kiểm tra – cấu kiện – hành động, và mỗi lần đổi trạng thái của hành động, kể cả lần kỹ sư xác nhận một đầu ra AI, chưa được ghi thành sự kiện có căn cứ, vai trò người thực hiện và bước xác minh sau sửa chữa.

Các điều kiện đó cần thiết vì việc thiết kế một hệ theo dõi phải xác định hành động nào được đưa ra và ai có thẩm quyền \[@EBB69J4F\], và bảo trì nhà công nghiệp thép cần hồ sơ hư hỏng cập nhật để theo dõi khắc phục \[22\]. Theo đánh giá của nghiên cứu này, khi xảy ra sự cố sau một lần sửa chữa, đơn vị quản lý cần truy ngược quyết định về bằng chứng và người phê duyệt.

Nghiên cứu này kiểm xem một mô hình thông tin mở rộng IFC 4.3 và BCF 3.0 bằng tầng bằng chứng và tầng trách nhiệm có phát hiện được các lỗi dùng bằng chứng ngoài phạm vi và đổi trạng thái không căn cứ hay không, so với hồ sơ kiểm định hiện hành và với mô hình chỉ dùng các chuẩn sẵn có (Mục tiêu 2), và có vận hành được trên một nhà xưởng thật hay không (Mục tiêu 3). Sau nghiên cứu, câu hỏi "ai đã xử lý, dựa vào đâu?" có một chuỗi bản ghi để truy ngược.

### 5.2.3. Quan hệ giữa hai khoảng trống

Hai khoảng trống nối với nhau qua bản ghi sử dụng bằng chứng: khoảng trống A xác định bằng chứng nào còn dùng được, khoảng trống B xác định việc dùng đó được ghi và giải trình ra sao. Yêu cầu về khoảng hiệu lực của quan hệ cảm biến – cấu kiện, trước đây nêu như một khoảng trống riêng, được xử lý như một ràng buộc của mô hình dữ liệu (Mục 5.5).

## 5.3. Luận đề trung tâm và mục tiêu nghiên cứu

### 5.3.1. Luận đề trung tâm

Từ hai khoảng trống trên, luận đề trung tâm của luận án được phát biểu như sau:

Với nhà công nghiệp khung thép liên kết bu lông, kết quả rút từ dữ liệu dao động là căn cứ đề nghị kiểm tra, còn kết luận hư hỏng do kỹ sư đưa ra sau kiểm tra. Kết quả đó trở thành căn cứ đáng tin và giải trình được khi mỗi bằng chứng trạng thái mang theo nguồn gốc, độ bất định và phạm vi hiệu lực, được kiểm tại lần sử dụng, và được nối qua hồ sơ kiểm tra tới lịch sử trạng thái của hành động kiểm tra – bảo trì.

Luận đề gồm ba mệnh đề, mỗi mệnh đề cần một loại bằng chứng riêng:

> 1\. đánh giá theo đơn vị độc lập cho biết bằng chứng từ dữ liệu dao động đáng tin trong phạm vi nào (Khoảng trống A);
>
> 2\. một mô hình thông tin bắt buộc phạm vi hiệu lực và ghi từng lần đổi trạng thái của hành động thành sự kiện có căn cứ phát hiện được các lỗi mà hồ sơ hiện hành và các chuẩn sẵn có không phát hiện (Khoảng trống A, B);
>
> 3\. chuỗi bằng chứng – hành động đó vận hành được trên một nhà xưởng đang khai thác với chi phí ghi nhận đo được (Khoảng trống A, B, áp dụng).

Kết quả của một mệnh đề không dùng để thay bằng chứng của mệnh đề khác: số liệu phòng thí nghiệm của mệnh đề 1 không được dùng làm kết luận về hiện trường ở mệnh đề 3.

### 5.3.2. Mục tiêu tổng quát

Mục tiêu tổng quát của luận án là phát triển và kiểm chứng một mô hình thông tin truy vết bằng chứng – trách nhiệm cho kiểm tra – bảo trì nhà công nghiệp khung thép, trong đó bằng chứng trạng thái từ dữ liệu dao động mang nguồn gốc, độ bất định và phạm vi hiệu lực, được gắn với cấu kiện BIM, hồ sơ kiểm tra và lịch sử trạng thái hành động.

Theo phân loại mức tích hợp của \[8\], hệ thống của luận án ở mức bóng số (digital shadow): dữ liệu đi tự động từ công trình vào mô hình số, còn mọi tác động trở lại công trình đi qua quyết định của con người. Trọng tâm của mục tiêu là quản lý thông tin và giải trình quyết định kiểm tra – bảo trì; các mô hình học máy là công cụ tạo bằng chứng (Mục 5.6A).

### 5.3.3. Mục tiêu cụ thể

**Mục tiêu 1 – Bằng chứng trạng thái có phạm vi hiệu lực (phòng thí nghiệm).** Định lượng hiệu năng của bốn mô hình, gồm rừng ngẫu nhiên (Random Forest, RF), máy vectơ hỗ trợ với nhân RBF (SVM-RBF), mạng tích chập một chiều (1D-CNN) và mạng phần dư một chiều (ResNet1D), trong việc phân biệt các trạng thái liên kết bu lông có kiểm soát trên mô hình khung thép tỉ lệ 1:10 khi đánh giá theo đơn vị độc lập ở hai mức, giữ lại một lần chạy (LORO) và giữ lại một đợt thí nghiệm (LOCO); đo mức chênh lệch của mỗi mức so với đánh giá cùng lần chạy; và khai báo phạm vi hiệu lực cho từng kết quả dưới dạng bản ghi bằng chứng.

**Mục tiêu 2 – Mô hình thông tin truy vết bằng chứng – hành động.** Xây dựng mô hình thông tin mở rộng mô hình IFC 4.3 của \[35\] và BCF 3.0 \[@K5SGFIGW\] bằng hai tầng: tầng bằng chứng (nguồn gốc, độ bất định, phạm vi hiệu lực) và tầng trách nhiệm (sự kiện chuyển trạng thái có căn cứ và vai trò người thực hiện, xác minh sau sửa chữa). Mô hình gồm sáu thực thể, năm ràng buộc kiểm bằng máy và logic hỗ trợ hành động bốn mức bằng luật minh bạch. Mô hình được đánh giá trên BIM của một nhà xưởng thật, so với hồ sơ kiểm định theo thực hành hiện hành (B0) và với mô hình chỉ dùng IFC 4.3 theo \[35\] và BCF 3.0 (B1), lấy tỉ lệ phát hiện lỗi chèn mù làm chỉ số chính.

**Mục tiêu 3 – Kiểm chứng khả thi trên nhà xưởng thật.** Triển khai chuỗi bằng chứng – hành động của Mục tiêu 2 trên một nhà xưởng khung thép đang khai thác có BIM: lắp 6–10 cảm biến ở các liên kết đại diện, lập đường cơ sở vận hành, sinh bằng chứng cảm biến bằng Autoencoder có bù nhiệt độ và trạng thái cầu trục, và chạy một kịch bản kiểm tra – xử lý – truy ngược đầu cuối. Mục tiêu này kiểm khả năng vận hành và truy vết của chuỗi; hiệu năng phát hiện hư hỏng ở hiện trường thuộc hướng mở rộng (Mục 5.8).

| Mục tiêu | Khoảng trống | Câu hỏi | Đối chứng | Kết quả đo | Sản phẩm |
|---|---|---|---|---|---|
| 1 | A (đánh giá, khai báo) | 1 | Đánh giá cùng lần chạy | Hiệu năng ở hai mức đơn vị độc lập (lần chạy, đợt) kèm biến thiên theo seed, fold và kiểm định hoán vị; mức chênh lệch; phạm vi hiệu lực của từng kết quả | Bài báo 1 |
| 2 | B (và A) | 2 | B0, B1 | Tỉ lệ phát hiện lỗi chèn mù theo nhóm lỗi (chỉ số chính); đủ thuộc tính bắt buộc; thời gian truy ngược; chi phí ghi nhận | Bài báo 2 |
| 3 | A, B (áp dụng) | 3 | Không | Tỉ lệ dữ liệu về đủ; ánh xạ cảm biến – cấu kiện đúng; truy ngược kịch bản đầu cuối; chi phí ghi nhận | Chương luận án; phần hiện trường của Bài báo 2 |

Mục tiêu 1 cấp cho Mục tiêu 2 một tập bằng chứng có phạm vi hiệu lực đã biết, dùng để chèn các ca dùng bằng chứng ngoài phạm vi. Mục tiêu 2 cấp mô hình thông tin và công cụ kiểm ràng buộc cho Mục tiêu 3. Đánh giá của Mục tiêu 2 không phụ thuộc thời gian quan trắc của Mục tiêu 3. Tiểu luận tổng quan xác lập căn cứ và thiết kế của ba mục tiêu; dữ liệu và kết quả thuộc các chuyên đề và bài báo tiếp theo.

## 5.4. Câu hỏi nghiên cứu

### 5.4.1. Câu hỏi nghiên cứu 1 – Bằng chứng phòng thí nghiệm

**Khi đánh giá theo đơn vị độc lập ở hai mức, giữ lại một lần chạy và giữ lại một đợt thí nghiệm, bốn mô hình RF, SVM-RBF, 1D-CNN và ResNet1D phân biệt các trạng thái liên kết bu lông có kiểm soát trên khung thép 1:10 ở mức nào, chênh lệch bao nhiêu so với đánh giá cùng lần chạy, và mỗi kết quả được dùng trong phạm vi nào?**

Câu hỏi đo độ tin cậy của bằng chứng theo đơn vị suy luận và phạm vi đã kiểm chứng. Kết quả so sánh các mô hình được báo cáo trong phạm vi đó; thứ hạng giữa các mô hình là kết quả phụ.

### 5.4.2. Câu hỏi nghiên cứu 2 – Mô hình thông tin bằng chứng – hành động

**Trên cùng BIM nhà xưởng, so với hồ sơ kiểm định theo thực hành hiện hành (B0) và với mô hình IFC 4.3 theo \[35\] cùng BCF 3.0 chưa có tầng bằng chứng và tầng trách nhiệm (B1), mô hình đề xuất phát hiện được tỉ lệ nào của các lỗi chèn mù theo từng nhóm lỗi, và mức đủ thuộc tính bắt buộc, khả năng truy ngược, chi phí ghi nhận thay đổi ra sao?**

Hai nhóm lỗi trọng tâm là dùng bằng chứng ngoài phạm vi hiệu lực và đổi trạng thái hành động không có căn cứ. Phần chênh lệch quy cho đóng góp của luận án là chênh lệch so với B1. Chênh lệch so với B0 mô tả khoảng cách với thực hành kiểm định hiện hành ở Việt Nam và được diễn giải trong bối cảnh đó. Danh sách lỗi, người chèn lỗi, bộ câu hỏi truy ngược và cách tính chỉ số được khóa trước khi đo.

### 5.4.3. Câu hỏi nghiên cứu 3 – Khả năng áp dụng trên nhà xưởng thật

**Trên một nhà xưởng khung thép thật có BIM, chuỗi bằng chứng – hành động có thu đủ dữ liệu, giữ đúng ánh xạ cảm biến – cấu kiện và truy ngược được một kịch bản kiểm tra – xử lý đầu cuối không, với chi phí ghi nhận bao nhiêu?**

Câu hỏi kiểm khả năng vận hành của chuỗi trong điều kiện có cầu trục, nhiệt độ thay đổi và nhãn hư hỏng hạn chế. Mỗi bất thường trong dữ liệu vận hành tạo một bằng chứng đề nghị kiểm tra; kết quả kiểm tra của kỹ sư được ghi làm nhãn hiện trường và bản ghi kiểm tra.

### 5.4.4. Logic kế tiếp giữa ba câu hỏi

**Câu hỏi 1: Bằng chứng đáng tin trong phạm vi nào?\
↓\
Câu hỏi 2: Bằng chứng đó được ghi, kiểm và nối tới hành động như thế nào, và mô hình thông tin phát hiện được lỗi nào?\
↓\
Câu hỏi 3: Chuỗi đó vận hành được trên nhà xưởng thật với chi phí bao nhiêu?**

Câu hỏi 1 cấp bằng chứng có phạm vi đã biết cho câu hỏi 2; câu hỏi 2 cấp mô hình thông tin cho câu hỏi 3.

## 5.5. Ánh xạ mục tiêu – câu hỏi nghiên cứu – gói công việc – bài báo – thiết kế kiểm chứng

### 5.5.1. Ma trận kiến trúc nghiên cứu

Trong chương này, RQ là câu hỏi nghiên cứu và WP là gói công việc. Phần kiểm chứng được trình bày như thiết kế phương pháp dự kiến, để cho thấy mỗi câu hỏi cần loại bằng chứng nào; trạng thái thực hiện và kết quả thuộc các chuyên đề và bài báo tiếp theo.

<span id="TLTQ_Bang_5_2" class="anchor"></span>Bảng 5.2. Ánh xạ mục tiêu, câu hỏi nghiên cứu, gói công việc, bài báo và thiết kế kiểm chứng

| Mục tiêu | Câu hỏi | Gói công việc | Nội dung cốt lõi | Công bố dự kiến | Thiết kế kiểm chứng |
|:--:|:--:|----|----|:--:|----|
| 1 | RQ1 | WP1 – Bằng chứng dao động phòng thí nghiệm | Dữ liệu ba đợt thí nghiệm trên khung thép 1:10; bốn mô hình; đánh giá ba mức: cùng lần chạy, giữ lại lần chạy (LORO), giữ lại đợt (LOCO); kiểm định hoán vị; khai báo phạm vi hiệu lực cho từng kết quả | Bài báo 1 | Mức chênh lệch giữa ba mức đánh giá và phạm vi hiệu lực của kết quả |
| 2 | RQ2 | WP2 – Mô hình thông tin bằng chứng – hành động; WP4 – logic hỗ trợ hành động bốn mức | Sáu thực thể, năm ràng buộc kiểm bằng máy, logic bốn mức bằng luật; mở rộng IFC 4.3 của \[35\] và BCF 3.0 \[@K5SGFIGW\] | Bài báo 2 | So sánh với B0 và B1 trên cùng BIM nhà xưởng; tỉ lệ phát hiện lỗi chèn mù theo nhóm lỗi là chỉ số chính |
| 3 | RQ3 | WP3 – Triển khai trên nhà xưởng thật | 6–10 cảm biến ở liên kết đại diện; đường cơ sở vận hành; Autoencoder có bù nhiệt độ và trạng thái cầu trục; kịch bản kiểm tra – xử lý – truy ngược đầu cuối | Phần hiện trường của Bài báo 2 hoặc chương luận án | Dữ liệu về đủ, ánh xạ cảm biến – cấu kiện đúng, truy ngược kịch bản, chi phí ghi nhận |

*Ghi chú Bảng 5.2:* B0 là hồ sơ kiểm định theo thực hành hiện hành; B1 là mô hình chỉ dùng IFC 4.3 theo \[35\] và BCF 3.0, chưa có tầng bằng chứng và tầng trách nhiệm. Chương tương ứng của luận án được ghép theo ba mục tiêu sau khi hoàn thành hai bài báo.

### 5.5.2. Nội dung các bước kiểm chứng dự kiến

**Bước kiểm chứng 1 – Mức chênh lệch giữa các cách đánh giá và phạm vi hiệu lực (Mục tiêu 1).**

Xác định đơn vị độc lập (lần chạy, đợt) trên dữ liệu ba đợt; đánh giá bốn mô hình theo ba mức, cùng lần chạy, giữ lại một lần chạy (LORO) và giữ lại một đợt (LOCO); báo cáo biến thiên theo seed và fold cùng kiểm định hoán vị; ghi mỗi kết quả thành bản ghi bằng chứng có phiên bản phương pháp, độ bất định và phạm vi hiệu lực.

**Bước kiểm chứng 2 – Khóa trước khi đo (Mục tiêu 2).**

Trước lần đo đầu tiên, khóa và lưu có phiên bản: quy tắc mã hóa 20–30 hồ sơ kiểm định cũ làm B0; đặc tả B1 bám sát \[35\] và BCF 3.0; danh sách khoảng 30 lỗi do một người không tham gia thiết kế chèn mù, gồm các nhóm dùng bằng chứng ngoài phạm vi, sai thời hạn ánh xạ cảm biến – cấu kiện và đổi trạng thái không căn cứ; bộ câu hỏi truy ngược, được xác nhận với người quản lý kiểm tra – bảo trì phía chủ đầu tư; cách tính bốn chỉ số.

**Bước kiểm chứng 3 – So sánh với hai đối chứng (Mục tiêu 2).**

Chạy cùng danh sách lỗi, cùng bộ câu hỏi và cùng tập bằng chứng của Mục tiêu 1 trên B0, B1 và mô hình đề xuất; đo tỉ lệ phát hiện lỗi theo nhóm, mức đủ thuộc tính bắt buộc, thời gian truy ngược và số phút ghi nhận mỗi bản ghi.

**Bước kiểm chứng 4 – Khả năng vận hành trên nhà xưởng thật (Mục tiêu 3).**

Lắp cảm biến với bản ghi lắp đặt và khoảng hiệu lực của ánh xạ; lập đường cơ sở vận hành trong 3–6 tháng; chạy kịch bản một bất thường dẫn tới bằng chứng gắn cột, kiểm tra của kỹ sư, phê duyệt, hành động, xác minh sau sửa chữa và truy ngược; đối chiếu ánh xạ với thực địa.

## 5.6. Khung nghiên cứu bốn lớp và kiến trúc bóng số dựa trên dữ liệu

### 5.6.1. Chuỗi nghiên cứu

Chuỗi nghiên cứu được giữ cố định theo Hình 1.1, và mỗi mũi tên trong chuỗi mang một nghĩa vụ kiểm chứng riêng. Mũi tên thứ nhất yêu cầu bằng chứng được tạo theo đơn vị độc lập, tách khỏi rò rỉ dữ liệu. Mũi tên thứ hai yêu cầu bằng chứng được gắn đúng cấu kiện và giữ được nguồn gốc. Mũi tên thứ ba yêu cầu hồ sơ kiểm tra là một bản ghi truy vết được. Mũi tên cuối yêu cầu mỗi lần đổi trạng thái hành động có căn cứ, vai trò người thực hiện và lịch sử truy lại được.

### 5.6.2. Chuỗi định danh và mô hình dữ liệu dạng đồ thị

![](../figures/Hinh_5_1_Chuoi_dinh_danh_cot_loi.png)
<!-- GĐ0: hình gốc vẽ bằng shape trong .docx; ảnh cắt từ PDF do Word xuất ngày 28/09/2026 -->

<span id="TLTQ_Hinh_5_1" class="anchor"></span>Hình 5.1. Chuỗi định danh cốt lõi

Trong đó *Sensor_ID* là định danh nguồn đo; *BIM_GUID* là định danh cấu kiện trong mô hình thông tin; *Condition_Evidence_ID* là định danh bản ghi bằng chứng trạng thái; *Inspection_Record_ID* là định danh hồ sơ kiểm tra; *Action_Status* là trạng thái xử lý hiện thời của hành động kiểm tra hoặc bảo trì.

Hình 5.1 là cách trình bày chuỗi cho người đọc. Mô hình dữ liệu của luận án là một đồ thị gồm sáu thực thể: cấu kiện, cảm biến cùng ánh xạ cảm biến – cấu kiện có khoảng hiệu lực, bằng chứng, hồ sơ kiểm tra, hành động và sự kiện chuyển trạng thái (Mục 5.7.2). Quan hệ giữa bằng chứng và cấu kiện là nhiều – nhiều; một hồ sơ kiểm tra dùng bằng chứng qua một quan hệ ghi bằng chứng đó có nằm trong phạm vi hiệu lực hay không. Sự kiện chuyển trạng thái là thực thể bắt buộc: trạng thái xử lý hiện thời được suy ra từ chuỗi sự kiện, mỗi sự kiện ghi thời điểm, vai trò người thực hiện, lý do và bằng chứng đã dùng. Bản ghi bằng chứng không bị sửa đè; một bản ghi mới thay bản cũ bằng một quan hệ trỏ về bản cũ. Chi tiết định danh và thuộc tính được trình bày ở Phụ lục A. *FEM_Node_ID*, nếu có, là siêu dữ liệu tùy chọn.

Cần phân biệt hai loại đúng đắn. Loại thứ nhất là tính toàn vẹn của dữ liệu: bộ ràng buộc kiểm được bản ghi mồ côi, ánh xạ đã hết hiệu lực tại thời điểm đo, bằng chứng dùng ngoài phạm vi mà không có lý do, và bước chuyển trạng thái không có căn cứ. Loại thứ hai là tính đúng của ánh xạ cảm biến – cấu kiện ngoài thực tế, tức là cảm biến có thực sự được lắp ở cấu kiện đã khai báo. Loại thứ hai dựa trên hồ sơ lắp đặt và đối chiếu tại hiện trường (Mục tiêu 3), vì dữ liệu của mô hình không chứa thông tin này. Quan hệ Sensor_ID → BIM_GUID ghi nguồn đo gắn với cấu kiện nào; nguồn vật lý của một bất thường được xác định qua kiểm tra của kỹ sư.

### 5.6.3. Bốn lớp bằng chứng

![](../figures/Hinh_5_2_Kien_truc_kiem_chung_bon_lop.png)
<!-- GĐ0: hình gốc vẽ bằng shape trong .docx; ảnh cắt từ PDF do Word xuất ngày 28/09/2026 -->

<span id="TLTQ_Hinh_5_2" class="anchor"></span>Hình 5.2. Kiến trúc kiểm chứng bốn lớp

Bốn lớp là bốn loại bằng chứng; mỗi lớp chỉ khẳng định điều nó kiểm chứng được và không mượn bằng chứng của lớp khác.

**Lớp 1 – Bằng chứng phòng thí nghiệm (Mục tiêu 1).** Phân biệt các trạng thái liên kết có kiểm soát trong phạm vi đã thí nghiệm, dưới đánh giá theo đơn vị độc lập. Đầu ra là bản ghi bằng chứng có nguồn gốc, cấu hình cảm biến, phiên bản phương pháp, độ bất định và phạm vi hiệu lực.

**Lớp 2 – Truy vết thông tin (Mục tiêu 2).** Chuỗi định danh, bản ghi và quan hệ có tính toàn vẹn, kiểm được bằng năm ràng buộc và bằng bộ lỗi chèn mù; trả lời được ba câu hỏi của người quản lý: cái gì bất thường, ở đâu; tin được đến mức nào; ai đã xử lý, dựa vào đâu.

**Lớp 3 – Khả năng áp dụng trong bối cảnh thực tế (Mục tiêu 3).** Chuỗi giữ được quan hệ giữa dữ liệu vận hành, cấu kiện, bằng chứng, hồ sơ kiểm tra và trạng thái hành động trên một nhà xưởng đang khai thác. Bộ phân loại và ngưỡng của mô hình 1:10 chỉ được dùng ở lớp này sau khi kiểm tra phạm vi hiệu lực.

**Lớp 4 – Hỗ trợ quyết định quản lý (Mục tiêu 2 và 3).** Một bằng chứng đi vào quá trình xem xét hành động theo logic bốn mức bằng luật minh bạch, có người rà soát và có sự kiện chuyển trạng thái được ghi; quyết định thuộc kỹ sư và người quản lý có thẩm quyền.

### 5.6.4. Thang kiểm chứng

<span id="TLTQ_Bang_5_3" class="anchor"></span>Bảng 5.3. Thang kiểm chứng của khung nghiên cứu

| **Mức** | **Mục tiêu** | **Nội dung kiểm chứng** | **Điều không được suy ra** |
|:--:|:--:|:---|:---|
| V1 – Giá trị phòng thí nghiệm | 1 | Phân biệt trạng thái có kiểm soát dưới đánh giá theo đơn vị độc lập (lần chạy, đợt); mức chênh lệch so với đánh giá cùng lần chạy | Chẩn đoán hiện trường |
| V2 – Giá trị truy vết | 2 | Tỉ lệ phát hiện lỗi chèn mù so với B0 và B1; trả lời bộ câu hỏi truy ngược | Độ chính xác kỹ thuật của mô hình phân loại |
| V3 – Khả năng áp dụng trong bối cảnh thực tế | 3 | Dữ liệu về đủ, ánh xạ đúng, truy ngược được kịch bản đầu cuối, chi phí ghi nhận | Phát hiện hư hỏng thực |
| V4 – Giá trị hỗ trợ quyết định | 2, 3 | Mỗi mức ưu tiên và mỗi sự kiện chuyển trạng thái truy được về luật, bằng chứng và người rà soát | Quyết định tự động hoặc hiệu quả của quyết định |

### 5.6.5. Luồng dữ liệu và luồng trách nhiệm

Kiến trúc nghiên cứu gồm hai luồng song song. **Luồng dữ liệu** đi từ cảm biến tới bằng chứng, cấu kiện, hồ sơ và trạng thái hành động. **Luồng trách nhiệm** đi từ người hoặc hệ thống tạo dữ liệu, qua người kiểm tra, người phê duyệt và người thực hiện hành động, tới người xác minh sau sửa chữa.

Hai luồng gặp nhau tại bản ghi. Bản ghi bằng chứng lưu giá trị cùng nguồn tạo ra, thời điểm, phiên bản phương pháp, độ bất định và phạm vi hiệu lực; sự kiện chuyển trạng thái lưu trạng thái trước và sau, thời điểm, vai trò người thực hiện, lý do và bằng chứng đã dùng. Khả năng giải trình trong quản lý tài sản dựa trên chính các trường này.

### 5.6.6. Định vị bóng số

Các nghiên cứu phân mức song sinh số theo nhiều cách: theo chiều và mức tự động của luồng dữ liệu \[8\], theo các mức biểu diễn số trong môi trường xây dựng \[9\], hoặc theo mô hình trưởng thành đa chiều cho quản lý tài sản \[10\]. Luận án dùng phân loại của \[8\] để khai báo mức tích hợp: dữ liệu đi tự động từ công trình vào mô hình số, còn mọi tác động trở lại công trình đi qua quyết định của con người, nên hệ thống ở mức bóng số (digital shadow). Tên đề tài giữ cụm "song sinh số dựa trên dữ liệu" theo hướng kiến trúc, kèm khai báo này.

Các thang trưởng thành của \[9\], \[10\] là tham chiếu để đánh giá năng lực đạt được sau triển khai trên nhà xưởng (Mục tiêu 3). Điều khiển tự động lên công trình, bảo trì dự đoán và dự báo tuổi thọ còn lại nằm ngoài phạm vi luận án (Mục 5.8).

## 5.6A. Công cụ trí tuệ nhân tạo và vai trò trong chuỗi bằng chứng

### 5.6A.1. Nguyên tắc: AI tạo bằng chứng, con người quyết định

Trong kiểm tra – bảo trì kết cấu thép, mỗi quyết định kiểm tra, siết lại hay thay thế cấu kiện phải truy ngược được tới người có thẩm quyền và căn cứ người đó đã dùng. Vì vậy, trong luận án, công cụ trí tuệ nhân tạo (AI) tạo bằng chứng, còn quyết định thuộc về kỹ sư và người quản lý có thẩm quyền. Mỗi đầu ra của mô hình được ghi thành một bản ghi bằng chứng (Mục 5.7.2) mang phiên bản phương pháp, trường độ bất định và trường phạm vi hiệu lực; chẩn đoán hư hỏng là kết luận của kỹ sư sau kiểm tra. Trên nền Mục 3.2.3, mục này xác định công cụ cho từng gói công việc và trường dữ liệu nhận đầu ra.

### 5.6A.2. Phòng thí nghiệm (WP1): phân biệt trạng thái liên kết có kiểm soát

Ở WP1, trạng thái liên kết được tạo có kiểm soát trên mô hình khung thép, nên bài toán là phân loại có giám sát. Họ mô hình thứ nhất học trên đặc trưng thủ công miền thời gian – tần số: rừng ngẫu nhiên (Random Forest, RF) \[@5TQ4AZVX\] và máy véc-tơ hỗ trợ với nhân hàm cơ sở bán kính (SVM-RBF) \[@JVI2GUPC\]. Họ thứ hai học trực tiếp trên tín hiệu đã chuẩn hóa. Mạng nơ-ron tích chập một chiều (1D-CNN) gộp trích đặc trưng và phân loại vào một khối học trên tín hiệu gia tốc thô \[@HPREAQAJ\], và đã được tổng quan cho tín hiệu một chiều, trong đó có theo dõi trạng thái kết cấu \[@IU5KZQEA\], \[@QUGY4928\]. Mạng dư một chiều (ResNet1D) kế thừa khối dư (residual block) của He và cộng sự (2016) \[@69U5H3TZ\]; Wang, Yan và Oates (2017) cho thấy cấu trúc ResNet học trực tiếp từ chuỗi thời gian thô đạt kết quả cạnh tranh trong phân loại \[@WXHN9TA2\]. Hai họ được dùng song song để đối chiếu xem kết luận có phụ thuộc cách biểu diễn tín hiệu hay không.

Giao thức đánh giá kế thừa Mục 3.3. Dữ liệu được chia theo nhóm ở hai mức, giữ lại cả lần chạy (LORO) và giữ lại cả đợt thí nghiệm (LOCO), để các cửa sổ của một bản ghi nằm trọn ở một phía của phép chia \[14\], \[53\]; mức đợt phản ánh biến thiên do tháo – lắp lại và trạng thái tiếp xúc \[18\], \[19\], \[56\]; đánh giá cùng lần chạy chỉ dùng làm mốc để đo mức lạc quan; điểm được chấm theo bản ghi, là đơn vị vật lý của phép đo; kiểm định hoán vị cho biết hiệu năng có vượt mức ngẫu nhiên hay không \[59\]. Siêu tham số được cố định trước hoặc chọn bên trong vòng huấn luyện của từng lần chia, vì sai số kiểm định chéo của một bộ phân loại đã tinh chỉnh bằng chính phép kiểm định đó bị lệch lạc quan \[@D28DT7CE\]; độ lệch lớn hơn khi cỡ mẫu nhỏ và khi chọn đặc trưng trên dữ liệu gộp \[@6JAQQCGE\]. Kết quả được báo cáo kèm biến thiên theo seed và theo fold.

Cấp nhóm, đơn vị chấm điểm và đợt lắp đặt ghi vào trường phạm vi hiệu lực của bản ghi bằng chứng (cách chia dữ liệu, đơn vị suy luận, đợt lắp đặt); biến thiên theo seed, fold và kết quả kiểm định hoán vị ghi vào trường độ bất định; nhãn hoặc xác suất lớp ghi vào trường giá trị; mã phiên bản của chuỗi xử lý (git commit) ghi vào trường phiên bản phương pháp. Kết quả thực nghiệm của WP1 thuộc chuyên đề tiếp theo.

### 5.6A.3. Hiện trường (WP3): từ phân loại sang phát hiện bất thường

Bốn nhóm bằng chứng tổng hợp ở Mục 3.2A.4 cho thấy bộ phân loại học ở phòng thí nghiệm khó chuyển nguyên sang nhà xưởng: nhãn hiện trường hiếm và đắt, độ lặp lại của kết cấu có mối nối phụ thuộc quy trình lắp ráp, biến đổi môi trường – vận hành có thể che lấp thay đổi do hư hỏng, và bộ phân loại học trên một kết cấu thất bại khi áp sang kết cấu tương tự.

Từ đó, luận án đề xuất đổi vai AI ở WP3: mô hình học đường cơ sở vận hành của chính công trình (Mục 4.5.2) và báo độ lệch so với đường cơ sở. Công cụ chính là bộ tự mã hóa (autoencoder). Wang và Cha (2021) huấn luyện autoencoder sâu chỉ bằng gia tốc đo ở trạng thái nguyên vẹn, lấy sai lệch tái tạo làm đặc trưng, và kiểm chứng trên cầu thép thu nhỏ có bu lông bị nới lỏng tại nút \[@TDRPDWJE\]. Ghazimoghadam và Hosseinzadeh (2024) cũng học từ trạng thái chưa hư hỏng và phát hiện bu lông liên kết bị nới lỏng trên kết cấu phòng thí nghiệm \[@G98ZWHKW\]. Luận án đề xuất áp dụng nguyên tắc này cho nhà công nghiệp khung thép; hiệu quả khi có cầu trục và máy móc vận hành là nội dung kiểm chứng của WP3. Sai số tái tạo được ghi thành bản ghi bằng chứng loại cảm biến với nghĩa là tín hiệu đề nghị kiểm tra. Vì định vị và định lượng hư hỏng vẫn khó khi dữ liệu huấn luyện thiếu thông tin hư hỏng \[@TDRPDWJE\], tình trạng cấu kiện được xác định qua kiểm tra của kỹ sư.

Để giảm báo động giả, luận án đề xuất bù ảnh hưởng môi trường – vận hành (EOV) theo hướng thứ nhất trong hai hướng Figueiredo và cộng sự (2011) phân biệt: tham số hóa đặc trưng theo các biến đo được, thay vì học trạng thái bình thường trực tiếp từ dữ liệu đáp ứng \[@23TBQTIP\]. Ở nhà xưởng, hai biến được ghi vào bối cảnh quan trắc của mỗi bằng chứng là nhiệt độ và trạng thái cầu trục (chạy hoặc dừng); phần bù là hồi quy theo hai biến này. Phân tích đồng liên kết (cointegration) tạo phần dư dừng đã loại xu hướng chung mà không cần đo điều kiện môi trường – vận hành \[@KPWFC4PI\]; luận án giữ phương pháp này làm hướng mở rộng khi xuất hiện nguồn biến động chưa đo được. Các thuật toán bù có thể thất bại với điều kiện chưa có trong dữ liệu huấn luyện \[@23TBQTIP\], nên dải điều kiện của đường cơ sở được ghi vào trường điều kiện áp dụng, và bằng chứng sinh ngoài dải đó phải kèm lý do khi sử dụng (ràng buộc về sử dụng bằng chứng ngoài phạm vi hiệu lực, Phụ lục B).

Nhãn hiện trường của luận án sinh từ vòng lặp kiểm tra tạo nhãn: một bằng chứng cảm biến vượt ngưỡng đề nghị kiểm tra theo logic bốn mức, kỹ sư kiểm tra cấu kiện, và kết quả được ghi thành bản ghi kiểm tra có người thực hiện, thời điểm và độ bất định của kiểm tra, làm nhãn hiện trường gắn với cấu kiện và với bằng chứng đã kích hoạt lần kiểm tra. Hughes và cộng sự (2022) coi mỗi lần hỏi nhãn là một lần kiểm tra kết cấu, với giả định kiểm tra cho thông tin hoàn hảo \[@Z9RD5DMZ\]; Bull và cộng sự (2022) lưu ý trạng thái ở thời điểm đã qua không kiểm tra lại được \[@87NKU5IS\], nên kết quả kiểm tra phải được ghi đúng lúc. Việc chọn lần kiểm tra theo giá trị kỳ vọng của thông tin (học chủ động), như hai nghiên cứu này đề xuất trên dữ liệu cầu, là hướng mở rộng của luận án (Mục 5.8).

### 5.6A.4. Hồ sơ và hỗ trợ hành động (WP2, WP4)

Ở WP2, đường cơ sở B0 được lập bằng cách mã hóa tay 20–30 hồ sơ kiểm định cũ theo quy tắc đã khóa trước khi đo (Mục 5.5); bước này không dùng công cụ AI. Ở WP4, logic bốn mức ưu tiên được viết bằng luật minh bạch, nên mỗi sự kiện chuyển trạng thái truy ngược được tới luật đã áp dụng, quan hệ sử dụng bằng chứng và bằng chứng đã dùng.

### 5.6A.5. Tổng hợp công cụ theo gói công việc

<span id="TLTQ_Bang_5_6A" class="anchor"></span>Bảng 5.6A. Công cụ trí tuệ nhân tạo theo gói công việc và trường dữ liệu tương ứng

| **Gói** | **Công cụ** | **Vai trò** | **Đầu ra** | **Trường dữ liệu tương ứng** |
|:--:|:---|:---|:---|:---|
| WP1 | RF, SVM-RBF; 1D-CNN, ResNet1D | Phân biệt trạng thái liên kết có kiểm soát | Nhãn hoặc xác suất lớp theo bản ghi | Giá trị của bản ghi bằng chứng |
| WP1 | Đánh giá theo nhóm, chấm điểm theo bản ghi, kiểm định hoán vị, biến thiên theo seed và fold | Căn cứ khai báo | Cấp chia, đơn vị suy luận, đợt lắp đặt; biến thiên | Phạm vi hiệu lực, độ bất định của bản ghi bằng chứng |
| WP3 | Autoencoder học đường cơ sở vận hành | Phát hiện độ lệch so với đường cơ sở | Sai số tái tạo; đề nghị kiểm tra | Bản ghi bằng chứng loại cảm biến |
| WP3 | Bù EOV bằng hồi quy theo nhiệt độ và trạng thái cầu trục | Giảm báo động giả do cầu trục, máy móc, nhiệt | Đặc trưng đã bù; dải điều kiện đường cơ sở | Bối cảnh quan trắc, điều kiện áp dụng |
| WP2 | Không dùng AI; mã hóa tay hồ sơ cũ | Phân loại lỗi; đường cơ sở B0 | Bản ghi lỗi đã mã hóa | Hồ sơ kiểm tra (B0) |
| WP4 | Logic bốn mức bằng luật minh bạch | Đề xuất mức ưu tiên | Mức ưu tiên kèm luật đã áp dụng | Mức ưu tiên của hành động; sự kiện chuyển trạng thái |

Công cụ hỗ trợ ngoài AI gồm Python, scikit-learn, PyTorch; git để cấp mã phiên bản phương pháp; IfcOpenShell để đọc và ghi IFC; SQLite để lưu bản ghi; một công cụ viết bằng Python để kiểm năm ràng buộc ở Phụ lục B. Việc sử dụng AI tạo sinh khi thực hiện Tiểu luận được khai báo ở phần đầu; phạm vi diễn giải của các công cụ trên được trình bày ở Mục 5.8.

## 5.7. Đóng góp dự kiến của luận án

### 5.7.1. Đóng góp 1 – Mức lạc quan của đánh giá cùng lần chạy và bằng chứng có phạm vi hiệu lực (thực nghiệm – phương pháp)

Đóng góp dự kiến thứ nhất là số đo mức chênh lệch giữa đánh giá cùng lần chạy và hai mức đánh giá theo đơn vị độc lập, giữ lại lần chạy và giữ lại đợt thí nghiệm, cho phân loại trạng thái liên kết bu lông từ dữ liệu dao động trên khung thép, cùng một cách ghi mỗi kết quả thành bản ghi bằng chứng có nguồn gốc, độ bất định và phạm vi hiệu lực. Nghiên cứu kế thừa cách so sánh hai thiết kế đánh giá từ \[19\], làm cho phát xạ âm trên dầm nhôm, và từ \[15\], làm cho ổ trục; phần riêng của luận án là tín hiệu dao động trên khung thép nhiều liên kết, bốn họ mô hình và khai báo phạm vi cho từng kết quả.

Nếu hiệu năng giảm khi giữ lại cả lần chạy hoặc cả đợt, mức giảm ở mỗi mức là kết quả cần báo cáo: nó cho biết phạm vi hiệu lực hẹp đến đâu. Đóng góp này thuộc RQ1, WP1 và Bài báo 1. Phạm vi diễn giải được trình bày ở Mục 5.8.

### 5.7.2. Đóng góp 2 – Mô hình thông tin bằng chứng – hành động được đánh giá với hai đối chứng (artefact thiết kế)

Đóng góp dự kiến thứ hai là mô hình thông tin mở rộng IFC 4.3 của \[35\] và BCF 3.0 \[@K5SGFIGW\] bằng tầng bằng chứng và tầng trách nhiệm. Tầng bằng chứng đặt phạm vi hiệu lực và độ bất định thành trường bắt buộc của từng bằng chứng và kiểm tại lần sử dụng. Tầng trách nhiệm ghi mỗi lần đổi trạng thái của hành động thành sự kiện trỏ về bằng chứng đã dùng, có vai trò người thực hiện và bước xác minh sau sửa chữa. Năm ràng buộc kiểm bằng máy là không có bản ghi mồ côi; thời điểm đo nằm trong khoảng hiệu lực của ánh xạ cảm biến – cấu kiện; dùng bằng chứng ngoài phạm vi phải có lý do; bước chuyển trạng thái có căn cứ và đúng vai trò; sự kiện trỏ tới phiên bản bằng chứng còn hiệu lực tại thời điểm chuyển. Các khái niệm của SOSA/SSN và PROV-O được đối chiếu bằng một bảng ánh xạ; luận án không xây dựng ontology hay nền tảng phần mềm mới.

Logic hỗ trợ hành động bốn mức (Bình thường → Theo dõi → Kiểm tra → Kiểm tra ưu tiên) là một phần của mô hình này. Mỗi mức ưu tiên gắn với bằng chứng, phạm vi hiệu lực, cấu kiện, hồ sơ kiểm tra, vai trò người rà soát và lịch sử trạng thái xử lý. Bất thường hiện trường dẫn tới kiểm tra; kết luận hư hỏng do kỹ sư đưa ra sau kiểm tra.

![](../figures/Hinh_5_3_Logic_ho_tro_hanh_dong.png)
<!-- GĐ0: hình gốc vẽ bằng shape trong .docx; ảnh cắt từ PDF do Word xuất ngày 28/09/2026 -->

<span id="TLTQ_Hinh_5_3" class="anchor"></span>Hình 5.3. Logic hỗ trợ hành động

Phần quy cho đóng góp là chênh lệch giữa mô hình đề xuất và B1, đo bằng tỉ lệ phát hiện lỗi chèn mù theo nhóm lỗi. Chênh lệch với B0 là đóng góp bối cảnh – thực tiễn cho thực hành kiểm định ở Việt Nam. Đóng góp này thuộc RQ2, WP2, WP4 và Bài báo 2. Phạm vi diễn giải được trình bày ở Mục 5.8.

### 5.7.3. Đóng góp 3 – Kiểm chứng khả thi của chuỗi bằng chứng – hành động trên nhà xưởng thật

Đóng góp dự kiến thứ ba là bằng chứng rằng chuỗi của Đóng góp 2 vận hành được trên một nhà xưởng khung thép đang khai thác có BIM, với số đo về dữ liệu thu được, độ đúng của ánh xạ cảm biến – cấu kiện, khả năng truy ngược một kịch bản đầu cuối và chi phí ghi nhận. Phần chuyển được từ mô hình 1:10 sang công trình là nguyên tắc tổ chức và truy vết bằng chứng; bộ phân loại và ngưỡng của phòng thí nghiệm được dùng lại chỉ sau khi kiểm tra phạm vi hiệu lực. Điều kiện vận hành, gồm trạng thái cầu trục và nhiệt độ, được ghi làm bối cảnh quan trắc của từng bằng chứng.

Đóng góp này thuộc RQ3, WP3, phần hiện trường của Bài báo 2 hoặc chương luận án tương ứng. Phạm vi diễn giải được trình bày ở Mục 5.8.

### 5.7.4. Đóng góp ở cấp ngành Quản lý xây dựng

Ba đóng góp trên hợp lại thành một cách tổ chức và kiểm chứng dòng thông tin từ bằng chứng kỹ thuật tới quy trình kiểm tra – bảo trì. Luận án dùng dữ liệu dao động, học máy và BIM làm công cụ; đối tượng quản lý là thông tin về trạng thái tài sản, hồ sơ kiểm tra và trạng thái hành động. Đóng góp ở cấp ngành được phát biểu ở dạng quản lý thông tin tài sản: mỗi hành động kiểm tra truy ngược được về căn cứ, phạm vi hiệu lực, người rà soát và lịch sử xử lý. Toàn bộ mục này là đóng góp dự kiến.

## 5.8. Phạm vi, giới hạn và điều kiện diễn giải kết quả

### 5.8.1. Phân lớp phạm vi

<span id="TLTQ_Bang_5_4" class="anchor"></span>Bảng 5.4. Phạm vi của luận án

| **Nhóm** | **Nội dung** |
|:---|:---|
| **Phạm vi cốt lõi** | Dữ liệu dao động → bằng chứng trạng thái; truy vết tới cấu kiện BIM; hồ sơ kiểm tra; trạng thái/hỗ trợ hành động; đánh giá khả năng áp dụng trong bối cảnh nhà công nghiệp khung thép |
| **Phạm vi hỗ trợ** | Học máy và học sâu như công cụ tạo bằng chứng; BIM/IFC; nguồn gốc dữ liệu; con người trong vòng lặp; mô hình phần tử hữu hạn danh nghĩa để tham chiếu |
| **Hướng phát triển sau luận án** | Kiểm chứng khung trên các loại kết cấu và tài sản công trình khác; hiệu chuẩn và cập nhật mô hình phần tử hữu hạn nếu có câu hỏi nghiên cứu phù hợp; đánh giá kinh tế quy mô lớn; các năng lực Song sinh số cao hơn khi có đủ dữ liệu và hạ tầng; đánh giá hiệu năng phát hiện hư hỏng ở hiện trường; chọn lần kiểm tra theo giá trị kỳ vọng của thông tin (học chủ động); bù EOV bằng đồng liên kết khi có nguồn biến động chưa đo được |
| **Ngoài phạm vi hiện tại** | Chẩn đoán hư hỏng hiện trường khi chưa có kiểm tra xác nhận; dự báo tuổi thọ còn lại; bảo trì dự báo; suy luận suy giảm độ cứng; chỉ số sức khỏe phức tạp; tối ưu vị trí cảm biến; bảo trì tự động; trí tuệ nhân tạo tại biên; Thành phố thông minh; động lực học chất lưu tính toán; phát triển phần mềm thương mại |

### 5.8.2. Ranh giới giữa bốn loại bằng chứng

**Bằng chứng phòng thí nghiệm** chỉ chứng minh khả năng phân biệt các trạng thái có kiểm soát trong điều kiện đã kiểm chứng. Nó không chứng minh hư hỏng trong bối cảnh sử dụng thực.

**Bằng chứng truy vết thông tin** chỉ chứng minh tính toàn vẹn và khả năng kiểm tra của chuỗi quan hệ. Nó không chứng minh độ chính xác của mô hình phân loại.

**Bằng chứng về khả năng áp dụng trong bối cảnh thực tế** chỉ chứng minh kiến trúc có thể duy trì các quan hệ thông tin cần thiết trong điều kiện vận hành. Nó không chứng minh phát hiện hư hỏng thực.

**Bằng chứng hỗ trợ quyết định** chỉ chứng minh quy trình có thể trình bày căn cứ minh bạch và được con người rà soát. Nó không chứng minh hành động là tối ưu hoặc tự động đúng trong mọi trường hợp.

Quy tắc chung:

Mọi bất thường trong dữ liệu vận hành dẫn tới xem xét và kiểm tra, không dẫn trực tiếp tới kết luận hư hỏng.

### 5.8.3. Giới hạn của mô hình phần tử hữu hạn

Mô hình phần tử hữu hạn chỉ được giữ như **mô hình danh nghĩa, chưa hiệu chuẩn, chỉ dùng để tham chiếu và không dùng cho chẩn đoán hư hỏng**. Mô hình có thể hỗ trợ minh họa vị trí cấu kiện hoặc tham khảo bố trí cảm biến nếu ghi rõ giới hạn, nhưng không được dùng để suy ra suy giảm độ cứng, suy ra lực siết bu lông, xác định mức độ hư hỏng, hiệu chuẩn bộ phân loại, hoặc chuyển kết luận định lượng từ mô hình 1:10 sang công trình thực. Mô hình phần tử hữu hạn không có câu hỏi nghiên cứu, gói công việc, chương, bài báo hoặc nghĩa vụ kiểm chứng độc lập.

### 5.8.4. Giới hạn của tổng quan tài liệu

Tiểu luận sử dụng **tổng quan tài liệu theo chủ đề có cấu trúc**, không tự nhận là tổng quan hệ thống toàn diện hoặc phân tích thư mục định lượng. Ba khoảng trống nghiên cứu trong tập tài liệu đã kiểm chứng; một số nguồn gần với lớp truy vết và hành động vẫn chưa đầy đủ và đang tiếp tục rà soát.

Các phát biểu về khoảng trống vì vậy dùng ngôn ngữ có điều kiện và không được nâng thành tuyên bố thiếu vắng phổ quát. Mức bằng chứng hiện tại đủ để xác lập một hướng nghiên cứu hẹp, kiểm chứng được, nhưng không đủ để tuyên bố độc quyền về các thành phần kỹ thuật riêng lẻ.

### 5.8.5. Giới hạn và điều kiện của định vị Song sinh số

Ở thời điểm tổng quan, Tiểu luận không khẳng định hệ thống đã đạt một mức Song sinh số cụ thể, không giả định đồng bộ hai chiều tự động khi chưa được kiểm chứng và không tự gán năng lực tự quản lý. Việc xác định mức năng lực thực tế thuộc giai đoạn nghiên cứu chuyên đề sau tổng quan và phải dựa trên các chức năng thực sự được hiện thực hóa, không dựa trên tên gọi của kiến trúc.

## 5.9. Định hướng nghiên cứu sau Tiểu luận tổng quan

Từ kết quả tổng quan, hai khoảng trống nghiên cứu đã được thu hẹp đủ để hình thành ba bước nghiên cứu theo ba mục tiêu. Các bước kế tiếp nhau về dữ liệu nhưng một phần làm song song được.

### 5.9.1. Định hướng 1 – Đánh giá theo đơn vị độc lập và khai báo phạm vi hiệu lực (Mục tiêu 1)

Chuyên đề thứ nhất thực hiện Bước kiểm chứng 1 trên dữ liệu ba đợt thí nghiệm và hình thành Bài báo 1. Tiểu luận xác lập yêu cầu phương pháp (Chương 3 và Mục 5.6A); dữ liệu, cấu hình phân tích, chỉ số và kết quả thuộc chuyên đề này.

### 5.9.2. Định hướng 2 – Mô hình thông tin và đánh giá với hai đối chứng (Mục tiêu 2)

Chuyên đề thứ hai đặc tả mô hình thông tin, viết công cụ kiểm năm ràng buộc và logic bốn mức, mã hóa hồ sơ B0, dựng B1, khóa các tiêu chí ở Bước kiểm chứng 2, rồi đo theo Bước kiểm chứng 3 để hình thành Bài báo 2. Bước này dùng BIM nhà xưởng thật và một tập bằng chứng của Mục tiêu 1, nên không chờ thời gian quan trắc của Mục tiêu 3.

### 5.9.3. Định hướng 3 – Triển khai trên nhà xưởng thật (Mục tiêu 3)

Khảo sát nhà xưởng, chọn vị trí cảm biến, thu hồ sơ B0 và trao đổi với người quản lý kiểm tra – bảo trì làm song song với Định hướng 1, trên cơ sở thỏa thuận với chủ đầu tư. Sau khi có mô hình thông tin của Định hướng 2, chuỗi được triển khai theo Bước kiểm chứng 4. Bất thường trong dữ liệu vận hành là căn cứ đề nghị kiểm tra; kết quả kiểm tra của kỹ sư được ghi làm nhãn hiện trường và bản ghi kiểm tra.

## 5.10. Tổng hợp chương

Tiểu luận cho thấy các thành phần kỹ thuật chính của bài toán đều đã có nền nghiên cứu: dữ liệu dao động và học máy cho theo dõi trạng thái; nguyên tắc về đơn vị độc lập, rò rỉ dữ liệu và đánh giá theo nhóm; liên kết cảm biến với BIM; IFC 4.3 và BCF 3.0 cho chuỗi kiểm tra – cấu kiện – hành động; nguồn gốc dữ liệu và con người trong quy trình. Khoảng trống của luận án vì vậy được xác lập ở điểm nối giữa các thành phần đó.

Hai khoảng trống còn lại sau khi đối chiếu tiền lệ là: bằng chứng trạng thái có phạm vi hiệu lực, gồm vế đánh giá và vế khai báo (khoảng trống A); và từ bằng chứng đến hành động có trách nhiệm (khoảng trống B). Cả hai được phát biểu trong phạm vi tập tài liệu đã rà soát.

Ba mục tiêu ứng với ba câu hỏi nghiên cứu và hai bài báo: Mục tiêu 1 đo mức lạc quan của đánh giá cùng lần chạy so với đánh giá giữ lại lần chạy và giữ lại đợt, và khai báo phạm vi hiệu lực trên khung thép 1:10 (Bài báo 1); Mục tiêu 2 xây dựng mô hình thông tin mở rộng IFC 4.3 và BCF 3.0, đánh giá so với hồ sơ hiện hành và với mô hình chỉ dùng chuẩn sẵn có (Bài báo 2); Mục tiêu 3 kiểm chứng khả thi của chuỗi trên một nhà xưởng thật có BIM. Hệ thống được khai báo ở mức bóng số theo \[8\].

Sau Tiểu luận, nghiên cứu chuyển từ xác lập khoảng trống sang kiểm chứng theo trình tự ba mục tiêu, giữ định vị Quản lý xây dựng:

Quản lý, liên kết và truy vết thông tin kỹ thuật để hỗ trợ kiểm tra – bảo trì một cách minh bạch và có thể kiểm chứng.
