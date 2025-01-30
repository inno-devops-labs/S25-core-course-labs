from flask import Flask

from services.get_time_service import GetTimeService

from config import TIMEZONE_NAME

app = Flask(__name__)


@app.get("/")
def get_time():
    """Shows the time in the timezone specified in configuration file (currently Moscow)"""
    return GetTimeService.get_time_by_timezone(TIMEZONE_NAME)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
