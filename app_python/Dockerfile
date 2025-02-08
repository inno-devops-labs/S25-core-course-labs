# Use the official Python image as a base image
FROM python:3.10-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies and clean up cache to keep the image small
RUN pip install --no-cache-dir -r requirements.txt

# Copy necessary application files
COPY ./main.py .

# Set environment variables for predictable behavior
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
    
# Create and switch to a non-root user
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /app
USER appuser

# Expose the port the application will run on
EXPOSE 8000

# Define the command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

