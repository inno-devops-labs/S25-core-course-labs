# Current Moscow time web application

## Overview

This web application displays the current time in Moscow. It supports two formats of the output:

- Web page containing current time in Moscow
- JSON with current time in Moscow

The Swagger documentation is available at the following path: `/docs`.

## Tools

- [FastAPI](https://fastapi.tiangolo.com/)
- [Jinja2](https://pypi.org/project/Jinja2/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Pylint](https://docs.pylint.org/)
- [Black](https://black.readthedocs.io/en/stable/)

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/danmaninc/S25-core-course-labs

# 2. Change directory
cd S25-core-course-labs/app_python

# 3. Install the dependencies
pip install -r requirements.txt

# 4. Run the production server
fastapi run src/main.py --port 80

# 5. Test the application
curl http://localhost
curl http://localhost/time
```

## Docker

### How to build?

You can build the Docker image using the following command:

```bash
docker build app_python -t app_python
```

### How to pull?

To pull the latest image from Docker Hub, use the following command:

```bash
docker pull dnworks/app_python:latest
```

### How to run?

Run the Docker container:
> **NB!** Port 80 must be exposed so you can access the web application at 80 port (`http://localhost/`).

- Self-built image:

```bash
docker run -p 80:80 app_python
```

- From Docker Hub:

```bash
docker run -p 80:80 dnworks/app_python:latest
```

## Distroless Image Version

### How to build?

```bash
docker build -f app_python/distroless.Dockerfile app_python -t app_python_dstlss
```

### How to pull?

```bash
docker pull dnworks/app_python_dstlss:latest
```

### How to run?

> **NB!** Port 80 must be exposed so you can access the web application at 80 port (`http://localhost/`).

- Self-built image:

```bash
docker run -p 80:80 app_python_dstlss
```

- From Docker Hub:

```bash
docker run -p 80:80 dnworks/app_python_dstlss:latest
```
