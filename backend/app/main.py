from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routers import rides

app = FastAPI(
    title=settings.PLATFORM_NAME,
    description="API REST de San Martín Conecta",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rides.router)


@app.get("/")
def read_root():
    """Endpoint raíz: confirma que la API está viva."""
    return {
        "platform": settings.PLATFORM_NAME,
        "status": "ok",
        "environment": settings.ENVIRONMENT,
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}
