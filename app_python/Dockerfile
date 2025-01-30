# syntax=docker/dockerfile:1

########################################
# Stage 1: Builder
########################################
FROM python:3.10-alpine3.15 AS builder
LABEL stage="builder"

# Update and install build dependencies if needed (optional)
# RUN apk update && apk add --no-cache gcc musl-dev

WORKDIR /app

# Copy only requirements first to leverage Docker caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app files
COPY main.py .

########################################
# Stage 2: Final
########################################
FROM python:3.10-alpine3.15
LABEL stage="final"

# Create a non-root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

# Copy installed site-packages from builder stage to final image
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
# Copy your application code as needed
COPY main.py .

# Switch to the non-root user
USER appuser

# Expose the port (Flask defaults to 5000)
EXPOSE 5050

# Set default command to run your Python app
CMD ["python", "main.py"]
