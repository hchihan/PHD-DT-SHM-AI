# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-15-16_val17_test18 | 42 | 0.5833 | 0.5833 | 0.5114 | 0.8426 | 1.1196 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-15-16_val18_test17 | 42 | 0.5000 | 0.5000 | 0.4500 | 0.8148 | 1.1074 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-15-17_val16_test18 | 42 | 0.7500 | 0.7500 | 0.7417 | 0.9259 | 0.9750 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-15-17_val18_test16 | 42 | 0.5000 | 0.5000 | 0.3750 | 0.7963 | 1.1525 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-15-18_val16_test17 | 42 | 0.5833 | 0.5833 | 0.5114 | 0.9352 | 0.9716 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-15-18_val17_test16 | 42 | 0.5833 | 0.5833 | 0.5114 | 0.7130 | 1.1629 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-16-17_val15_test18 | 42 | 0.7500 | 0.7500 | 0.6667 | 0.9444 | 0.8911 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-16-17_val18_test15 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6446 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-16-18_val15_test17 | 42 | 0.7500 | 0.7500 | 0.7595 | 0.9352 | 0.8589 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-16-18_val17_test15 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6260 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-17-18_val15_test16 | 42 | 0.6667 | 0.6667 | 0.6000 | 0.8796 | 1.0025 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-17-18_val16_test15 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6081 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-15-16-17_val14_test18 | 42 | 0.8333 | 0.8333 | 0.8125 | 0.9630 | 0.8797 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-15-16-17_val18_test14 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.5886 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-15-16-18_val14_test17 | 42 | 0.8333 | 0.8333 | 0.8333 | 0.9352 | 0.8626 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-15-16-18_val17_test14 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6049 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-15-17-18_val14_test16 | 42 | 0.6667 | 0.6667 | 0.6000 | 0.8796 | 1.0183 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-15-17-18_val16_test14 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6064 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-16-17-18_val14_test15 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9907 | 0.8476 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-16-17-18_val15_test14 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8262 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train14-15-16-17_val13_test18 | 42 | 0.7500 | 0.7500 | 0.6667 | 0.9444 | 0.8765 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train14-15-16-17_val18_test13 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6441 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train14-15-16-18_val13_test17 | 42 | 0.7500 | 0.7500 | 0.7429 | 0.9259 | 0.8664 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train14-15-16-18_val17_test13 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6548 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train14-15-17-18_val13_test16 | 42 | 0.6667 | 0.6667 | 0.6000 | 0.8889 | 0.9937 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train14-15-17-18_val16_test13 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6340 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train14-16-17-18_val13_test15 | 42 | 1.0000 | 1.0000 | 1.0000 | 0.9907 | 0.8377 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train14-16-17-18_val15_test13 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8446 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train15-16-17-18_val13_test14 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.7775 |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train15-16-17-18_val14_test13 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.8376 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-15-16_val17_test18 | 1 | 0.5833 |  | 0.5833 |  | 0.5114 |  | 0.8426 |  | 1.1196 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-15-16_val18_test17 | 1 | 0.5000 |  | 0.5000 |  | 0.4500 |  | 0.8148 |  | 1.1074 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-15-17_val16_test18 | 1 | 0.7500 |  | 0.7500 |  | 0.7417 |  | 0.9259 |  | 0.9750 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-15-17_val18_test16 | 1 | 0.5000 |  | 0.5000 |  | 0.3750 |  | 0.7963 |  | 1.1525 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-15-18_val16_test17 | 1 | 0.5833 |  | 0.5833 |  | 0.5114 |  | 0.9352 |  | 0.9716 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-15-18_val17_test16 | 1 | 0.5833 |  | 0.5833 |  | 0.5114 |  | 0.7130 |  | 1.1629 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-16-17_val15_test18 | 1 | 0.7500 |  | 0.7500 |  | 0.6667 |  | 0.9444 |  | 0.8911 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-16-17_val18_test15 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.6446 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-16-18_val15_test17 | 1 | 0.7500 |  | 0.7500 |  | 0.7595 |  | 0.9352 |  | 0.8589 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-16-18_val17_test15 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.6260 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-17-18_val15_test16 | 1 | 0.6667 |  | 0.6667 |  | 0.6000 |  | 0.8796 |  | 1.0025 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-14-17-18_val16_test15 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.6081 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-15-16-17_val14_test18 | 1 | 0.8333 |  | 0.8333 |  | 0.8125 |  | 0.9630 |  | 0.8797 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-15-16-17_val18_test14 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.5886 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-15-16-18_val14_test17 | 1 | 0.8333 |  | 0.8333 |  | 0.8333 |  | 0.9352 |  | 0.8626 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-15-16-18_val17_test14 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.6049 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-15-17-18_val14_test16 | 1 | 0.6667 |  | 0.6667 |  | 0.6000 |  | 0.8796 |  | 1.0183 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-15-17-18_val16_test14 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.6064 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-16-17-18_val14_test15 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9907 |  | 0.8476 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train13-16-17-18_val15_test14 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.8262 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train14-15-16-17_val13_test18 | 1 | 0.7500 |  | 0.7500 |  | 0.6667 |  | 0.9444 |  | 0.8765 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train14-15-16-17_val18_test13 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.6441 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train14-15-16-18_val13_test17 | 1 | 0.7500 |  | 0.7500 |  | 0.7429 |  | 0.9259 |  | 0.8664 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train14-15-16-18_val17_test13 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.6548 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train14-15-17-18_val13_test16 | 1 | 0.6667 |  | 0.6667 |  | 0.6000 |  | 0.8889 |  | 0.9937 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train14-15-17-18_val16_test13 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.6340 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train14-16-17-18_val13_test15 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.9907 |  | 0.8377 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train14-16-17-18_val15_test13 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.8446 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train15-16-17-18_val13_test14 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.7775 |  |
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train15-16-17-18_val14_test13 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.8376 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | 42 | 30 | 0.8333 | 0.1764 | 0.8333 | 0.1764 | 0.8070 | 0.2087 | 0.9435 | 0.0742 | 0.8440 | 0.1767 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_extra_trees | extra_trees | extra_trees-536c3a4 | 30 | 0.8333 | 0.1764 | 0.8333 | 0.1764 | 0.8070 | 0.2087 | 0.9435 | 0.0742 | 0.8440 | 0.1767 |

### Pooled confusion matrix: cp3_s123_extra_trees / extra_trees / extra_trees-536c3a4

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 84 | 4 | 2 | 0 |
| B1 | 37 | 53 | 0 | 0 |
| B2 | 17 | 0 | 73 | 0 |
| B3 | 0 | 0 | 0 | 90 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 93.33 | 4.44 | 2.22 | 0.00 |
| B1 | 41.11 | 58.89 | 0.00 | 0.00 |
| B2 | 18.89 | 0.00 | 81.11 | 0.00 |
| B3 | 0.00 | 0.00 | 0.00 | 100.00 |
