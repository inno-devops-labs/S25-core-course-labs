# Builder base image
FROM python:3.11-slim AS builder

# Set working directory
WORKDIR /app

# Copy requirements file and application code
COPY requirements.txt /app/requirements.txt
COPY main.py /app/main.py

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt && cp $(which uvicorn) /app

# Result running base distroless-nonroot image
FROM gcr.io/distroless/python3:nonroot AS result

# Set working directory
WORKDIR /app

# Copy application code from builder stage
COPY --from=builder /app /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run the application using uvicorn directly
CMD ["./uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]