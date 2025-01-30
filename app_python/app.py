import http.server
import socketserver
from datetime import datetime, timezone, timedelta
import json

PORT = 8000

# Moscow is UTC+3
MOSCOW_TZ = timezone(timedelta(hours=3))


class MoscowTimeAPIHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        moscow_time = datetime.now(MOSCOW_TZ).strftime("%Y-%m-%d %H:%M:%S")
        response = {"moscow_time": moscow_time}
        self.wfile.write(json.dumps(response).encode("utf-8"))


def main():
    with socketserver.TCPServer(("", PORT), MoscowTimeAPIHandler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
