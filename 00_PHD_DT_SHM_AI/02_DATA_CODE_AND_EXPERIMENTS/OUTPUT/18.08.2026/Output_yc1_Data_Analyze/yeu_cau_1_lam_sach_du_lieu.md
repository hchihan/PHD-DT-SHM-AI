# Yêu cầu 1 - Làm sạch dữ liệu

## Mục lục
- [Chi tiết vấn đề](#chi-tiết-vấn-đề)
- [Giải quyết](#giải-quyết)
- [Thống kê dataset sau xử lý](#thống-kê-dataset-sau-xử-lý)
- [Cơ sở lựa chọn tham số & huấn luyện](#cơ-sở-lựa-chọn-tham-số--huấn-luyện)
- [Kết quả huấn luyện](#kết-quả-huấn-luyện)

---

## Chi tiết vấn đề

### Vấn đề chung

Xóa null đối với các khúc cuối - không có data (1) và rename lại các cột (2)

**CP1:**
72 file CSV → một vài vị trí bị lẫn lộn vị trí sensor (Ra một thuật toán để xác định chỗ nào bị lẫn lộn → Clean lại data, chứng minh rằng thuật toán đáng tin)

**CP2:**
Trong bộ data thầy lấy 2 lần: Lần 1 lấy thiếu → Lấy bổ sung vào ngày 29. Ngày 2: Chỉ lấy 3 bộ dữ liệu (S0, B1, B2) không lấy B3

- 21 OK → lấy hết
- 21 không OK → 3 cái của ngày 22 (S0, B1, B2) + 1 cái của ngày 21 (B3)

**CP3:**
Không có yêu cầu

---

## Giải quyết

### CP1

Phần này đã làm vào phần `preprocessing_scripts_3/07b_detect_sensor_swap.py`, với thuật toán và hướng chứng minh ở [sensor_position_permutation_synchronization_notion](https://typhoon-storm-ff4.notion.site/sensor_position_permutation_synchronization_notion-3c04e1a58f8c8062a4f4db1ce36132de).

> Phần này nên chứng minh làm sao cho hợp lý và không loãng bài báo, hay là đưa hết vào? Vì thuật này không khó, chủ yếu là không có chứng minh sẵn dạng AIO.

### CP2

Để dễ metrics, làm cả hai bộ để xử lý cho dễ:

- **Bộ 1:** Lấy chỉ bộ 21
- **Bộ 2:** 3 cái của ngày 22 (S0, B1, B2) + 1 cái của ngày 21

### CP3

Không có yêu cầu gì khác

---

## Thống kê dataset sau xử lý

### Tổng quan 4 campaign

| Campaign | Recording | Kênh | Run | Mẫu/recording (min/med/max) | Window | Win/rec |
|---|---|---|---|---|---|---|
| cp1 | 72 | 8 | R1–R6 | 4.156 / 5.092 / 6.431 | 1.746 | 24,2 |
| cp2_21 | 72 | 12 | R7–R12 | 6.997 / 7.190 / 12.635 | 3.065 | 42,6 |
| cp2_2122 | 72 | 12 | R7–R12 | 6.997 / 7.092 / 12.231 | 3.049 | 42,3 |
| cp3 | 72 | 12 | R13–R18 | 6.030 / 6.065 / 6.106 | 2.088 | 29,0 |
| **Tổng** | **288** | | **24 run** | | | **9.948** |

### Cân bằng lớp — recording / window

| Campaign | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| cp1 | 18 / 437 | 18 / 436 | 18 / 433 | 18 / 440 |
| cp2_21 | 18 / 769 | 18 / 766 | 18 / 767 | 18 / 763 |
| cp2_2122 | 18 / 762 | 18 / 762 | 18 / 762 | 18 / 763 |
| cp3 | 18 / 522 | 18 / 522 | 18 / 522 | 18 / 522 |

Recording cân bằng tuyệt đối 18/lớp ở mọi campaign. Window lệch nhẹ (≤ 1,6%) vì recording dài ngắn khác nhau.

### Sensor

| Campaign | Cụm | Kênh | Vị trí vật lý |
|---|---|---|---|
| cp1 | 2 | 8 | Apex, BeamColumn |
| cp2_*, cp3 | 3 | 12 | Apex, BeamColumn, BraceColumn |

### Nguồn và xử lý riêng từng campaign

| Campaign | Buổi đo | Đặc điểm |
|---|---|---|
| cp1 | 1 buổi | 21/72 file lệch hoán vị → sắp lại kênh khi export |
| cp2_21 | 21/07 × 72 | Một buổi, không mượn |
| cp2_2122 | 22/07 × 54 + 21/07 × 18 | 18 recording B3 mượn từ 21/07 |
| cp3 | 1 buổi | Không cần sửa |

### Bước 02 — cắt null

270 file, 177 file bị cắt đuôi, tổng 1.171 mẫu = 0,061% dữ liệu, nhiều nhất 92 mẫu ở một file. Không file nào phải review.

### CP1 — 21 file lệch hoán vị, theo run

| R1 | R2 | R3 | R4 | R5 | R6 | Tổng |
|---|---|---|---|---|---|---|
| 6 | 6 | 1 | 2 | 4 | 2 | 21/72 |

Độ tin cậy: `pair_margin` nhỏ nhất 1,167, `sync_residual` lớn nhất 0,0000, `force_check` = agree 72/72.

### Hai điều bảng này lộ ra → Lệch

**Window/recording lệch tới 1,9×.** Đây là hệ quả của việc bỏ bước cắt cửa sổ chung 40 s:

| Campaign | Win/rec min | max | Tỉ lệ |
|---|---|---|---|
| cp1 | 19 | 31 | 1,63× |
| cp2_21 | 33 | 62 | 1,88× |
| cp2_2122 | 33 | 60 | 1,82× |
| cp3 | 29 | 29 | 1,00× |

Một recording ở cp2_21 có thể đóng góp gấp 1,88 lần recording khác cùng lớp khi train. cp3 không bị vì các recording vốn đã dài gần bằng nhau (6.030–6.106 mẫu). Muốn triệt tiêu thì hoặc đưa lại bước cắt cửa sổ chung, hoặc cân bằng ở tầng sampler.

cp2 có recording dài bất thường — max 12.635 mẫu so với median 7.190, tức gần gấp đôi. Đáng kiểm tra xem đó là file đo dài thật hay lỗi ghi, vì chính nó tạo ra phần lớn độ lệch 1,88× ở trên.

---

## Cơ sở lựa chọn tham số & huấn luyện

| Campaign | Kênh | Window train (4 run) | Fisher (tách lớp) |
|---|---|---|---|
| cp1 | 8 | 1.164 | 0,245–0,276 |
| cp2_21 | 12 | 2.043 | 0,022–0,054 |
| cp2_2122 | 12 | 2.032 | 0,022–0,054 |
| cp3 | 12 | 1.392 | 0,005–0,010 |

**Nguyên tắc:** giữ nguyên lịch huấn luyện (lr, batch, epochs, patience) cho mọi campaign để so sánh chéo được, chỉ scale sức chứa mô hình theo lượng dữ liệu và siết regularization theo độ yếu của tín hiệu.

| Campaign | 1dcnn fc-dim/dropout | resnet n-feature-maps | weight-decay | lr |
|---|---|---|---|---|
| cp1 | 64 / 0.5 | 16 | 1e-2 | 3e-4 |
| cp2_21 | 128 / 0.5 | 32 | 1e-2 | 3e-4 |
| cp2_2122 | 128 / 0.5 | 32 | 1e-2 | 3e-4 |
| cp3 | 64 / 0.5 | 16 | 3e-2 | 2e-4 |

cp2 có gần gấp đôi dữ liệu cp1 nên chịu được head to hơn; cp3 tín hiệu yếu nhất nên siết mạnh nhất.

---

## Kết quả huấn luyện

Xem chi tiết tại: https://www.kaggle.com/code/platformciviltwin/3rd-dataset-v5-training/output?scriptVersionId=343135195
