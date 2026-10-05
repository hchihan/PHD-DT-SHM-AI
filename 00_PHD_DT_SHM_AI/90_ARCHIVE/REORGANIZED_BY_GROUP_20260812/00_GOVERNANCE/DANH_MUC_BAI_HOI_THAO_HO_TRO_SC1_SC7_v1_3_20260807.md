# DANH MỤC BÀI HỘI THẢO HỖ TRỢ SC-1 ĐẾN SC-7

**Phiên bản:** v1.3
**Ngày cập nhật:** 07/08/2026
**Trạng thái:** TÀI LIỆU KIỂM SOÁT NỘI BỘ — SẴN SÀNG TRÌNH THẦY, CHƯA PHẢI PHÊ DUYỆT NỘP BÀI
**Source-of-truth level:** 8 (planning; dưới Charter, ACCEPTED ADRs, Evidence Gates, Paper 1 / Paper 2 directions)
**Supersedes:** `DANH_MUC_BAI_HOI_THAO_HO_TRO_SC1_SC5_v1_2_20260807.md`
**Superseded by:** Không.
**Change summary:** Sửa chuỗi định danh đã bị bãi bỏ; cập nhật Source of Truth lên tầng 20260719 và 20260804; ghi nhận mâu thuẫn số run giữa SC-1 và SC-5; bổ sung NO-GO về tính độc lập campaign cho SC-5; đảo lại thứ tự ưu tiên theo đòn bẩy; bổ sung SC-6 và SC-7 là hai bài không phụ thuộc Evidence Gate; bổ sung SC-8 tùy chọn có cảnh báo; bổ sung ánh xạ hội thảo, cơ chế thu hoạch phản biện và quy tắc đồng tác giả.

---

## 0. Nhật ký thay đổi v1.2 → v1.3

| # | Mục | Thay đổi | Lý do |
|---|---|---|---|
| **C-01** | §1 chuỗi định danh | `Action_Status` → `Action_Record_ID`; thêm `Asset_ID @ Model_Version_ID`; thêm `Status_Event_ID [PROPOSED]` | `01_MASTER_G1_G2_G3_EVIDENCE_SYNTHESIS_20260804` §K ghi `Action_Status`-as-chain là OLD POSITION; `CURRENT_STATUS` §6: *"must not be propagated"* |
| **C-02** | §1 chuỗi nghiên cứu | Bổ sung `Action_Record → Status_Event` | Đồng bộ với chuỗi hiện hành trong Synthesis §C |
| **C-03** | §18 Source of truth | Bỏ tham chiếu 20260717; thêm Charter v2.1 20260719 và toàn bộ tầng 20260804 | Danh sách cũ trễ ba tuần; chính lỗ hổng này sinh ra C-01 |
| **C-04** | SC-1 §3.4 và SC-5 §7.4 | Ghi nhận mâu thuẫn 3 run vs 6 run là **OPEN ITEM**, chặn cả hai bài | 36 cặp = 3 run/tổ hợp; 54 recording = 6 run/tổ hợp — không thể cùng đúng nếu chưa có văn bản giải thích |
| **C-05** | SC-5 §7.7 | Thêm NO-GO: campaign phải là các lần lắp đặt/tháo lắp độc lập | Nếu hai campaign thu trong cùng phiên đo, phân tích between-campaign mất hiệu lực |
| **C-06** | SC-3 §5.8 | Nâng "có toàn văn ISO 19650" thành điều kiện GO cứng | Living Evidence Base: ISO preview `EWBTQFTP`/`V3IYM6UC` **không phải toàn văn**; VN-LEGAL vẫn `Unverified` |
| **C-07** | §13 thứ tự ưu tiên | Đảo lại theo đòn bẩy thay vì theo độ sạch firewall; SC-2 hạ từ ưu tiên 1 xuống nhóm sau | SC-2 tự khai không tạo evidence cho Paper 1, không RQ/WP/Gate, nhưng chi phí thực hiện cao nhất |
| **C-08** | Mục mới §9, §10 | Bổ sung **SC-6** và **SC-7** | v1.2 không có bài nào khởi động được ngay → rủi ro không nộp được bài nào trong 2026 |
| **C-09** | Mục mới §11 | Bổ sung **SC-8** tùy chọn kèm cảnh báo trùng Mục 3 của Paper 1 | Phương án dự phòng nếu deadline gấp |
| **C-10** | Mục mới §13.2 | Ánh xạ bài ↔ hội thảo ↔ deadline | v1.2 không có ánh xạ venue |
| **C-11** | Mục mới §15 | Cơ chế thu hoạch phản biện chuyên gia | Mục đích tuyên bố là lấy góp ý, nhưng không có nơi lưu góp ý |
| **C-12** | §16 | Đồng tác giả phải thống nhất **trước khi bắt đầu viết**, không phải trước khi nộp | Giảm rủi ro viết xong mới bị bác |

---

## 1. Vị trí trong kiến trúc luận án

### 1.1 Chuỗi nghiên cứu lõi đã khóa *(đã sửa — C-02)*

```text
Dữ liệu dao động
→ bằng chứng trạng thái / biến đổi trạng thái
→ cấu kiện liên kết BIM
→ Inspection_Record
→ Action_Record
→ Status_Event
→ hỗ trợ hành động kiểm tra – bảo trì
```

### 1.2 Chuỗi định danh lõi *(đã sửa — C-01)*

```text
Sensor_ID
→ BIM_GUID / Asset_ID @ Model_Version_ID
→ Condition_Evidence_ID
→ Inspection_Record_ID
→ Action_Record_ID
→ Status_Event_ID   [PROPOSED — NOT ACCEPTED]
```

**Quy tắc bắt buộc:** `Action_Status` / `Workflow_Status` là **current-state projection** của `Action_Record`, **không phải identifier** và **không phải history**. Ký hiệu cũ `… → Inspection_Record_ID → Action_Status` chỉ tồn tại trong archive; **không được lan truyền sang bất kỳ tài liệu, slide hay bản thảo nào**.

`Status_Event_ID` đang ở trạng thái đề xuất trong `ADR_ACTION_STATUS_EVENT_20260804_DRAFT` — mọi lần nhắc tới đều phải kèm nhãn `PROPOSED — NOT ACCEPTED`.

### 1.3 Ràng buộc chung của Supporting Scope

Các bài SC-1 → SC-8 đều thuộc **Supporting Scope**. Không bài nào:

- mở RQ, WP, chương, Paper lõi hoặc Evidence Gate riêng;
- được dùng để tuyên bố đã đóng G1, G2, G3, G4 hoặc G5;
- được ưu tiên cao hơn việc khóa Gate 1;
- được thay đổi kiến trúc Limited-FEM đã được chấp thuận;
- được dùng từ *validated*, *passed*, *proven*, *field-ready* cho bất kỳ Gate nào.

**Evidence Gate hiện tại:** Gate 1 — `OPEN — PARTIAL EVIDENCE`.
**Nút chặn bắt buộc:** khóa canonical run registry → sensor identity/provenance → audit split-before-windowing → đánh giá run-aware/LORO đa seed chống rò rỉ → xác nhận hoặc loại ResNet1D theo provenance → gói bất định run/fold → acceptance matrix và chữ ký thầy.

**Cấm tuyệt đối trong mọi bài SC:** không con số ResNet1D nào cho tới khi sensor mode được chốt (`PAPER1_DIRECTION_AND_GATE` §Immediate blocker).

---

## 2. Danh mục tổng hợp

| Mã | Tên bài đề xuất | Mục tiêu chính | Dữ liệu | Quan hệ luận án | Khởi động được ngay? | Trạng thái |
|---|---|---|---|---|:---:|---|
| **SC-1** | Đánh giá sự tương hợp và chất lượng dữ liệu của phép đo PASCO–ADXL đồng bộ trên mô hình khung thép tỷ lệ | Định lượng tương hợp hai hệ đo trong miền thời gian và tần số | Các cặp PASCO–ADXL đồng bộ (số lượng chờ registry) | Tiếp giáp RQ1/WP1/C4/Paper 1/G1 | ❌ | **GO có điều kiện** |
| **SC-2** | Tối ưu siêu tham số 1D-CNN có kiểm soát ngân sách tính toán cho phân loại dao động kết cấu | So sánh hiệu năng–chi phí các chiến lược HPO dưới cùng ngân sách | Benchmark công khai; **tuyệt đối không Campaign 1–3** | Nghiên cứu phương pháp AI độc lập; không ánh xạ RQ/WP/Gate | ❌ | **GO có điều kiện; firewall sạch nhất, đòn bẩy thấp nhất** |
| **SC-3** | Ánh xạ yêu cầu quản lý thông tin BIM phục vụ vận hành và bảo trì từ TCVN 14177 và ISO 19650 sang IFC | Chuyển yêu cầu thông tin tài sản tĩnh thành trường IFC và quy tắc kiểm tra | Văn bản tiêu chuẩn chính thức + Revit/IFC + tập cấu kiện pilot | Tiếp giáp RQ2/WP2/C5/Paper 2/G2 | ❌ | **GO có điều kiện; chặn bởi quyền truy cập tiêu chuẩn** |
| **SC-4** | Từ đầu ra AI/SHM đến hồ sơ kiểm tra liên kết BIM: nghiên cứu ánh xạ hệ thống về chuyển giao thông tin | Bản đồ bằng chứng và taxonomy về information handover | Corpus văn liệu tái lập được | Cầu nối WP1–WP2; hỗ trợ C2/C5 | ❌ | **DỰ PHÒNG — GO chỉ sau pilot search** |
| **SC-5** | Đánh giá độ lặp lại theo run và độ ổn định giữa các campaign của dữ liệu dao động trạng thái khỏe | Định lượng biến thiên tự nhiên của phép đo S0 | PASCO, S0–Healthy, Campaign 1–3 | Tiếp giáp RQ1/WP1/C4/Paper 1/G1 | ❌ | **GO có điều kiện; rủi ro xâm phạm Paper 1 cao nhất** |
| **🆕 SC-6** | Thực trạng lập và lưu trữ hồ sơ kiểm tra – bảo trì công trình thép công nghiệp tại Việt Nam: khảo sát thực hành quản lý | Mô tả thực hành ghi chép, phê duyệt, xác nhận và đóng hồ sơ đang tồn tại | Phỏng vấn / bảng hỏi người hành nghề; **không dữ liệu đề tài** | Cung cấp bằng chứng thực hành cho các mục `EXPERT_REVIEW_REQUIRED` của G2 | ✅ **Có** | **GO — ưu tiên cao nhất trong nhóm SC** |
| **🆕 SC-7** | Lựa chọn hệ đo dao động chi phí thấp cho công trình thép công nghiệp ven biển: ràng buộc triển khai và tiêu chí đánh giá | Xây dựng khung tiêu chí lựa chọn và qualification hệ đo | Nghiên cứu bàn giấy; thông số kỹ thuật và văn liệu | Hỗ trợ chuẩn bị G4 (Stream C); không phải evidence G4 | ✅ **Có** | **GO** |
| *SC-8* | *Thiết kế và chế tạo mô hình khung thép bulông tỷ lệ 1:10: thiết lập thí nghiệm và quy trình thu số liệu* | *Mô tả thuần thiết lập, không kết quả* | *Metadata thiết lập* | *Trùng Mục 3 của Paper 1* | ✅ | ⚠️ **TÙY CHỌN — chỉ khi không còn lựa chọn khác** |

**Lưu ý chiến lược:** Đây là kho ý tưởng có kiểm soát, không phải cam kết nộp đủ tám bài. Mục tiêu thực tế cho 2026 là **hai đến ba bài**.

**Phát hiện của v1.3:** trong bản v1.2, **không bài nào (SC-1→SC-5) khởi động được ngay** — tất cả đều chờ Paper 1 khóa, chờ dataset độc lập, chờ tiêu chuẩn, hoặc chờ pilot search. Với hội thảo tháng 10 và tháng 12/2026, danh mục v1.2 có nguy cơ cao **không sinh ra bài nộp nào trong 2026**, khiến mục tiêu *tập viết và lấy phản biện chuyên gia* thất bại dù mọi firewall đều đúng. SC-6 và SC-7 được bổ sung chính xác để lấp khoảng trống này.

---

## 3. SC-1 — Tương hợp phép đo PASCO–ADXL

### 3.1 Tên đề xuất

**Tiếng Việt:** Đánh giá sự tương hợp và chất lượng dữ liệu của phép đo PASCO–ADXL đồng bộ trên mô hình khung thép tỷ lệ.
**Tiếng Anh:** *Cross-Sensor Agreement and Data-Quality Assessment of Synchronized PASCO and ADXL Measurements on a Scaled Steel Frame.*

### 3.2 Mục tiêu

Định lượng mức tương hợp giữa hai hệ đo trong dải tần chung hợp lệ; nhận diện sai khác có hệ thống do tần số lấy mẫu, độ trễ, giá trị thiếu, kênh phẳng, bão hòa và chất lượng phổ.

### 3.3 Định vị

| Hạng mục | Quyết định |
|---|---|
| RQ liên quan | Tiếp giáp RQ1; không trả lời khả năng phân loại trạng thái |
| WP / Chương / Paper | WP1 / C4 / Paper 1 — Supporting Scope |
| Gate | Tiếp giáp G1; **không** phải điều kiện đóng G1 |
| Đơn vị phân tích | Một cặp PASCO–ADXL đo đồng bộ, cùng vị trí/trục và đoạn thời gian hợp lệ |

### 3.4 Claim → Evidence → Limitation → Next action

**Claim.** Trong cùng khoảng thời gian và dải tần hợp lệ, PASCO và ADXL có mức tương hợp đo được; khác biệt giữa hai hệ có thể được định lượng bằng chỉ số chất lượng tín hiệu và phổ.

**Evidence.** Hồ sơ hiện có nêu 36 cặp đo đồng bộ (4 trạng thái × 3 kích thích × 3 run). Con số và tính đồng bộ chỉ được công bố sau khi `PASCO_ADXL_PAIR_REGISTRY` xác nhận file, timestamp, vị trí, trục, sampling rate và valid interval. Các cặp Healthy thu khác ngày/vị trí không được gộp vào phân tích chính.

> ### 🔴 OPEN ITEM OI-01 *(mới — C-04)*
> SC-1 giả định **3 run/tổ hợp**; SC-5 giả định **6 run/tổ hợp**. Hai con số không thể cùng đúng nếu cùng một thiết kế thí nghiệm. Có thể giải thích được — ví dụ PASCO ghi 6 run nhưng chỉ 3 run có ADXL đồng bộ — nhưng **hiện chưa có văn bản nào ghi nhận điều đó**.
>
> **OI-01 chặn cả SC-1 và SC-5.** Không viết dòng nào của hai bài này trước khi canonical run registry giải quyết xong. **Không được công bố con số 36 hay 54 trước khi registry xác nhận.**

**Limitation.** Kết quả chỉ áp dụng cho thiết bị, cách gá, khung, kích thích và dải tần đã thử; không chứng minh hai hệ thay thế nhau phổ quát, không chứng minh hiệu quả hiện trường hoặc khả năng chẩn đoán.

**Next action.** Giải quyết OI-01 → khóa `PASCO_ADXL_PAIR_REGISTRY` → phân tích cuối.

### 3.5 Dữ liệu và phương pháp tối thiểu

- Cắt đoạn hợp lệ chung; NaN cuối file PASCO được xem là giới hạn xuất dữ liệu, không tự động coi là lỗi đo.
- Ước lượng độ trễ và báo cáo rõ cách căn chỉnh.
- Lọc chống aliasing trước khi đưa về dải tần chung.
- Chỉ số chính: valid duration, missing/flat/clipping; cross-correlation lag; normalized waveform agreement; dominant-frequency difference; PSD similarity; coherence trong điều kiện phù hợp.
- Báo cáo theo cặp/run kèm độ biến thiên; nhãn S0/B1/B2/B3 chỉ dùng phân tầng mô tả, **không** dùng làm biến đích.

### 3.6 Firewall

Không phân loại S0/B1/B2/B3; không LORO/LOCO/random split; không RF/SVM/1D-CNN/ResNet1D; không xếp hạng vị trí hay cấu hình cảm biến; không CEI; không Autoencoder hiện trường.

### 3.7 Go / No-Go

**GO:** OI-01 đã giải quyết; cặp đo, vị trí, trục, sampling rate và valid interval được xác nhận; Paper 1 đã khóa bảng–hình và phạm vi kết quả.
**NO-GO:** không khôi phục được tính đồng bộ/đồng vị trí; hoặc đóng góp chính chỉ xuất hiện khi đưa bài toán phân loại vào.

### 3.8 Sản phẩm phụ cho luận án

✅ `PASCO_ADXL_PAIR_REGISTRY` và hồ sơ sensor provenance — trùng khớp với **G1 Stream A bước 1–2**. Đây là bài có đòn bẩy cao nhất trong nhóm dùng dữ liệu đề tài.

---

## 4. SC-2 — HPO theo ngân sách tính toán trên dữ liệu độc lập

### 4.1 Tên đề xuất

**Tiếng Việt:** Tối ưu siêu tham số 1D-CNN có kiểm soát ngân sách tính toán cho phân loại dao động kết cấu: nghiên cứu so sánh công bằng.
**Tiếng Anh:** *Compute-Budget-Aware Hyperparameter Optimization for 1D-CNN-Based Structural Vibration Classification: A Fair Comparative Study.*

### 4.2 Mục tiêu

So sánh các chiến lược HPO — dự kiến Random Search, GWO và SAFCA — dưới cùng số lần đánh giá hàm mục tiêu; đánh giá đồng thời macro-F1, độ ổn định, tốc độ hội tụ và chi phí tính toán.

### 4.3 Định vị và đánh giá đòn bẩy *(cập nhật — C-07)*

| Hạng mục | Quyết định |
|---|---|
| RQ / WP / Chương / Gate | **Không có**; nghiên cứu phương pháp AI độc lập |
| Paper lõi | **Không** tạo evidence cho Paper 1 |
| Đơn vị phân tích | Một lần HPO hoàn chỉnh trong một outer fold và một seed |
| Dữ liệu | Benchmark công khai hoặc dữ liệu hướng phụ, có quyền sử dụng và cấu trúc nhóm rõ |

> **Ghi nhận đánh đổi (mới).** SC-2 có firewall sạch nhất nhưng **đòn bẩy thấp nhất** trong danh mục: nó không sinh ra artifact nào cho G1 hoặc G2, đồng thời có chi phí thực hiện cao nhất (tìm dataset, xác lập cấu trúc nhóm, chạy nested HPO × 3 chiến lược × nhiều seed × outer fold).
>
> Ngoài ra, một bài so sánh thuật toán tối ưu trên dữ liệu benchmark không liên quan có thể bị hội đồng đặt câu hỏi về căn cước Quản lý Xây dựng. Đây là đánh đổi có thật, được ghi nhận công khai thay vì bỏ qua.
>
> **Quyết định v1.3:** giữ SC-2 trong danh mục nhưng hạ khỏi vị trí ưu tiên 1. Chỉ kích hoạt khi Gate 1 đã đóng và còn dư địa nguồn lực.

### 4.4 Claim → Evidence → Limitation → Next action

**Claim.** Dưới cùng ngân sách tìm kiếm, các chiến lược HPO khác nhau về hiệu năng ngoài mẫu, độ ổn định, đường hội tụ và chi phí.

**Evidence.** Nested group-aware evaluation, nhiều seed, cùng preprocessing, mô hình, early stopping, search space và số lần đánh giá hàm mục tiêu.

**Limitation.** Kết luận phụ thuộc dataset, search space, budget, protocol và phần cứng; không chứng minh một HPO vượt trội phổ quát và không chuyển kết quả sang dữ liệu luận án.

**Next action.** Chọn dataset độc lập và lập phiếu provenance / quyền sử dụng / đơn vị nhóm trước khi chạy.

### 4.5 Dữ liệu và phương pháp tối thiểu

- Khóa dataset, nhãn, đơn vị nhóm, search space và compute budget trước khi chạy.
- Nested group-aware evaluation khi có run/specimen/subject tự nhiên.
- **HPO phải nằm lồng bên trong vòng đánh giá.** Tuning trên toàn bộ dữ liệu rồi báo cáo kết quả grouped-CV là selection leakage và làm bài mất hiệu lực.
- Metric chính: macro-F1 outer test. Metric phụ: độ biến thiên, convergence, failed trials, wall-clock / accelerator time.
- Lặp nhiều seed; lưu trial log và cấu hình cuối. **Không báo cáo seed tốt nhất.**
- Phân biệt rõ LORO và LOCO nếu dataset có cả run và campaign.

### 4.6 Firewall

Tuyệt đối không dùng Campaign 1–3, window dẫn xuất, run registry, cấu hình cảm biến, LORO của đề tài, CEI hoặc metric Paper 1. Không gắn claim BIM, Digital Twin hay Quản lý Xây dựng nếu dữ liệu và câu hỏi không liên quan.

### 4.7 Go / No-Go

**GO:** dataset độc lập, quyền sử dụng rõ, nhóm dữ liệu đủ cho đánh giá hợp lệ, budget chung đã khóa, **và Gate 1 đã đóng**.
**NO-GO:** phải dùng dữ liệu luận án; các HPO không cùng ngân sách; kết quả dựa vào seed tốt nhất; metadata nhóm không rõ; hoặc công việc cạnh tranh nguồn lực với G1/G2.

---

## 5. SC-3 — TCVN 14177, ISO 19650 và IFC

### 5.1 Tên đề xuất

**Tiếng Việt:** Ánh xạ yêu cầu quản lý thông tin BIM phục vụ vận hành và bảo trì công trình: từ TCVN 14177 và ISO 19650 đến thuộc tính IFC.
**Tiếng Anh:** *From BIM Information-Management Requirements to IFC Properties for Building Operation and Maintenance: A Validation-Oriented Mapping.*

**Tên ngắn cho hội thảo trong nước:**
> Khung ánh xạ yêu cầu thông tin tài sản phục vụ bảo trì công trình theo TCVN 14177 và ISO 19650.

**Tên dự phòng nếu không có toàn văn ISO** *(xem GO-gate §5.8)*:
> Khung ánh xạ yêu cầu thông tin tài sản phục vụ bảo trì công trình theo TCVN 14177:2024.

### 5.2 Mục tiêu

Chuyển một tập yêu cầu thông tin tài sản **tĩnh** đã kiểm chứng đến cấp điều khoản thành ma trận `Requirement → IFC field / external record → validation rule`, sau đó pilot vòng Revit–IFC trên tập cấu kiện cố định.

### 5.3 Định vị

| Hạng mục | Quyết định |
|---|---|
| RQ liên quan | Tiếp giáp RQ2; không trả lời evidence-to-inspection traceability |
| WP / Chương / Paper | WP2 / C5 / Paper 2 — Supporting Scope |
| Gate | Tiếp giáp G2; **không** mở hoặc đóng G2–G3 |
| Đơn vị phân tích | Một yêu cầu thông tin đã kiểm chứng và ánh xạ triển khai tương ứng |

### 5.4 Claim → Evidence → Limitation → Next action

**Claim.** Một tập yêu cầu thông tin tài sản tĩnh có thể được ánh xạ sang IFC hoặc hồ sơ ngoài IFC và kiểm tra bằng quy tắc tái lập được.

**Evidence.** Bảng bằng chứng điều khoản từ **văn bản chính thức**; ma trận Requirement–Field–Rule; thử nghiệm sự hiện diện, kiểu dữ liệu, tính duy nhất và khả năng giữ giá trị sau vòng Revit–IFC.

**Limitation.** Chỉ chứng minh ánh xạ giới hạn; không chứng minh AIM đầy đủ, tuân thủ toàn bộ tiêu chuẩn, Digital Twin vận hành hoặc truy vết inspection–action.

**Next action.** Thu thập văn bản chính thức TCVN 14177-1/-2:2024 và phần ISO 19650 được chọn; khóa clause-evidence table trước danh sách trường.

> **Evidence is currently insufficient** để gọi bất kỳ trường nào là "bắt buộc theo TCVN/ISO" nếu chưa có neo điều khoản từ văn bản chính thức.

### 5.5 Ma trận dữ liệu bắt buộc

`Requirement_ID; Source_Clause; Requirement_Text; Required_Optional_Conditional; Asset_Field; IFC_Representation; External_Record; Data_Type; Allowed_Value; Validation_Rule; Pilot_Result`

### 5.6 Phương pháp tối thiểu

- Phân tích tiêu chuẩn đến cấp điều khoản; **không** diễn giải từ tài liệu thứ cấp thay cho văn bản chính thức.
- Chọn tập con thông tin tài sản tĩnh có chủ ý.
- Khai báo trước validation rules.
- Pilot trên tập cấu kiện cố định; báo cáo Pass / Limitation / Fail.
- Cách diễn đạt ưu tiên: *"phù hợp với tập yêu cầu đã kiểm chứng được lựa chọn cho nghiên cứu"* — **không** dùng *"AIM tuân thủ đầy đủ"*.

### 5.7 Firewall

Không dùng `Sensor_ID`, `Condition_Evidence_ID`, `Inspection_Record_ID`, `Action_Record_ID`, `Status_Event_ID`; không schema truy vết động; không competency questions; không truy vấn hai chiều; không quyền hạn / xác nhận / đóng hồ sơ; không dữ liệu Rapexco.

### 5.8 Go / No-Go *(cập nhật — C-06)*

> ### 🔴 GO-GATE bắt buộc kiểm tra trước tiên
> Living Evidence Base ghi nhận: bản ISO preview (`EWBTQFTP`, `V3IYM6UC`) **không được tag là toàn văn tiêu chuẩn**; và dòng `VN-LEGAL` vẫn ở trạng thái **`Unverified — REVIEW NEEDED`**.
>
> ISO 19650 là tiêu chuẩn trả phí. **Việc đầu tiên của SC-3 không phải viết bài, mà là xác nhận có truy cập được toàn văn hay không** (thư viện NTU, mua trực tiếp, hoặc qua đơn vị hợp tác).
>
> - Có toàn văn cả TCVN và ISO → GO với tên bài đầy đủ.
> - Chỉ có TCVN 14177 → **thu hẹp phạm vi**, dùng tên dự phòng §5.1, bỏ mọi claim về ISO 19650.
> - Không có văn bản chính thức nào → **NO-GO**.

**GO:** có văn bản nguồn chính thức, neo điều khoản, tập trường tĩnh và pilot tách khỏi Paper 2.
**NO-GO:** claim phải dựa vào chuỗi truy vết động, competency questions, hoặc không kiểm chứng được tiêu chuẩn từ văn bản chính thức.

### 5.9 Sản phẩm phụ cho luận án

✅ Giải quyết mục `REVIEW_REQUIRED` về xác minh nguồn pháp lý/tiêu chuẩn — công việc mà G2 dù sao cũng phải làm.

---

## 6. SC-4 — Systematic mapping về information handover

### 6.1 Tên đề xuất

**Tiếng Việt:** Từ đầu ra AI/SHM đến hồ sơ kiểm tra liên kết BIM: nghiên cứu ánh xạ hệ thống về chuyển giao thông tin trong bảo trì công trình.
**Tiếng Anh:** *From AI/SHM Outputs to BIM-Linked Inspection Records: A Systematic Mapping of Information Handover in Structural Maintenance.*

### 6.2 Mục tiêu

Lập bản đồ có hệ thống về cách đầu ra phân tích SHM/AI được liên kết với đối tượng BIM, hồ sơ kiểm tra, yêu cầu công việc hoặc hành động bảo trì; xác định loại thông tin nguồn gốc và mức truy hồi ngược đã được văn liệu báo cáo.

### 6.3 Định vị

| Hạng mục | Quyết định |
|---|---|
| RQ liên quan | Không có RQ riêng; hỗ trợ lập luận khoảng trống của RQ2 |
| WP / Chương | Cầu nối WP1→WP2; hỗ trợ C2 và nền phương pháp C5 |
| Paper / Gate | Không thay Paper 1 / Paper 2; không có Gate riêng |
| Đơn vị phân tích | Một nghiên cứu có mô tả đường chuyển giao từ đầu ra phân tích đến điểm đến nghiệp vụ |

### 6.4 Claim → Evidence → Limitation → Next action

**Claim dự kiến.** Văn liệu tích hợp SHM/AI–BIM chưa mô tả nhất quán việc chuyển giao đầu ra phân tích thành thông tin có thể dùng trong hồ sơ kiểm tra – bảo trì.

**Evidence.** Corpus tái lập được từ Scopus/WoS, sàng lọc theo protocol, snowballing và data-extraction matrix. Các bài đã deep-read (Round 1–3B) chỉ là **seed corpus**, không phải corpus hoàn chỉnh.

**Limitation.** Bài chỉ mô tả và phân loại văn liệu; không đề xuất schema mới, không kiểm chứng traceability, không tạo dữ liệu định lượng thí nghiệm và không giải quyết khoảng trống của Paper 2.

**Next action.** Pilot search 30–50 kết quả.

> **Evidence is currently insufficient** để khẳng định tính mới cho tới khi chứng minh đơn vị phân tích *"information handover"* khác biệt so với các tổng quan BIM–SHM / Digital Twin gần đây.

### 6.5 Dữ liệu và phương pháp tối thiểu

- File quản trị: `SC4_SEARCH_LOG`, `SC4_SCREENING_MATRIX`, `SC4_INCLUDED_STUDIES`, `SC4_EXCLUSION_REASONS`, `SC4_DATA_EXTRACTION_MATRIX`.
- Trường mã hóa: Study_ID / DOI / năm / loại công trình; nguồn đầu vào; đầu ra AI/SHM; điểm liên kết BIM; điểm đến nghiệp vụ; timestamp / identifier / model version / user confirmation; mức kiểm chứng; hướng liên kết một chiều / hai chiều.
- Protocol viết trước khi tìm kiếm; PRISMA 2020 và nguyên tắc systematic mapping; **không** meta-analysis.
- Ít nhất 20–25% mẫu được người thứ hai kiểm tra; AI chỉ hỗ trợ, không thay quyết định học thuật.

### 6.6 Firewall

Không dùng dữ liệu / metric / LORO / CEI của Paper 1; không đề xuất chuỗi định danh, schema, competency questions, round-trip test hoặc action lifecycle của Paper 2; không ánh xạ TCVN/ISO sang IFC như SC-3; không dữ liệu Rapexco.

### 6.7 Go / No-Go

**GO:** pilot xác nhận khoảng trống "information handover" riêng biệt; corpus đủ; protocol tái lập được.
**NO-GO:** kết quả chỉ lặp lại tổng quan BIM–SHM/DT chung; cần dùng schema của Paper 2 để tạo tính mới; hoặc khối lượng làm chậm G1/G2.

---

## 7. SC-5 — Độ lặp lại và ổn định của dữ liệu Healthy

### 7.1 Tên đề xuất

**Tiếng Việt:** Đánh giá độ lặp lại theo run và độ ổn định giữa các campaign của dữ liệu dao động trạng thái khỏe trên mô hình khung thép tỷ lệ 1:10.
**Tiếng Anh:** *Run-Level Repeatability and Between-Campaign Stability of Healthy-State Vibration Measurements on a 1:10 Scaled Steel Frame.*

### 7.2 Mục tiêu

Định lượng biến thiên tự nhiên của dữ liệu S0–Healthy trong cùng campaign và độ dịch chuyển giữa các campaign, từ đó mô tả giới hạn ổn định của phép đo trước khi diễn giải kết quả AI.

### 7.3 Định vị

| Hạng mục | Quyết định |
|---|---|
| RQ liên quan | Tiếp giáp RQ1; không trả lời khả năng phân loại S0/B1/B2/B3 |
| WP / Chương / Paper | WP1 / C4 / Paper 1 — Supporting Scope |
| Gate | Tiếp giáp G1; **không** phải điều kiện đóng G1 |
| Đơn vị phân tích | Một run S0 hợp lệ dưới một campaign, kích thích, sensor và trục xác định |

### 7.4 Claim → Evidence → Limitation → Next action

**Claim.** Mức biến thiên trong cùng campaign và mức dịch chuyển giữa campaign của dữ liệu Healthy có thể được định lượng ở cấp run, giúp phân biệt biến thiên phép đo tự nhiên với thay đổi do điều kiện thu nhận.

**Evidence.** Dữ liệu PASCO S0 từ Campaign 1–3, ba kích thích và tối đa sáu run/tổ hợp — tương đương tối đa 54 recording **nếu** run registry xác nhận đầy đủ và điều kiện lắp đặt tương đương.

> **OI-01 áp dụng cho SC-5** *(xem §3.4)*: mâu thuẫn 3 run vs 6 run chưa được giải quyết. Không công bố con số 54 trước khi registry xác nhận.

**Limitation.** Chỉ ba campaign nên phân tích between-campaign mang tính thăm dò; không phải hiệu chuẩn thiết bị, không suy rộng sang công trình thực, không chẩn đoán và không chứng minh độ ổn định dài hạn.

**Next action.** Khóa `SC5_HEALTHY_RUN_REGISTRY` và audit sự tương đương về cảm biến, vị trí, trục, kích thích, valid interval và mounting status.

### 7.5 Dữ liệu và phương pháp tối thiểu

- Chỉ PASCO và S0–Healthy; không gộp ADXL vì thuộc SC-1.
- Registry: `File_ID; Campaign_ID; Run_ID; Excitation; Sensor_ID; Axis; Sampling_Rate; Valid_Interval; Mounting_Status; QC_Flag; File_Hash`.
- Đặc trưng cấp run: valid-sample ratio, flat/clipping, RMS, standard deviation, peak-to-peak, crest factor, dominant frequency, spectral centroid, band energy, PSD similarity/distance.
- Báo cáo median, IQR, robust coefficient of variation, within-cell repeatability spread, between-campaign median shift và hierarchical bootstrap 95% CI theo run.
- Có thể dùng phân rã phương sai hoặc mô hình hỗn hợp như phân tích bổ sung; **không** dựa kết luận vào p-value khi chỉ có ba campaign.
- Không coi window chồng lấn là quan sát độc lập; không dùng coherence giữa các run không đồng bộ pha.

### 7.6 Firewall

Không B1/B2/B3; không classification; không random split/LORO/LOCO; không RF/SVM/CNN/ResNet1D; không accuracy/macro-F1/confusion matrix; không xếp hạng cấu hình cảm biến; không CEI / `Condition_Evidence_ID`; không chuyển thành baseline Rapexco.

### 7.7 Go / No-Go *(cập nhật — C-05)*

**GO:** Paper 1 đã khóa kết quả và bảng–hình; ba campaign được xác nhận; có đủ run hợp lệ; điều kiện lắp đặt và kích thích truy vết được; OI-01 đã giải quyết.

**NO-GO:**
- mapping Campaign 1–2 còn không ổn định;
- thay đổi gá hoặc hướng trục không kiểm soát;
- chỉ còn một campaign;
- kết quả chỉ có ý nghĩa khi thêm B1–B3 hoặc phân loại;
- 🔴 **MỚI:** **hai campaign bất kỳ không phải hai lần lắp đặt / tháo lắp độc lập.** Nếu Campaign 2 và Campaign 3 được thu trong cùng một phiên đo, thì "between-campaign shift" giữa chúng không phản ánh biến thiên giữa các lần lắp đặt mà chỉ là nhiễu trong phiên — toàn bộ claim between-campaign của SC-5 mất hiệu lực. **Phải xác nhận từ sổ ghi chép thí nghiệm trước khi bắt đầu.**

---

## 8. 🆕 SC-6 — Khảo sát thực hành hồ sơ kiểm tra – bảo trì

### 8.1 Tên đề xuất

**Tiếng Việt:** Thực trạng lập và lưu trữ hồ sơ kiểm tra – bảo trì công trình thép công nghiệp tại Việt Nam: khảo sát thực hành quản lý.
**Tiếng Anh:** *Current Practice in Inspection and Maintenance Record-Keeping for Industrial Steel Buildings in Vietnam: A Practitioner Survey.*

### 8.2 Mục tiêu

Mô tả một cách có phương pháp **thực hành đang tồn tại**: ai lập hồ sơ kiểm tra, ghi những trường thông tin gì, lưu ở đâu, ai phê duyệt, dựa vào đâu để coi một công việc bảo trì là đã hoàn tất, và trong trường hợp nào một hồ sơ đã đóng được mở lại.

### 8.3 Định vị

| Hạng mục | Quyết định |
|---|---|
| RQ liên quan | **Không** trả lời RQ nào; cung cấp bằng chứng thực hành làm đầu vào cho expert review của G2 |
| WP / Chương / Paper | Hỗ trợ bối cảnh C5; **không** thuộc Paper 1, Paper 2 hay Paper 3 |
| Gate | **Không tiếp giáp Gate nào.** Không phải điều kiện đóng, mở hay chuyển trạng thái G1–G5 |
| Đơn vị phân tích | Một người hành nghề trả lời về thực hành tại một cơ sở |
| Dữ liệu | Bảng hỏi và/hoặc phỏng vấn bán cấu trúc. **Không một byte nào từ Campaign 1–3. Không dữ liệu Rapexco.** |

### 8.4 Claim → Evidence → Limitation → Next action

**Claim.** Thực hành lập, phê duyệt, xác nhận hoàn tất và đóng/mở lại hồ sơ kiểm tra – bảo trì công trình thép công nghiệp tại Việt Nam có thể được mô tả và phân nhóm từ báo cáo của người hành nghề; các thực hành này không đồng nhất giữa các cơ sở.

**Evidence.** Bảng hỏi/phỏng vấn bán cấu trúc với người hành nghề; protocol mã hóa được khai báo trước; bảng tần suất và trích dẫn minh họa. Tiền lệ phương pháp: `YGZ32C8M` (*Identifying Maturity Dimensions for Smart Maintenance Management*, 48 phỏng vấn + 7 chuyên gia phản biện, ASCE) cho thấy loại nghiên cứu này được chấp nhận trong ngành Quản lý Xây dựng.

**Limitation.** Mẫu thuận tiện, quy mô nhỏ, không đại diện thống kê cho toàn ngành; mô tả tự báo cáo chứ không phải kiểm toán hồ sơ thực tế; **không đề xuất schema, không kiểm chứng traceability, không tạo yêu cầu kỹ thuật ràng buộc**.

**Next action.** Viết `SC6_SURVEY_PROTOCOL.md` (câu hỏi, tiêu chí chọn mẫu, phiếu đồng ý tham gia, khung mã hóa) **trước khi** tiếp cận người trả lời đầu tiên.

### 8.5 Khung bảng hỏi — ánh xạ tới G2 Decision Register

Đây là điểm giá trị cốt lõi của SC-6. Mỗi nhóm câu hỏi tương ứng một mục đang treo trong `01_MASTER_G1_G2_G3_EVIDENCE_SYNTHESIS` §F.

| Nhóm | Câu hỏi khảo sát (rút gọn) | Mục Decision Register | Trạng thái hiện tại |
|---|---|---|---|
| Q1 | Một lần kiểm tra thường dẫn tới bao nhiêu công việc bảo trì? Có trường hợp nhiều lần kiểm tra dồn vào một công việc không? | Exact Inspection-Action cardinality | `EXPERT_REVIEW_REQUIRED` |
| Q2 | Anh/chị dùng những trạng thái nào để mô tả tiến trình một công việc bảo trì, từ lúc phát hiện đến lúc kết thúc? | Action lifecycle vocabulary | `EXPERT_REVIEW_REQUIRED` |
| Q3 | Ai được phép phê duyệt, từ chối, hoặc yêu cầu làm lại? Người thực hiện và người xác nhận có phải hai người khác nhau không? | Role and permission matrix | `EXPERT_REVIEW_REQUIRED` |
| Q4 | Căn cứ nào để xác nhận một công việc đã hoàn tất *thật sự*, khác với việc chỉ được đánh dấu "đã xong"? | Exact verification criteria | `EXPERT_REVIEW_REQUIRED` |
| Q5 | Có cần văn bản ủy quyền/phê duyệt trước khi thực hiện không? Ở mức chi phí hoặc rủi ro nào? | Authorization requirement | `FREEZE_PROVISIONALLY` |
| Q6 | Việc xác nhận sau thi công có được ghi thành hồ sơ riêng, hay ghi chung vào biên bản kiểm tra? | Verification entity/subtype | `FREEZE_PROVISIONALLY` |
| Q7 | Trong trường hợp nào một hồ sơ đã đóng được mở lại? Ai quyết định? | Closure/reopen policy | `FREEZE_PROVISIONALLY` |
| Q8 | Hồ sơ được lưu ở đâu (giấy, Excel, phần mềm)? Lưu bao lâu? Có tra ngược lại được không? | Bối cảnh chung | — |

**Quy mô đề xuất:** 12–20 người trả lời từ tối thiểu 5 cơ sở khác nhau. Đủ cho một bài hội thảo mô tả; không đủ và không nhằm mục đích suy luận thống kê.

### 8.6 Firewall

- ❌ Không đề xuất schema, chuỗi định danh, hay mô hình dữ liệu nào.
- ❌ Không dùng `Sensor_ID`, `Condition_Evidence_ID`, `Inspection_Record_ID`, `Action_Record_ID`, `Status_Event_ID`, CEI.
- ❌ Không competency questions, không truy vấn hai chiều, không round-trip test.
- ❌ Không dữ liệu Campaign 1–3, không Rapexco, không AI/SHM.
- ❌ Không kết luận rằng thực hành hiện tại "sai" hay "cần thay bằng khung của luận án" — bài này **mô tả**, không **kê đơn**.
- ✅ Được phép nêu ở phần Discussion rằng sự không đồng nhất quan sát được cho thấy nhu cầu chuẩn hóa — nhưng **không** trình bày giải pháp.

### 8.7 Go / No-Go

**GO:**
- Protocol khảo sát viết xong và được thầy xem trước khi thu mẫu;
- Xác nhận yêu cầu ethics/consent của trường (xem OI-05);
- Tiếp cận được tối thiểu 5 cơ sở;
- Bài **không** đề xuất giải pháp kỹ thuật.

**NO-GO:**
- Không đủ người trả lời để mô tả có ý nghĩa (dưới ~8 người);
- Tính mới chỉ xuất hiện khi đưa schema hoặc chuỗi định danh của Paper 2 vào;
- Việc thu mẫu làm chậm Gate 1.

### 8.8 Sản phẩm phụ cho luận án

✅ **`SC6_EXPERT_FEEDBACK_RECORD.md` — dữ liệu thực hành trích dẫn được cho 4 mục `EXPERT_REVIEW_REQUIRED` và 3 mục `FREEZE_PROVISIONALLY` đang chặn G2.**

Đây là bài duy nhất trong toàn danh mục vừa **khởi động được ngay hôm nay**, vừa **không chạm ô nào trong ma trận sở hữu §12**, vừa **sinh ra chính xác loại bằng chứng đang chặn Gate 2**.

---

## 9. 🆕 SC-7 — Tiêu chí lựa chọn hệ đo dao động chi phí thấp

### 9.1 Tên đề xuất

**Tiếng Việt:** Lựa chọn hệ đo dao động chi phí thấp cho công trình thép công nghiệp ven biển: các ràng buộc triển khai và tiêu chí đánh giá.
**Tiếng Anh:** *Selecting Low-Cost Vibration Sensing for Coastal Industrial Steel Buildings: Deployment Constraints and Qualification Criteria.*

### 9.2 Mục tiêu

Xây dựng khung tiêu chí có cấu trúc để lựa chọn và kiểm định (*qualification*) hệ đo dao động chi phí thấp cho công trình thép công nghiệp trong môi trường ven biển, dựa trên phân tích thông số kỹ thuật, chi phí và ràng buộc môi trường — **không** dựa trên thí nghiệm mới.

### 9.3 Định vị

| Hạng mục | Quyết định |
|---|---|
| RQ liên quan | **Không**; hỗ trợ chuẩn bị Stream C (G4 readiness) |
| WP / Chương / Paper | Hỗ trợ bối cảnh C6; **không** thuộc Paper 1/2/3 |
| Gate | **Không tiếp giáp Gate nào**; không phải evidence G4 và không chứng minh field feasibility |
| Đơn vị phân tích | Một tiêu chí lựa chọn/kiểm định và các phương án đáp ứng tương ứng |
| Dữ liệu | Nghiên cứu bàn giấy: datasheet, giá công bố, văn liệu. **Không dữ liệu đo của đề tài.** |

### 9.4 Claim → Evidence → Limitation → Next action

**Claim.** Việc lựa chọn hệ đo dao động chi phí thấp cho công trình ven biển có thể được cấu trúc thành một tập tiêu chí tường minh gồm hiệu năng đo, độ bền môi trường, nguồn điện, truyền dữ liệu, khả năng bảo trì và chi phí vòng đời; các tiêu chí này cho thấy hệ chi phí thấp cần được kiểm định riêng cho từng ứng dụng thay vì chấp nhận theo thông số danh nghĩa.

**Evidence.** `LZPF7ILT` (node chi phí thấp: thành công với kích thích xung, thất bại với dao động môi trường → cần qualification riêng); `XSKNR656` (quy trình MEMS chi phí thấp trong vận hành); `9823WXJZ` (tiền lệ triển khai trên công trình khung thép); `TRZY4P6X`, `GE3XSAYV`, `D3TGCKXW` (ảnh hưởng nhiệt độ, ngưỡng vận hành, dữ liệu thiếu trong triển khai dài hạn). Bổ sung bằng datasheet và giá công bố có trích dẫn.

**Limitation.** Nghiên cứu bàn giấy; **không** có kiểm chứng thực nghiệm mới; **không** khuyến nghị một sản phẩm thương mại cụ thể; **không** chứng minh khả năng triển khai thực tế; **không** phải evidence cho G4.

**Next action.** Khóa danh mục tiêu chí và bảng nguồn trích dẫn trước khi so sánh phương án.

### 9.5 Cấu trúc khung tiêu chí đề xuất

| Nhóm | Tiêu chí | Ghi chú ràng buộc ven biển |
|---|---|---|
| Hiệu năng đo | Dải tần, noise floor, dải đo, độ phân giải, đồng bộ đa kênh | Dao động môi trường biên độ thấp là trường hợp khó nhất |
| Độ bền môi trường | Cấp bảo vệ IP, chống ăn mòn muối, dải nhiệt độ và độ ẩm | Yếu tố phân biệt chính của môi trường ven biển |
| Nguồn điện | Nguồn lưới / pin / năng lượng mặt trời; tuổi thọ; khả năng tiếp cận để thay | Nhà xưởng công nghiệp thường thiếu ổ cắm gần vị trí đo |
| Truyền dữ liệu | Có dây / không dây; băng thông; mất gói; lưu đệm khi mất kết nối | `D3TGCKXW`: dữ liệu thiếu chi phối phân tích thực địa |
| Vận hành – bảo trì | Cách gá, hiệu chuẩn lại, thay thế, tay nghề yêu cầu | Ảnh hưởng trực tiếp chi phí vòng đời |
| Chi phí | Đầu tư ban đầu, chi phí/kênh, chi phí vận hành năm | Trình bày dạng khoảng, không phải báo giá |
| Kiểm định | Thử nghiệm tối thiểu cần làm trước khi tin số liệu | Rút ra trực tiếp từ `LZPF7ILT` |

### 9.6 Firewall

- ❌ Không dữ liệu Campaign 1–3; không kết quả PASCO/ADXL của đề tài *(so sánh thực nghiệm hai hệ đo thuộc **SC-1**)*.
- ❌ Không phân loại, không AI, không LORO, không CEI.
- ❌ Không xếp hạng cấu hình cảm biến của đề tài.
- ❌ Không dữ liệu, hình ảnh hay thông số công trình Rapexco.
- ❌ Không tuyên bố sẵn sàng triển khai hoặc khả thi hiện trường.
- ❌ Không khuyến nghị mua sản phẩm cụ thể — trình bày theo **lớp thiết bị**, không theo thương hiệu.

### 9.7 Ranh giới với SC-1

| | SC-1 | SC-7 |
|---|---|---|
| Câu hỏi | Hai hệ đo cụ thể có tương hợp không? | Nên chọn hệ đo theo tiêu chí nào? |
| Bằng chứng | Thực nghiệm, dữ liệu đồng bộ | Bàn giấy, datasheet và văn liệu |
| Kết quả chính | Chỉ số tương hợp định lượng | Khung tiêu chí định tính |
| Dùng lại bảng/hình của nhau | **Không được** | **Không được** |

### 9.8 Go / No-Go

**GO:** khung tiêu chí đủ chi tiết để có giá trị thực hành; mọi thông số và giá đều có nguồn trích dẫn được; bài không tuyên bố tính khả thi hiện trường.
**NO-GO:** bài chỉ là bảng so sánh sản phẩm không có khung phân tích; hoặc phải dùng dữ liệu đo của đề tài để có kết luận.

### 9.9 Sản phẩm phụ cho luận án

✅ Khung tiêu chí dùng lại trực tiếp cho **Stream C bước 2** (field sensor register và mapping protocol) khi G4 readiness được kích hoạt.

---

## 10. ⚠️ SC-8 — Bài mô tả thiết lập thí nghiệm *(tùy chọn, có cảnh báo)*

**Tên:** Thiết kế và chế tạo mô hình khung thép liên kết bulông tỷ lệ 1:10 phục vụ nghiên cứu giám sát tình trạng: thiết lập thí nghiệm và quy trình thu số liệu.

**Nội dung:** thuần mô tả — hình học, vật liệu, cấu tạo liên kết, cách tạo trạng thái hư hỏng, bố trí cảm biến, kích thích, quy trình QC dữ liệu. **Không kết quả, không phân loại, không hiệu năng, không con số nào của Paper 1.**

> ### ⚠️ CẢNH BÁO
> Nội dung này chính là **Mục 3 (Experimental Setup) của Paper 1**. Công bố trước tạo trùng lặp văn bản với bài tạp chí. Nhiều tạp chí chấp nhận nếu khai báo đầy đủ trong cover letter và phần setup được viết lại hoàn toàn, nhưng đây là **rủi ro có thật**.

**Chỉ kích hoạt khi:** cần gấp một bài cho hội thảo tháng 10, và cả SC-6 lẫn SC-7 đều không kịp. **Nếu SC-6 kịp thì bỏ SC-8.**

**Bắt buộc nếu làm:** khai báo bài này trong cover letter khi nộp Paper 1; viết lại hoàn toàn Mục 3 của Paper 1, không copy văn bản.

---

## 11. Ma trận sở hữu tài sản nghiên cứu

**Ký hiệu:** **Lõi** = tài sản dành riêng cho Paper lõi · **Chính** = đóng góp riêng của bài SC · **Có ĐK** = chỉ dùng theo firewall và có khai báo · **Loại trừ** = không được dùng · **Bối cảnh** = chỉ dùng để định vị.

| Tài sản / dữ liệu / phương pháp | Chủ sở hữu ưu tiên | SC-1 | SC-2 | SC-3 | SC-4 | SC-5 | **SC-6** | **SC-7** |
|---|---|---|---|---|---|---|---|---|
| Campaign 1–3 và run registry lõi | Paper 1 | Có ĐK: paired subset | Loại trừ | Loại trừ | Loại trừ | Có ĐK: S0 subset | **Loại trừ** | **Loại trừ** |
| Phân loại S0/B1/B2/B3 | Paper 1 | Loại trừ | Loại trừ | Loại trừ | Loại trừ | Loại trừ | **Loại trừ** | **Loại trừ** |
| Random split vs run-aware/LORO | Paper 1 | Loại trừ | Loại trừ | Loại trừ | Loại trừ | Loại trừ | **Loại trừ** | **Loại trừ** |
| So sánh / xếp hạng cấu hình cảm biến | Paper 1 | Loại trừ | Loại trừ | Loại trừ | Loại trừ | Loại trừ | **Loại trừ** | **Loại trừ** |
| RF / CNN / ResNet1D và metric phân loại | Paper 1 | Loại trừ | Loại trừ trên dữ liệu luận án | Loại trừ | Loại trừ | Loại trừ | **Loại trừ** | **Loại trừ** |
| CEI / bằng chứng trạng thái đầu ra | Paper 1 → Paper 2 | Loại trừ | Loại trừ | Loại trừ | Loại trừ | Loại trừ | **Loại trừ** | **Loại trừ** |
| Tương hợp PASCO–ADXL | SC-1 | **Chính** | — | — | — | Loại trừ | — | Loại trừ |
| HPO hiệu năng–chi phí trên dữ liệu độc lập | SC-2 | — | **Chính** | — | — | — | — | — |
| Requirement-to-IFC cho thông tin tài sản tĩnh | SC-3 | — | — | **Chính** | Bối cảnh | — | Loại trừ | — |
| Taxonomy information handover trong văn liệu | SC-4 | — | — | Bối cảnh | **Chính** | — | Bối cảnh | — |
| Độ lặp lại S0 theo run/campaign | SC-5 | Loại trừ | — | — | — | **Chính** | — | — |
| **Dữ liệu khảo sát thực hành người hành nghề** | **SC-6** | — | — | — | Bối cảnh | — | **Chính** | — |
| **Khung tiêu chí lựa chọn hệ đo chi phí thấp** | **SC-7** | Loại trừ | — | — | — | — | — | **Chính** |
| Chuỗi `Sensor_ID → … → Action_Record_ID` | Paper 2 | Loại trừ | Loại trừ | Loại trừ | Loại trừ | Loại trừ | **Loại trừ** | **Loại trừ** |
| Competency questions, truy vết hai chiều, round-trip | Paper 2 | Loại trừ | Loại trừ | Loại trừ | Loại trừ | Loại trừ | **Loại trừ** | **Loại trừ** |
| Inspection/action lifecycle và quyền hạn hồ sơ *(dưới dạng schema đề xuất)* | Paper 2 / Paper 3 | Loại trừ | Loại trừ | Loại trừ | Loại trừ | Loại trừ | **Loại trừ**¹ | **Loại trừ** |
| Baseline hiện trường và Rapexco | Paper 3 | Loại trừ | Loại trừ | Loại trừ | Loại trừ | Loại trừ | **Loại trừ** | **Loại trừ** |
| Logic Normal→Watch→Inspect→Priority Inspection | WP4 / Paper 3–4 | Loại trừ | Loại trừ | Loại trừ | Loại trừ | Loại trừ | **Loại trừ** | **Loại trừ** |

> ¹ **Ranh giới quan trọng cho SC-6.** SC-6 được phép **mô tả** vòng đời hành động và phân quyền *đang tồn tại trong thực hành*, vì đó là dữ liệu quan sát được. SC-6 **không** được đề xuất, chuẩn hóa hay khuyến nghị một vòng đời/ma trận quyền hạn — đó là tài sản của Paper 2. Ranh giới: **mô tả được, kê đơn không.**

---

## 12. Ma trận xâm phạm đối với các Paper lõi

**Thang:** Thấp = độc lập rõ · Trung bình = tiếp giáp, cần firewall · Cao = dùng tài sản cùng nguồn, chỉ làm sau khi Paper lõi khóa.

| Bài | Paper 1 / G1 | Paper 2 / G2–G3 | Paper 3 / G4 | Nguyên nhân chính | Kiểm soát bắt buộc |
|---|---:|---:|---:|---|---|
| **SC-1** | **Trung bình** | Thấp | Thấp | Dùng một phần phiên đo liên quan WP1 | Chỉ sensor agreement; không phân loại/LORO; Paper 1 khóa trước; OI-01 giải quyết trước |
| **SC-2** | Thấp | Thấp | Thấp | Dữ liệu và câu hỏi độc lập | Cấm Campaign 1–3; khai báo dataset và quyền sử dụng |
| **SC-3** | Thấp | **Trung bình** | Thấp | Tiếp giáp quản lý thông tin và IFC | Chỉ asset information tĩnh; cấm schema/CQ/inspection-action; GO-gate về toàn văn tiêu chuẩn |
| **SC-4** | Thấp | **Trung bình** | Thấp | Có thể công bố trước khoảng trống và taxonomy của Paper 2 | Chỉ mapping văn liệu; không đề xuất giải pháp/schema; pilot novelty trước |
| **SC-5** | **Cao** | Thấp | Thấp | Dùng S0 của Campaign 1–3 và metadata run/campaign | Paper 1 sở hữu ưu tiên; chỉ Healthy repeatability; khóa Paper 1 trước; kiểm tra tính độc lập campaign |
| **🆕 SC-6** | **Thấp** | **Trung bình** | **Thấp** | Chủ đề tiếp giáp trách nhiệm giải trình của Paper 2 | **Mô tả được, kê đơn không.** Không schema, không định danh, không CQ. Chỉ thực hành đang tồn tại |
| **🆕 SC-7** | **Thấp** | **Thấp** | **Trung bình** | Tiếp giáp chuẩn bị hệ đo hiện trường của Paper 3 | Bàn giấy thuần túy; không dữ liệu Rapexco; không tuyên bố khả thi hiện trường |

### 12.1 Ma trận xâm phạm giữa các bài SC

| Cặp bài | Rủi ro | Điểm giao nhau | Firewall |
|---|---:|---|---|
| SC-1 ↔ SC-5 | Trung bình | Cùng bối cảnh lab, có thể cùng file PASCO Healthy | SC-1 sở hữu cross-sensor agreement; SC-5 sở hữu within/between-campaign variability; không dùng lại bảng/hình |
| SC-3 ↔ SC-4 | Trung bình | Cùng bối cảnh chuyển giao thông tin/BIM | SC-3 là clause-to-IFC pilot; SC-4 là taxonomy văn liệu; SC-4 không lập requirement matrix |
| **SC-1 ↔ SC-7** | **Trung bình** | **Cùng chủ đề lựa chọn và chất lượng hệ đo** | **SC-1 thực nghiệm hai hệ cụ thể; SC-7 bàn giấy về tiêu chí. SC-7 không dùng bất kỳ số liệu nào của SC-1** |
| **SC-3 ↔ SC-6** | **Trung bình** | **Cùng bối cảnh yêu cầu thông tin bảo trì** | **SC-3 = yêu cầu theo tiêu chuẩn → trường IFC. SC-6 = thực hành đang tồn tại theo báo cáo người hành nghề. SC-6 không lập requirement matrix; SC-3 không dùng dữ liệu khảo sát** |
| **SC-4 ↔ SC-6** | Thấp | Cùng chủ đề chuyển giao thông tin | SC-4 = văn liệu; SC-6 = thực hành thực địa. Không chia sẻ corpus hay bảng mã hóa |
| SC-1 ↔ SC-2 | Thấp | Cùng lĩnh vực dao động/AI | SC-2 dùng dữ liệu độc lập và HPO; SC-1 không AI |
| SC-2 ↔ SC-5 | Thấp | Cùng bối cảnh dữ liệu dao động | SC-2 dùng dataset độc lập; SC-5 không HPO/phân loại |
| **SC-6 ↔ SC-7** | Thấp | Cùng bối cảnh quản lý tài sản | SC-6 = hồ sơ và quy trình; SC-7 = thiết bị đo. Không giao nhau về dữ liệu hay kết luận |
| Các cặp còn lại | Thấp | Chỉ giao ở bối cảnh luận án | Không tái sử dụng claim, kết quả, bảng, hình hoặc văn bản đáng kể |

---

## 13. Thứ tự ưu tiên và ánh xạ hội thảo

### 13.1 Thứ tự ưu tiên *(đảo lại — C-07)*

Tiêu chí xếp hạng **mới**: **đòn bẩy = giá trị cho luận án ÷ công việc mới phát sinh**. Tiêu chí cũ (độ sạch firewall) đã bị thay thế, vì firewall sạch chỉ là sự vắng mặt của rủi ro, không phải giá trị.

| Thứ tự | Công việc | Đòn bẩy | Điều kiện kích hoạt |
|---:|---|:---:|---|
| **0** | **Hoàn thành Gate 1 / Paper 1** | — | Luôn ưu tiên trước mọi bài SC |
| **1** | **SC-6** | ⭐⭐⭐ | Không phụ thuộc Gate. **Bắt đầu ngay.** Sinh evidence cho 7 mục đang chặn G2 |
| **2** | **SC-1** | ⭐⭐⭐ | Sau khi OI-01 giải quyết và Paper 1 khóa. Sinh `PAIRED_REGISTRY` = G1 Stream A bước 1–2 |
| **3** | **SC-3** | ⭐⭐⭐ | Sau khi qua GO-gate về toàn văn tiêu chuẩn. Giải quyết mục `REVIEW_REQUIRED` của G2 |
| **4** | **SC-7** | ⭐⭐ | Không phụ thuộc Gate. Có thể chạy song song bất cứ lúc nào |
| **5** | **SC-5** | ⭐⭐ | Sau Paper 1 khóa + xác nhận tính độc lập campaign |
| **6** | **SC-2** | ⭐ | Chỉ sau khi Gate 1 đóng và còn dư nguồn lực |
| **7** | **SC-4** | ⭐ | Dự phòng. Dừng nếu pilot không chứng minh tính mới |
| *(dự phòng)* | *SC-8* | — | *Chỉ khi deadline gấp và SC-6/SC-7 không kịp* |

**Khuyến nghị danh mục thực dụng cho 2026:** **SC-6 và SC-7** là hai bài khả thi chắc chắn. **SC-1 và SC-3** là hai bài mục tiêu nếu điều kiện kích hoạt được giải quyết kịp. **SC-2, SC-4, SC-5** đẩy sang 2027.

### 13.2 Ánh xạ hội thảo *(mới — C-10)*

| Hội thảo | Thời điểm | Bài chính | Bài dự phòng | Ghi chú |
|---|---|---|---|---|
| Quốc tế trong nước — Miền Tây | Tháng 10/2026 | **SC-6** | SC-7 | Bài duy nhất khởi động ngay được; nếu thu mẫu không kịp thì đổi sang SC-7 |
| Quốc tế trong nước — Hà Nội | Tháng 12/2026 | **SC-1** | SC-7 | Cần OI-01 và Paper 1 khóa; nếu không kịp thì SC-7 |
| Hội thảo trong nước | Cuối 2026 (chưa rõ) | **SC-3** *(bản TCVN nếu không có ISO)* | SC-6 bản tiếng Việt | Tiếng Việt phù hợp với cả hai |

> 🔴 **Việc phải làm ngay:** tra deadline chính thức của cả ba hội thảo. Hội thảo tháng 10 nhiều khả năng có deadline trong tháng 8–9/2026. Nếu deadline quá gấp, ưu tiên tuyệt đối cho SC-7 (bàn giấy, viết nhanh nhất) thay vì SC-6 (cần thời gian thu mẫu).

---

## 14. Cơ chế thu hoạch phản biện chuyên gia *(mới — C-11)*

Mục đích tuyên bố của toàn bộ danh mục này là *tập viết và thu góp ý chuyên gia*. Góp ý nghe xong rồi quên là mất trắng. Mỗi bài phải có một file lưu trữ.

**File bắt buộc cho mỗi bài đã trình bày:** `SCx_EXPERT_FEEDBACK_RECORD.md`

| Trường | Nội dung |
|---|---|
| `Feedback_ID` | Định danh duy nhất |
| `Event` | Tên hội thảo, ngày, phiên |
| `Respondent_Name` | Tên người góp ý |
| `Respondent_Affiliation` | Đơn vị |
| `Respondent_Role` | Chức danh / lĩnh vực chuyên môn |
| `Feedback_Text` | Nội dung góp ý, ghi nguyên văn |
| `Mapped_Decision_Item` | Mục Decision Register tương ứng (nếu có) |
| `Action_Taken` | Đã tiếp thu / đã bác / đang xem xét |
| `Date_Recorded` | Ngày ghi nhận |

**Riêng SC-6:** phản hồi thu được **là dữ liệu nghiên cứu**, phải tuân thủ protocol khảo sát và phiếu đồng ý tham gia; không phải ghi chép ngẫu nhiên tại hội trường.

**Cách khai thác tối đa tại hội thảo:** chuẩn bị sẵn phiếu ghi ý kiến ngắn (in giấy hoặc mã QR dẫn tới form) phát tại phiên trình bày. Người dự thường sẵn sàng trả lời 5 câu trong 3 phút hơn là viết email sau đó.

---

## 15. Quy tắc Go / No-Go chung

### GO khi

- Câu hỏi, dữ liệu, đơn vị phân tích và **câu kết luận chính** khác Paper lõi. *(Đổi phương pháp hay mô hình là chưa đủ — tạp chí kiểm tra trùng kết luận, không kiểm tra trùng phương pháp.)*
- Protocol, metric và nội dung loại trừ được khóa trước phân tích cuối.
- Có provenance, quyền sử dụng dữ liệu và chính sách proceedings/tạp chí rõ.
- Không tái sử dụng bảng, hình, kết quả hoặc văn bản đáng kể.
- **Đồng tác giả đã thống nhất trước khi bắt đầu viết** *(C-12)*.
- Cả hai thầy xem ma trận chồng lấn và đồng ý nộp bằng văn bản.

### NO-GO khi

- Bài chỉ là phiên bản thu nhỏ của Paper 1 hoặc Paper 2.
- Tính mới chỉ xuất hiện khi dùng LORO, xếp hạng cảm biến, CEI, schema truy vết, competency questions hoặc dữ liệu Rapexco.
- Cần công bố trước một claim/kết quả mà Paper lõi chưa khóa.
- Chính sách prior publication / copyright không rõ.
- Công việc làm chậm Evidence Gate kế tiếp.

### Câu bắt buộc trong mục Limitations của mọi bài

**Tiếng Anh:**
> *Results reported here are preliminary and are produced under an internal evidence-gate process that has not been closed. They are not presented as validated structural diagnosis and are not transferable to field conditions.*

**Tiếng Việt:**
> *Kết quả trình bày là kết quả sơ bộ, được tạo ra trong quy trình nghiệm thu bằng chứng nội bộ chưa hoàn tất; không phải kết luận chẩn đoán kết cấu đã được kiểm chứng và không được suy diễn sang điều kiện hiện trường.*

---

## 16. Checklist trước mỗi lần nộp

- [ ] Xác nhận mã SC và phiên bản protocol.
- [ ] Khóa câu hỏi, dataset, đơn vị nhóm, metric chính và bảng–hình dự kiến.
- [ ] **Câu kết luận trong Abstract khác Paper 1 và Paper 2.**
- [ ] **Không có bất kỳ con số ResNet1D nào.**
- [ ] **Không dùng ký hiệu `… → Action_Status` ở bất kỳ đâu.**
- [ ] Nếu nhắc `Status_Event`, có ghi rõ `PROPOSED — NOT ACCEPTED`.
- [ ] Câu bắt buộc §15 có trong mục Limitations.
- [ ] Không dùng *validated* / *passed* / *proven* / *field-ready*.
- [ ] Cập nhật ma trận xâm phạm với Papers 1–3 và các SC đã nộp.
- [ ] Kiểm tra proceedings, indexing, copyright, prior publication và quyền mở rộng thành bài tạp chí.
- [ ] Khai báo đầy đủ dataset / phiên đo / bài liên quan trong manuscript và cover letter.
- [ ] Không có bản thảo chồng lấn đáng kể đang được xét đồng thời.
- [ ] **Đồng tác giả đã thống nhất trước khi bắt đầu viết.**
- [ ] Đã lập `SCx_EXPERT_FEEDBACK_RECORD.md` trước khi trình bày.
- [ ] Cả hai thầy phê duyệt Go/No-Go bằng văn bản.
- [ ] Nếu bằng chứng chưa đủ, ghi rõ: **Evidence is currently insufficient.**

---

## 17. Đoạn trình thầy

> Em tổng hợp bảy ý tưởng bài hội thảo thuộc Supporting Scope, kèm ma trận sở hữu tài sản và ma trận xâm phạm để bảo vệ đóng góp của Paper 1 và Paper 2.
>
> **SC-1** đánh giá tương hợp hai hệ đo PASCO–ADXL; **SC-2** so sánh chiến lược HPO trên dữ liệu độc lập ngoài đề tài; **SC-3** ánh xạ yêu cầu thông tin tài sản tĩnh theo TCVN 14177 và ISO 19650 sang thuộc tính IFC; **SC-4** là systematic mapping về chuyển giao thông tin từ đầu ra AI/SHM sang hồ sơ kiểm tra; **SC-5** định lượng độ lặp lại của dữ liệu trạng thái khỏe giữa run và campaign; **SC-6** khảo sát thực hành lập và lưu trữ hồ sơ kiểm tra – bảo trì của người hành nghề; **SC-7** xây dựng khung tiêu chí lựa chọn hệ đo dao động chi phí thấp cho công trình ven biển.
>
> Không bài nào sử dụng kết quả LORO, xếp hạng cấu hình cảm biến, CEI, chuỗi định danh truy vết, competency questions hoặc dữ liệu Rapexco để công bố trước. Gate 1 và Paper 1 vẫn là ưu tiên tuyệt đối.
>
> Em xin báo cáo ba điểm cần thầy cho ý kiến:
>
> 1. **SC-6 và SC-7 là hai bài duy nhất không phụ thuộc Evidence Gate nào** và có thể bắt đầu ngay. Em đề xuất ưu tiên SC-6 vì kết quả khảo sát sẽ cung cấp bằng chứng thực hành cho bảy mục đang treo `EXPERT_REVIEW_REQUIRED` và `FREEZE_PROVISIONALLY` của Gate 2. Em xin ý kiến thầy về việc thu mẫu và yêu cầu thủ tục của trường.
> 2. **SC-1 và SC-5 đang bị chặn bởi một mâu thuẫn số run** trong hồ sơ hiện có (36 cặp ứng với 3 run/tổ hợp, nhưng 54 recording ứng với 6 run/tổ hợp). Em sẽ giải quyết trong canonical run registry trước khi viết.
> 3. **SC-5 cần xác nhận rằng các campaign là những lần lắp đặt độc lập.** Nếu hai campaign được thu trong cùng một phiên đo thì phân tích between-campaign không còn hiệu lực.
>
> Trước mỗi lần nộp, em sẽ kiểm tra chính sách venue, cập nhật ma trận chồng lấn và xin thầy quyết định Go/No-Go bằng văn bản. Em cũng xin ý kiến thầy về việc đứng tên đồng tác giả, thống nhất trước khi bắt đầu viết.

---

## 18. Source of truth *(đã cập nhật — C-03)*

Tài liệu này được đối chiếu với danh sách thẩm quyền hiện hành theo `SOURCE_OF_TRUTH_HIERARCHY_v2.1`:

**Tầng 1 — Quyết định thầy và ADR đã chấp thuận**
1. Quyết định của hai thầy hướng dẫn và Limited-FEM ADR.
2. `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260719.md`
3. `RESEARCH_ARCHITECTURE_DECISION_RECORD_ACTION_ID_20260719.md` *(ACCEPTED — cơ sở của C-01)*

**Tầng 2 — Charter**

4. `MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`

**Tầng 3–4 — Ma trận và Gate**

5. `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md`
6. `EVIDENCE_GATES_v2.1.md`

**Tầng 5 — Chỉ mục và tổng hợp hiện hành**

7. `00_MASTER_INDEX_CURRENT_20260804.md`
8. `01_MASTER_G1_G2_G3_EVIDENCE_SYNTHESIS_20260804.md`
9. `CURRENT_STATUS_AND_NEXT_DIRECTION.md` (v2.2)
10. `MASTER_INDEX_CURRENT.md` (v2.2)

**Tầng 6 — Bằng chứng**

11. `LIVING_EVIDENCE_BASE_v2.1_TRACEABILITY_CORE.md`
12. Round 1–3B (immutable, có SHA-256)

**Tầng 7 — Định hướng Paper**

13. `PAPER1_DIRECTION_AND_GATE_v2.1_20260719.md` (nội dung v2.2)
14. `PAPER2_CURRENT_DIRECTION_v2.1_20260804.md` (nội dung v2.2)
15. `G2_G3_PAPER2_CURRENT_ROADMAP_v2.1_20260804.md`

**Đầu vào chưa chấp thuận (tham chiếu có nhãn)**

16. `ADR_ACTION_STATUS_EVENT_20260804_DRAFT.md` — `PROPOSED — NOT ACCEPTED`

**Đã gỡ khỏi danh sách đối chiếu ở v1.3:** `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` và `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md` — đã bị thay thế bởi tầng 20260719; việc còn đối chiếu với chúng chính là nguyên nhân sinh ra lỗi chuỗi định danh trong v1.2.

> Nếu có quyết định mới được hai thầy chấp thuận, quyết định đó có ưu tiên cao hơn tài liệu này và bản v1.3 phải được cập nhật trước khi sử dụng tiếp.

---

## 19. Danh mục việc còn mở (Open Items)

| Mã | Nội dung | Chặn cái gì | Cách giải quyết |
|---|---|---|---|
| **OI-01** | Số run thật: 3 hay 6 mỗi tổ hợp? | SC-1, SC-5, và gói bất định của Paper 1 | Canonical run registry + sổ ghi chép thí nghiệm |
| **OI-02** | Campaign 2 và Campaign 3 có phải hai lần lắp đặt độc lập không? | SC-5; **và thiết kế LORO của Paper 1** | Sổ ghi chép thí nghiệm |
| **OI-03** | NTU có quyền truy cập toàn văn ISO 19650-1/-2 không? | SC-3 GO-gate | Thư viện NTU hoặc mua trực tiếp |
| **OI-04** | Deadline chính thức của ba hội thảo | Toàn bộ lịch §13.2 | Trang web hội thảo |
| **OI-05** | Trường có yêu cầu thủ tục đạo đức/đồng ý tham gia cho khảo sát phỏng vấn không? | SC-6 | Phòng Quản lý Khoa học NTU |
| **OI-06** | Trạng thái xác minh văn bản pháp luật VN (`VN-LEGAL` vẫn `Unverified`) | SC-3, và bối cảnh Paper 2 | Cổng thông tin văn bản pháp luật chính thức |
| **OI-07** | Chính sách prior-conference-publication của *Sensors* | SC-1, SC-5, SC-8 | Trang Instructions for Authors |
| **OI-08** | ADR Action-Status-Event được chấp thuận hay bác | Ký hiệu `Status_Event_ID` trong mọi bài | Quyết định của thầy |

> **Evidence is currently insufficient** để khóa nội dung của bất kỳ bài SC nào cho tới khi các Open Item liên quan được giải quyết. Danh mục này là kho ý tưởng có kiểm soát, không phải cam kết xuất bản.
