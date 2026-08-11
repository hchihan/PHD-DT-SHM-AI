# Bổ sung nguồn cho claim "BIM-linked inspection records improve maintenance accountability"

**Bối cảnh:** Related Work, Paper 2 (component-level traceability từ condition evidence → inspection & maintenance action), luận án DT cho coastal industrial steel buildings.
**Ngày:** 2026-08-10

---

## 0. Trả lời thẳng trước khi vào danh sách

Tôi **không** đưa cho bạn một danh sách "vài paper Q1 phù hợp" được chọn theo nghĩa "nghe có vẻ khớp". Có hai lý do, và cả hai đều là lý do phương pháp luận chứ không phải sự dè dặt:

1. **Rủi ro citation fabrication.** Kiểu yêu cầu "thêm vài paper Q1 để củng cố claim X" là kiểu prompt dễ tạo ra reference không tồn tại hoặc tồn tại nhưng sai tạp chí / sai năm / sai tác giả. Mọi mục dưới đây tôi đều đã tra cứu lại và ghi rõ mức độ xác minh. Không có mục nào tôi viết ra từ trí nhớ mà không kiểm tra.

2. **Rủi ro nghiêm trọng hơn: citation–claim mismatch.** Đây mới là vấn đề thật của claim này. Reference có thật, nhưng **không paper nào trong số chúng thực sự chứng minh điều mà claim của bạn đang phát biểu.** Chi tiết ở §1.

Nói cách khác: vấn đề của bạn không phải là thiếu citation. Vấn đề là claim đang được phát biểu ở mức mạnh hơn những gì literature hiện có chống đỡ được.

---

## 1. Chẩn đoán claim: chỗ yếu nằm ở từ "accountability"

Claim hiện tại:

> "BIM-linked inspection records improve maintenance accountability."

Câu này chứa ba cam kết ngầm, và chỉ một trong ba có evidence base vững:

| Thành phần | Cam kết ngầm | Tình trạng evidence |
|---|---|---|
| "BIM-linked inspection records" | Có thể gắn dữ liệu inspection vào cấu kiện trong mô hình | **Vững.** Đây là phần đã được chứng minh nhiều lần bằng prototype + case study. |
| "improve" | Có so sánh trước/sau, hoặc có nhóm đối chứng, hoặc có chỉ số đo được | **Yếu.** Phần lớn là proof-of-concept + case study đơn lẻ, không có baseline định lượng. |
| "maintenance accountability" | Accountability là một construct đã được định nghĩa và đo | **Rất yếu.** Trong dòng literature BIM-FM, "accountability" gần như không được operationalise. Cái được đo/được mô tả là *traceability*, *auditability*, *data integrity*, *information availability* — không phải accountability theo nghĩa tổ chức (ai chịu trách nhiệm về quyết định gì, và có bị quy trách nhiệm được không). |

Đây là một **construct-substitution gap**: literature cung cấp *điều kiện kỹ thuật tiền đề* cho accountability (bản ghi gắn đúng cấu kiện, không sửa được, truy ngược được người ghi), rồi tác giả — thường là chính các paper đó — **suy diễn** ra accountability mà không đo. Nếu bạn viết claim ở dạng hiện tại và trích các paper dưới đây, reviewer nghiêm khắc của một tạp chí Q1 CM/AEC hoàn toàn có thể hỏi: *"Which of these studies measured accountability?"* — và câu trả lời trung thực là: không paper nào.

**Đây thực ra là tin tốt cho Paper 2 của bạn.** Khoảng trống này chính là chỗ đóng góp: bạn đang làm *component-level traceability từ condition evidence tới action*, tức là đúng cái mắt xích mà literature bỏ dở. Đừng khoả lấp nó bằng citation — hãy khai thác nó.

---

## 2. Đề xuất viết lại claim

Thay vì một câu tổng quát khó chống đỡ, tách thành chuỗi ba mệnh đề, mỗi mệnh đề có nguồn khớp:

> Linking inspection findings to individual model components has been repeatedly demonstrated as technically feasible in facility and infrastructure maintenance settings [R1, R2, R3, R6], and is consistently reported as improving the availability and structuring of condition information for maintenance decision-making [R4, R5]. More recently, distributed-ledger approaches have extended this to tamper-evident inspection records with explicit provenance of who recorded what, and when [R7, R8]. **However, the accountability benefit attributed to such records remains largely asserted rather than measured: existing studies report traceability and auditability as system properties, but do not evaluate whether responsibility attribution in maintenance practice actually improves.** This gap motivates the component-level evidence-to-action traceability model developed in this paper.

Ba lợi ích của cách viết này: (a) mọi mệnh đề đều có nguồn thật sự chống đỡ; (b) bạn tự nêu limitation của literature trước khi reviewer nêu; (c) đoạn văn kết thúc bằng research gap dẫn thẳng vào contribution của Paper 2 — Related Work làm đúng việc của nó.

---

## 3. Danh sách tham khảo (APA 7th)

Ký hiệu độ tin cậy:
- **[V]** — đã xác minh tác giả, năm, tạp chí, tập/trang, DOI qua nguồn thứ cấp độc lập (ScienceDirect / ASCE Library / Google Scholar record).
- **[V-part]** — thư mục xác minh được, nhưng một trường (thường là số tập/trang hoặc thứ tự tác giả) chỉ có một nguồn xác nhận → bạn nên đối chiếu lại trên trang publisher trước khi nộp.

Trong tất cả các trường hợp: **tôi chưa đọc toàn văn các paper này trong phiên làm việc này.** Phần "chứng minh điều gì" dưới đây dựa trên abstract/record công khai. Trước khi trích vào Paper 2, bạn cần đọc bản gốc — đặc biệt là phần Method và Limitations — để chắc rằng nội dung khớp với cách bạn dùng.

### Nhóm A — Traceability cấu kiện: inspection/maintenance data gắn vào model

**[R1] [V]**
Motamedi, A., Hammad, A., & Asen, Y. (2014). Knowledge-assisted BIM-based visual analytics for failure root cause detection in facilities management. *Automation in Construction, 43*, 73–83. https://doi.org/10.1016/j.autcon.2014.03.012

*Chứng minh điều gì:* tích hợp dữ liệu inspection/maintenance từ CMMS vào BIM, biểu diễn hình thức quan hệ giữa cấu kiện (fault tree) để hỗ trợ truy nguyên nguyên nhân hỏng hóc. *Dùng cho mệnh đề nào:* liên kết bản ghi hiện trường ↔ cấu kiện là khả thi và có giá trị chẩn đoán. *Không dùng cho:* accountability, hay bất kỳ hiệu quả tổ chức nào.

**[R2] [V]**
McGuire, B., Atadero, R., Clevenger, C., & Ozbek, M. (2016). Bridge information modeling for inspection and evaluation. *Journal of Bridge Engineering, 21*(4), 04015076. https://doi.org/10.1061/(ASCE)BE.1943-5592.0000850

*Chứng minh điều gì:* add-in cho phép inspector ghi loại / mức độ / vị trí hư hỏng trực tiếp lên mô hình, rồi chuyển sang đánh giá kết cấu và load rating. *Dùng cho mệnh đề nào:* đây là tiền lệ gần nhất với chuỗi *condition evidence → structural assessment → action* của bạn, ở domain hạ tầng thép. Rất đáng đọc kỹ cho Paper 2. *Không dùng cho:* accountability; đây là prototype, không có đánh giá vận hành.

**[R3] [V]**
Chen, W., Chen, K., Cheng, J. C. P., Wang, Q., & Gan, V. J. L. (2018). BIM-based framework for automatic scheduling of facility maintenance work orders. *Automation in Construction, 91*, 15–30. https://doi.org/10.1016/j.autcon.2018.03.007

*Chứng minh điều gì:* mapping IFC giữa BIM và hệ FM, rồi tự động sinh và xếp lịch work order. *Dùng cho mệnh đề nào:* mắt xích *evidence → action*, tức là bản ghi tình trạng được chuyển thành hành động bảo trì cụ thể gắn với cấu kiện. Đây là citation khớp nhất với trục "action" trong Paper 2.

### Nhóm B — Bối cảnh: BIM trong FM, yêu cầu dữ liệu, hiện trạng

**[R4] [V]**
Becerik-Gerber, B., Jazizadeh, F., Li, N., & Calis, G. (2012). Application areas and data requirements for BIM-enabled facilities management. *Journal of Construction Engineering and Management, 138*(3), 431–442. https://doi.org/10.1061/(ASCE)CO.1943-7862.0000433

*Chứng minh điều gì:* khảo sát + phỏng vấn về hiện trạng và yêu cầu dữ liệu của BIM trong FM. *Dùng cho mệnh đề nào:* đây là một trong số ít nguồn **có dữ liệu thực nghiệm từ người hành nghề**, hữu ích để nói về nhu cầu thông tin, chứ không phải để nói về hiệu quả. Lưu ý: 2012 — khá cũ so với khung DT của bạn; nên dùng làm mốc lịch sử.

**[R5] [V]**
Pärn, E. A., Edwards, D. J., & Sing, M. C. P. (2017). The building information modelling trajectory in facilities management: A review. *Automation in Construction, 75*, 45–55. https://doi.org/10.1016/j.autcon.2016.12.003

*Chứng minh điều gì:* review về BIM cho asset management giai đoạn O&M, gồm cả tiêu chuẩn. *Dùng cho mệnh đề nào:* câu framing mở đầu Related Work, và để chống lưng cho nhận định rằng đánh giá hiệu quả vận hành còn thiếu.

**[R6] [V]**
Cheng, J. C. P., Chen, W., Chen, K., & Wang, Q. (2020). Data-driven predictive maintenance planning framework for MEP components based on BIM and IoT using machine learning algorithms. *Automation in Construction, 112*, 103087. https://doi.org/10.1016/j.autcon.2020.103087

*Chứng minh điều gì:* khung condition monitoring → fault alarming → condition evaluation → maintenance planning, gắn với cấu kiện MEP. *Dùng cho mệnh đề nào:* kiến trúc data-informed DT của bạn có tiền lệ; đồng thời là điểm phân biệt — họ làm MEP, bạn làm kết cấu thép ven biển với cơ chế xuống cấp khác hẳn (ăn mòn).

### Nhóm C — Bản ghi không sửa được và provenance (gần "accountability" nhất trong literature hiện có)

**[R7] [V]**
Sheng, D., Ding, L., Zhong, B., Love, P. E. D., Luo, H., & Chen, J. (2020). Construction quality information management with blockchains. *Automation in Construction, 120*, 103373. https://doi.org/10.1016/j.autcon.2020.103373

*Chứng minh điều gì:* khung quản lý thông tin chất lượng phi tập trung trên Hyperledger Fabric, kiểm chứng qua dự án ga metro. *Dùng cho mệnh đề nào:* provenance và tính bất biến của bản ghi — tiền đề kỹ thuật của accountability. *Cảnh báo:* đây là **construction quality**, không phải **maintenance**; đừng để câu văn ngầm ám chỉ nó nói về O&M.

**[R8] [V-part]**
Wu, H., Zhong, B., Li, H., Guo, J., & Wang, Y. (2021). On-site construction quality inspection using blockchain and smart contracts. *Journal of Management in Engineering, 37*(6), 04021065. https://doi.org/10.1061/(ASCE)ME.1943-5479.0000967

*Cần đối chiếu:* thứ tự/danh sách tác giả và số article tôi chỉ xác nhận được qua một nguồn thứ cấp. Kiểm tra lại trên ASCE Library. *Dùng cho mệnh đề nào:* smart contract ràng buộc quy trình inspection tại hiện trường — đây là chỗ literature tiến gần nhất tới "ai chịu trách nhiệm cho bản ghi nào". Vẫn là construction phase, không phải maintenance.

### Nhóm D — Bối cảnh Digital Twin (tuỳ chọn, nếu Related Work có mục DT riêng)

**[R9] [V-part]**
Franciosi, M., Kasser, M., & Viviani, M. (2024). Digital twins in bridge engineering for streamlined maintenance and enhanced sustainability. *Automation in Construction, 168*, 105834. https://doi.org/10.1016/j.autcon.2024.105834

*Cần đối chiếu:* tên tác giả và số article chỉ xác nhận được qua nguồn thứ cấp — kiểm tra lại trên ScienceDirect trước khi dùng. *Dùng cho mệnh đề nào:* DT cho ra quyết định bảo trì hạ tầng. Chỉ đưa vào nếu Related Work của bạn cần một mốc DT gần đây; nó **không** chống đỡ claim accountability.

---

## 4. Việc bạn cần làm trước khi dán vào bản thảo

1. **Đọc toàn văn R2 và R3 trước tiên.** Đây là hai nguồn gần nhất với trục lập luận của Paper 2. Nếu chỉ đọc được hai bài, đọc hai bài này.
2. **Tự xác minh quartile.** Tôi không có quyền truy cập JCR/Scopus trong phiên này, nên **tôi không xác nhận "Q1" cho bất kỳ mục nào ở trên.** *Automation in Construction* thường được xếp Q1 trong Civil/Structural Engineering, và các tạp chí ASCE ở trên nhìn chung nằm ở Q1–Q2 — nhưng quartile phụ thuộc **năm và category cụ thể**, và hội đồng của bạn có thể dùng bảng khác (JCR vs Scopus CiteScore vs danh mục ngành). Hãy tra theo đúng năm xuất bản của từng bài.
3. **Kiểm tra hai mục [V-part]** (R8, R9) trực tiếp trên trang publisher.
4. **Đối chiếu với thư mục evidence hiện có của bạn** (`02_EVIDENCE_BASE/RQ2_GATES2_3`) để tránh trùng và để giữ nhất quán citation key.

---

## 5. Khoảng trống tôi không tìm được nguồn — và đó là điều đáng chú ý

Tôi đã chủ động tìm ba nhóm sau và **không tìm được nguồn Q1 đủ vững**:

- **Nghiên cứu thực nghiệm đo accountability trong bảo trì** (trước/sau, hoặc có đối chứng, với accountability được operationalise). Không tìm thấy. Đây là gap thật, không phải do tìm chưa kỹ — nhưng bạn nên tự chạy một lần systematic search để khẳng định trước khi tuyên bố gap trong bản thảo.
- **Traceability cấu kiện cho kết cấu thép công nghiệp ven biển cụ thể** (ăn mòn do khí quyển biển). Chỉ có tài liệu liền kề (cầu, hangers chịu ăn mòn–mỏi), không có nguồn khớp trực tiếp.
- **Nghiên cứu nối inspection record với trách nhiệm trong hợp đồng/quy định bảo trì.** Dòng blockchain chạm vào provenance nhưng dừng ở giai đoạn thi công.

Nếu ba khoảng trống này đứng vững sau khi bạn tìm kỹ, chúng là **ba câu mạnh nhất** cho phần cuối Related Work và cho phần positioning của contribution.

---

## Nguồn tra cứu đã dùng

- [Motamedi, Hammad & Asen (2014), Automation in Construction](https://www.sciencedirect.com/science/article/abs/pii/S0926580514000648)
- [McGuire, Atadero, Clevenger & Ozbek (2016), Journal of Bridge Engineering](https://ascelibrary.org/doi/abs/10.1061/(ASCE)BE.1943-5592.0000850)
- [Chen et al. (2018), Automation in Construction](https://www.sciencedirect.com/science/article/abs/pii/S0926580517307173)
- [Becerik-Gerber et al. (2012), Journal of Construction Engineering and Management](https://ascelibrary.org/doi/10.1061/(ASCE)CO.1943-7862.0000433)
- [Pärn, Edwards & Sing (2017), Automation in Construction](https://www.sciencedirect.com/science/article/abs/pii/S092658051630485X)
- [Cheng et al. (2020), Automation in Construction](https://www.sciencedirect.com/science/article/abs/pii/S0926580518308562)
- [Sheng et al. (2020), Automation in Construction](https://www.sciencedirect.com/science/article/abs/pii/S0926580520309535)
- [Wu et al. (2021), Journal of Management in Engineering](https://ascelibrary.org/doi/abs/10.1061/(ASCE)ME.1943-5479.0000967)
- [Franciosi, Kasser & Viviani (2024), Automation in Construction](https://www.sciencedirect.com/science/article/pii/S0926580524005703)
