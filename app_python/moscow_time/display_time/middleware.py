import os 
VISITS_FILE = '/app/visits'  # Path inside the Docker container

def visit_counter_middleware(get_response):
    def middleware(request):
        # Read the current count or start at 0
        if os.path.exists(VISITS_FILE):
            with open(VISITS_FILE, 'r') as f:
                count = int(f.read().strip())
        else:
            count = 0
        # Increment the count
        count += 1
        # Save the new count
        with open(VISITS_FILE, 'w') as f:
            f.write(str(count))
        # Attach the count to the request object
        request.visit_count = count
        # Proceed with the request
        response = get_response(request)
        return response
    return middleware