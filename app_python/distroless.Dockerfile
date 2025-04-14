# Stage 1: Build
FROM python:3.12-alpine AS builder

# Set working directory
WORKDIR /app

# Copy application code and requirements
COPY requirements.txt app.py ./  

# Install dependencies into a dedicated directory
RUN pip3 install --no-cache-dir -r requirements.txt -t /app

# Stage 2: Final - Use Distroless with non-root user
FROM gcr.io/distroless/python3:nonroot

# Copy application from the builder stage
COPY --from=builder /app /app

# Set working directory
WORKDIR /app

# Set environment variables
ENV PATH="/app/bin:${PATH}" 
ENV FLASK_APP=app.py

# Expose the application port
EXPOSE 5000

# Set the entry point to run Flask
ENTRYPOINT ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
