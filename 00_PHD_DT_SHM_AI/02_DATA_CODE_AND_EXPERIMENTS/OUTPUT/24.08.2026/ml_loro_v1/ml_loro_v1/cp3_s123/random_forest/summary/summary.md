# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-15-16_val17_test18 | 42 | 0.5833 | 0.5833 | 0.5114 | 0.8056 | 1.1213 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-15-16_val18_test17 | 42 | 0.5000 | 0.5000 | 0.4750 | 0.7870 | 1.0832 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-15-17_val16_test18 | 42 | 0.8333 | 0.8333 | 0.8125 | 0.9537 | 0.9566 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-15-17_val18_test16 | 42 | 0.5833 | 0.5833 | 0.5114 | 0.8056 | 1.1194 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-15-18_val16_test17 | 42 | 0.7500 | 0.7500 | 0.7417 | 0.9630 | 0.9390 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-15-18_val17_test16 | 42 | 0.6667 | 0.6667 | 0.6000 | 0.7222 | 1.1436 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-16-17_val15_test18 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9630 | 0.8536 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-16-17_val18_test15 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6214 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-16-18_val15_test17 | 42 | 0.8333 | 0.8333 | 0.8333 | 0.9352 | 0.8368 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-16-18_val17_test15 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6114 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-17-18_val15_test16 | 42 | 0.7500 | 0.7500 | 0.7417 | 0.8519 | 0.9848 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-17-18_val16_test15 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6130 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-15-16-17_val14_test18 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9537 | 0.8454 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-15-16-17_val18_test14 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.5945 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-15-16-18_val14_test17 | 42 | 0.8333 | 0.8333 | 0.8333 | 0.9444 | 0.8435 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-15-16-18_val17_test14 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6023 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-15-17-18_val14_test16 | 42 | 0.6667 | 0.6667 | 0.6000 | 0.8611 | 0.9816 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-15-17-18_val16_test14 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.5910 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-16-17-18_val14_test15 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.8583 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-16-17-18_val15_test14 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8438 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train14-15-16-17_val13_test18 | 42 | 0.8333 | 0.8333 | 0.8125 | 0.9537 | 0.8457 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train14-15-16-17_val18_test13 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6513 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train14-15-16-18_val13_test17 | 42 | 0.8333 | 0.8333 | 0.8333 | 0.9259 | 0.8386 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train14-15-16-18_val17_test13 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6381 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train14-15-17-18_val13_test16 | 42 | 0.6667 | 0.6667 | 0.6000 | 0.8611 | 0.9727 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train14-15-17-18_val16_test13 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6236 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train14-16-17-18_val13_test15 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9907 | 0.8630 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train14-16-17-18_val15_test13 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.8613 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train15-16-17-18_val13_test14 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8019 |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train15-16-17-18_val14_test13 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.8572 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-15-16_val17_test18 | 1 | 0.5833 |  | 0.5833 |  | 0.5114 |  | 0.8056 |  | 1.1213 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-15-16_val18_test17 | 1 | 0.5000 |  | 0.5000 |  | 0.4750 |  | 0.7870 |  | 1.0832 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-15-17_val16_test18 | 1 | 0.8333 |  | 0.8333 |  | 0.8125 |  | 0.9537 |  | 0.9566 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-15-17_val18_test16 | 1 | 0.5833 |  | 0.5833 |  | 0.5114 |  | 0.8056 |  | 1.1194 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-15-18_val16_test17 | 1 | 0.7500 |  | 0.7500 |  | 0.7417 |  | 0.9630 |  | 0.9390 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-15-18_val17_test16 | 1 | 0.6667 |  | 0.6667 |  | 0.6000 |  | 0.7222 |  | 1.1436 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-16-17_val15_test18 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9630 |  | 0.8536 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-16-17_val18_test15 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.6214 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-16-18_val15_test17 | 1 | 0.8333 |  | 0.8333 |  | 0.8333 |  | 0.9352 |  | 0.8368 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-16-18_val17_test15 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.6114 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-17-18_val15_test16 | 1 | 0.7500 |  | 0.7500 |  | 0.7417 |  | 0.8519 |  | 0.9848 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-14-17-18_val16_test15 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.6130 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-15-16-17_val14_test18 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9537 |  | 0.8454 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-15-16-17_val18_test14 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.5945 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-15-16-18_val14_test17 | 1 | 0.8333 |  | 0.8333 |  | 0.8333 |  | 0.9444 |  | 0.8435 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-15-16-18_val17_test14 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.6023 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-15-17-18_val14_test16 | 1 | 0.6667 |  | 0.6667 |  | 0.6000 |  | 0.8611 |  | 0.9816 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-15-17-18_val16_test14 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.5910 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-16-17-18_val14_test15 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.8583 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train13-16-17-18_val15_test14 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.8438 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train14-15-16-17_val13_test18 | 1 | 0.8333 |  | 0.8333 |  | 0.8125 |  | 0.9537 |  | 0.8457 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train14-15-16-17_val18_test13 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.6513 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train14-15-16-18_val13_test17 | 1 | 0.8333 |  | 0.8333 |  | 0.8333 |  | 0.9259 |  | 0.8386 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train14-15-16-18_val17_test13 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.6381 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train14-15-17-18_val13_test16 | 1 | 0.6667 |  | 0.6667 |  | 0.6000 |  | 0.8611 |  | 0.9727 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train14-15-17-18_val16_test13 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.6236 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train14-16-17-18_val13_test15 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9907 |  | 0.8630 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train14-16-17-18_val15_test13 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.8613 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train15-16-17-18_val13_test14 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.8019 |  |
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | train15-16-17-18_val14_test13 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.8572 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | 42 | 30 | 0.8611 | 0.1506 | 0.8611 | 0.1506 | 0.8464 | 0.1719 | 0.9420 | 0.0788 | 0.8333 | 0.1708 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_random_forest | random_forest | random_forest-536c3a4 | 30 | 0.8611 | 0.1506 | 0.8611 | 0.1506 | 0.8464 | 0.1719 | 0.9420 | 0.0788 | 0.8333 | 0.1708 |

### Pooled confusion matrix: cp3_s123_random_forest / random_forest / random_forest-536c3a4

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 82 | 4 | 4 | 0 |
| B1 | 31 | 59 | 0 | 0 |
| B2 | 11 | 0 | 79 | 0 |
| B3 | 0 | 0 | 0 | 90 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 91.11 | 4.44 | 4.44 | 0.00 |
| B1 | 34.44 | 65.56 | 0.00 | 0.00 |
| B2 | 12.22 | 0.00 | 87.78 | 0.00 |
| B3 | 0.00 | 0.00 | 0.00 | 100.00 |
