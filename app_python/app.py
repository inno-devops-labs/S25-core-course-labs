'''python web-app program'''
import os
import threading
from datetime import datetime
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import pytz
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import logging  # Import logging

logging.basicConfig(level=logging.INFO)  # Configure basic logging

app = FastAPI(lifespan=lifespan)
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")
# specify the folder with static files
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=TEMPLATES_DIR) # html template folder

REQUEST_COUNT = Counter('http_requests_total', 'Total number of HTTP requests', ['method', 'path'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP request latency in seconds', ['method', 'path'])

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    '''Middleware to collect request metrics'''
    start_time = datetime.now()
    response = await call_next(request)
    process_time = datetime.now() - start_time
    REQUEST_COUNT.labels(method=request.method, path=request.url.path).inc()
    REQUEST_LATENCY.labels(method=request.method, path=request.url.path).observe(process_time.total_seconds())
    return response

COUNTER_FILE = "visits"
counter_lock = threading.Lock()
persistent_counter = 0

def load_counter():
    global persistent_counter
    logging.info("load_counter() called - STARTUP LOGGING") # Add startup logging
    logging.info(f"Environment variables: {os.environ}") # Log environment variables
    try:
        with open(COUNTER_FILE, "r") as f:
            persistent_counter = int(f.read())
    except Exception as e:
        logging.error(f"Error loading counter: {e}") # Log error if loading counter fails
        persistent_counter = 0
    logging.info("load_counter() finished - STARTUP LOGGING") # Add startup logging


def save_counter():
    with open(COUNTER_FILE, "w") as f:
        f.write(str(persistent_counter))

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("lifespan event - STARTUP BEGIN") # Add lifespan startup logging
    load_counter()
    yield
    logging.info("lifespan event - SHUTDOWN") # Add lifespan shutdown logging

@REQUEST_LATENCY.time()
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    '''Displaying Moscow time'''
    logging.info("read_root() called - Request received") # Log when root path is accessed
    timezone = pytz.timezone('Europe/Moscow') # Selecting a time zone
    time = datetime.now(timezone).strftime("%d-%m-%Y %H:%M:%S")
    global persistent_counter
    with counter_lock:
        persistent_counter += 1
        save_counter()
    return templates.TemplateResponse("index.html", {"request": request, "msc_time": time})

@app.get("/metrics")
async def metrics():
    '''Endpoint Prometheus metrics'''
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/visits", response_class=PlainTextResponse)
async def get_visits():
    '''Number of visits'''
    return f"Visits №{persistent_counter}"

if __name__ == "__main__":
    # ip address and port to run the web application
    uvicorn.run(app, host="0.0.0.0", port=int(8000))