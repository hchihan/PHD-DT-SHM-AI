# DANH SÁCH EVIDENCE GAPS — CHUYÊN ĐỀ TỔNG QUAN
**Phiên bản:** v1 | **Ngày:** 18/07/2026 | **Kiến trúc:** Limited-FEM

---

## 1. Các phần đã có đủ tài liệu cơ bản

| Phần | Trạng thái | Ghi chú |
|---|---|---|
| Ch.2 — Định nghĩa DT, phân biệt BIM/DM/DS/DT | Đủ cơ bản | Kritzinger et al., Fuller et al., Boje et al. có sẵn; cần xác minh thêm nguồn cho construction-specific DT maturity |
| Ch.3.1 — Vibration-based monitoring tổng quan | Đủ | Avci et al. (2021) review paper là nguồn chính |
| Ch.3.2 — Bolted connection classification lab | Đủ cơ bản | Zhang/Biswal/Wang (2020), Eraliev et al. (2022), Ramasso et al. (2024); có 3+ nguồn substantive |
| Ch.4.1 — Sensor-BIM linking concept | Đủ cơ bản | Rio et al. (2013), Theiler & Smarsly (2018), Valinejadshoubi et al. (2019) |
| Ch.5.4 — FEM role (nominal, reference-only) | Đủ lập luận | Lập luận từ Research Direction and Scope + Charter; literature FEM-SHM có sẵn để đối chiếu |

---

## 2. Các phần còn yếu — cần tìm thêm tài liệu

| Phần | Mức độ thiếu | Tài liệu cần tìm thêm |
|---|---|---|
| Ch.2.2 — DT maturity trong construction | **YẾU** | Cần nguồn cụ thể cho phân loại mức trưởng thành DT trong AEC/construction (không chỉ manufacturing). Đã ghi nhận trong UNRESOLVED_ITEMS. |
| Ch.3.4 — Data leakage trong SHM vibration | **YẾU** | Cần thêm nguồn chứng minh leakage là vấn đề phổ biến trong vibration-based SHM classification (không chỉ general ML literature). |
| Ch.3.5 — Sensor config vs model choice | **TRUNG BÌNH** | Cần thêm nguồn so sánh ảnh hưởng của sensor configuration với model architecture choice trong vibration SHM. |
| Ch.3.6 — Small-n uncertainty trong SHM | **YẾU** | Cần nguồn về uncertainty quantification khi số run nhỏ; group-preserving permutation methodology. |
| Ch.4.2 — Condition_Evidence_ID concept | **YẾU** | Khái niệm evidence ID chưa được hình thức hóa trong literature; cần tìm các nghiên cứu gần nhất. |
| Ch.4.3 — Competency questions methodology | **YẾU** | Cần nguồn cho competency questions trong construction/BIM ontology — đã ghi nhận trong UNRESOLVED_ITEMS. |
| Ch.4.3 — Data provenance trong BIM/IoT | **TRUNG BÌNH** | Cần thêm nguồn về provenance tracking trong IoT-BIM integration. |
| Ch.4.5 — Low-cost sensor qualification | **TRUNG BÌNH** | Cần nguồn về tiêu chí đánh giá chất lượng cảm biến giá rẻ cho field SHM. |
| Ch.4.6 — Operational baseline methodology | **YẾU** | Cần nguồn về xây dựng baseline vận hành cho industrial steel buildings (phần lớn literature là bridge/wind turbine). |
| Ch.5.1–5.2 — Evidence-to-action framework | **TRUNG BÌNH** | Cần thêm nguồn về human-in-the-loop decision support cho inspection prioritization (không chỉ bridge SHM). |
| Ch.5.2 — Inspection record management | **YẾU** | Cần nguồn về quản lý hồ sơ kiểm tra trong asset management/facility management có liên kết với SHM data. |

---

## 3. Claim chưa được phép viết mạnh

| Claim | Lý do | Hành động cần thiết |
|---|---|---|
| "Không có nghiên cứu nào tích hợp toàn chuỗi vibration → evidence → BIM → inspection → action" | Chưa có systematic proof; chỉ dựa trên tập rà soát ban đầu | Dùng: "Trong phạm vi tập bằng chứng đã rà soát..." và kiểm chứng lại trong báo cáo |
| "Sensor configuration ảnh hưởng mạnh hơn model choice" | Chỉ có bằng chứng lab ban đầu (Gate 1 chưa khóa); LORO chưa chạy | Chờ kết quả Gate 1 trước khi tuyên bố; trong tổng quan chỉ nêu giả thuyết |
| "Run-aware evaluation làm giảm đáng kể accuracy so với random split" | Cần kết quả LORO chính thức; hiện chỉ là dự kiến | Chờ Gate 1; trong tổng quan nêu rủi ro leakage, không khẳng định con số |
| "CEI là chỉ số tin cậy bằng chứng" | CEI được đề xuất trong luận án; chưa có literature validation | Nêu là đề xuất, không phải khái niệm đã được chấp nhận |
| "FEM danh nghĩa đủ cho luận án Quản lý xây dựng" | Lập luận logic, không phải bằng chứng thực nghiệm | Trình bày lý do tại sao Limited-FEM phù hợp với định vị ngành |
| "Bốn mức hành động là đủ cho decision support" | WP4 chưa triển khai; kịch bản validation chưa có | Nêu là đề xuất kiến trúc; cần kiểm chứng tại Gate 5 |

---

## 4. Khoảng trống có thể phát triển thành Paper

| Khoảng trống | Paper tiềm năng | Trạng thái |
|---|---|---|
| Classification studies thiếu run-aware leakage control + sensor config evaluation | **Paper 1** (đã lên kế hoạch) | Gate 1 đang chờ: run registry → LORO → ResNet1D sensor mode |
| AI output dừng ở label, chưa trở thành traceable condition evidence gắn BIM | **Paper 2** (đã lên kế hoạch) | Concept note đã có; competency questions chưa phê duyệt |
| Field anomaly thiếu baseline, provenance và inspection confirmation | **Paper 3** (đã lên kế hoạch) | Phụ thuộc thỏa thuận tiếp cận công trình thực |
| Decision-support frameworks thiếu transparent evidence-to-action history | **Paper 4** (optional/support) | WP4 synthesis; không có RQ4 riêng |
| Chưa có chuỗi tích hợp vibration → evidence → BIM → inspection → action | **Đóng góp tổng thể của luận án** | Tổng hợp từ 4 papers |

---

## 5. Hành động ưu tiên để bổ sung evidence

1. **Ưu tiên cao:** Tìm thêm nguồn về data leakage / run-aware evaluation trong vibration-based SHM (Ch.3.4). Từ khóa: "data leakage" + "structural health monitoring", "leave-one-run-out", "grouped cross-validation" + "vibration".
2. **Ưu tiên cao:** Tìm nguồn về DT maturity classification trong construction/AEC (Ch.2.2). Từ khóa: "digital twin maturity" + "construction" OR "AEC" OR "built environment".
3. **Ưu tiên cao:** Tìm nguồn về competency questions methodology trong BIM/construction ontology (Ch.4.3). Từ khóa: "competency questions" + "BIM" OR "ontology" + "construction".
4. **Ưu tiên trung bình:** Tìm nguồn về operational baseline cho industrial steel buildings (Ch.4.6).
5. **Ưu tiên trung bình:** Tìm nguồn về inspection record management có liên kết SHM data (Ch.5.2).
6. **Ưu tiên thấp:** Bổ sung nguồn về low-cost sensor qualification (Ch.4.5) và provenance tracking trong IoT-BIM (Ch.4.3).

---

*Ghi chú: Danh sách này dựa trên tập bằng chứng đã rà soát (Living Evidence Base v1.1). Sẽ được cập nhật khi có kết quả tìm kiếm bổ sung.*
