from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn
from zoneinfo import ZoneInfo
from datetime import datetime

app = FastAPI()


class TimeProvider:
    def get_current_time(self, timezone: str = "Europe/Moscow") -> datetime:
        return datetime.now(ZoneInfo(timezone))


time_provider = TimeProvider()


@app.get("/")
def get_msc_time(request: Request):
    now = time_provider.get_current_time().strftime("%Y-%m-%d %H:%M:%S")
    if request.headers.get("user-agent") and "Mozilla" in request.headers.get(
        "user-agent", ""
    ):
        return HTMLResponse(
            content=f"<h1 style='text-align: center; font-family: Arial, sans-serif; font-weight: bold;'>Time in Moscow: {now}</h1>"
        )
    else:
        return {"time": now}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
