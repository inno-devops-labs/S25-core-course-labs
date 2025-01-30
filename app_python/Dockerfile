# Use a minimal Python image
FROM python:3.11.5-alpine3.18 AS builder

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt --target /app/deps

# Copy source code
COPY . .

# Final runtime image
FROM python:3.11.5-alpine3.18 AS runtime

# Set non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

WORKDIR /app

# Copy installed dependencies from builder
COPY --from=builder /app/deps /app/deps
COPY --from=builder /app .

# Set Python path to include dependencies
ENV PYTHONPATH=/app/deps

# Expose port
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]