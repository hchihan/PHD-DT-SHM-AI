# GATE 3 — SCIENTIFIC BASIS AND ACCEPTANCE PROTOCOL

**Research route:** RQ2 → WP2 → Chapter 5 → Paper 2  
**Current gate:** Gate 2  
**Next gate:** Gate 3  
**Scope:** Core Scope — Information traceability  
**Evidence type:** Information traceability  
**Bounded chain:** `Condition_Evidence → BIM-linked component → Inspection_Record`  
**Review date:** 12 August 2026

## 0. Evidence discipline used in this review

- **SOURCE-VERIFIED:** what the cited source itself demonstrates or specifies.
- **TUTOR-EXPLANATION:** interpretation used to teach the methodological meaning.
- **THESIS-APPLICATION:** a bounded design decision proposed for Paper 2; it is not attributed to the source.
- **UNKNOWN:** the available evidence is insufficient; no method, result, limitation or novelty claim is inferred.

No source is treated as a novelty claim by itself. A literature recommendation is not treated as a contribution, a prototype is not treated as scientific validation, an IFC `GlobalId` is not treated as proof of persistence across versions, a backward query is not treated as round-trip parity, and a candidate binding is not treated as a verified binding.

## 1. Authority audit and research boundary

### 1.1 Controlling documents

The governing position is consistent across the [Master Research Charter](sandbox:/workspace/scratch/eb2977115a54/project_sources/04-MASTER_RESEARCH_CHARTER.md), [Limited-FEM Charter v1.1](sandbox:/workspace/scratch/eb2977115a54/project_sources/06-MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md), [Research Architecture](sandbox:/workspace/scratch/eb2977115a54/project_sources/02-RESEARCH_ARCHITECTURE.md), and [Architecture Decision Record](sandbox:/workspace/scratch/eb2977115a54/project_sources/08-RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md): Paper 2 is an information-traceability study, not a diagnostic or commercial-software project.

The controlling route is:

`RQ2 → WP2 → Chapter 5 → Paper 2 → Gate 2 specification → Gate 3 end-to-end laboratory traceability`.

The only permitted description of FEM is: **“nominal, uncalibrated, reference-only, not used for damage diagnosis.”** It has no proof obligation in Gate 3.

### 1.2 Conflicts and resolutions

| Conflict | Resolution under the higher-authority documents |
|---|---|
| The Council review (§6) describes a traceability instance extending to action and mentions both lab and field cases. | Charter v1.1 §§8–12 separates Paper 2/G3 from Paper 3/G4. Gate 3 ends at `Inspection_Record` and is laboratory-only. Action selection and field feasibility are not Gate 3 proof obligations. |
| The Council review proposes operation-time/step-count metrics. No measurement protocol is approved. | Exclude these metrics from Gate 3 until the population, clock, task script, observer and analysis rule are frozen. No unmeasured efficiency claim is allowed. |
| The canonical identifier chain does not contain `Model_Version_ID`, while the Paper 2 outline proposes it. | Do not silently alter the locked chain. Treat model version as a mandatory provenance entity/relation for every BIM binding, subject to an ADR. It is not optional implementation trivia and is not inserted into the canonical chain without change control. |
| The outline’s result vocabulary mixes `PASS/FAIL` with `AMBIGUOUS/UNRESOLVED`. | Separate a **domain outcome** from a **test verdict**. An intentionally ambiguous fixture may have domain outcome `AMBIGUOUS` and test verdict `PASS`. |
| Pilot workflow and read-only Revit/IFC checks passed, but Gate 2 and Gate 3 completion matrices remain open. | These are instrument-readiness and design-observation evidence only. They neither lock Gate 2 nor pass Gate 3. |

## 2. Phần 1 — Bài giảng cho nghiên cứu sinh

### 2.1 Trực giác: tôi đang làm gì?

Bạn đang thiết kế và kiểm chứng một **sợi chỉ thông tin có thể kiểm toán**. Khi một `Condition_Evidence` xuất hiện, người quản lý phải chỉ ra được: bằng chứng đến từ đâu; nó liên quan tới vị trí nghiên cứu nào; vị trí đó có không, một hay nhiều BIM host candidate; ai chọn cấu kiện; binding được kiểm tra trên phiên bản mô hình nào; và hồ sơ kiểm tra nào đã được tạo. Từ một `Inspection_Record`, người kiểm toán cũng phải đi ngược lại đúng bằng chứng nguồn.

Bạn không chứng minh cấu kiện bị hỏng, mức độ hỏng, thời gian còn lại hay hành động bảo trì tối ưu. Bạn chứng minh rằng **thông tin đúng đối tượng, đúng phiên bản, đúng nguồn và đúng trách nhiệm** có thể được truy xuất và rằng hệ thống từ chối các record không hợp lệ.

### 2.2 Cơ chế nghiên cứu

| Thành phần | Định nghĩa cho Paper 2 |
|---|---|
| Đơn vị phân tích | Một **traceability instance** đã định biên: một đường đi có định danh từ `Condition_Evidence_ID`, qua quyết định chọn component và binding đã kiểm chứng trên một `Model_Version_ID`, tới ít nhất một `Inspection_Record_ID` trong fixture Gate 3. |
| Artefact | (1) constructs/vocabulary; (2) formal conceptual data model; (3) competency-question and constraint contract; (4) reference instantiation used only to exercise the contract. |
| Input | G1-admissible condition evidence; frozen lab BIM/IFC version; component-candidate set; accountable review decisions; inspection-record fixture; positive and negative fixtures; frozen question/oracle manifest. |
| Verification | Predeclared forward/backward queries; identity, reference, cardinality, provenance and staleness constraints; positive and deliberate-invalid fixtures; round-trip parity defined over a canonical comparison set; human review audit. |
| Output | Query result sets, validation reports, violation logs, decision/provenance records, version and hash manifest, round-trip comparison, and a signed Gate 3 acceptance record. |

### 2.3 Mức bảo vệ: khác “kết nối Revit với database” ở đâu?

Một integration project hỏi: “phần mềm có chuyển dữ liệu được không?” Paper 2 phải hỏi: “một lớp bài toán quản lý thông tin có thể được biểu diễn bằng artefact nào, những câu hỏi nghiệp vụ nào xác định adequacy, ràng buộc nào làm cho kết quả falsifiable, và artefact có vượt qua các trường hợp đúng lẫn cố ý sai hay không?”

**SOURCE-VERIFIED:** Hevner et al. định nghĩa DSR qua việc tạo và đánh giá artefact; artefact có thể là construct, model, method hoặc instantiation, và phải có relevance, rigorous evaluation và verifiable contribution (pp. 77–88, Tables 1–2). Peffers et al. trình bày chuỗi problem → objectives → design/development → demonstration → evaluation → communication (pp. 45–77, đặc biệt Activities 1–6). [Hevner et al. full text](https://www.uni-kassel.de/fb07/index.php?eID=dumpFile&f=4899&t=f&token=fda52302d42e5e5c05d7f89c2d578f80fedf7b28), [Peffers et al. full text](https://unhas.ac.id/rhiza/arsip/kuliah/Metode-Penelitian/REFERENCES/Design%20Science%20Research%20Methodology%202008.pdf).

**TUTOR-EXPLANATION:** chạy được một demo chỉ là demonstration. Evaluation đòi hỏi mục tiêu và oracle được định nghĩa trước, rồi kết quả quan sát được so với chúng.

**THESIS-APPLICATION — thứ tự định vị:**

1. **Primary: Design Science Research.** Artefact chính là formal traceability model và verification contract.
2. **Secondary: specification-and-verification study.** Gate 2 khóa đặc tả; Gate 3 tìm bằng chứng thực thi có thể bác bỏ artefact.
3. **Artefact-engineering method: ontology/data-model engineering.** Competency questions giới hạn phạm vi; entities, relationships, cardinalities and constraints tạo nghĩa kiểm chứng được.
4. **Evaluation strategy: bounded laboratory case-study validation.** Lab case là môi trường evaluation, không phải toàn bộ phương pháp và không cho phép suy rộng thống kê hoặc field diagnosis.

### 2.4 Vì sao thuộc Quản lý xây dựng?

Vấn đề trung tâm là quản trị asset information: thống nhất danh tính tài sản, kiểm soát phiên bản, phân công trách nhiệm, nối evidence với inspection work record và tạo audit trail cho quyết định. BIM/IFC, graph/relational storage và Revit chỉ là phương tiện. Đóng góp hướng tới tính kiểm chứng, trách nhiệm và khả năng sử dụng thông tin trong inspection-management workflow — đúng với Construction Information Management và Asset Information Management.

### 2.5 Gate 2 khác Gate 3 thế nào?

| Mốc | Ý nghĩa | Không được đánh đồng với |
|---|---|---|
| **Gate 2 — specification lock** | Entities, identifiers, cardinalities, status semantics, minimum `Inspection_Record` information requirement, CQs, expected answer shapes, constraints, fixtures, oracles và acceptance rule được duyệt, versioned và frozen. | Schema code, Revit bridge, query execution hoặc pilot PASS. |
| **Gate 3 — execution authorisation** | Người có thẩm quyền xác nhận Gate 2 baseline còn nguyên; G1 payload admissible; lab BIM/IFC version frozen; execution manifest, roles, storage and stop rules sẵn sàng. | Việc đã thực sự tạo evidence. |
| **Gate 3 — evidence execution** | Instantiation được xây đúng frozen specification; mọi mandatory CQ và fixture trong manifest được chạy; kết quả và failure được lưu. | Kết luận PASS tự động. |
| **Gate 3 — formal PASS** | Acceptance reviewer đối chiếu toàn bộ evidence bundle với frozen oracles; không còn mandatory `FAIL`, `NOT_RUN` hoặc `BLOCKED`; mọi deviation được xử lý theo change control; biên claim được ký. | Một workflow, một scenario, một query, hoặc pilot đã PASS. |

### 2.6 Vì sao chưa nên tiếp tục code?

Code trước khi khóa CQs sẽ làm cho câu hỏi nghiên cứu bị định hình bởi cấu trúc database/tool đã chọn; khi đó evaluation dễ trở thành “chứng minh phần mềm tự làm đúng điều phần mềm đã được viết để làm.” Hiện ba blocker vẫn mở: status semantics, model-version governance và minimum `Inspection_Record` information requirement. Việc code lúc này tạo rework và làm suy yếu tính predeclared/falsifiable của Gate 3.

### 2.7 Trong thời gian chờ Gate 1 có thể hoàn thành gì?

Có thể hoàn thành toàn bộ **verification contract** trên giấy: source ledger, CQs, expected answer shapes, status ADR, model-version ADR, minimum information requirement, constraint/fixture/oracle catalogue, acceptance protocol và review pack. Không instantiate schema, không chạy query, không sinh kết quả và không sửa Revit/IFC.

## 3. Phần 2 — Cross-paper evidence matrix

| Scientific proposition | Supporting source(s) | Exact locator | Strength | Limitation | Use in G2/G3 |
|---|---|---|---|---|---|
| DSR requires a purposeful artefact and rigorous evaluation, not a working demo alone. | Hevner et al. (2004); Peffers et al. (2007) | Hevner pp. 77–88, Tables 1–2; Peffers pp. 45–77, Activities 1–6 | **Strong — full text** | Neither source prescribes Paper 2’s entities or acceptance thresholds. | G2: define artefact/objectives; G3: compare observations with frozen objectives. |
| Competency questions define intended scope and evaluate whether the representation can answer required questions. | Grüninger & Fox (1995) | §§2–6: motivating scenarios, informal CQs, terminology/axioms, formal CQs and completeness | **Strong — author-hosted full text** | Does not establish “preregistration” as novelty and does not mandate a relational/graph implementation. | G2: lock CQs before implementation; G3: execute them as adequacy tests. [Paper](https://www.eil.utoronto.ca/wp-content/uploads/enterprise-modelling/papers/gruninger-ijcai95.pdf) |
| Provenance can distinguish entities, activities, agents, roles, attribution, association and revision. | W3C PROV-DM | §§2.1.1–2.1.3; §§5.2.2, 5.3.1–5.3.3 | **Strong — W3C Recommendation** | PROV does not itself define legal accountability or Paper 2’s review policy. | G2: provenance minimum; G3: actor/time/activity/plan and revision audit. [Specification](https://www.w3.org/TR/prov-dm/) |
| IFC GlobalId uniquely identifies an IFC object in an exchange context, but IFC alone does not guarantee object persistence through every authoring/export/version event. | buildingSMART IFC 4.3 `IfcGloballyUniqueId` and `IfcRoot`; Shafiq et al. (2018) | IFC §§8.21.2.2 and 5.1.3.44; Shafiq “Inconsistent version control” and “round trip” sections | **Strong for identifier semantics; medium/strong for version risk** | IFC docs define uniqueness, not cross-version persistence. `OwnerHistory` is optional and stores only last modification. | G2: require `Model_Version_ID`; G3: detect stale/cross-version bindings. [GlobalId](https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcGloballyUniqueId.htm), [IfcRoot](https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcRoot.htm), [Shafiq et al.](https://journal.hep.com.cn/fem/EN/10.15302/J-FEM-2018009) |
| BIM information validation requires explicit rule families including uniqueness, reference existence, semantic/existence and syntax checks. | Lee, Eastman & Solihin (2021); Solihin, Eastman & Lee (2015) | Lee §4.1 and §§5.1.1–5.1.4; Solihin abstract only | **Strong for Lee; abstract-bounded for Solihin** | Solihin full text was not available in this review; no method/result/limitation is inferred beyond the abstract. | G2: rule catalogue; G3: structured reports with focus record and violation. [Lee et al.](https://academic.oup.com/jcde/article/8/1/97/5898254), [Solihin et al. publisher record](https://doi.org/10.1016/j.aei.2015.07.006) |
| Cardinality constraints and machine-readable validation reports are established mechanisms. | W3C SHACL | §§3.6, 4.2.1–4.2.2 | **Strong — W3C Recommendation** | SHACL is one implementation option, not the thesis contribution or a required tool. SHACL severity is validation severity, not physical damage severity. | G2: expected violation structure and min/max constraints; G3: reproducible validation reports. [Specification](https://www.w3.org/TR/shacl/) |
| Deliberately invalid fixtures are established prior art in IFC schema verification. | Theiler & Smarsly (2018) | §4.4, pp. 20–22, Listing 3 and Table 1 | **Strong — full text** | Tests their IFC Monitor domain rules, not Paper 2’s evidence-to-inspection chain. | G2: require negative fixtures; G3: test for silent false passes. [Full text](https://www.researchgate.net/publication/324991665_IFC_Monitor_-_An_IFC_schema_extension_for_modeling_structural_health_monitoring_systems) |
| Bidirectional traceability means being able to follow linked artefacts forward and backward; it is not, by itself, round-trip preservation. | Gotel & Finkelstein (1994); Lee et al. (2021) | Gotel & Finkelstein definition, pp. 94–95; Lee §2, import/export validation discussion | **Strong for conceptual distinction** | Requirements traceability is an analogue, not direct evidence for BIM round-trip parity. Lee validates import/export requirements, not Paper 2’s parity relation. | G2: separate forward CQ, backward CQ and round-trip oracle; G3: execute all three. [Gotel & Finkelstein](https://discovery.ucl.ac.uk/749/1/2.2_rtprob.pdf), [Lee et al.](https://academic.oup.com/jcde/article/8/1/97/5898254) |
| Inspection information can be explicitly modelled and linked to BIM elements, findings, time, measurements and imagery; information requirements can be checked against an exchange specification. | Sacks et al. (2018), SeeBridge, *Automation in Construction* 90, 134–145, DOI 10.1016/j.autcon.2018.02.033 | accepted-manuscript pp. 1–2; pp. 10–12; pp. 14–17 | **Strong — peer-reviewed full text** | Bridge/defect context includes physical damage and severity that are outside this thesis. It does not define `Condition_Evidence_ID`. | G2: candidate minimum `Inspection_Record` information; G3: bounded linked record fixture without severity. [Repository record](https://www.repository.cam.ac.uk/items/e2dd3bd6-7173-4531-8d8a-e09955676d3b), [full text](https://www.repository.cam.ac.uk/bitstreams/c300f6df-1f3a-4139-b521-ac745b678ee3/download) |
| A physical or functional location may relate to several model elements or findings/inspections over time; cardinality must be explicit. | Sacks et al.; Theiler & Smarsly | SeeBridge pp. 14–16; IFC Monitor §§4.2–5.2 | **Moderate** | Neither source establishes Paper 2’s exact physical research location → BIM-host 0/1/N mapping. | G2: model 0/1/N explicitly; G3: include zero, one and many candidate cases. |
| BIM/asset-management ontologies and IFC inspection/maintenance frameworks exist close to the intended contribution. | Lorvão Antunes et al. (2024); Bellon et al. (2025) | Publisher/DOI metadata and abstracts only in this review | **UNKNOWN for method, schema, evaluation and limitations** | Full text was not available; cannot use to prove gap, novelty or minimum fields. | Required competitor audit before a strong novelty claim. [Antunes et al.](https://doi.org/10.1016/j.iswa.2024.200366), [Bellon et al.](https://doi.org/10.1016/j.autcon.2025.106157) |

## 4. Source-by-source audit of the eight pillars

### Pillar 1 — DSR and artefact evaluation

- **SOURCE-VERIFIED:** Hevner allows construct/model/method/instantiation artefacts and multiple evaluation methods; Peffers separates demonstration from evaluation.
- **TUTOR-EXPLANATION:** the database/Revit implementation is an instantiation; the scientific contribution must be visible in the constructs, formal model and evaluation contract.
- **THESIS-APPLICATION:** use DSR as the primary paradigm and specification-and-verification as the study logic.
- **UNKNOWN:** the present corpus does not prove the proposed artefact is novel.

### Pillar 2 — Competency questions

- **SOURCE-VERIFIED:** Grüninger & Fox use motivating scenarios and informal/formal CQs to characterize scope and evaluate ontological commitments.
- **TUTOR-EXPLANATION:** a CQ is a requirement and a falsifiable test target, not simply an example query written after the schema exists.
- **THESIS-APPLICATION:** freeze the question, answer shape and oracle before schema implementation.
- **UNKNOWN:** “pre-registration” as a distinct scientific contribution is not established by this source.

### Pillar 3 — Provenance and accountability

- **SOURCE-VERIFIED:** PROV-DM represents responsibility through agent/entity attribution, agent/activity association, role, plan and revision relations.
- **TUTOR-EXPLANATION:** provenance makes a decision auditable; it does not make it correct merely because a name is attached.
- **THESIS-APPLICATION:** every selection, acceptance, rejection and verification activity needs actor, role, time, object, model version, rationale/plan locator and record ID.
- **UNKNOWN:** PROV-DM does not determine who has contractual authority to approve Gate 3.

### Pillar 4 — BIM/IFC identity and model version

- **SOURCE-VERIFIED:** IFC `GlobalId` is a required 22-character encoded unique ID for IFC objects; `OwnerHistory` is optional and only stores last modification. Shafiq et al. report that GUID-only version comparison can be unreliable in practical authoring exchanges and that round tripping can change instances.
- **TUTOR-EXPLANATION:** `BIM_GUID` answers “which IFC object in this declared model context?” It does not answer “is this still the same physical component in every later export?”
- **THESIS-APPLICATION:** make model version a first-class provenance entity referenced by each binding.
- **UNKNOWN:** no source mandates the exact name `Model_Version_ID` or the thesis-specific hash policy.

### Pillar 5 — Rule-based validation

- **SOURCE-VERIFIED:** Lee et al. define uniqueness, reference existence, semantic accuracy/existence and syntax rule types; SHACL specifies min/max counts and structured validation results; Theiler & Smarsly execute both correct and purposefully incorrect test models.
- **TUTOR-EXPLANATION:** constraints turn the artefact from a diagram into something that can fail.
- **THESIS-APPLICATION:** define tool-independent constraint semantics; SHACL/SQL/SPARQL may implement them later.
- **UNKNOWN:** no evidence yet shows one implementation language is superior for this thesis.

### Pillar 6 — Bidirectional and round-trip traceability

- **SOURCE-VERIFIED:** bidirectional traceability supports following linked artefacts forward and backward. BIM literature separately identifies import/export translation and round-trip/version-change problems.
- **TUTOR-EXPLANATION:** two successful lookup queries do not prove that an export/import or materialize/reconstruct cycle preserved the same canonical identities and relationships.
- **THESIS-APPLICATION:** define three obligations: forward reachability, backward reachability, and round-trip equality over a frozen canonical comparison set.
- **UNKNOWN:** a universal round-trip equality criterion across all BIM tools is not established and is outside scope.

### Pillar 7 — BIM-linked inspection records

- **SOURCE-VERIFIED:** SeeBridge formalizes inspection-related information, element findings, time, measurements and imagery, and checks IFC instances against information requirements.
- **TUTOR-EXPLANATION:** an inspection record is an accountable event record, not merely a hyperlink to an image.
- **THESIS-APPLICATION:** use only fields required for evidence-to-inspection traceability; exclude severity, diagnosis and maintenance optimization.
- **UNKNOWN:** Bellon et al. could be the closest competitor, but its unavailable full text prevents schema and novelty comparison.

### Pillar 8 — Physical-location/BIM-object cardinality

- **SOURCE-VERIFIED:** inspection/BIM literature allows multiple findings and inspections associated with elements, and IFC relationship structures are not inherently one-to-one.
- **TUTOR-EXPLANATION:** a research location such as a joint or braced bay can be a physical/functional region whose correct BIM representation is zero, one or several objects.
- **THESIS-APPLICATION:** cardinality is an observed design requirement and must be tested explicitly.
- **UNKNOWN:** **Evidence is currently insufficient** to claim that the exact lab research-location → 0/1/N BIM-host problem is an established literature gap. Keep it as a `candidate gap`.

## 5. Phần 3 — Novelty boundary

| Proposed claim | Classification | Evidence and reasoning | Defensible wording |
|---|---|---|---|
| Sensor/condition data can be linked to BIM/IFC objects. | **Established prior art / reject as novelty** | IFC Monitor and many BIM-SHM studies already do this. | Context only. |
| BIM-linked inspection/maintenance information. | **Established prior art / reject as novelty** | SeeBridge establishes BIM-linked inspection information; Bellon 2025 is a close competitor pending full-text audit. | Context only. |
| Competency questions, formal constraints and validation reports. | **Established prior art / reject as novelty** | Grüninger & Fox, Lee et al. and SHACL. | Methodological foundation. |
| Deliberate invalid fixtures. | **Established prior art / reject as novelty** | Theiler & Smarsly §4.4 deliberately violate rules and check the expected false/error result. | Supporting evaluation element. |
| Forward and backward queries. | **Established prior art / reject as novelty in isolation** | Bidirectional traceability is long-established. | Supporting evaluation element. |
| Preregistered forward/backward questions with frozen answer shapes and oracles. | **Supporting element; possible methodological contribution, not core novelty** | CQ and bidirectionality are prior art. The temporal governance/frozen oracle strengthens falsifiability but the current corpus does not establish novelty. | “A predeclared verification contract used to evaluate the artefact.” |
| Accountable human review. | **Established concept / supporting element; reject as novelty in general** | PROV formalizes agents/roles/responsibility; inspection workflows already involve engineers. | “Human review is made auditable within the trace model.” |
| Candidate versus human-accepted versus verified binding. | **Strong candidate contribution as part of the integrated artefact** | The exact state separation is not established by the verified corpus, but candidate matching and human review separately exist. | “An explicit, version-aware binding lifecycle separating algorithmic candidature, human acceptance and constraint-based verification.” |
| Cardinality-aware binding. | **Established in general; candidate contribution only in the thesis-specific formulation** | General 0/1/N relationships are prior art. Exact physical research-location → BIM-host candidate cardinality remains insufficiently screened. | “A cardinality-explicit binding contract for the bounded laboratory mapping problem.” |
| Integrated `Condition_Evidence → component → Inspection_Record` chain with identity, version, provenance, two decisions and invalid-fixture evaluation. | **Strong candidate contribution** | Each ingredient has prior art; no verified source in the reviewed corpus demonstrates the same bounded combination and proof contract. | “A candidate novel configuration of established elements,” pending full competitor audit. |
| The integrated chain is definitely absent from prior research. | **Evidence currently insufficient** | Bellon 2025 and Antunes 2024 were not deep-read from full text; one paper cannot establish a gap. | Keep as `candidate gap`; do not claim absence. |
| Revit/database/IFC bridge or chosen software stack. | **Reject as novelty** | It is an instrument/instantiation. | Report reproducibility and limitations only. |

## 6. Review of the three conceptual blockers

### 6.1 Blocker 1 — one status enumeration conflates two decisions

**Claim:** the current single status list is semantically unsafe because it mixes selection of a research component with verification of a model binding.

**Evidence:** PROV-DM distinguishes activities, agents and roles; the pilot itself observed two separate decisions. No verified source prescribes the exact enums.

**Limitation:** status names and transitions are thesis design choices and require Gate 2 approval.

**Next action:** approve two orthogonal states and a separate derived trace-completeness outcome:

| State family | Candidate controlled vocabulary | Meaning |
|---|---|---|
| `Selection_Status` | `UNASSESSED`, `NO_CANDIDATE`, `AMBIGUOUS`, `SELECTED`, `REJECTED` | Decision A: whether and which candidate component is selected for the research location. |
| `Binding_Status` | `NOT_CHECKED`, `CANDIDATE`, `HUMAN_ACCEPTED`, `VERIFIED`, `REJECTED`, `STALE` | Decision B: confidence/governance state of the binding in one declared model version. `VERIFIED` means identity/version/constraints plus accountable review; it never means physical condition verified. |
| Derived trace outcome | `COMPLETE`, `PARTIAL`, `BROKEN` | Computed from required nodes/links; not used to encode either human decision. |

Allowed transitions and actor requirements must be frozen. In particular, `CANDIDATE → VERIFIED` must not bypass an accountable acceptance activity; any model revision invalidating the target produces `STALE`, not silent persistence.

### 6.2 Blocker 2 — `Model_Version_ID`

**Claim:** model version is necessary for provenance and staleness checking.

**Evidence:** IFC GlobalId guarantees identifier semantics within an IFC object context; `OwnerHistory` is optional and last-change-only. BIM versioning literature records cross-version GUID and round-trip problems.

**Limitation:** the sources do not mandate the exact thesis implementation.

**Next action:** approve `Model_Version` as a **mandatory logical entity and mandatory foreign reference on every component binding and query execution**. Minimum information requirement: `Model_Version_ID`, model/document identifier, version/revision label, IFC schema/MVD, export/freeze time, content hash or immutable locator, authoring/export application where relevant, and optional `wasRevisionOf` link. Do not insert it into the locked canonical identifier chain without a formal ADR. It is therefore **mandatory provenance, implemented as a first-class entity**, not optional implementation metadata.

### 6.3 Blocker 3 — minimum `Inspection_Record` information

The following is a **candidate minimum information requirement for Gate 2 approval, not an implemented schema**.

| Information group | Minimum field/relationship | Cardinality for general record | Gate 3 inclusion rule | Scientific basis |
|---|---|---:|---|---|
| Identity | `Inspection_Record_ID` | exactly 1, unique | exactly 1 | Identifier integrity requirement; thesis-specific name. |
| Inspected target | component binding (`BIM_GUID` + `Model_Version_ID`) | exactly 1 primary target in bounded Paper 2 design | exactly 1 verified binding | IFC identity plus version-control evidence. |
| Evidence trigger | link to `Condition_Evidence_ID` with link role/rationale | 0..N | at least 1 | Thesis-specific link; routine inspections may exist without condition evidence, but a Gate 3 traceability instance may not. |
| Inspection event | performed/observed time; scope/method | exactly 1 event | present | SeeBridge inspection/finding at a point in time. |
| Accountable actor | inspector/creator `Agent_ID`, role | at least 1 | present | PROV-DM agent/activity/role. |
| Finding | controlled outcome plus narrative | exactly 1 outcome; narrative conditional | present | SeeBridge findings; thesis outcome excludes damage severity. Suggested outcomes: `NO_FINDING`, `FINDING_RECORDED`, `INCONCLUSIVE`, `NOT_INSPECTED`. |
| Location/context | component-local or textual location | 0..1 or conditional | required when finding location matters | SeeBridge element/finding location. |
| Attachment | attachment locator + media type + hash | 0..N | at least one positive fixture with attachment and one valid no-attachment fixture | SeeBridge imagery; hash policy is thesis governance. |
| Record provenance | created time, creator, source activity, schema/spec version, revision relation | exactly 1 provenance bundle | present | PROV-DM. |
| Review state | reviewer, review time, decision and rationale locator | required before accepted/verified use | present for accepted Gate 3 record | Accountability contract. |

Recommended evidence/inspection cardinality is many-to-many over time: one condition evidence item may lead to zero or several inspections; one inspection may consider zero or several evidence items. Use an explicit link relation. For Gate 3’s included traceability instances, require `Inspection_Record → Condition_Evidence` cardinality `1..N`. This is a bounded thesis design decision; the literature does not dictate it.

## 7. Phần 4 — Gate 3 Scientific Basis and Acceptance Protocol

### 7.1 Objective and unit of analysis

**Objective:** demonstrate, in the bounded laboratory case and against a frozen verification contract, that an admissible `Condition_Evidence` can be traced to the correct versioned BIM component binding and linked `Inspection_Record`, and that the same chain can be reconstructed backward while invalid, ambiguous, conflicting and stale records are detected rather than silently accepted.

**Unit:** one traceability instance plus the execution records of all questions and constraints applied to it. The sample is the complete enumerated fixture manifest, not an unspecified convenience sample.

### 7.2 Mandatory inputs before evidence execution

1. Signed Gate 2 baseline and change-control identifier.
2. G1-admissible payload with evidence/run/sensor provenance.
3. Frozen laboratory authoring model and IFC export, each with `Model_Version_ID`, immutable locator and hash.
4. Frozen component-candidate manifest covering 0, 1 and N candidate cases.
5. Approved two-status lifecycle and accountable-review rule.
6. Approved candidate minimum `Inspection_Record` information requirement.
7. Frozen competency-question register, expected answer shapes and oracles.
8. Frozen positive/negative fixture manifest and expected domain outcomes.
9. Execution roles, reviewer independence/authority, environment/tool version manifest and stop rules.
10. Evidence repository layout and immutable record policy.

Missing any mandatory input yields `BLOCKED`; it is not converted into a “partial PASS.”

### 7.3 Minimum competency questions

| ID | Question | Expected answer shape | Proof obligation |
|---|---|---|---|
| CQ-F01 | Given `Condition_Evidence_ID`, what source run/sensor, research component, candidate set, selected component, binding status, `BIM_GUID`, `Model_Version_ID` and inspection records are linked? | One subject; ordered path nodes; candidate count/list; decision records; zero-or-more IR IDs; provenance locators; domain outcome | Forward traceability and completeness. |
| CQ-B01 | Given `Inspection_Record_ID`, which evidence, source run/sensor and versioned component binding justify it? | One IR; one primary target; one-or-more CE IDs for Gate 3; ordered provenance path | Backward traceability. |
| CQ-I01 | Are all identifiers non-null, correctly typed and unique within their declared scope? | Entity type, scope, duplicate/missing list | Entity/identifier integrity. |
| CQ-C01 | For a research location, are there zero, one or many BIM host candidates, and is the candidate count consistent with the list? | Integer count, candidate ID set, model version, domain outcome | 0/1/N cardinality. |
| CQ-C02 | Is there at most one selected primary host for a location and model version unless an approved composite-binding construct is used? | Selection set and decision provenance | Ambiguity/conflict control. |
| CQ-S01 | Are `Selection_Status` and `Binding_Status` semantically and transitionally valid? | Current states, prior state, transition, actor/time, violation if any | Candidate ≠ accepted ≠ verified. |
| CQ-P01 | Who performed, reviewed and approved each selection/binding/inspection activity, when, in what role and under what plan/specification? | Entity–activity–agent path with time/role/plan locator | Provenance and accountability. |
| CQ-V01 | Does every binding point to an existing object in the declared frozen model version? | GUID, version, lookup result, hash/locator | Component identity and reference integrity. |
| CQ-V02 | Has a model revision made a previously accepted binding stale? | prior/current model versions, revision relation, comparison and domain outcome | Version/staleness control. |
| CQ-R01 | Do forward and backward query paths return mutually consistent canonical identifiers and relationships? | Canonical set comparison and difference set | Bidirectional parity, not yet round-trip. |
| CQ-RT01 | After the declared serialization/export/import or reconstruction cycle, is the canonical comparison set unchanged, except predeclared allowed differences? | Before/after canonical sets, allowed-difference list, unexpected difference set | Round-trip parity. |
| CQ-IR01 | Does each included inspection record satisfy the approved minimum information requirement and link to the versioned component and at least one condition evidence item? | Field/relation presence and constraint results | `Inspection_Record` adequacy. |
| CQ-N01 | Does each deliberate-invalid fixture produce the exact expected violation and avoid creation of a verified binding/accepted record? | Fixture ID, expected/actual domain outcome, violation code, test verdict | Missing/duplicate/orphan/ambiguous/conflicting/stale detection. |

An expected answer shape is a logical contract, not a database schema. Field names can be refined at Gate 2, but subject, path, version, decision, provenance, domain outcome and violation information must remain testable.

### 7.4 Constraint families and fixtures

| Constraint family | Positive fixture | Negative fixture | Acceptance oracle |
|---|---|---|---|
| Required entity/identifier | Complete unique chain | missing CE/IR/GUID; malformed ID | exact missing/malformed violation; no silent repair |
| Uniqueness | unique IDs in frozen scope | duplicate CE, IR or binding ID | exact duplicate set reported |
| Referential integrity | all references resolve | orphan evidence, component, version, attachment or review | unresolved reference and focus record reported |
| Component identity | GUID exists in declared version | GUID from another/nonexistent version | binding not verified |
| 0/1/N cardinality | valid `NO_CANDIDATE`; valid 1:1; valid N-candidate ambiguous case | N candidates marked selected/verified without adjudication; two primary selections | expected domain outcome and constraint result |
| Status/transition | valid staged transition | candidate jumps to verified; stale binding remains verified; conflicting statuses | invalid transition reported |
| Provenance/accountability | actor/time/role/activity/plan present | missing reviewer, time, role or decision rationale locator | record cannot attain required accepted/verified state |
| Model version/staleness | binding and query use frozen version | model hash/revision changed or mixed-version path | `STALE` or violation, never silent persistence |
| Inspection record | minimum information present | missing event time, target, actor, finding or provenance | record excluded from complete trace instance |
| Bidirectional consistency | forward/backward canonical sets agree | reverse link absent or wrong source | non-empty difference set causes FAIL |
| Round-trip parity | canonical set preserved | dropped/changed identifier, link, status or version | unexpected before/after difference causes FAIL |
| Attachment integrity | valid locator/hash or valid optional absence | broken locator/hash mismatch | exact attachment violation |

### 7.5 Two vocabularies that must not be conflated

**Domain outcome:** `RESOLVED`, `NO_CANDIDATE`, `AMBIGUOUS`, `REJECTED`, `STALE`, `INCOMPLETE`.

**Test verdict:** `PASS`, `FAIL`, `NOT_RUN`, `BLOCKED`.

Example: a many-candidate fixture that correctly refuses automatic selection has domain outcome `AMBIGUOUS` and test verdict `PASS`. An ambiguous fixture that is silently labelled `VERIFIED` has test verdict `FAIL`.

### 7.6 Acceptance criteria for formal Gate 3 PASS

Formal PASS may be declared only when all of the following binary conditions are met against the frozen manifest:

1. Every mandatory CQ has been executed for every fixture to which it applies; none is `NOT_RUN` or `BLOCKED`.
2. Every positive fixture matches its complete expected answer set and constraint oracle.
3. Every negative fixture produces its predeclared domain outcome/violation and none is silently accepted as verified/complete.
4. Every binding uses an existing component in exactly one declared model version; stale or mixed-version paths are rejected.
5. Every human-dependent selection, acceptance, rejection and review is attributable to an identified actor, role, activity and time, with a rationale/plan locator.
6. Forward and backward canonical identity/link sets match the preregistered parity rule.
7. Round-trip comparison yields no unexpected difference in the frozen canonical comparison set. Allowed representational differences must have been declared before execution.
8. Every included `Inspection_Record` satisfies the approved minimum information requirement and is linked to at least one condition evidence item and one verified versioned component binding.
9. Rerunning the frozen protocol on the same frozen inputs yields the same canonical answer and violation sets.
10. The evidence bundle contains the protocol baseline, input/output hashes, model/tool versions, query/constraint versions, raw reports, decision logs, deviation log and signed acceptance record.

No performance, time-saving, accuracy-rate or generalizability metric is claimed unless its own measurement protocol has first been approved.

### 7.7 Mandatory evidence artefacts

- Gate 2 signed baseline and change log.
- CQ/oracle register and applicability matrix.
- Positive/negative fixture manifest.
- Input manifest: G1 payload IDs; BIM/IFC versions and hashes; inspection fixtures.
- Entity/link export or equivalent immutable snapshot.
- Raw forward/backward query outputs.
- Constraint/validation reports with focus records and violation codes.
- Before/after round-trip canonical sets and difference report.
- Selection/binding/inspection human-review records.
- Execution log, environment/tool manifest and deterministic rerun report.
- Deviation/exception register, including failures.
- Signed Gate 3 acceptance sheet with bounded claims.

### 7.8 Immediate FAIL conditions

- Any missing, duplicate or orphan mandatory identifier is silently accepted.
- A component binding lacks model version, references a nonexistent object, mixes versions, or remains `VERIFIED` after staleness is detected.
- Candidate, human-accepted and verified states cannot be distinguished.
- An ambiguous or conflicting case is auto-resolved without accountable review.
- Forward/backward canonical sets disagree without a predeclared explanation.
- Round-trip comparison is not run or compares only screenshots/visual similarity.
- An included inspection record lacks mandatory target, evidence link, actor, time, finding outcome or provenance.
- A negative fixture fails to trigger its expected violation or produces a silent false pass.
- Any mandatory test is `NOT_RUN`/`BLOCKED`, or the executed protocol differs from the frozen baseline without approved change control.
- A claim crosses into field diagnosis, severity, RUL, predictive maintenance, calibrated FEM, automated maintenance or commercial-product validation.

### 7.9 Conditions under which PASS must not be claimed

- Revit/database connectivity works.
- A pilot workflow or read-only lookup passes.
- Only forward or only backward retrieval works.
- Human acceptance exists but constraint/version verification is absent.
- A single happy-path trace instance works.
- Negative fixtures were not preregistered and executed.
- `GlobalId` is present but `Model_Version_ID` and staleness checks are absent.
- Results were manually repaired after execution without an auditable deviation record.
- The G1 evidence payload is provisional or inadmissible.

## 8. Paper 2 outline review — Claim → Evidence → Limitation → Next action

| Claim | Evidence | Limitation | Next action |
|---|---|---|---|
| Paper 2 is a publishable traceability study rather than system integration. | DSR and CQ literature; Charter/ADR; outline §§1, 6–15. | Contribution still framed partly as a bundle of implementation features; closest competitors are not fully audited. | Rewrite method and contribution around artefact + frozen verification contract; keep implementation as instrument. |
| Current pilot establishes cardinality and two human decisions as design observations. | Frozen pilot records summarized in outline §§15–16. | Candidate data only; 0 verified full chains; no G1 payload or approved IR schema. | Use observations to refine CQs/status ADR, not as Gate 3 result. |
| Two independent statuses are needed. | Pilot decisions A/B; provenance distinction. | Exact state machine has no approval. | Approve status ADR before schema. |
| `Model_Version_ID` is mandatory. | IFC and BIM versioning evidence. | Conflicts with locked-chain wording if silently inserted. | Approve model-version ADR; make it mandatory provenance entity/relation. |
| `Inspection_Record` needs a minimum schema. | SeeBridge + PROV provide a defensible information basis. | Bellon full text unavailable; exact CE↔IR relation is thesis-specific. | Approve minimum information requirement and cardinality at Gate 2; do not implement yet. |
| Negative fixtures strengthen Gate 3. | Theiler & Smarsly; SHACL/Lee. | Not novel alone. | Use as evaluation requirement and test silent false passes. |
| Current result vocabulary is adequate. | None. | Conflates domain outcome with test verdict. | Split the two vocabularies before freezing protocol. |
| The exact integrated chain is novel. | No verified paper in current full-text corpus shows the complete combination. | Absence not proven; Bellon/Antunes incomplete. | Keep `candidate gap`; perform two-source independent full-text competitor audit. |

## 9. Phần 5 — Plan while waiting for Gate 1

### 9.1 DO NOW — independent of Gate 1

| Work item | Deliverable | Acceptance criterion |
|---|---|---|
| Freeze source authority and evidence ledger | Versioned source ledger with `SOURCE-VERIFIED/TUTOR/THESIS/UNKNOWN`, DOI/URL and exact locator | Every protocol proposition has at least one primary source or is labelled thesis design/UNKNOWN; no abstract-derived method claim. |
| Draft CQ register | CQ IDs, wording, scope, expected answer shape, applicability and oracle | Covers all proof obligations and is independently reviewable without a schema. |
| Resolve status blocker | ADR for `Selection_Status`, `Binding_Status`, transitions and actor requirements | Decisions A/B are non-overlapping; candidate cannot equal verified; stale transition specified. |
| Resolve model-version blocker | ADR for `Model_Version` role and minimum information | Every binding/query is version-scoped; locked canonical chain remains unchanged unless formally amended. |
| Resolve `Inspection_Record` blocker | Minimum information requirement and cardinality note | Required/optional fields, general vs Gate 3 cardinality, actor/time/finding/attachment/provenance approved; no severity field. |
| Freeze outcome semantics | Domain-outcome and test-verdict vocabulary | Ambiguous fixture can PASS only when ambiguity is the oracle; no mixed meanings. |
| Draft constraint catalogue | Constraint IDs, focus entities, violation codes | Missing, duplicate, orphan, ambiguous, conflicting and stale cases all have deterministic oracles. |
| Draft fixture manifest | Positive and negative fixture descriptions; no fabricated execution results | Includes valid 0/1/N cases and all required invalid families; expected results only, clearly labelled as oracles. |
| Draft acceptance and evidence protocol | Signed-review-ready Gate 3 protocol | Distinguishes specification, authorisation, execution and PASS; contains stop/FAIL rules and evidence bundle list. |
| Independent expert review pack | One bounded review form | Reviewer must approve/reject every CQ, cardinality, status, IR requirement, round-trip definition and PASS rule. |

### 9.2 PREPARE BUT DO NOT EXECUTE

| Work item | Deliverable | Acceptance criterion |
|---|---|---|
| Execution manifest template | Empty manifest for inputs, versions, hashes, roles and run IDs | Contains no invented payload/results; all mandatory slots and stop rules visible. |
| Tool-independent query mapping | Mapping from each approved CQ to logical entities/relations | No SQL/SPARQL/Revit code; one-to-one coverage from CQ to proof obligation. |
| Canonical comparison-set specification | List of identities, links, statuses, versions and provenance fields used for parity | Allowed representational differences are explicit and reviewable before execution. |
| Evidence-bundle index template | Empty index for raw outputs, logs, decisions and signatures | Every acceptance criterion maps to a future artefact locator. |
| Change-control form | Baseline/deviation/reapproval template | Any post-freeze change invalidates prior authorisation until reviewed. |
| Reviewer calibration example | Paper-only examples of domain outcome versus test verdict | Reviewers agree on expected classification; no claimed empirical result. |

### 9.3 WAIT FOR GATE 1

| Work item | Deliverable after unblock | Acceptance criterion |
|---|---|---|
| Admit the real G1 payload | Signed G1 payload manifest | Run registry, LORO and sensor mode satisfy G1; provenance complete. |
| Authorise Gate 3 evidence execution | Formal authorisation record | Gate 2 baseline frozen, G1 payload admissible, model/fixtures frozen, roles assigned. |
| Implement schema/constraints/queries | Reference instantiation | Implements the approved contract exactly; no unapproved fields/semantics. |
| Perform Revit/IFC/database operations | Instrument execution log | Uses frozen versions and records every transform; no field/diagnostic extension. |
| Execute all fixtures and CQs | Raw evidence bundle | No mandatory `NOT_RUN`/`BLOCKED`; failures preserved, not repaired silently. |
| Conduct formal acceptance review | Gate 3 decision record | Apply §7.6 criteria; only the authorised reviewer can declare formal PASS. |

## 10. Three most important missing evidence items

1. **Closest-competitor full-text audit:** Bellon et al. (2025) and at least one independent inspection/asset-ontology study must be compared at method, schema, cardinality, validation and limitation level. Until then, the integrated novelty statement remains a `candidate gap`.
2. **Approved minimum `Inspection_Record` information requirement:** the proposed fields and CE↔IR cardinalities need supervisor/domain-expert approval and a signed Gate 2 baseline.
3. **Approved Gate 2 verification contract:** competency questions, expected answer shapes, two-status lifecycle, model-version ADR, fixtures, oracles and acceptance criteria are not yet formally approved.

## 11. Highest-priority next action

Convene a **Gate 2 specification review** whose sole output is approval or rejection of: (1) the CQ/oracle register; (2) the two-status ADR; (3) the model-version ADR; and (4) the `Inspection_Record` minimum information requirement. Do not implement schema or touch Revit/IFC until that review is signed.

## 12. Teach-back question

Nếu một fixture có ba BIM host candidates và hệ thống trả về `AMBIGUOUS`, trong điều kiện nào test đó được đánh giá `PASS`, và tại sao kết quả ấy vẫn chưa tạo ra một `VERIFIED binding` hay Gate 3 PASS?

## VERDICT

**READY WITH CONDITIONS**

The scientific basis is sufficient to freeze a Gate 3 protocol **after** the three missing evidence items above are resolved. It is not sufficient to authorise evidence execution, declare Gate 3 PASS, or make a definitive novelty claim now.
