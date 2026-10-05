---
name: govern-phd-evidence
description: Quản trị định hướng, phạm vi, bằng chứng và Evidence Gate cho luận án PhD "Data-informed Digital Twin — Limited-FEM" về nhà công nghiệp khung thép ven biển. Dùng khi tư vấn định hướng luận án; đọc, viết, phân tích hoặc cập nhật tài liệu nghiên cứu của luận án; lập kế hoạch và sắp thứ tự công việc; đánh giá hoặc phân loại evidence; đề xuất paper, phương pháp, schema, đóng góp hoặc novelty; rà soát phạm vi FEM; đánh giá tiến độ Evidence Gate; xử lý kết quả Gate 1, Gate 2-3, Gate 4 hoặc Gate 5; hoặc khi một yêu cầu có thể làm mở rộng phạm vi luận án. Định tuyến mọi nhiệm vụ theo RQ → WP → Chương/Paper → Evidence Gate → Scope → Evidence type, chặn tài liệu superseded và mở rộng ngoài phạm vi, và áp cấu trúc Claim → Evidence → Limitation → Next action. KHÔNG kích hoạt cho: hướng UAV hoặc công trình lịch sử; hướng AI-HPO hội thảo phụ; công việc giảng dạy; AAC79; và mọi việc cá nhân khác ngoài luận án này.
---

# Govern PhD Evidence

**Version:** v0.2 | **Cập nhật:** 2026-08-09
**Kiến trúc:** Limited-FEM (Verdict B, hai thầy hướng dẫn chấp thuận 17/07/2026).

Skill này không tạo ra thẩm quyền nghiên cứu mới. Nó định tuyến về thẩm quyền đã có
trong repo và chặn công việc dùng nguồn superseded hoặc vượt phạm vi.

## 0. Phạm vi kích hoạt

Chỉ áp dụng cho luận án **Data-informed Digital Twin — Limited-FEM** (nhà công nghiệp
khung thép ven biển). Không kích hoạt cho: UAV / công trình lịch sử; AI-HPO hội thảo phụ;
giảng dạy; AAC79; việc cá nhân khác. Nếu nhiệm vụ không thuộc luận án này, không áp
routing block và không áp guardrails — xử lý như một yêu cầu thông thường.

## 1. Nguyên tắc bất biến

- Không sửa, đổi tên, ghi đè hoặc xóa file quản trị nếu người dùng chưa yêu cầu rõ ràng.
- Không bịa citation, DOI, Zotero key, metric, tiêu chuẩn, điều luật, journal ranking hay
  kết quả nghiên cứu. Thiếu căn cứ thì ghi đúng: `Evidence is currently insufficient.`
- Không tự đánh dấu Gate / milestone / nhiệm vụ là COMPLETE hay PASS khi chưa có evidence,
  acceptance record và tiêu chí nghiệm thu tương ứng.
- Không âm thầm hợp nhất nguồn mâu thuẫn. Theo nguồn cao hơn, ghi nhận xung đột, nêu rõ
  trong câu trả lời.
- Trả lời bằng **tiếng Việt**, ngắn gọn, nghiêm ngặt, thực tế — trừ khi người dùng yêu cầu
  ngôn ngữ khác. Thuật ngữ đã khóa giữ nguyên tiếng Anh.

## 2. Nguồn có thẩm quyền — thứ tự đọc và thứ tự ưu tiên

Thứ tự ưu tiên khi xung đột:

```text
RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717 (ADR-2026-001)
→ MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717
→ CURRENT_STATUS_AND_NEXT_DIRECTION
→ các tài liệu còn lại
```

Bộ nguồn bắt buộc (8 file):

1. `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md` — ADR-2026-001, ACCEPTED, hai thầy
   hướng dẫn chấp thuận 17/07/2026. Quyết định Limited-FEM (Option B).
2. `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md` — hiến chương học thuật đầy đủ:
   RQ, WP, chương, paper, gate, validation ladder, allowed/prohibited claims.
3. `CURRENT_STATUS_AND_NEXT_DIRECTION.md` — hiện trạng và thứ tự ưu tiên công việc.
4. `MASTER_RESEARCH_CHARTER.md` — bản concise điều hướng.
5. `RESEARCH_DIRECTION_AND_SCOPE.md` — vì sao thuộc ngành QLXD, ranh giới phạm vi.
6. `RESEARCH_ARCHITECTURE.md` — kiến trúc bốn lớp.
7. `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md` — Verdict B, căn cứ gốc của ADR.
8. `00_README_START_HERE.md` — điểm vào và thứ tự đọc.

**Vị trí file (kiểm tra ngày 2026-08-09).** Nhánh 17/07 hiện nằm dưới
`90_ARCHIVE/HISTORICAL_UNIQUE_FILES/BACKUP_BEFORE_WRITEBACK_20260718/` và
`.../PRE_FINAL_CLEANUP_SNAPSHOT_20260718/`; `THE_COUNCIL_REVIEW_...` nằm tại
`00_GOVERNANCE/`. Đường dẫn có thể thay đổi — luôn xác minh bằng tên file và header
`Status:` trước khi trích dẫn, đừng giả định đường dẫn.

**Trạng thái và kết quả không được lấy từ skill này.** Trạng thái Gate, số run, metric mô
hình, kết quả LORO phải đọc từ `CURRENT_STATUS_AND_NEXT_DIRECTION.md` và evidence pack
hiện hành ngay tại thời điểm trả lời.

**Xung đột chưa giải quyết:** xem `references/research-guardrails.md` §6. Không tự chuyển
skill sang một nhánh kiến trúc khác khi chưa có yêu cầu rõ ràng của người dùng.

## 3. Routing block — output bắt buộc đầu mỗi nhiệm vụ thuộc luận án

```text
RQ:
WP:
Chương:
Paper:
Evidence Gate:
Scope: Core / Supporting / Future Work / Out of Scope
Evidence type:
```

Điền theo `references/rq-wp-paper-gate-map.md`. Không suy diễn, không đoán.
`Evidence type` là **một** trong bốn lớp ở §5.

Hai trường hợp rỗng khác nhau — không được nhầm:

- **Không tồn tại thành phần cấu trúc** (yêu cầu Out of Scope, hoặc liên quan FEM vốn
  không có RQ/WP/chương/Paper/Gate riêng): ghi
  `Không có — thành phần cấu trúc không tồn tại.`
  Không gán yêu cầu vào RQ gần nhất để làm nó trông hợp lệ.
- **Có thể tồn tại nhưng nguồn hiện hành không xác nhận:** ghi đúng
  `Evidence is currently insufficient.`

Nếu nhiệm vụ không chỉ định Gate, mặc định **Gate 1** (nút chặn kỹ thuật số 1 theo
`CURRENT_STATUS_AND_NEXT_DIRECTION.md` §5), và nói rõ đây là mặc định.

## 4. Cấu trúc phân tích — bắt buộc

```text
Claim → Evidence → Limitation → Next action
```

Không bỏ `Limitation`. `Next action` là **một** bước cụ thể, thực thi được, đưa Evidence
Gate kế tiếp gần hơn — hoặc nêu rõ rằng nó không làm Gate nào gần hơn.

## 5. Bốn lớp bằng chứng — tách biệt, không mượn chéo

| Lớp | Chứng minh được | Không được dùng để tuyên bố |
|---|---|---|
| **Laboratory evidence** | Phân biệt trạng thái liên kết có kiểm soát trên mô hình 1:10 dưới đánh giá run-aware chống rò rỉ | Chẩn đoán hiện trường; suy giảm độ cứng công trình thực; ngưỡng định lượng chuyển giao được |
| **Information traceability** | Định danh, hồ sơ, provenance, competency questions, tiêu chí truy vết hai chiều, toàn vẹn chuỗi | Độ chính xác chẩn đoán; khả thi hiện trường; hiệu quả quyết định |
| **Field feasibility** | Triển khai được, dữ liệu về, baseline vận hành, ánh xạ Sensor→BIM, kịch bản truy vết chạy end-to-end | Phát hiện hư hỏng thực; chuyển classifier lab→field; kiểm chứng chẩn đoán |
| **Management decision support** | Hỗ trợ hành động minh bạch bốn mức, có con người rà soát | Quyết định tự động; thay thế đánh giá kỹ thuật; chấm severity hoặc priority |

Mỗi claim thuộc đúng một lớp. Cần hai lớp thì tách làm hai claim, mỗi claim có evidence và
limitation riêng. Mọi bất thường hiện trường dẫn tới *kiểm tra*, không dẫn tới *kết luận
hư hỏng*.

## 6. Chuỗi đã khóa

Chuỗi nghiên cứu:

```text
Vibration data
→ condition/state-change evidence
→ BIM-linked component
→ inspection record
→ inspection-maintenance action support
```

Chuỗi định danh hiện hành:

```text
Sensor_ID
→ BIM_GUID
→ Condition_Evidence_ID
→ Inspection_Record_ID
→ Action_Status
```

Không tự đổi `Action_Status` thành định danh khác. Không thêm `Status_Event_ID` như thành
phần bắt buộc. `FEM_Node_ID` chỉ là metadata tùy chọn, không bao giờ là mắt xích bắt buộc.
CEI là confidence/evidence indicator gắn với `Condition_Evidence_ID` — không phải mức độ
hư hỏng vật lý, không phải Health Index, không phải severity.

## 7. Ranh giới FEM — phân loại ba mức, không chặn nhầm

Mọi lần nhắc FEM đều kèm qualifier: **nominal, uncalibrated, reference-only, not used for
damage diagnosis.**

| Trường hợp | Phân loại | Xử lý |
|---|---|---|
| FEM danh nghĩa, chưa hiệu chuẩn, chỉ tham chiếu: tham khảo dạng dao động; hỗ trợ chọn vị trí đặt cảm biến (reference-informed sensor placement); minh họa vị trí/thông tin cấu kiện; giả thuyết cơ học định tính trong Discussion/Limitation có nhãn "hypothesis, not confirmed" | **Supporting Scope** | **ĐƯỢC PHÉP.** Thực hiện bình thường, kèm qualifier. Không cấp RQ/WP/chương/Paper/Gate cho FEM. |
| Hiệu chuẩn FEM, model updating, EMA, MAC làm tiêu chí nghiệm thu, độ nhạy FEM, suy luận suy giảm độ cứng, suy luận lực siết bu lông, chẩn đoán hư hỏng bằng FEM, chuyển kết luận định lượng 1:10 → công trình thực | **Out of Scope / Future Work (post-PhD)** | **CHẶN.** Dừng, phân loại, cảnh báo, đề xuất phương án in-scope thay thế. |

FEM **không** có RQ, WP, chương, Paper hay Evidence Gate riêng, và không xuất hiện trong
tên bất kỳ thành phần cấu trúc nào của luận án.

**Test "Zombie FEM":** yêu cầu có tạo ra nghĩa vụ chứng minh độ trung thực của mô hình
(giá trị MAC, sai số tần số, tiêu chí chấp nhận hiệu chuẩn) không? Có → Out of Scope.
Không → FEM danh nghĩa hợp lệ, cho phép. **Không chặn nhầm trường hợp thứ hai.**

## 8. Firewall phạm vi — dừng và cảnh báo, không thực hiện

predictive maintenance · RUL / dự báo thời điểm hư hỏng · field damage diagnosis · chuyển
trực tiếp classifier từ lab sang field · calibrated FEM · stiffness-degradation inference ·
complex weighted Health Index · AI superiority · autonomous maintenance · commercial
software development · xây schema/demo/database trước khi khóa competency questions ·
dùng file superseded làm nguồn hiện hành · CFD · Smart City · Edge AI · optimal sensor
placement · severity/DSI.

Danh mục đầy đủ tuyên bố được phép / chưa đủ bằng chứng / bị cấm:
`references/research-guardrails.md`.

## 9. Evidence Gate

Gate theo Charter v1.1 §11 (bản tóm tắt; định nghĩa chi tiết xem
`references/rq-wp-paper-gate-map.md` §4):

G1 dataset integrity và run-aware evaluation · G2 traceability data model và competency
questions · G3 end-to-end laboratory traceability · G4 field mapping và baseline
feasibility · G5 inspection-action scenario review · G6 Paper 2 submission · G7 Paper 3
submission và thesis synthesis. **Không tồn tại gate FEM calibration / MAC / equivalent
stiffness / FEM sensor sensitivity.**

**Gate 1 là ưu tiên hiện tại** (`CURRENT_STATUS_AND_NEXT_DIRECTION.md` §5.2):

1. khóa run registry;
2. leakage-safe run-aware/LORO evaluation;
3. xác nhận sensor mode của ResNet1D.

**Điều kiện đóng Gate.** Kế hoạch, tên file, schema draft, báo cáo, demo, code chạy thành
công, website chạy được, số lượng test đã pass, artifact Revit/IFC/Dynamo/Pset/IDS/SQLite,
viewer — **không** cái nào tự động đóng Gate. Đóng Gate cần đủ ba thứ: evidence, tiêu chí
nghiệm thu tương ứng, và acceptance record đã ký. Thiếu một trong ba → Gate vẫn OPEN, và
ghi `Evidence is currently insufficient.`

## 10. Quy tắc ưu tiên

Khi không chỉ định Gate, ưu tiên công việc đóng Gate mở sớm nhất (hiện là Gate 1). Công
việc không tạo ra artifact bắt buộc của Gate nào thì gắn nhãn Supporting hoặc Future Work
và xếp sau. Không chuyển nguồn lực sang Gate muộn hơn để tạo cảm giác tiến độ.

## 11. Kết thúc nhiệm vụ

Báo cáo: file đã đọc; file đã tạo hoặc sửa; evidence đã dùng; hạn chế chưa giải quyết;
next action; và Evidence Gate kế tiếp có gần hơn hay không.

## References

- `references/research-guardrails.md` — tuyên bố được phép / chưa đủ bằng chứng / bị cấm;
  ranh giới Limited-FEM ba mức; thuật ngữ chuẩn; quy tắc bốn lớp; dấu hiệu nhận biết tài
  liệu superseded; xung đột nguồn chưa giải quyết; nguyên tắc ưu tiên đóng Gate.
- `references/rq-wp-paper-gate-map.md` — bản đồ RQ ↔ WP ↔ Chương ↔ Paper ↔ Gate ↔ loại
  bằng chứng; bản đồ chương C1–C8; validation ladder V1–V4; bất biến.
