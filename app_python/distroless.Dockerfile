# Stage 1: Build stage
FROM python:3.12-slim AS builder

# Working directory in the container
WORKDIR /app_python

# Copy only the necessary files for installation
COPY requirements.txt .
COPY app.py .

# Install dependencies into a specific target directory
RUN pip install --no-cache-dir -r requirements.txt -t /python_app/lib

# Stage 2: Final stage (Distroless)
FROM gcr.io/distroless/python3:nonroot

# Working directory in the container
WORKDIR /app_python

# Non-root user is already set in the distroless image

# Copy the installed dependencies from the builder stage
COPY --chown=nonroot:nonroot --from=builder /python_app/lib /python_app/lib

# Copy the app code from the builder stage
COPY --chown=nonroot:nonroot --from=builder /app_python/app.py .

# Set the port for the app
EXPOSE 5000

# Define environment variable
ENV PYTHONPATH=/python_app/lib
ENV FLASK_APP=app.py

# Run the application
ENTRYPOINT ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
