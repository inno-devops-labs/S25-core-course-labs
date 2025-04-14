from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/")
def get_moscow_time():
    moscow_time = datetime.now(pytz.timezone("Europe/Moscow"))
    return {"current_time": moscow_time.strftime("%Y-%m-%d %H:%M:%S")}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
