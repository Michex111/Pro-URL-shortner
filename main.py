from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path
from typing import Annotated
import uvicorn

from api.routes.url import router as url_router
from db.session import get_db, Base, engine, AsyncSession
from core.config import settings

@asynccontextmanager
async def lifespan(app_: FastAPI):
    """Lifespan context manager to handle startup and shutdown events."""
    # Create database tables on startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # No specific shutdown actions needed

app = FastAPI(title=settings.APP_NAME, description="A simple URL shortener API built with FastAPI.", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # fine for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(url_router, prefix="", tags=["URL Shortener"])

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/health")
def db_health_check(db: Annotated[AsyncSession, Depends(get_db)]):
    """Health check endpoint."""


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the home page."""
    return templates.TemplateResponse(
        request,
        "index.html",
    )

    
    


if __name__ == "__main__":    
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)    


