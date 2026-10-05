# R3 – Phản biện Paper 2 (MT2): Nguồn gốc dữ liệu, chất lượng thông tin (PROV-O, PAV, SOSA/SSN)

**Phản biện:** R3 (vai nguồn gốc, phạm vi hiệu lực, kiểm tại lần dùng). **Ngày:** 02/10/2026. **Pha:** 1.
**Ký hiệu:** [R3] = nhận định của phản biện. TG kèm trang chỉ dùng cho tiền lệ đã đọc toàn văn ([35], [44], [2]). Vị trí trong
hồ sơ ghi theo `tệp:dòng` (dòng của bản trong `src/`). Không thêm nguồn mới; chỗ cần nguồn ghi `[CẦN NGUỒN: …]`.
**Lớp 1** = thiết kế khóa (phuluc A–B, GD3b, CLAUDE.md §2/§8/§10, chương 5). **Lớp 2** = hồ sơ cũ (REFINED, gate2_3 v0.2,
giao diện G1→G2).

---

## 1. Tóm tắt nhận định

- [R3] Phần mới của Paper 2 theo góc nhìn nguồn gốc nằm ở **một chỗ hẹp**: phạm vi hiệu lực là thuộc tính của từng bằng chứng,
  có thành phần "đợt lắp đặt" mà giá trị đúng chỉ biết được tại lần dùng, và việc dùng được ghi thành quan hệ có thuộc tính
  (`EVIDENCE_USE`) để máy kiểm. PROV-O ghi được *ai/cái gì sinh ra* bằng chứng; SSN ghi được *cảm biến triển khai ở đâu, khi nào*;
  không cái nào (theo bảng A.3 của chính hồ sơ, `phuluc.md:93–102`) có hàng cho "phạm vi" hay "trong/ngoài phạm vi tại lần dùng".
- [R3] Nhưng như đang đặc tả, chỗ hẹp đó **chưa kiểm được bằng máy** và **suy biến trên chính tập dữ liệu dự kiến**:
  (i) vị từ `within_scope` (`phuluc.md:118`) thiếu nguồn dữ liệu, kiểu dữ liệu và logic khi thiếu giá trị;
  (ii) bằng chứng MT1 (khung 1:10) gắn vào cấu kiện nhà xưởng 1:1 thì `within_scope` luôn sai, nên nhóm lỗi C5 thu về
  phép kiểm "`justification` khác rỗng" – một ràng buộc NOT NULL, hiển nhiên thắng B0/B1;
  (iii) mốc đổi đợt lắp đặt đặt ở "Đã xác minh" (`phuluc.md:122`) làm C5 mù đúng ở bước xác minh sau sửa chữa;
  (iv) giao diện G1→G2 không sinh `install_batch`, `applicable_conditions` (Đ11).
- [R3] Bảng ánh xạ PROV-O/SOSA hiện ở mức khái niệm, có vài ánh xạ sai ngữ nghĩa và **không có hàng cho khái niệm trung tâm**;
  phản biện tạp chí sẽ coi là trang trí nếu giữ nguyên.
- **Khuyến nghị sơ bộ nếu nộp như dự kiến: major revision, nghiêng reject-resubmit** cho phần G-A/A2 của bài (M1, M2 là lỗi
  chặn). Phần G-B (C6) không thuộc vai này.

---

## 2. Major

### M1. Vị từ `within_scope` chưa đủ để máy kiểm (thiếu nguồn, kiểu, phép so, logic thiếu dữ liệu)

- **Vị trí:** `phuluc.md:118` (C5), `:122` (mốc đổi đợt), `:28` (4 trường scope), `:29`, `:61` (`obs_context`), `:47`
  (`EVIDENCE_USE`); `CLAUDE.md:345` (§8); `CLAUDE.md:435` (§10).
- **Vấn đề:** Vị từ có hai vế, cả hai không tính được trên 6 thực thể của Bảng A.1:
  1. "đợt lắp đặt hiện hành của cấu kiện tại `used_at`": `COMPONENT` chỉ có `BIM_GUID`, `model_version` (`phuluc.md:15–16`);
     không có trường đợt lắp đặt, `ACTION` không có trường loại hành động (siết lại, thay thế) để biết hành động nào là can
     thiệp lên liên kết. Kiểu của `scope.install_batch` cũng không rõ: A.3 định nghĩa nó là "khoảng thời gian kể từ lần lắp ráp
     hoặc lần can thiệp gần nhất" (`phuluc.md:57`), tức là một khoảng; B.1 so bằng phép "trùng" (`:118`), tức là một định danh.
  2. "điều kiện vận hành tại `used_at`": không thực thể nào chứa dữ liệu vận hành theo thời gian (nhật ký cầu trục, chuỗi nhiệt
     độ). `obs_context` là điều kiện **tại lần đo** của bằng chứng (`:61`), không phải tại lần dùng. Phép "nằm trong" cho điều
     kiện nhiều chiều (dải nhiệt độ liên tục, cờ cầu trục rời rạc, đo trên một khoảng thời gian chứ không phải một điểm) không
     được định nghĩa.
  3. Không nói khi thiếu giá trị (không có nhiệt độ, chưa có hồ sơ can thiệp) thì `within_scope` là gì. Logic hai trị sẽ ngầm
     coi "không biết" là đúng hoặc sai tùy cách viết truy vấn.
  4. `within_scope` "do công cụ tính" nhưng lại là thuộc tính lưu của `EVIDENCE_USE` (`:47`). Không có quy tắc so giá trị lưu với
     giá trị tính lại; một lỗi chèn kiểu "ghi `within_scope = true` cho một lần dùng thực ra ngoài phạm vi" sẽ lọt C5, vì C5 chỉ
     kiểm `justification` khi `within_scope` sai. Bản v0.2 cũ có đúng cơ chế này (`Scope_Snapshot` + R08b, `gate2_3_data_model_v0.2.md:180`).
- **Vì sao quan trọng với phản biện tạp chí:** Bài tuyên bố "kiểm được bằng máy" (`GD3b:77`, `05_chuong5.md:81`). Một phản
  biện tin học xây dựng sẽ yêu cầu đặc tả tái lập được của vị từ; nếu không có, toàn bộ M2 nhóm C5 không tái lập và không so
  được giữa B1 và mô hình đề xuất.
- **Yêu cầu sửa (kiểm được):**
  - Viết `within_scope` thành hàm `valid(E, c, t) → {TRUE, FALSE, UNKNOWN}` có pseudo-code hoặc SQL trong Phụ lục B, với
    nguồn dữ liệu của từng vế chỉ trỏ tới trường có trong Bảng A.1 (xem đề xuất ở mục 4(a), 4(b)).
  - Thêm một bảng (hoặc view suy ra) **đợt lắp đặt** theo cấu kiện: `(BIM_GUID, epoch_id, epoch_start, epoch_end,
    opened_by_Action_ID | initial_record_ref)`; thêm `ACTION.action_type` (kiểm tra / siết lại / thay thế / khác).
    Đây là chi tiết "cách ghi cụ thể được khóa cùng đặc tả Bài báo 2" (`phuluc.md:122`), không đổi số thực thể nếu để ở dạng
    view.
  - Định nghĩa kiểu của `applicable_conditions` và `obs_context` theo từng chiều (khoảng số có đơn vị, cận mở/đóng; tập giá trị
    rời rạc), và phép "nằm trong" từng chiều; `UNKNOWN` khi thiếu chiều, `UNKNOWN` xử lý như `FALSE` đối với C5 (bắt buộc lý do).
  - Thêm vế kiểm: giá trị `within_scope` lưu phải bằng giá trị tính lại; lệch là vi phạm C5.
- **Công sức:** M. **Mức:** **Chặn.**

### M2. Bằng chứng MT1 (1:10) dùng cho cấu kiện nhà xưởng (1:1) làm `within_scope` luôn sai: nhóm lỗi C5 suy biến

- **Vị trí:** `CLAUDE.md:83–86` (§2A: "Bài 2 … kiểm chứng bằng … dữ liệu MT1 (bằng chứng có phạm vi đã biết, dùng để chèn ca
  dùng ngoài phạm vi)"); `GD3b:139–140`, `:178–179`; `phuluc.md:118`, `:134`; `05_chuong5.md:243` (Lớp 3);
  `G1_TO_G2…:768` ("no quantitative laboratory result may be transferred directly to a field structure");
  `gate2_3_data_model_v0.2.md:154` (R09 cũ); tệp 00 §2 (khung 1:10 ↔ BIM 1:1 chỉ là tương ứng thông tin, Physical_Identity = FALSE).
- **Vấn đề:** `scope.install_batch` của bằng chứng phòng thí nghiệm là một lần lắp của khung 1:10; đợt lắp đặt hiện hành của cột
  nhà xưởng thuộc một không gian định danh khác, nên vế 1 của vị từ không bao giờ đúng. Vế 2 cũng không: dữ liệu phòng thí nghiệm
  không có cầu trục, nên `applicable_conditions` không chứa trạng thái "cầu trục chạy". Hệ quả:
  1. Mọi `EVIDENCE_USE` trỏ bằng chứng MT1 trên BIM nhà xưởng đều ngoài phạm vi **theo cấu tạo**. Lỗi chèn nhóm C5 chỉ còn một
     dạng: xóa `justification`. Phát hiện được bằng ràng buộc NOT NULL có điều kiện. Chênh lệch so với B0, B1 ("Không" ở
     `phuluc.md:134`) là hiển nhiên theo thiết kế, đúng loại lập luận mà chính hồ sơ đã tự loại cho M1 (`GD3b:160–161`).
  2. Không có ca "trong phạm vi" nào từ MT1, nên không đo được dương tính giả của phép tính `within_scope`, và không thử được hai
     thứ làm nên tính mới của A2: đổi đợt sau can thiệp, điều kiện vượt dải.
  3. Câu chuyện bài báo yếu: phản biện sẽ hỏi vì sao một kỹ sư lại dẫn kết quả khung 1:10 làm căn cứ kiểm tra một cột thật. Giao
     diện G1→G2 (`:768`) và luật R09 cũ cấm đúng việc này; thiết kế khóa thì biến việc bị cấm thành nguồn chính của ca lỗi.
- **Vì sao quan trọng:** Đây là nhóm lỗi trọng tâm của M2 (`CLAUDE.md` §8, "trọng tâm 'dùng bằng chứng ngoài phạm vi' (C5, C9)").
  Nếu nhóm này suy biến thành NOT NULL thì đóng góp phần G-A trong Paper 2 không còn được đo.
- **Yêu cầu sửa (kiểm được):**
  - Khai báo rõ trong bài: dùng bằng chứng 1:10 cho cấu kiện 1:1 là **ngoài phạm vi theo định nghĩa**; đây là một lớp ca, không
    phải toàn bộ nhóm C5.
  - Tạo tập bằng chứng mà `within_scope` **biến thiên thật**, ít nhất theo một trong hai cách (không cần dữ liệu mới):
    (a) **ngữ cảnh phòng thí nghiệm**: gắn bằng chứng MT1 vào cấu kiện của chính khung 1:10 (một mô hình thông tin của khung, có
    đợt lắp đặt = các lần lắp CP1–CP3), để một bằng chứng LORO của CP2 dùng trong CP2 là trong phạm vi, dùng ở CP3 là ngoài
    phạm vi; [NCS XÁC NHẬN] giữa các campaign có tháo – lắp lại hay không;
    (b) **ngữ cảnh nhà xưởng**: lập đợt lắp đặt của cấu kiện nhà xưởng từ lịch sử siết lại, thay thế trong hồ sơ B0 (20–30 hồ sơ
    thật), và tạo bằng chứng nhà xưởng tổng hợp có `obs_context`, `scope` khai báo trước, ghi rõ là tổng hợp.
  - Tách M2 nhóm C5 thành hai tầng và báo riêng: **C5-a** thiếu lý do (suy biến, chỉ mô tả); **C5-b** sai giá trị phạm vi (đổi
    đợt chưa ghi nhận, điều kiện vượt dải, `within_scope` lưu lệch giá trị tính). Chỉ C5-b được dùng làm căn cứ đóng góp so với B1.
- **Công sức:** M. **Mức:** **Chặn.**

### M3. "Phạm vi hiệu lực" có ba định nghĩa khác nhau và trộn hai mức bằng chứng; hai trường bắt buộc không tham gia phép kiểm

- **Vị trí:** `phuluc.md:28`, `:53–59` (4 trường, không có cấu hình cảm biến); `CLAUDE.md:435` (§10: 5 thành phần, có cấu hình
  cảm biến); `REFINED_v1.0_25092026.md:121` (đợt đo, cấu hình cảm biến, giao thức, đơn vị suy luận); `GD3b:124–125` và tệp 00
  1A-5 (chỉ `inference_unit`, `data_split`, `install_batch`, không có `applicable_conditions`); `phuluc.md:53–55` (`value` gồm
  "nhãn, xác suất lớp" – mức một dự đoán; `uncertainty` gồm "biến thiên theo seed và fold, kiểm định hoán vị" – mức quy trình);
  `G1_TO_G2…:182`, `:284` (bằng chứng chính thức ở mức lần chạy, một cấu kiện) so với tệp 00 R5 ("bản ghi EVIDENCE … của các
  kết quả R2–R4" – kết quả hiệu năng gộp).
- **Vấn đề:**
  1. Ba tập thành phần khác nhau cho cùng thuật ngữ; cấu hình cảm biến lúc là phạm vi (§10), lúc chỉ là bối cảnh (`obs_context`).
  2. Hồ sơ dùng một thực thể `EVIDENCE` cho hai loại nhận định khác nhau: (I) **bằng chứng mức quan sát** – một nhận định về
     cấu kiện c dựa trên một lần đo (nhãn của một lần chạy, điểm bất thường của Autoencoder trong một khoảng); (II) **bằng chứng
     mức phương pháp** – một nhận định về năng lực của quy trình (F1 dưới LORO, chênh lệch so với cùng lần chạy). Phạm vi của
     (II) là miền áp dụng của phương pháp; phạm vi của (I) gồm thêm "từ lần đo tới lần can thiệp kế tiếp". Bản v0.2 cũ tách hai
     mức này (`gate2_3_data_model_v0.2.md:142`, "mức 1 … Không được đọc như mức 2"); Bảng A.1 gộp lại.
  3. `inference_unit`, `data_split` bắt buộc (`phuluc.md:28`) nhưng không có trong vị từ C5 (`:118`). Một trường bắt buộc không
     tham gia phép kiểm nào chỉ được đo bằng M1 (đủ trường), tức là phần "hiển nhiên theo thiết kế".
- **Vì sao quan trọng:** Định nghĩa là đối tượng chính của A2. Phản biện sẽ chỉ ra ba định nghĩa trong cùng hồ sơ, và hỏi vì sao
  A1 (đánh giá theo đơn vị độc lập, phần sở hữu của 1A) lại không ảnh hưởng gì tới phép kiểm ở Paper 2. Nếu A1 và A2 không nối
  bằng một quy tắc máy kiểm, G-A trong Paper 2 chỉ còn là một danh sách trường.
- **Yêu cầu sửa (kiểm được):**
  - Chốt **một** định nghĩa vận hành (đề xuất ở mục 4(a)), dùng nhất quán ở §10, A.3, B.1 và bài báo.
  - Thêm `evidence_level ∈ {observation, method}` (hoặc tách hai `evidence_type`), và nói vị từ áp dụng thế nào cho từng mức.
  - Đưa `data_split` vào vị từ qua **mức khái quát đã kiểm** (same_run → không được dùng cho quan sát mới; LORO → chỉ trong cùng
    đợt lắp đặt; LOCO → được dùng qua các đợt thuộc tập đã kiểm). Đây là R07/R07b cũ (`gate2_3_data_model_v0.2.md:150–152`) viết
    lại theo trường mới. `inference_unit` dùng để xác định khoảng thời gian của nhận định và đơn vị của `uncertainty`; nếu không
    tham gia kiểm, chuyển khỏi `scope` sang nhóm nguồn gốc – độ bất định và ghi lý do.
  - Cấu hình cảm biến: hoặc thêm `scope.sensor_config` (so với `obs_context.sensor_config`), hoặc sửa §10. Không để hai nơi
    mâu thuẫn.
- **Công sức:** M. **Mức:** **Nặng** (chặn nếu không sửa cùng M1).

### M4. Kẽ hở giữa C5 và C9; mốc đổi đợt ở "Đã xác minh" làm C5 mù tại bước xác minh sau sửa chữa

- **Vị trí:** `phuluc.md:118` (C5 đánh giá tại `used_at`), `:120` (C9 chỉ dựa `revision_of`, `created_at`), `:122` (đợt đổi khi
  hành động can thiệp chuyển "Đã xác minh"), `:79–83` (Bảng A.2: bước "(tạo) → Mở" và "Hoàn thành → Đã xác minh" không đòi
  `EVIDENCE_USE`), `:101` (A.3 ánh xạ `prov:wasInvalidatedBy` nhưng Bảng A.1 không có trường thu hồi).
- **Vấn đề:** Chi tiết ở mục 4(e). Tóm tắt các kẽ hở:
  1. **Vòng lặp ở bước xác minh:** sau khi siết lại (Đang xử lý → Hoàn thành) và trước "Đã xác minh", đợt lắp đặt chưa đổi, nên
     bằng chứng đo **trước** can thiệp vẫn được tính là trong phạm vi khi bản ghi kiểm tra sau sửa chữa dẫn nó. Đúng tình huống
     mà G-B muốn chặn ("có bảo trì thì đã sửa", [35] tr. 10, TG) lại không bị C5 bắt.
  2. Hết phạm vi giữa `used_at` và `timestamp` của sự kiện: C5 đã đánh giá xong ở `used_at`, C9 chỉ xét thay thế bản ghi. Không
     ràng buộc nào bắt.
  3. Bằng chứng đã bị thay **trước** `used_at`: C5 không xét `revision_of`; C9 chỉ chạy khi có sự kiện trỏ tới lần dùng đó.
  4. Bằng chứng bị thu hồi mà không có bản thay: không có `revision_of`, C9 không thấy.
  5. `used_at` sớm hơn `EVIDENCE.created_at` (dùng một bằng chứng chưa tồn tại): không ràng buộc nào trong C1–C9 bắt.
- **Vì sao quan trọng:** C5 và C9 là hai ràng buộc mang phần "kiểm tại lần dùng". Một phản biện về nguồn gốc dữ liệu sẽ dựng
  đúng các ca thời gian này (chúng là ca biên kinh điển của dữ liệu song thời gian). Nếu bộ ~30 lỗi chèn do người thứ ba lập có
  các ca này, M2 sẽ báo bỏ sót; nếu không có, phản biện sẽ hỏi vì sao.
- **Yêu cầu sửa (kiểm được):**
  - Trong phạm vi khóa: ghi rõ năm kẽ hở trên vào phần giới hạn, hoặc đóng bằng chi tiết đặc tả: thêm vế "`used_at ≥
    EVIDENCE.created_at`" vào C1 hoặc C5; định nghĩa C9 xét cả bản thay có `created_at` trước `used_at`.
  - Ngoài phạm vi khóa (mục 6, P1–P3): dời mốc đổi đợt về thời điểm can thiệp xong; đánh giá vị từ phạm vi ở cả mỗi sự kiện có
    `evidence_ref`; thêm trường thu hồi.
  - Đưa các ca biên thời gian vào danh sách lỗi chèn như một lớp riêng, khóa trước khi đo.
- **Công sức:** S (ghi giới hạn) đến M (sửa ràng buộc). **Mức:** **Nặng.**

### M5. Mối nối 1A → Paper 2: giao diện G1→G2 không sinh được bản ghi `EVIDENCE` đủ trường; hai hồ sơ mâu thuẫn ở bốn điểm

- **Vị trí:** P2A_0 Đ11 (`P2A_0_kiem_toan_thu_muc_20261002.md:220`), D004 (`:187`); tệp 00 1A-5; `GD3b:124–125`;
  `G1_TO_G2…:182`, `:185`, `:284`, `:342`, `:352`, `:495`, `:561`; giao diện §15 (cờ đủ điều kiện đều `false`, dòng 14 sync note).
- **Vấn đề:** Chi tiết ở mục 4(c). Ngoài hai trường thiếu P2A_0 đã nêu (`install_batch`, `applicable_conditions`), còn:
  (i) 1A-5 và MT1(d) **không giao** `applicable_conditions`, nên lỗi không chỉ ở giao diện mà ở cả việc khóa của MT1;
  (ii) giao diện cấm danh sách GUID trong một trường và mặc định một cấu kiện mỗi bằng chứng (`:352`, `:495`), Bảng A.1 cho
  `BIM_GUID` một hoặc nhiều (`phuluc.md:23`), còn `scope.install_batch` là một giá trị – với bằng chứng nhiều cấu kiện thì đợt lắp
  đặt của cấu kiện nào?; (iii) giao diện buộc `uncertainty` thành cấu trúc CEI (`:342`), Bảng A.1 có một trường; (iv) giao diện
  có vòng đời `WITHDRAWN`, `REJECTED` (`:561`) mà Bảng A.1 không có, nên C9 không thấy thu hồi (M4.4).
  Thêm: G1 chưa ký, mọi bằng chứng 1A ở mức CANDIDATE (tệp 00 §2); bài phải nói Paper 2 dùng bằng chứng ứng viên.
- **Vì sao quan trọng:** CLAUDE.md §2A cho Paper 2 "không chờ quan trắc dài hạn" nhờ dữ liệu MT1. Nếu 1A không xuất được bản ghi
  đủ trường, Paper 2 sẽ tự điền `scope` khi chèn lỗi – tức là người thiết kế tạo cả phạm vi lẫn ca lỗi, đúng điều kiện mà v0.2
  cũ tự cảnh báo không được trích như kết quả (`gate2_3_data_model_v0.2.md` mục A.5, ghi chú ⚠️).
- **Yêu cầu sửa:** Thêm vào 1A-5 bộ trường xuất tối thiểu ở mục 4(c), ghi ai điền, khóa trước khi chèn lỗi; sửa giao diện G1→G2
  (bản v1.2) hoặc ghi rõ Bảng A.1 thay giao diện ở các điểm (ii)–(iv).
- **Công sức:** M. **Mức:** **Nặng** (chặn nhóm C5-b nếu không có).

### M6. Bảng A.3 (PROV-O/SOSA) ở mức khái niệm, có ánh xạ sai ngữ nghĩa, không có hàng cho "phạm vi"; C9 trùng một ràng buộc thứ tự đã có của PROV

- **Vị trí:** `phuluc.md:89–104`; `CLAUDE.md:359`; `GD3b:150`; `05_chuong5.md:327` (5.8.2); REFINED `:80`, `:491` (PAV).
- **Vấn đề:** Chi tiết ở mục 4(d). Các lỗi cụ thể: không có hàng cho `scope`, `within_scope`, `justification`, `obs_context`;
  `sosa:hasFeatureOfInterest` gán cho bằng chứng, trong khi bằng chứng mức phương pháp (M3) không phải một quan sát;
  `INSPECTION_RECORD` (bản ghi) bị ánh xạ như một hoạt động; `EVIDENCE_USE` có thuộc tính nhưng bảng không dùng mẫu
  quan hệ có định danh của PROV (qualified usage) [CẦN NGUỒN: W3C PROV-O, mục qualified terms]; `actor_role` không ánh xạ
  sang vai trò trong liên kết tác nhân của PROV; PAV có trong hồ sơ cũ nhưng bị bỏ không có lý do. Ngoài ra, PROV có ràng buộc
  thứ tự "dùng trước khi bị vô hiệu" [CẦN NGUỒN: W3C PROV-CONSTRAINTS, ràng buộc thứ tự sự kiện]; C9 gần với ràng buộc đó, nên
  nếu không nêu, phản biện sẽ coi C9 là tái phát minh.
- **Vì sao quan trọng:** Tạp chí hạng cao trong lĩnh vực này đọc nhiều bài dùng PROV/SSN; một bảng không có hệ quả nào lên
  thiết kế và có sai ngữ nghĩa sẽ làm giảm tin cậy của cả phần mô hình.
- **Yêu cầu sửa:** Chuyển thành bảng mức trường (mỗi trường Bảng A.1 một hàng), có cột **loại khớp** (tương đương / gần /
  rộng hơn / không có tương đương); ghi rõ các hàng "không có tương đương" là phần mới; ghi ràng buộc nào tương ứng ràng buộc có
  sẵn của PROV/SSN và ràng buộc nào không (C3 ↔ khoảng triển khai; C9 ↔ thứ tự sử dụng – vô hiệu; C5 không có). Không cần
  RDF. Chi tiết ở mục 4(d).
- **Công sức:** S–M. **Mức:** **Nặng.**

### M7. Đối chứng B1 trên chiều phạm vi – phiên bản: "Không" ở Bảng B.2 cho C5, C9 cần lý do chính xác, nếu không B1 bị dựng yếu

- **Vị trí:** `phuluc.md:134`, `:136`; `CLAUDE.md` §8 (B1 "tắt các ràng buộc C5, C6, C9 và các trường mới"); `bellon2025.md:19`
  và `NUTL57KJ.md:62–64` ([35] tr. 9–10, TG: bản ghi hư hỏng mới nhất là `ACTIVE`, bản trước `OUTDATED`; sau bảo trì, mọi hư
  hỏng báo trước đó đặt `REPAIRED`; tác giả gọi là quy ước đơn giản hóa).
- **Vấn đề:** [R3] Hai quy ước của [35] là dạng thô của đúng hai chiều mà C9 và C5 kiểm: `OUTDATED` ≈ bản ghi đã bị thay;
  `REPAIRED` sau bảo trì ≈ hết hiệu lực do can thiệp (đổi đợt). B1 dựng "bám sát [35]" (`GD3b:324`) sẽ có hai trạng thái
  này. Vậy B1 có trường để kiểm **một phần**: gán một hư hỏng `OUTDATED`/`REPAIRED` vào nhiệm vụ bảo trì mới (qua
  `IfcRelAssignsToProcess`). Lý do B1 thật sự không kiểm được C9 là sự kiện BCF không ghi căn cứ (`GD3b:94`), nên không nối
  được bước chuyển với bản ghi đã dùng; lý do B1 không kiểm được C5 là không có điều kiện áp dụng và không có quan hệ dùng có
  thuộc tính. Bảng B.2 hiện chỉ ghi "Không", không ghi lý do này.
- **Vì sao quan trọng:** Phần quy cho đóng góp là chênh lệch so với B1 (`05_chuong5.md:336`). Nếu phản biện thấy B1 bị tắt mất
  `ACTIVE/OUTDATED/REPAIRED` của [35], chênh lệch M2 nhóm C5/C9 sẽ bị coi là do B1 dựng yếu.
- **Yêu cầu sửa:** Trong đặc tả B1 (khóa trước khi đo), giữ `ACTIVE/OUTDATED/REPAIRED` theo [35] tr. 9–10 và viết truy vấn B1
  tương ứng; đổi ô Bảng B.2 thành "Một phần (hư hỏng OUTDATED/REPAIRED theo quy ước [35]; không nối được bước chuyển với căn cứ)"
  nếu đúng; báo M2 của B1 trên các lỗi này thay vì ghi 0 theo thiết kế. (Phối hợp với R1 – vai đối chứng.)
- **Công sức:** S. **Mức:** **Nặng.**

---

## 3. Minor

- **m1. Va chạm thuật ngữ "đợt".** "Đợt" là campaign trong A1 (LOCO = "giữ lại cả đợt", `CLAUDE.md:35`; "giữ lại đợt", `CLAUDE.md:63`) và là
  install batch trong A2 ("đợt lắp đặt", `phuluc.md:57`, `:118`). Một campaign có thể gồm nhiều lần lắp, một lần lắp có thể kéo
  qua nhiều campaign. *Sửa:* tiếng Anh dùng *assembly epoch* (hoặc *installation epoch*) cho `install_batch`, giữ *campaign* cho
  đợt thí nghiệm; tiếng Việt dùng "giai đoạn lắp đặt". Công sức S. Mức Nặng về đọc hiểu.
- **m2. `obs_context` trộn định danh và điều kiện.** Đợt đo, khoảng thời gian (định danh, thời gian) nằm chung với nhiệt độ, cờ
  cầu trục (điều kiện) (`phuluc.md:29`). *Sửa:* tách `obs_interval` [start, end) và `obs_conditions` (theo kiểu ở mục 4(b)(iii));
  đơn vị và cách tóm tắt trên khoảng (min/max hay toàn bộ mẫu). S.
- **m3. Thứ tự thời gian tối thiểu chưa có.** `EVIDENCE.created_at ≥ obs_interval.end` (giao diện `G1_TO_G2…` §7.7 có quy tắc
  này) và `EVIDENCE_USE.used_at ≥ EVIDENCE.created_at`; quan hệ giữa `used_at` và `INSPECTION_RECORD.inspected_at` chưa định
  nghĩa (bằng nhau? `used_at ≤ inspected_at`?). S.
- **m4. `justification` là văn bản tự do.** Chuỗi "ok" thỏa C5. *Sửa:* mã lý do từ danh mục đóng (ví dụ: đã kiểm tra trực tiếp sau
  can thiệp; dùng làm thông tin phụ; chấp nhận rủi ro có phê duyệt) + tham chiếu bắt buộc theo mã; ghi rõ trong bài rằng C5 chỉ kiểm
  *có giải trình*, không kiểm *giải trình đúng*; đưa ca "lý do giả" vào danh sách lỗi như ca đối chứng âm (dự kiến bỏ sót, báo cáo).
  Theo REFINED `:281`, hồ sơ cũ đã tự nêu giới hạn tương tự ("không kiểm tra được phạm vi có đúng về mặt khoa học"). S.
- **m5. Nhóm lỗi C5/C9 được gộp ở một nơi, tách ở nơi khác.** `CLAUDE.md` §8 (M2: "trọng tâm 'dùng ngoài phạm vi' (C5, C9)") so với
  Bảng B.2 (hai nhóm riêng, `phuluc.md:134`, `:136`). *Sửa:* chốt quy tắc gán một lỗi chèn vào đúng một nhóm (theo nguyên nhân chèn),
  và quy tắc khi một lỗi kích cả C5 lẫn C9 (xem 4(e)). S.
- **m6. Bằng chứng nhiều cấu kiện với một `install_batch`.** `BIM_GUID` n:m (`phuluc.md:23`) nhưng scope một giá trị. *Sửa:*
  phạm vi theo cặp (bằng chứng, cấu kiện), hoặc giới hạn bằng chứng mức quan sát vào một cấu kiện như giao diện G1→G2 (`:352`). S.
- **m7. Nguồn của SSN vẫn treo.** `ssn-system:Condition` và `ssn:Deployment` đều `[CẦN NGUỒN: Khuyến nghị W3C SSN]`
  (`05_chuong5.md:79`, `phuluc.md:95–96`, `:142`); GD3b F-3 đã ghi. Không thể nộp với ô treo này. S.
- **m8. Phiên bản bộ luật ưu tiên.** A.4 yêu cầu bộ luật bốn mức có phiên bản (`phuluc.md:87`) nhưng Bảng A.1 không có trường
  `rule_version` trên `ACTION`. Cùng kiểu với `method_version`; thiếu thì không truy được mức ưu tiên về luật đã áp (V4). S.

---

## 4. Trả lời các câu hỏi bắt buộc

### (a) "Phạm vi hiệu lực" khác "phiên bản" và "điều kiện SSN" ở điểm nào; định nghĩa vận hành

**So sánh** ([R3], dựa trên cách hồ sơ mô tả; mô tả SSN lấy từ `05_chuong5.md:79` và `phuluc.md:96`, chưa đối chiếu khuyến nghị
W3C – `[CẦN NGUỒN: W3C SSN, mục System Capabilities và Deployment]`):

| Khái niệm | Thuộc tính của cái gì | Trả lời câu hỏi nào | Khi nào đổi | Hệ quả khi đổi |
|---|---|---|---|---|
| `method_version` (git commit) | Quy trình sinh bằng chứng | "Cái gì đã tính ra giá trị này?" | Khi mã/cấu hình đổi | Bằng chứng mới là một thực thể khác; bằng chứng cũ **không** mất hiệu lực vì có phiên bản mới |
| `model_version` (BIM) | Ngữ cảnh định danh của `BIM_GUID` | "GUID này đọc theo mô hình nào?" | Khi mô hình BIM được sửa, xuất lại | Ảnh hưởng định danh (C1, C3), không ảnh hưởng tính đúng của bằng chứng. REFINED `:90` đã nêu đúng điều này |
| `revision_of` | Quan hệ giữa hai **bản ghi** | "Bản ghi nào là phát biểu có thẩm quyền hiện thời?" | Khi bản ghi được sửa (sai số, nhầm trường, tính lại) | Bản cũ bị thay; đó là thay đổi về **tri thức về** cấu kiện, không phải về cấu kiện |
| `ssn-system:Condition` | Năng lực đo của **cảm biến/hệ đo** (theo hồ sơ mô tả) | "Trong điều kiện môi trường nào độ chính xác danh định của cảm biến còn giữ?" | Gần như cố định theo loại thiết bị | Nói về chất lượng phép đo, không nói gì về lần lắp ráp của **kết cấu** hay về một nhận định cụ thể |
| `ssn:Deployment` + khoảng thời gian | Quan hệ cảm biến – nền tảng | "Cảm biến S ở cấu kiện nào, từ khi nào đến khi nào?" | Khi dời, thay cảm biến | Hiệu lực của **ánh xạ** (C3); bằng chứng không nhất thiết hết hiệu lực khi cảm biến dời đi |
| **Phạm vi hiệu lực** | Một **nhận định** (bản ghi bằng chứng) về một đối tượng quan tâm | "Nhận định này còn được dùng làm căn cứ cho cấu kiện c tại thời điểm t không?" | Không đổi trên bản ghi; **trạng thái của thế giới** đổi (can thiệp lên liên kết, điều kiện vận hành khác) | Bản ghi vẫn đúng như một ghi nhận về quá khứ, nhưng không còn là căn cứ cho hiện tại |

Ba điểm khác biệt cốt lõi [R3]:
1. **Đối tượng:** phiên bản và `revision_of` nói về bản ghi hoặc quy trình; điều kiện SSN nói về thiết bị đo; phạm vi nói về
   quan hệ giữa *một nhận định* và *trạng thái của đối tượng được nhận định*.
2. **Thời điểm có đủ thông tin để kiểm:** phiên bản, điều kiện SSN, khoảng triển khai biết được lúc tạo bản ghi; thành phần
   "giai đoạn lắp đặt" của phạm vi chỉ biết được tại lần dùng, vì can thiệp xảy ra sau khi bằng chứng đã tạo. Đây là lý do
   "kiểm tại lần dùng" là cần (GD3b `:76`: hiệu lực sau can thiệp có lúc mất, có lúc giữ, [18], Maes 2022, [48] – TG theo GD3b).
3. **Chiều tri thức:** phạm vi có một thành phần về **mức khái quát đã được kiểm** (`data_split`: cùng lần chạy / LORO / LOCO), tức
   là A1. Phiên bản và điều kiện SSN không có chiều này.

Hệ quả cho thiết kế [R3]: hết phạm vi **không** được ghi bằng `revision_of`. Nếu sau một lần siết lại người dùng tạo bản sửa của
bằng chứng cũ để "đánh dấu hết hạn", C9 sẽ bắt nhầm và lịch sử bị sai nghĩa (bản cũ không sai, chỉ hết áp dụng).

**Định nghĩa vận hành đề xuất cho bài báo** (đặt ở mục Methods; tiếng Anh ở mục 7):

> Cho bằng chứng E có `evidence_level` ∈ {observation, method}, cấu kiện c ∈ `E.BIM_GUID`, thời điểm dùng t. Phạm vi của E là bộ
> S(E) = ⟨u, d, b, A, k⟩:
> - u = `inference_unit` (recording | run | assembly | campaign | field_window);
> - d = `data_split` ∈ {same_run, LORO, LOCO, field_baseline}, xác định **mức khái quát đã kiểm** G(d): same_run → không áp
>   dụng cho quan sát mới; LORO → trong cùng giai đoạn lắp đặt; LOCO → qua các giai đoạn lắp đặt thuộc tập đã kiểm;
>   field_baseline → trong giai đoạn lắp đặt của đường cơ sở;
> - b = `install_batch`: định danh giai đoạn lắp đặt (epoch) mà quan sát của E thuộc về (mức quan sát), hoặc tập epoch có trong
>   dữ liệu huấn luyện – đánh giá (mức phương pháp);
> - A = `applicable_conditions`: tích Descartes của ràng buộc theo từng chiều (khoảng số có đơn vị; tập giá trị rời rạc), lấy từ
>   dải có trong dữ liệu tạo ra E;
> - k = cấu hình cảm biến (S12, S123, …).
>
> E **trong phạm vi** cho c tại t, ký hiệu valid(E, c, t), khi và chỉ khi:
> (1) **giai đoạn:** epoch(c, t) = epoch(c, E.obs_interval) **và** epoch(c, E.obs_interval) được G(d) cho phép theo b;
> (2) **điều kiện:** E.obs_conditions ⊆ A theo từng chiều;
> (3) **cấu hình:** E.obs_context.sensor_config ∈ k;
> (4) **bản ghi:** E chưa bị thay hoặc thu hồi trước t.
> Mỗi vế trả TRUE, FALSE hoặc UNKNOWN (thiếu dữ liệu); valid = TRUE chỉ khi cả bốn vế TRUE. Vế (4) là C9, các vế (1)–(3) là C5.
> Với bằng chứng mức phương pháp dùng để biện minh cho một bằng chứng mức quan sát O, các vế (1)–(3) áp cho O thay cho E.

Điểm cần NCS quyết khi chốt: vế (4) có gộp vào cùng hàm không (mục 6, P2), và mức khái quát G của LOCO trên ba campaign là
gì khi [NCS XÁC NHẬN] giữa các campaign có tháo – lắp hay không.

### (b) Bảng B.1 đã đủ để máy kiểm chưa? Các lỗ

**Kết luận: chưa** (M1). Từng lỗ:

**(i) `inference_unit`, `data_split` có tham gia không – nếu không thì vì sao bắt buộc.**
Không tham gia (`phuluc.md:118`). [R3] Hai trường này là chỗ nối A1 (đánh giá theo đơn vị độc lập, sở hữu của 1A) với A2
(khai báo, kiểm tại lần dùng). Bỏ khỏi vị từ thì:
- một bằng chứng sinh dưới chia **cùng lần chạy** (đúng cách đánh giá A1 chỉ ra là lạc quan) vẫn được tính trong phạm vi nếu
  trùng giai đoạn lắp đặt và điều kiện; tức là Paper 2 không phân biệt bằng chứng rò rỉ với bằng chứng LORO/LOCO;
- hai trường chỉ được đo bằng M1 (đủ trường), là phần chính hồ sơ đã gọi là hiển nhiên (`GD3b:160–161`).
*Đề xuất:* đưa `data_split` vào vế (1) qua G(d) như định nghĩa ở 4(a) (đây là R07/R07b của v0.2 viết lại); `inference_unit` xác
định khoảng thời gian của nhận định (để tính epoch(c, E.obs_interval)) và đơn vị của `uncertainty`. Nếu NCS không muốn mở rộng
vị từ, thì phải chuyển hai trường khỏi nhóm "scope" sang nhóm nguồn gốc – độ bất định và nói rõ trong bài.

**(ii) "Điều kiện vận hành tại `used_at`" lấy từ đâu.**
Không từ đâu cả trong 6 thực thể. Có ba cách đọc, và chỉ một cách đúng nghĩa:
- *Dữ liệu vận hành tại `used_at`* (nhiệt độ, cầu trục lúc kỹ sư mở hồ sơ): cần một thực thể chuỗi vận hành không có trong
  schema; và [R3] **không liên quan** tới tính đúng của bằng chứng: điều kiện lúc người đọc dùng không làm đổi điều đã đo.
- *`obs_context` của một bằng chứng khác gần `used_at`*: phụ thuộc có bằng chứng khác hay không; không xác định.
- *`obs_context` của chính quan sát mà E dựa vào*, so với `applicable_conditions` (dải của dữ liệu tạo ra phương pháp/đường cơ
  sở, `phuluc.md:59`): đúng nghĩa. Vế này kiểm được ngay lúc tạo E, nhưng vẫn nên tính lại tại lần dùng vì đường cơ sở có thể
  được học lại (phiên bản phương pháp mới, dải mới).
*Đề xuất:* sửa chữ "điều kiện vận hành tại `used_at`" thành "điều kiện trong `obs_context` của quan sát mà bằng chứng dựa vào".
Phần "tại lần dùng" của vị từ do vế giai đoạn lắp đặt gánh.

**(iii) Kiểu dữ liệu và phép "nằm trong" cho điều kiện nhiều chiều.**
Chưa có. Đề xuất tối thiểu:
- `applicable_conditions`: danh sách ràng buộc theo chiều, mỗi phần tử `{dim, kind ∈ {interval, set}, unit, lo, hi, lo_closed,
  hi_closed}` hoặc `{dim, kind: set, values}`. Ví dụ: `temperature_C ∈ [18, 34]`, `crane_state ∈ {stopped, running}`.
- `obs_conditions`: cùng chiều, tóm tắt trên `obs_interval`: khoảng [min, max] cho chiều số, tập giá trị đã xuất hiện cho chiều
  rời rạc (một khoảng đo có thể có cả "chạy" và "dừng").
- Phép "nằm trong" theo chiều: khoảng quan sát ⊆ khoảng cho phép; tập quan sát ⊆ tập cho phép. Chiều có trong A mà thiếu trong
  quan sát → UNKNOWN. Chiều có trong quan sát mà A không ràng buộc → không xét (ghi rõ).
- Giới hạn cần ghi: hộp chữ nhật theo từng chiều **chứa nhiều hơn** vùng dữ liệu thật đã có (ví dụ đường cơ sở chỉ có cầu trục
  chạy ở 25–30 °C, nhưng hộp nhận cả cầu trục chạy ở 18 °C). Hoặc dùng ô rời rạc hóa kết hợp (nhiệt độ theo bậc × trạng thái cầu
  trục, chỉ ô có dữ liệu mới thuộc A), hoặc ghi giới hạn. Với bù EOV bằng hồi quy nhiệt độ và cờ cầu trục (`CLAUDE.md:37–39`),
  A phải là dải của dữ liệu fit hồi quy.

**(iv) "Đợt lắp đặt hiện hành" đổi khi nào và ai ghi.**
B.1 ghi: đổi khi hành động can thiệp lên liên kết chuyển "Đã xác minh"; cách ghi khóa cùng đặc tả (`phuluc.md:122`). Lỗ:
- **Không có trường để biết hành động nào là can thiệp** (`ACTION` không có loại) và **không có nơi lưu epoch** (M1).
- **Sai mốc thời gian:** thay đổi vật lý xảy ra lúc làm (Đang xử lý → Hoàn thành), không phải lúc xác minh. Trong khoảng giữa,
  bằng chứng trước can thiệp vẫn "trong phạm vi" – kể cả khi bản ghi kiểm tra sau sửa chữa dẫn nó để xác minh (M4.1). Nếu xác minh
  "chưa đạt" (Hoàn thành → Mở, `phuluc.md:83`) thì epoch không bao giờ đổi, dù liên kết đã bị siết lại.
- **Can thiệp ngoài luồng ACTION** (sửa chữa khẩn, nhà thầu khác, va chạm cầu trục, lắp ráp ban đầu, các lần siết trước khi có
  hệ thống) không tạo epoch. Cần epoch khởi đầu lập từ hồ sơ (B0, hồ sơ hoàn công) với `initial_record_ref`.
- **Thời gian giao dịch và thời gian hiệu lực:** nếu can thiệp được ghi muộn, kết quả `within_scope` của một lần dùng đã qua sẽ
  đổi khi tính lại. Cần nói C5 đánh giá "theo thông tin có tại `used_at`" hay "theo thông tin hiện có"; đề xuất báo cả hai và
  đưa ca "can thiệp ghi muộn" vào lỗi chèn.
- **Ai ghi:** người thực hiện ghi thời điểm làm xong (vai trò ở Bảng A.2 bước Đang xử lý → Hoàn thành); kỹ sư kiểm tra xác nhận khi
  xác minh. Epoch nên mở theo thời điểm làm xong; xác minh chỉ xác nhận, không mở (mục 6, P1).
- **Phạm vi không gian:** can thiệp lên một liên kết của cấu kiện có làm đổi epoch của cả cấu kiện không, và của cấu kiện liền kề
  không? Cần quy tắc (đề xuất tối thiểu: cấu kiện được can thiệp; ghi giới hạn cho cấu kiện liền kề).

**(v) Bằng chứng phòng thí nghiệm 1:10 dùng cho cấu kiện nhà xưởng 1:1: `within_scope` luôn sai?**
**Có, theo đúng định nghĩa B.1** (M2): epoch của khung 1:10 không thể trùng epoch của cột nhà xưởng; dải điều kiện phòng thí
nghiệm không có cầu trục. Hệ quả:
- Cho nhóm lỗi "dùng ngoài phạm vi": mọi ca từ MT1 chỉ còn dạng "thiếu lý do"; M2 nhóm C5 thành phép kiểm NOT NULL, B0/B1 = 0 theo
  thiết kế, mô hình đề xuất = 100% theo thiết kế. Không đo được dương tính giả, không thử được đổi epoch và vượt dải.
- Cho câu chuyện bài báo: kịch bản "kỹ sư dẫn kết quả 1:10 làm căn cứ cho cột C3" mâu thuẫn với giao diện G1→G2 (`:768`), với R09
  cũ, và với Lớp 3 của chính chương 5 ("chỉ được dùng ở lớp này sau khi kiểm tra phạm vi hiệu lực", `05_chuong5.md:243`) – mà
  kiểm đó luôn cho sai. Phản biện sẽ hỏi điều gì trong bài cho thấy một lần dùng **trong** phạm vi.
- Hướng sửa (chi tiết ở M2): hai ngữ cảnh có epoch biến thiên thật – ngữ cảnh khung 1:10 (epoch = lần lắp CP1–CP3) và ngữ cảnh
  nhà xưởng (epoch lập từ lịch sử can thiệp trong B0); tách C5-a/C5-b khi báo M2. Câu chuyện bài báo đổi thành: "lab-to-field use
  is out of scope by construction and must be justified; the model detects scope changes *within* a context, which is where
  undetected misuse occurs."

### (c) Mối nối 1A → Paper 2: trường còn thiếu và bộ trường tối thiểu 1A phải xuất

**Đối chiếu** (Bảng A.1 cần – giao diện G1→G2 có – 1A-5/MT1(d) giao):

| Trường Paper 2 cần (Bảng A.1) | Giao diện G1→G2 | 1A-5 / MT1(d) | Khoảng hở |
|---|---|---|---|
| `scope.install_batch` | Không có. Có `Run_ID`, `Campaign_ID`; `Assembly_ID` chưa có (D004 BLOCKING_OPEN) | Có trong danh sách | **Thiếu ở giao diện; nguồn (Assembly registry) chưa tồn tại** |
| `scope.applicable_conditions` | Không có | **Không có** | **Thiếu ở cả hai.** Đ11 chỉ nêu giao diện; MT1 cũng không cam kết |
| `scope.data_split` | `Evaluation_Protocol_ID`, `Split_or_Fold_ID` (`:329–330`) | Có | Cần từ vựng đóng {same_run, LORO, LOCO}; hiện là định danh, không phải giá trị so được |
| `scope.inference_unit` | `Evidence_Granularity` {WINDOW, RECORDING, RUN, CAMPAIGN} (`:339`) | Có | Khớp được; cần ghi đơn vị chấm điểm (recording) ≠ đơn vị nhóm (run) (sync note `:17`) |
| `obs_context` (khoảng đo, cấu hình, nhiệt độ, cầu trục) | `Observation_Start/End_Time` (`:305`), `Sensor_Mode_ID` (`:312`); không có điều kiện | Không có | Thiếu điều kiện; với phòng thí nghiệm cần giá trị tường minh (ví dụ kích thích, nhiệt độ phòng nếu có, `crane_state = not_applicable`) thay vì để trống |
| `uncertainty` | CEI có cấu trúc (`:342`) | Có (seed, fold, p hoán vị) | Bảng A.1 một trường; cần quyết cấu trúc (D010) |
| `method_version` | `Code_Commit`, `Model_Version`, `Model_Config_ID`, `Environment_ID` | Có | Commit của 1A [NCS XÁC NHẬN] (tệp 00 §3); phụ thuộc siêu tham số 15/18 fold (1A-4) là giới hạn phải mang theo |
| `BIM_GUID` | Một cấu kiện, cấm danh sách GUID (`:352`, `:495`); binding CANDIDATE/VERIFIED | Không nêu | Bằng chứng 1:10 gắn GUID nào? Cần quyết ngữ cảnh (M2) |
| `revision_of` | `Supersedes_Condition_Evidence_ID` (`:293`) | Không nêu | Khớp; hướng ngược nhau (Supersedes trỏ cũ, như `revision_of`) – kiểm lại |
| (thiếu ở A.1) trạng thái thu hồi | `Evidence_Status` có `WITHDRAWN`, `REJECTED` (`:561`) | Không | Paper 2 cần cho C9 (M4.4) |
| (thiếu ở A.1) mức bằng chứng | `Evidence_Granularity` (một phần) | Không | Cần `evidence_level` (M3) |
| `created_at` | `Created_At` | Không nêu | Khớp |

**Bộ trường tối thiểu 1A phải xuất** (mỗi bản ghi, ghi vào 1A-5; [ĐỀ XUẤT], chờ NCS):

1. Định danh: `Condition_Evidence_ID`, `created_at`, `revision_of` (rỗng nếu bản đầu), `status` = CANDIDATE (G1 chưa ký).
2. Loại: `evidence_type` = sensor; `evidence_level` ∈ {observation (nhãn mức lần chạy/bản ghi), method (hiệu năng R2–R4)}.
3. Đối tượng: định danh cấu kiện **của khung 1:10** (vị trí S1/S2/S3 ↔ liên kết) và, nếu dùng ngữ cảnh nhà xưởng, cặp tương
   ứng thông tin có `Physical_Identity = FALSE` (tệp 00 §2).
4. Nguồn: `Sensor_ID` (danh sách qua bảng liên kết), `Campaign_ID`, `Run_ID`, `Assembly_ID`, `obs_interval` [start, end).
5. `obs_context`: cấu hình cảm biến (S12 | S123), trạng thái có kiểm soát (S0, B1–B3 – nhãn vị trí can thiệp), loại kích thích,
   nhiệt độ phòng nếu đã ghi (nếu không: `not_recorded`), `crane_state = not_applicable`.
6. `value`: nhãn hoặc xác suất (mức quan sát) / tên và giá trị chỉ số (mức phương pháp).
7. `uncertainty`: `sd_seed`, `sd_fold`, `perm_p`, `n_independent_units`, khoảng tin cậy nếu có.
8. `method_version`: commit, cấu hình mô hình, môi trường.
9. `scope`: `inference_unit`, `data_split` (từ vựng đóng), `install_batch` (Assembly_ID của quan sát, hoặc tập Assembly_ID trong
   dữ liệu huấn luyện – đánh giá), `applicable_conditions` (dải có trong dữ liệu: campaign, cấu hình, kích thích, nhiệt độ nếu có).
10. Kèm theo (một lần, không theo bản ghi): **sổ giai đoạn lắp đặt** của khung (Assembly_ID, bắt đầu, kết thúc, sự kiện tháo –
    lắp – can thiệp), để Paper 2 tính epoch mà không tự đặt ra.

Ai điền: 1A (người sở hữu R5, tệp 00 §5). Paper 2 chỉ đọc. Khóa trước khi người thứ ba chèn lỗi.

### (d) Ánh xạ PROV-O/SOSA chỉ là "một bảng": phản biện có chấp nhận không, cần thêm gì

**Như hiện tại: không** (M6). Một phản biện sẽ coi là trang trí vì (1) bảng không tác động tới thiết kế nào, (2) có sai ngữ nghĩa,
(3) khái niệm trung tâm không có hàng. Việc không triển khai RDF thì chấp nhận được (`CLAUDE.md:359`, quyết định khóa), miễn là
bảng làm được ba việc: định vị chính xác phần mới, cho phép kiểm lại ngữ nghĩa, và chỉ ra ràng buộc nào đã có ở chuẩn.

**Sai hoặc thiếu cụ thể trong Bảng A.3** ([R3]; tên thuật ngữ PROV/SOSA cần đối chiếu khuyến nghị W3C, `[CẦN NGUỒN: W3C PROV-O; W3C SOSA/SSN]`):
- **Không có hàng** cho `scope`, `within_scope`, `justification`, `obs_context`, `uncertainty`, `actor_role`, `created_at`.
- **Bằng chứng → cấu kiện qua `sosa:hasFeatureOfInterest`** (`phuluc.md:98`): thuộc tính này gắn với quan sát. Bằng chứng mức
  quan sát là kết quả **suy ra từ** quan sát (gần `prov:wasDerivedFrom` một `sosa:Observation`); bằng chứng mức phương pháp không
  phải quan sát. Thiếu cả đặc tính được quan sát (trạng thái liên kết) – `sosa:ObservableProperty`.
- **Bản ghi kiểm tra → bằng chứng** (`:97`): hàng gộp bản ghi (thực thể) với lần kiểm tra (hoạt động). Cần tách: lần kiểm tra là
  hoạt động; `INSPECTION_RECORD` là thực thể sinh ra từ nó.
- **`EVIDENCE_USE`** là quan hệ có thuộc tính (`used_at`, `within_scope`, `justification`, `phuluc.md:47`). Ánh xạ đúng là dạng
  quan hệ được định danh (qualified usage có thời điểm) chứ không phải `prov:used` trơn; và `within_scope`, `justification`
  **không có tương đương** – đó chính là phần mới, nên ghi thẳng như vậy.
- **`STATUS_EVENT` → `prov:Activity` với `prov:wasAssociatedWith`** (`:102`): vai trò người thực hiện (`actor_role`) ứng với vai
  trò trong liên kết tác nhân được định danh của PROV; bảng không nêu, trong khi "đúng vai trò" là nửa của C6.
- **Ánh xạ cảm biến – cấu kiện → `ssn:Deployment` "trên nền tảng"** (`:96`): cần nói cấu kiện vừa là nền tảng mang cảm biến vừa là
  đối tượng quan tâm, và đó là lựa chọn mô hình hóa.
- **PAV** có trong REFINED (`:80`, `:491`) nhưng bị bỏ khỏi A.3 không lý do; `method_version`, `revision_of`, `created_at` có ứng
  viên PAV. Hoặc thêm, hoặc ghi lý do bỏ.
- **Ràng buộc:** PROV có ràng buộc thứ tự giữa sử dụng và vô hiệu hóa `[CẦN NGUỒN: W3C PROV-CONSTRAINTS]`. C9 gần với ràng buộc
  đó; C3 gần với ràng buộc thời gian của triển khai; C5 không có tương đương. Không nêu thì phản biện sẽ cho C9 là tái phát minh.

**Cần thêm để không bị coi là trang trí (trong phạm vi khóa, không RDF):**
1. **Bảng mức trường**, mỗi trường Bảng A.1 một hàng, cột: trường | IFC 4.3/BCF 3.0 | PROV-O/PAV | SOSA/SSN | **loại khớp**
   (tương đương / gần / rộng hơn / không có) | ghi chú. Các hàng "không có" (phạm vi, trong/ngoài phạm vi, lý do, căn cứ của sự
   kiện) là bản đồ của tính mới.
2. **Bảng ràng buộc ↔ chuẩn:** C1, C3, C5, C6, C9 × "có ràng buộc tương đương ở PROV/SSN/IFC/[21]/[44] không" (C3, C9: có tương tự
   ở [21] tr. 17–18 theo `phuluc.md:142` và ở PROV; C6: khuôn ở [44]; C5: không). Đây là chỗ tuyên bố phần mới chính xác nhất.
3. **Một câu phương pháp** giải thích vì sao chỉ đối chiếu: đóng góp là ngữ nghĩa của ràng buộc, độc lập với cách lưu; ánh xạ giữ
   khả năng xuất về sau. Khai báo đây là giới hạn.
4. (Ngoài phạm vi khóa, mục 6, P7) một ví dụ chuỗi bằng ký pháp PROV dạng văn bản trong phụ lục.

### (e) C9 khác C5 thế nào; trùng và kẽ hở

**Khác nhau** ([R3]):

| | C5 | C9 |
|---|---|---|
| Kiểm cái gì | Thế giới đã đổi so với điều kiện của bằng chứng (epoch, điều kiện) | Bản ghi đã bị thay bằng bản khác |
| Neo ở đâu | `EVIDENCE_USE.used_at` | `STATUS_EVENT.timestamp` (qua `evidence_ref` → `EVIDENCE_USE` → `EVIDENCE`) |
| Dữ liệu | `scope`, epoch, `obs_context` | `revision_of`, `created_at` |
| Mức | Mềm: được dùng nếu có lý do | Cứng: vi phạm |
| Tầng | Bằng chứng (G-A, A2) | Trách nhiệm (G-B) |

**Trùng:** khi bản thay được tạo **vì** thế giới đổi (ví dụ tính lại bằng chứng sau can thiệp, `revision_of` trỏ bản cũ), cùng
một lỗi chèn có thể kích cả C5 (nếu `used_at` sau đổi epoch) lẫn C9. Cần quy tắc gán nhóm cho M2 (m5) và nguyên tắc: hết phạm vi
không ghi bằng `revision_of` (mục 4(a)).

**Kẽ hở** (ca thời gian; t_u = `used_at`, t_e = `timestamp` của sự kiện, t_r = `created_at` của bản thay, t_i = can thiệp):

| # | Ca | C5 | C9 | Kết quả |
|---|---|---|---|---|
| 1 | Bản thay sau t_u, trước t_e (t_u < t_r < t_e) – ca được hỏi | Không (đúng ở t_u) | **Bắt**, vì bằng chứng được trỏ đã bị thay trước t_e | Có phát hiện. Nhưng chưa nói phải làm gì: tạo `EVIDENCE_USE` mới cho cùng bản ghi kiểm tra (bản ghi kiểm tra có bất biến không?) hay tạo bản ghi kiểm tra mới |
| 2 | Bản thay trước t_u (t_r < t_u) | Không xét `revision_of` | Chỉ bắt nếu có sự kiện trỏ lần dùng này; bước "(tạo) → Mở" không đòi `EVIDENCE_USE` (`phuluc.md:79`) | **Lọt** khi lần dùng chỉ dẫn tới bản ghi kiểm tra và hành động mới mở |
| 3 | Can thiệp giữa t_u và t_e (t_u < t_i < t_e), không có bản thay | Không (đúng ở t_u) | Không (không có `revision_of`) | **Lọt.** Người phê duyệt chuyển Mở → Đang xử lý dựa trên căn cứ đã hết phạm vi |
| 4 | Xác minh sau sửa chữa dẫn bằng chứng trước can thiệp | Không: epoch chỉ đổi ở "Đã xác minh" (`phuluc.md:122`), nên trước bước đó bằng chứng cũ vẫn "trong phạm vi" | Bước Hoàn thành → Đã xác minh đòi bản ghi kiểm tra, không đòi `EVIDENCE_USE` (`:82`) | **Lọt, và do chính quy tắc đổi epoch** |
| 5 | Bằng chứng bị thu hồi, không có bản thay | Không | Không (không có `revision_of`; Bảng A.1 không có trường trạng thái) | **Lọt** |
| 6 | t_u < `EVIDENCE.created_at` | Không | Không | **Lọt** (m3) |
| 7 | Bản thay sửa lỗi biên tập (không đổi `value`, `scope`) | — | Bắt | **Dương tính giả** nếu mọi bản thay đều coi là vô hiệu; cần `revision_reason` hoặc tuyên bố "mọi bản thay đều vô hiệu" là chủ ý |
| 8 | t_r = t_e, khác múi giờ, `created_at` ghi lùi | — | Không xác định | Cần quy ước so sánh (nửa mở, UTC) và ghi `created_at` do hệ thống, không do người nhập |
| 9 | Chuỗi thay rẽ nhánh (hai bản cùng thay một bản) | — | Không xác định "bản còn hiệu lực" | Cần luật không rẽ nhánh như `CE-VER-006` của giao diện (`G1_TO_G2…:646`) |

**Đề xuất đóng** (phân theo phạm vi khóa):
- Trong phạm vi (chi tiết đặc tả): ca 6, 8, 9 – thêm vào C1/C9 dạng điều kiện thứ tự và không rẽ nhánh; ca 7 – tuyên bố chủ ý;
  ca 2 – mở rộng C9 xét cả bản thay có `created_at < used_at` cho mọi `EVIDENCE_USE` (vẫn là "căn cứ còn hiệu lực").
- Ngoài phạm vi (mục 6): ca 3 – đánh giá vế phạm vi ở cả t_e (P2); ca 4 – dời mốc epoch (P1); ca 5 – trường thu hồi (P3).
- Mọi ca trong bảng nên có trong danh sách lỗi chèn, kể cả ca dự kiến lọt, để M2 báo bỏ sót theo đúng cam kết của hồ sơ.

---

## 5. Đáng giữ / nên bỏ từ hồ sơ cũ (lớp 2), theo góc nhìn nguồn gốc

**Đáng giữ**
1. Tách độ bất định **mức 1 (một dự đoán)** và **mức 2 (quy trình)** – `gate2_3_data_model_v0.2.md:141–142`. Là nền cho
   `evidence_level` (M3).
2. **R07/R07b** (giao thức → mức phạm vi được phép; cross-campaign đòi LOCO) – `:150–152`. Viết lại thành G(d) trong vị từ.
3. **`Scope_Snapshot` + R08b** (bản chụp phạm vi tại lần dùng phải bằng giá trị gốc) – `:180`. Viết lại thành "`within_scope`
   lưu = giá trị tính lại" (M1).
4. **`Data_Origin` {lab_1_10, field_building}** và nội dung R09 – `:116`, `:154`: giữ làm *khai báo* ranh giới, không giữ làm luật
   cấm (thay bằng "ngoài phạm vi theo cấu tạo", M2).
5. Vòng đời bằng chứng có `WITHDRAWN` và luật không rẽ nhánh `CE-VER-006` – `G1_TO_G2…:561`, `:646` (M4, ca 5, 9).
6. Danh sách cấm diễn giải §16 của giao diện (đặc biệt `:768`) – đưa vào phần giới hạn của bài.
7. Câu "phiên bản mô hình khác phạm vi hiệu lực" – `REFINED_v1.0_25092026.md:90`; và tự nhận giới hạn "không kiểm được phạm vi
   có đúng về mặt khoa học" – `:281`.
8. Nguyên tắc ba điều kiện để kết quả lỗi chèn thành bằng chứng (người khác lập, dữ liệu thật, báo ca bỏ sót) – v0.2 mục A.5.

**Nên bỏ**
1. Từ vựng phạm vi dạng nhãn `not_validated | within_campaign | cross_campaign | field_baseline_only` làm *chính* phạm vi
   (`gate2_3_data_model_v0.2.md:143`): nhãn không so được với trạng thái cấu kiện tại lần dùng. Chỉ giữ như giá trị suy ra G(d).
2. CEI như một cấu trúc có tên riêng chồng lên `uncertainty` và `scope` (`G1_TO_G2…:185`): gộp "evidence-validity status" vào scope
   gây trùng nghĩa; giữ thành phần, bỏ tên.
3. Khung Gap 2A–2C với 2B là trung tâm (REFINED §4): trái phạm vi khóa (G-B chính); chỉ giữ ý ở 4.2 như căn cứ cho A2.
4. Kết luận dạng `NOT_ESTABLISHED_IN_TARGETED_CORPUS` (REFINED `:88`): không đưa vào bản thảo; viết theo phạm vi tìm kiếm đã ghi.
5. `Acknowledged_By` như thay thế cho kiểm máy (`gate2_3_data_model_v0.2.md:181`): "đã đọc" không phải giải trình; nếu giữ thì là
   một trường của `justification`.
6. SHACL, w3id, round-trip tests (REFINED `:313`) – mất cơ sở khi bỏ RDF (Đ3).
7. Mọi số kiểm thử 16/16, 2/2, 5,5 ms (v0.2 A.5–A.6) – kiểm thử đơn vị, không trích.

---

## 6. Đề xuất ngoài phạm vi khóa – chờ NCS duyệt

Mỗi đề xuất ghi rõ là **đổi văn bản khóa** (lớp 1) hay **chỉ là chi tiết đặc tả** mà `phuluc.md:122` cho phép khóa sau.

| Mã | Đề xuất | Loại | Lý do |
|---|---|---|---|
| P1 | Mốc mở giai đoạn lắp đặt mới = thời điểm can thiệp xong (sự kiện Đang xử lý → Hoàn thành của hành động có `action_type` ∈ {siết lại, thay thế}), không phải lúc "Đã xác minh". Xác minh chỉ xác nhận | **Đổi văn bản khóa** (`phuluc.md:122`) | Đóng kẽ hở 4(e) ca 4; tránh vòng lặp ở bước xác minh, đúng chỗ G-B nhắm tới |
| P2 | Đánh giá vế phạm vi (epoch, điều kiện) cả tại `timestamp` của mỗi sự kiện có `evidence_ref`, không chỉ tại `used_at`; hoặc mở rộng C9 thành "căn cứ còn hiệu lực = chưa bị thay/thu hồi **và** trong phạm vi hoặc có lý do tại thời điểm chuyển" | **Đổi văn bản khóa** (phát biểu C9 ở `phuluc.md:120`) | Đóng ca 3; làm nghĩa "kiểm tại lần dùng" nhất quán: mỗi lần phê duyệt cũng là một lần dùng |
| P3 | Thêm trường thu hồi trên `EVIDENCE` (`invalidated_at`, `invalidation_reason`), ánh xạ `prov:wasInvalidatedBy` đã có ở A.3 | Đổi Bảng A.1 (thêm trường, không thêm thực thể) | Đóng ca 5; A.3 đã ánh xạ khái niệm mà A.1 chưa có trường |
| P4 | `ACTION.action_type`; view `COMPONENT_EPOCH` (BIM_GUID, epoch_id, start, end, nguồn) | Chi tiết đặc tả | Điều kiện để `within_scope` tính được (M1) |
| P5 | `within_scope` ba trị (TRUE/FALSE/UNKNOWN), UNKNOWN đòi lý do | Chi tiết đặc tả | M1.3 |
| P6 | `justification` có mã lý do + tham chiếu | Chi tiết đặc tả | m4 |
| P7 | Một ví dụ chuỗi bằng ký pháp PROV dạng văn bản (một bằng chứng → một lần dùng → một sự kiện) trong phụ lục, không triển khai RDF | **Đổi văn bản khóa** ("chỉ trình bày bằng một bảng", `CLAUDE.md:359`) | Giúp phản biện kiểm ngữ nghĩa ánh xạ; chi phí nhỏ |
| P8 | Ngữ cảnh thông tin của khung 1:10 (cấu kiện, epoch = lần lắp) làm nguồn ca "trong/ngoài phạm vi" thật cho C5-b | **Đổi cách dựng tập bằng chứng** (`CLAUDE.md` §2A, "dùng để chèn ca dùng ngoài phạm vi") | M2; không cần dữ liệu mới |
| P9 | `applicable_conditions` vào danh sách giao của 1A-5 và MT1(d) | **Đổi văn bản khóa** (GD3b MT1(d), tệp 00 1A-5) | M5; hiện MT1 không cam kết trường mà C5 cần |

---

## 7. Câu tiếng Anh đề xuất cho bản thảo

1. *Definition.* "We define the validity scope of a condition-evidence record as the set of conditions under which its value and
   uncertainty are asserted to hold: the evaluated generalisation level (same-run, leave-one-run-out, leave-one-campaign-out), the
   assembly epoch of the observed connection, the sensor configuration, and the range of operating conditions present in the data
   that produced it."
2. *Distinction.* "Validity scope is distinct from versioning: a method or model version identifies the process that generated a
   record, and a revision supersedes a record that was wrong or incomplete, whereas an out-of-scope record remains a correct account
   of a past observation that no longer applies to the current state of the component."
3. *Check at use.* "Because the assembly epoch of a connection can change after the evidence is created, scope membership is
   evaluated when the evidence is used, as a three-valued predicate (true, false, unknown) over the current epoch of the component
   and the observation context of the record; any use that does not evaluate to true must carry a structured justification."
4. *Boundary.* "Evidence produced on the 1:10 laboratory frame is out of scope for the full-scale building by construction; the
   constraint therefore does not judge laboratory-to-field transfer, but detects changes of scope within one information context,
   which is where unjustified reuse is otherwise invisible."
5. *Mapping.* "The field-level mapping to PROV-O and SOSA/SSN shows that provenance, deployment intervals and record revision have
   standard counterparts, while the scope fields, the in-scope flag and the justification of an evidence use have none; these
   are the elements this model adds."
