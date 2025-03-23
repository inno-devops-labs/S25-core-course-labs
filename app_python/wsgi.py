from app import app as application
from app import VISITS_FILE
import os

if not os.path.exists(VISITS_FILE):
    with open(VISITS_FILE, "w") as f:
        f.write("0")

if __name__ == "__main__":
    application.run()