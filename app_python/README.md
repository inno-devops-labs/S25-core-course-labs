![CI Status](https://github.com/ch3rnushka/S25-core-course-labs/tree/lab3-solution/actions/workflows/ci.yml/badge.svg) 
#Moscow time web application

## overview
This is a simple Python web application that displays current time in Moscow.

## requirements
- Python 3
- Flask
- pytz

## installation
1. clone the repository
	```bash
	git clone https://github.com/ch3rnushka/S25-core-course-labs.git
	```
2. navigate to folder
	```bash
	cd app_python
	```
3. install dependencies
	```bash
	pip install -r requirements.txt
	```
4. run application
	```bash
	python app.py
	```

## usage
open http://127.0.0.1:5000 in your browser

# Docker

##How to build?
```bash
docker build -t meowal/msk-time-app .

##How to pull?
```bash
docker pull meowal/msk-time-app:latest

##How to run?
```bash
docker run -p 5000:5000 meowal/msk-time-app:latest
```

## Unit tests
to run unit tests ensure to have pytest
```bash
pytest
pytest test_app.py
```

##CI workflow information
this repository uses GitHub Actions for CI. the CI workflow performs:
- **Dependencies:** installs Python dependencies and required tools
- **Linter:** runs flake8 to ensure code style consistency
- **Tests:** executes unit tests using pytest
- **Docker Steps:** logs into Docker Hub builds and pushes the docker image
- **Security:** runs a Snyk vulnerability scan

##How to trigger the workflow
the workflow runs automatically on pushes and pull requests
