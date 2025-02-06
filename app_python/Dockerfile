# Use a lightweight specific version of Python
FROM python:3.9-slim

# Create a non-root user
RUN useradd --create-home appuser
WORKDIR /home/appuser

# Set the non-root user
USER appuser

# Copy only necessary files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .

# Expose the application port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
