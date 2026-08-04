# PAPER 2 — CONCEPT / DIRECTION & GATE (v2.1)
**Version:** v2.1 | **Date:** 2026-07-19 | **Status:** CURRENT direction (dưới Charter v2.1)
**RQ2 · WP2 · Chapter 5 · Gates G2, G3, G6 · Target: Automation in Construction / J. Building Engineering / Building & Environment (verify rank)**

> **Paper 2 là TRỤ CỘT NHẬN DIỆN NGÀNH QUẢN LÝ XÂY DỰNG của luận án.** Đây là nơi thesis giành bản sắc ngành.

## RQ2 (câu gốc đã khóa)
"How can condition evidence and its confidence be organised and linked to BIM components and inspection records to enable verifiable justification and accountability of inspection decisions under limited field damage data?"

Không mở rộng sang: ontology engineering thuần túy, phần mềm thương mại, quyết định tự động, damage diagnosis, predictive maintenance, RUL, weighted Health Index.

## Ba thứ phải nhúng vào Paper 2 (bản sắc QLXD)
1. **CEI = first-class attribute của chuỗi.** Evidence được liên kết cùng độ tin cậy của nó, không liên kết trần → chuỗi evidence-weighted, phân biệt với IFC linkage thường. CEI là **cấu trúc metadata** (evidence validity status, model confidence, run/fold variability, sensor configuration, data-quality status, provenance, timestamp/version), **không** phải scalar/Health Index. Nếu chưa đủ bằng chứng cho chỉ số đơn: ghi "Evidence is currently insufficient to define CEI as a universal scalar index."
2. **RCQ — relationship/decision competency question.** "For a given action level, can the complete evidence, CEI, BIM component, inspection record and applicable management obligation be traced and verified?"
3. **Legal-mapping table.** Mỗi action level (Normal → Watch → Inspect → Priority) ánh xạ tới nghĩa vụ quản lý cụ thể theo điều. **Chỉ neo nghĩa vụ** (management obligation), không suy ra ngưỡng kỹ thuật, không tự tạo ngưỡng từ luật. Bốn state là **vị trí** (apex, BCJ, brace, healthy), không phải severity grade → DSI/ordinal bị cấm. Mọi tham chiếu pháp lý chưa xác minh: "Legal reference pending official-source verification." Legal mapping phục vụ justification & accountability (không phải trách nhiệm pháp lý cá nhân).

## Accountability (định nghĩa đã khóa — Charter v2.1 §2.4)
> Accountability = khả năng truy vết vai trò, nguồn bằng chứng, người/đơn vị tạo hoặc xác nhận hồ sơ, thời điểm, phiên bản và trạng thái phê duyệt của một quyết định quản lý. **KHÔNG** phải kết luận trách nhiệm pháp lý hoặc quy lỗi cá nhân.

Định nghĩa này phải xuất hiện nhất quán trong concept note, competency questions và schema.

## Identifier chain + Action_Record schema
Chuỗi: `Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Record_ID`. `Action_Status` là **thuộc tính** của `Action_Record_ID`. `Action_Record_ID` phải truy được: evidence (`Condition_Evidence_ID`), CEI, component (`BIM_GUID`), inspection record (`Inspection_Record_ID`), **role**, **timestamp**, **version**, **approval status**, và **management/legal reference áp dụng**. (ADR: `RESEARCH_ARCHITECTURE_DECISION_RECORD_ACTION_ID_20260719.md`.)

## Pre-registration (bắt buộc TRƯỚC khi build schema/demo)
SCQ / VCQ / RCQ + acceptance criteria + Inspection_Record minimum schema + Action_Record schema — pre-register (Gate 2). Không xây framework phức tạp trước khi CQ và acceptance criteria được duyệt.

## Gates
- **G2** — traceability model, CEI attribute, competency questions, acceptance criteria, Inspection_Record schema.
- **G3** — end-to-end lab demo: evidence → CEI → BIM component → inspection record → action; round-trip; orphan-ID / duplicate-ID / missing-CEI tests; invalid-data / SHACL-or-equivalent validation.
- **G6** — Paper 2 submission.

## Claim → Evidence → Limitation → Next action
- **Claim:** Paper 2 định hướng theo trục traceability-core, CEI hạng nhất, legal mapping chỉ neo nghĩa vụ.
- **Evidence:** Charter v2.1 §6–8; RQ2 addendum `../../90_ARCHIVE/SNAPSHOTS_20260718/BACKUP_BEFORE_WRITEBACK_20260718/04_RQ2_TRACEABILITY_EVIDENCE_ADDENDUM_v1.2_20260718.md`; evidence base groups B/C: `../../02_EVIDENCE_BASE/CURRENT/LIVING_EVIDENCE_BASE_v2.1_TRACEABILITY_CORE.md` (closest competitor XUN8EX6X; CQ taxonomy LSYSC59G; provenance EMTIHHX4; governance YGZ32C8M).
- **Limitation:** SCQ/VCQ/RCQ chưa pre-register; CEI operational definition chưa khóa; legal refs chưa xác minh; 3 full text RQ2 còn thiếu (3II2WKLN, NUTL57KJ, Z4IBWW9Y).
- **Next action:** pre-register CQ + acceptance criteria; formalise CEI metadata; draft Inspection_Record schema; draft legal-mapping table (với nhãn pending verification).
