# app_python/distroless.Dockerfile

# Stage 1: Builder
FROM python:3.11-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt --target /app/deps

COPY main.py .

# Stage 2: Distroless Runtime
FROM gcr.io/distroless/python3.10:nonroot

WORKDIR /app
# Copy installed deps
COPY --from=builder /app/deps /app/deps
# Copy main Python file
COPY main.py /app/

# Set Python Path to the deps folder
ENV PYTHONPATH=/app/deps

# Distroless doesn't have root user or shell by default
# automatically runs as nonroot

EXPOSE 5000
CMD ["main.py"]
