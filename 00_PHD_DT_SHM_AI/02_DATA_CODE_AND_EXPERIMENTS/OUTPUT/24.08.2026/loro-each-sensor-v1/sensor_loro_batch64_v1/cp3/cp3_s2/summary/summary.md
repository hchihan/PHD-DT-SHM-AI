# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val17_test18 | 42 | 0.4167 | 0.4167 | 0.2986 | 0.5741 | 1.3861 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val18_test17 | 42 | 0.3333 | 0.3333 | 0.2078 | 0.5463 | 1.3871 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val16_test18 | 42 | 0.3333 | 0.3333 | 0.2083 | 0.5833 | 1.3869 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val18_test16 | 42 | 0.3333 | 0.3333 | 0.2078 | 0.5741 | 1.3927 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val16_test17 | 42 | 0.3333 | 0.3333 | 0.2222 | 0.5000 | 1.3878 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val17_test16 | 42 | 0.4167 | 0.4167 | 0.3679 | 0.6019 | 1.5501 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val15_test18 | 42 | 0.4167 | 0.4167 | 0.2917 | 0.7870 | 1.4597 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val18_test15 | 42 | 0.5833 | 0.5833 | 0.5167 | 0.8889 | 1.1972 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val15_test17 | 42 | 0.5000 | 0.5000 | 0.5028 | 0.8148 | 1.2937 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val17_test15 | 42 | 0.5000 | 0.5000 | 0.4280 | 0.9074 | 1.1901 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val15_test16 | 42 | 0.5000 | 0.5000 | 0.4611 | 0.6667 | 1.3792 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val16_test15 | 42 | 0.5833 | 0.5833 | 0.5750 | 0.8889 | 1.3653 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val14_test18 | 42 | 0.3333 | 0.3333 | 0.2154 | 0.7500 | 1.4544 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val18_test14 | 42 | 0.4167 | 0.4167 | 0.2917 | 0.8889 | 1.0749 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val14_test17 | 42 | 0.6667 | 0.6667 | 0.6595 | 0.8241 | 1.1863 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val17_test14 | 42 | 0.6667 | 0.6667 | 0.6250 | 0.9444 | 0.9640 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val14_test16 | 42 | 0.2500 | 0.2500 | 0.2167 | 0.6574 | 1.5554 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val16_test14 | 42 | 0.3333 | 0.3333 | 0.2364 | 0.8519 | 1.3446 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val14_test15 | 42 | 0.5833 | 0.5833 | 0.4792 | 0.8333 | 1.3003 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val15_test14 | 42 | 0.5000 | 0.5000 | 0.4417 | 0.8426 | 1.2367 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val13_test18 | 42 | 0.2500 | 0.2500 | 0.1833 | 0.7500 | 1.3500 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val18_test13 | 42 | 0.6667 | 0.6667 | 0.5810 | 0.8611 | 1.2110 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val13_test17 | 42 | 0.3333 | 0.3333 | 0.2078 | 0.7130 | 1.3427 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val17_test13 | 42 | 0.5000 | 0.5000 | 0.4167 | 0.7870 | 1.2766 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val13_test16 | 42 | 0.5833 | 0.5833 | 0.6028 | 0.6481 | 1.4061 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val16_test13 | 42 | 0.3333 | 0.3333 | 0.2798 | 0.7593 | 1.3602 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val13_test15 | 42 | 0.5000 | 0.5000 | 0.3375 | 0.5741 | 1.3984 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val15_test13 | 42 | 0.3333 | 0.3333 | 0.2222 | 0.5185 | 1.3853 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val13_test14 | 42 | 0.5833 | 0.5833 | 0.5333 | 0.9444 | 1.1050 |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val14_test13 | 42 | 0.4167 | 0.4167 | 0.3500 | 0.8148 | 1.2456 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val17_test18 | 1 | 0.4167 |  | 0.4167 |  | 0.2986 |  | 0.5741 |  | 1.3861 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-15-16_val18_test17 | 1 | 0.3333 |  | 0.3333 |  | 0.2078 |  | 0.5463 |  | 1.3871 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val16_test18 | 1 | 0.3333 |  | 0.3333 |  | 0.2083 |  | 0.5833 |  | 1.3869 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-15-17_val18_test16 | 1 | 0.3333 |  | 0.3333 |  | 0.2078 |  | 0.5741 |  | 1.3927 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val16_test17 | 1 | 0.3333 |  | 0.3333 |  | 0.2222 |  | 0.5000 |  | 1.3878 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-15-18_val17_test16 | 1 | 0.4167 |  | 0.4167 |  | 0.3679 |  | 0.6019 |  | 1.5501 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val15_test18 | 1 | 0.4167 |  | 0.4167 |  | 0.2917 |  | 0.7870 |  | 1.4597 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-16-17_val18_test15 | 1 | 0.5833 |  | 0.5833 |  | 0.5167 |  | 0.8889 |  | 1.1972 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val15_test17 | 1 | 0.5000 |  | 0.5000 |  | 0.5028 |  | 0.8148 |  | 1.2937 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-16-18_val17_test15 | 1 | 0.5000 |  | 0.5000 |  | 0.4280 |  | 0.9074 |  | 1.1901 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val15_test16 | 1 | 0.5000 |  | 0.5000 |  | 0.4611 |  | 0.6667 |  | 1.3792 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-14-17-18_val16_test15 | 1 | 0.5833 |  | 0.5833 |  | 0.5750 |  | 0.8889 |  | 1.3653 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val14_test18 | 1 | 0.3333 |  | 0.3333 |  | 0.2154 |  | 0.7500 |  | 1.4544 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-15-16-17_val18_test14 | 1 | 0.4167 |  | 0.4167 |  | 0.2917 |  | 0.8889 |  | 1.0749 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val14_test17 | 1 | 0.6667 |  | 0.6667 |  | 0.6595 |  | 0.8241 |  | 1.1863 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-15-16-18_val17_test14 | 1 | 0.6667 |  | 0.6667 |  | 0.6250 |  | 0.9444 |  | 0.9640 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val14_test16 | 1 | 0.2500 |  | 0.2500 |  | 0.2167 |  | 0.6574 |  | 1.5554 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-15-17-18_val16_test14 | 1 | 0.3333 |  | 0.3333 |  | 0.2364 |  | 0.8519 |  | 1.3446 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val14_test15 | 1 | 0.5833 |  | 0.5833 |  | 0.4792 |  | 0.8333 |  | 1.3003 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train13-16-17-18_val15_test14 | 1 | 0.5000 |  | 0.5000 |  | 0.4417 |  | 0.8426 |  | 1.2367 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val13_test18 | 1 | 0.2500 |  | 0.2500 |  | 0.1833 |  | 0.7500 |  | 1.3500 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train14-15-16-17_val18_test13 | 1 | 0.6667 |  | 0.6667 |  | 0.5810 |  | 0.8611 |  | 1.2110 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val13_test17 | 1 | 0.3333 |  | 0.3333 |  | 0.2078 |  | 0.7130 |  | 1.3427 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train14-15-16-18_val17_test13 | 1 | 0.5000 |  | 0.5000 |  | 0.4167 |  | 0.7870 |  | 1.2766 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val13_test16 | 1 | 0.5833 |  | 0.5833 |  | 0.6028 |  | 0.6481 |  | 1.4061 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train14-15-17-18_val16_test13 | 1 | 0.3333 |  | 0.3333 |  | 0.2798 |  | 0.7593 |  | 1.3602 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val13_test15 | 1 | 0.5000 |  | 0.5000 |  | 0.3375 |  | 0.5741 |  | 1.3984 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train14-16-17-18_val15_test13 | 1 | 0.3333 |  | 0.3333 |  | 0.2222 |  | 0.5185 |  | 1.3853 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val13_test14 | 1 | 0.5833 |  | 0.5833 |  | 0.5333 |  | 0.9444 |  | 1.1050 |  |
| cp3_s2 | resnet1D | resnet1D-843fbf2 | train15-16-17-18_val14_test13 | 1 | 0.4167 |  | 0.4167 |  | 0.3500 |  | 0.8148 |  | 1.2456 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s2 | resnet1D | resnet1D-843fbf2 | 42 | 30 | 0.4500 | 0.1250 | 0.4500 | 0.1250 | 0.3723 | 0.1511 | 0.7432 | 0.1364 | 1.3191 | 0.1321 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp3_s2 | resnet1D | resnet1D-843fbf2 | 30 | 0.4500 | 0.1250 | 0.4500 | 0.1250 | 0.3723 | 0.1511 | 0.7432 | 0.1364 | 1.3191 | 0.1321 |

### Pooled confusion matrix: cp3_s2 / resnet1D / resnet1D-843fbf2

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 24 | 8 | 20 | 38 |
| B1 | 9 | 40 | 25 | 16 |
| B2 | 7 | 31 | 39 | 13 |
| B3 | 15 | 5 | 11 | 59 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 26.67 | 8.89 | 22.22 | 42.22 |
| B1 | 10.00 | 44.44 | 27.78 | 17.78 |
| B2 | 7.78 | 34.44 | 43.33 | 14.44 |
| B3 | 16.67 | 5.56 | 12.22 | 65.56 |
