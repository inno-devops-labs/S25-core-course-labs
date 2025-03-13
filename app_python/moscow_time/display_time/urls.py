from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_time, name="moscow_time"),
    
    path('visits/', views.visits, name='visits'),
]
