# Python Web Application

## Overview

This is a simple python web application on FastAPI that shows current time in Moscow.

## Running locally

1. Clone this repository and enter its folder

    ```bash
    git clone https://github.com/dmhd6219/S25-core-course-labs.git -b lab1
    cd S25-core-course-labs
    cd app_python
    ```

2. Create virtual environment

   * On Linux:
   
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
   
   * On Windows:
   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Install dependencies

   * If you have [Poetry](https://python-poetry.org/docs/) installed:

    ```bash
    poetry install --no-root
    ```

   * If you have **no** [Poetry](https://python-poetry.org/docs/) installed:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application

```bash
fastapi dev main.py
```
