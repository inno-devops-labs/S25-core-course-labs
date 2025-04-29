FROM python:3.9-alpine3.15

LABEL authors="Matthew Rusakov"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create a non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set working directory
WORKDIR /app

COPY requirements.txt /app/

# Install dependencies with no cache to reduce layer size
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Switch to non-root user
USER appuser

EXPOSE 5000

CMD ["python", "run.py"]
