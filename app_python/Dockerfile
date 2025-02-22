# Use a minimal non-root Python base image
FROM python:3.13-alpine

# Set working directory
WORKDIR /app

# Install curl for healthcheck
RUN apk add --no-cache curl

# Copy necessary files (already filtered by .dockerignore)
COPY . /app/

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "-u", "-m", "app"]