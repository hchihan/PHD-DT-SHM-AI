# Yêu cầu 2 \- Đảo lại các run trong cùng CP → chạy thử ra kết quả

## Thuật toán được lựa chọn

### Support Points / SPlit

Support Points của Mak & Joseph được xây đúng cho bài toán:

> Có một tập điểm X, hãy lấy ra một tập con nhỏ sao cho tập con đó đại diện tốt nhất cho phân bố của toàn bộ tập.

Họ định nghĩa việc "đại diện tốt" bằng **energy distance**, và có kết quả lý thuyết về việc các support points hội tụ về distribution gốc.

Sau đó Joseph & Vakayil đưa nó thành thuật toán **SPlit**, dùng trực tiếp để chọn các subset train/test. Paper báo cáo rằng cách chia này cải thiện cả worst-case testing performance so với random split trên nhiều mô hình.

Link bài báo: [https://arxiv.org/abs/2012.10945](https://arxiv.org/abs/2012.10945)

## Chi tiết cách áp dụng

Selecting Run permutations worth training, with Support Points / SPlit

## Kết quả sau khi áp dụng

### CP1 — 6 split được chọn

| Vai trò | Val run | Test run | Train runs |
| :---- | :---- | :---- | :---- |
| representative | 1 | 3 | 2, 4, 5, 6 |
| worst\_case | 2 | 1 | 3, 4, 5, 6 |
| coverage | 2 | 4 | 1, 3, 5, 6 |
| coverage | 5 | 6 | 1, 2, 3, 4 |
| coverage | 6 | 1 | 2, 3, 4, 5 |
| coverage | 6 | 2 | 1, 3, 4, 5 |

### CP2-21 — 6 split được chọn

| Split | Role | Train | Val | Test |
| :---- | :---- | :---- | :---- | :---- |
| 1 | coverage | 8,10,11,12 | 7 | 9 |
| 2 | representative | 8,9,11,12 | 7 | 10 |
| 3 | coverage | 9,10,11,12 | 8 | 7 |
| 4 | coverage | 7,10,11,12 | 9 | 8 |
| 5 | coverage | 7,8,9,12 | 11 | 10 |
| 6 | worst\_case | 7,8,10,11 | 12 | 9 |

### CP2-2122 — 6 split được chọn

| Split | Role | Train | Val | Test |
| :---- | :---- | :---- | :---- | :---- |
| 1 | coverage | 9,10,11,12 | 7 | 8 |
| 2 | representative | 8,9,10,12 | 7 | 11 |
| 3 | coverage | 9,10,11,12 | 8 | 7 |
| 4 | coverage | 7,9,10,11 | 8 | 12 |
| 5 | coverage | 7,10,11,12 | 9 | 8 |
| 6 | worst\_case | 7,8,10,12 | 11 | 9 |

### CP3 — 6 split được chọn

| Split | Role | Train | Val | Test |
| :---- | :---- | :---- | :---- | :---- |
| 1 | representative | 14,15,17,18 | 13 | 16 |
| 2 | coverage | 13,16,17,18 | 14 | 15 |
| 3 | coverage | 14,15,16,18 | 17 | 13 |
| 4 | coverage | 13,15,16,18 | 17 | 14 |
| 5 | worst\_case | 13,14,15,16 | 17 | 18 |
| 6 | coverage | 14,15,16,17 | 18 | 13 |

## Kết quả sau khi chạy

[https://www.kaggle.com/code/platformciviltwin/3rd-dataset-v5-cover-test](https://www.kaggle.com/code/platformciviltwin/3rd-dataset-v5-cover-test)

---

*Nguồn: [Notion page](https://typhoon-storm-ff4.notion.site/Y-u-c-u-2-o-l-i-c-c-run-trong-c-ng-CP-ch-y-th-ra-k-t-qu-3bf4e1a58f8c806bbb4af7b67c22f88e)*  
