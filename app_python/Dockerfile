FROM python:3.10-alpine3.15

# Create non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and entrypoint script
COPY app.py .
COPY entrypoint.sh .

# Make the entrypoint script executable
RUN chmod +x entrypoint.sh

# Expose the port
EXPOSE 5000

# Use the entrypoint script
ENTRYPOINT ["./entrypoint.sh"]

