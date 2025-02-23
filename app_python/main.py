from fastapi import FastAPI
from datetime import datetime
import uvicorn
import pytz
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()


@app.get("/")
def get_moscow_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return {"current_time_in_moscow": current_time}


Instrumentator().instrument(app).expose(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
