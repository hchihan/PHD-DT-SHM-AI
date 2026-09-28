**ĐẠI HỌC ĐÀ NẴNG**

TRƯỜNG ĐẠI HỌC BÁCH KHOA

**TIỂU LUẬN TỔNG QUAN**

**TỔNG QUAN VỀ HỆ THỐNG SONG SINH KỸ THUẬT SỐ DỰA TRÊN DỮ LIỆU TRONG GIÁM SÁT TRẠNG THÁI VÀ HỖ TRỢ KIỂM TRA - BẢO TRÌ CÔNG TRÌNH CÔNG NGHIỆP KHUNG THÉP**

**Ngành: Quản lý xây dựng**

**Mã ngành: 7580302**

**Nghiên cứu sinh: HỒ CHÍ HÂN**

**Người hướng dẫn khoa học:**

**PGS.TS NGÔ NGỌC TRI**

**PGS.TS PHẠM ANH ĐỨC**

Đà Nẵng, tháng 09 năm 2026

MỤC LỤC

[DẪN NHẬP [13](#dẫn-nhập)](#dẫn-nhập)

[CHƯƠNG 1. GIỚI THIỆU VÀ PHƯƠNG PHÁP TỔNG QUAN [15](#chương-1.-giới-thiệu-và-phương-pháp-tổng-quan)](#chương-1.-giới-thiệu-và-phương-pháp-tổng-quan)

[1.1. Bối cảnh nghiên cứu [15](#bối-cảnh-nghiên-cứu)](#bối-cảnh-nghiên-cứu)

[1.1.1. Bối cảnh vận hành nhà công nghiệp khung thép [15](#bối-cảnh-vận-hành-nhà-công-nghiệp-khung-thép)](#bối-cảnh-vận-hành-nhà-công-nghiệp-khung-thép)

[1.1.2. Chuyển đổi số trong quản lý vận hành [15](#chuyển-đổi-số-trong-quản-lý-vận-hành)](#chuyển-đổi-số-trong-quản-lý-vận-hành)

[1.1.3. Song sinh số như mục tiêu kiến trúc của nghiên cứu [16](#song-sinh-số-như-mục-tiêu-kiến-trúc-của-nghiên-cứu)](#song-sinh-số-như-mục-tiêu-kiến-trúc-của-nghiên-cứu)

[1.1.4. Bối cảnh quản lý bảo trì và mô hình thông tin công trình tại Việt Nam [17](#bối-cảnh-quản-lý-bảo-trì-và-mô-hình-thông-tin-công-trình-tại-việt-nam)](#bối-cảnh-quản-lý-bảo-trì-và-mô-hình-thông-tin-công-trình-tại-việt-nam)

[1.2. Vấn đề nghiên cứu [17](#vấn-đề-nghiên-cứu)](#vấn-đề-nghiên-cứu)

[1.2.1. Vấn đề quản lý trung tâm [17](#vấn-đề-quản-lý-trung-tâm)](#vấn-đề-quản-lý-trung-tâm)

[1.2.2. Từ kết quả phân loại đến bằng chứng trạng thái [18](#từ-kết-quả-phân-loại-đến-bằng-chứng-trạng-thái)](#từ-kết-quả-phân-loại-đến-bằng-chứng-trạng-thái)

[1.2.3. Từ định danh cấu kiện đến truy vết thông tin [19](#từ-định-danh-cấu-kiện-đến-truy-vết-thông-tin)](#từ-định-danh-cấu-kiện-đến-truy-vết-thông-tin)

[1.2.4. Từ bằng chứng đến hỗ trợ hành động có thể giải trình [19](#từ-bằng-chứng-đến-hỗ-trợ-hành-động-có-thể-giải-trình)](#từ-bằng-chứng-đến-hỗ-trợ-hành-động-có-thể-giải-trình)

[1.2.5. Chuỗi nghiên cứu [20](#chuỗi-nghiên-cứu)](#chuỗi-nghiên-cứu)

[1.3. Sự cần thiết của nghiên cứu [20](#sự-cần-thiết-của-nghiên-cứu)](#sự-cần-thiết-của-nghiên-cứu)

[1.3.1. Cần nâng chất lượng của kết quả phân loại thành chất lượng của bằng chứng [20](#cần-nâng-chất-lượng-của-kết-quả-phân-loại-thành-chất-lượng-của-bằng-chứng)](#cần-nâng-chất-lượng-của-kết-quả-phân-loại-thành-chất-lượng-của-bằng-chứng)

[1.3.2. Cần chuyển từ tích hợp phần mềm sang truy vết có thể kiểm tra [21](#cần-chuyển-từ-tích-hợp-phần-mềm-sang-truy-vết-có-thể-kiểm-tra)](#cần-chuyển-từ-tích-hợp-phần-mềm-sang-truy-vết-có-thể-kiểm-tra)

[1.3.3. Cần phân biệt bằng chứng phòng thí nghiệm với khả năng áp dụng trong bối cảnh thực tế [21](#cần-phân-biệt-bằng-chứng-phòng-thí-nghiệm-với-khả-năng-áp-dụng-trong-bối-cảnh-thực-tế)](#cần-phân-biệt-bằng-chứng-phòng-thí-nghiệm-với-khả-năng-áp-dụng-trong-bối-cảnh-thực-tế)

[1.3.4. Cần một kiến trúc Song sinh số bám theo quá trình quản lý [21](#cần-một-kiến-trúc-song-sinh-số-bám-theo-quá-trình-quản-lý)](#cần-một-kiến-trúc-song-sinh-số-bám-theo-quá-trình-quản-lý)

[1.4. Mục tiêu của Tiểu luận tổng quan [22](#mục-tiêu-của-tiểu-luận-tổng-quan)](#mục-tiêu-của-tiểu-luận-tổng-quan)

[1.4.1. Mục tiêu tổng quát [22](#mục-tiêu-tổng-quát)](#mục-tiêu-tổng-quát)

[1.4.2. Mục tiêu cụ thể [22](#mục-tiêu-cụ-thể)](#mục-tiêu-cụ-thể)

[1.5. Đối tượng và phạm vi tổng quan [23](#đối-tượng-và-phạm-vi-tổng-quan)](#đối-tượng-và-phạm-vi-tổng-quan)

[1.5.1. Đối tượng tổng quan [23](#đối-tượng-tổng-quan)](#đối-tượng-tổng-quan)

[1.5.2. Phạm vi của Tiểu luận tổng quan [23](#phạm-vi-của-tiểu-luận-tổng-quan)](#phạm-vi-của-tiểu-luận-tổng-quan)

[1.5.3. Bốn loại bằng chứng [23](#bốn-loại-bằng-chứng)](#bốn-loại-bằng-chứng)

[1.6. Phương pháp thực hiện tổng quan [24](#phương-pháp-thực-hiện-tổng-quan)](#phương-pháp-thực-hiện-tổng-quan)

[1.6.1. Cách tiếp cận [24](#cách-tiếp-cận)](#cách-tiếp-cận)

[1.6.2. Các nhóm chủ đề [24](#các-nhóm-chủ-đề)](#các-nhóm-chủ-đề)

[1.6.3. Kiểm soát mức bằng chứng của nguồn tài liệu [25](#kiểm-soát-mức-bằng-chứng-của-nguồn-tài-liệu)](#kiểm-soát-mức-bằng-chứng-của-nguồn-tài-liệu)

[1.6.4. Cách xử lý khoảng trống nghiên cứu [25](#cách-xử-lý-khoảng-trống-nghiên-cứu)](#cách-xử-lý-khoảng-trống-nghiên-cứu)

[1.6.5. Nguồn tài liệu, chiến lược khảo sát và quy trình lựa chọn nghiên cứu [25](#nguồn-tài-liệu-chiến-lược-khảo-sát-và-quy-trình-lựa-chọn-nghiên-cứu)](#nguồn-tài-liệu-chiến-lược-khảo-sát-và-quy-trình-lựa-chọn-nghiên-cứu)

[1.7. Câu hỏi nghiên cứu và logic nghiên cứu [30](#câu-hỏi-nghiên-cứu-và-logic-nghiên-cứu)](#câu-hỏi-nghiên-cứu-và-logic-nghiên-cứu)

[1.7.1. Câu hỏi nghiên cứu [30](#câu-hỏi-nghiên-cứu)](#câu-hỏi-nghiên-cứu)

[1.7.2. Logic kế tiếp giữa ba câu hỏi [30](#logic-kế-tiếp-giữa-ba-câu-hỏi)](#logic-kế-tiếp-giữa-ba-câu-hỏi)

[1.7.3. Quan hệ với các gói công việc và thiết kế kiểm chứng [31](#quan-hệ-với-các-gói-công-việc-và-thiết-kế-kiểm-chứng)](#quan-hệ-với-các-gói-công-việc-và-thiết-kế-kiểm-chứng)

[1.8. Kiến trúc nghiên cứu tổng thể [31](#kiến-trúc-nghiên-cứu-tổng-thể)](#kiến-trúc-nghiên-cứu-tổng-thể)

[1.8.1. Bốn lớp và chuỗi định danh [31](#bốn-lớp-và-chuỗi-định-danh)](#bốn-lớp-và-chuỗi-định-danh)

[1.8.2. Định vị Song sinh số trong kiến trúc [31](#định-vị-song-sinh-số-trong-kiến-trúc)](#định-vị-song-sinh-số-trong-kiến-trúc)

[1.9. Cấu trúc của Tiểu luận tổng quan [32](#cấu-trúc-của-tiểu-luận-tổng-quan)](#cấu-trúc-của-tiểu-luận-tổng-quan)

[CHƯƠNG 2. TỔNG QUAN VỀ QUẢN LÝ TÀI SẢN VÀ SONG SINH SỐ TRONG GIAI ĐOẠN VẬN HÀNH [33](#chương-2.-tổng-quan-về-quản-lý-tài-sản-và-song-sinh-số-trong-giai-đoạn-vận-hành)](#chương-2.-tổng-quan-về-quản-lý-tài-sản-và-song-sinh-số-trong-giai-đoạn-vận-hành)

[2.1. Quản lý tài sản và thông tin công trình trong giai đoạn vận hành [33](#quản-lý-tài-sản-và-thông-tin-công-trình-trong-giai-đoạn-vận-hành)](#quản-lý-tài-sản-và-thông-tin-công-trình-trong-giai-đoạn-vận-hành)

[2.1.1. Nhà công nghiệp khung thép như một tài sản vận hành [33](#nhà-công-nghiệp-khung-thép-như-một-tài-sản-vận-hành)](#nhà-công-nghiệp-khung-thép-như-một-tài-sản-vận-hành)

[2.1.2. Thông tin phục vụ kiểm tra và bảo trì [33](#thông-tin-phục-vụ-kiểm-tra-và-bảo-trì)](#thông-tin-phục-vụ-kiểm-tra-và-bảo-trì)

[2.1.3. Sự phân tán dữ liệu và nhu cầu truy vết [34](#sự-phân-tán-dữ-liệu-và-nhu-cầu-truy-vết)](#sự-phân-tán-dữ-liệu-và-nhu-cầu-truy-vết)

[2.2. BIM và IFC trong quản lý thông tin vận hành [35](#bim-và-ifc-trong-quản-lý-thông-tin-vận-hành)](#bim-và-ifc-trong-quản-lý-thông-tin-vận-hành)

[2.2.1. BIM và mô hình thông tin tài sản [35](#bim-và-mô-hình-thông-tin-tài-sản)](#bim-và-mô-hình-thông-tin-tài-sản)

[2.2.2. IFC và định danh cấu kiện [35](#ifc-và-định-danh-cấu-kiện)](#ifc-và-định-danh-cấu-kiện)

[2.2.3. Giới hạn của định danh và mô hình thông tin [36](#giới-hạn-của-định-danh-và-mô-hình-thông-tin)](#giới-hạn-của-định-danh-và-mô-hình-thông-tin)

[2.3. Song sinh số trong xây dựng và quản lý tài sản [37](#song-sinh-số-trong-xây-dựng-và-quản-lý-tài-sản)](#song-sinh-số-trong-xây-dựng-và-quản-lý-tài-sản)

[2.3.1. Khái niệm và mức năng lực của Song sinh số [37](#khái-niệm-và-mức-năng-lực-của-song-sinh-số)](#khái-niệm-và-mức-năng-lực-của-song-sinh-số)

[2.3.2. Song sinh số dựa trên dữ liệu trong quản lý tài sản [38](#song-sinh-số-dựa-trên-dữ-liệu-trong-quản-lý-tài-sản)](#song-sinh-số-dựa-trên-dữ-liệu-trong-quản-lý-tài-sản)

[2.3.3. Khả năng liên thông, nguồn gốc dữ liệu và con người trong vòng lặp [38](#khả-năng-liên-thông-nguồn-gốc-dữ-liệu-và-con-người-trong-vòng-lặp)](#khả-năng-liên-thông-nguồn-gốc-dữ-liệu-và-con-người-trong-vòng-lặp)

[2.4. Hàm ý lý luận đối với trục nghiên cứu [39](#hàm-ý-lý-luận-đối-với-trục-nghiên-cứu)](#hàm-ý-lý-luận-đối-với-trục-nghiên-cứu)

[2.5. Tổng hợp chương [40](#tổng-hợp-chương)](#tổng-hợp-chương)

[CHƯƠNG 3. TỔNG QUAN VỀ DỮ LIỆU DAO ĐỘNG VÀ BẰNG CHỨNG TRẠNG THÁI [42](#chương-3.-tổng-quan-về-dữ-liệu-dao-động-và-bằng-chứng-trạng-thái)](#chương-3.-tổng-quan-về-dữ-liệu-dao-động-và-bằng-chứng-trạng-thái)

[3.1. Dữ liệu dao động trong theo dõi trạng thái kết cấu [42](#dữ-liệu-dao-động-trong-theo-dõi-trạng-thái-kết-cấu)](#dữ-liệu-dao-động-trong-theo-dõi-trạng-thái-kết-cấu)

[3.1.1. Theo dõi trạng thái kết cấu dựa trên dao động [42](#theo-dõi-trạng-thái-kết-cấu-dựa-trên-dao-động)](#theo-dõi-trạng-thái-kết-cấu-dựa-trên-dao-động)

[3.1.2. Theo dõi trạng thái liên kết bu lông trong khung thép [42](#theo-dõi-trạng-thái-liên-kết-bu-lông-trong-khung-thép)](#theo-dõi-trạng-thái-liên-kết-bu-lông-trong-khung-thép)

[3.1.3. Phân biệt bằng chứng trạng thái và chẩn đoán hư hỏng [44](#phân-biệt-bằng-chứng-trạng-thái-và-chẩn-đoán-hư-hỏng)](#phân-biệt-bằng-chứng-trạng-thái-và-chẩn-đoán-hư-hỏng)

[3.2. Cảm biến và chuỗi xử lý dữ liệu [44](#cảm-biến-và-chuỗi-xử-lý-dữ-liệu)](#cảm-biến-và-chuỗi-xử-lý-dữ-liệu)

[3.2.1. Loại, số lượng và cấu hình cảm biến [44](#loại-số-lượng-và-cấu-hình-cảm-biến)](#loại-số-lượng-và-cấu-hình-cảm-biến)

[3.2.2. Tiền xử lý, phân đoạn và tạo đầu vào [45](#tiền-xử-lý-phân-đoạn-và-tạo-đầu-vào)](#tiền-xử-lý-phân-đoạn-và-tạo-đầu-vào)

[3.2.3. Học máy và học sâu như công cụ tạo bằng chứng [45](#học-máy-và-học-sâu-như-công-cụ-tạo-bằng-chứng)](#học-máy-và-học-sâu-như-công-cụ-tạo-bằng-chứng)

[3.3. Độ tin cậy của bằng chứng trạng thái [46](#độ-tin-cậy-của-bằng-chứng-trạng-thái)](#độ-tin-cậy-của-bằng-chứng-trạng-thái)

[3.3.1. Đơn vị vật lý độc lập và lặp giả [46](#đơn-vị-vật-lý-độc-lập-và-lặp-giả)](#đơn-vị-vật-lý-độc-lập-và-lặp-giả)

[3.3.2. Rò rỉ dữ liệu và đánh giá theo nhóm [46](#rò-rỉ-dữ-liệu-và-đánh-giá-theo-nhóm)](#rò-rỉ-dữ-liệu-và-đánh-giá-theo-nhóm)

[3.3.3. Đánh giá giữ lại một lần chạy và giữ lại một đợt thí nghiệm [47](#đánh-giá-giữ-lại-một-lần-chạy-và-giữ-lại-một-đợt-thí-nghiệm)](#đánh-giá-giữ-lại-một-lần-chạy-và-giữ-lại-một-đợt-thí-nghiệm)

[3.3.4. Các cơ chế đánh giá bổ trợ [48](#các-cơ-chế-đánh-giá-bổ-trợ)](#các-cơ-chế-đánh-giá-bổ-trợ)

[3.4. Nguồn gốc và phạm vi hiệu lực của bằng chứng trạng thái [48](#nguồn-gốc-và-phạm-vi-hiệu-lực-của-bằng-chứng-trạng-thái)](#nguồn-gốc-và-phạm-vi-hiệu-lực-của-bằng-chứng-trạng-thái)

[3.4.1. Bằng chứng trạng thái như một bản ghi có bối cảnh [48](#bằng-chứng-trạng-thái-như-một-bản-ghi-có-bối-cảnh)](#bằng-chứng-trạng-thái-như-một-bản-ghi-có-bối-cảnh)

[3.4.2. Phạm vi hiệu lực [49](#phạm-vi-hiệu-lực)](#phạm-vi-hiệu-lực)

[3.4.3. Nguồn gốc dữ liệu và khả năng kiểm lại [50](#nguồn-gốc-dữ-liệu-và-khả-năng-kiểm-lại)](#nguồn-gốc-dữ-liệu-và-khả-năng-kiểm-lại)

[3.5. Tổng hợp chương [50](#tổng-hợp-chương-1)](#tổng-hợp-chương-1)

[CHƯƠNG 4. TỔNG QUAN VỀ TRUY VẾT BẰNG CHỨNG VÀ HỖ TRỢ KIỂM TRA – BẢO TRÌ [51](#chương-4.-tổng-quan-về-truy-vết-bằng-chứng-và-hỗ-trợ-kiểm-tra-bảo-trì)](#chương-4.-tổng-quan-về-truy-vết-bằng-chứng-và-hỗ-trợ-kiểm-tra-bảo-trì)

[4.1. Ranh giới khái niệm của truy vết trong quản lý tài sản [51](#ranh-giới-khái-niệm-của-truy-vết-trong-quản-lý-tài-sản)](#ranh-giới-khái-niệm-của-truy-vết-trong-quản-lý-tài-sản)

[4.1.1. Từ hiển thị dữ liệu đến truy vết bằng chứng [51](#từ-hiển-thị-dữ-liệu-đến-truy-vết-bằng-chứng)](#từ-hiển-thị-dữ-liệu-đến-truy-vết-bằng-chứng)

[4.1.2. Cấu kiện, bằng chứng, hồ sơ và hành động là các thực thể khác nhau [52](#cấu-kiện-bằng-chứng-hồ-sơ-và-hành-động-là-các-thực-thể-khác-nhau)](#cấu-kiện-bằng-chứng-hồ-sơ-và-hành-động-là-các-thực-thể-khác-nhau)

[4.2. Tích hợp cảm biến với BIM và IFC [52](#tích-hợp-cảm-biến-với-bim-và-ifc)](#tích-hợp-cảm-biến-với-bim-và-ifc)

[4.2.1. Các cách liên kết cảm biến với cấu kiện [52](#các-cách-liên-kết-cảm-biến-với-cấu-kiện)](#các-cách-liên-kết-cảm-biến-với-cấu-kiện)

[4.2.2. Liên kết cảm biến không đồng nghĩa với liên kết bằng chứng [53](#liên-kết-cảm-biến-không-đồng-nghĩa-với-liên-kết-bằng-chứng)](#liên-kết-cảm-biến-không-đồng-nghĩa-với-liên-kết-bằng-chứng)

[4.2.3. Định danh và tính liên tục qua hệ thống [54](#định-danh-và-tính-liên-tục-qua-hệ-thống)](#định-danh-và-tính-liên-tục-qua-hệ-thống)

[4.3. BIM trong quản lý hồ sơ kiểm tra và bảo trì [54](#bim-trong-quản-lý-hồ-sơ-kiểm-tra-và-bảo-trì)](#bim-trong-quản-lý-hồ-sơ-kiểm-tra-và-bảo-trì)

[4.3.1. Từ biểu diễn khiếm khuyết đến hồ sơ kiểm tra có cấu trúc [54](#từ-biểu-diễn-khiếm-khuyết-đến-hồ-sơ-kiểm-tra-có-cấu-trúc)](#từ-biểu-diễn-khiếm-khuyết-đến-hồ-sơ-kiểm-tra-có-cấu-trúc)

[4.3.2. Hồ sơ khiếm khuyết, sửa chữa và trạng thái hoàn thành [55](#hồ-sơ-khiếm-khuyết-sửa-chữa-và-trạng-thái-hoàn-thành)](#hồ-sơ-khiếm-khuyết-sửa-chữa-và-trạng-thái-hoàn-thành)

[4.3.3. Liên kết BIM với hệ quản lý bảo trì [55](#liên-kết-bim-với-hệ-quản-lý-bảo-trì)](#liên-kết-bim-với-hệ-quản-lý-bảo-trì)

[4.3.4. Từ hồ sơ gắn cấu kiện đến chuỗi thông tin có thể kiểm lại [56](#từ-hồ-sơ-gắn-cấu-kiện-đến-chuỗi-thông-tin-có-thể-kiểm-lại)](#từ-hồ-sơ-gắn-cấu-kiện-đến-chuỗi-thông-tin-có-thể-kiểm-lại)

[4.4. Định danh, nguồn gốc dữ liệu và kiểm chứng quan hệ [56](#định-danh-nguồn-gốc-dữ-liệu-và-kiểm-chứng-quan-hệ)](#định-danh-nguồn-gốc-dữ-liệu-và-kiểm-chứng-quan-hệ)

[4.4.1. Nguồn gốc dữ liệu [56](#nguồn-gốc-dữ-liệu)](#nguồn-gốc-dữ-liệu)

[4.4.2. Phiên bản và lịch sử thông tin [57](#phiên-bản-và-lịch-sử-thông-tin)](#phiên-bản-và-lịch-sử-thông-tin)

[4.4.3. Kiểm chứng quan hệ và dữ liệu không hợp lệ [57](#kiểm-chứng-quan-hệ-và-dữ-liệu-không-hợp-lệ)](#kiểm-chứng-quan-hệ-và-dữ-liệu-không-hợp-lệ)

[4.4.4. Truy vấn hai chiều và truy vết hai chiều [58](#truy-vấn-hai-chiều-và-truy-vết-hai-chiều)](#truy-vấn-hai-chiều-và-truy-vết-hai-chiều)

[4.5. Khả thi hiện trường và hỗ trợ hành động kiểm tra – bảo trì [58](#khả-thi-hiện-trường-và-hỗ-trợ-hành-động-kiểm-tra-bảo-trì)](#khả-thi-hiện-trường-và-hỗ-trợ-hành-động-kiểm-tra-bảo-trì)

[4.5.1. Khả thi triển khai khác với chẩn đoán hiện trường [58](#khả-thi-triển-khai-khác-với-chẩn-đoán-hiện-trường)](#khả-thi-triển-khai-khác-với-chẩn-đoán-hiện-trường)

[4.5.2. Đường cơ sở vận hành và bối cảnh hiện trường [58](#đường-cơ-sở-vận-hành-và-bối-cảnh-hiện-trường)](#đường-cơ-sở-vận-hành-và-bối-cảnh-hiện-trường)

[4.5.3. Con người trong vòng lặp [59](#con-người-trong-vòng-lặp)](#con-người-trong-vòng-lặp)

[4.5.4. Trạng thái hành động và lịch sử xử lý [59](#trạng-thái-hành-động-và-lịch-sử-xử-lý)](#trạng-thái-hành-động-và-lịch-sử-xử-lý)

[4.5.5. Hỗ trợ quyết định thay vì quyết định tự động [59](#hỗ-trợ-quyết-định-thay-vì-quyết-định-tự-động)](#hỗ-trợ-quyết-định-thay-vì-quyết-định-tự-động)

[4.6. Tổng hợp các dòng nghiên cứu và hàm ý cho Tiểu luận [60](#tổng-hợp-các-dòng-nghiên-cứu-và-hàm-ý-cho-tiểu-luận)](#tổng-hợp-các-dòng-nghiên-cứu-và-hàm-ý-cho-tiểu-luận)

[CHƯƠNG 5. TỔNG HỢP KHOẢNG TRỐNG VÀ ĐỊNH HƯỚNG NGHIÊN CỨU [63](#chương-5.-tổng-hợp-khoảng-trống-và-định-hướng-nghiên-cứu)](#chương-5.-tổng-hợp-khoảng-trống-và-định-hướng-nghiên-cứu)

[5.1. Tổng hợp những nội dung đã được giải quyết [63](#tổng-hợp-những-nội-dung-đã-được-giải-quyết)](#tổng-hợp-những-nội-dung-đã-được-giải-quyết)

[5.1.1. Từ quản lý tài sản đến yêu cầu duy trì tính liên tục của thông tin [63](#từ-quản-lý-tài-sản-đến-yêu-cầu-duy-trì-tính-liên-tục-của-thông-tin)](#từ-quản-lý-tài-sản-đến-yêu-cầu-duy-trì-tính-liên-tục-của-thông-tin)

[5.1.2. Dữ liệu dao động và các phương pháp đánh giá [63](#dữ-liệu-dao-động-và-các-phương-pháp-đánh-giá)](#dữ-liệu-dao-động-và-các-phương-pháp-đánh-giá)

[5.1.3. Liên kết cảm biến, BIM, hồ sơ kiểm tra và quản lý bảo trì [64](#liên-kết-cảm-biến-bim-hồ-sơ-kiểm-tra-và-quản-lý-bảo-trì)](#liên-kết-cảm-biến-bim-hồ-sơ-kiểm-tra-và-quản-lý-bảo-trì)

[5.1.4. Ranh giới giữa nội dung đã có và phần nghiên cứu còn lại [65](#ranh-giới-giữa-nội-dung-đã-có-và-phần-nghiên-cứu-còn-lại)](#ranh-giới-giữa-nội-dung-đã-có-và-phần-nghiên-cứu-còn-lại)

[5.2. Ba khoảng trống nghiên cứu [66](#ba-khoảng-trống-nghiên-cứu)](#ba-khoảng-trống-nghiên-cứu)

[5.2.1. Khoảng trống 1 – Xác lập chất lượng và phạm vi hiệu lực của bằng chứng trạng thái [66](#khoảng-trống-1-xác-lập-chất-lượng-và-phạm-vi-hiệu-lực-của-bằng-chứng-trạng-thái)](#khoảng-trống-1-xác-lập-chất-lượng-và-phạm-vi-hiệu-lực-của-bằng-chứng-trạng-thái)

[5.2.2. Khoảng trống 2 – Bảo toàn chất lượng của bằng chứng trong truy vết cấp cấu kiện [67](#khoảng-trống-2-bảo-toàn-chất-lượng-của-bằng-chứng-trong-truy-vết-cấp-cấu-kiện)](#khoảng-trống-2-bảo-toàn-chất-lượng-của-bằng-chứng-trong-truy-vết-cấp-cấu-kiện)

[5.2.3. Khoảng trống 3 – Từ bằng chứng có phạm vi hiệu lực đến trạng thái hành động có thể giải trình [69](#khoảng-trống-3-từ-bằng-chứng-có-phạm-vi-hiệu-lực-đến-trạng-thái-hành-động-có-thể-giải-trình)](#khoảng-trống-3-từ-bằng-chứng-có-phạm-vi-hiệu-lực-đến-trạng-thái-hành-động-có-thể-giải-trình)

[5.2.4. Quan hệ giữa ba khoảng trống [71](#quan-hệ-giữa-ba-khoảng-trống)](#quan-hệ-giữa-ba-khoảng-trống)

[5.3. Luận đề trung tâm và mục tiêu nghiên cứu [72](#luận-đề-trung-tâm-và-mục-tiêu-nghiên-cứu)](#luận-đề-trung-tâm-và-mục-tiêu-nghiên-cứu)

[5.3.1. Luận đề trung tâm [72](#luận-đề-trung-tâm)](#luận-đề-trung-tâm)

[5.3.2. Mục tiêu tổng quát [72](#mục-tiêu-tổng-quát-1)](#mục-tiêu-tổng-quát-1)

[5.3.3. Mục tiêu cụ thể [72](#mục-tiêu-cụ-thể-1)](#mục-tiêu-cụ-thể-1)

[5.4. Câu hỏi nghiên cứu [73](#câu-hỏi-nghiên-cứu-1)](#câu-hỏi-nghiên-cứu-1)

[5.4.1. Câu hỏi nghiên cứu 1 – Bằng chứng phòng thí nghiệm [73](#câu-hỏi-nghiên-cứu-1-bằng-chứng-phòng-thí-nghiệm)](#câu-hỏi-nghiên-cứu-1-bằng-chứng-phòng-thí-nghiệm)

[5.4.2. Câu hỏi nghiên cứu 2 – Truy vết cấp cấu kiện [73](#câu-hỏi-nghiên-cứu-2-truy-vết-cấp-cấu-kiện)](#câu-hỏi-nghiên-cứu-2-truy-vết-cấp-cấu-kiện)

[5.4.3. Câu hỏi nghiên cứu 3 – Khả năng áp dụng trong bối cảnh công trình thực và hỗ trợ kiểm tra [74](#câu-hỏi-nghiên-cứu-3-khả-năng-áp-dụng-trong-bối-cảnh-công-trình-thực-và-hỗ-trợ-kiểm-tra)](#câu-hỏi-nghiên-cứu-3-khả-năng-áp-dụng-trong-bối-cảnh-công-trình-thực-và-hỗ-trợ-kiểm-tra)

[5.4.4. Logic kế tiếp giữa ba câu hỏi [74](#logic-kế-tiếp-giữa-ba-câu-hỏi-1)](#logic-kế-tiếp-giữa-ba-câu-hỏi-1)

[5.5. Ánh xạ câu hỏi nghiên cứu – gói công việc – bài báo – thiết kế kiểm chứng [74](#ánh-xạ-câu-hỏi-nghiên-cứu-gói-công-việc-bài-báo-thiết-kế-kiểm-chứng)](#ánh-xạ-câu-hỏi-nghiên-cứu-gói-công-việc-bài-báo-thiết-kế-kiểm-chứng)

[5.5.1. Ma trận kiến trúc nghiên cứu [74](#ma-trận-kiến-trúc-nghiên-cứu)](#ma-trận-kiến-trúc-nghiên-cứu)

[5.5.2. Nội dung các bước kiểm chứng dự kiến [77](#nội-dung-các-bước-kiểm-chứng-dự-kiến)](#nội-dung-các-bước-kiểm-chứng-dự-kiến)

[5.6. Khung nghiên cứu bốn lớp và kiến trúc Song sinh số dựa trên dữ liệu [77](#khung-nghiên-cứu-bốn-lớp-và-kiến-trúc-song-sinh-số-dựa-trên-dữ-liệu)](#khung-nghiên-cứu-bốn-lớp-và-kiến-trúc-song-sinh-số-dựa-trên-dữ-liệu)

[5.6.1. Chuỗi nghiên cứu [77](#chuỗi-nghiên-cứu-1)](#chuỗi-nghiên-cứu-1)

[5.6.2. Chuỗi định danh [78](#chuỗi-định-danh)](#chuỗi-định-danh)

[5.6.3. Bốn lớp bằng chứng [79](#bốn-lớp-bằng-chứng)](#bốn-lớp-bằng-chứng)

[5.6.4. Thang kiểm chứng [80](#thang-kiểm-chứng)](#thang-kiểm-chứng)

[5.6.5. Luồng dữ liệu và luồng trách nhiệm [81](#luồng-dữ-liệu-và-luồng-trách-nhiệm)](#luồng-dữ-liệu-và-luồng-trách-nhiệm)

[5.6.6. Định vị Song sinh số [81](#định-vị-song-sinh-số)](#định-vị-song-sinh-số)

[5.7. Đóng góp dự kiến của luận án [81](#đóng-góp-dự-kiến-của-luận-án)](#đóng-góp-dự-kiến-của-luận-án)

[5.7.1. Đóng góp 1 – Bằng chứng trạng thái có chất lượng và phạm vi hiệu lực rõ [81](#đóng-góp-1-bằng-chứng-trạng-thái-có-chất-lượng-và-phạm-vi-hiệu-lực-rõ)](#đóng-góp-1-bằng-chứng-trạng-thái-có-chất-lượng-và-phạm-vi-hiệu-lực-rõ)

[5.7.2. Đóng góp 2 – Khung truy vết cấp cấu kiện bảo toàn chất lượng của bằng chứng [82](#đóng-góp-2-khung-truy-vết-cấp-cấu-kiện-bảo-toàn-chất-lượng-của-bằng-chứng)](#đóng-góp-2-khung-truy-vết-cấp-cấu-kiện-bảo-toàn-chất-lượng-của-bằng-chứng)

[5.7.3. Đóng góp 3 – Cơ sở kiểm chứng khả năng áp dụng của chuỗi truy vết [83](#đóng-góp-3-cơ-sở-kiểm-chứng-khả-năng-áp-dụng-của-chuỗi-truy-vết)](#đóng-góp-3-cơ-sở-kiểm-chứng-khả-năng-áp-dụng-của-chuỗi-truy-vết)

[5.7.4. Đóng góp 4 – Logic hỗ trợ hành động minh bạch và có thể giải trình [84](#đóng-góp-4-logic-hỗ-trợ-hành-động-minh-bạch-và-có-thể-giải-trình)](#đóng-góp-4-logic-hỗ-trợ-hành-động-minh-bạch-và-có-thể-giải-trình)

[5.7.5. Đóng góp ở cấp ngành Quản lý xây dựng [85](#đóng-góp-ở-cấp-ngành-quản-lý-xây-dựng)](#đóng-góp-ở-cấp-ngành-quản-lý-xây-dựng)

[5.8. Phạm vi, giới hạn và điều kiện diễn giải kết quả [85](#phạm-vi-giới-hạn-và-điều-kiện-diễn-giải-kết-quả)](#phạm-vi-giới-hạn-và-điều-kiện-diễn-giải-kết-quả)

[5.8.1. Phân lớp phạm vi [85](#phân-lớp-phạm-vi)](#phân-lớp-phạm-vi)

[5.8.2. Ranh giới giữa bốn loại bằng chứng [86](#ranh-giới-giữa-bốn-loại-bằng-chứng)](#ranh-giới-giữa-bốn-loại-bằng-chứng)

[5.8.3. Giới hạn của mô hình phần tử hữu hạn [86](#giới-hạn-của-mô-hình-phần-tử-hữu-hạn)](#giới-hạn-của-mô-hình-phần-tử-hữu-hạn)

[5.8.4. Giới hạn của tổng quan tài liệu [86](#giới-hạn-của-tổng-quan-tài-liệu)](#giới-hạn-của-tổng-quan-tài-liệu)

[5.8.5. Giới hạn và điều kiện của định vị Song sinh số [87](#giới-hạn-và-điều-kiện-của-định-vị-song-sinh-số)](#giới-hạn-và-điều-kiện-của-định-vị-song-sinh-số)

[5.9. Định hướng nghiên cứu sau Tiểu luận tổng quan [87](#định-hướng-nghiên-cứu-sau-tiểu-luận-tổng-quan)](#định-hướng-nghiên-cứu-sau-tiểu-luận-tổng-quan)

[5.9.1. Định hướng 1 – Kiểm chứng chất lượng bằng chứng trạng thái [87](#định-hướng-1-kiểm-chứng-chất-lượng-bằng-chứng-trạng-thái)](#định-hướng-1-kiểm-chứng-chất-lượng-bằng-chứng-trạng-thái)

[5.9.2. Định hướng 2 – Hình thức hóa mô hình dữ liệu và tiêu chí truy vết [87](#định-hướng-2-hình-thức-hóa-mô-hình-dữ-liệu-và-tiêu-chí-truy-vết)](#định-hướng-2-hình-thức-hóa-mô-hình-dữ-liệu-và-tiêu-chí-truy-vết)

[5.9.3. Định hướng 3 – Kiểm chứng tính toàn vẹn của chuỗi truy vết [88](#định-hướng-3-kiểm-chứng-tính-toàn-vẹn-của-chuỗi-truy-vết)](#định-hướng-3-kiểm-chứng-tính-toàn-vẹn-của-chuỗi-truy-vết)

[5.9.4. Định hướng 4 – Đánh giá khả năng áp dụng trong bối cảnh công trình thực [88](#định-hướng-4-đánh-giá-khả-năng-áp-dụng-trong-bối-cảnh-công-trình-thực)](#định-hướng-4-đánh-giá-khả-năng-áp-dụng-trong-bối-cảnh-công-trình-thực)

[5.9.5. Định hướng 5 – Kiểm chứng logic hỗ trợ hành động [88](#định-hướng-5-kiểm-chứng-logic-hỗ-trợ-hành-động)](#định-hướng-5-kiểm-chứng-logic-hỗ-trợ-hành-động)

[5.10. Tổng hợp chương [88](#tổng-hợp-chương-2)](#tổng-hợp-chương-2)

[TÀI LIỆU THAM KHẢO [90](#tài-liệu-tham-khảo)](#tài-liệu-tham-khảo)

DANH MỤC BẢNG

Bảng 2.1. Phân biệt ba mức theo luồng dữ liệu [37](#TLTQ_Bang_2_1)

Bảng 3.1. Một số nghiên cứu đại diện về đơn vị vật lý và cách đánh giá dữ liệu [43](#TLTQ_Bang_3_1)

Bảng 4.1. Phân biệt các mức liên kết thông tin trong quản lý tài sản [51](#TLTQ_Bang_4_1)

Bảng 4.2. Tổng hợp các dòng nghiên cứu chính [60](#TLTQ_Bang_4_2)

Bảng 5.1. Tổng hợp nội dung đã được xác lập và phần còn lại của nghiên cứu [65](#TLTQ_Bang_5_1)

Bảng 5.2. Ánh xạ câu hỏi nghiên cứu, gói công việc, bài báo và thiết kế kiểm chứng [75](#TLTQ_Bang_5_2)

Bảng 5.3. Thang kiểm chứng của khung nghiên cứu [80](#TLTQ_Bang_5_3)

Bảng 5.4. Phạm vi của luận án [85](#TLTQ_Bang_5_4)

**DANH MỤC HÌNH**

Hình 1.1. Chuỗi nghiên cứu tổng thể [20](#TLTQ_Hinh_1_1)

Hình 5.1. Chuỗi định danh cốt lõi [78](#TLTQ_Hinh_5_1)

Hình 5.2. Kiến trúc kiểm chứng bốn lớp [80](#TLTQ_Hinh_5_2)

Hình 5.3. Logic hỗ trợ hành động [84](#TLTQ_Hinh_5_3)

**GIẢI THÍCH THUẬT NGỮ**

1.  **Mô hình thông tin công trình và chuẩn trao đổi**

| **Viết tắt** | **Dạng đầy đủ** | **Giải thích** |
|:---|:---|:---|
| BIM | Building Information Modeling | Mô hình thông tin công trình. Trong luận án dùng như lớp ngữ cảnh cấu kiện, không phải công cụ dựng hình |
| IFC | Industry Foundation Classes | Lược đồ dữ liệu mở của buildingSMART cho trao đổi mô hình công trình giữa các phần mềm khác nhau. Là nền định danh cấu kiện của luận án |
| GUID | Globally Unique Identifier | Mã định danh duy nhất toàn cục gán cho từng đối tượng |
| GlobalId | GlobalId trong IFC | Thuộc tính định danh của đối tượng IFC, dạng chuỗi 22 ký tự. Mã này có thể đổi khi mô hình được xuất lại, nên tính bền vững của nó là vấn đề nghiên cứu ở Mục 2.2.3 |
| IDS | Information Delivery Specification | Chuẩn của buildingSMART mô tả yêu cầu thông tin dưới dạng máy đọc được, và kiểm tra tự động xem mô hình có đáp ứng hay không. Đang thay thế mvdXML |
| mvdXML | Model View Definition XML | Cơ chế cũ định nghĩa tập con của IFC cho một mục đích sử dụng. Đang được IDS thay thế |
| ICDD | Information Container for Linked Document Delivery | Container theo ISO 21597 để đóng gói và liên kết tài liệu đa miền |
| BrIM | Bridge Information Modeling | Biến thể của BIM cho công trình cầu |
| CMMS | Computerized Maintenance Management System | Hệ quản lý bảo trì bằng máy tính, nơi lưu lệnh công việc, lịch bảo trì và trạng thái xử lý |
| AIM, PIM | Asset Information Model, Project Information Model | Mô hình thông tin tài sản giai đoạn vận hành, và mô hình thông tin dự án giai đoạn thực hiện |
| CDE | Common Data Environment | Môi trường dữ liệu chung, nơi thông tin được chia sẻ và phê duyệt theo trạng thái |

2.  **Công nghệ web ngữ nghĩa và dữ liệu liên kết**

| **Viết tắt** | **Dạng đầy đủ** | **Giải thích** |
|:---|:---|:---|
| SOSA | Sensor, Observation, Sample, and Actuator | Từ vựng lõi của W3C và OGC mô tả cảm biến, quan trắc, mẫu và cơ cấu chấp hành. Luận án đặt bản ghi bằng chứng trên lớp này |
| SSN | Semantic Sensor Network | Phần mở rộng của SOSA, mô tả hệ cảm biến, quy trình đo và điều kiện triển khai |
| PROV-DM | PROV Data Model | Mô hình dữ liệu nguồn gốc của W3C, gồm ba lớp gốc là thực thể, hoạt động và tác nhân |
| PROV-O | PROV Ontology | Bản thể hóa PROV-DM dưới dạng OWL để máy suy luận được |
| PAV | Provenance, Authoring and Versioning | Từ vựng bổ sung cho PROV, phân biệt tác giả, người đóng góp, người biên tập và phiên bản |
| SHACL | Shapes Constraint Language | Ngôn ngữ ràng buộc của W3C để kiểm tra dữ liệu RDF. Luận án dùng để kiểm chứng quan hệ trong chuỗi truy vết |
| RDF | Resource Description Framework | Mô hình dữ liệu dạng bộ ba chủ thể, vị từ, đối tượng |
| SPARQL | SPARQL Protocol and RDF Query Language | Ngôn ngữ truy vấn dữ liệu RDF |
| OWL | Web Ontology Language | Ngôn ngữ mô tả bản thể luận, cho phép suy luận logic |
| DOLCE | Descriptive Ontology for Linguistic and Cognitive Engineering | Bản thể luận nền, dùng trong bài Borkowski để phân biệt cấu kiện với các giai đoạn vòng đời của nó |

**Ghi chú:**

- W3C là World Wide Web Consortium, tổ chức chuẩn hóa web, ban hành PROV, SOSA/SSN và SHACL. OGC là Open Geospatial Consortium, đồng ban hành SOSA/SSN.

- ISO 19650 là bộ tiêu chuẩn quản lý thông tin theo BIM, trong đó phần 3 năm 2020 dành cho giai đoạn vận hành. ISO 21597 là chuẩn cho container thông tin ICDD.

3.  **Theo dõi trạng thái kết cấu và đánh giá**

| **Viết tắt** | **Tên đầy đủ** | **Giải thích** |
|:---|:---|:---|
| LORO | Leave-One-Run-Out | Giao thức đánh giá giữ lại toàn bộ dữ liệu của một lần chạy làm tập kiểm tra. Trả lời câu hỏi kết quả có khái quát sang lần chạy mới trong cùng bối cảnh hay không |
| LOCO | Leave-One-Campaign-Out | Giữ lại trọn một đợt thí nghiệm, thường là sau khi tháo lắp lại. Khắt khe hơn LORO, trả lời câu hỏi kết quả có sống sót qua một lần lắp đặt mới hay không |
| FEM | Finite Element Method | Phương pháp phần tử hữu hạn. Trong luận án chỉ giữ ở vai trò mô hình danh nghĩa chưa hiệu chuẩn, theo giới hạn ở Mục 5.8.3 |
| VoI | Value of Information | Giá trị của thông tin, lượng hóa lợi ích của việc thu thêm dữ liệu quan trắc trước khi ra quyết định |
| RBI | Risk-Based Inspection | Kế hoạch kiểm tra theo rủi ro, chọn thời điểm và nội dung kiểm tra theo mức rủi ro và giá trị thông tin |

**4. Chuỗi định danh của luận án**

| **Ký hiệu** | **Giải thích** |
|:---|:---|
| Sensor_ID | Định danh nguồn đo, gồm vị trí lắp, loại cảm biến và cấu hình thu nhận |
| BIM_GUID | Định danh cấu kiện trong mô hình, neo vào GlobalId của IFC |
| Condition_Evidence_ID | Định danh bản ghi bằng chứng trạng thái. Bản ghi mang kết quả phân loại kèm nguồn gốc, giao thức đánh giá, độ bất định và phạm vi hiệu lực |
| Inspection_Record_ID | Định danh hồ sơ kiểm tra, có ngày tạo, người thực hiện, kết quả quan sát và lịch sử riêng |
| Action_Status | Trạng thái hành động theo bốn mức Bình thường, Theo dõi, Kiểm tra, Kiểm tra ưu tiên |
| FEM_Node_ID | Định danh nút trong mô hình phần tử hữu hạn. Là siêu dữ liệu tùy chọn, không nằm trong chuỗi bắt buộc |

# DẪN NHẬP

Trong giai đoạn vận hành, giá trị của một công trình phụ thuộc vào các đợt kiểm tra, bảo trì và vào khả năng quản lý thông tin liên tục trong suốt vòng đời tài sản. Với nhà công nghiệp khung thép, thông tin về trạng thái công trình đến từ nhiều nguồn: dữ liệu cảm biến, mô hình thông tin công trình, hồ sơ kiểm tra, lịch sử sửa chữa và các quyết định quản lý. Nhiều nguồn dữ liệu cùng tồn tại chưa tạo thành một hệ thống thông tin hỗ trợ được quyết định. Khó khăn nằm ở việc tổ chức, liên kết và giữ được quan hệ giữa các nguồn đó theo thời gian.

Cảm biến, học máy, BIM/IFC và Song sinh số (Digital Twin, còn gọi là Song sinh kỹ thuật số hay bản sao kỹ thuật số) đã tạo thêm nhiều công cụ cho quản lý tài sản công trình. Dữ liệu dao động giúp nhận biết thay đổi trạng thái; BIM cung cấp ngữ cảnh và định danh cho cấu kiện; hệ quản lý bảo trì lưu hồ sơ kiểm tra và công việc; kiến trúc Song sinh kỹ thuật số kết nối dữ liệu từ tài sản vật lý với bản sao số của nó và với các quá trình vận hành. Kết quả tổng quan tài liệu cho thấy phần lớn các thành phần này đã có tiền lệ phát triển riêng. Vì vậy, vấn đề khoa học không còn nằm ở việc lắp thêm cảm biến, xây thêm một mô hình học máy, đưa dữ liệu lên BIM hay dựng một giao diện Song sinh số.

Vấn đề quan trọng hơn nằm ở **tính liên tục của bằng chứng**. Một kết quả sinh ra từ dữ liệu dao động chỉ có giá trị khi xác định được nó được tạo từ dữ liệu nào, dưới điều kiện đo và cấu hình cảm biến nào, bằng phiên bản xử lý nào, được kiểm chứng bằng giao thức nào và có giá trị trong phạm vi nào. Khi kết quả đó đi vào hệ thống quản lý tài sản, thông tin về nguồn gốc và phạm vi hiệu lực phải được giữ lại. Người quản lý cần biết bằng chứng liên quan tới cấu kiện nào, hồ sơ kiểm tra nào được tạo hoặc cập nhật từ đó, hành động nào đã được đề xuất hoặc thực hiện và trạng thái xử lý hiện tại.

Vì vậy, Tiểu luận dùng khái niệm **bằng chứng trạng thái** thay vì đồng nhất đầu ra của mô hình phân loại với chẩn đoán hư hỏng. Trong định hướng nghiên cứu, dữ liệu dao động phòng thí nghiệm được xem là nguồn để kiểm chứng khả năng phân biệt các trạng thái liên kết có kiểm soát; kết quả ở lớp này không được suy rộng trực tiếp thành kết luận về hư hỏng trên công trình thực. Tương tự, một bất thường trong dữ liệu vận hành chỉ tạo căn cứ cho việc xem xét hoặc kiểm tra, chưa đủ để tự động xác định nguyên nhân hay mức độ hư hỏng. Ranh giới này tách bằng chứng kỹ thuật khỏi quyết định quản lý và giữ cho suy luận không vượt quá phạm vi đã được kiểm chứng.

Song sinh số được tiếp cận như một **mục tiêu kiến trúc phục vụ quản lý tài sản**, thay vì một nhãn công nghệ được mặc định từ đầu. Trọng tâm là mối liên hệ có thể cập nhật và truy vết giữa dữ liệu từ tài sản vật lý, bằng chứng trạng thái, cấu kiện trong BIM, hồ sơ kiểm tra và trạng thái hành động. Tiểu luận chỉ xác lập các năng lực cần được kiểm chứng và các điều kiện diễn giải; mức năng lực thực tế của khung là nội dung của các nghiên cứu chuyên đề và bước kiểm chứng tiếp theo, không phải kết quả của tổng quan tài liệu.

Tiểu luận đi theo một logic xuyên suốt: từ **chất lượng của thông tin kỹ thuật**, tới **khả năng truy vết của thông tin quản lý**, rồi tới **khả năng hỗ trợ kiểm tra – bảo trì trong bối cảnh thực tế**. Nội dung từng chương được giới thiệu ở mục 1.9.

Nhận định trung tâm rút ra từ tổng quan là khoảng trống nghiên cứu nằm chủ yếu tại **các điểm nối giữa những thành phần đã tồn tại**, chứ không ở sự thiếu vắng một công nghệ thành phần. Bằng chứng cần được xác lập chất lượng và phạm vi hiệu lực; các thuộc tính đó cần được bảo toàn khi bằng chứng được liên kết tới cấu kiện và hồ sơ; trạng thái của hành động quản lý cần truy ngược được về căn cứ đã sử dụng. Trục nghiên cứu vì thế được hình thành theo chuỗi:

**Dữ liệu dao động → Bằng chứng trạng thái → Cấu kiện liên kết BIM → Hồ sơ kiểm tra → Hỗ trợ hành động kiểm tra – bảo trì.**

Chuỗi này đặt nghiên cứu trong lĩnh vực Quản lý xây dựng. Dữ liệu dao động, học máy, BIM và các công nghệ số là phương tiện; đối tượng quản lý chính là **dòng thông tin về tình trạng tài sản và quá trình chuyển thông tin đó thành căn cứ cho kiểm tra – bảo trì**. Mục tiêu là làm cho căn cứ của quyết định rõ hơn, truy vết được và kiểm chứng lại được khi cần; quyết định vẫn thuộc về người quản lý. Trên nền đó, luận án định hướng phát triển một khung Song sinh số dựa trên dữ liệu cho nhà công nghiệp khung thép trong giai đoạn vận hành.
