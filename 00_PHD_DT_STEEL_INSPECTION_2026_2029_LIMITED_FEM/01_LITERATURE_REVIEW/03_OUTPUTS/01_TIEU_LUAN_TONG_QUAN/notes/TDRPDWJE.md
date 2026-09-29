# TDRPDWJE — Wang & Cha (2021)

Wang Z, Cha Y-J. Unsupervised deep learning approach using a deep auto-encoder with a one-class support
vector machine to detect damage. *Structural Health Monitoring* 20(1): 406–425. DOI 10.1177/1475921720934051.

**Bản đã đọc:** bản thảo tác giả (tệp `SHMpapermanuscript_2020_05_26.pdf`, 23 tr., có ghi DOI). Số trang
dưới đây là số trang của bản thảo, không phải trang bản in.

| Cột | Nội dung |
|---|---|
| Citekey / Số cũ | TDRPDWJE / mới (bosung-5.6A) |
| Tier / Cụm | Bổ sung 5.6A / SHM–bu lông–EOV |
| Luận điểm | Có thể phát hiện hư hỏng không giám sát bằng autoencoder sâu **chỉ huấn luyện trên gia tốc đo ở trạng thái nguyên vẹn/đường cơ sở**; sai lệch giữa tín hiệu gốc và tín hiệu tái tạo (MSE, ORSR, chênh lệch cường độ Arias) làm đặc trưng nhạy hư hỏng, OC-SVM làm bộ phát hiện điểm mới (tr. 3–7). |
| Bằng chứng | Mô hình số nhà 12 tầng (giảm độ cứng 10–20 %) và cầu thép thu nhỏ trong PTN 6,0 × 0,6 × 0,72 m, liên kết chính bằng bu lông, 10 gia tốc kế, kích động búa cao su; hư hỏng là **bu lông bị nới lỏng** tại các nút chính (tr. 9–10, Bảng 2). Biến động môi trường – vận hành chỉ được mô phỏng bằng nhiễu trắng Gauss trên mô hình số (tr. 8). |
| Giới hạn | *Tác giả:* do dữ liệu huấn luyện không chứa thông tin hư hỏng, định vị và định lượng hư hỏng vẫn khó; hướng tiếp theo là kết cấu lớn đang khai thác (tr. 21). Tác giả nêu lý do phương pháp có giám sát khó dùng cho công trình: khó thu đủ dữ liệu hư hỏng; mỗi công trình có điều kiện biên và vật liệu riêng; FEM tinh chỉnh khó xây và khó kiểm chứng cho mọi kịch bản (tr. 2, 20). *NCS:* chưa có dữ liệu hiện trường có EOV thực; đánh giá theo từng vị trí cảm biến độc lập; kích động bằng búa khác kích động vận hành. |
| Tác động K1/K2/K3 | K1: mở rộng — cho thấy đầu ra của mô hình học từ đường cơ sở là một chỉ báo bất thường, phạm vi hiệu lực gắn với kết cấu và điều kiện đo cụ thể. K2, K3: không liên quan trực tiếp. |
| Vị trí sử dụng | 5.6A.3 (vai trò Autoencoder ở hiện trường); 3.6 (cầu nối PTN – hiện trường). |
| Mức đã đọc | Toàn văn phần 1 (Giới thiệu), 2 (Phương pháp), 3 (Thiết lập), 5 (Kết luận); lướt phần 4. |
