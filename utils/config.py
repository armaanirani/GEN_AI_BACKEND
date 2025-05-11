from dotenv import load_dotenv
load_dotenv()

from pathlib import Path
import json
from pydantic_settings import BaseSettings
from utils.logger import logger

# Path to config file in root directory
CONFIG_PATH = Path(__file__).resolve().parent.parent / "config.json"

# Load config file
try:
    with open(CONFIG_PATH) as f:
        app_config = json.load(f)
        logger.info(f"Loaded app config from config.json successfully.")
except FileNotFoundError:
    logger.error(f"Config file not found at {CONFIG_PATH}.")
    raise
except json.JSONDecodeError as e:
    logger.exception(f"Invalid JSON format in config.json: {e}")
    raise
except Exception as e:
    logger.exception(f"Unexpected error while loading config.json.")
    raise

# Pydantic environment settings
class AppConfig(BaseSettings):
    GROQ_API_KEY: str
    OPENAI_API_KEY: str
    APP_API_KEY: str

    class Config:
        env_file = ".env"

try:
    env_config = AppConfig()
    logger.info(f"Loaded environment variables successfully from .env file.")
except Exception as e:
    logger.exception(f"Error loading environment variables with Pydantic.")
    raise