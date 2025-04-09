# Use a specific version of the base image
FROM python:3.11-slim

# Create a non-root user
RUN useradd -m appuser

# Set the working directory
WORKDIR /app

RUN mkdir -p /app/data && chmod 777 /app/data

# Copy only the necessary files
COPY requirements.txt requirements.txt
COPY main.py main.py
COPY routers/ routers/
COPY util/ util/
COPY templates/ templates/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Change to the non-root user
USER appuser

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]