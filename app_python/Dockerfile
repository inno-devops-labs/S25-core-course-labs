# Use a minimal base image with a specific version
FROM python:3.11.5-alpine3.18

# Set a non-root user for security
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Set working directory inside the container
WORKDIR /app

COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code after installing dependencies
COPY app.py .

EXPOSE 8080
# Run the application
CMD ["python", "app.py"]