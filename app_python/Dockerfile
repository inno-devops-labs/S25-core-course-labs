# Using a minimal and precise base image
FROM python:3.9-slim

# Variables for non-root execution
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# And adding a non-root user
RUN useradd --create-home appuser

# Set working directory
WORKDIR /app

# Copy only necessary files
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY ./app.py ./app.py

# Change ownership of files to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

EXPOSE 5000
CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0"]
