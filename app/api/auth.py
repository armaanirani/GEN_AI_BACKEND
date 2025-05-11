from fastapi import Header, HTTPException
from utils.config import env_config
from utils.logger import logger

async def verify_api_key(api_key: str = Header(...)):
    if api_key != env_config.APP_API_KEY:
        logger.warning(f"Invalid API key provided: {api_key}")
        raise HTTPException(status_code=401, detail="Invalid API key")
    logger.info(f"API key verified successfully.")