# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-15-16_val17_test18 | 42 | 0.2500 | 0.2500 | 0.2500 | 0.6204 | 1.3920 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-15-16_val18_test17 | 42 | 0.3333 | 0.3333 | 0.3250 | 0.7037 | 1.3416 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-15-17_val16_test18 | 42 | 0.5000 | 0.5000 | 0.4643 | 0.7593 | 1.3226 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-15-17_val18_test16 | 42 | 0.4167 | 0.4167 | 0.3409 | 0.6574 | 1.3710 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-15-18_val16_test17 | 42 | 0.7500 | 0.7500 | 0.7310 | 0.8704 | 1.2870 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-15-18_val17_test16 | 42 | 0.2500 | 0.2500 | 0.1964 | 0.5000 | 1.7257 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-16-17_val15_test18 | 42 | 0.4167 | 0.4167 | 0.3447 | 0.8056 | 1.4930 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-16-17_val18_test15 | 42 | 0.5000 | 0.5000 | 0.3506 | 0.9352 | 1.2604 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-16-18_val15_test17 | 42 | 0.5833 | 0.5833 | 0.5857 | 0.8333 | 1.2036 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-16-18_val17_test15 | 42 | 0.5833 | 0.5833 | 0.5125 | 0.8796 | 1.1520 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-17-18_val15_test16 | 42 | 0.3333 | 0.3333 | 0.3250 | 0.5926 | 1.4970 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-17-18_val16_test15 | 42 | 0.6667 | 0.6667 | 0.5833 | 0.8981 | 1.2963 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-15-16-17_val14_test18 | 42 | 0.4167 | 0.4167 | 0.3964 | 0.8333 | 1.2544 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-15-16-17_val18_test14 | 42 | 0.7500 | 0.7500 | 0.7375 | 0.8889 | 1.2803 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-15-16-18_val14_test17 | 42 | 0.5833 | 0.5833 | 0.5643 | 0.7870 | 1.1406 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-15-16-18_val17_test14 | 42 | 0.7500 | 0.7500 | 0.7268 | 0.9630 | 1.0639 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-15-17-18_val14_test16 | 42 | 0.3333 | 0.3333 | 0.3056 | 0.6111 | 1.5561 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-15-17-18_val16_test14 | 42 | 0.7500 | 0.7500 | 0.6667 | 0.9537 | 1.2621 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-16-17-18_val14_test15 | 42 | 0.6667 | 0.6667 | 0.6583 | 0.8148 | 1.2520 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-16-17-18_val15_test14 | 42 | 0.8333 | 0.8333 | 0.8375 | 0.8889 | 1.2160 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train14-15-16-17_val13_test18 | 42 | 0.5833 | 0.5833 | 0.5095 | 0.7963 | 1.3490 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train14-15-16-17_val18_test13 | 42 | 0.8333 | 0.8333 | 0.8125 | 0.8981 | 1.2122 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train14-15-16-18_val13_test17 | 42 | 0.5833 | 0.5833 | 0.5750 | 0.8704 | 1.1105 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train14-15-16-18_val17_test13 | 42 | 0.7500 | 0.7500 | 0.7268 | 0.9167 | 1.2465 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train14-15-17-18_val13_test16 | 42 | 0.4167 | 0.4167 | 0.4458 | 0.5741 | 1.5563 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train14-15-17-18_val16_test13 | 42 | 0.5833 | 0.5833 | 0.5167 | 0.8981 | 1.2853 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train14-16-17-18_val13_test15 | 42 | 0.5000 | 0.5000 | 0.3864 | 0.8426 | 1.2923 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train14-16-17-18_val15_test13 | 42 | 0.7500 | 0.7500 | 0.7429 | 0.9074 | 1.2650 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train15-16-17-18_val13_test14 | 42 | 0.7500 | 0.7500 | 0.7268 | 0.9630 | 1.0760 |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train15-16-17-18_val14_test13 | 42 | 0.6667 | 0.6667 | 0.6571 | 0.8611 | 1.1029 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-15-16_val17_test18 | 1 | 0.2500 |  | 0.2500 |  | 0.2500 |  | 0.6204 |  | 1.3920 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-15-16_val18_test17 | 1 | 0.3333 |  | 0.3333 |  | 0.3250 |  | 0.7037 |  | 1.3416 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-15-17_val16_test18 | 1 | 0.5000 |  | 0.5000 |  | 0.4643 |  | 0.7593 |  | 1.3226 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-15-17_val18_test16 | 1 | 0.4167 |  | 0.4167 |  | 0.3409 |  | 0.6574 |  | 1.3710 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-15-18_val16_test17 | 1 | 0.7500 |  | 0.7500 |  | 0.7310 |  | 0.8704 |  | 1.2870 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-15-18_val17_test16 | 1 | 0.2500 |  | 0.2500 |  | 0.1964 |  | 0.5000 |  | 1.7257 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-16-17_val15_test18 | 1 | 0.4167 |  | 0.4167 |  | 0.3447 |  | 0.8056 |  | 1.4930 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-16-17_val18_test15 | 1 | 0.5000 |  | 0.5000 |  | 0.3506 |  | 0.9352 |  | 1.2604 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-16-18_val15_test17 | 1 | 0.5833 |  | 0.5833 |  | 0.5857 |  | 0.8333 |  | 1.2036 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-16-18_val17_test15 | 1 | 0.5833 |  | 0.5833 |  | 0.5125 |  | 0.8796 |  | 1.1520 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-17-18_val15_test16 | 1 | 0.3333 |  | 0.3333 |  | 0.3250 |  | 0.5926 |  | 1.4970 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-14-17-18_val16_test15 | 1 | 0.6667 |  | 0.6667 |  | 0.5833 |  | 0.8981 |  | 1.2963 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-15-16-17_val14_test18 | 1 | 0.4167 |  | 0.4167 |  | 0.3964 |  | 0.8333 |  | 1.2544 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-15-16-17_val18_test14 | 1 | 0.7500 |  | 0.7500 |  | 0.7375 |  | 0.8889 |  | 1.2803 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-15-16-18_val14_test17 | 1 | 0.5833 |  | 0.5833 |  | 0.5643 |  | 0.7870 |  | 1.1406 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-15-16-18_val17_test14 | 1 | 0.7500 |  | 0.7500 |  | 0.7268 |  | 0.9630 |  | 1.0639 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-15-17-18_val14_test16 | 1 | 0.3333 |  | 0.3333 |  | 0.3056 |  | 0.6111 |  | 1.5561 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-15-17-18_val16_test14 | 1 | 0.7500 |  | 0.7500 |  | 0.6667 |  | 0.9537 |  | 1.2621 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-16-17-18_val14_test15 | 1 | 0.6667 |  | 0.6667 |  | 0.6583 |  | 0.8148 |  | 1.2520 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train13-16-17-18_val15_test14 | 1 | 0.8333 |  | 0.8333 |  | 0.8375 |  | 0.8889 |  | 1.2160 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train14-15-16-17_val13_test18 | 1 | 0.5833 |  | 0.5833 |  | 0.5095 |  | 0.7963 |  | 1.3490 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train14-15-16-17_val18_test13 | 1 | 0.8333 |  | 0.8333 |  | 0.8125 |  | 0.8981 |  | 1.2122 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train14-15-16-18_val13_test17 | 1 | 0.5833 |  | 0.5833 |  | 0.5750 |  | 0.8704 |  | 1.1105 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train14-15-16-18_val17_test13 | 1 | 0.7500 |  | 0.7500 |  | 0.7268 |  | 0.9167 |  | 1.2465 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train14-15-17-18_val13_test16 | 1 | 0.4167 |  | 0.4167 |  | 0.4458 |  | 0.5741 |  | 1.5563 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train14-15-17-18_val16_test13 | 1 | 0.5833 |  | 0.5833 |  | 0.5167 |  | 0.8981 |  | 1.2853 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train14-16-17-18_val13_test15 | 1 | 0.5000 |  | 0.5000 |  | 0.3864 |  | 0.8426 |  | 1.2923 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train14-16-17-18_val15_test13 | 1 | 0.7500 |  | 0.7500 |  | 0.7429 |  | 0.9074 |  | 1.2650 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train15-16-17-18_val13_test14 | 1 | 0.7500 |  | 0.7500 |  | 0.7268 |  | 0.9630 |  | 1.0760 |  |
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train15-16-17-18_val14_test13 | 1 | 0.6667 |  | 0.6667 |  | 0.6571 |  | 0.8611 |  | 1.1029 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | 42 | 30 | 0.5694 | 0.1738 | 0.5694 | 0.1738 | 0.5334 | 0.1816 | 0.8108 | 0.1272 | 1.2955 | 0.1521 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_resnet1d | resnet1D | resnet1D-75d5c1e | 30 | 0.5694 | 0.1738 | 0.5694 | 0.1738 | 0.5334 | 0.1816 | 0.8108 | 0.1272 | 1.2955 | 0.1521 |

### Pooled confusion matrix: cp3_s123_resnet1d / resnet1D / resnet1D-75d5c1e

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 41 | 21 | 24 | 4 |
| B1 | 20 | 50 | 15 | 5 |
| B2 | 23 | 25 | 36 | 6 |
| B3 | 2 | 4 | 6 | 78 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 45.56 | 23.33 | 26.67 | 4.44 |
| B1 | 22.22 | 55.56 | 16.67 | 5.56 |
| B2 | 25.56 | 27.78 | 40.00 | 6.67 |
| B3 | 2.22 | 4.44 | 6.67 | 86.67 |
