# Python Web Application Documentation

## Workflow Status Badge

!Python application

## Overview
This Python web application displays the current time in Moscow using the Flask framework.

## File Structure
```
├── app_python
│   ├── templates
│   │   ├── index.html
│   ├── tests
|   │   ├── app_test.py
│   ├── app.py
│   ├── CI.md
│   ├── PYTHON.md
│   ├── DOCKER.md
│   ├── README.md
│   ├── Dockerfile
│   ├── requirements.txt
```


## Setup

You have to go to the `app_python` folder first. Then:
1. Install dependencies from requirements.txt:
```pip install -r requirements.txt```
2. Run the application:
```python app.py```
3. Access the application in your web browser at http://127.0.0.1:5000/.

## Setup via Docker
Docker Containerized Application
This section describes how to run the application as a Docker container.

1. How to Build?
To build the Docker image, navigate to the app_python folder containing the Dockerfile and execute the following command:
```docker build -t kurkune/app_python .```
2. How to Pull?
If you haven't built the image locally, you can pull it from Docker Hub using the following command:
```docker pull kurkune/app_python```
3. How to Run?
To run the application as a Docker container, use the following command:
```docker run -p 5000:5000 kurkune/app_python```

## Counter
1. To run the application you have to run:
```markdown
docker-compose build
docker-compose up
```
inside the `app_python` folder.

## Dependencies
blinker==1.7.0
click==8.1.7
colorama==0.4.6
Flask==3.0.2
itsdangerous==2.1.2
Jinja2==3.1.3
MarkupSafe==2.1.5
Werkzeug==3.0.1

## Unit Tests

I have implemented unit tests for the application. You can find a detailed description of these tests in the `PYTHON.md`
file.

To run the tests, you can use the following command in the `app_python` directory:
```pytest```

## CI Pipeline

I use GitHub Actions to automate the building, testing, linting and Docker image deployment processes. There several
steps in my pipeline:

1. **Dependencies**
    - Check out the code from the repository and set up Python environment.
    - Install project dependencies.

2. **Linter**
    - Use Flake8 to lint the code.

3. **Tests**
    - Run unit tests with `pytest`.

4. **Vulnerability checks**
    - Use Snyk for Vulnerability checks.

5. **Docker Integration**
    - Build a Docker image.
    - Push the Docker image to Docker Hub.


## Maintainer
Alexandra Egorova
