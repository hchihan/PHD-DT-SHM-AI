# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-3-4_val5_test6 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4158 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-3-4_val6_test5 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4405 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-3-5_val4_test6 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3348 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-3-5_val6_test4 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3259 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-3-6_val4_test5 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9907 | 0.4978 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-3-6_val5_test4 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3782 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-4-5_val3_test6 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4047 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-4-5_val6_test3 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3543 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-4-6_val3_test5 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4395 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-4-6_val5_test3 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3172 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-5-6_val3_test4 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3735 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-5-6_val4_test3 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3551 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-3-4-5_val2_test6 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3611 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-3-4-5_val6_test2 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3499 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-3-4-6_val2_test5 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4785 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-3-4-6_val5_test2 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.3693 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-3-5-6_val2_test4 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3458 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-3-5-6_val4_test2 | 42 | 0.8333 | 0.8333 | 0.8286 | 1.0000 | 0.3488 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-4-5-6_val2_test3 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3158 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-4-5-6_val3_test2 | 42 | 0.8333 | 0.8333 | 0.8333 | 0.9815 | 0.3759 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train2-3-4-5_val1_test6 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4261 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train2-3-4-5_val6_test1 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4288 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train2-3-4-6_val1_test5 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.4522 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train2-3-4-6_val5_test1 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3435 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train2-3-5-6_val1_test4 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3384 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train2-3-5-6_val4_test1 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3991 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train2-4-5-6_val1_test3 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3208 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train2-4-5-6_val3_test1 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3982 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train3-4-5-6_val1_test2 | 42 | 0.8333 | 0.8333 | 0.8286 | 1.0000 | 0.3513 |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train3-4-5-6_val2_test1 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4135 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-3-4_val5_test6 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4158 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-3-4_val6_test5 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4405 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-3-5_val4_test6 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3348 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-3-5_val6_test4 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3259 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-3-6_val4_test5 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9907 |  | 0.4978 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-3-6_val5_test4 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3782 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-4-5_val3_test6 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4047 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-4-5_val6_test3 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3543 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-4-6_val3_test5 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4395 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-4-6_val5_test3 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3172 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-5-6_val3_test4 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3735 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-2-5-6_val4_test3 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3551 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-3-4-5_val2_test6 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3611 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-3-4-5_val6_test2 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3499 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-3-4-6_val2_test5 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4785 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-3-4-6_val5_test2 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.3693 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-3-5-6_val2_test4 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3458 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-3-5-6_val4_test2 | 1 | 0.8333 |  | 0.8333 |  | 0.8286 |  | 1.0000 |  | 0.3488 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-4-5-6_val2_test3 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3158 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train1-4-5-6_val3_test2 | 1 | 0.8333 |  | 0.8333 |  | 0.8333 |  | 0.9815 |  | 0.3759 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train2-3-4-5_val1_test6 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4261 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train2-3-4-5_val6_test1 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4288 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train2-3-4-6_val1_test5 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.4522 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train2-3-4-6_val5_test1 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3435 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train2-3-5-6_val1_test4 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3384 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train2-3-5-6_val4_test1 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3991 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train2-4-5-6_val1_test3 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3208 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train2-4-5-6_val3_test1 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3982 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train3-4-5-6_val1_test2 | 1 | 0.8333 |  | 0.8333 |  | 0.8286 |  | 1.0000 |  | 0.3513 |  |
| cp1_s1 | resnet1D | resnet1D-843fbf2 | train3-4-5-6_val2_test1 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4135 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp1_s1 | resnet1D | resnet1D-843fbf2 | 42 | 30 | 0.9333 | 0.0509 | 0.9333 | 0.0509 | 0.9316 | 0.0520 | 0.9978 | 0.0058 | 0.3818 | 0.0489 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp1_s1 | resnet1D | resnet1D-843fbf2 | 30 | 0.9333 | 0.0509 | 0.9333 | 0.0509 | 0.9316 | 0.0520 | 0.9978 | 0.0058 | 0.3818 | 0.0489 |

### Pooled confusion matrix: cp1_s1 / resnet1D / resnet1D-843fbf2

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 87 | 3 | 0 | 0 |
| B1 | 0 | 90 | 0 | 0 |
| B2 | 0 | 0 | 79 | 11 |
| B3 | 0 | 0 | 10 | 80 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 96.67 | 3.33 | 0.00 | 0.00 |
| B1 | 0.00 | 100.00 | 0.00 | 0.00 |
| B2 | 0.00 | 0.00 | 87.78 | 12.22 |
| B3 | 0.00 | 0.00 | 11.11 | 88.89 |
