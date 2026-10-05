# YÊU CẦU CẬP NHẬT WEBSITE `bim.aac79.com.vn`
**Mục đích:** chuyển website từ định dạng "SaaS BIM/IFC viewer thương mại" sang **bản trình diễn (demo) học thuật cho luận án PhD Digital Twin**, đúng phạm vi đã khóa trong Charter nghiên cứu.
**Ngày:** 27/07/2026 | **Người yêu cầu:** Han (chủ nhiệm đề tài) | **Đối tượng đọc:** IT/developer phụ trách site

---

## 1. Bối cảnh — tại sao phải đổi hướng

Site hiện tại là landing page kiểu SaaS thương mại (gói Free/Pro/Enterprise, đăng ký/đăng nhập, chia sẻ public link, đo đạc/QTO...). Đây không phải mục tiêu của site trong giai đoạn này.

Mục tiêu thật của site: **trình diễn khung Digital Twin dựa trên dữ liệu** đang được phát triển trong luận án — cụ thể là minh hoạ được **chuỗi truy vết thông tin** đi từ dữ liệu cảm biến đến hành động kiểm tra – bảo trì, có thể cho hội đồng, giảng viên hướng dẫn, hoặc đơn vị quản lý công trình xem trực tiếp **mà không cần đăng ký tài khoản**.

Do đó: **bỏ toàn bộ lớp "sản phẩm thương mại" (đăng ký, đăng nhập, gói giá, phân quyền nhóm), giữ lại phần lõi kỹ thuật xem mô hình 3D/IFC, và xây thêm lớp nội dung/chức năng thể hiện đúng chuỗi nghiên cứu.**

---

## 2. Chuỗi nghiên cứu và chuỗi định danh (bắt buộc bám sát — không tự diễn giải khác)

Đây là "sự thật nguồn" (source of truth) lấy từ Charter đã khóa của đề tài. Toàn bộ nội dung, nhãn, sơ đồ trên site phải nhất quán với đúng thuật ngữ này:

```
Dữ liệu dao động
→ condition/state-change evidence (+ CEI)
→ BIM-linked component
→ inspection record
→ justified, accountable inspection–maintenance action
```

Chuỗi định danh kỹ thuật (identifier chain) — đây là thứ site cần *hiển thị được*, không chỉ mô tả bằng lời:

```
Sensor_ID → BIM_GUID → Condition_Evidence_ID → Inspection_Record_ID → Action_Record_ID
```

Ghi chú thuật ngữ quan trọng cho dev:
- **CEI** (Confidence/Evidence Indicator) là một *thuộc tính metadata* của `Condition_Evidence_ID` — **không phải** một điểm số mức độ hư hỏng (severity/Health Index). Tuyệt đối không hiển thị CEI như thanh "sức khoẻ công trình" hay điểm số tổng hợp.
- **Action_Status** là thuộc tính của `Action_Record_ID`, không phải một mắt xích riêng trong chuỗi.
- **`FEM_Node_ID`** chỉ là metadata *tuỳ chọn*, không bao giờ là mắt xích bắt buộc trong chuỗi truy vết.
- Logic hành động chỉ có **4 mức, đơn giản, có con người rà soát**: `Normal → Watch → Inspect → Priority Inspection`. Không dựng thang điểm phức tạp hơn.

---

## 3. Phần cần GỠ BỎ hoặc ẩn khỏi bản demo

- Toàn bộ luồng **Đăng ký / Đăng nhập** (`/auth/register`, `/auth/login`) và nút CTA liên quan ("Bắt đầu miễn phí ngay", "Đăng ký", "Đăng nhập" trên header).
- Trang **Bảng giá** (`/pricing`) và mọi nhắc đến gói Free/Pro/Enterprise, giá VNĐ.
- Tính năng **"Cộng tác & phối hợp nhóm"** (mời thành viên, phân quyền Chỉ xem/Chỉnh sửa) — đây là logic multi-tenant SaaS, không cần cho demo học thuật một-chiều.
- Tính năng **"Chia sẻ bản vẽ 3D bằng đường link"** ở dạng public-link-cho-khách-hàng — có thể giữ lại về mặt kỹ thuật (hữu ích để gửi link cho hội đồng) nhưng đổi khung diễn giải (xem mục 5).
- Mọi câu chữ mang giọng điệu marketing thương mại ("siêu tốc", "1 cú nhấp chuột", "trải nghiệm ngay hôm nay"...) — thay bằng văn phong mô tả học thuật, khách quan, không cường điệu.

**Không xoá code/tính năng vĩnh viễn nếu không cần thiết** — có thể tắt qua feature flag/ẩn route, để không mất công sức đã làm nếu sau này cần dùng lại cho mục đích khác.

---

## 4. Phần lõi kỹ thuật cần GIỮ LẠI (đổi khung diễn giải, không đổi engine)

- **Trình xem 3D IFC** (nền tảng 3D Fragments / web-ifc) — đây là engine đúng hướng, giữ nguyên.
- **Mặt cắt, đo đạc, bóc tách khối lượng (QTO)** — hữu ích để minh hoạ Lớp 3 (field feasibility: vị trí cấu kiện, bố trí cảm biến tham chiếu mô hình danh nghĩa). Giữ lại nhưng gắn vào đúng ngữ cảnh nghiên cứu thay vì "cho nhà thầu bóc khối lượng dự toán".
- **Lịch sử phiên bản IFC** — đổi định hướng thuật ngữ sang mô hình trạng thái CDE theo ISO 19650 (xem mục 5.3), thay vì "version history" chung chung kiểu Git.

---

## 5. Phần cần XÂY MỚI — ưu tiên cao nhất

### 5.1. Module "Chuỗi truy vết" (Traceability Demo) — **việc quan trọng nhất, làm trước**

Đây là phần hiện hoàn toàn chưa có trên site và là nội dung khoa học cốt lõi của luận án. Yêu cầu chức năng tối thiểu (MVP):

1. Người dùng chọn một cấu kiện trong mô hình 3D (ví dụ một liên kết khung thép trong mô hình 1:10 hoặc công trình thực).
2. Site hiển thị `BIM_GUID` của cấu kiện đó.
3. Từ `BIM_GUID`, hiển thị `Sensor_ID` liên kết (nếu có cảm biến gắn tại/gần cấu kiện).
4. Hiển thị `Condition_Evidence_ID` gần nhất liên quan, kèm **CEI dưới dạng metadata có cấu trúc** (không phải điểm số đơn — ví dụ hiển thị dạng bảng: nguồn dữ liệu, thời điểm, độ tin cậy định tính, ghi chú), tuyệt đối không vẽ thành gauge/severity score.
5. Hiển thị `Inspection_Record_ID` liên quan (nếu đã có hồ sơ kiểm tra).
6. Hiển thị `Action_Status` hiện tại theo đúng 4 mức: Normal / Watch / Inspect / Priority Inspection — có ghi chú rõ "quyết định cuối do người quản lý xác nhận", không tự động hoá.

Dữ liệu cho module này ban đầu có thể là **dữ liệu mẫu/demo tĩnh** (2–3 kịch bản truy vết mẫu) — không cần kết nối hệ thống cảm biến thời gian thực ở giai đoạn này. Yêu cầu: dữ liệu mẫu phải khớp với cấu trúc identifier ở mục 2, để sau này có thể thay bằng dữ liệu thật mà không phải sửa lại giao diện.

### 5.2. Trang "Về dự án nghiên cứu" (`/nghien-cuu` hoặc `/about`)

Nội dung bắt buộc có:
- Tên đề tài (VN + EN) — lấy nguyên văn từ Charter mục 1.
- Một câu tóm tắt vấn đề nghiên cứu (Charter mục 4).
- Sơ đồ 4 lớp kiến trúc (Lab evidence → Traceability → Field feasibility → Inspection-maintenance support).
- **Disclaimer bắt buộc về vai trò FEM** (nguyên văn, không diễn giải lại theo hướng khác):
  > "Mô hình phần tử hữu hạn (FEM) trong hệ thống này chỉ đóng vai trò mô hình thiết kế tham chiếu danh nghĩa (nominal, uncalibrated, reference-only). FEM không được sử dụng để chẩn đoán hư hỏng, không suy luận mức suy giảm độ cứng hay lực siết bu lông, và không có kết luận nào từ FEM được chuyển trực tiếp sang công trình thực."
- Ghi chú trạng thái: đây là bản demo nghiên cứu đang phát triển (work-in-progress), không phải sản phẩm thương mại hoàn chỉnh.

### 5.3. Đổi thuật ngữ "Lịch sử phiên bản" sang mô hình trạng thái CDE (ISO 19650)

Thay nhãn trạng thái file/mô hình từ kiểu version-history chung chung sang các trạng thái chuẩn CDE: **WIP (Work in Progress) / Shared / Published / Archived**, có thể thêm mã status/suitability nếu dữ liệu cho phép. Đây là điểm cộng học thuật quan trọng vì Charter tham chiếu trực tiếp ISO 19650.

---

## 6. Yêu cầu kỹ thuật/UX khác (mức độ ưu tiên thấp hơn, làm sau khi xong mục 5)

- **Trang `/pricing` (nếu tạm giữ code):** có độ trễ vài giây với spinner trắng trước khi hiển thị nội dung — cần bỏ (do gỡ trang) hoặc nếu vẫn cần thì tối ưu lại (dữ liệu tĩnh không cần chờ fetch).
- **Ảnh minh hoạ ở hero trang chủ:** hiện là khung xám placeholder (chưa có ảnh/video thật) — thay bằng ảnh chụp màn hình thật hoặc GIF ngắn của trình xem 3D đang hoạt động với mô hình thật của đề tài (khung thép 1:10 hoặc kho công nghiệp 25×80m).
- **SEO/metadata:** `<title>` hiện chỉ là "BIM Viewer" chung chung, chưa có `<meta name="description">` hay Open Graph tags — bổ sung để khi chia sẻ link (email, Zalo) cho hội đồng/giảng viên hiển thị đúng ngữ cảnh nghiên cứu.
- **Footer:** hiện chỉ có bản quyền + link điều hướng trùng lặp — bổ sung: liên hệ tác giả, đơn vị/trường, link về trang "Về dự án nghiên cứu", (tuỳ chọn) link tới bài báo/luận án nếu đã công bố.
- **Ngôn ngữ:** kiểm tra nút chuyển "EN" có thực sự chuyển nội dung sang tiếng Anh đầy đủ hay chỉ là nút trang trí — nếu chưa hoàn chỉnh, hoặc hoàn thiện bản EN hoặc tạm ẩn nút.

---

## 7. Việc TUYỆT ĐỐI KHÔNG được làm trên site (đúng phạm vi luận án đã khóa)

Không thêm bất kỳ nội dung/chức năng nào ngụ ý các hướng sau (nằm ngoài phạm vi Charter, kể cả ở dạng "demo minh hoạ"):
- Hiệu chuẩn FEM, MAC, suy giảm độ cứng, dự đoán RUL, bảo trì dự đoán (predictive maintenance).
- Chẩn đoán hư hỏng hiện trường khi chưa có kiểm tra xác nhận thực tế.
- Health Index dạng điểm số tổng hợp trọng số, "tối ưu vị trí cảm biến" (optimal sensor placement), bảo trì tự động hoàn toàn không người rà soát.
- Ngôn ngữ định vị site như phần mềm thương mại hoàn chỉnh, Smart City, Edge AI, CFD.

Nếu trong quá trình phát triển phát sinh nhu cầu thêm tính năng ngoài danh sách ở mục 5, cần hỏi lại người yêu cầu trước khi triển khai — không tự quyết định mở rộng phạm vi.

---

## 8. Tiêu chí nghiệm thu (Definition of Done)

- [ ] Không còn luồng đăng ký/đăng nhập/bảng giá hiển thị công khai trên site.
- [ ] Trang chủ dẫn thẳng vào trình xem 3D hoặc trang "Về dự án nghiên cứu", không yêu cầu tài khoản.
- [ ] Module Chuỗi truy vết chạy được với ít nhất 2–3 kịch bản mẫu, hiển thị đủ 5 mắt xích định danh + CEI dạng metadata + Action_Status 4 mức.
- [ ] Trang "Về dự án nghiên cứu" có đủ: tên đề tài, sơ đồ 4 lớp, disclaimer FEM nguyên văn.
- [ ] Thuật ngữ "phiên bản" đổi sang trạng thái CDE (WIP/Shared/Published/Archived).
- [ ] Không còn câu chữ mang giọng điệu SaaS thương mại.
- [ ] Ảnh hero là ảnh/video thật, không còn placeholder xám.
- [ ] Có `<title>`, meta description, Open Graph cơ bản.
- [ ] Footer có thông tin liên hệ/đơn vị nghiên cứu.

---

*Tài liệu này dùng để bàn giao cho IT/developer. Khi có thay đổi định hướng nghiên cứu (ví dụ khi Gate 1/2 đóng), cần cập nhật lại tài liệu này trước khi yêu cầu sửa site tiếp — không sửa site theo yêu cầu miệng không có văn bản đối chiếu.*
