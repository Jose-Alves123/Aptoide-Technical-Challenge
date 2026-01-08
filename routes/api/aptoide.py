from fastapi import APIRouter, status, HTTPException
from services import scraper_service

router = APIRouter()

DEFAULT_PACKAGE_NAME = "com.facebook.katana"

@router.get("/", status_code=status.HTTP_200_OK)
async def package_data(package_name : str | None = DEFAULT_PACKAGE_NAME):
    
    assert isinstance(package_name, str) 
    if not len(package_name):
        package_name = DEFAULT_PACKAGE_NAME

    
    data =  scraper_service.scrape_metadata(package_name)

    if "metadata" not in data:
        raise HTTPException(status_code=400, detail=data)

    return data
