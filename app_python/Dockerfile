# Use an official Python image as the base
FROM python:3.13.1-alpine3.21

# Set environment variables to make the image more secure
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies and create non-root user
RUN apk add --no-cache \
        shadow=4.16.0-r1 \
        gcc=14.2.0-r4 \
        musl-dev=1.2.5-r8 \
        libffi-dev=3.4.6-r0 && \
    groupadd -r appgroup && \
    useradd -r -g appgroup appuser

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY app.py .

# Switch to non-root user
USER appuser

# Expose the port that the app will run on
EXPOSE 8080

# Command to run the app using Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app:app"]
