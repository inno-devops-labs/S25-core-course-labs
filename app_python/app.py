from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn
from zoneinfo import ZoneInfo
from datetime import datetime
from prometheus_fastapi_instrumentator import Instrumentator
import os

app = FastAPI()

# Add visit counter functionality
VISITS_FILE = "data/visits"


def read_visits():
    try:
        with open(VISITS_FILE, "r") as f:
            return int(f.read().strip() or "0")
    except (FileNotFoundError, ValueError):
        return 0


def save_visits(count):
    with open(VISITS_FILE, "w") as f:
        f.write(str(count))


class TimeProvider:
    def get_current_time(self, timezone: str = "Europe/Moscow") -> datetime:
        return datetime.now(ZoneInfo(timezone))


time_provider = TimeProvider()


@app.get("/")
def get_msc_time(request: Request):
    # Increment visit counter
    visits = read_visits() + 1
    save_visits(visits)

    now = time_provider.get_current_time().strftime("%Y-%m-%d %H:%M:%S")
    if request.headers.get("user-agent") and "Mozilla" in request.headers.get(
        "user-agent", ""
    ):
        return HTMLResponse(
            content=f"<h1 style='text-align: center; font-family: Arial, sans-serif; font-weight: bold;'>Time in Moscow: {now}</h1>"
        )
    else:
        return {"time": now}


@app.get("/visits")
def get_visits():
    visits = read_visits()
    return {"visits": visits}


instrumentator = Instrumentator().instrument(app)


@app.on_event("startup")
async def _startup():
    instrumentator.expose(app)


if __name__ == "__main__":
    if not os.path.exists("data"):
        os.mkdir("data")
    uvicorn.run(app, host="0.0.0.0", port=8000)
