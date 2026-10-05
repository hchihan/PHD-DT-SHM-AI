# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val8_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1946 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val9_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0727 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val12_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1911 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val9_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9907 | 0.4808 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val11_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1969 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val9_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.1842 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val10_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2271 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val9_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0791 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val11_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9722 | 0.4387 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val12_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2938 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val10_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.4422 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val12_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1731 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val10_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3345 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val11_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0873 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val12_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0830 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val8_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9907 | 0.3217 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val11_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0711 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val8_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2470 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val10_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0489 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val8_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0564 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val7_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2462 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val9_test7 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.1838 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val12_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1811 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val7_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9722 | 0.5215 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val11_test7 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2961 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val7_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4287 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val10_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1543 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val7_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0728 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val7_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0819 |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val8_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1735 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val8_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1946 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val9_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.0727 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val12_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1911 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val9_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9907 |  | 0.4808 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val11_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1969 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val9_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.1842 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val10_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2271 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val9_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.0791 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val11_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9722 |  | 0.4387 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val12_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2938 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val10_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.4422 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val12_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1731 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val10_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3345 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val11_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.0873 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val12_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.0830 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val8_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9907 |  | 0.3217 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val11_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.0711 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val8_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2470 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val10_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.0489 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val8_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.0564 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val7_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2462 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val9_test7 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.1838 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val12_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1811 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val7_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9722 |  | 0.5215 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val11_test7 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2961 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val7_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4287 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val10_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1543 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val7_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.0728 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val7_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.0819 |  |
| cp2_s13 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val8_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1735 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s13 | resnet1D | resnet1D-843fbf2 | 42 | 30 | 0.9667 | 0.0415 | 0.9667 | 0.0415 | 0.9657 | 0.0427 | 0.9969 | 0.0078 | 0.2188 | 0.1374 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s13 | resnet1D | resnet1D-843fbf2 | 30 | 0.9667 | 0.0415 | 0.9667 | 0.0415 | 0.9657 | 0.0427 | 0.9969 | 0.0078 | 0.2188 | 0.1374 |

### Pooled confusion matrix: cp2_s13 / resnet1D / resnet1D-843fbf2

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 85 | 5 | 0 | 0 |
| B1 | 2 | 83 | 5 | 0 |
| B2 | 0 | 0 | 90 | 0 |
| B3 | 0 | 0 | 0 | 90 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 94.44 | 5.56 | 0.00 | 0.00 |
| B1 | 2.22 | 92.22 | 5.56 | 0.00 |
| B2 | 0.00 | 0.00 | 100.00 | 0.00 |
| B3 | 0.00 | 0.00 | 0.00 | 100.00 |
