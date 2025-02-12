# syntax=docker/dockerfile:1

# Build stage
FROM python:3.11-alpine AS builder

# Create non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set working directory
WORKDIR /app

# Install build dependencies
RUN apk add --no-cache --virtual .build-deps gcc musl-dev

# Copy only requirements first for better caching
COPY --chown=appuser:appgroup requirements.txt .

# Install dependencies with pip
RUN pip install --no-cache-dir --user -r requirements.txt

# Create .local directory if it doesn't exist in builder stage
RUN mkdir -p /home/appuser/.local

# Copy installed packages from builder only if they exist
RUN [ -d /home/appuser/.local ] && cp -r /home/appuser/.local /home/appuser/ || echo "No .local directory to copy"

# Final stage
FROM python:3.11-alpine

# Create same user in final stage
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set working directory
WORKDIR /app

# Copy application files
COPY --chown=appuser:appgroup app.py .
COPY --chown=appuser:appgroup templates/ templates/
COPY --chown=appuser:appgroup static/ static/

# Set environment variables
ENV PATH=/home/appuser/.local/bin:$PATH \
    PYTHONPATH=/home/appuser/.local/lib/python3.11/site-packages \
    FLASK_APP=app.py \
    FLASK_ENV=production \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Switch to non-root user
USER appuser

# Expose the port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
    CMD wget --no-verbose --tries=1 --spider http://localhost:5000/ || exit 1

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
