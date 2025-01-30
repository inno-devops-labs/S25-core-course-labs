# Moscow Time Web App

Simple web application displaying current Moscow time, built with FastAPI

## Features
- Real-time Moscow time display
- Auto-update every second
- Clean minimal interface
- REST API endpoint

## Installation
```bash
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

## Usage
```bash
cd app/
uvicorn main:app --reload
```

Visit http://localhost:8000 in your browser

## Testing
```bash
pytest -v
```

## API Endpoints
- `GET /` - Main page with time display
- `GET /time` - JSON endpoint returning current Moscow time