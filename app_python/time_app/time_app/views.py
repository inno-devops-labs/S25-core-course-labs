from django.http import HttpResponse
from datetime import datetime
import pytz
from prometheus_client import generate_latest, REGISTRY
from prometheus_client.exposition import basic_auth_handler


def moscow_time(request):
    moscow_timezone = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_timezone).strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"<h1>Current Time in Moscow: {current_time}</h1>")

def metrics_view(request):
   
    metrics_data = generate_latest(REGISTRY)
    return HttpResponse(metrics_data, content_type="text/plain; version=0.0.4; charset=utf-8")