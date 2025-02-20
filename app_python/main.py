"""
This module defines a FastAPI application with the following features:
1. A root endpoint ("/") that serves an HTML template displaying the current time.
2. Static files served from the "static" directory.
3. HTML templates rendered using Jinja2 from the "templates" directory.

Author: Sviatoslav Sviatkin (s.sviatkin@innopolis.university)
"""

from datetime import datetime, timedelta, timezone

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Handle the root endpoint ("/") to render an HTML page displaying the current time.

    The current time is calculated based on a timezone with a UTC offset of +3 hours (Moscow).

    Args:
        request (Request): The incoming HTTP request object.

    Returns:
        TemplateResponse: An HTML response rendered using the "item.html" template
        with the current time passed to the template context.
    """
    zone = timezone(timedelta(hours=3))
    time = datetime.now(timezone.utc).astimezone(zone)

    return templates.TemplateResponse(request, "item.html", {"time": time})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
