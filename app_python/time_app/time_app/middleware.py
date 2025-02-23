from django.http import HttpResponseBadRequest
from django.utils.deprecation import MiddlewareMixin

class AllowPrometheusMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/metrics/':
            return None
        return super().process_request(request)