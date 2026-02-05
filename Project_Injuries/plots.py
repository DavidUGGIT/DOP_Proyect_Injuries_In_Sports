import matplotlib.pyplot as plt
import numpy as np

def regression_plot(x, y, intercept, coef, xlabel, ylabel, title):
    y_pred = x*coef+intercept
    order = np.argsort(x)
    x_sorted = x[order]
    y_pred_sorted = y_pred[order]
    plt.scatter(x, y)  # real observations (dots)
    plt.plot(x_sorted, y_pred_sorted)  # regression line
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()