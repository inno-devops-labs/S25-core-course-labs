# Python Web Application

[![Test and build python app](https://github.com/ortieom/S25-DevOps-labs/actions/workflows/main.yml/badge.svg)](https://github.com/ortieom/S25-DevOps-labs/actions/workflows/main.yml)

This web application is built using the Flask to display current time in Moscow and count visits.

## Site map

- Display current time in Moscow (`/`)
- Count and display number of visits (`/visits`)

## Running application locally

### Requirements

Before starting, make sure you have Flask and pytz installed. 

Initialise venv, and install dependencies using:

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

### Using the application

To run this application, execute `python3 app.py`, navigate to your browser, and visit `http://localhost:8080`.


## Docker

### How to build

Run following: `docker build -t python_app .`

### How to pull

Images are publically available. There are 2 tags that you may find useful:
- `jodak628286/python_app:python_app` - default version (root user)
- `jodak628286/python_app:rootless` - version built with best practices (non-root user, only required files)

To pull them respectfully:
```bash
docker pull jodak628286/python_app:python_app
docker pull jodak628286/python_app:rootless
```
### How to run

Use `docker compose up -d` inside the `app_python` directory to run the application.
Your app will be available at port `8080`.


## Unit Tests

I use pytest to run unit tests for this application.

To run tests execute `python -m pytest app_python` in the root of the repository.

More details in [PYTHON.MD](./PYTHON.MD).

## CI

Main workflow aims at providing 3 functions:

- testing code
- applying linter checks
- pushing image to DockerHub if everything is fine
