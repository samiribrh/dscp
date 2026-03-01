from joblib import dump
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


def train_geo_model(df):
    features = ["pm25_lag_1", "pm25_lag_2", "pm25_lag_3",
                "month", "sin_month", "cos_month", "location_code"]
    X = df[features]
    y = df["pm25"]

    model = LinearRegression()
    model.fit(X, y)

    preds = model.predict(X)
    mae = mean_absolute_error(y, preds)
    rmse = mean_squared_error(y, preds)

    return model, mae, rmse


def save_geo_model(model, path="ai/models/geo_model.joblib"):
    dump(model, path)
