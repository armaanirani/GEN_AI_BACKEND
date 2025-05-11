from fastapi import APIRouter
from utils.logger import logger

router = APIRouter()

@router.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify if the API is running.
    """
    logger.info("Health check endpoint called.")
    return {"status": "ok", "message": "API is running."}