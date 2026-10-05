# Đồng bộ bốn skill PhD với CLAUDE.md của Tiểu luận tổng quan (01/10/2026)

Lý do: các skill được tạo 07–08/2026; CLAUDE.md của dự án tiểu luận được NCS duyệt và cập nhật liên tục đến 01/10/2026.
Áp dụng nguyên tắc: với việc thuộc tiểu luận, **CLAUDE.md thắng bản tóm tắt cứng trong skill**.

## Thư mục

| Thư mục / tệp | Nội dung |
|---|---|
| `project-canon-tltq.md` | Bản tóm tắt đồng bộ từ CLAUDE.md (quyết định đã khóa, K1–K3, schema đồ thị, tiền lệ bắt buộc, quy tắc trích dẫn, khuôn đọc sâu, quy tắc phản chứng, cấu trúc tiểu luận v2). Được chép vào `references/` của cả bốn skill |
| `deep-read-phd-papers/`, `phd-gap-miner/`, `govern-phd-evidence/`, `phd-literature-scout/` | Bản đã đồng bộ (đã cài vào bộ nhớ skill trên máy này) |
| `_BAN_GOC_TRUOC_DONG_BO/` | Bản cài đặt trước khi sửa, để đối chiếu hoặc khôi phục |
| `_GOI_TAI_LEN_CLAUDE_AI/*.zip` | Gói để NCS tải lên claude.ai (cập nhật skill cùng tên) |

## Thay đổi chính

| Xung đột cũ | Sửa thành |
|---|---|
| Chuỗi định danh tuyến tính là mô hình dữ liệu; "không thêm Status_Event_ID như thành phần bắt buộc" (govern) | Chuỗi định danh lõi chỉ để trình bày (chi tiết ở Phụ lục A); mô hình dữ liệu là schema đồ thị CLAUDE.md mục 8, `STATUS_EVENT` và `AGENT` bắt buộc, ràng buộc C1–C8, hai trục priority_level / Action_Status |
| Ba "locked gaps" với câu chữ 17/07 (gap-miner) | K1–K3 là giả thuyết làm việc, câu chữ theo tiểu luận mục 5.2, chốt ở ĐD3; câu chữ cũ giữ để đối chiếu; mức bảo vệ làm việc 01/10/2026 |
| Ghi kết quả vào tệp kiểm toán "KHÔNG NỘP" bên ngoài (gap-miner) | Với tiểu luận: `revision/GD2_nhat_ky_khoang_trong.md`, `revision/GD2_phan_tich_khoang_trong_*.md`, `revision/changelog.md` |
| Ghi chú đọc sâu `<year>_<author>_deep-read.md` (deep-read) | Với tiểu luận: `notes/<khóa Zotero>.md` theo khuôn 7.4 + mục 1–8, một dòng ma trận |
| Chưa có quy tắc phản chứng, ngưỡng ba căn cứ ngoài nhóm 2025–2026, tiền lệ bắt buộc (BCF 3.0, IFC4, SSN Deployment, [44]) | Đã thêm vào deep-read (Pass D), gap-miner (bước 4, locked-gaps), canon |
| Thứ tự nguồn thẩm quyền không nhắc CLAUDE.md của tiểu luận (cả bốn skill) | CLAUDE.md của tiểu luận đứng đầu đối với nội dung tiểu luận |
| Trạng thái Gate 1 viết cứng (govern) | Gắn nhãn "ảnh chụp 08/2026, xác minh lại" |
| Chưa nêu nguyên tắc AI, danh sách công cụ AI được duyệt, cấm kết quả Paper 1 | Đã thêm vào deep-read, govern, canon |

Không đổi: tường lửa FEM, bốn lớp bằng chứng, thang mức xác minh, khuôn dạy học của deep-read, quy trình discovery của scout.

## Việc NCS cần làm để thay đổi không bị ghi đè

Bản cài trên máy nằm trong bộ nhớ đệm do Claude Desktop đồng bộ từ claude.ai; lần đồng bộ sau có thể ghi đè. Để giữ lâu dài,
tải bốn gói trong `_GOI_TAI_LEN_CLAUDE_AI/` lên claude.ai (cập nhật đúng skill cùng tên). Bản gốc trong
`08_CLAUDE_SKILLS/deep-read-phd-papers/` và `08_CLAUDE_SKILLS/govern-phd-evidence/` đã được thay bằng bản đồng bộ ngày 01/10/2026
(bản cũ lưu ở `_BAN_GOC_REPO_TRUOC_THAY/`).

## Bổ sung 01/10/2026: bộ `phd-dt-research-skills`

`_phd-canon/project-canon-tltq.md` được thêm; `research-chain.md`, `novelty-boundary.md`, `gate-model.md`, `which-skill.md` và
SKILL.md của `phd-literature-evidence`, `phd-research-state`, `phd-paper-reviewer` có dòng ưu tiên ở đầu: với việc thuộc tiểu luận,
CLAUDE.md và canon tiểu luận thắng chuỗi tuyến tính, nhãn `Status_Event_ID PROPOSED` và danh sách "strong core candidates" cũ.
Bản trước khi sửa: `_BAN_GOC_TRUOC_DONG_BO/phd-dt-research-skills/`. Bộ này chưa cài vào bộ nhớ skill trên máy.
