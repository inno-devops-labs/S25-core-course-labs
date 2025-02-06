from fastapi import APIRouter, Request  # Add Request here
from fastapi.templating import Jinja2Templates

from util import get_current_time

time_operations_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@time_operations_router.get("/current-time/{zone}")
async def display_time(zone: str, request: Request):  # Add request parameter
    """Endpoint to display the current time in a given zone."""
    current_time = get_current_time(zone)

    if current_time == "Invalid zone.":
        return templates.TemplateResponse(
            request,
            "error.html",  # Create an error template
            {"request": request, "message": f"Invalid time zone: {zone}"}
        )

    return templates.TemplateResponse(
        request,
        "index.html",
        {"request": request, "zone": zone, "current_time": current_time}  # Add "request" key
    )
