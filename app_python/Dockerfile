# Stage 1: Builder
########################################
FROM python:3.10.13-alpine3.18 AS builder
LABEL stage="builder"

# Set work directory
WORKDIR /app

# Install required dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY main.py .

########################################
# Stage 2: Final Image
########################################
FROM python:3.10.13-alpine
LABEL stage="final"

# Create a non-root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

# Copy installed dependencies from builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

# Copy application source code
COPY main.py .

# Ensure the app runs with the correct user
USER appuser

# Expose the correct port
EXPOSE 5050

# Set the entry point command
CMD ["python", "main.py"]
