# Dockerfile for app_python

# Use a specific version of the Python base image
FROM python:3.10-slim

# Set a non-root user
RUN useradd -m appuser
USER appuser

# Set the working directory
WORKDIR /home/appuser/app

# Copy only the necessary files
COPY --chown=appuser:appuser requirements.txt ./
COPY --chown=appuser:appuser app.py ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]