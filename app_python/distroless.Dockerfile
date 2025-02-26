# First stage: Build environment
FROM python:3.9-slim AS build

# Set the working directory
WORKDIR /app

# Copy only necessary files
COPY requirements.txt .
COPY web_app.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt --target /app

# Second stage: Distroless runtime
FROM gcr.io/distroless/python3-debian11:nonroot

# Set working directory
WORKDIR /app

# Copy the application from the build stage
COPY --from=build /app /app

# Expose the application port
EXPOSE 8000

# Run the application
CMD ["web_app.py"]
