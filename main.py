from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from app.api import routes as api_routes
from utils.config import app_config
from utils.logger import logger
import uvicorn

app = FastAPI(title="LLM API")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (All domains can access this site currently i.e. "*")
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
logger.info("CORS middleware added.")

# Include API routes
app.include_router(api_routes.router)
logger.info("API routes included.")

# Start the server
if __name__ == "__main__":
    host = app_config.get("api", {}).get("host", "localhost")
    port = app_config.get("api", {}).get("port", 8000)
    logger.info(f"Starting the server at http://{host}:{port}/")
    
    uvicorn.run("main:app", host=host, port=port, reload=True)