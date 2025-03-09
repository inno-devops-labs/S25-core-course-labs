"""
Main file for the web application. It includes two endpoints:

- `/` - returns web page containing current time in Moscow
- `/time` - returns current time in Moscow in JSON format
"""

import os
from pathlib import Path
from fastapi import FastAPI, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from prometheus_client import Counter, CONTENT_TYPE_LATEST, REGISTRY, generate_latest
from src.utils import get_time
from src.models import Time


# Create FastAPI application
app = FastAPI(description="""Web application for displaying current time in Moscow.""")


# Load templates from the corresponding directory
templates = Jinja2Templates(directory="src/templates")

# Register metrics
time_page_visits = Counter(
    "time_page_visits",
    "Visits of web page containing current time in Moscow. Bring time to human!",
)

time_json_visits = Counter(
    "time_json_visits",
    "Visits of API endpoint containing current time in Moscow. Bring time to robots!",
)

COUNTER = 0
INITIALIZED = False


def init_counter():
    """Inits counter if not initialized already."""
    global COUNTER, INITIALIZED

    if not os.path.isfile("visits/visits"):
        COUNTER = 0
    else:
        with open("visits/visits", "r", encoding="utf-8") as visits:
            number = visits.read()
            print(number, number.isdigit())
            if number.isdigit():
                COUNTER = int(number)
            else:
                COUNTER = 0
    INITIALIZED = True

    return COUNTER


def increment_counter():
    """Increments visits counter."""
    global COUNTER, INITIALIZED

    if not INITIALIZED:
        COUNTER = init_counter()

    COUNTER += 1
    Path("visits").mkdir(parents=True, exist_ok=True)
    with open("visits/visits", "w", encoding="utf-8") as visits:
        visits.write(str(COUNTER))
        visits.close()


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
    time_page_visits.inc()
    increment_counter()
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
    time_json_visits.inc()
    increment_counter()
    current_time = str(get_time())
    return {"time": current_time}


@app.get(
    "/metrics",
    response_model=None,
    status_code=status.HTTP_200_OK,
    description="""Get latest metrics""",
    tags=["metrics"],
    summary="Returns latest metrics",
    responses={status.HTTP_200_OK: {"description": "Latest metrics"}},
)
async def read_metrics():
    """Returns latest metrics."""
    metrics = generate_latest(registry=REGISTRY)
    return HTMLResponse(metrics, media_type=CONTENT_TYPE_LATEST)


@app.get(
    "/visits",
    response_model=None,
    status_code=status.HTTP_200_OK,
    description="""Get number of times the app accessed""",
    tags=["metrics"],
    summary="Returns number of times the app accessed",
    responses={status.HTTP_200_OK: {"description": "Number of times the app accessed"}},
)
async def read_counter():
    """Returns current counter value."""
    global COUNTER
    return COUNTER
