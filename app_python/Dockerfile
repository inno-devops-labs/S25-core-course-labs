# Use a minimal and specific base image
FROM python:3.10-alpine3.15  

# Set a non-root user for security
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Set the working directory inside the container
WORKDIR /app

# Copy only necessary files to keep layers clean
COPY requirements.txt ./

# Install dependencies without keeping cache
RUN pip install --no-cache-dir -r requirements.txt  

# Copy the application code
COPY app.py app.py 

# Set the default command to run the application
CMD ["python", "app.py"]
