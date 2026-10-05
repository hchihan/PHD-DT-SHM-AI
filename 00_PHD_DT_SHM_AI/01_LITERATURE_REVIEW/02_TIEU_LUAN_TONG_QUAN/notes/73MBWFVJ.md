# 73MBWFVJ — Mosqueira-Rey và cs. (2023)

Mosqueira-Rey E, Hernández-Pereira E, Alonso-Ríos D, Bobes-Bascarán J, Fernández-Leal Á. Human-in-the-loop machine learning:
a state of the art. *Artificial Intelligence Review* 56(4): 3005–3054, 2023 (trực tuyến 17/08/2022). DOI
10.1007/s10462-022-10246-w (Crossref xác minh 01/10/2026). Truy cập mở, CC BY 4.0.

**Bản đã đọc:** bản chính thức, tệp `pdf/73MBWFVJ_MosqueiraRey2023.pdf` (50 tr. PDF = tr. 3005–3054; tải từ Springer). Đọc
ngày 01/10/2026 có trọng tâm cho kiểm phản chứng UV-07 (N-24): toàn văn phần mở đầu (tr. 3005–3008), các mục "shortcomings"
của học chủ động và học tương tác (tr. 3012, 3021), mục 7 "Usable and useful AI" (tr. 3039–3042), mục 8 kết luận (tr. 3042–3045);
các mục kỹ thuật về học chủ động, dạy máy, học theo giáo trình, AI giải thích được (tr. 3008–3038) đọc lướt và tìm từ khóa
(accountab, responsib, audit, provenance, record, log, trust, noisy oracle). Trang dẫn theo bản in.

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | 73MBWFVJ / mới (phanchung-GD2) |
| Tier / Cụm | Bổ sung phản chứng (không thuộc 30 key) / Giá trị quyết định |
| Luận điểm | Học máy có người trong vòng (HITL-ML) được phân loại theo ai kiểm soát quá trình học: học chủ động (hệ kiểm soát, người là "oracle" gán nhãn), học máy tương tác (tương tác chặt, gia tăng), dạy máy (chuyên gia miền kiểm soát); thêm học theo giáo trình và AI giải thích được (tr. 3005–3006). |
| Bằng chứng | Tổng quan tài liệu, sơ đồ tư duy cho từng hướng, danh mục ứng dụng (y sinh, ảnh, chuỗi thời gian, ngôn ngữ). Không có thực nghiệm. |
| Giới hạn | Xem mục 3. |
| Tác động K1/K2/K3 | K3 (UV-07): căn cứ cùng chiều — xác nhận của con người được mô tả là đóng góp cho **quá trình học**; chất lượng nhãn là vấn đề mở. K1, K2: không liên quan. |
| Vị trí sử dụng | 5.6A (vòng lặp kiểm tra tạo nhãn: nhãn kỹ sư có thể sai, "noisy oracle"); 3.6 (vai trò của kỹ sư khi gán nhãn hiện trường); 5.2 (căn cứ cho khoảng trống về ghi xác nhận như bản ghi trách nhiệm, nếu NCS chấp nhận). |
| Mức đã đọc | Toàn văn phần liên quan; phần kỹ thuật đọc lướt (01/10/2026) |

## 1. Các ý chính (a)

- Ba cách đưa người vào vòng học khác nhau ở **ai kiểm soát quá trình học**; với học chủ động, hệ "treats humans as oracles to
  annotate unlabeled data" (tr. 3006). Ở mục 7, vai trò của người được tóm lại: "humans can be oracles who are responsible for
  labeling data unknown to the model (AL), they can interact with the model … (IML) or they can act as teachers … (MT)" (tr. 3039).
- Sau khi triển khai, người dùng có thể gửi **sửa lỗi**, dùng để sinh thêm dữ liệu huấn luyện, cải thiện dần hiệu năng (tr. 3040).
- **Oracle có nhiễu** (noisy oracles): thường giả định nhãn từ oracle có chất lượng cao, nhưng có mẫu khó với cả người; người có
  thể mất tập trung, mệt mỏi, làm chất lượng nhãn biến thiên; còn phải quyết định khi nào một nhãn đáng tin, khi nào hỏi nhiều
  oracle (tr. 3012).
- Học tương tác phụ thuộc vào sự có mặt của chuyên gia (sẵn có, chú ý, khác biệt chuyên môn) (tr. 3021); thành phần con người
  giúp "re-traceability" và khả năng giải thích (tr. 3021).
- Mô hình có thể suy giảm, "no longer valid if the context changes" sau khi triển khai (tr. 3040; cũng tr. 3006).
- "Accountability" chỉ xuất hiện như một thuộc tính của AI "hữu ích", cùng độ bền vững, công bằng, minh bạch (tr. 3044); hướng dẫn
  về AI giải thích được nêu kế hoạch giải thích có phân vai trò và trách nhiệm trong nhóm phát triển (tr. 3038).

## 2. Đoạn dùng được cho tiểu luận

| Luận điểm trong tiểu luận | Trang | Loại |
|---|---|---|
| Trong học máy có người trong vòng, người chủ yếu đóng vai nguồn nhãn, người tương tác hoặc người dạy mô hình | 3006, 3039 | trực tiếp |
| Sửa lỗi của người dùng sau triển khai được dùng làm dữ liệu huấn luyện bổ sung | 3040 | trực tiếp |
| Nhãn do người cung cấp có thể sai, chất lượng biến thiên; cách quyết định nhãn đáng tin còn để ngỏ | 3012 | trực tiếp (TG) |
| Xác nhận của kỹ sư cần được ghi đồng thời như bản ghi trách nhiệm và như nhãn hiện trường có độ bất định | — | diễn giải của NCS |

## 3. Giới hạn

- (b) Các giả định của học chủ động không luôn đúng (truy vấn theo lô, oracle có nhiễu, chi phí nhãn thay đổi, …) (tr. 3012);
  học tương tác trộn yếu tố học máy với tương tác người – máy, cần nỗ lực phát triển lớn (tr. 3021); thuật ngữ và mục tiêu của AI
  giải thích được chưa thống nhất (tr. 3035).
- **[NCS]** Tổng quan thiên về y sinh, ảnh, ngôn ngữ; không có công trình, kiểm tra kết cấu hay bảo trì. Không mục nào bàn việc ghi
  lại lần xác nhận/sửa của người (ai, vai trò, thẩm quyền, thời điểm, căn cứ) như một bản ghi có giá trị giải trình; trách nhiệm
  được bàn ở mức thiết kế hệ và nhóm phát triển (tr. 3038), không ở mức từng đầu ra.

## 4. Kiểm phản chứng

- **UV-07: không giải quyết; căn cứ cùng chiều (TG mô tả + [NCS]).** Bài tổng quan xếp vai trò của người theo mức kiểm soát
  **quá trình học** (tr. 3006, 3039) và coi xác nhận/sửa của người là nguồn dữ liệu huấn luyện (tr. 3040); chất lượng nhãn là vấn
  đề mở (tr. 3012). Không có hướng nào ghi lần xác nhận như bản ghi trách nhiệm gắn với đầu ra đã xác nhận. Đề xuất NCS tính là
  **căn cứ độc lập thứ năm** của UV-07 (nhóm A Coruña, 2023, trước 2025; dạng tổng quan).
- **UV-05 (nhãn hiện trường):** cùng chiều — nhãn của người có độ bất định và cần cách đánh giá độ tin của nhãn (tr. 3012); không
  tính căn cứ mới (UV-05 đã đủ).
