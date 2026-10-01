# Research Guardrails — govern-phd-evidence v0.2

Cập nhật 2026-08-09. Kiến trúc Limited-FEM (ADR-2026-001, 17/07/2026).
Chỉ chứa quy tắc ổn định. Trạng thái Gate, số run, metric và kết quả mô hình **không**
nằm ở đây — đọc từ `CURRENT_STATUS_AND_NEXT_DIRECTION.md` và evidence pack hiện hành.

---

## 1. Tuyên bố được phép

Nguồn: Charter v1.1 §13; MASTER_RESEARCH_CHARTER.md §10.

- Bằng chứng lab phân biệt được các trạng thái liên kết có kiểm soát dưới đánh giá chống
  rò rỉ dữ liệu.
- Cấu hình cảm biến ảnh hưởng đến phân loại mạnh hơn lựa chọn kiến trúc mô hình AI.
- Khung truy vết liên kết được cảnh báo với cấu kiện và hồ sơ kiểm tra, kiểm chứng qua
  kịch bản và competency questions định trước.
- Khung khả thi khi triển khai tại công trình thực (feasibility, không phải diagnosis).
- FEM danh nghĩa cung cấp tham chiếu bố trí cảm biến.
- CEI là chỉ số tin cậy/bằng chứng (confidence/evidence indicator).

**Điều kiện chung:** mọi kết luận định lượng chỉ được phát biểu khi Gate tương ứng đã đóng
với acceptance record. Trước đó, nêu tính chất tạm thời và dẫn về evidence pack hiện hành.

## 2. Khi nào phải ghi "Evidence is currently insufficient."

Ghi đúng câu này (hoặc biến thể cụ thể) khi được yêu cầu khẳng định mà không có artifact
đã ghi nhận và được chấp nhận:

- Trạng thái Gate bất kỳ không có trong tài liệu hiện hành tại thời điểm trả lời.
- Kết quả LORO, số run đã khóa, metric mô hình, sensor mode của ResNet1D.
- Số chương, tạp chí, ngày tháng, số đếm, ranking, tiêu chuẩn không có trong nguồn.
- Tham chiếu pháp lý chưa xác minh → "Legal reference pending official-source verification."
- Tình trạng ký thỏa thuận tiếp cận công trình thực.
- Yêu cầu chính thức của chương trình đào tạo; thành phần hội đồng bảo vệ.
- Tiêu chí nghiệm thu chi tiết của từng Gate: file `EVIDENCE_GATES_v1.1_LIMITED_FEM.md`
  và `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v1.1.md` được Charter v1.1 §11 viện dẫn nhưng
  **không tìm thấy trong repo** (kiểm tra 2026-08-09). Chi tiết gate ngoài phần tóm tắt
  G1–G7 → `Evidence is currently insufficient.`

Không bao giờ điền một ô routing hoặc một ô bảng bằng suy diễn.

## 3. Tuyên bố bị cấm

Nguồn: Charter v1.1 §14; ADR-2026-001; MASTER_RESEARCH_CHARTER.md §11.

- Chẩn đoán hư hỏng hiện trường khi chưa có kiểm tra xác nhận.
- Mọi tuyên bố dựa trên FEM đã hiệu chuẩn; suy luận lực siết bu lông hoặc suy giảm độ
  cứng thực từ FEM.
- Chuyển kết luận định lượng từ mô hình 1:10 sang công trình thực.
- RUL, predictive maintenance, dự báo thời điểm hư hỏng.
- Mức độ hư hỏng ordinal (severity/DSI); mô tả CEI như mức độ hư hỏng vật lý.
- "AI tốt nhất" / ưu việt tổng quát; Health Index trọng số; "optimal sensor placement";
  bảo trì tự động; Digital Twin thương mại hoàn thiện; áp dụng phổ quát.
- Chuyển trực tiếp classifier từ lab sang field.
- Dùng file superseded làm nguồn hiện hành.
- Xây schema, demo hoặc database trước khi khóa competency questions.

## 4. Ranh giới Limited-FEM

Qualifier bắt buộc ở lần nhắc đầu tiên trong mỗi tài liệu hoặc mỗi mục:

```text
nominal, uncalibrated, reference-only, not used for damage diagnosis
```

### 4.1 Supporting Scope — ĐƯỢC PHÉP

Nguồn: ADR-2026-001 "What FEM may still do"; Charter v1.1 §15.

- Mô hình thiết kế tham chiếu danh nghĩa, không hiệu chuẩn.
- Tham khảo dạng dao động của mô hình danh nghĩa.
- Hỗ trợ chọn vị trí đặt cảm biến — dùng thuật ngữ "reference-informed sensor placement".
- Minh họa vị trí và thông tin cấu kiện.
- Giả thuyết cơ học định tính cho các anomaly của Paper 1, đặt trong Discussion/Limitation,
  có nhãn "hypothesis, not confirmed".
- `FEM_Node_ID` như metadata tùy chọn.

Các trường hợp trên **không bị chặn**. Thực hiện bình thường, kèm qualifier, và không cấp
RQ/WP/chương/Paper/Gate cho FEM.

### 4.2 Out of Scope / Future Work — CHẶN

Nguồn: ADR-2026-001 "What FEM must not do"; Charter v1.1 §17.

Hiệu chuẩn FEM · model updating · EMA · MAC làm tiêu chí nghiệm thu · nghiên cứu độ nhạy
FEM · suy luận suy giảm độ cứng tương đương · suy luận lực siết bu lông · chẩn đoán hư
hỏng bằng FEM · luật đồng dạng 1:10 → công trình thực · FEM là mắt xích bắt buộc trong
chuỗi định danh · "physics-informed condition evidence" · FEM trong tên RQ/WP/chương/
Paper/Gate.

Post-PhD: hiệu chuẩn FEM với EMA và model updating; luật đồng dạng lab → field.

### 4.3 Test "Zombie FEM"

Câu hỏi duy nhất: **yêu cầu này có tạo ra nghĩa vụ chứng minh độ trung thực của mô hình
không** (phải công bố giá trị MAC, sai số tần số từng mode, hoặc tiêu chí chấp nhận hiệu
chuẩn)?

- **Có** → §4.2, chặn, phân loại Out of Scope/Future Work, đề xuất thay thế in-scope.
- **Không** → §4.1, cho phép.

Rủi ro hai chiều, cả hai đều là lỗi: (a) để FEM quay lại thành trục lõi; (b) chặn nhầm
việc dùng FEM danh nghĩa hợp lệ — vốn chính là lý do Council chọn B thay vì C.

## 5. Dấu hiệu tài liệu superseded

Coi là **không hiện hành** khi có bất kỳ dấu hiệu nào:

1. Header ghi `SUPERSEDED`, hoặc `Superseded by:` trỏ tới file khác.
2. Là bản v1.0 FEM-core, hoặc bất kỳ tài liệu nào đặt FEM làm trục lõi.
3. Dùng notation cũ: chuỗi định danh `Sensor_ID → FEM_Node_ID → BIM_GUID`; FEM_Node_ID là
   mắt xích bắt buộc; RSAP/FEM trong tên chương/Paper/Gate; "physics-informed condition
   evidence"; "optimal sensor placement" như ngôn ngữ luận án; gate hiệu chuẩn FEM.
4. Là prompt, discovery output, demo, slide, handoff IT hoặc ghi chú văn liệu — đây là
   input, không phải governance và tự thân không phải gate evidence.
5. Nằm trong thư mục backup/snapshot/archive **và** có một bản kế nhiệm đã được phê duyệt.

**Lưu ý riêng:** bộ 8 file nguồn của nhánh 17/07 hiện nằm dưới thư mục archive nhưng
**vẫn là nguồn có thẩm quyền của skill này** theo chỉ định của người dùng — vị trí lưu trữ
không tự động biến chúng thành superseded. Xác minh bằng header, không bằng đường dẫn.

Tài liệu lịch sử là ngữ cảnh chỉ-đọc. Không trích vào văn bản mới mà chưa chuyển sang
thuật ngữ hiện hành.

## 6. Xung đột nguồn chưa giải quyết (ghi nhận, không tự xử lý)

**Cập nhật 01/10/2026:** đối với Tiểu luận tổng quan, NCS đã duyệt (29/09/2026) schema đồ thị có thực thể `STATUS_EVENT` và `AGENT` trong CLAUDE.md của dự án; với nội dung tiểu luận, theo CLAUDE.md. Với hồ sơ quản trị luận án ngoài tiểu luận, xung đột dưới đây vẫn để ngỏ cho NCS và thầy hướng dẫn.

Kiểm tra 2026-08-09: thư mục `00_GOVERNANCE/` chứa một bộ file đánh dấu v2.1/v2.2 (ngày
19/07/2026 và 04/08/2026) tự khai `Status: CURRENT`, đề xuất chuỗi định danh kết thúc bằng
`Action_Record_ID`, thực thể `Status_Event`, và hệ gate có G6/G7 định nghĩa khác.

Trạng thái xử lý trong skill này:

- Skill v0.2 vận hành trên nhánh 17/07 Limited-FEM theo chỉ định của người dùng.
- Bằng chứng phê duyệt cấp thầy hướng dẫn cho bộ v2.1: `Evidence is currently insufficient.`
  ADR 19/07 viện dẫn "Council review 17–19/07/2026" và "Charter v2.0 (docx)" — hai tài
  liệu này không tìm thấy trong repo. Phê duyệt duy nhất xác minh được là Verdict B ngày
  17/07/2026 trong ADR-2026-001.
- Xung đột này **chưa được giải quyết**. Không tự chuyển skill sang nhánh v2.1, và cũng
  không tự tuyên bố v2.1 là superseded. Cần người dùng xác nhận với thầy hướng dẫn.

## 7. Thuật ngữ chuẩn

| Dùng | Thay cho |
|---|---|
| condition evidence / state-change evidence | damage proof, alert, prediction |
| component-level traceability; BIM-linked inspection record | sensor-to-BIM integration như novelty |
| field feasibility | field validation of diagnosis |
| nominal reference model | FEM model, calibrated FEM |
| reference-informed sensor placement | optimal sensor placement / OSP |
| confidence/evidence indicator (CEI) | damage severity, DSI, Health Index |
| inspection-maintenance support | autonomous maintenance decision |
| data-informed Digital Twin (cấp quản lý thông tin, tự định nghĩa mức trưởng thành) | predictive Digital Twin |
| qualitative mechanical hypothesis (nominal model; not confirmed) | mechanical damage interpretation |

Trước mỗi lần nộp hoặc đóng gate: chạy keyword check cho FEM, RSAP, MAC, modal, calibrat*,
severity, RUL, optimal sensor, physics-informed; ghi kết quả vào gate evidence pack.

## 8. Nguyên tắc ưu tiên đóng Gate

1. Đọc `CURRENT_STATUS_AND_NEXT_DIRECTION.md`; xác định Gate mở sớm nhất và các hạng mục
   đang chặn. Hiện tại là **Gate 1**: khóa run registry → leakage-safe run-aware/LORO →
   xác nhận sensor mode của ResNet1D.
2. Xếp hạng công việc theo việc nó có tạo ra artifact bắt buộc của Gate kèm tiêu chí
   nghiệm thu và người rà soát hay không.
3. Công việc không tạo ra artifact như vậy → Supporting hoặc Future Work, xếp sau.
4. Gate chỉ đóng bằng evidence + tiêu chí nghiệm thu + acceptance record. Kế hoạch, code,
   demo, website chạy được, số test đã pass — không cái nào đủ.
5. Không đánh dấu Gate PASS; không trình bày bằng chứng một phần như đã đóng Gate.
