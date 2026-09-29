# Báo cáo nguồn cho mục Công cụ AI (5.6A)

Ngày: 29/09/2026. Dữ liệu chi tiết: `revision/nguon_5_6A_ung_vien.csv` (29 ứng viên) và
`revision/nguon_5_6A_kiem_ke.csv` (9 tài liệu phương pháp, Việc 1).

Cách làm: tìm ứng viên bằng Consensus (17 truy vấn), xác minh từng ứng viên qua Crossref
(tiêu đề, tác giả, năm, tạp chí, tập/trang, DOI), rồi tra bản sao chỉ-đọc `zotero.sqlite`.
Đề xuất nhận hoặc dự phòng dựa trên **tóm tắt**, chưa đọc toàn văn. Mọi nội dung trích vào
5.6A vẫn phải đối chiếu với đoạn tương ứng trong bản gốc (quy tắc 4.1).

## 1. Tổng hợp theo nhóm

| Nhóm | Nội dung | Ứng viên | Crossref xác minh | Đề xuất nhận | Đã có trong Zotero | Cần nhập Zotero |
|---|---|---|---|---|---|---|
| G1 | Autoencoder cho SHM | 5 | 5 | 3 | 0 | 3 |
| G2 | Bù EOV | 5 | 5 | 2 | 0 | 2 |
| G3 | Học chủ động | 5 | 5 | 3 | 0 | 3 |
| G4 | ResNet cho chuỗi thời gian | 4 | 4 | 3 | 0 | 3 |
| G5 | 1D-CNN trong SHM dao động | 5 | 5 | 3 | 3 | 1 |
| G6 | LLM trích xuất hồ sơ kiểm tra | 5 | 5 | 2 | 0 | 2 |
| **Cộng** | | **29** | **29** | **16** | **3** | **14** |

Ở G5, ba bài đã có trong Zotero là Kiranyaz và cs. 2021 (IU5KZQEA), Avci và cs. 2021
(QUGY4928) và Pal và cs. 2022 (SL6IEB2E, số [48] trong danh mục). Pal được để dự phòng vì
tác giả dùng CNN trên ảnh scalogram chứ không dùng 1D-CNN.

Không ứng viên nào bị loại vì không xác minh được. Tất cả gợi ý của NCS đều khớp Crossref:
Pathirage 2018, Figueiredo 2011, Cross/Worden/Chen 2011, Bull 2018 và 2019,
Wang/Yan/Oates 2017, Abdeljaber 2017. Năm theo Crossref khác Consensus ở năm bài: Wang & Cha
(2021), Shang (2021), Maes (2022), Hughes (2022), Ismail Fawaz (2019). Danh sách dùng năm
Crossref.

## 2. Danh sách đề xuất nhập Zotero (chờ NCS duyệt)

Thứ tự ưu tiên dựa trên mức phục vụ trực tiếp lập luận chính của 5.6A: vì sao chuyển vai AI từ
phân loại ở PTN sang phát hiện bất thường ở hiện trường, và vòng lặp kiểm tra tạo nhãn.

| Ưu tiên | Nhóm | Tài liệu | DOI | Lý do chọn |
|---|---|---|---|---|
| 1 | G2 | Figueiredo và cs. (2011), *Structural Health Monitoring* 10(6): 559–572 | 10.1177/1475921710388971 | Nền tảng về tách hư hỏng khỏi biến động vận hành – môi trường; hư hỏng được mô tả là tương tự liên kết lỏng |
| 2 | G1 | Wang & Cha (2021), *Structural Health Monitoring* 20(1): 406–425 | 10.1177/1475921720934051 | Autoencoder chỉ huấn luyện trên dữ liệu kết cấu nguyên vẹn |
| 3 | G3 | Hughes và cs. (2022), *MSSP* 167: 108569 | 10.1016/j.ymssp.2021.108569 | Coi mỗi truy vấn nhãn là một lần kiểm tra kết cấu |
| 4 | G3 | Bull và cs. (2022), *Proc. R. Soc. A* 478: 20210790 | 10.1098/rspa.2021.0790 | Quản lý chi phí kiểm tra; dùng dữ liệu cầu hiện trường |
| 5 | G5 | Abdeljaber và cs. (2017), *J. Sound Vib.* 388: 154–170 | 10.1016/j.jsv.2016.10.043 | Nền tảng 1D-CNN trên tín hiệu gia tốc thô |
| 6 | G1 | Zhang và cs. (2023), *Eng. Struct.* 283: 115873 | 10.1016/j.engstruct.2023.115873 | CAE huấn luyện bằng dao động vận hành của một nhà đang khai thác |
| 7 | G2 | Cross, Worden & Chen (2011), *Proc. R. Soc. A* 467: 2712–2732 | 10.1098/rspa.2011.0023 | Nền tảng cointegration; bù EOV mà không cần đo biến môi trường |
| 8 | G1 | Ghazimoghadam & Hosseinzadeh (2024), *Measurement* 229: 114410 | 10.1016/j.measurement.2024.114410 | Autoencoder học trạng thái chưa hư hỏng, có ca lỏng bu lông liên kết |
| 9 | G3 | Bull và cs. (2018), *J. Sound Vib.* 437: 373–388 | 10.1016/j.jsv.2018.08.040 | Nền tảng học chủ động trong SHM |
| 10 | G4 | Wang, Yan & Oates (2017), *IJCNN 2017*: 1578–1585 | 10.1109/ijcnn.2017.7966039 | ResNet làm mô hình cơ sở cho phân loại chuỗi thời gian |
| 11 | G4 | Ismail Fawaz và cs. (2019), *DMKD* 33(4): 917–963 | 10.1007/s10618-019-00619-1 | So sánh thực nghiệm lớn các kiến trúc học sâu, trong đó có ResNet |
| 12 | G6 | Zhang và cs. (2024), *Dev. Built Environ.* 20: 100549 | 10.1016/j.dibe.2024.100549 | LLM trích xuất báo cáo kiểm tra, có đo độ chính xác trích xuất |
| 13 | G4 | He và cs. (2016), *CVPR 2016*: 770–778 | 10.1109/cvpr.2016.90 | Nguồn gốc khối dư (chỉ dùng cho định nghĩa kiến trúc) |
| 14 | G6 | Xu và cs. (2024), *Front. Comput. Sci.* 18(6): 186357 | 10.1007/s11704-024-40555-y | Tổng quan LLM cho trích xuất thông tin |

Nếu NCS muốn giới hạn chặt hơn, có thể bỏ trước các mục 13 và 14. He 2016 chỉ phục vụ định
nghĩa; Xu 2024 là tổng quan chung, không thuộc xây dựng.

Còn bốn tài liệu phương pháp từ Việc 1 đã được xác minh nhưng chưa có trong Zotero. Chúng nằm
ngoài G1–G6 và cũng chờ duyệt nhập: Breiman 2001 (RF), Cortes & Vapnik 1995 (SVM),
Varma & Simon 2006 (thiên lệch chọn mô hình), Vabalas và cs. 2019 (đánh giá với mẫu nhỏ).

## 3. Các nhóm chưa có nguồn đủ tin cậy cho một phần lập luận

- **G6 – LLM trích xuất hồ sơ kiểm tra.** Nguồn tìm được là cầu (Zhang 2024; Wang 2024), nhà
  dân dụng (Urlainis 2025, 16 báo cáo) hoặc vấn đề giai đoạn tiền thi công (Girgin 2026).
  Chưa có nguồn về hồ sơ kiểm tra nhà công nghiệp khung thép. Hầu hết tài liệu LLM thuộc
  2024–2026. Nên viết vai trò LLM ở 5.6A như một công cụ hỗ trợ có kỹ sư xác nhận, có đo độ
  chính xác trích xuất, và không đặt lập luận chính lên nhóm này. `[CẦN NGUỒN]` nếu muốn nói
  riêng về nhà công nghiệp.
- **G1 – Autoencoder ở nhà công nghiệp thép.** Chưa có nguồn autoencoder trên nhà xưởng thép
  có cầu trục hoặc máy móc. Nguồn gần nhất là một nhà thi đấu cách chấn (Zhang 2023) và các
  kết cấu PTN có ca lỏng bu lông (Ghazimoghadam 2024). Việc chuyển sang nhà xưởng là diễn
  giải của NCS và cần được viết rõ như vậy.
- **G4 – ResNet1D trong SHM trên tín hiệu thô.** Chưa tìm được nguồn có phản biện dùng
  ResNet1D trên tín hiệu dao động thô cho SHM công trình. Wang và cs. (2021) dùng dạng dao
  động. Căn cứ cho ResNet1D tạm dựa vào tài liệu phân loại chuỗi thời gian nói chung (Wang/Yan/
  Oates 2017; Ismail Fawaz 2019).
- **G3 – Học chủ động ở công trình xây dựng.** Các nguồn mạnh nhất cùng một nhóm tác giả
  (Sheffield: Bull, Hughes, Worden) và dữ liệu là cầu hoặc máy bay. Có thể dùng làm căn cứ
  phương pháp. Việc áp dụng cho nhà công nghiệp là đề xuất của luận án.
- **G2** và **G5** có nguồn nền tảng đủ tin cậy.

## 4. Việc cần NCS quyết định

1. Duyệt danh sách mục 2 (14 tài liệu G1–G6 và 4 tài liệu phương pháp từ Việc 1) trước khi
   nhập Zotero.
2. Quyết định collection đích khi nhập: `TL-Key` hay một collection riêng cho 5.6A.
   *Đính chính 29/09 (phiên nhập):* `TL-Key` (PRGXUPFZ) và `TL-Key/Bổ sung` (TKVJVWDZ) đã tồn tại;
   ghi "chưa tạo" ở bản trước là sai. NCS đã chọn `TL-Key/Bổ sung`.
3. Xác nhận cách viết cho G6 và phần chuyển sang nhà xưởng ở G1 (mục 3).
