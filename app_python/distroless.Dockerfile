# Stage 1: Build stage
FROM python:3.12-slim AS builder

# Working directory in the container
WORKDIR /app_python

# Copy only the necessary files for installation
COPY requirements.txt .
COPY app.py .

# Create data directory in builder stage
RUN mkdir -p /app_python/data && chmod 777 /app_python/data

# Install dependencies into a specific target directory
RUN pip install --no-cache-dir -r requirements.txt -t /python_app/lib

# Stage 2: Final stage (Distroless)
FROM gcr.io/distroless/python3:nonroot

# Working directory in the container
WORKDIR /app_python

# Non-root user is already set in the distroless image

# Copy data directory with proper permissions
COPY --chown=nonroot:nonroot --from=builder /app_python/data ./data

# Copy the installed dependencies from the builder stage
COPY --chown=nonroot:nonroot --from=builder /python_app/lib /usr/local/lib/python3.12/site-packages

# Copy the app code from the builder stage
COPY --chown=nonroot:nonroot app.py .

# Set up required for Prometheus environment variables
ENV PYTHONPATH=/usr/local/lib/python3.12/site-packages
ENV PROMETHEUS_MULTIPROC_DIR=/tmp

# Set the port for the app
EXPOSE 5000

# Run the application
ENTRYPOINT ["python3", "app.py"]