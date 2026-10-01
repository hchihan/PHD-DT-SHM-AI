# Chuẩn hiện hành của dự án (đồng bộ từ CLAUDE.md, 01/10/2026)

Tệp này là **bản tóm tắt đồng bộ** từ `CLAUDE.md` của dự án Tiểu luận tổng quan
(`00_PHD_DT_STEEL_INSPECTION_2026_2029_LIMITED_FEM/01_LITERATURE_REVIEW/03_OUTPUTS/01_TIEU_LUAN_TONG_QUAN/CLAUDE.md`).
CLAUDE.md đã được NCS duyệt từng mục và được cập nhật sau mỗi phiên; skill được tạo trước đó (07–08/2026).

## 0. Quy tắc ưu tiên

1. Khi làm việc trong thư mục Tiểu luận tổng quan (TLTQ) hoặc cho bất kỳ nội dung nào sẽ vào tiểu luận: **đọc CLAUDE.md của
   dự án trước, và CLAUDE.md thắng mọi bản tóm tắt cứng trong skill** (chuỗi, bản đồ RQ/WP, câu chữ khoảng trống, nơi ghi kết quả).
2. Nếu có thay đổi mới hơn tệp này trong CLAUDE.md (mục 2 "Quyết định đã khóa", mục 6.1, mục 7.4, mục 8, mục 12), **theo CLAUDE.md**
   và ghi chú rằng tệp đồng bộ đã cũ.
3. Ngoài phạm vi tiểu luận (hồ sơ quản trị luận án, Gate, run registry): vẫn đọc nguồn quản trị hiện hành; nếu không có trong
   phiên thì ghi `Evidence is currently insufficient.` Ghi chú: ngày 01/10/2026 các tệp trong `00_GOVERNANCE/` và
   `01_CURRENT_CONTROL/` đang ở trạng thái bị xóa trong cây làm việc Git; không giả định đường dẫn.

## 1. Quyết định đã khóa (CLAUDE.md mục 2)

1. Hướng sửa: đi xuôi từ bài toán thực tế → đối tượng → hạn chế hiện tại → khoảng trống.
2. **Kết quả Paper 1 không được đưa vào tiểu luận** dưới bất kỳ hình thức nào (số liệu, bảng, hình, "kết quả sơ bộ"); chỉ mô
   tả thiết kế và công cụ của thực nghiệm.
3. Công cụ AI ở WP1 đúng theo Paper 1: Random Forest, SVM-RBF, 1D-CNN, ResNet1D; đánh giá theo nhóm (giữ lại cả lần chạy),
   chấm điểm theo bản ghi, kiểm định hoán vị, báo cáo biến thiên theo seed và fold.
4. Công cụ AI ở hiện trường (WP3): Autoencoder phát hiện bất thường so với đường cơ sở vận hành, bù ảnh hưởng môi trường –
   vận hành (EOV), vòng lặp kiểm tra tạo nhãn. WP2: LLM trích xuất hồ sơ, kỹ sư xác nhận. WP4: luật minh bạch, không AI hộp đen.
   Không thêm mô hình khác (Gradient Boosting, SHAP/Grad-CAM, calibration/conformal) khi NCS chưa duyệt.
5. Nguyên tắc AI: **"AI tạo bằng chứng, con người quyết định"**; mọi đầu ra AI là một bản ghi `EVIDENCE` có `method_version`,
   `uncertainty`, `VALIDITY_SCOPE`.
6. **Schema dạng đồ thị, không phải chuỗi tuyến tính** (mục 3 dưới đây). Chuỗi định danh
   `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status` vẫn là chuỗi định danh lõi để
   trình bày, chi tiết chuyển sang Phụ lục A; nó **không** còn là mô hình dữ liệu.
7. Tách hai trục: `priority_level` (Bình thường → Theo dõi → Kiểm tra → Kiểm tra ưu tiên) và `Action_Status` (Mở → Đang xử lý
   → Hoàn thành → Đã xác minh).
8. **K1–K3 là giả thuyết làm việc, chưa khóa.** Khoảng trống chỉ được chốt ở Điểm duyệt 3 (ĐD3), sau khi đọc sâu 20–30 tài
   liệu key; không viết lại khoảng trống trước ĐD3.

## 2. Ba giả thuyết khoảng trống K1–K3 (câu chữ hiện hành, tiểu luận mục 5.2)

- **K1 — Xác lập chất lượng và phạm vi hiệu lực của bằng chứng trạng thái.** Một kết quả phân loại từ dữ liệu dao động chỉ
  có thể trở thành bằng chứng dùng được khi đơn vị vật lý độc lập, rò rỉ dữ liệu và phạm vi chuyển giao được kiểm soát và
  báo cáo rõ.
- **K2 — Bảo toàn chất lượng của bằng chứng trong truy vết cấp cấu kiện.** Liên kết cảm biến – BIM, BIM – hệ quản lý bảo
  trì, hồ sơ kiểm tra – cấu kiện đều đã có tiền lệ; phần còn thiếu là bảo toàn các thuộc tính xác lập chất lượng của bằng
  chứng khi bằng chứng đi qua chuỗi tới cấu kiện và hồ sơ.
- **K3 — Từ bằng chứng có phạm vi hiệu lực đến trạng thái hành động có thể giải trình.** Quy trình kiểm tra có người tham
  gia, bản ghi sửa chữa, trạng thái hoàn thành đã có tiền lệ; phần còn thiếu là truy ngược trạng thái của một hành động về
  đúng căn cứ kỹ thuật, khi căn cứ đó mang theo phạm vi hiệu lực và lịch sử xử lý.

Ghi chú: câu chữ "Gap 1–3" trong skill (bản 17/07) là bản cũ; khi khác nhau, dùng câu chữ ở trên. Mọi phát biểu về khoảng
trống là **trong phạm vi tập tài liệu đã đọc**.

## 3. Schema (CLAUDE.md mục 8)

**Thực thể:** `COMPONENT` (BIM_GUID, model_version) · `MODEL_VERSION` · `SENSOR` (Sensor_ID) · `SENSOR_MAPPING` (valid_from,
valid_to, install_record_ref) · `OBS_CONTEXT` (campaign, sensor_config) · `EVIDENCE` (Condition_Evidence_ID, evidence_type =
cảm biến | quan sát | NDT, value, uncertainty, method_version) · `VALIDITY_SCOPE` (inference_unit, data_split, install_batch,
applicable_conditions) · `EVIDENCE_USE` (within_scope, justification) · `INSPECTION_RECORD` · `ACTION` (priority_level,
Action_Status) · `STATUS_EVENT` (from_to, reason, timestamp) · `AGENT` (role, authority).

**Quan hệ chính:** SENSOR–COMPONENT qua SENSOR_MAPPING có thời hạn; EVIDENCE n:m COMPONENT; EVIDENCE 1:1 VALIDITY_SCOPE (bắt
buộc); INSPECTION_RECORD dùng EVIDENCE qua EVIDENCE_USE; INSPECTION_RECORD → ACTION → STATUS_EVENT; STATUS_EVENT dựa trên
EVIDENCE_USE; AGENT thực hiện/chuyển trạng thái.

**Ràng buộc C1–C8:** C1 không mồ côi · C2 ID duy nhất · C3 thời điểm quan trắc nằm trong hiệu lực ánh xạ · C4 khớp phiên bản
mô hình · C5 dùng ngoài phạm vi phải có lý do · C6 bước chuyển có căn cứ và đúng thẩm quyền · C7 bước chuyển hợp lệ theo máy
trạng thái · C8 bằng chứng cảm biến bắt buộc có OBS_CONTEXT và method_version.

**Ánh xạ chuẩn:** SOSA/SSN (cảm biến, quan trắc) · PROV-O · IFC (cấu kiện) · IDS · SHACL.

`STATUS_EVENT` **là thực thể bắt buộc** của schema; điều "không thêm Status_Event_ID như thành phần bắt buộc" trong skill
cũ không còn áp dụng cho tiểu luận.

## 4. Tiền lệ bắt buộc nêu (kết quả kiểm phản chứng GĐ2, 30/09/2026; CLAUDE.md mục 6.1)

- **BCF 3.0**: trạng thái vấn đề, sự kiện chuyển trạng thái (BCF-API). Phần mới của luận án: quan hệ giữa sự kiện chuyển
  trạng thái với bản ghi sử dụng bằng chứng.
- **IFC4** (`IfcActionRequest`, `IfcProjectOrder` loại lệnh bảo trì, `IfcTask`, `IfcApproval`, `IfcPerformanceHistory`): hành
  động có trạng thái, phê duyệt, dữ liệu đo theo thời gian. Phần mới: lịch sử chuyển trạng thái và quan hệ định kiểu từ
  hành động về bằng chứng tình trạng.
- **SSN `Deployment`** và **IFC Monitor [2]**: ánh xạ cảm biến – cấu kiện. Phần mới: khoảng hiệu lực bắt buộc và ràng buộc C3.
- **[44] García 2026**: khuôn "bước chuyển có bằng chứng và đúng thẩm quyền" (C6) cho gói thông tin bàn giao. Phần mới: áp
  khuôn đó cho hành động kiểm tra – bảo trì dựa trên bằng chứng tình trạng.

## 5. Quy tắc bằng chứng và trích dẫn (CLAUDE.md mục 4)

- Không bịa trích dẫn, tác giả, năm, tạp chí, DOI; mọi trích dẫn phải có trong Zotero với định danh đã xác minh. Kết quả
  Consensus chỉ là gợi ý.
- Không trích nội dung chưa đọc đoạn tương ứng trong bản gốc; nếu chỉ đọc tóm tắt, ghi rõ.
- Tài liệu 2025–2026: kiểm trạng thái xuất bản; **mỗi khoảng trống ở GĐ3 cần ít nhất ba căn cứ không thuộc nhóm 2025–2026**.
- Không dùng [23] (nhà văn phòng UCLA) làm căn cứ cho nhà công nghiệp.
- Thiếu nguồn: ghi `[CẦN NGUỒN]`, không lấp bằng nhận định chung.
- Quy ước trích dẫn: tài liệu cũ `\[n\]` theo `matrix/doi_chieu_danh_muc.csv`; tài liệu mới `\[@KHÓA_ZOTERO\]`; không tự đánh số.
- PDF lưu trong `pdf/` của dự án, tên tệp bắt đầu bằng khóa Zotero.

## 6. Khuôn đọc sâu và quy tắc phản chứng (CLAUDE.md mục 7.4)

- Mỗi tài liệu: một ghi chú `notes/<khóa Zotero>.md` và một dòng `matrix/literature_matrix.csv`, các cột: Citekey/Số cũ ·
  Tier/Cụm (Song sinh số · SHM–bu lông–EOV · Độ tin cậy đánh giá · Truy vết thông tin · Giá trị quyết định) · Luận điểm ·
  Bằng chứng · Giới hạn (tách tác giả tự nêu và nhận định NCS) · Tác động K1/K2/K3 · Vị trí sử dụng · Mức đã đọc.
- Ghi chú có thêm các mục 1–8 của phiên T1-1: câu hỏi nghiên cứu và đối tượng; phương pháp và kiến trúc thông tin; cách kiểm
  chứng; luận điểm chính kèm trang; giới hạn; điều bài không xử lý theo chuỗi của luận án (nguồn gốc bằng chứng cảm biến;
  phạm vi hiệu lực; quan hệ bằng chứng – cấu kiện có thời hạn; trách nhiệm/thẩm quyền; trạng thái hành động và lịch sử chuyển
  trạng thái; truy ngược từ hành động về dữ liệu gốc); tác động K1–K3; vị trí sử dụng.
- Ứng viên khoảng trống ghi ở `revision/GD2_nhat_ky_khoang_trong.md` (mã UV-NN): phát biểu, căn cứ kèm trang, loại căn cứ (tác
  giả tự nêu / NCS nhận định), liên quan K, số căn cứ độc lập, năm; **thêm căn cứ vào ứng viên đã có trước khi tạo mới**.
- **Quy tắc phản chứng:** mỗi ứng viên có trường "Phản chứng đã kiểm" (nguồn, chuẩn, hệ thống có thể đã giải quyết; kết quả kèm
  trang hoặc "chưa kiểm") và "Phát biểu đã thu hẹp". Ứng viên chỉ vào GĐ3 khi không còn mục "chưa kiểm".
- Gắn tag Zotero `Doc:toan_van` và `K1`/`K2`/`K3` sau khi đọc toàn văn.

## 7. Văn phong và giới hạn (CLAUDE.md mục 4.2, 4.5, 10)

- Tiếng Việt học thuật; tách bằng chứng (tài liệu nói gì) và diễn giải (NCS suy ra gì).
- Câu giới hạn gom về mục giới hạn (nhãn tạm 5.8); không rải "không chứng minh…" trong thân bài.
- Thuật ngữ: bằng chứng trạng thái (condition evidence) là một nhận định về tình trạng của một cấu kiện, kèm nguồn tạo ra nó
  và phạm vi được phép sử dụng; phân biệt kết quả phân loại ≠ bằng chứng trạng thái ≠ chẩn đoán hư hỏng; phạm vi hiệu lực;
  nguồn gốc; đường cơ sở vận hành; vòng lặp kiểm tra tạo nhãn; DM/DS/DT theo Kritzinger và cs. 2018. Không gọi hệ thống là
  "song sinh số" khi chưa khai báo mức tích hợp.

## 8. Cấu trúc tiểu luận v2 để định tuyến (CLAUDE.md mục 6.3)

| Mục tiểu luận | Nội dung | Ứng với |
|---|---|---|
| 1.2, 1.3, 1.4 (mới) | Đối tượng; bằng chứng trạng thái; ba câu hỏi của người quản lý | Bối cảnh |
| 2.1–2.3 | Quản lý tài sản (+ISO 55000); BIM/IFC (+BCF); song sinh số | Tổng quan |
| 3.1–3.7 | Dao động; hạn chế với công trình công nghiệp (mới); cảm biến – học máy; độ tin cậy; nguồn gốc – phạm vi hiệu lực; cầu nối PTN – hiện trường (mới) | RQ1, WP1; K1 |
| Chương 4 | Truy vết thông tin; 4.5.4 tách priority_level và Action_Status | RQ2, WP2; K2 |
| 5.2 | Khoảng trống (viết lại sau ĐD3) | K1–K3 |
| 5.5 | Schema đồ thị | RQ2, WP2 |
| 5.6 | Công cụ AI | WP1–WP4 |
| 5.7 | Kiểm chứng – chỉ số (B0, B1, M2.x, M3.x) | RQ2, RQ3 |
| Mục giới hạn (nhãn tạm 5.8) | Phạm vi diễn giải | — |
| Phụ lục A, B, C | Chuỗi định danh chi tiết và thang V1–V4; ràng buộc C1–C8; ma trận RQ–WP–Paper–Gate | — |

## 9. Những điều không làm (CLAUDE.md mục 11)

Không đưa kết quả Paper 1 vào tiểu luận · không bịa hoặc "hoàn thiện" thông tin thư mục · không chốt hay viết lại khoảng trống
trước ĐD3 · không sửa nhiều chương trong một phiên, không sửa tệp .docx gốc · không gọi hệ thống là song sinh số khi chưa khai
báo mức tích hợp · không mở rộng sang bảo trì dự đoán, tuổi thọ còn lại hay tối ưu chi phí. Tường lửa FEM của skill giữ nguyên.

## 10. Cách làm việc

Mỗi phiên một nhiệm vụ; kết thúc phiên có tóm tắt, diff, trích dẫn mới, việc còn mở, rồi dừng chờ NCS duyệt; cập nhật
`revision/changelog.md` và bảng tiến độ (CLAUDE.md mục 12); commit trên nhánh `revision-v2`, chỉ thêm đường dẫn cụ thể.
