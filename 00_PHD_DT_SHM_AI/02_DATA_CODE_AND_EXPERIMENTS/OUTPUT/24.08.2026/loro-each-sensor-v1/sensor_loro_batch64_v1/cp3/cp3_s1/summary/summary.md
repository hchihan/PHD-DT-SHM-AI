# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val17_test18 | 42 | 0.2500 | 0.2500 | 0.2431 | 0.5370 | 1.4689 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val18_test17 | 42 | 0.3333 | 0.3333 | 0.2154 | 0.6481 | 1.3787 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val16_test18 | 42 | 0.4167 | 0.4167 | 0.3540 | 0.6944 | 1.3660 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val18_test16 | 42 | 0.4167 | 0.4167 | 0.4409 | 0.5926 | 1.5511 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val16_test17 | 42 | 0.5833 | 0.5833 | 0.5254 | 0.8148 | 1.3259 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val17_test16 | 42 | 0.5000 | 0.5000 | 0.4940 | 0.5556 | 1.5031 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val15_test18 | 42 | 0.3333 | 0.3333 | 0.2964 | 0.7407 | 1.5250 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val18_test15 | 42 | 0.6667 | 0.6667 | 0.6000 | 0.8426 | 1.2970 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val15_test17 | 42 | 0.5833 | 0.5833 | 0.5583 | 0.8796 | 1.1569 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val17_test15 | 42 | 0.6667 | 0.6667 | 0.6488 | 0.9074 | 1.1986 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val15_test16 | 42 | 0.3333 | 0.3333 | 0.3083 | 0.5833 | 1.5307 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val16_test15 | 42 | 0.4167 | 0.4167 | 0.3333 | 0.7407 | 1.3329 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val14_test18 | 42 | 0.5833 | 0.5833 | 0.5554 | 0.7778 | 1.2798 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val18_test14 | 42 | 0.5833 | 0.5833 | 0.5643 | 0.6667 | 1.4063 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val14_test17 | 42 | 0.5833 | 0.5833 | 0.5750 | 0.8796 | 1.1900 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val17_test14 | 42 | 0.5000 | 0.5000 | 0.4500 | 0.6667 | 1.3779 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val14_test16 | 42 | 0.3333 | 0.3333 | 0.3361 | 0.5278 | 1.4805 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val16_test14 | 42 | 0.4167 | 0.4167 | 0.3631 | 0.7407 | 1.3553 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val14_test15 | 42 | 0.3333 | 0.3333 | 0.2321 | 0.6944 | 1.3517 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val15_test14 | 42 | 0.5833 | 0.5833 | 0.5881 | 0.6574 | 1.4317 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val13_test18 | 42 | 0.4167 | 0.4167 | 0.4143 | 0.6852 | 1.3627 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val18_test13 | 42 | 0.5000 | 0.5000 | 0.4236 | 0.7222 | 1.3771 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val13_test17 | 42 | 0.5833 | 0.5833 | 0.5750 | 0.8519 | 1.1910 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val17_test13 | 42 | 0.5000 | 0.5000 | 0.4179 | 0.8148 | 1.4420 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val13_test16 | 42 | 0.4167 | 0.4167 | 0.4409 | 0.5833 | 1.5377 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val16_test13 | 42 | 0.5000 | 0.5000 | 0.4167 | 0.7130 | 1.3581 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val13_test15 | 42 | 0.4167 | 0.4167 | 0.4107 | 0.6481 | 1.3660 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val15_test13 | 42 | 0.3333 | 0.3333 | 0.2984 | 0.7037 | 1.3652 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val13_test14 | 42 | 0.3333 | 0.3333 | 0.3458 | 0.6759 | 1.3829 |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val14_test13 | 42 | 0.5000 | 0.5000 | 0.4137 | 0.7407 | 1.2868 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val17_test18 | 1 | 0.2500 |  | 0.2500 |  | 0.2431 |  | 0.5370 |  | 1.4689 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val18_test17 | 1 | 0.3333 |  | 0.3333 |  | 0.2154 |  | 0.6481 |  | 1.3787 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val16_test18 | 1 | 0.4167 |  | 0.4167 |  | 0.3540 |  | 0.6944 |  | 1.3660 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val18_test16 | 1 | 0.4167 |  | 0.4167 |  | 0.4409 |  | 0.5926 |  | 1.5511 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val16_test17 | 1 | 0.5833 |  | 0.5833 |  | 0.5254 |  | 0.8148 |  | 1.3259 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val17_test16 | 1 | 0.5000 |  | 0.5000 |  | 0.4940 |  | 0.5556 |  | 1.5031 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val15_test18 | 1 | 0.3333 |  | 0.3333 |  | 0.2964 |  | 0.7407 |  | 1.5250 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val18_test15 | 1 | 0.6667 |  | 0.6667 |  | 0.6000 |  | 0.8426 |  | 1.2970 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val15_test17 | 1 | 0.5833 |  | 0.5833 |  | 0.5583 |  | 0.8796 |  | 1.1569 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val17_test15 | 1 | 0.6667 |  | 0.6667 |  | 0.6488 |  | 0.9074 |  | 1.1986 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val15_test16 | 1 | 0.3333 |  | 0.3333 |  | 0.3083 |  | 0.5833 |  | 1.5307 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val16_test15 | 1 | 0.4167 |  | 0.4167 |  | 0.3333 |  | 0.7407 |  | 1.3329 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val14_test18 | 1 | 0.5833 |  | 0.5833 |  | 0.5554 |  | 0.7778 |  | 1.2798 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val18_test14 | 1 | 0.5833 |  | 0.5833 |  | 0.5643 |  | 0.6667 |  | 1.4063 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val14_test17 | 1 | 0.5833 |  | 0.5833 |  | 0.5750 |  | 0.8796 |  | 1.1900 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val17_test14 | 1 | 0.5000 |  | 0.5000 |  | 0.4500 |  | 0.6667 |  | 1.3779 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val14_test16 | 1 | 0.3333 |  | 0.3333 |  | 0.3361 |  | 0.5278 |  | 1.4805 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val16_test14 | 1 | 0.4167 |  | 0.4167 |  | 0.3631 |  | 0.7407 |  | 1.3553 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val14_test15 | 1 | 0.3333 |  | 0.3333 |  | 0.2321 |  | 0.6944 |  | 1.3517 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val15_test14 | 1 | 0.5833 |  | 0.5833 |  | 0.5881 |  | 0.6574 |  | 1.4317 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val13_test18 | 1 | 0.4167 |  | 0.4167 |  | 0.4143 |  | 0.6852 |  | 1.3627 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val18_test13 | 1 | 0.5000 |  | 0.5000 |  | 0.4236 |  | 0.7222 |  | 1.3771 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val13_test17 | 1 | 0.5833 |  | 0.5833 |  | 0.5750 |  | 0.8519 |  | 1.1910 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val17_test13 | 1 | 0.5000 |  | 0.5000 |  | 0.4179 |  | 0.8148 |  | 1.4420 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val13_test16 | 1 | 0.4167 |  | 0.4167 |  | 0.4409 |  | 0.5833 |  | 1.5377 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val16_test13 | 1 | 0.5000 |  | 0.5000 |  | 0.4167 |  | 0.7130 |  | 1.3581 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val13_test15 | 1 | 0.4167 |  | 0.4167 |  | 0.4107 |  | 0.6481 |  | 1.3660 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val15_test13 | 1 | 0.3333 |  | 0.3333 |  | 0.2984 |  | 0.7037 |  | 1.3652 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val13_test14 | 1 | 0.3333 |  | 0.3333 |  | 0.3458 |  | 0.6759 |  | 1.3829 |  |
| cp3_s1 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val14_test13 | 1 | 0.5000 |  | 0.5000 |  | 0.4137 |  | 0.7407 |  | 1.2868 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s1 | resnet1D | resnet1D-843fbf2 | 42 | 30 | 0.4639 | 0.1130 | 0.4639 | 0.1130 | 0.4280 | 0.1196 | 0.7096 | 0.1041 | 1.3726 | 0.1058 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s1 | resnet1D | resnet1D-843fbf2 | 30 | 0.4639 | 0.1130 | 0.4639 | 0.1130 | 0.4280 | 0.1196 | 0.7096 | 0.1041 | 1.3726 | 0.1058 |

### Pooled confusion matrix: cp3_s1 / resnet1D / resnet1D-843fbf2

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 27 | 18 | 20 | 25 |
| B1 | 13 | 55 | 18 | 4 |
| B2 | 5 | 21 | 45 | 19 |
| B3 | 14 | 14 | 22 | 40 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 30.00 | 20.00 | 22.22 | 27.78 |
| B1 | 14.44 | 61.11 | 20.00 | 4.44 |
| B2 | 5.56 | 23.33 | 50.00 | 21.11 |
| B3 | 15.56 | 15.56 | 24.44 | 44.44 |
