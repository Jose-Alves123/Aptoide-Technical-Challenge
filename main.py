from fastapi import FastAPI
from routes import aptoide_router

app = FastAPI(title="Aptoide API", version="0.1.0")

app.include_router(aptoide_router, prefix="/aptoide", tags=["Aptoide"])