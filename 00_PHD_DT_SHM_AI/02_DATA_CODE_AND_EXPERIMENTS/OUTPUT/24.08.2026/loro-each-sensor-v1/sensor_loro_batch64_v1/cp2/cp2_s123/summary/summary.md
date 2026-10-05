# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val8_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2098 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val9_test8 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2880 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val12_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2582 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val9_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3342 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val11_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1621 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val9_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.1890 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val10_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2239 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val9_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1256 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val11_test12 | 42 | 0.8333 | 0.8333 | 0.8310 | 0.9907 | 0.3557 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val12_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2510 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val10_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4242 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val12_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1271 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val10_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.1477 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val11_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1327 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val12_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1587 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val8_test12 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2771 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val11_test8 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3455 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val8_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.1668 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val10_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2308 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val8_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1370 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val7_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1600 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val9_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1642 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val12_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2361 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val7_test12 | 42 | 0.8333 | 0.8333 | 0.8375 | 0.9907 | 0.4980 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val11_test7 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3113 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val7_test11 | 42 | 0.8333 | 0.8333 | 0.8286 | 1.0000 | 0.4620 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val10_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1578 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val7_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1008 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val7_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2028 |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val8_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2423 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val8_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2098 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val9_test8 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2880 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val12_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2582 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val9_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3342 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val11_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1621 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val9_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.1890 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val10_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2239 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val9_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1256 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val11_test12 | 1 | 0.8333 |  | 0.8333 |  | 0.8310 |  | 0.9907 |  | 0.3557 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val12_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2510 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val10_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4242 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val12_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1271 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val10_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.1477 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val11_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1327 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val12_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1587 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val8_test12 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2771 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val11_test8 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3455 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val8_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.1668 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val10_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2308 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val8_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1370 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val7_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1600 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val9_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1642 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val12_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2361 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val7_test12 | 1 | 0.8333 |  | 0.8333 |  | 0.8375 |  | 0.9907 |  | 0.4980 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val11_test7 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3113 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val7_test11 | 1 | 0.8333 |  | 0.8333 |  | 0.8286 |  | 1.0000 |  | 0.4620 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val10_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1578 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val7_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1008 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val7_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2028 |  |
| cp2_s123 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val8_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2423 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s123 | resnet1D | resnet1D-843fbf2 | 42 | 30 | 0.9583 | 0.0569 | 0.9583 | 0.0569 | 0.9575 | 0.0576 | 0.9994 | 0.0023 | 0.2360 | 0.1034 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s123 | resnet1D | resnet1D-843fbf2 | 30 | 0.9583 | 0.0569 | 0.9583 | 0.0569 | 0.9575 | 0.0576 | 0.9994 | 0.0023 | 0.2360 | 0.1034 |

### Pooled confusion matrix: cp2_s123 / resnet1D / resnet1D-843fbf2

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 85 | 5 | 0 | 0 |
| B1 | 1 | 85 | 4 | 0 |
| B2 | 0 | 0 | 89 | 1 |
| B3 | 0 | 0 | 4 | 86 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 94.44 | 5.56 | 0.00 | 0.00 |
| B1 | 1.11 | 94.44 | 4.44 | 0.00 |
| B2 | 0.00 | 0.00 | 98.89 | 1.11 |
| B3 | 0.00 | 0.00 | 4.44 | 95.56 |
