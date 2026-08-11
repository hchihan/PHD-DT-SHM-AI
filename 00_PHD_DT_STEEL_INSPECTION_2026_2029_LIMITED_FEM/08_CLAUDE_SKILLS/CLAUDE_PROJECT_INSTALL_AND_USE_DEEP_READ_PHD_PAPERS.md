# Cài đặt và sử dụng Deep Read PhD Papers trong Claude Project

## 1. Hiểu đúng ba lớp

| Thành phần | Vai trò |
|---|---|
| Skill `Deep Read PhD Papers` | Quy trình đọc sâu, phản biện, giảng dạy và định tuyến luận án |
| Claude Project | Không gian làm việc giữ hướng dẫn và knowledge của luận án |
| PDF paper + tài liệu quản trị | Bằng chứng thực tế mà skill phải đọc; không được thay bằng trí nhớ của AI |

Skill không chứa trạng thái tiến độ cố định. Vì vậy, phải giữ các tài liệu quản trị hiện hành trong Project knowledge.

## 2. Cài skill vào tài khoản Claude

1. Vào **Settings → Capabilities** và bật **Code execution and file creation**.
2. Vào **Customize → Skills**.
3. Nhấn **+ → Create skill → Upload a skill**.
4. Chọn file `deep-read-phd-papers-claude.zip`.
5. Sau khi tải xong, bật skill trong danh sách Skills.

Gói ZIP đã đúng cấu trúc Claude yêu cầu:

```text
deep-read-phd-papers-claude.zip
└── deep-read-phd-papers/
    ├── skill.md
    ├── references/
    └── scripts/
```

Tài liệu chính thức: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) và [How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

## 3. Chuẩn bị Claude Project luận án

Trong Project `PHD DT - Limited-FEM 2026–2029`, tải vào **Project knowledge** tám file:

1. `MASTER_RESEARCH_CHARTER.md`
2. `MASTER_RESEARCH_CHARTER_v1.1_LIMITED_FEM_20260717.md`
3. `RESEARCH_DIRECTION_AND_SCOPE.md`
4. `RESEARCH_ARCHITECTURE.md`
5. `CURRENT_STATUS_AND_NEXT_DIRECTION.md`
6. `RESEARCH_ARCHITECTURE_DECISION_RECORD_20260717.md`
7. `THE_COUNCIL_REVIEW_FEM_OR_NO_FEM_17.07.2026.md`
8. `00_README_START_HERE.md`

Khi có evidence pack hoặc Gate report mới, bổ sung vào Project và thay file trạng thái cũ bằng bản đã được xác nhận. Project knowledge là nơi lưu sự thật nghiên cứu; skill chỉ quản trị cách đọc và suy luận.

Claude Projects dùng knowledge và project instructions làm ngữ cảnh cho các chat trong cùng Project: [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects).

## 4. Project instructions tối thiểu

Thêm đoạn sau vào Project instructions nếu chưa có quy tắc tương đương:

```text
Đối với mọi nhiệm vụ đọc paper thuộc luận án, hãy sử dụng skill deep-read-phd-papers.
Trước khi kết luận về luận án, phải đọc nguồn quản trị liên quan trong Project knowledge.
ADR đã chấp thuận kiểm soát kiến trúc Limited-FEM; Charter v1.1 kiểm soát ranh giới FEM;
CURRENT_STATUS_AND_NEXT_DIRECTION hoặc Gate report mới nhất kiểm soát tiến độ động.
Không suy diễn trạng thái từ tên file hoặc trí nhớ cuộc trò chuyện.
Trả lời bằng tiếng Việt, phân biệt SOURCE-VERIFIED, TUTOR-EXPLANATION và THESIS-APPLICATION.
```

## 5. Cách dùng hằng ngày

### Đọc sâu và định tuyến

Đính kèm PDF vào chat trong Project rồi dùng:

```text
Hãy dùng Deep Read PhD Papers ở chế độ AUDIT.
Đọc sâu paper đính kèm, kiểm chứng research gap, phương pháp, dữ liệu,
validation, kết quả, limitations và future work trên PDF gốc.
Sau đó định tuyến vào RQ–WP–Chương–Paper–Evidence Gate và nêu next action.
```

### Yêu cầu giáo sư giảng lại

```text
Hãy dùng Deep Read PhD Papers ở chế độ PROFESSOR.
Giảng paper này cho tôi theo ba tầng: trực giác, cơ chế phương pháp,
và phản biện ở mức bảo vệ PhD. Tập trung vào [khái niệm/phương pháp].
Phân biệt rõ nội dung của tác giả, lời thầy giải thích và cách vận dụng vào luận án.
```

### Học tương tác

```text
Hãy dùng Deep Read PhD Papers ở chế độ INTERACTIVE.
Giảng cho tôi từng phần, mỗi lần chỉ hỏi một câu.
Chờ tôi trả lời, chỉ ra chỗ hiểu sai bằng bằng chứng rồi mới chuyển sang phần tiếp theo.
```

### Báo cáo hoàn chỉnh để lưu

```text
Hãy dùng Deep Read PhD Papers ở chế độ FULL.
Tạo hồ sơ deep-read hoàn chỉnh A–N, có locator theo trang/section/table/figure,
ma trận Claim → Evidence → Limitation → Next action và phần giảng dạy như giáo sư hướng dẫn.
```

### Tổng hợp nhiều paper

```text
Đọc độc lập từng paper trước, không để diễn giải của paper trước làm nhiễm paper sau.
Sau đó tạo cross-paper synthesis, phân biệt convergence, disagreement,
candidate gap và nội dung cần tìm thêm. Không tuyên bố research gap chỉ từ một paper.
```

## 6. Quy trình nên dùng cho mỗi paper

1. Đính kèm PDF gốc; Markdown chỉ là bản dẫn xuất hỗ trợ tìm kiếm.
2. Chạy `AUDIT` để tạo hồ sơ bằng chứng.
3. Chọn một phần khó và chạy `PROFESSOR`.
4. Chạy `INTERACTIVE` để kiểm tra mức hiểu.
5. Chỉ sau đó mới quyết định `CITE`, `ADAPT`, `BENCHMARK`, `AVOID` hoặc `DEFER/REJECT`.
6. Lưu record đã xác minh; mọi số liệu quan trọng phải có locator về PDF.

## 7. Dấu hiệu skill đang hoạt động đúng

- Không chỉ tóm tắt abstract.
- Phân biệt lời tác giả với lời giải thích và ứng dụng luận án.
- Nêu đơn vị phân tích, split/grouping, validation và claim boundary.
- Không biến lab classification thành field diagnosis.
- Không phục hồi FEM lõi hoặc predictive maintenance.
- Không dùng một paper để khẳng định khoảng trống toàn văn liệu.
- Hỏi lại đúng một câu trong chế độ tương tác.
- Ghi `Evidence is currently insufficient.` khi thiếu căn cứ.

## 8. Nếu Claude không tự dùng skill

1. Kiểm tra skill đã được bật trong **Customize → Skills**.
2. Mở đầu prompt bằng: `Hãy dùng Deep Read PhD Papers...`.
3. Kiểm tra PDF và tài liệu quản trị đã nằm trong đúng Project.
4. Nếu vẫn không kích hoạt, kiểm tra `description` của skill và tải lại đúng file ZIP, không giải nén trước khi upload.
