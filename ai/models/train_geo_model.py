from pathlib import Path

from ai.models.geo_model import train_geo_model, save_geo_model
from ai.preprocessing.prepare_geo_pm25 import preprocess_geo_pm25


def main():
    csv_path = Path("ai/data/raw/air_quality.csv")
    df = preprocess_geo_pm25(csv_path)
    model, mae, rmse = train_geo_model(df)
    save_geo_model(model)
    print(f"Geo Model trained and saved. MAE: {mae:.4f}, RMSE: {rmse:.4f}")


if __name__ == "__main__":
    main()
