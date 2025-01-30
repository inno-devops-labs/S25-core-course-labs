# Python Web App (Flask)
## Overview
A simple Flask web application that displays the current time in Moscow.

## Installation
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Docker

### Build the Docker Image
To build the Docker image, run:
```
docker build -t yourusername/app_python .
docker pull yourusername/app_python
docker run -p 5000:5000 yourusername/app_python
```

