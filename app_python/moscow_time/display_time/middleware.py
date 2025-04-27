import os
from django.conf import settings

VISITS_FILE = os.getenv('VISITS_FILE', os.path.join(os.path.dirname(settings.BASE_DIR), 'data', 'visits'))

def visit_counter_middleware(get_response):
    def middleware(request):
        if request.path != '/visits':
            try:
                os.makedirs(os.path.dirname(VISITS_FILE), exist_ok=True)
                
                if os.path.exists(VISITS_FILE):
                    with open(VISITS_FILE, 'r') as f:
                        content = f.read().strip()
                        count = int(content) if content else 0
                else:
                    count = 0
                
                count += 1
                
                with open(VISITS_FILE, 'w') as f:
                    f.write(str(count))
            except Exception as e:
                print(f"Error updating visits: {e}")

        response = get_response(request)
        return response

    return middleware
