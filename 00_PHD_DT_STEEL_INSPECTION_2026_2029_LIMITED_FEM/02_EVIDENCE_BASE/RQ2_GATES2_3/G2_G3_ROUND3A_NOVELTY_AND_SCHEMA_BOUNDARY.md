# G2-G3 Round 3A Novelty and Schema Boundary

**Research mapping:** RQ2/WP2 -> Chapter 5 -> Paper 2 -> Gate 2-3  
**Deep-read date:** 2026-08-04  
**Locked chain:** `Condition_Evidence -> BIM component -> Inspection_Record -> Action_Record -> Status_Event -> accountable review -> verified closure`  
**Locked corpus:** đúng bốn bài Li et al. (2023), Piras et al. (2026), Nuyts et al. (2024), và Hagedorn et al. (2023). Không sử dụng bài thứ năm để hỗ trợ claim.

Nguồn đọc:

- Li et al. (2023), DOI `10.1038/s41598-023-27924-6`, Zotero key `YY8TP9ZT`, PDF attachment `ER985KT3`.
- Piras et al. (2026), DOI `10.3390/app16104642`, Zotero key `P3YLFNJZ`, PDF attachment `7NWG5TLX`.
- Nuyts et al. (2024), DOI `10.1016/j.aei.2024.102443`. Item không có trong Zotero hiện tại; đọc đúng accepted-manuscript PDF từ Ghent University repository, được DOI/OpenAlex/Unpaywall liên kết tới bài.
- Hagedorn et al. (2023), DOI `10.1016/j.autcon.2023.105106`. Item không có trong Zotero hiện tại; đọc đúng full-text PDF từ Eindhoven University of Technology repository.
- Chỉ kiểm tra supplementary repositories do chính Nuyts và Hagedorn dẫn trong bài. Không thêm, sửa, gắn tag hoặc tạo note trong Zotero.

Supplementary snapshots inspected on 2026-08-04:

- Nuyts OSF root cited at PDF p. 3 footnote 2 and p. 14 Data availability: node `5rwt6`, view-only token `7637d2f2718341a59a5bd6635965e973`, API `date_modified=2024-02-13T18:12:32.184491Z`, inspected 2026-08-04. The project is not an immutable registration; repository-absence findings are limited to this dated snapshot. Approach subprojects and inspected files are named in Section 5.
- Hagedorn directly cites `https://philhag.github.io/icdd-shacl-validation` at PDF p. 3 footnote 2 and p. 17 Data availability. That landing page links to `github.com/philhag/icdd-shacl-validation`; inspected commit `b15113f213abdf03bbb4350d91c10ecd12d1f194`, paths `datasets/{1..4}/`, `rules/{1..3}/shapes-{1,2}.ttl`, and `sourcecode/`.

Quy ước:

- `PDF p.` là số trang vật lý của file PDF đã đọc.
- `Yes` chỉ dùng cho entity, record, rule hoặc query được mô tả và thực thi rõ. UI capability, platform capability, conceptual statement và future work không được nâng thành `Yes`.
- Deliberate negative test yêu cầu phân biệt fixture cố ý sai, expected result, execution, và actual-versus-expected assertion.
- Mọi absence claim chỉ áp dụng cho đúng bốn tài liệu Round 3A. Khi full text không đủ để xác nhận, báo cáo ghi `Evidence is currently insufficient.`

## 1. Executive summary

- **Đối thủ gần nhất về defect-to-repair records:** Li et al. (2023). Bài triển khai defect ID, MySQL defect database, component/defect display linkage và maintenance recommendation; bài chỉ tuyên bố repair records được lưu và defect đã giải quyết được đánh dấu `completed` (defect ID: PDF p. 3, **Coding**; recommendation/completion statement: p. 7, **Recommendations**, Table 4; linkage narrative: p. 8, **Utilization**; UI: pp. 12-15, Figs. 13-17). Không có populated repair record, tên bảng/cột repair, Action ID, actor/time, execution payload, verification hoặc reopen relation. `completed` là current scalar semantics, không phải `Status_Event` history.
- **Đối thủ gần nhất về BIM-CMMS identity:** Piras et al. (2026). Bài giữ `IfcGlobalId` làm unique asset identifier khi import 428 maintainable assets vào OpenMAINT và ánh xạ Pset qua JSON (PDF pp. 18, 22-23, §§2.4.2, 3.1.2-3.2.1; Tables 6-7). Figure 4 mô tả architecture ở PDF p. 19; visual lookup hai hướng được mô tả và triển khai ở pp. 24-26, §§3.2.3, 3.3.1-3.3.3. Luồng dữ liệu vẫn một chiều IFC-to-CMMS; CMMS-to-IFC write-back và transactional synchronization được xác nhận là chưa có (PDF pp. 29-30, §4.3).
- **Bài mạnh nhất về deliberate fixtures:** Nuyts et al. (2024). Bài tạo four variants cho IFC/RDF (`pass`, `fail`, `pass_preprocessed`, `fail_preprocessed`) và two fixtures cho XML/JSON (`pass`, `fail`), rồi dùng chúng theo yêu cầu của tám approaches trên năm requirement categories (PDF pp. 3-4, §§3.1-3.4; Table 1; Fig. 2; OSF root cited above). Artifacts có actual outputs cho XSD, JSON Schema, SPARQL và SHACL, nhưng không có machine-readable oracle manifest, automated diff/assertion hoặc false-pass/false-fail metrics (PDF pp. 4-13, §4; Listings 2-36; OSF approach subprojects).
- **Bài mạnh nhất về direct/inverse link validation:** Hagedorn et al. (2023). Bài materialize direct và inverse RDF predicates từ ICDD links, rồi dùng chúng trong SHACL validation trên bốn datasets và ba link configurations (PDF pp. 5-12, §§2.4-3.2; Figs. 4-9; Listings 1-3; Tables 1-3). Đây là relation-level reverse navigation, không phải reverse transformation, source reconstruction hoặc round-trip parity (PDF pp. 16-17, §§4.3-5).
- **Novelty boundary:** generic BIM-linked defect management, IFC-to-CMMS identity import, deliberate valid/invalid fixtures, executable constraints, và direct/inverse RDF navigation đều đã có prior art trong bốn bài. Novelty không còn defensible ở từng kỹ thuật riêng lẻ. Ranh giới còn lại là integrated, identity-governed record-event contract với stable inspection-action relation, immutable event history, accountable authorization, formal verification, guarded closure/reopen, chain-specific mutations, và exact forward/reverse acceptance oracle.
- **G2 có thể khóa sau Round 3A:** tách component identity khỏi record identity; tách current condition/status scalar khỏi `Status_Event`; giữ `Inspection_Record`, `Action_Record`, `Status_Event`, `Agent`, và `Verification_Record` là các entity riêng; dùng chain-specific valid/invalid fixtures với expected violation codes; định nghĩa forward/reverse acceptance riêng với round-trip parity. Exact cardinality, Action fields, role permissions, transition vocabulary và verification criteria chưa đủ evidence để freeze.
- **Gate interpretation:** Round 3A đủ để khóa structural boundary của G2 v0.1, nhưng chưa đủ để khóa toàn bộ fields/cardinalities hoặc tuyên bố G2/G3 PASS.

## 2. Evidence extraction theo từng bài

### 2.1 Li et al. (2023)

#### Claim extraction

| Claim được chứng minh | Exact page/section | Implemented artifact | Validation | Limitation | Thesis implication |
|---|---|---|---|---|---|
| BMS là web prototype dùng HTML/CSS/JavaScript, PHP và MySQL | PDF p. 2, **Methods - Workflow of the development and utilization of BMS**, Fig. 1 | Web BMS, data layer và model layer | Case Cocodala được chạy; không có test log | Không có ERD, DDL, schema hoặc source code | Chỉ dùng như operational prototype precedent, không dùng làm database specification |
| Upload defect tự tạo ID bằng prefix cộng IFD code, ví dụ `1-68-10 10 10`, tiếp theo `2-68-10 10 10` | PDF p. 3, **Coding of bridge defect data**, sau Table 3 | Defect-occurrence ID generation | Hai populated examples trong text | Không nêu uniqueness scope, concurrency, immutability hoặc taxonomy migration | Li supports defect-occurrence identity only; a distinct `Condition_Evidence_ID` remains thesis-defined |
| Defect model được ghép tới bridge model bằng corresponding `ID attribute` trong MySQL sau Revit -> IFC 2x3 -> OBJ | Linkage narrative: PDF p. 8, **Utilization of the BIM-based Cocodala bridge defect maintenance system**; UI: PDF p. 13, Fig. 15 | One-way visualization linkage | Deck-crack được hiển thị trên BMS | Không đặt tên ID, không có `IfcGlobalId` mapping; OBJ làm mất native parameters | Không được coi là stable BIM-database identity contract |
| Inspection form có bridge/date/section/last inspection/structure/component/type/scale/location/characteristic/recorder/reviewer | PDF p. 11, **Collection of the Cocodala bridge defect data**, Fig. 12 | Populated business form | Một inspection row được điền | `Recorder` và `Reviewer` trống; không chứng minh MySQL schema | Hỗ trợ minimum inspection fields ở mức form, không hỗ trợ `Inspection_Record_ID` |
| Upload UI có structure, component, location, defect type, parameter, scale và evidence file | PDF p. 12, **Collection...**, Fig. 13 | Populated UI form | Ví dụ `Site Code S3-1`, transverse crack, image `01-crack.jpg` | Width 5 cm ở Fig. 13 khác width 2 cm ở Fig. 12; không có reconciliation | G2 cần source record binding và consistency constraint |
| Maintenance recommendation nối defect/score tới four priorities | PDF p. 7, **Recommendations for bridge maintenance suggestions**, Table 4; narrative: pp. 8-9, **Utilization/Discussion**; UI: PDF p. 15, Fig. 17 | Rule table và populated recommendation UI | Bốn recommendation examples | Không có recommendation/action ID, rule version, approval hoặc link tới inspection row | Action recommendation không đồng nghĩa formal `Action_Record` |
| Solved defects được đánh dấu `completed`; repair records được lưu | PDF p. 7, **Recommendations for bridge maintenance suggestions** | Textual implementation statement | Không có populated repair record | Không có field list, ID, actor/time, verification, event sequence hoặc reopen | `completed` chỉ là current scalar; formal action/closure chưa established |
| Revit-to-OBJ conversion làm mất native parameters; code hiện tại không định vị defect chính xác và QR được đề xuất | PDF p. 13, **Discussion/limitations** | Confirmed implementation limitation; QR là future work | Không có loss report hoặc QR test | Mapping và identity hiện tại không ổn định | G2 phải có declared loss policy, persistent component key và stale-link checks |

#### Component audit

| Thành phần | Yes / Partial / No | Exact evidence |
|---|---|---|
| Stable component/asset ID | Partial | Unnamed MySQL `ID attribute` ở narrative PDF p. 8; `Site Code S3-1` ở p. 12, Fig. 13; display ở p. 13, Fig. 15; tác giả xác nhận code chưa định vị chính xác ở p. 13 |
| BIM/IFC GlobalId mapping | No | IFC 2x3 được xuất rồi chuyển OBJ, nhưng không có `IfcGlobalId`, crosswalk hoặc populated GUID. `Evidence is currently insufficient.` |
| Defect/Condition_Evidence ID | Partial | Auto-generated defect-occurrence IDs `1-68-10 10 10` và `2-68-10 10 10`, PDF p. 3, **Coding...**; không có distinct evidence-record ID |
| Inspection_Record ID | No | Fig. 12 có `No.` cho row nhưng không có inspection-event ID. `Evidence is currently insufficient.` |
| Action/repair/work-order ID | No | Repair records chỉ được nêu trong text; không có ID hoặc schema, PDF p. 7 |
| Inspection-to-action relation | Partial | Inspection input -> defect database -> score -> recommendation được mô tả ở PDF pp. 2, 7-8, Fig. 2 và được minh họa trong UI ở pp. 12-15, Figs. 13-17; không có FK/cardinality |
| Current status field | Partial | `completed` cho solved defect, PDF p. 7; không có populated field hoặc controlled vocabulary |
| Timestamped Status_Event history | No | Không có event ID, previous/new state hoặc ordered events. `Evidence is currently insufficient.` |
| Actor/time/reason | Partial | Date, last inspection date, Recorder, Reviewer ở PDF p. 11, Fig. 12; actor fields trống và không có reason |
| Approval/rejection | No | `Reviewer` field trống không chứng minh approval workflow. `Evidence is currently insufficient.` |
| Repair execution record | Partial | Repair-record storage được tác giả tuyên bố ở p. 7, nhưng không có populated execution record |
| Post-action verification | No | Không có reinspection, before/after evidence hoặc acceptance record. `Evidence is currently insufficient.` |
| Closure/reopen rule | Partial | `completed` là closure-like scalar; không có guard, timestamp hoặc reopen |
| Provenance/audit history | Partial | Inspection form, evidence photo và historical repair statement tồn tại; không có source ID/hash/version/change history |
| Executable constraints | No | Có score/recommendation logic nhưng không công bố database/integrity/lifecycle constraints. `Evidence is currently insufficient.` |
| Deliberate invalid fixtures | No | Không có intentionally invalid record hoặc controlled corruption. `Evidence is currently insufficient.` |
| Predefined expected result | Partial | Tables 3-4 và score-color rules định nghĩa expected mapping, nhưng không được dùng như test oracle |
| Actual-versus-expected assertion | No | Không có pass/fail assertion hoặc exact result comparison. `Evidence is currently insufficient.` |
| Forward traceability | Partial | Inspection/defect input -> ID/database -> BIM display -> score -> advice được minh họa, nhưng không cùng stable record ID xuyên chuỗi |
| Reverse traceability | No | Không có query từ recommendation/component về source inspection. `Evidence is currently insufficient.` |
| Round-trip parity | No | Revit -> IFC -> OBJ là một chiều và lossy; không có reconstruction/equality test |

### 2.2 Piras et al. (2026)

#### Claim extraction

| Claim được chứng minh | Exact page/section | Implemented artifact | Validation | Limitation | Thesis implication |
|---|---|---|---|---|---|
| Workflow chạy Revit/IFC4 -> Python/IfcOpenShell enrichment -> buildingSMART validation -> OpenMAINT import | PDF pp. 10-11, §§2-2.1, steps 1-7; pp. 12-19, §§2.2-2.4 | Standalone post-export enrichment and import pipeline | Hai residential cases | Handover pipeline, không phải dynamic synchronization | BIM-CMMS import không còn là novelty |
| `ConstantElementProperties` chứa bảy FM fields | PDF p. 13, §2.3, Table 2 | `IfcPropertySet` và `IfcPropertySingleValue` specification | Pset được đọc qua multiple viewers | Figure 2 dùng `CustomElementProperties` và datatype/vocabulary khác Table 2 | G2 phải version field dictionary và kiểm tra schema-vocabulary consistency |
| Script tạo hoặc cập nhật Pset trong IFC đang xử lý và sinh processing log | PDF pp. 14-15, §2.3, Algorithm 1 | `pset.add_pset`, `pset.edit_pset`, enriched IFC và log | Table 5 báo no processing errors/missing entities | Không công bố source code hoặc log artifact | Đây là within-file enrichment, không phải CMMS write-back |
| JSON template ánh xạ IFC/Pset sang OpenMAINT; `IfcGlobalId` là unique asset identifier | PDF p. 18, §2.4.2; PDF p. 23, §3.2.1, Table 7 | JSON mapping và CMMS asset creation | Four asset classes x three fields checked in Table 6, p. 22 | Không công bố JSON document, internal OpenMAINT key hoặc source-target value pairs | Identity contract có precedent cho initial import; ownership/revision policy còn mở |
| 428 maintainable assets được tạo từ khoảng 9000 IFC elements | PDF p. 20, §3, Table 5; pp. 22-24, §§3.1.2-3.2.2 | Populated OpenMAINT database | 100% workflow success được báo cáo | Fig. 5 p. 25 hiển thị 398 items, không được giải thích | G2 phải có reconciliation count và import manifest |
| buildingSMART service kiểm tra STEP syntax, IFC4 schema, normative rules, inverse/cardinality/type; viewers đọc Pset | PDF p. 17, §2.4.1; pp. 20-22, §§3-3.1.1, Table 5, Fig. 3 | Executed positive IFC validation và cross-viewer checks | 100% schema compliance được báo cáo | Không có invalid fixture, report ID hoặc machine-readable result | Positive conformance phải tách khỏi chain-integrity negative tests |
| BIM selection mở CMMS card; CMMS record locate/isolate BIM element | Architecture: PDF p. 19, Fig. 4; implementation: PDF pp. 24-26, §§3.2.3, 3.3.1-3.3.3 | Visual bidirectional lookup bằng GUID | 428 assets được báo cáo accessible | Không truyền update data ngược về IFC | Reverse lookup không phải two-way exchange hoặc parity |
| OpenMAINT có thể liên kết work order với component | PDF p. 19, §2.4.2; pp. 24, 26, §§3.2.3, 3.3.2 | Platform/UI capability | Không có populated work-order instance | Không có work-order ID/status/execution/closure | Không được nâng capability thành `Action_Record = Yes` |
| Workflow một chiều; maintenance completion, inspection outcomes và replacement không được write back | PDF pp. 29-30, §4.3 | Explicit implementation boundary | Bidirectional synchronization được để future work | Không có transaction/version/conflict handling | Transactional synchronization và parity vẫn mở |

#### Component audit

| Thành phần | Yes / Partial / No | Exact evidence |
|---|---|---|
| Stable component/asset ID | Partial | Original `IfcGlobalId` giữ làm CMMS unique asset identifier cho initial import, PDF pp. 18, 22-24, §§2.4.2, 3.1.2-3.2.2, Tables 6-7; persistence qua IFC revision/replacement/resynchronization không được test |
| BIM/IFC GlobalId mapping | Yes | `IfcGlobalId -> Asset unique identifier`, PDF p. 23, Table 7 |
| Defect/Condition_Evidence ID | No | Chỉ có scalar `Condition`; không có evidence/defect entity hoặc ID. `Evidence is currently insufficient.` |
| Inspection_Record ID | No | `Last_Check_Date` không phải record ID. `Evidence is currently insufficient.` |
| Action/repair/work-order ID | No | Work order chỉ là capability; không có instance/ID, PDF pp. 19, 24, 26 |
| Inspection-to-action relation | No | Không có inspection record hoặc action instance để tạo relation |
| Current status field | Yes | `Condition` được populate và map, PDF pp. 13-14, 22-25, Tables 2-3, 6-7, Fig. 5 |
| Timestamped Status_Event history | No | Chỉ current condition và latest check date; không có event sequence |
| Actor/time/reason | Partial | `Installation_Date`, `Last_Check_Date` có time semantics; không có actor/reason |
| Approval/rejection | No | Không có reviewer/approver/outcome. `Evidence is currently insufficient.` |
| Repair execution record | No | Không có executed work order hoặc maintenance completion record |
| Post-action verification | No | Không có reinspection, verifier hoặc before/after acceptance |
| Closure/reopen rule | No | Không có action closure hoặc reopen semantics |
| Provenance/audit history | Partial | Table 3 mô tả source/assignment logic và Algorithm 1 tạo log, PDF pp. 14-15; không có per-value source ID/actor/version |
| Executable constraints | Yes | IFC syntax/schema/normative/inverse/cardinality/type checks được chạy, PDF pp. 17, 20-21 |
| Deliberate invalid fixtures | No | Chỉ positive-path models/imports. `Evidence is currently insufficient.` |
| Predefined expected result | Partial | OIR/Pset mapping xác định target fields, nhưng không có negative oracle |
| Actual-versus-expected assertion | Partial | Table 6, PDF p. 22, so sánh sample source fields với CMMS mapping và ghi `Correctly mapped`; comparison là positive-path, sample-based, không công bố exact pairs hoặc automated assertion |
| Forward traceability | Yes | IFC entity/GlobalId/Pset -> JSON -> OpenMAINT card, PDF pp. 18-23, Tables 6-7 |
| Reverse traceability | Partial | CMMS card <-> BIM visual navigation bằng GUID, PDF pp. 24-26; không có reverse data transfer |
| Round-trip parity | No | §4.3 xác nhận luồng một chiều; không có IFC -> CMMS -> IFC reconstruction, PDF pp. 29-30 |

### 2.3 Nuyts et al. (2024)

#### Claim extraction

| Claim được chứng minh | Exact page/section | Implemented artifact | Validation | Limitation | Thesis implication |
|---|---|---|---|---|---|
| Năm requirement categories được áp dụng cho tám approaches | PDF p. 3, §§3.1-3.3, Table 1; p. 4, Fig. 2 | SMC, IDS, XSD, JSON Schema, OWL, SWRL, SPARQL, SHACL comparison | Coverage summarized in Fig. 8, p. 13 | Generic design compliance, không phải inspection-action chain | Constraint language/approach không phải novelty độc lập |
| Tác giả chủ động tạo compliant và non-compliant models, rồi raw/preprocessed variants | PDF p. 4, §3.4; OSF root cited at PDF p. 3 footnote 2 | Four variants cho IFC/RDF; `pass`/`fail` cho XML/JSON | Tám approaches dùng fixture variants phù hợp với format/approach | Một fail file gộp năm lỗi; không có mutation generator | Generic deliberate fixture use đã established |
| Năm fault categories có object/value cụ thể | PDF p. 3, Table 1; pp. 6-12, Listings 2-34; OSF root `5rwt6`, fail files `HS_fail.ifc`, `HS_fail.xml`, `HS_fail.json`, `HS_fail.ttl` | Missing width, width below 900, one railing, stair formula below range, ramp slope failure | Actual outputs lưu cho XSD/JSON/SPARQL/SHACL | Không one-mutation-per-file; không boundary/wrong-type/duplicate-ID cases | G2 cần isolated chain-specific mutation manifest |
| XSD, JSON Schema, SPARQL và SHACL có archived outputs | PDF p. 4, §4; OSF subprojects `3dxag`, `n4389`, `yznrx`, `j7raf`, inspected output files named `validation output.txt` or `*-output.json` | Validation reports/JSON bindings | XSD 6 messages, JSON 5, SPARQL 6 bindings, SHACL 5 violations | Không có normalized result codes hoặc exact expected set | G3 phải normalize outputs trước assertion |
| Không có automated expected-versus-actual assertion | PDF pp. 4-13, §4, Listings 2-36; OSF root/subproject wikis inspected 2026-08-04 | Manual run recipes và stored outputs | Người dùng được yêu cầu chạy/verify manually | Không có oracle manifest, CI, assertion code hoặc false-pass/fail metrics | Automated oracle remains defensible contribution |
| Requirement boundary semantics khác nhau giữa approaches | PDF pp. 7-13, Listings 8-9, 13, 23-24, 28-29, 34-36 | Different executable constraints | Các rules chạy | Không có fixtures ở 250, 500, 570, 630, 0.0625 | G2 phải khai báo inclusivity và boundary fixtures |
| SHACL-SPARQL có thể bị bỏ qua bởi validator thiếu feature support | PDF p. 11, §4.3.4 | Validator capability limitation | Potential silent false pass được tác giả cảnh báo | Không có engine-capability preflight test | G3 cần feature/version precondition và fail-closed behavior |

#### Component audit

| Thành phần | Yes / Partial / No | Exact evidence |
|---|---|---|
| Stable component/asset ID | Partial | IFC GlobalId/URIs được giữ trong derived formats, PDF p. 4, §3.4; không test uniqueness/version stability |
| BIM/IFC GlobalId mapping | Partial | Identity xuất hiện xuyên IFC/XML/JSON/RDF fixtures; không có identity acceptance test |
| Defect/Condition_Evidence ID | No | Design requirements, không có operational condition evidence |
| Inspection_Record ID | No | Không có inspection entity/ID |
| Action/repair/work-order ID | No | Không có action entity/ID |
| Inspection-to-action relation | No | Ngoài scope của bài |
| Current status field | No | Không có persisted workflow status |
| Timestamped Status_Event history | No | Không có event model |
| Actor/time/reason | No | Không có actor-bound event/time/reason |
| Approval/rejection | No | Human review chỉ được nêu, không có approval record, PDF p. 13 |
| Repair execution record | No | Không có repair execution |
| Post-action verification | No | Không có corrected/reinspection/acceptance fixture |
| Closure/reopen rule | No | Không có lifecycle closure |
| Provenance/audit history | Partial | OSF root `5rwt6` cited at PDF p. 14, Data availability, contains artifact metadata; dated snapshot has no run ID, engine version binding hoặc immutable result lineage |
| Executable constraints | Yes | Constraints được chạy cho five categories với coverage theo approach, PDF pp. 6-13, Listings 2-36 |
| Deliberate invalid fixtures | Yes | Fail datasets được tạo có chủ đích, PDF p. 4, §3.4 |
| Predefined expected result | Partial | Pass/fail names và fault labels ngụ ý category outcome; không có exact machine-readable focus-node/count/code oracle |
| Actual-versus-expected assertion | No | Không có automated runner/diff/CI. `Evidence is currently insufficient.` |
| Forward traceability | Partial | Requirement -> constraint -> validator output tồn tại; không có locked operational chain |
| Reverse traceability | No | Không có reverse operational query hoặc source reconstruction |
| Round-trip parity | No | Không có source-target-source transformation/equality test |

### 2.4 Hagedorn et al. (2023)

#### Claim extraction

| Claim được chứng minh | Exact page/section | Implemented artifact | Validation | Limitation | Thesis implication |
|---|---|---|---|---|---|
| ICDD chứa index metadata, payload documents/triples, ontology resources và linksets | PDF p. 5, §2.4, Figs. 3-4 | ISO 21597-style container and link model | Four underlying datasets represented by twelve containers, PDF pp. 9-10, Table 2 | Payload triples cần proxy để được tham chiếu như document | Evidence packaging có precedent, nhưng record-level provenance vẫn cần định nghĩa |
| Link model hỗ trợ binary/directed/direct/inverse predicates | PDF pp. 5-8, §§2.4-3.1, Figs. 4, 6, Listing 1 | SHACL-SPARQL inference | Direct/inverse triples được materialize | Derived relations không sửa canonical source/linkset | Reverse relation inference không phải reverse transformation |
| Inference rules encode ba identifier combinations | PDF pp. 7-8, §3.1, Listing 1 | Rule capability cho string-string, string-URI, URI-URI | Benchmark datasets demonstrate `StringBasedIdentifier` resolution, PDF p. 9, §3.2.1; Table 3 không validate cả ba combinations | Query-based identifiers và mixed/URI benchmark coverage không được đánh giá; không có uniqueness/stale-ID tests | G2 có thể dùng typed identifier-resolution tests nhưng phải thêm per-combination fixtures |
| Benchmark có four datasets x three link configurations | PDF pp. 9-10, §§3.2.1-3.2.2, Figs. 7-9, Tables 1-2 | Garage, Apartment, Duplex, Office; Binary, DirectedBinary, Directed1ToN | Inference and validation performance measured | Không phải inspection/action data | Generic link-validation benchmark đã established |
| R1-R3 chạy trên original và inferred graphs | PDF pp. 10-12, §3.2.3, Listings 2-3; pp. 18-21, Appendices A-B | SHACL Core/SPARQL rules | Actual violations and runtimes | Rules là construction task/schedule rules, không phải lifecycle authorization/closure |
| R1 phát hiện element không nối task; actual counts được báo cáo | PDF pp. 10-12, §3.2.3; p. 16, §4.2.4, Table 4 | Missing domain relation validation | R1 counts `0, 30, 39, 1`; R3 `0, 0, 7, 0` | Không có expected-count oracle hoặc deliberate mutation |
| Một số links không infer được vì IFC opening entities không tồn tại trong RDF | PDF p. 12, §4.1, Table 3 | Naturally unresolved source links | Missing inferred triples được quan sát | Không có dedicated broken-link violation/code hoặc fail-fast assertion | Paper 2 vẫn cần controlled orphan/broken-ID fixtures |
| Repository công bố containers, source IFC/XML, inferences, six shapes và JMH code | PDF p. 3, footnote 2; p. 17, Data availability; directly cited landing page `philhag.github.io/icdd-shacl-validation`; linked GitHub commit `b15113f213abdf03bbb4350d91c10ecd12d1f194`, paths `datasets/{1..4}/`, `rules/{1..3}/`, `sourcecode/` | Reproducibility artifacts | Benchmark có thể rerun | Không có `src/test`, oracle manifest hoặc committed validation reports tại commit đã kiểm tra | Artifact availability không đồng nghĩa expected-vs-actual test suite |

#### Component audit

| Thành phần | Yes / Partial / No | Exact evidence |
|---|---|---|
| Stable component/asset ID | Partial | IFC GUID qua `StringBasedIdentifier` và URI identity, PDF pp. 5-8; không có cross-version persistence |
| BIM/IFC GlobalId mapping | Partial | String identifier có thể map tới IFC property, PDF pp. 7-8, Listing 1; không có migration/collision test |
| Defect/Condition_Evidence ID | No | Dataset dùng component/task/schedule, không có condition evidence |
| Inspection_Record ID | No | Không có inspection record |
| Action/repair/work-order ID | No | Construction task không được dùng như maintenance Action_Record |
| Inspection-to-action relation | No | Ngoài scope của bài |
| Current status field | No | Không có action workflow status |
| Timestamped Status_Event history | No | Không có event sequence |
| Actor/time/reason | No | Task dates không phải actor-bound status event |
| Approval/rejection | No | Industry-partner review không phải persisted approval record, PDF p. 10, §3.2.3 |
| Repair execution record | No | Không có repair/intervention record |
| Post-action verification | No | Không có action verification |
| Closure/reopen rule | No | Không có closure/reopen semantics |
| Provenance/audit history | Partial | ICDD metadata/source packaging có provenance potential; không có record-event audit history |
| Executable constraints | Yes | SHACL Core/SPARQL inference/validation executed, PDF pp. 6-16 |
| Deliberate invalid fixtures | No | Actual violations và unresolved links không được tạo có chủ đích. `Evidence is currently insufficient.` |
| Predefined expected result | Partial | R1-R3 predefine required conditions ở PDF pp. 10-11, §3.2.3; không có fixture-specific expected focus-node/count manifest để đối chiếu Table 4 |
| Actual-versus-expected assertion | No | Repository không có assertion tests/golden reports |
| Forward traceability | Yes | Source IFC/XML -> RDF/ICDD identifiers -> links -> inferred predicates -> SHACL result |
| Reverse traceability | Yes | Direct/inverse predicates và validation paths hỗ trợ relation-level reverse navigation, PDF pp. 7-12, Listings 1-3 |
| Round-trip parity | No | Không có RDF/ICDD -> source reconstruction/write-back hoặc equality test, PDF pp. 16-17, §§4.3-5 |

## 3. Li et al. - operational record audit

| Audit target | Exact extraction | Evidence classification | Boundary decision |
|---|---|---|---|
| Database tables | Chỉ nêu `bridge defect database`, database of specifications và MySQL `ID attribute`, PDF pp. 2, 7-8 | Implemented statement, không có schema | Tên bảng, PK/FK, datatype và cardinality: `Evidence is currently insufficient.` |
| Inspection form structure | `Bridge Name`, `Date`, `Page`, `Pile number`, `Last date`, `No.`, `Structure`, `Component`, `Type`, `Scale`, `Location`, `Characteristic`, `Recorder`, `Reviewer`, PDF p. 11, Fig. 12 | Populated business form | Hỗ trợ candidate fields, không chứng minh database columns |
| Upload record | Structure/component/location/defect type/parameters/scale/evidence file, PDF p. 12, Fig. 13 | Populated UI | Thiếu Inspection ID, upload timestamp và reviewer binding |
| Defect ID | `<sequence>-<IFD code>`, ví dụ `1-68-10 10 10`, PDF p. 3 | Implemented statement with examples | Condition/defect identity present; stability policy absent |
| Component-defect linkage | Unnamed MySQL ID đặt defect OBJ ở corresponding bridge location, PDF p. 8 | Implemented visual link | Không có GlobalId hoặc declared mapping table |
| Inspection storage | Twice-weekly inspection form được upload để lập defect database, PDF p. 8, Figs. 12-13 | Operational workflow | Không có `Inspection_Record_ID` hoặc one-inspection-to-many-findings relation |
| Recommendation fields | Defect type, condition score, defect level, maintenance priority, PDF p. 7, Table 4; p. 15, Fig. 17 | Rule/UI records | Không có Action ID, rule version, created-by/time hoặc approval |
| Repair fields | Chỉ nêu repair records được lưu, PDF p. 7 | Textual implementation statement | Field list và populated record: `Evidence is currently insufficient.` |
| `completed` | Solved defect problems are marked `completed`, PDF p. 7 | Current scalar semantics | Không có event ID, timestamp, prior state, actor, reason hoặc guard |
| Actor/time/version | Form có Date, Last date, Recorder, Reviewer; actors trống, PDF p. 11 | Partial form evidence | Không có user ID, action actor, record version hoặc change reason |
| Verification/reopen | Không xuất hiện trong schema, UI, workflow hoặc result | No evidence | `Evidence is currently insufficient.` |

Kết luận Li:

1. `completed` là scalar/current marker theo text, không phải timestamped event.
2. Repair record có thể xem là operational history precedent nhưng chưa đủ bằng chứng để đồng nhất với formal `Action_Record`, vì không có identity, fields, actor/time, execution result hoặc populated instance.
3. Không có stable `Inspection_Record_ID -> Action_Record_ID` relation. Luồng inspection-to-recommendation/repair chỉ được chứng minh về chức năng.

## 4. Piras et al. - BIM-CMMS identity audit

### 4.1 IFC Pset và mapping

| Source field | Reported IFC datatype | Sample value | Source/assignment | OpenMAINT target | Exact evidence |
|---|---|---|---|---|---|
| `Condition` | `IfcLabel` | `Working`, `To Inspect`, `Out of Order` | Inspection/on-site verification | Operational state | PDF pp. 13-14, §2.3, Tables 2-3; p. 23, Table 7 |
| `Criticality` | `IfcInteger` | 1 Low, 2 Medium, 3 High | OIR/technical assessment | Priority index | Same |
| `Installation_Date` | `IfcDate` | `2017-03-15` | Installation documentation | Installation/maintenance log | Same |
| `Last_Check_Date` | `IfcDate` | `2025-01-12` | Latest inspection/maintenance | Inspection log | Same |
| `Maintenance_Frequency` | `IfcTimeMeasure` | `P12M` | Maintenance plan | Preventive interval | Same |
| `Manufacturer` | `IfcLabel` | `Vaillant S.p.A.` | Datasheet/manufacturer document | Supplier/brand | Same |
| `Model_ID` | `IfcIdentifier` | `BLDG01-AHU-003` | Naming/CMMS coding rules | Reference code | Same |
| `IfcGlobalId` | IFC rooted-object identifier, outside custom Pset | Populated per asset | Original IFC | CMMS unique asset identifier | PDF p. 18, §2.4.2; p. 23, Table 7 |

Internal inconsistencies requiring G2 guard:

- Table 2 names `ConstantElementProperties`; Figure 2, PDF p. 16 uses `CustomElementProperties`.
- Table 2 uses `IfcPropertySingleValue`, `Criticality` integer 1-3; Figure 2 uses enumerated values including `Extreme`.
- Figure 2 uses `Installation_date`/`Last_check_date`, while Table 2 uses capitalized `_Date`.
- Figure 5, PDF p. 25 shows `Broken`, while Table 2 defines `Out of Order`.

### 4.2 Identity, logs và lifecycle

| Audit question | Finding | Exact evidence |
|---|---|---|
| Asset-key ownership | `IfcGlobalId` originates in IFC/AIM and is reused as CMMS unique identifier; source-owned for initial import | PDF pp. 18, 22-24, §§2.4.2, 3.1.2-3.2.2 |
| `Model_ID` role | Human-readable/reference code; not demonstrated as PK | PDF pp. 13, 23, Tables 2, 7 |
| OpenMAINT internal ID | Not documented or crosswalked | `Evidence is currently insufficient.` |
| Validation outputs | 100% IFC schema compliance and correct mappings reported; no report artifact/ID | PDF pp. 17, 20-22, §§2.4.1, 3.1, Tables 5-6 |
| Processing logs | Element ID, assigned fields, processed count and anomalies are said to be logged | PDF p. 15, §2.3, Algorithm 1 |
| Import reconciliation | 428 assets from about 9000 elements; Fig. 5 shows 398 items without explanation | PDF pp. 20, 22, 24-25, Table 5, Fig. 5 |
| Work order | OpenMAINT can link work orders, but no populated record, ID, assignee, status or result | PDF pp. 19, 24, 26 |
| Update in IFC file | Existing Pset can be retrieved and edited during enrichment | PDF pp. 14-15, Algorithm 1 |
| CMMS write-back | Not implemented | PDF pp. 29-30, §4.3 |
| Replacement | Mentioned operationally; no old/new identity relation or transaction | PDF p. 30, §4.3 |
| Retirement | No entity, field or transition | `Evidence is currently insufficient.` |
| Identity across IFC revisions | Not tested | `Evidence is currently insufficient.` |

### 4.3 Four distinct interoperability levels

| Level | Result | Strict interpretation |
|---|---|---|
| Visual bidirectional lookup | Implemented, PDF pp. 24-26 | Two UI directions reuse GUID; no data mutation |
| Two-way data exchange | Not implemented, PDF pp. 29-30, §4.3 | No CMMS value export to IFC/AIM |
| Transactional synchronization | Not implemented, PDF p. 30 | No transaction ID, version check, conflict resolution, commit/rollback or retry |
| Source-target-source parity | Not implemented | No IFC -> CMMS -> reconstructed IFC execution or equality/semantic-equivalence assertion |

## 5. Nuyts et al. - fixture and oracle audit

### 5.1 Fixture manifest reconstructed from paper/artifacts

| Requirement | Deliberate fail | Fault granularity | Missing coverage | Exact evidence |
|---|---|---|---|---|
| Req01 availability | `doorA_fail01` missing `overallWidth` | One missing property | Null, duplicate, wrong datatype | PDF p. 3, Table 1; pp. 6-12, Listings |
| Req02 value | `doorB_fail02` width 850 below 900 | Below-minimum value | Boundary 900, units, above range | Same |
| Req03 relational | `stairA_fail03-04-06` has one railing | Cardinality; shared object with Req04 | Zero/three, same-side, duplicate URI, wrong relation type | Same |
| Req04 mathematical | `2 x 177.7778 + 200 = 555.5556`, below 570 | Below-range formula | Exactly 570/630, above 630 | Same |
| Req05 conditional | Height 420 and slope 0.072433 above 0.0625 | Conditional violation | 250/500 boundaries, missing antecedent/consequent | Same |

Một `fail` file gộp năm faults trên bốn objects; đây không phải one-mutation-per-file suite. RDF được dịch thủ công từ IFC; XML/JSON được tạo từ RDF; không có mutation generator (PDF p. 4, §3.4).

### 5.2 Validator output and oracle

| Approach | Constraint coverage | Actual output retained | Expected oracle | Automated assertion | Exact evidence |
|---|---|---|---|---|---|
| SMC | Five categories | Screenshots only | Dataset/category implication | No | PDF pp. 4-6, §4.1.1, Figs. 3-7; no SMC subproject in dated OSF snapshot `5rwt6` |
| IDS | Req01-Req03 | No archived report | Pass/fail naming and prose | No | PDF pp. 5-6, §4.1.2, Listing 4; OSF `jkh2z`, `ids.xml` and manual wiki |
| XSD | Five categories | Six messages | Category-level only | No | PDF pp. 6-7, §4.2.1, Listings 5-9; OSF `3dxag`, `validation output.txt` |
| JSON Schema | Four; mathematical unsupported | Five errors | Category-level only | No | PDF pp. 7-8, §4.2.2, Listings 10-13; OSF `n4389`, `validation output.txt` |
| OWL | Mathematical unsupported; missing failures need query complement | No separate report | Partial labels | No | PDF pp. 8-9, §4.3.1, Listings 14-19; OSF `vzw65`, `OWL.ttl` and manual wiki |
| SWRL | Five with SPARQL complement | No clean separate report | Partial labels | No | PDF pp. 9-10, §4.3.2, Listings 20-24; OSF `f4j8t`, `SWRL.ttl` and manual wiki |
| SPARQL | Five queries | Six bindings; Req02 returns two doors | Expected category implied, no exact set | No | PDF pp. 10-11, §4.3.3, Listings 25-29; OSF `yznrx`, five `*-output.json` files |
| SHACL | Five | `Conforms: False`, five results | Expected five categories implied | No | PDF pp. 11-13, §4.3.4, Listings 30-36; OSF `j7raf`, `validation output.txt` |

Audit conclusion:

- **Established:** deliberate paired compliant/non-compliant construction datasets; four IFC/RDF variants and two XML/JSON fixtures; execution across multiple validators; stored actual outputs for four approaches.
- **Not established:** machine-readable `{fixture, mutation, rule, expected focus node, expected code, expected count}` manifest; isolated mutations; positive-output archive; automated exact-set assertion; boundary/unit parity; false-pass/false-fail metrics.
- **Paper 2 cannot claim:** novelty for using deliberate valid/invalid fixtures, SHACL/SPARQL execution, hoặc manual comparison of validator outputs.
- **Open chain-specific contribution:** duplicate/reused record IDs, orphan/wrong-type links, missing evidence basis, illegal transitions, unauthorized approval, stale BIM mapping, closure without verification, and exact automated expected-versus-actual assertions.

## 6. Hagedorn et al. - link-integrity audit

### 6.1 Identifier, container and link model

| Audit target | Implemented evidence | Boundary |
|---|---|---|
| Container | Index metadata, ontology resources, payload documents/triples, linksets, PDF p. 5, §2.4, Figs. 3-4 | Payload triples need proxy for document reference |
| Identifier types | String-, URI-, query-based identifiers, PDF p. 5, Fig. 4 | Query-based identifier excluded from evaluation |
| Link types | Binary, DirectedBinary, Directed1ToN and generic variants, PDF p. 5, Fig. 4 | Benchmark uses three configurations |
| Direct relation | Materialized predicate between resolved RDF entities, PDF pp. 6-8, §3.1, Listing 1 | Derived graph only |
| Inverse relation | Symmetric second edge for binary; named inverse for directed links, PDF pp. 7-8, Listing 1 | Not a reverse transformation |
| Missing relation | R1 checks element has task, PDF pp. 10-12, Listings 2-3 | Domain relation, not universal link referential integrity |
| Unresolved source link | Some IFC opening entities absent in RDF, so no inferred triple, PDF p. 12, §4.1, Table 3 | No dedicated broken-link violation |

### 6.2 Benchmark and output

| Evidence | Exact result | Interpretation |
|---|---|---|
| Dataset design | Four datasets x three link configurations, PDF pp. 9-10, Tables 1-2 | Reproducible link benchmark, not deliberate invalid suite |
| Inference output | Per link type: 18, 126, 336, 1622 triples, PDF p. 12, Table 3 | Actual derived-edge count; not expected oracle |
| Validation output | R1 counts `0, 30, 39, 1`; R2 all 0; R3 `0, 0, 7, 0`, PDF p. 16, Table 4 | Aggregate actual counts only |
| Violation structure | SHACL result has message/focus node, PDF p. 4, Fig. 1; Listings 2-3 | Repository lacks committed full reports |
| Repository | Containers, source IFC/XML, inference TTL, six shapes, JMH code, PDF p. 3 footnote 2; p. 17 Data availability; directly cited landing page plus linked GitHub commit `b15113f213abdf03bbb4350d91c10ecd12d1f194`, paths `datasets/{1..4}/`, `rules/{1..3}/`, `sourcecode/` | No `src/test`, oracle manifest or golden report at inspected commit |

### 6.3 Four distinct reverse capabilities

| Capability | Verdict | Exact boundary |
|---|---|---|
| Inverse relation inference | Yes | Direct/inverse predicates materialized, PDF pp. 7-8, Listing 1 |
| Reverse query/navigation | Yes, relation-level only | Validation paths use direct/inverse predicates, PDF pp. 10-12, Listings 2-3; appendices |
| Reverse transformation | No | No RDF/inferred graph -> IFC/XML/linkset transformation |
| Round-trip parity | No | No source -> target -> reconstructed source, equality, semantic-equivalence or loss assertion |

Broken-link/oracle conclusion:

- R1 validates a missing element-to-task relation, but the paper does not publish intentionally deleted/corrupted link fixtures.
- Naturally unresolved IFC openings do not become explicit violations.
- Table 4 reports actual counts but not expected counts.
- Direct/inverse relation navigation is established; controlled referential-integrity mutation, reverse reconstruction and parity are not.

## 7. Cross-paper competitor matrix

| Study | Main artifact | Identity | Inspection/action | Status/event | Accountability | Fixtures/oracle | Direct/reverse | Main remaining gap |
|---|---|---|---|---|---|---|---|---|
| Li et al. (2023) | Web BMS, defect database, BIM3D defect library | Defect ID yes; component key partial; no GlobalId contract | Implemented inspection/defect capture, scoring and recommendations; repair-record storage and `completed` are uninstantiated textual claims | `completed` scalar only | Recorder/reviewer form fields unpopulated | No deliberate fixtures/assertions | Forward functional flow only | Formal Action_Record, event history, verification, reopen, provenance |
| Piras et al. (2026) | IFC enrichment plus OpenMAINT import | `IfcGlobalId` preserved for 428 initial-import assets | Latest condition/check fields; work order only capability | No action status/event history | No actor/approval | Positive IFC validation only | Forward transfer yes; reverse visual lookup partial | Write-back, replacement identity, actions, events, verification, parity |
| Nuyts et al. (2024) | Multi-approach ACC fixture comparison | Component IDs across formats partial | None | None | Human review conceptual | Deliberate fixtures yes; exact oracle/assertion no | Requirement-to-output forward only | Chain-specific mutations, exact oracle, false-pass/fail evaluation |
| Hagedorn et al. (2023) | ICDD link inference and SHACL validation benchmark | Typed string/URI resolution partial | Construction task relations, not inspection/action records | None | Industry review only | No deliberate invalid fixtures/oracle | Direct/inverse relation navigation yes | Broken-link fixtures, reverse transform, parity, operational chain |

## 8. Novelty stress test

### 8.1 Stable `Inspection_Record`-`Action_Record` relation

**Claim ->** Paper 2 needs an explicit, stable relation rather than a functional handoff.  
**Prior art achieved ->** Li implements inspection/defect capture, recommendations, repair-history statement and `completed`; Piras maps latest check/condition into CMMS but no action instance (Li PDF pp. 7-12; Piras PDF pp. 18-26).  
**Remaining gap ->** Trong phạm vi bốn bài Round 3A, không có `Inspection_Record_ID`, `Action_Record_ID`, FK/cardinality, evidence basis hoặc inverse query được công bố.  
**Required thesis validation ->** Populated one-to-one, one-to-many and aggregation cases; orphan/wrong-type/missing-basis fixtures; exact forward/reverse expected answers.  
**Verdict: Narrowed.**

### 8.2 Immutable/queryable `Status_Event` history

**Claim ->** Current scalar status must be separated from events.  
**Prior art achieved ->** Li has `completed`; Piras has current `Condition` and latest check date (Li PDF p. 7; Piras PDF pp. 13, 23-25).  
**Remaining gap ->** Trong phạm vi bốn bài Round 3A, không có event ID, prior/new state, actor, timestamp, reason, sequence hoặc event-history query.  
**Required thesis validation ->** Append-only event fixtures, allowed/illegal transitions, one-current-state projection, history reconstruction and supersession tests.  
**Verdict: Still strong.**

### 8.3 Evidence-basis preservation

**Claim ->** Every inspection/action/review/closure decision must retain its evidence basis.  
**Prior art achieved ->** Li captures form/photo context; Piras documents source categories; Hagedorn packages source documents/triples/links in ICDD (Li PDF pp. 11-12; Piras p. 14, Table 3; Hagedorn p. 5, Figs. 3-4).  
**Remaining gap ->** Trong phạm vi bốn bài Round 3A, không có complete source-record ID, version/hash, interpretation, action rationale và closure-evidence chain.  
**Required thesis validation ->** Forward/reverse queries from evidence to closure and closure to exact evidence/version; missing/stale evidence fixtures.  
**Verdict: Narrowed.**

### 8.4 Accountable authorization

**Claim ->** Review/approval requires identified actor, role, time, rationale and permission.  
**Prior art achieved ->** Li form includes Recorder/Reviewer but leaves them blank; other three papers do not implement operational approval (Li PDF p. 11, Fig. 12).  
**Remaining gap ->** Trong phạm vi bốn bài Round 3A, không có authenticated role matrix, approve/reject event, separation of duties, override hoặc audit query.  
**Required thesis validation ->** Authorized and unauthorized fixtures, self-approval rule, missing rationale, rejection/rework and override logging.  
**Verdict: Still strong.**

### 8.5 Formal post-action verification

**Claim ->** Completion must depend on a linked verification record.  
**Prior art achieved ->** Li states repair records and `completed`; Piras has no executed work order (Li PDF p. 7; Piras pp. 24-26).  
**Remaining gap ->** Trong phạm vi bốn bài Round 3A, không có verifier, criteria, before/after evidence, acceptance/rejection, rework hoặc linkage to action.  
**Required thesis validation ->** Populated pass/fail verification cases and closure blocked when verification is absent/failed.  
**Verdict: Still strong.**

### 8.6 Guarded closure/reopen

**Claim ->** Closure and reopening must be controlled events.  
**Prior art achieved ->** `completed` supplies minimal closure-like semantics only (Li PDF p. 7).  
**Remaining gap ->** Trong phạm vi bốn bài Round 3A, không có closure preconditions, closer/time/reason, failed-verification guard, reopen trigger hoặc old/new event link.  
**Required thesis validation ->** Valid closure, premature closure, closure after rejection, reopen after new finding, and immutable history assertions.  
**Verdict: Still strong.**

### 8.7 Chain-specific controlled mutations

**Claim ->** Paper 2 must not claim novelty for deliberate fixtures generally.  
**Prior art achieved ->** Nuyts implements deliberate compliant/non-compliant fixtures over five categories (PDF pp. 3-4, §§3.1-3.4).  
**Remaining gap ->** Trong phạm vi bốn bài Round 3A, không có chain-specific duplicate/reused IDs, orphan/wrong-type relation, missing basis, illegal transition, unauthorized approval hoặc closure-without-verification suite.  
**Required thesis validation ->** Isolated mutation manifest with stable violation code, expected focus ID/count and automated actual comparison.  
**Verdict: Narrowed.**

### 8.8 Paired forward/reverse acceptance tests

**Claim ->** Reverse lookup alone is insufficient.  
**Prior art achieved ->** Hagedorn materializes and queries direct/inverse relations; Piras performs two-direction visual lookup (Hagedorn PDF pp. 7-12; Piras pp. 24-26).  
**Remaining gap ->** Trong phạm vi bốn bài Round 3A, không có full operational forward/reverse answer contract, reverse transformation hoặc source-target-source reconstruction.  
**Required thesis validation ->** Paired CQs with exact sets in both directions, plus equality/semantic-equivalence and permitted-loss policy.  
**Verdict: Narrowed.**

### 8.9 Complete integrated chain

**Claim ->** Contribution unit is the integrated identity/event/verification contract.  
**Prior art achieved ->** Li covers implemented defect capture/scoring/recommendations plus an uninstantiated repair-history statement; Piras covers IFC-CMMS identity import; Nuyts covers deliberate fixtures; Hagedorn covers direct/inverse link validation.  
**Remaining gap ->** Trong phạm vi bốn bài Round 3A, không bài nào combines stable evidence, component, inspection, action, immutable event, accountable review và verified closure với exact mutation/oracle và parity tests.  
**Required thesis validation ->** One populated end-to-end valid chain, controlled invalid chain families, accountable decisions, closure guard and forward/reverse acceptance execution.  
**Verdict: Still strong.**

## 9. G2 specification impact

| G2 decision | Evidence from Round 3A | Decision status | Required change |
|---|---|---|---|
| Component identity | Piras preserves `IfcGlobalId`; Li component code is unstable/unnamed | LOCK_PROVISIONALLY | Keep generic external identifier `{Identifier_Scheme, Identifier_Value, Model_Version_Context}` plus internal `Component_ID`; treat `IfcGlobalId` as the literature-supported IFC profile, not a mandatory technology; add duplicate/stale/replacement tests |
| Record IDs separate from component ID | Li defect ID exists; no inspection/action ID in four papers | LOCK | Require distinct stable IDs for evidence, inspection, finding, action, event and verification |
| Inspection-Action cardinality | Functional linkage exists but no published keys/cardinality | WAIT_FOR_MORE_EVIDENCE | Do not freeze 1:1; test multiple findings/actions and aggregation before decision |
| `Action_Record` fields | Li repair fields absent; Piras work order is capability only | WAIT_FOR_MORE_EVIDENCE | Round 3B/expert review must distinguish recommendation, work order, execution and history |
| `Workflow_Status` | Li `completed` and Piras `Condition` are current scalars | REVISE | Rename/separate asset condition, action current-state projection and event history |
| `Status_Event` entity | No paper implements it; scalar/event confusion is demonstrated | LOCK_PROVISIONALLY | Keep separate append-only entity; exact vocabulary/transitions await expert review |
| Defect severity vs Action_Level | Li maps defect/condition to recommendation priority but does not equate them | REMOVE | Remove any rule that automatically treats defect severity as Action_Level |
| Role/permission matrix | Only blank Recorder/Reviewer form fields in Li | WAIT_FOR_MORE_EVIDENCE | Read Celik in Round 3B and obtain domain expert decision on roles/separation of duties |
| `Verification_Record` | No post-action verification in four papers | LOCK_PROVISIONALLY | Keep separate entity required for closure; exact fields/criteria need expert review |
| Closure/reopen rules | Li only has `completed` scalar | LOCK_PROVISIONALLY | Define closure guard, rejection/rework and reopen semantics; do not freeze transition names yet |
| Provenance fields | Li form/photo, Piras source table/log, Hagedorn container metadata | LOCK_PROVISIONALLY | Require source reference, version/hash, actor/time and derivation; exact payload binding awaits G1 |
| Constraint families | Piras validates IFC; Nuyts/Hagedorn execute generic constraints | LOCK | Keep uniqueness, requiredness, datatype, cardinality, typed reference, chronology, transition, authorization and closure families technology-neutral |
| Fixture/oracle design | Nuyts establishes fixtures but lacks exact automated oracle | LOCK | Require isolated mutations, expected focus IDs/codes/counts and automated actual-vs-expected comparison |
| Paired query and round-trip definitions | Hagedorn inverse navigation and Piras reverse visual lookup stop before parity | LOCK_PROVISIONALLY | Define paired forward/reverse query acceptance separately from transformation round-trip; specify equality, semantic equivalence and permitted loss only for the latter |

## 10. Candidate entity model

Đây là candidate conceptual model, không phải implementation schema.

| Entity | Candidate field/relation | Evidence label | Round 3A basis |
|---|---|---|---|
| `Component` | `Component_ID` | THESIS_DEFINED | Piras proves external `IfcGlobalId`; Li shows component-code instability, requiring governed internal identity |
| `Component` | `External_Identifier_Scheme`, `External_Identifier_Value` | MULTI_SOURCE_INFERRED | Piras implements IFC GlobalId mapping; Hagedorn implements typed string/URI identifier resolution |
| `Component` | `IFC_GlobalId` as an IFC profile | LITERATURE_SUPPORTED | Piras PDF pp. 18, 23, Table 7; not a mandatory implementation choice |
| `Component` | `Human_Readable_Code` / `Model_ID` | LITERATURE_SUPPORTED | Li site code, PDF p. 12; Piras `Model_ID`, p. 13, Table 2 |
| `Component` | `Model_Version_Context` | MULTI_SOURCE_INFERRED | Piras lacks revision persistence; Hagedorn identifiers depend on source representations |
| `Component` | `Current_Condition` | LITERATURE_SUPPORTED | Piras `Condition`, PDF pp. 13, 23-25; this is asset state, not action history |
| `Condition_Evidence` | `Condition_Evidence_ID` | THESIS_DEFINED | Li supports defect-occurrence identity at PDF p. 3, but not a separate evidence-record identity |
| `Condition_Evidence` | `Source_Reference` | LITERATURE_SUPPORTED | Li photo/form, pp. 11-12; Hagedorn payload document model, p. 5 |
| `Condition_Evidence` | `Observed_Value`, `Unit`, `Location`, `Observed_At` | LITERATURE_SUPPORTED | Li scale/location/characteristic/date, PDF p. 11, Fig. 12 |
| `Condition_Evidence` | `Source_Version_or_Hash` | THESIS_DEFINED | Four papers do not implement per-evidence immutable version binding |
| `Inspection_Record` | `Inspection_Record_ID` | THESIS_DEFINED | No explicit ID in four papers; required to stabilize Li's inspection form |
| `Inspection_Record` | `Inspection_Date`, `Previous_Inspection_Date`, `Scope` | LITERATURE_SUPPORTED | Li PDF p. 11, Fig. 12 |
| `Inspection_Record` | `Inspector_Agent_ID` | MULTI_SOURCE_INFERRED | Li has unpopulated Recorder; actor binding is required but not implemented |
| `Inspection_Record` | `Finding_IDs` | THESIS_DEFINED | Relation implied by Li workflow; exact cardinality insufficient |
| `Finding` | `Finding_ID` | THESIS_DEFINED | Li defect ID could identify evidence/defect, but finding/evidence separation is not established |
| `Finding` | `Defect_Type`, `Scale`, `Location`, `Assessment` | LITERATURE_SUPPORTED | Li PDF pp. 11-12, Figs. 12-13 |
| `Finding` | `Based_On_Evidence_ID` | MULTI_SOURCE_INFERRED | Li connects form/photo/defect; Hagedorn demonstrates explicit typed links |
| `Action_Record` | `Action_Record_ID` | THESIS_DEFINED | No formal Action ID in four papers |
| `Action_Record` | `Action_Type`, `Recommendation`, `Priority` | MULTI_SOURCE_INFERRED | Li supports recommendation/priority semantics at PDF pp. 7, 15, but not a formal Action_Record |
| `Action_Record` | `Based_On_Finding_or_Inspection` | MULTI_SOURCE_INFERRED | Li functional chain; no stable relation/cardinality |
| `Action_Record` | `Assignee`, `Planned_At`, `Executed_At`, `Execution_Result` | EVIDENCE_INSUFFICIENT | Piras work-order capability and Li repair statement do not expose fields |
| `Action_Record` | `Current_Status` as derived projection | THESIS_DEFINED | Required to separate current action state from history; it may only be derived from the latest valid `Status_Event` |
| `Status_Event` | `Status_Event_ID` | THESIS_DEFINED | Required to avoid treating Li `completed` or Piras `Condition` as history |
| `Status_Event` | `Previous_Status`, `New_Status`, `Occurred_At`, `Actor_ID`, `Reason` | THESIS_DEFINED | No paper implements this tuple; it is required by the locked accountability question |
| `Status_Event` | `For_Action_ID` | THESIS_DEFINED | No explicit relation in four papers |
| `Agent` | `Agent_ID`, `Role` | MULTI_SOURCE_INFERRED | Li Recorder/Reviewer roles; implementation evidence insufficient |
| `Agent` | `Authorization_Context` | THESIS_DEFINED | No permission model in Round 3A |
| `Verification_Record` | `Verification_Record_ID` | THESIS_DEFINED | No formal verification in four papers; required for guarded closure |
| `Verification_Record` | `For_Action_ID`, `Verifier_ID`, `Criteria`, `Before_Evidence`, `After_Evidence`, `Outcome`, `Verified_At` | THESIS_DEFINED | Post-action fields are absent; exact field set requires expert review |
| `Verification_Record` | Closure permission relation | THESIS_DEFINED | Needed to make closure guard executable; not literature-established in Round 3A |

## 11. Paper 2 boundary

### Updated central claim

> Trong phạm vi bốn tài liệu Round 3A đã deep-read, Paper 2 will propose and, subject to accepted G2 decisions, evaluate an implementation-neutral, identity-governed evidence-to-action specification that separates current state from immutable events; links condition evidence, an externally identified component, inspection and action records, actor-bound review events and verification records; and will test the chain through predeclared integrity mutations, exact expected outcomes, paired forward/reverse queries and guarded closure.

### Contribution statements

1. Trong phạm vi bốn tài liệu Round 3A đã deep-read, candidate contribution 1 là một record-event contract tách component identity, evidence identity, inspection identity, action identity, current-state projection và immutable status events; claim này contingent on retained and reviewed G3 outputs.
2. Trong phạm vi bốn tài liệu Round 3A đã deep-read, candidate contribution 2 là accountable closure contract nối action với actor-authorized review events, verification evidence, acceptance/rework và reopen semantics; claim này contingent on retained and reviewed G3 outputs.
3. Trong phạm vi bốn tài liệu Round 3A đã deep-read, candidate contribution 3 là chain-specific validation contract gồm isolated mutations, stable violation codes, machine-readable expected results, automated actual-versus-expected assertions và paired forward/reverse acceptance queries; claim này contingent on retained and reviewed G3 outputs.

### Claims phải loại bỏ

- Novel BIM-linked defect database hoặc maintenance recommendation.
- Novel use of `IfcGlobalId` for BIM-CMMS asset linkage.
- Novel IFC-to-CMMS import hoặc visual lookup hai chiều.
- Novel use of SHACL/SPARQL/executable constraints.
- Novel use of compliant/non-compliant fixtures nói chung.
- Novel direct/inverse link navigation.
- Closed-loop maintenance nếu chỉ có `completed` hoặc current condition.
- Round-trip parity nếu chỉ có reverse lookup hoặc inverse predicate.
- Accountable workflow nếu chỉ có role labels/blank form fields.

### Claims chỉ dùng sau G3 validation

- The specification is executable and internally consistent.
- Every valid chain is retrievable in both directions with exact expected answers.
- Invalid identity/relation/workflow/authorization/closure cases are rejected with correct violation codes.
- Current-state projection equals the latest valid event after normalization.
- Closure is impossible without accepted verification and authorized actor.
- Round-trip equality hoặc semantic equivalence đạt theo declared policy.

## 12. Decision checkpoint

1. **Round 3A có đủ để khóa G2 v0.1 không?** Đủ để khóa structural boundary và validation principles; không đủ để freeze exact Action fields, Inspection-Action cardinality, status vocabulary, role permissions, verification criteria hoặc replacement/retirement semantics.
2. **Có cần đọc Mohamed et al. và Celik et al. trong Round 3B không?** Có. Mohamed cần để kiểm tra inspection/maintenance history và repaired/unrepaired field model; Celik cần để kiểm tra implemented transaction provenance, actor/responsibility và audit history. Không dùng hai bài này để hỗ trợ kết luận Round 3A hiện tại.
3. **Thành phần đủ evidence để freeze:** entity separation; distinct record IDs; generic external component identifier với `IfcGlobalId` là literature-supported IFC profile, không phải record ID hoặc mandatory technology; current scalar khác event history; technology-neutral constraint families; isolated fixture plus exact oracle requirement; reverse lookup khác parity.
4. **Thành phần cần expert review:** inspection-action cardinality; recommendation/work-order/execution boundaries; role/permission matrix; allowed transitions; separation of duties; verification criteria; closure/reopen policy.
5. **Thành phần phải chờ payload G1:** exact `Condition_Evidence` source fields, payload IDs, acquisition/processing version, quality/confidence context, component-binding method, permitted loss và stale-mapping behavior.
6. **G3 có thể mở ở mức prototype chưa?** Có thể mở một bounded prototype sau khi G2 ghi rõ các provisional decisions và unresolved items. Prototype chỉ được dùng để test feasibility; không được mô tả là accepted specification, validated chain hoặc G3 PASS.

## 13. Next actions

1. Freeze G2 structural boundary: eight candidate entities, identity separation và scalar-versus-event rule.
2. Tạo G2 decision register, ghi rõ `LOCK`, `LOCK_PROVISIONALLY`, `REVISE`, `WAIT_FOR_MORE_EVIDENCE`, `REMOVE`, và owner cho từng unresolved decision.
3. Thực hiện Round 3B đúng hai bài Mohamed và Celik, với extraction questions giới hạn ở history/status, actor, authorization, responsibility và audit.
4. Tổ chức expert review cho Inspection-Action cardinality, action lifecycle, role permissions, verification và closure/reopen.
5. Nhận payload G1 và khóa minimum `Condition_Evidence` context, source/version binding và component mapping contract.
6. Soạn technology-neutral fixture/oracle manifest gồm valid baseline, isolated mutations, expected focus IDs, violation codes và counts.
7. Soạn paired forward/reverse CQ contract và tách query-answer parity khỏi transformation round-trip parity.
8. Chỉ sau các bước trên mới mở bounded G3 prototype; giữ mọi PASS/validated claim ở trạng thái cấm cho tới khi test outputs được retained và reviewed.

**AI-assisted research disclosure:** ZoteroMCP và AI-assisted extraction được dùng để truy xuất, chia trang, đối chiếu full text và kiểm tra author-linked supplementary artifacts. Detailed paper claims được giới hạn bởi page/section/table/figure/listing; supplementary claims được giới hạn bởi URL/project/path và dated OSF snapshot hoặc Git commit nêu trong báo cáo. Không có Zotero writeback.
