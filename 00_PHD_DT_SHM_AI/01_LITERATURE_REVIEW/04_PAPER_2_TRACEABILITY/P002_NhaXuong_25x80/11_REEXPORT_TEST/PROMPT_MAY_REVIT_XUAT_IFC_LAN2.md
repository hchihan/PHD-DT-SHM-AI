# Prompt cho máy có Revit 2027: xuất IFC lần 2 (ADR-RQ2-008)

Cách dùng: trên máy có Revit, mở Claude Code tại thư mục `04_PAPER_2_TRACEABILITY` trên Google Drive rồi dán toàn bộ khối dưới đây. Nếu không dùng Claude Code, tự làm theo các bước 1–6.

---

```text
Bối cảnh: Paper 2 (traceability BIM, ca nhà xưởng P002 25×80 m). WP2 đang FINAL_FROZEN. Tôi đã chọn Phương án A của ADR-RQ2-008: xuất IFC lần 2 từ CÙNG file RVT đã đăng ký, không chỉnh sửa gì, rồi so GlobalId với lần xuất 1. Máy trước không có Revit nên chưa làm được.

Đọc trước, theo thứ tự:
1. P002_NhaXuong_25x80/11_REEXPORT_TEST/REEXPORT_PROTOCOL.md  (quy trình + quy tắc đọc kết quả đã cố định trước; KHÔNG được đổi sau khi thấy kết quả)
2. P002_NhaXuong_25x80/00_PROJECT_CONTROL/DECISIONS/ADR-RQ2-008_REEXPORT_STABILITY_TEST.md
3. P002_NhaXuong_25x80/00_PROJECT_CONTROL/P002_MODEL_VERSION_REGISTRY.csv (dòng MV-RVT-20261005-47748cbe và dòng IFC)

Việc cần làm:
0. Hỏi tôi xác nhận duyệt ADR-RQ2-008 Phương án A. Khi tôi đồng ý, nối thêm mục "Human decision record" vào ADR (Approved_By: Ho Chi Han, ngày), theo mẫu ADR-RQ2-005. Không sửa nội dung cũ.
1. Tìm Revit 2027 trên máy và ghi build (phải là 27.3.0.28; nếu khác thì DỪNG và báo tôi, vì đó là yếu tố gây nhiễu).
2. Tính SHA-256 của P002_NhaXuong_25x80/models/P002_KCNX_80m_v4_APPLY_TARGET.rvt. Phải bằng
   47748cbeb460229eabd9db01ca1e3f0119ed0b195200ff971703952b93ec9624. Khác thì DỪNG.
   Nên chép RVT sang một thư mục cục bộ (không phải Google Drive) rồi mở bản chép, để Drive không đồng bộ giữa chừng.
3. Xuất IFC theo mục B của protocol: IFC 4.3 (IFC4X3_ADD2), Export base quantities BẬT, Shared Coordinates, cùng export setup như lần 1 nếu còn lưu.
   BẮT BUỘC TẮT "Store the IFC GUID in an element parameter after export". Không lưu RVT, không upgrade.
   Nếu có công cụ/MCP điều khiển Revit thì chỉ dùng thao tác đọc + export; nếu không thì hướng dẫn tôi bấm từng bước và chờ tôi báo xong.
   Tên file: P002_KCNX_80m_v4_REEXPORT_2.ifc, đặt vào P002_NhaXuong_25x80/models/.
4. Đóng Revit KHÔNG lưu, tính lại SHA-256 của RVT (phải không đổi). Ghi SHA-256 của IFC mới.
5. Chạy (Python 3, không cần thư viện ngoài):
   python P002_NhaXuong_25x80/11_REEXPORT_TEST/compare_ifc_exports.py P002_NhaXuong_25x80/models/P002_KCNX_80m_v4_APPLY_TARGET.ifc P002_NhaXuong_25x80/models/P002_KCNX_80m_v4_REEXPORT_2.ifc P002_NhaXuong_25x80/11_REEXPORT_TEST
   Kết quả ra P002_REEXPORT_SUMMARY.md và P002_REEXPORT_GLOBALID_COMPARISON.csv.
6. Viết P002_NhaXuong_25x80/11_REEXPORT_TEST/REEXPORT_RUN_RECORD.md: ngày giờ, máy, build Revit, tên export setup, các tùy chọn đã chọn (chụp màn hình hộp thoại export nếu được), hash RVT trước/sau, hash IFC mới, header có IDENTICAL không, và xếp kết quả vào R1/R2/R3 theo mục D của protocol.

Dừng ở đây và báo cáo cho tôi. CHƯA sửa registry, evidence log hay bản thảo Paper 2: các bước đó làm sau khi tôi xem kết quả (xem mục "Sau khi có kết quả" trong file prompt này).

Nguyên tắc: không sửa validator, rules, fixtures, schema hay kết quả Gate 3; không ghi gì vào RVT; báo cáo đúng kết quả quan sát được, kể cả khi bất lợi.
```

---

## Sau khi có kết quả (làm ở máy nào cũng được, không cần Revit)

1. Thêm một dòng vào `P002_MODEL_VERSION_REGISTRY.csv`: một DERIVED_EXCHANGE_MODEL thứ hai của `MV-RVT-20261005-47748cbe`, kèm hash IFC mới.
2. Nối entry E2 mới vào `00_PROJECT_CONTROL/P002_RQ2_RESEARCH_EVIDENCE_LOG.md` (EV-RQ2-044…). Log chỉ được nối thêm.
3. Nối một dòng vào `00_PROJECT_CONTROL/CHANGELOG.md`.
4. Sửa Paper 2 trong `outputs/paper2/build/v3_source.md` theo R1/R2/R3:
   - §4: kết quả nhận dạng;
   - §5.1: bằng chứng khách quan;
   - §5.5: hạn chế (2);
   - Abstract: chỉ khi kết quả là R2 hoặc R3.
5. Build lại bản thảo:
   1. `python outputs/paper2/build/build_mdpi.py`;
   2. pandoc với `--reference-doc=build/ref_mdpi.docx --resource-path=.`;
   3. Word xuất PDF.
6. Tạo `P002_WP2_FINAL_TECHNICAL_STATUS_v4.md` ghi rằng WP2 quay lại trạng thái FINAL_FROZEN.

## Trạng thái tại thời điểm tạo prompt (2026-10-07)

- Bản thảo `PAPER2_MANUSCRIPT_v3_Buildings` (.md/.docx/.pdf) đã sửa theo Rico Thirion 2026 (đã đọc toàn văn). Bản trước khi sửa nằm ở `outputs/paper2/build/_history_v3_pre_RT/`.
- Script so sánh đã tự kiểm tra: so file IFC lần 1 với chính nó cho 760/760 cấu kiện, khớp inventory, kể cả 8 cặp trùng IfcGUID.
- Việc còn mở khác:
  - Kochovski 2026 mới đọc ở mức abstract;
  - tên tác giả trong bản thảo vẫn là chỗ trống;
  - cần dán bản thảo vào template Word chính thức của MDPI Buildings;
  - `outputs/` và `P002_NhaXuong_25x80/` chưa commit; file .rvt nặng, nên đưa vào .gitignore.
