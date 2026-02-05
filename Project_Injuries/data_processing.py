import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split


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

def collegiate_prepare_knn(college_processed):
    college_processed = college_processed.drop(["Athlete_ID", "League"], axis = 1)
    college_processed_encode = pd.get_dummies(college_processed, columns=['Gender', 'Position', 'ACL_Risk_Category'])
    print(f'liczba braków danych:\n {college_processed_encode.isna().sum()}')
    injury_part = college_processed_encode.loc[college_processed_encode.Injury_Indicator == 1,:]
    healthy_part = college_processed_encode.loc[college_processed_encode.Injury_Indicator == 0,:]
    return injury_part, healthy_part

def ml_split_collegiate(injury_part, healthy_part):

    X_injured = injury_part.drop(["Injury_Indicator"],axis=1, inplace = False)
    y_injured = injury_part.Injury_Indicator
    X_healthy = healthy_part.drop(["Injury_Indicator"], axis=1, inplace=False)
    y_healthy = healthy_part.Injury_Indicator
    X_train_inj, X_test_inj, y_train_inj, y_test_inj = train_test_split(
        X_injured, y_injured,
        test_size=0.5,  # 50% of data for testing
        random_state=42)
    X_train_h, X_test_h, y_train_h, y_test_h = train_test_split(
        X_healthy, y_healthy,
        test_size=0.5,  # 50% of data for testing
        random_state=42)

    X_train = pd.concat([X_train_inj, X_train_h])
    y_train = pd.concat([y_train_inj, y_train_h])
    X_test = pd.concat([X_test_inj, X_test_h])
    y_test = pd.concat([y_test_inj, y_test_h])

    return X_train, y_train, X_test, y_test



