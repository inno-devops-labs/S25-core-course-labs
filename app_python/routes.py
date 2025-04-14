import datetime

from fastapi import APIRouter

from schemas import TimeResponse

router = APIRouter(
        prefix="/time",
)


@router.get(
        "",
        description="Get current time with Moscow timezone"
)
def get_time() -> TimeResponse:
    return TimeResponse(
            time=datetime.datetime.now(
                    tz=datetime.timezone(datetime.timedelta(hours=3))
            )
    )
