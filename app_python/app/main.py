from fastapi import FastAPI
from prometheus_client import generate_latest, REGISTRY
from prometheus_client.exposition import CONTENT_TYPE_LATEST
from starlette.responses import Response
import time

from app.routes.time_routes import router as time_router
from app.middlewares.prometheus_middleware import PrometheusMiddleware
from app.utils.count_visits import get_visit_count, update_visit_count

app = FastAPI()

# Include the time router
app.include_router(time_router)

app.add_middleware(PrometheusMiddleware)

@app.get("/")
def read_root():
    count = get_visit_count()
    count += 1
    update_visit_count(count)
    return {"message": "Lab1 Moscow Time API"}

@app.get("/metrics")
def metrics():
    """Expose Prometheus metrics."""
    return Response(content=generate_latest(REGISTRY), media_type=CONTENT_TYPE_LATEST)

@app.get('/visits')
def visits():
    return {'visits': get_visit_count()}
