from pydantic import BaseModel, Field


class ErrorResponse(BaseModel):
    """Error API response."""
    message: str = Field(..., description="Error message describing what went wrong")
    time: str = Field(..., description="Server timestamp of response")
