from fastapi import FastAPI, Response
from datetime import datetime
import pytz
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import json
import os

app = FastAPI()

VISITS_FILE = "visits"
VISITS_COUNT = 0

def load_visits():
    global VISITS_COUNT
    try:
        if os.path.exists(VISITS_FILE):
            with open(VISITS_FILE, 'r') as f:
                VISITS_COUNT = int(f.read().strip())
    except Exception as e:
        print(f"Error loading visits: {e}")
        VISITS_COUNT = 0

def save_visits():
    try:
        with open(VISITS_FILE, 'w') as f:
            f.write(str(VISITS_COUNT))
    except Exception as e:
        print(f"Error saving visits: {e}")

# Load visits count on startup
load_visits()

REQUEST_COUNT = Counter(
    'app_request_count',
    'Application Request Count',
    ['method', 'endpoint', 'http_status']
)

REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds',
    'Application Request Latency',
    ['method', 'endpoint']
)

@app.middleware("http")
async def metrics_middleware(request, call_next):
    start_time = time.time()
    
    response = await call_next(request)
    
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.url.path,
        http_status=response.status_code
    ).inc()
    
    REQUEST_LATENCY.labels(
        method=request.method,
        endpoint=request.url.path
    ).observe(time.time() - start_time)
    
    return response

@app.get("/")
async def show_time():
    global VISITS_COUNT
    # Increment visits counter
    VISITS_COUNT += 1
    save_visits()
    
    # Set the timezone to Moscow
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return {
        "message": f"The current time in Moscow is: {current_time}",
        "visits": VISITS_COUNT
    }

@app.get("/visits")
async def show_visits():
    return {"total_visits": VISITS_COUNT}

@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
