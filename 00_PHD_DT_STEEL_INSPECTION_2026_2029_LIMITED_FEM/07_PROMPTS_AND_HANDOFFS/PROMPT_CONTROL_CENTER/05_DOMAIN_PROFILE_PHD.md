# DOMAIN PROFILE — PHD DT LIMITED-FEM

Chỉ dùng file này khi nhiệm vụ thuộc luận án NCS.

## Định vị

- RQ1/WP1/Chương 4/Paper 1: laboratory vibration evidence — Gate 1.
- RQ2/WP2/Chương 5/Paper 2: component-level traceability — Gate 2–3.
- RQ3/WP3/Chương 6/Paper 3: field feasibility — Gate 4.
- WP4/Chương 7/Paper 3 hoặc 4: inspection-maintenance support — Gate 5.

## Chuỗi nghiên cứu

`Vibration data → condition/state-change evidence → BIM-linked component → inspection record → inspection-maintenance action support`

## Chuỗi định danh

`Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Status`

`FEM_Node_ID` chỉ là metadata tùy chọn.

## FEM

Nominal, uncalibrated, reference-only, not used for damage diagnosis.

## Phạm vi cấm tự mở rộng

CFD, Smart City, Edge AI, RUL, predictive maintenance, field damage diagnosis, calibrated FEM, stiffness-degradation inference, complex weighted Health Index, autonomous maintenance và commercial software development.

## Cấu trúc phân tích

`Claim → Evidence → Limitation → Next action`

Khi bằng chứng chưa đủ:

`Evidence is currently insufficient.`

## Ưu tiên hiện tại

Gate 1:
- run registry;
- leakage-safe run-aware/LORO evaluation;
- xác nhận sensor mode của ResNet1D.
