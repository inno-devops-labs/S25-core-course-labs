# Use a minimal and specific base image for Python
FROM python:3.9-alpine3.15

# Set the working directory inside the container to /app
WORKDIR /app

# Create a non-root user for security purposes
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Copy only the requirements file to the container
COPY requirements.txt requirements.txt

# Install dependencies using pip with no cache to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files (main script and templates) to the container
COPY src/ src/

# Adjust ownership of the /app directory to the non-root user
RUN chown -R appuser:appgroup /app

# Switch to the non-root user after all ownership changes are complete
USER appuser

# Expose port 5000 so the application can be accessed on this port
EXPOSE 5000

# Define the entry point for the container
CMD ["python", "src/main.py"]
