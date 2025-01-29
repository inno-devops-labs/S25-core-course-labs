# Python Web Application: Moscow Time

## Overview
This is a simple Python web application that displays the current time in Moscow. The application is built using FastAPI with Python 3.12+ based on standard Python type hints.

## Features
- Displays the current time in Moscow.
- Automatically updates the time upon page refresh.
- Interactive API documentation provided by FastAPI.

## Installation
To run this application locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Fridorovich/S25-core-course-labs/tree/lab1/app_python.git
    cd app_python
2. **Set up a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
4. **Run the application**:
    ```bash
    uvicorn main:app --reload
5. **Access the application**:
    Open your browser and go to http://127.0.0.1:8000/.