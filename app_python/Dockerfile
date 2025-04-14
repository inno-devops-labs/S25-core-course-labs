# Python
FROM python:3.10-alpine

# Using non-root user for integrity
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Working directory setting
WORKDIR /app

# Copying only needed files
COPY requirements.txt .

# Install needed dependencies and requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copying out app copy
COPY app.py .

# Opening port 5000
EXPOSE 5000

# Starting the web application
CMD ["python", "app.py"]
