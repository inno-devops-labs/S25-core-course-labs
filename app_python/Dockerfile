# Use a precise version of the base image
FROM python:3.9-slim
WORKDIR /app

# Set a non-root user for security
RUN useradd -ms /bin/bash appuser
USER appuser

# Copy only necessary files
COPY requirements.txt ./
COPY web_app.py ./

# Install dependencies and expose the application port
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

# Command to run the application
CMD ["python", "web_app.py"]
