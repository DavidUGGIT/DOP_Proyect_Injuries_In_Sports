from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def simple_regression(train_test_sets):
    train_x, train_y, test_x, test_y = train_test_sets
    train_x = np.array(train_x)
    test_x = np.array(test_x)
    if train_x.ndim == 1:
        train_x, test_x = train_x.reshape(-1, 1),test_x.reshape(-1, 1)

    model = LinearRegression()
    model.fit(train_x, train_y)
    preds = model.predict(test_x)
    return {
        "Coefficients": model.coef_,
        "Intercept": model.intercept_,
        "R²": model.score(test_x, test_y),
    }
