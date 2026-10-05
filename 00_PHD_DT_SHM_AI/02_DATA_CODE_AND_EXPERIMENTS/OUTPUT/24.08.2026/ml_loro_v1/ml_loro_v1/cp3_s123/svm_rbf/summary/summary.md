# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-15-16_val17_test18 | 42 | 0.4167 | 0.4167 | 0.4325 | 0.6574 | 1.8545 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-15-16_val18_test17 | 42 | 0.5000 | 0.5000 | 0.5194 | 0.7407 | 1.6868 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-15-17_val16_test18 | 42 | 0.7500 | 0.7500 | 0.7542 | 0.8796 | 1.1864 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-15-17_val18_test16 | 42 | 0.4167 | 0.4167 | 0.4556 | 0.6389 | 1.8843 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-15-18_val16_test17 | 42 | 0.6667 | 0.6667 | 0.6000 | 0.9167 | 1.0745 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-15-18_val17_test16 | 42 | 0.3333 | 0.3333 | 0.3750 | 0.6204 | 1.8620 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-16-17_val15_test18 | 42 | 0.7500 | 0.7500 | 0.7268 | 0.9167 | 1.1476 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-16-17_val18_test15 | 42 | 0.8333 | 0.8333 | 0.8125 | 0.9815 | 0.8581 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-16-18_val15_test17 | 42 | 0.7500 | 0.7500 | 0.7595 | 0.9259 | 0.9698 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-16-18_val17_test15 | 42 | 0.7500 | 0.7500 | 0.7417 | 0.9815 | 0.9645 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-17-18_val15_test16 | 42 | 0.5000 | 0.5000 | 0.4778 | 0.7222 | 1.5331 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-17-18_val16_test15 | 42 | 0.7500 | 0.7500 | 0.7595 | 0.9537 | 0.9611 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-15-16-17_val14_test18 | 42 | 0.7500 | 0.7500 | 0.7268 | 0.9074 | 1.1278 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-15-16-17_val18_test14 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.5789 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-15-16-18_val14_test17 | 42 | 0.5833 | 0.5833 | 0.5861 | 0.8981 | 0.9827 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-15-16-18_val17_test14 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.6856 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-15-17-18_val14_test16 | 42 | 0.5000 | 0.5000 | 0.4861 | 0.6852 | 1.4983 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-15-17-18_val16_test14 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.5112 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-16-17-18_val14_test15 | 42 | 0.5000 | 0.5000 | 0.4364 | 0.8889 | 1.6308 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-16-17-18_val15_test14 | 42 | 0.7500 | 0.7500 | 0.7476 | 0.9259 | 1.1819 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train14-15-16-17_val13_test18 | 42 | 0.7500 | 0.7500 | 0.7268 | 0.9352 | 1.0986 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train14-15-16-17_val18_test13 | 42 | 0.8333 | 0.8333 | 0.8036 | 0.9722 | 0.9276 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train14-15-16-18_val13_test17 | 42 | 0.7500 | 0.7500 | 0.7500 | 0.8981 | 0.8924 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train14-15-16-18_val17_test13 | 42 | 0.7500 | 0.7500 | 0.7268 | 0.9815 | 0.9535 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train14-15-17-18_val13_test16 | 42 | 0.5000 | 0.5000 | 0.4750 | 0.7037 | 1.4271 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train14-15-17-18_val16_test13 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.7468 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train14-16-17-18_val13_test15 | 42 | 0.5833 | 0.5833 | 0.5643 | 0.8704 | 1.3342 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train14-16-17-18_val15_test13 | 42 | 0.5833 | 0.5833 | 0.5583 | 0.8889 | 1.3868 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train15-16-17-18_val13_test14 | 42 | 0.8333 | 0.8333 | 0.8286 | 0.9630 | 0.9214 |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train15-16-17-18_val14_test13 | 42 | 0.7500 | 0.7500 | 0.7202 | 0.8796 | 1.2031 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-15-16_val17_test18 | 1 | 0.4167 |  | 0.4167 |  | 0.4325 |  | 0.6574 |  | 1.8545 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-15-16_val18_test17 | 1 | 0.5000 |  | 0.5000 |  | 0.5194 |  | 0.7407 |  | 1.6868 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-15-17_val16_test18 | 1 | 0.7500 |  | 0.7500 |  | 0.7542 |  | 0.8796 |  | 1.1864 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-15-17_val18_test16 | 1 | 0.4167 |  | 0.4167 |  | 0.4556 |  | 0.6389 |  | 1.8843 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-15-18_val16_test17 | 1 | 0.6667 |  | 0.6667 |  | 0.6000 |  | 0.9167 |  | 1.0745 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-15-18_val17_test16 | 1 | 0.3333 |  | 0.3333 |  | 0.3750 |  | 0.6204 |  | 1.8620 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-16-17_val15_test18 | 1 | 0.7500 |  | 0.7500 |  | 0.7268 |  | 0.9167 |  | 1.1476 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-16-17_val18_test15 | 1 | 0.8333 |  | 0.8333 |  | 0.8125 |  | 0.9815 |  | 0.8581 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-16-18_val15_test17 | 1 | 0.7500 |  | 0.7500 |  | 0.7595 |  | 0.9259 |  | 0.9698 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-16-18_val17_test15 | 1 | 0.7500 |  | 0.7500 |  | 0.7417 |  | 0.9815 |  | 0.9645 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-17-18_val15_test16 | 1 | 0.5000 |  | 0.5000 |  | 0.4778 |  | 0.7222 |  | 1.5331 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-14-17-18_val16_test15 | 1 | 0.7500 |  | 0.7500 |  | 0.7595 |  | 0.9537 |  | 0.9611 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-15-16-17_val14_test18 | 1 | 0.7500 |  | 0.7500 |  | 0.7268 |  | 0.9074 |  | 1.1278 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-15-16-17_val18_test14 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.5789 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-15-16-18_val14_test17 | 1 | 0.5833 |  | 0.5833 |  | 0.5861 |  | 0.8981 |  | 0.9827 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-15-16-18_val17_test14 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.6856 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-15-17-18_val14_test16 | 1 | 0.5000 |  | 0.5000 |  | 0.4861 |  | 0.6852 |  | 1.4983 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-15-17-18_val16_test14 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.5112 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-16-17-18_val14_test15 | 1 | 0.5000 |  | 0.5000 |  | 0.4364 |  | 0.8889 |  | 1.6308 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train13-16-17-18_val15_test14 | 1 | 0.7500 |  | 0.7500 |  | 0.7476 |  | 0.9259 |  | 1.1819 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train14-15-16-17_val13_test18 | 1 | 0.7500 |  | 0.7500 |  | 0.7268 |  | 0.9352 |  | 1.0986 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train14-15-16-17_val18_test13 | 1 | 0.8333 |  | 0.8333 |  | 0.8036 |  | 0.9722 |  | 0.9276 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train14-15-16-18_val13_test17 | 1 | 0.7500 |  | 0.7500 |  | 0.7500 |  | 0.8981 |  | 0.8924 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train14-15-16-18_val17_test13 | 1 | 0.7500 |  | 0.7500 |  | 0.7268 |  | 0.9815 |  | 0.9535 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train14-15-17-18_val13_test16 | 1 | 0.5000 |  | 0.5000 |  | 0.4750 |  | 0.7037 |  | 1.4271 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train14-15-17-18_val16_test13 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.7468 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train14-16-17-18_val13_test15 | 1 | 0.5833 |  | 0.5833 |  | 0.5643 |  | 0.8704 |  | 1.3342 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train14-16-17-18_val15_test13 | 1 | 0.5833 |  | 0.5833 |  | 0.5583 |  | 0.8889 |  | 1.3868 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train15-16-17-18_val13_test14 | 1 | 0.8333 |  | 0.8333 |  | 0.8286 |  | 0.9630 |  | 0.9214 |  |
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | train15-16-17-18_val14_test13 | 1 | 0.7500 |  | 0.7500 |  | 0.7202 |  | 0.8796 |  | 1.2031 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | 42 | 30 | 0.6889 | 0.1750 | 0.6889 | 0.1750 | 0.6793 | 0.1727 | 0.8778 | 0.1188 | 1.1690 | 0.3730 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s123_svm_rbf | svm_rbf | svm_rbf-536c3a4 | 30 | 0.6889 | 0.1750 | 0.6889 | 0.1750 | 0.6793 | 0.1727 | 0.8778 | 0.1188 | 1.1690 | 0.3730 |

### Pooled confusion matrix: cp3_s123_svm_rbf / svm_rbf / svm_rbf-536c3a4

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 55 | 14 | 12 | 9 |
| B1 | 24 | 56 | 8 | 2 |
| B2 | 15 | 7 | 61 | 7 |
| B3 | 7 | 1 | 6 | 76 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 61.11 | 15.56 | 13.33 | 10.00 |
| B1 | 26.67 | 62.22 | 8.89 | 2.22 |
| B2 | 16.67 | 7.78 | 67.78 | 7.78 |
| B3 | 7.78 | 1.11 | 6.67 | 84.44 |
