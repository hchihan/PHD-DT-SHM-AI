# CHƯƠNG 2. TỔNG QUAN VỀ QUẢN LÝ TÀI SẢN VÀ SONG SINH SỐ TRONG GIAI ĐOẠN VẬN HÀNH

## 2.1. Quản lý tài sản và thông tin công trình trong giai đoạn vận hành

### 2.1.1. Nhà công nghiệp khung thép như một tài sản vận hành

Nhà công nghiệp khung thép được thiết kế và nghiệm thu tại một thời điểm nhưng được khai thác lâu dài dưới điều kiện vận hành và môi trường thay đổi. Trong suốt thời gian đó, chủ sở hữu hoặc đơn vị quản lý phải trả lời lặp lại một tập câu hỏi: cấu kiện nào cần kiểm tra, khi nào, bằng chứng nào làm phát sinh nhu cầu kiểm tra, ai thực hiện, kết quả ghi ở đâu và hành động tiếp theo đang ở trạng thái nào.

ISO 19650-3:2020 coi quản lý thông tin trong giai đoạn vận hành là một phần riêng của vòng đời tài sản, với trọng tâm là duy trì thông tin cần cho khai thác và quản lý \[1\]. Theo cách nhìn này, mô hình số, hồ sơ kiểm tra, dữ liệu vận hành và lịch sử bảo trì là thành phần của một hệ thống thông tin tài sản chứ không phải những tệp độc lập.

Ở cấp tổ chức, bộ tiêu chuẩn ISO 55000 cung cấp thuật ngữ, tổng quan và nguyên tắc của quản lý tài sản; ấn bản hiện hành là ISO 55000:2024, thay ấn bản năm 2014 \[@8PB7EN2E\]. Tiểu luận dùng ISO 55000:2024 làm khung tham chiếu cho quản lý tài sản và ISO 19650-3:2020 làm khung cho quản lý thông tin trong giai đoạn vận hành; nhà xưởng khung thép được xét như một tài sản mà quyết định kiểm tra – bảo trì cần dựa trên thông tin về tình trạng của nó.
<!-- ISO 55000:2024 chưa tiếp cận toàn văn (trang iso.org bị Cloudflare chặn khi kiểm 02/10/2026); chỉ dẫn ở mức tên, phạm vi và ấn bản. Cần NCS cung cấp toàn văn nếu muốn trích nội dung điều khoản. -->

Với nhà công nghiệp khung thép, yêu cầu quản lý thông tin đặc biệt quan trọng vì trạng thái khai thác chịu tác động đồng thời của tải trọng sản xuất, thiết bị, rung động, thay đổi công năng, điều kiện môi trường và lịch sử can thiệp. Những yếu tố này làm cho dữ liệu trạng thái cần được đặt trong bối cảnh thời gian và vận hành thay vì được đọc như một chỉ báo vật lý độc lập. Vì vậy, lịch sử kiểm tra, sửa chữa, điều kiện tiếp xúc và các thay đổi vận hành là thông tin cần được duy trì cùng hồ sơ tài sản.

Hai hướng nghiên cứu song song đã khá trưởng thành. Ở phía quản lý, bảo trì kết cấu thép công nghiệp được tổ chức như một chương trình kiểm tra – bảo trì \[22\]. Ở phía kỹ thuật, quan trắc dài hạn đã chứng minh khả năng thu dữ liệu động lực học liên tục trên kết cấu thép ở quy mô công trình thực, điển hình là hệ thống trên UCLA Factor Building \[23\]. Điều còn thiếu với quản lý tài sản là cách biến dữ liệu kỹ thuật thành thông tin dùng được và truy vết được trong quy trình kiểm tra – bảo trì.

### 2.1.2. Thông tin phục vụ kiểm tra và bảo trì

Ngoài hình học và thuộc tính cố định của cấu kiện, quy trình kiểm tra – bảo trì cần các thông tin theo thời gian: sự kiện làm phát sinh kiểm tra, bản ghi kiểm tra, người thực hiện, kết quả quan sát, hành động được đề xuất, trạng thái xử lý và lịch sử cập nhật. Mô hình thông tin vận hành vì vậy phải tiếp nhận và duy trì được các bản ghi mới trong suốt vòng đời tài sản.

ISO 19650-3:2020 cung cấp khuôn khổ cho việc đó: thông tin được hình thành và trao đổi theo nhu cầu của tổ chức và tài sản \[1\]. Các nghiên cứu áp dụng tiêu chuẩn trong vận hành lại cho thấy khoảng cách giữa nguyên tắc và triển khai: yêu cầu thông tin phải xuất phát từ phía quản lý tài sản, không suy ra được từ mô hình thiết kế \[24\], và nội dung nghiệp vụ vẫn phải được cấu trúc riêng cho từng loại tài sản và mục tiêu sử dụng \[25\]. Tiêu chuẩn tạo khuôn khổ quản trị; công việc thiết kế thông tin vẫn phải làm riêng.

Trong kiểm tra – bảo trì, một thay đổi phát hiện từ dữ liệu vận hành là một **sự kiện kích hoạt thông tin**: nó làm phát sinh nhu cầu rà soát hoặc kiểm tra thêm nhưng tự nó chưa phải kết luận về hư hỏng. Với dữ liệu dao động, một tín hiệu thay đổi có thể là căn cứ để yêu cầu kiểm tra cấu kiện, còn nguyên nhân vật lý phải được xác nhận bằng hoạt động kiểm tra phù hợp.

Cách đặt vấn đề này tách hai lớp công việc. Lớp kỹ thuật tạo bằng chứng từ dữ liệu đo; lớp quản lý tiếp nhận bằng chứng, đặt nó vào bối cảnh tài sản và hồ sơ, rồi quyết định có kiểm tra hay hành động tiếp hay không. Nhờ ranh giới này, một kết quả phân loại từ cảm biến không bị diễn giải quá mức thành chẩn đoán hư hỏng.

### 2.1.3. Sự phân tán dữ liệu và nhu cầu truy vết

Một khó khăn lớn của quản lý vận hành là thông tin về cùng một tài sản thường nằm rải rác ở nhiều hệ thống: dữ liệu cảm biến trong hệ thu nhận, hình học và thuộc tính cấu kiện trong BIM, biên bản kiểm tra trong tệp văn phòng hoặc hệ quản lý bảo trì, lịch sử công việc trong hệ thống quản lý công việc hoặc hồ sơ kỹ thuật. Khi các hệ thống không dùng chung định danh hoặc quan hệ dữ liệu, việc truy ngược một quyết định về căn cứ ban đầu trở nên khó khăn.

Vấn đề nằm ở quan hệ và ngữ cảnh giữa các nguồn nhiều hơn ở khâu lưu trữ. Chính các giải pháp đã đề xuất cho thấy điều này: để nối thông tin công việc quản lý vận hành với đối tượng IFC, Kim và cộng sự (2018) \[6\] phải xây thêm một lớp ngữ nghĩa; để đưa trạng thái hệ tự động hóa tòa nhà vào ngữ cảnh BIM, Quinn và cộng sự (2020) \[26\] phải dựng một cấu trúc dữ liệu liên kết; khi rà soát mức sẵn sàng của BIM và IFC cho tích hợp dữ liệu, Du và cộng sự (2024) \[27\] vẫn ghi nhận các vấn đề về chuyển đổi và biểu diễn dữ liệu động. Trong cả ba trường hợp, phần phải bổ sung là lớp quan hệ.

Hệ quả quản lý của sự phân mảnh là suy giảm khả năng giải trình. Khi có một cảnh báo hoặc một bằng chứng trạng thái, người phụ trách cần xác định nguồn đo, cấu kiện liên quan, hồ sơ kiểm tra gần nhất và trạng thái xử lý; nếu không truy xuất được các quan hệ này, dữ liệu quan trắc khó đi vào quy trình ra quyết định dù hệ cảm biến và thuật toán vẫn chạy tốt. Kamariotis và cộng sự (2022) cũng đặt giá trị của theo dõi trạng thái kết cấu ở tác động của thông tin tới quyết định quản lý \[28\]; Johannes và cộng sự (2021) xem quan hệ giữa tài sản, tình trạng và công việc là thành phần của quản lý bảo trì thông minh \[29\]. Theo đó, **khả năng truy vết** là điều kiện để thông tin kỹ thuật tham gia minh bạch vào quản lý tài sản.

## 2.2. BIM và IFC trong quản lý thông tin vận hành

### 2.2.1. BIM và mô hình thông tin tài sản

Trong giai đoạn vận hành, BIM không nên chỉ được hiểu là mô hình thiết kế được lưu lại sau khi công trình hoàn thành. Khái niệm **mô hình thông tin tài sản** nhấn mạnh rằng mô hình phải phục vụ nhu cầu thông tin của giai đoạn khai thác và được duy trì khi tài sản thay đổi; ISO 19650-3:2020 đặt việc thiết lập và duy trì thông tin tài sản trong một quá trình liên tục của giai đoạn này \[1\].

Hai loại mô hình khác nhau ở một điểm có ý nghĩa trực tiếp với kiểm tra – bảo trì. Mô hình thiết kế mô tả hình học và thuộc tính tại một thời điểm; mô hình thông tin tài sản phải gắn được với thông tin phát sinh theo thời gian như kiểm tra, thay thế, sửa chữa, thay đổi thiết bị hay cập nhật hiện trạng. Giá trị của BIM trong vận hành vì vậy phụ thuộc vào khả năng duy trì quan hệ thông tin nhiều hơn vào độ chi tiết hình học, và yêu cầu này phức tạp hơn hẳn giai đoạn chuyển giao \[30\]. Khi Carvalho và cộng sự (2023) đề xuất cấu trúc thông tin bảo trì gồm mã cấu kiện, loại hoạt động, lịch, đơn vị chịu trách nhiệm và chi phí, điều kiện tiên quyết vẫn là đối tượng và bản ghi có định danh đủ rõ để liên kết qua thời gian và qua hệ thống \[31\].

### 2.2.2. IFC và định danh cấu kiện

IFC cung cấp một lược đồ mở để trao đổi dữ liệu BIM giữa các công cụ và là nền kỹ thuật quan trọng cho việc liên kết thông tin vận hành với cấu kiện. Trong IFC, các đối tượng kế thừa từ *IfcRoot* sử dụng *GlobalId* làm định danh toàn cục, tạo một điểm neo để nối thông tin từ các hệ thống bên ngoài về đúng đối tượng BIM.

Giá trị của định danh vượt ra ngoài việc tìm đúng cấu kiện trên mô hình. Một định danh dùng được xuyên hệ thống cho phép các bản ghi khác nhau (dữ liệu cảm biến, hồ sơ kiểm tra, công việc bảo trì) tham chiếu tới cùng một đối tượng mà không dựa vào tên gọi thủ công. Đây là điều kiện cần cho những truy vấn quản lý như “các bằng chứng nào đã được ghi cho cấu kiện này?” hoặc “hồ sơ kiểm tra nào liên quan tới cảnh báo này?”.

Lớp liên kết này đã có nền kỹ thuật tương đối rõ, thể hiện qua ba cách tiếp cận bổ sung cho nhau: mở rộng chính lược đồ IFC để mô hình hóa các thành phần của hệ theo dõi trạng thái cùng quan hệ của chúng với cấu kiện chịu lực \[2\]; ánh xạ định danh giữa BIM và thiết bị cảm biến để hỗ trợ tích hợp dữ liệu \[4\]; và dùng *GlobalId* làm khóa nối cơ sở dữ liệu IFC với dữ liệu chuỗi thời gian nhằm truy xuất theo đối tượng \[5\].

### 2.2.2A. Chuẩn biểu diễn vấn đề, yêu cầu và hành động bảo trì

<!-- Nhãn tạm 2.2.2A; đánh số lại ở GĐ5. Tiền lệ bắt buộc nêu theo CLAUDE.md 6.1 (BCF 3.0, IFC4, [35]); nội dung theo revision/GD2_nhat_ky_khoang_trong.md (kiểm 30/09/2026) và mapping/bellon2025.md. -->

Ngoài định danh cấu kiện, các chuẩn openBIM đã có cách biểu diễn cho vấn đề, yêu cầu và hành động bảo trì. Ba tiền lệ dưới đây là nền mà mô hình thông tin của luận án mở rộng (mục 5.5).

Thứ nhất, IFC4 có nhóm thực thể điều khiển cho quản lý vận hành. `IfcActionRequest` biểu diễn yêu cầu hành động, kể cả báo hỏng cho bảo trì, có trường trạng thái và gán được người yêu cầu, người thực hiện; `IfcProjectOrder` loại lệnh công việc bảo trì và `IfcTask` cũng mang trạng thái; `IfcApproval` ghi trạng thái phê duyệt, thời điểm, người đề nghị và người phê duyệt, kể cả phê duyệt nhiều cấp; `IfcPerformanceHistory` ghi dữ liệu đo theo thời gian từ hệ tự động hóa tòa nhà và gán được cho sản phẩm \[CẦN NGUỒN: IFC4 ADD2 TC1\]. Trường trạng thái lưu giá trị hiện tại, còn `IfcOwnerHistory` lưu lần sửa cuối của đối tượng.

Thứ hai, Bellon và cộng sự (2025) dùng các thực thể chuẩn của IFC 4.3 để biểu diễn chuỗi lần kiểm tra – hư hỏng – cấu kiện – nhiệm vụ bảo trì – chi phí cho hư hỏng phát hiện bằng mắt: lần kiểm tra là một `IfcTask` loại kiểm tra, hư hỏng là sản phẩm của lần kiểm tra qua `IfcRelAssignsToProduct`, hư hỏng gắn vào cấu kiện qua `IfcRelAdheresToElement`, và nhiệm vụ bảo trì nhận hư hỏng qua `IfcRelAssignsToProcess` \[35\] (tr. 4–7, 9). Đây là tiền lệ gần nhất của chuỗi kiểm tra – cấu kiện – hành động bằng thực thể chuẩn.

Thứ ba, BIM Collaboration Format (BCF) 3.0 của buildingSMART biểu diễn vấn đề trao đổi giữa các bên trên mô hình. Mỗi vấn đề có trạng thái và loại lấy từ danh sách của dự án, người tạo và thời điểm tạo, các bình luận có tác giả và ngày; cấu kiện liên quan được chỉ qua góc nhìn mang `IfcGuid` (BCF-XML, mục Topic, Comment, Components). Giao diện lập trình BCF-API 3.0 có dịch vụ sự kiện của vấn đề, mỗi lần đổi trạng thái hay người được giao sinh một sự kiện có ngày, tác giả và giá trị mới, nhằm giữ lịch sử đầy đủ; máy chủ có thể giới hạn thao tác theo người dùng (BCF-API, mục 1.2, 3.1.5, 3.9) \[@K5SGFIGW\].

Ba tiền lệ cho thấy trạng thái, phê duyệt, lịch sử đổi trạng thái và liên kết vấn đề với cấu kiện đã có chuẩn biểu diễn. Phần mà luận án bổ sung nằm ở chỗ nối các cấu trúc đó với bằng chứng tình trạng: quan hệ định kiểu từ yêu cầu hay hành động về bằng chứng đã làm phát sinh nó, nguồn gốc và phạm vi hiệu lực của bằng chứng, và căn cứ cùng vai trò chuyên môn của từng lần đổi trạng thái. Theo nhận định của nghiên cứu sinh, trong IFC4 cả yêu cầu hành động lẫn lịch sử đo đều là lớp con của `IfcControl`, và quan hệ gán điều khiển cho điều khiển bị loại trừ, nên chưa có quan hệ định kiểu từ yêu cầu về dữ liệu quan trắc làm căn cứ. Hai khoảng trống tương ứng được phát biểu ở mục 5.2.

### 2.2.3. Giới hạn của định danh và mô hình thông tin

Định danh đúng vẫn chưa đồng nghĩa với truy vết đầy đủ, vì ba lý do.

Thứ nhất, định danh phải được duy trì trong bối cảnh mô hình và hệ thống thay đổi. Việc kiểm tra quy tắc và tính hợp lệ của trao đổi BIM có thể thực hiện ở mức lược đồ và dữ liệu \[32\], nhưng tính đúng bên trong một tệp không tự bảo đảm tính liên tục của định danh qua các phiên bản hoặc qua các công cụ khác nhau. Các nghiên cứu về so sánh phiên bản và quản trị thay đổi BIM cho thấy định danh đối tượng qua vòng đời là một vấn đề riêng cần được xử lý \[33\].

Thứ hai, các hệ thống vận hành không nhất thiết dùng chung một khóa. Kim và cộng sự (2018) phải bổ sung một lớp liên kết giữa dữ liệu công việc và đối tượng IFC, và trong thực hành quản lý cơ sở, các mã tài sản đọc được bởi con người vẫn thường tồn tại song song với *GlobalId* của mô hình IFC \[6\]. Kiến trúc dữ liệu vì vậy cần chấp nhận việc ánh xạ giữa nhiều hệ định danh thay vì giả định một mã duy nhất giải quyết toàn bộ bài toán.

Thứ ba, một hồ sơ kiểm tra hoặc một hành động bảo trì không phải thuộc tính tĩnh của cấu kiện mà là bản ghi có thời điểm, người tạo, trạng thái và quan hệ với các sự kiện trước – sau. Các nghiên cứu gần đây về BIM cho kiểm tra và bảo trì đã bắt đầu mô hình hóa các thực thể như khiếm khuyết, hoạt động sửa chữa và trạng thái xử lý \[34\]–\[36\], cho thấy BIM/IFC là nền định danh quan trọng nhưng chưa đủ: phục vụ quản lý tài sản còn cần thêm cấu trúc bản ghi và quan hệ theo thời gian.

Kết luận trung gian: **BIM và IFC tạo nền để nhận diện và liên kết tài sản, nhưng khả năng truy vết vận hành đòi hỏi thêm quan hệ dữ liệu, lịch sử bản ghi, nguồn gốc thông tin và quy tắc kiểm tra tính toàn vẹn**. Chuỗi truy vết được tổng hợp chi tiết ở Chương 4.

## 2.3. Song sinh số trong xây dựng và quản lý tài sản

### 2.3.1. Khái niệm và mức năng lực của Song sinh số

Thuật ngữ **Song sinh số** (Digital Twin), còn gọi là Song sinh kỹ thuật số hay bản sao số, được dùng với nội hàm chưa thống nhất giữa các lĩnh vực. Một số cách tiếp cận nhấn mạnh bản sao số gắn với tài sản vật lý và được cập nhật bằng dữ liệu; số khác yêu cầu trao đổi dữ liệu tự động hai chiều, mô phỏng và khả năng tác động ngược. Khi dùng thuật ngữ này trong quản lý tài sản xây dựng, cần nói rõ chức năng nào được triển khai và mức năng lực nào thực sự đạt được.

Kritzinger và cộng sự (2018) đề xuất phân biệt ba mức dựa trên mức tự động hóa của luồng dữ liệu giữa đối tượng vật lý và đối tượng số: **Mô hình số** (Digital Model), **Bóng số** (Digital Shadow) và **Song sinh số** (Digital Twin) \[8\]. Điểm mạnh của cách phân loại này là làm rõ rằng “có mô hình số” và “có dữ liệu cảm biến” chưa đủ để suy ra cùng một mức tích hợp. Sepasgozar (2021) đưa vấn đề vào môi trường xây dựng và nhấn mạnh vai trò của trao đổi dữ liệu, khả năng tương tác và mức tự chủ trong việc phân biệt Song sinh số với các hệ thống BIM hoặc giám sát thông thường \[9\].

<span id="TLTQ_Bang_2_1" class="anchor"></span>Bảng 2.1. Phân biệt ba mức theo luồng dữ liệu

| **Mức** | **Đặc trưng luồng dữ liệu** | **Ý nghĩa điển hình trong vận hành** |
|:--:|:---|:---|
| Mô hình số | Dữ liệu được trao đổi chủ yếu bằng thao tác thủ công | Mô hình hồ sơ, tra cứu tài sản |
| Bóng số | Dữ liệu từ tài sản vật lý cập nhật tự động sang mô hình số | Quan trắc và theo dõi trạng thái |
| Song sinh số | Có cơ chế phản hồi và tương tác hai chiều ở mức hệ thống | Hỗ trợ vận hành thích ứng, điều khiển hoặc vòng phản hồi quản lý tùy phạm vi |

Phân loại theo luồng dữ liệu không phải cách duy nhất. Chen và cộng sự (2021) phát triển mô hình trưởng thành Song sinh số nhiều chiều cho quản lý tài sản, cho thấy một dự án có thể mạnh ở một số năng lực và yếu ở năng lực khác, điều mà thang đo một chiều không biểu diễn được \[10\]. Davila Delgado và cộng sự (2021) lưu ý rằng các mô hình Song sinh số phát triển trong sản xuất không chuyển nguyên trạng sang xây dựng mà phải điều chỉnh theo đặc thù vòng đời, dữ liệu và quá trình quản lý tài sản \[37\].

Vì vậy, thay vì coi Song sinh số là nhãn nhị phân “có hoặc không”, Tiểu luận xem nó như một kiến trúc gồm nhiều năng lực kiểm chứng được riêng: kết nối với tài sản vật lý, cập nhật dữ liệu, liên thông hệ thống, duy trì ngữ cảnh, phản hồi thông tin và hỗ trợ quyết định. Mức năng lực phải được đánh giá trên trường hợp triển khai cụ thể.

### 2.3.2. Song sinh số dựa trên dữ liệu trong quản lý tài sản

Nhiều triển khai Song sinh số trong quản lý tài sản xây dựng phát triển từ việc kết hợp BIM với dữ liệu vận hành; điểm chung của chúng nằm ở lớp tổ chức dữ liệu hơn là ở mức tự chủ: dùng mô hình số cùng định danh tài sản để tích hợp dữ liệu ở cấp tòa nhà và khuôn viên \[38\]; tích hợp BIM với dữ liệu thiết bị và Internet vạn vật \[4\]; nối IFC với dữ liệu chuỗi thời gian để truy xuất giá trị hiện tại và lịch sử theo đối tượng \[5\]; hoặc tích hợp BIM với Song sinh số trong một hệ giám sát bảo trì có cảnh báo \[39\].

Giá trị thực tế của Song sinh số trong vận hành thường xuất hiện trước hết ở **tổ chức dữ liệu theo tài sản**: đưa dữ liệu hiện trường về đúng đối tượng, duy trì lịch sử và cho phép truy xuất theo ngữ cảnh. Các tổng quan gần đây ghi nhận lợi ích tiềm năng cho vận hành và bảo trì, đồng thời chỉ ra các rào cản lặp lại về phân mảnh dữ liệu, chuẩn hóa và khả năng liên thông \[40\], \[41\]

Boje và cộng sự (2020) cho rằng BIM cần được mở rộng về ngữ nghĩa và dữ liệu động để tiến tới các kiến trúc Song sinh số trong xây dựng \[7\]. Quản lý tài sản cần đúng điều đó: ngoài hình học và thuộc tính tĩnh, hệ thống phải tiếp nhận dữ liệu động, sự kiện, lịch sử và quan hệ với quá trình quản lý. Khái niệm **Song sinh số dựa trên dữ liệu** trong nghiên cứu này được hiểu theo hướng ưu tiên kết nối dữ liệu thực với ngữ cảnh tài sản và duy trì một dòng thông tin truy vết được phục vụ kiểm tra – bảo trì.

“Dựa trên dữ liệu” không có nghĩa dữ liệu tự đưa ra kết luận kỹ thuật. Dữ liệu đo được xử lý thành bằng chứng; bằng chứng được đặt vào bối cảnh cấu kiện và hồ sơ; con người dùng nó cùng các thông tin khác để quyết định kiểm tra hay hành động. Trong quản lý tài sản, mỗi quyết định cần có căn cứ, bối cảnh và người chịu trách nhiệm giải trình.

### 2.3.3. Khả năng liên thông, nguồn gốc dữ liệu và con người trong vòng lặp

Ba năng lực có ý nghĩa đặc biệt đối với Song sinh số phục vụ quản lý tài sản là **khả năng liên thông**, **nguồn gốc dữ liệu** và **con người trong vòng lặp**.

Khả năng liên thông cho phép dữ liệu từ các hệ thống khác nhau được kết nối theo cùng ngữ cảnh tài sản. IFC cung cấp nền lược đồ cho BIM, nhưng dữ liệu vận hành, dữ liệu cảm biến và dữ liệu quy trình thường nằm ngoài mô hình gốc. Ramonell và cộng sự (2023) cho thấy đồ thị tri thức có thể hợp nhất BIM, siêu dữ liệu thiết bị và thông tin quy trình trong một cấu trúc tích hợp cho Song sinh số của tài sản xây dựng \[42\]; kiến trúc Song sinh số vì vậy cần một lớp liên kết dữ liệu nằm ngoài mô hình hình học.

Nguồn gốc dữ liệu cho biết một thông tin đến từ đâu, được tạo thế nào, bởi ai hoặc bởi quá trình nào và đã qua những biến đổi gì. Tavakoli và cộng sự (2023) nhấn mạnh vai trò của nguồn gốc dữ liệu đối với độ tin cậy của Song sinh số trong quản lý tài sản \[43\]; García và cộng sự (2026) cho thấy giá trị của việc lưu bằng chứng kiểm soát chất lượng và quyết định công bố dữ liệu ở cấp quản trị thông tin \[44\]. Với nghiên cứu dựa trên cảm biến, cùng một giá trị dự đoán có thể mang ý nghĩa khác nhau nếu được sinh ra từ cấu hình cảm biến, đợt đo hoặc giao thức đánh giá khác nhau.

Con người trong vòng lặp giữ cho hỗ trợ quyết định không bị đồng nhất với quyết định tự động. Wu, El-Assady và De Wolf (2026) phát triển một khung tăng cường trí tuệ cho kiểm kê công trình, trong đó chuyên gia rà soát và tương tác với kết quả \[17\]; ở góc độ quản lý bảo trì, Johannes và cộng sự (2021) nhấn mạnh quản trị con người cùng quan hệ giữa tài sản, tình trạng và công việc \[29\]. Với kiểm tra – bảo trì công trình, hệ thống số tổ chức và trình bày căn cứ, còn quyết định quản lý gắn với người hoặc vai trò có thẩm quyền.

Khi kết hợp với định danh tài sản và dữ liệu vận hành, ba năng lực này (liên thông để các hệ thống trao đổi được dữ liệu, nguồn gốc để thông tin kiểm lại được, con người trong vòng lặp để quyết định có người chịu trách nhiệm) giúp Song sinh số vượt khỏi vai trò trực quan hóa và trở thành hạ tầng thông tin cho quản lý tài sản.

## 2.4. Hàm ý lý luận đối với trục nghiên cứu

Từ các nhóm tài liệu trên có thể rút ra bốn hàm ý lý luận.

Đối tượng cần quản lý gồm cấu kiện và thông tin phát sinh quanh cấu kiện theo thời gian. Một cấu kiện có thể được nhận diện trong BIM, nhưng để phục vụ vận hành nó cần gắn với dữ liệu đo, sự kiện, hồ sơ kiểm tra và lịch sử hành động. Trọng tâm vì thế dịch từ mô hình hóa hình học sang quản lý thông tin tài sản.

Dữ liệu cảm biến chỉ có giá trị quản lý khi được đặt trong ngữ cảnh và truy về được nguồn. Liên kết với BIM cho biết dữ liệu thuộc cấu kiện nào; để dùng làm căn cứ, còn cần biết bằng chứng được tạo dưới điều kiện nào, có hiệu lực tới đâu và đã qua phiên bản xử lý nào (Chương 3).

Khả năng truy vết cần đi xa hơn việc hiển thị dữ liệu trên mô hình. Một hệ thống có thể hiển thị cảm biến hoặc cảnh báo trên BIM mà vẫn chưa trả lời được câu hỏi về hồ sơ kiểm tra, trạng thái xử lý và căn cứ của hành động. Chương 4 vì vậy xét quan hệ thông tin giữa bằng chứng, cấu kiện, hồ sơ và hành động.

Cuối cùng, Song sinh số nên được đánh giá bằng năng lực đã triển khai chứ không bằng tên gọi. Nghiên cứu giữ Song sinh số dựa trên dữ liệu làm **mục tiêu kiến trúc** cho quản lý tài sản; mức năng lực thực tế được đánh giá sau nghiên cứu trường hợp, dựa trên chức năng đã thực hiện và tiêu chí tham chiếu từ các nghiên cứu đã nêu. Nghiên cứu không tự gán trước một mức trưởng thành, và cũng không mặc định rằng BIM cộng cảm biến là đã đạt Song sinh số.

Vòng phản hồi mà nghiên cứu hướng tới trước hết là **vòng phản hồi thông tin trong quản lý tài sản**: dữ liệu từ công trình cập nhật lớp bằng chứng; kết quả kiểm tra và trạng thái hành động được ghi trở lại hồ sơ số; các bản ghi đó trở thành bối cảnh cho lần đánh giá tiếp theo. Mức độ vòng phản hồi này đáp ứng các tiêu chí Song sinh số sẽ được kiểm chứng ở nghiên cứu trường hợp.

Mô hình phần tử hữu hạn không bắt buộc cho định vị này; trong phạm vi nghiên cứu, nó chỉ là **mô hình danh nghĩa, chưa hiệu chuẩn, dùng để tham chiếu và không dùng cho chẩn đoán hư hỏng** (mục 5.8.3).

## 2.5. Tổng hợp chương

Chương 2 cho thấy quản lý nhà công nghiệp khung thép trong giai đoạn vận hành là bài toán quản lý thông tin theo thời gian. Chủ sở hữu cần biết dữ liệu thuộc cấu kiện nào, được tạo trong hoàn cảnh nào, gắn với hồ sơ nào và đã dẫn tới hành động gì. Sự phân tán giữa hệ cảm biến, BIM và hồ sơ bảo trì làm suy giảm khả năng truy vết và giải trình của quá trình ra quyết định.

BIM và IFC là nền cho định danh cấu kiện và trao đổi thông tin nhưng không tự tạo ra chuỗi truy vết vận hành. Nhiều nghiên cứu đã liên kết cảm biến, dữ liệu vận hành và hồ sơ quản lý với đối tượng BIM, nên tích hợp cảm biến – BIM không còn là điểm mới; giá trị quản lý nằm ở việc duy trì quan hệ và lịch sử của các bản ghi khi thông tin đi qua nhiều hệ thống và nhiều thời điểm.

Các nghiên cứu về Song sinh số mở rộng vấn đề từ mô hình thông tin tĩnh sang kiến trúc có dữ liệu động, liên thông, nguồn gốc dữ liệu và vòng phản hồi, đồng thời cho thấy năng lực của nó phải được đánh giá trên triển khai cụ thể. Tiểu luận giữ Song sinh số dựa trên dữ liệu làm mục tiêu kiến trúc; mức năng lực đạt được sẽ được kiểm chứng trong nghiên cứu trường hợp.

Kết luận của chương là để dữ liệu kỹ thuật tham gia được vào kiểm tra – bảo trì, cần chuyển từ **dữ liệu** sang **bằng chứng có bối cảnh**, từ **định danh cấu kiện** sang **quan hệ truy vết**, và từ **cảnh báo** sang **hồ sơ và hành động có căn cứ**.

Bước chuyển thứ nhất đặt ra câu hỏi mà chương này chưa trả lời: nếu bằng chứng chỉ có giá trị quản lý khi mang theo bối cảnh và phạm vi hiệu lực của nó, thì điều kiện nào khiến một kết quả từ dữ liệu dao động có đủ các thuộc tính ấy? Chương 3 trả lời câu hỏi này; Chương 4 xét cách bằng chứng được liên kết tới cấu kiện, hồ sơ kiểm tra và hành động.
