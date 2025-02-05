![CI Workflow](https://github.com/Galyusha/s25-core-course-labs/actions/workflows/ci.yml/badge.svg)
#  Moscow Time Django App

## Description
A simple Django application that displays the current time in Moscow.

## Installation
```bash
git clone https://github.com/Galyusha/S25-core-course-labs.git
git checkout lab1
cd app_python
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 manage.py runserver
```
## Unit Tests

### Running Tests
To run the unit tests, use the following command:

```bash
python manage.py test
```

## Continuous Integration & Deployment (CI/CD)

### GitHub Actions Workflow
This repository uses GitHub Actions to automate the following:
1. **Linting**: Runs flake8 to enforce code style.
2. **Unit Testing**: Runs Django's test suite.
3. **Docker Build & Push**: If tests pass, the app is containerized and pushed to Docker Hub.

