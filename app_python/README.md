# Devops python time API

## Overview

### Implementation technologies:

1) `Python` - programming language
2) `FastAPI` - framework for API development
3) `uvicorn` - webserver for serving API
4) `Pydantic` - for data validation and response serialization

### App structure:

```
app_python/       # application
    - main.py     # program entrypoint
    - routes.py   # API endpoints
    - schemas.py  # Pydantic models for response
    - settings.py # Environemnt variables
```

## Launch

### Prepare environment

```bash
cd app_python
```

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

### Run

```bash
python main.py
```

Then you can reach docs at http://localhost:8000/docs

## Docker

### Build

```bash
docker build -t wensiet/devops-py-app:latest .
```

### Pull

```bash
docker pull wensiet/devops-py-app:latest
```

### Run

```bash
docker run -p 8000:8000 wensiet/devops-py-app:latest
```
