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
COPY --chown=appuser:appgroup requirements.txt .

# Install dependencies directly in this stage
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_APP=app.py \
    FLASK_ENV=production \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create logs directory
RUN mkdir -p /home/appuser/logs && chown -R appuser:appgroup /home/appuser/logs

# Switch to non-root user
USER appuser

# Expose the port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
    CMD wget --no-verbose --tries=1 --spider http://localhost:5000/ || exit 1

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
