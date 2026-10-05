# Paper 1A — Gate 1 (Paper 1 status record)

**Cập nhật:** 13/09/2026, sync sau khi Paper 1 khóa khoa học. Bản 28/08 lưu tại `01_LITERATURE_REVIEW/90_ARCHIVE/01_SUPERSEDED_VERSIONS/PRE_SYNC_20260913/`.
**Routing:** RQ1 · WP1 · C4 · Paper 1 · G1 · Core · Laboratory evidence.

## Trạng thái

- **Paper 1:** `SCIENCE LOCKED`, chưa submission-ready, chưa nộp. Tạp chí đích: Structural Health Monitoring (SAGE).
- **Gate 1:** `OPEN — PARTIAL EVIDENCE`. Bằng chứng khoa học đã chạy và đã kiểm toán. Repository chưa có `G1_EXECUTION_PACK` và chưa có `G1_ACCEPTANCE_MATRIX.md` đã ký. Evidence is currently insufficient để ghi G1 = CLOSED.

## Artefact hiện hành

- **Manuscript:** `PAPER1_v8.1_SHM_RISK_REDUCED.docx`, tên bài "Run-Aware Evaluation of Vibration-Based Connection-State Classification: Within-Campaign Performance and Cross-Campaign Limits on a Scaled Bolted Steel Frame".
- **Kiểm toán:**
  - `PAPER1_v8.1_SHM_PRE_SUBMISSION_AUDIT.md`: 50/50 PASS; kết luận "READY AFTER AUTHOR METADATA / FIGURE FIXES".
  - `PAPER1_v8.1_SHM_CHANGELOG.md` và `PAPER1_v8.1_NEW_REFERENCE_AUDIT.md`.
  - `../BAO_CAO_IT01_IT06.md`: overriding evidence cho số liệu.
- **Hình:** `PAPER1_v8.1_Figure3_redrawn_400dpi.png` và `../PAPER1_Figure3_A4_Editable.pptx`, chờ tác giả duyệt.
- **Superseded:** v6, v7 (Buildings), v8 (SHM).

## Claim được phép

Thuộc lớp Laboratory evidence. Ghi "Candidate claim pending Gate 1 closure" cho tới khi G1 PASS.

- Dưới LORO và chấm điểm cấp recording, RF và SVM không tuning đạt pooled Macro-F1 1.000 (CP1), 0.986 (CP2) và 0.875 / 0.690 (CP3). CP3 yếu hơn và phụ thuộc fold (SD_fold tới 0.139).
- Mức phân biệt trạng thái thay đổi theo campaign, theo run giữ lại và theo mô hình.
- Chuyển giao exploratory CP2 ↔ CP3 không xác lập được chuyển giao hợp lệ. CP1 không được đánh giá chuyển giao.
- Classification output chỉ dùng được như condition evidence khi đi kèm provenance, giao thức đánh giá và độ biến thiên quan sát được.
- Các biện pháp kiểm soát và tổ hợp của chúng không được tuyên bố là mới.

## Không claim

- Cấu hình cảm biến chi phối kiến trúc mô hình (thuộc Paper 1B; chưa có bằng chứng hỗ trợ).
- AI hoặc một họ mô hình vượt trội.
- Độ lớn của mức thổi phồng do rò rỉ.
- Chẩn đoán hiện trường, severity, độ cứng, preload.
- Chuyển classifier từ lab sang field.

Paper 1 không dùng FEM. Nếu có nhắc tới FEM thì phải kèm: nominal, uncalibrated, reference-only, not used for damage diagnosis.

## Còn thiếu cho G1 và M1

**Artefact:**
- `G1_EXECUTION_PACK`, gồm: manifest; run registry đã khóa kèm data dictionary; file provenance; sensor metadata; model configuration register; seeds/config; rerun note; `RESNET1D_PROVENANCE_AUDIT.md`.
- File bàn giao IT-01 đến IT-06 và thư mục `evidence/` chưa được lưu vào project.
- `PAPER1_CLAIM_STATUS_TABLE.md`.
- Keyword check.
- `G1_ACCEPTANCE_MATRIX.md` đã ký.

**Quyết định cần thầy** (sync report §5):
- C-04: ngoại lệ M1.
- C-05: câu chữ tiêu chí và việc giao thức không preregistered.
- C-06: phân tích bổ sung có bắt buộc cho G1 hay không.

## Mục tác giả trước khi nộp

- Tên, affiliation, e-mail, ORCID.
- Funding và COI.
- Bốn điểm của AI disclosure.
- Duyệt Figure 3.
- Ảnh B1 thật, và ảnh gốc cho Figure 1(b–c) và 2(d–e).
- Quyết định data/code DOI.

## Ranh giới

- Không sở hữu claim sensor-subset và marginal-benefit của Paper 1B.
- Bàn giao sang Paper 2 theo `01_CURRENT_CONTROL/CURRENT_STATUS_AND_NEXT_DIRECTION.md` §4: Paper 2 không coi raw AI prediction là ground truth vô điều kiện.

Chi tiết: `01_LITERATURE_REVIEW/01_CURRENT_CONTROL/PAPER1_SCIENCE_LOCK_PROJECT_SYNC_REPORT_20260913.md`.
