# GĐ3b: Khoảng trống và ba mục tiêu, bản hiệu chỉnh (chờ NCS duyệt, gửi thầy)

Lập ngày 01/10/2026 theo `prompt_GD3b_cap_nhat_muc_tieu.md` (D1–D8). Không ghi đè bản 01/10
(`revision/GD3_khoang_trong_va_muc_tieu.md`, commit `62f1695`) và không sửa `tieuluan/`.

- **Đã đọc:** `CLAUDE.md` (commit `5bd3eb2`; mục 2, 2A, 6.2, 8, 11, 13); bản GĐ3 01/10 (toàn bộ);
  `revision/GD2_nhat_ky_khoang_trong.md`.
- **Ghi chú đã mở để kiểm D1, D2:** `RWHW6F9I` [19], `RG9FMT8Y` [15], `L97BIAI3` [14], `JQKJGUER` [53],
  `IW7JBB3E` [56], `SL6IEB2E` [48], `VVBGM9EN` Eraliev 2022, `VPFBB9SG` [18], `2ZJSENQU` Maes 2022,
  `82WQNDHU` Mitchell 2019, `73MBWFVJ` Mosqueira-Rey 2023, `lebo2013provo` [69], `GNTQNBWM` [44], `B2JXAM9M` [22].
- Không đọc tài liệu ngoài `notes/`.
- **Ký hiệu:** TG = tác giả tự nêu; [NCS] = nhận định của NCS từ việc tài liệu không xử lý một ý.
- **Lưu ý trang dẫn:** Mitchell 2019 theo bản arXiv, Maes 2022 theo bản postprint, [19] theo bản tiền in arXiv v1,
  Eraliev 2022 theo bản MDPI.

**Một mâu thuẫn với CLAUDE.md:** D4 (thêm đối chứng B1) trái với CLAUDE.md mục 8 ("Bỏ B1") và mục 11 (không thêm ngoài
mục 2A và 8). Theo mục 5 của prompt, phần B1 dừng lại, ghi ở Phần F (F-1) kèm văn bản sẵn sàng thay thế.
Các phần còn lại của D4 không mâu thuẫn nên đã áp dụng: M2 là chỉ số chính, báo cáo M2 theo nhóm lỗi, giới hạn của M1 so với B0.

## Bảng kiểm

### Kiểm theo ứng viên

Giữ nguyên bảng của bản 01/10 (UV-02, UV-06, UV-01, UV-05, UV-07, UV-03, UV-08, UV-04); không thay đổi nội dung.
Bảng dưới chỉ ghi phần thêm cho **A1** (D1).

| Vế | Vào | Căn cứ độc lập trước 2025 (theo nhóm tác giả, kèm trang) | Nguồn 2025–2026 | Phản chứng đã kiểm | Phát biểu đã thu hẹp |
|---|---|---|---|---|---|
| A1 | G-A | Hiện tượng "con số hiệu năng phụ thuộc đơn vị chia dữ liệu": [18] tr. 283, 292 (TG; lắp lại làm dữ liệu cũ mất tác dụng, độ lặp lại giữa các lần lắp); [14] tr. 1, 3–5 (TG; chia theo phổ thay vì theo đơn vị độc lập cho kết quả lạc quan); [15] tr. 169879–169881, 169889–169892 (TG; chia theo lần chạy so với theo ngày, theo chi tiết); [53] tr. 3–6 (TG; rò rỉ làm hiệu năng lạc quan); [56] tr. 011102-1, -4 (TG, gián tiếp; bộ phân loại học trên một mẫu thất bại ở mẫu khác). Năm nhóm. | [19] (2025, tiền in; cùng nhóm Teloli với [56], không tính thêm) | [19] tr. 2, 12–14: **giải quyết một phần**. Đã định lượng chênh lệch cùng đợt và để riêng đợt cho phát xạ âm trên dầm nhôm ba bu lông M4: khoảng 99 % so với 26–35 % ở cấu hình cơ sở. [15]: giải quyết cho ổ trục, không cho liên kết bu lông. [48] tr. 3–9 và Eraliev 2022 tr. 5, 12: chia tập trong cùng lần lắp ráp hoặc cùng bản ghi, không báo chênh lệch ([NCS]). [56]: định lượng giữa các mẫu, không giữa các lần chạy của cùng mẫu. | Mức chênh lệch đã được định lượng cho phát xạ âm trên dầm nhôm nối bu lông [19] và cho chẩn đoán ổ trục [15]. Với phân loại trạng thái liên kết bu lông **dựa trên dao động trong khung thép**, các nghiên cứu đã rà soát chia tập trong cùng lần lắp ráp hoặc cùng bản ghi ([48], Eraliev 2022), nên mức chênh lệch chưa được báo cáo. |

### Kiểm ở cấp khoảng trống (thêm cột A1)

| Tiêu chí | A1 | A2 (= G-A của bản 01/10) | G-B |
|---|---|---|---|
| (i) ≥ 3 căn cứ độc lập ngoài nhóm 2025–2026 | **Đạt** cho hiện tượng (5 nhóm). Vế "chưa báo cáo cho khung thép dao động" dựa trên 2 nghiên cứu đã đọc, loại [NCS] | Đạt (bản 01/10) | Đạt (bản 01/10) |
| (ii) Không còn "chưa kiểm" | **Đạt trong phạm vi tài liệu đã đọc.** Không tìm kiếm có hệ thống thêm (QĐ 11) | Đạt | Đạt có điều kiện (CMMS qua nguồn thứ cấp) |
| (iii) Mọi trang dẫn có trong `notes/` | **Đạt** (đã dò các trang ở bảng trên) | Đạt | Đạt |

**Kết luận D1:** A1 đạt, nên A1 và A2 được trình bày là hai vế của G-A. Phát biểu A1 phải thu hẹp so với D1:
không viết "chưa được định lượng cho bài toán này" chung chung, vì [19] đã định lượng cho phát xạ âm.

**[NCS] Lưu ý cho Bài 1:** [19] và [15] là hai công trình gần nhất, phải nêu trong phần tổng quan của Bài 1. Phần mới của Bài 1
là ba điều cộng lại:
- tín hiệu dao động trên khung thép nhiều liên kết;
- bốn họ mô hình;
- khai báo phạm vi hiệu lực cho từng kết quả.

## Phần A. Khoảng trống

### G-A. Bằng chứng trạng thái có phạm vi hiệu lực

**A1 – Đánh giá.** Con số hiệu năng của bộ phân loại trạng thái liên kết bu lông phụ thuộc đơn vị dùng để chia dữ liệu
(lần chạy, đợt, lần lắp ráp). Các căn cứ:
- Sau mỗi lần lắp lại khi bảo trì, phần lớn dữ liệu đáp ứng đã thu mất tác dụng cho theo dõi trạng thái ([18] tr. 283, TG).
- Chia tập theo đơn vị thấp hơn đơn vị độc lập cho kết quả lạc quan ([14] tr. 1, 3–5; [15] tr. 169889–169892; [53] tr. 3–6; TG).

Mức chênh lệch giữa đánh giá giữ lại cả lần chạy và đánh giá cùng lần chạy đã được định lượng cho phát xạ âm trên dầm nhôm
nối bu lông ([19] tr. 12–14, TG, tiền in 2025) và cho chẩn đoán ổ trục ([15]). Với phân loại dựa trên dao động của liên kết
bu lông trong khung thép, các nghiên cứu đã rà soát chia tập trong cùng lần lắp ráp hoặc cùng bản ghi ([48] tr. 3–9;
Eraliev 2022 tr. 5, 12; [NCS]). Mức chênh lệch đó vì vậy chưa được báo cáo cho bài toán này.

**A2 – Khai báo.** Trong các tài liệu đã rà soát, phạm vi hiệu lực và độ bất định chưa là trường bắt buộc của từng bằng chứng,
có lần lắp ráp – can thiệp và điều kiện vận hành làm thành phần, và chưa được kiểm tại lần sử dụng. Phần đã được giải quyết và
phần còn thiếu giữ như bản 01/10 (PROV-O [69], SSN `ssn-system:Condition`, thẻ mô hình, phiếu thông tin mô hình [53]).

**Vì sao từng điều kiện là cần thiết (D2):**

| Điều kiện | Vì sao cần (tiền lệ không đáp ứng, hoặc bỏ đi thì vấn đề còn) | Căn cứ | Loại |
|---|---|---|---|
| "theo đơn vị độc lập" (A1) | Chia trong cùng lần chạy hay lần lắp ráp đo cả "dấu vết" của nguồn, không chỉ trạng thái liên kết | [15] tr. 169879–169881; [14] tr. 1; [19] tr. 4–5 | TG |
| "bắt buộc" | Thẻ mô hình và phiếu thông tin là tài liệu do người lập soạn, độ tin cậy phụ thuộc người lập; chuẩn báo cáo hiện có không xử lý rò rỉ, nên khai báo tự nguyện không bảo đảm có | Mitchell 2019 tr. PDF 9; [53] tr. 3, 5 | TG |
| "của từng bằng chứng" | Cùng một mô hình cho ra kết quả trước và sau một lần can thiệp có hiệu lực khác nhau; khai ở mức mô hình không phân biệt được hai kết quả này | Maes 2022 tr. 6, 12, 20; [18] tr. 283; mức mô hình: Mitchell tr. PDF 3–5 | TG + [NCS] |
| "độ bất định" | Với ít đơn vị độc lập, hiệu năng đo được có khoảng bất định rộng, không chứng minh được nếu không báo | [14] tr. 1, 9–10 | TG |
| "lần lắp ráp – can thiệp làm thành phần" | Mỗi lần tháo – lắp tạo ra một hệ khác; can thiệp lên liên kết bu lông làm mô hình trạng thái ban đầu không còn đại diện | [18] tr. 283, 292; Maes 2022 tr. 6, 20; [19] tr. 4–5, 20 (2025) | TG |
| "điều kiện vận hành làm thành phần" | Mô hình học từ trạng thái bình thường không bảo đảm với điều kiện chưa có trong huấn luyện; sai số tăng với bất kỳ tín hiệu chưa ghi | Figueiredo 2011 tr. 571; [45] tr. 553, 557 | TG |
| "kiểm tại lần sử dụng" | Hiệu lực sau can thiệp không đoán trước được: có lúc mất ([18], Maes 2022), có lúc giữ (một lần siết lại vẫn phân loại đúng, [48] tr. 9–10). Vì vậy chỉ kiểm được khi dùng, không khai một lần lúc tạo | [18] tr. 283; Maes 2022 tr. 20; [48] tr. 9–10 | TG + [NCS] |
| "kiểm được bằng máy" | Khi không có kiểm tính toán được, một trạng thái dễ thành mốc hành chính; tiền lệ này ở quản trị gói thông tin, áp sang bằng chứng là diễn giải | [44] tr. 3, 9 (2026, chỉ hỗ trợ); [21] tr. 17–18 | [NCS] |

Không có điều kiện nào phải bỏ. Điều kiện "kiểm được bằng máy" chỉ có căn cứ loại [NCS], dựa trên tương tự từ [44] và [21].
Câu chữ trong Phần D vì vậy đặt điều kiện này trong mô tả mục tiêu MT2 (C5, C9), không đặt trong câu khẳng định khoảng trống.

**Vì sao quan trọng (giữ bản 01/10):** câu hỏi "tin được đến mức nào?" của người quản lý. Phần diễn giải giữ nhãn [NCS].

### G-B. Từ bằng chứng đến hành động có trách nhiệm

Phát biểu, phần đã được giải quyết và phần còn thiếu giữ như bản 01/10.

**Vì sao từng điều kiện là cần thiết (D2):**

| Điều kiện | Vì sao cần | Căn cứ | Loại |
|---|---|---|---|
| "bằng chứng có phạm vi hiệu lực (cảm biến, NDT) đi vào chuỗi" | Chuỗi chuẩn của [35] chỉ cho hư hỏng phát hiện bằng mắt; khung song sinh số của [3] dừng ở cảnh báo | [35] tr. 4–5, 18; [3] tr. 6, 13–14 | TG + [NCS] |
| "mỗi lần đổi trạng thái của hành động" | Trạng thái trong [35] gắn với hư hỏng và bị ghi đè theo quy ước; "đã sửa" được gán khi có lần bảo trì | [35] tr. 9–10 (tác giả gọi là đơn giản hóa) | TG |
| "có căn cứ" | Sự kiện BCF ghi loại và giá trị mới, không ghi căn cứ (BCF-API mục 3.9, ghi ở nhật ký UV-01). Bước chuyển có gói bằng chứng mới có ở gói thông tin bàn giao | `K5SGFIGW`; [44] tr. 3, 19–21 | [NCS] (từ đặc tả) |
| "vai trò người thực hiện" | Thiết kế hệ SHM phải xác định ai ra quyết định; tách nhiệm vụ giữa người tạo, người xác nhận, người phê duyệt | Cawley 2018 tr. 14, 16; [44] tr. 23 | TG |
| "bước xác minh sau sửa chữa" | Giả định "có bảo trì thì đã sửa" là đơn giản hóa; bảo trì nhà thép công nghiệp cần theo dõi giai đoạn và tiến độ khắc phục | [35] tr. 10; [22] tr. 192 | TG |
| "kể cả lần kỹ sư xác nhận đầu ra AI" | Xác nhận của người được dùng làm nhãn, phản hồi; nhãn có thể sai; khung song sinh số yêu cầu người dùng xác nhận mà không nêu cách ghi | Mosqueira-Rey 2023 tr. 3006, 3012, 3039–3040; Hughes 2022 tr. 27–28; [7] tr. 12 | TG |

Không đề xuất bỏ điều kiện nào. Điều kiện "có căn cứ" dựa trên đối chiếu đặc tả BCF ghi ở nhật ký, chưa có trong `notes/`.
Trang dẫn của điều kiện này lấy theo mục của đặc tả, không theo trang.

**Vì sao quan trọng (D6, tách bằng chứng và diễn giải):**
- *Bằng chứng (TG):* thiết kế hệ phải xác định hành động và người có thẩm quyền (Cawley 2018 tr. 14, 16); bảo trì nhà thép
  công nghiệp cần hồ sơ hư hỏng cập nhật để theo dõi khắc phục ([22] tr. 192).
- *Diễn giải ([NCS]):*
  - Khi xảy ra sự cố sau sửa chữa, đơn vị quản lý cần truy ngược quyết định về bằng chứng và người phê duyệt.
  - Hồ sơ hiện hành (B0) ghi kết quả cuối, không ghi chuỗi đó.
  - Nhận định về B0 sẽ được đối chiếu với hồ sơ thật khi mã hóa B0 (D5).

## Phần B. Ba mục tiêu

### MT1. Bằng chứng trạng thái liên kết bu lông có phạm vi hiệu lực (phòng thí nghiệm)

1. **Mục tiêu:** định lượng hiệu năng của bốn mô hình (RF, SVM-RBF, 1D-CNN, ResNet1D) phân biệt trạng thái liên kết bu lông có
   kiểm soát trên khung thép 1:10 khi đánh giá theo đơn vị độc lập, đo chênh lệch so với đánh giá cùng lần chạy, và khai báo
   phạm vi hiệu lực cho từng kết quả.
2. **RQ1:** Khi giữ lại cả lần chạy trong đánh giá, bốn mô hình phân biệt các trạng thái liên kết ở mức nào? Chênh lệch bao nhiêu
   so với đánh giá cùng lần chạy? Mỗi kết quả được phép dùng trong phạm vi nào?
3. **Nội dung:**
   - (a) xác định đơn vị độc lập (lần chạy, đợt) trên dữ liệu ba đợt;
   - (b) huấn luyện RF, SVM-RBF trên đặc trưng thủ công miền thời gian – tần số, và 1D-CNN, ResNet1D trên tín hiệu chuẩn hóa;
   - (c) đánh giá theo nhóm giữ lại cả lần chạy, so với đánh giá cùng lần chạy; chấm điểm theo bản ghi, kiểm định hoán vị, báo
     cáo biến thiên theo seed và fold;
   - (d) ghi mỗi kết quả thành bản ghi `EVIDENCE` có `method_version` (git commit), `uncertainty` và phạm vi (`inference_unit`,
     `data_split`, `install_batch`).
4. **Dữ liệu và tài sản:** dữ liệu ba đợt thí nghiệm; thực thể `EVIDENCE` của schema rút gọn.
5. **Tiêu chí hoàn thành:**
   - hiệu năng theo đơn vị độc lập, kèm biến thiên seed – fold và p hoán vị;
   - chênh lệch so với đánh giá cùng lần chạy;
   - mọi kết quả trong bài có khai báo phạm vi hiệu lực.
6. **Sản phẩm:** Bài 1 (Q2/Q3, SHM – đo lường); chương MT1 của luận án.
7. **Rủi ro:**
   - Ba đợt cho ít đơn vị độc lập, khoảng tin cậy rộng ([14] tr. 1, 9–10). *Giảm:* báo cáo số đơn vị, khoảng tin cậy và kiểm định
     hoán vị; luận điểm của bài là giao thức đánh giá và khai báo phạm vi, không phụ thuộc mô hình nào thắng.
   - Phản biện so với [19], [15]. *Giảm:* nêu rõ hai bài này trong tổng quan và chỉ ra phần khác (dao động, khung thép nhiều liên
     kết, bốn họ mô hình, khai báo phạm vi).
8. **Loại đóng góp (D3):** thực nghiệm – phương pháp. Gồm giao thức đánh giá theo đơn vị độc lập và khai báo phạm vi, cùng bằng
   chứng định lượng về mức chênh lệch cho phân loại dựa trên dao động trên khung thép.
9. **Phụ thuộc (D7):** không phụ thuộc mục tiêu khác. Cấp cho MT2 tập bằng chứng có phạm vi đã biết, dùng để chèn ca dùng ngoài
   phạm vi.

### MT2. Mô hình thông tin truy vết bằng chứng → hành động

1. **Mục tiêu:** xây dựng mô hình thông tin 6 thực thể, 5 ràng buộc (C1, C3, C5, C6, C9), mở rộng IFC 4.3 của [35] và BCF 3.0
   bằng tầng bằng chứng và tầng trách nhiệm, và đánh giá bằng M1–M4 so với B0 trên BIM nhà xưởng thật. M2 là chỉ số chính.
2. **RQ2:** So với hồ sơ kiểm định theo thực hành hiện hành (B0), mô hình thông tin mở rộng IFC 4.3 – BCF 3.0 bằng tầng bằng
   chứng và tầng trách nhiệm phát hiện được tỉ lệ nào của các lỗi chèn mù, theo từng nhóm lỗi (M2)? M1, M3, M4 thay đổi ở mức nào?
   Nếu NCS duyệt F-1, RQ2 thay bằng bản có B1.
3. **Nội dung:**
   - (a) đặc tả 6 thực thể, ánh xạ sang IFC 4.3 ([35]) và BCF 3.0, kèm một bảng ánh xạ khái niệm sang SOSA/SSN, PROV-O;
   - (b) viết script Python kiểm 5 ràng buộc và logic bốn mức `priority_level` bằng luật;
   - (c) mã hóa tay 20–30 hồ sơ kiểm định cũ làm B0;
   - (d) khóa trước các mục ở D8, rồi đo M1–M4 trên BIM nhà xưởng thật, với bằng chứng từ MT1.
4. **Dữ liệu và tài sản:** schema rút gọn; BIM nhà xưởng thật (đã có thỏa thuận với chủ đầu tư); hồ sơ kiểm định cũ làm B0;
   bằng chứng có phạm vi đã biết từ MT1.
5. **Tiêu chí hoàn thành:**
   - **M2 (chính):** tỉ lệ lỗi chèn mù được script bắt, báo cáo riêng cho từng nhóm lỗi. Hai nhóm trọng tâm:
     - "dùng bằng chứng ngoài phạm vi hiệu lực" (C5, C9);
     - "đổi trạng thái hành động không có căn cứ" (C6).
   - **M1:** tỉ lệ bản ghi đủ thuộc tính bắt buộc. Ghi rõ: so với B0, phần lớn chênh lệch M1 là do schema bắt buộc trường, nên
     hiển nhiên theo thiết kế; M1 chỉ dùng để mô tả, không dùng làm căn cứ đóng góp.
   - **M3:** thời gian hoặc số bước trả lời ba câu hỏi của người quản lý.
   - **M4:** số phút mỗi bản ghi.
6. **Sản phẩm:** Bài 2 (Q2, tin học xây dựng); chương MT2 của luận án.
7. **Rủi ro:**
   - Hồ sơ B0 không đồng nhất về mẫu và mức chi tiết. *Giảm:* khóa quy tắc mã hóa trước; ghi trường nào B0 không có thay vì suy
     ra; báo cáo theo từng loại hồ sơ.
   - Không có B1 (theo CLAUDE.md hiện hành), nên chênh lệch so với B0 gộp cả phần do chuẩn sẵn có ([35], BCF) và phần do luận
     án. *Giảm:* trong bài, tách định tính phần nào chuẩn sẵn có đã làm được (bảng tiền lệ ở 5.5); hoặc duyệt F-1.
8. **Loại đóng góp (D3):** artefact thiết kế được đánh giá, theo hướng design science: mô hình thông tin, ràng buộc kiểm bằng máy,
   đánh giá so với đối chứng.
   - **Bối cảnh Việt Nam (D5):** so sánh với B0 là đóng góp **bối cảnh – thực tiễn** cho thực hành kiểm định ở Việt Nam. Khả năng
     khái quát sang thực hành nơi khác chưa được kiểm.
   - Đặc điểm của B0 chỉ ghi khi quan sát được từ hồ sơ.
   - Yêu cầu pháp lý về hồ sơ kiểm định: `[CẦN NGUỒN: văn bản quy định hồ sơ kiểm định nhà công nghiệp]`. Zotero đã có [11],
     Thông tư 32/2026, TCVN 9381, nhưng điều khoản về hồ sơ chưa được đối chiếu (N-31).
9. **Phụ thuộc (D7):**
   - Cần tập bằng chứng có phạm vi đã biết từ MT1 cho nhóm lỗi "dùng ngoài phạm vi". Có thể dùng một tập con kết quả MT1 ngay
     khi đã khóa giao thức đánh giá, không cần chờ Bài 1 được nhận.
   - Cấp schema và script cho MT3.
   - Không phụ thuộc MT3.
10. **Khóa trước khi đo (D8):**
    - quy tắc mã hóa B0;
    - danh sách khoảng 30 lỗi chèn mù và người chèn (người thứ ba);
    - bộ câu hỏi truy ngược;
    - cách tính M1–M4;
    - đặc tả B1 (nếu duyệt F-1).
    - Nơi lưu: đề xuất thư mục `03_PAPERS/PAPER_2/khoa_truoc_khi_do/` trong repo, mỗi tệp có commit trước lần đo đầu tiên.
      Đường dẫn cuối cùng: `[NCS ĐIỀN]`.

### MT3. Triển khai và kiểm chứng khả thi trên nhà xưởng thật

1. **Mục tiêu:** triển khai chuỗi bằng chứng → hành động của MT2 trên một nhà xưởng khung thép có BIM (6–10 cảm biến ở liên kết
   đại diện, quan trắc 3–6 tháng) và kiểm chứng khả thi bằng kịch bản cột C3 đầu cuối.
2. **RQ3:** giữ như bản 01/10.
3. **Nội dung:** giữ như bản 01/10.
4. **Dữ liệu và tài sản:** BIM nhà xưởng thật; thỏa thuận với chủ đầu tư; cam kết lắp cảm biến; schema rút gọn.
5. **Tiêu chí hoàn thành:** giữ như bản 01/10. MT3 chỉ tuyên bố khả thi và truy vết.
6. **Sản phẩm:** giữ như bản 01/10.
7. **Rủi ro:** giữ như bản 01/10.
8. **Loại đóng góp (D3):** kiểm chứng khả thi và truy vết trong bối cảnh thực.
9. **Phụ thuộc (D7):**
   - Cần schema và script của MT2 trước khi chạy kịch bản C3.
   - **Làm song song với MT1 được:** khảo sát nhà xưởng, chọn vị trí cảm biến, lấy hồ sơ B0, và (nếu duyệt F-2) phỏng vấn.
     Có thể bắt đầu ngay vì đã có thỏa thuận với chủ đầu tư.
   - Mốc thời gian theo CLAUDE.md mục 13; mốc ngày cụ thể: `[NCS ĐIỀN]`.
10. **Khóa trước khi đo (D8):**
    - danh sách vị trí cảm biến và bản ghi lắp đặt (`install_record_ref`);
    - khoảng thời gian lập đường cơ sở;
    - kịch bản cột C3;
    - bộ câu hỏi truy ngược dùng chung với MT2;
    - cách tính M3, M4.
    - Nơi lưu: cùng thư mục khóa của MT2, `[NCS ĐIỀN]`.

## Phần C. Ma trận

| Khoảng trống | Mục tiêu | RQ | Bài báo | Chương | Đối chứng | Chỉ số / kết quả đo | Loại đóng góp |
|---|---|---|---|---|---|---|---|
| G-A (A1, A2) | MT1 | RQ1 | Bài 1 | MT1 | Đánh giá cùng lần chạy | Hiệu năng theo đơn vị độc lập; chênh lệch; khai báo phạm vi | Thực nghiệm – phương pháp |
| G-B (+ G-A, A2) | MT2 | RQ2 | Bài 2 | MT2 | B0, B1 (F-1 đã duyệt) | **M2 theo nhóm lỗi (chính)**; M1 (mô tả), M3, M4 | Artefact thiết kế được đánh giá |
| G-A, G-B (áp dụng) | MT3 | RQ3 | Bài 2 (phần hiện trường, nếu kịp) | MT3 | — | Dữ liệu về đủ; ánh xạ đúng (C3); M3 kịch bản C3; M4 | Kiểm chứng khả thi và truy vết |

## Phần D. Văn bản đề xuất thay mục 5.2 và 5.4 (chờ NCS duyệt, chưa chèn vào `tieuluan/`)

### 5.2. Hai khoảng trống nghiên cứu

#### 5.2.1. Khoảng trống A – Bằng chứng trạng thái có phạm vi hiệu lực

Một kết quả rút từ dữ liệu dao động của kết cấu có liên kết bu lông chỉ có nghĩa trong điều kiện đã tạo ra nó. Sau mỗi lần
lắp lại khi bảo trì, phần lớn dữ liệu đáp ứng đã thu mất tác dụng cho theo dõi trạng thái \[18\]. Trên cầu thép KW51, sau khi
liên kết bu lông được gia cường, mô hình huấn luyện trên dữ liệu trước can thiệp không còn đại diện cho trạng thái bình thường
\[@2ZJSENQU\]. Ở phía đánh giá, chia dữ liệu theo đơn vị thấp hơn đơn vị độc lập làm con số hiệu năng lạc quan \[14\], \[15\],
\[53\]. Với phát xạ âm trên dầm nhôm nối bu lông, độ chính xác giảm mạnh khi kiểm tra trên một lần lắp chưa thấy \[19\].

Điều còn chưa chắc gồm hai vế. Vế thứ nhất là mức lạc quan đó lớn đến đâu đối với phân loại dựa trên dao động của liên kết bu
lông trong khung thép. Các nghiên cứu đã rà soát cho bài toán này chia tập trong cùng lần lắp ráp hoặc cùng bản ghi \[48\],
\[@VVBGM9EN\], nên không báo được chênh lệch. Vế thứ hai là cách ghi để biết khi nào một kết quả còn dùng được. Từ vựng nguồn gốc
cho từng kết quả đã có trong PROV-O \[69\]; SSN có khái niệm điều kiện mà năng lực đo của cảm biến có hiệu lực
\[CẦN NGUỒN: Khuyến nghị W3C SSN, mục 5.1\]; thẻ mô hình \[@82WQNDHU\] và phiếu thông tin mô hình \[53\] khai phạm vi ở mức mô
hình, do người lập soạn. Trong các tài liệu đã rà soát, phạm vi hiệu lực và độ bất định chưa là trường bắt buộc của từng bằng
chứng, có lần lắp ráp – can thiệp và điều kiện vận hành làm thành phần, và chưa được kiểm tại lần sử dụng.

Các điều kiện đó cần thiết vì hiệu lực sau can thiệp không đoán trước được. Có trường hợp mất \[18\], \[@2ZJSENQU\], có trường
hợp một lần siết lại vẫn được phân loại đúng \[48\], nên chỉ kiểm được khi bằng chứng được dùng. Mô hình học từ trạng thái bình
thường cũng không bảo đảm với điều kiện vận hành chưa có trong huấn luyện \[@23TBQTIP\], \[45\]. Với nhà xưởng có cầu trục, điều
kiện vận hành thuộc phạm vi này (Mục 3.2).

Nghiên cứu này kiểm hai điều: mức chênh lệch giữa đánh giá giữ lại cả lần chạy và đánh giá cùng lần chạy trên khung thép thu
nhỏ (MT1), và khả năng kiểm bằng máy việc dùng bằng chứng ngoài phạm vi (MT2). Sau nghiên cứu, người quản lý có một con số về
mức lạc quan của cách đánh giá thường gặp, và một bản ghi bằng chứng mang phạm vi để trả lời câu hỏi "tin được đến mức nào?".

#### 5.2.2. Khoảng trống B – Từ bằng chứng đến hành động có trách nhiệm

Chuỗi lần kiểm tra – hư hỏng – cấu kiện – nhiệm vụ bảo trì đã được biểu diễn bằng thực thể chuẩn IFC 4.3 cho phát hiện bằng
mắt \[35\]. IFC4 có lệnh bảo trì có trạng thái và phê duyệt ghi người, thời điểm \[CẦN NGUỒN: IFC4 ADD2 TC1\]. BCF 3.0 ghi trạng
thái vấn đề gắn cấu kiện và sự kiện đổi trạng thái \[@K5SGFIGW\]. Bước chuyển có gói bằng chứng và vai trò tách biệt đã được áp
cho gói thông tin bàn giao \[44\].

Điều còn chưa chắc nằm ở chỗ nối dữ liệu đo với hành động. Chuỗi của các khung song sinh số đã đọc dừng ở cảnh báo và hỗ trợ
quyết định \[3\], hoặc yêu cầu người dùng xác nhận mà không nêu cách ghi lần xác nhận \[7\]. Xác nhận của chuyên gia thường được
dùng làm nhãn hay dữ liệu huấn luyện, và nhãn có thể sai \[@73MBWFVJ\], \[@Z9RD5DMZ\]. Trạng thái trong \[35\] gắn với hư hỏng và
được gán "đã sửa" khi có lần bảo trì. Trong các tài liệu đã rà soát, bằng chứng có phạm vi hiệu lực chưa đi vào chuỗi kiểm tra
– cấu kiện – hành động. Mỗi lần đổi trạng thái của hành động, kể cả lần kỹ sư xác nhận một đầu ra AI, cũng chưa được ghi thành
sự kiện có căn cứ, vai trò người thực hiện và bước xác minh sau sửa chữa.

Các điều kiện đó cần thiết vì việc thiết kế một hệ theo dõi phải xác định hành động nào được đưa ra và ai có thẩm quyền
\[@EBB69J4F\]. Bảo trì nhà công nghiệp thép cũng cần hồ sơ hư hỏng cập nhật để theo dõi khắc phục \[22\]. Theo đánh giá của
nghiên cứu này, khi xảy ra sự cố sau một lần sửa chữa, đơn vị quản lý cần truy ngược quyết định về bằng chứng và người phê
duyệt.

Nghiên cứu này kiểm xem một mô hình thông tin mở rộng IFC 4.3 và BCF 3.0 bằng tầng bằng chứng và tầng trách nhiệm có phát hiện
được các lỗi dùng bằng chứng ngoài phạm vi và đổi trạng thái không căn cứ hay không (MT2), và có vận hành được trên một nhà
xưởng thật hay không (MT3). Sau nghiên cứu, câu hỏi "ai đã xử lý, dựa vào đâu?" có một chuỗi bản ghi để truy ngược.

Hai khoảng trống nối với nhau qua bản ghi sử dụng bằng chứng: khoảng trống A xác định bằng chứng nào còn dùng được, khoảng
trống B xác định việc dùng đó được ghi và giải trình ra sao.

### 5.4. Câu hỏi nghiên cứu

RQ1 (MT1). Khi giữ lại cả lần chạy trong đánh giá, bốn mô hình RF, SVM-RBF, 1D-CNN và ResNet1D phân biệt các trạng thái liên kết
bu lông có kiểm soát trên khung thép 1:10 ở mức nào? Chênh lệch bao nhiêu so với đánh giá cùng lần chạy? Mỗi kết quả được dùng
trong phạm vi nào?

RQ2 (MT2). So với hồ sơ kiểm định theo thực hành hiện hành, mô hình thông tin mở rộng IFC 4.3 \[35\] và BCF 3.0 bằng tầng bằng
chứng và tầng trách nhiệm phát hiện được tỉ lệ nào của các lỗi chèn mù, theo từng nhóm lỗi? Mức đủ thuộc tính bắt buộc, khả năng
truy ngược và chi phí ghi nhận thay đổi ra sao?

RQ3 (MT3). Trên một nhà xưởng khung thép thật có BIM, chuỗi bằng chứng – hành động có thu đủ dữ liệu, giữ đúng ánh xạ cảm biến –
cấu kiện và truy ngược được một kịch bản kiểm tra – xử lý đầu cuối không, với chi phí ghi nhận bao nhiêu?

## Phần E. Nhật ký thay đổi so với bản 01/10

| # | Thay đổi | Quyết định | Lý do |
|---|---|---|---|
| 1 | Thêm A1 vào bảng kiểm; kết luận A1 đạt; G-A gồm A1 (đánh giá) và A2 (khai báo) | D1 | Bài 1 cần một khoảng trống tương ứng |
| 2 | Thu hẹp A1: không viết "chưa được định lượng cho bài toán này" chung; ghi [19] đã định lượng cho phát xạ âm, [15] cho ổ trục | D1 | [19] tr. 12–14 giải quyết một phần |
| 3 | Thêm bảng "vì sao cần" cho 8 điều kiện của G-A và 6 điều kiện của G-B | D2 | Mỗi điều kiện phải có căn cứ |
| 4 | Điều kiện "kiểm được bằng máy" chuyển từ câu khẳng định khoảng trống sang mô tả mục tiêu MT2 | D2 | Chỉ có căn cứ [NCS] |
| 5 | Thêm trường "Loại đóng góp" cho MT1–MT3 | D3 | Nêu rõ loại đóng góp, không dùng từ tuyệt đối |
| 6 | M2 là chỉ số chính, báo cáo theo nhóm lỗi; M1 ghi giới hạn so với B0; sửa RQ2 theo M2 | D4 (phần không mâu thuẫn) | Chênh lệch M1 so với B0 hiển nhiên do thiết kế |
| 7 | B1 **chưa** đưa vào MT2, RQ2; văn bản sẵn sàng ở F-1 | D4 (phần mâu thuẫn) | Trái CLAUDE.md mục 8 ("Bỏ B1"), mục 11 |
| 8 | Ghi so sánh với B0 là đóng góp bối cảnh – thực tiễn Việt Nam; `[CẦN NGUỒN]` cho yêu cầu pháp lý | D5 | Không khái quát, không dẫn pháp quy theo trí nhớ |
| 9 | Tách bằng chứng và diễn giải ở "Vì sao quan trọng" của G-B; đề xuất phỏng vấn ở F-2 | D6 | Ý nghĩa của G-B hiện chủ yếu là [NCS] |
| 10 | Thêm trường "Phụ thuộc"; ghi việc làm song song được với MT1 | D7 | NCS năm thứ nhất, đã có thỏa thuận với chủ đầu tư |
| 11 | Thêm danh sách "khóa trước khi đo" cho MT2, MT3 | D8 | Tránh chỉnh tiêu chí sau khi thấy kết quả |
| 12 | Viết lại Phần D theo chuỗi đã biết → còn chưa chắc → vì sao điều kiện quan trọng → nghiên cứu kiểm gì → sau nghiên cứu biết gì; thêm trích \[@VVBGM9EN\], \[@EBB69J4F\], \[@23TBQTIP\], \[45\], \[14\], \[15\], \[19\] | Mục 4 (6) của prompt | Theo cấu trúc yêu cầu |

## Phần F. Việc mở cho NCS

**F-1. Thêm đối chứng B1 (D4, mâu thuẫn với CLAUDE.md mục 8 và 11).** **→ NCS DUYỆT 01/10/2026; CLAUDE.md mục 2 (QĐ 12), 2A, 8 đã sửa. Văn bản RQ2, tiêu chí, rủi ro dưới đây thay cho bản ở MT2.**
- **Đề xuất của cố vấn: duyệt.** Lý do:
  - Không có B1 thì chênh lệch so với B0 gộp cả phần [35] và BCF đã làm được, khó quy cho luận án. Phản biện Bài 2 nhiều khả năng
    hỏi đúng điểm này.
  - B1 là tập con của mô hình đề xuất (bỏ tầng bằng chứng và tầng trách nhiệm), dựng trên cùng BIM, dùng cùng script nên chi phí
    nhỏ. NCS đã xác nhận làm được trong khung thời gian.
- Nếu duyệt, cần sửa CLAUDE.md mục 8 (bỏ câu "Bỏ B1", thêm định nghĩa B1) và mục 2A (cột kết quả đo của MT2). Sau đó thay vào
  MT2 các đoạn sau:
  - *RQ2:* "Trên cùng BIM nhà xưởng, so với B0 (hồ sơ kiểm định theo thực hành hiện hành) và B1 (mô hình IFC 4.3 theo [35] và BCF
    3.0, chưa có tầng bằng chứng và tầng trách nhiệm), mô hình đề xuất phát hiện được tỉ lệ nào của các lỗi chèn mù theo từng
    nhóm lỗi (M2)? M1, M3, M4 thay đổi ra sao?"
  - *Tiêu chí:* B0, B1 và mô hình đề xuất dùng cùng danh sách lỗi, cùng bộ câu hỏi, cùng tập bằng chứng MT1. Phần quy cho đóng
    góp của luận án là chênh lệch mô hình đề xuất so với B1. Chênh lệch so với B0 là chênh lệch so với thực hành hiện hành
    (bối cảnh Việt Nam). So sánh với B1 không phụ thuộc bối cảnh Việt Nam.
  - *Rủi ro thêm:* B1 bị dựng yếu một cách vô ý. *Giảm:* đặc tả B1 bám sát [35] (tr. 4–7) và BCF 3.0, khóa trước khi đo, ghi
    mọi lựa chọn khi dựng B1.

**F-2. Phỏng vấn có cấu trúc 3–5 người quản lý kiểm tra – bảo trì phía chủ đầu tư (D6).** **→ NCS DUYỆT 01/10/2026 (CLAUDE.md QĐ 12); còn chờ thầy duyệt.**
- Mục đích: xác nhận bộ câu hỏi truy ngược trước khi khóa M3, và nêu nhu cầu cho G-B.
- Cần đồng thuận của người tham gia; không thay thế M1–M4.
- **Đề xuất của cố vấn: làm ở mức tối thiểu**, khoảng 30 phút mỗi người, gộp vào đợt khảo sát nhà xưởng. Lý do: chi phí nhỏ,
  biến phần "vì sao quan trọng" của G-B từ diễn giải thành có căn cứ.
- Nếu không làm: hạ G-B xuống "đóng góp thực tiễn, kiểm bằng M3" và ghi vào nhật ký.
- Lưu ý: đây là hoạt động thu dữ liệu mới. CLAUDE.md mục 11 không cấm hoạt động này, nhưng NCS nên ghi quyết định vào CLAUDE.md
  mục 2A nếu duyệt.

**F-3. Ba nguồn cần cho Phần D chưa có bản ghi Zotero:** IFC4 ADD2 TC1, Khuyến nghị W3C SSN (mục 5.1), quy định hồ sơ kiểm
định ở Việt Nam. Đề xuất: nhập hai chuẩn đầu như tài liệu chuẩn, không cần đọc thêm vì đã đối chiếu ở GĐ2; điều khoản hồ sơ
kiểm định gộp vào N-31.

**F-3b. Eraliev 2022 `VVBGM9EN`** được trích ở Phần D (5.2.1) nhưng chưa có dòng `so_cu = moi` trong
`matrix/doi_chieu_danh_muc.csv` (CLAUDE.md 4.4). Cần thêm dòng trước khi chèn Phần D vào `tieuluan/`. DOI ghi trong
`notes/VVBGM9EN.md`.

**F-4. Nơi lưu bản khóa trước khi đo (D8):** xác nhận đường dẫn, đề xuất `03_PAPERS/PAPER_2/khoa_truoc_khi_do/`.

**F-5. Duyệt phát biểu A1 đã thu hẹp** (có [19], [15] là tiền lệ). Nếu NCS muốn giữ A1 rộng hơn, cần thêm căn cứ, mà việc đó
trái QĐ 11.

## Tự kiểm

- [x] Không có khoảng trống mới ngoài G-A (A1, A2) và G-B.
- [x] Mọi trang dẫn mới có trong `notes/`. Ngoại lệ đã ghi: sự kiện BCF dẫn theo mục đặc tả ở nhật ký UV-01.
- [x] Mỗi điều kiện có câu giải thích có căn cứ. "Kiểm được bằng máy" chỉ có căn cứ [NCS], đã chuyển sang MT2 (Phần E dòng 4).
- [x] RQ2 nêu cả B0 và B1: đạt sau khi NCS duyệt F-1 (01/10/2026); bản RQ2 có hiệu lực là bản ở F-1. M2 là chỉ số chính và giới hạn của M1 so với B0 đã ghi.
- [x] Bối cảnh Việt Nam của B0 nêu là đóng góp bối cảnh – thực tiễn, không khái quát hóa.
- [x] Không có từ "đầu tiên", "chưa từng", "lấp đầy khoảng trống", "đóng góp lý thuyết".
- [x] Không tự đặt mốc ngày; không dẫn văn bản pháp quy theo trí nhớ.
- [x] Bản 01/10 và `tieuluan/` không bị sửa.
