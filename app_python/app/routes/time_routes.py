from fastapi import APIRouter, Request
from app.controllers.time_controller import get_moscow_time_page

router = APIRouter()


@router.get("/time")
def moscow_time(request: Request):
    """Moscow Time web page endpoint"""
    return get_moscow_time_page(request)
