import math
import numpy as np

from fastapi import APIRouter, Depends

from backend.app.api.v1.schemas.predict_geo import (
    PredictionGeoInput,
    PredictionGeoResponse,
)
from backend.app.api.v1.dependencies.auth import verify_api_key
from backend.app.core.logger import logger
from ai.models.save_model import load_model


router = APIRouter()
model = load_model("ai/models/geo_model.joblib")


@router.post("/predict/geo", response_model=PredictionGeoResponse)
def predict_pm25_geo(data: PredictionGeoInput, _: str = Depends(verify_api_key)):
    sin_month = math.sin(2 * math.pi * data.month / 12)
    cos_month = math.cos(2 * math.pi * data.month / 12)
    features = np.array([[
        data.pm25_lag_1, data.pm25_lag_2, data.pm25_lag_3, data.month,
        sin_month, cos_month, data.location_code
    ]])
    pred = model.predict(features)[0]
    logger.info(f"Geo prediction input: {data.model_dump()}, output: {round(pred, 2)}")
    return PredictionGeoResponse(predicted_pm25=round(pred, 2))
