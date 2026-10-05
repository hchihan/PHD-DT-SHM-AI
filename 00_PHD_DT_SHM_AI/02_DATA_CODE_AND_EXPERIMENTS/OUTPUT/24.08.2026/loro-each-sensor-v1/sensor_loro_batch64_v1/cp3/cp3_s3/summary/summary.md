# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val17_test18 | 42 | 0.4167 | 0.4167 | 0.3825 | 0.6852 | 1.2799 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val18_test17 | 42 | 0.4167 | 0.4167 | 0.3409 | 0.6204 | 1.3431 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val16_test18 | 42 | 0.5833 | 0.5833 | 0.5179 | 0.7593 | 1.2645 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val18_test16 | 42 | 0.4167 | 0.4167 | 0.3500 | 0.6204 | 1.4789 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val16_test17 | 42 | 0.5833 | 0.5833 | 0.5167 | 0.7963 | 1.2396 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val17_test16 | 42 | 0.4167 | 0.4167 | 0.3143 | 0.5648 | 1.3497 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val15_test18 | 42 | 0.5000 | 0.5000 | 0.4540 | 0.7778 | 1.2218 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val18_test15 | 42 | 0.5000 | 0.5000 | 0.4179 | 0.8981 | 1.0978 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val15_test17 | 42 | 0.5833 | 0.5833 | 0.5861 | 0.7407 | 1.2333 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val17_test15 | 42 | 0.5833 | 0.5833 | 0.5554 | 0.9352 | 0.9624 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val15_test16 | 42 | 0.5000 | 0.5000 | 0.4762 | 0.6481 | 1.5257 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val16_test15 | 42 | 0.5000 | 0.5000 | 0.3750 | 0.9074 | 1.2221 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val14_test18 | 42 | 0.6667 | 0.6667 | 0.6000 | 0.8333 | 1.0692 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val18_test14 | 42 | 0.8333 | 0.8333 | 0.8286 | 0.9907 | 0.8191 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val14_test17 | 42 | 0.5833 | 0.5833 | 0.5643 | 0.7685 | 1.2486 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val17_test14 | 42 | 0.8333 | 0.8333 | 0.8375 | 0.9537 | 0.9316 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val14_test16 | 42 | 0.4167 | 0.4167 | 0.3393 | 0.6389 | 1.4799 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val16_test14 | 42 | 0.5833 | 0.5833 | 0.5114 | 0.9352 | 1.2000 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val14_test15 | 42 | 0.6667 | 0.6667 | 0.6583 | 0.8056 | 1.1061 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val15_test14 | 42 | 0.5833 | 0.5833 | 0.5000 | 0.9167 | 1.1624 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val13_test18 | 42 | 0.5833 | 0.5833 | 0.5095 | 0.8241 | 1.1469 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val18_test13 | 42 | 0.6667 | 0.6667 | 0.5685 | 0.9444 | 1.0357 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val13_test17 | 42 | 0.5000 | 0.5000 | 0.4750 | 0.7130 | 1.3628 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val17_test13 | 42 | 0.5833 | 0.5833 | 0.4792 | 0.8981 | 1.0648 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val13_test16 | 42 | 0.4167 | 0.4167 | 0.3250 | 0.6759 | 1.6419 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val16_test13 | 42 | 0.6667 | 0.6667 | 0.6000 | 0.8889 | 1.2301 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val13_test15 | 42 | 0.5833 | 0.5833 | 0.5179 | 0.7963 | 1.1910 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val15_test13 | 42 | 0.4167 | 0.4167 | 0.3030 | 0.7685 | 1.2271 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val13_test14 | 42 | 0.8333 | 0.8333 | 0.8333 | 0.9259 | 0.9416 |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val14_test13 | 42 | 0.6667 | 0.6667 | 0.6500 | 0.9352 | 0.9835 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val17_test18 | 1 | 0.4167 |  | 0.4167 |  | 0.3825 |  | 0.6852 |  | 1.2799 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val18_test17 | 1 | 0.4167 |  | 0.4167 |  | 0.3409 |  | 0.6204 |  | 1.3431 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val16_test18 | 1 | 0.5833 |  | 0.5833 |  | 0.5179 |  | 0.7593 |  | 1.2645 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val18_test16 | 1 | 0.4167 |  | 0.4167 |  | 0.3500 |  | 0.6204 |  | 1.4789 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val16_test17 | 1 | 0.5833 |  | 0.5833 |  | 0.5167 |  | 0.7963 |  | 1.2396 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val17_test16 | 1 | 0.4167 |  | 0.4167 |  | 0.3143 |  | 0.5648 |  | 1.3497 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val15_test18 | 1 | 0.5000 |  | 0.5000 |  | 0.4540 |  | 0.7778 |  | 1.2218 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val18_test15 | 1 | 0.5000 |  | 0.5000 |  | 0.4179 |  | 0.8981 |  | 1.0978 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val15_test17 | 1 | 0.5833 |  | 0.5833 |  | 0.5861 |  | 0.7407 |  | 1.2333 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val17_test15 | 1 | 0.5833 |  | 0.5833 |  | 0.5554 |  | 0.9352 |  | 0.9624 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val15_test16 | 1 | 0.5000 |  | 0.5000 |  | 0.4762 |  | 0.6481 |  | 1.5257 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val16_test15 | 1 | 0.5000 |  | 0.5000 |  | 0.3750 |  | 0.9074 |  | 1.2221 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val14_test18 | 1 | 0.6667 |  | 0.6667 |  | 0.6000 |  | 0.8333 |  | 1.0692 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val18_test14 | 1 | 0.8333 |  | 0.8333 |  | 0.8286 |  | 0.9907 |  | 0.8191 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val14_test17 | 1 | 0.5833 |  | 0.5833 |  | 0.5643 |  | 0.7685 |  | 1.2486 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val17_test14 | 1 | 0.8333 |  | 0.8333 |  | 0.8375 |  | 0.9537 |  | 0.9316 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val14_test16 | 1 | 0.4167 |  | 0.4167 |  | 0.3393 |  | 0.6389 |  | 1.4799 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val16_test14 | 1 | 0.5833 |  | 0.5833 |  | 0.5114 |  | 0.9352 |  | 1.2000 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val14_test15 | 1 | 0.6667 |  | 0.6667 |  | 0.6583 |  | 0.8056 |  | 1.1061 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val15_test14 | 1 | 0.5833 |  | 0.5833 |  | 0.5000 |  | 0.9167 |  | 1.1624 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val13_test18 | 1 | 0.5833 |  | 0.5833 |  | 0.5095 |  | 0.8241 |  | 1.1469 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val18_test13 | 1 | 0.6667 |  | 0.6667 |  | 0.5685 |  | 0.9444 |  | 1.0357 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val13_test17 | 1 | 0.5000 |  | 0.5000 |  | 0.4750 |  | 0.7130 |  | 1.3628 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val17_test13 | 1 | 0.5833 |  | 0.5833 |  | 0.4792 |  | 0.8981 |  | 1.0648 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val13_test16 | 1 | 0.4167 |  | 0.4167 |  | 0.3250 |  | 0.6759 |  | 1.6419 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val16_test13 | 1 | 0.6667 |  | 0.6667 |  | 0.6000 |  | 0.8889 |  | 1.2301 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val13_test15 | 1 | 0.5833 |  | 0.5833 |  | 0.5179 |  | 0.7963 |  | 1.1910 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val15_test13 | 1 | 0.4167 |  | 0.4167 |  | 0.3030 |  | 0.7685 |  | 1.2271 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val13_test14 | 1 | 0.8333 |  | 0.8333 |  | 0.8333 |  | 0.9259 |  | 0.9416 |  |
| cp3_s3 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val14_test13 | 1 | 0.6667 |  | 0.6667 |  | 0.6500 |  | 0.9352 |  | 0.9835 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s3 | resnet1D | resnet1D-843fbf2 | 42 | 30 | 0.5694 | 0.1240 | 0.5694 | 0.1240 | 0.5129 | 0.1478 | 0.8056 | 0.1200 | 1.2020 | 0.1874 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s3 | resnet1D | resnet1D-843fbf2 | 30 | 0.5694 | 0.1240 | 0.5694 | 0.1240 | 0.5129 | 0.1478 | 0.8056 | 0.1200 | 1.2020 | 0.1874 |

### Pooled confusion matrix: cp3_s3 / resnet1D / resnet1D-843fbf2

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 51 | 18 | 14 | 7 |
| B1 | 35 | 33 | 16 | 6 |
| B2 | 26 | 23 | 37 | 4 |
| B3 | 3 | 0 | 3 | 84 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 56.67 | 20.00 | 15.56 | 7.78 |
| B1 | 38.89 | 36.67 | 17.78 | 6.67 |
| B2 | 28.89 | 25.56 | 41.11 | 4.44 |
| B3 | 3.33 | 0.00 | 3.33 | 93.33 |
