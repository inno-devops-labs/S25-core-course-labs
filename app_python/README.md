# Python Web Application: Moscow Time <br>
[![Python application CI](https://github.com/TheAnushervon/S25-core-course-labs/actions/workflows/app_python.yml/badge.svg?branch=lab3)](https://github.com/TheAnushervon/S25-core-course-labs/actions/workflows/app_python.yml) <br> 
Web-application for displaying current time in Moscow. Developed by Django framework and follows best practices for coding standards and quality. <br>

## Features
- Displays current time in Moscow.
- Dynamically shows time (no need for refreshing).

## CI/CD

This project uses GitHub Actions for CI/CD to automate testing, security scanning, and Docker image building.  
The workflow is triggered on both **push** and **pull_request** events when changes occur in:
- `app_python/**`
- `.github/workflows/app_python.yml`

This ensures that CI checks run for both direct pushes and pull requests.

For more details, [click here](https://github.com/TheAnushervon/S25-core-course-labs/blob/lab3/.github/workflows/app_python.yml).


## How to launch 

### Prerequisites
1. Python 3.7 or later installed. 

### Installation 
1. Clone this repository: 
```bash 
git clone <repository-url>
cd app_python
```

2.(Optional) Create a virtual environment(good practice escaping any problems): 

```bash
python -m venv env
source env/bin/activate #On Windows .\env\Scripts\activate
```

3. Install required dependencies from requirements.txt: 

```bash 
pip install -r requirements.txt
```

### Running application

1. Run Django project:

```bash 
cd moscow_time
python3 manage.py runserver
```
2. Open your browser and navigate to `http://127.0.0.1:8000/` or `http://localhost:8000`.

## Docker

### How to build: 
Navigating to ```app_python``` and build docker image locally 
```bash 
cd app_python/
docker build -t moscow_time .
```

### How to pull: 
Pull image from Docker Hub: 
```bash
docker pull theanushervon/moscow_time:latest
```

### How to run: 
Run container locally providing ```<host_port>:<container_port>```
```bash 
docker run -p 8000:8000 theanushervon/moscow_time:latest
```
Go to ```http://localhost:8000```

## Unit Testing 

### Where to look :
 ```test_views.py``` has tests 

 ### How to run: 
 ```bash 
 python3 manage.py test
 ```

 ### Test coverage: 
```bash
coverage run --source="display_time" manage.py test
coverage report 
``` 
