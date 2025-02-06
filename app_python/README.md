# Python datetime app

This project is a simple Python web application that displays a static page with the current time in Moscow (at the moment of the response generation). If pinged by curl or other non-browser user agent, it will return a JSON response with the current time in Moscow timezone.

## Installation

```bash
# clone this repo
# change the directory name to the app root
cd app_python
# Create a virtual environment
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate
# install dependencies
pip install -r requirements.txt
```

## Run the app

```bash
uvicorn app:app --port 8000 --reload
```

## Use the app

```bash
curl http://localhost:8000
```
