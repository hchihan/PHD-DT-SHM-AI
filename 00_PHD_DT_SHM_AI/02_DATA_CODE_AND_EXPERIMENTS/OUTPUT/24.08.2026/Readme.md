# Yêu cầu sửa đổi

## CP2_21 và CP2_2122 (Done)

Chọn 1 trong 2, vì sao chọn?

📄 [Note](https://typhoon-storm-ff4.notion.site/Note-3c14e1a58f8c80b7a453de9f0bb711fb)

## Raw data (Done)

Convert and change structure into same with example:

```
dataset/
├── canonical/
│   ├── campaigns/
│   │   ├── CP1/
│   │   │   ├── RUN001/
│   │   │   │   ├── REC0001_HEALTHY_BEAT_L1.csv
│   │   │   │   ├── REC0002_HEALTHY_BEAT_L2.csv
│   │   │   │   ├── REC0003_HEALTHY_WN.csv
│   │   │   │   ├── REC0004_B1_BEAT_L1.csv
│   │   │   │   ├── REC0005_B1_BEAT_L2.csv
│   │   │   │   ├── REC0006_B1_WN.csv
│   │   │   │   ├── REC0007_B2_BEAT_L1.csv
│   │   │   │   ├── REC0008_B2_BEAT_L2.csv
│   │   │   │   ├── REC0009_B2_WN.csv
│   │   │   │   ├── REC0010_B3_BEAT_L1.csv
│   │   │   │   ├── REC0011_B3_BEAT_L2.csv
│   │   │   │   └── REC0012_B3_WN.csv
│   │   │   │
│   │   │   ├── RUN002/
│   │   │   │   └── ... 12 recordings
│   │   │   ├── RUN003/
│   │   │   ├── RUN004/
│   │   │   ├── RUN005/
│   │   │   └── RUN006/
│   │   │
│   │   ├── CP2/
│   │   │   ├── RUN007/
│   │   │   ├── RUN008/
│   │   │   ├── RUN009/
│   │   │   ├── RUN010/
│   │   │   ├── RUN011/
│   │   │   └── RUN012/
│   │   │
│   │   └── CP3/
│   │       ├── RUN013/
│   │       ├── RUN014/
│   │       ├── RUN015/
│   │       ├── RUN016/
│   │       ├── RUN017/
│   │       └── RUN018/
│   │
│   ├── registry/
│   │   ├── campaigns.csv
│   │   ├── runs.csv
│   │   ├── recordings.csv
│   │   └── manifest.json
│   │
│   └── README.md
│
├── processed/
│   ├── full_duration/
│   ├── middle_40s/
│   └── model_npz/
│
└── experiments/
    ├── intra_campaign/
    ├── cross_campaign/
    └── sensor_ablation/
```

## LORO (Done)

Trong mỗi đợt, hoán vị các run và chạy lần lượt từng hoán vị

VD:

```
1 2 3 4 5 6
1 2 5 6 3 4
…
```

Expected: 0.8 → 0.9

Results: https://www.kaggle.com/code/platformciviltwin/signal-loro-v1

### Check code có thiếu 2 ý này không (Done)

- Báo cáo kết quả ở cấp recording: macro-F1, balanced accuracy, accuracy, confusion matrix, mean ± SD theo fold và seed.
- Lưu predictions, scores, seed, split và model version của từng lần chạy.

### 3rd_dataset_v5_Cross-campaign → Done

Chạy thêm các hoán vị

```
--train-run-ids 7,8,9,10,11 \
--val-run-ids 12 \
```

Apply for cp2 & cp3

Results: https://www.kaggle.com/code/platformciviltwin/signal-loro-cross-campaign-v1

### https://www.kaggle.com/code/platformciviltwin/3rd-dataset-v6-training → Done

Chạy lại trên bộ dữ liệu đã bỏ bớt 1 nhánh CP2

Với mỗi trường hợp CP/cảm biến → Chạy hoán vị cho các run. (Note là cùng CP)

Results: https://www.kaggle.com/code/platformciviltwin/signal-loro-each-sensor-v1

Thêm random_forest, sau đó train và test các cp

Hiện tại e cho chạy 4 mô hình ml luôn (Tại dù sao nó cũng chạy nhanh, chạy nhiều có cái để xem kkk)

https://www.kaggle.com/code/platformciviltwin/signal-loro-ml-v1
