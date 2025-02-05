# Moscow Time Display

## Overview
A simple web app that shows the current time in Moscow. Built with Flask, updates automatically, and looks nice!

## Features
- Shows current Moscow time
- Updates automatically
- Works on phones too
- Nice clean design

## Docker Usage
### How to Build
```bash
docker build -t marketer7/flask-time:v1 .
```

### How to Pull
```bash
docker pull marketer7/flask-time:v1
```

### How to Run
```bash
docker run -d -p 8000:8000 marketer7/flask-time:v1
```
Then open http://localhost:8000 in your browser

## Standard Installation
1. Clone this repo
```bash
git clone https://github.com/MarketerKA/S25-core-course-labs.git
```
2. Go to the project folder
```bash
cd app_python
```
3. Install what you need (better use a virtual environment)
```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
4. Run it!
```bash
python app.py
```
5. Open http://127.0.0.1:8000 in your browser

## Pull Requests
I made 2 PRs for this project:
1. Initial setup with basic time display
2. Added auto-updates and better design

## Tech Used
- Python + Flask
- HTML & CSS
- pytz for Moscow time
- Docker for containerization

## Local Setup Tips
- Make sure you have Python 3.x
- Virtual environment recommended
- Check requirements.txt for dependencies
- Needs internet for Moscow timezone data
- Docker as alternative deployment option

## Notes
- Time is always Moscow time (MSK)
- Refreshes every second
- Works offline once loaded
- Container runs as non-root user for security


## Unit Tests
The application includes a test suite that verifies core functionality:

### Test Coverage
- Page accessibility check
- Time format validation (HH:MM:SS)
- Date format validation (DD.MM.YYYY)
- Moscow timezone verification

### Running Tests
```bash
# Using unittest
python -m unittest test_app.py
```

## CI Workflow Status
![Python Flask App CI](https://github.com/MarketerKA/S25-core-course-labs/workflows/Python%20Flask%20App%20CI/badge.svg)

### CI Pipeline Features
- Automated testing on push and pull requests
- Python 3.9 environment
- Dependencies caching
- Snyk security scanning
- Flake8 linting
- Docker image build and push