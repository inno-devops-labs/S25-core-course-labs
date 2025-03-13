from django.shortcuts import render
from django.http import HttpResponse

def show_time(request):
    return render(request, "time_display.html")


def visits(request): 
    count = request.visit_count
    
    return HttpResponse(f"Total visits: {count}")