# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val17_test18 | 42 | 0.2500 | 0.2500 | 0.2500 | 0.6204 | 1.3920 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val18_test17 | 42 | 0.3333 | 0.3333 | 0.3250 | 0.7037 | 1.3416 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val16_test18 | 42 | 0.5000 | 0.5000 | 0.4643 | 0.7593 | 1.3226 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val18_test16 | 42 | 0.4167 | 0.4167 | 0.3409 | 0.6574 | 1.3710 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val16_test17 | 42 | 0.7500 | 0.7500 | 0.7310 | 0.8704 | 1.2870 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val17_test16 | 42 | 0.2500 | 0.2500 | 0.1964 | 0.5000 | 1.7257 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val15_test18 | 42 | 0.4167 | 0.4167 | 0.3447 | 0.8056 | 1.4930 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val18_test15 | 42 | 0.5000 | 0.5000 | 0.4179 | 0.8704 | 1.4779 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val15_test17 | 42 | 0.5833 | 0.5833 | 0.5857 | 0.8333 | 1.2036 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val17_test15 | 42 | 0.5000 | 0.5000 | 0.4375 | 0.8889 | 1.2661 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val15_test16 | 42 | 0.4167 | 0.4167 | 0.4429 | 0.6204 | 1.5026 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val16_test15 | 42 | 0.6667 | 0.6667 | 0.5833 | 0.8981 | 1.2963 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val14_test18 | 42 | 0.4167 | 0.4167 | 0.3964 | 0.8333 | 1.2544 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val18_test14 | 42 | 0.7500 | 0.7500 | 0.7268 | 0.9444 | 1.0113 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val14_test17 | 42 | 0.5833 | 0.5833 | 0.5643 | 0.7870 | 1.1406 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val17_test14 | 42 | 0.7500 | 0.7500 | 0.7667 | 0.9630 | 1.1365 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val14_test16 | 42 | 0.4167 | 0.4167 | 0.3958 | 0.6204 | 1.7272 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val16_test14 | 42 | 0.7500 | 0.7500 | 0.6667 | 0.9537 | 1.2621 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val14_test15 | 42 | 0.6667 | 0.6667 | 0.6583 | 0.8148 | 1.2520 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val15_test14 | 42 | 0.8333 | 0.8333 | 0.8375 | 0.8889 | 1.2160 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val13_test18 | 42 | 0.5833 | 0.5833 | 0.5095 | 0.7963 | 1.3490 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val18_test13 | 42 | 0.8333 | 0.8333 | 0.8036 | 0.9167 | 1.1985 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val13_test17 | 42 | 0.5833 | 0.5833 | 0.5750 | 0.8704 | 1.1105 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val17_test13 | 42 | 0.7500 | 0.7500 | 0.7268 | 0.9167 | 1.2465 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val13_test16 | 42 | 0.4167 | 0.4167 | 0.3750 | 0.6019 | 1.5860 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val16_test13 | 42 | 0.5833 | 0.5833 | 0.5167 | 0.8981 | 1.2853 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val13_test15 | 42 | 0.5000 | 0.5000 | 0.3864 | 0.8426 | 1.2923 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val15_test13 | 42 | 0.7500 | 0.7500 | 0.7429 | 0.9074 | 1.2650 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val13_test14 | 42 | 0.7500 | 0.7500 | 0.7268 | 0.9630 | 1.0760 |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val14_test13 | 42 | 0.6667 | 0.6667 | 0.6571 | 0.8981 | 1.1140 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val17_test18 | 1 | 0.2500 |  | 0.2500 |  | 0.2500 |  | 0.6204 |  | 1.3920 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val18_test17 | 1 | 0.3333 |  | 0.3333 |  | 0.3250 |  | 0.7037 |  | 1.3416 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val16_test18 | 1 | 0.5000 |  | 0.5000 |  | 0.4643 |  | 0.7593 |  | 1.3226 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val18_test16 | 1 | 0.4167 |  | 0.4167 |  | 0.3409 |  | 0.6574 |  | 1.3710 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val16_test17 | 1 | 0.7500 |  | 0.7500 |  | 0.7310 |  | 0.8704 |  | 1.2870 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val17_test16 | 1 | 0.2500 |  | 0.2500 |  | 0.1964 |  | 0.5000 |  | 1.7257 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val15_test18 | 1 | 0.4167 |  | 0.4167 |  | 0.3447 |  | 0.8056 |  | 1.4930 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val18_test15 | 1 | 0.5000 |  | 0.5000 |  | 0.4179 |  | 0.8704 |  | 1.4779 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val15_test17 | 1 | 0.5833 |  | 0.5833 |  | 0.5857 |  | 0.8333 |  | 1.2036 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val17_test15 | 1 | 0.5000 |  | 0.5000 |  | 0.4375 |  | 0.8889 |  | 1.2661 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val15_test16 | 1 | 0.4167 |  | 0.4167 |  | 0.4429 |  | 0.6204 |  | 1.5026 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val16_test15 | 1 | 0.6667 |  | 0.6667 |  | 0.5833 |  | 0.8981 |  | 1.2963 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val14_test18 | 1 | 0.4167 |  | 0.4167 |  | 0.3964 |  | 0.8333 |  | 1.2544 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val18_test14 | 1 | 0.7500 |  | 0.7500 |  | 0.7268 |  | 0.9444 |  | 1.0113 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val14_test17 | 1 | 0.5833 |  | 0.5833 |  | 0.5643 |  | 0.7870 |  | 1.1406 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val17_test14 | 1 | 0.7500 |  | 0.7500 |  | 0.7667 |  | 0.9630 |  | 1.1365 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val14_test16 | 1 | 0.4167 |  | 0.4167 |  | 0.3958 |  | 0.6204 |  | 1.7272 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val16_test14 | 1 | 0.7500 |  | 0.7500 |  | 0.6667 |  | 0.9537 |  | 1.2621 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val14_test15 | 1 | 0.6667 |  | 0.6667 |  | 0.6583 |  | 0.8148 |  | 1.2520 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val15_test14 | 1 | 0.8333 |  | 0.8333 |  | 0.8375 |  | 0.8889 |  | 1.2160 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val13_test18 | 1 | 0.5833 |  | 0.5833 |  | 0.5095 |  | 0.7963 |  | 1.3490 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val18_test13 | 1 | 0.8333 |  | 0.8333 |  | 0.8036 |  | 0.9167 |  | 1.1985 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val13_test17 | 1 | 0.5833 |  | 0.5833 |  | 0.5750 |  | 0.8704 |  | 1.1105 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val17_test13 | 1 | 0.7500 |  | 0.7500 |  | 0.7268 |  | 0.9167 |  | 1.2465 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val13_test16 | 1 | 0.4167 |  | 0.4167 |  | 0.3750 |  | 0.6019 |  | 1.5860 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val16_test13 | 1 | 0.5833 |  | 0.5833 |  | 0.5167 |  | 0.8981 |  | 1.2853 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val13_test15 | 1 | 0.5000 |  | 0.5000 |  | 0.3864 |  | 0.8426 |  | 1.2923 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val15_test13 | 1 | 0.7500 |  | 0.7500 |  | 0.7429 |  | 0.9074 |  | 1.2650 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val13_test14 | 1 | 0.7500 |  | 0.7500 |  | 0.7268 |  | 0.9630 |  | 1.0760 |  |
| cp3_s123 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val14_test13 | 1 | 0.6667 |  | 0.6667 |  | 0.6571 |  | 0.8981 |  | 1.1140 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s123 | resnet1D | resnet1D-843fbf2 | 42 | 30 | 0.5722 | 0.1677 | 0.5722 | 0.1677 | 0.5384 | 0.1763 | 0.8148 | 0.1247 | 1.3068 | 0.1729 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s123 | resnet1D | resnet1D-843fbf2 | 30 | 0.5722 | 0.1677 | 0.5722 | 0.1677 | 0.5384 | 0.1763 | 0.8148 | 0.1247 | 1.3068 | 0.1729 |

### Pooled confusion matrix: cp3_s123 / resnet1D / resnet1D-843fbf2

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 42 | 21 | 21 | 6 |
| B1 | 21 | 50 | 13 | 6 |
| B2 | 22 | 24 | 36 | 8 |
| B3 | 2 | 4 | 6 | 78 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 46.67 | 23.33 | 23.33 | 6.67 |
| B1 | 23.33 | 55.56 | 14.44 | 6.67 |
| B2 | 24.44 | 26.67 | 40.00 | 8.89 |
| B3 | 2.22 | 4.44 | 6.67 | 86.67 |
