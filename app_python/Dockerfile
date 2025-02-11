# Build Stage
FROM python:3.12-slim as builder
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/app/venv/bin:$PATH"
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/* \
    && python -m venv venv \
    && ./venv/bin/pip install --no-cache-dir --upgrade pip \
    && ./venv/bin/pip install --no-cache-dir -r requirements.txt
# Runtime Stage
FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/app/venv/bin:$PATH"
WORKDIR /app
COPY --from=builder /app/venv /app/venv
COPY src/ src/
RUN useradd -m python_user && chown -R python_user:python_user /app
USER python_user
EXPOSE 8000
CMD ["python", "-m", "src.app"]