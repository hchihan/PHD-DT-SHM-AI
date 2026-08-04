# ARCHITECTURE DECISION RECORD — 2026-07-19 (v2.1 Traceability-Core)
**Status:** ACCEPTED | **Date:** 2026-07-19 | **Supersedes as current:** ADR 2026-07-17 (Limited-FEM) — giữ làm nguồn lịch sử, không xóa.
**Basis:** Council review 17–19/07/2026; supervisor Verdict B (17/07/2026); Charter v2.0 (docx) và v2.1 (traceability-core).

---

## Context
ADR 20260717 đã hạ FEM xuống nominal reference và đặt traceability làm lõi. Nhưng RQ còn viết bằng ngôn ngữ ontology-engineering; hội đồng QLXD sẽ hỏi "quyết định quản lý nào thay đổi, ai chịu trách nhiệm?". v2.0 tái định khung sang traceability-to-decision với CEI hạng nhất và justification/accountability làm mục đích. v2.1 siết bốn điều chỉnh học thuật bắt buộc để chống overclaim.

## Decision
1. **Trục lõi:** evidence + CEI → BIM component → inspection record → justified, accountable inspection action. FEM giữ nguyên vai trò nominal, uncalibrated, reference-only.
2. **RQ2 là câu gốc đã khóa** (justification & accountability under limited field damage data) — trụ cột nhận diện QLXD.
3. **Field feasibility:** Paper 3 publication optional; **minimum field feasibility evidence mandatory.**
4. **Paper 1 claims:** candidate cho tới khi Gate 1 đóng.
5. **CEI:** first-class metadata structure, không phải scalar/Health Index.
6. **Legal mapping:** chỉ neo nghĩa vụ quản lý; không tạo ngưỡng kỹ thuật; tham chiếu chưa xác minh ghi "pending official-source verification".

## Consequences
- **Positive:** đóng góp QLXD không thể nhầm lẫn; mọi claim gắn evidence; chống scope creep.
- **Negative / cost:** phải pre-register CQ trước khi build; phải thu thập minimum field evidence dù không công bố Paper 3.
- **Rejected alternatives:** calibrated FEM / model updating; ontology-engineering-as-contribution; RUL/predictive maintenance; weighted Health Index; direct lab-to-field transfer — tất cả out of scope (post-PhD hoặc prohibited).

## Firewall (bất biến)
Không RQ/WP/chương/Paper/Gate FEM. `FEM_Node_ID` chỉ optional metadata. Bốn lớp bằng chứng (lab / traceability / field feasibility / decision support) không trộn lẫn.

## Traceability
- Charter: `MASTER_RESEARCH_CHARTER_v2.1_TRACEABILITY_CORE_20260719.md`
- Matrix: `RQ_WP_CHAPTER_PAPER_GATE_MATRIX_v2.1.md`
- Gates: `EVIDENCE_GATES_v2.1.md`
- Hierarchy: `SOURCE_OF_TRUTH_HIERARCHY_v2.1.md`
