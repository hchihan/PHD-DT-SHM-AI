# KEYWORD & CONFLICT CHECK REPORT
**Date:** 2026-07-19 | Scope kiểm tra: file dẫn hướng CURRENT (00_GOVERNANCE, 01_CURRENT_CONTROL, 03_PAPERS direction). Loại trừ: archive (99/90/92), evidence-base, coursework, discovery prompts, và Council decision doc (historical).

| Keyword | Kết quả trong file CURRENT | Ghi chú |
|---|---|---|
| FEM calibration / calibrated FEM | ✅ chỉ trong prohibited/exclusion | Charter §10, §2.3; EVIDENCE_GATES "gates không tồn tại" |
| MAC | ✅ chỉ trong "gates không tồn tại" | — |
| EMA | ✅ chỉ trong "gates không tồn tại" | — |
| stiffness degradation | ✅ chỉ trong prohibited | Charter §10 |
| optimal sensor placement | ✅ chỉ trong prohibited/"gates không tồn tại" | — |
| damage diagnosis | ✅ chỉ trong prohibited ("not used for damage diagnosis"; "không field damage diagnosis") | — |
| damage severity / DSI | ✅ chỉ trong prohibited | — |
| RUL | ✅ chỉ trong prohibited | — |
| predictive maintenance | ✅ chỉ trong prohibited | — |
| weighted Health Index | ✅ chỉ trong prohibited ("không phải scalar/Health Index") | — |
| autonomous maintenance | ✅ chỉ trong prohibited | — |
| **workstation-only** | ✅ PASS | Chỉ còn trong rule thay thế của TERMINOLOGY; không dùng làm live term |
| **Action_Status trong identifier chain** | ✅ PASS trong CURRENT | Mọi file CURRENT: Action_Status = thuộc tính của Action_Record_ID. Tồn dư ngoài scope: `THE_COUNCIL_REVIEW` (historical), `02_EVIDENCE_BASE/**`, `04_PHD_SPECIAL_TOPICS/**`, `07_PROMPTS/**` — giữ nguyên (không sửa evidence/lịch sử) |
| **v1.1 marked CURRENT** | ✅ PASS | v1.1 charter + ADR 20260717 = SUPERSEDED, đã archive vào 99_; không file nào dẫn v1.1 như CURRENT |
| **multiple source of truth** | ✅ PASS | Duy nhất Charter v2.1 là SoT cao nhất (xem SOURCE_OF_TRUTH_VALIDATION_REPORT) |

## FEM qualifier
Mọi lần nhắc FEM trong file CURRENT kèm "nominal, uncalibrated, reference-only, not used for damage diagnosis" hoặc tương đương. ✅

## Kết luận
Không phát hiện vi phạm keyword hay mâu thuẫn source-of-truth trong file dẫn hướng CURRENT. Tồn dư notation lịch sử nằm ngoài scope guidance (evidence/coursework/prompts/decision-doc) và được giữ nguyên theo quy tắc không sửa evidence.
