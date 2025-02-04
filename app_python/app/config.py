import os
import sys

from dotenv import load_dotenv

DEFAULT_ENV_FILE = '.env'


class Config:
    """
    Config class with necessary variables for the program startup & runtime
    """
    DEBUG = os.environ.get('DEBUG', 'False')
    PORT = os.environ.get('PORT', '5000')


def load_environment():
    dotenv_path = DEFAULT_ENV_FILE

    if len(sys.argv) > 1:
        dotenv_path = sys.argv[1]

    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
        print(f"Variables properly fetched from the next .env file: {dotenv_path}")
    else:
        print(f".env file {dotenv_path} not found. Falling back to the default ones...")
        load_dotenv(DEFAULT_ENV_FILE)


load_environment()
