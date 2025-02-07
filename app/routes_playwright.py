from fastapi import APIRouter, HTTPException, Depends, Query
from pydantic import BaseModel

import json
from .logger_config import logger
from .play_sup import play_sync_screenshot, play_sync_index_title, play_async_screenshot
# Create a router for the cards endpoints
router = APIRouter()

class ScreenshotRequest(BaseModel):
    endpoint: str
    protocol: str
    sut_ip: str
    sut_port: str
    browsers: list

# Endpoint to create a screenshot
@router.post("/screenshot")
def screenshot(request: ScreenshotRequest):
    endpoint = request.endpoint
    sut_ip = request.sut_ip
    sut_port = request.sut_port
    browsers = request.browsers
    protocol = request.protocol
    if endpoint == None:
        URL = f"{protocol}://{sut_ip}:{sut_port}"
    else:
        URL = f"{protocol}://{sut_ip}:{sut_port}/{endpoint}"
        
    if not URL or not browsers:
        logger.error(f"endpoint screenshot URL: {URL} browsers: {browsers}")
        raise HTTPException(status_code=400, detail="Missing url or browsers")
    filenames = play_sync_screenshot(URL, browsers)
    return {"filenames": filenames}
