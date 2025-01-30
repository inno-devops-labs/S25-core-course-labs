# Use Python 3.11 slim as base image for smaller footprint
FROM python:3.11-slim-bullseye as builder

# Set working directory for builder
WORKDIR /app

# Set build-time arguments and labels
ARG BUILD_DATE
ARG VERSION=1.0
LABEL org.opencontainers.image.created="${BUILD_DATE}" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.authors="Sergei Polin" \
      org.opencontainers.image.description="Moscow Time Display Application" \
      org.opencontainers.image.source="https://github.com/SergePolin/S25-core-course-labs"

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies with specific pip configuration for security
RUN pip install --no-cache-dir --no-compile -r requirements.txt

# Final stage
FROM python:3.11-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/home/appuser/.local/bin:$PATH" \
    PIP_NO_CACHE_DIR=1 \
    PYTHONPATH="/app" \
    TZ="Europe/Moscow"

# Create non-root user with specific UID/GID
RUN groupadd -r appuser -g 1001 && \
    useradd -r -g appuser -u 1001 -s /sbin/nologin -c "Docker image user" appuser

# Set working directory and create necessary directories
WORKDIR /app

# Copy only necessary files
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --chown=appuser:appuser main.py config.py ./
COPY --chown=appuser:appuser templates/ ./templates/

# Set ownership and permissions
RUN chown -R appuser:appuser /app && \
    chmod -R 755 /app

# Switch to non-root user
USER 1001

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/ || exit 1

# Run the application with specific security flags
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers", "--forwarded-allow-ips", "*"] 