# TERMINOLOGY CONTROL
**Version:** v2.2 | **Issued:** 2026-07-17 | **Updated:** 2026-08-04
**Status:** CURRENT | **Source-of-truth level:** 4
**Supersedes:** v1.1 lineage and v2.1 addendum as current terminology control. | **Superseded by:** None.
**Change summary:** Adds identity/event/verification distinctions, corpus-bounded novelty language and G3 authorization wording; preserves the Limited-FEM controls.

Applies to: all thesis chapters, papers, reports, slides, evidence files, and agent outputs from this date.

## 1. Allowed terms (use these)

| Term | Usage note |
|---|---|
| condition evidence | Output of the vibration-to-evidence layer; never "damage proof" |
| state-change evidence | Alternative when no condition label is claimed |
| component-level traceability | Core Paper 2 term |
| BIM-linked inspection record | Core Paper 2/3 term |
| field feasibility | Core Paper 3 term; never "field validation of diagnosis" |
| inspection-maintenance support | Thesis-level framing |
| nominal reference model | The only sanctioned FEM descriptor |
| reference-informed sensor placement | Replaces "optimal sensor placement" |
| practical sensor configuration | Alternative replacement |
| confidence/evidence indicator (CEI) | CEI definition; never physical severity |
| descriptive-diagnostic Digital Twin (management level) | DT maturity self-definition (C3) |
| Workflow_Status | Current-state projection/attribute of Action_Record; never an identifier or history |
| Status_Event | Candidate append-only action-lifecycle history entity; exact schema pending accepted ADR |
| post-action verification | Operational verification of action outcome; not generic provenance verification |
| guarded closure/reopen | Candidate lifecycle requirement; closure requires approved conditions and retained history |

## 2. Controlled or removed terms

| Term | Rule | Replacement / condition |
|---|---|---|
| calibrated FEM | REMOVE from all core text | Only in Post-PhD/limitations as explicitly deferred work |
| calibration (of FEM) | REMOVE as an activity of this thesis | "the nominal model is deliberately uncalibrated" |
| physics-informed condition evidence | REMOVE - prohibited in core architecture | "condition evidence" |
| equivalent stiffness degradation | REMOVE from claims | Only inside SUPPORTING_REFERENCE literature descriptions of other authors' work |
| mechanical damage interpretation | REMOVE as thesis activity | "qualitative mechanical hypothesis (nominal model; not confirmed)" |
| optimal sensor placement / OSP | REMOVE from thesis language | "reference-informed sensor placement"; OSP may appear only when citing the OSP literature as such |
| FEM-based diagnosis | REMOVE | - |
| damage severity / DSI | REMOVE from claims | CEI (confidence/evidence indicator) |
| MAC (as thesis acceptance criterion) | REMOVE as criterion | MAC may appear only in literature descriptions |
| stiffness degradation (of the real structure) | REMOVE from claims | - |
| RUL / remaining useful life | REMOVE | Out of scope; Post-PhD |
| predictive maintenance | REMOVE as thesis claim | "condition-based inspection support"; PdM only as literature-context label |
| autonomous maintenance decision | REMOVE | "human-reviewed decision support" |
| FEM_Node_ID (as chain link) | CONTROL | Optional metadata attribute only; never in the identifier chain |
| RSAP/FEM (in RQ/WP/chapter/paper/gate names) | REMOVE from all structural names | FEM confined to C3 methods subsection + Limitations |
| Action_Status (as identifier) | REMOVE | Use `Action_Record_ID`; status is a current projection |
| completed (as verified closure) | REMOVE | Require approved post-action verification and closure event |
| reverse lookup (as round-trip parity) | REMOVE | Distinguish lookup/navigation, paired query-answer parity and transformation round-trip |
| website/viewer (as novelty) | REMOVE | Supporting implementation instrument only |
| first / no study worldwide | REMOVE | Use corpus-bounded statements only |

## 3. Mandatory FEM qualifier

Every remaining mention of FEM in any current document must carry at first mention per document/section: **"nominal, uncalibrated, reference-only, not used for damage diagnosis."**

## 4. Enforcement

Before any submission or gate closure: run a keyword check for the Section 2 terms plus FEM, RSAP, MAC, modal, calibrat*, severity, RUL, optimal sensor, physics-informed; record results in the gate evidence pack. Legacy/archived files are exempt (historical record) but must not be quoted into new text without translation to current terminology.

## 5. v2.1 addendum (2026-07-19)

**Allowed (bổ sung):** condition evidence; state-change evidence; confidence/evidence indicator (CEI); CEI metadata; traceability-to-decision; component-level traceability; BIM-linked inspection record; justified inspection action; accountable decision; management accountability; role and approval traceability; `Action_Record_ID`; field feasibility; field preparation; field deployment; limited field damage data; operational baseline; human-reviewed decision support; nominal reference model; reference-informed sensor placement.

**Accountability — định nghĩa đã khóa (Charter v2.1 §2.4):** khả năng truy vết vai trò, nguồn bằng chứng, người/đơn vị tạo hoặc xác nhận hồ sơ, thời điểm, phiên bản và trạng thái phê duyệt của một quyết định quản lý. **KHÔNG** phải kết luận trách nhiệm pháp lý hoặc quy lỗi cá nhân. Không dùng accountability như tuyên bố pháp lý.

**Controlled / prohibited (bổ sung):** damage diagnosis; damage severity; DSI; calibrated FEM; FEM-based diagnosis; physics-informed diagnosis; equivalent stiffness degradation; bolt-preload inference; optimal sensor placement; predictive maintenance; RUL; weighted Health Index; autonomous maintenance; automatic work order; commercial Digital Twin platform; direct lab-to-field classifier transfer.

**Quy tắc từ ngữ đặc thù:**
- Chuỗi định danh kết thúc bằng **`Action_Record_ID`**; **`Action_Status` chỉ là thuộc tính** của `Action_Record_ID`, không dùng làm mắt xích định danh (ADR Action_ID 20260719).
- Thay **"workstation-only"** bằng **"field-site independent (can progress without access to Rapexco)"**.
- Phân biệt **field preparation** (được phép sớm) vs **field deployment** (sau khi G4 mở).
- Không dùng **"alert"** thay cho **"condition evidence"** nếu chưa có ngưỡng hành động được xác nhận.
- Không dùng **"prediction"** khi chỉ đang classification hoặc state-change indication.
- Paper 1 metric/kết luận trước Gate 1: ghi **"Candidate claim pending Gate 1 closure."**
- CEI thiếu bằng chứng cho chỉ số đơn: ghi **"Evidence is currently insufficient to define CEI as a universal scalar index."**
- Tham chiếu pháp lý chưa xác minh: ghi **"Legal reference pending official-source verification."**

## 6. v2.2 identity, event and novelty controls (2026-08-04)

- Canonical identity context: `Sensor_ID → BIM_GUID / Asset_ID @ Model_Version_ID → Condition_Evidence_ID → Inspection_Record_ID → Action_Record_ID`.
- Do not add `Component_ID` when `Asset_ID + BIM_GUID + Model_Version_ID` is sufficient. Database surrogate keys are technical implementation keys only.
- `Recommendation != Action_Record`; `completed != verified closure`; defect severity `!= Action_Level`.
- `Verification_Record` may be a separate entity or an `Inspection_Record` subtype; status is **GOVERNANCE_DECISION_REQUIRED** until ADR/expert review.
- Established prior art must not be claimed independently as novelty: sensor-to-BIM, BIM-linked records, IFC GlobalId, BIM-CMMS, generic action information/workflow, CQ, provenance, SHACL/SPARQL/MVD/IDS/database validation, generic fixtures, direct/inverse navigation, generic human-in-the-loop, current status/completed flags, viewer/dashboard/website.
- `CLOSE_SEARCH` means corpus-bounded structural closure, not universal absence and not G2 PASS.
- G3 may be described as `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED`; claimed execution remains `NOT OPEN` before an accepted G2 baseline.
