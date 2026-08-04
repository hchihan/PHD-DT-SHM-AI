# G2-G3 Round 1 Deep Read and Novelty Boundary

Corpus khóa cứng: đúng bốn items trong Zotero collection `RQ2_RQ3_CORE_DEEP_READ_20260803` (`C9J2V33M`). Không sử dụng tài liệu ngoài bốn bài và không thực hiện Zotero writeback.

Quy ước bằng chứng:

- `PDF p.` là số trang của file PDF; khi hữu ích, số trang in của proceedings/journal được ghi trong ngoặc.
- Bellon et al. (2025) chỉ có publisher HTML bị paywall trong Zotero. Vị trí bằng chứng của bài này được ghi theo section/snippet; không có page, table hoặc figure khả kiểm từ attachment hiện tại.
- `Yes` chỉ dùng khi bài mô tả hoặc thực thi rõ; future work không được tính là `Yes`.
- Deliberate negative test yêu cầu đủ bốn điều kiện: intentionally invalid fixture, predefined expected failure, execution, và actual-versus-expected comparison.
- Mọi diễn giải novelty trong báo cáo này dùng phạm vi: **Trong phạm vi bốn tài liệu đã deep-read...**

## 1. Executive summary

- **Đối thủ gần nhất về schema/workflow:** Bellon et al. (2025) bao phủ inspection data, damage reports, proposed maintenance services và costs trong một IFC workflow; Methodology snippet mô tả framework inspection-maintenance, còn Highlights và Framework application snippet nói đã implementation và đánh giá bằng hai applications. Tuy nhiên, full text bị paywall nên exact entities, relationships, identifiers và validation outputs không kiểm chứng được. **Evidence is currently insufficient** cho comparison ở mức field/entity.
- **Đối thủ gần nhất về semantic linkage/CQ:** Lorvão Antunes et al. (2024) đã biểu diễn `Inspection` như `Procedure`, condition result như `Observation/Result`, nối structural element tới IFC GlobalId, công bố CQ8-CQ10 và thực thi `GetInspectionResult` để trả condition indicator cùng GUID cho BIM display (PDF pp. 6-10, Table 2, Fig. 4-5, Listings 3-5, Fig. 9-10).
- **Validation đã có:** Lee et al. (2021) đã thực thi IFC/MVD rules cho GUID length/uniqueness, references/inverse references, requiredness, datatype, values, cardinality và syntax (PDF pp. 5, 7-14, §§4.1, 5.1-5.2, Figs. 9-17). Oraskari et al. (2021) đã thực thi SHACL-SPARQL feasibility/unit checks cho IFC/ifcOWL-to-LBD correspondence, selected relations, change detection và RDF view construction (PDF pp. 4-9 [696-701], §§3-5, Listings 1-6).
- **Negative testing chưa được xác lập:** Lee có actual PASS/FAIL conformance defects nhưng không có predefined invalid-fixture manifest hoặc actual-versus-expected comparison (PDF pp. 6, 10-14, §4.2, Figs. 9-17). Oraskari báo warning khi triple set thay đổi nhưng không mô tả deliberately corrupted fixture hay expected violation (PDF p. 6 [698], §3.2, Listing 3). Antunes chỉ có OOPS! pitfall scan, không có intentionally invalid records (PDF p. 9, §6.2).
- **Forward/reverse:** Antunes chứng minh forward subchain từ inspection tới condition result, element, GUID và BIM display (PDF pp. 9-10, Listing 5, §§7.2-7.3), nhưng không có reverse query. Oraskari kiểm tra source IFC/ifcOWL -> LBD và tạo LBD -> restricted RDF view, nhưng không chạy LBD -> IFC hoặc source -> target -> source parity (PDF pp. 4-9 [696-701], §§3-5).
- **Khoảng trống mạnh nhất:** integrated referential-integrity failure testing kết hợp forward/reverse parity cho toàn chuỗi `Condition_Evidence -> BIM component -> Inspection_Record -> Action_Record -> Status_Event`.
- **Hướng G2:** phát triển một implementation-neutral Evidence-to-Action Traceability Specification, khóa identifiers, entities, provenance, status transitions, CQs, constraints, positive/negative fixtures và query contract; chưa chọn SHACL là công nghệ bắt buộc và chưa tuyên bố G2/G3 đạt.

## 2. Evidence extraction theo từng bài

### 2.1 Bellon et al. (2025)

#### Citation và vai trò

- **Citation:** Bellon, F. G., Martins, A. C. P., Franco de Carvalho, J. M., de Souza, C. A. F., Ribeiro, J. C. L., César Júnior, K. M. L., & de Oliveira, D. S. (2025). IFC framework for inspection and maintenance representation in facility management. *Automation in Construction, 174*, 106157. https://doi.org/10.1016/j.autcon.2025.106157
- **Zotero key:** `NUTL57KJ`
- **DOI:** `10.1016/j.autcon.2025.106157`
- **Academic role:** closest schema/workflow competitor ở mức broad IFC inspection-maintenance framework.
- **Relevance to G2/G3:** trực tiếp đe dọa claim về việc tích hợp inspection, damage, maintenance và cost trong IFC; attachment hiện tại không đủ để xác nhận identifier governance, record/event schema hoặc test coverage.
- **Full-text status:** chỉ có ScienceDirect HTML preview. Complete Methodology, Framework application, Discussion, Conclusion, figures và tables bị paywall. **Evidence is currently insufficient.**

#### Claim → Evidence → Limitation → Thesis implication

| Claim được bài chứng minh | Evidence page/section | Validation used | Limitation | Implication for thesis |
|---|---|---|---|---|
| Methodology bao phủ inspection data, damage reports, proposed maintenance services và costs trong IFC workflow | Accessible **Introduction**, hai đoạn cuối trước paywall | Conceptual methodology statement | Không thấy exact IFC entities, attributes, relationships hoặc identifiers | Paper 2 không được claim broad inspection-maintenance integration là novelty; phải chỉ rõ record/event semantics và identity contract |
| Framework nhằm biểu diễn typical workflow giữa inspection và maintenance, tập trung vào information-flow structure | Accessible **Methodology snippet** | Conceptual framework | Snippet không cho thấy chain direction, cardinality, traceability hoặc status transitions | G2 cần công bố ER model, not-null/cardinality rules và allowed transitions, không chỉ workflow diagram |
| Hai practical applications được thiết kế để đánh giá framework; case đầu tạo IFC file từ đầu và không có spatial representation/3D visualization | Accessible **Framework application snippet** | Case-evaluation statement | Snippet bị cắt; không thấy datasets, software, outputs, criteria hoặc results | Không được dùng bài này để khẳng định empirical effectiveness hay full interoperability; cần full PDF ở Round 2 |
| Spatial, process và cost decompositions dùng official IFC 4.3.2.0 entities và hướng tới tránh IFC extension | Accessible **Discussion snippet** | Schema-design statement | Không thấy entity/relationship names hoặc mapping | G2 phải kiểm tra reuse-versus-extension decision ở từng entity; broad use of official IFC entities đã có prior art |
| Bài tuyên bố implementation, automated study cases/IFC generation và successful validation bằng open-source tools/buildingSMART services | Accessible **Highlights**; partial **Conclusion snippet** | Implementation and schema-validation statements | Không kiểm chứng được validator, test input, expected result, warnings, failures hoặc pass criteria. **Evidence is currently insufficient.** | Không được mô tả Bellon là đã có negative tests, CQ, parity hoặc referential-integrity battery |

#### Kiểm tra các thành phần

| Thành phần | Yes / Partial / No | Exact evidence |
|---|---|---|
| Condition evidence | Partial | Introduction nói detect/document damage và integrate damage information; không có evidence object, context fields hoặc identifier. **Evidence is currently insufficient.** |
| BIM/IFC identity | No | Discussion snippet chỉ nói official IFC 4.3.2.0 entities; không thấy `GlobalId`, GUID hay cross-system identifier. **Evidence is currently insufficient.** |
| Inspection record | Partial | Introduction và Methodology snippet nêu inspection reports/data; không thấy record fields, timestamps hoặc identifier. **Evidence is currently insufficient.** |
| Action record | Partial | Introduction/Methodology snippet nêu proposed maintenance services, costs và interventions; không thấy Action_Record, work-order identity hoặc execution result. **Evidence is currently insufficient.** |
| Status event/history | No | Không có explicit event, transition hoặc history trong accessible text. **Evidence is currently insufficient.** |
| Provenance/accountability | No | Không thấy source lineage, actor, reviewer, approver hoặc audit fields. **Evidence is currently insufficient.** |
| Competency questions | No | Không thấy CQ registry, query hoặc expected answers. **Evidence is currently insufficient.** |
| Executable constraints | Partial | Highlights tuyên bố validation bằng open-source/buildingSMART services; exact rules và execution reports không đọc được. **Evidence is currently insufficient.** |
| Deliberate negative tests | No | Không thấy invalid fixtures, expected failures hoặc actual-versus-expected results. **Evidence is currently insufficient.** |
| Forward traceability | No | “Information flow structure” được nêu ở Methodology snippet nhưng không có trace query hoặc chain demonstration. **Evidence is currently insufficient.** |
| Reverse traceability | No | Không có reverse query hoặc reconstruction trong accessible text. **Evidence is currently insufficient.** |
| Round-trip parity | No | Không có source-target-source comparison trong accessible text. **Evidence is currently insufficient.** |
| Human review | No | Introduction nhắc assessments by experienced engineers như problem context; không chứng minh framework có review/approval workflow. **Evidence is currently insufficient.** |

**Evidence-level verdict:** conceptual framework statement: present; implementation/schema/case-validation statements: present; detailed implemented artifact, exact constraints, query execution, negative testing và parity: **Evidence is currently insufficient.**

### 2.2 Lorvão Antunes et al. (2024)

#### Citation và vai trò

- **Citation:** Lorvão Antunes, A., Barateiro, J., Marecos, V., Petrović, J., & Cardoso, E. (2024). Ontology-based BIM-AMS integration in European Highways. *Intelligent Systems with Applications, 22*, 200366. https://doi.org/10.1016/j.iswa.2024.200366
- **Zotero key:** `XUN8EX6X`
- **DOI:** `10.1016/j.iswa.2024.200366`
- **Academic role:** closest semantic-linkage, CQ và component-level inspection competitor.
- **Relevance to G2/G3:** trực tiếp xác lập Inspection/Observation/Result-to-structural-element-to-GlobalId subchain và executed SPARQL/API demonstration.

#### Claim → Evidence → Limitation → Thesis implication

| Claim được bài chứng minh | Evidence page/section | Validation used | Limitation | Implication for thesis |
|---|---|---|---|---|
| Inspection-generated condition data được mô hình hóa bằng `Inspection`/`Procedure`, `Observation`, `Agent`, `Structural Element`, `hasSimpleResult` và `hasResult` | PDF p. 7, §5.2.3, Fig. 4 | Conceptual ontology plus populated pilot artifact (§5.3) | Scope giới hạn ở tunnel, bridge, pavement pilots (PDF p. 12, §8.3) | Reuse subchain này; Condition_Evidence của thesis phải thêm source/run/version/quality provenance và stable identifier |
| Structural element được nối qua ifcOWL representation path tới IFC GlobalId | PDF p. 7, §5.2.4, Fig. 5; PDF p. 9, §6.1, Listing 5 | Implemented ontology relation and SPARQL query | Mapping ontology entities với ifcOWL instances còn thủ công (PDF p. 12, §§8.2-8.3) | GlobalId linkage không còn là novelty; G2 phải thêm identity governance và broken-link tests |
| CQs cho bridge inspection/risk-condition được pre-specified và formalized bằng SPARQL | PDF p. 6, §5.1.5, Table 2, CQ8-CQ10; PDF pp. 8-9, §6.1, Listings 3-5 | CQ evaluation/query formulation | Không có CQ cho action, status, accountability hoặc reverse traversal | CQ method không mới; thesis contribution phải là chain-complete registry và acceptance execution |
| `GetInspectionResult` trả pairs condition indicator và IFC GUID, rồi Bexel add-in colorize bridge elements theo inspection | PDF p. 10, §§7.2-7.3, Figs. 9-10 | Executed API/query and pilot demonstration | Population/export và ifcOWL mapping phụ thuộc manual intervention (PDF p. 12, §8.3) | Đây là forward subchain; Paper 2 phải thêm action/status, reverse query và parity validation |
| Formal evaluation gồm CQ answering và OOPS! pitfall scan, không gồm SHACL/SWRL | PDF pp. 8-9, §6.1-6.2; PDF p. 12, §8.3 | Query evaluation and ontology-pitfall scan | SHACL/SWRL chưa được addressed; OOPS! không kiểm tra instance-level chain integrity | G3 cần executable domain constraints và intentionally invalid fixtures; không dùng OOPS! như bằng chứng referential integrity |

#### Kiểm tra các thành phần

| Thành phần | Yes / Partial / No | Exact evidence |
|---|---|---|
| Condition evidence | Yes | Observation có 1-5 indicator hoặc descriptive state, inspection due date và photo URL: PDF p. 7, §5.2.3, Fig. 4 |
| BIM/IFC identity | Yes | PhysicalObject-to-ifcElement GlobalId path: PDF p. 7, §5.2.4, Fig. 5; query/output: PDF pp. 9-10, Listing 5, Fig. 9 |
| Inspection record | Yes | Inspection là `Procedure`/`InspectionActivity`, có `prov:atTime`, liên kết observations/results: PDF p. 7, §5.2.3; PDF pp. 8-9, Listings 4-5 |
| Action record | No | Không có maintenance/repair action entity trong Fig. 4, Table 2 CQ8-CQ10, Listings 3-5 hoặc conclusion (PDF pp. 6-9, 13) |
| Status event/history | Partial | Listing 4 lấy latest inspection result bằng `MAX(?time)`; không có event sequence hoặc transition: PDF p. 8, Listing 4 |
| Provenance/accountability | Partial | `Agent` makes observation và `prov:atTime`: PDF p. 7, §5.2.3; PDF p. 8, Listing 4. Không có approver/audit workflow |
| Competency questions | Yes | Table 2 CQ1-CQ13 và Listings 1-5: PDF pp. 6, 8-9, §§5.1.5, 6.1 |
| Executable constraints | No | SHACL/SWRL chỉ được nêu như khả năng và explicitly chưa addressed: PDF pp. 11-12, §§8.2-8.3 |
| Deliberate negative tests | No | OOPS! scan ở PDF p. 9, §6.2 không dùng intentionally invalid record fixtures |
| Forward traceability | Partial | Inspection -> Observation/Result -> Structural Element -> GUID -> BIM display: PDF pp. 9-10, Listing 5, §§7.2-7.3; chain dừng trước action/status |
| Reverse traceability | No | Listing 5/API bắt đầu từ inspection và trả GUID; không có GUID/BIM-to-originating-inspection query: PDF pp. 9-10 |
| Round-trip parity | No | Không có BIM-to-AMS write-back hoặc loss/equality comparison: PDF p. 10, §7.3; limitations PDF p. 12, §8.3 |
| Human review | Partial | Experts validate shared conceptualization (PDF p. 11, §8); user selects inspection trong add-in (PDF p. 10, §7.3). Không có review/approval record |

**Evidence-level verdict:** conceptual proposal, implemented OWL/GraphDB/API artifact và executed forward query/pilot đều present; schema validation chỉ ở mức ontology pitfall scan; deliberate negative testing, reverse traceability và round-trip parity absent.

### 2.3 Lee et al. (2021)

#### Citation và vai trò

- **Citation:** Lee, Y.-C., Eastman, C. M., & Solihin, W. (2021). Rules and validation processes for interoperable BIM data exchange. *Journal of Computational Design and Engineering, 8*(1), 97-114. https://doi.org/10.1093/jcde/qwaa064
- **Zotero key:** `GWP87WLC`
- **DOI:** `10.1093/jcde/qwaa064`
- **Academic role:** IFC/MVD constraint and generic referential-integrity validation foundation.
- **Relevance to G2/G3:** cung cấp rule families và executed pass/fail reporting có thể chuyển thành G2 constraint catalogue; không bao phủ domain chain.

#### Claim → Evidence → Limitation → Thesis implication

| Claim được bài chứng minh | Evidence page/section | Validation used | Limitation | Implication for thesis |
|---|---|---|---|---|
| Bốn rule families gồm uniqueness, reference existence, semantic accuracy và general syntax | PDF p. 5, §4.1; PDF p. 7, §5.1 | MVD-rule taxonomy and implementation | MVD scope/definitions có ambiguity và multiple interpretations (PDF p. 16, §6) | Dùng bốn families làm validation kernel, rồi định nghĩa domain-specific constraints |
| IFC GUID phải có length 22 và unique giữa object instances trong IFC file | PDF p. 8, §5.1.1 | Static format-length and global uniqueness checks | Không có permitted-character rule, regex, lifecycle persistence hoặc executed GUID-failure result | G2 dùng GlobalId nhưng phải bổ sung cross-file/revision persistence và deliberate duplicate/invalid fixtures |
| Forward-reference và inverse-reference correctness gồm đúng target relationship/entity | PDF p. 8, §5.1.2; failures PDF pp. 10-14, Figs. 9-11, 15-16 | Executed instance conformance with UI/HTML pass/fail reports | Không có external record/FK chain; reference interpretations còn đa dạng (PDF p. 16, §6) | Chuyển thành typed FK, inverse-consistency và orphan checks cho từng chain edge |
| Requiredness, cardinality, datatype, allowed value và syntax là independently checkable | PDF pp. 9-12, §§5.1.3-5.2, Fig. 12 | Static schema/MVD conformance | Checking sequence và mandatory/optional evaluation còn là challenge (PDF p. 16, §6) | G2 phải gán explicit violation codes và expected outcomes cho each field/relation |
| Bài phát hiện actual defects nhưng không chứng minh controlled negative-test protocol | Test model: PDF p. 6, §4.2; actual failures: PDF pp. 10-14, Figs. 9-17 | Executed case conformance | Không có seeded-invalid manifest, predefined expected failures hoặc actual-versus-expected comparison | G3 chỉ được claim negative testing khi thesis bổ sung fixture manifest và oracle |

#### Kiểm tra các thành phần

| Thành phần | Yes / Partial / No | Exact evidence |
|---|---|---|
| Condition evidence | No | Rule taxonomy ở PDF pp. 5, 7-10 không có condition-evidence entity hoặc relation |
| BIM/IFC identity | Yes | `IfcGloballyUniqueId` length 22 và within-file uniqueness: PDF p. 8, §5.1.1 |
| Inspection record | Partial | “Product Inspection” chỉ là COBie exchange-model name ở PDF p. 5, Fig. 3; không có record schema hoặc validation |
| Action record | No | Không có action-record entity; high-level COBie task concepts ở PDF p. 5, Fig. 2 không đủ để suy ra Action_Record |
| Status event/history | No | Không có event/transition/history model trong §§4.1, 5.1-5.2 |
| Provenance/accountability | No | Không có evidence/action actor, reviewer, approver hoặc audit chain trong scoped sections |
| Competency questions | No | Không có CQ registry hoặc query-based evaluation; phương pháp là MVD rule validation, PDF pp. 5-16 |
| Executable constraints | Yes | IfcDoc rules và pass/fail UI/HTML reports: PDF pp. 7-14, §5, Figs. 9-17 |
| Deliberate negative tests | No | Execution có, nhưng intentional fixture, expected failure và actual-versus-expected comparison không được báo cáo: PDF pp. 6, 10-14 |
| Forward traceability | No | Generic reference checking ở PDF p. 8, §5.1.2 không phải evidence-to-action traceability |
| Reverse traceability | No | Không có reverse lifecycle query hoặc reconstruction |
| Round-trip parity | No | Không có source-target-source execution hoặc parity comparison |
| Human review | No | Manually developed test model ở PDF p. 6, §4.2 không phải operational review/approval workflow |

**Evidence-level verdict:** implemented generic IFC/MVD validator và executed case conformance present; chain-specific schema/query absent; observed failures không đạt strict deliberate-negative-test criterion.

### 2.4 Oraskari et al. (2021)

#### Citation và vai trò

- **Citation:** Oraskari, J., Senthilvel, M., & Beetz, J. (2021). SHACL is for LBD what mvdXML is for IFC. In *Proceedings of the CIB W78 2021 Conference, 11-15 October 2021, Luxembourg* (pp. 693-702).
- **Zotero key:** `AQDJR2UE`
- **DOI:** không có DOI của paper trong PDF; DOI ở reference list thuộc IFCtoLBD software.
- **Academic role:** SHACL feasibility/unit/regression validation foundation for LBD conversion and model views.
- **Relevance to G2/G3:** cung cấp transferable patterns cho missing counterpart, selected relation preservation và view validation; không bao phủ inspection/action chain hoặc bidirectional parity.

#### Claim → Evidence → Limitation → Thesis implication

| Claim được bài chứng minh | Evidence page/section | Validation used | Limitation | Implication for thesis |
|---|---|---|---|---|
| GUID có thể nối source IFC individuals với LBD counterparts | PDF pp. 4-5 (696-697), §3.1, Listing 1 | Executed SHACL-SPARQL feasibility test | Listing 1 chỉ bắt absence; không count exactly one, check class hoặc reject duplicate | G2 cần exactly-one assertion và explicit duplicate/mismatched-class fixtures |
| Selected relations và output changes có thể kiểm tra bằng property-specific rules/checksum | PDF pp. 5-6 (697-698), §3.2, Listings 2-3 | Java/TopBraid unit and change-detection tests | Generic alignment rule được xem là implausible; Listing 3 hash predicates, không hash full triples/values | Thesis parity oracle phải canonicalize complete payload, không chỉ predicate set |
| Independent converter output có thể tạo expected topology constraints cho converter khác | PDF pp. 6-7 (698-699), §3.2, Listing 4 | Differential/example-based comparison | Listing 4 bắt missing expected edges nhưng không reject extra edges; shown rule không tự chứa GUID check | G3 có thể dùng golden fixtures, nhưng phải test missing, extra, duplicate và swapped relationships |
| SHACL có thể validate required LBD content và construct restricted MVD-like RDF view | PDF pp. 7-9 (699-701), §4-5, Listings 5-6 | TopBraid feasibility tests and SPARQL `CONSTRUCT` | Missing target nodes có thể pass; copied view chỉ gồm direct triples và không recursive | Không đồng nhất view construction với reverse traceability hoặc round-trip parity |

#### Kiểm tra các thành phần

| Thành phần | Yes / Partial / No | Exact evidence |
|---|---|---|
| Condition evidence | No | Không có condition/evidence entity trong §§3-5 hoặc Listings 1-6, PDF pp. 4-9 (696-701) |
| BIM/IFC identity | Yes | GUID-based correspondence trong §3.1, Listing 1 và cross-converter alignment §3.2: PDF pp. 4-7 (696-699) |
| Inspection record | No | Không có inspection model/instance/property trong §§3-5 |
| Action record | No | Không có action concept trong §§3-5 |
| Status event/history | No | Không có timestamped state transition hoặc event rule |
| Provenance/accountability | No | Không có source lineage agent, reviewer, approver hoặc audit event |
| Competency questions | No | Không có CQ registry/expected answers; tests là SHACL shapes/listings |
| Executable constraints | Yes | SHACL-SPARQL constraints/rules, TopBraid execution: PDF pp. 4-9 (696-701), Listings 1-6 |
| Deliberate negative tests | No | Unknown-change warning ở PDF p. 6 (698), §3.2 không kèm intentionally corrupted fixture và expected violation |
| Forward traceability | Partial | IFC/ifcOWL source -> LBD counterpart bằng GUID: PDF pp. 4-5 (696-697), §3.1; không có lifecycle chain |
| Reverse traceability | No | Không có LBD -> IFC transformation/query |
| Round-trip parity | No | Không có source -> target -> source hoặc equality/semantic-equivalence comparison: PDF pp. 4-9 (696-701), §§3-5 |
| Human review | No | Không có operational review/approval workflow trong method/results |

**Listing audit:** Listing 1 không enforce “precisely one”; Listing 2 có thể tạo site-building cross-product và không check reverse/extra relations; Listing 3 hash predicates thay vì complete triples; Listing 4 không reject extra storeys; Listings 5-6 copy direct triples theo URI/object-type conditions, không recursive và không tạo reverse transformation (PDF pp. 4-8 [696-700], §§3.1-4).

**Evidence-level verdict:** implemented SHACL feasibility/unit checks present; regression evidence partial; deliberate negative testing, reverse transformation và round-trip parity absent.

## 3. Cross-paper comparison

| Study | Main artifact | Identity | Inspection/action coverage | CQ | Constraints | Negative tests | Forward/reverse | Main missing element |
|---|---|---|---|---|---|---|---|---|
| Bellon et al. (2025) | IFC inspection-maintenance framework; implementation/validation statements | Exact identifier not visible | Broad inspection, damage, maintenance, cost scope; exact chain unavailable | Not visible | Validation claimed, exact rules unavailable | Not visible | Information flow claimed; trace directions not visible | Full-text evidence for entities, identifiers, status, queries và test outputs; **Evidence is currently insufficient** |
| Lorvão Antunes et al. (2024) | OWL ontology, GraphDB/API/BIM pilot | IFC GlobalId through ifcOWL, PDF p. 7 Fig. 5; p. 9 Listing 5 | Inspection/condition yes; Action_Record absent; latest state only, PDF pp. 7-9 | Yes, Table 2 and Listings 1-5, PDF pp. 6, 8-9 | OOPS! only; SHACL/SWRL future, PDF pp. 9, 12 | No | Forward subchain yes/partial, PDF pp. 9-10; reverse/parity no | Action/status, executable integrity rules, negative fixtures, reverse parity |
| Lee et al. (2021) | IfcDoc/MVD rule-validation process | GUID length/uniqueness, PDF p. 8 §5.1.1 | Product Inspection only as COBie label; no chain, PDF p. 5 Fig. 3 | No | Yes: uniqueness/reference/semantic/syntax, PDF pp. 5, 7-14 | No under strict criterion | No lifecycle traceability/parity | Domain records and chain-specific integrity fixtures |
| Oraskari et al. (2021) | SHACL-SPARQL conversion/unit/view checks | GUID source-output matching, PDF pp. 4-7 §§3.1-3.2 | None | No | Yes, Listings 1-6, PDF pp. 4-9 | No under strict criterion | IFC/ifcOWL -> LBD partial; reverse/parity no | Full-chain semantics, exact-one checks, negative fixtures, reverse conversion/parity |

## 4. Prior art đã được xác lập

### IFC-linked inspection/maintenance representation

Broad IFC inspection-maintenance representation không còn là claim độc lập an toàn: Bellon Introduction và Methodology snippet nêu IFC workflow cho inspection data, damage reports, proposed maintenance services và costs; Antunes mô hình hóa Inspection/Observation/Result và BIM link ở PDF p. 7, §§5.2.3-5.2.4, Figs. 4-5. Exact Bellon schema vẫn **Evidence is currently insufficient**, nên chỉ broad claim được coi là established trong corpus này.

### IFC GlobalId linkage

Antunes nối PhysicalObject/Structural Element tới `ifcElement` GlobalId và trả GUID qua query/API (PDF pp. 7, 9-10, Fig. 5, Listing 5, Fig. 9). Lee định nghĩa GUID length 22 và within-file uniqueness checks (PDF p. 8, §5.1.1). Paper 2 không được lấy “use IFC GlobalId” làm contribution; phần còn mở là persistence, crosswalk governance và failure handling.

### Competency questions

Antunes pre-specifies general và pilot-specific CQs ở Table 2 và formalizes queries trong Listings 1-5 (PDF pp. 6, 8-9, §§5.1.5, 6.1). Việc dùng CQ để scope/evaluate semantic model đã established; novelty chỉ có thể nằm ở chain-complete CQ registry, expected answers và validation coverage.

### SHACL hoặc IFC constraint validation

Lee thực thi IFC/MVD uniqueness, reference, semantic và syntax checks (PDF pp. 5, 7-14, §§4.1, 5.1-5.2). Oraskari thực thi SHACL-SPARQL checks cho source-output correspondence, selected relations và view construction (PDF pp. 4-9 [696-701], §§3-5, Listings 1-6). Constraint technology hoặc SHACL use không còn là standalone novelty.

### BIM-linked condition/inspection information

Antunes biểu diễn inspection observation/result, structural-element relation, condition indicator/state, due date/photo URL và GlobalId retrieval (PDF pp. 7-10, Fig. 4-5, Listings 3-5, Figs. 9-10). Claim “link condition/inspection information to BIM” phải bị loại khỏi novelty boundary.

### Human review nói chung

Trong bốn bài, Antunes chỉ báo expert validation của shared conceptualization và user selection trong add-in (PDF pp. 10-11, §§7.3, 8); Bellon Introduction chỉ nêu assessments by experienced engineers như problem context; Lee và Oraskari không có operational review workflow. **Evidence is currently insufficient** để dùng bốn bài này làm bằng chứng rằng accountable human review đã được triển khai, nhưng generic human interaction cũng không nên được dùng như contribution nếu không có explicit review event, actor, rationale và audit trace.

## 5. Candidate gaps

### 5.1 Integrated referential-integrity failure testing

**Claim**  
Một controlled failure battery cho toàn bộ external identifier/reference chain là candidate gap mạnh.

**Supporting evidence**  
Lee định nghĩa GUID, forward/inverse references, requiredness, datatype, value, cardinality và syntax rules (PDF pp. 8-12, §§5.1.1-5.2) và hiện actual defects ở Figs. 9-17 (PDF pp. 10-14). Oraskari kiểm tra missing source-output counterpart và selected relations (PDF pp. 4-7 [696-699], Listings 1-4). Antunes không triển khai SHACL/SWRL (PDF p. 12, §8.3).

**What prior studies already achieved**  
Generic IFC/MVD conformance execution và selected RDF conversion checks đã có.

**Remaining gap**  
Trong phạm vi bốn tài liệu đã deep-read, chưa thấy predefined invalid fixtures + expected failures + execution + actual-versus-expected results cho orphan/duplicate/mismatched links xuyên suốt evidence, BIM, inspection, action và status.

**Required thesis validation**  
Fixture manifest cho missing/duplicate/invalid IDs, wrong target type, orphan records, stale crosswalk, illegal status transition và broken inverse relation; stable violation codes; expected-versus-actual report; coverage và false-pass accounting.

**Verdict:** Strong candidate.

### 5.2 Bidirectional forward/reverse parity

**Claim**  
Forward/reverse query parity và source-target-source equality là candidate gap mạnh.

**Supporting evidence**  
Antunes thực thi inspection-to-GUID/BIM display (PDF pp. 9-10, Listing 5, §§7.2-7.3). Oraskari kiểm tra IFC/ifcOWL -> LBD correspondence và LBD -> restricted RDF view, không chạy LBD -> IFC (PDF pp. 4-9 [696-701], §§3-5).

**What prior studies already achieved**  
Forward retrieval/mapping ở selected subchains và change/conversion checks đã có.

**Remaining gap**  
Không có reverse reconstruction từ Status_Event/Action_Record về Inspection_Record, Condition_Evidence và source context; không có source -> target -> source parity test.

**Required thesis validation**  
Pre-specified forward/reverse CQs; exactly-one and set-equality assertions; canonical payload/hash comparison; tests cho missing, extra, duplicate, swapped và stale nodes/edges; hop-level diagnostics.

**Verdict:** Strong candidate.

### 5.3 Condition_Evidence context and provenance

**Claim**  
Condition_Evidence có stable identity và minimum context/provenance profile là candidate gap, nhưng condition result-to-BIM linkage tự nó đã established.

**Supporting evidence**  
Antunes có indicator, descriptive state, due date, photo URL, Agent và `prov:atTime` (PDF pp. 7-8, §5.2.3, Fig. 4, Listing 4), nhưng không có complete source/run/model-version/reviewer lineage. Bellon accessible Introduction nói damage/inspection information nhưng không expose evidence schema.

**What prior studies already achieved**  
Condition observations/results, inspection timestamp, agent và BIM GlobalId linkage ở mức selected fields.

**Remaining gap**  
Stable Evidence_ID, acquisition source, processing run, method/model version, quality/confidence, derivation, reviewer decision và immutable lineage chưa được kết hợp và validated trong bốn bài.

**Required thesis validation**  
Data dictionary và completeness rules; evidence-to-source/component reconstruction; model/version change cases; missing source/run/version, duplicate evidence và mismatched component fixtures.

**Verdict:** Promising.

### 5.4 Inspection_Record-Action_Record-Status_Event chain

**Claim**  
Một explicit, queryable record-event chain có allowed transitions là candidate gap, nhưng broad inspection-maintenance information flow đã bị Bellon bao phủ ở mức statement.

**Supporting evidence**  
Antunes có Inspection_Record-like structure nhưng không có Action_Record (PDF pp. 7-9, §5.2.3, Listings 3-5). Bellon Introduction/Methodology snippet nêu inspection-to-maintenance workflow, proposed services và costs; full entity model không đọc được. Lee và Oraskari không có domain chain.

**What prior studies already achieved**  
Inspection/condition subchain được implemented ở Antunes; broad inspection-maintenance IFC framework được Bellon tuyên bố.

**Remaining gap**  
Explicit Action_Record identity, Status_Event history, predecessor/successor rules, execution/verification state và integrity constraints chưa được xác nhận. Bellon full text thiếu nên boundary ở entity level chưa thể khóa hoàn toàn.

**Required thesis validation**  
Record/event IDs, timestamps, actor, evidence basis, allowed transitions, terminal states; queries cho proposed/approved/rejected/executed/verified; illegal-transition, missing-predecessor, action-without-inspection và closure-without-verification fixtures.

**Verdict:** Promising.

### 5.5 Accountable human-reviewed action workflow

**Claim**  
Accountability có thể là supporting/secondary contribution nếu được biểu diễn và tested, không chỉ có human interaction.

**Supporting evidence**  
Antunes có Agent, timestamp, expert validation và user selection (PDF pp. 7-8, 10-11, §5.2.3, Listing 4, §§7.3, 8), nhưng không có approver/audit event. Bellon accessible text không expose review schema. Lee/Oraskari không có operational human review.

**What prior studies already achieved**  
Agent attribution ở observation level và human participation trong demonstration/evaluation.

**Remaining gap**  
Inspector/reviewer/approver identity, rationale, authorization, separation of duties, rejection/override và action-closure audit trace chưa được demonstrated trong bốn bài.

**Required thesis validation**  
Role-event model; authorization and separation rules; fixtures cho unauthorized approval, self-approval, missing rationale, superseded review và unverified closure; reverse trace từ action tới evidence and responsible agents.

**Verdict:** Promising.

## 6. Closest-competitor verdict

1. **Bellon et al. gần Paper 2 ở điểm nào?** Bài đặt đúng broad problem space: IFC-based information flow tích hợp inspection, damage reports, proposed maintenance services và costs; Methodology snippet gọi đây là typical inspection-maintenance workflow. Highlights/Framework application/Conclusion snippets tuyên bố implementation và testing. Tuy nhiên, exact schema, identifiers, constraints và results không đọc được từ Zotero attachment. **Evidence is currently insufficient** để kết luận Bellon đã có full `Inspection_Record-Action_Record-Status_Event` semantics.
2. **Lorvão Antunes et al. gần Paper 2 ở điểm nào?** Bài đã implemented semantic subchain gồm Inspection/Procedure, Observation/Result, Structural Element và IFC GlobalId; CQ8-CQ10 và `GetInspectionResult` được dùng để truy condition result/GUID và display trong BIM (PDF pp. 6-10, Table 2, Fig. 4-5, Listings 3-5, Figs. 9-10). Đây là closest competitor cho semantic linkage/CQ, nhưng thiếu Action_Record, explicit Status_Event, executable constraints, deliberate failures và reverse parity.
3. **Lee và Oraskari bao phủ validation đến đâu?** Lee bao phủ generic IFC/MVD uniqueness, references, semantics, syntax và actual conformance defects (PDF pp. 5, 7-14), nhưng không có controlled negative-fixture protocol. Oraskari bao phủ SHACL feasibility checks cho missing counterpart, selected relation, change detection và view construction (PDF pp. 4-9 [696-701]), nhưng Listings có coverage gaps và không có reverse conversion/parity. Cả hai không validate target domain chain.
4. **Paper 2 phải làm thêm gì để không trở thành bài system integration?** Phải công bố implementation-neutral domain specification, pre-specified CQs, exact identifier/relationship/status semantics, constraint catalogue, controlled positive/negative fixtures, forward/reverse parity contract và accountable human-review events; UI hoặc technology stack chỉ là test harness. Kết quả phải báo theo acceptance criteria, không chỉ screenshots/happy-path retrieval.

## 7. G2 implications

| Artifact cần khóa | Classification | Evidence basis | G2 decision cần khóa |
|---|---|---|---|
| Identifier schema | directly supported | Antunes GlobalId path/query: PDF pp. 7, 9-10, Fig. 5, Listing 5, Fig. 9; Lee GUID rules: PDF p. 8, §5.1.1 | Tách Asset/Component ID, IFC GlobalId, Evidence_ID, Inspection_ID, Action_ID, StatusEvent_ID; define uniqueness, persistence và crosswalk ownership |
| Entity-relationship model | directly supported | Antunes Inspection/Observation/Result/Element model: PDF p. 7, Fig. 4-5; Bellon Methodology snippet broad workflow | Khóa entities, typed edges, cardinalities, temporal direction và inverse relations, độc lập serialization |
| Condition_Evidence dictionary | indirectly supported | Antunes fields: PDF p. 7, §5.2.3; provenance precursor PDF p. 8, Listing 4 | Khóa source, time, location/component, method/run/model version, result, quality/confidence, creator/reviewer và derivation |
| Inspection_Record | directly supported | Antunes `Inspection` as Procedure/InspectionActivity: PDF pp. 7-9, §5.2.3, Listings 4-5 | Khóa ID, scope, inspector, time, evidence set, findings, decision/review state và version |
| Action_Record | indirectly supported | Bellon Introduction/Methodology snippet nêu proposed maintenance services/costs; exact schema unavailable | Khóa ID, originating inspection/finding, proposed action, owner, priority, rationale, due/execution/verification fields |
| Status_Event | thesis-defined | Antunes chỉ có latest result bằng `MAX(?time)`: PDF p. 8, Listing 4; không có event history | Khóa immutable event ID, record ID, prior/new status, time, actor, reason, source event và allowed transition |
| Competency-question registry | directly supported | Antunes Table 2 and Listings 1-5: PDF pp. 6, 8-9 | Mỗi CQ có owner, wording, input, expected answer shape, query, fixture và acceptance result |
| Constraint catalogue | directly supported | Lee rule families: PDF pp. 5, 7-12; Oraskari Listings 1-6: PDF pp. 4-9 | Khóa technology-neutral rule ID, scope, severity, rationale, expected violation và possible SQL/RDF/other implementations |
| Positive/negative fixture manifest | thesis-defined | Strict negative protocol absent in Lee PDF pp. 6, 10-14; Oraskari PDF p. 6 (698); Antunes PDF p. 9 §6.2 | Khóa valid baselines, one-fault mutations, expected violations, versioning, coverage và regression policy |
| Forward/reverse query contract | thesis-defined | Antunes forward subchain: PDF pp. 9-10; Oraskari source-to-LBD only: PDF pp. 4-7 | Khóa paired CQs/queries, exactly-one/set-equality rules, canonical payload comparison và hop-level diagnostics |

Không artifact nào trong bảng đồng nghĩa G2 đã đạt. Classification chỉ cho biết mức hỗ trợ bằng chứng để xây specification.

## 8. Novelty boundary

### Central claim an toàn

> Trong phạm vi bốn tài liệu đã deep-read, Paper 2 có thể định vị đóng góp ở việc thiết kế và kiểm chứng một implementation-neutral, identity-governed evidence-to-action specification liên kết context-preserving `Condition_Evidence` với IFC-identified component, `Inspection_Record`, `Action_Record` và `Status_Event`, được đánh giá bằng pre-specified competency questions, executable integrity constraints, deliberate invalid fixtures, forward/reverse parity và accountable human-review events.

Claim này chỉ sử dụng được sau khi G3 thực thi acceptance tests. Trước thời điểm đó, chỉ được gọi là proposed specification và validation plan.

### Contribution statements

1. **Information artifact:** một canonical identifier/entity/relationship/status specification bảo toàn evidence context và liên kết xuyên suốt evidence-to-action chain.
2. **Validation contract:** một technology-neutral CQ/constraint/fixture framework kiểm tra schema conformance, external referential integrity, deliberate failures và forward/reverse parity.
3. **Accountability layer:** một explicit human-review event model cho attribution, review, approval/rejection, action execution và verified closure, cùng executable authorization/traceability tests.

### Claims bị cấm hoặc phải thu hẹp

- Không claim novelty cho IFC-linked inspection/maintenance representation: Bellon Introduction/Methodology snippet và Antunes PDF p. 7 đã bao phủ broad space.
- Không claim novelty cho IFC GlobalId linkage: Antunes PDF pp. 7, 9-10 và Lee PDF p. 8 đã bao phủ linkage/rules.
- Không claim novelty cho competency questions: Antunes PDF pp. 6, 8-9 đã công bố và formalize CQs.
- Không claim novelty cho SHACL hoặc generic IFC constraint validation: Lee PDF pp. 5, 7-14 và Oraskari PDF pp. 4-9 đã thực thi các phương pháp này.
- Không gọi conformance defects là deliberate negative tests nếu thiếu fixture intent, expected failure và actual-versus-expected result.
- Không gọi IFC/ifcOWL -> LBD hoặc ontology -> BIM display là bidirectional/round-trip nếu chưa có reverse execution và parity oracle.
- Không gọi `Agent`/timestamp hoặc user selection là accountable human review nếu chưa có reviewer/approver identity, rationale, authorization và audit event.
- Không tuyên bố exact Bellon entities, relationships, identifiers hoặc validation outcomes cho đến khi có complete full text. **Evidence is currently insufficient.**
- Không định vị Paper 2 như website, BIM viewer, ontology-only, SHACL-only hoặc commercial system integration.

## 9. Next actions

1. **Khóa governance decision:** quyết định canonical ID ownership, IFC GlobalId persistence policy, crosswalk versioning, duplicate resolution, record immutability và implementation-neutral constraint language.
2. **Xây schema:** tạo Evidence-to-Action ER model và data dictionary cho sáu identifiers, Condition_Evidence, Inspection_Record, Action_Record, Status_Event, Agent/Review_Event; ghi cardinality, temporal và inverse rules.
3. **Viết CQ registry:** tối thiểu các paired CQs cho evidence-to-component, component-to-evidence, inspection-to-action/status, action/status-to-originating evidence, accountability và exception cases; định nghĩa expected answer shape trước implementation.
4. **Tạo fixture manifest:** valid baseline plus one-fault cases cho missing/duplicate/invalid ID, orphan FK, wrong target type, stale mapping, missing provenance, illegal transition, unauthorized review và unverified closure.
5. **Thực hiện G3 tests:** chạy schema/constraint checks, forward/reverse queries, exactly-one/set-equality assertions, canonical payload parity và expected-versus-actual negative-test reports bằng ít nhất một implementation; không khóa SHACL nếu SQL hoặc cơ chế khác đáp ứng contract tốt hơn.
6. **Round 2 verification:** lấy complete Bellon PDF để xác nhận entity/relationship/identifier/validation details; kiểm tra Antunes ontology/API artifacts, Lee IfcDoc definitions/test models và Oraskari test code/listing behavior nếu artifacts đi kèm bốn bài khả dụng.
7. **Khóa dependency với G1:** yêu cầu output G1 cung cấp stable `Condition_Evidence_ID`, source/run/time/component candidate, method/model version và quality context; G2 chỉ quản trị evidence/traceability, không mở rộng sang damage diagnosis, prediction hoặc autonomous action.
