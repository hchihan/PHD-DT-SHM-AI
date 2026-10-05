# Yêu cầu 3 - Kiểm tra chéo của các đợt chạy

Vì target đã là campaign khác, distribution shift đã được tạo ra ở cấp campaign rồi. Nên hiện tại, không còn cần thuật toán chọn một Run "khó" để tạo shift nữa.

## Phase 1

| # | Train | Val | Test | e_shift |
|---|-------|-----|------|---------|
| 1 | cp2_21 R7–11 | R12 | cp3 R13–18 | 1.4988 |
| 2 | cp2_2122 R7–11 | R12 | cp3 R13–18 | 1.0848 |
| 3 | cp3 R13–17 | R18 | cp2_21 R7–12 | 1.5399 |
| 4 | cp3 R13–17 | R18 | cp2_2122 R7–12 | 1.0902 |

## Kết quả

https://www.kaggle.com/code/platformciviltwin/3rd-dataset-v5-cross-campaign?scriptVersionId=343174171

## Phase 2
