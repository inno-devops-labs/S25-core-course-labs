# Use an explicit Python version and Alpine image for stability
FROM python:3.9-alpine3.15

# Create a non-root user and set up the working directory
RUN adduser -D myuser && mkdir -p /app && chown myuser:myuser /app
USER myuser
WORKDIR /app

# Install dependencies
COPY --chown=myuser:myuser requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Copy application code
COPY --chown=myuser:myuser app.py .

# Set environment variables for production
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PATH="/home/myuser/.local/bin:${PATH}"

# Expose port and run the application
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
