#!/bin/bash

# Navigate to the app_python directory
cd "$(dirname "$0")"

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Please ensure it exists."
    exit 1
fi

# Run the FastAPI application
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
