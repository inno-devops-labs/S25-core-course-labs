# Use a lightweight Python base image
FROM python:3.9-slim

# Set a working directory for the app
WORKDIR /home/appuser

# Copy application files while still running as root
COPY app.py requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user
RUN useradd --create-home --shell /bin/bash appuser

RUN mkdir -p /data && chown -R appuser:appuser /data

# Switch to non-root user
USER appuser

# Expose port 5000
EXPOSE 5000

# Set default entrypoint
ENTRYPOINT ["python", "app.py"]
