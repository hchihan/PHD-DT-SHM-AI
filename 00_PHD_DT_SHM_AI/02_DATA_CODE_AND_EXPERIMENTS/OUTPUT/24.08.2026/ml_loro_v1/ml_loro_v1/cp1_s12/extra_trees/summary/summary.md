# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-3-4_val5_test6 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4038 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-3-4_val6_test5 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3702 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-3-5_val4_test6 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4088 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-3-5_val6_test4 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3351 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-3-6_val4_test5 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3785 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-3-6_val5_test4 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3382 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-4-5_val3_test6 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3928 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-4-5_val6_test3 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3316 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-4-6_val3_test5 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3696 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-4-6_val5_test3 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3335 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-5-6_val3_test4 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3392 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-5-6_val4_test3 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3446 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-3-4-5_val2_test6 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3979 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-3-4-5_val6_test2 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3673 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-3-4-6_val2_test5 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3764 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-3-4-6_val5_test2 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3706 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-3-5-6_val2_test4 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3251 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-3-5-6_val4_test2 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3624 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-4-5-6_val2_test3 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3439 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-4-5-6_val3_test2 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3800 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train2-3-4-5_val1_test6 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4036 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train2-3-4-5_val6_test1 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4145 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train2-3-4-6_val1_test5 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3631 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train2-3-4-6_val5_test1 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4120 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train2-3-5-6_val1_test4 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3299 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train2-3-5-6_val4_test1 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4129 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train2-4-5-6_val1_test3 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3338 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train2-4-5-6_val3_test1 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4169 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train3-4-5-6_val1_test2 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3877 |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train3-4-5-6_val2_test1 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4360 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-3-4_val5_test6 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.4038 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-3-4_val6_test5 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3702 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-3-5_val4_test6 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.4088 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-3-5_val6_test4 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3351 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-3-6_val4_test5 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3785 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-3-6_val5_test4 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3382 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-4-5_val3_test6 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3928 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-4-5_val6_test3 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3316 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-4-6_val3_test5 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3696 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-4-6_val5_test3 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3335 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-5-6_val3_test4 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3392 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-2-5-6_val4_test3 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3446 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-3-4-5_val2_test6 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3979 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-3-4-5_val6_test2 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3673 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-3-4-6_val2_test5 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3764 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-3-4-6_val5_test2 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3706 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-3-5-6_val2_test4 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3251 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-3-5-6_val4_test2 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3624 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-4-5-6_val2_test3 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3439 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train1-4-5-6_val3_test2 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3800 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train2-3-4-5_val1_test6 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.4036 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train2-3-4-5_val6_test1 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.4145 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train2-3-4-6_val1_test5 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3631 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train2-3-4-6_val5_test1 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.4120 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train2-3-5-6_val1_test4 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3299 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train2-3-5-6_val4_test1 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.4129 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train2-4-5-6_val1_test3 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3338 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train2-4-5-6_val3_test1 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.4169 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train3-4-5-6_val1_test2 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3877 |  |
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | train3-4-5-6_val2_test1 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.4360 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | 42 | 30 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 0.3727 | 0.0321 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp1_s12_extra_trees | extra_trees | extra_trees-536c3a4 | 30 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 0.3727 | 0.0321 |

### Pooled confusion matrix: cp1_s12_extra_trees / extra_trees / extra_trees-536c3a4

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 90 | 0 | 0 | 0 |
| B1 | 0 | 90 | 0 | 0 |
| B2 | 0 | 0 | 90 | 0 |
| B3 | 0 | 0 | 0 | 90 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 100.00 | 0.00 | 0.00 | 0.00 |
| B1 | 0.00 | 100.00 | 0.00 | 0.00 |
| B2 | 0.00 | 0.00 | 100.00 | 0.00 |
| B3 | 0.00 | 0.00 | 0.00 | 100.00 |
