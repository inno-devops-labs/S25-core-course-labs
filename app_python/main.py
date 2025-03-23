from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from datetime import datetime
import pytz
from prometheus_client import Counter, make_asgi_app
import os

app = FastAPI(title="Moscow Time App", port=8000)
templates = Jinja2Templates(directory="templates")

# Add prometheus metrics
REQUESTS = Counter('http_requests_total', 'Total HTTP requests')
TIME_REQUESTS = Counter('time_requests_total', 'Total time endpoint requests')

# Add prometheus metrics endpoint
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

VISITS_FILE = os.getenv("VISITS_FILE", "visits.txt")

def increment_visit_counter():
    try:
        if not os.path.exists(VISITS_FILE):
            with open(VISITS_FILE, "w") as f:
                f.write("0")
        with open(VISITS_FILE, "r+") as f:
            count = int(f.read().strip())
            count += 1
            f.seek(0)
            f.write(str(count))
            f.truncate()
        return count
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating visits counter: {str(e)}")

def get_visit_counter():
    try:
        if not os.path.exists(VISITS_FILE):
            return 0
        with open(VISITS_FILE, "r") as f:
            count = int(f.read().strip())
        return count
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading visits counter: {str(e)}")

@app.get("/", response_class=HTMLResponse)
async def get_moscow_time(request: Request):
    try:
        REQUESTS.inc()
        TIME_REQUESTS.inc()
        increment_visit_counter()
        moscow_tz = pytz.timezone('Europe/Moscow')
        moscow_time = datetime.now(moscow_tz)
        formatted_time = moscow_time.strftime("%Y-%m-%d %H:%M:%S %Z")
        return templates.TemplateResponse(
            request,
            "index.html",
            {"formatted_time": formatted_time}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/visits", response_class=PlainTextResponse)
async def visits():
    count = get_visit_counter()
    return f"Total visits: {count}"
