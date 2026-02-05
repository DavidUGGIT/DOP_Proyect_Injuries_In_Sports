import pytest
import pandas
import openpyxl

from pathlib import Path




def test_injury_data_consolidated():
    my_file = Path("../data/injury_data_consolidated.xlsx")
    assert (my_file.exists()), f"File {my_file} does not exist"

def test_injury_data_consolidated_isnt_empty():
    df = pandas.read_excel("../data/injury_data_consolidated.xlsx")
    assert "Ricky Rubio - 2010/11" in df.iloc[:, 0].values, f"Injury data does not contain the tested data"

def test_collegiate_injury_data():
    my_file = Path("../data/collegiate_athlete_injury_dataset.csv")
    assert (my_file.exists()), f"File {my_file} does not exist"

def test_collegiate_injury_data_isnt_empty():
    df = pandas.read_csv("../data/collegiate_athlete_injury_dataset.csv")
    expected = (df.iloc[:, 0].astype(str).eq("A189") & df.iloc[:, 1].eq(20) & df.iloc[:, 2].eq("Male"))
    assert expected.any(), f"Collegiate athlete injury isnt the expected data"
