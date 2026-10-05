# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-10-11-12_val8_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1964 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-10-11-12_val9_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1737 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-10-11_val12_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1916 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-10-11_val9_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2679 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-10-12_val11_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1936 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-10-12_val9_test11 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1741 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-11-12_val10_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2043 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-11-12_val9_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1537 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-9-10_val11_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2843 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-9-10_val12_test11 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1774 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-9-11_val10_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2738 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-9-11_val12_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1463 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-9-12_val10_test11 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1752 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-9-12_val11_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1550 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-9-10-11_val12_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1673 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-9-10-11_val8_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2799 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-9-10-12_val11_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1636 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-9-10-12_val8_test11 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1620 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-9-11-12_val10_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1704 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-9-11-12_val8_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1441 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train8-10-11-12_val7_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1869 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train8-10-11-12_val9_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2086 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train8-9-10-11_val12_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2121 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train8-9-10-11_val7_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2774 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train8-9-10-12_val11_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2203 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train8-9-10-12_val7_test11 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1721 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train8-9-11-12_val10_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2199 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train8-9-11-12_val7_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1459 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train9-10-11-12_val7_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2137 |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train9-10-11-12_val8_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2674 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-10-11-12_val8_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1964 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-10-11-12_val9_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1737 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-10-11_val12_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1916 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-10-11_val9_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2679 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-10-12_val11_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1936 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-10-12_val9_test11 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1741 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-11-12_val10_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2043 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-11-12_val9_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1537 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-9-10_val11_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2843 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-9-10_val12_test11 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1774 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-9-11_val10_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2738 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-9-11_val12_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1463 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-9-12_val10_test11 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1752 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-8-9-12_val11_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1550 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-9-10-11_val12_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1673 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-9-10-11_val8_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2799 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-9-10-12_val11_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1636 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-9-10-12_val8_test11 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1620 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-9-11-12_val10_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1704 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train7-9-11-12_val8_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1441 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train8-10-11-12_val7_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1869 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train8-10-11-12_val9_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2086 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train8-9-10-11_val12_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2121 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train8-9-10-11_val7_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2774 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train8-9-10-12_val11_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2203 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train8-9-10-12_val7_test11 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1721 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train8-9-11-12_val10_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2199 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train8-9-11-12_val7_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1459 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train9-10-11-12_val7_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2137 |  |
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | train9-10-11-12_val8_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2674 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | 42 | 30 | 0.9861 | 0.0316 | 0.9861 | 0.0316 | 0.9857 | 0.0325 | 1.0000 | 0.0000 | 0.1993 | 0.0442 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s123_random_forest | random_forest | random_forest-536c3a4 | 30 | 0.9861 | 0.0316 | 0.9861 | 0.0316 | 0.9857 | 0.0325 | 1.0000 | 0.0000 | 0.1993 | 0.0442 |

### Pooled confusion matrix: cp2_s123_random_forest / random_forest / random_forest-536c3a4

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 90 | 0 | 0 | 0 |
| B1 | 0 | 85 | 5 | 0 |
| B2 | 0 | 0 | 90 | 0 |
| B3 | 0 | 0 | 0 | 90 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 100.00 | 0.00 | 0.00 | 0.00 |
| B1 | 0.00 | 94.44 | 5.56 | 0.00 |
| B2 | 0.00 | 0.00 | 100.00 | 0.00 |
| B3 | 0.00 | 0.00 | 0.00 | 100.00 |
