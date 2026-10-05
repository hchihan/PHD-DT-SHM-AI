# PROMPT OPENCODE + ZOTERO MCP
## Deep-read toàn bộ tài liệu mới và cập nhật Evidence Base Limited-FEM

**Ngày chạy dự kiến:** 2026-07-18  
**Mục tiêu:** Đọc sâu toàn văn tất cả PDF mới trong các collection Zotero liên quan, chống trùng lặp, trích xuất bằng chứng theo trang, và cập nhật Evidence Base mà không phá vỡ source of truth.

## 0. KIẾN TRÚC KHÓA — KHÔNG ĐƯỢC THAY ĐỔI

Chuỗi nghiên cứu:

Vibration data → condition/state-change evidence → BIM-linked component → inspection record → inspection-maintenance action support.

Chuỗi định danh:

Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status.

FEM chỉ là: nominal, uncalibrated, reference-only, not used for damage diagnosis.

Không được mở rộng sang calibrated FEM, stiffness degradation, bolt-preload inference, direct lab-to-field classifier transfer, field damage diagnosis, RUL, predictive maintenance, Edge AI, Smart City, complex weighted Health Index, autonomous maintenance, commercial software development hoặc “optimal sensor placement”.

**Lưu ý:** Không có RQ4. Collection `RQ4` phải đổi thành `WP4/Decision Support/Gate 5`.

## 1. SOURCE OF TRUTH — ĐỌC TRƯỚC KHI LÀM

1. MASTER_RESEARCH_CHARTER.md
2. MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md
3. RESEARCH_DIRECTION_AND_SCOPE.md
4. RESEARCH_ARCHITECTURE.md
5. CURRENT_STATUS_AND_NEXT_DIRECTION.md
6. RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md
7. LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md
8. Các addendum RQ/Paper/Gate hiện có
9. Các note deep-read Zotero hiện có

Khi có mâu thuẫn, ưu tiên Charter v1.1 và ADR Limited-FEM.

## 2. COLLECTION ZOTERO CẦN XỬ LÝ

Đọc toàn bộ PDF trong:

- RQ1/WP1/Paper 1/Gate 1
- RQ2/WP2/Paper 2/Gate 2–3
- RQ3/WP3/Paper 3/Gate 4
- WP4/Decision Support/Gate 5

Không chỉ đọc title/abstract. Nếu thiếu PDF: ghi FULLTEXT_UNAVAILABLE, không gắn DEEP_READ.

## 3. PHASE A — INVENTORY VÀ CHỐNG TRÙNG

Với mọi item, trích xuất:
- Zotero key
- title, authors, year, venue
- DOI, URL
- collection
- file attachment
- ngày thêm
- tag và note hiện tại

Kiểm tra trùng theo:
1. DOI
2. title chuẩn hóa
3. authors + year
4. cùng dataset/case nhưng paper khác
5. conference và journal extension

Phân loại:
- EXACT_DUPLICATE
- VERSION_DUPLICATE
- CONFERENCE_TO_JOURNAL_EXTENSION
- SAME_CASE_DIFFERENT_CONTRIBUTION
- NOT_DUPLICATE

Không xóa tự động; chỉ ghi log và đề xuất canonical record.

## 4. PHASE B — DEEP-READ TOÀN VĂN

Mỗi paper phải theo cấu trúc:

Claim → Evidence → Limitation → Next action.

Mỗi claim quan trọng phải có trang, section, bảng/hình liên quan.

### Trường trích xuất bắt buộc

- Zotero_Key
- DOI
- RQ
- WP
- Paper
- Gate
- Evidence_Role: DIRECT / METHODOLOGICAL / STRONG_ADJACENT / BACKGROUND / NORMATIVE / SUPPORTING_FEM / OUT_OF_SCOPE
- Evidence_Type: LAB_EVIDENCE / FIELD_FEASIBILITY / TRACEABILITY / DECISION_SUPPORT
- Study_Object
- Data
- Sensors
- Grouping_Unit
- Validation_Design
- Identifier_Model
- Provenance
- Inspection_Linkage
- Action_Status
- Main_Claim
- Evidence
- Limitation
- Allowed_Use
- Prohibited_Inference
- Relevant_Pages
- Deep_Read_Status
- Duplicate_Status

## 5. YÊU CẦU RIÊNG THEO RQ/GATE

### RQ1 / WP1 / Paper 1 / Gate 1

Trích:
- independent run/group definition
- windowing trước/sau split
- train-only normalization
- leakage risk
- LORO/LOGO
- sensor configuration comparison
- fair model comparison
- uncertainty method
- group-level permutation/Wilcoxon
- giới hạn n≈6 run/class
- ResNet1D sensor mode nếu có tài liệu liên quan

Không chấp nhận bootstrap individual windows, random-window split làm bằng chứng chính, “AI tốt nhất” hoặc field diagnosis.

### RQ2 / WP2 / Paper 2 / Gate 2–3

Trích:
- competency-question methodology
- scoping vs validation CQ
- ontology/schema requirements
- SHACL/constraint validation
- referential integrity
- bidirectional traceability
- source provenance
- IFC GlobalId/BIM_GUID
- inspection-record fields
- relationship cardinality
- action-status history
- query/test reproducibility

Xây competitor matrix:
raw sensor → derived evidence → BIM/IFC identifier → inspection record → action status → CQ validation.

Không tuyên bố novelty ở sensor-to-BIM integration nói chung.

### RQ3 / WP3 / Paper 3 / Gate 4

Trích:
- real field deployment
- industrial/steel-building relevance
- sensor type
- placement rationale
- sampling
- duration
- environmental/operational variability
- missing data
- sensor fault/drift
- operational baseline
- Sensor_ID → BIM_GUID
- practical limitations
- human inspection role

Không chuyển classifier lab sang field; không kết luận damage field; không dùng calibrated FEM; không áp thời gian baseline tối thiểu chung nếu evidence chưa đủ.

### WP4 / Decision Support / Gate 5

Trích:
- transparent escalation
- Normal/Watch/Inspect/Priority hoặc logic tương đương thực sự có trong paper
- expert/facility-manager review
- inspection trigger
- action-status workflow
- audit trail
- scenario validation
- explainability

Không ép AHP, weighted condition index, Markov deterioration hoặc maintenance optimization thành logic bốn mức.

## 6. KIỂM SOÁT CLAIM

Mỗi paper có ba dòng:

ALLOWED CLAIM:
PROHIBITED INFERENCE:
EVIDENCE SUFFICIENCY:

Dùng câu “Evidence is currently insufficient.” khi thiếu toàn văn, metadata mâu thuẫn, không thấy validation, thiếu direct evidence hoặc claim vượt context.

## 7. CẬP NHẬT EVIDENCE BASE — KHÔNG GHI ĐÈ

Không sửa:
- LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md
- Charter
- ADR
- file lịch sử

Tạo mới:

1. 01_LIVING_EVIDENCE_BASE_v1.2_LIMITED_FEM_20260718.md
2. 02_NEW_DEEP_READ_EVIDENCE_MATRIX_20260718.csv
3. 03_RQ1_GATE1_METHOD_EVIDENCE_ADDENDUM_v1.0_20260718.md
4. 04_RQ2_TRACEABILITY_EVIDENCE_ADDENDUM_v1.2_20260718.md
5. 05_RQ3_FIELD_FEASIBILITY_EVIDENCE_ADDENDUM_v1.0_20260718.md
6. 06_WP4_DECISION_SUPPORT_EVIDENCE_ADDENDUM_v1.0_20260718.md
7. 07_CLOSEST_COMPETITOR_MATRIX_PAPER2_20260718.csv
8. 08_DUPLICATE_AND_METADATA_CORRECTION_LOG_20260718.csv
9. 09_ZOTERO_DEEP_READ_COMPLETION_REPORT_20260718.md

Living Evidence Base v1.2 phải nêu số item kiểm tra, số PDF toàn văn, số deep-read mới, duplicate, metadata sửa, evidence map theo RQ, unresolved evidence và next actions.

## 8. CẬP NHẬT ZOTERO NOTES VÀ TAGS

Mỗi item deep-read có child note:

DEEP READ — LIMITED-FEM
Date:
RQ/WP/Paper/Gate:
Evidence role:
Evidence type:
Claim ID:
Claim:
Evidence:
Validation:
Limitation:
Allowed use:
Prohibited inference:
Relevant pages:
Duplicate status:
Metadata corrections:

Tag chuẩn:
RQ1 RQ2 RQ3 WP4 WP1 WP2 WP3 PAPER1 PAPER2 PAPER3 GATE1 GATE2 GATE3 GATE4 GATE5 DIRECT METHODOLOGICAL STRONG_ADJACENT BACKGROUND NORMATIVE LAB_EVIDENCE FIELD_FEASIBILITY TRACEABILITY DECISION_SUPPORT DEEP_READ FULLTEXT VERIFIED LEAKAGE LORO CQ SHACL PROVENANCE INSPECTION_RECORD ACTION_STATUS

Không tạo tag RQ4.

## 9. QUALITY CONTROL

- Không DOI/journal/trang bịa.
- Không gọi DEEP_READ nếu chưa mở PDF.
- Không trộn lab evidence với field feasibility.
- Không trộn field anomaly với damage diagnosis.
- Không đưa FEM vào core chain.
- Không severity/DSI.
- Không predictive maintenance/RUL.
- Không tuyên bố “no study exists” tuyệt đối.
- Novelty claim dùng “within the reviewed evidence base...”.
- Gate 1 vẫn là ưu tiên hiện tại.
- RQ4 đã đổi thành WP4/Decision Support/Gate 5.

## 10. COMPLETION CRITERIA

Chỉ báo hoàn thành khi:
1. tất cả PDF trong bốn collection đã được mở và đọc;
2. mọi paper có note page-level;
3. duplicate được log;
4. metadata được xác minh;
5. Evidence Base v1.2 được tạo không ghi đè v1.1;
6. competitor matrix Paper 2 hoàn thành;
7. từng RQ có Claim–Evidence–Limitation–Next action;
8. điểm thiếu bằng chứng được ghi rõ;
9. báo cáo cuối phân loại COMPLETED / PARTIAL / FULLTEXT_UNAVAILABLE / DUPLICATE / OUT_OF_SCOPE.

## 11. BÁO CÁO CUỐI CHO NGƯỜI DÙNG

Trả lời ngắn gọn bằng tiếng Việt:
- số PDF đã đọc
- số paper mới vào canonical evidence
- số duplicate
- metadata đã sửa
- Gate được tăng cường
- evidence vẫn thiếu
- danh sách file đầu ra
- ba hành động ưu tiên tiếp theo

Không tự thay đổi Charter hoặc định hướng nghiên cứu.
