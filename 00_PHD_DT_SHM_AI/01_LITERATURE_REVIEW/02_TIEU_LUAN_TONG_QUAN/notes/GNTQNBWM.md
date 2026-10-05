# GNTQNBWM — García, Toledo, Aragonés & Bañón (2026) — [44]

García JA, Toledo I, Aragonés L, Bañón L. A CDE-Centered Quality Gate Framework to Operationalize ISO 19650 Governance
in Hybrid Railway Depots. *Applied Sciences* 16(5): 2562. DOI 10.3390/app16052562. Xuất bản 06/03/2026 (tr. 1).

**Bản đã đọc:** toàn văn thân bài (tr. 1–34), bản PDF của nhà xuất bản (45 tr.). Phụ lục A–D (tr. 35–44) đọc phần lời
và tiêu đề bảng; không đọc từng dòng số liệu của các bảng A1–A4. Các hình chỉ đọc qua chú thích. Đọc ngày 30/09/2026,
phiên T1-1. Tài liệu năm 2026: không dùng làm căn cứ chính cho một khoảng trống (CLAUDE.md 4.1).

Ký hiệu: (a) điều tác giả nói; (b) giới hạn tác giả tự nêu; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | GNTQNBWM / [44] |
| Tier / Cụm | Tier 1 / Truy vết thông tin |
| Luận điểm | Trong môi trường dữ liệu chung (CDE) theo ISO 19650, bước chuyển Shared → Published cần được biến thành một quyết định "công bố/giữ lại" cho từng tệp IFC theo từng phiên bản, dựa trên một gói bằng chứng lưu trong CDE và do các vai trò tách biệt thực hiện (tr. 1, 3, 12). |
| Bằng chứng | Kiểm chứng thủ tục trên 22 tệp IFC (IFC2x3) của hai đề-pô đường sắt ở Tây Ban Nha; 8/22 tệp đạt cả ba nhóm kiểm tra, 14/22 bị giữ lại (tr. 10–11, 27–29). |
| Giới hạn | Xem mục 5. |
| Tác động K1/K2/K3 | K3: thu hẹp về khuôn mẫu (bước chuyển trạng thái có bằng chứng và thẩm quyền đã có tiền lệ, cho gói thông tin). K2: thu hẹp một phần (truy vết tệp – bằng chứng – vấn đề – quyết định). K1: không liên quan trực tiếp. |
| Vị trí sử dụng | 2.1–2.2 (quản trị thông tin theo ISO 19650, trạng thái CDE); 4.5 (trạng thái và thẩm quyền); 5.5 (tiền lệ của ràng buộc bước chuyển có căn cứ và đúng thẩm quyền); Phụ lục ánh xạ. |
| Mức đã đọc | Toàn văn thân bài; phụ lục đọc phần lời |

## 1. Câu hỏi nghiên cứu và đối tượng

- Ba câu hỏi (tr. 5): làm sao để bước Shared → Published thành quyết định truy vết được ở mức tệp IFC; dùng Đơn vị chức
  năng (Functional Unit, FU) thế nào để ổn định giao diện và giữ liên tục từ mô hình thông tin dự án (PIM) sang mô hình
  thông tin tài sản (AIM); đặc tả cổng chất lượng thế nào thành thủ tục kiểm toán được.
- Đối tượng: **gói thông tin bàn giao** (tệp IFC theo phiên bản) của xưởng và đề-pô đường sắt, nơi có cả nhà, hệ cơ điện –
  công nghiệp và hạ tầng tuyến (tr. 2–3). Giai đoạn: thiết kế, thi công, hoàn công. Không có dữ liệu vận hành hay quan trắc.
- Bối cảnh: chủ đầu tư Ferrocarrils de la Generalitat Valenciana (FGV), có Sổ tay BIM riêng (tr. 4, 21).

## 2. Phương pháp và kiến trúc thông tin

- Chuỗi "yêu cầu → sản phẩm kiểm tra → quyết định": yêu cầu thông tin của chủ đầu tư và kế hoạch thực hiện BIM được
  dịch thành luật kiểm, bằng chứng lưu giữ, vai trò chịu trách nhiệm và bước chuyển trạng thái (tr. 11–13, Bảng 4).
- **Trạng thái theo ISO 19650** (tr. 3, 21, 23): WIP là phát triển nội bộ, từng bộ môn tự kiểm; Shared là nơi phối hợp
  liên bộ môn, chạy cổng chất lượng và đóng các điểm không phù hợp; Published là thông tin đã được xác nhận và cho phép,
  có ý nghĩa hợp đồng; Archived giữ lịch sử phiên bản và quyết định. Bước Shared → Published là "sự kiện được quản trị".
- **Cổng chất lượng kiểm gì** (tr. 15–17, Bảng 5), ba nhóm không bù trừ cho nhau:
  - *Không gian:* có thông tin gốc tọa độ; khoảng cách điểm neo tới điểm tham chiếu của gói trong dung sai (5 m cho nhà và
    cơ điện, 20 m cho tuyến và hạ tầng); hướng bắc không lệch khỏi các tệp cùng gói; thang hình học hợp lệ.
  - *Ngữ nghĩa:* tỷ lệ phần tử chung chung/thay thế (proxy) dưới 50 %.
  - *Dữ liệu:* đủ nhóm thuộc tính bắt buộc theo giai đoạn; với gói tuyến, có lý trình và tham chiếu tim tuyến.
  - Quyết định: đạt cả ba thì công bố, nếu không thì giữ lại. Ngưỡng là ranh giới vận hành, không phải giá trị tối ưu (tr. 17).
- **Ai phê duyệt** (tr. 12, 21–25, Bảng 7): người điều phối BIM hoặc văn phòng kỹ thuật BIM chạy cổng và lập gói bằng
  chứng; người phụ trách BIM của giai đoạn ký xác nhận kỹ thuật; người phụ trách hợp đồng của chủ đầu tư phê duyệt
  chuyển sang Published. Nguyên tắc tách nhiệm vụ: người tạo thông tin không xác nhận, người xác nhận không cho phép công bố (tr. 23).
- **Gói bằng chứng** cho mỗi tệp và phiên bản (tr. 3, 19–21, Bảng 6): báo cáo mức tệp, tóm tắt mức gói, bản ghi quyết
  định, tham chiếu tới báo cáo không phù hợp (NCR) và vấn đề BCF. Siêu dữ liệu tối thiểu: định danh, bộ môn, giai đoạn,
  trạng thái, phiên bản và ngày, tác giả và tổ chức, gói hợp đồng, FU; khuyến nghị thêm phần mềm xuất và mã băm của tệp (tr. 17–20).
- **Vòng xử lý không phù hợp** (tr. 22, 24): mở vấn đề, giao người sửa, phát hành phiên bản mới, chạy lại cổng, đóng và
  xác minh trước khi đề nghị công bố.
- **Bảng đối chiếu theo thời gian (crosswalk)** (tr. 25–27, Bảng 8): ghi đường cơ sở yêu cầu nào áp cho từng giai đoạn;
  có phiên bản, ngày, người lập; khi đóng kỳ thì "đóng băng", sửa sau ghi thành phiên bản mới, không viết lại quyết định cũ.
- Chuẩn: ISO 19650-1/2/3, IFC (ISO 16739-1), IDS, BCF, LOIN. Không dùng SOSA/SSN, PROV-O, SHACL.

## 3. Cách kiểm chứng

- Dữ liệu thật: 22 tệp IFC từ CDE của chủ đầu tư, hai dự án (El Campello, Nazaret), ba trạng thái tài sản (hiện trạng,
  thiết kế, đã thi công) (tr. 10–11, Bảng 3). Mục tiêu là kiểm chứng thủ tục (chạy được, kiểm toán được), không suy
  luận thống kê (tr. 11).
- Chỉ số: tỷ lệ đạt từng nhóm và đạt cả ba theo từng trường hợp (25,0 % đến 44,4 %) (tr. 28, Bảng 9); phân bố nguyên
  nhân bị giữ (tr. 29, Hình 7); phân tích độ nhạy ±10 % của ngưỡng (Phụ lục C, tr. 43).
- So sánh: với các logic quyết định một chiều giả định (chỉ dữ liệu 72,7 %, chỉ không gian 63,6 %, chỉ ngữ nghĩa 54,5 %,
  cả ba 36,4 %) (tr. 29, Bảng 10). Không so với thực hành hiện hành của chủ đầu tư và không đo lợi ích về sau (tr. 32).

## 4. Luận điểm chính

1. ISO 19650 cho khung trạng thái và vai trò, nhưng không quy định cổng kiểm tính toán được hay gói bằng chứng tối
   thiểu ở mức tệp; nếu không có, Published dễ thành mốc hành chính (tr. 3, 9 Bảng 2).
2. Kết quả kiểm tra mô hình chỉ có giá trị khi nằm trong một mạch quản trị: ai quyết định, bằng chứng nào được lưu,
   điểm không phù hợp được ghi và đóng thế nào (tr. 4, 7, 29).
3. Ba nhóm rủi ro không gian, ngữ nghĩa và dữ liệu không bù trừ cho nhau; khả năng công bố do nhóm yếu nhất quyết định
   (tr. 15, 29–30).
4. FU được đưa thành siêu dữ liệu của gói trong CDE (ngoài thuộc tính ở phần tử IFC) để cấu trúc theo vận hành tham gia
   vào quyết định công bố và giữ liên tục PIM → AIM (tr. 14–15, 29–30).
5. Chuyển từ bàn giao (ISO 19650-2) sang quản lý trong vận hành (ISO 19650-3) thường không liên tục; mô hình mất giá trị
   nhanh sau nghiệm thu nếu không có tiêu chí cập nhật và trách nhiệm dài hạn (tr. 3–4, 23).

### Bài có khái niệm bằng chứng tình trạng công trình không?

**Không.** "Bằng chứng" trong bài là bằng chứng kiểm tra chất lượng của **gói thông tin** (báo cáo kiểm, bản ghi quyết
định, vấn đề), dùng để biện minh việc công bố một tệp (tr. 3 Bảng 1, 19). Tìm trong văn bản không có cảm biến, quan trắc,
tình trạng kết cấu, kiểm tra hiện trường, nguồn gốc dữ liệu đo hay độ bất định. Bài nói mô hình tài sản cần truy vết
các can thiệp bảo trì (tr. 4, 23) nhưng không mô hình hóa chúng.

## 5. Giới hạn

**(b) Tác giả tự nêu:**
- Tập mẫu nhỏ: hai đề-pô ở Tây Ban Nha, 22 tệp; tỷ lệ đạt chỉ mang tính chỉ báo (tr. 11, 32, 34).
- Tỷ lệ phần tử thay thế chỉ là đại lượng gần đúng cho suy giảm ngữ nghĩa và phụ thuộc cách xuất tệp (tr. 32).
- Ngưỡng là ranh giới vận hành; tệp sát ngưỡng có thể đổi kết quả (tr. 17, 32).
- Chưa đo lợi ích về sau (giảm làm lại, tiến độ, chi phí) (tr. 32).
- Phụ thuộc chất lượng tệp IFC và bộ xuất; IFC2x3 hạn chế ngữ nghĩa với hạ tầng tuyến (tr. 33).
- Cổng phân loại được tệp nhưng không thay cho phân tích nguyên nhân gốc (tr. 33).
- Công việc sau: tự động hóa trong CDE, IFC 4.3, IDS, gắn chặt hơn với AIM và quản lý vận hành (tr. 34).

**[NCS] nhận định:**
- Đối tượng quản trị là tệp bàn giao, không phải tình trạng cấu kiện; giai đoạn vận hành mới ở mức định hướng.
- Kiểm chứng là chạy cổng trên một ảnh chụp các tệp; bài không cho thấy vòng sửa – phát hành lại – chạy lại đã diễn ra,
  cũng không có bản ghi quyết định thật của các vai trò.
- Dữ liệu gốc và tài liệu quản trị không công khai (tr. 34).
- Tạp chí MDPI, xuất bản 03/2026; cần dùng thận trọng theo quy tắc tài liệu 2025–2026.

## 6. Điều bài KHÔNG xử lý, xét theo chuỗi của luận án

| Ý | Mức | Căn cứ |
|---|---|---|
| Nguồn gốc bằng chứng cảm biến | không xử lý | Không có cảm biến. Có nguồn gốc của **tệp**: phiên bản, tác giả, phần mềm xuất, mã băm (tr. 17–20) |
| Phạm vi hiệu lực của bằng chứng | xử lý một phần ([NCS], tương tự về ý) | Bảng đối chiếu ghi đường cơ sở yêu cầu mà trong đó một quyết định còn so sánh được (tr. 25–27); không phải phạm vi hiệu lực của nhận định về tình trạng |
| Quan hệ bằng chứng – cấu kiện có thời hạn | không xử lý | Bằng chứng gắn với tệp và phiên bản (tr. 19–21); phần tử IFC chỉ mang FU và vị trí kỹ thuật (tr. 14) |
| Trách nhiệm, thẩm quyền | có xử lý | Ma trận RACI, tách nhiệm vụ, hai cấp ký (tr. 21–25, Bảng 7) |
| Trạng thái hành động và lịch sử chuyển trạng thái | có xử lý, cho trạng thái thông tin | Bước Shared → Published có bản ghi quyết định; vấn đề NCR/BCF có trạng thái, người chịu trách nhiệm, ngày (tr. 12–13, 20, 24) |
| Truy ngược từ hành động về dữ liệu gốc | xử lý một phần | Liên kết bền: tệp → báo cáo → tóm tắt gói → NCR/BCF → bản ghi quyết định → trạng thái (tr. 21); điểm cuối là tệp IFC, không phải dữ liệu đo |

## 7. Tác động tới K1/K2/K3

- **K3: thu hẹp về khuôn mẫu.** Ý "mỗi bước chuyển trạng thái phải có bằng chứng lưu giữ, đúng vai trò, tái dựng được
  ai, khi nào, dựa vào đâu" đã được phát biểu và thử cho gói thông tin (tr. 3, 24, 33). Phần còn lại cho luận án: áp
  khuôn mẫu đó cho **hành động kiểm tra – bảo trì** dựa trên **bằng chứng tình trạng** có phạm vi hiệu lực. Tác giả tự
  nêu khoảng đứt giữa bàn giao và vận hành (tr. 3–4, 23) và để phần gắn với quản lý vận hành cho công việc sau (tr. 34).
- **K2: thu hẹp một phần.** Chuỗi liên kết bền tệp – bằng chứng – vấn đề – quyết định là tiền lệ về truy vết (tr. 21).
- **K1: không liên quan trực tiếp.** Ý "điều kiện mà quyết định còn so sánh được" của bảng đối chiếu là một tương tự xa.

## 8. Vị trí sử dụng trong tiểu luận v2

- 2.1–2.2: trạng thái CDE và ý nghĩa của Published; khoảng đứt ISO 19650-2 → 19650-3 (nêu là nhận định của [44]).
- 4.5 và 5.5: tiền lệ cho ràng buộc "bước chuyển có căn cứ và đúng thẩm quyền" và tách nhiệm vụ.
- Không dùng [44] làm căn cứ chính cho khoảng trống (tài liệu 2026); không dùng số liệu tỷ lệ đạt ngoài bối cảnh đề-pô.
- Bảng ánh xạ: `mapping/garcia2026.md`.
