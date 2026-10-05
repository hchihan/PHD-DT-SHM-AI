# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-10-11-12_val8_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2062 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-10-11-12_val9_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2628 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-10-11_val12_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2534 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-10-11_val9_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3212 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-10-12_val11_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2887 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-10-12_val9_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.1631 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-11-12_val10_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2748 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-11-12_val9_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2009 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-9-10_val11_test12 | 42 | 0.8333 | 0.8333 | 0.8310 | 0.9907 | 0.3650 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-9-10_val12_test11 | 42 | 0.8333 | 0.8333 | 0.8286 | 1.0000 | 0.4227 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-9-11_val10_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3348 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-9-11_val12_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1571 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-9-12_val10_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.1890 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-9-12_val11_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1462 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-9-10-11_val12_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1614 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-9-10-11_val8_test12 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2574 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-9-10-12_val11_test8 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3008 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-9-10-12_val8_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.1689 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-9-11-12_val10_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2061 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-9-11-12_val8_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1976 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train8-10-11-12_val7_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1905 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train8-10-11-12_val9_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1450 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train8-9-10-11_val12_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2333 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train8-9-10-11_val7_test12 | 42 | 0.8333 | 0.8333 | 0.8375 | 1.0000 | 0.4148 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train8-9-10-12_val11_test7 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3075 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train8-9-10-12_val7_test11 | 42 | 0.8333 | 0.8333 | 0.8286 | 1.0000 | 0.5023 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train8-9-11-12_val10_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2532 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train8-9-11-12_val7_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1161 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train9-10-11-12_val7_test8 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2509 |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train9-10-11-12_val8_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2468 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-10-11-12_val8_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2062 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-10-11-12_val9_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2628 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-10-11_val12_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2534 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-10-11_val9_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3212 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-10-12_val11_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2887 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-10-12_val9_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.1631 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-11-12_val10_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2748 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-11-12_val9_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2009 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-9-10_val11_test12 | 1 | 0.8333 |  | 0.8333 |  | 0.8310 |  | 0.9907 |  | 0.3650 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-9-10_val12_test11 | 1 | 0.8333 |  | 0.8333 |  | 0.8286 |  | 1.0000 |  | 0.4227 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-9-11_val10_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3348 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-9-11_val12_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1571 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-9-12_val10_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.1890 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-8-9-12_val11_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1462 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-9-10-11_val12_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1614 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-9-10-11_val8_test12 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2574 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-9-10-12_val11_test8 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3008 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-9-10-12_val8_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.1689 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-9-11-12_val10_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2061 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train7-9-11-12_val8_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1976 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train8-10-11-12_val7_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1905 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train8-10-11-12_val9_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1450 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train8-9-10-11_val12_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2333 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train8-9-10-11_val7_test12 | 1 | 0.8333 |  | 0.8333 |  | 0.8375 |  | 1.0000 |  | 0.4148 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train8-9-10-12_val11_test7 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3075 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train8-9-10-12_val7_test11 | 1 | 0.8333 |  | 0.8333 |  | 0.8286 |  | 1.0000 |  | 0.5023 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train8-9-11-12_val10_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2532 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train8-9-11-12_val7_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1161 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train9-10-11-12_val7_test8 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2509 |  |
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | train9-10-11-12_val8_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2468 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | 42 | 30 | 0.9556 | 0.0609 | 0.9556 | 0.0609 | 0.9547 | 0.0618 | 0.9997 | 0.0017 | 0.2513 | 0.0912 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s123_resnet1d | resnet1D | resnet1D-75d5c1e | 30 | 0.9556 | 0.0609 | 0.9556 | 0.0609 | 0.9547 | 0.0618 | 0.9997 | 0.0017 | 0.2513 | 0.0912 |

### Pooled confusion matrix: cp2_s123_resnet1d / resnet1D / resnet1D-75d5c1e

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 85 | 5 | 0 | 0 |
| B1 | 1 | 85 | 4 | 0 |
| B2 | 0 | 0 | 89 | 1 |
| B3 | 0 | 0 | 5 | 85 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 94.44 | 5.56 | 0.00 | 0.00 |
| B1 | 1.11 | 94.44 | 4.44 | 0.00 |
| B2 | 0.00 | 0.00 | 98.89 | 1.11 |
| B3 | 0.00 | 0.00 | 5.56 | 94.44 |
