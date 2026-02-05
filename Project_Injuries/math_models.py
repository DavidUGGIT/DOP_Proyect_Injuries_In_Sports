from sklearn.linear_model import LinearRegression
from utils.simple_stats import simple_regression

def linear_regr_basket(basketball_processed):
    train_x, train_y, test_x, test_y = basketball_processed
    model = LinearRegression()
    train_x = train_x[["PTS", "AST", "REB"]]
    test_x = test_x[["PTS", "AST", "REB"]]
    results = []
    for stat in ("PTS", "AST", "REB"):
        train_y = train_y.loc[:,stat]
        test_y = train_y.loc[:, stat]
        model.fit(train_x, train_y)
        preds = model.predict(test_x)
        results.append({"Coefficients": model.coef_,
        "Intercept": model.intercept_,
        "R²": model.score(test_x, test_y)})
    results_three_var = pd.DataFrame(results)
    for stat in ("PTS", "AST", "REB"):
        train_y = train_y.loc[:,stat]
        test_y = train_y.loc[:, stat]
        train_x = train_x.loc[:, stat]
        test_x = test_x.loc[:, stat]
        model.fit(train_x, train_y)
        preds = model.predict(test_x)
        results.append({"Coefficients": model.coef_,
        "Intercept": model.intercept_,
        "R²": model.score(X_test, y_test)})
    results_simple_reg = pd.DataFrame(results)
    return results_three_var, results_simple_reg

def linear_regr_basket(basketball_processed):
    train_x, train_y, test_x, test_y = basketball_processed

    train_x = train_x[["PTS", "AST", "REB"]]
    test_x = test_x[["PTS", "AST", "REB"]]
    results = []
    for stat in ("PTS", "AST", "REB"):
        train_y_temp = train_y.loc[:,stat]
        test_y_temp = train_y.loc[:, stat]
        part_results = simple_regression((train_x, train_y_temp, test_x, test_y_temp))
        results.append(part_results)
    results_three_var = pd.DataFrame(results)
    for stat in ("PTS", "AST", "REB"):
        train_y_temp2 = train_y.loc[:,stat]
        test_y_temp2 = train_y.loc[:, stat]
        train_x_temp2 = train_x.loc[:, stat]
        test_x_temp2 = test_x.loc[:, stat]
        model.fit(train_x, train_y)
        preds = model.predict(test_x)
        results.append({"Coefficients": model.coef_,
        "Intercept": model.intercept_,
        "R²": model.score(X_test, y_test)})
    results_simple_reg = pd.DataFrame(results)
    return results_three_var, results_simple_reg

