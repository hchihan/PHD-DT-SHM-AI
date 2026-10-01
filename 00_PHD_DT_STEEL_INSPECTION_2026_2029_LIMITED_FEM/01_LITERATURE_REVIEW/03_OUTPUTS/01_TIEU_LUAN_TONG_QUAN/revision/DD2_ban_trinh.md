# Bản trình Điểm duyệt 2 (ĐD2) — Đọc sâu tài liệu key

Lập ngày 01/10/2026. Trạng thái: **trình có điều kiện** — 29/30 tài liệu đã đọc toàn văn; [80] Bull 2025 chờ PDF
(`viec_cho_NCS.md` N-01). Theo CLAUDE.md mục 6, ĐD2 là bước NCS kiểm cột "Giới hạn" của ma trận. Mọi việc NCS cần làm
được gom ở `revision/viec_cho_NCS.md`; bản này chỉ tổng hợp để NCS quyết định.

## 1. Sản phẩm GĐ2

| Sản phẩm | Trạng thái | Tệp |
|---|---|---|
| Ma trận tài liệu key | 29/30 dòng đủ cột; dòng 22 ([80]) trống | `matrix/literature_matrix.csv` |
| Ghi chú đọc sâu | 29 tài liệu key + 9 nguồn phản chứng/bổ sung | `notes/` |
| Ba bảng ánh xạ thực thể với [2], [35], [44] | Xong (T1-1) | `mapping/theiler2018.md`, `bellon2025.md`, `garcia2026.md` |
| Nhật ký ứng viên khoảng trống (UV-01 – UV-08) | Cập nhật đến 01/10/2026 | `revision/GD2_nhat_ky_khoang_trong.md` |
| Kế hoạch đọc, tiến độ phiên | T1-1 – T1-4, T2-1 – T2-4 xong | `revision/GD2_ke_hoach_doc.md` |

Nguồn phản chứng/bổ sung đã đọc toàn văn ngoài 30 key: Cross 2011 `KPWFC4PI`, Graybeal 2002 `8IMKCTE5`, Phares 2004
`J7FAWJ8I`, Gardner 2021 `GXVWFUSA`, Papic & Cerovsek 2019 `EKAT6IMC` (Sepasgozar 2021 [9] `XVLWEXVZ`, Eraliev 2022 `VVBGM9EN`; cùng Bull 2022, Wang & Cha 2021 đọc ở phiên 5.6A).

## 2. Ma trận: phân bố và việc kiểm

**Phân bố theo cụm (29 dòng đã điền + [80]):** SHM–bu lông–EOV 10 · Truy vết thông tin 8 · Song sinh số 5 · Giá trị quyết
định 4 (gồm [80]) · Độ tin cậy đánh giá 3.

**Phiên bản đọc khác bản in** (trang dẫn theo bản đã đọc, cần đối chiếu trước GĐ6 — N-04): [19] arXiv v1 · Hughes 2022 arXiv v2 ·
[28] arXiv v2 · [14] bản thảo tác giả arXiv v3 · [16] bản in thử · Cawley 2018 bản trực tuyến.

**Tài liệu 2025–2026 trong 30 key** (CLAUDE.md 4.1: không để khoảng trống dựa chủ yếu vào nhóm này): [35] Bellon 2025,
[44] García 2026, [17] Wu 2026, [19] Ramasso 2025 (tiền in), [82] Seiß 2025, [80] Bull 2025.

**Dòng cần NCS kiểm (N-10):** 28 dòng mang dấu "CẦN NCS KIỂM" — tất cả trừ dòng 13 ([45] Sohn), 14 (Figueiredo 2011) và 22 (chưa điền). Dòng 13–14 đã bỏ dấu ở phiên T2-1
khi đọc bổ sung thành toàn văn, nhưng **chưa được NCS kiểm** — nên kiểm cùng (tổng 30 dòng khi có [80]). Gợi ý thứ tự kiểm theo mức ảnh hưởng tới khoảng trống:

| Ưu tiên | Dòng | Lý do |
|---|---|---|
| 1 | 1–3 ([2], [35], [44]), 11–12 ([16], [17]) | Tiền lệ trực tiếp cho K2, K3 và schema 5.5 |
| 2 | 5–6 ([18], [19]), 18–20 ([56], [57], [48]), 23–24 ([14], [15]) | Căn cứ và phản chứng của UV-06 (K1) |
| 3 | 7–10 ([8], [7], [3], [53]), 21 (Hughes), 25 ([28]) | Căn cứ của UV-02, UV-05, UV-07 |
| 4 | Các dòng còn lại | Bối cảnh, định vị, luận điểm 3.2 |

Khi kiểm cột Giới hạn, NCS xem hai điều: (i) phần ghi "Tác giả" có đúng là tác giả tự nêu (có trang); (ii) phần "NCS" có
đúng là nhận định mình chấp nhận, hay cần sửa/xóa.

## 3. Tình trạng ứng viên khoảng trống (đầu vào cho GĐ3)

Quy tắc 7.4: một ứng viên chỉ vào GĐ3 khi trường "Phản chứng đã kiểm" không còn mục "chưa kiểm". Ngưỡng GĐ3: ≥ 3 căn cứ
không thuộc nhóm 2025–2026.

| Mã | Giả thuyết | Căn cứ độc lập (trước 2025) | Phản chứng | Vào GĐ3? | Phần còn lại sau thu hẹp (rút gọn) |
|---|---|---|---|---|---|
| UV-01 | K3 | 4 (3) | Còn **CMMS** chưa kiểm (N-20) | Chưa | Bằng chứng có nguồn gốc và phạm vi hiệu lực đi vào chuỗi kiểm tra – cấu kiện – hành động; mỗi lần đổi trạng thái là sự kiện có căn cứ và thẩm quyền |
| UV-02 | K1 | 4 (4) | Còn thẻ mô hình, PROV-O, MLflow/DVC (N-21) | Chưa | Bản ghi cho **từng** kết quả sinh từ dữ liệu đo, mang cùng lúc nguồn gốc xử lý, phiên bản phương pháp, phạm vi hiệu lực |
| UV-03 | K2 | 3 (3) | Đã kiểm hết | **Đủ điều kiện** | Khoảng hiệu lực bắt buộc trên quan hệ cảm biến – cấu kiện, lịch sử, ràng buộc C3. [NCS] Nên coi là yêu cầu mô hình dữ liệu hơn là khoảng trống độc lập |
| UV-04 | định vị | 2 | **Đã kiểm hết** ([10], Papic 2019 một phần; [9], [29], [42] không) | Không dự kiến (chỉ định vị) | Chưa nguồn nào áp ba mức DM/DS/DT của [8] cho kiểm tra – bảo trì kết cấu có kỹ sư quyết định; luận án khai báo mức theo [8] |
| UV-05 | mới (nhãn hiện trường) | 5 nhóm (3); +[28]? (N-12) | **Đã kiểm hết** (01/10/2026) | **Đủ điều kiện** | Nhãn sinh từ kiểm tra thực ở công trình vận hành, mang độ bất định của kiểm tra, ghi như bản ghi gắn phép đo đã kích hoạt và cấu kiện. [NCS] Gần UV-07, K3 — có thể gộp |
| UV-06 | K1 | 4 (3), [56] gián tiếp; 1 dữ liệu ngược chiều một phần ([48]) | Còn theo dõi dài hạn sau bảo trì (N-23) | Chưa | Xem đề xuất phát biểu thu hẹp ở mục 4 |
| UV-07 | K3 (+5.6A) | 4 (3) | Còn human-in-the-loop, thẻ mô hình (N-24) | Chưa | Dự kiến: áp khuôn phê duyệt (IFC4, [44]) cho đầu ra AI và tách khỏi việc dùng làm nhãn |
| UV-08 | mới (L2.2) | 3 nhóm cho EOV chung; 0 cho nhà xưởng | Còn toàn văn Hu 2023 (N-25); Eraliev 2022 đã kiểm, không giải quyết | [NCS] Đề xuất không thành K4 | Giữ làm luận điểm 3.2 và yêu cầu nội dung của K1 (trạng thái cầu trục, máy móc trong bối cảnh quan trắc) |

**Đọc nhanh:** hiện có hai ứng viên đủ điều kiện hình thức (UV-03, UV-05); UV-04 đã kiểm hết nhưng chỉ dùng để định vị. Bốn ứng viên chính còn lại (UV-01, UV-02, UV-06,
UV-07) mỗi ứng viên còn một nhóm phản chứng; cả bốn đều đã đủ số căn cứ trước 2025. Việc còn thiếu chủ yếu là tìm và đọc
1–2 nguồn cho mỗi nhóm (N-20, N-21, N-23, N-24).

## 4. Đề xuất phát biểu thu hẹp cho UV-06 (mới, chờ NCS)

Sau khi kiểm Cross 2011, [57], [56], [48], [14], [15], Gardner 2021:
"Đã biết rằng kết quả rút từ dữ liệu dao động của mối nối bu lông phụ thuộc lần lắp ráp và mẫu kết cấu ([18], [19]; [56]
gián tiếp), và đánh giá phải tách theo đơn vị độc lập ([53]; [14], [15] cùng chiều). Các hướng xử lý hiện có hoặc chuyển giao
giữa các kết cấu ([56], Gardner 2021), hoặc đưa thay đổi do vận hành, bảo trì vào trạng thái bình thường ([57]). Phần chưa thấy:
ghi lần lắp ráp và lần can thiệp như một thành phần bắt buộc của phạm vi hiệu lực, để kiểm được một bằng chứng có còn dùng được
sau can thiệp hay không." Có một dữ liệu ngược chiều một phần: ca siết lại của [48] vẫn được phân loại đúng (tr. 9–10), nên
phát biểu nói "phải ghi để kiểm được", không nói "luôn làm mất hiệu lực".

## 5. Quyết định NCS cần đưa ra tại ĐD2

1. Chấp nhận ma trận (sau khi kiểm N-10) và ba bảng ánh xạ.
2. Cho GĐ3 bắt đầu khi [80] còn thiếu: đề xuất **có** — [80] thuộc cụm Giá trị quyết định, không phải căn cứ hay phản chứng
   của ứng viên nào trong nhật ký; đọc bổ sung khi có PDF.
3. Cách xử lý bốn nhóm phản chứng còn mở: cho phép Claude tìm, xác minh, nhập Zotero 1–2 nguồn mỗi nhóm (N-21, N-23, N-24),
   hoặc NCS cung cấp nguồn.
4. Quyết định về UV-04 (chỉ định vị), UV-08 (không thành K4), và gộp UV-05 với UV-07 khi gom cụm ở GĐ3.
5. Ba câu hỏi về mức căn cứ ở N-12.
