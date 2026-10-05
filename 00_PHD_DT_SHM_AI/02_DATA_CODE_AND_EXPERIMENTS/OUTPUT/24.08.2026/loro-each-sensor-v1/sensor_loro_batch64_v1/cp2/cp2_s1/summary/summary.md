# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val8_test9 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3448 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val9_test8 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9907 | 0.4186 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val12_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3168 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val9_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.4627 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val11_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3198 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val9_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.5499 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val10_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3650 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val9_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3066 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val11_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9907 | 0.3867 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val12_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4206 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val10_test12 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3223 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val12_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2933 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val10_test11 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3646 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val11_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2705 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val12_test8 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.5024 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val8_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3611 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val11_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3994 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val8_test11 | 42 | 0.8333 | 0.8333 | 0.8286 | 1.0000 | 0.5337 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val10_test8 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4850 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val8_test10 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3399 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val7_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2844 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val9_test7 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4464 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val12_test7 | 42 | 0.8333 | 0.8333 | 0.8310 | 0.9815 | 0.4724 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val7_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3447 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val11_test7 | 42 | 0.8333 | 0.8333 | 0.8375 | 0.9815 | 0.7884 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val7_test11 | 42 | 0.7500 | 0.7500 | 0.7202 | 0.9815 | 0.5842 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val10_test7 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.5506 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val7_test10 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3699 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val7_test8 | 42 | 0.8333 | 0.8333 | 0.8310 | 0.9907 | 0.4182 |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val8_test7 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9907 | 0.4568 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val8_test9 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3448 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val9_test8 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9907 |  | 0.4186 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val12_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3168 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val9_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.4627 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val11_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3198 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val9_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.5499 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val10_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3650 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val9_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3066 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val11_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9907 |  | 0.3867 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val12_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4206 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val10_test12 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3223 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val12_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2933 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val10_test11 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3646 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val11_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2705 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val12_test8 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.5024 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val8_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3611 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val11_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3994 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val8_test11 | 1 | 0.8333 |  | 0.8333 |  | 0.8286 |  | 1.0000 |  | 0.5337 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val10_test8 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4850 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val8_test10 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3399 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val7_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2844 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val9_test7 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4464 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val12_test7 | 1 | 0.8333 |  | 0.8333 |  | 0.8310 |  | 0.9815 |  | 0.4724 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val7_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3447 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val11_test7 | 1 | 0.8333 |  | 0.8333 |  | 0.8375 |  | 0.9815 |  | 0.7884 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val7_test11 | 1 | 0.7500 |  | 0.7500 |  | 0.7202 |  | 0.9815 |  | 0.5842 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val10_test7 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.5506 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val7_test10 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3699 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val7_test8 | 1 | 0.8333 |  | 0.8333 |  | 0.8310 |  | 0.9907 |  | 0.4182 |  |
| cp2_s1 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val8_test7 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9907 |  | 0.4568 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s1 | resnet1D | resnet1D-843fbf2 | 42 | 30 | 0.9278 | 0.0647 | 0.9278 | 0.0647 | 0.9254 | 0.0681 | 0.9957 | 0.0072 | 0.4160 | 0.1111 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s1 | resnet1D | resnet1D-843fbf2 | 30 | 0.9278 | 0.0647 | 0.9278 | 0.0647 | 0.9254 | 0.0681 | 0.9957 | 0.0072 | 0.4160 | 0.1111 |

### Pooled confusion matrix: cp2_s1 / resnet1D / resnet1D-843fbf2

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 87 | 3 | 0 | 0 |
| B1 | 0 | 86 | 4 | 0 |
| B2 | 0 | 3 | 82 | 5 |
| B3 | 2 | 0 | 9 | 79 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 96.67 | 3.33 | 0.00 | 0.00 |
| B1 | 0.00 | 95.56 | 4.44 | 0.00 |
| B2 | 0.00 | 3.33 | 91.11 | 5.56 |
| B3 | 2.22 | 0.00 | 10.00 | 87.78 |
