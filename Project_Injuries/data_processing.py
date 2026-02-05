import pandas as pd

def basketball_process_test_train(summary_basketball):
    summary_basketball = summary_basketball.iloc[:, :-2]

    basketball_before = summary_basketball.loc[summary_basketball.Period == 'Summary Before', :]
    basketball_after = summary_basketball.loc[summary_basketball.Period == 'Summary After', :]

    basketball_train_before = basketball_before.iloc[:20, :]
    basketball_train_after = basketball_after.iloc[:20, :]
    basketball_test_after = basketball_after.iloc[20:, :]
    basketball_test_before = basketball_before.iloc[20:, :]
    return (basketball_train_before, basketball_train_after,basketball_test_before, basketball_test_after)
