# Use a specific version of Python Alpine for a smaller base image
FROM python:3.11-alpine3.19

# Set working directory
WORKDIR /app

# Create a non-root user
RUN adduser -D appuser

# Install dependencies first (for better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only necessary files
COPY app.py .

# Switch to non-root user
USER appuser

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"] 