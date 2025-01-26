from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

def get_moscow_time() -> str:
    try:
        moscow_time = datetime.now(pytz.timezone("Europe/Moscow"))
        return moscow_time.strftime("%H:%M:%S")
    except Exception as e:
        return f"Error: {str(e)}"

@app.get("/")
def read_root() -> dict[str, str]:
    moscow_time = get_moscow_time()
    return {"message": f"The current time in Moscow is {moscow_time}"}
