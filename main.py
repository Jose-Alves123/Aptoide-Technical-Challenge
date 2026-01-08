from fastapi import FastAPI
from routes import scraper_router

app = FastAPI(title="Aptoide API", version="0.1.0")

app.include_router(scraper_router, prefix="/aptoide", tags=["Aptoide"])