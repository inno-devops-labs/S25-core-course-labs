# Python Web Application

This is a web application that displays the current time in Moscow using FastAPI.

### Installation

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
### Run

   ```bash
   uvicorn main:app --reload
   ```
Then go to http://localhost:8000/docs#/

## Docker

### Build

   ```bash
   cd app_python
   ```
   ```bash
   docker build -t python-web-app .
   ```

### Pull & Run

   ```bash
   docker pull netpo4ki/python-web:latest
   ```
   ```bash
   docker run -d -p 8000:8000 netpo4ki/python-web:latest
   ```
Then go to http://localhost:8000/docs#/

## Unit Tests

   ```bash
   cd app_python
   ```
   ```bash
   pytest test_main.py
   ```

![CI Status](https://github.com/NetPo4ki/S25-core-course-labs/actions/workflows/ci.yml/badge.svg)