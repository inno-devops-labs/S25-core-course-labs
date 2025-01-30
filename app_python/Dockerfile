# Use the official Python image as the base image
FROM python:3.10-slim

# Create necessary directories and set appropriate permissions
RUN mkdir /app && chown -R nobody /app

# Set the working directory inside the container
WORKDIR /app

# Copy application files into the container
COPY entrypoint.sh /entrypoint.sh
COPY . .

# Open port 5000
EXPOSE 5000

# Install dependencies and set execute permissions

RUN pip install --no-cache-dir -r requirements.txt && chmod +x /entrypoint.sh

# Set the default user for the container to 'nobody'
USER nobody

# Specify my-app-entrypoint.sh as the entry point
ENTRYPOINT ["/entrypoint.sh"]
