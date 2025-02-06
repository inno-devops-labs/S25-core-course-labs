# Use a minimal and precise base image
FROM python:3.10-bullseye

# Set a non-root user for security
RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup

# Set the working directory
WORKDIR /app

# Copy only necessary files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY app.py config.py /app/
COPY services /app/services
COPY templates /app/templates

# Set permissions to non-root user
USER appuser

# Expose the required port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]