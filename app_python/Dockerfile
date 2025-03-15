# Use the official Python slim image 
FROM python:3.9.7-slim

# Set the working directory
WORKDIR /app

# Create a non-root user and group 
RUN groupadd -r appgroup && \
    useradd -r -g appgroup --no-create-home --shell /bin/false appuser

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies as root
RUN pip install --no-cache-dir -r requirements.txt

# Copy main folder of Django application
#(without this folder it would not run Django web app)
COPY moscow_time/ /app/moscow_time

# Transfer ownership of /app to appuser (recursively)
RUN chown -R appuser:appgroup /app

# Switch to non-privileged user
USER appuser

# Expose the Django development server port
EXPOSE 8000

# Run the Django application
CMD ["python3", "moscow_time/manage.py", "runserver", "0.0.0.0:8000"]