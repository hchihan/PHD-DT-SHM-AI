# G2-G3 Round 2 Inspection-Action Model Deep Read

Corpus khóa cứng: đúng bốn Zotero items trong collection `RQ2_RQ3_CORE_DEEP_READ_20260803` (`C9J2V33M`). Không sử dụng nguồn ngoài bốn items và không thực hiện Zotero writeback.

Quy ước:

- `PDF p.` là số trang của file PDF được đọc.
- `Yes` chỉ dùng khi bài mô tả hoặc triển khai rõ; workflow UI không tự động được coi là formal information model.
- Xu et al. (2022) không có child attachment; Zotero full-text endpoint trả `No suitable attachment found`. Abstract không được dùng để hỗ trợ detailed claims. **Evidence is currently insufficient.**
- Mọi diễn giải về novelty được giới hạn bằng: **Trong phạm vi bốn tài liệu đã deep-read...**
- Các model đề xuất dưới đây là candidate specifications, không phải kết quả đã được kiểm chứng và không đồng nghĩa G2/G3 đã đạt.

## 1. Executive summary

- **Formal inspection specification mạnh nhất:** Sacks et al. (2018), với BPMN/IDM, information exchanges, IFC4 Add2 MVD/mvdXML, defect entities, mandatory/optional/value constraints, QC loop và inspection signing (PDF pp. 3, 6-18, §§2, 4-6, Figs. 2, 5-10).
- **Defect/action representation mạnh nhất:** Isailović et al. (2020) là bằng chứng toàn văn mạnh nhất cho defect finding schema: `IfcTask -> IfcElementAssembly(INSPECTIONFINDING) -> IfcSurfaceFeature(DAMAGE) -> IfcElement`, cùng type, location, extent-by-geometry, severity và inspection time (PDF pp. 6-9, 19, §§3.2.2.1-3.2.2.3, Figs. 7-9, 24-25). Wan et al. (2019) là bằng chứng toàn văn mạnh nhất cho action categories/repair-plan representation qua `Pset-reinforcetype`, repair solutions và model-linked repair records (PDF pp. 4, 14-15, Tables 1, 3, Figs. 15-16). Xu et al. có scope rất gần theo metadata/abstract nhưng detailed evidence không khả dụng.
- **Operational workflow mạnh nhất:** Wan et al. (2019): manager creates inspection project -> inspector captures component-linked defect evidence -> manager checks data -> system displays condition/alerts -> repair project/plan -> repair -> manager checks result and qualified/not-qualified outcome (PDF pp. 13-15, §5.2.2-5.3, Figs. 12-16). Đây là UI/process evidence, không phải persisted state/event schema.
- **Condition_Evidence context mạnh nhất:** Isailović et al. (2020) có inspection date/type, finding description/geometry, BMS catalog code/type, host-relative location, geometry-based extent, severity scale và explicit IFC relations (PDF pp. 6-9, 19, §§3.2.2.1-3.2.2.3, Figs. 7-9, 24-25). Per-finding source provenance, confidence, processing version và reviewer identity vẫn không được encoded.
- **Khoảng trống còn lại:** explicit and queryable `Inspection_Record -> Action_Record -> Status_Event` linkage; stable IDs; evidence basis; actor/time/reason for each transition; accountable approval; post-action verification record; và workflow integrity tests.
- **Xu limitation:** chi tiết geometry, maintenance-action relations, scenario validation và interoperability chỉ xuất hiện trong abstract metadata; chúng không được dùng để phân loại field hoặc workflow step. **Evidence is currently insufficient.**

## 2. Evidence extraction theo từng bài

### 2.1 Sacks et al. (2018), SeeBridge

**Citation:** Sacks, R., Kedar, A., Borrmann, A., Ma, L., Brilakis, I., Hüthwohl, P., Daum, S., Kattel, U., Yosef, R., Liebich, T., Barutcu, B. E., & Muhic, S. (2018). SeeBridge as next generation bridge inspection: Overview, information delivery manual and model view definition. *Automation in Construction, 90*, 134-145. https://doi.org/10.1016/j.autcon.2018.02.033  
**Zotero key:** `F8RMUZ44`

| Claim được chứng minh | Exact page/section | Implementation/validation | Limitation | Thesis implication |
|---|---|---|---|---|
| IDM tách process/information requirements khỏi IFC-bound MVD/mvdXML implementation | PDF p. 3, §2; PDF pp. 12-14, §§5-5.2, Fig. 5 | BPMN/IDM, ifcDoc, BIM*Q, mvdXML; expert workshops và XBIM checks ở PDF p. 18, §6 | Chỉ một phần repositories/MVD được trình bày; semantic enrichment details ngoài scope (PDF p. 7, §4) | Thesis phải tách normative process, information schema, implementation và validation evidence |
| Inspection pipeline đi từ assignment/acquisition tới defect capture, QC/signing và rehab/maintenance planning | PDF p. 6, Fig. 2; PDF pp. 7-10, §§4.1-4.4, Fig. 3 | Implemented exchange models `EM-2`, `EM-3A/B`, `EM-4`; four IFC models checked, PDF p. 18, §6 | Maintenance branch chỉ dừng ở alternatives/working plan; repair execution và operational outcome không được validated | Không suy maintenance completion từ inspection process map; cần Action_Record và Status_Event riêng |
| Finding được biểu diễn bằng located `ElementDefect`, grouped thành `Defect` | PDF pp. 15-17, §5.3, Fig. 8, Table 6 | `Defect -> IfcElementAssembly`; `ElementDefect -> IfcSurfaceFeature`; `IfcRelAggregates`; embedded in `EM-4` | Không có named Inspection_Record ID, author, action record hoặc lifecycle state | Giữ occurrence identity tách khỏi defect grouping và inspection identity |
| Evidence kết hợp geometry/measurements với registered high-resolution imagery | PDF p. 10, §4.4; PDF pp. 16-18, §5.3, Table 6, Fig. 9 | `IfcImageTexture`, BREP, SeeBridge viewer | Không có source-file ID/hash, device, acquisition time, confidence hay registration-error field; occluded components có thể bị bỏ (PDF p. 9, §4.2) | Evidence source/context phải là linked record, không chỉ texture/geometry |
| Validation xác lập requirements/MVD conformance, không xác lập operational repair effectiveness | PDF p. 18, §6; PDF pp. 19-20, §7 và Conclusion | Five bridge engineers, three workshops, four IFC bridge models, XBIM syntax/semantic/content checks | Không có quantitative workflow outcome, action completion, post-repair check hoặc strict negative fixture suite | G3 phải tách conformance, workflow integrity, action traceability và verification tests |

| Thành phần | Yes / Partial / No | Exact evidence |
|---|---|---|
| BIM component identity | Yes | IFC mappings và component classifications, PDF pp. 14-15, Figs. 6-7; four bridge IFC models checked, PDF p. 18, §6 |
| Condition/defect evidence | Yes | `Condition`, `Defect`, `ElementDefect`, geometry và defect properties, PDF pp. 15-17, Fig. 8, Table 6 |
| Evidence source/context | Partial | Point cloud/video/photogrammetry và registered imagery, PDF pp. 7, 10, 17, §§4.1, 4.4, 5.3; không có per-evidence provenance fields |
| Inspection_Record | Partial | Assignment, inspection, signing và time-specific `ElementDefect`, PDF p. 6 Fig. 2; pp. 15-16 §5.3; không có named record entity/ID |
| Inspector/author identity | No | `Bridge Inspector` role và inspector library ở PDF p. 6, Fig. 2; schema ở Figs. 6-8 không bind author/inspector to finding |
| Inspection finding | Yes | `ElementDefect` là one type/location/element/time finding, PDF p. 15, §5.3; IFC binding PDF p. 16 |
| Recommended action | Partial | Treatment library và alternative rehab/maintenance projects, PDF p. 6, Fig. 2; không có recommendation entity/link |
| Action_Record identity | No | Planning steps ở PDF p. 6, Fig. 2; Figs. 6-8 không có action/work-order ID |
| Action priority/level | No | Severity 1-5 ở PDF p. 11, Table 5 là defect severity, không phải action priority |
| Workflow status | Partial | `QC pass` và `Bridge Stock Finished?` decisions, PDF p. 6, Fig. 2; không có persisted status vocabulary |
| Status-event history | No | Không có previous/new status, event log hoặc history collection trong process/schema, PDF pp. 6, 14-17 |
| Actor/time/reason | Partial | Roles ở PDF p. 6; finding tại particular point in time ở PDF p. 15; không có event binding actor-time-reason |
| Review/approval | Partial | `Bridge QC Engineer`, QC pass và Inspection Signing, PDF p. 6, Fig. 2; không có review record/signatory ID/timestamp |
| Repair execution | No | Process dừng ở alternatives và network working plan, PDF p. 6, Fig. 2 |
| Post-action verification | No | Model verification/QC/signing là pre-action inspection checks; không có post-repair acceptance loop, PDF p. 6, Fig. 2 |
| Provenance/audit trail | No | Exchange outputs được đặt tên, PDF pp. 7-10; schema không có derivation/version/change-author/audit relations |
| Integrity constraints | Yes | Mandatory/Optional/Not Recommended/Excluded, value restrictions và omission checks, PDF pp. 12, 15, 17-18, §§5.1, 5.3, 6 |
| Negative tests | No | Errors/refinement ở PDF p. 18, §6 không có intentionally invalid fixtures + expected failures + actual-versus-expected comparison |

### 2.2 Xu et al. (2022)

**Citation:** Xu, S., Wang, J., Wang, X., Wu, P., Shou, W., & Liu, C. (2022). A parameter-driven method for modeling bridge defects through IFC. *Journal of Computing in Civil Engineering, 36*. https://doi.org/10.1061/(ASCE)CP.1943-5487.0001026  
**Zotero key:** `Z4IBWW9Y`

Zotero record không có PDF/HTML child; full-text extraction không tìm thấy suitable attachment. Abstract chỉ cho biết broad scope về parametric defect geometry, relations với bridge elements/root causes/maintenance actions, bridge case và interoperability evaluation. Theo quy tắc đọc, các nội dung này không được dùng để hỗ trợ detailed claim.

| Claim được chứng minh | Exact page/section | Implementation/validation | Limitation | Thesis implication |
|---|---|---|---|---|
| Exact parameterized defect schema | Không có full text/page trong Zotero | Không thể kiểm chứng | **Evidence is currently insufficient.** | Không lấy field/entity từ abstract |
| Exact bridge-element/root-cause/maintenance-action relations | Không có full text/page trong Zotero | Không thể kiểm chứng | **Evidence is currently insufficient.** | Không khẳng định explicit Inspection_Record-Action_Record linkage |
| Exact case scenarios và interoperability results | Không có full text/page trong Zotero | Không thể kiểm chứng | **Evidence is currently insufficient.** | Không dùng làm validation evidence trong Round 2 |

| Thành phần | Yes / Partial / No | Exact evidence |
|---|---|---|
| BIM component identity | No | Không có full-text evidence. **Evidence is currently insufficient.** |
| Condition/defect evidence | No | Không có full-text evidence. **Evidence is currently insufficient.** |
| Evidence source/context | No | Không có full-text evidence. **Evidence is currently insufficient.** |
| Inspection_Record | No | Không có full-text evidence. **Evidence is currently insufficient.** |
| Inspector/author identity | No | Không có full-text evidence. **Evidence is currently insufficient.** |
| Inspection finding | No | Không có full-text evidence. **Evidence is currently insufficient.** |
| Recommended action | No | Không có full-text evidence. **Evidence is currently insufficient.** |
| Action_Record identity | No | Không có full-text evidence. **Evidence is currently insufficient.** |
| Action priority/level | No | Không có full-text evidence. **Evidence is currently insufficient.** |
| Workflow status | No | Không có full-text evidence. **Evidence is currently insufficient.** |
| Status-event history | No | Không có full-text evidence. **Evidence is currently insufficient.** |
| Actor/time/reason | No | Không có full-text evidence. **Evidence is currently insufficient.** |
| Review/approval | No | Không có full-text evidence. **Evidence is currently insufficient.** |
| Repair execution | No | Không có full-text evidence. **Evidence is currently insufficient.** |
| Post-action verification | No | Không có full-text evidence. **Evidence is currently insufficient.** |
| Provenance/audit trail | No | Không có full-text evidence. **Evidence is currently insufficient.** |
| Integrity constraints | No | Không có full-text evidence. **Evidence is currently insufficient.** |
| Negative tests | No | Không có full-text evidence. **Evidence is currently insufficient.** |

Các giá trị `No` trong bảng Xu có nghĩa “không được chứng minh từ attachment hiện có”, không phải kết luận rằng chức năng không tồn tại trong bài.

### 2.3 Wan et al. (2019)

**Citation:** Wan, C., Zhou, Z., Li, S., Ding, Y., Xu, Z., Yang, Z., Xia, Y., & Yin, F. (2019). Development of a bridge management system based on the building information modeling technology. *Sustainability, 11*(17), 4583. https://doi.org/10.3390/su11174583  
**Zotero key:** `Y44EIXWG`

| Claim được chứng minh | Exact page/section | Implementation/validation | Limitation | Thesis implication |
|---|---|---|---|---|
| IFC property-set extension nối bridge components với defect/reinforcement information | PDF pp. 3-4, §3.1.1, Tables 1-4, Fig. 1 | `Pset-diseasetype`, `Pset-reinforcetype`, defect/reinforcement fields; case database/model UI ở PDF pp. 9-11 | Không có complete logical database schema, PK/FK, cardinality, record IDs hoặc version rules | IFC layer không thay Inspection/Action database; thesis cần explicit records/keys |
| Manager-inspector mobile inspection workflow được operationalize | PDF p. 13, §5.2.2, Figs. 12-13; field use PDF p. 15, §5.3 | Web project creation, mobile capture, model/QR localization, standardized record, upload và manager data check | Không có assignment/status/rejection/signature schema | Dùng process skeleton nhưng formalize state/event/authorization |
| Defects/condition gắn component qua properties, coding, templates và colors | PDF pp. 4-6, §3.1.1-3.1.2, Tables 2, 4-6, Fig. 3; PDF pp. 13-14, Figs. 13-14 | Grand Canal Bridge records/images và color display | Ngoài crack, formal defect properties chủ yếu Boolean; color semantics không phải formal status và thresholds không được công bố | Tách evidence observation, condition assessment và visualization |
| Maintenance workflow có alert, repair project/plan, repair display và qualified/not-qualified check | PDF pp. 14-15, §5.2.2, Figs. 15-16 | Populated repair-plan rows và model-linked maintenance location | Không có trigger threshold, action ID, assignee, dates, progress states, criteria, verifier identity hoặc closure/reopen | Đây là strongest operational precedent; thesis phải formalize action/status/verification records |
| Validation là single-case feasibility với qualitative feedback | PDF pp. 11, 15-16, §§5.2-6, Figs. 9-16 | Real bridge deployment at maintenance company | Không có user count, baseline, time/error/usability metrics hoặc statistics | Không claim measured effectiveness; G3 cần acceptance tests |

| Thành phần | Yes / Partial / No | Exact evidence |
|---|---|---|
| BIM component identity | Partial | Bridge/component coding ở PDF p. 5, §3.1.2, Fig. 3; model/QR localization PDF pp. 13, 15; không có published populated component key/GlobalId crosswalk |
| Condition/defect evidence | Yes | `Pset-diseasetype`, Boolean defect fields, crack direction/length/width, PDF p. 4, Tables 1-4; text/image/report evidence PDF pp. 13, 15 |
| Evidence source/context | Partial | Text, pictures và reports, PDF p. 15, §5.3; không có source metadata/provenance schema |
| Inspection_Record | Partial | Project/template/upload/data-check workflow, PDF p. 13, Fig. 12; không có formal record ID/fields/schema |
| Inspector/author identity | Partial | Inspector logs in/selects project/captures data, PDF p. 13, §5.2.2; no author field or persisted actor relation |
| Inspection finding | Yes | Standardized common-defect template và member-linked defect/photo display, PDF pp. 13-14, Figs. 12-14 |
| Recommended action | Yes | Repair/reinforcement project and populated repair plans, PDF p. 14, §5.2.2, Fig. 15 |
| Action_Record identity | No | `Program NO.` appears as UI column, PDF p. 14, Fig. 15; datatype, uniqueness và inspection linkage không được specified |
| Action priority/level | Partial | Repair priorities được nói là defined nhưng values không công bố, PDF p. 5, §3.1.2; defect colors không phải action priority |
| Workflow status | Partial | Task release/receipt/progress tracking asserted, PDF p. 15, §5.3; không có enumerated persisted statuses |
| Status-event history | No | Implementation sections PDF pp. 11-15 không có status transition/event log schema |
| Actor/time/reason | Partial | Manager/inspector roles và `Creation data` UI column, PDF pp. 13-15, Figs. 12, 15; không có event-bound actor/time/reason |
| Review/approval | Partial | Manager data check và manager repair-result check, PDF pp. 13-14, §5.2.2; không có approval authority/outcome record |
| Repair execution | Yes | Text explicitly states after repair and displays maintenance location/effects, PDF pp. 14-15, §5.2.2, Fig. 16; execution record fields absent |
| Post-action verification | Partial | Qualified/not-qualified judgement and manager result check, PDF pp. 14-15, §5.2.2, Fig. 16; criteria/verifier/evidence/closure absent |
| Provenance/audit trail | No | No author/version/change history/audit relation in §§3.1, 4.2, 5.2-5.3 |
| Integrity constraints | No | Property types exist in Tables 1-4, nhưng không có executed record/workflow constraints |
| Negative tests | No | Không có intentionally invalid records, expected violations hoặc actual-versus-expected report |

### 2.4 Isailović et al. (2020)

**Citation:** Isailović, D., Stojanovic, V., Trapp, M., Richter, R., Hajdin, R., & Döllner, J. (2020). Bridge damage: Detection, IFC-based semantic enrichment and visualization. *Automation in Construction, 112*, 103088. https://doi.org/10.1016/j.autcon.2020.103088  
**Zotero key:** `9TDVUE9Q`

| Claim được chứng minh | Exact page/section | Implementation/validation | Limitation | Thesis implication |
|---|---|---|---|---|
| Inspection finding là process-linked grouped BIM object | PDF pp. 7-8, §§3.2.2.1-3.2.2.2, Figs. 7-8; implementation PDF p. 19, Figs. 24-25 | `IfcTask`, `IfcRelAssignsToProcess`, `IfcElementAssembly(INSPECTIONFINDING)`, `IfcRelAggregates`, `IfcSurfaceFeature(DAMAGE)` | Không có inspector, source document, approver hoặc record author attached | Tách Inspection_Record, Finding, Evidence và actor relations |
| Defect context kết hợp catalog semantics và IFC geometry | PDF pp. 6-9, §§3.2.2.1-3.2.2.3, Figs. 7-9; PDF p. 19, Fig. 24 | Type/code, `AssessmentCondition`, host-relative location và mesh extent | Deterioration process không có independent field; extent không có normalized area/volume field; severity cần expert | Tách observation type, interpretation, normalized extent và assessor |
| Damage được linked object-level tới host component | PDF pp. 7-9, §§3.2.2.2-3.2.2.3, Figs. 8-9; PDF p. 17, Fig. 20 | `IfcRelVoidsElement` và tessellated mesh; C++/IFCEngine implementation PDF p. 12, §4.1.5 | Mesh phải enlarge 100.5% để Boolean ổn định, làm thay đổi geometry (PDF p. 13, §6.2; p. 19, Fig. 26) | Lưu observed geometry tách visualization/Boolean geometry và transformation provenance |
| Validation so automatic enrichment với manually prepared baseline | PDF p. 13, §§5.2, 6.3; PDF pp. 18-20, Figs. 21-25, Tables 2-3 | Occurrence counts và missing-volume comparison trên một bridge | Single bridge/baseline; không có IFC conformance, BMS import, round trip hoặc inter-rater study | Tách detection performance khỏi information-integrity validation |
| Output là inspection deliverable supporting prioritization, không phải implemented action system | PDF pp. 16-17, §6.4; PDF pp. 17-20, §7 | As-is BrIM và proposed BMS integration routes | Không có recommendation, intervention, work order, priority, closure hoặc completed-action record | Không để finding tự động trở thành action; cần explicit decision/action layer |

| Thành phần | Yes / Partial / No | Exact evidence |
|---|---|---|
| BIM component identity | Yes | `IfcElement` host, `IfcBeam` example và `IfcRelVoidsElement`, PDF pp. 7-9, Figs. 8-9 |
| Condition/defect evidence | Yes | `IfcSurfaceFeature(DAMAGE)`, geometry, catalog type/code, severity, PDF pp. 6-9, 19, Figs. 7-9, 24 |
| Evidence source/context | Partial | Case point cloud/manual baseline, PDF pp. 9-10, §4; không có per-finding file/image/cluster/operator/version link |
| Inspection_Record | Yes | `IfcTask` + `IfcTaskTime` + inspection type + assigned findings, PDF p. 8, Fig. 8; PDF p. 19, Fig. 25 |
| Inspector/author identity | No | Human roles được mô tả ở PDF pp. 1, 6, 20, Table 4; không encoded qua IFC actors/authorship |
| Inspection finding | Yes | `IfcElementAssembly(INSPECTIONFINDING)` groups damage instances, PDF pp. 7-8, Figs. 7-8 |
| Recommended action | No | Maintenance prioritization chỉ là downstream use, PDF pp. 16-17, §6.4 |
| Action_Record identity | No | Không có action/treatment/work-order entity, PDF pp. 16-20, §§6.4-7 |
| Action priority/level | No | Severity 1-5 ở PDF pp. 6-8 là condition rating, không phải action level |
| Workflow status | No | Dated current as-is snapshot không có persisted finding/action status |
| Status-event history | No | Không có supersession/change/resolution event sequence trong Figs. 7-9, 24-25 |
| Actor/time/reason | Partial | Task start/finish và type, PDF p. 19, Fig. 25; actors/reason không bind vào record |
| Review/approval | No | Expert assessment role được nêu ở PDF p. 6; không có review/approval relation |
| Repair execution | No | Không có maintenance execution record, PDF pp. 16-20 |
| Post-action verification | No | Không có completed-action verification |
| Provenance/audit trail | No | Không có per-finding source/process version/change actor; PDF pp. 9-10, 19 |
| Integrity constraints | Partial | IFC relation/geometry requirements và point-cloud prerequisites được mô tả, PDF pp. 3-9, 17-20; không có executed schema validator |
| Negative tests | No | Missed/false detections ở PDF pp. 13, 20, Tables 2-3 là empirical errors; mesh-scale trials PDF pp. 13, 19 test geometry rendering, không phải workflow/schema negatives |

## 3. Cross-paper comparison

| Study | Evidence model | Inspection model | Action model | Status history | Human review | BIM linkage | Validation | Main missing element |
|---|---|---|---|---|---|---|---|---|
| Sacks et al. (2018) | `Defect`/`ElementDefect`, geometry, measurements, registered imagery, PDF pp. 10, 15-18 | Formal BPMN/IDM/MVD; QC/signing, PDF pp. 6, 12-18 | Treatment library và planning handoff only, PDF p. 6 | No persisted history | QC engineer/signing at process level, PDF p. 6 | IFC4 entities/relations and MVD, PDF pp. 14-17 | Expert review + XBIM conformance, PDF p. 18 | Action identity, execution, status events, provenance and post-action verification |
| Xu et al. (2022) | Detailed model unavailable | Detailed model unavailable | Detailed model unavailable | Unavailable | Unavailable | Unavailable | Unavailable | No full-text attachment; **Evidence is currently insufficient** |
| Wan et al. (2019) | IFC property sets + text/image/report + component display, PDF pp. 4, 13-15 | Manager project/mobile inspector/data check, PDF p. 13 | Repair projects/plans/categories and result UI, PDF pp. 14-15 | No formal vocabulary/history | Manager checks inspection and repair results, PDF pp. 13-15 | Model hierarchy, codes and QR/tag localization, PDF pp. 5, 12-15 | Single operational case/qualitative feedback, PDF pp. 11-16 | Logical record schema, actor-bound states, verification criteria and audit trail |
| Isailović et al. (2020) | Formal finding/damage/geometry/type/severity/time model, PDF pp. 6-9, 19 | `IfcTask/IfcTaskTime` assigned to findings, PDF pp. 8, 19 | None implemented, PDF pp. 16-20 | None | Experts participate but not encoded, PDF pp. 6, 20 | `IfcRelAssignsToProcess`, `IfcRelAggregates`, `IfcRelVoidsElement`, PDF pp. 7-9 | Single-bridge baseline occurrence/volume comparison, PDF pp. 13, 18-20 | Action/status/accountability and per-finding source provenance |

## 4. Prior art đã được xác lập

### BIM-linked defect/inspection records

Sacks formalizes `Defect`/`ElementDefect` in IFC and embeds them in `EM-4` (PDF pp. 10, 15-17, §4.4, §5.3, Fig. 8, Table 6). Isailović implements `IfcTask -> INSPECTIONFINDING -> DAMAGE -> host IfcElement` (PDF pp. 7-9, 19, Figs. 7-9, 24-25). Claim “link inspection/defect records to BIM components” không còn là novelty an toàn.

### Inspection images và findings gắn cấu kiện

Sacks registers high-resolution imagery onto object surfaces using `IfcImageTexture` and demonstrates a viewer (PDF pp. 10, 17-18, §4.4, §5.3, Fig. 9). Wan links text/pictures/reports and submitted defect information to selected components (PDF pp. 13, 15, §5.2.2-5.3, Figs. 12-13). Image/finding-to-component linkage đã có tiền lệ.

### Maintenance action representation

Wan defines `Pset-reinforcetype`, reinforcement properties and populated repair-plan categories (PDF p. 4, Tables 1, 3; PDF p. 14, Fig. 15). Sacks includes Bridge Treatment Library Data and alternative rehabilitation/maintenance projects (PDF p. 6, Fig. 2), nhưng không có formal action record. Broad maintenance-action category/plan representation không còn mới; stable Action_Record identity và event history vẫn mở.

### Inspection-to-repair workflow

Wan operationally demonstrates inspection capture, manager check, alert, repair project/plan, repair display và result check (PDF pp. 13-15, §5.2.2-5.3, Figs. 12-16). Sacks formal process chuyển từ inspection/QC/signing tới rehabilitation/maintenance alternatives and network work plan (PDF p. 6, Fig. 2). Workflow sequence nói chung không phải standalone contribution.

### Manager/engineer review nói chung

Sacks có Bridge QC Engineer, QC pass và Inspection Signing (PDF p. 6, Fig. 2). Wan có manager data check và repair-result check (PDF pp. 13-15, §5.2.2, Figs. 12, 16). Isailović yêu cầu experienced structural engineer cho deterioration assessment (PDF p. 6, §3.2.2.1). Generic human review đã có tiền lệ; novelty chỉ có thể nằm ở explicit actor/authorization/reason/audit records và executable accountability rules.

## 5. Minimum Condition_Evidence model

| Proposed field | Supporting study | Exact evidence | Classification |
|---|---|---|---|
| `Condition_Evidence_ID` | Sacks; Isailović | Defect occurrences exist as IFC objects, PDF Sacks pp. 15-16 §5.3; Isailović pp. 7-8 Figs. 7-8, nhưng không có dedicated evidence ID contract | THESIS_DEFINED |
| `source_reference` | Sacks; Wan; Isailović | Registered imagery, Sacks pp. 10, 17-18; text/picture/report, Wan pp. 13, 15; point cloud source at case level, Isailović pp. 9-10 §4 | INDIRECTLY_SUPPORTED |
| `BIM_GUID` | Sacks; Wan; Isailović | IFC component/finding relations, Sacks pp. 14-17; component code/model/QR, Wan pp. 5, 13, 15; host element relation, Isailović pp. 7-9 | INDIRECTLY_SUPPORTED |
| `observation_or_inspection_time` | Sacks; Isailović | Particular point in time, Sacks p. 15 §5.3; `IfcTaskTime` start/finish, Isailović p. 19 Fig. 25 | DIRECTLY_SUPPORTED |
| `finding_type` | Sacks; Wan; Isailović | Defect classes, Sacks pp. 15-17 Fig. 8/Table 6; defect codes/properties, Wan pp. 4-6; catalog type/code, Isailović pp. 6-8, 19 | DIRECTLY_SUPPORTED |
| `location` | Sacks; Wan; Isailović | ElementDefect geometry, Sacks pp. 15-17; component localization, Wan p. 13 Fig. 12; mesh/host/placement, Isailović pp. 7-9 | DIRECTLY_SUPPORTED |
| `extent` | Sacks; Wan; Isailović | Diameter/depth/width, Sacks pp. 15-17; crack length/width, Wan p. 4 Table 4; geometry-based extent, Isailović pp. 6-9 | DIRECTLY_SUPPORTED |
| `quality_or_confidence` | Isailović | Input-quality limits and baseline performance, PDF pp. 3-4, 13, 20; no per-finding confidence field | THESIS_DEFINED |
| `method_or_model_version` | Sacks; Isailović | Model stages `EM-2/3/4`, Sacks pp. 7-10; as-designed/as-built/as-is states, Isailović pp. 6-9; no explicit version field | INDIRECTLY_SUPPORTED |
| `responsible_agent` | Sacks; Wan; Isailović | Inspector/QC roles, Sacks p. 6; inspectors/managers, Wan pp. 13-15; specialist roles, Isailović p. 20 Table 4; actors not encoded | INDIRECTLY_SUPPORTED |
| `review_status` | Sacks; Wan | QC/signing, Sacks p. 6; manager data check, Wan p. 13; no persisted field vocabulary | INDIRECTLY_SUPPORTED |
| `limitation_or_context` | Sacks; Isailović | Occlusion/resolution omissions, Sacks p. 9 §4.2; registration/resolution/geometry constraints, Isailović pp. 3-5, 12-13, 17-20 | INDIRECTLY_SUPPORTED |

`quality_or_confidence` phải biểu diễn độ tin cậy/chất lượng của evidence hoặc processing result. Nó không đồng nghĩa và không thay thế defect severity/condition rating.

## 6. Minimum Inspection_Record model

| Proposed field | Supporting study | Exact evidence | Classification |
|---|---|---|---|
| `Inspection_Record_ID` | Sacks; Wan; Isailović | Inspection activities/tasks tồn tại, Sacks p. 6; Wan p. 13; Isailović pp. 8, 19; không có stable record-ID contract | THESIS_DEFINED |
| `linked_BIM_GUID` | Sacks; Wan; Isailović | Findings/components linked in IFC/model, Sacks pp. 14-17; Wan pp. 12-15; Isailović pp. 7-9 | DIRECTLY_SUPPORTED |
| `triggering_Condition_Evidence_ID` | None explicitly | Findings thường được tạo trong inspection, nhưng không có external evidence-to-inspection ID relation | THESIS_DEFINED |
| `inspection_date_time` | Sacks; Isailović | Point-in-time finding, Sacks p. 15; start/finish in `IfcTaskTime`, Isailović p. 19 Fig. 25 | DIRECTLY_SUPPORTED |
| `inspection_method` | Sacks; Wan; Isailović | Acquisition/manual inspection, Sacks pp. 6-10; daily/patrol codes, Wan p. 6 Table 5; `Routine inspection`, Isailović p. 19 Fig. 25 | DIRECTLY_SUPPORTED |
| `inspector` | Sacks; Wan; Isailović | Workflow/specialist roles, Sacks p. 6; Wan p. 13; Isailović pp. 1, 20; no actor field attached | INDIRECTLY_SUPPORTED |
| `finding` | Sacks; Wan; Isailović | `ElementDefect`, Sacks p. 15; common-defect template, Wan p. 13; `INSPECTIONFINDING`, Isailović pp. 7-8 | DIRECTLY_SUPPORTED |
| `supporting_image_or_document` | Sacks; Wan | `IfcImageTexture`, Sacks pp. 17-18; text/picture/report, Wan pp. 13, 15 | DIRECTLY_SUPPORTED |
| `recommendation` | Sacks; Wan | Treatment library/alternative projects, Sacks p. 6; repair-plan solutions, Wan p. 14 Fig. 15; no formal field link | INDIRECTLY_SUPPORTED |
| `review_or_approval` | Sacks; Wan | QC/signing, Sacks p. 6; manager data check, Wan p. 13 | INDIRECTLY_SUPPORTED |
| `record_version` | Sacks; Isailović | Model stages/states exist, Sacks pp. 7-10; Isailović pp. 6-9; no record-version semantics | THESIS_DEFINED |

## 7. Minimum Action_Record and Status_Event model

### Action_Record

| Proposed field | Supporting study | Exact evidence | Classification |
|---|---|---|---|
| `Action_Record_ID` | Wan | `Program NO.` appears in repair-plan UI, PDF p. 14 Fig. 15; no identifier contract/uniqueness/link | THESIS_DEFINED |
| `originating_Inspection_Record_ID` | Sacks; Wan | Inspection-to-planning sequence, Sacks p. 6 Fig. 2; Wan pp. 13-14 §5.2.2; no formal key relation | INDIRECTLY_SUPPORTED |
| `action_type` | Sacks; Wan | Treatment library, Sacks p. 6; `Pset-reinforcetype` and repair solutions, Wan pp. 4, 14, Tables 1, 3, Fig. 15 | DIRECTLY_SUPPORTED |
| `Action_Level` | Wan | Repair priorities said to be defined but exact values absent, PDF p. 5 §3.1.2 | EVIDENCE_INSUFFICIENT |
| `responsible_owner` | Wan | Managers receive alert/create project/check result, PDF pp. 14-15 §5.2.2; no formal owner field | INDIRECTLY_SUPPORTED |
| `assignee` | Wan | Task release/receipt asserted, PDF p. 15 §5.3; no action-assignee schema | THESIS_DEFINED |
| `target_date` | None explicitly | `Creation data` UI field exists, Wan p. 14 Fig. 15, nhưng không phải target date | THESIS_DEFINED |
| `rationale_or_evidence_basis` | Wan | Defect extent/safety concern triggers repair project, PDF p. 14 §5.2.2; no persisted rationale/evidence link | INDIRECTLY_SUPPORTED |

### Workflow_Status

Các status dưới đây là candidate vocabulary; không được trình bày như vocabulary đã được bốn bài xác nhận.

| Candidate status | Supporting study | Exact evidence | Classification |
|---|---|---|---|
| `Draft` | None explicitly | Không có exact term/state field | THESIS_DEFINED |
| `Open` | Wan | Project creation/selection, PDF p. 13 Fig. 12; exact status không được defined | THESIS_DEFINED |
| `Approved` | Sacks; Wan | Inspection signing/QC, Sacks p. 6; manager check, Wan p. 13; exact action status absent | THESIS_DEFINED |
| `In Progress` | Wan | Progress tracking asserted, PDF p. 15 §5.3; no exact vocabulary/schema | INDIRECTLY_SUPPORTED |
| `Completed` | Wan | “After repair” process evidence, PDF p. 14 §5.2.2; no persisted completed state | THESIS_DEFINED |
| `Verified` | Wan | Qualified/not-qualified judgement and manager result check, PDF pp. 14-15 §5.2.2, Fig. 16 | INDIRECTLY_SUPPORTED |
| `Closed` | None explicitly | No closure state or criteria | THESIS_DEFINED |
| `Rejected` | Sacks; Wan | QC fail loop, Sacks p. 6; not-qualified outcome, Wan p. 14; neither is formal Action_Record rejection status | INDIRECTLY_SUPPORTED |

### Status_Event

| Proposed field | Supporting study | Exact evidence | Classification |
|---|---|---|---|
| `Status_Event_ID` | None explicitly | Không có event identity/history model | THESIS_DEFINED |
| `previous_status` | None explicitly | Không có transition-event schema | THESIS_DEFINED |
| `new_status` | Sacks; Wan | QC branches và qualified/not-qualified outcomes, Sacks p. 6; Wan p. 14; not persisted | INDIRECTLY_SUPPORTED |
| `actor` | Sacks; Wan | QC engineer/inspector roles, Sacks p. 6; manager/inspector roles, Wan pp. 13-15 | INDIRECTLY_SUPPORTED |
| `timestamp` | Isailović; Wan | Inspection task time, Isailović p. 19 Fig. 25; repair-plan creation date UI, Wan p. 14 Fig. 15; no status-event timestamp | THESIS_DEFINED |
| `reason` | Wan | Safety-threatening defect triggers project, PDF p. 14 §5.2.2; no event reason field | INDIRECTLY_SUPPORTED |
| `approval_or_authorization` | Sacks; Wan | QC/signing, Sacks p. 6; manager checks, Wan pp. 13-15; no authorization record | INDIRECTLY_SUPPORTED |
| `related_evidence` | Sacks; Wan; Isailović | Findings/images/components exist, nhưng no status-event-to-evidence link | THESIS_DEFINED |

## 8. Workflow model

Candidate workflow dưới đây là synthesis cần kiểm chứng, không phải workflow đã được một bài triển khai đầy đủ.

| Candidate step | Supporting study | Support level | Required record/event | Required human role |
|---|---|---|---|---|
| Condition evidence available | Sacks pp. 10, 15-18; Wan pp. 13, 15; Isailović pp. 6-9, 19 | directly supported | Condition_Evidence | Evidence producer/inspector |
| Inspection initiated | Sacks p. 6 Fig. 2; Wan p. 13 Fig. 12 | directly supported as process | Inspection_Record created + `Draft/Open` event | Manager/bridge office |
| Inspection performed | Sacks pp. 6-10; Wan pp. 13, 15; Isailović pp. 8, 19 | directly supported | Inspection execution + findings + evidence links | Inspector |
| Finding reviewed | Sacks p. 6 QC/signing; Wan p. 13 manager data check | directly supported as process, not schema | Review_Event + decision + rationale | QC engineer/manager |
| Action proposed | Sacks p. 6 alternative projects; Wan p. 14 repair project/plan | directly supported as planning | Action_Record + rationale/evidence basis | Engineer/manager |
| Action approved or rejected | Sacks p. 6 inspection signing/QC; Wan p. 14 repair workflow | inferred for Action_Record | Authorization Status_Event | Authorized approver distinct from proposer where required |
| Action executed | Wan pp. 14-15 §5.2.2, Fig. 16 | directly supported operationally, not formalized | Execution record/evidence + status event | Assignee/contractor |
| Result verified | Wan pp. 14-15 qualified/not-qualified check | directly supported weakly at UI/process level | Verification_Record + evidence + `Verified/Rejected` event | Reviewer/verifier |
| Action closed | None explicitly | inferred | Closure Status_Event with satisfied preconditions | Authorized manager/approver |

## 9. Integrity và failure cases

| Proposed test | Classification | Evidence basis | Expected failure |
|---|---|---|---|
| Inspection_Record không có `BIM_GUID` | INDIRECT_METHOD_SUPPORT | Sacks MVD mandatory/omission checks, PDF pp. 12, 18; Isailović host relations, PDF pp. 7-9 | Reject orphan inspection/component linkage |
| Inspection không có evidence source | THESIS_DEFINED_REQUIREMENT | Sacks/Wan/Isailović use evidence artifacts but do not require source field, PDF Sacks pp. 10, 17; Wan pp. 13, 15; Isailović pp. 9-10 | Reject or flag incomplete evidence basis |
| Action_Record không có Inspection_Record | THESIS_DEFINED_REQUIREMENT | Sacks/Wan show process sequence, PDF Sacks p. 6; Wan pp. 13-14; no formal relation | Reject orphan action |
| Action không có rationale | THESIS_DEFINED_REQUIREMENT | Wan safety concern triggers repair, PDF p. 14; no rationale field | Reject approval or flag incomplete action |
| Illegal status transition | THESIS_DEFINED_REQUIREMENT | No persisted transition vocabulary in readable full texts | Reject transition and retain prior state |
| Status change thiếu actor/time/reason | THESIS_DEFINED_REQUIREMENT | Roles/times exist separately, Sacks p. 6; Wan pp. 13-15; Isailović p. 19; no event binding | Reject unauditable event |
| Action completed nhưng chưa verified | INDIRECT_METHOD_SUPPORT | Wan separates repair from qualified/not-qualified manager check, PDF pp. 14-15 | Prevent closure until verification event exists |
| Conflicting simultaneous statuses | THESIS_DEFINED_REQUIREMENT | No direct workflow constraint evidence | Reject non-single-current-state condition |
| Self-approval hoặc unauthorized approval | THESIS_DEFINED_REQUIREMENT | Sacks/Wan identify different roles but no authorization matrix, Sacks p. 6; Wan pp. 13-15 | Reject unauthorized decision |
| Closure không truy ngược được evidence | THESIS_DEFINED_REQUIREMENT | Full reverse chain absent; evidence/action fragments in Sacks, Wan, Isailović | Reject closure or flag broken lineage |

Không test nào trong bảng được coi là đã chạy. Sacks cung cấp indirect method support qua MVD conformance; Wan/Isailović không có workflow-negative fixture suites.

## 10. Candidate gaps

### 10.1 Explicit Inspection_Record-Action_Record linkage

**Claim**  
Explicit record-to-record linkage với stable identifiers là candidate gap mạnh.

**Evidence**  
Sacks đi từ inspection/signing tới alternative maintenance projects nhưng không có action entity (PDF p. 6, Fig. 2; PDF pp. 14-17, Figs. 6-8). Wan đi từ inspection data check tới repair project/plan nhưng chỉ trình bày UI/process (PDF pp. 13-15, Figs. 12-16). Isailović có formal inspection/finding model nhưng không có action record (PDF pp. 7-9, 16-20).

**What prior studies achieved**  
Inspection submodels, action categories/plans và operational handoff đã có.

**Remaining limitation**  
Trong phạm vi bốn tài liệu đã deep-read, chưa thấy stable `Inspection_Record_ID -> Action_Record_ID` relation, cardinality, rationale/evidence basis hoặc inverse query được chứng minh.

**Required thesis validation**  
PK/FK or equivalent identifiers; mandatory/inverse constraints; forward/reverse CQs; orphan/multiple-action fixtures; evidence-basis completeness.

**Verdict:** Strong candidate.

### 10.2 Queryable Status_Event history

**Claim**  
Immutable, queryable status-transition history là candidate gap mạnh.

**Evidence**  
Sacks có BPMN decisions nhưng không persisted status (PDF p. 6, Fig. 2). Wan nói progress tracking và qualified/not-qualified outcome nhưng không có status vocabulary/history (PDF pp. 14-15, §5.2.2-5.3). Isailović chỉ có dated inspection/as-is snapshot (PDF pp. 8, 19).

**What prior studies achieved**  
Process order, decision points, current visualization và selected outcomes.

**Remaining limitation**  
Trong phạm vi bốn tài liệu đã deep-read, chưa thấy `Status_Event_ID`, previous/new status, actor/time/reason, supersession hoặc history query.

**Required thesis validation**  
Transition table; one-current-state rule; immutable events; legal/illegal transition fixtures; chronological and actor-based CQs.

**Verdict:** Strong candidate.

### 10.3 Evidence-basis preservation

**Claim**  
Preserving source/context from evidence through inspection and action là candidate gap.

**Evidence**  
Sacks links imagery/geometry but lacks source hash/device/confidence (PDF pp. 10, 17-18). Wan uses text/picture/report without metadata schema (PDF pp. 13, 15). Isailović identifies case point cloud and task context but no per-finding source/process lineage (PDF pp. 9-10, 19).

**What prior studies achieved**  
Evidence artifacts, component links, finding type/location/extent/time and selected context.

**Remaining limitation**  
Per-evidence stable ID, source reference, acquisition/processing version, quality/confidence, responsible agent và action rationale lineage chưa được combined.

**Required thesis validation**  
Completeness rules; evidence-to-source/component/action reverse query; missing-source/version/agent fixtures; canonical payload and provenance checks.

**Verdict:** Promising.

### 10.4 Accountable review and approval

**Claim**  
Review/approval có explicit actor, authority, rationale và outcome có thể là supporting contribution mạnh.

**Evidence**  
Sacks có QC Engineer, QC pass và inspection signing (PDF p. 6). Wan có manager data check và repair-result check (PDF pp. 13-15). Isailović có expert interpretation roles nhưng không encoded actors (PDF pp. 6, 20).

**What prior studies achieved**  
Human roles và review/check steps ở process level.

**Remaining limitation**  
Trong phạm vi bốn tài liệu đã deep-read, chưa thấy role-permission matrix, reviewer/approver ID, rationale, signature timestamp, separation-of-duties rule hoặc auditable override.

**Required thesis validation**  
Authorization matrix; review event schema; unauthorized/self-approval/missing-rationale fixtures; reverse trace to reviewer and evidence.

**Verdict:** Promising.

### 10.5 Post-action verification

**Claim**  
Formal post-action verification record là candidate gap, trong khi generic result checking đã có tiền lệ.

**Evidence**  
Wan mô tả qualified/not-qualified judgement và manager check sau repair (PDF pp. 14-15, §5.2.2, Fig. 16). Sacks chỉ có inspection QC/signing trước maintenance planning (PDF p. 6). Isailović không có action execution/verification (PDF pp. 16-20).

**What prior studies achieved**  
Operational post-repair check ở Wan, nhưng không có criteria/verifier/evidence/closure schema.

**Remaining limitation**  
Verification_Record, acceptance criteria, verifier identity, before/after evidence, rejection/rework path và closure preconditions chưa được formalized.

**Required thesis validation**  
Mandatory verification evidence; independent verifier rule where applicable; completed-not-verified fixture; reject/reopen paths; closure guard.

**Verdict:** Promising.

### 10.6 Integrity testing cho workflow

**Claim**  
Controlled integrity/failure testing cho inspection-action-status workflow là candidate gap mạnh.

**Evidence**  
Sacks executes MVD conformance and omission checks but not strict negative fixtures (PDF pp. 12, 18). Wan does not report executable workflow constraints (PDF pp. 11-16). Isailović reports empirical misses/false detections and geometry trials, not malformed workflow records (PDF pp. 13, 19-20).

**What prior studies achieved**  
Schema conformance, case feasibility, baseline performance và limited failure-oriented geometry trials.

**Remaining limitation**  
Trong phạm vi bốn tài liệu đã deep-read, chưa thấy controlled valid/invalid fixtures, expected workflow violations và actual-versus-expected results cho record linkage/status/accountability.

**Required thesis validation**  
Versioned fixture manifest; one-fault mutations; stable violation codes; test oracle; coverage by entity/relation/transition/role; regression execution.

**Verdict:** Strong candidate.

## 11. G2 specification decisions

| Specification area | Evidence status | Decision có thể khóa sau Round 2 | Validation obligation |
|---|---|---|---|
| Condition_Evidence fields | quyết định suy ra từ nhiều nguồn | ID, source ref, BIM link, time, type, location, extent, quality/confidence, method/version, agent, review/context | Completeness, provenance and reverse-source tests |
| Inspection_Record fields | quyết định đã có bằng chứng cho core; thesis-defined cho ID/version | ID, component link, evidence link, time, method, inspector, finding, media, recommendation, review, version | Mandatory links, uniqueness, review-state and reverse queries |
| Action_Record fields | quyết định suy ra từ Sacks/Wan; thesis-defined cho identity/governance | ID, originating inspection, action type/level, owner, assignee, target, rationale/evidence basis | Orphan action, missing rationale, assignment and evidence-basis tests |
| Workflow_Status vocabulary | quyết định riêng của luận án cần kiểm chứng | Candidate states only; define meanings, entry/exit guards and terminal states before implementation | Stakeholder review, transition coverage and illegal-transition fixtures |
| Status_Event fields | quyết định riêng của luận án cần kiểm chứng | ID, previous/new status, actor, time, reason, authorization, related evidence | Immutability, chronology, authorization and one-current-state tests |
| Human-role matrix | quyết định suy ra từ nhiều nguồn | Inspector, manager, QC/reviewer, proposer, approver, assignee, verifier; define permissions/separation | Unauthorized and self-approval tests; actor traceability |
| Cardinality | core method supported by Sacks; values thesis-defined | One inspection has one-or-more findings; action requires originating inspection; status event belongs to one record; exact optionalities to be reviewed | Positive/negative cardinality fixtures |
| Mandatory/optional relationships | method supported; domain choices thesis-defined | Evidence-component, finding-inspection, action-inspection, status-record, review-actor and verification-action relations | Missing-link and wrong-target tests |
| Workflow transition rules | quyết định riêng của luận án cần kiểm chứng | Define allowed transition matrix, rejection/rework, verification and closure guards | Every allowed/forbidden edge tested with expected outcome |

Round 2 đủ để khóa candidate specification scope và evidence provenance của từng quyết định. Nó chưa đủ để tuyên bố schema/status vocabulary đã validated.

## 12. Novelty boundary

### Contribution statement an toàn

> Trong phạm vi bốn tài liệu đã deep-read, Paper 2 có thể định vị Inspection-Action Model như một implementation-neutral specification liên kết stable `Condition_Evidence`, `Inspection_Record`, `Action_Record` và immutable `Status_Event`, bảo toàn evidence basis và human accountability, đồng thời được kiểm chứng bằng bidirectional queries, authorization/transition constraints, valid/invalid fixtures và post-action verification guards.

Statement này chỉ dùng sau khi các tests được thực thi. Trước đó, đây là proposed contribution và validation plan.

### Supporting contributions

- Minimum Condition_Evidence dictionary tái dùng defect type/location/extent/time/context precedents từ Sacks pp. 15-18 và Isailović pp. 6-9, 19, đồng thời bổ sung provenance/quality fields cần kiểm chứng.
- Human-role and approval matrix mở rộng process roles/QC/checking từ Sacks p. 6 và Wan pp. 13-15 thành actor-bound authorization events.
- Technology-neutral integrity catalogue chuyển MVD conformance precedent của Sacks pp. 12, 18 sang record linkage, status transition, verification và audit requirements.

### Claims không được sử dụng

- Không claim BIM-linked defects, component-linked inspection images, inspection findings hoặc maintenance categories là novelty: Sacks PDF pp. 10, 15-18; Wan PDF pp. 4, 13-15; Isailović PDF pp. 6-9, 19.
- Không claim generic inspection-to-repair sequence hoặc manager review là novelty: Sacks PDF p. 6; Wan PDF pp. 13-15.
- Không coi color-coded condition hoặc UI progress/check screens là formal status/event model: Wan PDF pp. 13-15.
- Không coi defect severity là Action_Level: Sacks PDF p. 11 Table 5; Isailović PDF pp. 6-8.
- Không coi empirical missed/false detections hoặc mesh-scaling trials là workflow negative tests: Isailović PDF pp. 13, 19-20.
- Không tuyên bố Xu exact schema, fields, validation hoặc interoperability outcome cho đến khi full text khả dụng. **Evidence is currently insufficient.**
- Không mô tả Action_Record/status/verification chain như đã validated trước khi G3 chạy fixtures, queries và transition tests.
- Không mặc định toàn bộ records phải nằm trong IFC; specification phải cho phép IFC, relational, graph hoặc hybrid persistence nếu giữ nguyên IDs, constraints và traceability contract.

## 13. Next actions

1. **Governance:** khóa ownership/format/versioning cho `Action_Record_ID`, định nghĩa `Action_Status` là current projection hay stored attribute, và xác định `Status_Event` là immutable source of truth.
2. **Schema:** khóa candidate ER/data dictionary cho Condition_Evidence, Inspection_Record, Action_Record, Status_Event, Review_Event và Verification_Record; chỉ rõ mandatory/optional relations và IFC/external-storage boundary.
3. **Role/status model:** workshop với domain stakeholders để duyệt role-permission/separation matrix, candidate status meanings, allowed transitions, rejection/rework và closure guards.
4. **Competency questions:** viết paired forward/reverse CQs cho evidence-component-inspection-action-status, review authority, pending verification, rejection/rework và closure lineage; predefine expected answer shapes.
5. **Fixtures:** tạo valid baseline và one-fault invalid records cho orphan IDs, missing source/rationale/actor/time/reason, illegal transitions, conflicting statuses, unauthorized approval và unverified closure.
6. **G3 workflow tests:** chạy schema/cardinality/reference/authorization/transition constraints, forward/reverse queries, expected-versus-actual failure reports và regression suite; không khóa một validation technology trước khi so sánh implementation options.
7. **G1 dependency:** định nghĩa interface yêu cầu evidence thật từ G1 gồm stable ID, source reference, candidate BIM link, observation time, method/model version, quality/confidence và limitations; G2 tiếp nhận evidence mà không biến nó thành diagnosis hoặc tự động quyết định action.
