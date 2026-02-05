import sys
from pathlib import Path
import numpy as np

# dodajemy src/ do PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "Project_Injuries"
sys.path.insert(0, str(SRC_DIR))

from utils.simple_stats import simple_regression

def test_simple_regression_linear_case():
    # y = 2x + 1
    train_x = [0, 1, 2, 3]
    train_y = [1, 3, 5, 7]

    test_x = [4, 5]
    test_y = [9, 11]

    train_test_sets = (train_x, train_y, test_x, test_y)

    result = simple_regression(train_test_sets)

    # sprawdzamy klucze
    assert set(result.keys()) == {"Coefficients", "Intercept", "R²"}

    # sprawdzamy wartości (z tolerancją numeryczną)
    assert np.isclose(result["Intercept"], 1.0, atol=1e-6)
    assert np.isclose(result["Coefficients"][0], 2.0, atol=1e-6)

    # R² dla idealnych danych powinno być 1
    assert np.isclose(result["R²"], 1.0)

