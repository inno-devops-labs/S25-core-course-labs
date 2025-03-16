import os

visits_file = 'visits'

def get_visit_count():
    if not os.path.exists(visits_file):
        return 0
    with open(visits_file, 'r') as f:
        return int(f.read().strip() or 0)

def update_visit_count(count):
    with open(visits_file, 'w') as f:
        f.write(str(count))