from fastapi import APIRouter, Request
from app.controllers.time_controller import get_moscow_time_page
from app.utils.count_visits import get_visit_count, update_visit_count

router = APIRouter()


@router.get("/time")
def moscow_time(request: Request):
    """Moscow Time web page endpoint"""
    count = get_visit_count()
    count += 1
    update_visit_count(count)
    return get_moscow_time_page(request)
