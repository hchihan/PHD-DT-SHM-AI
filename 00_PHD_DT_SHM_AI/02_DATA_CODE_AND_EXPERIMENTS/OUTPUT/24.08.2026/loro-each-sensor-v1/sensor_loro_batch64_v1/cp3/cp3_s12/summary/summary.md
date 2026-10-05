# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val17_test18 | 42 | 0.1667 | 0.1667 | 0.1250 | 0.4074 | 1.4588 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val18_test17 | 42 | 0.3333 | 0.3333 | 0.3083 | 0.5741 | 1.4583 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val16_test18 | 42 | 0.3333 | 0.3333 | 0.2250 | 0.5833 | 1.4268 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val18_test16 | 42 | 0.6667 | 0.6667 | 0.6643 | 0.6667 | 1.4392 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val16_test17 | 42 | 0.3333 | 0.3333 | 0.2154 | 0.6944 | 1.3927 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val17_test16 | 42 | 0.1667 | 0.1667 | 0.1214 | 0.5833 | 1.5491 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val15_test18 | 42 | 0.4167 | 0.4167 | 0.2750 | 0.8148 | 1.3513 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val18_test15 | 42 | 0.5000 | 0.5000 | 0.4280 | 0.7963 | 1.4095 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val15_test17 | 42 | 0.5000 | 0.5000 | 0.5000 | 0.8333 | 1.2789 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val17_test15 | 42 | 0.7500 | 0.7500 | 0.7417 | 0.8889 | 1.1701 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val15_test16 | 42 | 0.4167 | 0.4167 | 0.3500 | 0.5463 | 1.4837 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val16_test15 | 42 | 0.3333 | 0.3333 | 0.3125 | 0.6759 | 1.2951 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val14_test18 | 42 | 0.4167 | 0.4167 | 0.2917 | 0.7037 | 1.4037 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val18_test14 | 42 | 0.5000 | 0.5000 | 0.4778 | 0.8148 | 1.3294 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val14_test17 | 42 | 0.5000 | 0.5000 | 0.5060 | 0.8241 | 1.2176 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val17_test14 | 42 | 0.5833 | 0.5833 | 0.5643 | 0.8519 | 1.1907 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val14_test16 | 42 | 0.2500 | 0.2500 | 0.2054 | 0.6204 | 1.5876 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val16_test14 | 42 | 0.6667 | 0.6667 | 0.6250 | 0.8519 | 1.2261 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val14_test15 | 42 | 0.5833 | 0.5833 | 0.5179 | 0.6759 | 1.3413 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val15_test14 | 42 | 0.3333 | 0.3333 | 0.2197 | 0.7593 | 1.3785 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val13_test18 | 42 | 0.3333 | 0.3333 | 0.2154 | 0.6481 | 1.4085 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val18_test13 | 42 | 0.6667 | 0.6667 | 0.6250 | 0.8056 | 1.3216 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val13_test17 | 42 | 0.3333 | 0.3333 | 0.2909 | 0.7130 | 1.3596 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val17_test13 | 42 | 0.6667 | 0.6667 | 0.5893 | 0.8333 | 1.3904 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val13_test16 | 42 | 0.0833 | 0.0833 | 0.0500 | 0.6019 | 1.4470 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val16_test13 | 42 | 0.6667 | 0.6667 | 0.6071 | 0.8056 | 1.3108 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val13_test15 | 42 | 0.3333 | 0.3333 | 0.2222 | 0.6296 | 1.3786 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val15_test13 | 42 | 0.3333 | 0.3333 | 0.2078 | 0.7037 | 1.4004 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val13_test14 | 42 | 0.5833 | 0.5833 | 0.5643 | 0.8333 | 1.2244 |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val14_test13 | 42 | 0.7500 | 0.7500 | 0.7292 | 0.8519 | 1.2242 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val17_test18 | 1 | 0.1667 |  | 0.1667 |  | 0.1250 |  | 0.4074 |  | 1.4588 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val18_test17 | 1 | 0.3333 |  | 0.3333 |  | 0.3083 |  | 0.5741 |  | 1.4583 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val16_test18 | 1 | 0.3333 |  | 0.3333 |  | 0.2250 |  | 0.5833 |  | 1.4268 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val18_test16 | 1 | 0.6667 |  | 0.6667 |  | 0.6643 |  | 0.6667 |  | 1.4392 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val16_test17 | 1 | 0.3333 |  | 0.3333 |  | 0.2154 |  | 0.6944 |  | 1.3927 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val17_test16 | 1 | 0.1667 |  | 0.1667 |  | 0.1214 |  | 0.5833 |  | 1.5491 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val15_test18 | 1 | 0.4167 |  | 0.4167 |  | 0.2750 |  | 0.8148 |  | 1.3513 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val18_test15 | 1 | 0.5000 |  | 0.5000 |  | 0.4280 |  | 0.7963 |  | 1.4095 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val15_test17 | 1 | 0.5000 |  | 0.5000 |  | 0.5000 |  | 0.8333 |  | 1.2789 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val17_test15 | 1 | 0.7500 |  | 0.7500 |  | 0.7417 |  | 0.8889 |  | 1.1701 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val15_test16 | 1 | 0.4167 |  | 0.4167 |  | 0.3500 |  | 0.5463 |  | 1.4837 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val16_test15 | 1 | 0.3333 |  | 0.3333 |  | 0.3125 |  | 0.6759 |  | 1.2951 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val14_test18 | 1 | 0.4167 |  | 0.4167 |  | 0.2917 |  | 0.7037 |  | 1.4037 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val18_test14 | 1 | 0.5000 |  | 0.5000 |  | 0.4778 |  | 0.8148 |  | 1.3294 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val14_test17 | 1 | 0.5000 |  | 0.5000 |  | 0.5060 |  | 0.8241 |  | 1.2176 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val17_test14 | 1 | 0.5833 |  | 0.5833 |  | 0.5643 |  | 0.8519 |  | 1.1907 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val14_test16 | 1 | 0.2500 |  | 0.2500 |  | 0.2054 |  | 0.6204 |  | 1.5876 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val16_test14 | 1 | 0.6667 |  | 0.6667 |  | 0.6250 |  | 0.8519 |  | 1.2261 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val14_test15 | 1 | 0.5833 |  | 0.5833 |  | 0.5179 |  | 0.6759 |  | 1.3413 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val15_test14 | 1 | 0.3333 |  | 0.3333 |  | 0.2197 |  | 0.7593 |  | 1.3785 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val13_test18 | 1 | 0.3333 |  | 0.3333 |  | 0.2154 |  | 0.6481 |  | 1.4085 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val18_test13 | 1 | 0.6667 |  | 0.6667 |  | 0.6250 |  | 0.8056 |  | 1.3216 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val13_test17 | 1 | 0.3333 |  | 0.3333 |  | 0.2909 |  | 0.7130 |  | 1.3596 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val17_test13 | 1 | 0.6667 |  | 0.6667 |  | 0.5893 |  | 0.8333 |  | 1.3904 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val13_test16 | 1 | 0.0833 |  | 0.0833 |  | 0.0500 |  | 0.6019 |  | 1.4470 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val16_test13 | 1 | 0.6667 |  | 0.6667 |  | 0.6071 |  | 0.8056 |  | 1.3108 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val13_test15 | 1 | 0.3333 |  | 0.3333 |  | 0.2222 |  | 0.6296 |  | 1.3786 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val15_test13 | 1 | 0.3333 |  | 0.3333 |  | 0.2078 |  | 0.7037 |  | 1.4004 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val13_test14 | 1 | 0.5833 |  | 0.5833 |  | 0.5643 |  | 0.8333 |  | 1.2244 |  |
| cp3_s12 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val14_test13 | 1 | 0.7500 |  | 0.7500 |  | 0.7292 |  | 0.8519 |  | 1.2242 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s12 | resnet1D | resnet1D-843fbf2 | 42 | 30 | 0.4500 | 0.1799 | 0.4500 | 0.1799 | 0.3925 | 0.1983 | 0.7198 | 0.1177 | 1.3618 | 0.1029 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s12 | resnet1D | resnet1D-843fbf2 | 30 | 0.4500 | 0.1799 | 0.4500 | 0.1799 | 0.3925 | 0.1983 | 0.7198 | 0.1177 | 1.3618 | 0.1029 |

### Pooled confusion matrix: cp3_s12 / resnet1D / resnet1D-843fbf2

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 24 | 14 | 25 | 27 |
| B1 | 14 | 55 | 18 | 3 |
| B2 | 14 | 16 | 51 | 9 |
| B3 | 25 | 8 | 25 | 32 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 26.67 | 15.56 | 27.78 | 30.00 |
| B1 | 15.56 | 61.11 | 20.00 | 3.33 |
| B2 | 15.56 | 17.78 | 56.67 | 10.00 |
| B3 | 27.78 | 8.89 | 27.78 | 35.56 |
