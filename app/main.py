from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import datetime
from .logger_config import logger
from .routes_playwright import router as routes_playwright  # Import the cards router

app = FastAPI()

start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
logger.info(f"Webserver started at {start_time}")

# Include the cards router
app.include_router(routes_playwright)
