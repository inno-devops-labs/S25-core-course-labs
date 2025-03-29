# Overview

This is a small python service that displays time !

And gives number of visits of the main page, on `/visit` endpoint

## Service deployment

![workflow](https://github.com/Processor228/S25-core-course-labs/actions/workflows/app_python.yml/badge.svg)

## Local installation and testing

Optional: you may wanna set up venv

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Beforehand, install the dependencies:

```bash
pip install -r reqiurements.txt
```

And starting the service is as easy as running one command (make sure project root is `service` folder)!

```bash
cd service
python3 -m uvicorn main:app
```

### Docker

To build the image:

```bash
docker build \
   --tag $(whoami)/app_python:v1.1 \
   --build-arg UID=10001 \
   --build-arg GID=10001 .
```

To pull the image:

```bash
docker pull elonmaxx/time_service:latest
```

To run image:

```bash
docker run time_service
```

To run distroless:

```bash
docker build -f distroless.dockerfile -t dless .
docker run dless
```

## CI workflow

CI workflow was implemented, that verifies code is well-formatted, runs tests, and lints all the code with pylint. After all these steps are performed, SNYK vulnirability check is run, and then the docker image is built and pushed to dockerhub.
