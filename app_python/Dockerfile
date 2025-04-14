# Use a minimal and specific base image
FROM python:3.10-alpine3.15

# Set environment variables for security and efficiency
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Create a non-root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set working directory
WORKDIR /app

# Copy only required files (avoid unnecessary files)
COPY requirements.txt .

# Install dependencies without cache to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

COPY /templates /app/templates

# Copy application files
COPY app.py .

# Switch to non-root user
USER appuser

# Expose the application port
EXPOSE 5000

# Define the startup command
CMD ["python", "app.py"]
