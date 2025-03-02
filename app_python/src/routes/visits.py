from fastapi import APIRouter
from src.utils.visits_manager import read_visits


router = APIRouter()

@router.get("/visits")
async def get_visits_number():
    visits = read_visits()
    return {"Visits number": visits}
