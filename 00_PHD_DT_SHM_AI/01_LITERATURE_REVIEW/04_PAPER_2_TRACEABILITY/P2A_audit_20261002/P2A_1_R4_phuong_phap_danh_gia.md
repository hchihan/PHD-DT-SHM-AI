# R4 – Phản biện phương pháp đánh giá (design science) – Paper 2 (MT2)

Người phản biện: R4 (vai phương pháp đánh giá). Ngày: 02/10/2026. Đối tượng: thiết kế đã khóa (lớp 1) và bộ khung bản thảo cũ (lớp 2) theo `BRIEF_PHA1.md`.
Quy ước: **TG** = nội dung của tài liệu nguồn (kèm tệp + dòng/mục, hoặc trang với tiền lệ); **[R4]** = nhận định của phản biện. Số dòng lấy theo `cat -n` của tệp trong `src/`.

---

## 1. Tóm tắt nhận định

- [R4] Phần mới của Bài 2, nhìn từ phương pháp đánh giá, nằm ở chỗ đánh giá artefact bằng lỗi chèn mù so với hai đối chứng (B0, B1) và tách M2 theo nhóm lỗi; bảng 8 tiêu chí cho thấy tiêu chí (7) không có bài nào trong tập rà soát đạt (TG `P2A_0_phuluc_C1.md` dòng 279).
- [R4] Thiết kế hiện tại nếu nộp như dự kiến: **major revision, sát ranh giới reject-resubmit**. Lý do chính: (i) danh mục lỗi định nghĩa từ chính 5 ràng buộc, nên M2 của mô hình đề xuất gần 100% và M2 của B1 ở nhóm C3/C5/C9 bằng 0% theo thiết kế; kết quả chính vì vậy là hệ quả của định nghĩa, không phải kết quả đo; (ii) M2 không có mẫu số âm (dương tính giả), nên không đo được độ đặc hiệu; (iii) chưa có thiết kế độc lập của người chèn, người lập đáp án, người chấm.
- [R4] Bằng chứng mạnh nhất có thể có của bài: (a) phân tích "khả năng kiểm theo thiết kế" (mở rộng Bảng B.2) đi trước, khai báo trước; (b) M2 thực nghiệm có ca "khó" và ca ngoài danh mục, báo cáo cả bỏ sót; (c) mẫu số âm gồm ca hợp lệ "giáp ranh".
- [R4] Năm ràng buộc như phát biểu ở `phuluc.md` Bảng B.1 không bắt được một phần danh mục lỗi prompt v2 (định danh trùng, liên kết xung đột, sai phiên bản mô hình, đứt chuỗi trạng thái). Đây là điều tốt cho tính bác bỏ được, với điều kiện phải khai báo trước là "dự kiến bỏ sót", không sửa script sau khi thấy kết quả.
- [R4] M3, M4 hiện có nguy cơ cao bị chính NCS đo trên hệ do NCS dựng; nếu không có người đo độc lập, hai chỉ số này chỉ nên ở mức mô tả.

---

## 2. Major

### M1. Vòng tròn giữa danh mục lỗi và ràng buộc: M2 đo đúng cài đặt, chưa đo hiệu lực

- *Vị trí:* `phuluc.md` Bảng B.2 (dòng 128–138): mỗi nhóm lỗi gắn đúng một ràng buộc; `CLAUDE.md` mục 8 (bảng 4 chỉ số, dòng M2); `GD3b` MT2 mục 5 và 10; danh mục lỗi prompt v2 (4 nhóm, mỗi nhóm ghi kèm mã ràng buộc C1, C3, C5, C6, C9).
- *Vấn đề:* TG `phuluc.md` dòng 126 nói Bảng B.2 "nối mỗi nhóm lỗi chèn mù với ràng buộc phát hiện". Danh mục lỗi prompt v2 cũng được đặt tên theo ràng buộc ("(3) Dùng ngoài phạm vi (C5, C9)", "(4) Chuyển trạng thái không căn cứ (C6)"). [R4] Khi lỗi được định nghĩa là "vi phạm Ck" và người chèn tạo lỗi theo định nghĩa đó, script kiểm Ck bắt gần 100% theo định nghĩa. Chính hồ sơ cũ đã ghi nhận đúng rủi ro này: TG `gate2_3_data_model_v0.2.md` dòng 278 ("việc phát hiện 16/16 là tất yếu: đây là kiểm thử đơn vị, không phải kiểm chứng"). Đổi người chèn mà giữ danh mục lỗi suy từ ràng buộc chỉ đổi người gõ, không đổi bản chất.
- *Vì sao quan trọng:* Phản biện tạp chí tin học xây dựng sẽ đọc M2 = 100% (đề xuất) vs. 0% (B1) là phép thử khẳng định chính định nghĩa (verification), không phải đánh giá artefact (validation). Câu hỏi đầu tiên sẽ là "lỗi lấy từ đâu, ai quyết định lỗi nào đáng chèn".
- *Yêu cầu sửa (kiểm được):*
  1. Danh mục lỗi phải có **nguồn gốc ghi rõ cho từng lỗi**, ít nhất bốn nguồn, không nguồn nào suy từ Bảng B.1: (S1) lỗi quan sát được khi mã hóa B0 (hồ sơ thật); (S2) lỗi thật trong BIM (RD-001…RD-008, TG `MANUSCRIPT_OUTLINE_24092026.md` dòng 301, 369; mức "nghi ngờ" theo TG `P2A_0_kiem_toan_thu_muc_20261002.md` dòng 159); (S3) phân loại lỗi độc lập có sẵn trong hồ sơ cũ, lập trước 5 ràng buộc (9 loại lỗi ở `MANUSCRIPT_OUTLINE` mục 5.5 dòng 383; 10 loại lỗi cài ở `REFINED_v1.0` mục 10.3 dòng 271–282); (S4) lỗi "ngoài danh mục" người chèn tự nghĩ sau khi đọc kịch bản nghiệp vụ, không đọc ràng buộc. Tỉ lệ đề xuất: S4 ≥ 1/5 tổng số lỗi.
  2. Mỗi lỗi trong manifest mang hai nhãn **do người khác NCS gán trước khi chạy**: nhóm nghiệp vụ (4 nhóm) và **lớp khả năng phát hiện dự kiến** (D1 vi phạm cấu trúc/tham chiếu – ràng buộc dự kiến bắt; D2 sai ngữ nghĩa kiểm được bằng luật chéo trường chưa có trong 5 ràng buộc; D3 chỉ con người hoặc hiện trường xác nhận được). Khuôn có sẵn: cột "Giới hạn" của `REFINED_v1.0` mục 10.3 (dòng 271–282).
  3. Báo cáo M2 tách ba phần: M2 trên D1 (xác nhận cài đặt), M2 trên D2/D3 (dự kiến thấp, báo cáo để chỉ ranh giới), và M2 trên lỗi S4. Tuyên bố đóng góp chỉ dựa trên phần mà kết quả **có thể** ra khác dự đoán.
  4. Khóa script (commit) trước khi người chèn bắt đầu; mọi sửa script sau khi có kết quả là phiên bản mới, báo cáo riêng, không thay kết quả lần đầu.
- *Công sức:* M. *Mức:* **Chặn**.

### M2. Năm ràng buộc như phát biểu không phủ danh mục lỗi prompt v2; phần lệch phải được khai báo trước là dự kiến bỏ sót

- *Vị trí:* `phuluc.md` Bảng B.1 (dòng 114–120), Bảng A.2 (dòng 75–85); danh mục lỗi prompt v2 nhóm 1, 2, 4; `P2A_0_phuluc_B2.md` mục 8.1 (dòng 393: không luật cũ nào phát biểu trực tiếp C9).
- *Vấn đề (TG theo chữ của Bảng B.1; hệ quả là [R4]):*
  - "Định danh trùng", "GUID sai" (nhóm 1): C1 chỉ đòi tham chiếu trỏ tới bản ghi **tồn tại** (dòng 116). Hai cấu kiện cùng GUID, hoặc GUID đúng cú pháp nhưng trỏ sai cấu kiện, đều tồn tại → C1 không báo. Luật R01, R14, R15 cũ (`gate2_3` dòng 235, 249–251) không được giữ trong 5 ràng buộc; TG `P2A_0_phuluc_B2.md` dòng 393 xếp R14a/b, R15 "ngoài 5 ràng buộc".
  - "Liên kết xung đột" (nhóm 1): C3 phát biểu dạng tồn tại ("tồn tại một ánh xạ … sao cho", dòng 117). Một cảm biến có hai ánh xạ chồng lấn sang hai cấu kiện vẫn thỏa C3. Luật chống chồng lấn R03b cũ (`gate2_3` dòng 237) không có trong B.1.
  - "Sai phiên bản mô hình" (nhóm 2): C9 kiểm `revision_of` của **bằng chứng** (dòng 120), không đọc `COMPONENT.model_version`. Không ràng buộc nào so phiên bản mô hình.
  - "Bỏ bước đã xác minh" (nhóm 4): C6 kiểm từng sự kiện (dòng 119), không kiểm `from` của sự kiện sau bằng `to` của sự kiện trước, không kiểm thứ tự `timestamp`. Chuỗi "Mở → Đang xử lý" rồi "Hoàn thành → Đã xác minh" (thiếu sự kiện giữa) thỏa C6 từng dòng. Luật R11c cũ (`gate2_3` dòng 246) không có trong B.1. Một hành động dừng ở "Hoàn thành" không vi phạm gì: đó là trạng thái hợp lệ.
  - `evidence_ref` (nhóm 4): C6 chỉ đòi "khác rỗng khi bảng yêu cầu căn cứ". Bảng A.2 đòi "bản ghi kiểm tra sau sửa chữa" cho bước Hoàn thành → Đã xác minh (dòng 82), nhưng `evidence_ref` theo `CLAUDE.md` mục 8 trỏ `EVIDENCE_USE`, không trỏ bản ghi kiểm tra; script không kiểm được loại, đích hay thời điểm của căn cứ.
- *Vì sao quan trọng:* Nếu NCS phát hiện các lệch này **sau** khi chạy và thêm luật, kết quả bị coi là điều chỉnh sau khi thấy dữ liệu. Nếu khai báo **trước**, chính các lệch này là phần bác bỏ được của M2, làm mạnh bài (trả lời M1).
- *Yêu cầu sửa:* (a) lập bảng "lỗi × ràng buộc × dự kiến bắt/không bắt × lý do" từ chữ của Bảng B.1, khóa cùng manifest; (b) với mỗi lỗi dự kiến không bắt, ghi rõ trong bài là giới hạn của 5 ràng buộc; (c) nếu NCS muốn thêm kiểm chồng lấn, tính liên tục chuỗi, phiên bản mô hình, thì phải quyết **trước** khi khóa (xem mục 6, vì đây là đổi phạm vi khóa).
- *Công sức:* S. *Mức:* **Nặng**.

### M3. Người chèn lỗi chưa độc lập theo nghĩa phản biện chấp nhận

- *Vị trí:* `GD3b` MT2 mục 10 dòng 184 ("danh sách khoảng 30 lỗi chèn mù và người chèn (người thứ ba)"); `05_chuong5.md` mục 5.5.2 dòng 197 ("một người không tham gia thiết kế"); `CLAUDE.md` mục 8 dòng 370 ("khoảng 30 lỗi do người thứ ba chèn"); `MANUSCRIPT_OUTLINE` mục 3.5 (dòng 301, có `[CẦN BỔ SUNG: tên hoặc vai trò của người lập ca lỗi]`).
- *Vấn đề:* TG chỉ nêu điều kiện "người thứ ba / không tham gia thiết kế". Không nêu người đó được đọc gì, ai lập đáp án, ai chấm khớp, ai giữ niêm phong. [R4] Ba chỗ yếu: (i) nếu người chèn đọc Bảng B.1, M1 ở trên lặp lại; (ii) nếu NCS vừa chạy script vừa đối chiếu với manifest, NCS quyết "bắt được" theo quy tắc khớp tự chọn; (iii) kho khóa là repo của NCS (`GD3b` MT2 mục 10, đường dẫn `[NCS ĐIỀN]`), commit có thể viết lại, nên không chứng minh được thời điểm khóa với bên ngoài.
- *Vì sao quan trọng:* "Chèn mù" là luận điểm khác biệt chính so với tiền lệ (tiêu chí (7), TG `P2A_0_phuluc_C1.md` dòng 279). Thiếu giao thức thì phản biện coi như tác giả tự chèn.
- *Yêu cầu sửa:* giao thức tối thiểu ở mục 4(a); bài phải có một bảng vai trò (ai, biết gì, không biết gì) và một hình dòng thời gian khóa – chèn – chạy – mở niêm phong.
- *Công sức:* M. *Mức:* **Chặn**.

### M4. So sánh với B1 (và B0) ở nhóm C3, C5, C9 là hiển nhiên theo thiết kế

- *Vị trí:* `CLAUDE.md` mục 8 ("B1 … cùng script (tắt các ràng buộc C5, C6, C9 và các trường mới)"); `phuluc.md` Bảng B.2 (B1 "Không" ở C3, C5, C9; "Một phần" ở C6); `05_chuong5.md` 5.8.2 (dòng 336: "Phần quy cho đóng góp là chênh lệch giữa mô hình đề xuất và B1, đo bằng tỉ lệ phát hiện lỗi chèn mù").
- *Vấn đề:* TG `phuluc.md` dòng 138 tự nhận hai cột B0/B1 là "trường mà mỗi đối chứng có theo thiết kế". [R4] Khi B1 không có trường `scope`, `within_scope`, `revision_of`, `evidence_ref`, M2 của B1 ở các nhóm đó bằng 0 không phải vì B1 kém trong phát hiện mà vì lỗi **không biểu diễn được** trong B1. Gộp "không biểu diễn được" vào "bỏ sót" làm M2(B1) thấp giả tạo. Mặt khác, câu 5.8.2 quy toàn bộ đóng góp vào chênh lệch M2 với B1, tức đặt đóng góp lên đúng phần hiển nhiên. Thêm nữa, "tắt C6" mâu thuẫn với Bảng B.2 ghi B1 "Một phần" ở C6: nếu tắt hoàn toàn, B1 không được dùng cả phần BCF có (người và loại thay đổi).
- *Vì sao quan trọng:* Đây là chỗ dễ bị gọi là tautology nhất của bài; phản biện có thể đòi bỏ B1 hoặc coi kết quả chính không có giá trị thông tin.
- *Yêu cầu sửa:* (a) tách hai tầng kết quả: **tầng 1 – phân tích khả năng biểu diễn và kiểm theo thiết kế** (Bảng B.2 mở rộng tới từng loại lỗi, khóa trước, có người thứ hai rà) là kết quả chính về đóng góp; **tầng 2 – M2 thực nghiệm** chỉ là kiểm xác nhận và nơi đo bỏ sót; (b) với mỗi đối chứng, mẫu số M2 chia ba: biểu diễn được và bắt được / biểu diễn được nhưng bỏ sót / không biểu diễn được; chỉ phần biểu diễn được mới tính tỉ lệ; (c) B1 được dùng hết khả năng của nó: chạy kiểm C1 trên quan hệ IFC và kiểm phần C6 có trong BCF (người, loại, thời điểm sự kiện), cộng một người rà thủ công trên giao diện B1 với cùng thời gian cho phép; (d) sửa câu 5.8.2 dòng 336 (đề xuất tiếng Anh ở mục 7). Chi tiết ở mục 4(e).
- *Công sức:* M. *Mức:* **Chặn**.

### M5. M2 không có mẫu số âm: không đo được dương tính giả, không phân biệt được script "báo tất cả"

- *Vị trí:* `CLAUDE.md` mục 8 (định nghĩa M2 chỉ "tỉ lệ bắt được"); `GD3b` MT2 mục 5; `05_chuong5.md` 5.5.2. Đối chiếu: hồ sơ cũ có FP (TG `gate2_3` dòng 290 "kèm tỷ lệ dương tính giả trên chuỗi hợp lệ"; `OUTLINE_BIEN_TAP` dòng 104; `REFINED` dòng 284).
- *Vấn đề:* [R4] Định nghĩa khóa bỏ mất vế dương tính giả đã có ở hồ sơ cũ. Ràng buộc C5 càng dễ cho FP: nếu mọi bằng chứng MT1 dùng trên BIM nhà xưởng đều có `install_batch` khác đợt lắp đặt của cấu kiện (xem M6), `within_scope` luôn sai và script báo mọi lần dùng thiếu `justification`. Thiếu tập hợp lệ thì không phân biệt được chuyện này với phát hiện đúng.
- *Yêu cầu sửa:* M2 gồm cặp (độ nhạy theo nhóm, tỉ lệ báo sai trên tập hợp lệ). Tập hợp lệ gồm (i) chuỗi hợp lệ thường và (ii) **ca hợp lệ giáp ranh** do người chèn lập: dùng ngoài phạm vi có lý do thật; bước Hoàn thành → Mở hợp lệ (Bảng A.2 dòng 83); bằng chứng bị thay **sau** thời điểm sự kiện (C9 phải không báo); ánh xạ kết thúc đúng lúc dời cảm biến. Báo cáo số bản ghi hợp lệ đã kiểm (mẫu số FP) và FP kèm khoảng tin cậy.
- *Công sức:* S. *Mức:* **Nặng**.

### M6. Môi trường thử của nhóm "dùng ngoài phạm vi" có thể suy biến; C5 không đọc phần A1 của phạm vi

- *Vị trí:* `phuluc.md` Bảng B.1 dòng 118 (C5: `within_scope` đúng khi `scope.install_batch` trùng đợt lắp đặt hiện hành của cấu kiện và điều kiện vận hành thuộc `applicable_conditions`); `CLAUDE.md` 2A ("dữ liệu MT1 … dùng để chèn ca dùng ngoài phạm vi"); `CLAUDE.md` mục 8 (`scope` có `inference_unit`, `data_split`); `MANUSCRIPT_OUTLINE` mục 3.3 dòng 291 (bằng chứng phòng thí nghiệm không được làm căn cứ cho cấu kiện công trình thực); `P2A_0_kiem_toan` dòng 246 (giao diện G1→G2 chưa có `install_batch`, `applicable_conditions`).
- *Vấn đề:* [R4] (i) Bằng chứng MT1 sinh trên khung 1:10; đợt lắp đặt của nó không thể trùng đợt lắp đặt của cấu kiện nhà xưởng. Theo chữ của C5, mọi lần dùng bằng chứng MT1 trên BIM nhà xưởng đều ngoài phạm vi. Khi đó không có lần dùng "trong phạm vi" thật, và "lỗi dùng ngoài phạm vi không lý do" rút về thao tác xóa trường `justification`: dễ, không thông tin. (ii) C5 không đọc `inference_unit`, `data_split`. Bằng chứng từ đánh giá cùng lần chạy (lạc quan, đúng vế A1 của G-A) được dùng làm căn cứ không bị C5 báo. Luật R07/R07b cũ đã kiểm điều này (TG `gate2_3` dòng 241); bộ khóa bỏ nó. Hệ quả: mối nối A1 → MT2 không được kiểm trong M2.
- *Vì sao quan trọng:* Nhóm này là một trong hai nhóm trọng tâm (`GD3b` MT2 mục 5). Nếu môi trường thử làm nó suy biến, trọng tâm của RQ2 mất nội dung; phản biện SHM sẽ hỏi ngay vì sao bằng chứng phòng thí nghiệm lại đi vào hồ sơ nhà xưởng.
- *Yêu cầu sửa:* (a) đặc tả, khóa trước, cách "gắn" bằng chứng MT1 lên BIM nhà xưởng cho mục đích thử (ví dụ: gán đợt lắp đặt và điều kiện vận hành mô phỏng, ghi rõ là kịch bản mô phỏng), sao cho có cả lần dùng trong phạm vi và ngoài phạm vi; báo tỉ lệ hai loại; (b) đưa "dùng bằng chứng có `data_split` cùng lần chạy làm căn cứ" vào danh mục như lỗi D2 dự kiến không bắt, và nói rõ trong bài; (c) câu giới hạn trong bài: bằng chứng MT1 chỉ là vật liệu thử của chuỗi thông tin, không là căn cứ kỹ thuật cho cấu kiện thật.
- *Công sức:* M. *Mức:* **Nặng**.

### M7. Cỡ mẫu và cách báo cáo M2 theo nhóm chưa được đặc tả

- *Vị trí:* `GD3b` MT2 mục 5, 10; `CLAUDE.md` mục 8 ("khoảng 30 lỗi"; "báo cáo theo từng nhóm lỗi").
- *Vấn đề:* [R4] 30 lỗi chia 4 nhóm (5 dòng ở Bảng B.2) cho 5–10 lỗi mỗi nhóm. Với n = 10 bắt 10/10, khoảng Clopper-Pearson 95% là [0,69; 1,00]; với n = 5 bắt 5/5 là [0,48; 1,00] (tính bằng phân phối beta, mục 4(d)). Không có quy định cỡ mẫu tối thiểu mỗi nhóm, phương pháp khoảng tin cậy, hay đơn vị đếm (lỗi, bản ghi bị ảnh hưởng, hay cặp lỗi – đích).
- *Yêu cầu sửa:* khóa trước: phân bổ theo nhóm (mục 4(d)), đơn vị đếm, quy tắc khớp, khoảng Clopper-Pearson (chính) và Wilson (phụ); cấm gộp một tỉ lệ chung làm kết quả chính; so sánh cặp đề xuất – B1 bằng số cặp bất đồng (McNemar chính xác) chỉ trên lỗi biểu diễn được ở cả hai.
- *Công sức:* S. *Mức:* **Nặng**.

### M8. M3, M4 dễ thành tự đánh giá; M3 chưa có đối tượng so

- *Vị trí:* `CLAUDE.md` mục 8 (M3 "thời gian hoặc số bước trả lời ba câu hỏi"; M4 "số phút mỗi bản ghi"); `GD3b` MT2 mục 5; `MANUSCRIPT_OUTLINE` mục 3.6 dòng 305 (`[CẦN BỔ SUNG: quy trình đo M3 thủ công: ai thực hiện, bao nhiêu lần …]`).
- *Vấn đề:* TG không nêu ai trả lời câu hỏi, ai ghi bản ghi, so với gì. [R4] Nếu NCS tự truy vấn hệ do mình dựng và tự tra hồ sơ giấy, thời gian đo chủ yếu phản ánh độ quen của NCS. "Thời gian **hoặc** số bước" để ngỏ lựa chọn sau khi đo. M4 do NCS nhập là chi phí của chuyên gia, không phải của kỹ sư chủ đầu tư.
- *Yêu cầu sửa:* mục 4(f). Tối thiểu: khóa một định nghĩa (số bước **và** thời gian, cả hai), người đo không phải NCS, so ba hệ B0 – B1 – đề xuất trên cùng ba câu, chấm đúng/sai theo đáp án lập trước; nếu không có người đo độc lập, hạ M3, M4 xuống mô tả và nói rõ.
- *Công sức:* M. *Mức:* **Nặng**.

### M9. Danh mục "khóa trước khi đo" thiếu các mục quyết định kết quả; nơi khóa chưa chứng minh được với bên ngoài

- *Vị trí:* `GD3b` MT2 mục 10; `CLAUDE.md` mục 8 (đoạn "Khóa trước khi đo"); `GD3b` F-4.
- *Vấn đề:* TG khóa 5 mục: quy tắc mã hóa B0, danh sách lỗi và người chèn, bộ câu hỏi, cách tính M1–M4, đặc tả B1. [R4] Thiếu: commit của script và bộ luật bốn mức; quy tắc khớp "bắt được"; tập hợp lệ (mẫu số FP); quy tắc chuyển lỗi sang dạng B0 và B1; quy tắc loại trừ ca (ví dụ lỗi người chèn làm hỏng cả chuỗi); kế hoạch phân tích (CI, không gộp); điều kiện dừng sửa script. Kho trong repo do NCS giữ không chứng minh thời điểm.
- *Yêu cầu sửa:* bổ sung các mục trên vào D8; lưu băm SHA-256 của gói khóa ở một bên thứ ba có dấu thời gian (gửi thư cho thầy hướng dẫn và người chèn, hoặc kho lưu trữ có DOI ở chế độ ẩn) `[CẦN NGUỒN: hướng dẫn đăng ký trước cho nghiên cứu thiết kế/phần mềm]`; bài báo nêu ngày khóa và băm.
- *Công sức:* S. *Mức:* **Nặng**.

---

## 3. Minor

- **m1. Ba bộ nhóm lỗi không khớp nhau.** *Vị trí:* `05_chuong5.md` 5.5.2 dòng 197 (3 nhóm: ngoài phạm vi, sai thời hạn ánh xạ, đổi trạng thái); `phuluc.md` Bảng B.2 (5 dòng theo ràng buộc); prompt v2 (4 nhóm); `MANUSCRIPT_OUTLINE` 5.5 dòng 383 ("chín loại … gộp theo bảy nhóm"). *Vấn đề [R4]:* M2 "theo nhóm" có mẫu số đổi theo cách gộp, nên phải chốt một bảng phân loại trước khi chèn. *Sửa:* chốt 4 nhóm nghiệp vụ của prompt v2 làm đơn vị báo cáo, Bảng B.2 làm cột phụ; sửa câu 5.5.2 cho đủ 4 nhóm. *S.*
- **m2. `STATUS_EVENT` chỉ có `actor_role`, không có định danh người.** *Vị trí:* `CLAUDE.md` mục 8, bảng 6 thực thể (dòng STATUS_EVENT). *Vấn đề:* lỗi "vai trò đúng nhưng người khác", "tự phê duyệt" không biểu diễn được ở bất kỳ hệ nào; TG [44] tách nhiệm vụ giữa người tạo, người kiểm tra, người phê duyệt (`garcia2026.md` Phần D mục 1, dẫn tr. 23). *Sửa:* ghi giới hạn này trong bài; đề xuất thêm trường ở mục 6. *S.*
- **m3. Logic bốn mức `priority_level` thuộc MT2 nhưng không chỉ số nào đánh giá.** *Vị trí:* `GD3b` MT2 mục 3(b); `phuluc.md` dòng 87 (bộ luật khóa và có phiên bản). *Sửa:* hoặc đưa lỗi "mức ưu tiên không khớp phiên bản bộ luật" vào nhóm 4 như ca D2, hoặc nói rõ trong bài là logic chỉ được minh họa, không được đánh giá. *S.*
- **m4. Xác nhận của kỹ sư đối với đầu ra AI (một điều kiện của G-B) không có lỗi chèn tương ứng.** *Vị trí:* `GD3b` G-B bảng D2, dòng "kể cả lần kỹ sư xác nhận đầu ra AI". *Sửa:* thêm ít nhất một ca (ví dụ hành động mở từ bằng chứng AI mà không có bản ghi kiểm tra của kỹ sư) hoặc ghi rằng M2 không kiểm điều kiện này. *S.*
- **m5. Tên chỉ số cũ và mới hoán đổi nghĩa.** *Vị trí:* TG `P2A_0_kiem_toan` dòng 215 (Đ6: M1 cũ = phát hiện, M2 cũ = đủ trường). *Sửa:* khi lấy câu chữ từ `MANUSCRIPT_OUTLINE` 3.6, 6.3, 6.4 phải đổi tên theo bộ khóa; khuyến nghị dùng tên mô tả trong bài (ví dụ *seeded-error detection*), số hiệu chỉ trong bảng. *S.*
- **m6. "Khoảng 30" và "20–30 hồ sơ" không có lý do cỡ mẫu.** *Vị trí:* `GD3b` MT2 mục 3(c), 10. *Sửa:* nêu lý do (nguồn lực, số hồ sơ có được) và hệ quả độ rộng khoảng tin cậy; không viết như thể đủ để suy rộng. *S.*
- **m7. "Thiết kế đặc tả – kiểm chứng" chưa gắn với khung đánh giá design science.** *Vị trí:* `MANUSCRIPT_OUTLINE` 3.1 dòng 283 (tự ghi `[CẦN BỔ SUNG: phương pháp luận tham chiếu …]`); `GD3b` MT2 mục 8 ("theo hướng design science"). *Sửa:* nêu loại đánh giá (nhân tạo, sau khi dựng artefact; phần tự nhiên thuộc MT3) theo một khung có nguồn `[CẦN NGUỒN: khung chiến lược đánh giá trong design science research]`; nếu không có nguồn đã đọc thì bỏ nhãn, chỉ mô tả trình tự (đúng như outline cũ đề nghị). *S.*
- **m8. Bảng bước chuyển gọi là A.3 ở `CLAUDE.md` mục 8 nhưng là A.2 ở `phuluc.md` dòng 75.** Đã ghi ở TG `P2A_0_kiem_toan` dòng 225 (Đ16a). Nhắc lại vì đặc tả C6 trong gói khóa phải trỏ đúng bảng. *S.*

---

## 4. Trả lời các câu hỏi bắt buộc

### (a) Người chèn lỗi có độc lập thật không? Thiết kế tối thiểu

**Trả lời thẳng [R4]:** chưa. Tài liệu khóa chỉ có tiêu chí loại trừ ("không tham gia thiết kế"), không có giao thức. Hồ sơ cũ có khung tốt hơn (TG `MANUSCRIPT_OUTLINE` 3.5 dòng 301: ba vai, manifest Test_ID – đích – mã lỗi mong đợi – số lượng, niêm phong SHA-256 trước khi chạy), nhưng ở đó người lập ca "nhận bản đặc tả đã khóa", tức đọc luật, và "mã lỗi mong đợi" là mã luật. Như vậy vẫn là vòng tròn ở M1.

**Thiết kế tối thiểu đề xuất (5 vai, NCS chỉ giữ một vai):**

| Vai | Ai (đề xuất) | Được biết | Không được biết |
|---|---|---|---|
| V1 Người dựng artefact | NCS | Toàn bộ | Manifest, vị trí lỗi, số lỗi mỗi nhóm cho tới khi mở niêm phong |
| V2 Người chèn lỗi | Một kỹ sư kiểm định hoặc NCS khác, ngoài nhóm thiết kế, có kinh nghiệm hồ sơ kiểm tra – bảo trì | Mô tả nghiệp vụ (kịch bản cột C3, Bảng A.2 bước chuyển và vai trò, mô tả trường Bảng A.1 bằng lời), tập dữ liệu hợp lệ ở ba dạng (B0, B1, đề xuất), bảng phân loại nhóm nghiệp vụ, nguồn S1–S3 | Bảng B.1 (phát biểu ràng buộc), Bảng B.2, mã nguồn script, kết quả chạy thử 16/16 |
| V3 Người lập đáp án và gán lớp D1/D2/D3 | Người thứ hai khác V2 (ví dụ thầy hướng dẫn hoặc đồng nghiệp tin học xây dựng); hoặc V2 nếu không đủ người, kèm ghi rõ | Manifest của V2, Bảng B.1 (để dự đoán) | Kết quả chạy |
| V4 Người chạy | NCS được, vì chỉ chạy commit đã khóa trên tệp niêm phong; mọi lệnh ghi nhật ký | Tệp dữ liệu đã chèn (không kèm manifest) | Manifest |
| V5 Người chấm khớp | V3 hoặc người thứ ba; không phải NCS | Manifest, báo cáo của script, quy tắc khớp đã khóa | — |

Quy tắc:
- **Thứ tự:** khóa script + bộ luật (commit) → V2 nhận gói đầu vào → V2 chèn, lập manifest → V3 gán đáp án và lớp dự kiến → niêm phong (SHA-256 của tệp dữ liệu, manifest, đáp án) gửi cho thầy hướng dẫn và V2 bằng thư có dấu thời gian → V4 chạy → V5 chấm → mở niêm phong cho NCS.
- **Quy tắc khớp (khóa trước):** một lỗi là "bắt được" khi script báo đúng bản ghi đích **và** đúng nhóm nghiệp vụ (hoặc một ràng buộc mà V3 đã ghi là chấp nhận được cho lỗi đó). Báo đúng bản ghi nhưng sai lý do: ghi riêng là "bắt một phần", không cộng vào tử số chính.
- **Mẫu số âm:** V2 lập cả ca hợp lệ giáp ranh (M5); V2 biết tỉ lệ, V4 không biết ca nào hợp lệ.
- **Nhật ký:** (i) nhật ký chèn (V2: lỗi, nguồn S1–S4, lý do); (ii) nhật ký chạy (lệnh, commit, băm đầu vào và đầu ra); (iii) nhật ký sai lệch so với giao thức (mọi lần mở niêm phong sớm, sửa dữ liệu, loại ca). Ba nhật ký công bố kèm bài.
- **Câu cho bài:** nêu V2, V3 theo vai trò (không cần tên), quan hệ với tác giả, và họ đã đọc gì. Nếu V2 đã từng thấy Bảng B.1 (ví dụ do dự hội đồng tiểu luận), phải khai báo.

### (b) Danh mục có thiên về loại script được thiết kế để bắt? Cách phá vòng tròn

**Trả lời [R4]:** có, theo cấu trúc. Prompt v2 đặt tên từng nhóm kèm mã ràng buộc; `phuluc.md` Bảng B.2 viết theo ràng buộc; hồ sơ cũ cho thấy ca NT đều được lập để kích một luật cụ thể (TG `gate2_3` A.4, cột "Ca kiểm thử" dòng 233–251; A.5 dòng 261–274). Ngược lại, chính danh mục prompt v2 có chứa lỗi mà 5 ràng buộc **không** bắt (M2 của báo cáo này), nên vòng tròn chưa kín. Nhưng nếu không khai báo trước, NCS dễ "sửa" bằng cách thêm luật, và vòng tròn khép lại.

**Cách phá (khóa cùng manifest):**
1. **Nguồn lỗi tách khỏi ràng buộc**, ghi nguồn cho từng lỗi:
   - S1 – **hồ sơ thật B0**: khi mã hóa 20–30 hồ sơ, người mã hóa ghi mọi bất nhất quan sát được (thiếu cấu kiện, ngày không khớp, ký thay, kết luận không có căn cứ đo, không có lần kiểm tra lại sau sửa). Lỗi tự nhiên này được chuyển thành lỗi chèn trên ba hệ. Đây là nguồn mạnh nhất vì không ai thiết kế nó.
   - S2 – **RD-001…RD-008** (IfcGUID trùng, TG `MANUSCRIPT_OUTLINE` dòng 369). Lưu ý: dưới schema khóa, RD là lỗi D2 dự kiến **không** bắt bằng C1 (hai phần tử đều tồn tại). Đó chính là giá trị của chúng: lỗi thật nằm ngoài tầm ràng buộc. Trạng thái "nghi ngờ" (TG `P2A_0_kiem_toan` dòng 159) phải được xác minh trước khi dùng.
   - S3 – **phân loại lập trước 5 ràng buộc**: 9 loại của `MANUSCRIPT_OUTLINE` 5.5, 10 loại lỗi cài của `REFINED` 10.3. Lấy chúng làm khung, không lấy Bảng B.1.
   - S4 – **lỗi ngoài danh mục**: V2 được yêu cầu nghĩ ít nhất 6 lỗi "người ghi hồ sơ thực sự hay làm sai" sau khi đọc kịch bản nghiệp vụ.
   - Tiền lệ cho lỗi tự nhiên trên dữ liệu thật: TG [44] kiểm 22 tệp IFC thật, 14/22 bị giữ lại (`GNTQNBWM.md` dòng 17, dẫn tr. 10–11, 27–29). Bài có thể nêu như cách bổ sung lỗi chèn bằng lỗi tự nhiên.
2. **Dự đoán trước khả năng bắt** cho từng lỗi (lớp D1/D2/D3, mục (a) V3). Kết quả "đúng như dự đoán" ở D1 là xác nhận cài đặt; kết quả ở D2/D3 và S4 mới là phần thông tin.
3. **Báo cáo riêng lỗi ngoài tầm ràng buộc**: một bảng "lỗi không bắt được và vì sao", tách khỏi tỉ lệ chính, không bỏ. Đúng điều kiện (3) "báo cáo cả ca bị bỏ sót" của hồ sơ cũ (TG `gate2_3` dòng 284).
4. **Giới hạn tỉ trọng D1:** đề xuất D1 không quá khoảng 60% tổng lỗi, để M2 không bị chi phối bởi ca dễ.

### (c) Lỗi "khó" (hợp lệ cú pháp, sai ngữ nghĩa): ví dụ, script có bắt được không, bài phải nói gì

Đánh giá "bắt / không bắt" là [R4] theo chữ của `phuluc.md` Bảng B.1 dòng 116–120 và Bảng A.2 dòng 77–83.

| Nhóm | Lỗi khó (ví dụ cụ thể) | Bắt? | Vì sao |
|---|---|---|---|
| 1 Định danh – liên kết | Bằng chứng loại quan sát/NDT gắn `BIM_GUID` của cột C4 (tồn tại) thay vì C3 | Không | C1 chỉ kiểm tồn tại; C3 chỉ áp cho bằng chứng loại cảm biến |
| 1 | Ánh xạ cảm biến gắn sai cấu kiện ngay từ đầu, bằng chứng chép đúng GUID của ánh xạ đó | Không | Nhất quán nội bộ; đúng đắn loại 2, chỉ kiểm bằng hồ sơ lắp đặt và hiện trường (TG `phuluc.md` dòng 144) |
| 1 | Hai ánh xạ chồng lấn: cảm biến S gắn C3 và C4 cùng khoảng thời gian | Không | C3 dạng tồn tại |
| 1 | Hai cấu kiện cùng `BIM_GUID` (kiểu RD-001…008) | Không (trừ khi `BIM_GUID` là khóa chính) | C1 không kiểm duy nhất |
| 1 | `valid_from` ghi theo ngày kế hoạch lắp, không theo ngày lắp thật | Không | Hợp lệ cú pháp, phủ khoảng đo |
| 1 | Bản ghi kiểm tra của C4 dùng bằng chứng của C3 không ghi lý do | Không | Không ràng buộc nào so cấu kiện của `INSPECTION_RECORD` với cấu kiện của `EVIDENCE` (luật R10b cũ, `gate2_3` dòng 245, không giữ) |
| 2 Phiên bản | Bằng chứng gắn GUID ở `model_version` v2, trong khi lúc đo (v1) GUID đó là phần tử khác | Không | Không ràng buộc nào đọc `model_version` |
| 2 | Bằng chứng cũ đã bị phân tích lại (commit mới sửa lỗi) nhưng không ai tạo bản ghi `revision_of` | Không | C9 chỉ thấy thay thế đã ghi |
| 2 | `created_at` của bản thay thế ghi lùi ngày | Bắt sai hướng (có thể báo sai hoặc bỏ sót) | C9 tin `created_at` |
| 3 Ngoài phạm vi | `justification` = "xem hồ sơ", "ok", hoặc chép từ ca khác | Không | C5 chỉ kiểm khác rỗng |
| 3 | `applicable_conditions` khai quá rộng (mọi nhiệt độ, cầu trục mọi trạng thái), nên `within_scope` đúng | Không | Phạm vi khai sai về khoa học (TG `REFINED` dòng 281: "không kiểm tra được phạm vi có đúng về mặt khoa học") |
| 3 | Bằng chứng `data_split` cùng lần chạy (đánh giá lạc quan) dùng làm căn cứ | Không | C5 không đọc `data_split`, `inference_unit` (M6) |
| 3 | Bu lông đã được siết lại ngoài hệ (hành động không lên "Đã xác minh"), `install_batch` không đổi, bằng chứng cũ được coi là trong phạm vi | Không | Đợt lắp đặt chỉ đổi khi hành động lên "Đã xác minh" (TG `phuluc.md` dòng 122) |
| 3 | Cờ cầu trục tại `used_at` ghi sai | Không | `within_scope` tính từ dữ liệu ghi |
| 4 Chuyển trạng thái | `actor_role` = người phê duyệt nhưng là chính kỹ sư kiểm tra (tự phê duyệt) | Không biểu diễn được | Không có định danh người (m2) |
| 4 | `evidence_ref` khác rỗng, đúng kiểu, nhưng trỏ `EVIDENCE_USE` của hành động/cấu kiện khác | Không | C6 chỉ kiểm khác rỗng |
| 4 | Hoàn thành → Đã xác minh, căn cứ là bản ghi kiểm tra **trước** sửa chữa | Không | C6 không kiểm thời điểm hay loại căn cứ |
| 4 | Thiếu sự kiện giữa (Mở → Đang xử lý, rồi Hoàn thành → Đã xác minh) | Không | C6 kiểm từng sự kiện, không kiểm liên tục |
| 4 | `timestamp` xác minh sớm hơn `timestamp` hoàn thành | Không | Không kiểm thứ tự |
| 4 | `reason` có nội dung nhưng vô nghĩa | Không | Không có kiểm ngữ nghĩa |

**Bài phải nói gì [R4]:**
- Có một mục "Ranh giới của kiểm bằng máy" phân biệt D1 (vi phạm cấu trúc, tham chiếu, thời gian đã ghi), D2 (sai ngữ nghĩa kiểm được bằng luật chéo trường mà bộ 5 ràng buộc **chưa** có) và D3 (chỉ con người hoặc hiện trường xác nhận). Dựa trên phân biệt "hai loại đúng đắn" đã có (TG `gate2_3` dòng 255–257; `MANUSCRIPT_OUTLINE` 3.4 dòng 295–297), mở rộng sang phạm vi và trách nhiệm.
- Nói rõ: mô hình **làm cho lỗi D2/D3 nhìn thấy được với người rà** (trường có mặt, chuỗi tái dựng được), không tuyên bố tự phát hiện. Nếu muốn đo phần này, cho một người rà (không phải NCS) đọc chuỗi trên ba hệ với cùng thời gian, đếm lỗi D2/D3 tìm được; báo cáo như kết quả phụ.
- Không thêm luật sau khi thấy bỏ sót; ghi luật đề xuất vào "hướng tiếp theo".

### (d) Nhóm 4 đã đủ chưa? Phân bổ ~30 lỗi; báo cáo với n nhỏ

**Đủ chưa [R4]:** nhóm 4 phủ được "thiếu căn cứ, sai vai trò, bước ngoài bảng". Còn thiếu bốn kiểu, nên đưa vào nhóm 4 làm loại con (không thêm nhóm): (i) đứt chuỗi (from ≠ to trước); (ii) sai thứ tự thời gian; (iii) căn cứ sai đích hoặc sai loại (trỏ bản ghi trước sửa chữa, của cấu kiện khác); (iv) tự phê duyệt / không tách nhiệm vụ. Cộng ca về xác nhận đầu ra AI (m4) và về mức ưu tiên không khớp bộ luật (m3). Phần lớn các loại con này là D2 hoặc D3 theo Bảng B.1 hiện hành, tức dự kiến bỏ sót, và phải khai báo như vậy.

**Phân bổ đề xuất** (khoảng 36 lỗi, vẫn trong tinh thần "khoảng 30" nếu NCS chấp nhận; nếu giữ đúng 30 thì giảm S4 xuống 4 và nhóm 1 xuống 5):

| Nhóm nghiệp vụ | Tổng | Trong đó D1 | D2/D3 | Nguồn bắt buộc có |
|---|:--:|:--:|:--:|---|
| 1 Định danh – liên kết | 6 | 3 | 3 (gồm ≥2 ca RD) | S2, S3 |
| 2 Phiên bản | 5 | 2 | 3 | S3 |
| 3 Dùng ngoài phạm vi (trọng tâm) | 10 | 6 | 4 (gồm `data_split` cùng lần chạy, justification rỗng nghĩa) | S1, MT1 |
| 4 Chuyển trạng thái (trọng tâm) | 10 | 6 | 4 (đứt chuỗi, thứ tự, căn cứ sai đích, tự phê duyệt) | S1 |
| S4 ngoài danh mục (báo riêng) | ≥5 | V3 gán | V3 gán | S4 |
| Ca hợp lệ giáp ranh (mẫu số FP) | ≥10 | — | — | V2 lập |

Ngoài ra chuỗi hợp lệ thường đủ lớn để có mẫu số FP có nghĩa (ví dụ ≥ 50 bản ghi hợp lệ: 0/50 cho khoảng Clopper-Pearson [0; 0,07]).

**Cách báo cáo (khóa trước):**
- Mỗi nhóm và mỗi lớp D: x/n, tỉ lệ, **khoảng tin cậy 95% Clopper-Pearson** (chính, vì bảo thủ khi tỉ lệ gần 0 hoặc 1) và Wilson (phụ). Giá trị tham khảo đã tính bằng phân phối beta: 5/5 → CP [0,48; 1,00]; 10/10 → CP [0,69; 1,00], Wilson [0,72; 1,00]; 8/10 → CP [0,44; 0,97]; 0/10 → CP [0; 0,31]; 30/30 → CP [0,88; 1,00].
- **Không gộp** một tỉ lệ chung làm kết quả chính; tỉ lệ chung (nếu có) chỉ trong bảng phụ kèm cảnh báo trộn nhóm.
- So sánh đề xuất – B1: chỉ trên lỗi **biểu diễn được ở cả hai**, báo số cặp bất đồng (đề xuất bắt, B1 không, và ngược lại); kiểm McNemar chính xác chỉ nêu nếu số cặp bất đồng đủ (ví dụ ≥ 6); nếu không, chỉ mô tả.
- Đơn vị đếm là một lỗi trong manifest (không phải số bản ghi bị kéo theo); lỗi làm hỏng nhiều bản ghi vẫn đếm 1.
- Câu cho bài: "với n nhỏ, các khoảng tin cậy rộng; kết quả chỉ ra loại lỗi nào được kiểm bằng máy, không ước lượng tỉ lệ phát hiện ở quy mô khác".

### (e) M2 so với B0 và B1: tránh tautology

**Trả lời [R4]:** đúng là tautology nếu giữ cách viết hiện tại. TG `CLAUDE.md` mục 8 cho B1 "tắt các ràng buộc C5, C6, C9 và các trường mới", nên ở nhóm C5, C9 (và C3, vì B1 không có `valid_from`, `valid_to` – `phuluc.md` dòng 96 "Không có trường thời hạn") M2(B1) = 0 trước khi đo.

Đề xuất ba lớp, báo cáo theo thứ tự:
1. **Khả năng biểu diễn và kiểm theo thiết kế (phân tích, khóa trước).** Mở rộng Bảng B.2 xuống từng loại lỗi trong manifest, với 3 hệ × 3 ô: lỗi có biểu diễn được không; nếu có, kiểm được bằng máy không; nếu không bằng máy, người đọc có trường để phát hiện không. Lập bởi NCS, **rà bởi V3**, khóa trước khi chèn. Đây là kết quả chính về đóng góp so với B1, và phải nói thẳng là kết quả phân tích, không phải đo.
2. **M2 thực nghiệm trên phần biểu diễn được.** Đề xuất: chạy script khóa. B1: chạy kiểm có thể làm trên IFC + BCF (C1 qua quan hệ IFC; phần C6 BCF có: người, loại, thời điểm sự kiện, TG `garcia2026.md` Phần E dòng "Căn cứ của bước chuyển … BCF 3.0: không") **cộng** một người rà thủ công (không phải NCS, không phải V2) trên giao diện B1 với thời gian cho phép bằng nhau. B0: hai người mã hóa độc lập (không phải NCS) tìm lỗi trên hồ sơ dạng B0 với cùng thời gian, báo thỏa thuận giữa người mã hóa (kappa Cohen) `[CẦN NGUỒN: tham chiếu cho kappa và ngưỡng diễn giải]`.
3. **Ca không biểu diễn được** ở mỗi hệ: đếm riêng, không đưa vào mẫu số của tỉ lệ bắt được. Bài không viết "B1 bỏ sót 100%" mà viết "x lỗi không biểu diễn được trong B1".

Điều kiện cho B0: phải có **quy tắc chuyển lỗi** từ kịch bản chung sang dạng hồ sơ B0 (biên bản, bảng kết quả), khóa trước. Vì B0 là hồ sơ giấy thật của công trình khác thời điểm, cần một "bản B0 của kịch bản thử": dựng hồ sơ theo mẫu B0 cho cùng tình huống trên BIM nhà xưởng, rồi chèn lỗi tương đương. Nếu không làm được, phải nói M2(B0) chỉ là đánh giá khả năng biểu diễn (lớp 1), không phải đo.

Câu 5.8.2 dòng 336 ("Phần quy cho đóng góp là chênh lệch … đo bằng tỉ lệ phát hiện lỗi chèn mù") cần sửa thành: đóng góp so với B1 là các loại lỗi chuyển từ "không biểu diễn được" sang "kiểm được bằng máy", và M2 thực nghiệm xác nhận điều đó cùng ranh giới bỏ sót.

### (f) M1, M3, M4: cách đo, ai đo, M3 so với gì; rủi ro tự đánh giá tổng thể

**M1.** Tính bằng script trên toàn bộ bản ghi; với B0 do người mã hóa (hai người, kappa). TG `GD3b` MT2 mục 5 đã tự hạ M1 với B0 xuống "chỉ mô tả" – đúng. [R4] Với B1, M1 cũng gần hiển nhiên nếu "trường bắt buộc" lấy theo schema đề xuất (B1 không có các trường mới). M1 có nghĩa chỉ khi tính trên **tập trường mà cả hai hệ có** (giao), hoặc trên các trường B0 có. Khóa danh sách trường dùng cho M1 của từng so sánh.

**M3.** Đề xuất khóa:
- Ba câu hỏi (sau phỏng vấn, QĐ 12); đáp án lập trước bởi V3.
- Người trả lời: không phải NCS. Tốt nhất là 2–3 kỹ sư phía chủ đầu tư (có thể trùng người phỏng vấn, nhưng phỏng vấn trước, đo sau), hoặc NCS khác ngoài nhóm. Huấn luyện ngang nhau cho ba hệ (cùng thời lượng hướng dẫn).
- So với: B0 (tra hồ sơ giấy/PDF), B1 (trình xem IFC + BCF), đề xuất (truy vấn có sẵn). Thứ tự hệ đổi giữa người để giảm hiệu ứng học.
- Đo **cả** số bước (định nghĩa trước: số tài liệu/bản ghi mở, số lần nối) **và** thời gian, **và** đúng/sai theo đáp án. Chấm đúng/sai bởi V5.
- Với 2–5 người × 3 câu: chỉ mô tả (trung vị, khoảng), không kiểm định.
- Phần thời gian máy (ms của truy vấn, TG `gate2_3` dòng 292) không phải M3; nếu báo, đặt riêng.

**M4.** Phút mỗi bản ghi do người ghi thật (kỹ sư) trên một mẫu bản ghi chuẩn (ví dụ 10 bản ghi mỗi loại), so B1 với đề xuất (chênh lệch là chi phí của các trường mới). Nếu chỉ NCS ghi: ghi rõ "ước lượng của tác giả", không dùng để kết luận khả thi.

**Rủi ro tự đánh giá tổng thể [R4]:** NCS dựng artefact, viết ràng buộc, dựng B1 (đối chứng mà NCS có lợi khi nó yếu – rủi ro đã ghi ở TG `GD3b` F-1), mã hóa B0, chạy script, có thể đo M3, M4. Biện pháp giảm, theo thứ tự chi phí:
1. **Đăng ký trước** gói khóa mở rộng (M9) có băm gửi bên ngoài.
2. **Thành viên thứ hai** ở ba điểm: rà đặc tả B1 so với [35] tr. 4–7 và BCF 3.0 (chống B1 yếu); mã hóa B0 song song (kappa); V3/V5 ở M2.
3. **Báo cáo âm tính bắt buộc**: bảng bỏ sót, bảng FP, bảng ca không biểu diễn được, nhật ký sai lệch; nêu cả kết quả nếu B1 bắt được nhiều hơn dự kiến.
4. **Công bố gói tái lập**: dữ liệu đã chèn, manifest, script commit, nhật ký (hồ sơ cũ đã định hướng, TG `MANUSCRIPT_OUTLINE` 5.6 dòng 387).
5. **Phần nào không có người thứ hai thì hạ cấp tuyên bố** xuống mô tả, ghi ở mục giới hạn.

---

## 5. Đáng giữ / nên bỏ từ hồ sơ cũ (lớp 2), góc nhìn đánh giá

**Đáng giữ**
1. Câu cảnh báo 16/16 là kiểm thử đơn vị và "ba điều kiện để thành bằng chứng" (TG `gate2_3` dòng 278–284; `REFINED` dòng 286): dùng gần nguyên văn trong mục phương pháp.
2. Giao thức ba vai, manifest, niêm phong SHA-256 (TG `MANUSCRIPT_OUTLINE` 3.5 dòng 301), mở rộng thành 5 vai như mục 4(a).
3. Cột "Giới hạn / khả năng phát hiện dự kiến" của bảng lỗi cài (TG `REFINED` 10.3 dòng 271–282): khuôn cho dự đoán trước D1/D2/D3.
4. Phân biệt hai loại đúng đắn (TG `gate2_3` dòng 255–257; `MANUSCRIPT_OUTLINE` 3.4) làm nền cho mục "ranh giới của kiểm bằng máy".
5. Vế dương tính giả trên chuỗi hợp lệ trong định nghĩa phát hiện (TG `gate2_3` dòng 290; `OUTLINE_BIEN_TAP` dòng 104).
6. Bảng 10 và Hình 7 dự kiến (TG `MANUSCRIPT_OUTLINE` dòng 426, 428): cột bỏ sót, FP, nguồn thật/tổng hợp; thêm cột lớp D và cột "không biểu diễn được".
7. RD-001…RD-008 như lỗi thật ngoài tầm C1 (sau khi xác minh).
8. Câu "chỉ số không được diễn giải thành độ chính xác chẩn đoán hay hiệu quả quyết định" (TG `OUTLINE_BIEN_TAP` dòng 21, cột giới hạn diễn giải dòng 103–106).

**Nên bỏ**
1. Kết quả 16/16, 2/2, 5,5 ms (TG `gate2_3` dòng 290–292): không đưa vào bài dưới bất kỳ dạng nào, kể cả "thử nghiệm sơ bộ".
2. Tên M1/M2/M3 cũ (nghĩa hoán đổi, m5).
3. "Mã lỗi mong đợi" là mã luật trong manifest (TG `MANUSCRIPT_OUTLINE` dòng 301): thay bằng nhóm nghiệp vụ + lớp D, để manifest không viết theo luật.
4. M3 dạng thời gian máy (trung vị, p95 ms của CQ05): không phải câu hỏi của người quản lý.
5. "Người lập ca nhận bản đặc tả đã khóa" (TG `MANUSCRIPT_OUTLINE` dòng 301) nếu đặc tả gồm phát biểu luật: thay bằng mô tả nghiệp vụ.
6. 12 CQ làm đơn vị đánh giá: bộ khóa chỉ dùng 3 câu truy ngược; các CQ còn lại chỉ là kiểm thử nội bộ.

---

## 6. Đề xuất ngoài phạm vi khóa – chờ NCS duyệt

Các đề xuất dưới đây chạm `CLAUDE.md` mục 11 ("Không thêm … ràng buộc hay chỉ số ngoài mục 2A và 8") hoặc định nghĩa khóa ở mục 8; R4 không tự áp dụng.

- **P1. Đưa dương tính giả vào định nghĩa M2** (M5). Lý do: không đổi số chỉ số, chỉ bổ sung mẫu số âm cho M2; hồ sơ cũ đã có. Nếu không duyệt, bài phải nói rõ M2 chỉ đo độ nhạy.
- **P2. Mở rộng phát biểu của ràng buộc hiện có, không thêm mã mới**, quyết **trước** khi khóa script: C1 thêm duy nhất `BIM_GUID` trong một `model_version`; C3 thêm "đúng một" ánh xạ (không chồng lấn); C6 thêm liên tục chuỗi (from = to trước) và thứ tự `timestamp`; C5 thêm kiểm `data_split` khác "cùng lần chạy". Lý do: các lỗi tương ứng đã có trong danh mục prompt v2 và trong luật cũ (R01, R03b, R11c, R07). Đánh đổi: nếu duyệt, số lỗi D1 tăng và M2 dễ cao hơn; nếu không duyệt, các lỗi này thành D2 dự kiến bỏ sót, có giá trị cho tính bác bỏ được. R4 nghiêng về **không duyệt** P2 cho Bài 2 và báo chúng như giới hạn, trừ C3 "đúng một" (vì C3 dạng tồn tại làm lỗi "liên kết xung đột" của chính danh mục trở nên trái ngược với tên ràng buộc).
- **P3. Thêm trường định danh người (`actor_id`) vào `STATUS_EVENT`** để biểu diễn tách nhiệm vụ (TG [44] tr. 23 qua `garcia2026.md` Phần D). Không thêm ràng buộc; chỉ để lỗi "tự phê duyệt" biểu diễn được và người rà thấy được.
- **P4. Người đo M3, M4 là kỹ sư phía chủ đầu tư**, mở rộng hoạt động phỏng vấn (QĐ 12) thêm một buổi đo khoảng 30–45 phút mỗi người. Cần thầy duyệt như hoạt động thu dữ liệu với người tham gia.

---

## 7. Câu tiếng Anh đề xuất cho bản thảo

1. *"Because the detection rules and the error taxonomy were developed by the same author, a seeded-error test designed from the rules would confirm the implementation rather than evaluate the model; we therefore separated rule authoring, error seeding, answer-key preparation and match adjudication across four roles, and the seeder did not have access to the constraint statements or the checking script."*
2. *"For each baseline, seeded errors were classified as not representable, representable but missed, or detected; detection rates are reported only over representable errors, and the count of non-representable errors is reported separately as a property of the representation rather than as a detection failure."*
3. *"Before seeding, each error was assigned an expected detectability class: violations of recorded structure, references or time intervals (D1); semantic inconsistencies that would require cross-field rules not included in the five constraints (D2); and faults that only human review or field verification can establish (D3). We report detection separately for each class and do not add rules after observing misses."*
4. *"Given the small number of errors per group, we report each group as x/n with exact Clopper–Pearson 95% intervals and do not pool groups into a single detection rate; false-positive rates are reported over a separate set of valid and borderline-valid records."*
5. *"The comparison with B1 is primarily analytical: it identifies which error types move from not representable to machine-checkable when the evidence and accountability layers are added; the seeded-error experiment confirms this mapping and documents its limits."*
