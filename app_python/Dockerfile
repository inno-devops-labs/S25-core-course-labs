FROM python:3.9-alpine3.15 AS builder

# The working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY templates/ ./templates/

COPY test_app.py .
RUN pytest test_app.py

# A new stage for the final image
FROM python:3.9-alpine3.15

# The working directory
WORKDIR /app

# Copy installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Copy the application files
COPY app.py .
COPY templates/ ./templates/

# Non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
RUN chown -R appuser:appgroup /app
USER appuser

# The app runs on
EXPOSE 5000

# Labels for better organization
LABEL maintainer="ohibloom@gmail.com" \
      version="1.0" \
      description="Flask application to display current time in Moscow"

# Running the application
CMD ["python", "app.py"]