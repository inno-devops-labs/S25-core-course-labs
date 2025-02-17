# Use a multi-stage build to create the application
FROM python:3.11-slim AS builder

# Install required dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy only the necessary files
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .

# Use Distroless Python runtime for the final stage
FROM gcr.io/distroless/python3-debian12:nonroot

# Set the working directory
WORKDIR /app

# Copy dependencies and application code from builder
COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=builder /app /app
ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages

# Switch to non-root user
USER nonroot:nonroot

# Expose the application port
EXPOSE 5000

# Command to run the application
CMD ["app.py"]
