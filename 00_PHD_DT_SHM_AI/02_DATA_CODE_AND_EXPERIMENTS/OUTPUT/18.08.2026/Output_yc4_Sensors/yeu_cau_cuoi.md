# Yêu cầu cuối

Đợt CP1 có 2 sensor, CP2 và CP3 đều có 3 sensor

- CP1 → So sánh sensor1, sensor2 và 2 sensor (Kết quả nhận thấy: Khi kết hợp 2 sensor và dùng dữ liệu đó train mô hình → Độ chính xác tốt hơn, F1 macro và conf matrix đều higher so với từng sensor riêng lẻ)
- Lần 2 & lần 3 có 3 cái → Nếu mà 3 nó không cải thiện đáng kể so với 2
- Chạy theo từng dữ liệu (x, y, z, resultant) của sensor
- Với 3 sensor, liệu nó có tăng so với 1 và 2 sensor không? Và nó tăng bao nhiêu, vì sao?
- **Bao nhiêu sensor là đủ?**

---

## Mục tiêu

Xác định số lượng sensor tối thiểu cần sử dụng để mô hình vẫn đạt hiệu quả phân loại tốt.

Cụ thể:
- So sánh hiệu quả khi dùng 1, 2 và 3 sensor.
- Đánh giá việc thêm sensor có cải thiện Macro-F1, accuracy và confusion matrix hay không.
- Không đánh giá sensor nào tốt nhất; chỉ đánh giá ảnh hưởng của số lượng sensor.

---

## Phương pháp chứng minh

Giữ cố định model, hyperparameter, seed và cách chia run. Chỉ thay đổi số lượng/tổ hợp sensor.

### Các thí nghiệm

**CP1:**
- 1 sensor → s1, s2
- 2 sensors → s12

**CP2 và CP3:**
- 1 sensor → s1, s2, s3
- 2 sensors → s12, s13, s23
- 3 sensors → s123

### Chia run

- CP1: train R1–R4, val R5, test R6
- CP2: train R7–R10, val R11, test R12
- CP3: train R13–R16, val R17, test R18

### Tổng hợp theo số lượng sensor

- Kết quả 1 sensor = trung bình s1, s2, s3
- Kết quả 2 sensors = trung bình s12, s13, s23
- Kết quả 3 sensors = kết quả s123

### So sánh mức cải thiện

$$\Delta_{2-1} = F1_{\text{2 sensors}} - F1_{\text{1 sensor}}$$

$$\Delta_{3-2} = F1_{\text{3 sensors}} - F1_{\text{2 sensors}}$$

**Metric chính** là Macro-F1; **metric phụ** gồm accuracy, balanced accuracy và confusion matrix.

---

## Kết quả hướng tới

Dự kiến chứng minh:
- Hai sensor cải thiện rõ rệt so với một sensor.
- Ba sensor không cải thiện đáng kể so với hai sensor.
- Mức tăng từ hai lên ba sensor nhỏ hơn ngưỡng thực tế, ví dụ 2 percentage points Macro-F1.

Từ đó đưa ra kết luận: **Hai sensor là số lượng đủ cho bài toán** — tốt hơn rõ rệt so với một sensor, trong khi sensor thứ ba làm tăng chi phí và độ phức tạp nhưng không mang lại cải thiện tương xứng.

---

## Các tổ hợp cần chạy

```
CP1
├── 1 sensor
│   ├── cp1_s1
│   └── cp1_s2
└── 2 sensors
    └── cp1_s12

CP2
├── 1 sensor
│   ├── cp2_21_s1
│   ├── cp2_21_s2
│   └── cp2_21_s3
├── 2 sensors
│   ├── cp2_21_s12
│   ├── cp2_21_s13
│   └── cp2_21_s23
└── 3 sensors
    └── cp2_21_s123

CP3
├── 1 sensor
│   ├── cp3_s1
│   ├── cp3_s2
│   └── cp3_s3
├── 2 sensors
│   ├── cp3_s12
│   ├── cp3_s13
│   └── cp3_s23
└── 3 sensors
    └── cp3_s123
```

### Tổng cộng

| Campaign | 1 sensor | 2 sensors | 3 sensors | Tổng |
|---|---|---|---|---|
| CP1 | 2 | 1 | 0 | 3 |
| CP2 | 3 | 3 | 1 | 7 |
| CP3 | 3 | 3 | 1 | 7 |
| **Tổng** | **8** | **7** | **2** | **17 thí nghiệm** |

---

## Kết quả

https://www.kaggle.com/code/platformciviltwin/3rd-dataset-v6-training?scriptVersionId=343288214
