"""
This module defines a FastAPI application with the following features:
1. A root endpoint ("/") that serves an HTML template displaying the current time.
2. Static files served from the "static" directory.
3. HTML templates rendered using Jinja2 from the "templates" directory.
4. A counter to track the number of visits, saved in a file.
5. An endpoint "/visits" to display the visit count.

Author: Sviatoslav Sviatkin (s.sviatkin@innopolis.university)
"""

from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

Instrumentator().instrument(app).expose(app)

VISITS_FILE = "visits.txt"

def read_visits() -> int:
    try:
        with open(VISITS_FILE, "r") as file:
            content = file.read().strip()
            return int(content) if content else 0
    except (FileNotFoundError, ValueError):
        return 0

def write_visits(count: int) -> None:
    with open(VISITS_FILE, "w") as file:
        file.write(str(count))

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Handle the root endpoint ("/") to render an HTML page displaying the current time and increment the visit counter.

    The current time is calculated based on a timezone with a UTC offset of +3 hours (Moscow).

    Args:
        request (Request): The incoming HTTP request object.

    Returns:
        TemplateResponse: An HTML response rendered using the "item.html" template
        with the current time passed to the template context.
    """
    # Increment visit counter
    current_visits = read_visits()
    current_visits += 1
    write_visits(current_visits)

    # Get current time
    zone = timezone(timedelta(hours=3))
    time = datetime.now(timezone.utc).astimezone(zone)

    return templates.TemplateResponse(request, "item.html", {"time": time})

@app.get("/visits")
async def get_visits():
    """
    Endpoint to retrieve the current number of visits.

    Returns:
        dict: A JSON object containing the visit count.
    """
    visits = read_visits()
    return {"visits": visits}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)