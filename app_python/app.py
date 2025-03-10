import http.server
import socketserver
from datetime import datetime, timezone, timedelta
import json
from prometheus_client import start_http_server, Counter, Histogram
import time

# Moscow is UTC+3
MOSCOW_TZ = timezone(timedelta(hours=3))

# Prometheus metrics
REQUEST_COUNT = Counter('moscow_time_requests_total', 'Total requests to the Moscow Time API')
REQUEST_DURATION = Histogram('moscow_time_request_duration_seconds', 'Request duration in seconds')

class MoscowTimeAPIHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        REQUEST_COUNT.inc()
        start_time = time.time()
        
        try:
            if self.path == '/health':
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                health_response = {"status": "healthy"}
                self.wfile.write(json.dumps(health_response).encode("utf-8"))
                return

            self.log_message("Request path: %s, method: %s", self.path, self.command)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            moscow_time = datetime.now(MOSCOW_TZ).strftime("%Y-%m-%d %H:%M:%S")
            response = {"moscow_time": moscow_time}
            self.log_message("Response: %s", response)
            self.wfile.write(json.dumps(response).encode("utf-8"))
        finally:
            # Record request duration
            REQUEST_DURATION.observe(time.time() - start_time)


def main(port: int = 8001):
    # Start prometheus metrics server on port 8000
    start_http_server(8000)
    
    # Start the main application server on port 8001
    with socketserver.TCPServer(("", port), MoscowTimeAPIHandler) as httpd:
        print(f"Serving Moscow Time API on port {port}")
        print(f"Serving Prometheus metrics on port 8000")
        httpd.serve_forever()


if __name__ == "__main__":
    print("Starting Moscow Time API server...")
    main()