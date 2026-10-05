# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-10-11-12_val8_test9 | 42 | 0.5000 | 0.5000 | 0.4917 | 0.8426 | 1.0939 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-10-11-12_val9_test8 | 42 | 0.6667 | 0.6667 | 0.5804 | 0.9074 | 0.9035 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-10-11_val12_test9 | 42 | 0.4167 | 0.4167 | 0.4125 | 0.7870 | 1.2504 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-10-11_val9_test12 | 42 | 0.5000 | 0.5000 | 0.5000 | 0.8333 | 1.0961 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-10-12_val11_test9 | 42 | 0.4167 | 0.4167 | 0.4589 | 0.8056 | 1.2159 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-10-12_val9_test11 | 42 | 0.7500 | 0.7500 | 0.6667 | 0.9537 | 0.7987 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-11-12_val10_test9 | 42 | 0.5833 | 0.5833 | 0.5167 | 0.8056 | 1.0907 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-11-12_val9_test10 | 42 | 0.6667 | 0.6667 | 0.6667 | 0.8056 | 1.0336 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-9-10_val11_test12 | 42 | 0.6667 | 0.6667 | 0.6750 | 0.8241 | 1.4198 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-9-10_val12_test11 | 42 | 0.7500 | 0.7500 | 0.7292 | 0.9630 | 1.0374 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-9-11_val10_test12 | 42 | 0.6667 | 0.6667 | 0.6554 | 0.8704 | 1.2037 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-9-11_val12_test10 | 42 | 0.8333 | 0.8333 | 0.8310 | 0.8611 | 1.0742 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-9-12_val10_test11 | 42 | 0.7500 | 0.7500 | 0.7429 | 0.9259 | 0.8426 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-9-12_val11_test10 | 42 | 0.6667 | 0.6667 | 0.6667 | 0.9074 | 1.0086 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-9-10-11_val12_test8 | 42 | 0.5833 | 0.5833 | 0.5643 | 0.8704 | 1.0433 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-9-10-11_val8_test12 | 42 | 0.5000 | 0.5000 | 0.4708 | 0.8333 | 1.1048 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-9-10-12_val11_test8 | 42 | 0.6667 | 0.6667 | 0.6071 | 0.8981 | 0.8823 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-9-10-12_val8_test11 | 42 | 0.8333 | 0.8333 | 0.8125 | 0.9907 | 0.7238 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-9-11-12_val10_test8 | 42 | 0.7500 | 0.7500 | 0.7375 | 0.8981 | 0.9088 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-9-11-12_val8_test10 | 42 | 0.5833 | 0.5833 | 0.6048 | 0.8611 | 0.9217 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train8-10-11-12_val7_test9 | 42 | 0.4167 | 0.4167 | 0.4111 | 0.7963 | 1.2902 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train8-10-11-12_val9_test7 | 42 | 0.8333 | 0.8333 | 0.8036 | 0.9907 | 0.7333 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train8-9-10-11_val12_test7 | 42 | 0.8333 | 0.8333 | 0.8375 | 0.9630 | 0.7779 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train8-9-10-11_val7_test12 | 42 | 0.6667 | 0.6667 | 0.6542 | 0.8519 | 1.2089 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train8-9-10-12_val11_test7 | 42 | 0.7500 | 0.7500 | 0.7292 | 0.9074 | 0.9162 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train8-9-10-12_val7_test11 | 42 | 0.8333 | 0.8333 | 0.8375 | 0.9907 | 1.0616 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train8-9-11-12_val10_test7 | 42 | 0.7500 | 0.7500 | 0.7286 | 0.9630 | 0.7793 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train8-9-11-12_val7_test10 | 42 | 0.5000 | 0.5000 | 0.5125 | 0.8426 | 0.9992 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train9-10-11-12_val7_test8 | 42 | 0.5833 | 0.5833 | 0.5595 | 0.8333 | 1.0726 |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train9-10-11-12_val8_test7 | 42 | 0.8333 | 0.8333 | 0.8310 | 0.9352 | 0.9635 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-10-11-12_val8_test9 | 1 | 0.5000 |  | 0.5000 |  | 0.4917 |  | 0.8426 |  | 1.0939 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-10-11-12_val9_test8 | 1 | 0.6667 |  | 0.6667 |  | 0.5804 |  | 0.9074 |  | 0.9035 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-10-11_val12_test9 | 1 | 0.4167 |  | 0.4167 |  | 0.4125 |  | 0.7870 |  | 1.2504 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-10-11_val9_test12 | 1 | 0.5000 |  | 0.5000 |  | 0.5000 |  | 0.8333 |  | 1.0961 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-10-12_val11_test9 | 1 | 0.4167 |  | 0.4167 |  | 0.4589 |  | 0.8056 |  | 1.2159 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-10-12_val9_test11 | 1 | 0.7500 |  | 0.7500 |  | 0.6667 |  | 0.9537 |  | 0.7987 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-11-12_val10_test9 | 1 | 0.5833 |  | 0.5833 |  | 0.5167 |  | 0.8056 |  | 1.0907 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-11-12_val9_test10 | 1 | 0.6667 |  | 0.6667 |  | 0.6667 |  | 0.8056 |  | 1.0336 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-9-10_val11_test12 | 1 | 0.6667 |  | 0.6667 |  | 0.6750 |  | 0.8241 |  | 1.4198 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-9-10_val12_test11 | 1 | 0.7500 |  | 0.7500 |  | 0.7292 |  | 0.9630 |  | 1.0374 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-9-11_val10_test12 | 1 | 0.6667 |  | 0.6667 |  | 0.6554 |  | 0.8704 |  | 1.2037 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-9-11_val12_test10 | 1 | 0.8333 |  | 0.8333 |  | 0.8310 |  | 0.8611 |  | 1.0742 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-9-12_val10_test11 | 1 | 0.7500 |  | 0.7500 |  | 0.7429 |  | 0.9259 |  | 0.8426 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-8-9-12_val11_test10 | 1 | 0.6667 |  | 0.6667 |  | 0.6667 |  | 0.9074 |  | 1.0086 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-9-10-11_val12_test8 | 1 | 0.5833 |  | 0.5833 |  | 0.5643 |  | 0.8704 |  | 1.0433 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-9-10-11_val8_test12 | 1 | 0.5000 |  | 0.5000 |  | 0.4708 |  | 0.8333 |  | 1.1048 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-9-10-12_val11_test8 | 1 | 0.6667 |  | 0.6667 |  | 0.6071 |  | 0.8981 |  | 0.8823 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-9-10-12_val8_test11 | 1 | 0.8333 |  | 0.8333 |  | 0.8125 |  | 0.9907 |  | 0.7238 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-9-11-12_val10_test8 | 1 | 0.7500 |  | 0.7500 |  | 0.7375 |  | 0.8981 |  | 0.9088 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train7-9-11-12_val8_test10 | 1 | 0.5833 |  | 0.5833 |  | 0.6048 |  | 0.8611 |  | 0.9217 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train8-10-11-12_val7_test9 | 1 | 0.4167 |  | 0.4167 |  | 0.4111 |  | 0.7963 |  | 1.2902 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train8-10-11-12_val9_test7 | 1 | 0.8333 |  | 0.8333 |  | 0.8036 |  | 0.9907 |  | 0.7333 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train8-9-10-11_val12_test7 | 1 | 0.8333 |  | 0.8333 |  | 0.8375 |  | 0.9630 |  | 0.7779 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train8-9-10-11_val7_test12 | 1 | 0.6667 |  | 0.6667 |  | 0.6542 |  | 0.8519 |  | 1.2089 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train8-9-10-12_val11_test7 | 1 | 0.7500 |  | 0.7500 |  | 0.7292 |  | 0.9074 |  | 0.9162 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train8-9-10-12_val7_test11 | 1 | 0.8333 |  | 0.8333 |  | 0.8375 |  | 0.9907 |  | 1.0616 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train8-9-11-12_val10_test7 | 1 | 0.7500 |  | 0.7500 |  | 0.7286 |  | 0.9630 |  | 0.7793 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train8-9-11-12_val7_test10 | 1 | 0.5000 |  | 0.5000 |  | 0.5125 |  | 0.8426 |  | 0.9992 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train9-10-11-12_val7_test8 | 1 | 0.5833 |  | 0.5833 |  | 0.5595 |  | 0.8333 |  | 1.0726 |  |
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | train9-10-11-12_val8_test7 | 1 | 0.8333 |  | 0.8333 |  | 0.8310 |  | 0.9352 |  | 0.9635 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | 42 | 30 | 0.6583 | 0.1355 | 0.6583 | 0.1355 | 0.6432 | 0.1328 | 0.8840 | 0.0635 | 1.0152 | 0.1723 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s123_1dcnn | 1dcnn | 1dcnn-75d5c1e | 30 | 0.6583 | 0.1355 | 0.6583 | 0.1355 | 0.6432 | 0.1328 | 0.8840 | 0.0635 | 1.0152 | 0.1723 |

### Pooled confusion matrix: cp2_s123_1dcnn / 1dcnn / 1dcnn-75d5c1e

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 57 | 24 | 8 | 1 |
| B1 | 44 | 28 | 17 | 1 |
| B2 | 9 | 10 | 71 | 0 |
| B3 | 6 | 0 | 3 | 81 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 63.33 | 26.67 | 8.89 | 1.11 |
| B1 | 48.89 | 31.11 | 18.89 | 1.11 |
| B2 | 10.00 | 11.11 | 78.89 | 0.00 |
| B3 | 6.67 | 0.00 | 3.33 | 90.00 |
