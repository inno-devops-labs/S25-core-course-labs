from django.shortcuts import render


def show_time(request):
    return render(request, "time_display.html")
