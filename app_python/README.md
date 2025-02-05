# Python Web Application

## Overview

This is a simple Python web application that displays the current time in Moscow.

## Local Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/nikolaevaElizaveta/S25-core-course-labs
   ```

2. Navigate to the app_python directory:

    ```bash
    cd S25-core-course-labs/app_python
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python app.py
    ```

5. Open the browser at <http://127.0.0.1:5000>.

## Docker

1. How to build

    ```bash
    docker build -t my-flask-app .
    ```

2. How to pull

    ```bash
    docker pull nikolaevaelizaveta/my-flask-app
    ```

3. How to run

    ```bash
    docker run -p 5000:5000 my-flask-app
    ```

[![CI Pipeline](https://github.com/nikolaevaElizaveta/S25-core-course-labs/actions/workflows/ci.yml/badge.svg)](https://github.com/nikolaevaElizaveta/S25-core-course-labs/actions/workflows/ci.yml)
