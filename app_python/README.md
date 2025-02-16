# Python datetime app

![test workflow](https://github.com/FallenChromium/s25-core-course-labs/actions/workflows/app_python.yaml/badge.svg)

This project is a simple Python web application that displays a static page with the current time in Moscow (at the moment of the response generation). If pinged by curl or other non-browser user agent, it will return a JSON response with the current time in Moscow timezone.

## Installation

```bash
# clone this repo
git clone https://github.com/FallenChromium/S25-core-course-labs.git
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

## Use the app

```bash
curl http://localhost:8000 # or open this url in the browser
```

## Unit tests

Tests are located in the `test.py`.
To run them, you first need to install the dev dependencies of the project by running `pip install -r requirements.dev.txt`.
Then you can run the test suite by executing `pytest test.py -v`.

## Continuous Integration

This repo uses GitHub Actions to test and lint the app code on pull requests (see `.github/workflows/` folder). Make sure to use `ruff check .` and `ruff format .` before submitting a pull request. An action to build and push the Docker image to Docker Hub is also available but currently can be only run manually.

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
