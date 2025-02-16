# Use a specific, lightweight base image
FROM python:3.11.6-alpine3.18 AS builder

# Create a non-root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set working directory
WORKDIR /app

# Copy only necessary files (avoid copying everything)
COPY requirements.txt .

# Install dependencies efficiently
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code (excluding unnecessary files via .dockerignore)
COPY src/ src/

# Set ownership and permissions
RUN chown -R appuser:appgroup /app

# Switch to non-root user
USER appuser

# Expose only necessary port
EXPOSE 5000

# Run the application
CMD ["python", "src/main.py"]
