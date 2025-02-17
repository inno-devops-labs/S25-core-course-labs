'''python web-app program'''
import os
from datetime import datetime
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import pytz
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI()
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

@REQUEST_LATENCY.time()
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    '''Displaying Moscow time'''
    timezone = pytz.timezone('Europe/Moscow') # Selecting a time zone
    time = datetime.now(timezone).strftime("%d-%m-%Y %H:%M:%S")
    return templates.TemplateResponse(request, "index.html", {"msc_time": time})

@app.get("/metrics")
async def metrics():
    '''Endpoint Prometheus metrics'''
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    # ip address and port to run the web application
    uvicorn.run(app, host="127.0.0.1", port=int(8000))