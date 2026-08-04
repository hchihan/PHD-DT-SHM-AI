# CHANGELOG — v2.1 (2026-07-19)
Thay đổi từ v1.1 (LIMITED-FEM, 17/07/2026) và v2.0 (Traceability-Core docx, 19/07/2026).

## Từ v1.1 → v2.0 (đã diễn ra trong Charter docx)
- Reframe RQ2 từ ngôn ngữ ontology-engineering sang traceability-to-decision với lăng kính quản lý.
- CEI nâng từ "by-product của Paper 1" thành first-class attribute của chuỗi định danh.
- Decision logic 4 mức kéo vào Paper 2 (application layer) thay vì để WP4/Paper 4.
- Legal mapping nâng từ "background context" thành neo QLXD ở cấp điều luật.
- Paper 3 (field) hạ từ "trụ cột chịu lực" xuống "bonus/stretch".
- FEM: giữ nguyên nominal, uncalibrated, reference-only.

## Từ v2.0 → v2.1 (bốn điều chỉnh học thuật bắt buộc)
1. **Field feasibility:** tách rõ **Paper 3 publication (optional)** vs **minimum field feasibility evidence (MANDATORY cho luận án)**. v2.0 mô tả toàn bộ field là "bonus" → v2.1 siết lại: evidence tối thiểu bắt buộc (field sensor register; Sensor_ID→BIM_GUID; data return & completeness; operational baseline; inspection-record workflow; 2–3 traceability scenarios). Không yêu cầu field damage diagnosis.
2. **Paper 1 claims:** mọi kết luận định lượng (sensor config dominates architecture; RF ~0.862 / 1D-CNN S12 ~0.841 / ResNet1D ~0.828; ResNet1D corroborates) chuyển thành **candidate**, ghi nhãn "Candidate claim pending Gate 1 closure" cho tới khi G1 đóng (run registry, split-before-windowing, LORO, preprocessing train-only, common seeds, run-level uncertainty, ResNet1D sensor-mode & provenance).
3. **CEI:** khóa định nghĩa là **cấu trúc metadata hạng nhất** (evidence validity status; model confidence; run/fold variability; sensor configuration; data-quality status; provenance; timestamp/version). **Không** mặc định thành weighted scalar/Health Index. Nếu chưa đủ bằng chứng: "Evidence is currently insufficient to define CEI as a universal scalar index."
4. **Legal mapping:** chỉ neo QLXD/nghĩa vụ quản lý/trách nhiệm; **không** suy ra ngưỡng hư hỏng, không tuyên bố mọi công trình bắt buộc quan trắc, không làm căn cứ chẩn đoán, không tự tạo ngưỡng Normal–Watch–Inspect–Priority từ luật. Mọi tham chiếu pháp lý chưa xác minh: "Legal reference pending official-source verification."

## Thay đổi cấu trúc file (governance)
- Tạo mới: Charter v2.1, matrix v2.1, evidence gates v2.1, ADR 20260719, source-of-truth hierarchy v2.1, AGENT_RULES.md, 3 paper direction v2.1, 3 report (system update, changelog, unresolved tracker).
- Cập nhật: README, concise charter, direction, architecture, terminology (+§5), CLAUDE.md, current status, master index.
- SUPERSEDED (giữ lại): Charter v1.1; ADR 20260717 → HISTORICAL; Charter v2.0 docx → HISTORICAL_DECISION_SOURCE.

## Bất biến (không đổi giữa v1.1 → v2.1)
- Chuỗi evidence và chuỗi định danh (chỉ thêm CEI tường minh + justified/accountable action ở đuôi).
- FEM nominal, uncalibrated, reference-only, not used for damage diagnosis.
- Không RQ/WP/chương/Paper/Gate FEM; `FEM_Node_ID` chỉ optional metadata.
- Danh mục Out of Scope (RUL, PdM, field diagnosis, Health Index phức tạp, calibrated FEM, CFD, Smart City, Edge AI, commercial DT, autonomous maintenance).
- Không sửa metric/citation/evidence khoa học.

## Acceptance / keyword check
Xem `UNRESOLVED_ITEMS_TRACKER_v2.1.md` và báo cáo cuối. Không còn RQ/WP/chương/Paper/Gate FEM trong file v2.1; `FEM_Node_ID` không xuất hiện trong chuỗi bắt buộc; Paper 2 = QLXD core; Paper 1 claims = candidate; CEI ≠ severity/Health Index; legal mapping không tạo ngưỡng kỹ thuật.
