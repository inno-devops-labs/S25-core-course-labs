# Stage 1: Build the application dependencies
FROM python:3.9-alpine3.15 as builder
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt && \
    cp -r /usr/local/lib/python3.9/site-packages /site-packages

# Stage 2: Create a lightweight runtime image using Distroless
FROM gcr.io/distroless/python3:nonroot
WORKDIR /app

# Copy the site-packages from the builder stage
COPY --from=builder /site-packages /usr/bin/python3.11/site-packages

# Copy the main application file
COPY ./main.py /app/

# Set non-root user
USER nonroot

# Expose port 80
EXPOSE 80

# Set environment variable
ENV PYTHONPATH /site-packages

# Command to run the application using uvicorn
CMD ["/app/main.py"]