# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-15-16_val17_test18 | 42 | 0.5000 | 0.5000 | 0.5214 | 0.8148 | 1.7840 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-15-16_val18_test17 | 42 | 0.5833 | 0.5833 | 0.5861 | 0.7963 | 1.9471 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-15-17_val16_test18 | 42 | 0.8333 | 0.8333 | 0.8286 | 0.9259 | 1.4611 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-15-17_val18_test16 | 42 | 0.5833 | 0.5833 | 0.5278 | 0.7593 | 2.1952 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-15-18_val16_test17 | 42 | 0.6667 | 0.6667 | 0.6458 | 0.9352 | 1.3710 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-15-18_val17_test16 | 42 | 0.5000 | 0.5000 | 0.4881 | 0.7500 | 1.9599 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-16-17_val15_test18 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9630 | 0.8835 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-16-17_val18_test15 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.5683 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-16-18_val15_test17 | 42 | 0.8333 | 0.8333 | 0.8333 | 0.9074 | 1.0242 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-16-18_val17_test15 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.5681 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-17-18_val15_test16 | 42 | 0.5000 | 0.5000 | 0.4881 | 0.8426 | 1.7731 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-17-18_val16_test15 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4912 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-15-16-17_val14_test18 | 42 | 0.8333 | 0.8333 | 0.8286 | 0.9815 | 0.9104 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-15-16-17_val18_test14 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4128 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-15-16-18_val14_test17 | 42 | 0.6667 | 0.6667 | 0.6667 | 0.9537 | 0.9953 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-15-16-18_val17_test14 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3615 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-15-17-18_val14_test16 | 42 | 0.6667 | 0.6667 | 0.6762 | 0.8241 | 1.4637 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-15-17-18_val16_test14 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3229 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-16-17-18_val14_test15 | 42 | 0.7500 | 0.7500 | 0.7321 | 0.9907 | 0.9997 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-16-17-18_val15_test14 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.9079 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train14-15-16-17_val13_test18 | 42 | 0.8333 | 0.8333 | 0.8286 | 0.9537 | 0.9320 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train14-15-16-17_val18_test13 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3727 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train14-15-16-18_val13_test17 | 42 | 0.7500 | 0.7500 | 0.7595 | 0.9630 | 0.9056 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train14-15-16-18_val17_test13 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3568 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train14-15-17-18_val13_test16 | 42 | 0.6667 | 0.6667 | 0.6762 | 0.8426 | 1.5162 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train14-15-17-18_val16_test13 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3911 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train14-16-17-18_val13_test15 | 42 | 0.8333 | 0.8333 | 0.8375 | 0.9630 | 1.0289 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train14-16-17-18_val15_test13 | 42 | 0.8333 | 0.8333 | 0.8125 | 0.9815 | 0.9080 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train15-16-17-18_val13_test14 | 42 | 0.8333 | 0.8333 | 0.8375 | 0.9907 | 0.9452 |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train15-16-17-18_val14_test13 | 42 | 0.8333 | 0.8333 | 0.8375 | 0.9630 | 1.0637 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-15-16_val17_test18 | 1 | 0.5000 |  | 0.5000 |  | 0.5214 |  | 0.8148 |  | 1.7840 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-15-16_val18_test17 | 1 | 0.5833 |  | 0.5833 |  | 0.5861 |  | 0.7963 |  | 1.9471 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-15-17_val16_test18 | 1 | 0.8333 |  | 0.8333 |  | 0.8286 |  | 0.9259 |  | 1.4611 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-15-17_val18_test16 | 1 | 0.5833 |  | 0.5833 |  | 0.5278 |  | 0.7593 |  | 2.1952 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-15-18_val16_test17 | 1 | 0.6667 |  | 0.6667 |  | 0.6458 |  | 0.9352 |  | 1.3710 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-15-18_val17_test16 | 1 | 0.5000 |  | 0.5000 |  | 0.4881 |  | 0.7500 |  | 1.9599 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-16-17_val15_test18 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9630 |  | 0.8835 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-16-17_val18_test15 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.5683 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-16-18_val15_test17 | 1 | 0.8333 |  | 0.8333 |  | 0.8333 |  | 0.9074 |  | 1.0242 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-16-18_val17_test15 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.5681 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-17-18_val15_test16 | 1 | 0.5000 |  | 0.5000 |  | 0.4881 |  | 0.8426 |  | 1.7731 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-14-17-18_val16_test15 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.4912 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-15-16-17_val14_test18 | 1 | 0.8333 |  | 0.8333 |  | 0.8286 |  | 0.9815 |  | 0.9104 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-15-16-17_val18_test14 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.4128 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-15-16-18_val14_test17 | 1 | 0.6667 |  | 0.6667 |  | 0.6667 |  | 0.9537 |  | 0.9953 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-15-16-18_val17_test14 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3615 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-15-17-18_val14_test16 | 1 | 0.6667 |  | 0.6667 |  | 0.6762 |  | 0.8241 |  | 1.4637 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-15-17-18_val16_test14 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3229 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-16-17-18_val14_test15 | 1 | 0.7500 |  | 0.7500 |  | 0.7321 |  | 0.9907 |  | 0.9997 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train13-16-17-18_val15_test14 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.9079 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train14-15-16-17_val13_test18 | 1 | 0.8333 |  | 0.8333 |  | 0.8286 |  | 0.9537 |  | 0.9320 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train14-15-16-17_val18_test13 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3727 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train14-15-16-18_val13_test17 | 1 | 0.7500 |  | 0.7500 |  | 0.7595 |  | 0.9630 |  | 0.9056 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train14-15-16-18_val17_test13 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3568 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train14-15-17-18_val13_test16 | 1 | 0.6667 |  | 0.6667 |  | 0.6762 |  | 0.8426 |  | 1.5162 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train14-15-17-18_val16_test13 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3911 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train14-16-17-18_val13_test15 | 1 | 0.8333 |  | 0.8333 |  | 0.8375 |  | 0.9630 |  | 1.0289 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train14-16-17-18_val15_test13 | 1 | 0.8333 |  | 0.8333 |  | 0.8125 |  | 0.9815 |  | 0.9080 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train15-16-17-18_val13_test14 | 1 | 0.8333 |  | 0.8333 |  | 0.8375 |  | 0.9907 |  | 0.9452 |  |
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | train15-16-17-18_val14_test13 | 1 | 0.8333 |  | 0.8333 |  | 0.8375 |  | 0.9630 |  | 1.0637 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | 42 | 30 | 0.8083 | 0.1669 | 0.8083 | 0.1669 | 0.8052 | 0.1699 | 0.9361 | 0.0796 | 1.0274 | 0.5366 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_hist_gradient_boosting | hist_gradient_boosting | hist_gradient_boosting-536c3a4 | 30 | 0.8083 | 0.1669 | 0.8083 | 0.1669 | 0.8052 | 0.1699 | 0.9361 | 0.0796 | 1.0274 | 0.5366 |

### Pooled confusion matrix: cp3_s123_hist_gradient_boosting / hist_gradient_boosting / hist_gradient_boosting-536c3a4

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 69 | 11 | 10 | 0 |
| B1 | 22 | 63 | 5 | 0 |
| B2 | 10 | 5 | 73 | 2 |
| B3 | 0 | 0 | 4 | 86 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 76.67 | 12.22 | 11.11 | 0.00 |
| B1 | 24.44 | 70.00 | 5.56 | 0.00 |
| B2 | 11.11 | 5.56 | 81.11 | 2.22 |
| B3 | 0.00 | 0.00 | 4.44 | 95.56 |
