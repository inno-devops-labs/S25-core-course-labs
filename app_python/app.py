from fastapi import FastAPI
from datetime import datetime
import pytz
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response


app = FastAPI()


@app.get("/")
def moscow_time():
    # Get Moscow time (UTC+3)
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
    return {"Current time in Moscow": current_time}


@app.get("/metrics")
def metrics():
    # Generate Prometheus metrics in the text format
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
