# PAPER1 Supervisor Report v1 → v2: changelog

**Ngày:** 13/09/2026
**File sửa:** `PAPER1_SUPERVISOR_REPORT_DUT_TEMPLATE_v2.pptx` (18 slide, giữ nguyên template, layout, hình ảnh, biểu đồ, số liệu Paper 1) và `PAPER1_GIAI_THICH_NGHIEN_CUU_DE_HIEU_v2.md`.
**Phương pháp:** sửa trực tiếp trong script sinh slide gốc (python-pptx) rồi build lại — không thiết kế lại từ đầu; mọi vị trí, màu sắc, ảnh, biểu đồ giữ nguyên trừ ba chỗ có yêu cầu đơn giản hóa bố cục (nêu ở dưới). File `.md` được viết lại toàn văn với các đoạn cần sửa thay đổi, phần còn lại giữ nguyên nội dung.
**Không đổi:** tiêu đề Paper 1, mọi số liệu kết quả (CP1/CP2/CP3, RF/SVM/1D-CNN/ResNet1D), 18 run/216 recording/6.899 window, mục tiêu SHM, trục nghiên cứu, chuỗi định danh, firewall Limited-FEM.

---

## 1. Slide 4 — Kiến trúc RQ/WP/Paper/Gate

| | Cũ | Mới | Lý do | Nguồn |
|---|---|---|---|---|
| Thông điệp chính | "Paper 1 là trụ đầu tiên của trục chịu lực RQ1 + RQ2; mỗi Paper gắn với Evidence Gate cụ thể." | "Paper 1 là trụ bằng chứng đầu tiên của luận án: RQ1/WP1/Chương 4/Gate 1. Đầu ra của Paper 1 là đầu vào cho RQ2/WP2." | Ngầm hiểu sai rằng Paper 1 gánh cả RQ2. Kiến trúc khóa quy định Paper 1 chỉ thuộc RQ1; đầu ra của nó là đầu vào cho RQ2, không phải một phần của RQ2 | Yêu cầu #1 của người dùng (kiến trúc khóa) |
| Bảng — hàng Paper 2 | Gate: "G2, G3, G6" | Gate: "G2–G3" | G6 không nằm trong kiến trúc khóa hiện hành do người dùng cung cấp | Yêu cầu #1 |
| Bảng — hàng Paper 3 | Paper: "Paper 3 (bonus)"; Trạng thái: "Chỉ ở mức chuẩn bị" | Paper: "Paper 3"; Trạng thái: "Đang chuẩn bị hiện trường (11/08/2026)" | Bỏ nhãn "bonus"; gắn ngày cho trạng thái lịch sử theo yêu cầu #10 | Yêu cầu #2, #10 |
| Bảng — hàng WP4 | WP: "WP4 (gộp)"; Chương: "C7 (tùy chọn)"; Paper: "Paper 4 (tùy chọn)"; Lớp bằng chứng: "Decision support" | WP: "WP4"; Chương: "Tổng hợp"; Paper: "— (không bắt buộc)"; Lớp bằng chứng: "Decision-support synthesis" | Bỏ Paper 4 riêng và C7 tùy chọn — không được kiến trúc khóa hỗ trợ rõ ràng; WP4 là tổng hợp quyết định, không có Paper bắt buộc | Yêu cầu #1 |
| Bảng — hàng Paper 1, cột Trạng thái | "G1 mở — bằng chứng một phần" | "Gói G1: sẵn sàng khoa học — chờ ký nghiệm thu" | Thống nhất một trạng thái Gate 1 duy nhất trong toàn bộ tài liệu, không dùng đồng thời hai cách nói mâu thuẫn | Yêu cầu #1, #10 |
| Tiêu đề cột trạng thái | "Trạng thái (11/08/2026)" áp cho mọi hàng | "Trạng thái" (không ngày chung); các hàng lịch sử (Paper 2, Paper 3) tự ghi "(11/08/2026)" trong ô | Ngày 11/08 chỉ đúng cho Paper 2/3 (chưa cập nhật); trạng thái Paper 1 hiện tại hơn (theo audit IT 12–13/09), không nên gắn chung một ngày | Yêu cầu #10 |
| Ghi chú trình bày (speaker notes) | "Theo Charter v2.1.2 và Evidence Gates (cập nhật 11/08/2026)... Paper 3 là bài bonus; bằng chứng khả thi hiện trường tối thiểu vẫn bắt buộc cho luận án." | Viết lại: nêu rõ gói G1 sẵn sàng khoa học chờ ký nghiệm thu; "Paper 1 không gánh RQ2 — đầu ra của Paper 1 là đầu vào cho Paper 2"; đổi cách gọi Charter; nêu rõ Paper 3 là quyết định chiến lược công bố, không phải "bonus"; thêm mô tả WP4 (logic Normal → Watch → Inspect → Priority Inspection) | Đồng bộ toàn bộ các điểm sửa liên quan đến slide này trong ghi chú | Yêu cầu #1, #2, #10 |

## 2. Slide 5 — Đầu ra chuyển cho luận án (CEI)

| Cũ | Mới | Lý do | Nguồn |
|---|---|---|---|
| "Biến động giữa run và đợt đo — một phần của CEI" | "Biến động giữa run và đợt đo — dữ liệu đầu vào cho Condition_Evidence metadata" | Giảm nhấn mạnh CEI như một khái niệm đã hoàn thiện; CEI được giải thích đầy đủ và đúng phạm vi ở Slide 15 | Yêu cầu #7 |

## 3. Slide 9 — Vì sao không chia ngẫu nhiên theo window

| | Cũ | Mới | Lý do | Nguồn |
|---|---|---|---|---|
| Thông điệp chính | "Các window cắt từ cùng một run gần giống nhau; chia ngẫu nhiên khiến tập kiểm tra 'đã thấy' dữ liệu huấn luyện." | "Chia ngẫu nhiên theo window tạo nguy cơ đánh giá lạc quan giả tạo, vì các window từ cùng nguồn vật lý có thể lọt vào cả hai tập." | Chuyển từ khẳng định chắc chắn ("khiến … đã thấy") sang đúng bản chất là một *nguy cơ* | Yêu cầu #3 |
| Nhãn trong ô đỏ | "Window chồng lấn 50% nằm ở cả hai phía → điểm số bị thổi phồng" | "Window chồng lấn 50% có thể rơi vào cả hai phía → nguy cơ đánh giá lạc quan giả tạo" | Cùng lý do trên, áp dụng cho nhãn trực quan trong hình | Yêu cầu #3 |
| Ghi chú trình bày | "…window gần như giống hệt nhau nằm ở cả huấn luyện và kiểm tra, điểm số bị thổi phồng… Nghiên cứu về chẩn đoán ổ lăn cho thấy đổi cách chia làm thay đổi sai số hàng chục điểm phần trăm (Wheat 2024; Vieira 2026)." | Viết lại: nêu rõ đây là *nguy cơ*, và **"Paper 1 không chạy đối chứng random-window split trên chính dataset này, nên không định lượng mức lạc quan giả tạo nếu dùng cách chia sai"**; bằng chứng về hướng tác động dẫn nguồn từ dữ liệu chẩn đoán ổ lăn (Wheat 2024; Vieira 2026), không phải từ dataset khung thép này | Bỏ tuyên bố ngầm rằng Paper 1 đã đo lường/chứng minh mức độ inflation trên chính dataset của mình | Yêu cầu #3, #12 |
| Hình ảnh trực quan (khung SAI/ĐÚNG, lưới ô vuông) | — | **Giữ nguyên** | Người dùng yêu cầu giữ so sánh trực quan; chỉ đổi phần diễn giải khoa học từ tuyệt đối sang có điều kiện | Yêu cầu #3 |

## 4. Slide 10 — Thiết kế đánh giá (giảm chi tiết kỹ thuật)

| Cũ | Mới | Lý do | Nguồn |
|---|---|---|---|
| Hai băng cuối slide: "Lựa chọn mô hình chỉ dùng validation … (tái lập 192 lựa chọn đã lưu)" **và** "Số lần huấn luyện: 540 (học sâu) + 180 (RF, SVM) + 72 (chuyển giao) — Bảng 3 của bản thảo" | Một băng duy nhất: "Lựa chọn mô hình chỉ dựa trên tập validation — dữ liệu kiểm tra không tham gia lựa chọn." | Chuyển hai chi tiết định lượng (192 lựa chọn; 540/180/72 fit) xuống ghi chú trình bày, để thầy nắm logic nghiên cứu trước khi vào cơ chế kiểm chứng | Yêu cầu #9 |
| Ghi chú trình bày | không có số 540/180/72 | Thêm câu: "Số lần huấn luyện thực thi: 540 (học sâu) + 180 (RF, SVM) + 72 (chuyển giao) — Bảng 3 bản thảo." | Giữ chi tiết định lượng ở lớp ghi chú thay vì slide chính | Yêu cầu #9 |

## 5. Slide 11 — Mô hình (giảm chi tiết kỹ thuật)

| Cũ | Mới | Lý do | Nguồn |
|---|---|---|---|
| "Random forest: 300 cây; không tinh chỉnh" / "SVM-RBF: C = 5, gamma = scale; không tinh chỉnh" | "Random forest: không tinh chỉnh" / "SVM-RBF: không tinh chỉnh" | Bỏ thông số kỹ thuật cụ thể khỏi slide chính, giữ trên ghi chú | Yêu cầu #9 |
| "25 đặc trưng/kênh + tương quan cặp kênh → 228 chiều (CP1), 366 chiều (CP2, CP3)" | "Đặc trưng tính sẵn theo từng kênh tín hiệu — không học trực tiếp từ dữ liệu thô" | Giữ ý nghĩa nghiên cứu (đặc trưng thủ công so với học trực tiếp), bỏ số chiều cụ thể khỏi slide chính | Yêu cầu #9 |
| Ghi chú trình bày | không có 300 cây / C=5 / 228 / 366 | Thêm: "…(thông số cụ thể: Random forest 300 cây; SVM-RBF C = 5, gamma = scale)… Số chiều đặc trưng: 228 (CP1, 8 kênh), 366 (CP2/CP3, 12 kênh) — Bảng A2, §3.6 bản thảo." | Giữ chi tiết định lượng ở ghi chú | Yêu cầu #9 |
| Cột học sâu (siêu tham số phụ thuộc HPO) | không đổi | **Giữ nguyên** — đây là hạn chế bắt buộc phải hiển thị trên slide | Yêu cầu #9 |

## 6. Slide 15 — Vai trò condition evidence + CEI

| | Cũ | Mới | Lý do | Nguồn |
|---|---|---|---|---|
| Thông điệp chính | "Paper 1 xác định những gì một bản ghi condition evidence phải mang theo trước khi đi vào chuỗi truy vết." | "Paper 1 cung cấp căn cứ thực nghiệm để Paper 2 xác định những thuộc tính condition evidence cần lưu giữ." | Câu cũ khiến Paper 1 nghe như đã thiết lập một chuẩn báo cáo hoàn chỉnh; đúng vai trò là Paper 1 cung cấp *căn cứ thực nghiệm*, Paper 2 mới là nơi hình thức hóa | Yêu cầu #6 |
| Tiêu đề hộp trái | "Bản ghi evidence cần mang theo" | "Thuộc tính evidence được Paper 1 chỉ ra là cần thiết / để diễn giải đúng kết quả (Paper 2 hình thức hóa thành schema)" | Đúng theo câu chữ yêu cầu; làm rõ Paper 2 là nơi hình thức hóa | Yêu cầu #6 |
| 5 gạch đầu dòng (bối cảnh thu đo, cấu hình cảm biến, giao thức, biến động, ranh giới hiệu lực) | không đổi | **Giữ nguyên** | Đúng 5 mục người dùng yêu cầu giữ | Yêu cầu #6 |
| Hộp phải (CEI) | "CEI là cấu trúc metadata — không phải điểm số, không phải mức hư hỏng" | "CEI: cấu trúc metadata/evidence đang đề xuất cho giai đoạn tích hợp — không phải điểm số, không phải mức hư hỏng" | Thêm rõ CEI là cấu trúc **đang đề xuất cho giai đoạn tích hợp** (Paper 2), không phải một đóng góp đã hoàn thiện và kiểm chứng của Paper 1 | Yêu cầu #7 |
| Ghi chú trình bày | "…Paper 1 cung cấp nội dung cho mắt xích Condition_Evidence_ID… CEI là cấu trúc metadata, không phải một điểm số." | Viết lại theo đúng khung Claim ở trên; thêm "đang đề xuất cho giai đoạn tích hợp ở Paper 2" | Đồng bộ với các sửa trên | Yêu cầu #6, #7 |

## 7. Slide 16 — Vị trí Paper 2/Paper 3

| | Cũ | Mới | Lý do | Nguồn |
|---|---|---|---|---|
| Ghi chú trình bày | "…Paper 3 là bài bonus, nhưng bằng chứng khả thi hiện trường tối thiểu là bắt buộc cho luận án…" | "Bằng chứng khả thi hiện trường tối thiểu (RQ3) là thành phần bắt buộc của luận án; việc công bố Paper 3 thành bài báo riêng là quyết định chiến lược công bố, không phải điều kiện của luận án." | Bỏ nhãn "bonus"; phân biệt rõ bằng chứng (bắt buộc) và việc xuất bản thành bài riêng (chiến lược) | Yêu cầu #2, #11 |
| Cột 1 (Paper 1), tiêu đề nhỏ | "Paper 1 · RQ1 · G1" — trạng thái: "Bản thảo v8.1; G1 chưa ký nghiệm thu" | trạng thái: "Gói G1 sẵn sàng khoa học — chờ ký nghiệm thu" | Thống nhất trạng thái Gate 1 | Yêu cầu #10 |
| Cột 2 (Paper 2), tiêu đề | "Paper 2 · RQ2 · G2, G3, G6" — trạng thái: "Đang thiết kế; CQ và tiêu chí chưa khóa" | tiêu đề: "Paper 2 · RQ2 · G2–G3"; trạng thái: "Đang thiết kế; CQ và tiêu chí chưa khóa (11/08/2026)" | Bỏ G6; gắn ngày cho trạng thái lịch sử | Yêu cầu #1, #2, #10 |
| Cột 3 (Paper 3), tiêu đề | "Paper 3 · RQ3 · G4, G5 (bonus)" — trạng thái: "Chỉ chuẩn bị; chưa xác nhận tiếp cận hiện trường" | tiêu đề: "Paper 3 · RQ3 · G4–G5"; trạng thái: "Đang chuẩn bị hiện trường (11/08/2026)" | Bỏ "(bonus)"; gắn ngày cho trạng thái lịch sử | Yêu cầu #2, #10 |

## 8. Slide 17 — Chiến lược nộp tạp chí (thiết kế lại theo yêu cầu #8)

| Phần | Cũ | Mới | Lý do | Nguồn |
|---|---|---|---|---|
| Nội dung chính | Bảng điểm 6 tạp chí (80/76/76/67/61/54) + 4 lý do dạng danh sách | 4 lý do dạng thẻ số (1–4): Đúng phạm vi · Hội tụ độc lập (Scopus + OpenAlex) · Có tiền lệ liên quan (tổng quát hóa + chất lượng thông tin SHM) · Thực tế (đường xuất bản không APC) | Bỏ bảng điểm nội bộ có thể gây phân tán; giữ đúng 4 luận điểm người dùng liệt kê | Yêu cầu #8 |
| Bậc thang tạp chí | Bảng 6 dòng có điểm số | "Vòng 1: Structural Health Monitoring" (thẻ nổi bật) + hàng "Dự phòng" gồm 4 tạp chí: Structural Control & HM, Engineering Structures, ASCE-ASME JRUES-B, J. Civil Struct. Health Monit. | Thay bảng điểm bằng bậc thang gọn, đúng danh sách yêu cầu | Yêu cầu #8 |
| Rủi ro desk-reject | "thấp–trung bình" | "TRUNG BÌNH" | Theo đúng yêu cầu, không dùng "thấp–trung bình" | Yêu cầu #8 |
| Ghi chú trình bày | Nhắc điểm 65/20/15 và Zorzi/Deng cụ thể | Viết lại: không nhắc thang điểm nội bộ trên slide; giữ mô tả OpenAlex STRONG và rủi ro TRUNG BÌNH | Đồng bộ với thiết kế mới | Yêu cầu #8 |

## 9. File giải thích (.md) — các mục đã sửa

| Mục | Cũ | Mới | Lý do | Nguồn |
|---|---|---|---|---|
| Đầu trang | "Mọi con số… chờ nghiệm thu Gate 1…" | Thêm câu đầu: "**Gói bằng chứng Gate 1: sẵn sàng về mặt khoa học; chờ thầy rà soát và ký nghiệm thu chính thức.**" | Đưa trạng thái Gate 1 thống nhất lên đầu tài liệu | Yêu cầu #10 |
| §3 (trục nghiên cứu) | "Paper 3 (bài phụ, không bắt buộc phải công bố) thử triển khai khung này ở một công trình thật." | "Paper 3 kiểm chứng khả thi triển khai khung này tại một công trình thật. Bằng chứng khả thi hiện trường ở mức tối thiểu là thành phần **bắt buộc** của luận án; việc có tách nội dung đó thành một bài báo riêng để công bố hay không chỉ là một **quyết định chiến lược công bố**." + thêm câu "Đầu ra của Paper 1 là đầu vào cho Paper 2 — Paper 1 không gánh câu hỏi nghiên cứu của RQ2." | Yêu cầu #11, #2 | |
| §4 (thuật ngữ), dòng CEI | "…ghi lại độ tin cậy của nó (không phải một con số điểm số đơn giản, không phải 'mức độ hư hỏng')." | "Một cấu trúc metadata/evidence **đang được đề xuất cho giai đoạn tích hợp** (Paper 2)…" | Yêu cầu #7 | |
| §5 (mô hình thí nghiệm) | "…để có thể tháo — vặn lỏng lại — giả lập bốn trạng thái…"; "B1 — liên kết ở đỉnh mái bị vặn lỏng có kiểm soát" (và tương tự B2, B3) | "…để có thể tháo và điều chỉnh, tạo ra bốn trạng thái…"; "B1 — liên kết ở đỉnh mái được thao tác có chủ đích" (và tương tự B2, B3); thêm câu "Mức độ điều chỉnh **không được định lượng bằng torque (lực siết) hay preload (lực căng trước)** của bu lông" | Tránh ngụ ý đã đo lường được mức độ làm lỏng; làm rõ không có torque/preload | Yêu cầu #4 |
| §7 (rò rỉ dữ liệu) | "…đóng góp của Paper 1 là áp dụng đúng nguyên tắc đó và **chứng minh nó tạo ra sự khác biệt lớn trên chính loại dữ liệu rung động khung thép bu lông này**…" | Thêm đoạn riêng: "Paper 1 áp dụng nguyên tắc chia theo đơn vị vật lý cho chính dữ liệu này và báo cáo bằng chứng run-aware thu được — nhưng **không chạy phép đối chứng chia ngẫu nhiên theo window trên chính dataset này**, nên **không đo lường được mức chênh lệch cụ thể**. Bằng chứng về hướng tác động đến từ nghiên cứu khác (Wheat 2024; Vieira 2026), không phải từ phép đo trực tiếp trên dataset này." Câu kết luận đổi thành: "áp dụng đúng nguyên tắc đó cho loại dữ liệu… và báo cáo đầy đủ bằng chứng run-aware thu được" | Bỏ tuyên bố "đã chứng minh" một kết quả định lượng chưa từng được đo trên chính dataset này | Yêu cầu #12 |
| §11 (chuyển giao giữa đợt đo) | "…nhưng gần như mất hết khả năng đó khi đem áp dụng cho một đợt đo khác chưa từng thấy." | "…trong phép thử thăm dò CP2↔CP3, hiệu năng phân biệt trạng thái không được duy trì khi chuyển sang đợt đo chưa từng thấy; kết quả hiện chưa thiết lập được khả năng chuyển giao (transfer) giữa hai đợt đo này." + thêm rõ trong câu giới hạn: "để không hiểu sai theo hướng ngược lại — tức không được đọc thành 'mô hình mất hoàn toàn khả năng' hay 'không thể chuyển giao được'" | Bỏ khẳng định tuyệt đối "mất hết khả năng"; nêu đúng mức độ (chưa thiết lập được) | Yêu cầu #5 |
| §12 (đóng góp) | Next action không nhắc trạng thái Gate 1 | Thêm câu: "Gói bằng chứng đã sẵn sàng về mặt khoa học cho bước này; phần còn thiếu là quy trình rà soát và ký nghiệm thu." | Thống nhất trạng thái Gate 1 | Yêu cầu #10 |
| §13 (vì sao đóng góp quan trọng) | "…Paper 1 chính là nơi xác định những thông tin bắt buộc đó là gì…" | "Paper 1 chính là nơi cung cấp **căn cứ thực nghiệm** cho việc xác định những thông tin bắt buộc đó là gì… còn việc hình thức hóa chúng thành schema chính thức… là công việc của Paper 2." + CEI: "đang được đề xuất cho giai đoạn tích hợp ở Paper 2" | Yêu cầu #6, #7 | |
| §15 (chiến lược tạp chí) | "Rủi ro… được đánh giá ở mức thấp đến trung bình." | "…được đánh giá ở mức **trung bình**." + thêm câu liệt kê vòng 1 và 4 tạp chí dự phòng | Đồng bộ với slide 17 | Yêu cầu #8, #10 |
| §16 (tình trạng hiện tại) | Không có câu trạng thái Gate 1 chuẩn ở đầu mục | Thêm: "**Gói bằng chứng Gate 1: sẵn sàng về mặt khoa học; chờ thầy rà soát và ký nghiệm thu chính thức.**" | Thống nhất trạng thái Gate 1 | Yêu cầu #10 |

---

## Kiểm tra tự động đã chạy

- `python-pptx` build lại thành công, 18 slide; qua kiểm tra cấu trúc `validate.py --original tpl.pptx` (PASS toàn bộ).
- `markitdown` dump toàn văn slide: 0 lần xuất hiện "G6", "bonus", "RQ1 + RQ2", "G1 mở", "vặn lỏng", "thấp–trung bình".
- File `.md` v2: cùng bộ kiểm tra trên đều 0 lần xuất hiện; câu "gần như mất hết" không còn.
- Xem lại trực quan (render PNG) các slide 4, 5, 9, 10, 11, 15, 16, 17: không chữ tràn khung, không chồng chữ, khoảng cách hợp lý.
- Không có ô/thẻ nào dưới 16pt.
