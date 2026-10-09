# CLAUDE.md — Repo luận án Data-informed Digital Twin – Limited-FEM (NCS Hồ Chí Hân)

Repo này là kho nghiên cứu, không phải phần mềm. Văn bản tiếng Việt; Markdown là nguồn, Word/PDF là bản xuất.
Khi làm trong `01_LITERATURE_REVIEW/02_TIEU_LUAN_TONG_QUAN/`, đọc thêm `CLAUDE.md` ở đó (quyết định đã khóa của tiểu luận); tệp đó thắng khi mâu thuẫn.

## Mục tiêu và phạm vi
- Tốt nghiệp sớm với **2 bài Q2/Q3** (Bài 1: cảm biến/SHM; Bài 2: truy vết, Buildings/MDPI). Việc không phục vụ trực tiếp một trong hai bài thì hoãn hoặc ghi vào "hướng phát triển". Không mở rộng tài liệu hay kiểm phản chứng ngoài nhu cầu hai bài.
- K1–K3 là giả thuyết làm việc, chỉ chốt ở Điểm duyệt 3. Kết quả Bài 1 không đưa vào tiểu luận.

## Bản đồ thư mục
- `01_LITERATURE_REVIEW/` tiểu luận, Bài 1 (`03_PAPER_1_SENSOR`), Bài 2 (`04_PAPER_2_TRACEABILITY`), kiểm soát nghiên cứu.
- `02_DATA_CODE_AND_EXPERIMENTS/` dữ liệu 3 đợt, kết quả (`OUTPUT/`), phân tích lại. `CANONICAL_THREE_CAMPAIGN_DATASET/` là bản chuẩn, không sửa.
- `04_AI_SKILL_SYSTEM/` skill của đề tài. Nguồn chính: `08_CLAUDE_SKILLS/govern-phd-evidence/`; các bản trong `_DONG_BO_*` là lịch sử, không chép thêm.
- `90_ARCHIVE/` chỉ đọc. `99_REPOSITORY_LOGS/` nhật ký.
- Gốc Git là thư mục cha `01_PHD_DT_AI_AM/`; thư mục này là thư mục con. Đường dẫn trong Git có tiền tố `00_PHD_DT_SHM_AI/`.

## Gắn skill govern-phd-evidence
Gọi skill `govern-phd-evidence` trước khi: viết hoặc sửa claim, số liệu, đóng góp, novelty; đưa kết quả vào bản thảo; xếp việc theo RQ/WP/Gate; hoặc khi yêu cầu có thể mở rộng phạm vi. Trình bày theo Claim → Evidence → Limitation → Next action. Hook trong `.claude/hooks/guard.py` nhắc điều này một lần mỗi phiên khi sửa `.md` dưới `01_LITERATURE_REVIEW/`; hook chỉ nhắc, không tự gọi skill.

## Tái lập thí nghiệm (bắt buộc cho số liệu đưa vào bản thảo)
- Mỗi thư mục kết quả có `run_manifest.json` theo mẫu `02_DATA_CODE_AND_EXPERIMENTS/_tools/run_manifest.template.json`: seed, commit của repo mã lồng nhau (`sensor_signal_analyzer/`, `signal_experiments/` nằm ngoài Git gốc), SHA-256 dữ liệu vào, kiểu chia (LORO hoặc LOCO) và danh sách fold, kiến trúc và băm checkpoint, phiên bản thư viện, dòng lệnh.
- Kiểm tra bằng `python 02_DATA_CODE_AND_EXPERIMENTS/_tools/check_run_manifest.py <thư_mục_chạy>` hoặc subagent `repro-auditor`.
- Kết quả chưa có manifest chỉ là khám phá; không trích làm bằng chứng. Không ghi đè thư mục `ddp_seed*` đã chốt: chạy lại thì tạo thư mục mới.
- Notebook commit ở trạng thái sạch (không output) và đặt seed ở đầu.

## Hook và Git
- `.claude/settings.json` bật `PreToolUse` chạy `.claude/hooks/guard.py`: chặn ghi đè tệp có sẵn trong `90_ARCHIVE`, `CANONICAL_THREE_CAMPAIGN_DATASET`, `ddp_seed*`; chạy kiểm tra commit khi Claude gọi `git commit`; không cho `--no-verify`.
- `.githooks/pre-commit` chặn tệp > 5 MB (ngoại lệ ghi ở `.githooks/allow_large.txt`), đuôi mô hình/nhị phân (`.pt .pth .joblib .npz .pkl .h5 .onnx .pdf .rvt .ifc .dwg .zip .mp4 .m4a`), chuỗi giống khóa API, notebook còn output. Cài một lần ở gốc Git: `git config core.hooksPath 00_PHD_DT_SHM_AI/.githooks`.
- Git chỉ theo dõi md, csv, json, txt và code; PDF qua Zotero, tệp lớn ở Drive.

## Lệnh thường dùng
- Xuất tiểu luận: `python 01_LITERATURE_REVIEW/02_TIEU_LUAN_TONG_QUAN/xuat_ban/build.py [tên_tệp]` (cần Zotero đang chạy; cần tệp Word mẫu của bản gốc).
- Xuất Bài 2: `01_LITERATURE_REVIEW/04_PAPER_2_TRACEABILITY/outputs/paper2/build/build_mdpi.py` (chưa kiểm tra tham số).
- Kiểm tra tham chiếu chéo tiểu luận: `revision/HT18_final_scripts/crossref_check.py`.
- Không có test tự động.

## Trích dẫn
Zotero là nguồn duy nhất cho trích dẫn. Consensus, OpenAlex, Scopus, Perplexity chỉ để gợi ý, phải xác minh trước khi đưa vào bản thảo.
