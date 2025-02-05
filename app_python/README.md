# Moscow Time Web App

## Overview
This is a simple Python web application using **Flask** that displays the **current time in Moscow**. The time updates each time the page is refreshed.

## Installation Guide

### Prerequisites
- Python 3 installed
- `pip` installed

### Steps to Run Locally
1. Clone this repository:
   ```bash
    https://github.com/SuleimanKarimEddin/S25-core-course-labs/tree/master
    cd S25-core-course-labs
    git checkout lab1
    cd app_python
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    python app.py 
    docker build -t suleimankrimeddin/app_python:latest .
   ```

# My Flask Time Application

This application displays the current time in Moscow.

## Features
- Displays current Moscow time using Flask and pytz.
- Tested using pytest to ensure routes work as expected.

## Unit Tests

We use [pytest](https://docs.pytest.org/en/latest/) for unit testing. To run the tests locally, install the requirements and then execute:

```bash
pip install -r requirements.txt
pytest
