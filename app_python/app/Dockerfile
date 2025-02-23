# Use a specific version of the Python Alpine base image
FROM python:3.9-alpine3.15

ENV PYTHONUNBUFFERED=1

# Create a non-root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set the working directory
WORKDIR /app

# Copy only necessary files
COPY requirements.txt .
COPY app.py .
COPY templates/ ./templates/
COPY static/ ./static/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN chown -R appuser:appgroup ./

# Switch to the non-root user
USER appuser


# Expose the application port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]