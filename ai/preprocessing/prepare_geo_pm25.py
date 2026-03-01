import pandas as pd
import numpy as np


def preprocess_geo_pm25(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    df = df[df["Name"] == "Fine particles (PM 2.5)"].copy()

    df["Date"] = pd.to_datetime(df["Start_Date"])
    df["month"] = df["Date"].dt.month
    df["year"] = df["Date"].dt.year
    df["sin_month"] = np.sin(2 * np.pi * df["month"] / 12)
    df["cos_month"] = np.cos(2 * np.pi * df["month"] / 12)
    df["location_code"] = df["Geo Join ID"].astype("category").cat.codes

    df.sort_values(["Geo Join ID", "Date"], inplace=True)
    df["pm25_lag_1"] = df.groupby("Geo Join ID")["Data Value"].shift(1)
    df["pm25_lag_2"] = df.groupby("Geo Join ID")["Data Value"].shift(2)
    df["pm25_lag_3"] = df.groupby("Geo Join ID")["Data Value"].shift(3)

    df = df.dropna(subset=["pm25_lag_1", "pm25_lag_2", "pm25_lag_3"])
    df = df.rename(columns={"Data Value": "pm25"})
    return df
