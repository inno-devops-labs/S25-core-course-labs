from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
import pytz
from pathlib import Path
import uvicorn
from typing import Dict, Any
from config import settings
from prometheus_client import Counter, Histogram, make_asgi_app
import time
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(title=settings.APP_TITLE)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create templates directory and initialize templates
settings.TEMPLATES_DIR.mkdir(exist_ok=True)
templates = Jinja2Templates(directory=str(settings.TEMPLATES_DIR))

# Add prometheus metrics
REQUEST_COUNT = Counter(
    'app_request_count',
    'Application Request Count',
    ['endpoint', 'method', 'status_code']
)

REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds',
    'Application Request Latency',
    ['endpoint', 'method']
)

# Add prometheus metrics endpoint
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

@app.middleware("http")
async def track_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    latency = time.time() - start_time
    REQUEST_COUNT.labels(endpoint=request.url.path, method=request.method, status_code=response.status_code).inc()
    REQUEST_LATENCY.labels(endpoint=request.url.path, method=request.method).observe(latency)
    return response

def get_formatted_times() -> Dict[str, str]:
    """Get current Moscow time and format it."""
    try:
        moscow_tz = pytz.timezone(settings.TIMEZONE)
        moscow_time = datetime.now(moscow_tz)
        
        return {
            "moscow_time": moscow_time.strftime("%H:%M:%S"),
            "current_time": moscow_time.strftime("%Y-%m-%d %H:%M:%S %Z")
        }
    except pytz.exceptions.PytzError as e:
        raise HTTPException(status_code=500, detail=f"Timezone error: {str(e)}")

@app.get("/", response_class=HTMLResponse)
async def get_moscow_time(request: Request) -> templates.TemplateResponse:
    """
    Endpoint to display the current Moscow time.
    
    Args:
        request: FastAPI request object
    
    Returns:
        TemplateResponse: Rendered HTML template with current time
    """
    times = get_formatted_times()
    template_context = {"request": request, **times}
    return templates.TemplateResponse("index.html", template_context)

@app.get("/get_time")
async def get_time() -> Dict[str, str]:
    """
    API endpoint to get the current Moscow time.
    
    Returns:
        Dict[str, str]: Dictionary containing formatted moscow_time and current_time
    """
    return get_formatted_times()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )