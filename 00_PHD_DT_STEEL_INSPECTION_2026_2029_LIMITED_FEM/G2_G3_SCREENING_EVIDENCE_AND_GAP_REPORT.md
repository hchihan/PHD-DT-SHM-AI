# G2-G3 Screening Evidence and Gap Report

Collection được sàng lọc: `RQ2_RQ3_CORE_DEEP_READ_20260803` (`C9J2V33M`), là collection duy nhất Zotero trả về khi tìm `RQ2_RQ3_CORE_DEEP_READ_202608`.

Ngày sàng lọc: 2026-08-04.

Phạm vi diễn giải trong báo cáo này luôn là: **Trong phạm vi các tài liệu đã sàng lọc...** Không có kết luận nào được hiểu là tuyên bố bao quát toàn bộ học thuật.

## 1. Executive summary

- **Quy mô:** 34 entries đã được rà soát, gồm 33 bibliographic/web records và 1 standalone academic PDF. Kết quả: **12 Tier A, 14 Tier B, 2 Tier C và 6 Exclude**.
- **Cách đọc:** toàn bộ 34 entries được đọc title, metadata, abstract/keywords khi có. Các bài gần G2-G3 nhất được kiểm tra thêm introduction/problem, method, implementation/query, validation/results và conclusion từ PDF hoặc publisher full-text snippets. Không dùng tài liệu thương mại hay báo cáo Perplexity làm academic evidence.
- **Editorial notice check:** Scite kiểm tra được 13 items có DOI trong collection; không phát hiện retraction, correction, expression of concern hoặc editorial notice tại thời điểm sàng lọc. Các items không có DOI không nằm trong phép kiểm tra này.
- **Đối thủ gần nhất về schema/workflow:** **Bellon et al. (2025)**, vì đã đề xuất IFC 4.3.2.0 framework tích hợp inspection, damage, maintenance service và cost, có implementation và schema/software validation.
- **Đối thủ gần nhất về semantic linkage/CQ/identity:** **Lorvão Antunes et al. (2024)**, vì đã liên kết inspection/risk-condition observations với structural elements và IFC GlobalId, thực thi SPARQL competency questions và minh họa BIM-AMS pilot.
- **Khoảng trống mạnh nhất:** không phải từng công nghệ riêng lẻ, mà là **validation tích hợp của chuỗi identity-governed Condition_Evidence -> BIM component -> Inspection_Record -> Action_Record -> Status_Event**, gồm deliberate referential-integrity failure tests, forward/reverse traceability và accountability của human review.
- **Deep-read trước:** Bellon et al. (2025), Lorvão Antunes et al. (2024), Sacks et al. (2018), Xu et al. (2022), Wan et al. (2019), Isailović et al. (2020), Lee et al. (2021) và Oraskari et al. (2021).
- **Kết luận sơ bộ:** hướng G2-G3 có đủ nền tảng để tiếp tục nếu novelty được khóa ở **artifact tích hợp + protocol validation**, không đặt ở BIM viewer, ontology, GlobalId, CQ, provenance hoặc SHACL riêng lẻ.

Giới hạn bằng chứng: một số records chỉ có metadata/abstract hoặc publisher snippets; bài Hüthwohl et al. (2018) không có PDF child trong Zotero; Xu et al. (2022) không có full-text attachment; record Stolk and McGlinn (2020) có sai khác tên tác giả trong Zotero (`Sanne` so với `Sander` trên PDF) và abstract Zotero mô tả quá rộng về WHERE-rules. Những điểm này được tính vào độ tin cậy và priority.

## 2. Screening matrix

| Rank | Citation | Tier | Topic | What it demonstrates | Validation level | Relevance to G2/G3 | Main limitation | Deep-read priority |
|---:|---|---|---|---|---|---|---|---|
| 1 | Bellon et al. (2025), *IFC framework for inspection and maintenance representation in facility management* | Tier A | IFC inspection-maintenance schema | IFC 4.3.2.0 framework cho inspection, damage, maintenance service và cost; tạo IFC study cases | IFC schema verification, open-source/buildingSMART checks và semantic evaluation trên nhiều BIM tools | Đối thủ gần nhất cho Inspection_Record-Action_Record | Chưa có CQ, provenance/accountability formal, deliberate negative fixtures hoặc round-trip identity test; real-world integration là future work | P1 — đọc ngay |
| 2 | Lorvão Antunes et al. (2024), *Ontology-based BIM-AMS integration in European Highways* | Tier A | BIM-AMS ontology, CQ, GlobalId | Inspection/risk-condition observations gắn structural element; SPARQL trả result + IFC GlobalId; GraphDB/API/BIM pilot | CQ execution, OOPS! ontology scan, expert-informed data dictionary và ba pilots | Bao phủ identity, inspection, CQ, implementation và condition result | Mapping còn thủ công; SHACL/SWRL chưa triển khai; không có action/status chain, negative fixtures hoặc round-trip parity | P1 — đọc ngay |
| 3 | Sacks et al. (2018), *SeeBridge as next generation bridge inspection* | Tier A | Formal bridge inspection exchange | IDM, BPMN, MVD/mvdXML, defect schema, QC gate, signing và conformance workflow | Expert workshops; bốn bridge IFC models; syntax/semantic/content/omission checks | Tiền lệ mạnh cho formal specification, inspection evidence, constraints và human review | Không formal hóa provenance, Action_Record/Status_Event, CQ, accountability identity hoặc end-to-end repair closure | P1 — đọc ngay |
| 4 | Xu et al. (2022), *A Parameter-Driven Method for Modeling Bridge Defects through IFC* | Tier A | IFC defect-action representation | Parametric defect geometry và quan hệ với bridge element, root cause, maintenance action | Concrete highway bridge; hai scenarios; cross-tool interoperability evaluation | Rất gần chuỗi condition evidence-BIM-action | Không thấy CQ, event/status model, provenance, negative tests hay accountable review trong abstract; chưa có PDF Zotero để xác nhận sâu | P1 — đọc ngay |
| 5 | Wan et al. (2019), *Development of a Bridge Management System Based on BIM Technology* | Tier A | Operational inspection-to-repair workflow | Mobile inspection, component-linked evidence, manager check, condition scoring, repair plan, notification và repair-result check | Single real bridge deployment; functional demonstration; qualitative feedback | Tiền lệ vận hành rõ nhất cho inspection-action-review | Workflow states chưa thành semantic Status_Event; không GlobalId, CQ, constraints, negative tests hoặc audit trail | P1 — đọc ngay |
| 6 | Isailović et al. (2020), *Bridge damage: detection, IFC-based semantic enrichment and visualization* | Tier A | Contextual condition findings | As-is IFC với finding geometry, inspection date/type, damage type, deterioration process, location, extent và severity linked to elements | Real bridge against manual baseline; reported type-specific detection and correspondence performance | Tiền lệ trực tiếp cho context-preserving Condition Evidence | Chưa có longitudinal state transition, encoded provenance/reviewer identity, action closure, CQ hoặc controlled negative tests | P1 — đọc ngay |
| 7 | Lee et al. (2021), *Rules and validation processes for interoperable BIM data exchange* | Tier A | IFC/MVD constraints | GUID 22-character format, within-file GUID uniqueness, mandatory values, datatype, relationship/inverse and semantic rules in IfcDoc | Multiple IFC cases with itemized pass/fail reports | Nền tảng mạnh cho G2 constraint catalog và G3 failure reporting | Failures không phải controlled negative fixtures; không external FK/orphan tests, lifecycle identity hoặc inspection-action chain | P1 — đọc ngay |
| 8 | Oraskari et al. (2021), *SHACL is for LBD what mvdXML is for IFC* | Tier A | SHACL unit/regression testing | GUID-based IFC-to-LBD correspondence, selected relationship preservation, checksum/regression và model-view shapes | Java/TopBraid tests on Duplex model and independent converter output | Nền tảng gần nhất cho executable identity/traceability tests | R1 chỉ chắc chắn bắt missing counterpart, chưa reject duplicate; không reverse conversion hay full-chain traceability | P1 — đọc ngay |
| 9 | Hüthwohl et al. (2018), *Integrating RC bridge defect information into BIM models* | Tier A | Defect/inspection schema | Schema nhúng bridge defect và inspection attributes vào BIM elements | Metadata/abstract và Zotero research notes; full-text attachment không hiện diện | Trực tiếp ảnh hưởng Condition_Evidence và Inspection_Record schema | Concrete-bridge scope; validation, integrity tests, provenance và action/status cần xác nhận từ full text | P2 — đọc sau |
| 10 | Wang et al. (2024), *Enhancement and validation of ifcOWL ontology based on SHACL* | Tier A | SHACL for IFC integrity | Chuyển EXPRESS WHERE rules thành SPARQL-based SHACL và phát hiện lỗi/inconsistency trong ifcOWL graphs | Implemented graph validation theo abstract/publisher metadata | Nền tảng mới và trực tiếp cho G3 constraint engine | Generic ifcOWL quality control; không evidence-inspection-action chain, deliberate domain fixtures hoặc round-trip traceability | P2 — đọc sau |
| 11 | Stolk and McGlinn (2020), *Validation of IfcOWL datasets using SHACL* | Tier A | Closed-world ifcOWL validation | Chuyển OWL restrictions thành SHACL cardinality/class/datatype/value shapes; RDF validation reports | Executed on R2RML-generated ifcOWL sample; violations hỗ trợ sửa mapping | Nền tảng cho SHACL structural integrity | Không global GUID uniqueness, external FK, deliberate negatives hoặc round trip; Zotero metadata có author-name/abstract discrepancy | P2 — đọc sau |
| 12 | buildingSMART International (2024), *IfcRoot and IfcGloballyUniqueId - IFC 4.3.2.0 official documentation* | Tier A | Normative BIM identity | `IfcRoot.GlobalId` mandatory, unique và encoded 22-character identifier; rule UR1 | Normative schema definition | Khóa semantic và constraint của BIM identity | Chỉ định nghĩa identity trong IFC; không giải quyết persistence qua revisions hay external records | P3 — background |
| 13 | Kim et al. (2018), *Integration of IFC objects and facility management work information using Semantic Web* | Tier B | BIM-linked work records | OWL/FM ontology, Jena/BOSSAM/SPARQL, liên kết IFC objects với 590 historical work records | Two-storey office case; retrieval demonstration | Tiền lệ cho BIM-linked records và action history | Dùng STEP instance IDs, không chứng minh GlobalId; không condition provenance, CQ, status events, constraints hoặc synchronization | P2 — đọc sau |
| 14 | Theiler and Smarsly (2018), *IFC Monitor* | Tier B | Sensor/SHM schema | EXPRESS IFC extension cho sensor nodes, networks, topology và quan hệ với structural elements | Syntax/semantic/unit checks, deliberately invalid model checks và lab SHM prototype | Nền tảng schema identity và tiền lệ controlled invalid cases | Không biểu diễn observation/condition transition hoặc inspection-action chain; topology rule còn future work | P2 — đọc sau |
| 15 | Pauwels and Terkaj (2016), *EXPRESS to OWL for construction industry* | Tier B | ifcOWL foundation | Methodology chuyển IFC EXPRESS schema sang reusable OWL representation | Ontology/schema engineering validation | Cơ sở kỹ thuật cho ifcOWL identity và SHACL route | Không có inspection, action, provenance hay domain validation chain | P3 — background |
| 16 | Theiler et al. (2017), *BIM-based design of structural health monitoring systems* | Tier B | IFC Monitor application | Áp dụng IFC Monitor để thiết kế SHM system gồm sensor nodes/base station | Laboratory application | Hỗ trợ sensor-to-BIM implementation precedent | Không condition evidence record, inspection/action/status hoặc integrity battery | P3 — background |
| 17 | Quinn et al. (2020), *Building automation system-BIM integration using a linked data structure* | Tier B | Time-series state-to-BIM | Timestamped BAS states và naming chain `BuildingID.SysID.BASID.PointID` mapped to Revit context | Local network và khoảng 10,000 near-real-time points in a building | Hỗ trợ context-preserving operational evidence và identity mapping | Không IFC GlobalId, inspection/action chain, semantic provenance, user validation hoặc formal negative tests | P2 — đọc sau |
| 18 | Carvalho et al. (2023), *BIM model to support O&M tasks* | Tier B | Maintenance/action fields | Maintenance sheet gồm element ID, inspection/cleaning/correction/replacement, procedure, responsible entity, schedule và cost | Literature-informed schema and illustrative Revit/spreadsheet figures | Hỗ trợ Action_Record fields và responsibility vocabulary | Không query/integration, evidence finding, status transition, integrity tests hay case validation | P3 — background |
| 19 | Ciccarese et al. (2013), *PAV ontology: provenance, authoring and versioning* | Tier B | Provenance/accountability vocabulary | Phân biệt author, curator, contributor, creator/software; import/retrieval/derivation/version timestamps | Multiple project adoption; SPARQL/OWL interoperability demonstrations | Hỗ trợ provenance và responsibility fields | Không BIM/inspection semantics; compact PAV không đủ detailed process lineage hoặc approval enforcement | P2 — đọc sau |
| 20 | Moreau and Missier (2013), *PROV-DM: the PROV data model* | Tier B | Provenance model | Entity-Activity-Agent, generation, usage, derivation, attribution, association và revision | W3C data-model specification | Nền tảng cho evidence lineage và accountable agents | Domain-neutral; không inspection/action schema hoặc validation implementation trong collection | P3 — background |
| 21 | Lebo et al. (2013), *PROV-O: the PROV ontology* | Tier B | Executable provenance vocabulary | OWL2 classes/properties cho `prov:used`, `prov:wasDerivedFrom`, `prov:generated` | W3C ontology specification | Có thể tái dùng cho evidence-action lineage | Không tự cung cấp domain constraints, human approval hay BIM identity mapping | P3 — background |
| 22 | Monfardini et al. (2023), *Use of competency questions in ontology engineering: a survey* | Tier B | CQ methodology | Survey 63 ontology engineers; CQ hỗ trợ scope/evaluation nhưng khó viết, dùng và quản lý | Empirical practitioner survey | Chứng minh CQ là established method và cần quản trị chặt | Không phải domain schema/implementation; không chứng minh G2/G3 CQs cụ thể | P3 — background |
| 23 | Keet and Khan (2025), *Characterising Competency Questions for Ontologies* | Tier B | CQ taxonomy and validation | Phân loại SCQ, VCQ, FCQ, RCQ, MpCQ; yêu cầu VCQ formalizable/answerable; ROCQS repository | Conceptual model plus SewerNet use case | Hữu ích để khóa pre-specified CQ và phân biệt CQ với constraint checks | Standalone attachment thiếu Zotero bibliographic metadata; không trực tiếp về BIM/inspection | P2 — đọc sau |
| 24 | Rasmussen et al. (2020), *Building topology ontology (BOT)* | Tier B | Lightweight BIM topology | Lightweight ontology cho storey, space, element và interface; alignment với IFC | Published ontology/model | Hỗ trợ component context và modular ontology design | Không GlobalId governance, inspection/action/provenance hoặc validation battery | P3 — background |
| 25 | U.S. GSA (2011), *GSA BIM Guide Series 08: Facility Management* | Tier B | Persistent asset identity | Yêu cầu BIM GUID cùng persistent human-readable Asset ID để nối Record BIM, COBie, CMMS và BAS/EMS | Owner/federal guidance | Hỗ trợ dual-identifier governance | Gray guidance, không peer-reviewed validation; không evidence-action chain | P3 — background |
| 26 | Celik et al. (2023), *Blockchain supported BIM data provenance for construction projects* | Tier B | BIM provenance/accountability | Blockchain model ghi discipline, version, responsibility/liability; bridge-construction experiment | Ethereum test network, real-world bridge scenario và cost analysis | Hỗ trợ BIM object provenance/accountability precedent | Construction information exchange, không inspection-action chain; blockchain không cần thiết cho Paper 2 | P3 — background |
| 27 | International Organization for Standardization (2024), *Asset management - vocabulary, overview and principles* | Tier C | Asset-management vocabulary | Lifecycle, value, risk và performance principles | International standard | Bối cảnh thuật ngữ quản lý tài sản | Không schema/query/implementation hoặc G2/G3 validation | P3 — background |
| 28 | Du et al. (2024), *BIM and IFC Data Readiness for AI Integration* | Tier C | BIM/IFC data readiness | PRISMA review 93 papers; nêu IFC time-series và conversion-toolchain limitations | Systematic literature review | Bối cảnh về data readiness | Trọng tâm AI integration, không inspection-action traceability; ngoài novelty core | P3 — background |
| 29 | Armijo and Zamora-Sánchez (2024), *Railway Bridge SHM with IoT and a Digital Twin* | Exclude | Predictive/anomaly monitoring | Low-cost accelerometers, ML anomaly alerts và two-year bridge pilot | Field deployment | Chỉ là field feasibility context | Ngoài phạm vi: damage/anomaly diagnosis, predictive monitoring và automated warnings | P3 — background |
| 30 | *Development of a Bridge Management System Based on BIM Technology* (webpage, no author/date) | Exclude | Duplicate/weak metadata | Có PDF/web entry trùng tiêu đề với Wan et al. (2019) | Không độc lập | Không bổ sung evidence | Metadata không đủ và trùng bibliographic article đã giữ | P3 — background |
| 31 | Monfardini et al. (2023), conference record cùng tiêu đề CQ survey | Exclude | Duplicate record | Cùng study về 63 ontology engineers | Duplicate bibliographic representation | Không bổ sung evidence ngoài retained book-section record | Trùng study; tránh double counting | P3 — background |
| 32 | *PROV-O: The PROV Ontology* (webpage, no author/date) | Exclude | Duplicate specification page | Web record của PROV-O | Duplicate/weak metadata | Không bổ sung evidence | Đã giữ Lebo et al. (2013) với metadata tốt hơn | P3 — background |
| 33 | *5.1.3.44 IfcRoot - IFC 4.3.2 Documentation* (webpage, no author/date) | Exclude | Duplicate specification page | Web record về IfcRoot | Duplicate/weak metadata | Không bổ sung evidence | Đã giữ buildingSMART International (2024) | P3 — background |
| 34 | *ISO 55000:2024* (webpage, no author/date) | Exclude | Duplicate standard page | Web record của ISO 55000 | Duplicate/weak metadata | Không bổ sung evidence | Đã giữ bibliographic standard record với corporate author | P3 — background |

## 3. Evidence already established

Các nội dung sau đã có tiền lệ và **không được tiếp tục xem là novelty độc lập**:

### Sensor-to-BIM và operational data linkage

Theiler and Smarsly (2018), Theiler et al. (2017), Quinn et al. (2020) và Lorvão Antunes et al. (2024) đã cho thấy sensor/SHM/BAS data hoặc metadata có thể được nối với BIM/structural context. Novelty không thể là “đưa dữ liệu cảm biến vào BIM”.

### IFC GlobalId/BIM identity

buildingSMART International (2024) đã định nghĩa normatively `IfcRoot.GlobalId`; Lee et al. (2021) đã kiểm tra format và uniqueness trong một IFC file; Lorvão Antunes et al. (2024) đã truy xuất inspection result cùng IFC GUID; Oraskari et al. (2021) đã dùng GUID để align representations. Novelty chỉ còn ở **governance và kiểm chứng persistence/cross-system identity**, không ở việc sử dụng GlobalId.

### BIM-linked inspection và condition records

Hüthwohl et al. (2018), Sacks et al. (2018), Isailović et al. (2020), Xu et al. (2022), Lorvão Antunes et al. (2024) và Bellon et al. (2025) đã biểu diễn defect/condition/inspection information gắn với BIM components. Novelty không thể là “lưu inspection record trong/ngoài BIM và tạo liên kết”.

### Maintenance/action information

Kim et al. (2018) liên kết historical FM work records; Wan et al. (2019) có inspection-to-repair workflow; Xu et al. (2022) biểu diễn maintenance actions; Carvalho et al. (2023) đề xuất maintenance sheets; Bellon et al. (2025) tích hợp inspection, damage, maintenance và cost. Novelty không thể là “thêm maintenance action vào BIM”.

### Competency questions

Monfardini et al. (2023) cho thấy CQ là thực hành đã được dùng trong ontology engineering; Keet and Khan (2025) phân loại CQ và yêu cầu validation CQs phải formalizable/answerable; Lorvão Antunes et al. (2024) đã thực thi SPARQL CQs cho bridge inspection/risk-condition. Novelty không thể là “dùng competency questions”.

### Provenance

PROV-DM, PROV-O và PAV đã cung cấp vocabulary về entity-activity-agent, derivation, attribution, version và authoring; Celik et al. (2023) đã áp dụng provenance/responsibility ở BIM object level. Novelty không thể là “thêm provenance”; đóng góp chỉ có thể nằm ở **domain-specific provenance coverage và validation**.

### SHACL và constraint validation

Lee et al. (2021) đã chứng minh IFC/MVD rule validation; Stolk and McGlinn (2020), Oraskari et al. (2021) và Wang et al. (2024) đã chứng minh SHACL cho ifcOWL/LBD constraints, conversion checks hoặc WHERE-rule-derived validation. Novelty không thể là “dùng SHACL”.

### Human review trong inspection workflow

Sacks et al. (2018) đã có QC gate, inspection signing và manual supplementation; Wan et al. (2019) đã có manager checking và repair-result checking; Isailović et al. (2020) yêu cầu expert judgement ở nhiều bước. Novelty không thể là “có con người trong vòng lặp”, mà phải là **accountability được biểu diễn và kiểm thử**.

## 4. Candidate academic gaps

### 4.1 Context-preserving Condition Evidence

**Claim**  
Một `Condition_Evidence` artifact bảo toàn source/run/time/method/version/quality context và liên kết ổn định tới BIM component có thể là đóng góp, nhưng “condition evidence linked to BIM” tự nó không mới.

**Evidence**  
Isailović et al. (2020) lưu inspection date/type, geometry, damage type, process, location, extent và severity; Sacks et al. (2018) liên kết findings/images với bridge surfaces; Lorvão Antunes et al. (2024) nối observation/inspection result với structural element và GlobalId; Quinn et al. (2020) giữ timestamp và point naming context.

**Limitation**  
Các bài chưa đồng thời formal hóa acquisition source, transformation/model version, responsible agent, review decision, quality/confidence và immutable derivation chain cho mỗi evidence item. Tuy nhiên, một phần lớn ngữ cảnh condition đã có tiền lệ.

**Required validation**  
Định nghĩa minimum provenance profile; ingest nhiều evidence cases; kiểm tra completeness/cardinality; tái dựng evidence-to-source và evidence-to-component; chứng minh thay model/version không làm mất identity; deliberate tests cho missing source, missing model version, duplicate evidence ID và mismatched component.

**Verdict:** Promising.

### 4.2 Pre-specified competency questions

**Claim**  
CQs phải được khóa trước schema và được thực thi như acceptance criteria, nhưng việc dùng pre-specified CQs không phải novelty độc lập.

**Evidence**  
Monfardini et al. (2023) xác nhận CQ được dùng để scope/evaluate ontology; Keet and Khan (2025) phân biệt scoping và validation CQ; Lorvão Antunes et al. (2024) công bố và thực thi CQs bằng SPARQL cho inspection/risk-condition.

**Limitation**  
Collection chưa cho thấy một CQ suite bao phủ đầy đủ evidence provenance, cross-system identity, action/status, reverse traceability và accountability; nhưng phương pháp CQ đã established.

**Required validation**  
Pre-register domain CQs, expected answer shape và test dataset trước implementation; map mỗi CQ tới schema elements, query và acceptance result; phân biệt CQ với low-level constraint check.

**Verdict:** Already established.

### 4.3 Integrated referential-integrity failure testing

**Claim**  
Đóng góp mạnh có thể là một battery deliberate negative tests cho toàn chuỗi external IDs/foreign keys, không chỉ IFC schema conformance.

**Evidence**  
Lee et al. (2021) kiểm tra GUID, mandatory references và inverse relationships; Stolk and McGlinn (2020) và Wang et al. (2024) kiểm tra RDF/ifcOWL constraints; Theiler and Smarsly (2018) có deliberately invalid schema-model cases; Oraskari et al. (2021) kiểm tra missing output counterpart và regression changes.

**Limitation**  
Phần lớn failures là ordinary conformance defects, không phải predefined invalid fixtures với expected failures. Trong phạm vi các tài liệu đã sàng lọc, chưa thấy kiểm thử tích hợp orphan `Sensor_ID`, orphan `BIM_GUID`, missing `Condition_Evidence_ID`, invalid Inspection-Action reference, duplicate crosswalk hoặc conflicting status transition.

**Required validation**  
Tạo controlled positive/negative fixtures; định nghĩa expected violation code/message; chạy constraints ở database và/hoặc RDF layer; báo cáo detection coverage, false passes và false failures; kiểm tra cả insert/update/delete và model-revision scenarios.

**Verdict:** Strong candidate.

### 4.4 Bidirectional round-trip traceability

**Claim**  
Forward và reverse reconstruction qua toàn chuỗi, kèm parity sau round trip, có thể là novelty defensible.

**Evidence**  
Lorvão Antunes et al. (2024) đưa AMS inspection knowledge vào BIM environment và trả GlobalId; Oraskari et al. (2021) kiểm tra selected IFC-to-LBD correspondence bằng GUID; Kim et al. (2018) truy xuất records từ IFC objects; Bellon et al. (2025) tạo và kiểm tra IFC study cases.

**Limitation**  
Trong phạm vi các tài liệu đã sàng lọc, chưa thấy chứng minh đầy đủ source evidence -> BIM component -> inspection -> action -> status và truy ngược status/action -> inspection -> evidence -> source, rồi so sánh identifier/payload parity sau export-import-reconstruction. “Bidirectional information flow” hoặc viewer retrieval không đồng nghĩa round-trip validation.

**Required validation**  
Khóa forward/reverse CQs; thực thi set-equality và uniqueness assertions; kiểm tra source-target-reconstructed-source IDs, hashes/canonical payloads và timestamps; deliberate tests cho missing, duplicate, swapped và stale identifiers; báo cáo từng hop thất bại.

**Verdict:** Strong candidate.

### 4.5 Inspection_Record-Action_Record-Status_Event chain

**Claim**  
Một event-aware, queryable chain có explicit record identities và state-transition semantics có thể là đóng góp; “inspection linked to maintenance” không mới.

**Evidence**  
Wan et al. (2019) có inspection, manager check, score, repair plan và repair-result check; Xu et al. (2022) nối defect với maintenance action; Bellon et al. (2025) tích hợp inspection, damage, maintenance service và cost; Carvalho et al. (2023) đưa responsible entity/schedule/cost vào activity sheets.

**Limitation**  
Các tiền lệ chủ yếu biểu diễn workflow/application functions hoặc maintenance entities, chưa cho thấy một common, independently queryable `Inspection_Record`-`Action_Record`-`Status_Event` chain với allowed transitions, immutable history, evidence basis và integrity constraints.

**Required validation**  
Định nghĩa record/event identities, event timestamps, actors, transition preconditions và terminal states; chạy CQs cho open/approved/rejected/completed/verified actions; test illegal transition, missing predecessor, conflicting simultaneous status, action without inspection và closure without verification.

**Verdict:** Strong candidate.

### 4.6 Accountable human-reviewed action workflow

**Claim**  
Formal accountability cho review/approval/rejection/action closure có thể là đóng góp hỗ trợ mạnh, nhưng human-in-the-loop tự nó đã established.

**Evidence**  
Sacks et al. (2018) có QC/signing; Wan et al. (2019) có manager checks; Isailović et al. (2020) yêu cầu engineering judgement; PAV và PROV cung cấp attribution/association vocabulary; Celik et al. (2023) biểu diễn responsibility/liability cho BIM data.

**Limitation**  
Các nghiên cứu chưa kết hợp role/agent identity, review rationale, approval state, authorization, timestamps, separation of duties và traceable override vào cùng evidence-to-action chain. Không có bằng chứng đủ để claim một autonomous decision workflow.

**Required validation**  
Định nghĩa role matrix và human decision events; test unauthorized approval, self-approval khi bị cấm, missing rationale, superseded review, rejected action và verified closure; chứng minh mọi action truy được tới evidence, inspector, reviewer và approver.

**Verdict:** Promising.

## 5. Closest competitors

Ký hiệu: `Yes` = được triển khai/chứng minh; `Partial` = có thành phần nhưng chưa đủ chain/validation; `No` = không thấy bằng chứng trong phần đã đọc.

| Study | Condition evidence | BIM identity | Inspection | Action/status | CQ | Constraints | Negative tests | Main missing element |
|---|---|---|---|---|---|---|---|---|
| Bellon et al. (2025) | Yes: damage/inspection representation | Yes: IFC 4.3.2.0 entities; identity governance chưa xác nhận | Yes | Partial: maintenance/cost có schema, explicit Status_Event chưa thấy | No | Partial: schema/semantic validation | No controlled fixtures | Provenance, CQ, explicit event history, accountability và round-trip integrity |
| Lorvão Antunes et al. (2024) | Yes: risk/condition observation/result | Yes: SPARQL tới IFC GlobalId | Yes | Partial: next inspection; không Action_Record chain | Yes, executed | Partial: ontology/OOPS!; SHACL chỉ đề xuất | No | Executable domain constraints, deliberate failures, action/status và mapping automation |
| Xu et al. (2022) | Yes: parametric defect geometry/context | Yes: IFC entity relations | Yes | Partial: maintenance action represented; event states chưa thấy | No | Partial: IFC/interoperability validation | No | Provenance, accountability, CQ, negative integrity tests và reverse traceability |
| Sacks et al. (2018) | Yes: ElementDefect/images/time | Partial: IFC element links; persistent GlobalId use chưa explicit | Yes, formal IDM/BPMN/MVD | Partial: alternatives/signing; repair execution/closure không demonstrated | No | Yes: mvdXML/conformance and omission checks | Partial: failed checks, không controlled battery | Explicit provenance, record/event vocabulary, action closure và identity round trip |
| Wan et al. (2019) | Yes: defect text/images/reports | Partial: component codes/tags, không GlobalId | Yes, mobile and reviewed | Yes operationally; status semantics/audit trail implicit | No | No formal constraints | No | Machine-testable schema, provenance, explicit status events, referential integrity và CQ |

## 6. Recommended deep-reading queue

### P1 — đọc ngay

1. **Bellon et al. (2025):** xác nhận entity mapping, exact IFC relationships, maintenance/action decomposition, validation cases và có/không có persistent identity, actor và status history.
2. **Lorvão Antunes et al. (2024):** trích đầy đủ ontology classes/properties, CQs/SPARQL, GlobalId path, pilot data flow và explicit limitations; đây là semantic competitor gần nhất.
3. **Sacks et al. (2018):** khóa IDM/MVD requirements, defect evidence schema, QC/signing, omission checks và ranh giới giữa conformance checking với deliberate negative testing.
4. **Xu et al. (2022):** cần lấy full text để xác nhận defect-element-root cause-maintenance action relationships, interoperability test và giới hạn provenance/status.
5. **Wan et al. (2019):** lập state diagram từ inspection project tới repair verification và xác định phần nào nằm trong database/schema thay vì chỉ UI workflow.
6. **Isailović et al. (2020):** dùng để thiết kế minimum context profile cho `Condition_Evidence` và tránh claim mới về BIM-linked condition findings.
7. **Lee et al. (2021):** chuyển GUID/reference/MVD rules thành G2 constraint catalog, đồng thời ghi rõ bài không chứng minh deliberate negative fixtures.
8. **Oraskari et al. (2021):** kiểm tra source code và sửa R1 thành exactly-one counterpart; dùng làm nền cho forward/reverse identity tests, không gọi đây là round trip đã established.

### P2 — đọc sau

1. **Hüthwohl et al. (2018):** lấy full text để so sánh exact defect/inspection attributes với proposed Condition_Evidence và Inspection_Record.
2. **Wang et al. (2024):** xác nhận coverage khi chuyển WHERE rules sang SHACL, error fixtures và khả năng tái dùng cho domain constraints.
3. **Stolk and McGlinn (2020):** tái dùng closed-world cardinality/class/value patterns; sửa metadata trước khi trích dẫn chính thức.
4. **Kim et al. (2018):** so sánh historical FM work-record ontology với Action_Record và kiểm tra hạn chế của STEP instance IDs.
5. **Theiler and Smarsly (2018):** học cách thiết kế deliberately invalid models và schema checking, không mở rộng sang damage diagnosis.
6. **Quinn et al. (2020):** rút minimum fields cho temporal/context identity và các failure modes do naming/null/lookup mappings.
7. **Ciccarese et al. (2013):** chọn PAV/PROV fields tối thiểu cho authoring, curation, derivation và version; tránh tự tạo provenance vocabulary.
8. **Keet and Khan (2025):** khóa loại CQ nào dùng cho scope, validation và relationship; tách CQ acceptance tests khỏi low-level constraints.

## 7. Recommended Paper 2 positioning

### Central claim an toàn

> Paper 2 develops and validates an implementation-neutral, identity-governed evidence-to-action information artifact that preserves the context and provenance of condition evidence; links it to IFC GlobalId-addressed components, inspection records, action records and status events; and demonstrates accountable human review through pre-specified competency questions, executable integrity constraints, deliberate failure cases, and forward/reverse traceability tests.

Central claim này chỉ defensible nếu artifact và validation được thực thi. Nếu chỉ có schema diagram, ontology hoặc prototype viewer, claim phải hạ xuống “design and feasibility demonstration”.

### Đơn vị novelty nên khóa

- **Không phải website/viewer:** UI chỉ là inspection surface để chứng minh query và traceability.
- **Không phải BIM viewer:** BIM highlighting/coloring đã có ở Lorvão Antunes et al. (2024), Wan et al. (2019) và các bridge studies.
- **Không phải ontology-only:** ontology, PROV/PAV, ifcOWL và BOT đã established; contribution phải gồm executable data/query/validation artifacts.
- **Không phải SHACL technology paper:** SHACL chỉ là một cơ chế thực thi constraints; validation contract và deliberately invalid domain fixtures mới là contribution.
- **Không phải “first” claim:** chỉ dùng “Trong phạm vi các tài liệu đã sàng lọc...” và mô tả precisely phần kết hợp/validation chưa thấy được chứng minh.

### Minimum publishable artifact

Một **Evidence-to-Action Traceability Specification** độc lập với implementation, gồm:

- canonical entities và identifiers: `Asset_ID`, `IFC_GlobalId`, `Condition_Evidence_ID`, `Inspection_Record_ID`, `Action_Record_ID`, `Status_Event_ID`, `Agent_ID`;
- explicit relationships, cardinalities, temporal rules, provenance fields và allowed status transitions;
- pre-specified CQ suite với expected answers;
- executable query set cho forward và reverse traceability;
- constraint catalog có stable violation codes;
- positive fixtures và deliberate negative fixtures cho orphan, duplicate, missing, mismatched, stale và illegal-transition cases;
- human review/accountability events cho inspect, review, approve, reject, execute và verify;
- validation report tách schema conformance, referential integrity, query adequacy, round-trip parity và workflow accountability.

### Claims phải tránh

- “Novel sensor-to-BIM integration.”
- “Novel use of IFC GlobalId.”
- “First BIM-linked inspection record.”
- “Novel use of competency questions/provenance/SHACL.”
- “Closed-loop maintenance” nếu chưa có action execution và post-action verification.
- “Bidirectional” nếu mới chỉ có read/write hoặc display ở hai systems mà chưa có forward/reverse parity tests.
- “Accountable” nếu mới chỉ có role labels, không có agent identity, review event, rationale và audit trace.
- “Autonomous decision support/action” vì human-reviewed action workflow là phạm vi được yêu cầu và collection không hỗ trợ claim autonomous maintenance.

## 8. Conclusion

1. **Hướng G2-G3 có đủ cơ sở tiếp tục không?** Có. Trong phạm vi các tài liệu đã sàng lọc, các building blocks đều có tiền lệ đủ mạnh để thiết kế artifact, và chưa thấy một study trong collection chứng minh đồng thời full evidence-to-action chain, deliberate external referential-integrity failures, forward/reverse parity và accountable human review. Điều này đủ để tiếp tục, nhưng chưa đủ để tuyên bố uniqueness ngoài collection.
2. **Khoảng trống mạnh nhất?** **Integrated referential-integrity failure testing kết hợp bidirectional traceability trên chuỗi Condition_Evidence -> BIM component -> Inspection_Record -> Action_Record -> Status_Event.** Inspection/action linkage riêng lẻ đã có; phần defensible là explicit identity governance, executable failure contract và reverse reconstruction.
3. **Claim nào phải loại bỏ?** Loại bỏ novelty claims độc lập về sensor-to-BIM, IFC GlobalId, BIM-linked inspection, maintenance action linkage, CQ, provenance, ontology, SHACL, BIM viewer và generic human-in-the-loop. Mọi absence claim phải được giới hạn bằng cụm “Trong phạm vi các tài liệu đã sàng lọc...”.
4. **Tài liệu nào phải deep-read trước?** Bellon et al. (2025), Lorvão Antunes et al. (2024), Sacks et al. (2018), Xu et al. (2022), Wan et al. (2019), Isailović et al. (2020), Lee et al. (2021) và Oraskari et al. (2021).
5. **G2 cần khóa artifact gì tiếp theo?** Khóa **Evidence-to-Action Traceability Specification v1**: canonical identifiers, schema/relationships/cardinalities, minimum provenance, role/status model, pre-specified CQs, forward/reverse query contract, executable constraints và positive/negative fixture manifest. G2 không nên khóa một UI hoặc một ontology serialization cụ thể.

**Overall verdict:** Trong phạm vi các tài liệu đã sàng lọc, G2-G3 là hướng khả thi và có khoảng trống defensible ở cấp **integrated artifact plus validation**, với điều kiện G3 thực sự chạy deliberate failure tests và chứng minh reverse traceability thay vì chỉ minh họa happy-path retrieval.
