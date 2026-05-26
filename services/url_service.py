from sqlalchemy import select
from typing import Optional

from db.session import AsyncSession
from db.models import URL
from utils import base62
from core.config import settings


class URLService:
    """Service for handling URL shortening logic."""

    def __init__(self, cache, db: AsyncSession):
        self.db = db
        self.cache = cache

    async def resolve_url(self, code: str) -> str | None:
        """Resolve a short URL code to its original URL."""
        # Check cache first
        
        cached_url: str = await self.cache.get(code)
        if cached_url:
            return cached_url
        
        id = base62.decode(code)
        url_record = await self.db.get(URL, id)

        if not url_record:
            return None
        
        await self.cache.set(code, url_record.original_url, ex=settings.REDIS_CACHE_TTL)
        return url_record.original_url


    async def shorten_url(self, original_url: str) -> str:
        """Shorten the given URL."""
        stmt = select(URL).where(URL.original_url == original_url)
        result: Optional[URL] = await self.db.scalar(stmt)
        if result:
            return f"{settings.BASE_URL}/url/{result.short_url}"
        
        new_url = URL(original_url=original_url, short_url="")
        self.db.add(new_url)
        await self.db.flush()  # Ensure ID is generated
        new_url.short_url = base62.encode(new_url.id)
        await self.db.commit()
        return f"{settings.BASE_URL}/url/{new_url.short_url}"
