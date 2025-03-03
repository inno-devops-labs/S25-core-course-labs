# Use a precise and lightweight base image
FROM python:3.11-slim

# Set a non-root user for the container
RUN groupadd -r app && useradd --no-log-init -r -g app app

# Set the working directory for the application
WORKDIR /app

# Copy only the required files to avoid unnecessary layers
COPY app.py requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p data && chown myuser data && chmod -R 0777 data

# Expose only the required port
EXPOSE 8080

# Switch to the non-root user
USER app

# Run the application
CMD ["python", "app.py"]
