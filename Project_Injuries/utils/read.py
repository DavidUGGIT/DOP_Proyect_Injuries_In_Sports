import os
import pandas as pd
from pathlib import Path

def load_data_consolidated(folder_path):
    '''ładowanie danych'''
    data_frames = dict()
    file_path = os.path.join(folder_path, "injury_data_consolidated.xlsx")
    print(file_path)
    xls = pd.ExcelFile(file_path)
    tables_names = xls.sheet_names
    for name in tables_names:
        data_frames.update({name:pd.read_excel(file_path, sheet_name=name)})
    return data_frames


def load_football_player_impact():

    BASE_DIR = Path(__file__).resolve().parents[1]  # project root
    DATA_PATH = BASE_DIR / "data" / "player_injuries_impact.csv"
    return pd.read_csv(DATA_PATH)


    # df = pd.read_csv(DATA_PATH)
    # for filename in os.listdir(//):
    #     if filename.endswith(".xlsx"):
    #         if filename == "powierzchnia_i_ludnosc_w_przekroju_" \
    #                        "terytorialnym_w_2024_roku_tablice.xlsx":
    #             file_path = os.path.join(folder_path, filename)
    #             print(f"Reading: {file_path}")
    #             pow_ludn_2024_woj = pd.read_excel(file_path, sheet_name="Tabl. 1", skiprows=5)
    #             pow_ludn_2024_pow = pd.read_excel(file_path, sheet_name="Tabl. 2", skiprows=2)
    #             data_frames.append((filename, pow_ludn_2024_woj))
    #             data_frames.append((filename, pow_ludn_2024_pow))
    #         elif filename == "nowe_mieszkania.xlsx":
    #             file_path = os.path.join(folder_path, filename)
    #             print(f"Reading: {file_path}")
    #             nowe_mieszk = pd.read_excel(file_path, sheet_name="TABLICA", skiprows=2)
    #             data_frames.append((filename, nowe_mieszk))
    #         else:
    #             file_path = os.path.join(folder_path, filename)
    #             print(f"Reading: {file_path}")
    #             df = pd.read_excel(file_path)
    #             data_frames.append((filename, df))
    #     if filename.endswith(".csv"):
    #         file_path = os.path.join(folder_path, filename)
    #         print(f"Reading: {file_path}")
    #         df = pd.read_csv(file_path)
    #         data_frames.append((filename, df))
    # return data_frames

