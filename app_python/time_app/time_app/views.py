from django.http import HttpResponse
from datetime import datetime
import pytz


def moscow_time(request):
    moscow_timezone = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_timezone).strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"<h1>Current Time in Moscow: {current_time}</h1>")
