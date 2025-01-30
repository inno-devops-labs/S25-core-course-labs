# Use Python base for building
FROM python:3.11.5 AS builder

WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir --target=/app/deps -r requirements.txt

COPY . .

# Use Distroless runtime (non-root)
FROM gcr.io/distroless/python3-debian12:nonroot

WORKDIR /app

# Copy application code and installed dependencies
COPY --from=builder /app /app
COPY --from=builder /app/deps /app/deps

# Set Python path to include installed dependencies
ENV PYTHONPATH="/app/deps"

# Expose port
EXPOSE 8080

# Run the application
CMD ["app.py"]