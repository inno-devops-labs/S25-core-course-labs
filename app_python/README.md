[![Python application](https://github.com/favelanky/S25-core-course-labs/actions/workflows/python-app.yml/badge.svg?branch=lab3)](https://github.com/favelanky/S25-core-course-labs/actions/workflows/python-app.yml)

# Python Web App (Flask)
## Overview
A simple Flask web application that displays the current time in Moscow.

## Installation
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Unit Tests
To run the unit tests, execute the following command:

```bash
python -m unittest test_app.py
```

## Docker

### Build the Docker Image
To build the Docker image, run:
```
docker build -t favelanky/app_python .
docker pull favelanky/app_python
docker run favelanky/app_python
```

