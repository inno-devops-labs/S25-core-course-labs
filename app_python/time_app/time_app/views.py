import os
from django.http import HttpResponse
from datetime import datetime
import pytz
from prometheus_client import generate_latest, REGISTRY
from prometheus_client.exposition import basic_auth_handler


VISITS_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'visits.txt')

def increment_visits():
    if os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, 'r') as file:
            visits = int(file.read())
    else:
        visits = 0
    
    visits += 1
    
    with open(VISITS_FILE, 'w') as file:
        file.write(str(visits))
    
    return visits

def moscow_time(request):
    visits = increment_visits()
    moscow_timezone = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_timezone).strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"<h1>Current Time in Moscow: {current_time}</h1><p>You are vistor number {visits}.</p>")

def visits(request):
    if os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, 'r') as file:
            visits = file.read()
    else:
        visits = "0"
    
    return HttpResponse(f"<h1>Total Visits: {visits}</h1>")

def metrics_view(request):
   
    metrics_data = generate_latest(REGISTRY)
    return HttpResponse(metrics_data, content_type="text/plain; version=0.0.4; charset=utf-8")
