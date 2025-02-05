# Python datetime app

This project is a simple Python web application that displays a static page with the current time in Moscow (at the moment of the response generation). If pinged by curl or other non-browser user agent, it will return a JSON response with the current time in Moscow timezone.

## Installation

```bash
# clone this repo
git clone https://github.com/FallenChromium/
# change the directory name to the app root
cd app_python
# Create a virtual environment
python -m venv .venv
## Linux / macOS
source .venv/bin/activate
## Windows
.venv\Scripts\activate
# install dependencies
pip install -r requirements.txt
```

## Run the app

```bash
uvicorn app:app --port 8000 --reload
```

## Unit tests

Tests are located in the `test.py`. You can run the test suite by executing `pytest test.py -v`.

## Use the app

```bash
curl http://localhost:8000 # or open this url in the browser
```

## Docker

### Pull the image

```bash
docker pull fallenchromium/moscow-timezone-app:latest
```

### Run the image

```bash
docker run -p 8000:8000 fallenchromium/moscow-timezone-app:latest
```

### Build the image

```bash
docker build -t fallenchromium/moscow-timezone-app:latest .
```
