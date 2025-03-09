# Python Web Application

[![Python Package CI](https://github.com/UFA-MOROZOV/S25-core-course-labs/actions/workflows/app_python.yml/badge.svg)](https://github.com/UFA-MOROZOV/S25-core-course-labs/actions/workflows/app_python.yml)

## Overview

This is a simple python web application that has a functionality of showing current Moscow time.

It also contains functionality of checking number of visits at `/visits` endpoint.

## Installation

- Clone the repository.

    ```bash
    git clone https://github.com/UFA-MOROZOV/S25-core-course-labs.git
    ```

- Go to `app_python` folder.

    ```bash
    cd S25-core-course-labs/app_python
    ```

- Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

- Run the application:

    ```bash
    python app/app.py
    ```

- Open the app using the link:

    `http://127.0.0.1:5000/`

## Docker

This application also is containerised and there are two options of running container:

1. Build and run the Docker image:

    ```bash
    docker build -t lab2 .
    docker run -p 5000:5000 -d lab2
    ```

2. Pull the latest version of image from Docker Hub:

    ```bash
    docker pull leha0704/morozov_devops_webapp:latest
    docker run -p 5000:5000 -d leha0704/morozov_devops_webapp:latest
    ```

## Unit tests

- You can test web application using unit tests:

    ```bash
    python -m unittest discover -s app_python/tests -t . -v
    ```
