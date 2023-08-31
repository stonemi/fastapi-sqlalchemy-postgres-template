from fastapi import APIRouter, Depends, HTTPException, status
from schemas.models import HealthResponse

router = APIRouter(tags=["basic"])

@router.get("/health", response_model=HealthResponse)
async def health():
    return HealthResponse(status="Ok")