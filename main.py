from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI
from typing import Annotated
import uvicorn

from api.routes.url import router as url_router
from db.session import get_db, Base, engine, AsyncSession
from db.models import URL
from core.config import settings
from core.redis import redis_client
from services.url_service import URLService

@asynccontextmanager
async def lifespan(app_: FastAPI):
    """Lifespan context manager to handle startup and shutdown events."""
    # Create database tables on startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # No specific shutdown actions needed

app = FastAPI(name=settings.APP_NAME, description="A simple URL shortener API built with FastAPI.", lifespan=lifespan)

app.include_router(url_router, prefix="/url", tags=["URL Shortener"])


@app.get("/health")
def db_health_check(db: Annotated[AsyncSession, Depends(get_db)]):
    """Health check endpoint."""

    
    


if __name__ == "__main__":    
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)    


