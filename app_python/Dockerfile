# Use a minimal non-root Python base image
FROM python:3.13-alpine

# Set working directory
WORKDIR /app

# Copy necessary files (already filtered by .dockerignore)
COPY . /app/

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "/app/app.py"]
