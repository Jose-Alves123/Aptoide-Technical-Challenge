from fastapi import APIRouter, status, HTTPException, Query
from typing import Dict, Any
from models import ErrorResponse, SuccessResponse
from services import scraper_service

DEFAULT_PACKAGE_NAME = "com.facebook.katana"
router = APIRouter()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=SuccessResponse,
    responses={
        400: {"model": ErrorResponse, "description": "Invalid package name or Aptoide API error"},
        500: {"description": "Internal server error"},
    },
    tags=["Aptoide App Metadata"],
    summary="Get Android App Metadata",
    description="""
    Retrieve detailed metadata and information about an Android application from the Aptoide store.
    
    This endpoint fetches comprehensive app information including:
    - Basic app details (name, size, version, downloads)
    - Hardware requirements (CPU architectures, screen sizes)
    - Developer certificate information
    - File signatures and identifiers
    
    The data is scraped from the Aptoide API for the specified package name.
    """
)
async def package_data(
    package_name: str = Query(
        "com.facebook.katana", 
        description="Android package name (e.g., 'com.facebook.katana')"
    )
) -> Dict[str, Any]:
    """
    Get metadata for an Android application.
    
    Args:
        package_name: The Android package identifier to lookup
        
    Returns:
        Dictionary with metadata if found
        
    Raises:
        HTTPException: 400 if package not found or API error occurs
    """
    assert isinstance(package_name, str) 
    if not len(package_name):
        package_name = DEFAULT_PACKAGE_NAME

    data : dict = scraper_service.scrape_metadata(package_name)

    if "metadata" not in data:
        raise HTTPException(status_code=400, detail=data)

    return data
