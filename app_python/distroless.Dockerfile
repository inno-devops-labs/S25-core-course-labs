# Stage 1: Build Stage
# Use a minimal Python image to install dependencies and build the app
FROM python:3.10-slim AS build

# Set the working directory for the build stage
WORKDIR /app

# Copy only the necessary files to install dependencies
COPY requirements.txt ./

# Install dependencies (Flask, etc.) without cache and unnecessary files
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the application code (avoid unnecessary files)
COPY main.py ./

# Stage 2: Production Stage with Distroless Image
# Use the Distroless Python image with the nonroot tag (automatically creates a non-root user)
FROM gcr.io/distroless/python3:nonroot

# Set the working directory for the production stage
WORKDIR /app

# Copy the installed dependencies from the build stage
COPY --from=build /usr/local/lib/python3.*/site-packages /usr/local/lib/python3.*/site-packages

# Set the PYTHONPATH environment variable to include the path to installed dependencies
ENV PYTHONPATH=/usr/local/lib/python3.*/site-packages

# Copy the application code from the build stage
COPY --from=build /app /app

# Expose the port the app will run on
EXPOSE 5000

# Command to run the app
CMD ["main.py"]
