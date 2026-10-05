# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val8_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.5144 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val9_test8 | 42 | 0.8333 | 0.8333 | 0.8125 | 1.0000 | 0.5905 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val12_test9 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.5372 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val9_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.6500 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val11_test9 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.5665 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val9_test11 | 42 | 0.8333 | 0.8333 | 0.8286 | 1.0000 | 0.5915 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val10_test9 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.5030 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val9_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4644 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val11_test12 | 42 | 0.8333 | 0.8333 | 0.8036 | 0.9630 | 0.6463 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val12_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.5885 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val10_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.5835 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val12_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4554 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val10_test11 | 42 | 0.8333 | 0.8333 | 0.8286 | 0.9815 | 0.6220 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val11_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4850 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val12_test8 | 42 | 0.8333 | 0.8333 | 0.8286 | 1.0000 | 0.5885 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val8_test12 | 42 | 0.7500 | 0.7500 | 0.7542 | 0.9722 | 0.6357 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val11_test8 | 42 | 0.8333 | 0.8333 | 0.8286 | 1.0000 | 0.5340 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val8_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.6088 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val10_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.5266 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val8_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4441 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val7_test9 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.5324 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val9_test7 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.6196 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val12_test7 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9630 | 0.7034 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val7_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9630 | 0.6404 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val11_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6620 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val7_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.7050 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val10_test7 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9907 | 0.6390 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val7_test10 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4653 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val7_test8 | 42 | 0.8333 | 0.8333 | 0.8310 | 0.9722 | 0.6517 |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val8_test7 | 42 | 0.7500 | 0.7500 | 0.7476 | 0.9630 | 0.7812 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val8_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.5144 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val9_test8 | 1 | 0.8333 |  | 0.8333 |  | 0.8125 |  | 1.0000 |  | 0.5905 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val12_test9 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.5372 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val9_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.6500 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val11_test9 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.5665 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val9_test11 | 1 | 0.8333 |  | 0.8333 |  | 0.8286 |  | 1.0000 |  | 0.5915 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val10_test9 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.5030 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val9_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.4644 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val11_test12 | 1 | 0.8333 |  | 0.8333 |  | 0.8036 |  | 0.9630 |  | 0.6463 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val12_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.5885 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val10_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.5835 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val12_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.4554 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val10_test11 | 1 | 0.8333 |  | 0.8333 |  | 0.8286 |  | 0.9815 |  | 0.6220 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val11_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.4850 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val12_test8 | 1 | 0.8333 |  | 0.8333 |  | 0.8286 |  | 1.0000 |  | 0.5885 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val8_test12 | 1 | 0.7500 |  | 0.7500 |  | 0.7542 |  | 0.9722 |  | 0.6357 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val11_test8 | 1 | 0.8333 |  | 0.8333 |  | 0.8286 |  | 1.0000 |  | 0.5340 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val8_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.6088 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val10_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.5266 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val8_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.4441 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val7_test9 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.5324 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val9_test7 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.6196 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val12_test7 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9630 |  | 0.7034 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val7_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9630 |  | 0.6404 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val11_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.6620 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val7_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.7050 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val10_test7 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9907 |  | 0.6390 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val7_test10 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4653 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val7_test8 | 1 | 0.8333 |  | 0.8333 |  | 0.8310 |  | 0.9722 |  | 0.6517 |  |
| cp2_s2 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val8_test7 | 1 | 0.7500 |  | 0.7500 |  | 0.7476 |  | 0.9630 |  | 0.7812 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s2 | resnet1D | resnet1D-843fbf2 | 42 | 30 | 0.9056 | 0.0717 | 0.9056 | 0.0717 | 0.9021 | 0.0741 | 0.9892 | 0.0140 | 0.5845 | 0.0821 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s2 | resnet1D | resnet1D-843fbf2 | 30 | 0.9056 | 0.0717 | 0.9056 | 0.0717 | 0.9021 | 0.0741 | 0.9892 | 0.0140 | 0.5845 | 0.0821 |

### Pooled confusion matrix: cp2_s2 / resnet1D / resnet1D-843fbf2

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 80 | 10 | 0 | 0 |
| B1 | 9 | 76 | 2 | 3 |
| B2 | 1 | 0 | 83 | 6 |
| B3 | 0 | 0 | 3 | 87 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 88.89 | 11.11 | 0.00 | 0.00 |
| B1 | 10.00 | 84.44 | 2.22 | 3.33 |
| B2 | 1.11 | 0.00 | 92.22 | 6.67 |
| B3 | 0.00 | 0.00 | 3.33 | 96.67 |
