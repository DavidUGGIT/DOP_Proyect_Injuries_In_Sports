from sklearn.linear_model import LinearRegression

def simple_regression(train_test_sets):
    train_x, train_y, test_x, test_y = train_test_sets
    model = LinearRegression()
    model.fit(train_x, train_y)
    preds = model.predict(test_x)
    return {"Coefficients": model.coef_,
    "Intercept": model.intercept_,
    "R²": model.score(test_x, test_y)}
