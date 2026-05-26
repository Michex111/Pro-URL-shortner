from pydantic import BaseModel, Field, HttpUrl

class URLBase(BaseModel):
    """Base model for URL."""
    url: HttpUrl = Field(..., description="The original URL to be shortened.")