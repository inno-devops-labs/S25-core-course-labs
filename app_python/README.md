# Python Web Application

[![Python package](https://github.com/Angelika2707/S25-core-course-labs/actions/workflows/pipeline.yml/badge.svg?branch=lab3)](https://github.com/Angelika2707/S25-core-course-labs/actions/workflows/pipeline.yml)

## Description
 A Python web application that displays the current time in Moscow.

## Prerequisites
- Python 3.x
- pip

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Angelika2707/S25-core-course-labs.git
cd app_python
```
    
### 2. Set up a Virtual Environment

Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install the Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Linux
```bash
python3 main.py
```
Windows
```bash
python main.py
```

Then you can find the application on the address: `http://127.0.0.1:5000`

# Docker

### How to build?
```bash
docker build -t lab2 .
```

### How to pull?
```bash
docker pull angelika2707/lab2
```

### How to run?
```bash
docker run -p 5000:5000 angelika2707/lab2
```

# Unit tests
1. **test_index_route**: Test verifies that the `/` route returns a 200 status and contains the text "Current Time in Moscow".

2. **test_moscow_time_correctness**: Test verifies the Moscow time rendered in the template matches the expected time.

# CI Pipeline
- Checkout repository
- Set up Python environment
- Install dependencies
- Linter - flake8
- Run tests
- Run Snyk security scan
- Set up Docker Buildx
- Login to Docker Hub
- Build and push Docker image

## Site Visits Count

The `/visits` endpoint tracks the number of times the site has been visited. 
On each visit, the application reads the current count from `visits/visits.txt`, increments it by one, and updates the file.

To **persist the visit count across container restarts**, a host directory is mounted in `docker-compose.yml`, so `visits.txt` remains unchanged even if the container stops or restarts.