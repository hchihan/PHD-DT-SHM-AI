# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val8_test9 | 42 | 0.8333 | 0.8333 | 0.8125 | 1.0000 | 0.4279 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val9_test8 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3766 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val12_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3913 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val9_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9907 | 0.3753 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val11_test9 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9907 | 0.4164 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val9_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.3312 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val10_test9 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3818 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val9_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2660 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val11_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9722 | 0.4531 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val12_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3190 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val10_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9907 | 0.3654 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val12_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2352 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val10_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.4124 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val11_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3040 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val12_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3598 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val8_test12 | 42 | 0.8333 | 0.8333 | 0.8310 | 0.9907 | 0.4427 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val11_test8 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3566 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val8_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2927 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val10_test8 | 42 | 0.8333 | 0.8333 | 0.8125 | 1.0000 | 0.4267 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val8_test10 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3015 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val7_test9 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3627 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val9_test7 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2849 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val12_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3183 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val7_test12 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4077 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val11_test7 | 42 | 0.8333 | 0.8333 | 0.8125 | 1.0000 | 0.4900 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val7_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.6409 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val10_test7 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4401 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val7_test10 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3502 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val7_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3230 |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val8_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3131 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val8_test9 | 1 | 0.8333 |  | 0.8333 |  | 0.8125 |  | 1.0000 |  | 0.4279 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val9_test8 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3766 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val12_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3913 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val9_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9907 |  | 0.3753 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val11_test9 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9907 |  | 0.4164 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val9_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.3312 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val10_test9 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3818 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val9_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2660 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val11_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9722 |  | 0.4531 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val12_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3190 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val10_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9907 |  | 0.3654 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val12_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2352 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val10_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.4124 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val11_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3040 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val12_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3598 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val8_test12 | 1 | 0.8333 |  | 0.8333 |  | 0.8310 |  | 0.9907 |  | 0.4427 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val11_test8 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3566 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val8_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2927 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val10_test8 | 1 | 0.8333 |  | 0.8333 |  | 0.8125 |  | 1.0000 |  | 0.4267 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val8_test10 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3015 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val7_test9 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3627 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val9_test7 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2849 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val12_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3183 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val7_test12 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.4077 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val11_test7 | 1 | 0.8333 |  | 0.8333 |  | 0.8125 |  | 1.0000 |  | 0.4900 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val7_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.6409 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val10_test7 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4401 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val7_test10 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3502 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val7_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3230 |  |
| cp2_s23 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val8_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3131 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s23 | resnet1D | resnet1D-843fbf2 | 42 | 30 | 0.9306 | 0.0540 | 0.9306 | 0.0540 | 0.9270 | 0.0585 | 0.9960 | 0.0076 | 0.3722 | 0.0791 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s23 | resnet1D | resnet1D-843fbf2 | 30 | 0.9306 | 0.0540 | 0.9306 | 0.0540 | 0.9270 | 0.0585 | 0.9960 | 0.0076 | 0.3722 | 0.0791 |

### Pooled confusion matrix: cp2_s23 / resnet1D / resnet1D-843fbf2

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 78 | 12 | 0 | 0 |
| B1 | 9 | 77 | 4 | 0 |
| B2 | 0 | 0 | 90 | 0 |
| B3 | 0 | 0 | 0 | 90 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 86.67 | 13.33 | 0.00 | 0.00 |
| B1 | 10.00 | 85.56 | 4.44 | 0.00 |
| B2 | 0.00 | 0.00 | 100.00 | 0.00 |
| B3 | 0.00 | 0.00 | 0.00 | 100.00 |
