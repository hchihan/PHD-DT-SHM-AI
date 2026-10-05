# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-3-4_val5_test6 | 42 | 0.6667 | 0.6667 | 0.6643 | 0.9074 | 0.9578 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-3-4_val6_test5 | 42 | 0.6667 | 0.6667 | 0.6542 | 0.9074 | 0.9196 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-3-5_val4_test6 | 42 | 0.6667 | 0.6667 | 0.6643 | 0.9167 | 0.9757 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-3-5_val6_test4 | 42 | 0.6667 | 0.6667 | 0.6643 | 0.9352 | 0.9614 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-3-6_val4_test5 | 42 | 0.6667 | 0.6667 | 0.6607 | 0.9444 | 1.0327 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-3-6_val5_test4 | 42 | 0.5000 | 0.5000 | 0.4810 | 0.8704 | 0.9758 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-4-5_val3_test6 | 42 | 0.6667 | 0.6667 | 0.6643 | 0.9722 | 0.8925 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-4-5_val6_test3 | 42 | 0.6667 | 0.6667 | 0.6554 | 0.9167 | 0.8882 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-4-6_val3_test5 | 42 | 0.5000 | 0.5000 | 0.4643 | 0.8704 | 1.0390 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-4-6_val5_test3 | 42 | 0.5000 | 0.5000 | 0.4125 | 0.8426 | 1.0234 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-5-6_val3_test4 | 42 | 0.5833 | 0.5833 | 0.5542 | 0.8704 | 0.9711 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-5-6_val4_test3 | 42 | 0.6667 | 0.6667 | 0.6583 | 0.9167 | 1.0343 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-3-4-5_val2_test6 | 42 | 0.6667 | 0.6667 | 0.6542 | 0.9074 | 0.9146 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-3-4-5_val6_test2 | 42 | 0.7500 | 0.7500 | 0.7571 | 0.8981 | 0.9978 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-3-4-6_val2_test5 | 42 | 0.5833 | 0.5833 | 0.5655 | 0.8704 | 1.0230 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-3-4-6_val5_test2 | 42 | 0.5833 | 0.5833 | 0.5554 | 0.8611 | 1.0102 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-3-5-6_val2_test4 | 42 | 0.5833 | 0.5833 | 0.5643 | 0.8611 | 1.0126 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-3-5-6_val4_test2 | 42 | 0.7500 | 0.7500 | 0.7476 | 0.8611 | 1.1583 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-4-5-6_val2_test3 | 42 | 0.5000 | 0.5000 | 0.4226 | 0.8796 | 0.9477 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-4-5-6_val3_test2 | 42 | 0.7500 | 0.7500 | 0.7292 | 0.9352 | 1.0316 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train2-3-4-5_val1_test6 | 42 | 0.5833 | 0.5833 | 0.5000 | 0.8333 | 0.9964 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train2-3-4-5_val6_test1 | 42 | 0.5833 | 0.5833 | 0.5095 | 0.8796 | 1.0460 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train2-3-4-6_val1_test5 | 42 | 0.7500 | 0.7500 | 0.7595 | 0.8704 | 1.0201 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train2-3-4-6_val5_test1 | 42 | 0.5000 | 0.5000 | 0.4375 | 0.8704 | 1.0444 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train2-3-5-6_val1_test4 | 42 | 0.6667 | 0.6667 | 0.5714 | 0.8611 | 1.0009 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train2-3-5-6_val4_test1 | 42 | 0.6667 | 0.6667 | 0.6488 | 0.9167 | 1.1938 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train2-4-5-6_val1_test3 | 42 | 0.5833 | 0.5833 | 0.5167 | 0.8796 | 0.9590 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train2-4-5-6_val3_test1 | 42 | 0.5833 | 0.5833 | 0.5125 | 0.8889 | 1.0088 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train3-4-5-6_val1_test2 | 42 | 0.8333 | 0.8333 | 0.8375 | 0.9167 | 0.9335 |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train3-4-5-6_val2_test1 | 42 | 0.5833 | 0.5833 | 0.5095 | 0.8704 | 0.9698 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-3-4_val5_test6 | 1 | 0.6667 |  | 0.6667 |  | 0.6643 |  | 0.9074 |  | 0.9578 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-3-4_val6_test5 | 1 | 0.6667 |  | 0.6667 |  | 0.6542 |  | 0.9074 |  | 0.9196 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-3-5_val4_test6 | 1 | 0.6667 |  | 0.6667 |  | 0.6643 |  | 0.9167 |  | 0.9757 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-3-5_val6_test4 | 1 | 0.6667 |  | 0.6667 |  | 0.6643 |  | 0.9352 |  | 0.9614 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-3-6_val4_test5 | 1 | 0.6667 |  | 0.6667 |  | 0.6607 |  | 0.9444 |  | 1.0327 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-3-6_val5_test4 | 1 | 0.5000 |  | 0.5000 |  | 0.4810 |  | 0.8704 |  | 0.9758 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-4-5_val3_test6 | 1 | 0.6667 |  | 0.6667 |  | 0.6643 |  | 0.9722 |  | 0.8925 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-4-5_val6_test3 | 1 | 0.6667 |  | 0.6667 |  | 0.6554 |  | 0.9167 |  | 0.8882 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-4-6_val3_test5 | 1 | 0.5000 |  | 0.5000 |  | 0.4643 |  | 0.8704 |  | 1.0390 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-4-6_val5_test3 | 1 | 0.5000 |  | 0.5000 |  | 0.4125 |  | 0.8426 |  | 1.0234 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-5-6_val3_test4 | 1 | 0.5833 |  | 0.5833 |  | 0.5542 |  | 0.8704 |  | 0.9711 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-2-5-6_val4_test3 | 1 | 0.6667 |  | 0.6667 |  | 0.6583 |  | 0.9167 |  | 1.0343 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-3-4-5_val2_test6 | 1 | 0.6667 |  | 0.6667 |  | 0.6542 |  | 0.9074 |  | 0.9146 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-3-4-5_val6_test2 | 1 | 0.7500 |  | 0.7500 |  | 0.7571 |  | 0.8981 |  | 0.9978 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-3-4-6_val2_test5 | 1 | 0.5833 |  | 0.5833 |  | 0.5655 |  | 0.8704 |  | 1.0230 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-3-4-6_val5_test2 | 1 | 0.5833 |  | 0.5833 |  | 0.5554 |  | 0.8611 |  | 1.0102 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-3-5-6_val2_test4 | 1 | 0.5833 |  | 0.5833 |  | 0.5643 |  | 0.8611 |  | 1.0126 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-3-5-6_val4_test2 | 1 | 0.7500 |  | 0.7500 |  | 0.7476 |  | 0.8611 |  | 1.1583 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-4-5-6_val2_test3 | 1 | 0.5000 |  | 0.5000 |  | 0.4226 |  | 0.8796 |  | 0.9477 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train1-4-5-6_val3_test2 | 1 | 0.7500 |  | 0.7500 |  | 0.7292 |  | 0.9352 |  | 1.0316 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train2-3-4-5_val1_test6 | 1 | 0.5833 |  | 0.5833 |  | 0.5000 |  | 0.8333 |  | 0.9964 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train2-3-4-5_val6_test1 | 1 | 0.5833 |  | 0.5833 |  | 0.5095 |  | 0.8796 |  | 1.0460 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train2-3-4-6_val1_test5 | 1 | 0.7500 |  | 0.7500 |  | 0.7595 |  | 0.8704 |  | 1.0201 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train2-3-4-6_val5_test1 | 1 | 0.5000 |  | 0.5000 |  | 0.4375 |  | 0.8704 |  | 1.0444 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train2-3-5-6_val1_test4 | 1 | 0.6667 |  | 0.6667 |  | 0.5714 |  | 0.8611 |  | 1.0009 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train2-3-5-6_val4_test1 | 1 | 0.6667 |  | 0.6667 |  | 0.6488 |  | 0.9167 |  | 1.1938 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train2-4-5-6_val1_test3 | 1 | 0.5833 |  | 0.5833 |  | 0.5167 |  | 0.8796 |  | 0.9590 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train2-4-5-6_val3_test1 | 1 | 0.5833 |  | 0.5833 |  | 0.5125 |  | 0.8889 |  | 1.0088 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train3-4-5-6_val1_test2 | 1 | 0.8333 |  | 0.8333 |  | 0.8375 |  | 0.9167 |  | 0.9335 |  |
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | train3-4-5-6_val2_test1 | 1 | 0.5833 |  | 0.5833 |  | 0.5095 |  | 0.8704 |  | 0.9698 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | 42 | 30 | 0.6306 | 0.0867 | 0.6306 | 0.0867 | 0.5999 | 0.1105 | 0.8910 | 0.0322 | 0.9980 | 0.0659 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp1_s12_1dcnn | 1dcnn | 1dcnn-75d5c1e | 30 | 0.6306 | 0.0867 | 0.6306 | 0.0867 | 0.5999 | 0.1105 | 0.8910 | 0.0322 | 0.9980 | 0.0659 |

### Pooled confusion matrix: cp1_s12_1dcnn / 1dcnn / 1dcnn-75d5c1e

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 54 | 12 | 13 | 11 |
| B1 | 14 | 52 | 17 | 7 |
| B2 | 6 | 26 | 32 | 26 |
| B3 | 0 | 1 | 0 | 89 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 60.00 | 13.33 | 14.44 | 12.22 |
| B1 | 15.56 | 57.78 | 18.89 | 7.78 |
| B2 | 6.67 | 28.89 | 35.56 | 28.89 |
| B3 | 0.00 | 1.11 | 0.00 | 98.89 |
