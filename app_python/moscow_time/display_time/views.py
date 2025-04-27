from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os
import datetime 

VISITS_FILE = os.getenv('VISITS_FILE', os.path.join(os.path.dirname(settings.BASE_DIR), 'data', 'visits'))


def show_time(request):
    return render(request, "time_display.html")


def visits(request):
    try:
        if os.path.exists(VISITS_FILE):
            with open(VISITS_FILE, 'r') as f:
                count = f.read().strip()
            return HttpResponse(f"Total Visits: {count}")
        else:
            return HttpResponse("No visits recorded yet.")
    except Exception as e:
        return HttpResponse(f"Error reading visits: {e}")