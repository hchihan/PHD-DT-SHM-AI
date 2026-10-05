# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val8_test9 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.5981 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val9_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2883 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val12_test9 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.4037 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val9_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9444 | 0.5155 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val11_test9 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4537 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val9_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.3686 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val10_test9 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.4749 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val9_test10 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.3962 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val11_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9630 | 0.7050 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val12_test11 | 42 | 0.8333 | 0.8333 | 0.8125 | 0.9815 | 0.4111 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val10_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9444 | 0.5587 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val12_test10 | 42 | 0.8333 | 0.8333 | 0.8125 | 0.9815 | 0.3820 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val10_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.3585 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val11_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2993 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val12_test8 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2606 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val8_test12 | 42 | 0.8333 | 0.8333 | 0.8310 | 0.9444 | 0.6596 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val11_test8 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2374 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val8_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.3513 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val10_test8 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2763 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val8_test10 | 42 | 0.8333 | 0.8333 | 0.8333 | 0.9815 | 0.5440 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val7_test9 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.5407 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val9_test7 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3960 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val12_test7 | 42 | 0.8333 | 0.8333 | 0.8125 | 0.9722 | 0.4193 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val7_test12 | 42 | 0.7500 | 0.7500 | 0.7321 | 0.9444 | 0.8829 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val11_test7 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4438 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val7_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.4795 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val10_test7 | 42 | 0.8333 | 0.8333 | 0.8333 | 0.9815 | 0.3719 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val7_test10 | 42 | 0.8333 | 0.8333 | 0.8333 | 0.9630 | 0.4040 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val7_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2746 |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val8_test7 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9907 | 0.4458 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val8_test9 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.5981 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val9_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2883 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val12_test9 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.4037 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val9_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9444 |  | 0.5155 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val11_test9 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4537 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val9_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.3686 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val10_test9 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.4749 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val9_test10 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.3962 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val11_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9630 |  | 0.7050 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val12_test11 | 1 | 0.8333 |  | 0.8333 |  | 0.8125 |  | 0.9815 |  | 0.4111 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val10_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9444 |  | 0.5587 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val12_test10 | 1 | 0.8333 |  | 0.8333 |  | 0.8125 |  | 0.9815 |  | 0.3820 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val10_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.3585 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val11_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2993 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val12_test8 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2606 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val8_test12 | 1 | 0.8333 |  | 0.8333 |  | 0.8310 |  | 0.9444 |  | 0.6596 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val11_test8 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2374 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val8_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.3513 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val10_test8 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2763 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val8_test10 | 1 | 0.8333 |  | 0.8333 |  | 0.8333 |  | 0.9815 |  | 0.5440 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val7_test9 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.5407 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val9_test7 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3960 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val12_test7 | 1 | 0.8333 |  | 0.8333 |  | 0.8125 |  | 0.9722 |  | 0.4193 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val7_test12 | 1 | 0.7500 |  | 0.7500 |  | 0.7321 |  | 0.9444 |  | 0.8829 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val11_test7 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4438 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val7_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.4795 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val10_test7 | 1 | 0.8333 |  | 0.8333 |  | 0.8333 |  | 0.9815 |  | 0.3719 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val7_test10 | 1 | 0.8333 |  | 0.8333 |  | 0.8333 |  | 0.9630 |  | 0.4040 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val7_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2746 |  |
| cp2_s3 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val8_test7 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9907 |  | 0.4458 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s3 | resnet1D | resnet1D-843fbf2 | 42 | 30 | 0.9000 | 0.0554 | 0.9000 | 0.0554 | 0.8957 | 0.0595 | 0.9809 | 0.0180 | 0.4400 | 0.1425 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s3 | resnet1D | resnet1D-843fbf2 | 30 | 0.9000 | 0.0554 | 0.9000 | 0.0554 | 0.8957 | 0.0595 | 0.9809 | 0.0180 | 0.4400 | 0.1425 |

### Pooled confusion matrix: cp2_s3 / resnet1D / resnet1D-843fbf2

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 73 | 17 | 0 | 0 |
| B1 | 14 | 71 | 1 | 4 |
| B2 | 0 | 0 | 90 | 0 |
| B3 | 0 | 0 | 0 | 90 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 81.11 | 18.89 | 0.00 | 0.00 |
| B1 | 15.56 | 78.89 | 1.11 | 4.44 |
| B2 | 0.00 | 0.00 | 100.00 | 0.00 |
| B3 | 0.00 | 0.00 | 0.00 | 100.00 |
