# Literature Matrix cho Related Work — Paper 2 (`Inspection_Record` / `Action_Record`)

**v1.0 · 2026-08-10 · read-only output, không sửa file nào trong thesis repository.**

```text
Declaration: RQ2 → WP2 → C5/Paper 2 → G2 (G3 execution NOT OPEN) → Scope: Core
```

---

## 0. Đọc bảng này như thế nào

**Corpus bound.** Toàn bộ ma trận dưới đây được dựng từ **19 nguồn đã deep-read** trong Rounds 1–4 (`02_EVIDENCE_BASE/RQ2_GATES2_3/`), cộng lớp screening 2023–2026. Mọi nhận định về "đông" hay "mỏng" đều mang giới hạn: **trong phạm vi corpus đã sàng lọc và deep-read**. Đây không phải systematic review.

**`CLOSE_SEARCH` đang có hiệu lực** (`G2_G3_ROUND3B_HISTORY_ACCOUNTABILITY_AND_SEARCH_CLOSURE.md`, §8). Ma trận này **không mở lại broad search**. Nếu anh muốn mở rộng discovery cho Related Work, đó là quyết định của người nghiên cứu, không phải của phân tích này — và tôi sẽ nói rõ ở §9 chỗ nào việc mở lại là hợp lý.

**Chỗ mỏng ≠ tính mới.** Cột "mật độ" ở §3 đo **prior art đã được xác lập trong corpus**, không đo tính mới. `Scarcity is not novelty`: một vùng mỏng chỉ trở thành gap claim khi có nguồn nói ra gap đó, hoặc có documented absence kèm corpus bound được nêu tường minh. §5 phân biệt hai loại này.

**Layer.** Toàn bộ 19 nguồn nằm ở **Layer 2 — information traceability**. Không nguồn nào trong ma trận này được dùng để chống đỡ claim của Layer 1 (lab), Layer 3 (field feasibility) hay Layer 4 (decision support).

**Trạng thái epistemic của Paper 2 khi viết Related Work.** Chuỗi G2 hiện ở **rung 2 — DESIGN** (`epistemic-ladder.md`). Related Work phải được viết ở ngôn ngữ "designs / proposes / is prepared for validation", không phải "implements / validates / demonstrates".

---

## 1. Literature matrix — sắp theo chain element

Sắp theo **chain element**, không theo năm. Lý do: lập luận đóng góp của luận án là lập luận **cấu trúc**, nên ma trận sắp theo mắt xích sẽ lộ ngay chỗ nào chật và chỗ nào trống.

Ký hiệu locator: `[Tác giả Năm, PDF p. n, §x]`. Locator gốc nằm trong Round report tương ứng; tôi ghi kèm Round để anh truy ngược.

### 1.1 Condition evidence / defect record gắn cấu kiện BIM

| Nguồn | Năm | Venue type | Xác lập điều gì | Chain element | Layer | Liên quan RQ2 | Giới hạn đối với luận án |
|---|---|---|---|---|---|---|---|
| Isailović et al., *Autom. Constr.* 112:103088 | 2020 | Q1 journal | Damage là BIM object có type/code, host-relative location, geometry-based extent, severity, inspection time; `IfcSurfaceFeature(DAMAGE)` → `IfcRelVoidsElement` → host `IfcElement` `[PDF pp. 6–9, 19, §§3.2.2.1–3.2.2.3, Figs. 7–9, 24–25]` (R2) | condition evidence | 2 | Bằng chứng toàn văn **mạnh nhất** cho defect/finding schema | Không có per-finding source provenance, confidence, processing version, reviewer identity. Không có action layer. Mesh phải phóng 100.5% để Boolean ổn định → geometry bị biến đổi `[PDF p. 13, §6.2]` |
| Sacks et al., *Autom. Constr.* 90:134–145 | 2018 | Q1 journal | `Defect`/`ElementDefect` trong IFC4, geometry + measurements + registered imagery (`IfcImageTexture`), nhúng trong exchange model `EM-4` `[PDF pp. 10, 15–18, §§4.4, 5.3, Fig. 8, Table 6]` (R2) | condition evidence | 2 | Formal inspection specification mạnh nhất (BPMN/IDM → MVD/mvdXML) | Không có source-file ID/hash, device, acquisition time, confidence, registration-error field. Không bind author/inspector vào finding |
| Wan et al., *Sustainability* 11(17):4583 | 2019 | Q2 journal | IFC Pset extension (`Pset-diseasetype`) nối cấu kiện với defect/reinforcement info; text/image/report gắn cấu kiện `[PDF p. 4, Tables 1–4; pp. 13, 15, §5.2.2–5.3]` (R2) | condition evidence | 2 | Precedent vận hành thực địa | Ngoài crack, defect properties chủ yếu Boolean. Color semantics không phải formal status; thresholds không công bố |
| Lorvão Antunes et al., *ISWA* 22:200366 | 2024 | Q2 journal | `Observation`/`Result` với condition indicator 1–5 hoặc descriptive state, inspection due date, photo URL, `Agent`, `prov:atTime` `[PDF p. 7, §5.2.3, Fig. 4; p. 8, Listing 4]` (R1) | condition evidence | 2 | Closest competitor về semantic linkage | Không có complete source/run/model-version/reviewer lineage. Không có Action_Record |
| Li et al., *Sci. Rep.* 13:846 | 2023 | Q1 journal | Defect ID tự sinh `<sequence>-<IFD code>` (vd. `1-68-10 10 10`); MySQL defect database; upload form có structure/component/location/type/parameter/scale/evidence file `[PDF p. 3 §Coding; pp. 11–12, Figs. 12–13]` (R3A) | condition evidence | 2 | Closest operational competitor cho defect-to-repair | Không nêu uniqueness scope, concurrency, immutability, taxonomy migration. **Mâu thuẫn nội bộ**: crack width 5 cm (Fig. 13) vs 2 cm (Fig. 12) |
| Mohamed et al., *Buildings* 13(11):2798 | 2023 | Q1 journal | Populated defect card: cause, image, comment, dimensions, component location; damage cubes `[PDF pp. 7, 13–15, §§3.4, 4.3.2, 4.4; Figs. 4, 10, 12]` (R3B) | condition evidence | 2 | Precedent mạnh cho populated inspection/defect display | **Không có stable defect ID**. Mâu thuẫn xuyên view: cùng expansion-joint ở `DE-19` (Figs. 8, 12) vs `EJ-5` (Fig. 14); spalling `800 mm` vs `400 mm` |
| Xu et al., *J. Comput. Civ. Eng.* 36 | 2022 | Q1 journal | — | condition evidence | 2 | Scope rất gần theo abstract | **`UNVERIFIED` ở mức chi tiết.** Zotero không có child attachment; full-text extraction trả `No suitable attachment found`. **Evidence is currently insufficient.** Không được trích entity/field từ abstract (R2 §2.2) |

### 1.2 Component identity / BIM anchor

| Nguồn | Năm | Venue type | Xác lập điều gì | Chain element | Layer | Liên quan RQ2 | Giới hạn đối với luận án |
|---|---|---|---|---|---|---|---|
| Piras et al., *Appl. Sci.* 16:4642 | 2026 | Q2 journal | `IfcGlobalId` được giữ làm CMMS unique asset identifier khi import 428 maintainable assets từ ~9000 IFC elements vào OpenMAINT; JSON mapping template `[PDF pp. 18, 22–24, §§2.4.2, 3.1.2–3.2.2; Tables 6–7]` (R3A) | component identity | 2 | **Closest competitor về BIM–CMMS identity** | Một chiều IFC→CMMS. Không test persistence qua IFC revision/replacement. Fig. 5 hiển thị 398 items không giải thích (vs 428). Không có work-order instance |
| Lee, Y.-C. et al., *JCDE* 8(1):97–114 | 2021 | Q1 journal | `IfcGloballyUniqueId` length 22 + within-file uniqueness; bốn rule families: uniqueness, reference existence, semantic accuracy, syntax `[PDF pp. 5, 8, §§4.1, 5.1.1–5.1.2]` (R1) | component identity + constraint | 2 | Validation kernel chuyển giao được | Không có permitted-character rule, regex, lifecycle persistence, cross-file/revision governance |
| Mohamed et al. | 2023 | Q1 journal | Element coding `CO-6`, `DE-19`, `GI-41`, `EJ-5` trong BrIM inventory `[PDF pp. 4, 9–10, §§3.1, 4.1, Fig. 6]` (R3B) | component identity | 2 | Component identity precedent | Không có uniqueness test, revision-stability policy, `IfcGlobalId` crosswalk |
| Hagedorn et al., *Autom. Constr.* 156:105106 | 2023 | Q1 journal | ICDD typed identifier resolution: string-based, URI-based, query-based; `StringBasedIdentifier` resolve tới IFC GUID `[PDF pp. 5–8, §§2.4–3.1, Fig. 4, Listing 1]` (R3A) | component identity | 2 | Precedent cho typed identifier resolution | Query-based identifier không được đánh giá. Không có uniqueness/stale-ID test |
| Li et al. | 2023 | Q1 journal | Ghép defect model với bridge model qua MySQL `ID attribute` sau Revit → IFC 2x3 → OBJ `[PDF p. 8, §Utilization]` (R3A) | component identity | 2 | Cho thấy **failure mode** của identity | **Cảnh báo trực tiếp**: tác giả tự nhận code hiện tại chưa định vị defect chính xác; OBJ làm mất native parameters `[PDF p. 13]` |
| Kim et al., *Autom. Constr.* 87:173–187 | 2018 | Q1 journal | FM work record gắn IFC object qua `IfcRelSpaceBoundary` → `relatedElements`; vật liệu qua `IfcMaterialLayerSetUsage` `[PDF p. 7 (printed 179), §3.2 layer 1]` (R4, P2-C5) | component identity | 2 | **Cảnh báo phương pháp then chốt** | Dùng **IFC instance number** (`#31982`, `#66803`), **không** dùng `GlobalId`. Cấu kiện mà evidence gắn vào **phụ thuộc đường quan hệ IFC được chọn** — G2 phải cố định đường đó tường minh |
| buildingSMART, *IfcRoot / IfcGloballyUniqueId, IFC 4.3.2.0* | 2024 | Normative doc | Mandatory `GlobalId`, uniqueness rule, identifier semantics (Zotero `EY3GJVZV`) | component identity | 2 | Normative identity basis | Documentation, không phải workflow evidence; không validate cross-version identity |

### 1.3 `Inspection_Record`

| Nguồn | Năm | Venue type | Xác lập điều gì | Chain element | Layer | Liên quan RQ2 | Giới hạn đối với luận án |
|---|---|---|---|---|---|---|---|
| Isailović et al. | 2020 | Q1 journal | Inspection là `IfcTask` + `IfcTaskTime` + inspection type + assigned findings; `Routine inspection` được populate `[PDF p. 8, Fig. 8; p. 19, Fig. 25]` (R2) | inspection record | 2 | **Bằng chứng mạnh nhất** cho inspection-as-entity | Không có inspector, source document, approver, record author gắn vào task. Không có record-ID contract |
| Lorvão Antunes et al. | 2024 | Q2 journal | `Inspection` là `Procedure`/`InspectionActivity`, có `prov:atTime`, liên kết observations/results; `GetInspectionResult` trả condition indicator + GUID cho BIM display `[PDF pp. 7–10, §5.2.3, Listings 4–5, Figs. 9–10]` (R1) | inspection record | 2 | Forward subchain đã chạy thật | Chuỗi **dừng trước** action/status. Không có reverse query. Không có SHACL/SWRL (tác giả nêu rõ là future work) |
| Sacks et al. | 2018 | Q1 journal | Inspection pipeline formal: assignment → acquisition → defect capture → QC/signing → rehab planning; `ElementDefect` là one type/location/element/time finding `[PDF p. 6, Fig. 2; p. 15, §5.3]` (R2) | inspection record | 2 | Formal process + information requirement tách nhau | **Không có named Inspection_Record ID**, author, hoặc lifecycle state |
| Mohamed et al. | 2023 | Q1 journal | Inspection data chia General Data / Inspection Data / Inspection Analysis Results; populated: inspector `Ahmed Khaled`, routine inspection `10-1-2023`, next exceptional inspection `1-4-2023` `[PDF pp. 6–7, 12–13, §§3.3, 4.3.1–4.3.2, Figs. 9–10]` (R3B) | inspection record | 2 | Populated fields phong phú nhất trong corpus | **Không có `Inspection_Record_ID`**, không ERD, không PK/FK, không cardinality. Mâu thuẫn ngày: `10-1-2023` (text, Figs. 8/10/12) vs `10/1/2022` (Fig. 14); `12 January 2022` (§4.3.1) vs `21-1-2022` (Fig. 9) |
| Li et al. | 2023 | Q1 journal | Inspection form: Bridge Name, Date, Pile number, Last date, No., Structure, Component, Type, Scale, Location, Characteristic, Recorder, Reviewer `[PDF p. 11, Fig. 12]` (R3A) | inspection record | 2 | Field list ở mức business form | `Recorder`/`Reviewer` **để trống**. `No.` là row number, không phải inspection-event ID |
| Wan et al. | 2019 | Q2 journal | Manager tạo inspection project → inspector capture qua mobile/QR → upload → manager data check `[PDF p. 13, §5.2.2, Figs. 12–13]` (R2) | inspection record | 2 | Workflow vận hành mạnh nhất | UI/process evidence, **không phải persisted record schema**. Không có assignment/status/rejection/signature schema |
| Kim et al. | 2018 | Q1 journal | 590 hồ sơ bảo trì kiến trúc không định kỳ gắn với "common BIM file – office"; SPARQL trả 12 hồ sơ cho space '139' → 7 tường, 2 loại vật liệu `[PDF pp. 10–12 (printed 182–184), §4.1–4.2.1, Tables 5–6]` (R4, P2-C7/C9) | inspection record | 2 | Prior art gần nhất cho **work record ↔ IFC object** | **Đây là maintenance work record, KHÔNG phải inspection record** (không có kết quả kiểm tra). Hồ sơ thật nhưng model là file mẫu tham chiếu — không có tương ứng as-is. Không precision/recall, không ground truth |
| Bellon et al., *Autom. Constr.* 174:106157 | 2025 | Q1 journal | Methodology snippet nêu IFC workflow bao phủ inspection data, damage reports, proposed maintenance services, costs (accessible Introduction/Methodology) (R1) | inspection record + action record | 2 | Closest schema/workflow competitor ở mức **broad statement** | **`UNVERIFIED` ở mức chi tiết.** Full text paywalled. Exact entities, relationships, identifiers, validation outputs **không kiểm chứng được**. **Evidence is currently insufficient.** |

### 1.4 `Action_Record`

| Nguồn | Năm | Venue type | Xác lập điều gì | Chain element | Layer | Liên quan RQ2 | Giới hạn đối với luận án |
|---|---|---|---|---|---|---|---|
| Wan et al. | 2019 | Q2 journal | `Pset-reinforcetype`, repair solutions, **populated repair-plan rows**, model-linked maintenance location, repair display, qualified/not-qualified check `[PDF pp. 4, 14–15, Tables 1, 3, Figs. 15–16]` (R2) | action record | 2 | **Precedent vận hành mạnh nhất** cho maintenance action | `Program NO.` chỉ là **UI column**: datatype, uniqueness, inspection linkage không specified. Không có trigger threshold, assignee, dates, progress states, criteria, verifier identity, closure/reopen |
| Sacks et al. | 2018 | Q1 journal | Bridge Treatment Library Data; alternative rehabilitation/maintenance projects; network working plan `[PDF p. 6, Fig. 2]` (R2) | action record | 2 | Action **category** representation | **Không có action entity, không có work-order ID.** Process dừng ở alternatives/working plan; repair execution và outcome không validated |
| Li et al. | 2023 | Q1 journal | Rule table nối defect/score → 4 mức maintenance priority; UI recommendation populated; text tuyên bố repair records được lưu và defect đã giải quyết được đánh dấu `completed` `[PDF p. 7, §Recommendations, Table 4; p. 15, Fig. 17]` (R3A) | action record | 2 | Closest defect→repair competitor | **Repair record là tuyên bố văn bản không có instance.** Không field list, không ID, không actor/time, không execution payload. `completed` là **current scalar**, không phải event |
| Mohamed et al. | 2023 | Q1 journal | Deterioration → maintenance recommendation (`Medium or major repair`, `Major repair or reconstruction`); `Maintenance History = Routine Maintenance (2-3-2022)` gắn `CO-6` `[PDF pp. 7–8, 12–14, §§3.5, 4.3.1, 4.3.3, Table 1, Figs. 9, 11]` (R3B) | action record | 2 | Maintenance history precedent | **Không có action/work-order ID.** `Routine Maintenance (2-3-2022)` là **dated history label**, không phải populated action record có executor/scope/result. Recommended date để trống |
| Piras et al. | 2026 | Q2 journal | OpenMAINT **có thể** liên kết work order với component `[PDF pp. 19, 24, 26, §§2.4.2, 3.2.3, 3.3.2]` (R3A) | action record | 2 | Platform capability | **Không có populated work-order instance**, ID, assignee, status, execution, result. Đây là capability, không được nâng thành `Action_Record = Yes` |
| Kim et al. | 2018 | Q1 journal | FM work record có Date, Area, Elements, Work contents, Labors, Work time, Working floor `[PDF p. 9 (printed 181), Table 2]` (R4) | action record | 2 | Field list cho work record thật | **Không ID, không owner, không approval, không verification.** Không có condition/defect object đi kèm |
| Carvalho et al. (screening) | 2023 | journal | Maintenance sheet nối Element ID với inspection, cleaning, correction, replacement, schedule, cost (Zotero `MSI2K38K`) | action record | 2 | Field-level comparator | **Chỉ ở mức screening** — abstract/notes không xác lập event identity, status transitions, inverse queries, verified closure |

### 1.5 Status / event history

| Nguồn | Năm | Venue type | Xác lập điều gì | Chain element | Layer | Liên quan RQ2 | Giới hạn đối với luận án |
|---|---|---|---|---|---|---|---|
| Çelik et al., *Comput. Ind.* | 2023 | Q1 journal | Provenance tuple **đã triển khai**: `{operation, time, model, version, objectID, owner}`; smart contracts đăng ký/cập nhật user/object + verification; Kovan experiments 5–30 operations/updates/actors `[PDF pp. 8, 10–13, §§5.1–7.3, Tables 1–4]` (R3B) | status/event history | 2 | **Prior art mạnh nhất** cho generic actor-object-operation-time-version provenance | **Không có event ID/tx hash công bố, không previous/new state, không reason, không approval, không liability record.** Tables 2–4 đo gas/cost, **không** đo semantic correctness. Frontend có lúc lấy provenance từ database chứ không phải blockchain `[PDF p. 11, §6.2]` |
| Lee, D. et al., *Autom. Constr.* 127:103688 | 2021 | Q1 journal | Blockchain **là** distributed ledger, chỉ lưu compliance statement (~0.5 kB × 49); sensor + as-built BIM **không** lên chain; 49 block sinh ra `[PDF pp. 2–3, 5–6, §§3, 4, 4.1, 5.1–5.2]` (R4, P4-C2/C3) | status/event history | 2 | **Nguyên lý thiết kế chuyển giao được**: tách evidence payload khỏi attestation record | Cảm biến **giả định** (`virtual hypothetical sensors`). Compliance check chỉ gồm vị trí + loại gạch. Tác giả tự nêu `blockchain trilemma` → **lý do không nhận blockchain vào G2/G3** `[PDF p. 8, §6]` |
| Mohamed et al. | 2023 | Q1 journal | `Inspection Reports History`, `Maintenance Reports History`, `Defects History`; `Status: not treated` `[PDF pp. 10, 12, §4.2, Fig. 8]` (R3B) | status/event history | 2 | Precedent cho "history" ở mức repository | **History là danh sách report, không phải event sequence.** `not treated` là **current scalar/display**, không có transition `unrepaired → repaired`, không actor/time, không append-only |
| Li et al. | 2023 | Q1 journal | `completed` cho defect đã giải quyết `[PDF p. 7]` (R3A) | status/event history | 2 | Closure-like scalar | Không event ID, timestamp, prior state, actor, reason, guard |
| Piras et al. | 2026 | Q2 journal | `Condition` (`Working`, `To Inspect`, `Out of Order`) + `Last_Check_Date` `[PDF pp. 13, 23–25, Tables 2–3, 7]` (R3A) | status/event history | 2 | Current scalar được map sang CMMS | Chỉ current/latest. **Mâu thuẫn nội bộ**: Fig. 5 hiển thị `Broken` trong khi Table 2 định nghĩa `Out of Order` |
| Lorvão Antunes et al. | 2024 | Q2 journal | Lấy latest inspection result bằng `MAX(?time)` `[PDF p. 8, Listing 4]` (R1) | status/event history | 2 | Latest-state query | Không có event sequence, không transition |

### 1.6 Authorization / accountable review

| Nguồn | Năm | Venue type | Xác lập điều gì | Chain element | Layer | Liên quan RQ2 | Giới hạn đối với luận án |
|---|---|---|---|---|---|---|---|
| Sacks et al. | 2018 | Q1 journal | `Bridge QC Engineer`, `QC pass` decision, `Inspection Signing` `[PDF p. 6, Fig. 2]` (R2) | authorization | 2 | Human review ở **process level** | Không có review record, signatory ID, timestamp, rationale |
| Wan et al. | 2019 | Q2 journal | Manager data check + manager repair-result check `[PDF pp. 13–15, §5.2.2, Figs. 12, 16]` (R2) | authorization | 2 | Human review ở **UI level** | Không có approval authority/outcome record |
| Çelik et al. | 2023 | Q1 journal | User/discipline registration, role update, user deletion, "leaving discipline can be blocked", authenticator narrative `[PDF pp. 10–12, Table 1, §§6.2–6.4]` (R3B) | authorization | 2 | Generic user/role administration | **Không có RBAC matrix, separation of duties, approve/reject event, approver-decision-time-rationale tuple.** Không có denied-call output |
| Mohamed et al. | 2023 | Q1 journal | Recommended date do **maintenance authority** quyết định, không phải inspector `[PDF p. 14, §4.3.3, Fig. 11]` (R3B) | authorization | 2 | Phân tách vai trò ở mức khái niệm | Không có named authority actor, authorization record, permission rule. Recommended-date field **để trống** |
| Li et al. | 2023 | Q1 journal | Form có `Recorder` và `Reviewer` `[PDF p. 11, Fig. 12]` (R3A) | authorization | 2 | — | **Cả hai field để trống.** Không chứng minh approval workflow |
| Lee, D. et al. | 2021 | Q1 journal | 3/10 node gieo chữ ký không hợp lệ (#3, #7, #10); 7 node hợp lệ xác thực ở 2.41 s; theo quy tắc 51%, 3 node kia vẫn nhận cùng dữ liệu ở 3.42 s `[PDF pp. 5–6, §§5.1–5.2, Fig. 7]` (R4, P4-C4) | authorization | 2 | **Gần nhất với một invalid fixture có expected outcome định trước** trong toàn corpus | Kiểm chứng **đồng thuận sổ cái**, không phải **toàn vẹn tham chiếu domain**. Node đồng thuận bằng mật mã — không role model, không rationale, không SoD |

### 1.7 Post-action verification / closure–reopen

| Nguồn | Năm | Venue type | Xác lập điều gì | Chain element | Layer | Liên quan RQ2 | Giới hạn đối với luận án |
|---|---|---|---|---|---|---|---|
| Wan et al. | 2019 | Q2 journal | Qualified/not-qualified judgement + manager result check sau repair `[PDF pp. 14–15, §5.2.2, Fig. 16]` (R2) | verification | 2 | **Precedent gần nhất** trong corpus cho post-repair check | Chỉ ở mức UI/process. Không criteria, không verifier identity, không before/after evidence, không closure/reopen |
| Çelik et al. | 2023 | Q1 journal | `verification` contract kiểm actor-object-operation-time-version `[PDF pp. 12–13, §7]` (R3B) | verification | 2 | Verification **của provenance** | **Không phải post-repair verification.** Không maintenance completion, closure, reopen |
| Jeon et al., *Buildings* 14(12):4032 (screening) | 2024 | Q1 journal | Ghi nhận condition grade sau khi sửa | verification | 2 | Hỗ trợ lập luận cần post-repair assessment | **Chỉ screening.** Quan sát sau sửa **không** được encode như verification transaction gắn với closure |
| Sacks et al. | 2018 | Q1 journal | Model verification / QC / signing `[PDF p. 6, Fig. 2]` (R2) | verification | 2 | — | Đây là **pre-action inspection check**, không phải post-repair acceptance loop |

### 1.8 Validation method — constraints, fixtures, CQ, representation

| Nguồn | Năm | Venue type | Xác lập điều gì | Chain element | Layer | Liên quan RQ2 | Giới hạn đối với luận án |
|---|---|---|---|---|---|---|---|
| Nuyts et al., *AEI* 60:102443 | 2024 | Q1 journal | **Deliberate** compliant/non-compliant fixtures: 4 variant IFC/RDF + 2 XML/JSON, 5 fault categories, 8 approaches; archived outputs cho XSD/JSON Schema/SPARQL/SHACL `[PDF pp. 3–13, §§3.1–4, Table 1, Listings 2–36]` (R3A) | validation method | 2 | **Xóa "dùng fixture hợp lệ/không hợp lệ" khỏi novelty** | Một `fail` file gộp **5 lỗi trên 4 objects** — không one-mutation-per-file. **Không có machine-readable oracle manifest, không automated diff/assertion, không false-pass/false-fail metric** |
| Hagedorn et al. | 2023 | Q1 journal | SHACL-SPARQL inference materialize **direct + inverse** predicates từ ICDD links; benchmark 4 datasets × 3 link configurations; R1 counts `0, 30, 39, 1` `[PDF pp. 5–16, §§2.4–4.2, Listings 1–3, Tables 1–4]` (R3A) | validation method | 2 | **Xóa "direct/inverse navigation" khỏi novelty** | Đây là **relation-level reverse navigation**, không phải reverse transformation hay round-trip parity. Table 4 báo actual counts, **không** expected counts. Không deliberate invalid fixture |
| Lee, Y.-C. et al. | 2021 | Q1 journal | IfcDoc/MVD rules đã chạy: uniqueness, forward/inverse reference, requiredness, datatype, allowed value, cardinality, syntax; pass/fail UI/HTML reports `[PDF pp. 5, 7–14, §§4.1, 5.1–5.2, Figs. 9–17]` (R1) | validation method | 2 | Rule families chuyển giao được | Actual conformance defects **không đạt** tiêu chí negative test chặt (thiếu seeded-invalid manifest + expected failure + so sánh actual-vs-expected) |
| Oraskari et al., *CIB W78 2021*, 693–702 | 2021 | Peer-rev. proceedings | SHACL-SPARQL feasibility/unit checks: missing counterpart, selected relations, change detection, restricted RDF view `[PDF pp. 4–9 (696–701), §§3–5, Listings 1–6]` (R1) | validation method | 2 | **Xóa "dùng SHACL" khỏi novelty** | Listing 1 không assert "exactly one"; Listing 3 hash predicates chứ không hash full triples; Listing 4 không reject extra edges. Không reverse conversion, không parity |
| Jia et al., *Buildings* 15:2633 | 2025 | Q1 journal | Jena rules + SPARQL templates chạy trên IFC-derived RDF qua Fuseki; rule có `Rule NO.` (1-1…1-4); check thật trả 2 `IfcRailing` ở 900 mm dưới ngưỡng 1100 mm `[PDF pp. 4, 11, 16, 20–21, §§3, 5.1–5.2.2, 6.2, Table 3, Figs. 13–14]` (R4, P3) | validation method | 2 | Rule-checking pipeline **đã chạy thật**; khung soạn rule 3 phần (constrained objects / contents / preconditions) chuyển giao được | **Không có họ rule toàn vẹn tham chiếu** — chỉ value rule và spatial rule. Không severity, không violation taxonomy, không oracle. 2 railing 900 mm là **dữ liệu thật**, không phải fixture gieo → không đạt tiêu chí negative test. Railing **không** có liên kết không gian trực tiếp trong IFC → phải suy ra bằng bounding box `[PDF p. 21]` |
| Keet & Khan, *JOWO/CEUR* Vol-4176 caos-9 | 2025 | Peer-rev. workshop | 5 loại CQ (SCQ/VCQ/FCQ/RCQ/MpCQ); **SCQ không nhất thiết trả lời được**, **VCQ bắt buộc formalisable + answerable** với `Lv ⊆ Lo`; câu hỏi kiểm disjointness/cardinality **không phải CQ** mà là constraint-checking query; ROCQS 558 CQ `[PDF pp. 4–5, 11–12, §§3.2, 4.2, Def. 1–3, Fig. 6]` (R4, P1) | validation method | 2 | **Thẩm quyền phương pháp** cho CQ Registry; use case SewerNet (`Maintenance` atelic vs `Repair`) tương đồng trực tiếp với ngữ nghĩa `Action_Record` | Không có đánh giá thực nghiệm, không có ngữ nghĩa pass/fail cho một bộ CQ. Domain-neutral |
| Lorvão Antunes et al. | 2024 | Q2 journal | CQ8–CQ10 pre-specified + formalized bằng SPARQL `[PDF pp. 6, 8–9, Table 2, Listings 3–5]` (R1) | validation method | 2 | **Xóa "dùng CQ" khỏi novelty** | Không có CQ cho action, status, accountability, reverse traversal. Đánh giá chỉ tới OOPS! pitfall scan |
| Pauwels & Terkaj, *Autom. Constr.* 63:100–133 | 2016 | Q1 journal | `RULE`/`FUNCTION` của EXPRESS **không chuyển được** sang OWL2 DL class expression; `WHERE` rule **không nằm trong** conversion. IFC4_ADD1.exp có 2 `RULE` + 45 `FUNCTION` `[PDF pp. 5, 33 (printed 104, 132), §§1.3.4, 2, 6]` (R4, P5) | representation | 2 | **Đóng góp phủ định quan trọng nhất của Round 4** | Hệ quả trực tiếp: chuyển IFC sang OWL **làm mất lớp ràng buộc của chính schema**. Mọi Constraint Catalogue của G2 phải **soạn riêng**, không thừa kế từ ifcOWL. Ngoài ra: kiểm nhất quán được kỳ vọng xảy ra trong BIM tool theo **CWA**, không trong RDF theo **OWA** — "thiếu" ≠ "vi phạm" |

---

## 2. Bốn nguồn phải xử lý đặc biệt

| Nguồn | Trạng thái | Được dùng thế nào trong Related Work |
|---|---|---|
| **Bellon et al. (2025)** | `UNVERIFIED` ở mức chi tiết — full text paywalled | Trích **chỉ** ở mức "broad IFC inspection-maintenance framework đã tồn tại". **Không** trích entity, relationship, identifier, validation outcome. Ghi kèm: *Evidence is currently insufficient* nếu reviewer hỏi chi tiết. Nếu muốn nâng cấp: mua/xin full text — đây là một trong hai nguồn duy nhất còn có thể dịch chuyển boundary ở mức entity |
| **Xu et al. (2022)** | `UNVERIFIED` — không có attachment | Chỉ nêu tồn tại scope gần. Không trích field, schema, validation. R2 §2.2 đã ghi rõ mọi `No` trong bảng Xu nghĩa là "không chứng minh được từ attachment hiện có", **không** phải "chức năng không tồn tại" |
| **Kim et al. (2018) — phát biểu "200%"** | `SOURCE-VERIFIED` là bài **có nêu câu này**, nhưng **không có suy dẫn, không mẫu số, không baseline, không bất định** `[PDF p. 14 (printed 186), §5]` (R4, P2-C12) | **Không được trích như kết quả hiệu năng.** Chỉ dùng như minh họa rằng độ mịn của liên kết (space-level vs element-level) làm đổi tập kết quả |
| **Jia et al. — chuẩn "GB 50096-2011"** | Bản v1.0 của Round 4 ghi năm; PDF chỉ in `GB-50096`, **năm không xuất hiện** trên trang đã soi `[PDF p. 20, §6.2]` (R4, V-14) | Ghi `GB-50096`, năm = `UNKNOWN`, cho tới khi xác minh reference [46] |

---

## 3. Bản đồ mật độ — chỗ nào đã đông, chỗ nào còn mỏng

Đếm trên **19 nguồn deep-read**. `Yes` chỉ dùng khi entity/record/rule/query được **mô tả và triển khai rõ** — capability statement, UI screenshot, narrative và future work không được nâng thành `Yes`.

| Mắt xích | Yes | Partial | No | Mật độ | Diễn giải |
|---|---:|---:|---:|---|---|
| Component identity / BIM anchor | 6 | 7 | 6 | ██████████ **rất đông** | `IfcGlobalId` linkage đã bị Piras, Antunes, Lee Y.-C., Hagedorn phủ kín |
| Condition evidence gắn cấu kiện | 5 | 5 | 9 | █████████ **đông** | Isailović + Sacks là chuẩn tham chiếu; Wan/Li/Mohamed bổ sung populated data |
| Executable constraints | 6 | 3 | 10 | █████████ **đông** | Lee Y.-C., Oraskari, Nuyts, Hagedorn, Jia, Piras — 6 nguồn đã **chạy thật** |
| `Inspection_Record` như một entity | 2 | 6 | 11 | ██████ **trung bình–đông** | Đông ở mức *attributes*; Isailović và Antunes là hai nguồn duy nhất có inspection-as-entity |
| Action **category / recommendation / plan** | 3 | 4 | 12 | █████ **trung bình** | Wan là mạnh nhất (populated repair plan); Sacks/Li/Mohamed ở mức recommendation |
| Deliberate valid/invalid fixtures | 1 | 1 | 17 | ███ **mỏng nhưng ĐÃ ĐƯỢC CHIẾM** | Chỉ Nuyts, nhưng Nuyts đủ để **xóa** claim này khỏi novelty |
| Direct/inverse navigation | 2 | 3 | 14 | ███ **mỏng nhưng ĐÃ ĐƯỢC CHIẾM** | Hagedorn (relation-level) + Piras (visual lookup) đủ để xóa claim |
| Generic provenance (actor/object/time/version) | 2 | 5 | 12 | ████ **trung bình, ĐÃ ĐƯỢC CHIẾM** | Çelik + Lee D. + PROV-O/PAV foundations |
| Competency questions | 2 | 0 | 17 | ███ **mỏng nhưng ĐÃ ĐƯỢC CHIẾM** | Antunes (áp dụng) + Keet & Khan (phương pháp) |
| **Stable `Inspection_Record_ID`** | **0** | 0 | 19 | ▁ **trống** | Không nguồn nào công bố ID contract |
| **Stable `Action_Record_ID`** | **0** | 1 | 18 | ▁ **trống** | Wan `Program NO.` chỉ là UI column |
| **Quan hệ `Inspection_Record_ID → Action_Record_ID`** (FK + cardinality + inverse) | **0** | 5 | 14 | ▁ **trống** | Có functional handoff ở Sacks/Wan/Li/Mohamed, **không** có key relation |
| **`Status_Event` maintenance-specific** (append-only, prev/new state, actor, time, reason) | **0** | 4 | 15 | ▁ **trống** | Çelik có tuple generic; **không** có prev/new state, reason, approval |
| **Accountable authorization** (approve/reject event, RBAC, SoD, rationale) | **0** | 6 | 13 | ▁ **trống** | Có role label và QC step; **không** có persisted decision |
| **`Verification_Record` sau hành động** | **0** | 2 | 17 | ▁ **trống** | Wan qualified/not-qualified là UI; Çelik là provenance verification |
| **Guarded closure / reopen** | **0** | 2 | 17 | ▁ **trống** | Chỉ có scalar `not treated` / `completed` |
| **Chain-specific mutations + exact oracle** | **0** | 2 | 17 | ▁ **trống** | Nuyts có fixtures nhưng không oracle manifest; Lee D. có 3/10 node nhưng ở tầng consensus |
| **Paired forward/reverse acceptance với expected set chính xác** | **0** | 6 | 13 | ▁ **trống** | Antunes/Piras/Hagedorn/Mohamed/Çelik đều dừng trước exact parity |
| **Evidence-basis preservation xuyên chuỗi** | **0** | 8 | 11 | ▁▁ **rất mỏng** | Nhiều mảnh (Hagedorn ICDD, Çelik hash, Mohamed image/report) nhưng chưa nối thành một chuỗi |

**Đọc bản đồ này ra sao.** Ba nhóm khác nhau:

1. **Đông và đã được chiếm** (component identity, condition evidence, constraints, CQ, fixtures, direct/inverse, generic provenance) → Related Work phải **thừa nhận và trích đầy đủ**. Mỗi mục ở đây mà anh vô tình đóng khung như đóng góp sẽ là điểm phản biện đầu tiên của reviewer.
2. **Đông ở mức attribute, trống ở mức identity** (`Inspection_Record`, `Action_Record`) → đây là **luận điểm chính** của Related Work. Corpus có rất nhiều *fields*, rất nhiều *forms*, rất nhiều *UI*, nhưng **không một nguồn nào công bố một record ID contract**. Đây là điểm tinh tế nhất và cũng thuyết phục nhất.
3. **Trống** (status event, authorization, verification, closure, mutation+oracle, parity) → là chỗ mỏng, nhưng **mỏng không tự động thành gap**. Xem §5.

---

## 4. Prior-art decomposition — cho phần Contribution của Paper 2

| Mức | Câu hỏi | Kết luận |
|---|---|---|
| **Technique** | Từng kỹ thuật riêng lẻ có mới không? | **`ESTABLISHED PRIOR ART`** cho toàn bộ: sensor-to-BIM, `IfcGlobalId` anchoring, BIM-linked inspection record, BIM–CMMS integration, action information modelling, competency questions, provenance modelling, SHACL/SPARQL/MVD/IDS validation, generic valid/invalid fixtures, direct/inverse navigation, generic human-in-the-loop review, viewer/dashboard, ontology engineering. Nguồn: §1 ở trên; `novelty-boundary.md`; `AGENT_RULES.md` §5 |
| **Combination** | Tổ hợp có mới trong corpus đã đọc không? | **`CANDIDATE NOVELTY` — corpus-bounded.** Không nguồn deep-read nào tích hợp: stable evidence/component/inspection/action identities + maintenance `Status_Event` + accountable authorization + formal post-action verification + guarded closure/reopen + exact chain-specific forward/reverse validation (`ROUND3B §5.9`, verdict `FREEZE_AS_CORE_GAP`) |
| **Distinct work** | Tổ hợp có làm được việc mà các phần riêng lẻ không làm được không? | **Đây là claim duy nhất sống sót trước reviewer giỏi** — và là claim phải được **luận chứng**, không phải khẳng định. Cụ thể: chỉ khi identity + append-only event + authorization + verification cùng tồn tại thì mới trả lời được câu "action này đã đóng hợp lệ chưa, ai cho phép, dựa trên bằng chứng nào, và tái mở được không" — mỗi thành phần riêng lẻ **không** trả lời được câu này |

**Câu contribution an toàn để dùng trong Related Work → Contribution:**

> Trong phạm vi corpus đã sàng lọc và deep-read, không một mô hình đơn lẻ nào mang đồng thời identity governance, append-only event history, actor-bound authorization, post-action verification và guarded closure như **một chuỗi được kiểm chứng**; từng thành phần riêng lẻ đều là established prior art.

Câu này **chưa** được dùng ở thì hoàn thành cho phần validation: G3 execution `NOT OPEN`, nên mọi mô tả phải là *designs / is prepared for validation*, không phải *validates*.

---

## 5. Gap audit — chỗ mỏng nào là gap thật, chỗ nào chỉ là scarcity

Áp dụng `claim-source-mapping.md` §4. `scarcity-only` và `none` đều quy về `UNSUPPORTED NOVELTY CLAIM`.

### 5.1 Quan hệ `Inspection_Record` ↔ `Action_Record`

```text
Gap as asserted:  "Chưa có nghiên cứu nào công bố quan hệ ổn định Inspection_Record_ID → Action_Record_ID
                   với cardinality, evidence basis và inverse query."
Evidence type:    documented-absence (component audit của 19/19 nguồn deep-read)
Corpus bound:     Rounds 1, 2, 3A, 3B + recent screening 2023–2026
Verdict:          PARTIALLY SUPPORTED GAP
Residue:          Functional handoff inspection → recommendation → repair ĐÃ có ở Sacks (p. 6, Fig. 2),
                  Wan (pp. 13–15), Li (pp. 7–8), Mohamed (pp. 7–8, 14). Phần còn mở đúng là:
                  stable IDs hai đầu, FK/cardinality, evidence basis field, inverse navigation.
                  Round 3B chốt: FREEZE_AS_CORE_GAP; cardinality chuyển sang EXPERT_REVIEW_DEPENDENT.
```

### 5.2 Immutable/queryable maintenance `Status_Event` history

```text
Gap as asserted:  "Chưa có nghiên cứu nào triển khai maintenance-specific append-only status event."
Evidence type:    documented-absence (0/19 Yes)
Corpus bound:     Rounds 1–3B; Çelik là stress test mạnh nhất và vẫn không đạt
Verdict:          SUPPORTED GAP
Residue:          Generic provenance tuple ĐÃ có (Çelik PDF p. 8, §5.1). Phần còn mở: previous/new status,
                  reason, quan hệ tới Action_Record, allowed transition, replay query,
                  reconstruction của current state từ event mới nhất.
                  Round 3B: FREEZE_AS_CORE_GAP. Round 4 bổ sung: Lee D. cho thấy attestation-tách-payload
                  là nguyên lý chuyển giao được, nhưng blockchain KHÔNG được nhận vào G2/G3 (trilemma).
```

### 5.3 Accountable authorization

```text
Gap as asserted:  "Chưa có approve/reject event với actor, role, authority, time, rationale và permission enforcement."
Evidence type:    documented-absence
Corpus bound:     Rounds 1–3B; Çelik + Mohamed là hai nguồn gần nhất
Verdict:          SUPPORTED GAP
Residue:          Role label, QC step, user administration ĐÃ có. Phần còn mở: RBAC matrix,
                  separation of duties, override record, unauthorized-decision test.
                  Round 3B: FREEZE_AS_CORE_GAP. Exact role matrix → EXPERT_REVIEW_DEPENDENT.
```

### 5.4 Formal post-action verification + guarded closure/reopen

```text
Gap as asserted:  "Chưa có Verification_Record gắn action với verifier, criteria, before/after evidence,
                   outcome, và closure guard."
Evidence type:    documented-absence
Corpus bound:     Rounds 1–3B; Wan là precedent gần nhất, Jeon (2024) chỉ ở mức screening
Verdict:          SUPPORTED GAP
Residue:          Post-repair check ở mức UI/process ĐÃ có (Wan pp. 14–15). Phần còn mở: verification identity,
                  acceptance criteria, independent-verifier rule, rejection/rework path, closure precondition,
                  reopen trigger. Round 3B: FREEZE_AS_CORE_GAP (cả 5.5 và 5.6).
```

### 5.5 Evidence-basis preservation xuyên chuỗi

```text
Gap as asserted:  "Chưa có chuỗi source-version/hash → inspection → finding → action rationale
                   → verification → closure hoàn chỉnh."
Evidence type:    documented-absence, nhưng nhiều mảnh đã tồn tại (8/19 Partial)
Corpus bound:     Rounds 1–3B; Hagedorn (ICDD), Çelik (hash), Schuler (screening) là các mảnh gần nhất
Verdict:          PARTIALLY SUPPORTED GAP
Residue:          Generic provenance vocabulary (PROV-O/PAV) và evidence packaging (ICDD) ĐÃ có.
                  Phần còn mở đúng là việc GHÉP chúng thành một chuỗi truy vấn được.
                  Round 3B: FREEZE_AS_SUPPORTING_GAP — không đủ để tự mang đóng góp.
```

### 5.6 Chain-specific mutations + exact oracle; paired forward/reverse parity

```text
Gap as asserted:  "Chưa có mutation manifest chain-specific với expected focus ID/violation code/count
                   và automated actual-vs-expected assertion; chưa có paired CQ với exact expected set."
Evidence type:    documented-absence
Corpus bound:     Rounds 1–3B; Nuyts là nguồn mạnh nhất và vẫn thiếu oracle
Verdict:          PARTIALLY SUPPORTED GAP
Residue:          Deliberate fixture generic ĐÃ bị Nuyts chiếm; direct/inverse navigation ĐÃ bị Hagedorn chiếm.
                  Phần còn mở: isolated one-fault mutations cho duplicate ID, orphan link, wrong target type,
                  missing evidence basis, illegal transition, unauthorized approval, closure-without-verification;
                  cộng machine-readable oracle. Round 3B: FREEZE_AS_SUPPORTING_GAP (cả 5.7 và 5.8).
```

### 5.7 Một điểm KHÔNG phải gap

```text
Gap as asserted:  "Ít nghiên cứu về inspection/action record cho nhà thép công nghiệp ven biển."
Evidence type:    scarcity-only
Verdict:          UNSUPPORTED NOVELTY CLAIM
```

Nếu Related Work hiện có câu nào theo dạng "few studies address X" hoặc "còn ít nghiên cứu về Y", câu đó phải bị viết lại. Sự khan hiếm có thể có nghĩa là chủ đề không thú vị, hoặc đã được giải ở nơi khác dưới tên gọi khác, hoặc phạm vi tìm kiếm quá hẹp. Loại structure-type (cầu vs nhà thép công nghiệp) **không** được dùng như một trục gap: toàn bộ corpus là bridge/building FM, và chuỗi thông tin không phụ thuộc loại kết cấu — nếu lấy nó làm gap, reviewer sẽ hỏi "vậy điều gì trong chuỗi thay đổi khi kết cấu là nhà thép ven biển?" và câu trả lời hiện tại là: không có gì ở tầng thông tin.

---

## 6. Sáu cái bẫy khi viết Related Work về inspection/action record

Đây là các mâu thuẫn khái niệm đã được ghi nhận trong corpus. Chúng phải được **nêu ra** trong Related Work, không được làm mượt.

**1. `Recommendation` ≠ `Action_Record`.** Mohamed tách rõ: inspector đưa recommendation, còn recommended date do **maintenance authority** quyết định `[PDF p. 14, §4.3.3]`. Li và Sacks đều dừng ở recommendation/treatment library. Nếu Related Work gộp hai thứ này, toàn bộ luận điểm authorization sụp.

**2. `completed` / `not treated` / `repaired` ≠ verified closure.** Li có `completed` `[PDF p. 7]`, Mohamed có `not treated` `[PDF p. 12, Fig. 8]`. Cả hai là **current scalar/display**, không phải transition, không phải closure. Round 3B §7.3 liệt kê "closed-loop maintenance claim dựa chỉ trên `not treated`/`repaired`/`completed`/current condition/maintenance-history label" vào danh sách **claims removed from novelty** — nhưng cũng có nghĩa là: khi mô tả prior art, không được nói các bài này "đã đóng vòng lặp".

**3. Bốn khái niệm "event" không tương đương** (Round 3B §3.3 — nên đưa trực tiếp thành một đoạn trong Related Work):

| Khái niệm | Ai triển khai | Ranh giới |
|---|---|---|
| Blockchain transaction | Çelik, Lee D. | Ledger-level execution. Bất biến **không** biến nó thành maintenance action |
| BIM information-exchange event | Çelik tuple `{operation, time, model, version, objectID, owner}` | Design/construction exchange chung. Thiếu inspection/action/status/closure semantics |
| Maintenance `Status_Event` | **Không ai** | Cần action-scoped identity, previous/new workflow state, actor, time, reason, transition rule |
| Operational approval event | **Không ai** | Capability/contract validation ≠ persisted approve/reject decision bởi actor được ủy quyền |

Blockchain consensus xác thực việc đưa block vào chuỗi; authenticator/verification contract xác thực điều kiện provenance đã nêu; **không cái nào** là bằng chứng của accountable maintenance authorization hay post-action acceptance.

**4. Defect severity ≠ `Action_Level`.** Sacks có severity 1–5 `[PDF p. 11, Table 5]`, Isailović có condition rating 1–5 `[PDF pp. 6–8]`. Đây là **condition rating**, không phải action priority. Round 3A ghi decision `REMOVE` cho mọi rule tự động coi defect severity là `Action_Level`.

**5. Lớp ràng buộc của IFC không sống sót khi sang OWL.** Pauwels & Terkaj: `RULE`/`FUNCTION` không chuyển được sang OWL2 DL; `WHERE` rule không nằm trong conversion `[PDF p. 33 (printed 132), §6]`. Kèm theo: kiểm nhất quán được kỳ vọng diễn ra trong BIM tool theo **CWA**, không trong RDF theo **OWA** `[PDF p. 5 (printed 104), §1.3.4]`. Hệ quả cho Related Work: khi mô tả các nghiên cứu SHACL/SPARQL, phải nói rõ họ **không** thừa kế ràng buộc của IFC schema — họ soạn ràng buộc mới. Đây cũng là lý do Constraint Catalogue của G2 phải được soạn riêng.

**6. CQ ≠ constraint-checking query.** Keet & Khan tách tường minh: câu hỏi kiểm disjointness/cardinality **không phải** CQ, chúng là "general constraint-checking queries" `[PDF p. 11, §4.2]`. Antunes trộn hai loại này. Nếu Related Work trình bày CQ Registry và Constraint Catalogue như một artifact, đó là một lỗi phương pháp mà reviewer ontology sẽ bắt ngay.

---

## 7. Nguồn chỉ ở mức screening — không được trích ở mức field

Các nguồn dưới đây có trong `G2_G3_RECENT_EVIDENCE_SCREENING_2023_2026.md` nhưng **chưa deep-read**. Có thể trích ở mức "tồn tại, thuộc nhóm X", **không** được trích entity/field/kết quả cụ thể cho tới khi deep-read.

| Nguồn | Nhóm | Vì sao có thể hữu ích cho Related Work | Trạng thái |
|---|---|---|---|
| Jeon, C.-H. et al. (2023), *Buildings* 13(9):2332 | A | Inventory-code system + inspection information mapping cho cầu hiện hữu | Screening; P2 priority |
| Carvalho et al. (2023) | A, B | Maintenance sheet nối Element ID → inspection/cleaning/correction/replacement/schedule/cost | Screening |
| Schuler et al. (2025), *ITiCBE* | A, D | ICDD ISO 21597 nối bằng chứng từ test design tới result — gần nhất với evidence-basis preservation | Screening |
| Jaskula et al. (2025), *JCEM* 151(9) | B, D | User requirements cho accountable/tamper-resistant whole-asset history | Screening; **conceptual**, không phải operational ledger |
| Hüthwohl et al. (2018) | A | IFC schema cho component-linked bridge defect | Screening; pre-2023, chồng với Round 2 |
| Cavieres-Lagos et al. (2024), *Appl. Sci.* 14:6209 | A, C | Bidirectional Revit–Dynamo–Excel exchange | Screening |
| Jeon, C.-H. et al. (2024), *Buildings* 14(12):4032 | A, B | Quan sát condition grade sau sửa chữa | Screening |
| Wang et al. (2024) | C | Chuyển IFC `WHERE` rule sang SHACL/SPARQL | Screening; đối chiếu với Pauwels & Terkaj P5-C3 |
| Stolk & McGlinn (2020); Theiler & Smarsly (2018); Quinn et al. (2020); BOT (2020) | C, A | Method/identity support | Screening |
| PROV-O, PROV-DM, PAV; ISO 55000:2024; GSA BIM Guide 08 | D, A | Vocabulary/normative background | Background only |

Loại trừ khỏi evidence queue (đã ghi nhận trong screening report): Armijo & Zamora-Sánchez (2024) — đóng góp chính là SHM/anomaly detection, nằm ngoài scope thông tin đã khóa; cùng với các record trùng lặp/webpage không kiểm chứng.

---

## 8. Đề xuất cấu trúc Related Work

Sắp theo **mắt xích**, không theo năm và không theo công nghệ. Lý do: cấu trúc theo mắt xích tự nó dựng lên lập luận đóng góp; cấu trúc theo năm thì không.

```text
2.x.1  Condition evidence gắn cấu kiện BIM
       → Sacks 2018; Isailović 2020; Wan 2019; Antunes 2024; Li 2023; Mohamed 2023
       → Kết đoạn: representation đã trưởng thành; provenance per-finding thì chưa

2.x.2  Component identity và BIM–CMMS anchoring
       → Piras 2026; Lee Y.-C. 2021; Hagedorn 2023; Kim 2018 (cảnh báo đường quan hệ IFC)
       → Kết đoạn: IfcGlobalId anchoring là established; persistence qua revision thì chưa

2.x.3  Inspection record: từ form đến entity
       → Isailović 2020 (IfcTask); Antunes 2024 (Procedure); Sacks 2018; Wan 2019; Li 2023; Mohamed 2023
       → Kết đoạn (điểm mấu chốt #1): corpus giàu FIELD, trống ID CONTRACT

2.x.4  Action record: recommendation, plan, work order
       → Wan 2019 (mạnh nhất); Sacks 2018; Li 2023; Mohamed 2023; Piras 2026 (capability); Kim 2018
       → Kết đoạn (điểm mấu chốt #2): không nguồn nào công bố Action_Record_ID;
         và recommendation ≠ action ≠ execution ≠ verified closure

2.x.5  Status, history và provenance
       → Çelik 2023; Lee D. 2021; Mohamed 2023; Li 2023; Piras 2026
       → Đoạn "bốn khái niệm event không tương đương" (§6.3) đặt ở đây

2.x.6  Accountability: review, approval, verification, closure
       → Sacks 2018; Wan 2019; Çelik 2023; Mohamed 2023; Li 2023; Lee D. 2021
       → Kết đoạn (điểm mấu chốt #3): role label và QC step có; persisted decision không

2.x.7  Validation methods và giới hạn của chúng
       → Lee Y.-C. 2021; Oraskari 2021; Nuyts 2024; Hagedorn 2023; Jia 2025;
         Keet & Khan 2025 (CQ ≠ constraint query); Pauwels & Terkaj 2016 (ràng buộc IFC không sống sót)
       → Kết đoạn: phương pháp là prior art; contract chain-specific thì chưa có

2.x.8  Tổng hợp khoảng trống  →  bảng decomposition ở §4
```

Cách viết mỗi kết đoạn: **nêu prior art đã đạt được gì trước**, rồi mới nêu phần còn mở. Thứ tự ngược lại (nêu gap trước) là dấu hiệu của novelty inflation và reviewer đọc ra ngay.

---

## 9. Khi nào nên mở lại search

`CLOSE_SEARCH` đóng broad discovery, **không** cấm mở lại khi có câu hỏi có khả năng dịch chuyển structural novelty boundary. Ba trường hợp hợp lý:

1. **Bellon et al. (2025) full text.** Đây là nguồn duy nhất trong corpus có thể còn chứa `Inspection_Record`–`Action_Record` semantics ở mức entity mà ta chưa nhìn thấy. Round 1 §6.1 đã ghi rõ: *Evidence is currently insufficient* để kết luận Bellon **không** có chuỗi đầy đủ. Đây là rủi ro lớn nhất còn lại cho contribution statement.
2. **Xu et al. (2022) full text.** Cùng lý do, mức độ thấp hơn.
3. **Nếu reviewer/expert review đề xuất một trục mới** — ví dụ asset-management standard compliance (ISO 55000 / ISO 19650 / TCVN 14177:2024) như một trục Related Work, thì trục đó chưa được screening bao phủ ở mức peer-reviewed implementation evidence.

Ngoài ba trường hợp trên, mở rộng search sẽ tốn context mà không dịch chuyển boundary — Round 3B §8.3 đã kết luận không còn identified unread competitor nào có khả năng đó, và các điểm chưa giải quyết là **governance question**, không phải **literature-discovery question**.

---

## 10. Claim → Evidence → Limitation → Next action

**Claim.** Trong phạm vi 19 nguồn deep-read và lớp screening 2023–2026, prior art về `Inspection_Record` và `Action_Record` trong asset management **đông đặc ở tầng thuộc tính và tầng quy trình**, nhưng **trống ở tầng identity contract và tầng vòng đời có trách nhiệm giải trình**. Cụ thể: 0/19 nguồn công bố stable `Inspection_Record_ID`, 0/19 công bố stable `Action_Record_ID`, 0/19 công bố quan hệ khóa giữa hai bên, 0/19 có maintenance-specific `Status_Event`, 0/19 có persisted approve/reject event, 0/19 có `Verification_Record` sau hành động, 0/19 có guarded closure/reopen.

**Evidence.** Component audit của từng nguồn trong `G2_G3_ROUND1_DEEP_READ_AND_NOVELTY_BOUNDARY.md` §2, `G2_G3_ROUND2_INSPECTION_ACTION_MODEL_DEEP_READ.md` §2, `G2_G3_ROUND3A_NOVELTY_AND_SCHEMA_BOUNDARY.md` §2, `G2_G3_ROUND3B_HISTORY_ACCOUNTABILITY_AND_SEARCH_CLOSURE.md` §§2–4, `ROUND4_VERIFIED_EVIDENCE_RECORD_v1.1.md` §4; novelty stress test `ROUND3B §5.1–5.9` (verdict `FREEZE_AS_CORE_GAP` cho 5.1, 5.2, 5.3, 5.5, 5.6, 5.9); decision matrix `ROUND3B §6`; search closure register `ROUND3B §9`; cross-candidate capability check `G2_G3_RECENT_EVIDENCE_SCREENING_2023_2026.md` §5.0.

**Limitation.** Ma trận này **corpus-bounded** và không phải systematic review — nó không hỗ trợ bất kỳ phát biểu "first", "no study worldwide" hay universal absence nào. Hai nguồn (Bellon 2025, Xu 2022) `UNVERIFIED` ở mức chi tiết, và Bellon nằm đúng chỗ nhạy cảm nhất của boundary. Các con số đếm ở §3 dựa trên nhãn Yes/Partial/No do các Round report gán, không phải do tôi đọc lại PDF gốc trong phiên này. Round 4 tự khai báo `PROVISIONAL IN PART`: nhiều trang PDF chưa được soi trực quan (§3.2 liệt kê cụ thể), nên một số claim của Round 4 chưa ở mức `SOURCE-VERIFIED`. Ma trận này cũng **không** đánh giá phương pháp (thuộc `phd-methodology-audit`), **không** đánh giá gate (thuộc `phd-gate-evidence-audit`), và **không** viết prose bản thảo (thuộc `phd-paper-builder`).

**Next action.**
1. Dựng Related Work theo khung §8 — sắp theo mắt xích, mỗi kết đoạn nêu prior art trước.
2. Rà toàn bộ bản thảo Related Work hiện có bằng §6: sáu cái bẫy này là nơi overclaim thường lọt qua.
3. Rà mọi câu dạng "còn ít nghiên cứu về..." và viết lại theo §5.7.
4. Quyết định (đây là quyết định của người nghiên cứu, không phải của phân tích này) có mua/xin full text Bellon et al. (2025) hay không. Nếu không, ghi rõ trong Limitation của Paper 2 rằng ranh giới ở mức entity so với Bellon chưa khóa được.
5. Nếu cần bảng claim–source map cho từng câu cụ thể trong bản thảo Related Work, gửi câu verbatim — tôi map theo `claim-source-mapping.md` §1, không diễn giải lại câu trong lúc audit.

---

## 11. Báo cáo đóng nhiệm vụ

**Files đã đọc (read-only, không sửa gì):**
- `08_AI_SKILL_SYSTEM/phd-dt-research-skills/phd-literature-evidence/SKILL.md` + `references/{corpus-map, claim-source-mapping, source-verification}.md`
- `08_AI_SKILL_SYSTEM/phd-dt-research-skills/_phd-canon/{novelty-boundary, output-discipline, research-chain, epistemic-ladder, scope-control}.md`
- `02_EVIDENCE_BASE/RQ2_GATES2_3/00_README_START_HERE.md`
- `02_EVIDENCE_BASE/RQ2_GATES2_3/G2_G3_ROUND1_DEEP_READ_AND_NOVELTY_BOUNDARY.md`
- `02_EVIDENCE_BASE/RQ2_GATES2_3/G2_G3_ROUND2_INSPECTION_ACTION_MODEL_DEEP_READ.md`
- `02_EVIDENCE_BASE/RQ2_GATES2_3/G2_G3_ROUND3A_NOVELTY_AND_SCHEMA_BOUNDARY.md`
- `02_EVIDENCE_BASE/RQ2_GATES2_3/G2_G3_ROUND3B_HISTORY_ACCOUNTABILITY_AND_SEARCH_CLOSURE.md`
- `02_EVIDENCE_BASE/RQ2_GATES2_3/ROUND4_VERIFIED_EVIDENCE_RECORD_v1.1.md` (§§1–5)
- `02_EVIDENCE_BASE/RQ2_GATES2_3/G2_G3_RECENT_EVIDENCE_SCREENING_2023_2026.md`

**Files tạo:** đúng một — file này.
**Files sửa/xóa:** không có. Không chạm `00_GOVERNANCE`, `01_CURRENT_CONTROL`, `02_EVIDENCE_BASE`, `03_PAPERS`, `05_DATA_CODE_AND_EXPERIMENTS`, `06_LITERATURE_AND_ZOTERO`, `07_PROMPTS_AND_HANDOFFS`. Không chạm Zotero.

**Bằng chứng đã dùng:** 19 nguồn deep-read Rounds 1–4 + screening matrix 2023–2026. Không nguồn nào được thêm từ trí nhớ; không citation, DOI, Zotero key, tác giả, năm, venue hay quartile nào được bịa. Hai nguồn được đánh dấu `UNVERIFIED` ở mức chi tiết và không bị bỏ im lặng.

**Giới hạn chưa giải quyết:** ranh giới entity-level so với Bellon et al. (2025) và Xu et al. (2022); các trang PDF chưa soi trực quan trong Round 4; cardinality `Inspection_Record`↔`Action_Record`, role/permission matrix, transition vocabulary, verification criteria và closure/reopen policy đều là `EXPERT_REVIEW_DEPENDENT`; payload `Condition_Evidence` là `G1_DEPENDENT`.

**Gate có gần hơn không?** Có, ở mức Related Work evidence cho G2. Nhưng đây là **literature evidence**, không phải **validation evidence**: nó không đóng G2 và không mở G3. G2 giữ nguyên `OPEN — LITERATURE BOUNDARY CLOSED, SPECIFICATION NOT YET FROZEN`; G3 execution `NOT OPEN`.

**AI-assisted research disclosure:** phân tích này được tạo có hỗ trợ AI, đọc từ các Round report bất biến trong repository. Mọi locator được truy về file nguồn và trang/section do các Round report đã ghi. Không có PDF gốc nào được đọc lại trực tiếp trong phiên này, nên các nhãn Yes/Partial/No được kế thừa từ các Round report, không phải được tái kiểm chứng độc lập.
