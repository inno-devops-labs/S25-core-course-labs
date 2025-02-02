# FastAPI app
- Shows the current time in Moscow.
- Error handling for 404 (Not Found) and 500 (Internal Server Error) scenarios.
- Logging to track server activity and errors.
- Static file serving for CSS.

## Local Installation
```bash
git clone URL
cd app_python
pip install -r requirements.txt
chmod +x server.sh
server.sh
```

## Testing

```
python -m unittest tests/test_app.py

```

## Logs
Logs are saved to app.log and printed to the console.
