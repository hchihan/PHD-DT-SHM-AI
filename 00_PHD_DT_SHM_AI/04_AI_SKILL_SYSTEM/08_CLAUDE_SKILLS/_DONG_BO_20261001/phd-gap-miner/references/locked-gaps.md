# Locked gaps, evidence layers and prohibited claims

Restated from `RESEARCH_ARCHITECTURE.md` (Charter v1.1 Limited-FEM, ADR-2026-001, 17/07/2026) and Chapter 4 §4.4 of the literature review. This file is a convenience copy — if the user supplies a current `RESEARCH_ARCHITECTURE.md` or the audit file and it conflicts with this file, the supplied file wins.

## The four evidence layers

```
Laboratory evidence → Information traceability → Field feasibility → Inspection-maintenance support
```

Each layer only claims what it verified; no layer may borrow another layer's evidence. FEM is nominal, uncalibrated, reference-only, never used for damage diagnosis, and carries no dedicated RQ/WP/chapter/Paper/Gate.

## Ba giả thuyết khoảng trống hiện hành K1–K3 (đồng bộ 01/10/2026 từ tiểu luận mục 5.2)

Trạng thái: **giả thuyết làm việc**, chốt ở Điểm duyệt 3. Khi chấm, dùng câu chữ này; câu chữ "Gap 1–3" bên dưới là bản lịch sử 17/07 để đối chiếu.

- **K1 — Xác lập chất lượng và phạm vi hiệu lực của bằng chứng trạng thái.** Một kết quả phân loại từ dữ liệu dao động chỉ có thể trở thành bằng chứng dùng được khi đơn vị vật lý độc lập, rò rỉ dữ liệu và phạm vi chuyển giao được kiểm soát và báo cáo rõ.
- **K2 — Bảo toàn chất lượng của bằng chứng trong truy vết cấp cấu kiện.** Các liên kết cảm biến – BIM, BIM – hệ quản lý bảo trì, hồ sơ – cấu kiện đã có tiền lệ; phần còn thiếu là bảo toàn các thuộc tính xác lập chất lượng của bằng chứng khi đi qua chuỗi tới cấu kiện và hồ sơ.
- **K3 — Từ bằng chứng có phạm vi hiệu lực đến trạng thái hành động có thể giải trình.** Phần còn thiếu là truy ngược trạng thái của một hành động về đúng căn cứ kỹ thuật, khi căn cứ đó mang theo phạm vi hiệu lực và lịch sử xử lý.

Tiền lệ bắt buộc phải trừ trước khi phát biểu phần còn lại (CLAUDE.md mục 6.1): BCF 3.0; IFC4 IfcActionRequest / IfcProjectOrder / IfcTask / IfcApproval / IfcPerformanceHistory; SSN Deployment và IFC Monitor [2]; García 2026 [44]. Quy tắc phản chứng và ngưỡng ≥3 căn cứ ngoài nhóm 2025–2026: `project-canon-tltq.md` §5–6.

## The three gaps — historical 17/07 Claim wording (kept for comparison)

Do not rename these, do not add a fourth, do not loosen the wording.

### Gap 1 — Condition-evidence qualification gap

**Claim.** Trong phạm vi tập tài liệu được rà soát, bằng chứng dao động dùng để phân biệt trạng thái liên kết bu lông trên khung thép chưa luôn được đánh giá trên đơn vị độc lập vật lý, chưa luôn có kiểm soát rò rỉ dữ liệu ở dạng tường minh, và chưa luôn được báo cáo kèm phạm vi hiệu lực đã kiểm chứng.

**Touches this gap when a new paper reports:** unit-of-analysis / pseudoreplication in vibration-based bolted-connection classification on steel frames; data-leakage taxonomy or detection methods for this exact application; run-aware or session-aware train/test splitting for this exact application; validity-scope reporting for condition-evidence claims.

### Gap 2 — Component-level traceability gap

**Claim.** Trong phạm vi tập tài liệu được rà soát, bằng chứng hiện có chưa cho thấy một chuỗi định danh kiểm chứng được nối từ bằng chứng trạng thái tới cấu kiện có định danh trong mô hình thông tin và tới hồ sơ kiểm tra, trong đó cả ba mắt xích đều có định danh ổn định và quan hệ giữa chúng được kiểm chứng.

**Touches this gap when a new paper reports:** GUID/identifier persistence across model versions or software tools; sensor-to-BIM-element linkage; inspection-record-to-component linkage with its own identifier; bidirectional lookup with verified data equivalence at both ends; provenance/versioning applied to condition evidence specifically (not just to design/construction-phase BIM exchange).

### Gap 3 — Evidence-to-action gap

**Claim.** Trong phạm vi tập tài liệu được rà soát, bằng chứng hiện có chưa cho thấy một sự nối tiếp minh bạch từ một bằng chứng đã qualification tới trạng thái của một hành động kiểm tra, trong điều kiện dữ liệu hư hỏng hiện trường hạn chế.

**Touches this gap when a new paper reports:** action-status as a timestamped, queryable event chain (not just a current-state field); reviewer identity/role/rationale/approval encoded as data attached to the record (not just a software workflow step); a post-action verification record with an acceptance criterion and a verifier; a chain where the action's status traces back to the qualified evidence's own validity scope.

## Defense-level scale

- `STRONG` — no credible counter-evidence found after a real search.
- `NARROW_BUT_DEFENSIBLE` — real counter-evidence narrows the gap, but a specific, statable residue remains unaddressed by every source found so far. Đánh giá làm việc 01/10/2026 (`revision/GD2_phan_tich_khoang_trong_T1.md`): K1, K2, K3 đều NARROW_BUT_DEFENSIBLE; K2 có nguy cơ WEAK ở vế ánh xạ cảm biến – cấu kiện.
- `WEAK` — counter-evidence covers most of the claim; only a thin residue remains, and it may not survive one more good source.
- `NOT_DEFENSIBLE` — a source (or the combination of sources) already does what the gap claims is missing. Stop citing the gap as stated; escalate to the user immediately rather than silently softening the wording.

Never move a gap down more than one level from a single new paper. State the number of independent sources behind any level change.

## Verification-level scale (source strength, not gap strength)

`FULLTEXT_VERIFIED` (read the actual PDF passage) → `ABSTRACT_VERIFIED` (only abstract/metadata seen) → `DISCOVERY_ONLY` (found but not read at all). A gap-impact score built on anything less than `FULLTEXT_VERIFIED` must be labeled a candidate, not a confirmed narrowing.

## Prohibited as an allowed-usage-location, regardless of what the new source does

Field damage diagnosis; lab-to-field classifier transfer; predictive maintenance; remaining useful life (RUL); damage severity index (DSI); optimal sensor placement as a contribution; autonomous maintenance decisions; calibrated FEM used for diagnosis; a weighted Health Index; claiming compliance with ISO 19650, TCVN 14177, or any IFC clause from a secondary academic source instead of the original standard text.
