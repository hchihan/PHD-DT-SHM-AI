# BẮT ĐẦU TẠI ĐÂY

**Ngày lập:** 17/07/2026  
**Cập nhật mới nhất:** 19/07/2026  
**Kiến trúc hiện hành:** **Traceability-Core v2.1 · Limited-FEM**  
**Lĩnh vực:** Quản lý xây dựng / Quản lý tài sản công trình

> **SOURCE OF TRUTH hiện hành:**  
> `00_GOVERNANCE/MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`
>
> Charter v2.0 và v1.1 chỉ được giữ làm tài liệu lịch sử. Khi có mâu thuẫn, áp dụng  
> `00_GOVERNANCE/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`.

## 1. Luận án giải quyết vấn đề gì

Luận án phát triển một **data-informed Digital Twin framework** để tổ chức và truy vết bằng chứng trạng thái từ dữ liệu dao động đến cấu kiện BIM, hồ sơ kiểm tra và hành động kiểm tra–bảo trì.

Đóng góp cốt lõi thuộc **Quản lý xây dựng**:

> hỗ trợ biện minh và truy vết trách nhiệm của quyết định kiểm tra trong điều kiện dữ liệu hư hỏng hiện trường hạn chế.

Không phải mục tiêu của luận án:

- chẩn đoán hư hỏng hiện trường;
- dự báo RUL hoặc predictive maintenance;
- phát triển thuật toán AI mới;
- hiệu chuẩn FEM;
- xây dựng phần mềm Digital Twin thương mại.

## 2. Trục nghiên cứu đã khóa

### Chuỗi bằng chứng

```text
Vibration data
→ condition/state-change evidence (+ CEI)
→ BIM-linked component
→ inspection record
→ justified, accountable inspection–maintenance action
```

### Chuỗi định danh

```text
Sensor_ID
→ BIM_GUID
→ Condition_Evidence_ID (+ CEI)
→ Inspection_Record_ID
→ Action_Status
```

`CEI` là thuộc tính metadata của `Condition_Evidence_ID`, không phải mức độ hư hỏng hoặc Health Index.

`FEM_Node_ID` chỉ là metadata tùy chọn.

FEM luôn được mô tả:

> **nominal, uncalibrated, reference-only, not used for damage diagnosis.**

## 3. Cấu trúc nghiên cứu

| Trục | Nội dung | Vai trò |
|---|---|---|
| **RQ1 / WP1 / C4 / Paper 1 / G1** | Lab evidence, run registry, LORO, sensor configuration, CEI | Bằng chứng trạng thái có kiểm soát |
| **RQ2 / WP2 / C5 / Paper 2 / G2–G3–G6** | Traceability-to-decision, CEI, BIM, inspection record, competency questions | **Trụ cột nhận diện ngành QLXD** |
| **RQ3 / WP3 / C6 / G4–G5** | Field feasibility tại Rapexco | Bằng chứng khả thi hiện trường |
| **WP4** | Logic Normal → Watch → Inspect → Priority | Hỗ trợ quyết định minh bạch, có con người rà soát |

**Paper 3 có thể là bonus về công bố, nhưng minimum field-feasibility evidence là bắt buộc đối với luận án.**

## 4. Evidence Gate hiện tại

### G1 — Dataset integrity and run-aware evaluation

G1 chưa đóng. Các việc ưu tiên:

1. khóa run registry;
2. hoàn thiện sensor metadata và file provenance;
3. xác nhận split-before-windowing và train-only preprocessing;
4. chạy LORO với common seeds;
5. xác nhận sensor mode và provenance của ResNet1D;
6. tổng hợp metrics và uncertainty ở cấp run/fold;
7. chỉ sau đó mới khóa claim của Paper 1.

Cho tới khi G1 đóng, các kết quả như macro-F1 và nhận định “sensor configuration dominates model architecture” phải ghi:

> **Candidate claim pending Gate 1 closure.**

Công việc được phép chạy song song:

- draft SCQ / VCQ / RCQ;
- thiết kế CEI metadata structure;
- draft Inspection_Record schema;
- lập danh mục tham chiếu pháp lý cần xác minh;
- chuẩn bị sơ bộ field-access và Sensor_ID → BIM_GUID mapping.

## 5. Tám file cần đọc và duy trì

1. `00_GOVERNANCE/MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`  
   Hiến chương học thuật cao nhất.

2. `00_GOVERNANCE/RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md`  
   Ma trận RQ–WP–Chapter–Paper–Gate.

3. `00_GOVERNANCE/EVIDENCE_GATES_v2.1.md`  
   Điều kiện đóng từng Evidence Gate.

4. `00_GOVERNANCE/SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`  
   Thứ tự ưu tiên khi tài liệu mâu thuẫn.

5. `00_GOVERNANCE/RESEARCH_DIRECTION_AND_SCOPE.md`  
   Vấn đề nghiên cứu, lý do thuộc QLXD và ranh giới phạm vi.

6. `00_GOVERNANCE/RESEARCH_ARCHITECTURE.md`  
   Kiến trúc laboratory evidence → traceability → field feasibility → decision support.

7. `01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md`  
   Trạng thái thực tế và nhiệm vụ tiếp theo.

8. `01_CURRENT_CONTROL/PROJECT_CLEANUP_20260718/MASTER_INDEX_CURRENT.md`  
   Chỉ mục dẫn tới các tài liệu hiện hành.

## 6. Nguyên tắc bắt buộc

Mọi phân tích dùng cấu trúc:

```text
Claim → Evidence → Limitation → Next action
```

Phải phân biệt:

1. laboratory evidence;
2. information traceability;
3. field feasibility;
4. management decision support.

Không dùng bằng chứng của lớp này để tuyên bố kết quả của lớp khác.

Legal mapping chỉ dùng để neo nghĩa vụ quản lý và khả năng giải trình. Không dùng văn bản pháp luật để tạo ngưỡng hư hỏng hoặc chẩn đoán kỹ thuật.

Khi bằng chứng chưa đủ, ghi rõ:

> **Evidence is currently insufficient.**

## 7. Trạng thái tài liệu cũ

- Charter v2.0: **HISTORICAL DECISION SOURCE**.
- Charter v1.1 và các file FEM-core: **SUPERSEDED**.
- Không dùng file cũ làm nguồn hiện hành khi mâu thuẫn với v2.1.
- Không xóa dữ liệu, evidence, metric hoặc citation gốc; chỉ cập nhật trạng thái và liên kết tới nguồn hiện hành.

---

**Ưu tiên vận hành hiện tại:** dừng mở rộng governance; tập trung đóng **G1** và chuẩn bị tối thiểu cho **G2**.
