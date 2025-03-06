from fastapi import FastAPI
from datetime import datetime
import pytz
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
import os


app = FastAPI()

VISITS_FILE = "/data/visits"


def get_visit_count():
    """Read the current visit count from the file."""
    try:
        with open(VISITS_FILE, "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 0


def increment_visit_count():
    """Increment the visit count and save to the file."""
    count = get_visit_count() + 1
    os.makedirs(os.path.dirname(VISITS_FILE), exist_ok=True)  # Ensure directory exists
    with open(VISITS_FILE, "w") as f:
        f.write(str(count))
    return count


@app.get("/")
def moscow_time():
    increment_visit_count()
    # Get Moscow time (UTC+3)
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
    return {"Current time in Moscow": current_time}


@app.get("/visits")
def get_visits():
    """Return the current visit count."""
    count = get_visit_count()
    return {"visits": count}

@app.get("/metrics")
def metrics():
    # Generate Prometheus metrics in the text format
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
