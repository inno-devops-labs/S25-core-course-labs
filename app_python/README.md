[![CI Pipeline](https://github.com/Vitalo-bit/S25-core-course-labs/actions/workflows/ci.yml/badge.svg?branch=lab3)](https://github.com/Vitalo-bit/S25-core-course-labs/actions/workflows/ci.yml)

# Python Web Application

## Overview
This app shows the current time in Moscow. It is built on Python using Flask framework.

## Features
- Displays real-time updates upon page refresh.
- Handles Moscow time zone using `pytz`.
- Containerized solution for consistent execution across environments.
- Automated CI/CD Pipeline with unit testing

## Local Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Vitalo-bit/S25-core-course-labs
   cd app_python
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open the application in your browser: `http://127.0.0.1:5000/`.

## Development Tools
- Flask
- Python 3.8+
- pytz

## Docker Instructions

### Build and Run the Docker Image
1. You can build and run it locally
```bash
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```
2. Or you can pull it from the Docker Hub
```bash
docker pull synavtora/flask-app
docker run -p 5000:5000 synavtora/flask-app
```

## Unit Tests

### Running Tests
To run the unit tests, execute:
```bash
pytest
