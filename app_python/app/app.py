from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
import pytz
import logging
import uvicorn
import os

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
)

app = FastAPI()

# Serve static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

VISITS_FILE = "visits"

def get_visit_count():
    try:
        with open(VISITS_FILE, "r") as f:
            return int(f.read().strip() or "0")
    except (FileNotFoundError, ValueError):
        return 0

def save_visit_count(count):
    with open(VISITS_FILE, "w") as f:
        f.write(str(count))

# Custom exception handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logging.error(f"HTTPException: {exc.detail} (status_code={exc.status_code})")
    return templates.TemplateResponse(
        "error.html",
        {"request": request, "status_code": exc.status_code, "detail": exc.detail},
        status_code=exc.status_code,
    )


# Root route to display the current time in Moscow
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    try:
        # Get the current time in Moscow
        moscow_timezone = pytz.timezone("Europe/Moscow")
        current_time = datetime.now(moscow_timezone).strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"Displaying current time in Moscow: {current_time}")
        
        # Update visit counter
        count = get_visit_count() + 1
        save_visit_count(count)
        
        return templates.TemplateResponse(
            "index.html", {"request": request, "time": current_time}
        )
    except Exception as e:
        logging.error(f"Error in root: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


# Custom 404 error handler
@app.exception_handler(404)
async def not_found_handler(request: Request, exc: HTTPException):
    logging.warning(f"404 Not Found: {request.url}")
    return templates.TemplateResponse(
        "error.html",
        {
            "request": request,
            "status_code": 404,
            "detail": "The page you are looking for does not exist.",
        },
        status_code=404,
    )


@app.get("/visits", response_class=HTMLResponse)
async def visits(request: Request):
    count = get_visit_count()
    return templates.TemplateResponse(
        "visits.html", {"request": request, "count": count}
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
