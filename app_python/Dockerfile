# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/local/app

# Copy requirements.txt
COPY backend/requirements.txt ./

# Copy the tests directory from the parent directory
COPY tests ./tests

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install pytest
RUN pip install pytest

# Copy the rest of the application code from the backend directory
COPY backend/ ./backend

# Create a non-root user
RUN adduser --disabled-password --disabled-login myuser

# Change ownership of the application files
RUN chown -R myuser:myuser /usr/local/app

# Create the visits file and set ownership
RUN touch /usr/local/app/visits && \
    echo "0" > /usr/local/app/visits && \
    chown myuser:myuser /usr/local/app/visits

# Switch to the non-root user
USER myuser

# Expose the application port
EXPOSE 8080

# Command to run the application
CMD ["python", "backend/main.py"]
