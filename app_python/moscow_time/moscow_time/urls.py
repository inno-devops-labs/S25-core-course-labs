"""
URL configuration for moscow_time project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from prometheus_client import start_http_server, REGISTRY, MetricsHandler

# Define a custom metrics view
def metrics_view(request):
    from prometheus_client.exposition import generate_latest
    return HttpResponse(generate_latest(REGISTRY), content_type='text/plain')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('display_time.urls')), 
    path('metrics', metrics_view),
]
