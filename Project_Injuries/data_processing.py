import pandas as pd
import numpy as np

def basketball_process_test_train(summary_basketball):
    summary_basketball = summary_basketball.iloc[:, :-2]

    basketball_before = summary_basketball.loc[summary_basketball.Period == 'Summary Before', :]
    basketball_after = summary_basketball.loc[summary_basketball.Period == 'Summary After', :]

    basketball_train_before = basketball_before.iloc[:20, :]
    basketball_train_after = basketball_after.iloc[:20, :]
    basketball_test_after = basketball_after.iloc[20:, :]
    basketball_test_before = basketball_before.iloc[20:, :]
    return (basketball_train_before, basketball_train_after,basketball_test_before, basketball_test_after)

def processing_for_lr_plot(train_test_sets):

    train_x, train_y, test_x, test_y = train_test_sets
    train_x, train_y, test_x, test_y = train_x.loc[:, 'PTS'], train_y.loc[:, 'PTS'], test_x.loc[:, 'PTS'], test_y.loc[:,'PTS']
    train_x, train_y, test_x, test_y = np.array(train_x), np.array(train_y), np.array(test_x), np.array(test_y)
    X_all = np.concatenate((train_x, test_x))
    Y_all = np.concatenate((train_y, test_y))
    return X_all, Y_all

