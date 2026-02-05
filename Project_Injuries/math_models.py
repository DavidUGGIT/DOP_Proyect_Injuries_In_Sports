from sklearn.linear_model import LinearRegression
from .utils.simple_stats import simple_regression
import pandas as pd


def linear_regr_basket(basketball_processed):
    train_x, train_y, test_x, test_y = basketball_processed

    cols = ["PTS", "AST", "REB"]

    train_x_multi = train_x[cols]
    test_x_multi = test_x[cols]

    results_multi = []

    for target in cols:
        train_y_temp = train_y[target]
        test_y_temp = test_y[target]

        res = simple_regression((train_x_multi, train_y_temp, test_x_multi, test_y_temp))
        res["Model"] = "3 variables"
        res["Target"] = target
        results_multi.append(res)

    results_multi_df = pd.DataFrame(results_multi)

    results_single = []

    for col in cols:
        train_x_single = train_x[[col]]  # podwójne [[]] → zawsze 2D
        test_x_single = test_x[[col]]

        train_y_temp = train_y[col]
        test_y_temp = test_y[col]

        res = simple_regression((train_x_single, train_y_temp, test_x_single, test_y_temp))
        res["Model"] = "1 variable"
        res["Target"] = col
        results_single.append(res)

    results_single_df = pd.DataFrame(results_single)

    return results_multi_df, results_single_df