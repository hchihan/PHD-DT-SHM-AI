# Paper 1 — Giải thích nghiên cứu (bản dễ hiểu cho người ngoài chuyên ngành AI)

**Ngày soạn:** 13/09/2026 · **Cập nhật v2:** 13/09/2026 (hiệu chỉnh kiến trúc RQ/WP/Paper/Gate và wording theo yêu cầu rà soát)
**Dùng cho:** đọc kèm bộ slide `PAPER1_SUPERVISOR_REPORT_DUT_TEMPLATE_v2.pptx`, hoặc đọc độc lập.
**Bản thảo tương ứng:** `PAPER1_v8.1_SHM_RISK_REDUCED.docx` — nộp tạp chí *Structural Health Monitoring* (SAGE).

```text
RQ: RQ1
WP: WP1
Chương: C4
Paper: Paper 1
Evidence Gate: G1
Scope: Core (laboratory evidence, run-aware evaluation, provenance) + Supporting (chiến lược tạp chí)
Evidence type: Laboratory evidence
```

**Gói bằng chứng Gate 1: sẵn sàng về mặt khoa học; chờ thầy rà soát và ký nghiệm thu chính thức.** Mọi con số phần trăm trong tài liệu này là kết quả ứng viên (candidate claim), thuộc gói bằng chứng đó — theo quy định của Charter luận án, chúng chỉ trở thành kết quả chính thức sau khi Gate 1 được ký nghiệm thu. Tài liệu này không tự đóng Gate nào; nó chỉ giải thích để thầy đọc và cho ý kiến.

---

## 1. Tóm tắt trong một câu

Paper 1 trả lời câu hỏi: *"Dữ liệu rung động đo được từ một khung thép thu nhỏ có phân biệt được các trạng thái liên kết bu lông khác nhau hay không, và độ tin cậy của kết quả phân biệt đó phụ thuộc vào điều gì?"* — chứ **không phải** câu hỏi "AI có phát hiện được hư hỏng thật ngoài công trình hay không".

---

## 2. Vì sao luận án cần một nghiên cứu như thế này

Một nhà xưởng khung thép ven biển, sau một thời gian sử dụng, có thể có bu lông bị lỏng ở một vài liên kết. Cách kiểm tra truyền thống là con người đi kiểm tra bằng mắt hoặc bằng tay, tốn thời gian và không thể làm liên tục. Ý tưởng của luận án là gắn cảm biến rung động lên công trình, để hệ thống có thể "nghe" xem kết cấu có gì thay đổi, rồi báo cho người quản lý biết chỗ nào cần kiểm tra.

Nhưng muốn dùng một kết quả phân loại (ví dụ: "liên kết này có thể đang lỏng") làm căn cứ cho quyết định kiểm tra, người đọc phải biết:

1. Kết quả đó đến từ cảm biến nào, đo lúc nào, trong điều kiện nào;
2. Kết quả đó đáng tin đến mức nào — có ổn định giữa các lần đo khác nhau không;
3. Kết quả đó có áp dụng được cho những tình huống nó *chưa từng thấy* hay không.

Ba câu hỏi này chính là nội dung của Paper 1. Nói cách khác, **Paper 1 không đi tìm một thuật toán AI tốt hơn**; nó đi tìm ra **những gì một kết quả phân loại cần phải mang theo** thì mới được xem là bằng chứng đáng tin — cái mà luận án gọi là **condition evidence** (bằng chứng về tình trạng kết cấu).

---

## 3. Trục nghiên cứu của toàn luận án — Paper 1 đứng ở đâu

Luận án đi theo một chuỗi năm bước, đã được hai thầy hướng dẫn thông qua:

```text
Dữ liệu rung động
→ Bằng chứng về thay đổi trạng thái (condition evidence)
→ Cấu kiện gắn với mô hình BIM
→ Hồ sơ kiểm tra
→ Hỗ trợ ra quyết định kiểm tra – bảo trì
```

- **Paper 1** (bài này) lo hai bước đầu tiên: tạo ra bằng chứng về trạng thái trong phòng thí nghiệm, và xác định bằng chứng đó có những giới hạn gì. Đầu ra của Paper 1 là **đầu vào** cho Paper 2 — Paper 1 không gánh câu hỏi nghiên cứu của RQ2.
- **Paper 2** lo việc nối bằng chứng đó với mô hình BIM (mô hình thông tin công trình — một dạng "bản vẽ số" ghi mọi cấu kiện của tòa nhà) và với hồ sơ kiểm tra, để mọi thứ đều truy vết được (biết cảnh báo này từ đâu ra, thuộc cấu kiện nào).
- **Paper 3** kiểm chứng khả thi triển khai khung này tại một công trình thật. Bằng chứng khả thi hiện trường ở mức tối thiểu là thành phần **bắt buộc** của luận án; việc có tách nội dung đó thành một bài báo riêng để công bố hay không chỉ là một **quyết định chiến lược công bố**, không phải một điều kiện của luận án.

Mỗi mắt xích trong chuỗi trên có một chuỗi định danh đi kèm — nghĩa là mỗi thứ đều có "mã số" để có thể truy ngược lại:

```text
Sensor_ID (mã cảm biến) → BIM_GUID (mã cấu kiện trong BIM)
→ Condition_Evidence_ID (mã bằng chứng trạng thái)
→ Inspection_Record_ID (mã hồ sơ kiểm tra) → Action_Status (trạng thái hành động)
```

Paper 1 chịu trách nhiệm cho nội dung đứng sau `Condition_Evidence_ID` — tức là, khi Paper 2 tạo ra một mã bằng chứng, Paper 1 cung cấp căn cứ thực nghiệm để xác định nó cần chứa những thông tin gì thì mới đáng tin.

**FEM** (mô hình phần tử hữu hạn — một cách mô phỏng kết cấu bằng máy tính) chỉ xuất hiện trong luận án như một mô hình tham khảo *chưa hiệu chuẩn*, dùng để minh họa vị trí cấu kiện, chứ không dùng để chẩn đoán hư hỏng hay tính độ cứng thật của liên kết. FEM không có RQ, WP, Chương, Paper hay Gate riêng.

---

## 4. Bảng thuật ngữ Anh–Việt (đọc trước khi qua các phần sau)

| Thuật ngữ tiếng Anh | Giải thích dễ hiểu |
|---|---|
| **Vibration-based** | Dựa trên dữ liệu rung động (đo bằng cảm biến gia tốc) |
| **Connection state / connection-state classification** | Trạng thái của một liên kết bu lông; việc phân loại xem liên kết đang ở trạng thái nào |
| **Condition evidence** | Bằng chứng về tình trạng kết cấu — kết quả phân loại, kèm theo mọi thông tin cần để hiểu nó đáng tin đến đâu |
| **Campaign** (đợt đo) | Một đợt thu thập dữ liệu trọn vẹn, thực hiện trong một ngày, với một cấu hình cảm biến cố định. Nghiên cứu này có 3 đợt đo, gọi là CP1, CP2, CP3 |
| **Run** | Một lần chạy thí nghiệm liên tục, trong đó lần lượt đo đủ 4 trạng thái liên kết bằng 3 kiểu rung kích thích. Mỗi đợt đo có 6 run |
| **Recording** | Một file ghi âm rung động, ứng với đúng một tổ hợp (trạng thái liên kết × kiểu rung kích thích) trong một run. Có 216 recording tất cả |
| **Window (cửa sổ tín hiệu)** | Một đoạn tín hiệu ngắn (ở đây là 4 giây, 400 mẫu) cắt ra từ một recording để đưa vào mô hình. Một recording dài được cắt thành nhiều window gối lên nhau |
| **Data leakage (rò rỉ dữ liệu)** | Nguy cơ khi dữ liệu "kiểm tra" (test) vô tình chứa thông tin gần giống dữ liệu "huấn luyện" (train), khiến kết quả trông tốt hơn thực tế |
| **Run-aware evaluation** | Cách đánh giá bảo đảm mọi window thuộc cùng một run phải nằm trọn ở một bên (huấn luyện, xác nhận, hoặc kiểm tra) — không được chia lẻ, để tránh nguy cơ rò rỉ dữ liệu |
| **Leave-one-run-out (LORO)** | Một cách kiểm tra: lần lượt để dành một run ra làm "run kiểm tra", các run còn lại dùng để huấn luyện; lặp lại cho đến khi mọi run đều từng được kiểm tra một lần |
| **Training / validation / test set** (tập huấn luyện / xác nhận / kiểm tra) | Ba phần tách biệt của dữ liệu: huấn luyện để mô hình học, xác nhận để chọn mô hình tốt nhất trong lúc huấn luyện, kiểm tra để đánh giá kết quả cuối cùng — không được để ba tập này lẫn vào nhau |
| **Feature-based model** (mô hình dựa trên đặc trưng) | Mô hình học máy dùng các con số được tính sẵn từ tín hiệu (ví dụ: độ lệch, tần số trội) làm đầu vào, thay vì đọc tín hiệu thô |
| **Random forest (RF)** | Một thuật toán học máy cổ điển, kết hợp nhiều "cây quyết định" đơn giản để ra một dự đoán chung |
| **Support vector machine (SVM)** | Một thuật toán học máy cổ điển khác, tìm ranh giới phân chia tốt nhất giữa các nhóm dữ liệu |
| **Deep learning (học sâu)** | Nhóm mô hình học máy dùng mạng nơ-ron nhiều lớp, tự học đặc trưng trực tiếp từ tín hiệu thô, không cần người tính sẵn đặc trưng |
| **1D-CNN** | Một mạng nơ-ron học sâu quét tín hiệu một chiều (theo thời gian) để tìm mẫu hình |
| **ResNet1D** | Một mạng nơ-ron học sâu khác, có thêm "đường tắt" giữa các lớp giúp huấn luyện các mạng sâu hơn ổn định hơn |
| **Hyperparameter (siêu tham số)** | Các lựa chọn thiết kế của mô hình học sâu (ví dụ: tốc độ học) phải chọn trước khi huấn luyện, không phải thứ mô hình tự học được |
| **Hyperparameter tuning / development** | Quá trình thử nhiều lựa chọn siêu tham số khác nhau để tìm ra bộ tốt nhất, thực hiện trước khi chạy đánh giá chính thức |
| **Checkpoint** | Bản lưu tạm thời của một mô hình học sâu tại một thời điểm huấn luyện, để sau này có thể lấy lại đúng bản mô hình tốt nhất |
| **Standardisation / StandardScaler** (chuẩn hóa) | Phép biến đổi đưa dữ liệu về cùng một thang đo (trừ trung bình, chia độ lệch chuẩn), giúp mô hình học ổn định hơn |
| **Macro-F1** | Một chỉ số đánh giá độ chính xác phân loại, tính trung bình đều cho cả 4 trạng thái (không thiên vị nhóm nào có nhiều mẫu hơn) |
| **Balanced accuracy** (độ chính xác cân bằng) | Độ chính xác tính theo cách đối xử công bằng với mọi nhóm, dù số lượng mẫu mỗi nhóm khác nhau |
| **SD_fold, SD_seed** | Độ lệch chuẩn (đo mức dao động) của kết quả — SD_fold đo dao động giữa các run kiểm tra khác nhau, SD_seed đo dao động giữa các lần chạy lại cùng mô hình với hạt giống ngẫu nhiên (seed) khác nhau |
| **Cross-campaign transfer** (chuyển giao giữa đợt đo) | Thử nghiệm: huấn luyện mô hình ở đợt đo này rồi đem áp dụng cho đợt đo khác, xem còn hoạt động tốt không |
| **Permutation test (kiểm định hoán vị)** | Một cách kiểm tra thống kê: xáo trộn ngẫu nhiên nhãn thật rất nhiều lần để xem kết quả quan sát được có khác biệt hẳn so với việc đoán mò hay không |
| **p-value** | Một con số cho biết kết quả quan sát được có thể chỉ là ngẫu nhiên hay không; càng nhỏ thì càng ít khả năng là ngẫu nhiên |
| **Provenance (nguồn gốc dữ liệu)** | Toàn bộ thông tin về xuất xứ của một dữ liệu: đo lúc nào, bằng thiết bị gì, trong điều kiện nào, ai xử lý |
| **Sensor configuration** (cấu hình cảm biến) | Số lượng và vị trí các cảm biến được lắp khi đo — ví dụ đợt đo đầu chỉ có 2 cảm biến, hai đợt sau có 3 |
| **CEI (Confidence/Evidence Indicator)** | Một cấu trúc metadata/evidence **đang được đề xuất cho giai đoạn tích hợp** (Paper 2), đi kèm mỗi bằng chứng trạng thái để ghi lại độ tin cậy của nó — **không phải** một điểm số (numerical score) đơn giản, **không phải** "mức độ hư hỏng" (damage severity) |
| **BIM (Building Information Modeling)** | Mô hình thông tin công trình — một mô hình số 3D chứa đầy đủ thông tin về từng cấu kiện của công trình (kích thước, vật liệu, vị trí…) |
| **GUID (Globally Unique Identifier)** | Mã định danh duy nhất toàn cục, dùng để chỉ đích danh một cấu kiện trong mô hình BIM mà không thể nhầm với cấu kiện khác |

---

## 5. Mô hình thí nghiệm

Vật thí nghiệm là một khung thép thu nhỏ theo tỉ lệ 1:10, mô phỏng hình dạng của một nhà xưởng công nghiệp một nhịp, làm từ tấm thép SS400 dày 2 mm. Khung dùng bu lông M3 ở một số liên kết, để có thể tháo và điều chỉnh, tạo ra bốn trạng thái liên kết khác nhau:

- **S0** — trạng thái tham chiếu (liên kết siết chặt bình thường);
- **B1** — liên kết ở đỉnh mái được thao tác có chủ đích;
- **B2** — liên kết dầm–cột được thao tác có chủ đích;
- **B3** — liên kết giằng được thao tác có chủ đích.

Quan trọng: **các nhãn S0/B1/B2/B3 chỉ là vị trí bị tác động**, không phải là thang đo mức độ hư hỏng nặng nhẹ. Mức độ điều chỉnh **không được định lượng bằng torque (lực siết) hay preload (lực căng trước)** của bu lông — không có số liệu về lực siết hay độ cứng liên kết nào được ghi lại trong hồ sơ thí nghiệm.

Để tạo dữ liệu, một máy rung (PASCO WA-9855) tạo ra rung động theo ba kiểu khác nhau (hai kiểu nhịp và một kiểu nhiễu trắng), còn ba cảm biến gia tốc không dây (PASCO PS-3223) ghi lại phản ứng của khung tại các vị trí gần đỉnh mái, dầm–cột và giằng, với tần số lấy mẫu 100 lần/giây.

---

## 6. Dữ liệu được tổ chức như thế nào

Dữ liệu chia thành bốn cấp, từ lớn đến nhỏ:

```text
3 đợt đo (campaign)
  → 18 run (mỗi đợt đo có 6 run)
    → 216 recording (mỗi run có 12 recording = 4 trạng thái × 3 kiểu rung)
      → 6.899 window (mỗi recording cắt ra nhiều đoạn tín hiệu 4 giây)
```

Ba đợt đo (CP1, CP2, CP3) được thực hiện vào ba ngày khác nhau, và **khác nhau ở một vài điểm quan trọng**:

- CP1 chỉ dùng 2 cảm biến; CP2 và CP3 dùng đủ 3 cảm biến;
- Thứ tự đo các trạng thái cũng khác nhau: ở CP1 và CP2, trạng thái tham chiếu S0 được đo *đầu tiên*; ở CP3, S0 lại được đo *cuối cùng* trong mỗi run.

Đây không phải là chi tiết vụn vặt. Bài báo xử lý những khác biệt này như một phần của dữ liệu cần công bố, vì chúng ảnh hưởng tới cách đọc kết quả (xem mục 9).

Một điểm được kiểm chứng kỹ: toàn bộ 216 recording có mã định danh duy nhất và có "dấu vân tay" số học (hash SHA-256) riêng, không trùng lặp, không bị lẫn dữ liệu nguồn giữa các đợt đo.

---

## 7. Vì sao không được chia dữ liệu ngẫu nhiên (vấn đề rò rỉ dữ liệu)

Đây là phần kỹ thuật quan trọng nhất để hiểu vì sao bài báo này có giá trị.

Một recording bị cắt thành nhiều window dài 4 giây, và các window liền kề nhau **chồng lấn tới 50%** dữ liệu (bước cắt chỉ bằng nửa độ dài window). Nếu ta xáo trộn ngẫu nhiên tất cả các window rồi chia ngẫu nhiên vào tập huấn luyện và tập kiểm tra, sẽ có **nguy cơ** hai window gần như giống hệt nhau — một cái ở tập huấn luyện, một cái ở tập kiểm tra — khiến mô hình "kiểm tra" thực ra đang được kiểm tra bằng dữ liệu nó gần như đã thấy rồi, và kết quả đo được có thể đẹp hơn thực tế. Đây chính là nguy cơ **rò rỉ dữ liệu (data leakage)**, một lỗi phổ biến và nghiêm trọng trong các nghiên cứu học máy áp dụng vào tín hiệu công trình.

Cách khắc phục mà Paper 1 áp dụng: chia dữ liệu theo **nguyên cả run**, không theo window. Nghĩa là mọi window thuộc cùng một run phải nằm trọn vẹn ở một phía — hoặc toàn bộ vào huấn luyện, hoặc toàn bộ vào xác nhận, hoặc toàn bộ vào kiểm tra — không bao giờ bị chia lẻ. Cách làm này gọi là **run-aware evaluation** (đánh giá có ý thức về đơn vị run), và khi lặp lại lần lượt để mỗi run một lần được dùng làm "run kiểm tra", nó được gọi là **leave-one-run-out (LORO)**.

**Cần nói rõ giới hạn của chính lập luận này:** Paper 1 áp dụng nguyên tắc chia theo đơn vị vật lý (physically grouped evaluation) cho chính dữ liệu khung thép bu lông này và báo cáo bằng chứng run-aware thu được — nhưng bài **không chạy một phép đối chứng chia ngẫu nhiên theo window trên chính dataset này**, nên **không đo lường được mức chênh lệch cụ thể** sẽ xảy ra nếu chia sai. Bằng chứng về *hướng* tác động (chia sai theo mẫu nhỏ lẻ thường làm kết quả báo cáo lạc quan hơn thực tế) đến từ các nghiên cứu khác trên dữ liệu chẩn đoán ổ lăn máy móc (Wheat 2024; Vieira 2026), không phải từ một phép đo trực tiếp trên chính dataset khung thép này.

Đây không phải là kỹ thuật do Paper 1 phát minh ra — nguyên tắc "chia theo đơn vị vật lý, không chia theo mẫu nhỏ lẻ" đã có trong nhiều nghiên cứu khác. Đóng góp của Paper 1 là **áp dụng đúng nguyên tắc đó cho loại dữ liệu rung động khung thép bu lông này và báo cáo đầy đủ bằng chứng run-aware thu được** — một điều mà các nghiên cứu trước đó về khung thép bu lông chưa trình bày rõ ràng cùng lúc với sổ đăng ký thu đo công khai.

---

## 8. Quy trình đánh giá được thiết kế ra sao

Trong mỗi đợt đo có 6 run. Ở mỗi lần thử: 4 run dùng để huấn luyện, 1 run dùng để xác nhận (giúp chọn thời điểm dừng huấn luyện tốt nhất), và 1 run còn lại dùng để kiểm tra. Toàn bộ 30 tổ hợp (xác nhận, kiểm tra) khác nhau đều được chạy, để mỗi run lần lượt đóng vai trò "run kiểm tra".

Việc chọn cấu hình mô hình tốt nhất trong mỗi lần thử **chỉ dựa vào kết quả trên tập xác nhận** — dữ liệu kiểm tra không hề được nhìn thấy trong quá trình chọn. Đội kiểm chứng độc lập đã chạy lại và tái lập đúng 192 lựa chọn đã được lưu, xác nhận quy tắc này được tuân thủ.

Kết quả cuối cùng của mỗi trạng thái không tính trên từng window riêng lẻ, mà **gộp xác suất của tất cả window trong một recording lại thành một dự đoán** cho cả recording đó. Đây gọi là chấm điểm theo recording — đơn vị chấm điểm khác với đơn vị chia dữ liệu (là run).

Ngoài đánh giá trong cùng đợt đo, bài báo còn có một thử nghiệm phụ, mang tính thăm dò: huấn luyện mô hình bằng dữ liệu của một đợt đo, rồi đem áp dụng cho *toàn bộ* đợt đo khác chưa từng thấy — gọi là **chuyển giao giữa đợt đo (cross-campaign transfer)**.

---

## 9. Bốn mô hình được dùng — và vì sao mô hình không phải là trọng tâm

Bài báo thử bốn mô hình học máy, chia thành hai nhóm:

- **Nhóm dựa trên đặc trưng (feature-based):** Random forest và SVM. Cả hai được tính toán từ 25 đặc trưng số học rút ra từ mỗi kênh tín hiệu (như độ lệch, tần số trội…), **không hề được tinh chỉnh** — dùng đúng một cấu hình cố định từ đầu đến cuối.
- **Nhóm học sâu (deep learning):** 1D-CNN và ResNet1D, học trực tiếp từ tín hiệu thô đã chuẩn hóa.

Điểm quan trọng cần thầy lưu ý: **siêu tham số của hai mô hình học sâu được chọn từ một giai đoạn thử nghiệm trước**, dùng 5 trong 6 run của mỗi đợt đo. Điều này có nghĩa là, trong 18 lần kiểm tra trong cùng đợt đo, có tới 15 lần mà "run kiểm tra" đã từng góp mặt trong giai đoạn chọn siêu tham số đó. Bài báo **công khai rõ điều này như một hạn chế**, chứ không giấu đi — và chính vì hạn chế này, **kết quả chính thức của bài dựa trên nhóm Random forest/SVM** (không bị ảnh hưởng bởi vấn đề trên), còn kết quả của hai mô hình học sâu chỉ mang tính tham khảo, đối chiếu.

Bốn mô hình được chọn để **đối chiếu hai cách tiếp cận khác nhau**, không phải để tìm ra "AI nào giỏi nhất". Không có kết luận nào trong bài nói rằng một họ mô hình vượt trội hơn họ kia một cách tổng quát.

---

## 10. Kết quả trong cùng đợt đo (kết quả ứng viên)

Khi huấn luyện và kiểm tra trong cùng một đợt đo:

- Ở **CP1 và CP2**, cả Random forest và SVM đạt Macro-F1 gần như tuyệt đối (1.000 và 0.986) — nghĩa là phân biệt đúng gần như toàn bộ các trạng thái liên kết.
- Ở **CP3**, kết quả thấp hơn rõ rệt: Random forest đạt 0.875, SVM chỉ đạt 0.690, và độ dao động giữa các run kiểm tra (SD_fold) lên tới 0.139 — nghĩa là kết quả thay đổi khá nhiều tùy vào run nào được chọn làm kiểm tra.

Hai mô hình học sâu (1D-CNN, ResNet1D) cho kết quả thấp hơn ở mọi đợt đo, phù hợp với hạn chế đã nêu ở mục 9.

**Vì sao CP3 lại yếu hơn?** Bài báo *ghi nhận* rằng CP3 có thứ tự đo trạng thái khác với hai đợt đo kia (S0 đo cuối cùng thay vì đầu tiên), nhưng **không kết luận đây là nguyên nhân** — vì có nhiều yếu tố khác nhau giữa các đợt đo cùng lúc, và không có phép đo lực siết bu lông hay độ cứng để tách bạch nguyên nhân thật sự. Đây là một ví dụ cụ thể cho nguyên tắc "không tuyên bố vượt quá bằng chứng có được" mà toàn bộ luận án tuân theo.

---

## 11. Kết quả chuyển giao giữa đợt đo — giới hạn quan trọng nhất

Đây là phần thể hiện rõ nhất *lý do khoa học* của bài báo.

Khi huấn luyện mô hình bằng dữ liệu của CP2 rồi đem áp dụng cho CP3 (và ngược lại), độ chính xác cân bằng chỉ đạt khoảng **0.227 đến 0.278** — rất gần với **0.25, tức là mức đoán ngẫu nhiên** cho bài toán có 4 lựa chọn. Kiểm định hoán vị (permutation test) cho thấy không có trường hợp nào đạt mức có ý nghĩa thống kê thông thường (p nhỏ nhất là 0.167, trong khi ngưỡng thường dùng là 0.05).

Nói cách khác: **trong phép thử thăm dò CP2↔CP3, hiệu năng phân biệt trạng thái không được duy trì khi chuyển sang đợt đo chưa từng thấy; kết quả hiện chưa thiết lập được khả năng chuyển giao (transfer) giữa hai đợt đo này.**

Cần nói rõ giới hạn của chính phép thử này (để không hiểu sai theo hướng ngược lại — tức không được đọc thành "mô hình mất hoàn toàn khả năng" hay "không thể chuyển giao được"): thử nghiệm này chỉ làm với hai mô hình học sâu (vốn đã có hạn chế về siêu tham số như mục 9), chỉ thử hai chiều (CP2↔CP3), CP1 chưa từng được thử làm nguồn hay đích chuyển giao, và giả định về tính hoán vị được (exchangeability) làm nền cho kiểm định thống kê trên chưa được chứng minh cho cấu trúc thu đo phân cấp của dữ liệu này. Vì vậy, kết luận đúng đắn là: **"chưa thiết lập được khả năng chuyển giao"**, chứ không phải "đã chứng minh là không thể chuyển giao".

---

## 12. Ý nghĩa khoa học — đóng góp thật sự của Paper 1 là gì

Đây là phần trả lời trực tiếp yêu cầu "làm rõ đóng góp cho luận văn".

**Claim (điều bài báo khẳng định):**
Việc một mô hình phân biệt tốt các trạng thái *trong cùng một bối cảnh thu đo* (cùng đợt đo, cùng cấu hình cảm biến, cùng quy trình) **không tự động có nghĩa là** kết quả đó là bằng chứng có thể chuyển giao sang bối cảnh khác. Ý nghĩa của một con số phần trăm chính xác phụ thuộc vào: đơn vị dùng để chia dữ liệu (run), giao thức đánh giá, cấu hình cảm biến, mức độ dao động quan sát được, và bối cảnh thu đo.

**Evidence (bằng chứng cho claim đó):**
- Trong cùng đợt đo: Macro-F1 gần như tuyệt đối (CP1, CP2) hoặc dao động mạnh (CP3, SD_fold tới 0.139).
- Chuyển giao giữa đợt đo: kết quả tụt xuống gần mức đoán ngẫu nhiên (0.227–0.278), dù dùng đúng dữ liệu, đúng khung thí nghiệm.
- Ba đợt đo khác nhau về cấu hình cảm biến và thứ tự đo trạng thái — là thông tin có thật, có thể ảnh hưởng tới kết quả, nhưng chưa tách bạch được nguyên nhân.

**Limitation (giới hạn):**
- Toàn bộ kết luận này giới hạn trong phạm vi thí nghiệm phòng thí nghiệm trên một mẫu khung 1:10 duy nhất, không suy ra được cho công trình thật.
- Hai mô hình học sâu có phụ thuộc vào giai đoạn chọn siêu tham số trước, nên phần kết quả của chúng cần đọc kèm hạn chế này.
- Chuyển giao chỉ thử được hai chiều trong ba đợt đo có thể có (CP1 chưa thử).
- Nguyên tắc "phân tách tốt trong cùng bối cảnh không đảm bảo chuyển giao được" *bản thân nó không phải phát hiện mới* trong lĩnh vực học máy nói chung — cái mới ở đây là **ghi nhận thực nghiệm cụ thể của nguyên tắc đó trên chính loại dữ liệu rung động khung thép bu lông**, kèm đầy đủ số liệu định lượng, mà theo rà soát tài liệu (Scopus, OpenAlex) thì chưa có nghiên cứu khung thép bu lông nào trước đây trình bày đầy đủ cùng lúc: sổ đăng ký thu đo công khai, chia dữ liệu đúng theo run, đánh giá dao động giữa các run, và một phép thử chuyển giao rõ ràng.

**Next action (bước tiếp theo, đưa luận án gần Gate 1 hơn):**
Hoàn thiện hồ sơ nghiệm thu Gate 1 (biên bản ký xác nhận sổ đăng ký run, quy trình chống rò rỉ, và bảng độ dao động giữa run/seed) để chuyển các con số ở trên từ "candidate claim" (kết quả ứng viên) sang kết quả chính thức có thể trích dẫn trong Chương 4 và Paper 2. Gói bằng chứng đã sẵn sàng về mặt khoa học cho bước này; phần còn thiếu là quy trình rà soát và ký nghiệm thu.

---

## 13. Vì sao đóng góp này quan trọng cho luận án nói chung

Luận án không đặt mục tiêu tạo ra một thuật toán AI tốt hơn để chẩn đoán hư hỏng. Mục tiêu của luận án là xây dựng một **khung thông tin có thể truy vết được**, giúp người quản lý công trình biện minh được cho quyết định kiểm tra của mình (đây gọi là *justification & accountability* — khả năng giải trình và truy trách nhiệm — vốn là lõi thuộc ngành Quản lý xây dựng, không phải ngành AI hay Cơ học).

Để một kết quả phân loại có thể trở thành một mắt xích đáng tin trong chuỗi đó (`Condition_Evidence_ID`), nó phải mang theo đầy đủ thông tin về nguồn gốc, giao thức đánh giá và giới hạn hiệu lực — nếu không, một cảnh báo "trông có vẻ chính xác" trong phòng thí nghiệm có thể bị hiểu nhầm là áp dụng được cho mọi tình huống, dẫn tới quyết định sai. Paper 1 chính là nơi cung cấp **căn cứ thực nghiệm** cho việc xác định những thông tin bắt buộc đó là gì, dựa trên bằng chứng cụ thể (mục 10–12) — còn việc hình thức hóa chúng thành schema chính thức cho `Condition_Evidence_ID` là công việc của Paper 2. CEI (chỉ số tin cậy/bằng chứng, đang được đề xuất cho giai đoạn tích hợp ở Paper 2) nhờ đó có nội dung thật để mô tả — một cấu trúc thông tin, không phải một điểm số đơn — thay vì là một khái niệm trừu tượng không có căn cứ.

---

## 14. Paper 1 không làm những gì (để tránh hiểu lầm phạm vi)

| Paper 1 **có** làm | Paper 1 **không** làm |
|---|---|
| Phân loại 4 trạng thái liên kết có kiểm soát trên khung 1:10 | Chẩn đoán hư hỏng thật tại công trình |
| Đánh giá theo đơn vị run, chấm điểm theo recording | Suy ra độ cứng liên kết hay lực siết bu lông |
| Báo cáo mức dao động giữa các run và các lần chạy | Xếp hạng mức độ hư hỏng (severity), tính tuổi thọ còn lại (RUL) |
| Thử chuyển giao giữa hai đợt đo (mang tính thăm dò) | Bảo trì dự đoán hoặc bảo trì tự động, không có người rà soát |
| Ghi lại đầy đủ nguồn gốc dữ liệu | Dùng mô hình FEM đã hiệu chuẩn để tính toán |
| | Đề xuất thuật toán hay phương pháp kiểm định hoàn toàn mới |
| | So sánh các cấu hình cảm biến khác nhau (thuộc một bài khác, Paper 1B) |

---

## 15. Vì sao chọn nộp tạp chí *Structural Health Monitoring* (SAGE)

Bài báo được rà soát trên hai công cụ tra cứu học thuật độc lập (Scopus và OpenAlex). Cả hai đều xếp *Structural Health Monitoring* là lựa chọn phù hợp nhất, vì ba lý do:

1. **Đúng phạm vi:** tạp chí này công bố nhiều nghiên cứu về giám sát dựa trên rung động và liên kết bu lông, đúng chủ đề của bài.
2. **Có tiền lệ về đúng loại lập luận mà bài này đưa ra:** tạp chí đã từng đăng các bài viết riêng về "chất lượng thông tin" của bằng chứng giám sát công trình (information quality) — rất gần với cách đặt vấn đề "bằng chứng cần đi kèm nguồn gốc" của Paper 1.
3. **Có đường xuất bản không mất phí bắt buộc** (không giống một số tạp chí cùng lĩnh vực bắt buộc phí xuất bản mở).

Rủi ro bị từ chối ngay từ vòng xét duyệt sơ bộ (desk-reject) được đánh giá ở mức **trung bình**; rủi ro lớn nhất có thể gặp là biên tập viên đọc bài như "chỉ là một điểm về quy trình đánh giá" — bài báo đã chủ động đưa lập luận đóng góp (mục 12) lên đầu phần giới thiệu và tóm tắt để giảm rủi ro này. Vòng nộp đầu tiên: *Structural Health Monitoring*; các tạp chí dự phòng theo thứ tự tham khảo: *Structural Control and Health Monitoring*, *Engineering Structures*, *ASCE-ASME JRUES-B*, *Journal of Civil Structural Health Monitoring*.

---

## 16. Tình trạng hiện tại và những việc cần thầy cho ý kiến

**Gói bằng chứng Gate 1: sẵn sàng về mặt khoa học; chờ thầy rà soát và ký nghiệm thu chính thức.**

Bản thảo hiện ở phiên bản **v8.1**, đã qua một vòng kiểm chứng độc lập từng con số so với dữ liệu gốc (mang tên nội bộ IT-01 đến IT-06), và một vòng rà soát giảm rủi ro nộp bài riêng cho tạp chí SHM. Về mặt khoa học, bản thảo **không còn vướng mắc**; các việc còn lại chủ yếu là thủ tục và các quyết định cần thầy:

**Việc tác giả tự hoàn thiện được:**
- Bổ sung email, mã ORCID, tên khoa/bộ môn vào trang bìa bài báo;
- Xác nhận lại tuyên bố tài trợ và xung đột lợi ích;
- Duyệt lại một hình minh họa vẽ tay (Hình 3) và tìm ảnh chụp gốc độ phân giải cao hơn cho một số hình;
- Soạn thư gửi ban biên tập (cover letter).

**Cần thầy cho ý kiến:**
- **Ký nghiệm thu Gate 1** trước khi cho phép nộp bài (đây là điều kiện bắt buộc theo quy định luận án — chưa có biên bản ký thì mọi con số vẫn chỉ là "candidate claim", dù gói bằng chứng đã sẵn sàng khoa học);
- Đồng ý chọn *Structural Health Monitoring* (SAGE) làm nơi nộp đầu tiên;
- Có nên chạy thêm một thử nghiệm bổ sung: dùng Random forest/SVM (hai mô hình *không* bị ảnh hưởng bởi vấn đề siêu tham số) để thử chuyển giao CP2↔CP3, nhằm củng cố thêm kết luận ở mục 11 hay không;
- Có nên công bố công khai bộ dữ liệu và mã nguồn kèm mã định danh DOI hay không (hiện dữ liệu và mã đã có đầy đủ ở dạng nội bộ, nhưng chưa công khai).

---

## 17. Đọc thêm

- Bản thảo đầy đủ: `PAPER1_v8.1_SHM_RISK_REDUCED.docx`
- Nhật ký chỉnh sửa từ v8 sang v8.1: `PAPER1_v8.1_SHM_CHANGELOG.md`
- Rà soát rủi ro trước khi nộp: `PAPER1_v8.1_SHM_PRE_SUBMISSION_AUDIT.md`
- Bộ slide trình bày: `PAPER1_SUPERVISOR_REPORT_DUT_TEMPLATE_v2.pptx`
- Nhật ký hiệu chỉnh v1 → v2 của bộ báo cáo: `PAPER1_SUPERVISOR_REPORT_v2_CHANGELOG.md`
