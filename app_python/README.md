# Current Moscow Time Application

[![CI](https://github.com/Gendiro/S25-core-course-labs/actions/workflows/ci.yml/badge.svg)](https://github.com/my-username/my-project/actions)

## Running the application

1. Setup the virtual environment:
```bash
python -m venv venv
```
2. Activate it (Linux):
```bash
source venv/bin/activate
```
3. Install all necessary dependencies
```bash
pip install -r requirements.txt
```

4. Run the server with uvicorn:
```bash
uvicorn app.main:app --
```

## Endpoints

It's a FastAPI based python application that currently has two endpoints:

1. A Web UI interface on `/` endpoint (the address is `localhost:8000` by default, configurable by `uvicorn`)
2. An `/api/moscow_time` endpoint that returns the `TimeData` structure: 

```python
class TimeData(BaseModel):
    time: str
    timestamp: float
```

Also, don't forget that FastAPI provides `/docs` and `/redoc` endpoint for documentation.

## Unit tests

The tests are done with `unittest` and `TestCleint`. 

To ensure that the app is working properly, you can run them yourself with:
```bash
python -m unittest tests/
```

The current tests are not using heavy testing tools like `selenium`, so it's not a 100% coverage when it
comes to front-end part.

## Docker

### How to Build

Run the command:

```bash
docker build -t moscow-time-app .
```

### How to Pull

Do this command (I hope I won't forget to make it public):

```bash
docker pull gendiro/moscow-time-app:latest
```

### How to Run

If you build it yourself, do
```bash
docker run -p 8000:8000 moscow-time-app
```

If you decided to load dockerhub servers for fun, it's a bit different:
```bash
docker run -p 8000:8000 gendiro/moscow-time-app:latest
```

Add `-d` flag to run the app in detached mode or change port in `-p` flag if you feel like it.

### Distroless

Also, you can also build the distroless version using the `distroless.Dockerfile`:

```bash
docker build -t moscow-time-distroless -f distroless.Dockerfile .
```

# CI

The repository has a CI implemented via GitHub Actions, so each push and pull_request to the master branch is 
being checked on compliance with tests and linting, and sends the new-built image to docker hub.
