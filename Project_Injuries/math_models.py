from Project_Injuries.data_processing import basketball_process_test_train

from sklearn.linear_model import LinearRegression


def linear_regr_basket():
    train_x, train_y, test_x, test_y = basketball_process_test_train()
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

