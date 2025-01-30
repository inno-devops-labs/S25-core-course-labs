# time_service_python

A simple Python Web application to show current time in Moscow.

## Prerequisites

- [Python](https://www.python.org/downloads/)
- [FastApi](https://fastapi.tiangolo.com/)

## Install

Clone the repository:

```sh
git clone https://github.com/nai1ka/S25-core-course-labs
cd S25-core-course-labs/app_python
```

Create and activate virtual environment:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```sh
pip install -r requirements.txt
```

Run the app:

```sh
cd app
python -m uvicorn main:app --reload
```

The server will be available at [http://localhost:8000](http://localhost:8000)

## Docker

### Building

To build the image, run:

```sh
docker build -t nai1ka/time-service:latest .
```

You can use any tag you want instead of `nai1ka/time-service:latest`.

### Pulling

To pull the image from the Docker Hub, run:

```sh
docker pull nai1ka/time-service:latest
```

### Running

To run the container, run:

```sh
docker run -p 8000:8000 nai1ka/time-service:latest
```

Don't forget to replace `nai1ka/time-service:latest` with the tag you are using.

## Distroless Image Version

You can also build a distroless image:

```sh
# Build the image
docker build -t time-service-distroless -f distroless.Dockerfile .
# Run the container
docker run -p 8000:8000 time-service-distroless
```

## Layout

Directory structure (dotfiles are omitted):

```sh
.
├── PYTHON.md
├── README.md
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   └── routes
│       ├── __init__.py
│       └── index.py
├── requirements.txt
└── templates
    └── index.html
```
