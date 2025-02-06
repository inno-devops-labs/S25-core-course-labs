# Moscow Time Web-Application

## About

This is a simple web application on Python that displays the current time in Moscow.

## How to Use

1. Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

2. Run the application using the one of the following commands:

```bash
python main.py
```

```bash
uvicorn --host 0.0.0.0 --port 8001 main:app
```

3. Open your web browser and navigate to `http://0.0.0.0:8001/` to view the current time in Moscow.

## Endpoints

- `/` - Displays the current time in Moscow as an HTML response using `/api/time` endpoint.
- `/api/time` - Returns the current time in Moscow as a JSON response.
- `/docs` - Interactive OpenAPI documentation.
