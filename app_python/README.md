# Current Moscow Time Application

## Running the application

1. Setup the virtual environment:
```bash
python -m venv venv
```
2. Activate it (Linux):
```bash
source venv/bin/activate
```
3. Install all necessary dependencies
```bash
pip install -r requirements.txt
```

4. Run the server with uvicorn:
```bash
uvicorn app.main:app --
```

## Endpoints

It's a FastAPI based python application that currently has two endpoints:

1. A Web UI interface on `/` endpoint (the address is `localhost:8000` by default, configurable by `uvicorn`)
2. An `/api/moscow_time` endpoint that returns the `TimeData` structure: 

```python
class TimeData(BaseModel):
    time: str
    timestamp: float
```

Also, don't forget that FastAPI provides `/docs` and `/redoc` endpoint for documentation.

## Testing

The tests are done with `unittest` and `TestCleint`. 

To ensure that the app is working properly, you can run them yourself with:
```bash
python -m unittest tests/
```

