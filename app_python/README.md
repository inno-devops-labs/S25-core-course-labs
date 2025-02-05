# Python Web Application

A simple web application built with Flask that displays the current time timezone (Moscow time by default).


## Usage

#### Installation

To prepare virtual environment run:

```
virtualenv venv
source venv/bin/activate
```
or
```
python -m venv venv
source venv/bin/activate
```
To install dependencies file `requirements.txt` file run:
```
pip install -r requirements.txt
```

#### Settings

Edit the `config.txt` file to set the time zone of interest. To do this, delete everything from it and type in your sona. To find out all possible options, perform 
```
>>> import pytz
>>> pytz.all_timezones
```
Using the python interpreter in the console.
In case of a configuration error, Moscow time is displayed.
To disable debugging mode change the last line in `app.py` use `debug=False` instead `debug=True`.

## Using
```
pip install -r requirements.txt
```

To use this application run `python app.py`.


## Docker

There is an ability to use application in Docker. You may build it manually or use image from Docker Hub.
=======
```
>>> import pytz
>>> pytz.all_timezones
```

#### Building

To build image manually run:
```
docker build --no-cache -t <name> .
```

#### Pulling

To pull image from Docker Hub run:
```
docker pull voronm1522/devops:python-app
```

#### Running

To run image run:
```
docker run <name>
```

## Unit Tests

There are unit tests for application in `unittests.py` file. To run it use:
```
python unittests.py
```
Output will contain `OK` in case of success or backtrace for function(s) with error.

## CI
[![Application CI](https://github.com/VoronM1522/S25-core-course-labs/actions/workflows/python-app.yml/badge.svg)](https://github.com/VoronM1522/S25-core-course-labs/actions/workflows/python-app.yml)

CI triggers on push. It runs on ubuntu-latest. It clones (copy) repository using `actions/checkout@v3` and execute the next steps:
    - Setting up python;
    - Dependencies and linter (`flake8`) installation;
    - Linting the app;
    - Running tests (unit tests);
    - Login to Docker Hub:
        - I use username as a plain text (environment variable), since it is not a secret from the previous pushes and README.md, where I describe pulling it from Docker Hub public repository. However password is a sencetive data, so I use GitHub Secrets
    - Build & Push Docker image

As you can see, most of the steps use predefined workflaws.
