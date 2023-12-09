"""Health check route"""
from fastapi import APIRouter

health_router = APIRouter(
    prefix="/api/v1",
    tags=["Health"],
)


@health_router.get("/healthz")
def health_check():
    return {"status": "up", "current_version": "v1"}
