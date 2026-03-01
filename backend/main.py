from fastapi import FastAPI
from backend.app.api.v1 import api_router

app = FastAPI(
    title="PM2.5 Forecast API",
    version="1.0.0"
)

app.include_router(api_router, prefix="/v1")
