from fastapi import APIRouter, status, HTTPException
import logging
from utils import json_util

router = APIRouter()

logger = logging.getLogger("uvicorn.error")  # uvicorn logs

@router.get("/", status_code=status.HTTP_200_OK)
async def package_data(package_name : str | None = None):
    logger.info("Attempting to scrape Aptoide API")

    return json_util.get_success("Hello World", {})