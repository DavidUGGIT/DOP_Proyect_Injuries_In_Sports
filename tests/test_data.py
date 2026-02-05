import pytest
import pandas

from pathlib import Path




def test_injury_data_consolidated():
    my_file = Path("/../data/injury_data_consolidated.xlsx")
    assert (my_file.exists()), f"File {my_file} does not exist"

def test_injury_data():
    df = pandas.read_csv("/../data/injury_data_consolidated.xlsx")
    assert "Ricky Rubio - 2012/13" in df.iloc[:, 0].values, f"Injury data does not contain the tested data"

