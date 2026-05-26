from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from typing import Annotated

from dependencies import get_url_service
from services.url_service import URLService
from schemas.url_schemas import URLBase

router = APIRouter()


@router.get("/url/{code}")
async def resolve_url(code: str, url_service: Annotated[URLService, Depends(get_url_service)]):
    """Endpoint to resolve a short URL code to its original URL."""
    original_url = await url_service.resolve_url(code)
    if not original_url:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
    

    return RedirectResponse(url=original_url, status_code=status.HTTP_307_TEMPORARY_REDIRECT)

@router.post("/shorten")
async def shorten_url(url_base: URLBase, url_service: Annotated[URLService, Depends(get_url_service)]):
    """Endpoint to shorten a given URL."""
    short_url = await url_service.shorten_url(str(url_base.url))
    return {"short_url": short_url}
