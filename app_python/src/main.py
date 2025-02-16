"""
Main file for the web application. It includes two endpoints:

- `/` - returns web page containing current time in Moscow
- `/time` - returns current time in Moscow in JSON format
"""

from fastapi import FastAPI, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from utils import get_time
from models import Time


# Create FastAPI application
app = FastAPI(description="""Web application for displaying current time in Moscow.""")


# Load templates from the corresponding directory
templates = Jinja2Templates(directory="src/templates")


@app.get(
    "/",
    response_class=HTMLResponse,
    status_code=status.HTTP_200_OK,
    description="""Get web page containing current time in Moscow""",
    tags=["time"],
    summary="Returns web page containing current time in Moscow",
    responses={
        status.HTTP_200_OK: {
            "description": "The web page containing current time in Moscow"
        }
    },
)
async def read_time(request: Request):
    """Returns web page containing current time in Moscow."""
    current_time = get_time().strftime("%d.%m.%Y %H:%M:%S")
    return templates.TemplateResponse(
        request=request, name="time.html", context={"time": current_time}
    )


@app.get(
    "/time",
    response_model=Time,
    status_code=status.HTTP_200_OK,
    description="""Get current time in Moscow""",
    tags=["time"],
    summary="Returns current time in Moscow",
    responses={
        status.HTTP_200_OK: {"model": Time, "description": "Current time in Moscow"}
    },
)
async def read_time_json():
    """Returns current time in Moscow in JSON format."""
    current_time = str(get_time())
    return {"time": current_time}
