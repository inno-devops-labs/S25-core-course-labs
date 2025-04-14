FROM python:3.9-alpine3.15

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a non-root user and set workdir
RUN adduser -D appuser && \
    mkdir /app && \
    chown appuser:appuser /app
USER appuser
WORKDIR /app

# Copy only requirements.txt first (for layer caching)
COPY --chown=appuser:appuser requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy only necessary application files (explicitly listed)
COPY --chown=appuser:appuser app.py .

# Expose port and define runtime command
EXPOSE 5000
CMD ["/home/appuser/.local/bin/uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]