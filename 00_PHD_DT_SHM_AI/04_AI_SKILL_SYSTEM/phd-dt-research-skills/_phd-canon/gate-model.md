# Canon — Evidence Gate Model

> **Đồng bộ 01/10/2026 — Tiểu luận tổng quan.** Với mọi việc thuộc Tiểu luận tổng quan (`01_LITERATURE_REVIEW/03_OUTPUTS/01_TIEU_LUAN_TONG_QUAN/`), `CLAUDE.md` của tiểu luận và `_phd-canon/project-canon-tltq.md` thắng tệp này. Khác biệt chính: mô hình dữ liệu là schema đồ thị (CLAUDE.md mục 8), `STATUS_EVENT` và `AGENT` là thực thể bắt buộc, chuỗi định danh tuyến tính chỉ để trình bày (Phụ lục A); hai trục `priority_level` / `Action_Status` tách riêng; K1–K3 là giả thuyết làm việc, chốt ở ĐD3; ứng viên khoảng trống phải qua quy tắc phản chứng (CLAUDE.md mục 7.4). Ngoài tiểu luận, tệp này giữ nguyên hiệu lực.


**v1.0 · 2026-08-10 ·** derived from `00_GOVERNANCE/EVIDENCE_GATES_v2.1.md` (v2.2, source-of-truth level 4), `CURRENT_STATUS_AND_NEXT_DIRECTION.md` §1 §5, `AGENT_RULES.md` §9.

`EVIDENCE_GATES_v2.1.md` holds the full artifact tables. Read it directly before any gate assessment; this file carries the rules and the shape.

---

## The one rule that matters most

**No skill in this suite emits `PASS`.**

`PASS (signed)` requires a human sign-off artifact. Code running successfully is not a pass. A complete-looking document is not a pass. The strongest verdict any skill may emit is:

```text
READY-FOR-REVIEW
```

and only when every acceptance criterion for that gate item has a named evidence path. Anything less is `PARTIAL EVIDENCE`, `IN-PROGRESS`, `OPEN`, `BLOCKED`, `NOT_RUN`, `EXECUTION-NOT-OPEN`, or `N/A`.

A gate is an **execution gate**: artifact + acceptance criterion + evidence path + owner + reviewer/sign-off + status. Never close one by assumption.

---

## Status vocabulary

| Status | Meaning |
|---|---|
| `OPEN` | Not started or not evidenced |
| `PARTIAL EVIDENCE` | Some artifacts exist; acceptance not met |
| `IN-PROGRESS` | Actively being produced |
| `READY-FOR-REVIEW` | Every acceptance criterion has a named evidence path; awaiting human sign-off |
| `EXECUTION-NOT-OPEN` | Work is forbidden until a prerequisite gate is baselined |
| `BLOCKED` | A hard prerequisite outside the researcher's control is missing |
| `NOT_RUN` | The check was not performed in this session |
| `PASS (signed)` | Human sign-off exists — **only a human may set this** |
| `N/A` | Not applicable to this gate |

---

## Current gate states (2026-08-04 — re-verify before use)

| Gate | State |
|---|---|
| **G1** — Dataset integrity & run-aware evaluation | `OPEN — PARTIAL EVIDENCE`. Reanalysis documentation exists; no accepted Condition_Evidence payload, no signed `G1_ACCEPTANCE_MATRIX.md` |
| **G2** — Traceability model & competency questions | `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN` |
| **G3** — End-to-end lab traceability-to-decision demo | `OPEN — NOT IMPLEMENTED, NOT VALIDATED, NOT OFFICIALLY PASSED`; execution authorization `EXECUTION-NOT-OPEN` until the G2 package is approved and baselined |
| **G4** — Minimum field mapping & baseline feasibility | `OPEN`. Field-access basis is a hard prerequisite and unresolved. Preparation permitted; deployment not |
| **G5** — Inspection-action scenario review | `OPEN` |
| **G6** — Paper 2 submission · **G7** — Thesis synthesis / Paper 3 | `OPEN` |

`CLOSE_SEARCH` is corpus-bounded and is **not** G2 PASS.

**Milestone M1** (Paper 1 submission readiness) sits *below* G1 and is not a new gate.

---

## Required output shape for a gate assessment

Per gate item, deterministic and in this order:

```text
Gate:                G_
Item:                <gate item name, quoted from EVIDENCE_GATES_v2.1.md>
Entry conditions:    <what must be true to even work on this>
Required artifact:   <exact artifact named in the gate table>
Acceptance criterion:<quoted, not paraphrased>
Available evidence:  <repository path, or "none found">
Missing evidence:    <specific, actionable>
Violations:          <rule breaches observed, or "none observed">
Status:              <from the vocabulary above>
Next action:         <single concrete step>
```

End the whole assessment with `Claim → Evidence → Limitation → Next action`.

Quote acceptance criteria verbatim. Paraphrasing an acceptance criterion is how a gate gets softened.

---

## G1 artifact checklist (Stream A)

`DATASET_MANIFEST.csv` · `RUN_REGISTRY_LOCKED.csv` + `RUN_REGISTRY_DATA_DICTIONARY.md` · `FILE_PROVENANCE_REGISTER.csv` · `SENSOR_METADATA_REGISTER.csv` · commit hash / repo tag · `LORO_PROTOCOL_PREREGISTERED.md` · split-before-windowing evidence log · train-only preprocessing evidence log · seed config · `MODEL_CONFIGURATION_REGISTER.csv` · metrics table (macro-F1 + per-class, per-fold) · run/fold uncertainty table (mean ± sd) · `RESNET1D_PROVENANCE_AUDIT.md` · rerun conditions note · `G1_ACCEPTANCE_MATRIX.md` (signed).

Existing related material lives in `05_DATA_CODE_AND_EXPERIMENTS/CANONICAL_THREE_CAMPAIGN_DATASET/` and `.../THREE_CAMPAIGN_REANALYSIS/`. Existing material is not the same as an accepted G1 payload — check each artifact against its acceptance criterion individually.

## G2 artifact checklist (Stream B)

G2 Final Decision Register · Action-Status-Event ADR (reviewed; currently `PROPOSED`) · identifier governance schema · CEI attribute structure · `Action_Record` schema · SCQ/VCQ/RCQ preregistration · acceptance criteria per CQ · `Inspection_Record` schema · `Status_Event` schema · verification and closure rules · CQ Registry with expected answers (paired forward/reverse; query-answer parity distinguished from transformation round-trip) · Constraint Catalogue (identity, relation, chronology, transition, authorization, evidence, closure families) · Fixture/Oracle Manifest (controlled valid/invalid fixtures, isolated mutations, expected focus IDs/codes/counts) · G2 baseline and sign-off.

## G3 (execution not open)

Chain demo · paired forward/reverse CQ tests · identity/relation tests · evidence tests · event/chronology tests · authorization tests · verification/closure tests · exact oracle validation. Do not describe any of these as done, partly done, or in progress against real data.

## G4 (readiness only)

Field-access basis (hard prerequisite) · field sensor register · `Sensor_ID → BIM_GUID` mapping · data return log · completeness & drift QC · operational baseline · 2–3 end-to-end traceability scenarios. Minimum field feasibility evidence is **mandatory** for the thesis even if Paper 3 is not published. Field damage diagnosis is not required and not permitted.

## G5

Four-level logic Normal → Watch → Inspect → Priority Inspection, transparent and unweighted · expert review record · no-automated-decision design note · no-field-damage-conclusion design note.

---

## Gates that do not exist and may not be created

calibrated FEM · MAC · EMA · equivalent stiffness · stiffness degradation · FEM sensitivity · optimal sensor placement.
