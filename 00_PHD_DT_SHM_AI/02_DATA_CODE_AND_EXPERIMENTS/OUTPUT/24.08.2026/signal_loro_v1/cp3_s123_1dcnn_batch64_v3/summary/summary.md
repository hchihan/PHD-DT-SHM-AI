# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-15-16_val17_test18 | 42 | 0.4167 | 0.4167 | 0.3364 | 0.8148 | 1.3483 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-15-16_val18_test17 | 42 | 0.4167 | 0.4167 | 0.3500 | 0.5833 | 1.4304 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-15-17_val16_test18 | 42 | 0.4167 | 0.4167 | 0.2917 | 0.8056 | 1.2784 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-15-17_val18_test16 | 42 | 0.5000 | 0.5000 | 0.3750 | 0.7963 | 1.2931 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-15-18_val16_test17 | 42 | 0.4167 | 0.4167 | 0.3601 | 0.6481 | 1.3894 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-15-18_val17_test16 | 42 | 0.5833 | 0.5833 | 0.5254 | 0.7500 | 1.3093 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-16-17_val15_test18 | 42 | 0.3333 | 0.3333 | 0.2429 | 0.7500 | 1.2858 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-16-17_val18_test15 | 42 | 0.5000 | 0.5000 | 0.4095 | 0.7407 | 1.3235 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-16-18_val15_test17 | 42 | 0.4167 | 0.4167 | 0.3393 | 0.5741 | 1.5063 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-16-18_val17_test15 | 42 | 0.4167 | 0.4167 | 0.3667 | 0.7685 | 1.3390 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-17-18_val15_test16 | 42 | 0.2500 | 0.2500 | 0.2167 | 0.6852 | 1.4140 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-17-18_val16_test15 | 42 | 0.3333 | 0.3333 | 0.2250 | 0.7778 | 1.2919 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-15-16-17_val14_test18 | 42 | 0.5000 | 0.5000 | 0.3375 | 0.7130 | 1.3272 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-15-16-17_val18_test14 | 42 | 0.4167 | 0.4167 | 0.3631 | 0.7130 | 1.3181 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-15-16-18_val14_test17 | 42 | 0.3333 | 0.3333 | 0.3125 | 0.6296 | 1.3835 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-15-16-18_val17_test14 | 42 | 0.5833 | 0.5833 | 0.5095 | 0.8426 | 1.2524 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-15-17-18_val14_test16 | 42 | 0.3333 | 0.3333 | 0.2125 | 0.7963 | 1.2857 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-15-17-18_val16_test14 | 42 | 0.6667 | 0.6667 | 0.6583 | 0.8241 | 1.2884 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-16-17-18_val14_test15 | 42 | 0.3333 | 0.3333 | 0.2798 | 0.7130 | 1.3622 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-16-17-18_val15_test14 | 42 | 0.4167 | 0.4167 | 0.3611 | 0.7222 | 1.3403 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train14-15-16-17_val13_test18 | 42 | 0.4167 | 0.4167 | 0.3614 | 0.8148 | 1.3479 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train14-15-16-17_val18_test13 | 42 | 0.5833 | 0.5833 | 0.4970 | 0.8889 | 1.2110 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train14-15-16-18_val13_test17 | 42 | 0.3333 | 0.3333 | 0.3125 | 0.5463 | 1.5139 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train14-15-16-18_val17_test13 | 42 | 0.5833 | 0.5833 | 0.5750 | 0.8056 | 1.2812 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train14-15-17-18_val13_test16 | 42 | 0.1667 | 0.1667 | 0.1705 | 0.7037 | 1.4448 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train14-15-17-18_val16_test13 | 42 | 0.5000 | 0.5000 | 0.4375 | 0.7593 | 1.2731 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train14-16-17-18_val13_test15 | 42 | 0.4167 | 0.4167 | 0.3631 | 0.7130 | 1.3717 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train14-16-17-18_val15_test13 | 42 | 0.5000 | 0.5000 | 0.4095 | 0.7407 | 1.3233 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train15-16-17-18_val13_test14 | 42 | 0.4167 | 0.4167 | 0.3679 | 0.6944 | 1.4013 |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train15-16-17-18_val14_test13 | 42 | 0.4167 | 0.4167 | 0.3512 | 0.7130 | 1.3201 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-15-16_val17_test18 | 1 | 0.4167 |  | 0.4167 |  | 0.3364 |  | 0.8148 |  | 1.3483 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-15-16_val18_test17 | 1 | 0.4167 |  | 0.4167 |  | 0.3500 |  | 0.5833 |  | 1.4304 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-15-17_val16_test18 | 1 | 0.4167 |  | 0.4167 |  | 0.2917 |  | 0.8056 |  | 1.2784 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-15-17_val18_test16 | 1 | 0.5000 |  | 0.5000 |  | 0.3750 |  | 0.7963 |  | 1.2931 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-15-18_val16_test17 | 1 | 0.4167 |  | 0.4167 |  | 0.3601 |  | 0.6481 |  | 1.3894 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-15-18_val17_test16 | 1 | 0.5833 |  | 0.5833 |  | 0.5254 |  | 0.7500 |  | 1.3093 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-16-17_val15_test18 | 1 | 0.3333 |  | 0.3333 |  | 0.2429 |  | 0.7500 |  | 1.2858 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-16-17_val18_test15 | 1 | 0.5000 |  | 0.5000 |  | 0.4095 |  | 0.7407 |  | 1.3235 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-16-18_val15_test17 | 1 | 0.4167 |  | 0.4167 |  | 0.3393 |  | 0.5741 |  | 1.5063 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-16-18_val17_test15 | 1 | 0.4167 |  | 0.4167 |  | 0.3667 |  | 0.7685 |  | 1.3390 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-17-18_val15_test16 | 1 | 0.2500 |  | 0.2500 |  | 0.2167 |  | 0.6852 |  | 1.4140 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-14-17-18_val16_test15 | 1 | 0.3333 |  | 0.3333 |  | 0.2250 |  | 0.7778 |  | 1.2919 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-15-16-17_val14_test18 | 1 | 0.5000 |  | 0.5000 |  | 0.3375 |  | 0.7130 |  | 1.3272 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-15-16-17_val18_test14 | 1 | 0.4167 |  | 0.4167 |  | 0.3631 |  | 0.7130 |  | 1.3181 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-15-16-18_val14_test17 | 1 | 0.3333 |  | 0.3333 |  | 0.3125 |  | 0.6296 |  | 1.3835 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-15-16-18_val17_test14 | 1 | 0.5833 |  | 0.5833 |  | 0.5095 |  | 0.8426 |  | 1.2524 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-15-17-18_val14_test16 | 1 | 0.3333 |  | 0.3333 |  | 0.2125 |  | 0.7963 |  | 1.2857 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-15-17-18_val16_test14 | 1 | 0.6667 |  | 0.6667 |  | 0.6583 |  | 0.8241 |  | 1.2884 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-16-17-18_val14_test15 | 1 | 0.3333 |  | 0.3333 |  | 0.2798 |  | 0.7130 |  | 1.3622 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train13-16-17-18_val15_test14 | 1 | 0.4167 |  | 0.4167 |  | 0.3611 |  | 0.7222 |  | 1.3403 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train14-15-16-17_val13_test18 | 1 | 0.4167 |  | 0.4167 |  | 0.3614 |  | 0.8148 |  | 1.3479 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train14-15-16-17_val18_test13 | 1 | 0.5833 |  | 0.5833 |  | 0.4970 |  | 0.8889 |  | 1.2110 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train14-15-16-18_val13_test17 | 1 | 0.3333 |  | 0.3333 |  | 0.3125 |  | 0.5463 |  | 1.5139 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train14-15-16-18_val17_test13 | 1 | 0.5833 |  | 0.5833 |  | 0.5750 |  | 0.8056 |  | 1.2812 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train14-15-17-18_val13_test16 | 1 | 0.1667 |  | 0.1667 |  | 0.1705 |  | 0.7037 |  | 1.4448 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train14-15-17-18_val16_test13 | 1 | 0.5000 |  | 0.5000 |  | 0.4375 |  | 0.7593 |  | 1.2731 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train14-16-17-18_val13_test15 | 1 | 0.4167 |  | 0.4167 |  | 0.3631 |  | 0.7130 |  | 1.3717 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train14-16-17-18_val15_test13 | 1 | 0.5000 |  | 0.5000 |  | 0.4095 |  | 0.7407 |  | 1.3233 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train15-16-17-18_val13_test14 | 1 | 0.4167 |  | 0.4167 |  | 0.3679 |  | 0.6944 |  | 1.4013 |  |
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train15-16-17-18_val14_test13 | 1 | 0.4167 |  | 0.4167 |  | 0.3512 |  | 0.7130 |  | 1.3201 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | 42 | 30 | 0.4306 | 0.1074 | 0.4306 | 0.1074 | 0.3639 | 0.1086 | 0.7343 | 0.0806 | 1.3418 | 0.0704 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | 30 | 0.4306 | 0.1074 | 0.4306 | 0.1074 | 0.3639 | 0.1086 | 0.7343 | 0.0806 | 1.3418 | 0.0704 |

### Pooled confusion matrix: cp3_s123_1dcnn / 1dcnn / 1dcnn-75d5c1e

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 55 | 21 | 1 | 13 |
| B1 | 43 | 25 | 4 | 18 |
| B2 | 46 | 25 | 3 | 16 |
| B3 | 12 | 5 | 1 | 72 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 61.11 | 23.33 | 1.11 | 14.44 |
| B1 | 47.78 | 27.78 | 4.44 | 20.00 |
| B2 | 51.11 | 27.78 | 3.33 | 17.78 |
| B3 | 13.33 | 5.56 | 1.11 | 80.00 |
