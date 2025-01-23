# Moscow Time Web Application

## Overview

This is a web app that shows current date and time in Moscow. It is written in Python with Bottle framework.

## Installation

Clone this repository:

``` git clone https://github.com/cuprum-acid/devops-labs.git -b lab1 ```

Open directory:

``` cd devops-labs/app_python ```

Install virtual environment and dependencies:

``` python -m venv venv ```

``` source venv/bin/activate ```

``` pip install pip install -r requirements.txt ```

Run the app:

``` python app.py ```

Now it is available on `localhost:8080` in browser. Or you can run in terminal:

``` curl localhost:8080 ```

## Run tests

If you want to run automatic tests, then you need to install additional packages:

``` pip install pytest==8.3.4 ```

``` pip install requests==2.32.3 ```

They were not included in `requirements.txt` because they are not required to run application

After that run:
``` pytest test_app.py ```
