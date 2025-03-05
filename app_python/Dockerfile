# Use a minimal non-root Python base image
FROM python:3.13-alpine

# Set working directory
WORKDIR /app

# Install curl for healthcheck and prometheus_client
RUN apk add --no-cache curl && \
    pip install prometheus_client

# Copy necessary files (already filtered by .dockerignore)
COPY . /app/

# Expose ports
EXPOSE 8000 8001

# Run the application
CMD ["python", "-u", "-m", "app"]