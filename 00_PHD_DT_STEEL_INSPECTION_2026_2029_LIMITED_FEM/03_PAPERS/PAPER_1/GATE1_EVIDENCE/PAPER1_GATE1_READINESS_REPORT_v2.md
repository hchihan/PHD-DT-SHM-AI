# PAPER 1 / GATE 1 — READINESS REPORT (v2)
**Date:** 2026-07-18 | **Position:** RQ1 → WP1 → C4/Paper 1 → Gate 1 | **Classification:** Core Scope

## Claim
Manuscript v2 đã được viết lại toàn bộ theo verified-evidence control: khung phương pháp run-aware/LORO hoàn chỉnh, 7 nguồn RQ1 mới đã deep-read được dùng đúng vai trò, mọi kết quả số sơ bộ được thay bằng placeholder chuẩn, và Gate 1 được tuyên bố trung thực là chưa đóng.

## Evidence
- Manuscript canonical hiện có: `../../../90_ARCHIVE/HISTORICAL_UNIQUE_FILES/PRE_FINAL_CLEANUP_SNAPSHOT_20260718/Paper 1/PAPER1_GATE1_Q2_VERIFIED_EVIDENCE_REVISED_v2_MANUSCRIPT_SOURCE_20260718.md`. DOCX v2 được bản cũ tham chiếu không tồn tại trong working tree và phải được tái xuất từ nguồn Markdown nếu cần.
- Nguồn evidence: `../../../90_ARCHIVE/GOVERNANCE_HISTORY/EVIDENCE_BASE/01_LIVING_EVIDENCE_BASE_v1.2_LIMITED_FEM_20260718.md`; `../../../02_EVIDENCE_BASE/ZOTERO_DEEP_READ/02_NEW_DEEP_READ_EVIDENCE_MATRIX_20260718.csv`; `../../../90_ARCHIVE/SNAPSHOTS_20260718/BACKUP_BEFORE_WRITEBACK_20260718/03_RQ1_GATE1_METHOD_EVIDENCE_ADDENDUM_v1.0_20260718.md`; `../../../02_EVIDENCE_BASE/ZOTERO_DEEP_READ/08_DUPLICATE_AND_METADATA_CORRECTION_LOG_20260718.csv`; `../../../02_EVIDENCE_BASE/ZOTERO_DEEP_READ/09_ZOTERO_DEEP_READ_COMPLETION_REPORT_20260718.md`; `../../../90_ARCHIVE/GOVERNANCE_HISTORY/EVIDENCE_BASE/LIVING_EVIDENCE_BASE_v1.1_LIMITED_FEM.md` (canonical RQ1 corpus).
- Audit files: `PAPER1_GATE1_CLAIM_EVIDENCE_AUDIT_v2.md`; `PAPER1_GATE1_VERIFIED_REFERENCE_AUDIT_v2.csv`; `PAPER1_GATE1_MAJOR_REVISION_LOG_v2.md`; `PAPER1_GATE1_DATA_ANALYSIS_REQUESTS_FOR_IT_v2.md`.

## Limitation — evidence still missing (chặn Gate 1)
1. `RUN_REGISTRY_LOCKED.csv` và `DATASET_FILE_MANIFEST.csv` chưa tồn tại; số run (6/class, 72 recordings) mới là con số báo cáo, chưa khóa.
2. LORO chưa được thực thi; chưa có common fold registry, per-run predictions, metrics.
3. Split-before-windowing audit và train-only preprocessing audit chưa có.
4. ResNet1D provenance (sensor/channel mode, folds, seeds, checkpoint) chưa xác minh → chưa quyết định include/exclude.
5. Group-preserving permutation, effect sizes, sensitivity analyses chưa chạy; phương pháp suy luận cuối chưa được phê duyệt (METHOD DECISION REQUIRED).
6. Sensor/channel metadata và excitation metadata chưa đối chiếu hồ sơ thí nghiệm.
7. Metadata một số canonical v1.1 references cần xác nhận trước submission; Zotero writeback vẫn BLOCKED (local-only mode).

## Gate 1 conclusion

**NOT READY.**

Manuscript framework và evidence control đã sẵn sàng, nhưng Gate 1 không thể xem xét đóng khi các artifact thực nghiệm T01–T11 và T13 (xem IT task register) chưa tồn tại. Gate 1 chưa đóng và không được tuyên bố đóng dựa trên văn liệu.

## Next action
1. IT thực hiện T01–T02 (run registry + manifest) trước tiên — nút chặn số 1.
2. Chạy LORO theo protocol §4 manuscript; nộp T05–T08, T10–T11.
3. Quyết định ResNet1D (T09) và phê duyệt phương pháp suy luận (§4.8) với người hướng dẫn.
4. Sau khi đủ artifact: cập nhật §5–§6, chạy lại quality checklist, chuyển trạng thái sang CONDITIONALLY READY / READY FOR GATE REVIEW.
5. Cấu hình Zotero writeback (ZOTERO_API_KEY, ZOTERO_LIBRARY_ID) để xử lý queue metadata trước khi xuất bibliography chính thức.

**Evidence Gate kế tiếp có tiến gần hơn không:** Có — khung manuscript, claim audit và task register làm rõ chính xác phần còn thiếu của Gate 1, nhưng khoảng cách còn lại là thực nghiệm, không phải văn liệu.
