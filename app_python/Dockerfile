# Python base image
FROM python:3.9-slim

# Create a non-root user
RUN useradd --create-home appuser

# Create a working directory
WORKDIR /home/appuser

# Copy installation requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files
COPY app.py .

# Use the non-root user
USER appuser

# Expose the Flask default port
EXPOSE 5000

# Default command to start Flask
CMD ["python", "app.py"]
