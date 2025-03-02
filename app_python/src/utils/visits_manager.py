import os

FILE_DIR = '/tmp/app'
FILE_PATH = f'{FILE_DIR}/visits'

def read_visits() -> int:
    os.makedirs(FILE_DIR, exist_ok=True)
    try:
        with open(FILE_PATH, 'r') as file:
            contents = file.read().strip()
            number = int(contents or '0')
            return number
    except FileNotFoundError:
        with open(FILE_PATH, 'w') as file:
            file.write("0")
        return 0

def inc_visits():
    cur = read_visits()
    with open(FILE_PATH, 'w') as file:
        file.write(str(cur + 1))
