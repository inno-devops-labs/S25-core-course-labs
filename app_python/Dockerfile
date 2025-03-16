# Use a lightweight Python base image
FROM python:3.9-slim

# Set a working directory for the app
WORKDIR /home/appuser

# Copy application files first while still running as root
COPY app.py requirements.txt ./

# Ensure the visits file exists and is writable
RUN touch visits && chmod 666 visits

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user and switch to it
RUN useradd --create-home appuser && chown -R appuser:appuser /home/appuser
USER appuser

# Expose port 5000
EXPOSE 5000

# Set default entrypoint
ENTRYPOINT ["python", "app.py"]
