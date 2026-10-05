# UNRESOLVED ITEMS TRACKER — v2.1
**Date:** 2026-07-19 | **Rule:** không mục nào được giải quyết bằng giả định; mỗi mục cần nguồn bằng chứng có tên hoặc quyết định của người dùng/thầy hướng dẫn.
Kế thừa `UNRESOLVED_ITEMS_CURRENT.md` (v1.1); file này là bản hiện hành v2.1.

## A. Nút chặn bắt buộc (blocking)

| # | Item | Vì sao chưa giải quyết | Chặn | Đường giải quyết |
|---|---|---|---|---|
| 1 | **Gate 1 chưa đóng** | LORO chưa chạy; run registry chưa khóa; run-level uncertainty chưa cập nhật | G1; Paper 1 claims | Khóa run registry → LORO (6 folds, common seeds) → uncertainty |
| 2 | **ResNet1D sensor mode & provenance** | Chưa xác nhận input sensor mode | G1 | Verify sensor mode vs run registry; không con số ResNet1D vào Paper 1 tới khi xong |
| 3 | **LORO stability** | Chưa có kết quả LORO leakage-safe | G1 (submission condition) | Chạy LORO trên registered runs; ghi kết quả + variability |
| 4 | **CEI operational definition** | CEI chưa được khóa thành cấu trúc metadata vận hành | G2 | Định nghĩa metadata fields; nếu chưa đủ: ghi "insufficient to define CEI as universal scalar index" |
| 5 | **Competency-question approval** | SCQ/VCQ/RCQ chưa pre-register/duyệt | G2, G3, G6 | Soạn + supervisor review + pre-register trước khi build schema/demo |
| 6 | **Official legal-reference verification** | Luật XD 135/2025; NĐ 207/2026/NĐ-CP; TT 32/2026/TT-BXD; QĐ 46/2026/QĐ-UBND Khánh Hòa; Công văn 3839 — chưa xác minh nguồn chính thức | Paper 2 legal mapping | Xác minh từng văn bản/điều bằng nguồn chính thức; tới khi đó ghi "Legal reference pending official-source verification" |
| 7 | **Field-access confirmation (Rapexco)** | Trạng thái ký chưa xác nhận | G4 (hard prerequisite) | Xác nhận thỏa thuận ký với chủ/vận hành công trình |
| 8 | **Minimum field-feasibility protocol** | Protocol tối thiểu (register, mapping, completeness/drift, baseline, scenarios) chưa khóa | G4 (mandatory evidence) | Predefine protocol; chỉ triển khai sau khi Paper 1–2 nộp |

## B. Mục kế thừa còn mở (v1.1)

| # | Item | Hành động |
|---|---|---|
| 9 | Inspection_Record minimum schema chưa duyệt | Soạn từ vocabulary 4LKDXFMK/GIIUUEW8 + quy định hồ sơ bảo trì VN; supervisor approval |
| 10 | Digital Twin maturity definition thiếu nguồn | OpenCode/Zotero deep-read; viết C3 subsection |
| 11 | Program regulations (nội dung kỹ thuật trong luận án QLXD) | Lấy quy định chính thức của chương trình đào tạo |
| 12 | AGENT_RULES/RESEARCH_CHARTER cũ (AI_SYSTEM/AGENTS) nếu còn | `AGENT_RULES.md` v2.1 tuyên bố thay vai trò; audit & supersede khi tiếp cận được |
| 13 | 3 full text RQ2 còn thiếu (3II2WKLN, NUTL57KJ, Z4IBWW9Y) | Thu thập trong phiên OpenCode/Zotero |
| 14 | Zotero writeback queue pending | Không sửa Zotero tới khi người dùng phê duyệt |

## C. Mục phát sinh từ đồng bộ v2.1 (phase 2, 2026-07-19)

| # | Item | Hành động |
|---|---|---|
| 15 | Action_Record schema chưa định nghĩa | Soạn schema: Action_Record_ID ↔ evidence/CEI/component/inspection/role/timestamp/version/approval/legal ref (G2) |
| 16 | Accountability đưa vào CQ + schema | Nhúng định nghĩa (Charter §2.4) vào SCQ/VCQ/RCQ và Inspection/Action_Record schema khi pre-register |
| 17 | G1 execution artifacts chưa tạo | Khởi tạo `05_DATA_CODE_AND_EXPERIMENTS/G1_EXECUTION_PACK/` (12 file template); điền khi có dữ liệu/code xác minh |
| 18 | Evidence-base & coursework còn notation `Action_Status`-in-chain | Reconcile sang Action_Record_ID khi các addenda/chuyên đề được revise chính thức (không sửa evidence lúc này) |
| 19 | Discovery prompts (07_PROMPTS) pre-v2 | Tái tạo từ v2.1 khi dùng lại |

## Claim → Evidence → Limitation → Next action
- **Claim:** 8 mục blocking + 6 mục kế thừa + 5 mục phase-2 đang mở; không mục nào được đóng bằng giả định.
- **Evidence:** Charter v2.1 §8/§12; EVIDENCE_GATES_v2.1; UNRESOLVED_ITEMS_CURRENT (v1.1).
- **Limitation:** legal + field-access + CQ nằm ngoài kiểm soát kỹ thuật đơn thuần (cần văn bản/phê duyệt).
- **Next action:** ưu tiên #1–#3 (đóng G1) song song #4–#5 (CEI + CQ); #6–#8 chuẩn bị nền.
