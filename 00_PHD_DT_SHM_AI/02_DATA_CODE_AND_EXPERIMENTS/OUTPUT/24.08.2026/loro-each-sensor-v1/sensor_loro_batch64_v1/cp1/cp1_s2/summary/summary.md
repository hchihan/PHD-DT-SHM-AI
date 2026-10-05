# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-3-4_val5_test6 | 42 | 0.8333 | 0.8333 | 0.8310 | 0.9815 | 0.7621 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-3-4_val6_test5 | 42 | 0.7500 | 0.7500 | 0.7476 | 0.9630 | 0.7812 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-3-5_val4_test6 | 42 | 0.8333 | 0.8333 | 0.8286 | 0.9815 | 0.7846 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-3-5_val6_test4 | 42 | 0.7500 | 0.7500 | 0.7667 | 0.9444 | 0.7567 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-3-6_val4_test5 | 42 | 0.8333 | 0.8333 | 0.8286 | 0.9815 | 0.7734 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-3-6_val5_test4 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.6873 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-4-5_val3_test6 | 42 | 0.8333 | 0.8333 | 0.8036 | 0.9630 | 0.8180 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-4-5_val6_test3 | 42 | 0.8333 | 0.8333 | 0.8375 | 1.0000 | 0.7498 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-4-6_val3_test5 | 42 | 0.7500 | 0.7500 | 0.7542 | 0.9907 | 0.7608 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-4-6_val5_test3 | 42 | 0.7500 | 0.7500 | 0.7667 | 0.9907 | 0.7580 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-5-6_val3_test4 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9907 | 0.7056 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-5-6_val4_test3 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.7625 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-3-4-5_val2_test6 | 42 | 0.8333 | 0.8333 | 0.8286 | 1.0000 | 0.7431 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-3-4-5_val6_test2 | 42 | 0.8333 | 0.8333 | 0.8310 | 0.9815 | 0.8021 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-3-4-6_val2_test5 | 42 | 0.7500 | 0.7500 | 0.7476 | 0.9630 | 0.7840 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-3-4-6_val5_test2 | 42 | 0.7500 | 0.7500 | 0.7667 | 0.9537 | 0.8222 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-3-5-6_val2_test4 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.6881 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-3-5-6_val4_test2 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9907 | 0.7657 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-4-5-6_val2_test3 | 42 | 0.8333 | 0.8333 | 0.8375 | 0.9907 | 0.8191 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-4-5-6_val3_test2 | 42 | 0.8333 | 0.8333 | 0.8375 | 0.9815 | 0.8297 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train2-3-4-5_val1_test6 | 42 | 0.7500 | 0.7500 | 0.7667 | 1.0000 | 0.7594 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train2-3-4-5_val6_test1 | 42 | 0.7500 | 0.7500 | 0.7667 | 1.0000 | 0.8222 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train2-3-4-6_val1_test5 | 42 | 0.7500 | 0.7500 | 0.7667 | 0.9722 | 0.7968 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train2-3-4-6_val5_test1 | 42 | 0.7500 | 0.7500 | 0.7667 | 0.9722 | 0.8462 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train2-3-5-6_val1_test4 | 42 | 0.7500 | 0.7500 | 0.7667 | 0.9630 | 0.7710 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train2-3-5-6_val4_test1 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9907 | 0.8364 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train2-4-5-6_val1_test3 | 42 | 0.7500 | 0.7500 | 0.7595 | 0.9722 | 0.7686 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train2-4-5-6_val3_test1 | 42 | 0.8333 | 0.8333 | 0.8375 | 1.0000 | 0.8001 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train3-4-5-6_val1_test2 | 42 | 0.7500 | 0.7500 | 0.7667 | 0.9537 | 0.8079 |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train3-4-5-6_val2_test1 | 42 | 0.7500 | 0.7500 | 0.7542 | 0.9815 | 0.8398 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-3-4_val5_test6 | 1 | 0.8333 |  | 0.8333 |  | 0.8310 |  | 0.9815 |  | 0.7621 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-3-4_val6_test5 | 1 | 0.7500 |  | 0.7500 |  | 0.7476 |  | 0.9630 |  | 0.7812 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-3-5_val4_test6 | 1 | 0.8333 |  | 0.8333 |  | 0.8286 |  | 0.9815 |  | 0.7846 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-3-5_val6_test4 | 1 | 0.7500 |  | 0.7500 |  | 0.7667 |  | 0.9444 |  | 0.7567 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-3-6_val4_test5 | 1 | 0.8333 |  | 0.8333 |  | 0.8286 |  | 0.9815 |  | 0.7734 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-3-6_val5_test4 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.6873 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-4-5_val3_test6 | 1 | 0.8333 |  | 0.8333 |  | 0.8036 |  | 0.9630 |  | 0.8180 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-4-5_val6_test3 | 1 | 0.8333 |  | 0.8333 |  | 0.8375 |  | 1.0000 |  | 0.7498 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-4-6_val3_test5 | 1 | 0.7500 |  | 0.7500 |  | 0.7542 |  | 0.9907 |  | 0.7608 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-4-6_val5_test3 | 1 | 0.7500 |  | 0.7500 |  | 0.7667 |  | 0.9907 |  | 0.7580 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-5-6_val3_test4 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9907 |  | 0.7056 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-2-5-6_val4_test3 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.7625 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-3-4-5_val2_test6 | 1 | 0.8333 |  | 0.8333 |  | 0.8286 |  | 1.0000 |  | 0.7431 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-3-4-5_val6_test2 | 1 | 0.8333 |  | 0.8333 |  | 0.8310 |  | 0.9815 |  | 0.8021 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-3-4-6_val2_test5 | 1 | 0.7500 |  | 0.7500 |  | 0.7476 |  | 0.9630 |  | 0.7840 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-3-4-6_val5_test2 | 1 | 0.7500 |  | 0.7500 |  | 0.7667 |  | 0.9537 |  | 0.8222 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-3-5-6_val2_test4 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.6881 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-3-5-6_val4_test2 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9907 |  | 0.7657 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-4-5-6_val2_test3 | 1 | 0.8333 |  | 0.8333 |  | 0.8375 |  | 0.9907 |  | 0.8191 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train1-4-5-6_val3_test2 | 1 | 0.8333 |  | 0.8333 |  | 0.8375 |  | 0.9815 |  | 0.8297 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train2-3-4-5_val1_test6 | 1 | 0.7500 |  | 0.7500 |  | 0.7667 |  | 1.0000 |  | 0.7594 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train2-3-4-5_val6_test1 | 1 | 0.7500 |  | 0.7500 |  | 0.7667 |  | 1.0000 |  | 0.8222 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train2-3-4-6_val1_test5 | 1 | 0.7500 |  | 0.7500 |  | 0.7667 |  | 0.9722 |  | 0.7968 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train2-3-4-6_val5_test1 | 1 | 0.7500 |  | 0.7500 |  | 0.7667 |  | 0.9722 |  | 0.8462 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train2-3-5-6_val1_test4 | 1 | 0.7500 |  | 0.7500 |  | 0.7667 |  | 0.9630 |  | 0.7710 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train2-3-5-6_val4_test1 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9907 |  | 0.8364 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train2-4-5-6_val1_test3 | 1 | 0.7500 |  | 0.7500 |  | 0.7595 |  | 0.9722 |  | 0.7686 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train2-4-5-6_val3_test1 | 1 | 0.8333 |  | 0.8333 |  | 0.8375 |  | 1.0000 |  | 0.8001 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train3-4-5-6_val1_test2 | 1 | 0.7500 |  | 0.7500 |  | 0.7667 |  | 0.9537 |  | 0.8079 |  |
| cp1_s2 | resnet1D | resnet1D-843fbf2 | train3-4-5-6_val2_test1 | 1 | 0.7500 |  | 0.7500 |  | 0.7542 |  | 0.9815 |  | 0.8398 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp1_s2 | resnet1D | resnet1D-843fbf2 | 42 | 30 | 0.8111 | 0.0654 | 0.8111 | 0.0654 | 0.8150 | 0.0596 | 0.9818 | 0.0164 | 0.7801 | 0.0415 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp1_s2 | resnet1D | resnet1D-843fbf2 | 30 | 0.8111 | 0.0654 | 0.8111 | 0.0654 | 0.8150 | 0.0596 | 0.9818 | 0.0164 | 0.7801 | 0.0415 |

### Pooled confusion matrix: cp1_s2 / resnet1D / resnet1D-843fbf2

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 70 | 3 | 3 | 14 |
| B1 | 3 | 70 | 4 | 13 |
| B2 | 7 | 8 | 67 | 8 |
| B3 | 1 | 0 | 4 | 85 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 77.78 | 3.33 | 3.33 | 15.56 |
| B1 | 3.33 | 77.78 | 4.44 | 14.44 |
| B2 | 7.78 | 8.89 | 74.44 | 8.89 |
| B3 | 1.11 | 0.00 | 4.44 | 94.44 |
