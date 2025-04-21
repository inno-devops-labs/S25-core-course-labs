"""
This module defines a FastAPI application with the following features:
1. A root endpoint ("/") that serves an HTML template displaying the current time.
2. Static files served from the "static" directory.
3. HTML templates rendered using Jinja2 from the "templates" directory.
4. A counter to track the number of visits, saved in a file.
5. An endpoint "/visits" to display the visit count.

Author: Sviatoslav Sviatkin (s.sviatkin@innopolis.university)
"""

import os
from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from prometheus_fastapi_instrumentator import Instrumentator
from starlette.responses import JSONResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

Instrumentator().instrument(app).expose(app)

VISITS_FILE = "/data/visits.txt"


def visit():
    """Increments visits count of root handler"""
    if not os.path.isfile(VISITS_FILE):
        with open(VISITS_FILE, "w") as file:
            file.write("0")
    with open(VISITS_FILE, "r") as file:
        v = int(file.read())
    with open(VISITS_FILE, "w") as file:
        file.write(str(v + 1))


@app.get("/visits", response_class=JSONResponse)
async def get_visits():
    with open(VISITS_FILE, "r") as file:
        return JSONResponse(content={"visits": int(file.read())})



@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Handle the root endpoint ("/") to render an HTML page displaying
    the current time and increment the visit counter.

    The current time is calculated based on a timezone with a UTC offset of +3 hours (Moscow).

    Args:
        request (Request): The incoming HTTP request object.

    Returns:
        TemplateResponse: An HTML response rendered using the "item.html" template
        with the current time passed to the template context.
    """
    visit()

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
