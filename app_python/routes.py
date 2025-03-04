import datetime
import os

from fastapi import APIRouter

from schemas import TimeResponse, VisitsResponse

time_router = APIRouter(
        prefix="/time",
)

def _incr_visits():
    filename = "visits"
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("0")
    
    with open(filename, "r+") as f:
        visits = int(f.read().strip() or 0)
        visits += 1
        f.seek(0)
        f.write(str(visits))
        f.truncate()
    
    return visits

def total_visits():
    filename = "visits"
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("0")
    
    return _incr_visits()


@time_router.get(
        "",
        description="Get current time with Moscow timezone"
)
def get_time() -> TimeResponse:
    _incr_visits()
    return TimeResponse(
            time=datetime.datetime.now(
                    tz=datetime.timezone(datetime.timedelta(hours=3))
            )
    )

visits_router = APIRouter(
    prefix="/visits"
)


@visits_router.get(
    "",
    description="Get amount of time this app was visited"
)
def get_visits() -> VisitsResponse:
    return VisitsResponse(
        count=total_visits(),
    )

