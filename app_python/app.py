"""
Main application file. Contains the route information and necessary setups.
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from app_python.app_service import get_time

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def show_time(request: Request):
    return get_time(request)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
