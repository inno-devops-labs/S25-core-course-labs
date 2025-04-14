# Use a precise version of Python base image
FROM python:3.9-alpine3.15

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy only specific files
COPY app.py ./
COPY templates/ templates/

# Change ownership to non-root user
RUN chown -R appuser:appgroup /app

# Switch to non-root user
USER appuser

# Expose the port the app runs on
EXPOSE 5000

# Define the default command
CMD ["python", "app.py"]