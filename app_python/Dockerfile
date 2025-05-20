# Use a precise version of the official Python runtime as a parent image
FROM python:3.9-alpine3.15

# Set environment variables to avoid running as root user
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VERSION=1.1.12

# Install dependencies
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    libressl-dev \
    && pip install "poetry==$POETRY_VERSION"

# Create a non-root user
RUN adduser -D appuser

# Set the working directory in the container
WORKDIR /home/appuser/app

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Install application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code (excluding unnecessary files)
COPY . .

# Change ownership of the application directory to the non-root user
RUN chown -R appuser:appuser /home/appuser/app

# Create /data directory and set ownership
RUN mkdir -p /data && chown appuser:appuser /data

# Switch to the non-root user
USER appuser

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]