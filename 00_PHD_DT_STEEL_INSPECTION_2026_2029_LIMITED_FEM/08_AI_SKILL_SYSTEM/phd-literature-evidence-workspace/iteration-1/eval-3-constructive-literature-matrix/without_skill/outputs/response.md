# Literature Matrix cho Related Work — Paper 2
## Trục: `Inspection_Record` và `Action_Record` trong asset management

**Ngày lập:** 2026-08-10
**Phạm vi:** RQ2 → WP2 → Chương 5 → Paper 2 → Gate 2/3
**Trạng thái:** công cụ làm việc (working artifact) — **không phải** tuyên bố Gate 2 PASS, không phải tuyên bố "chưa ai làm trên thế giới".

---

## 0. Cách tôi dựng ma trận này (đọc trước khi dùng)

Tôi **không** đi tìm nguồn mới. Tôi đọc lại đúng những gì repo của anh/chị đã deep-read và screening rồi **tái cấu trúc lại thành ma trận theo chiều "prior art density"**, vì câu hỏi thật của anh/chị là: *chỗ nào đã đông, chỗ nào còn mỏng*. Nguồn tôi dùng:

| Nguồn trong repo | Vai trò |
|---|---|
| `...\02_EVIDENCE_BASE\RQ2_GATES2_3\G2_G3_ROUND1_DEEP_READ_AND_NOVELTY_BOUNDARY.md` | Bellon, Antunes, Lee Y.-C., Oraskari |
| `...\02_EVIDENCE_BASE\RQ2_GATES2_3\G2_G3_ROUND2_INSPECTION_ACTION_MODEL_DEEP_READ.md` | Sacks, Xu, Wan, Isailović |
| `...\02_EVIDENCE_BASE\RQ2_GATES2_3\G2_G3_ROUND3A_NOVELTY_AND_SCHEMA_BOUNDARY.md` | Li, Piras, Nuyts, Hagedorn |
| `...\02_EVIDENCE_BASE\RQ2_GATES2_3\G2_G3_ROUND3B_HISTORY_ACCOUNTABILITY_AND_SEARCH_CLOSURE.md` | Mohamed, Celik + bảng so sánh chéo R1–R3B |
| `...\02_EVIDENCE_BASE\RQ2_GATES2_3\ROUND4_VERIFIED_EVIDENCE_RECORD_v1.1.md` | Keet & Khan, Kim, Jia, Lee D., Pauwels & Terkaj |
| `...\02_EVIDENCE_BASE\RQ2_GATES2_3\G2_G3_RECENT_EVIDENCE_SCREENING_2023_2026.md` | vành ngoài 13 ứng viên 2023–2026 |
| `...\02_EVIDENCE_BASE\CURRENT\01_MASTER_G1_G2_G3_EVIDENCE_SYNTHESIS_20260804.md` | chuỗi nghiên cứu chính thức |

**Ký hiệu ô (giữ nguyên kỷ luật bằng chứng của repo):**

| Ký hiệu | Nghĩa |
|---|---|
| ● | Có, được **mô tả rõ + triển khai + có locator** trong bài |
| ◐ | Một phần — có ở mức UI / process / narrative / thuộc tính rời, **chưa** đạt semantics đang xét |
| ○ | Không có bằng chứng trong bài |
| **?** | `Evidence is currently insufficient` — không đọc được full text, **không** kết luận là thiếu |
| — | Ngoài phạm vi bài (domain-neutral) |

**Cột trạng thái kiểm chứng:** `DR` = deep-read có locator trang; `FT` = đã soi full text mức screening; `PW` = paywall/không có attachment.

**Nguyên tắc số 1 của ma trận này:** ô ○ nghĩa là *"không tìm thấy trong corpus đã đọc"*, **không** phải *"không tồn tại trong văn liệu thế giới"*. §6 nói rõ chỗ nào cái "mỏng" có thể là mỏng giả.

---

## 1. Ma trận A — Lớp định danh và bản ghi (identity & record layer)

| # | Nguồn | KC | A1 Component identity (BIM anchor) | A2 Nội dung condition evidence | A3 Provenance của evidence (source ID/version/quality/agent) | A4 `Inspection_Record` có ID ổn định | A5 `Action_Record` có ID ổn định | A6 Quan hệ tường minh Inspection→Action (khóa + cardinality) |
|---|---|---|---|---|---|---|---|---|
| 1 | Sacks et al. (2018) SeeBridge | DR | ● IFC4 MVD, 4 mô hình cầu | ● `Defect`/`ElementDefect` + geometry + ảnh đăng ký | ◐ ảnh/point cloud nhưng **không** hash/thiết bị/thời điểm/confidence | ◐ có assignment + signing, **không** entity ID | ○ chỉ Treatment Library + alternatives | ○ chỉ chuỗi process |
| 2 | Wan et al. (2019) BMS | DR | ◐ mã cấu kiện + QR | ● `Pset-diseasetype`, crack length/width | ◐ text/ảnh/report, không schema metadata | ◐ project/template/upload | ◐ `Program NO.` là cột UI, không có kiểu dữ liệu/uniqueness | ◐ chuỗi thao tác, không có FK |
| 3 | Isailović et al. (2020) | DR | ● `IfcRelVoidsElement` tới host | ● `IfcSurfaceFeature(DAMAGE)` + catalog code + severity | ◐ point cloud ở mức case, không per-finding | ● `IfcTask` + `IfcTaskTime` + type | ○ không có action entity | ○ |
| 4 | Xu et al. (2022) | PW | ? | ? | ? | ? | ? | ? |
| 5 | Bellon et al. (2025) | PW | ? | ? (abstract nói damage report) | ? | ? | ? (nói maintenance services + costs) | ? |
| 6 | Lorvão Antunes et al. (2024) | DR | ● PhysicalObject → ifcOWL → `GlobalId` | ● Observation/Result, indicator 1–5, photo URL | ◐ `Agent` + `prov:atTime`, không có run/version/quality | ● `Inspection` là `Procedure` có `prov:atTime` | ○ **không có action entity** | ○ |
| 7 | Kim et al. (2018) | DR | ◐ dùng **số instance IFC** `#31982`, không `GlobalId` | ○ chỉ text công việc, không có defect object | ○ | ○ (bản ghi là công việc, không phải kiểm tra) | ◐ có Date/Area/Elements/Work contents/Labors/Work time — **không** ID/owner/approval | ○ |
| 8 | Li et al. (2023) | FT/DR | ◐ component key một phần | ● defect ID sinh tự động, ảnh, form | ◐ form/photo/DB statement | ○ | ◐ có repair record lưu trữ, không có Action ID chuẩn | ◐ defect → recommendation → repair, không công bố khóa |
| 9 | Mohamed et al. (2023) BrIM | DR | ● `CO-6`, `DE-19`, `GI-41`, `EJ-5` | ● defect card + ảnh + kích thước + vị trí | ◐ ảnh/report/cause/date; **có cross-view inconsistency** | ○ có date/type/report nhưng **không** record ID | ○ chỉ nhãn `Routine Maintenance (2-3-2022)` | ◐ inspection analysis → recommendation, không FK |
| 10 | Piras et al. (2026) | FT/DR | ● **giữ `IfcGlobalId`** khi import 428 asset sang OpenMAINT | ◐ current condition + last check | ◐ source mapping + processing log | ○ | ○ chỉ **capability** work-order, không có instance | ○ |
| 11 | Celik et al. (2023) | DR | ◐ `address objectID` | ○ | ◐ actor/time/version/hash generic | ○ | ○ | ○ |
| 12 | Lee, D. et al. (2021) | DR | ◐ brick ID | ○ | ● tách attestation khỏi payload (nguyên lý) | ○ | ○ | ○ |
| 13 | Lee, Y.-C. et al. (2021) | DR | ● GUID length 22 + uniqueness rule | ○ | ○ | ◐ "Product Inspection" chỉ là tên COBie exchange model | ○ | ○ |
| 14 | Oraskari et al. (2021) | DR | ● GUID matching source↔LBD | ○ | ○ | ○ | ○ | ○ |
| 15 | Hagedorn et al. (2023) ICDD | FT/DR | ◐ typed link identifier | ○ | ◐ ICDD link metadata | ○ | ○ | ○ (link construction task, không phải maintenance) |
| 16 | Nuyts et al. (2024) | FT/DR | ◐ component ID trong fixture | ○ | ○ | ○ | ○ | ○ |
| 17 | Jia et al. (2025) | DR | ◐ cá thể IfcOWL | ○ (design compliance) | ○ | ○ | ○ | ○ |
| 18 | Pauwels & Terkaj (2016) | DR | — | — | — | — | — | — |
| 19 | Keet & Khan (2025) | DR | — | — | — | — | — | — |

---

## 2. Ma trận B — Lớp vòng đời, trách nhiệm giải trình, nghiệm thu

| # | Nguồn | B1 Current `Workflow_Status` | B2 `Status_Event` append-only (prev/new + actor + time + reason) | B3 Authorization có trách nhiệm (approve/reject, RBAC, SoD) | B4 `Verification_Record` sau hành động | B5 Closure/reopen có guard |
|---|---|---|---|---|---|---|
| 1 | Sacks (2018) | ◐ `QC pass` là nhánh BPMN, không persisted | ○ | ◐ có Bridge QC Engineer + Inspection Signing, **không** record/ID/timestamp | ○ (QC là **trước** hành động) | ○ |
| 2 | Wan (2019) | ◐ progress tracking được khẳng định, không có enum | ○ | ◐ manager data check + repair-result check | ◐ qualified/not-qualified ở mức UI, **không** criteria/verifier/evidence | ○ |
| 3 | Isailović (2020) | ○ snapshot as-is có ngày | ○ | ○ | ○ | ○ |
| 4 | Xu (2022) | ? | ? | ? | ? | ? |
| 5 | Bellon (2025) | ? | ? | ? | ? | ? |
| 6 | Antunes (2024) | ◐ chỉ lấy latest bằng `MAX(?time)` | ○ | ○ | ○ | ○ |
| 7 | Kim (2018) | ○ | ○ | ○ | ○ | ○ |
| 8 | Li (2023) | ● cờ `completed` | ○ | ○ (trường Recorder/Reviewer **để trống**) | ○ | ○ |
| 9 | Mohamed (2023) | ● `Status: not treated` + condition level | ○ history là **danh sách report**, không phải event sequence | ○ (authority quyết định ngày ở mức khái niệm) | ○ | ○ |
| 10 | Piras (2026) | ● `Condition` + last check | ○ | ○ | ○ | ○ |
| 11 | Celik (2023) | ○ | ◐ tuple `operation-time-model-version-objectID-owner`, **không** prev/new state, không reason, không event ID | ◐ user/role administration + authenticator narrative, **không** approve/reject record, không SoD | ○ (verification là provenance verification) | ○ |
| 12 | Lee, D. (2021) | ○ | ◐ block chain có timestamp + Merkle root (generic) | ○ đồng thuận mật mã ≠ phê duyệt của con người | ○ | ○ |
| 13 | Lee, Y.-C. (2021) | ○ | ○ | ○ | ○ | ○ |
| 14 | Oraskari (2021) | ○ | ○ | ○ | ○ | ○ |
| 15 | Hagedorn (2023) | ○ | ○ | ○ | ○ | ○ |
| 16 | Nuyts (2024) | ○ | ○ | ○ | ○ | ○ |
| 17 | Jia (2025) | ○ | ○ | ○ | ○ | ○ |
| 18 | Pauwels & Terkaj (2016) | — | — | — | — | — |
| 19 | Keet & Khan (2025) | — | — | — | — | — |

---

## 3. Ma trận C — Lớp kiểm chứng

| # | Nguồn | C1 Executable constraints | C2 Fixture sai có chủ đích + oracle chính xác | C3 CQ registry / truy vấn xuôi đã chạy | C4 Truy vấn ngược / round-trip parity | C5 Mức validation |
|---|---|---|---|---|---|---|
| 1 | Sacks (2018) | ● mandatory/optional + omission check (mvdXML, XBIM) | ○ | ○ | ○ | Expert workshop + conformance 4 mô hình |
| 2 | Wan (2019) | ○ | ○ | ○ | ○ | 1 case, phản hồi định tính |
| 3 | Isailović (2020) | ◐ yêu cầu quan hệ IFC, không có validator chạy | ○ (miss/false detection là lỗi thực nghiệm) | ○ | ○ | 1 cầu, so baseline thủ công |
| 4 | Xu (2022) | ? | ? | ? | ? | ? |
| 5 | Bellon (2025) | ? (Highlights tuyên bố validated) | ? | ? | ? | ? |
| 6 | Antunes (2024) | ○ (SHACL/SWRL là future work) | ○ (chỉ OOPS! pitfall scan) | ● CQ1–CQ13, `GetInspectionResult` chạy thật | ○ | Pilot đường cao tốc EU |
| 7 | Kim (2018) | ○ (reasoning là phân loại BOSSAM) | ○ | ◐ SPARQL ad hoc, không có registry | ○ | 1 case, 590 bản ghi, **model là file mẫu** |
| 8 | Li (2023) | ○ | ○ | ◐ | ○ | 1 case |
| 9 | Mohamed (2023) | ○ | ○ | ◐ điều hướng UI | ○ | 1 cầu, demonstration |
| 10 | Piras (2026) | ● IFC validation đã chạy | ○ | ◐ tra cứu GUID hai chiều bằng mắt | ◐ visual lookup, **không** write-back | 1 case, 428 asset |
| 11 | Celik (2023) | ◐ smart contract require/revert | ○ (không có tamper test) | ◐ query capability, **không** công bố kết quả trả về | ○ | Kovan/Ganache, đo gas |
| 12 | Lee, D. (2021) | ◐ compliance = vị trí + loại gạch | ◐ **gieo 3/10 node sai chữ ký, có expected outcome** — nhưng là tính hợp lệ node, không phải bản ghi domain | ○ | ○ | Mô phỏng, cảm biến giả định |
| 13 | Lee, Y.-C. (2021) | ● 4 họ rule: uniqueness / reference / semantic / syntax, có report PASS-FAIL | ○ (lỗi thật, không có manifest + expected) | ○ | ○ | Conformance thực thi |
| 14 | Oraskari (2021) | ● SHACL-SPARQL, Listings 1–6 | ○ | ○ | ◐ chỉ IFC→LBD, không có LBD→IFC | Feasibility/unit test |
| 15 | Hagedorn (2023) | ● SHACL cross-document + inferred direct/inverse | ○ | ○ | ◐ direct/inverse link, **không** parity oracle | Benchmark dataset |
| 16 | Nuyts (2024) | ● nhiều validator | ● **fixture compliant/non-compliant có chủ đích, output lưu lại** — nhưng không có oracle so khớp tập vi phạm chính xác | ○ | ○ | So sánh nhiều công cụ |
| 17 | Jia (2025) | ● Jena rules + SPARQL trên Fuseki, đã chạy | ○ (2 railing 900 mm là dữ liệu thật, không gieo) | ○ | ○ | 1 công trình 21 tầng |
| 18 | Pauwels & Terkaj (2016) | **Đóng góp phủ định:** `RULE`/`FUNCTION` EXPRESS **không** chuyển được sang OWL2 DL; `WHERE` rule **không** nằm trong conversion (2 RULE + 45 FUNCTION trong IFC4_ADD1) | — | — | — | Converter đã triển khai |
| 19 | Keet & Khan (2025) | — | — | ● thẩm quyền phương pháp: 5 loại CQ; **CQ ≠ constraint-checking query**; 4 nguyên nhân CQ hỏng; ROCQS 558 CQ | — | Không có đánh giá người dùng |

---

## 4. Bản đồ mật độ prior art — **chỗ nào đã đông, chỗ nào còn mỏng**

Đếm trên 19 nguồn deep-read (bỏ 2 nguồn `?` và 2 nguồn domain-neutral khỏi mẫu số khi cột không áp dụng):

| Chiều | ● | ◐ | ○/? | Mật độ | Hệ quả cho Paper 2 |
|---|---:|---:|---:|---|---|
| **C1** Executable constraints (SHACL/mvdXML/IDS/Jena) | **8** | 3 | 8 | 🔴 **RẤT ĐÔNG** | Không được claim "dùng SHACL/rule checking" là đóng góp |
| **A1** Component identity / BIM anchor | **7** | 8 | 4 | 🔴 **RẤT ĐÔNG** | `IfcGlobalId` linkage là prior art dứt khoát |
| **A2** Nội dung condition evidence gắn cấu kiện | **6** | 2 | 11 | 🔴 **ĐÔNG** | Defect type/location/extent/time/ảnh đã có tiền lệ mạnh |
| **B1** Current `Workflow_Status` (scalar) | **4** | 3 | 12 | 🟠 **KHÁ ĐÔNG** | `not treated` / `completed` / `Condition` đã có; đừng gọi là closed-loop |
| **C3** CQ / truy vấn xuôi | 2 | 4 | 13 | 🟡 **TRUNG BÌNH** | Phương pháp CQ không mới; cái mới chỉ có thể là registry phủ hết chuỗi |
| **A3** Provenance của evidence (source ID/version/quality) | **0** | 8 | 11 | 🟢 **MỎNG** | Có nhiều mảnh rời, chưa ai ghép thành lineage hoàn chỉnh |
| **A4** `Inspection_Record` có ID ổn định | **2** | 4 | 13 | 🟢 **MỎNG** | Chỉ Isailović (`IfcTask`) và Antunes (`Procedure`) đạt ● |
| **A5** `Action_Record` có ID ổn định | **0** | 4 | 15 | 🟢🟢 **RẤT MỎNG** | Không nguồn nào công bố Action ID có contract |
| **A6** Quan hệ tường minh Inspection→Action | **0** | 3 | 16 | 🟢🟢 **RẤT MỎNG** | Chỉ có chuỗi process/UI, không có khóa + cardinality |
| **B2** `Status_Event` append-only (prev/new + actor + time + reason) | **0** | 2 | 17 | 🟢🟢🟢 **TRỐNG** | Celik/Lee D. chỉ có provenance generic |
| **B3** Authorization có trách nhiệm (RBAC + SoD + rationale) | **0** | 4 | 15 | 🟢🟢🟢 **TRỐNG** | Chỉ có vai trò và bước "manager check" |
| **B4** `Verification_Record` sau hành động | **0** | 1 | 18 | 🟢🟢🟢 **TRỐNG** | Chỉ Wan có qualified/not-qualified ở mức UI |
| **B5** Closure/reopen có guard | **0** | 0 | 19 | 🟢🟢🟢 **TRỐNG TUYỆT ĐỐI** | Không nguồn nào có tiền điều kiện đóng hồ sơ |
| **C2** Fixture sai chủ đích + oracle chính xác | 1 | 2 | 16 | 🟢 **MỎNG** | Nuyts đã lấy mất "fixture generic"; oracle chính xác vẫn mở |
| **C4** Truy vấn ngược / round-trip parity | **0** | 3 | 16 | 🟢🟢 **RẤT MỎNG** | Toàn bộ corpus là forward-only |

### 4.1 Hình dạng của khoảng trống — một câu

> Prior art **rất dày ở nửa trái của chuỗi** (neo định danh cấu kiện + biểu diễn bằng chứng hư hỏng + công nghệ ràng buộc), và **mỏng dần rồi trống hẳn ở nửa phải** (bản ghi hành động có định danh → sự kiện trạng thái bất biến → phê duyệt có trách nhiệm → nghiệm thu sau hành động → đóng hồ sơ có điều kiện → truy ngược).

Đây chính xác là hình dạng mà một Related Work tốt nên trình bày: **không** kể lể theo thời gian, mà **kể theo mức độ mất dần bằng chứng dọc chuỗi**.

### 4.2 Ba cột "đông" mà anh/chị **phải chủ động nhường**

| Cột | Nguồn phải trích để nhường | Câu nên viết |
|---|---|---|
| BIM/IFC linkage của hồ sơ kiểm tra | Sacks 2018; Isailović 2020; Antunes 2024; Kim 2018; Piras 2026 | "Việc gắn hồ sơ kiểm tra/hư hỏng vào cấu kiện BIM đã được xác lập vững chắc; bài này không xem đó là đóng góp." |
| Rule/constraint checking | Lee Y.-C. 2021; Oraskari 2021; Hagedorn 2023; Nuyts 2024; Jia 2025; Wang 2024; Pauwels 2024; Cerovšek & Omar 2025 | "SHACL/IDS/mvdXML là công nghệ sẵn có; đóng góp nằm ở **nội dung** ràng buộc gắn với chuỗi, không ở ngôn ngữ ràng buộc." |
| Provenance actor-object-time-version | Celik 2023; Lee D. 2021; Jaskula 2025; Schuler 2025 | "Provenance tổng quát và sổ cái bất biến đã là prior art; cái còn thiếu là **ngữ nghĩa bảo trì** gắn vào các sự kiện đó." |

---

## 5. Vành ngoài — 12 nguồn mới ở mức screening (chưa deep-read)

Những nguồn này **chưa** đủ tư cách để điền ô trong Ma trận A/B/C. Chúng đứng ở Related Work như *bằng chứng chiều rộng*, không phải *bằng chứng chiều sâu*.

| Nguồn | DOI | Đóng góp theo screening | Vắng mặt theo screening | Vai trò trong Related Work |
|---|---|---|---|---|
| Jeon et al. (2023) BrIM BMS | `10.3390/buildings13092332` | Yêu cầu owner/manager/inspector, mã kiểm kê, ánh xạ thông tin kiểm tra | Không có work-order lifecycle, không verified closure | Đối thủ domain hạng 2 |
| Jeon et al. (2024) Health Index | `10.3390/buildings14124032` | **Quan sát cấp tình trạng SAU sửa chữa** | Không mã hóa quan hệ repair→inspection thành verification transaction | Nguồn duy nhất chạm B4 — phải trích khi lập luận gap nghiệm thu |
| Jaskula et al. (2025) blockchain CDE | `10.1061/JCEMD4.COENG-14852` | Yêu cầu lịch sử toàn vòng đời có trách nhiệm, chống sửa | Khái niệm; không có transition bảo trì, không test authorization | Hỗ trợ requirement cho B2/B3 |
| Schuler et al. (2025) ICDD inspection | `10.1007/978-3-031-84224-5_32` | Liên kết bằng chứng dị chủng từ thiết kế thử → kết quả (ISO 21597) | Không authorization, không closure, không negative link | Hỗ trợ mạnh cho A3 |
| Pauwels et al. (2024) | `10.1016/j.aei.2024.102426` | Kiểm tra yêu cầu ngữ nghĩa + hình học, có điều kiện invalid đã biết | Không phải mutation suite cấp chuỗi | Hỗ trợ C1/C2 |
| Wang et al. (2024) ifcOWL+SHACL | (Zotero `3II2WKLN`) | Chuyển WHERE rule của IFC sang SHACL/SPARQL | Không có bản ghi evidence-to-action | **Quan trọng:** đối trọng với Pauwels & Terkaj (2016) |
| Cerovšek & Omar (2025) IDS | `10.3390/buildings15152621` | 7 IDS check trên 5 công cụ, kết quả **phân kỳ** | Không phải oracle có thẩm quyền | Bằng chứng "checker không đáng tin tuyệt đối" |
| Cavieres-Lagos et al. (2024) | `10.3390/app14146209` | Trao đổi hai chiều Revit–Dynamo–Excel gắn condition record | Không action identity, không event history | Lấy mất "bidirectional exchange" khỏi novelty |
| Oliveira et al. (2024) EIR/LOIN | `10.36680/j.itcon.2024.014` | Yêu cầu thông tin theo mục đích cho FM | Không có work-order state, không closure | Hỗ trợ phương pháp đặc tả trường bắt buộc |
| Gao et al. (2024) GIS+BIM DT | `10.3390/buildings14123731` | WebGIS/WebBIM/CDE + JSON defect | Không có cross-system record ID | Bối cảnh hệ thống |
| Yang et al. (2025) DT monitoring | (Zotero `QMPFIBQX`) | Sensor→cloud→BIM, time series, alert | Dừng ở monitoring/alert | Ranh giới G1→G2 |
| Stolk & McGlinn (2020) | (Zotero `8HJN7D7E`) | SHACL từ OWL restriction | Không có bản ghi domain | Hỗ trợ C1 |

---

## 6. ⚠️ Ba cảnh báo phải xử lý trước khi coi "mỏng" là "gap"

Đây là phần tôi nghĩ có giá trị nhất trong cả tài liệu này.

### 6.1 Hai lỗ đen trong ma trận: Bellon (2025) và Xu (2022)

Hai nguồn này đang là `?` chứ không phải `○`. **Bellon et al. (2025)**, *IFC framework for inspection and maintenance representation in facility management*, `10.1016/j.autcon.2025.106157` — theo chính Round 1, đây là **đối thủ gần nhất về schema/workflow**, và Highlights tuyên bố đã implementation + validation. Nếu Bellon có `Action_Record` entity với ID và quan hệ tới inspection, thì **hai cột A5 và A6 sụp**, và central claim của Paper 2 phải viết lại.

**Đây là rủi ro đơn lẻ lớn nhất của Related Work Paper 2.** Đề nghị: lấy full text (ILL / liên hệ tác giả / ScienceDirect qua thư viện) **trước khi** viết đoạn novelty. Không được nộp bài với một `?` nằm đúng ô mà mình tuyên bố là gap.

### 6.2 "Mỏng" có thể là mỏng giả vì corpus bị bó trong văn liệu AEC/BIM

Corpus hiện tại gần như hoàn toàn nằm trong AEC/BIM/semantic web, và ~80% là **cầu**. Bốn cột đang "trống" (B2 status event, B3 authorization/SoD, B4 verification, B5 guarded closure) lại là những thứ **đã chín muồi từ lâu ở các văn liệu khác**:

| Văn liệu liền kề chưa được rà | Vì sao nguy hiểm cho claim gap |
|---|---|
| **CMMS/EAM + ISO 55000/55001, ISO 19650-3, MIMOSA CCOM/OSA-EAM** | Work order lifecycle (requested → planned → approved → executed → verified → closed) là **mô hình chuẩn công nghiệp** hàng chục năm. Nếu reviewer biết EAM, "Action_Record + Status_Event" nghe như đang phát minh lại bánh xe. |
| **Bridge/highway management systems thực địa** (AASHTOWare BrM/Pontis, Danbrø, KUBA) — tài liệu kỹ thuật, không phải journal | Có inspection record + work candidate + work order + hoàn công. Không nằm trong Scopus nên search journal-only bỏ sót. |
| **21 CFR Part 11 / ALCOA+ / GAMP 5 (electronic records + audit trail + e-signature)** | Đây **chính xác** là B2+B3+B5: bản ghi bất biến, chữ ký điện tử có định danh + thời gian + lý do, phân tách nhiệm vụ. Rất mạnh về mặt phương pháp. |
| **Nuclear/aviation inspection recordkeeping, RCM, MSG-3** | Chuỗi finding → disposition → corrective action → sign-off → close là bắt buộc theo quy định. |
| **W3C PROV-O / PAV, workflow provenance** | Đã có `prov:wasGeneratedBy`, `prov:Activity`, `prov:Agent`, qualified association — trùng nhiều với A3. |

**Khuyến nghị chiến lược:** *đừng* claim "chưa ai làm". Thay vào đó dùng khung mà repo đã dùng đúng: **"Trong phạm vi văn liệu AEC/BIM đã sàng lọc và deep-read..."** + một đoạn ngắn thừa nhận rằng lifecycle work-order và audit-trail là chuẩn mực trong EAM/quy định, và **đóng góp của Paper 2 là đưa các chuẩn mực đó xuống mức cấu kiện, gắn với condition evidence và kiểm chứng được**, chứ không phải phát minh chúng. Câu chuyện này **mạnh hơn** câu chuyện "gap trống", vì nó không thể bị một reviewer ngành EAM đánh sập.

### 6.3 Khoảng trống miền (coastal industrial steel building) — dùng thế nào cho đúng

Toàn bộ corpus là cầu bê tông/cầu đường; **không có nguồn nào** về nhà công nghiệp thép ven biển. Đó là một khoảng trống thật, nhưng **novelty theo miền là loại novelty yếu nhất** và reviewer thường bác. Cách dùng đúng: đặt miền ven biển làm **nguồn của yêu cầu** (ăn mòn tiến triển liên tục, kiểm tra theo chu kỳ ngắn, bằng chứng phân tán giữa nhiều đợt, cấu kiện lặp lại số lượng lớn ⇒ vì sao cần định danh bản ghi ổn định và lịch sử trạng thái), **không** làm đóng góp chính.

---

## 7. Từ ma trận → dàn ý Related Work (đề xuất)

Cấu trúc theo **mức mất dần bằng chứng**, không theo thời gian. Con số là ước lượng tải trích dẫn.

| § | Tiêu đề đề xuất | Thông điệp | Nguồn chính (≈) |
|---|---|---|---|
| 2.1 | Component-anchored condition information in BIM | Đã giải quyết; nêu để nhường | Sacks 2018; Isailović 2020; Wan 2019; Antunes 2024; Kim 2018; Piras 2026; Mohamed 2023 (7–9) |
| 2.2 | From inspection information to maintenance intent | Recommendation/repair plan đã có tiền lệ; **định danh hành động thì không** | Wan 2019; Mohamed 2023; Li 2023; Jeon 2023; Sacks 2018 (5–7) |
| 2.3 | Workflow state versus state history | Current scalar ≠ lịch sử sự kiện — đây là **trục lập luận chính** | Mohamed 2023; Li 2023; Piras 2026 (đối lập) vs. Celik 2023; Lee D. 2021 (generic) (5–6) |
| 2.4 | Provenance, accountability and authorization | Provenance generic đã có; **phê duyệt vận hành có trách nhiệm thì chưa** | Celik 2023; Lee D. 2021; Jaskula 2025; Schuler 2025; Antunes 2024 (5–6) |
| 2.5 | Verifying that maintenance actually closed the loop | Cột trống nhất; dùng Jeon 2024 làm mỏ neo trung thực | Wan 2019; Jeon 2024; Mohamed 2023 (3–4) |
| 2.6 | Validating information models: constraints, fixtures, queries | Công nghệ đã đông; oracle theo chuỗi + parity còn mỏng | Lee Y.-C. 2021; Oraskari 2021; Hagedorn 2023; Nuyts 2024; Jia 2025; Pauwels & Terkaj 2016; Keet & Khan 2025 (7–9) |
| 2.7 | Synthesis: what is settled, what is not | Đưa nguyên bảng mật độ §4 vào bài dưới dạng 1 figure/table | — |

**Gợi ý trình bày:** biến §4 thành **một heatmap duy nhất** (hàng = nguồn, cột = 15 chiều, màu = ●/◐/○). Đó là loại hình mà reviewer nhớ được, và nó tự nó làm luận cứ gap mà không cần một câu "no study has ever...".

---

## 8. Việc cần làm tiếp, theo thứ tự ưu tiên

1. **Gỡ `?` của Bellon et al. (2025)** — ưu tiên tuyệt đối. Trước khi có full text, mọi câu về A5/A6 chỉ được viết ở thì điều kiện.
2. **Gỡ `?` của Xu et al. (2022)** — `10.1061/(ASCE)CP.1943-5487.0001026`; abstract nói có quan hệ defect ↔ maintenance action.
3. **Chạy một vòng search bổ sung có chủ đích, hẹp** vào các văn liệu ở §6.2. Từ khóa đề xuất:
   - `("work order" OR "maintenance order") AND ("state model" OR "status transition" OR lifecycle) AND (asset management OR EAM OR CMMS)`
   - `("audit trail" OR "electronic signature") AND ("inspection record" OR "corrective action") AND (traceability OR accountability)`
   - `("corrective action" AND "verification of effectiveness") AND (record OR closure)`
   - `PROV-O AND (inspection OR maintenance OR "condition assessment")`
   - `ISO 55001 AND (information requirements OR traceability OR "asset register")`
   - `ISO 19650-3 AND (asset information model OR "information exchange" AND operation)`
   Mục tiêu **không** phải mở rộng corpus mà là **bảo vệ** claim: cần biết chuẩn mực bên ngoài AEC nói gì trước khi tuyên bố mỏng.
4. **Chuyển ma trận này thành file dữ liệu** (CSV/Sheets) với schema: `source_id, citation, doi, verification_status(DR/FT/PW), dimension_id, value(●◐○?), locator, note`. Một hàng = một ô. Như vậy bảng trong bài và heatmap được sinh ra từ cùng một nguồn, không lệch — và mỗi ô mang theo locator, đúng kỷ luật `Tên paper → PDF p. n [printed p. m] → section` mà Round 4 đã thiết lập.
5. **Viết §2.7 trước, §2.1 sau.** Kết luận tổng hợp quyết định cách kể phần trước nó.

---

## 9. Hai điều tôi cố ý **không** làm

- **Không** tự thêm nguồn ngoài repo vào ma trận. Những nguồn ở §6.2 tôi liệt kê là **hướng tìm**, không phải bằng chứng đã đọc; đưa chúng vào ô ma trận lúc này sẽ vi phạm đúng nguyên tắc mà repo đang giữ.
- **Không** nâng bất kỳ ô `?` nào thành `○`. Việc đó sẽ tạo ra một gap trông đẹp trên giấy nhưng có thể sai.

---

**Ghi chú AI:** Tài liệu này do AI hỗ trợ tổng hợp từ các báo cáo deep-read/screening có sẵn trong repository. Không có file nào trong repository bị sửa, xóa hoặc ghi đè. Mọi locator trang gốc nằm trong các báo cáo Round 1–4 được dẫn ở §0; ma trận này là lớp tổng hợp phía trên, **không** thay thế chúng làm nguồn bằng chứng.
