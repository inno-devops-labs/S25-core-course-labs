# Moscow Time Web Application

Simple Python web application for Lab 1 that displays the current time in Moscow. It is built using the FastAPI framework and Jinja2 templating for rendering the HTML page.

## Requirements

- Python 3.7+
- Dependencies listed in `requirements.txt`

## Setup

1. Clone the repository

2. Make sure you're in the python application directory

   ```bash
   cd ./app_python
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
uvicorn app.main:app --reload
```

## Using the Application

Go to <http://127.0.0.1:8000/time> (in case it runs locally)
