# Stage 1: Build
FROM python:3.9-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.9-slim

WORKDIR /app

# Copy installed dependencies from the builder stage
COPY --from=builder /root/.local /home/appuser/.local

# Copy application files
COPY app.py .
COPY templates/ ./templates/

# Create non-root user and set permissions
RUN groupadd -r appuser && useradd -r -g appuser appuser \
    && chown -R appuser:appuser /home/appuser
USER appuser

# Add /home/appuser/.local/bin to PATH
ENV PATH=/home/appuser/.local/bin:$PATH
ENV FLASK_APP=app.py

EXPOSE 5001
CMD ["flask", "run", "--host=0.0.0.0","--port=5001"]