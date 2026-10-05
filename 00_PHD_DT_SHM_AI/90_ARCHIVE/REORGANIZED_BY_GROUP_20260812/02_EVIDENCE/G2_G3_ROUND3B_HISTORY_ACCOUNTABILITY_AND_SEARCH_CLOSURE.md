# G2-G3 Round 3B History, Accountability, and Search Closure

**Research mapping:** RQ2/WP2 -> Chapter 5 -> Paper 2 -> Gate 2-3  
**Deep-read date:** 2026-08-04  
**Locked chain:** `Condition_Evidence -> BIM component -> Inspection_Record -> Action_Record -> Status_Event -> accountable review -> verified closure`  
**Round 3B corpus:** đúng hai bài Mohamed et al. (2023) và Celik et al. (2023), đối chiếu với báo cáo nền `G2_G3_ROUND3A_NOVELTY_AND_SCHEMA_BOUNDARY.md`. Không dùng tài liệu thứ ba để hỗ trợ claim Round 3B.

Nguồn đọc:

- Mohamed, A. G., Khaled, A., & Abotaleb, I. S. (2023), DOI `10.3390/buildings13112798`. Item không xuất hiện khi tra DOI, title, `BrIM`, hoặc `Abotaleb` trong Zotero library hiện tại; do đó đọc đúng publisher full-text PDF 20 trang từ MDPI. Không thêm item hoặc sửa Zotero.
- Celik, Y., Petri, I., & Barati, M. (2023), DOI `10.1016/j.compind.2022.103768`, Zotero item `EMTIHHX4`, PDF attachment `YEVE3FRE`; full text được truy xuất bằng ZoteroMCP.

Quy ước:

- `PDF p.` là số trang vật lý của file PDF đã đọc. Celik có hai trang proof front matter trước article title page; vì vậy `PDF p.3` tương ứng article p.1.
- `Yes` chỉ dùng khi entity, record, rule, field hoặc query được mô tả và triển khai đủ rõ. Capability, narrative, UI, future work và blockchain consensus không được nâng thành operational approval hoặc maintenance event.
- `Partial` giữ nguyên giới hạn bằng chứng: conceptual requirement, implemented attribute, populated display, current scalar, event-like tuple, hoặc cost experiment có thể tồn tại nhưng chưa đạt semantics đang kiểm tra.
- Khi full text không đủ để xác nhận, báo cáo ghi `Evidence is currently insufficient.`

## 1. Executive summary

- **Mohamed bao phủ inspection-maintenance history ở mức repository/report list và current snapshot.** BrIM chứa `Inspection Reports History`, `Maintenance Reports History`, `Defects History`, element-level history strings, bốn inspection operations, và populated inspection/finding displays (PDF pp. 10-17, §§4.2-4.6; Figs. 8-14). Không có stable `Inspection_Record_ID`, `Finding_ID`, `Action_Record_ID`, event ordering, prior/new state, hoặc immutable audit semantics.
- **Repaired/unrepaired không phải event history.** Text nói defect history bao gồm defects “whether repaired or not”, còn Fig. 8 populate `Status: not treated` cho expansion-joint failure (PDF pp. 10, 12, §4.2, Fig. 8). Đây là current scalar/display. Không có transition `unrepaired -> repaired`, repair event, verifier, acceptance criteria, closure, hoặc reopen.
- **Maintenance history có precedent nhưng Action identity không có.** Fig. 9 populate `Maintenance History = Routine Maintenance (2-3-2022)` và `Inspection History = Routine Inspection (21-1-2022)` (PDF pp. 12-13, §4.3.1, Fig. 9). Đây là dated history references liên kết với component `CO-6`, không phải populated action record có ID, executor, scope, result và relation đến inspection/finding.
- **Celik bao phủ generic transaction provenance đến actor-object-operation-time-version.** Tuple được báo cáo gồm `operation`, `time`, `model`, `version`, `objectID`, `owner`; smart contracts/functions đăng ký user/object, update user/object và verification; Kovan experiments thực thi transactions cho operation/time, object updates và actor retrieval (PDF pp. 8, 10-13, §§5.1-7.3; Table 1; Tables 2-4). Tuy nhiên, paper không công bố transaction hash/event ID, actual returned history rows, prior/new state hoặc rationale.
- **Actor/time/version được lưu theo implemented design nhưng bằng chứng truy vấn semantics còn partial.** Provenance contract được mô tả là lưu discipline, object, operation, time, actor và update version; verification contract kiểm tra actor-object-operation-time-version. Tables 2-4 chứng minh execution/cost scaling, không chứng minh completeness hoặc exact semantic query answers (PDF pp. 12-13, §§7-7.3).
- **Responsibility/liability và approval không được operationalize đầy đủ.** Celik nêu responsibility/liability như mục tiêu và có `owner`, discipline IDs, role updates, user deletion/access narrative; không có liability assignment record, RBAC matrix, separation-of-duties rule, approver-decision-time-rationale tuple, hoặc persisted approve/reject event (PDF pp. 3, 8, 10-12, Abstract, §§5.1-6.4; Table 1).
- **Hai bài không làm suy yếu core gap.** Mohamed established prior art cho BrIM-linked inspection documentation, report histories, current condition/status và maintenance recommendations. Celik established prior art cho tamper-oriented generic BIM provenance and verification transactions. Không bài nào nối stable inspection/action identities với maintenance-specific `Status_Event`, accountable authorization, post-action verification, guarded closure/reopen và exact forward/reverse acceptance results.
- **Giới hạn chính thức:** blockchain transaction khác BIM information-exchange event; BIM information-exchange event khác maintenance `Status_Event`; consensus/authenticator verification khác operational approval; data-provenance verification khác post-repair verification.
- **Quyết định:** corpus Round 1-3B đủ để xây G2 Specification v0.1 ở mức structural contract và validation contract. Exact cardinalities, role permissions, transition vocabulary, verification criteria và evidence payload binding được chuyển sang expert review, governance decision hoặc G1 payload. Không cần mở rộng literature search diện rộng.

## 2. Mohamed et al. deep-read

### 2.1 Claim extraction

| Claim | Exact page/section | Implemented artifact | Validation | Limitation | Thesis implication |
|---|---|---|---|---|---|
| Mỗi bridge element nhận unique ID trong BrIM/inventory | PDF p. 4, §3.1; pp. 9-10, §4.1; Fig. 6 | Revit/BrIM element coding, ví dụ `DE`, `EJ`, `GI`, `CO`; populated `CO-6`, `DE-19`, `GI-41`, `EJ-5` | Case bridge được model và populate | Không có uniqueness test, revision-stability policy hoặc `IfcGlobalId` crosswalk | Component identity là established prior art; record identity vẫn phải tách riêng |
| Inspection data được tổ chức thành General Data, Inspection Data và Inspection Analysis Results | PDF pp. 6-7, §3.3; pp. 12-14, §§4.3-4.3.3; Figs. 9-11 | BrIM attributes và populated inspection displays | Routine inspection case ngày 10-1-2023 được nhập | Không có `Inspection_Record_ID`, ERD, PK/FK hoặc cardinality | Candidate fields có precedent; formal record contract chưa established |
| Repository chứa inspection, maintenance và defect histories | PDF pp. 6, 10-13, §§3.2-3.3, 4.2-4.3.1; Figs. 3, 8-9 | Project-browser report collections và element-level history fields | Bốn inspection operations được nêu; Fig. 9 có dated history values | History là report list/string references; không có ordered event model | G2 phải tách document/report history khỏi `Status_Event` history |
| Defect history bao gồm repaired/unrepaired và current status | PDF p. 10, §4.2; p. 12, Fig. 8 | Defect-history UI/card; populated `Status: not treated` | Một defect card được hiển thị | Không có old/new state, transition ID, repair record, actor/time hoặc append-only rule | `not treated` là current scalar, không phải transition hoặc closure evidence |
| Inspector, date, defect cause, image, comment và next inspection được populate | PDF pp. 12-13, §§4.3.1-4.3.2; Figs. 9-10 | Populated inspection/finding attributes | `Ahmed Khaled`, `10-1-2023`, defect image, cause/comment, `1-4-2023 Exceptional inspection` | Không có source version/hash, inspector ID hoặc inspection record ID | Hỗ trợ minimum evidence/inspection payload; provenance binding còn mở |
| Deterioration maps to maintenance recommendation | PDF pp. 7-8, §3.5, Table 1; p. 14, §4.3.3, Fig. 11; p. 17, Fig. 14 | Color/rating rule và recommendation fields | Case rows có `Medium or major repair` và `Major repair or reconstruction` | Recommendation không phải approved work order hoặc executed action | `Action_Record` phải phân biệt recommendation, authorization, execution và verification |
| Recommended date do maintenance authority quyết định, không phải inspector | PDF p. 14, §4.3.3, Fig. 11 | Conceptual responsibility split; blank recommended-date fields | Không có populated authority decision | Không có named authority actor, authorization, decision record hoặc permission rule | Cần expert review về role/authority; paper không chứng minh approval workflow |
| Defects được model bằng geometry/photo và linked component location | PDF pp. 7, 13-15, §§3.4, 4.3.2, 4.4; Figs. 4, 10, 12 | Damage cubes, photo, dimensions, component location | Concrete spalling, joint degradation và pothole được populate | Không có stable defect ID; identity/value conflicts xuất hiện giữa views | Cần `Finding_ID`, source binding và cross-view consistency constraints |
| Reports được generated từ BrIM schedules | PDF pp. 8-9, §3.6; pp. 16-17, §4.6; Fig. 14 | Master/defect/condition/NDT/maintenance/inspection report capability; populated master report | Fig. 14 là generated report | UI/report generation không phải executed trace query hoặc integrity validation | Report prior art phải loại khỏi novelty; acceptance tests vẫn mở |
| Case study “validates” framework | PDF p. 9, §4; pp. 17-18, §5 | Practical demonstration on one bridge | One routine-inspection case | Không có accuracy metric, referential-integrity test, expected oracle, longitudinal performance hoặc invalid fixture | Chỉ dùng như feasibility demonstration, không dùng như formal integrity validation |

### 2.2 Component audit

| Thành phần | Yes / Partial / No | Exact evidence |
|---|---|---|
| Component/asset ID | Yes | Unique element IDs được assigned trong §3.1 và §4.1; populated `CO-6`, `DE-19`, `GI-41`, `EJ-5`, PDF pp. 4, 9-10, 12-17, Figs. 6, 8-14. Stability across revisions chưa được test. |
| Inspection_Record ID | No | Inspection date/type/name và report history có mặt, nhưng không có inspection-event identifier, report number hoặc PK. `Evidence is currently insufficient.` |
| Finding/defect ID | No | `11`, `12`, `13` trong Project Browser không được định nghĩa là stable defect IDs; `Location` dùng component IDs. `Evidence is currently insufficient.` PDF pp. 12-15, Figs. 8, 10, 12. |
| Maintenance/Action_Record ID | No | Maintenance report/history và recommendation tồn tại nhưng không có action/work-order ID. `Evidence is currently insufficient.` |
| Inspection-to-action relation | Partial | Inspection analysis tạo maintenance recommendation và prospective date, PDF pp. 7-8, 14, §4.3.3, Table 1, Fig. 11; không có FK, cardinality hoặc Action instance. |
| Maintenance history | Partial | `Maintenance Reports History` và `Routine Maintenance (2-3-2022)`, PDF pp. 10-13, §§4.2-4.3.1, Figs. 8-9; không có identified action records hoặc immutable sequence. |
| Repaired/unrepaired field | Partial | Text nêu defects “whether repaired or not”; populated status là `not treated`, PDF pp. 10, 12, §4.2, Fig. 8. Bằng chứng là category/current display, không phải event transition. |
| Current status | Yes | Fig. 8 populate `Status: not treated`; Figs. 11-14 populate current condition/deterioration levels, PDF pp. 12, 14-17. Đây chỉ là current scalar semantics. |
| Timestamped event history | No | Dated inspections/maintenance strings không có event ID, previous/new state, sequence hoặc append-only semantics. `Evidence is currently insufficient.` |
| Actor/time/reason | Partial | `Ahmed Khaled`, `Mohamed Ahmed`, inspection dates, defect causes/comments được populate, PDF pp. 12-13, Figs. 8-10; không có action actor/time/reason hoặc audit attribution. |
| Approval/rejection | No | Authority quyết định recommended date về mặt conceptual, nhưng không có approve/reject record, approver, time hoặc rationale, PDF p. 14, §4.3.3. `Evidence is currently insufficient.` |
| Repair execution | No | `Routine Maintenance (2-3-2022)` là history label; không có work scope, executor, start/end, result hoặc completion record. `Evidence is currently insufficient.` |
| Post-action verification | No | Framework validation không phải repair verification; không có verifier, criteria, before/after evidence hoặc outcome. `Evidence is currently insufficient.` |
| Closure/reopen | No | Không có closed/reopened state, guard hoặc event. `Evidence is currently insufficient.` |
| Forward/reverse query | Partial | Component/history field -> report và Defects History -> card được minh họa bằng UI, PDF pp. 12-13, Figs. 8-9. Không có query statement, returned exact set hoặc reverse query. |
| Integrity validation | No | §3.6 nêu QA/validation và §4 chạy case demonstration, nhưng không có constraint execution, invalid fixture, actual-versus-expected assertion hoặc integrity result, PDF pp. 9, 17-18. |

### 2.3 Strict interpretation of history and status

1. **History là danh sách record/report, không phải event sequence.** `Inspection Reports History`, `Maintenance Reports History` và `Defects History` là navigation collections; element-level values như `Routine Inspection (21-1-2022)` là dated references. Không có `Status_Event_ID`, ordering, previous/new state hoặc replay semantics.
2. **Repaired/unrepaired là current-state classification.** `Status: not treated` được display cho defect tại Fig. 8. Paper không ghi transition từ untreated sang repaired, không ghi transition actor/time, và không chứng minh `repaired` là verified.
3. **Không có stable `Action_Record` relation.** Recommendation và recommended date là inspection-analysis fields. Maintenance history label không đủ để xác nhận action identity, execution payload hoặc `Inspection_Record_ID -> Action_Record_ID` relation.
4. **Không có formal verification/closure.** Không có verifier, acceptance criteria, after-evidence, approve/reject outcome, closure guard hoặc reopen relation. `Evidence is currently insufficient.`

### 2.4 Populated evidence and consistency limitations

| Populated evidence | Exact location | Strict interpretation |
|---|---|---|
| `Maintenance Responsibility = Owner`; browser paths tới inspection/maintenance/defect histories; `Estimated Annual Maintenance Costs = 175,000 EGP` | PDF p. 12, Fig. 8 | Current project attributes và UI links, không phải accountable action assignment |
| `Expansion joint failure on DE-19`; `Status: not treated`; inspected `10-1-2023` | PDF p. 12, Fig. 8 | Populated current defect card, không phải status transition |
| `CO-6`; `Maintenance History = Routine Maintenance (2-3-2022)`; `Inspection History = Routine Inspection (21-1-2022)` | PDF p. 13, Fig. 9 | Dated history references attached to component, không phải identified events |
| Inspector `Ahmed Khaled`; routine inspection `10-1-2023`; image, cause/comment; next exceptional inspection `1-4-2023` | PDF p. 13, Fig. 10 | Populated inspection snapshot and plan, không có Inspection ID hoặc Finding ID |
| `Possible risk`, degree `0.8`, Level I, `Major repair or reconstruction`; recommended date blank | PDF p. 14, Fig. 11 | Current analysis/recommendation; no authorization or execution |
| Master report rows for `GI-41`, `EJ-5`, `CO-6`, `DE-19` | PDF p. 17, Fig. 14 | Generated schedule/report, không phải stable record relation hoặc query acceptance result |

Observed consistency limitations:

- Main case text/Figs. 8, 10, 12 use inspection date `10-1-2023`; Fig. 14 uses `10/1/2022` (PDF pp. 9, 12-17, §4; Figs. 8, 10, 12, 14).
- §4.3.1 states prior inspection `12 January 2022`; Fig. 9 shows `21-1-2022` (PDF pp. 12-13).
- Similar expansion-joint evidence is located at `DE-19` in Figs. 8 and 12 but at `EJ-5` in Fig. 14 (PDF pp. 12, 15, 17).
- `CO-6` spalling length is `800 mm` in Fig. 12 and `400 mm` in Fig. 14 (PDF pp. 15, 17).
- Level-I labels vary among `Potentially hazardous`, `Possible risk`, và `High Risk`; Level-V labels vary between `Exceptional condition` and `Like new` (PDF pp. 8, 14-16, Table 1; Figs. 11-13).

Các inconsistency này không chứng minh framework sai toàn bộ, nhưng bác bỏ việc nâng case demonstration thành integrity validation. Chúng trực tiếp hỗ trợ requirement cho controlled vocabulary, identity consistency, cross-view parity và expected oracle.

## 3. Celik et al. deep-read

### 3.1 Claim extraction

| Claim | Exact page/section | Implemented artifact | Validation | Limitation | Thesis implication |
|---|---|---|---|---|---|
| Provenance metadata nhằm xác định transaction, issuing discipline, object version và responsibility/liability | PDF p. 3, Abstract | Conceptual provenance requirement | Case framework discusses these dimensions | Không có explicit transaction ID hoặc liability record | Generic provenance requirement là prior art; operational semantics còn mở |
| Mỗi discipline update tạo tuple `operation`, `time`, `model`, `version`, `objectID`, `owner` | PDF p. 8, §5.1 | Event-like provenance struct/tuple | Framework implemented through smart contracts | Không có prior/new state, rationale, approval, status hoặc actual tuple values | Actor-object-operation-time-version là minimum provenance precedent, không phải maintenance `Status_Event` |
| User/discipline và object registration/update functions được implemented | PDF pp. 10-11, §6.2; Table 1; Appendix A.2-A.4, PDF pp. 15-16 | `newUser()`, `newObject()`, `Input()`, `updateUser()`, `updateObject()`, `getModel()`, `updateModel()`, `addUSer()`, `deleteUSer()`, `updateUSerProfile()` | Contracts deployed/tested in experimental environment | Contract topology không nhất quán giữa three contracts, two named contracts và single test contract | G2 nên technology-neutral; không sao chép contract topology như evidence of workflow completeness |
| Provenance history được described as chronological and immutable/tamper-proof | PDF p. 6, §4.1; pp. 7-8, §5.1; p. 12, §6.4; p. 14, §§8-9 | Blockchain-backed provenance architecture and file hash/proof narrative | Kovan/Ganache transactions được thực thi | Không có tamper mutation test; frontend có lúc retrieve provenance từ database thay vì blockchain | Immutable audit pattern established only at generic provenance level |
| Object history có thể truy xuất bằng BIM Model ID, Object ID và optional discipline ID | PDF pp. 11-12, §§6.3-6.4 | Verification/query interface and UI | Verification transactions được executed; cost scaling in Tables 2-4 | Không có query text, transaction hash hoặc returned semantic rows | Queryable-history capability partial; exact CQ answer contract vẫn là thesis validation |
| Verification contract checks actor-created/manipulated objects, operation/time and updated versions | PDF p. 12, §7 | Named `provenance` and `verification` contracts | Kovan experiments in §§7.1-7.3, Tables 2-4 | Validation targets provenance lookup/cost, không phải inspection correctness hoặc post-repair acceptance | Không đồng nhất provenance verification với `Verification_Record` |
| Operation/time verification được run cho 5-30 operations | PDF pp. 12-13, §7.1, Table 2 | Executed verification transactions | Gas `194235` tới `1165410`; five executions/parameter settings | Không hiển thị operation, actor, object hoặc actual returned time | Empirical evidence là cost/performance, không phải semantic correctness |
| Object-history verification được run cho 5-30 updates | PDF p. 13, §7.2, Table 3 | Executed history transactions | Gas `48033` tới `121050`; reported ETH costs | Không có actual version chain hoặc exact result set | Version/history implementation partial; replay/parity chưa established |
| Actor retrieval được run cho 5-30 actors | PDF p. 13, §7.3, Table 4 | Executed actor-retrieval transactions | Gas `55251` tới `291230`; reported ETH costs | Không có returned actor identities, roles hoặc permission outcomes | Actor query performance established; accountability semantics chưa established |
| Approval status có thể được determined và authenticator checks contract requirements | PDF pp. 11-12, §§6.3-6.4 | Capability/narrative, not an approval record | Không có populated approval transaction | Không có approver, decision, time, rationale, signature hoặc rejection/rework | Không được coi là accountable authorization |
| Role/access can be updated; leaving discipline can be blocked | PDF p. 10, Table 1; p. 11, §6.2; Appendix A.4 | User administration functions and scenario | Không có denied-call output hoặc policy test | Không có RBAC matrix, least privilege hoặc separation of duties | Exact permission model phải qua expert review/governance |
| Future validation must address scalability/performance | PDF p. 14, §9 | Explicit limitation/future work | Current work reports gas/cost | Testnet/prototype, not production deployment | Blockchain không phải mandatory solution cho G2; provenance requirements remain implementation-neutral |

### 3.2 Component audit

| Thành phần | Yes / Partial / No | Exact evidence |
|---|---|---|
| Transaction/Event ID | No | Abstract yêu cầu clear transaction identification và §4.1 nhắc blockchain receipt, nhưng không công bố `transactionID`, tx hash, block number hoặc populated receipt. `Evidence is currently insufficient.` PDF pp. 3, 6. |
| BIM object identity | Partial | Tuple có `address objectID`; `newObject()`/`Input()` và Model ID/Object ID query được mô tả, PDF pp. 8, 10-12, §§5.1-6.4. Không có populated on-chain object ID hoặc stability test. |
| Actor/discipline identity | Partial | Hashed user ID, unique Blockchain discipline ID, `owner`, Client/Architect/Engineer/MEP roles, PDF pp. 6, 8, 10, §§4.1, 5.1-6; Table 1. Không có populated address/hash result. |
| Timestamp | Partial | Tuple `uint time` và Table 1 output `Timestamp`; provenance/verification contracts store/check operation time, PDF pp. 8, 10, 12, §§5.1, 7. Không có actual event timestamp value. |
| Version history | Partial | Tuple `uint version`; chronological versions and update verification are described; 5-30 updates executed, PDF pp. 8, 12-13, §§5.1, 6.4, 7.2; Table 3. Không có returned version sequence. |
| Responsibility/liability | Partial | Abstract claims responsibility/liability can be recorded; tuple has `owner`, PDF pp. 3, 8. Không có `responsibility`/`liability` field or populated assignment. |
| Previous/new state | No | Printed tuple lacks old/new values, delta or predecessor relation, PDF p. 8, §5.1. `Evidence is currently insufficient.` |
| Reason/rationale | No | Table 1 has undefined `Txt`; scenario narrative is not a rationale field. `Evidence is currently insufficient.` PDF p. 10, Table 1. |
| Approval/authorization | No | “Whether it was approved” and authenticator narrative are capability statements; no approval entity/event, approver, decision or outcome, PDF pp. 11-12, §§6.3-6.4. |
| Immutable audit trail | Partial | Unchangeable/tamper-proof chronological provenance and immutable ledger are described, PDF pp. 6-8, 12, §§4.1, 5.1, 6.4. Không có tamper test và on-chain/off-chain boundary rõ. |
| Queryable history | Partial | Model ID/Object ID/discipline ID lookup and verification executions exist, PDF pp. 11-13, §§6.4-7.3; Tables 2-4. Không có exact query/returned history rows. |
| Tamper evidence | Partial | File hash/proof and tamper-proof architecture are described, PDF pp. 7-8, 11, §§5.1, 6.3. Không có modified-file/hash-mismatch experiment. |
| Role permissions | Partial | User registration/update/deletion and leaving-discipline access blocking are described, PDF pp. 10-11, Table 1, §6.2. Không có policy matrix, modifiers or denied-call result. |
| Separation of duties | No | Multiple roles and authenticator exist, but no enforced maker-checker/incompatible-role constraint or test. `Evidence is currently insufficient.` |
| Inspection/action semantics | No | `operation` covers generic create/share/add/delete/modify BIM activities; no inspection, finding, maintenance action, execution or condition semantics, PDF pp. 8, 10-12, §§5.1-7. |
| Verification/closure semantics | No | Verification contract checks provenance dimensions, not repair acceptance; no maintenance completion, closure or reopen. `Evidence is currently insufficient.` |

### 3.3 Four non-equivalent event concepts

| Concept | What Celik implements or discusses | Strict boundary |
|---|---|---|
| Blockchain transaction | Smart-contract function call; failed validation reverts execution, successful action broadcasts to network; cost/gas measured on Kovan, PDF pp. 10, 12-13, Table 1, §§7.1-7.3 | Ledger-level execution. No published transaction ID/receipt value; not a maintenance action merely because it is immutable. |
| BIM information-exchange event | Discipline updates/shares IFC model/object; event-like tuple stores `operation-time-model-version-objectID-owner`, PDF p. 8, §5.1 | Generic design/construction exchange. It lacks inspection/action/status/closure semantics. |
| Maintenance `Status_Event` | Not implemented | Requires action-scoped identity, previous/new workflow state, actor, time, reason and transition rule. Generic `operation` is insufficient. |
| Operational approval event | Paper mentions determining whether data was approved and authenticator checks requirements, PDF pp. 11-12, §§6.3-6.4 | Capability/contract validation is not persisted approve/reject decision by an authorized maintenance actor. |

Blockchain consensus validates block inclusion; authenticator/verification contract validates specified provenance conditions; neither is evidence of accountable maintenance authorization or post-action acceptance.

### 3.4 Implemented functions, executions, and limitations

The only main-text provenance tuple is reported at PDF p. 8, §5.1:

```text
struct contract [
  string operation,
  uint time,
  string model,
  uint version,
  address objectID,
  string owner
];
```

Strict classification: implemented event-like provenance aggregate, not a maintenance `Status_Event`. The tuple contains no explicit event ID, transaction hash, prior/new state, reason, approval, liability, evidence basis, verification outcome or closure relation.

| Experimental evidence | Exact result | What it validates | What it does not validate |
|---|---|---|---|
| Contract deployment | `provenance` 854979 and `verification` 767248 in reported deployment units, PDF p. 12, §7 | Contracts were deployed in experimental environment | Provenance completeness, semantic correctness, authorization or closure |
| Operation/time verification | 5-30 operations; gas 194235-1165410; five executions, PDF pp. 12-13, §7.1, Table 2 | Transaction execution and cost scaling | Actual object/actor/operation/time results |
| Object-history verification | 5-30 updates; gas 48033-121050, PDF p. 13, §7.2, Table 3 | Cost scaling for update-history verification | Returned chronological version records or replay correctness |
| Actor retrieval | 5-30 actors; gas 55251-291230, PDF p. 13, §7.3, Table 4 | Cost scaling for actor retrieval | Actor-role authorization, responsibility or separation of duties |

Material limitations:

- No transaction hash, block number, contract address, populated receipt, query text or returned semantic history rows are published.
- The frontend is reported to retrieve provenance from a database rather than directly from blockchain in one implementation description (PDF p. 11, §6.2), leaving the immutable boundary ambiguous.
- No deliberate tamper attempt, unauthorized call, role conflict, false approval, or altered-file/hash-mismatch case is tested.
- Contract count/topology is inconsistent: three functional contracts in §6.2, two named contracts in §7, and a single test contract in deployment narrative (PDF pp. 10-12).
- Tables 2-4 validate gas/cost/mining behavior, not the integrity or completeness of actor-object-operation-time-version semantics.
- The bridge case concerns design/model exchange; inspection and maintenance workflow are outside the implemented scenario.

## 4. Cross-paper comparison

| Study | Record identity | History/status | Actor/accountability | Audit/provenance | Operational maintenance coverage | Main missing element |
|---|---|---|---|---|---|---|
| Mohamed et al. (2023) | Component IDs yes; no Inspection, Finding or Action IDs (PDF pp. 9-17, §§4.1-4.6; Figs. 6-14) | Report/history lists and populated current statuses; no event sequence (PDF pp. 10-13, §§4.2-4.3.2; Figs. 8-10) | Inspector names/dates and generic `Owner`; no approval/permission model (PDF pp. 12-14, Figs. 8-11) | Photos, reports, causes and dates; mutable BrIM/UI semantics, no audit history (PDF pp. 12-17, Figs. 8-14) | Inspection/finding/recommendation strong; maintenance history label partial; no execution/verification | Stable inspection-action relation and status/verification/closure events |
| Celik et al. (2023) | Object/user/model fields partial; no published transaction/event ID (PDF pp. 6, 8, 10-12, §§4.1-7) | Generic chronological version/update provenance; no maintenance status (PDF pp. 8, 12-13, §§5.1, 6.4-7.2) | Discipline/user/owner and role administration partial; no accountable approve/reject or SoD (PDF pp. 8, 10-12, §§5.1-6.4; Table 1) | Blockchain-backed event-like tuple, history queries and cost experiments; tamper test absent (PDF pp. 8, 11-13, §§5.1, 6.3-7.3; Tables 2-4) | Generic BIM design-information exchange only | Operational inspection/action semantics and accountable authorization/closure |
| Li et al. (2023), Round 3A | Defect ID yes; component key partial; no Inspection/Action ID (PDF pp. 3, 8, §§Coding, Utilization) | Repair-history claim and `completed` current scalar (PDF p. 7, §Recommendations) | Recorder/Reviewer fields unpopulated (PDF p. 11, Fig. 12) | Form/photo/database statements (PDF pp. 7-12, Figs. 12-17) | Defect-to-recommendation/repair function | Formal Action identity, event history and verification |
| Piras et al. (2026), Round 3A | `IfcGlobalId` preserved for asset import (PDF pp. 18, 22-24, §§2.4.2, 3.1.2-3.2.2; Tables 6-7) | Current condition/latest check only (PDF pp. 13-14, 23-25, Tables 2-3, 7; Fig. 5) | No operational actor/approval | Source mapping and processing log partial (PDF pp. 14-15, Algorithm 1) | Work-order capability, no populated action (PDF pp. 19, 24, 26) | Write-back, action lifecycle and parity |
| Nuyts et al. (2024), Round 3A | Generic component IDs in fixtures (PDF p. 4, §3.4) | No operational status | None | Reproducible artifacts, no run lineage (PDF pp. 4-13, §4; Listings 2-36) | None | Chain-specific exact oracle and assertions |
| Hagedorn et al. (2023), Round 3A | Typed link identifiers partial (PDF pp. 5-8, §§2.4-3.1; Fig. 4; Listing 1) | No operational status event | None | ICDD metadata/link provenance potential (PDF p. 5, §2.4, Figs. 3-4) | Construction task links, not maintenance (PDF pp. 10-12, §3.2.3; Listings 2-3) | Operational events, controlled mutations and parity |

Round 3B therefore narrows but does not remove the Round 3A boundary. Mohamed establishes a stronger precedent for populated inspection/defect histories and current repaired/unrepaired semantics. Celik establishes a stronger precedent for generic actor-time-version provenance and executed history transactions. Neither reaches the operational chain from `Action_Record` through accountable review to verified closure.

## 5. Final novelty stress test

### 5.1 Stable `Inspection_Record`-`Action_Record` relation

**Claim ->** Stable record identities and explicit relation are required to distinguish recommendation, authorized work, execution and verification.  
**Prior art achieved ->** Mohamed populates inspection/finding attributes, histories and recommendations; Li provides defect ID and repair-history statement; Piras links assets to CMMS. Mohamed PDF pp. 10-17, §§4.2-4.6; Li PDF pp. 3, 7-12, §§Coding, Recommendations, Utilization; Piras PDF pp. 18, 22-26, §§2.4.2, 3.1.2-3.3.3, Tables 6-7.  
**Remaining gap ->** No reviewed paper publishes both `Inspection_Record_ID` and `Action_Record_ID`, relation cardinality, stable inverse navigation and populated execution relation.  
**Required thesis validation ->** Multi-finding/multi-action and aggregated-action fixtures; orphan, duplicate, wrong-type and missing-basis mutations; paired exact forward/reverse answers.  
**Final verdict -> FREEZE_AS_CORE_GAP.**

### 5.2 Immutable/queryable `Status_Event` history

**Claim ->** Current status must be a projection from ordered, actor-bound events rather than an editable scalar.  
**Prior art achieved ->** Mohamed has `not treated` and condition levels; Li has `completed`; Piras has `Condition`; Celik has generic operation-time-version provenance. Mohamed PDF pp. 12, 14-17, Figs. 8, 11-14; Celik PDF pp. 8, 12-13, §§5.1, 7.  
**Remaining gap ->** No maintenance-specific event ID, previous/new state, reason, action relation, valid transition, replay query or immutable status reconstruction.  
**Required thesis validation ->** Append-only fixtures, allowed/illegal transitions, current-state projection, sequence/chronology, supersession and history replay assertions.  
**Final verdict -> FREEZE_AS_CORE_GAP.**

### 5.3 Accountable authorization

**Claim ->** Approval/rejection requires identified actor, role, authority context, time, rationale and permission enforcement.  
**Prior art achieved ->** Mohamed distinguishes inspector recommendation from authority-set date; Celik implements user/discipline identity and role administration and mentions approval determination. Mohamed PDF p. 14, §4.3.3; Celik PDF pp. 10-12, §§6.2-6.4.  
**Remaining gap ->** No operational approve/reject event, RBAC matrix, separation-of-duties constraint, override record or unauthorized-decision test.  
**Required thesis validation ->** Authorized/unauthorized, self-approval, missing-rationale, reject/rework, revoked-role and override fixtures with retained outcomes.  
**Final verdict -> FREEZE_AS_CORE_GAP.**

### 5.4 Evidence-basis preservation

**Claim ->** Inspection, action, review and closure must retain exact evidence identity/version and derivation.  
**Prior art achieved ->** Mohamed stores images, causes, geometry, comments and reports; Hagedorn packages documents/triples/links; Celik uses model/object/actor/time/version and file hash/proof. Mohamed PDF pp. 12-17, Figs. 8-14; Hagedorn PDF p. 5, §2.4, Figs. 3-4; Celik PDF pp. 7-12, §§5.1-6.4.  
**Remaining gap ->** No complete source-version/hash -> inspection -> finding -> action rationale -> verification -> closure chain; Mohamed's cross-view inconsistencies expose missing binding controls.  
**Required thesis validation ->** Exact evidence/version forward and reverse queries; missing, stale, substituted and cross-view-inconsistent evidence fixtures.  
**Final verdict -> FREEZE_AS_SUPPORTING_GAP.**

### 5.5 Formal post-action verification

**Claim ->** Maintenance completion and closure require a linked verification record with independent actor, criteria, before/after evidence and outcome.  
**Prior art achieved ->** Mohamed has maintenance history and recommendations; Celik has a provenance verification contract. Mohamed PDF pp. 12-14, Figs. 8-11; Celik PDF p. 12, §7.  
**Remaining gap ->** Neither artifact verifies executed repair quality or provides verifier/criteria/accept-reject/rework semantics.  
**Required thesis validation ->** Populated verification pass/fail cases, evidence comparison and blocked closure when verification is absent, failed or unauthorized.  
**Final verdict -> FREEZE_AS_CORE_GAP.**

### 5.6 Guarded closure/reopen

**Claim ->** Closure and reopening are controlled events with preconditions, accountable actors and preserved history.  
**Prior art achieved ->** Mohamed has `not treated` (PDF p. 12, Fig. 8); Li has `completed` (PDF p. 7, §Recommendations); neither supplies guards.  
**Remaining gap ->** No closure event, accepted-verification precondition, closer/time/reason, reopen trigger or relation to new evidence/finding.  
**Required thesis validation ->** Valid closure, premature closure, failed-verification closure, reopen after new evidence, and immutable prior-state tests.  
**Final verdict -> FREEZE_AS_CORE_GAP.**

### 5.7 Chain-specific controlled mutations

**Claim ->** Validation contribution is chain-specific controlled corruption, not generic use of valid/invalid fixtures.  
**Prior art achieved ->** Nuyts establishes deliberate generic pass/fail fixtures (PDF pp. 3-4, §§3.1-3.4, Table 1, Fig. 2); Celik describes reverted/successful blockchain functions (PDF p. 10, Table 1) but does not publish chain-specific invalid data.  
**Remaining gap ->** No isolated duplicate record ID, orphan inspection-action link, missing evidence basis, illegal status transition, unauthorized approval, or closure-without-verification suite.  
**Required thesis validation ->** Machine-readable mutation manifest with expected focus ID, violation code/count, engine/version and exact actual-versus-expected assertion.  
**Final verdict -> FREEZE_AS_SUPPORTING_GAP.**

### 5.8 Paired forward/reverse acceptance tests

**Claim ->** UI navigation, inverse predicates and history capability do not establish exact bidirectional traceability.  
**Prior art achieved ->** Mohamed demonstrates forward-like UI navigation; Hagedorn direct/inverse relations; Piras two-direction visual lookup; Celik Model/Object/Discipline history-query capability. Mohamed PDF pp. 12-13, Figs. 8-9; Hagedorn PDF pp. 7-12, §§3.1-3.2.3, Listings 1-3; Piras PDF pp. 24-26, §§3.2.3, 3.3.1-3.3.3, Fig. 4; Celik PDF pp. 11-13, §§6.4-7.3.  
**Remaining gap ->** No complete operational CQ pairs with predeclared exact sets, automated assertions, reverse source reconstruction or declared permitted-loss policy.  
**Required thesis validation ->** Paired CQs from evidence to closure and closure to evidence, exact result sets, query-answer parity, plus separately declared transformation equivalence where applicable.  
**Final verdict -> FREEZE_AS_SUPPORTING_GAP.**

### 5.9 Complete integrated chain

**Claim ->** Contribution unit is the integrated identity-event-authorization-verification contract, not any individual BIM, history, provenance or constraint technique.  
**Prior art achieved ->** Across Round 1-3B, prior art covers BIM-linked condition documentation and report histories (Mohamed PDF pp. 10-17, §§4.2-4.6), component identity and recommendations (Mohamed PDF pp. 9-17, Figs. 6-14; Li PDF pp. 3, 7-8), current status (Mohamed PDF p. 12, Fig. 8; Li PDF p. 7), generic provenance transactions (Celik PDF pp. 8, 10-13, §§5.1-7.3), direct/inverse links (Hagedorn PDF pp. 7-12), executable constraints and deliberate fixtures (Nuyts PDF pp. 3-13; Hagedorn PDF pp. 10-16).  
**Remaining gap ->** No deep-read source integrates stable evidence/component/inspection/action identities, maintenance `Status_Event`, accountable authorization, formal post-action verification, guarded closure/reopen and exact chain-specific forward/reverse validation.  
**Required thesis validation ->** One populated end-to-end valid chain; isolated invalid families; retained authorization/verification/closure outcomes; exact bidirectional CQ results and current-state reconstruction.  
**Final verdict -> FREEZE_AS_CORE_GAP.**

## 6. G2 final decision matrix

| G2 decision | Round 1-3B evidence | Final status | Required specification action |
|---|---|---|---|
| `BIM_GUID`/component identity | Piras preserves `IfcGlobalId` (PDF pp. 18, 22-24, Tables 6-7); Mohamed populates component codes (PDF pp. 9-17, Figs. 6-14); Li exposes mapping weakness (PDF pp. 8, 13) | FREEZE | Keep internal `Component_ID`, external `IFC_GlobalId`/BIM anchor, human-readable code and model-version context; add duplicate/stale/replacement constraints |
| `Condition_Evidence_ID` | Li has generated defect ID (PDF p. 3, §Coding); Mohamed shows multiple evidence objects without stable defect ID (PDF pp. 12-17, Figs. 8-14) | FREEZE | Require distinct stable evidence identity, source reference, observed-at, unit/location and component binding |
| `Inspection_Record_ID` | Mohamed populates inspection attributes/history but no record ID (PDF pp. 12-17, §§4.3-4.6); no Round 1-3B source supplies one | FREEZE | Require stable ID separate from component/finding; bind inspector, time, scope, source evidence and record version |
| `Action_Record_ID` | Mohamed recommendation/history (PDF pp. 12-17), Li repair statement (PDF p. 7), and Piras work-order capability (PDF pp. 19, 24, 26) lack a populated action ID | FREEZE | Require stable action ID and distinguish recommendation, authorized plan, execution and result |
| Inspection-Action cardinality | Functional linkage exists in Mohamed (PDF pp. 7-8, 14, Table 1, Fig. 11) and Li (PDF pp. 7-8); no published PK/FK/cardinality | EXPERT_REVIEW_REQUIRED | Do not force 1:1; review many findings-to-actions, one action addressing multiple findings and inspection-level aggregation |
| `Workflow_Status` | Mohamed `not treated` (PDF p. 12, Fig. 8), Li `completed` (PDF p. 7), and Piras `Condition` (PDF pp. 13, 23-25) are current scalars | FREEZE | Define as current projection scoped to action/workflow; prohibit treating it as history or asset-condition synonym |
| `Status_Event` | Celik supplies generic operation-time-version provenance (PDF pp. 8, 12-13, §§5.1, 7) but no maintenance event; scalar/event confusion persists | FREEZE | Separate append-only entity with stable ID, action relation, previous/new status, actor, occurred-at, reason and authorization context |
| Actor/role model | Mohamed has inspector/Owner (PDF pp. 12-14, Figs. 8-11); Celik has discipline/user/owner and role updates (PDF pp. 8, 10-11, §§5.1-6.2) | EXPERT_REVIEW_REQUIRED | Freeze `Agent_ID` structurally; experts define domain roles, authority boundaries, delegations and accountable owner |
| Authorization | Celik capability/user administration is not operational approval (PDF pp. 10-12, §§6.2-6.4); no approve/reject record in corpus | FREEZE_PROVISIONALLY | Require decision event, actor/role/time/rationale and permission check; exact role matrix and SoD rules require expert review |
| `Verification_Record` or subtype | Celik verification is provenance verification (PDF pp. 12-13, §§7-7.3); Mohamed has no post-action verification (PDF pp. 12-17) | FREEZE | Keep separate action-linked record/subtype with verifier, criteria, before/after evidence, outcome and verified-at |
| Closure/reopen | Mohamed `not treated` (PDF p. 12, Fig. 8) and Li `completed` (PDF p. 7) are scalars; no guards or reopen | FREEZE_PROVISIONALLY | Require accepted verification and authorized closer before closure; define reopen event and evidence trigger; exact vocabulary via expert review |
| Event provenance fields | Celik implements actor/object/operation/time/version (PDF pp. 8, 12, §§5.1, 7) but lacks event ID, before/after and rationale | FREEZE | Minimum event envelope: event ID, subject/action ID, actor/role, timestamp, previous/new state, reason, record version and source reference |
| Evidence payload provenance | Mohamed has image/report fields (PDF pp. 12-17, Figs. 8-14); Celik has hash/version pattern (PDF pp. 8, 11-12); exact G1 payload not yet available | WAIT_FOR_G1_PAYLOAD | Bind source payload ID, acquisition/processing version, hash, quality/confidence, component mapping and permitted loss after G1 delivery |
| Constraint families | Nuyts/Hagedorn execute generic constraints (Nuyts PDF pp. 3-13; Hagedorn PDF pp. 10-16); Mohamed exposes identity/status inconsistencies (PDF pp. 8-17) | FREEZE | Keep uniqueness, requiredness, datatype, vocabulary, referential integrity, cardinality, chronology, transition, authorization, evidence and closure guards |
| Fixture/oracle | Nuyts establishes fixtures but not exact oracle (PDF pp. 3-13); Mohamed exposes realistic cross-view inconsistencies (PDF pp. 8-17) | FREEZE | Require isolated mutation, expected focus ID/code/count, engine/version, retained report and automated exact-set assertion |
| Forward/reverse parity | Hagedorn inverse links (PDF pp. 7-12), Piras visual lookup (PDF pp. 24-26), Mohamed UI navigation (PDF pp. 12-13), and Celik query capability (PDF pp. 11-13) stop before exact parity | FREEZE | Define paired CQ answers and query-answer parity separately from transformation round-trip; declare equivalence and permitted loss |

`FREEZE` ở đây là quyết định specification-development, không phải tuyên bố G2 hoặc G3 PASS. Exact field types, enumerations, permissions và empirical acceptance vẫn phải được reviewed và tested.

## 7. Final Paper 2 boundary

### 7.1 Central claim for G2 design

> Trong phạm vi các tài liệu đã sàng lọc và deep-read, Paper 2 designs an implementation-neutral, identity-governed evidence-to-action contract that separates component and record identities, current workflow state and immutable status events, and connects accountable authorization and post-action verification to guarded closure; the contract is prepared for chain-specific constraint and paired forward/reverse validation.

### 7.2 Contribution statements

1. Trong phạm vi các tài liệu đã sàng lọc và deep-read, contribution 1 là một record-event specification tách `Condition_Evidence`, BIM-addressed `Component`, `Inspection_Record`, `Action_Record`, current `Workflow_Status` và append-only `Status_Event`, với explicit identity và relation semantics.
2. Trong phạm vi các tài liệu đã sàng lọc và deep-read, contribution 2 là accountable action-lifecycle specification gồm authorization/rejection, actor-role-time-rationale provenance, post-action `Verification_Record`, và guarded closure/reopen semantics.
3. Trong phạm vi các tài liệu đã sàng lọc và deep-read, contribution 3 là validation contract cho chính integrated chain, gồm controlled mutations, stable violation oracles và paired forward/reverse competency-query expectations.

### 7.3 Claims removed from novelty

- BrIM/BIM-linked bridge inspection documentation, defect visualization hoặc centralized report generation.
- Component coding hoặc `IfcGlobalId`-based BIM/CMMS linkage.
- Inspection history, maintenance report history hoặc repaired/unrepaired display nói chung.
- Current condition/status, color coding hoặc maintenance recommendation nói chung.
- Generic actor-object-operation-time-version provenance.
- Blockchain-based BIM provenance, immutable-ledger capability hoặc smart-contract transaction execution.
- Generic user/role administration, queryable history capability hoặc provenance verification.
- Generic compliant/non-compliant fixtures, executable constraints, direct/inverse links hoặc two-direction UI lookup.
- Closed-loop maintenance claim dựa chỉ trên `not treated`, `repaired`, `completed`, current condition hoặc maintenance-history label.
- Accountable authorization claim dựa chỉ trên role label, authority narrative, blockchain validator hoặc authenticator.

### 7.4 Claims permitted only after G3 validation

- The specification is executable and internally consistent.
- Every valid chain is retrievable in both directions with exact expected answers.
- Current `Workflow_Status` reconstructs exactly from the latest valid `Status_Event` under declared ordering rules.
- Invalid identity, relation, chronology, transition, authorization, evidence and closure cases are rejected with expected violation codes.
- Closure cannot occur without accepted verification and an authorized actor.
- Reopen preserves prior closure and creates a valid new event path.
- Query-answer parity and any claimed transformation equivalence meet the declared policy and permitted-loss rules.

## 8. Literature search closure decision

1. **Có thể đóng vòng tìm kiếm G2-G3 không?** Có. Round 3B đã đọc đúng hai đối thủ được Round 3A chỉ định để stress-test history/status và provenance/accountability. Mohamed strengthens prior art for populated inspection/defect history and current repaired/unrepaired display; Celik strengthens prior art for generic transaction provenance. Hai bài không cung cấp integrated maintenance event/authorization/verification/closure contract và không làm mất core gap.
2. **Corpus hiện tại đã đủ để xây G2 Specification v0.1 chưa?** Đủ cho structural entities, identity separation, scalar-versus-event rule, provenance envelope, verification/closure guard requirement, constraint families, fixture/oracle contract và paired CQ contract. Chưa đủ để tuyên bố implementation validity hoặc G2/G3 PASS.
3. **Còn tài liệu nào bắt buộc phải tìm thêm không?** Không có tài liệu bắt buộc nào trong bounded Round 1-3B corpus. Không còn identified unread competitor có khả năng thay đổi structural novelty boundary. Exact unresolved choices là domain-governance questions, không phải literature-discovery questions.
4. **Những khoảng trống đủ để freeze:** stable Inspection-Action identity relation; maintenance-specific `Status_Event`; accountable authorization; formal post-action verification; guarded closure/reopen; integrated chain; supporting evidence binding, chain-specific mutations và paired forward/reverse acceptance.
5. **Những vấn đề chuyển sang expert review:** Inspection-Action cardinality; recommendation/work-order/execution boundaries; role and delegation model; permission matrix; separation of duties; allowed transition vocabulary; verification criteria; closure/reopen policy; exceptional override handling.
6. **Những vấn đề chờ G1 payload:** exact `Condition_Evidence` source fields; source/payload IDs; acquisition and processing versions; units, quality/confidence and uncertainty context; component-binding method; hash/version location; permitted-loss and stale-mapping behavior.

Closure conditions are satisfied:

- Round 3A identified exactly Mohamed and Celik as the remaining structural competitors; both are now deep-read.
- Round 3B narrows prior-art boundaries but preserves the core integrated gap.
- Unresolved fields can be resolved by expert review, governance decision or G1 payload.
- No broad additional search is required before G2 Specification v0.1.

**Decision: `CLOSE_SEARCH`.**

## 9. Search closure register

| Evidence topic | Key sources | Final evidence status | Search status |
|---|---|---|---|
| BIM/component identity | Piras; Mohamed; Li | External BIM/component anchors established; revision/replacement governance remains specification-defined | CLOSED_WITH_LIMITATION |
| `Condition_Evidence` identity and payload | Li; Mohamed; Hagedorn | Evidence identity precedent partial; exact source/version/quality payload awaits G1 | G1_DEPENDENT |
| `Inspection_Record` identity | Mohamed; Li | Inspection attributes/reports established; stable inspection identity absent | CLOSED |
| `Action_Record` identity and semantics | Mohamed; Li; Piras | Recommendation/history/capability established; stable action identity and execution record absent | CLOSED_WITH_LIMITATION |
| Inspection-Action cardinality | Mohamed; Li | Functional linkage established; exact domain cardinality unresolved | EXPERT_REVIEW_DEPENDENT |
| Current status versus event history | Mohamed; Li; Piras; Celik | Current scalars and generic provenance established; maintenance event sequence absent | CLOSED |
| Actor/time/version provenance | Celik; Mohamed | Generic actor-object-operation-time-version prior art established | CLOSED_WITH_LIMITATION |
| Accountable authorization and SoD | Celik; Mohamed; Li | Role/capability evidence partial; operational approve/reject and SoD absent | EXPERT_REVIEW_DEPENDENT |
| Immutable/queryable audit history | Celik; Hagedorn | Generic immutable/queryable provenance and link history partial; operational chain audit absent | CLOSED_WITH_LIMITATION |
| Post-action verification | Mohamed; Celik; Li | Framework/provenance verification exists, but repair acceptance record absent | CLOSED |
| Closure/reopen | Mohamed; Li | Closure-like current scalars only; formal guards/events absent | EXPERT_REVIEW_DEPENDENT |
| Constraint families | Piras; Nuyts; Hagedorn; Mohamed | Generic executable checks established; chain-specific rules remain thesis work | CLOSED |
| Fixture/oracle | Nuyts; Hagedorn; Mohamed | Deliberate fixtures established; exact chain oracle and cross-view consistency validation absent | CLOSED_WITH_LIMITATION |
| Forward/reverse parity | Hagedorn; Piras; Mohamed; Celik | Link/query/UI bidirectionality partial; exact operational parity absent | CLOSED_WITH_LIMITATION |
| Complete integrated chain | All Round 1-3B deep-read studies | Components exist separately; integrated identity-event-authorization-verification-closure contract not found in bounded corpus | CLOSED |

`CLOSED_WITH_LIMITATION` chỉ ghi nhận kết luận giới hạn trong corpus đã đọc. `EXPERT_REVIEW_DEPENDENT` và `G1_DEPENDENT` là specification inputs và không giữ literature search ở trạng thái mở.

## 10. Next actions

1. Ban hành ADR `Action-Status-Event`, khóa distinction giữa recommendation, authorized action, execution, current projection và append-only event.
2. Xây G2 Decision Register từ Section 6, gán owner, due decision và evidence class cho mọi `FREEZE_PROVISIONALLY`, `EXPERT_REVIEW_REQUIRED` và `WAIT_FOR_G1_PAYLOAD` item.
3. Khóa ER model v0.1 với distinct identities cho evidence, component, inspection, finding, action, status event, agent và verification; không khóa 1:1 Inspection-Action trước expert review.
4. Khóa CQ Registry gồm paired forward/reverse questions từ evidence tới closure và closure về exact evidence/version, kèm expected result sets.
5. Khóa Constraint Catalogue cho identity, requiredness, vocabulary, typed reference, cardinality, chronology, transition, authorization, evidence basis, verification và closure guards.
6. Tạo Fixture/Oracle Manifest với valid baseline, isolated mutations, expected focus IDs, violation codes/counts, engine/version và retained outputs.
7. Tổ chức expert review giới hạn ở cardinality, action lifecycle, roles/permissions/SoD, transition vocabulary, verification criteria và closure/reopen/override policy; nhận G1 payload để khóa evidence binding.
8. Mở bounded G3 prototype chỉ sau khi ADR, Decision Register, ER v0.1, CQ Registry, Constraint Catalogue và Fixture/Oracle Manifest được baselined; prototype không được mô tả là G2/G3 PASS.

**AI-assisted research disclosure:** ZoteroMCP và AI-assisted full-text extraction được dùng để truy xuất và đối chiếu hai bài Round 3B. Mohamed được đọc từ exact publisher PDF vì item không có trong Zotero library hiện tại; Celik được đọc từ Zotero attachment. Không có Zotero writeback, note, tag, CSV, schema hoặc code được tạo.

`CLOSE_SEARCH`
