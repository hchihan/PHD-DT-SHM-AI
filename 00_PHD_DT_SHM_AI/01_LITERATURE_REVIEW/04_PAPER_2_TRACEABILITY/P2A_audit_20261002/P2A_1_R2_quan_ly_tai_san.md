# R2 – Phản biện Paper 2 (MT2) từ góc nhìn quản lý tài sản, kiểm định – bảo trì

Ngày lập: 02/10/2026 · Vai: R2 (quản lý tài sản, kiểm định – bảo trì) · Pha 1 theo `BRIEF_PHA1.md`.
Đã đọc: `src/GD3b_khoang_trong_va_muc_tieu.md` (toàn văn); `src/CLAUDE.md` (toàn văn; trọng tâm mục 2 QĐ 8, 12, 13; 2A; 6.1; 8; 10; 11);
`src/phuluc.md` (toàn văn); `src/05_chuong5.md` mục 5.2–5.5, 5.8, 5.9; `src/04_chuong4.md` mục 4.1, 4.3, 4.5;
`src/GNTQNBWM.md`, `src/garcia2026.md`, `src/NUTL57KJ.md`, `src/bellon2025.md` (Phần D); `src/P2A_0_kiem_toan_thu_muc_20261002.md` mục 0–7;
`src/REFINED_v1.0_25092026.md` (mục 10.1 và các dòng về chủ đầu tư, pháp lý); `src/OUTLINE_BIEN_TAP_24092026.md` (các mục 2.3, 3.3–3.4, 4.2, 4.5, 7, 8);
`src/gate2_3_data_model_v0.2.md` mục A.2.6 (R11–R13).
Ký hiệu: **TG** = tác giả nguồn nói (kèm trang); **[NCS]** = nhận định của NCS trong tài liệu nguồn; **[R2]** = nhận định của phản biện này.
Số dòng `CLAUDE.md` theo bản trong `src/` (L58 = QĐ 12; L361 = đối chứng; L371–372 = M3, M4; L446–450 = kịch bản C3, ba câu hỏi).

---

## 1. Tóm tắt nhận định

- [R2] Phần mới của Paper 2, nhìn từ phía chủ đầu tư, nằm ở **tầng trách nhiệm**: bước chuyển trạng thái của hành động có căn cứ trỏ về bản ghi sử dụng bằng chứng, có bước "đã xác minh" tách khỏi "hoàn thành", và đợt lắp đặt (`install_batch`) đổi theo can thiệp. Ba điểm này thật sự khác [35] (TG, `NUTL57KJ` tr. 9–10: "đã sửa" gán theo quy ước khi có bảo trì) và khác BCF (sự kiện không ghi căn cứ, `garcia2026.md` Phần E).
- [R2] Nhưng thiết kế hiện tại **chưa trả lời được chính câu hỏi thứ ba của người quản lý ("Ai đã xử lý?")**: schema chỉ lưu `actor_role`/`inspector_role`, không lưu người, tổ chức hay tư cách hành nghề (Bảng A.1, `phuluc.md` L34, L43). Bảng A.2 không có đường ghi quyết định **không can thiệp**. Đây lại là loại quyết định bị truy ngược nhiều nhất sau một sự cố.
- [R2] B0 hiện dễ bị phản biện coi là **strawman**. Bảng B.2 đã ghi "Không" cho 3/5 nhóm lỗi ở B0 theo thiết kế (`phuluc.md` L133–136), nhưng chưa định nghĩa ai và bằng cách nào "phát hiện" lỗi trên hồ sơ giấy. Ngoài ra, 20–30 hồ sơ cũ gần như chắc không cùng nhà xưởng với BIM, trái với câu "trên cùng BIM nhà xưởng" của RQ2 (`05_chuong5.md` L153).
- [R2] Ba câu hỏi của người quản lý và nhu cầu G-B đến nay hoàn toàn là [NCS] (GD3b L82, L102–108; REFINED L240: "Evidence is currently insufficient"). F-2 (3–5 người, một chủ đầu tư) quá mỏng để đỡ M3.
- **Khuyến nghị sơ bộ nếu nộp như dự kiến: major revision** (nghiêng về reject-resubmit nếu B0 giữ nguyên cách đo và không có dữ liệu người dùng thật).

---

## 2. Major

### M1. "Ai đã xử lý?" không trả lời được: schema chỉ ghi vai trò, không ghi tác nhân

- *Vị trí:* `phuluc.md` Bảng A.1 L34 (`inspector_role`), L43 (`timestamp`, `actor_role`); Bảng A.2 L77–85; B.1 C6 L119. `CLAUDE.md` §8 (STATUS_EVENT: `actor_role`), §10 L450 (câu hỏi 3).
- *Vấn đề:* C6 chỉ kiểm `actor_role` có thuộc tập vai trò được phép. Không có định danh người, tổ chức (chủ đầu tư, đơn vị kiểm định, nhà thầu) hay tư cách (chứng chỉ hành nghề, quyết định giao nhiệm vụ). Vì vậy:
  - (i) câu hỏi "Ai đã xử lý?" chỉ trả lời được ở mức "một người có vai trò kỹ sư kiểm tra";
  - (ii) không kiểm được tách nhiệm vụ. Cùng một người có thể mở hành động rồi tự xác minh, vì hai bước đều thuộc "Kỹ sư kiểm tra" (A.2 L79, L82). Theo TG [44] tr. 23 (`GNTQNBWM.md` mục 2), nguyên tắc là người tạo không xác nhận, người xác nhận không cho phép công bố. `CLAUDE.md` §6.1 ghi đề xuất tách nhiệm vụ của `mapping/garcia2026.md` Phần D mục 1 là "chờ NCS quyết định khi viết 5.5", nhưng đến nay chưa có quyết định.
- *Vì sao phản biện tạp chí quan tâm:* bài tự đặt tầng trách nhiệm làm đóng góp chính (5.8.2 L327) và dẫn [44] làm tiền lệ C6. Phản biện sẽ so ngay với [44]: [44] có tác giả, tổ chức, hai cấp ký (TG tr. 17–20, 21–25), còn bài chỉ có nhãn vai trò. Khi đó "accountability layer" bị coi là yếu hơn tiền lệ chính nó viện dẫn.
- *Yêu cầu sửa (kiểm được):*
  - (a) Trong phạm vi khóa: viết rõ ở Methods rằng `actor_role` là vai trò, còn câu hỏi 3 được trả lời ở mức vai trò cộng tham chiếu công việc (`reason`). Sửa câu hỏi 3 thành đúng mức mà schema trả lời được, hoặc ghi giới hạn ở mục 5.9.
  - (b) Ngoài phạm vi khóa (mục 6, Đ-1): thêm `actor_id` và `actor_org` vào STATUS_EVENT, INSPECTION_RECORD. Bổ sung một điều kiện vào C6: người xác minh khác người thực hiện, và khác người mở hành động.
- *Công sức:* S (sửa văn bản) / M (nếu duyệt Đ-1). *Mức:* **Nặng** (thành **Chặn** nếu giữ câu hỏi 3 nguyên văn trong bài).

### M2. Bảng A.2 thiếu đường ghi quyết định "không can thiệp / hoãn", loại quyết định bị truy ngược nhiều nhất

- *Vị trí:* `phuluc.md` A.2 L77–85 (5 bước chuyển; "bước chuyển không có trong bảng ... vi phạm C6"); `CLAUDE.md` QĐ 8 (4 trạng thái); kịch bản C3 `CLAUDE.md` L446.
- *Vấn đề:* với bằng chứng từ cảm biến, phần lớn ca đề nghị kiểm tra sẽ kết thúc bằng "đã xem, không cần can thiệp" hoặc "theo dõi, hoãn đến đợt dừng máy" [R2]. A.2 không cho chuyển Mở → Hoàn thành hay Mở → Đã xác minh. Vì vậy một quyết định không sửa chỉ có hai cách ghi, cả hai đều sai: để hành động Mở mãi, hoặc ghi một bước "Đang xử lý" giả. Trong khi đó, sau sự cố (kịch bản "sáu tháng sau", L446), câu hỏi pháp lý – bảo hiểm điển hình là *"ai đã quyết định không xử lý cảnh báo, dựa vào đâu"* [R2]. Đây đúng là chỗ G-B tự nhận là cần (GD3b L106: truy ngược quyết định về bằng chứng và người phê duyệt).
- *Vì sao quan trọng:* phản biện có kinh nghiệm vận hành sẽ thấy ngay. Một máy trạng thái chỉ mô tả "luồng sửa chữa thành công" sẽ bị gọi là không phản ánh quy trình thật. Ngoài ra, M2 sẽ có dương tính giả khi dữ liệu thật có quyết định không can thiệp.
- *Yêu cầu sửa (trong phạm vi khóa, vì A.2 ghi "đề xuất, khóa trước khi đo"):*
  - Thêm bước chuyển **Mở → Hoàn thành** do *Người phê duyệt* thực hiện, căn cứ bắt buộc là bản ghi sử dụng bằng chứng, `reason` thuộc tập {không can thiệp; hoãn đến <mốc>}, kèm điều kiện đổi `priority_level`.
  - Thêm **Hoàn thành → Đã xác minh** cho trường hợp không can thiệp: kỹ sư kiểm tra xác nhận theo dõi tiếp, không đổi `install_batch`.
  - Thêm **Đang xử lý → Mở** (trả lại).
  - Không thêm trạng thái mới nên không đụng QĐ 8.
  - Đưa ít nhất 3 lỗi chèn loại "quyết định không can thiệp không có căn cứ" vào danh sách M2.
- *Công sức:* S. *Mức:* **Nặng**.

### M3. B0 có nguy cơ strawman: chưa định nghĩa thủ tục "phát hiện" trên B0, và B0 không cùng nhà xưởng với BIM

- *Vị trí:* `phuluc.md` Bảng B.2 L130–138; `05_chuong5.md` L153 (RQ2 "Trên cùng BIM nhà xưởng, so với ... B0"), L197, L201; GD3b MT2 3(c) L152, Rủi ro L166–167; `CLAUDE.md` L361 ("B0, B1 và mô hình đề xuất dùng cùng danh sách lỗi chèn mù").
- *Vấn đề:*
  1. B.2 đã ghi B0 "Không" có trường để kiểm cho C3, C5, C9. Nếu M2(B0) được tính bằng *script*, B0 = 0 % ở ba nhóm theo định nghĩa, nên phép so sánh hiển nhiên đúng, giống điều GD3b tự thừa nhận về M1 (L160–161). Trên thực tế, lỗi trên hồ sơ giấy được phát hiện bởi **người rà soát**: trưởng phòng kỹ thuật, kỹ sư soát xét của đơn vị kiểm định [R2]. Thiết kế không có thủ tục đó.
  2. Hồ sơ B0 lấy ở đâu chưa được ghi. Một nhà xưởng tư nhân khó có 20–30 hồ sơ kiểm định [R2]. Vậy hồ sơ nhiều khả năng đến từ nhiều công trình hoặc từ kho hồ sơ của đơn vị kiểm định. Khi đó không thể "chèn lỗi vào B0 trên cùng BIM": phải dựng lại cùng kịch bản theo *mẫu B0* rút ra từ mã hóa.
  3. Lỗi chèn dựa trên cấu trúc ràng buộc (B.2 nối mỗi nhóm lỗi với đúng một ràng buộc), nên mô hình đề xuất có tỉ lệ phát hiện cao gần như theo thiết kế. Danh sách lỗi chưa được neo vào khiếm khuyết thực quan sát được trong hồ sơ.
- *Vì sao quan trọng:* đây là chỗ phản biện sẽ đánh mạnh nhất: "baseline was designed to fail". `CLAUDE.md` 2A đã chuyển đóng góp khoa học sang so với B1. Nhưng B0 vẫn được viết là "đóng góp bối cảnh – thực tiễn" (5.8.2 L336), nên con số B0 phải đứng được.
- *Yêu cầu sửa (trong phạm vi: thuộc "quy tắc mã hóa B0" và "cách tính M1–M4" phải khóa trước, GD3b L182–187):*
  - (a) Tách hai bước. **B0-mẫu** là tập trường và thực hành ghi chép rút ra từ 20–30 hồ sơ. **B0-ca** là cùng kịch bản và cùng tập bằng chứng của nhà xưởng có BIM, được viết lại theo B0-mẫu. RQ2 sửa câu chữ cho khớp.
  - (b) Định nghĩa **M2(B0) bằng rà soát của người**: ≥ 2 kỹ sư có kinh nghiệm soát xét hồ sơ kiểm định, không biết danh sách lỗi, giới hạn thời gian theo thực hành, có phiếu ghi. Báo cáo cả M2(B0-script) "theo thiết kế" lẫn M2(B0-người) "theo thực hành".
  - (c) Rút ít nhất một phần danh sách lỗi chèn từ **khiếm khuyết thật** quan sát được khi mã hóa B0 (thiếu ngày, thiếu người ký, tham chiếu cấu kiện mơ hồ, "đã khắc phục" không có biên bản kiểm lại). Ghi rõ tỉ lệ lỗi rút từ thực tế so với lỗi do thiết kế.
  - (d) Thêm vào danh sách lỗi một nhóm nằm ngoài năm ràng buộc, để báo cả phần không bắt được.
  - Chi tiết mã hóa ở mục 4(c).
- *Công sức:* M. *Mức:* **Chặn**.

### M4. Ba câu hỏi của người quản lý và nhu cầu G-B chưa có người thật xác nhận; F-2 hiện quá mỏng để đỡ M3

- *Vị trí:* `CLAUDE.md` L450, QĐ 12 (L58); GD3b L82 ("Phần diễn giải giữ nhãn [NCS]"), L102–108, F-2 L327–334; REFINED L240, L253; `05_chuong5.md` L197 ("được xác nhận với người quản lý ...").
- *Vấn đề:* ba câu hỏi do NCS đặt, được chọn sao cho khớp với ba tầng của schema: vị trí ↔ COMPONENT/EVIDENCE, tin cậy ↔ scope/uncertainty, ai/dựa vào đâu ↔ STATUS_EVENT. Nếu M3 đo thời gian trả lời đúng ba câu này, phép đo bị vòng tròn: câu hỏi được thiết kế từ đáp án. F-2 như đã duyệt gồm 3–5 người, một chủ đầu tư (đơn vị đã đồng ý hợp tác), 30 phút, mục đích "xác nhận". Mẫu này nhỏ, thiên lệch chọn, và dễ gợi ý câu trả lời.
- *Vì sao quan trọng:* với tạp chí kiểu AutCon/AEI, "requirements elicitation" là một bước của design science (GD3b MT2 mục 8 tự xếp bài vào hướng design science). Thiếu bước này, M3 bị coi là chỉ số tự đặt. REFINED L253 đã tự viết việc cần làm, nhưng chưa có trong thiết kế khóa.
- *Yêu cầu sửa:* thiết kế phỏng vấn tối thiểu ở mục 4(b). Điều kiện kiểm được:
  - giao thức và bộ câu hỏi phỏng vấn được commit trước buổi đầu;
  - bản ghi và mã hóa có hai người mã hóa;
  - bộ câu hỏi truy ngược sau phỏng vấn được commit **trước** lần đo M3 đầu;
  - bài báo có bảng "yêu cầu → câu hỏi → nguồn (mã người tham gia)".
- *Công sức:* M. *Mức:* **Nặng**.

### M5. Đổi `install_batch` gắn vào bước "Đã xác minh" tạo cửa sổ phạm vi sai; can thiệp không ghi nhận không bị phát hiện

- *Vị trí:* `phuluc.md` B.1 L118 (C5: `within_scope` theo `install_batch` hiện hành tại `used_at`), L122 ("đợt lắp đặt hiện hành ... đổi khi một hành động can thiệp ... chuyển sang 'Đã xác minh'; cách ghi cụ thể được khóa cùng đặc tả Bài báo 2"); A.3 L57.
- *Vấn đề:*
  1. Trạng thái vật lý của liên kết đổi lúc **thi công xong**, tức bước Hoàn thành, không phải lúc xác minh. Giữa Hoàn thành và Đã xác minh (vài ngày đến vài tuần, có khi không bao giờ xác minh) [R2], mọi bằng chứng cảm biến mới vẫn mang `install_batch` cũ. Khi đó C5 tính là "trong phạm vi", nhưng thực chất bằng chứng đã ngoài phạm vi. Đây đúng là loại lỗi bài muốn chặn. Nếu bước xác minh không bao giờ được làm, lỗi này kéo dài vô hạn.
  2. Can thiệp không qua ACTION không đổi `install_batch` và không bị phát hiện. Ví dụ: tổ bảo trì cơ điện tự siết bu lông, hoặc nhà thầu cầu trục chỉnh ray. Ở nhà xưởng tư nhân, loại can thiệp này có lẽ là nguồn rủi ro lớn nhất [R2; CẦN NGUỒN: thực hành ghi nhận can thiệp nhỏ ở nhà xưởng].
  3. C5 chỉ đòi `justification` khác rỗng. Mỗi lần siết lại làm mọi bằng chứng cũ của cấu kiện thành ngoài phạm vi, nên số lần phải ghi lý do tăng. Người dùng thật sẽ ghi lý do rập khuôn ("OK", "theo dõi"), và C5 vẫn qua [R2].
- *Vì sao quan trọng:* phản biện từ phía vận hành sẽ hỏi: "the scope is reset at verification, not at intervention: what about the window in between?" và "how are unrecorded interventions handled?". Nếu không có câu trả lời, nhóm lỗi trọng tâm C5 bị nghi ngờ ngay ở giả định.
- *Yêu cầu sửa (trong phạm vi: B.1 L122 để mở "cách ghi cụ thể"):*
  - (a) Gắn việc đổi `install_batch` vào **thời điểm can thiệp thực tế**: `timestamp` của sự kiện Đang xử lý → Hoàn thành, kèm tham chiếu biên bản công việc. Bước Đã xác minh chỉ xác nhận đợt mới hợp lệ.
  - (b) Bằng chứng tạo trong cửa sổ Hoàn thành – Đã xác minh được đánh dấu ngoài phạm vi, cho tới khi có xác minh. Đây là một quy tắc tính `within_scope`, không phải ràng buộc mới.
  - (c) Ghi ở mục giới hạn: can thiệp không ghi nhận nằm ngoài khả năng phát hiện của năm ràng buộc. Ghi MT3 có thể quan sát gián tiếp qua dịch chuyển đường cơ sở, nhưng không tuyên bố.
  - (d) Trong M2, thêm lỗi "lý do rập khuôn". Báo cáo C5 chỉ bắt được lý do rỗng, không bắt được lý do vô nghĩa.
- *Công sức:* S–M. *Mức:* **Nặng**.

### M6. Bảng A.2 chưa khớp tổ chức thật của chủ đầu tư; thiếu đơn vị kiểm định độc lập và nhà thầu sửa chữa

- *Vị trí:* `phuluc.md` A.2 L77–85 (ba vai trò; "Tên vai trò theo tổ chức của chủ đầu tư được điền khi khóa đặc tả"); `CLAUDE.md` L446 (kỹ sư A, trưởng phòng B); `04_chuong4.md` 4.1.2 L26 ("hồ sơ kiểm tra ... do một người hoặc đơn vị có trách nhiệm").
- *Vấn đề:* xem trả lời (a) ở mục 4. Tóm tắt: "kỹ sư kiểm tra" trong A.2 gộp hai chủ thể khác nhau về pháp nhân và trách nhiệm:
  - kỹ sư bảo trì nội bộ của chủ đầu tư, người theo dõi hằng ngày;
  - kỹ sư của đơn vị kiểm định độc lập, người lập hồ sơ kiểm định (B0) và ký kết luận [R2].
  "Người thực hiện" phần lớn là nhà thầu bên ngoài. Nhà thầu không có quyền ghi vào hệ của chủ đầu tư, nên bước Đang xử lý → Hoàn thành thực tế do người nhận bàn giao phía chủ đầu tư ghi thay [R2]. Đây là một điểm M4 phải tính.
- *Vì sao quan trọng:* ma trận vai trò là phần dễ kiểm chứng nhất với người đọc từ ngành. Ma trận sai tổ chức làm hỏng tính thực tế của toàn bộ tầng trách nhiệm.
- *Yêu cầu sửa (trong phạm vi):*
  - Bổ sung một bảng "vai trò A.2 ↔ chức danh/đơn vị thật" cho nhà xưởng MT3, lấy từ phỏng vấn F-2.
  - Mỗi vai trò ghi thuộc tổ chức nào (chủ đầu tư / đơn vị kiểm định / nhà thầu).
  - Ghi rõ ai nhập dữ liệu cho từng bước chuyển. Nếu là người khác người thực hiện, ghi rõ điều đó.
  - Thêm vai trò "đơn vị kiểm định độc lập" vào tập giá trị `actor_role` (giá trị, không phải trường mới).
- *Công sức:* S. *Mức:* **Nặng**.

### M7. M4 (phút/bản ghi) chưa so được với B0 và dễ làm bài yếu đi nếu trình bày trơn

- *Vị trí:* `CLAUDE.md` L372; GD3b L163; `05_chuong5.md` L197, L139.
- *Vấn đề:*
  - Đơn vị không tương thích. B0 là *báo cáo*, mất giờ đến ngày để lập. Mô hình đề xuất có *nhiều bản ghi nhỏ*, phút mỗi bản ghi. "Phút/bản ghi" vì vậy có thể làm B0 có vẻ đắt hay rẻ tùy cách đếm.
  - Chưa tách trường điền tự động (EVIDENCE từ pipeline: 0 phút người) với trường điền tay (INSPECTION_RECORD, STATUS_EVENT, `justification`).
  - Chưa nói *ai* đo. Nếu NCS tự ghi, đó là cận dưới của một chuyên gia quen hệ.
- *Vì sao quan trọng:* chi phí ghi nhận là rào cản áp dụng đã được nêu trong tài liệu (`CLAUDE.md` 7.5 dòng L2.1: Cawley 2018, Ostachowicz 2019 nêu chi phí là rào cản; Tiểu luận gắn ý này với chỉ số chi phí). Nếu M4 cao hơn B0 nhiều mà không có khung lợi ích – chi phí, phản biện sẽ dùng chính M4 để kết luận "không khả thi cho chủ đầu tư".
- *Yêu cầu sửa:* xem trả lời (e) ở mục 4. Tóm tắt:
  - đổi đơn vị so sánh sang **phút người trên một chu trình "phát hiện → đóng"** (một kịch bản), tách theo vai trò và theo tự động/tay;
  - đo trên người ghi không phải NCS (≥ 2 người);
  - báo cáo M4 cạnh M2 theo nhóm lỗi, thành dạng "phút tăng thêm trên một lỗi bắt thêm được so với B1".
- *Công sức:* S–M. *Mức:* **Nặng**.

## 3. Minor

- **m1. Vị thế pháp lý của B0 chưa được nêu.**
  - *Vị trí:* GD3b L175–176; `05_chuong5.md` L155.
  - *Vấn đề:* bài gọi B0 là "thực hành hiện hành ở Việt Nam" nhưng chưa có căn cứ, nên B0 có thể bị đọc là mẫu của một đơn vị.
  - *Sửa:* xem 4(d). Đổi câu chữ thành "observed practice in the sampled records" cho đến khi có nguồn. *S.*
- **m2. Kịch bản C3 dựng lại có thể bị nhầm với sự cố thật.**
  - *Vị trí:* `CLAUDE.md` L446 ("sáu tháng sau có sự cố"); MT3 quan trắc 3–6 tháng (2A).
  - *Vấn đề:* sự cố thật trong 3–6 tháng gần như không xảy ra, nên phần "sáu tháng sau" sẽ là truy ngược dựng lại.
  - *Sửa:* ghi rõ là kịch bản dựng lại. Giữ nguyên tắc của OUTLINE 4.5 (L143): "rà soát tư liệu hồi cứu được gọi đúng là rà soát tư liệu". *S.*
- **m3. Bài chưa nói ai cập nhật mô hình trong vận hành.**
  - *Vị trí:* A.1 `model_version` L16; 2A ("BIM nhà xưởng thật").
  - *Vấn đề:* bài chưa nói ai giữ và cập nhật BIM/IFC trong vận hành. Nhà xưởng tư nhân thường không có bộ phận BIM [R2; CẦN NGUỒN: mức dùng BIM trong vận hành nhà xưởng ở Việt Nam].
  - *Sửa:* nêu giả định về "người quản lý thông tin" (đơn vị tư vấn hay chủ đầu tư) ở Methods. *S.*
- **m4. Hồ sơ B0 có thể do chính NCS hoặc đơn vị của NCS lập.**
  - *Vị trí:* `CLAUDE.md` 7.5 L321 ("nhận định của NCS từ thực tế kiểm định").
  - *Vấn đề:* nếu đúng vậy thì NCS vừa là tác giả hồ sơ, vừa là người mã hóa, vừa là người thiết kế mô hình.
  - *Sửa:* khai báo xung đột lợi ích. Người mã hóa thứ hai không thuộc đơn vị lập hồ sơ. *S.*
- **m5. Bảo mật và chia sẻ dữ liệu B0.**
  - *Vấn đề:* hồ sơ kiểm định là tài liệu của chủ đầu tư.
  - *Sửa:* cần văn bản đồng ý sử dụng của chủ đầu tư/đơn vị kiểm định, ẩn danh tên công trình, chủ đầu tư và người ký. Tuyên bố dữ liệu của bài chỉ công bố bảng mã hóa ẩn danh và sổ mã (codebook). *S.*
- **m6. Bảng A.2 chưa nối với `priority_level`.**
  - *Vị trí:* A.2 không có cột mức ưu tiên; A.4 L87.
  - *Vấn đề:* chủ đầu tư quyết định theo mức ưu tiên kết hợp với lịch dừng sản xuất [R2]. Hiện chưa có quy tắc nào nói "Kiểm tra ưu tiên" thì Mở → Đang xử lý phải trong bao lâu.
  - *Sửa:* nếu không đưa vào ràng buộc, ghi là hướng phát triển. Không thêm ràng buộc. *S.*
- **m7. "Người thứ ba" chèn lỗi nên có kinh nghiệm kiểm định.**
  - *Vị trí:* GD3b L184.
  - *Sửa:* người chèn lỗi nên là kỹ sư có kinh nghiệm kiểm định, không chỉ "không tham gia thiết kế", để lỗi giống lỗi thật. Ghi tiêu chí chọn người chèn trong tệp khóa. *S.*
- **m8. Số liệu BIM trong hồ sơ cũ chưa truy được nguồn.**
  - *Vị trí:* P2A-0 mục 5 điểm 3; Đ15.
  - *Vấn đề:* số liệu BIM (718/676, 8 cặp GUID) chưa truy được nguồn, và thỏa thuận với chủ đầu tư "chưa xác nhận ký" theo tệp 06_PAPER_3. Phản biện sẽ hỏi về quyền dùng BIM và hồ sơ.
  - *Sửa:* có văn bản thỏa thuận trước khi khóa B0. Ghi trong bài ở dạng "with the owner's written consent". *S.*

---

## 4. Trả lời các câu hỏi bắt buộc

### (a) Ai trong đơn vị chủ đầu tư dùng chuỗi này, dùng khi nào? Bảng A.2 có khớp tổ chức thật không? Thiếu vai trò nào?

**Bảng A.2 hiện có** (`phuluc.md` L77–83):

| Vai trò A.2 | Bước chuyển |
|---|---|
| Kỹ sư kiểm tra | (tạo) → Mở; Hoàn thành → Đã xác minh; Hoàn thành → Mở |
| Người phê duyệt | Mở → Đang xử lý |
| Người thực hiện | Đang xử lý → Hoàn thành |

Tên vai trò thật để "điền khi khóa đặc tả" (L85).

**Tổ chức thường gặp ở một nhà xưởng tư nhân khung thép** [R2, nhận định nghề nghiệp; chưa có nguồn trong `notes/`, cần F-2 xác nhận]:

| Chủ thể | Thuộc | Dùng chuỗi khi nào | Ứng với A.2 |
|---|---|---|---|
| Kỹ sư/trưởng ca bảo trì (phòng cơ điện, bộ phận bảo trì) | Chủ đầu tư | Hằng ngày – hằng tuần: nhận cảnh báo theo `priority_level`, đi kiểm tra bằng mắt, siết bu lông nhỏ | "Kỹ sư kiểm tra" (nội bộ) và nhiều khi cả "người thực hiện" |
| Trưởng phòng kỹ thuật / giám đốc nhà máy | Chủ đầu tư | Khi cần dừng máy, chi ngân sách, gọi nhà thầu | "Người phê duyệt" |
| Cán bộ an toàn (HSE) | Chủ đầu tư | Khi mức ưu tiên cao, liên quan cầu trục, khu vực người làm việc | **Thiếu** |
| Kỹ sư đơn vị kiểm định độc lập | Bên thứ ba có pháp nhân riêng | Kiểm định định kỳ hoặc theo yêu cầu, sau sự cố; ký kết luận; **là người lập hồ sơ B0** | Bị gộp vào "Kỹ sư kiểm tra"; **thiếu vai trò riêng** |
| Nhà thầu sửa chữa/gia cường | Bên thứ ba | Thi công can thiệp; lập biên bản công việc | "Người thực hiện", nhưng **không có quyền ghi** vào hệ của chủ đầu tư |
| Đơn vị tư vấn/quản lý thông tin (có thể là nhóm NCS) | Bên thứ ba | Duy trì BIM, pipeline bằng chứng, chạy script kiểm | **Thiếu**; là tác nhân tạo `EVIDENCE` |
| Cơ quan quản lý nhà nước / bảo hiểm | Bên ngoài | Chỉ khi sự cố hoặc thanh tra; là **người hỏi** ba câu hỏi, không ghi | Không cần vai trò ghi, nhưng là người dùng của truy ngược |

**Kết luận (a):**
1. Ba vai trò của A.2 khớp *luồng nội bộ* của một chủ đầu tư có bộ phận kỹ thuật. Bảng chưa phân biệt **pháp nhân**: cùng nhãn "kỹ sư kiểm tra" nhưng kết luận của đơn vị kiểm định độc lập có giá trị pháp lý và trách nhiệm khác hẳn kết luận của kỹ sư bảo trì nội bộ [R2]. Bước Hoàn thành → Đã xác minh có tách được người xác minh khỏi người sửa hay không phụ thuộc đúng vào phân biệt này (M1, M6).
2. Vai trò thiếu, theo thứ tự cần: **đơn vị kiểm định độc lập** (thêm làm giá trị của `actor_role`); **nhà thầu**, kèm quy ước "người nhập thay" (ghi trong `reason` hoặc trong Methods); **tác nhân hệ thống/tư vấn** tạo EVIDENCE (A.1 hiện không có trường người tạo cho EVIDENCE; `method_version` chỉ ghi mã). Cơ quan quản lý không cần vai trò ghi nhưng nên được nêu là người dùng câu hỏi 3.
3. **"Dùng khi nào":** chuỗi có ba thời điểm dùng. (i) Khi có bằng chứng mới hoặc mức ưu tiên đổi: kỹ sư bảo trì, hằng tuần. (ii) Khi lập kế hoạch dừng máy hoặc bảo trì năm: trưởng phòng kỹ thuật. (iii) Khi sự cố, thanh tra, bàn giao hoặc chuyển nhượng tài sản: người quản lý, bảo hiểm, đơn vị kiểm định. Ba câu hỏi của `CLAUDE.md` L450 chủ yếu phục vụ thời điểm (iii). Bài nên nói rõ M3 đo cho thời điểm nào [R2].
4. Thiếu bước chuyển "không can thiệp / hoãn" (M2).

### (b) Ba câu hỏi đã được người thật xác nhận chưa? Phản biện sẽ nói gì? Thiết kế phỏng vấn tối thiểu

**Hiện trạng:**
- **Chưa.** Ba câu hỏi xuất hiện từ góp ý G5 của thầy (`CLAUDE.md` §3: "1.4 ba câu hỏi") và do NCS soạn.
- GD3b ghi "Vì sao quan trọng" của G-B chủ yếu là [NCS] (L102–108). Lý do đề xuất F-2 là để "biến phần 'vì sao quan trọng' của G-B từ diễn giải thành có căn cứ" (L330–331).
- Hồ sơ cũ tự ghi "Nguồn yêu cầu từ người dùng thực (phỏng vấn đơn vị quản lý vận hành) chưa có: Evidence is currently insufficient" (REFINED L240).
- `05_chuong5.md` L197 viết bộ câu hỏi "được xác nhận với người quản lý". Câu này đang mô tả một việc chưa làm như thể đã làm; cần giữ ở thì dự kiến.

**Phản biện sẽ nói** [R2, dự đoán]:
1. "The three manager questions appear to be researcher-defined and mirror the three layers of the proposed schema; M3 therefore measures how well the schema answers questions derived from itself."
2. "Three to five interviewees from the single partner owner are insufficient to claim requirements validity; selection bias toward a cooperative owner."
3. "Confirmation-style interviews (presenting the questions and asking for agreement) do not elicit requirements."
4. "No evidence that owners in practice need post-repair verification records or evidence validity scope."

**Thiết kế tối thiểu để đủ sức nặng.** Phần trong khuôn F-2 đã duyệt và phần vượt khuôn được tách riêng. Phần vượt ở mục 6, Đ-2.

| Hạng mục | Tối thiểu trong khuôn F-2 | Lý do |
|---|---|---|
| Số người | 5 (cận trên của F-2), trải ≥ 3 vai trò: kỹ sư/trưởng bảo trì, trưởng phòng kỹ thuật hoặc giám đốc nhà máy, HSE hoặc người phụ trách hồ sơ | Một vai trò thì không kiểm được ma trận A.2 |
| Thời lượng | 30–40 phút, bán cấu trúc | Giữ chi phí nhỏ như F-2 |
| Thứ tự câu hỏi | **Khơi gợi trước, đối chiếu sau.** Phần 1 hỏi mở: "Lần gần nhất anh/chị phải tìm lại vì sao một liên kết được sửa hoặc không sửa, anh/chị cần biết gì, tìm ở đâu, mất bao lâu?" (kỹ thuật sự cố điển hình). Phần 2 mới đưa ba câu hỏi và kịch bản C3 để đánh giá (cần / không cần / thiếu gì). Phần 3 đưa bảng A.2 để người tham gia chỉ ra chức danh thật cho từng vai trò và bước chuyển còn thiếu | Tránh gợi ý câu trả lời; lấy được lỗi thật cho M2 và vai trò thật cho A.2 |
| Câu hỏi bắt buộc khác | Ai ký nghiệm thu sau sửa; có kiểm lại sau siết bu lông không; ai được ghi vào hồ sơ; hồ sơ lưu bao lâu, ở đâu; lần gần nhất bị thanh tra hoặc bảo hiểm hỏi gì; chấp nhận thêm bao nhiêu phút mỗi lần ghi | Neo M4, (e), (d) |
| Cách ghi | Ghi âm khi có đồng ý, nếu không thì ghi tay hai người. Gỡ băng, ẩn danh (mã P1–P5, chỉ ghi vai trò và loại tổ chức) | Kiểm lại được |
| Phân tích | Phân tích chủ đề theo sổ mã khóa trước. Hai người mã hóa độc lập trên toàn bộ bản gỡ băng; báo mức đồng thuận và cách giải bất đồng | Không dựa vào một người diễn giải |
| Đồng thuận | Phiếu đồng ý bằng văn bản: mục đích, quyền rút lui, ẩn danh, dùng trích dẫn ẩn danh trong bài. Thủ tục đạo đức theo quy định của trường [CẦN KIỂM: NTU có hội đồng đạo đức hoặc thủ tục miễn xét cho phỏng vấn chuyên gia không]. Cần thầy duyệt (QĐ 12) | Tạp chí thường yêu cầu tuyên bố đạo đức cho nghiên cứu có người tham gia [R2] |
| Khóa trước M3 | Thứ tự commit: (1) giao thức và bộ câu hỏi phỏng vấn, trước buổi đầu; (2) bản tổng hợp yêu cầu và bảng "yêu cầu → câu hỏi truy ngược → mã người tham gia"; (3) bộ câu hỏi truy ngược cuối và cách tính M3, **trước** khi dựng B0-ca, B1 và chạy M3. Mọi sửa sau (3) ghi thành phiên bản mới, có lý do | Đúng D8 (GD3b L182–189) |
| Sản phẩm trong bài | Một bảng yêu cầu, kèm 2–4 trích dẫn ẩn danh. Câu hỏi nào người tham gia không xác nhận thì vẫn giữ trong M3 nhưng ghi là "researcher-defined" | Minh bạch |

Nếu không làm F-2, GD3b F-2 đã ghi phương án (L332): hạ G-B xuống "đóng góp thực tiễn, kiểm bằng M3" và ghi nhật ký. [R2] Theo tôi phương án này không đủ, vì M3 khi đó vẫn vòng tròn (xem M4).

### (c) B0 có đồng nhất để mã hóa không? Rủi ro, quy tắc mã hóa, người mã hóa, độ tin cậy, nguy cơ strawman

**Đồng nhất:** gần như chắc **không** [R2]. GD3b đã tự nêu rủi ro "không đồng nhất về mẫu và mức chi tiết" (L166–167), nhưng biện pháp giảm ("khóa quy tắc, ghi trường nào không có, báo theo loại") chưa đủ. Các nguồn không đồng nhất:

| Nguồn không đồng nhất | Rủi ro | Biện pháp đề xuất (trong phạm vi khóa) |
|---|---|---|
| **Loại hồ sơ:** kiểm định chất lượng, đánh giá an toàn chịu lực, kiểm định định kỳ, báo cáo quan trắc (lún, nghiêng, chuyển vị), kiểm tra sau sự cố, biên bản nghiệm thu sửa chữa [R2; tên loại và căn cứ CẦN NGUỒN] | Mỗi loại có mục đích khác nhau. Quan trắc có số đo nhưng không có hành động; kiểm định có kết luận nhưng ít theo dõi khắc phục. Gộp chung thì "B0 thiếu trường X" chỉ phản ánh loại hồ sơ | Phân tầng. Khóa tiêu chí nhận: chỉ nhận hồ sơ có ít nhất một phát hiện về liên kết hoặc cấu kiện thép và một kiến nghị xử lý. Báo M1/M2(B0) **theo từng loại**; nếu một loại có < 5 hồ sơ thì chỉ mô tả |
| **Đơn vị lập** | Mẫu biểu riêng của từng đơn vị. B0 thành "mẫu của đơn vị A" | Ghi số đơn vị lập. Yêu cầu tối thiểu ≥ 2 đơn vị (lý tưởng ≥ 3). Không nhận > 50 % hồ sơ từ một đơn vị; nếu không đạt thì ghi giới hạn |
| **Năm lập** | Mẫu biểu đổi theo thời gian và theo văn bản quy định | Ghi năm. Ưu tiên hồ sơ gần đây; nêu khoảng năm |
| **Công trình khác nhà xưởng có BIM** | Không chèn lỗi được "trên cùng BIM" | Tách B0-mẫu và B0-ca (M3 ở mục 2): mã hóa để rút ra *mẫu thực hành*, rồi dựng kịch bản của nhà xưởng có BIM theo mẫu đó. Nếu nhà xưởng MT3 có hồ sơ cũ, dùng chúng làm nhóm con "cùng công trình" để kiểm chéo |
| **Đơn vị mã hóa** | Hồ sơ, phát hiện hay kiến nghị? Chọn sai đơn vị thì M1 lệch | Khóa trước: đơn vị = **một phát hiện kèm kiến nghị xử lý** (≈ một chuỗi INSPECTION_RECORD → ACTION); hồ sơ là cụm |

**Quy tắc mã hóa (sổ mã, khóa trước):**
1. Danh sách trường B0 suy từ Bảng A.1. Mỗi trường mã hóa {có, rõ ràng / có, mơ hồ / không có / không áp dụng}. Ví dụ: cấu kiện định danh theo trục và cao độ được tính là "có"; "khu vực mái" là "mơ hồ".
2. Các khái niệm mà B0 không có (phạm vi hiệu lực, phiên bản phương pháp) ghi "không có", **không suy ra**, đúng như GD3b L166.
3. Trường hợp "đã khắc phục" không có biên bản kiểm lại được mã riêng. Đây là bằng chứng thực cho nhu cầu bước "Đã xác minh".
4. Ghi riêng các **khiếm khuyết ghi chép quan sát được** để làm nguồn cho danh sách lỗi M2 (M3 ở mục 2, điểm c).
5. Trích một số dòng ẩn danh làm ví dụ cho sổ mã.

**Ai mã hóa:** hai người.
- Người 1 là NCS.
- Người 2 là kỹ sư kiểm định, **không thuộc đơn vị lập phần lớn hồ sơ** và không tham gia thiết kế schema.
- Thứ tự: mã hóa thử 3–5 hồ sơ để chỉnh sổ mã, sổ mã khóa (commit), rồi mã hóa độc lập toàn bộ.
- Báo cáo độ tin cậy giữa hai người mã hóa theo từng trường (Cohen's κ hoặc Krippendorff's α; chọn khi khóa) và cách giải bất đồng. Trường có độ tin cậy thấp chỉ dùng mô tả. Ngưỡng nhận κ là quyết định khóa trước, [NCS ĐIỀN].

**B0 có thể bị dựng yếu thế nào (strawman) và cách chặn:**

| Cách dựng yếu | Cách chặn |
|---|---|
| Tính M2(B0) bằng script trên trường không tồn tại → 0 % theo định nghĩa (B.2) | M2(B0) đo bằng **rà soát của người** (≥ 2 kỹ sư, không biết danh sách lỗi, giới hạn thời gian). Báo cả hai con số, ghi rõ con số nào "theo thiết kế" |
| Chọn hồ sơ cũ, sơ sài, từ một đơn vị yếu | Tiêu chí nhận và phân tầng ở trên; ghi khung lấy mẫu; báo cả hồ sơ bị loại và lý do |
| Bỏ qua kênh thông tin ngoài hồ sơ (sổ giao ca, email, ảnh, nhật ký nhà thầu) mà người thật dùng để trả lời ba câu hỏi | Khi đo M3(B0), cho người trả lời dùng **toàn bộ** hồ sơ mà chủ đầu tư thực có (kể cả biên bản nghiệm thu), không chỉ báo cáo kiểm định. Hỏi trong F-2 họ thực sự tìm ở đâu |
| Chèn vào B0 những lỗi B0 không bao giờ có lý do để mắc (ví dụ ánh xạ cảm biến hết hạn khi B0 không có cảm biến) rồi tính "B0 bỏ sót" | Chỉ tính M2(B0) trên nhóm lỗi **áp dụng được** cho B0 (C1, C6 và các khiếm khuyết thực). Nhóm C3, C5, C9 ghi "không áp dụng cho B0", **không** ghi 0 %. So sánh ở ba nhóm này chỉ làm với B1 |
| Dùng M1 (đủ trường) làm lợi thế | Đã chặn ở GD3b L160–161 và `CLAUDE.md` L369; giữ |

### (d) Điều khoản pháp lý về hồ sơ kiểm định: bài quốc tế có cần không, đặt ở đâu, rủi ro nếu thiếu

**Hiện trạng:**
- GD3b L175–176 ghi `[CẦN NGUỒN: văn bản quy định hồ sơ kiểm định nhà công nghiệp]`. Zotero có [11], Thông tư 32/2026, TCVN 9381, nhưng điều khoản về hồ sơ chưa được đối chiếu (N-31).
- REFINED L240 nhắc "Nghị định 207/2026/NĐ-CP" với ghi chú "Legal reference pending official-source verification". P2A-0 mục 5 ghi [CẦN KIỂM].
- Tôi không kiểm và không dẫn nội dung các văn bản này. Cả bốn tên văn bản trên đều **[CẦN KIỂM]** (số hiệu, hiệu lực, điều khoản).

**Có cần không:** cần, nhưng **ở mức tối thiểu và đúng chức năng**.
- Bài quốc tế không cần phân tích pháp lý.
- Bài cần 2–4 câu định nghĩa B0. B0 là bản ghi do *ai* lập theo *yêu cầu nào*, gồm *những gì tối thiểu*, lưu ở *đâu*, có bắt buộc ghi xác nhận sau sửa chữa không.
- Không có những câu này, khái niệm "current practice" của B0 không có neo.

**Đặt ở đâu:**
- (1) Methods, tiểu mục "Baselines – B0": 2–3 câu cộng một trích dẫn văn bản đã đối chiếu.
- (2) Tài liệu bổ sung: một bảng "yêu cầu hồ sơ theo văn bản ↔ trường A.1".
- (3) Discussion, đúng một câu: kết quả B0 phản ánh thực hành trong mẫu hồ sơ, **không** phải đánh giá sự tuân thủ pháp luật.
- Không đặt trong Introduction như một luận điểm "quy định Việt Nam thiếu…". Câu đó dễ thành tuyên bố pháp lý không đủ căn cứ.

**Rủi ro nếu thiếu:**
1. B0 bị coi là tùy tiện hoặc là mẫu của một đơn vị (liên quan M3).
2. Nếu văn bản thực ra *đã* bắt buộc ghi người phê duyệt hay biên bản sau sửa, phần "B0 thiếu" có thể là **không tuân thủ** của hồ sơ trong mẫu, không phải giới hạn của thực hành. Khi đó diễn giải đóng góp "bối cảnh – thực tiễn" (2A) đổi nghĩa.
3. Phản biện người Việt hoặc khu vực có thể chỉ ra sai sót pháp lý, làm mất uy tín toàn bài.

**Cách xử lý khi chưa có nguồn:**
- Viết B0 là "observed recording practice in N sampled records from K organisations".
- Bỏ mọi câu về yêu cầu pháp lý.
- Giữ `[CẦN NGUỒN]` trong bản nháp. Pha 2 tìm văn bản, đọc **điều khoản cụ thể**, ghi số điều và ngày truy cập.

### (e) Bước "đã xác minh sau sửa chữa" và đổi `install_batch`: có thực tế không, ai làm, tốn gì; M4 có làm bài yếu đi không

**Thực tế đến đâu** [R2, nhận định nghề nghiệp, cần F-2 xác nhận]:
- Với siết lại bu lông thông thường ở nhà xưởng tư nhân, "xác minh" thường chỉ là nghiệm thu nội bộ. Tổ bảo trì hoặc nhà thầu tự kiểm lực siết (cờ lê lực, đánh dấu), người phụ trách ký biên bản. Một lần kiểm tra độc lập riêng là hiếm, trừ gia cường lớn hoặc sau sự cố.
- Tài liệu cho thấy nhu cầu, không cho thấy thực hành. [22] tr. 192 (TG, qua GD3b L96): bảo trì nhà thép công nghiệp cần theo dõi giai đoạn và tiến độ khắc phục. [35] tr. 10 (TG): "có bảo trì thì đã sửa" là đơn giản hóa.
- Vì vậy bước Đã xác minh **thực tế được nếu định nghĩa vừa đủ**. "Bản ghi kiểm tra sau sửa chữa" (A.2 L82) nên chấp nhận *biên bản nghiệm thu kèm số đo lực siết hoặc ảnh*, do một vai trò khác người thực hiện lập. Không nên đòi kiểm định lại.
- Nếu đòi kiểm định độc lập cho mọi can thiệp, chủ đầu tư sẽ bỏ qua bước này. Hành động sẽ dừng ở Hoàn thành mãi, và `install_batch` không bao giờ đổi (M5).

**Ai làm, tốn gì:**

| Việc | Ai | Chi phí chính |
|---|---|---|
| Ghi Hoàn thành + tham chiếu biên bản công việc | Người nhận bàn giao phía chủ đầu tư (nhập thay nhà thầu) | Vài phút nếu có biên bản; chậm nếu biên bản giấy đến muộn |
| Kiểm lại sau sửa, lập bản ghi kiểm tra sau sửa | Kỹ sư bảo trì (khác người thi công) hoặc đơn vị kiểm định nếu can thiệp lớn | Một lượt lên cấu kiện (có khi phải dừng cầu trục hoặc dùng xe nâng người); cờ lê lực; ảnh |
| Đổi `install_batch` | Tự động theo quy tắc khi có sự kiện can thiệp (đề xuất M5a) | Gần 0 phút người |
| **Hệ quả của đổi `install_batch`** | Pipeline, tư vấn | Mọi bằng chứng cũ của cấu kiện thành ngoài phạm vi. Ở MT3, đường cơ sở Autoencoder cho cấu kiện đó phải lập lại, nên có **khoảng mù** đến khi đủ dữ liệu mới [R2]. Đây là chi phí thật lớn nhất và phải được nêu |
| Ghi `justification` mỗi lần dùng bằng chứng ngoài phạm vi trong khoảng mù | Kỹ sư kiểm tra | Tăng theo số lần can thiệp; dễ thành lý do rập khuôn (M5) |

**M4 có làm bài yếu đi không:**
- Có, nếu trình bày trơn "phút/bản ghi, đề xuất > B0". M4 của mô hình đề xuất gần như chắc cao hơn B0 tính theo phút người, vì có thêm STATUS_EVENT, `justification` và bản ghi xác minh [R2].
- Không làm yếu bài nếu sửa theo M7, tức là:
  - (1) đơn vị chung là **phút người trên một chu trình phát hiện → đóng**, tách theo vai trò;
  - (2) tách phần **tự động** (EVIDENCE, `within_scope`, đổi `install_batch`) khỏi phần **tay**;
  - (3) đo trên ≥ 2 người ghi không phải NCS, hoặc ghi rõ M4 của NCS là cận dưới;
  - (4) báo **chi phí biên** so với **B1**, không phải so với B0: "+x phút mỗi chu trình để bắt thêm y lỗi thuộc nhóm C5/C6/C9". So với B0, đơn vị không tương thích (báo cáo so với bản ghi);
  - (5) hỏi trong F-2 mức phút tăng thêm mà người dùng chấp nhận, rồi dùng làm ngưỡng diễn giải đã khóa trước (không làm ngưỡng đạt/không đạt).
- Một bài thẳng thắn rằng "trách nhiệm có giá X phút" thuyết phục phản biện từ ngành hơn một bài lờ M4 đi [R2].

---

## 5. Đáng giữ / nên bỏ từ hồ sơ cũ (lớp 2), theo góc nhìn R2

**Đáng giữ:**
1. Mục A.2.6 của `gate2_3_data_model_v0.2.md` (L184–208): ACTION_STATUS_EVENT có `Actor_ID` **và** `Actor_Role`, `Basis_Refs`, `Post_Action_Verification_Ref`. R12 ("đóng hành động phải có xác minh sau hành động"). Đây là cơ sở để sửa M1 (tác nhân) và (e) (tham chiếu xác minh).
2. `Acknowledged_By` của EVIDENCE_USE (data model L181): người đã đọc phạm vi hiệu lực trước khi dùng. Ứng với yêu cầu trách nhiệm khi dùng ngoài phạm vi (C5). Có thể dùng như nội dung của `justification` mà không thêm trường.
3. REFINED mục 10.1 (L238–253): nguyên tắc "CQ phải xuất phát từ yêu cầu thông tin thực" và việc cần làm (bao phủ yêu cầu → CQ). Đây là khung đúng cho F-2.
4. OUTLINE 3.3 (L93–95): người xây dựng quy tắc không quyết định đáp án cho ca lỗi. Nên mở rộng thành "người chèn lỗi có kinh nghiệm kiểm định" (m7).
5. OUTLINE 4.5 (L143): rà soát tư liệu hồi cứu được gọi đúng tên (m2).
6. OUTLINE 3.4, dòng "Thời gian truy ngược" (L106): giới hạn diễn giải "không suy rộng thành tăng hiệu quả quyết định bảo trì nếu chưa có nghiên cứu người dùng". Giữ nguyên cho M3.
7. REFINED L185 và OUTLINE 3.2: tách xác nhận vị trí vật lý khỏi xác minh định danh IFC. Cần cho câu trả lời "ở đâu?" ở hiện trường.

**Nên bỏ:**
1. Mọi câu xem ACTION/STATUS_EVENT là ngoài lõi (REFINED; P2A-0 Đ2). Nhìn từ chủ đầu tư, đây là phần có giá trị nhất.
2. `Record_Status` của hồ sơ kiểm tra (draft → submitted → reviewed → closed, data model L172) chạy song song với `Action_Status`. Ba trục trạng thái sẽ làm người dùng rối. Giữ hai trục theo QĐ 8.
3. Máy 9 trạng thái (D3, P2A-0 3.2). Không khớp với tổ chức nhà xưởng tư nhân [R2].
4. Câu "Nghị định 207/2026/NĐ-CP" ở REFINED L240 dùng như tham chiếu nội dung hồ sơ bảo trì, khi chưa kiểm.
5. OUTLINE 8 (L221): "tránh suy rộng sang ... khả năng áp dụng tại nhà xưởng thực". Câu này lỗi thời vì MT3 nay có nhà xưởng thật. Thay bằng ranh giới "khả thi và truy vết" của 2A.
6. "Tra cứu thủ công" làm đối chứng thời gian duy nhất (P2A-0 Đ7). Phải thay bằng B0 có thủ tục rõ (mục 4(c)).

---

## 6. Đề xuất ngoài phạm vi khóa – chờ NCS duyệt

- **Đ-1. Thêm định danh tác nhân và một điều kiện tách nhiệm vụ (liên quan M1).**
  - *Nội dung:* thêm trường `actor_id`, `actor_org` vào STATUS_EVENT và INSPECTION_RECORD; thêm `created_by` cho EVIDENCE. Bổ sung vào C6 điều kiện: tác nhân của Hoàn thành → Đã xác minh khác tác nhân của Đang xử lý → Hoàn thành.
  - *Vì sao vượt khóa:* `CLAUDE.md` §11 không cho thêm thực thể, ràng buộc. Trường thêm vào ràng buộc có sẵn (C6) có thể coi là đổi đặc tả.
  - *Lý do đề xuất:* câu hỏi 3 ("Ai") là câu hỏi lõi. [44] tr. 21–25 có tác giả, tổ chức và tách nhiệm vụ. `mapping/garcia2026.md` Phần D mục 1 đã đề xuất, và `CLAUDE.md` §6.1 để "chờ NCS quyết định".
  - *Chi phí:* S–M (thêm cột, thêm một truy vấn).
  - *Rủi ro:* lưu tên người là dữ liệu cá nhân. Lưu mã nội bộ, khóa ánh xạ mã ↔ người ở chủ đầu tư [CẦN NGUỒN: quy định bảo vệ dữ liệu cá nhân hiện hành ở Việt Nam].
- **Đ-2. Mở rộng F-2 ra ngoài "phía chủ đầu tư".**
  - *Nội dung:* thêm 2–3 người: ≥ 1 kỹ sư của đơn vị kiểm định độc lập (không phải đơn vị lập phần lớn hồ sơ B0), ≥ 1 nhà thầu sửa chữa kết cấu thép. Nếu được, thêm 1–2 người quản lý bảo trì ở một chủ đầu tư thứ hai. Tổng 7–10 người.
  - *Vì sao vượt khóa:* QĐ 12 ghi "3–5 người quản lý kiểm tra – bảo trì phía chủ đầu tư".
  - *Lý do:* vai trò thiếu của A.2 (mục 4(a)) chỉ được xác nhận khi hỏi đúng người giữ vai trò đó. Một chủ đầu tư duy nhất tạo thiên lệch chọn (M4).
  - *Chi phí:* thêm khoảng 3–4 giờ phỏng vấn và mã hóa. Có thể gộp với việc lấy hồ sơ B0 từ các đơn vị kiểm định. Cần thầy duyệt.
- **Đ-3. Báo cáo hai con số M2(B0), theo thiết kế và theo rà soát của người.**
  - *Ghi chú:* đề xuất này nằm trong phạm vi "cách tính M1–M4" (GD3b L186). Nhưng nếu NCS coi việc thêm người rà soát B0 là hoạt động thu dữ liệu mới, cần duyệt như F-2 (có người tham gia, đồng thuận).
  - *Chi phí:* 2 kỹ sư × khoảng 2–3 giờ.

---

## 7. Câu tiếng Anh đề xuất cho bản thảo

1. *(Methods – B0)* "Baseline B0 represents the recording practice observed in N inspection records issued by K organisations for steel industrial buildings in Vietnam between [years]; records were coded at the level of a single finding with its recommended action, using a codebook frozen before coding, and two coders achieved [κ/α] on field presence."
2. *(Methods – B0 detection)* "Because B0 contains no machine-checkable fields for sensor mapping validity, evidence scope or evidence revision, error groups C3, C5 and C9 are reported as not applicable to B0 rather than as zero detection; for the remaining groups, detection in B0 was performed by two experienced reviewers blinded to the injected-error list."
3. *(Methods – requirements)* "The three traceback questions were elicited from, and then confirmed by, [n] practitioners holding the inspection, approval and execution roles at the partner owner; the questions and the M3 procedure were committed to the repository before any baseline was instantiated."
4. *(Discussion – verification)* "The scope of sensor-based evidence is reset at the time of the physical intervention recorded by the completion event, not at verification, so that evidence acquired between repair and verification is flagged as out of scope until a post-repair inspection record confirms the new installation batch."
5. *(Discussion – cost)* "Accountability is not free: the proposed model added [x] person-minutes per detection-to-closure cycle relative to B1, of which [y] were spent on manual justification and post-repair records, in exchange for detecting [z] additional injected errors in the out-of-scope and unsupported-transition groups."
