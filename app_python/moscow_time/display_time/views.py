from django.shortcuts import render
from django.http import HttpResponse

def show_time(request):
    return render(request, "time_display.html")

