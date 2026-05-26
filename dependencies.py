from fastapi import Depends
from db.session import get_db
from core.redis import redis_client
from services.url_service import URLService

def get_url_service(db=Depends(get_db)) -> URLService:
    """Dependency to get the URLService instance."""
    return URLService(cache=redis_client, db=db)