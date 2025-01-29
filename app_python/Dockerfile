FROM python:3-alpine3.15

# Set a working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY main.py .

# Create and switch to a non-root user
RUN adduser -D appuser
USER appuser

# Expose the port the app will run on
EXPOSE 5000

# Command to run the app
CMD ["python", "main.py"]
