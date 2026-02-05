import pandas as pd
from pathlib import Path


# katalog projektu (jeden poziom wyżej niż tests/)
ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"


def test_injury_data_consolidated_exists():
    file_path = DATA_DIR / "injury_data_consolidated.xlsx"
    assert file_path.exists(), f"File {file_path} does not exist"


def test_injury_data_consolidated_isnt_empty():
    file_path = DATA_DIR / "injury_data_consolidated.xlsx"
    df = pd.read_excel(file_path)

    assert not df.empty, "Injury data file is empty"
    assert "Ricky Rubio - 2010/11" in df.iloc[:, 0].astype(str).values, \
        "Injury data does not contain the tested data"


def test_collegiate_injury_data_exists():
    file_path = DATA_DIR / "collegiate_athlete_injury_dataset.csv"
    assert file_path.exists(), f"File {file_path} does not exist"


def test_collegiate_injury_data_isnt_empty():
    file_path = DATA_DIR / "collegiate_athlete_injury_dataset.csv"
    df = pd.read_csv(file_path)

    assert not df.empty, "Collegiate athlete injury dataset is empty"

    expected = (
        df.iloc[:, 0].astype(str).eq("A189")
        & df.iloc[:, 1].eq(20)
        & df.iloc[:, 2].eq("Male")
    )

    assert expected.any(), "Collegiate athlete injury dataset does not contain expected data"
