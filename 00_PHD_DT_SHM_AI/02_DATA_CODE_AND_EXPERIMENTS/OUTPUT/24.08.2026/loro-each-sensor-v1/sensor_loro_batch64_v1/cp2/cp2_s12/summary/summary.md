# Recording-level results

Metrics are computed per recording: the window probabilities of a recording
are averaged before the argmax. `sd` is the sample standard deviation.

## Per run

| dataset_name | model_name | version | split_id | seed | accuracy | balanced_accuracy | f1_macro | roc_auc_macro | test_loss |
|---|---|---|---|---|---|---|---|---|---|
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val8_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2448 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val9_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2743 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val12_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2969 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val9_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.5637 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val11_test9 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2833 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val9_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2743 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val10_test9 | 42 | 0.8333 | 0.8333 | 0.8310 | 0.9907 | 0.3454 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val9_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2313 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val11_test12 | 42 | 0.7500 | 0.7500 | 0.7595 | 0.9630 | 0.6635 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val12_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4173 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val10_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9815 | 0.5008 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val12_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2227 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val10_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2478 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val11_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1959 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val12_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2570 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val8_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4244 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val11_test8 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.3741 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val8_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.2822 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val10_test8 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.2931 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val8_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1799 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val7_test9 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1792 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val9_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.3531 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val12_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4309 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val7_test12 | 42 | 0.9167 | 0.9167 | 0.9143 | 1.0000 | 0.4070 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val11_test7 | 42 | 0.8333 | 0.8333 | 0.8286 | 1.0000 | 0.5997 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val7_test11 | 42 | 0.9167 | 0.9167 | 0.9143 | 0.9907 | 0.3860 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val10_test7 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4352 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val7_test10 | 42 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.1979 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val7_test8 | 42 | 0.7500 | 0.7500 | 0.7310 | 0.9722 | 0.4961 |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val8_test7 | 42 | 0.8333 | 0.8333 | 0.8310 | 0.9537 | 0.7033 |

## Mean ± SD across seeds (one row per split/fold)

| dataset_name | model_name | version | split_id | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val8_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2448 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-10-11-12_val9_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2743 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val12_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2969 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-10-11_val9_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.5637 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val11_test9 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2833 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-10-12_val9_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2743 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val10_test9 | 1 | 0.8333 |  | 0.8333 |  | 0.8310 |  | 0.9907 |  | 0.3454 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-11-12_val9_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2313 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val11_test12 | 1 | 0.7500 |  | 0.7500 |  | 0.7595 |  | 0.9630 |  | 0.6635 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-9-10_val12_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4173 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val10_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9815 |  | 0.5008 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-9-11_val12_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2227 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val10_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2478 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-8-9-12_val11_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1959 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val12_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2570 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-9-10-11_val8_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4244 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val11_test8 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.3741 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-9-10-12_val8_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.2822 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val10_test8 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.2931 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train7-9-11-12_val8_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1799 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val7_test9 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1792 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train8-10-11-12_val9_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.3531 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val12_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.4309 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train8-9-10-11_val7_test12 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 1.0000 |  | 0.4070 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val11_test7 | 1 | 0.8333 |  | 0.8333 |  | 0.8286 |  | 1.0000 |  | 0.5997 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train8-9-10-12_val7_test11 | 1 | 0.9167 |  | 0.9167 |  | 0.9143 |  | 0.9907 |  | 0.3860 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val10_test7 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.4352 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train8-9-11-12_val7_test10 | 1 | 1.0000 |  | 1.0000 |  | 1.0000 |  | 1.0000 |  | 0.1979 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val7_test8 | 1 | 0.7500 |  | 0.7500 |  | 0.7310 |  | 0.9722 |  | 0.4961 |  |
| cp2_s12 | resnet1D | resnet1D-843fbf2 | train9-10-11-12_val8_test7 | 1 | 0.8333 |  | 0.8333 |  | 0.8310 |  | 0.9537 |  | 0.7033 |  |

## Mean ± SD across splits/folds (one row per seed)

| dataset_name | model_name | version | seed | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s12 | resnet1D | resnet1D-843fbf2 | 42 | 30 | 0.9361 | 0.0748 | 0.9361 | 0.0748 | 0.9346 | 0.0764 | 0.9944 | 0.0121 | 0.3587 | 0.1431 |

## Mean ± SD across every run (seeds and folds pooled)

| dataset_name | model_name | version | n_runs | accuracy_mean | accuracy_sd | balanced_accuracy_mean | balanced_accuracy_sd | f1_macro_mean | f1_macro_sd | roc_auc_macro_mean | roc_auc_macro_sd | test_loss_mean | test_loss_sd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| cp2_s12 | resnet1D | resnet1D-843fbf2 | 30 | 0.9361 | 0.0748 | 0.9361 | 0.0748 | 0.9346 | 0.0764 | 0.9944 | 0.0121 | 0.3587 | 0.1431 |

### Pooled confusion matrix: cp2_s12 / resnet1D / resnet1D-843fbf2

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 85 | 5 | 0 | 0 |
| B1 | 2 | 84 | 4 | 0 |
| B2 | 0 | 3 | 84 | 3 |
| B3 | 0 | 0 | 6 | 84 |

Row-normalized:

| true \ pred | Healthy | B1 | B2 | B3 |
|---|---|---|---|---|
| Healthy | 94.44 | 5.56 | 0.00 | 0.00 |
| B1 | 2.22 | 93.33 | 4.44 | 0.00 |
| B2 | 0.00 | 3.33 | 93.33 | 3.33 |
| B3 | 0.00 | 0.00 | 6.67 | 93.33 |
