# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-3-4_val5_test6 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3511 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-3-4_val6_test5 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3296 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-3-5_val4_test6 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3923 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-3-5_val6_test4 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2880 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-3-6_val4_test5 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3538 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-3-6_val5_test4 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3183 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-4-5_val3_test6 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3554 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-4-5_val6_test3 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3222 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-4-6_val3_test5 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3588 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-4-6_val5_test3 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3508 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-5-6_val3_test4 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3188 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-5-6_val4_test3 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2977 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-3-4-5_val2_test6 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3466 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-3-4-5_val6_test2 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3408 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-3-4-6_val2_test5 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3539 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-3-4-6_val5_test2 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.3937 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-3-5-6_val2_test4 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2978 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-3-5-6_val4_test2 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3559 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-4-5-6_val2_test3 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3264 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-4-5-6_val3_test2 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3624 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train2-3-4-5_val1_test6 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3670 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train2-3-4-5_val6_test1 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4075 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train2-3-4-6_val1_test5 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3716 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train2-3-4-6_val5_test1 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4167 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train2-3-5-6_val1_test4 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4136 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train2-3-5-6_val4_test1 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4497 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train2-4-5-6_val1_test3 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3557 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train2-4-5-6_val3_test1 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4166 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train3-4-5-6_val1_test2 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9907 | 0.4049 |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train3-4-5-6_val2_test1 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4278 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-3-4_val5_test6 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3511 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-3-4_val6_test5 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3296 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-3-5_val4_test6 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3923 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-3-5_val6_test4 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2880 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-3-6_val4_test5 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3538 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-3-6_val5_test4 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3183 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-4-5_val3_test6 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3554 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-4-5_val6_test3 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3222 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-4-6_val3_test5 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3588 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-4-6_val5_test3 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3508 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-5-6_val3_test4 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3188 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-2-5-6_val4_test3 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2977 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-3-4-5_val2_test6 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3466 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-3-4-5_val6_test2 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3408 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-3-4-6_val2_test5 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3539 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-3-4-6_val5_test2 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.3937 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-3-5-6_val2_test4 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2978 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-3-5-6_val4_test2 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3559 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-4-5-6_val2_test3 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3264 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train1-4-5-6_val3_test2 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3624 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train2-3-4-5_val1_test6 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3670 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train2-3-4-5_val6_test1 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4075 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train2-3-4-6_val1_test5 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3716 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train2-3-4-6_val5_test1 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.4167 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train2-3-5-6_val1_test4 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4136 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train2-3-5-6_val4_test1 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4497 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train2-4-5-6_val1_test3 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3557 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train2-4-5-6_val3_test1 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4166 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train3-4-5-6_val1_test2 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9907 |  | 0.4049 |  |
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | train3-4-5-6_val2_test1 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4278 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | 42 | 30 | 0.9417 | 0.0388 | 0.9417 | 0.0388 | 0.9400 | 0.0400 | 0.9991 | 0.0037 | 0.3615 | 0.0412 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp1_s12_resnet1d | resnet1D | resnet1D-75d5c1e | 30 | 0.9417 | 0.0388 | 0.9417 | 0.0388 | 0.9400 | 0.0400 | 0.9991 | 0.0037 | 0.3615 | 0.0412 |

### Pooled confusion matrix: cp1_s12_resnet1d / resnet1D / resnet1D-75d5c1e

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 89 | 1 | 0 | 0 |
| B1 | 0 | 90 | 0 | 0 |
| B2 | 0 | 0 | 77 | 13 |
| B3 | 0 | 0 | 7 | 83 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 98.89 | 1.11 | 0.00 | 0.00 |
| B1 | 0.00 | 100.00 | 0.00 | 0.00 |
| B2 | 0.00 | 0.00 | 85.56 | 14.44 |
| B3 | 0.00 | 0.00 | 7.78 | 92.22 |
