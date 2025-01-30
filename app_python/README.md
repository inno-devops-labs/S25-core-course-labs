# Python Web Application

This is a web application that displays the current time in Moscow using FastAPI.

## Installation

   ```bash
   cd app_python
   ```
   ```bash
   # Virtual environment
   python3 -m venv venv
   source venv/bin/activate
   ```
   ```bash
   pip install -r requirements.txt
   ```
## Run

   ```bash
   uvicorn main:app --reload
   ```
Then go to http://localhost:8000/docs#/