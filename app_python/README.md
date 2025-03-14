# Python Web Application

[![CI/CD](https://github.com/WellNotWell/DevOps-labs/actions/workflows/app_python.yml/badge.svg?branch=lab-3)](https://github.com/WellNotWell/DevOps-labs/actions/workflows/app_python.yml)

## Overview

This is a simple Python web application that displays the current time in the Moscow timezone.

**Stack**: `Python 3.x`, `Flask`, `pytz`

## Prerequisites

Make sure you have Python 3.x is installed on your machine. You can check by running:
```bash
python3 --version
```
or
```bash
python --version
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/WellNotWell/DevOps-labs.git
cd app_python
```
    
### 2. Set up a Virtual Environment

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install the Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python3 app.py
```
or
```bash
python app.py
```

### 5. Access the application 
Access the application in your web browser at `http://127.0.0.1:5000/`.

## Docker

### How to Build the Docker Image

```bash
cd app_python
docker build -t lab2 .
```

### How to Pull the Docker Image
```bash
docker pull wellnotwell/lab2
```

### How to Run the Docker Image
```bash
docker run -p 5000:5000 wellnotwell/lab2
```

## Unit Tests

1. `test_moscow_time_calc`: Checks that the displayed Moscow time is correctly calculated and formatted.
2. `test_home_page_rendering`: Checks that the homepage (`/`) renders the correct template containing "Moscow Time:".

## CI Pipeline

The CI pipeline includes the following steps:

1. Check out the code from the repository.
2. Set up the Python environment.
3. Install project dependencies.
4. Lint the Python code using `flake8`.
5. Run unit tests.
6. Install and authenticate Snyk.
7. Run Snyk test to check for vulnerabilities in dependencies.
8. Log in to Docker Hub.
9. Build and Push the Docker image to Docker Hub.


## Visits Counter

The `/visits` endpoint tracks the number of site visits. Each time a user accesses the site, the application:
1. Reads the current visit count from `visits/visits.txt`.
2. Increments the count.
3. Saves the updated count back to the file.

The visit count persists across container restarts. This is achieved by mapping a host directory in `docker-compose.yml` 
to store `visits.txt`, ensuring data is not lost when the container stops or restarts.