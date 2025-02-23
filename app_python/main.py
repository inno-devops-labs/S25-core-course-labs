from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from datetime import datetime
import pytz
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import make_asgi_app

app = FastAPI(title="Moscow Time App", port=8000)
templates = Jinja2Templates(directory="templates")

# Add prometheus metrics
REQUESTS = Counter('http_requests_total', 'Total HTTP requests')
TIME_REQUESTS = Counter('time_requests_total', 'Total time endpoint requests')

# Add prometheus metrics endpoint
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

@app.get("/", response_class=HTMLResponse)
async def get_moscow_time(request: Request):
    try:
        REQUESTS.inc()
        TIME_REQUESTS.inc()
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
