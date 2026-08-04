# MODEL ROUTING GUIDE

| Nhiệm vụ | Mô hình ưu tiên | Lý do |
|---|---|---|
| Đọc kỹ PDF đã nạp | NotebookLM | Bám nguồn, trích trang và hình |
| Phân tích folder/file/code | Claude Code | Có khả năng thao tác và tạo file |
| Tìm paper, luật, tin mới | Perplexity | Tìm kiếm và kiểm chứng web |
| Viết, tổng hợp, phản biện | ChatGPT / Claude / Gemini | Mạnh về lập luận và biên tập |
| Tạo ảnh hoặc chỉnh ảnh | Image model | Đầu ra trực quan |
| Word/Excel/PPT/PDF | Office agent hoặc ChatGPT có công cụ | Tạo artifact trực tiếp |

## Quy tắc chọn

1. Dùng NotebookLM khi câu trả lời phải nằm trong nguồn đã nạp.
2. Dùng Claude Code khi nhiệm vụ cần đọc nhiều file, chạy mã hoặc tạo output trong folder.
3. Dùng Perplexity khi dữ liệu có thể thay đổi hoặc cần nguồn web mới.
4. Dùng ChatGPT/Claude/Gemini khi cần lập luận, biên tập và tổng hợp đa mục tiêu.
5. Dùng chuỗi nhiều mô hình chỉ khi mỗi mô hình có vai trò rõ:
   - Perplexity tìm nguồn.
   - NotebookLM deep-read.
   - Claude Code xử lý dữ liệu.
   - ChatGPT tổng hợp và phản biện.
