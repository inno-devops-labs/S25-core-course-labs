FROM python:3.11-alpine

LABEL authors="Egor Valikov"

# Set environment variables to optimize python behavior, and prevents python from writing .pyc files and enables unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create a non-root user for better security
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set the working directory to the root
WORKDIR /app

# Copy dependencies file to the container
COPY requirements.txt /app/

# Install dependencies without caching to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files to the container
COPY . /app

# Switch to the non-root user
USER appuser

# Expose the Flask application port
EXPOSE 5000

# Define the command to run the application
CMD ["python", "run.py"]