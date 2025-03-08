from fastapi import FastAPI
from datetime import datetime
import pytz
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Initialize metrics instrumentation
instrumentator = Instrumentator().instrument(app)

# Expose metrics endpoint
instrumentator.expose(app)

@app.get("/time")
def get_time():
    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_tz)
    return {"time": moscow_time.strftime("%H:%M:%S")}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
