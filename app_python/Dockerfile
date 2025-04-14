# Use the official lightweight Python image
FROM python:3.11-slim AS base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    APP_HOME=/app

# Set the working directory
WORKDIR $APP_HOME

# Copy requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY src src
COPY static static
COPY templates templates

COPY entrypoint.sh ./
RUN chmod +x entrypoint.sh

# Run the application
ENTRYPOINT ["./entrypoint.sh"]
