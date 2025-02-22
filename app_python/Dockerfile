# Use the official lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy application files into the container
COPY web_app.py /app/web_app.py

# Install required Python packages
RUN pip install flask prometheus-client pytz

# Expose ports for the app and metrics
EXPOSE 8000 8001

# Command to run the application
CMD ["python3", "web_app.py"]
