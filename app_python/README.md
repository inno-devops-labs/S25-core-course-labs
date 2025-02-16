# Python Web Application Documentation
## Overview
This Python web application displays the current time in Moscow using the Flask framework.

## File Structure
```
├── app_python
│   ├── templates
│   │   ├── index.html
│   ├── app.py
│   ├── PYTHON.md
│   ├── README.md
│   ├── requirements.txt
```


## Setup
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
```docker build -t kurkune/myapp .```
2. How to Pull?
If you haven't built the image locally, you can pull it from Docker Hub using the following command:
```docker pull kurkune/myapp```
3. How to Run?
To run the application as a Docker container, use the following command:
```docker run -p 8080:8080 kurkune/myapp```

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

You can find a description of unit tests for the application. in the `PYTHON.md`
file.

To run the tests, use the following command in the `app_python` directory:
```pytest```

## CI Pipeline

I use GitHub Actions to automate the building, testing, linting and Docker image deployment processes. 

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
