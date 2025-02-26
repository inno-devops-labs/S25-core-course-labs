from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

# Prometheus Counter
from prometheus_client import Counter

from util import get_current_time

time_operations_router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Create a Prometheus Counter: "time_zone_requests_total"
# Label: "zone"
TIME_ZONE_REQUEST_COUNT = Counter(
    "time_zone_requests_total",
    "Number of time zone requests made",
    ["zone"]
)

@time_operations_router.get("/current-time/{zone}")
async def display_time(zone: str, request: Request):
    """
    Endpoint to display the current time in a given zone.
    Increments the TIME_ZONE_REQUEST_COUNT for each request.
    """

    # Increment the counter for this zone
    TIME_ZONE_REQUEST_COUNT.labels(zone=zone).inc()

    current_time = get_current_time(zone)
    if current_time == "Invalid zone.":
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "message": f"Invalid time zone: {zone}"}
        )

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "zone": zone, "current_time": current_time}
    )
