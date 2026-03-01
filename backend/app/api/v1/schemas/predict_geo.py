from pydantic import BaseModel


class PredictionGeoInput(BaseModel):
    pm25_lag_1: float
    pm25_lag_2: float
    pm25_lag_3: float
    month: int
    location_code: int


class PredictionGeoResponse(BaseModel):
    predicted_pm25: float
