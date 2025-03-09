# Overview

This python application uses Flask framework to display current time in Moscow. It follows several practices to ensure
code quality, they are described in detail in `PYTHON.md`.

## Installation instructions

1. Make sure you are in `app_python` directory: `cd app_python`
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the application: `python main.py`
4. Enjoy!

## Docker

### How to build?

To build the image run: `docker build -t flask-app .`

### How to pull?

To pull the image from docker hub use: `docker pull mishablin/devops-labs`

### How to run?

To run the container use: `docker run -p 5000:5000 mishablin/devops-labs`

## Unit tests

To run unit tests run: `pytest`

## Visits counter

The application stores the number of visits.

To access the number of visits - visit the `/visits` endpoint.

```bash
docker exec -it monitoring-app_python-1 bash

nonroot@6712670824c7:/src$ ls
main.py  requirements.txt  static  templates  visits.txt

nonroot@6712670824c7:/src$ cat visits.txt
2
```
