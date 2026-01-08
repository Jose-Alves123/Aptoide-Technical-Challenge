from pydantic import BaseModel, Field
from typing import Optional

class AppMetadata(BaseModel):
    """Complete metadata for an Android application."""
    
    name: Optional[str] = Field(None, description="Application name")
    size: Optional[int] = Field(None, description="Application size in bytes")
    downloads: Optional[int] = Field(None, description="Total number of downloads")
    version: Optional[str] = Field(None, description="Current application version")
    release_date: Optional[str] = Field(None, description="Release/modification date as Unix timestamp")
    package_id: Optional[str] = Field(None, description="Android package identifier (e.g., com.example.app)")
    sha1_signature: Optional[str] = Field(None, description="SHA1 hash of application signature")
    developer_cn: Optional[str] = Field(None, description="Developer Common Name from certificate")
    organization: Optional[str] = Field(None, description="Developer organization from certificate")
    local: Optional[str] = Field(None, description="Developer locality from certificate")
    country: Optional[str] = Field(None, description="Developer country from certificate")
    state_city: Optional[str] = Field(None, description="Developer state/city from certificate")
    min_screen: Optional[str] = Field(None, description="Minimum screen size requirement")
    supported_cpus: Optional[list] = Field(None, description="Supported CPU architectures")


class SuccessResponse(BaseModel):
    """Successful API response with app metadata."""
    
    metadata: AppMetadata = Field(..., description="Application metadata and information")
    message: str = Field(..., description="Success message")
    time: str = Field(..., description="Server timestamp of response")
