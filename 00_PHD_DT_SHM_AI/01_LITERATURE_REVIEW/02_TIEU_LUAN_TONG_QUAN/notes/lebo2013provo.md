# lebo2013provo — PROV-O: The PROV Ontology ([69]), kèm đối chiếu MLflow và DVC

Lebo T, Sahoo S, McGuinness D (biên tập). *PROV-O: The PROV Ontology*. Khuyến nghị W3C, 30/04/2013.
https://www.w3.org/TR/2013/REC-prov-o-20130430/ . Số cũ [69]; Zotero có 4 bản ghi trùng (FJJAV9T4, TMZJ5PYK, PQUX27P4, 3XFEVIGR —
gộp ở N-37); ghi chú đặt theo citekey trong `doi_chieu_danh_muc.csv`.

**Bản đã đọc:** trang chuẩn chính thức (HTML, tải 01/10/2026); đặc tả không đánh số trang nên dẫn theo **mục**. Đọc mục 3.1
Starting Point Terms, 3.2 Expanded Terms (phần đầu), 3.3 Qualified Terms, và định nghĩa trong mục 4 (Cross reference) của
`prov:Plan`, `prov:Association`/`wasAssociatedWith`, `prov:Role`, `prov:wasRevisionOf`, `prov:invalidatedAtTime`/`wasInvalidatedBy`,
`prov:Bundle`. Kiểm phản chứng UV-02 (N-21a); bổ sung cho UV-07.

Ký hiệu: (a) điều chuẩn quy định; **[NCS]** nhận định của NCS.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | lebo2013provo / [69] |
| Tier / Cụm | Chuẩn tra cứu / Truy vết thông tin |
| Luận điểm | (a) PROV-O biểu diễn mô hình dữ liệu PROV-DM bằng OWL2: ba lớp gốc Entity, Activity, Agent và các quan hệ sinh ra, sử dụng, dẫn xuất, quy trách nhiệm; mẫu "định tính" (Qualification Pattern) cho phép thêm chi tiết vào mỗi quan hệ (mục 3.1, 3.3). |
| Bằng chứng | Đặc tả chuẩn, có ví dụ Turtle cho từng thuật ngữ; báo cáo triển khai riêng. |
| Giới hạn | Xem mục 3. |
| Tác động K1/K2/K3 | K1 (UV-02): giải quyết một phần — đủ từ vựng cho nguồn gốc và phương pháp ở mức **từng** thực thể; không có từ vựng cho phạm vi hiệu lực, độ bất định. K3 (UV-07): giải quyết một phần về hình thức — quy trách nhiệm cho tác nhân theo vai trò; không có trạng thái phê duyệt, thẩm quyền. |
| Vị trí sử dụng | 3.5, 5.5 (ánh xạ chuẩn: `EVIDENCE` là `prov:Entity`; lần chạy phương pháp là `prov:Activity`; `method_version` là `prov:Plan` qua `prov:qualifiedAssociation`/`prov:hadPlan`; thay bản ghi bằng `prov:wasRevisionOf`, `prov:wasInvalidatedBy` — đã ghi ở CLAUDE.md mục 8); Phụ lục B. |
| Mức đã đọc | Các mục liên quan của đặc tả chính thức (01/10/2026) |

## 1. Các thuật ngữ liên quan (a)

- **Starting Point (mục 3.1):** Entity, Activity, Agent; `prov:wasGeneratedBy`, `prov:used`, `prov:wasDerivedFrom`,
  `prov:startedAtTime`/`endedAtTime`; Agent "bears some form of responsibility for an activity taking place, for the existence of an
  entity, or for another agent's activity". Có thể dùng thuộc tính RDF tùy ý để mô tả các khía cạnh cố định của một Entity.
- **Qualified Terms (mục 3.3):** mẫu định tính thay một quan hệ đơn bằng một lớp trung gian có thể chú thích thêm — ví dụ
  `prov:qualifiedGeneration`/`prov:Generation`, `prov:qualifiedUsage`/`prov:Usage`, `prov:qualifiedAssociation`/`prov:Association`,
  `prov:qualifiedRevision`, `prov:qualifiedInvalidation` (Bảng 2, 3).
- **Association:** "an assignment of responsibility to an agent for an activity, indicating that the agent had a role in the
  activity. It further allows for a plan to be specified" (mục 4, `prov:Association`); **Role** là chức năng của thực thể hay tác
  nhân đối với một hoạt động.
- **Plan:** thực thể biểu diễn tập hành động/bước mà tác nhân dự định để đạt mục tiêu; "There exist no prescriptive requirement on
  the nature of plans, their representation, the actions or steps they consist of, or their intended goals" (mục 4, `prov:Plan`).
- **Revision, Invalidation:** bản sửa là một dẫn xuất cho ra phiên bản sửa của bản gốc; vô hiệu hóa là bắt đầu sự hủy, chấm dứt
  hay hết hạn của một thực thể, sau đó thực thể không còn được dùng (mục 4).
- **Bundle:** tập mô tả nguồn gốc có tên, bản thân là Entity, cho phép ghi nguồn gốc của nguồn gốc (mục 4).
- Tìm trong toàn văn đặc tả: không có thuật ngữ cho độ bất định, độ tin cậy, phạm vi hiệu lực hay điều kiện áp dụng; "applicable"
  chỉ xuất hiện trong câu hướng dẫn dùng quan hệ cụ thể nhất.

## 2. Đối chiếu bổ sung: MLflow và DVC (tài liệu chính thức, không nhập Zotero vì không trích)

- **MLflow Model Registry** (trang "MLflow Model Registry", mlflow.org/docs/latest/ml/model-registry/, truy cập 01/10/2026): kho mô
  hình tập trung, cung cấp "lineage (i.e., which MLflow experiment and run produced the model), versioning, aliasing, metadata
  tagging and annotation support"; "Each registered model version is linked to the MLflow run, logged model or notebook that
  produced it" — truy ngược cách huấn luyện, dữ liệu, tham số. Trang không đề cập việc ghi từng kết quả suy luận.
- **DVC** (doc.dvc.org, mục "dvc.yaml files" và "Defining pipelines", truy cập 01/10/2026): `dvc.lock` ghi cho mỗi bước của
  pipeline các phụ thuộc và đầu ra kèm mã băm nội dung (md5, etag hoặc checksum) và giá trị tham số đầy đủ.
- **[NCS]** Hai công cụ cho dòng dõi ở mức **phiên bản mô hình** và **tệp đầu ra của pipeline**; đủ để cấp `method_version` có thể
  truy ngược (đúng vai trò đã ghi ở 5.6A). Không có phạm vi hiệu lực; không gắn vào từng kết quả khi kết quả được dùng về sau.

## 3. Giới hạn

- (a) Chuẩn không quy định bản chất, cách biểu diễn của Plan (mục 4, `prov:Plan`) — tức phiên bản phương pháp được biểu diễn
  được nhưng nội dung do ứng dụng tự định nghĩa.
- **[NCS]** PROV-O là từ vựng mô tả, không có ràng buộc "bắt buộc phải có" (việc đó cần SHACL, như [21]); không có khái niệm phạm vi
  hiệu lực, độ bất định, trạng thái phê duyệt hay thẩm quyền.

## 4. Kiểm phản chứng

- **UV-02: giải quyết một phần.** Phần được giải quyết: một bản ghi cho **từng** kết quả với nguồn gốc xử lý (sinh bởi hoạt động
  nào, dùng dữ liệu nào, lúc nào) và phiên bản phương pháp (Plan gắn qua Association) **biểu diễn được** bằng chuẩn sẵn có; MLflow/DVC
  cấp phiên bản và dòng dõi ở mức mô hình/tệp. Phần không giải quyết: phạm vi hiệu lực (và độ bất định) như thành phần bắt buộc,
  kiểm được bằng máy, đi theo kết quả đến lần sử dụng.
- **UV-07: giải quyết một phần về hình thức.** `prov:Association` + `prov:hadRole` ghi được tác nhân nào chịu trách nhiệm cho hoạt
  động nào với vai trò gì (cùng chiều với `IfcApproval`, [44]); không có trạng thái phê duyệt, thẩm quyền hay căn cứ của quyết định.
