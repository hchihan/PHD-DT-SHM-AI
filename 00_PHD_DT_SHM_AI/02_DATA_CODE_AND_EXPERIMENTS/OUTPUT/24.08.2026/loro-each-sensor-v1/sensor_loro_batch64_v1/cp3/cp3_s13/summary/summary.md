# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val17_test18 | 42 | 0.5000 | 0.5000 | 0.5083 | 0.7222 | 1.3731 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val18_test17 | 42 | 0.5000 | 0.5000 | 0.3750 | 0.7870 | 1.3156 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val16_test18 | 42 | 0.6667 | 0.6667 | 0.6375 | 0.7500 | 1.3306 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val18_test16 | 42 | 0.2500 | 0.2500 | 0.1667 | 0.6944 | 1.4266 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val16_test17 | 42 | 0.5000 | 0.5000 | 0.3750 | 0.8426 | 1.2788 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val17_test16 | 42 | 0.5000 | 0.5000 | 0.4435 | 0.6481 | 1.5507 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val15_test18 | 42 | 0.5833 | 0.5833 | 0.5095 | 0.8241 | 1.6349 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val18_test15 | 42 | 0.6667 | 0.6667 | 0.6583 | 0.9444 | 0.9788 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val15_test17 | 42 | 0.5833 | 0.5833 | 0.5750 | 0.8426 | 1.1572 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val17_test15 | 42 | 0.6667 | 0.6667 | 0.6667 | 0.9167 | 1.0174 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val15_test16 | 42 | 0.3333 | 0.3333 | 0.3111 | 0.6667 | 1.4917 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val16_test15 | 42 | 0.7500 | 0.7500 | 0.7571 | 0.8889 | 1.1680 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val14_test18 | 42 | 0.5000 | 0.5000 | 0.4333 | 0.8333 | 1.3477 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val18_test14 | 42 | 0.5833 | 0.5833 | 0.5167 | 0.8981 | 1.1511 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val14_test17 | 42 | 0.5000 | 0.5000 | 0.4940 | 0.8426 | 1.1200 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val17_test14 | 42 | 0.7500 | 0.7500 | 0.7310 | 0.9630 | 1.0222 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val14_test16 | 42 | 0.3333 | 0.3333 | 0.3095 | 0.6574 | 1.5292 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val16_test14 | 42 | 0.8333 | 0.8333 | 0.8333 | 0.9722 | 0.9419 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val14_test15 | 42 | 0.6667 | 0.6667 | 0.6310 | 0.8889 | 1.0533 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val15_test14 | 42 | 0.6667 | 0.6667 | 0.6542 | 0.8889 | 1.2451 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val13_test18 | 42 | 0.5000 | 0.5000 | 0.4500 | 0.8333 | 1.2426 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val18_test13 | 42 | 0.7500 | 0.7500 | 0.7417 | 0.9444 | 1.1544 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val13_test17 | 42 | 0.5833 | 0.5833 | 0.5643 | 0.8241 | 1.1964 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val17_test13 | 42 | 0.7500 | 0.7500 | 0.7268 | 0.9259 | 1.1369 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val13_test16 | 42 | 0.3333 | 0.3333 | 0.3000 | 0.6667 | 1.4750 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val16_test13 | 42 | 0.5833 | 0.5833 | 0.5114 | 0.8981 | 1.2578 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val13_test15 | 42 | 0.4167 | 0.4167 | 0.3500 | 0.8241 | 1.2587 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val15_test13 | 42 | 0.5000 | 0.5000 | 0.3506 | 0.7685 | 1.3826 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val13_test14 | 42 | 0.6667 | 0.6667 | 0.6750 | 0.9630 | 1.0155 |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val14_test13 | 42 | 0.5833 | 0.5833 | 0.5750 | 0.8889 | 1.0366 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val17_test18 | 1 | 0.5000 |  | 0.5000 |  | 0.5083 |  | 0.7222 |  | 1.3731 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val18_test17 | 1 | 0.5000 |  | 0.5000 |  | 0.3750 |  | 0.7870 |  | 1.3156 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val16_test18 | 1 | 0.6667 |  | 0.6667 |  | 0.6375 |  | 0.7500 |  | 1.3306 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val18_test16 | 1 | 0.2500 |  | 0.2500 |  | 0.1667 |  | 0.6944 |  | 1.4266 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val16_test17 | 1 | 0.5000 |  | 0.5000 |  | 0.3750 |  | 0.8426 |  | 1.2788 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val17_test16 | 1 | 0.5000 |  | 0.5000 |  | 0.4435 |  | 0.6481 |  | 1.5507 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val15_test18 | 1 | 0.5833 |  | 0.5833 |  | 0.5095 |  | 0.8241 |  | 1.6349 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val18_test15 | 1 | 0.6667 |  | 0.6667 |  | 0.6583 |  | 0.9444 |  | 0.9788 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val15_test17 | 1 | 0.5833 |  | 0.5833 |  | 0.5750 |  | 0.8426 |  | 1.1572 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val17_test15 | 1 | 0.6667 |  | 0.6667 |  | 0.6667 |  | 0.9167 |  | 1.0174 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val15_test16 | 1 | 0.3333 |  | 0.3333 |  | 0.3111 |  | 0.6667 |  | 1.4917 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val16_test15 | 1 | 0.7500 |  | 0.7500 |  | 0.7571 |  | 0.8889 |  | 1.1680 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val14_test18 | 1 | 0.5000 |  | 0.5000 |  | 0.4333 |  | 0.8333 |  | 1.3477 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val18_test14 | 1 | 0.5833 |  | 0.5833 |  | 0.5167 |  | 0.8981 |  | 1.1511 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val14_test17 | 1 | 0.5000 |  | 0.5000 |  | 0.4940 |  | 0.8426 |  | 1.1200 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val17_test14 | 1 | 0.7500 |  | 0.7500 |  | 0.7310 |  | 0.9630 |  | 1.0222 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val14_test16 | 1 | 0.3333 |  | 0.3333 |  | 0.3095 |  | 0.6574 |  | 1.5292 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val16_test14 | 1 | 0.8333 |  | 0.8333 |  | 0.8333 |  | 0.9722 |  | 0.9419 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val14_test15 | 1 | 0.6667 |  | 0.6667 |  | 0.6310 |  | 0.8889 |  | 1.0533 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val15_test14 | 1 | 0.6667 |  | 0.6667 |  | 0.6542 |  | 0.8889 |  | 1.2451 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val13_test18 | 1 | 0.5000 |  | 0.5000 |  | 0.4500 |  | 0.8333 |  | 1.2426 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val18_test13 | 1 | 0.7500 |  | 0.7500 |  | 0.7417 |  | 0.9444 |  | 1.1544 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val13_test17 | 1 | 0.5833 |  | 0.5833 |  | 0.5643 |  | 0.8241 |  | 1.1964 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val17_test13 | 1 | 0.7500 |  | 0.7500 |  | 0.7268 |  | 0.9259 |  | 1.1369 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val13_test16 | 1 | 0.3333 |  | 0.3333 |  | 0.3000 |  | 0.6667 |  | 1.4750 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val16_test13 | 1 | 0.5833 |  | 0.5833 |  | 0.5114 |  | 0.8981 |  | 1.2578 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val13_test15 | 1 | 0.4167 |  | 0.4167 |  | 0.3500 |  | 0.8241 |  | 1.2587 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val15_test13 | 1 | 0.5000 |  | 0.5000 |  | 0.3506 |  | 0.7685 |  | 1.3826 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val13_test14 | 1 | 0.6667 |  | 0.6667 |  | 0.6750 |  | 0.9630 |  | 1.0155 |  |
| cp3_s13 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val14_test13 | 1 | 0.5833 |  | 0.5833 |  | 0.5750 |  | 0.8889 |  | 1.0366 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s13 | resnet1D | resnet1D-843fbf2 | 42 | 30 | 0.5667 | 0.1425 | 0.5667 | 0.1425 | 0.5277 | 0.1646 | 0.8336 | 0.0983 | 1.2430 | 0.1848 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s13 | resnet1D | resnet1D-843fbf2 | 30 | 0.5667 | 0.1425 | 0.5667 | 0.1425 | 0.5277 | 0.1646 | 0.8336 | 0.0983 | 1.2430 | 0.1848 |

### Pooled confusion matrix: cp3_s13 / resnet1D / resnet1D-843fbf2

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 38 | 16 | 25 | 11 |
| B1 | 22 | 34 | 23 | 11 |
| B2 | 18 | 11 | 53 | 8 |
| B3 | 4 | 3 | 4 | 79 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 42.22 | 17.78 | 27.78 | 12.22 |
| B1 | 24.44 | 37.78 | 25.56 | 12.22 |
| B2 | 20.00 | 12.22 | 58.89 | 8.89 |
| B3 | 4.44 | 3.33 | 4.44 | 87.78 |
