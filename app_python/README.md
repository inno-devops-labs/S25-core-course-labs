# Moscow Time Web Application

![CI Pipeline](https://github.com/tolmachdr/S25-core-course-labs/actions/workflows/python_app_ci.yml/badge.svg?branch=lab3)

This is a Python web application built with FastAPI that displays the current time in Moscow.

## Application setup

1. Clone the repo
```
git clone https://github.com/tolmachdr/S25-core-course-labs -b lab1
```
2. Setup virtual environment
```aiignore
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```
3. Go to the folder and run the app
```aiignore
cd app_python
uvicorn main:app --reload
```

## Docker 

To run this application you also can use docker, for this you need to:

1. Build image
```
docker build -t python-app .
```

2. Run the container
```aiignore
docker run -p 8000:8000 python-app
```

OR

1. Pull existing image from dockerhub
```aiignore
docker pull dtolmach/python-app:latest
```
2. Run the container
```aiignore
docker run -p 8000:8000 python-app
```

## Unit tests

You can test the application using
```aiignore
pytest test_app.py
```

## CI

The project uses GitHub Actions for continuous integration. The workflow includes:

1. Installs required Python libraries

2. `flake8` checks for code style issues

3. `pytest` tests API 

4. `Snyk` detects and reports vulnerabilities

5. Builds and pushes the image to Docker Hub
