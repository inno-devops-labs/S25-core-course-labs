import json
import os
import sys
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.responses import Response
from prometheus_fastapi_instrumentator import Instrumentator
from datetime import datetime
import pytz
import logging


VISITS_FILE = "/data/visits.txt"

log_formatter = logging.Formatter(json.dumps({
    "level": "%(levelname)s",
    "message": "%(message)s"
}))

log_file_handler = logging.FileHandler("/var/log/app_logs/python_app.log")
log_file_handler.setFormatter(log_formatter)

log_console_handler = logging.StreamHandler(sys.stdout)
log_console_handler.setFormatter(log_formatter)

logging.basicConfig(
    level=logging.INFO,
    handlers=[log_file_handler, log_console_handler]
)

logger = logging.getLogger(__name__)

app = FastAPI()

Instrumentator().instrument(app).expose(app, endpoint="/metrics")

MOSCOW_TZ = pytz.timezone("Europe/Moscow")

@app.get("/health")
async def health_check():
    return Response(status_code=200)

@app.get("/", response_class=HTMLResponse)
def get_moscow_time():
    visit_count = read_visits() + 1
    write_visits(visit_count)
    
    moscow_time = datetime.now(MOSCOW_TZ).strftime("%d.%m.%Y %H:%M:%S")
    logger.info(f"Moscow Time API called, current time: {moscow_time}")

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Moscow Time</title>
        <style>
            body {{
                text-align: center;
            }}
            h1 {{
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }}
            p {{
                font-size: 1.2rem;
            }}
        </style>
    </head>
    <body>
        <h1>Current Time in Moscow</h1>
        <p>{moscow_time}</p>
        <p>Refresh to update the time.</p>
    </body>
    </html>
    """
    return html_content


def read_visits():
    """Read the visit count from the file."""
    if not os.path.exists(VISITS_FILE):
        return 0
    try:
        with open(VISITS_FILE, "r") as f:
            return int(f.read().strip())
    except ValueError:
        return 0

def write_visits(count):
    """Write the updated visit count to the file."""
    with open(VISITS_FILE, "w") as f:
        f.write(str(count))


@app.get("/visits")
def get_visits():
    """Endpoint to retrieve the visit count."""
    visit_count = read_visits()
    return {"visits": visit_count}