from fastapi import FastAPI
from datetime import datetime
import pytz
import os

app = FastAPI()

# File to store visit count
VISITS_FILE = "visits"

def get_visit_count():
    """Get the current visit count from the file."""
    try:
        if os.path.exists(VISITS_FILE):
            with open(VISITS_FILE, "r") as f:
                return int(f.read().strip() or "0")
        return 0
    except Exception:
        return 0

def save_visit_count(count):
    """Save the visit count to the file."""
    try:
        with open(VISITS_FILE, "w") as f:
            f.write(str(count))
    except Exception as e:
        print(f"Error saving visit count: {e}")

@app.get("/time")
def get_time():
    # Increment visit counter
    count = get_visit_count() + 1
    save_visit_count(count)
    
    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_tz)
    return {"time": moscow_time.strftime("%H:%M:%S")}

@app.get("/visits")
def get_visits():
    """Return the current visit count."""
    count = get_visit_count()
    return {"visits": count}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
