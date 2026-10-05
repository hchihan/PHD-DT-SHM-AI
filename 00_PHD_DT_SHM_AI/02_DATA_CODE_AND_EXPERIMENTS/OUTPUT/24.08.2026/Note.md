# Note

Trong [13_export_sensor_signal_analyzer.py (line 41)](/Users/nguyenquangvinh/Desktop/CE/project_ce/3rd_dataset/preprocessing_scripts/13_export_sensor_signal_analyzer.py:41), cp2_21 và cp2_2122 không được phân loại trực tiếp. Script đọc cột campaign từ `07b_campaign_manifest.csv`. Quy tắc tạo manifest nằm trong [07b_resolve_campaigns.py (line 423)](/Users/nguyenquangvinh/Desktop/CE/project_ce/3rd_dataset/preprocessing_scripts/07b_resolve_campaigns.py:423).

## cp2_21

Lấy toàn bộ file CSV trong:

```
cp2/thinghiem_210726_PASCO/*.csv
```

Tức toàn bộ dữ liệu phiên ngày 21/07, gồm đủ bốn lớp:

- Healthy
- B1
- B2
- B3

Mỗi lớp 18 file, tổng cộng 72 file. Không có file vay mượn (borrowed=no).

## cp2_2122

Được ghép từ hai phiên:

Từ phiên 22/07:

```
cp2/thinghiem_220726_PASCO/*.csv
```

Chỉ lấy các lớp:

- Healthy
- B1
- B2

Tổng cộng 53 file trong thư mục này, cộng thêm file B1 bị thiếu nằm ở raw root:

```
BS1B1L1R12_bo_sung_file_thieu_dot_2.csv
```

Như vậy phần ngày 22/07 có 54 file.

Lớp B3 lấy từ phiên 21/07:

```
cp2/thinghiem_210726_PASCO/*B3*.csv
```

Có 18 file B3, được đánh dấu borrowed=yes, vì ngày 22/07 không đo lớp B3.

**Kết quả:**

```
cp2_2122 =
Healthy ngày 22/07
+ B1 ngày 22/07 (bao gồm file bổ sung)
+ B2 ngày 22/07
+ B3 mượn từ ngày 21/07
```

Tổng cộng cũng là 72 file, 18 file mỗi lớp.

**Lưu ý quan trọng:** trong cp2_2122, toàn bộ B3 đến từ ngày khác với Healthy/B1/B2. Vì vậy mô hình có thể học sự khác biệt giữa hai phiên đo thay vì chỉ học trạng thái hư hỏng. cp2_21 là tập đối chứng sạch hơn vì cả bốn lớp đều thuộc cùng phiên 21/07.
