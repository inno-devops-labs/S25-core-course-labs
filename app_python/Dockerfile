# Build Stage
FROM python:3.9-alpine as builder
### Set the working directory
WORKDIR /app
### Install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application files
COPY . .

# Preparing and running app
FROM python:3.9-alpine
### Set the working directory
WORKDIR /app
### Copy the installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
### Copy the application code
COPY --from=builder /app /app
### Add a non-root user
RUN adduser -D nonroot
USER nonroot
### Expose the port
EXPOSE 8000
### Command to run the application using uvicorn
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]