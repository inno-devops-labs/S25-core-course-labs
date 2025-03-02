# Web application to display current time in Moscow

![Workflow status](https://github.com/Tedor49/S25-core-course-labs/actions/workflows/python-app.yml/badge.svg)

## Overview

This application uses [Python](https://www.python.org),
[Flask](https://flask.palletsprojects.com) and [Waitress](https://github.com/Pylons/waitress)
to host a web page to shown the current time in Moscow. The app serves a single webpage,
which contains the current time and date in Moscow, along with some minimalistic
formatting. You can find the source code in [app.py](app.py), the [HTML](resources/templates)
and [CSS](resources/static) files in [resources](resources). Required python packages are in
[requirements.txt](requirements.txt) and some implementation justifications are in [PYTHON.md](PYTHON.md)

## Setup

### Python

Download Python 3 from [the official website](https://www.python.org/downloads/) and make sure to add it to PATH.

Install pip from command line if it is not already installed:

```batch
python -m ensurepip --upgrade
```

### Requirements

From the command line, inside the app_python directory, run

```batch
pip install -r requirements.txt
```

### Running the web application

From the command line, inside the app_python directory, run

```batch
waitress-serve --host your_ip --port your_port "app:app"
```

your_ip and your_port have to be replaced by the ip you wish to host on
and the port number respectively, for example:

```batch
waitress-serve --host 127.0.0.1 --port 8080 "app:app"
```

After hosting, you can connect to the web app from any browser using
the provided ip and port, which will also be shown in the terminal.

## Docker

You can run this app using a Docker container, if you wish to do so.
To do this, you can either build the image yourself, or pull it from
DockerHub, and then run the image.

### Install Docker

If you do not have Docker already, install it from
[the official website](https://docs.docker.com/get-started/get-docker/),
and make sure you can use it via the command line

### Building the image

From the command line, inside the app_python directory, run

```batch
docker build -t python_msk_time:latest .
```

### Pulling the image

From the command line, run

```batch
docker image pull tedor49/python_msk_time
```

You may be asked to authorize on DockerHub, you can do it with

```batch
docker login
```

### Running the container

After obtaining the image, you can run

```batch
docker run -p 8000:8000 -t python_msk_time:latest
```

or

```batch
docker run -p 8000:8000 -t docker.io/tedor49/python_msk_time:latest
```

depending on whether you built or pulled the image.

## Distroless Docker

### Building the image

From the command line, inside the repository directory, run

```batch
docker build -f distroless.Dockerfile -t python_msk_time_distroless:latest .
```

Running the image is the same as with regular Docker, just replace the image name

## Unit Tests

There are some unit tests provided inside of the [test.py](test.py) file

### Installing dependencies

From the command line, run

```batch
pip install pytest coverage pytest-cov
```

### Running the tests

From the command line, inside the app_python directory, run

```batch
pytest test.py --cov=app
```

This will run all of the unit tests and show you the results, as well as
code coverage of the app

## CI/CD

There is a GitHub actions workflow configured which allows for testing the app and
building and pushing it to DockerHub. The workflow configuration file is located
at [.github/workflows/python-app.yml](../.github/workflows/python-app.yml).
The workflow installs all dependencies and tests the app using the provided
test.py file. Furthermore, it also lints the code using flake8. Meanwhile, another job
gets the DockerHub login details from secrets hosted on GitHub itself, and builds
and pushes the image automatically. You can view the workflow status by going
into Actions page on GitHub or by checking the status of the badge at the top of this document.
