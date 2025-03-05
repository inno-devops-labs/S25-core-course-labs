# Builder stage
FROM python:3.9-slim AS builder

# Create fixed-UID user and structure
RUN groupadd -g 1000 appuser && \
    useradd -u 1000 -g appuser -d /home/appuser appuser && \
    mkdir -p /home/appuser /app && \
    chown -R appuser:appuser /home/appuser /app

USER appuser
WORKDIR /app

# Install dependencies to user space
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Copy application files
COPY --chown=appuser:appuser app.py .

# Final Distroless stage
FROM gcr.io/distroless/python3-debian11:nonroot

# Copy Python dependencies from user directory
COPY --from=builder --chown=1000:1000 /home/appuser/.local /home/appuser/.local

# Copy application code
COPY --from=builder --chown=1000:1000 /app /app

# Configure environment
ENV PATH="/home/appuser/.local/bin:$PATH"
ENV PYTHONPATH="/home/appuser/.local/lib/python3.9/site-packages"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set runtime context
USER 1000:1000
WORKDIR /app

# Run application
CMD ["/home/appuser/.local/bin/uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]