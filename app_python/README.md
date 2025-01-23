# Python Web Application

## Overview

This is a simple python web application on FastAPI that shows current time in Moscow.

## Running locally

* Make sure you have [Poetry](https://python-poetry.org/docs/) installed

* Clone this repository and enter its folder
```bash
git clone https://github.com/dmhd6219/S25-core-course-labs.git
cd S25-core-course-labs
```

* Create virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

* Install dependencies
```bash
poetry install --no-root
```

* Run the application
```bash
fastapi dev main.py
```
