# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-10-11-12_val8_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2464 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-10-11-12_val9_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2029 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-10-11_val12_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2336 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-10-11_val9_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2913 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-10-12_val11_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2420 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-10-12_val9_test11 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2001 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-11-12_val10_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2575 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-11-12_val9_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1903 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-9-10_val11_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3035 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-9-10_val12_test11 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2010 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-9-11_val10_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3009 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-9-11_val12_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1704 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-9-12_val10_test11 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2075 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-9-12_val11_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1791 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-9-10-11_val12_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1941 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-9-10-11_val8_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2918 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-9-10-12_val11_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1918 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-9-10-12_val8_test11 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1884 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-9-11-12_val10_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2015 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-9-11-12_val8_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1739 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train8-10-11-12_val7_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2215 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train8-10-11-12_val9_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2333 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train8-9-10-11_val12_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2453 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train8-9-10-11_val7_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2962 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train8-9-10-12_val11_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2594 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train8-9-10-12_val7_test11 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1993 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train8-9-11-12_val10_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2531 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train8-9-11-12_val7_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1701 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train9-10-11-12_val7_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2374 |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train9-10-11-12_val8_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2987 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-10-11-12_val8_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2464 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-10-11-12_val9_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2029 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-10-11_val12_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2336 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-10-11_val9_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2913 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-10-12_val11_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2420 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-10-12_val9_test11 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2001 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-11-12_val10_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2575 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-11-12_val9_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1903 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-9-10_val11_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3035 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-9-10_val12_test11 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2010 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-9-11_val10_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3009 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-9-11_val12_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1704 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-9-12_val10_test11 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2075 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-8-9-12_val11_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1791 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-9-10-11_val12_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1941 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-9-10-11_val8_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2918 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-9-10-12_val11_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1918 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-9-10-12_val8_test11 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1884 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-9-11-12_val10_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2015 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train7-9-11-12_val8_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1739 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train8-10-11-12_val7_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2215 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train8-10-11-12_val9_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2333 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train8-9-10-11_val12_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2453 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train8-9-10-11_val7_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2962 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train8-9-10-12_val11_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2594 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train8-9-10-12_val7_test11 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1993 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train8-9-11-12_val10_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2531 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train8-9-11-12_val7_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1701 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train9-10-11-12_val7_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2374 |  |
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | train9-10-11-12_val8_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2987 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | 42 | 30 | 0.9861 | 0.0316 | 0.9861 | 0.0316 | 0.9857 | 0.0325 | 1.0000 | 0.0000 | 0.2294 | 0.0430 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s123_extra_trees | extra_trees | extra_trees-536c3a4 | 30 | 0.9861 | 0.0316 | 0.9861 | 0.0316 | 0.9857 | 0.0325 | 1.0000 | 0.0000 | 0.2294 | 0.0430 |

### Pooled confusion matrix: cp2_s123_extra_trees / extra_trees / extra_trees-536c3a4

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
