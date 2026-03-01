from fastapi.testclient import TestClient

from backend.app.core.config import settings
from backend.main import app


client = TestClient(app)


def test_geo_predict_valid_input():
    response = client.post(
        "/v1/predict/predict/geo",
        headers={"x-api-key": settings.API_KEY},
        json={
            "pm25_lag_1": 8.7,
            "pm25_lag_2": 8.4,
            "pm25_lag_3": 8.1,
            "month": 5,
            "location_code": 42
        }
    )
    assert response.status_code == 200
    json_data = response.json()
    assert "predicted_pm25" in json_data
    assert isinstance(json_data["predicted_pm25"], float)


def test_geo_predict_invalid_input():
    response = client.post(
        "/v1/predict/predict/geo",
        headers={"x-api-key": settings.API_KEY},
        json={
            "pm25_lag_1": "bad",  # invalid type
            "pm25_lag_2": 8.4,
            "pm25_lag_3": 8.1,
            "month": 5,
            "location_code": 42
        }
    )
    assert response.status_code == 422
