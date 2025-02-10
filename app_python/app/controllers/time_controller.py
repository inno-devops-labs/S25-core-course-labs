from fastapi import Request
from fastapi.templating import Jinja2Templates
from app.utils.time_utils import get_moscow_time

# Initialize templates
templates = Jinja2Templates(directory="app/templates")


def get_moscow_time_page(request: Request):
    """Controller function to get Moscow time and render the template."""
    current_time = get_moscow_time()
    return templates.TemplateResponse(
        request, "moscow_time.html", {"current_time": current_time}
    )
