# Base image
FROM python:3.10-alpine

# Working directory
WORKDIR /app

# Copy and run the requirements file into the container
COPY app_python/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app_python/main.py .

# Create user with limited permissions
RUN addgroup -S user && \
    adduser -S -G user user && \
    chown -R user:user /app
USER user
RUN mkdir -p /app/data && chown -R user:user /app/data && chmod -R 777 /app/data

# Expose the port the app runs on
EXPOSE 8000
# Define the command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]