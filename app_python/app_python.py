from datetime import datetime
from fastapi.responses import HTMLResponse
import os


def create_time_string(timezone) -> str:
    now = datetime.now(timezone)
    return now.strftime("%H:%M:%S")


def create_time_response(time_string: str) -> HTMLResponse:
    html_content = f"""
    <!doctype html>
    <html>
        <head>
            <title>Time in Moscow</title>
        </head>
        <body>
            <p>Current time in Moscow is:</p>
            <p>{time_string}</p>
        </body>
    </html>
    """

    return HTMLResponse(content=html_content, status_code=200)


def create_visit_response(visit_count: int) -> HTMLResponse:
    html_content = f"""
    <!doctype html>
    <html>
        <head>
            <title>Time in Moscow</title>
        </head>
        <body>
            <p>Visit count is:</p>
            <p>{visit_count}</p>
        </body>
    </html>
    """

    return HTMLResponse(content=html_content, status_code=200)


VISITS_FILE_PATH = "visits"


def get_visit_count() -> int:
    if not os.path.exists(VISITS_FILE_PATH):
        with open(VISITS_FILE_PATH, "w") as file:
            file.write("0")

    with open(VISITS_FILE_PATH, "r") as file:
        return int(file.read())


def increment_visit_count():
    count = get_visit_count() + 1
    with open(VISITS_FILE_PATH, "w") as file:
        file.write(str(count))
