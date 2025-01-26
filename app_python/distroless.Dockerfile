# Stage 1: Build stage
FROM python:3.9-slim AS build-env

# Set working directory
WORKDIR /app

# Copy application files and requirements
COPY templates /app/templates
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt

# Install Python dependencies into a separate folder
RUN pip install --no-cache-dir -r requirements.txt --target /app/dependencies

# Stage 2: Distroless runtime
FROM gcr.io/distroless/python3:nonroot

# Set environment variable to point to dependencies
ENV PYTHONPATH=/app/dependencies

# Copy application files and dependencies to the final image
COPY --from=build-env /app /app

# Set working directory
WORKDIR /app

# Expose port 5000
EXPOSE 5000

# Set the start command
CMD ["app.py"]
