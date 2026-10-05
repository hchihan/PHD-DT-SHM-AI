# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val17_test18 | 42 | 0.4167 | 0.4167 | 0.3583 | 0.6667 | 1.4581 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val18_test17 | 42 | 0.4167 | 0.4167 | 0.3154 | 0.7037 | 1.3226 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val16_test18 | 42 | 0.3333 | 0.3333 | 0.2321 | 0.7315 | 1.3411 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val18_test16 | 42 | 0.4167 | 0.4167 | 0.3154 | 0.6389 | 1.3550 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val16_test17 | 42 | 0.4167 | 0.4167 | 0.3154 | 0.7315 | 1.3209 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val17_test16 | 42 | 0.3333 | 0.3333 | 0.3111 | 0.4630 | 1.8111 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val15_test18 | 42 | 0.5000 | 0.5000 | 0.4364 | 0.8241 | 1.5681 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val18_test15 | 42 | 0.5833 | 0.5833 | 0.5167 | 0.8981 | 1.2145 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val15_test17 | 42 | 0.6667 | 0.6667 | 0.6595 | 0.8333 | 1.1327 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val17_test15 | 42 | 0.5833 | 0.5833 | 0.5167 | 0.9074 | 0.9977 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val15_test16 | 42 | 0.3333 | 0.3333 | 0.3389 | 0.5833 | 1.7394 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val16_test15 | 42 | 0.7500 | 0.7500 | 0.7310 | 0.8704 | 1.2059 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val14_test18 | 42 | 0.5000 | 0.5000 | 0.4333 | 0.7870 | 1.4342 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val18_test14 | 42 | 0.6667 | 0.6667 | 0.5810 | 0.9630 | 0.9431 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val14_test17 | 42 | 0.5000 | 0.5000 | 0.4464 | 0.7778 | 1.1631 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val17_test14 | 42 | 0.7500 | 0.7500 | 0.7268 | 0.9352 | 0.9330 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val14_test16 | 42 | 0.4167 | 0.4167 | 0.4048 | 0.5926 | 1.5237 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val16_test14 | 42 | 0.5000 | 0.5000 | 0.4500 | 0.9074 | 1.2664 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val14_test15 | 42 | 0.5000 | 0.5000 | 0.4792 | 0.8333 | 1.1188 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val15_test14 | 42 | 0.6667 | 0.6667 | 0.6458 | 0.8241 | 1.2424 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val13_test18 | 42 | 0.5833 | 0.5833 | 0.5167 | 0.8333 | 1.2548 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val18_test13 | 42 | 0.6667 | 0.6667 | 0.6488 | 0.8796 | 1.1006 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val13_test17 | 42 | 0.5833 | 0.5833 | 0.5833 | 0.8241 | 1.1808 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val17_test13 | 42 | 0.5833 | 0.5833 | 0.5000 | 0.8981 | 1.1550 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val13_test16 | 42 | 0.2500 | 0.2500 | 0.2625 | 0.5741 | 1.5731 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val16_test13 | 42 | 0.5833 | 0.5833 | 0.4792 | 0.8796 | 1.2180 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val13_test15 | 42 | 0.5000 | 0.5000 | 0.3750 | 0.8241 | 1.2825 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val15_test13 | 42 | 0.2500 | 0.2500 | 0.2250 | 0.7130 | 1.3848 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val13_test14 | 42 | 0.7500 | 0.7500 | 0.6667 | 0.9630 | 0.9382 |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val14_test13 | 42 | 0.6667 | 0.6667 | 0.6667 | 0.8796 | 1.0308 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val17_test18 | 1 | 0.4167 |  | 0.4167 |  | 0.3583 |  | 0.6667 |  | 1.4581 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val18_test17 | 1 | 0.4167 |  | 0.4167 |  | 0.3154 |  | 0.7037 |  | 1.3226 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val16_test18 | 1 | 0.3333 |  | 0.3333 |  | 0.2321 |  | 0.7315 |  | 1.3411 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val18_test16 | 1 | 0.4167 |  | 0.4167 |  | 0.3154 |  | 0.6389 |  | 1.3550 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val16_test17 | 1 | 0.4167 |  | 0.4167 |  | 0.3154 |  | 0.7315 |  | 1.3209 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val17_test16 | 1 | 0.3333 |  | 0.3333 |  | 0.3111 |  | 0.4630 |  | 1.8111 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val15_test18 | 1 | 0.5000 |  | 0.5000 |  | 0.4364 |  | 0.8241 |  | 1.5681 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val18_test15 | 1 | 0.5833 |  | 0.5833 |  | 0.5167 |  | 0.8981 |  | 1.2145 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val15_test17 | 1 | 0.6667 |  | 0.6667 |  | 0.6595 |  | 0.8333 |  | 1.1327 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val17_test15 | 1 | 0.5833 |  | 0.5833 |  | 0.5167 |  | 0.9074 |  | 0.9977 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val15_test16 | 1 | 0.3333 |  | 0.3333 |  | 0.3389 |  | 0.5833 |  | 1.7394 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val16_test15 | 1 | 0.7500 |  | 0.7500 |  | 0.7310 |  | 0.8704 |  | 1.2059 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val14_test18 | 1 | 0.5000 |  | 0.5000 |  | 0.4333 |  | 0.7870 |  | 1.4342 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val18_test14 | 1 | 0.6667 |  | 0.6667 |  | 0.5810 |  | 0.9630 |  | 0.9431 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val14_test17 | 1 | 0.5000 |  | 0.5000 |  | 0.4464 |  | 0.7778 |  | 1.1631 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val17_test14 | 1 | 0.7500 |  | 0.7500 |  | 0.7268 |  | 0.9352 |  | 0.9330 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val14_test16 | 1 | 0.4167 |  | 0.4167 |  | 0.4048 |  | 0.5926 |  | 1.5237 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val16_test14 | 1 | 0.5000 |  | 0.5000 |  | 0.4500 |  | 0.9074 |  | 1.2664 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val14_test15 | 1 | 0.5000 |  | 0.5000 |  | 0.4792 |  | 0.8333 |  | 1.1188 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val15_test14 | 1 | 0.6667 |  | 0.6667 |  | 0.6458 |  | 0.8241 |  | 1.2424 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val13_test18 | 1 | 0.5833 |  | 0.5833 |  | 0.5167 |  | 0.8333 |  | 1.2548 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val18_test13 | 1 | 0.6667 |  | 0.6667 |  | 0.6488 |  | 0.8796 |  | 1.1006 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val13_test17 | 1 | 0.5833 |  | 0.5833 |  | 0.5833 |  | 0.8241 |  | 1.1808 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val17_test13 | 1 | 0.5833 |  | 0.5833 |  | 0.5000 |  | 0.8981 |  | 1.1550 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val13_test16 | 1 | 0.2500 |  | 0.2500 |  | 0.2625 |  | 0.5741 |  | 1.5731 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val16_test13 | 1 | 0.5833 |  | 0.5833 |  | 0.4792 |  | 0.8796 |  | 1.2180 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val13_test15 | 1 | 0.5000 |  | 0.5000 |  | 0.3750 |  | 0.8241 |  | 1.2825 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val15_test13 | 1 | 0.2500 |  | 0.2500 |  | 0.2250 |  | 0.7130 |  | 1.3848 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val13_test14 | 1 | 0.7500 |  | 0.7500 |  | 0.6667 |  | 0.9630 |  | 0.9382 |  |
| cp3_s23 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val14_test13 | 1 | 0.6667 |  | 0.6667 |  | 0.6667 |  | 0.8796 |  | 1.0308 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s23 | resnet1D | resnet1D-843fbf2 | 42 | 30 | 0.5222 | 0.1434 | 0.5222 | 0.1434 | 0.4713 | 0.1492 | 0.7914 | 0.1268 | 1.2737 | 0.2218 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s23 | resnet1D | resnet1D-843fbf2 | 30 | 0.5222 | 0.1434 | 0.5222 | 0.1434 | 0.4713 | 0.1492 | 0.7914 | 0.1268 | 1.2737 | 0.2218 |

### Pooled confusion matrix: cp3_s23 / resnet1D / resnet1D-843fbf2

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 35 | 10 | 36 | 9 |
| B1 | 16 | 27 | 43 | 4 |
| B2 | 10 | 23 | 52 | 5 |
| B3 | 1 | 4 | 11 | 74 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 38.89 | 11.11 | 40.00 | 10.00 |
| B1 | 17.78 | 30.00 | 47.78 | 4.44 |
| B2 | 11.11 | 25.56 | 57.78 | 5.56 |
| B3 | 1.11 | 4.44 | 12.22 | 82.22 |
