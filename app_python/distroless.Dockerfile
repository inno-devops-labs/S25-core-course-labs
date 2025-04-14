# Stage 1: Build
FROM python:3.13.1-alpine3.21@sha256:f9d772b2b40910ee8de2ac2b15ff740b5f26b37fc811f6ada28fce71a2542b0e AS builder

# Set working directory
WORKDIR /app_python

# Copy application code and requirements
COPY requirements.txt app.py ./
COPY templates ./templates

# Install dependencies into a dedicated directory
RUN pip3 install --no-cache-dir -r requirements.txt -t /app_python

# Stage 2: Final
FROM gcr.io/distroless/python3:nonroot

# Copy application from the builder stage
COPY --from=builder /app_python /app_python

# Set working directory
WORKDIR /app_python

ENV PATH="/app_python/bin:${PATH}" 
ENV FLASK_APP=app.py

# Expose the application port
EXPOSE 5000 5001

# Set the entry point to run Flask
ENTRYPOINT ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]

