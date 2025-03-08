from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from datetime import datetime
import pytz
import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

router = APIRouter()

from pathlib import Path

# using relative pathes (thanks to pytest)
BASE_DIR = Path(__file__).resolve().parent.parent

VISITS_DIR = Path('/app/app/visits')
VISITS_FILE = VISITS_DIR / "visits_count.txt"

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

logger.debug(f"Visits directory: {VISITS_DIR}")
logger.debug(f"Visits file path: {VISITS_FILE}")
logger.debug(f"Directory exists? {os.path.exists(VISITS_DIR)}")
logger.debug(f"Directory is writable? {os.access(VISITS_DIR, os.W_OK)}")

def get_visit_count():
    """Get the current visit count from the file"""
    logger.debug(f"Getting visit count from {VISITS_FILE}")
    if not os.path.exists(VISITS_FILE):
        logger.debug("File does not exist, returning 0")
        return 0
    
    try:
        with open(VISITS_FILE, "r") as f:
            content = f.read().strip()
            result = int(content) if content else 0
            logger.debug(f"Read visit count: {result}")
            return result
    except (IOError, ValueError) as e:
        logger.error(f"Error reading visit count: {e}")
        return 0

def increment_visit_count():
    """Increment the visit count and save it to the file"""
    count = get_visit_count() + 1
    logger.debug(f"Incrementing visit count to {count}")
    
    try:
        with open(VISITS_FILE, "w") as f:
            f.write(str(count))
            logger.debug(f"Wrote visit count {count} to file")
        return count
    except IOError as e:
        logger.error(f"Error writing visit count: {e}")
        return count

@router.get("/")
async def root(request: Request):
    """Default page with the current MSK time (UTC+3)"""
    # Increment the visit counter
    logger.debug("Root endpoint called, incrementing visit count")
    visit_count = increment_visit_count()
    
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%H:%M:%S')
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "moscow_time": moscow_time, "visit_count": visit_count}
    )

@router.get("/time")
async def get_time():
    """Returns the current MSK time (UTC+3)"""
    moscow_tz = pytz.timezone('Europe/Moscow')
    return {"time": datetime.now(moscow_tz).strftime('%H:%M:%S')}

@router.get("/visits")
async def get_visits():
    """Returns the current number of visits"""
    logger.debug("Visits endpoint called")
    visit_count = get_visit_count()
    return {"visits": visit_count}