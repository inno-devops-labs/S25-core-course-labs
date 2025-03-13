'''python web-app program -  максимально упрощенная синхронная версия без lifespan'''
import os
import threading
from datetime import datetime
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import pytz
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI() # Убрали lifespan
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

REQUEST_COUNT = Counter('http_requests_total', 'Total number of HTTP requests', ['method', 'path'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP request latency in seconds', ['method', 'path'])

@app.middleware("http")
async def metrics_middleware(request: Request, call_next): # Оставляем middleware асинхронным, так как это middleware FastAPI
    start_time = datetime.now()
    response = await call_next(request)
    process_time = datetime.now() - start_time
    REQUEST_COUNT.labels(method=request.method, path=request.url.path).inc()
    REQUEST_LATENCY.labels(method=request.method, path=request.url.path).observe(process_time.total_seconds())
    return response

COUNTER_FILE = "/tmp/visits"
counter_lock = threading.Lock()
persistent_counter = 0

def load_counter(): # Синхронная функция
    global persistent_counter
    try:
        with open(COUNTER_FILE, "r") as f:
            persistent_counter = int(f.read())
    except Exception:
        persistent_counter = 0

def save_counter(): # Синхронная функция
    with open(COUNTER_FILE, "w") as f:
        f.write(str(persistent_counter))

load_counter() # Загружаем счетчик сразу при запуске модуля, вне lifespan

@REQUEST_LATENCY.time()
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request): # Синхронная функция - убрали async
    '''Displaying Moscow time'''
    timezone = pytz.timezone('Europe/Moscow') # Selecting a time zone
    time = datetime.now(timezone).strftime("%d-%m-%Y %H:%M:%S")
    global persistent_counter
    with counter_lock:
        persistent_counter += 1
        save_counter()
    return templates.TemplateResponse("index.html", {"request": request, "msc_time": time})

@app.get("/metrics")
async def metrics(): # Оставляем metrics endpoint асинхронным, так как это рекомендуется для Prometheus client
    '''Endpoint Prometheus metrics'''
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/visits", response_class=PlainTextResponse)
def get_visits(): # Синхронная функция - убрали async
    '''Number of visits'''
    return f"Visits №{persistent_counter}"

if __name__ == "__main__":
    # ip address and port to run the web application
    uvicorn.run(app, host="127.0.0.1", port=int(8000))