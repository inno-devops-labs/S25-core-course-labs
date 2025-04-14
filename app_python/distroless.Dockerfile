# Build Stage
FROM python:3.11-slim-bookworm as builder

WORKDIR /app
COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    pip install --user --no-cache-dir -r requirements.txt

# Runtime Stage
FROM gcr.io/distroless/python3-debian11:nonroot

WORKDIR /app

COPY --from=builder /root/.local /home/nonroot/.local
COPY --chown=nonroot:nonroot app.py .

ENV PYTHONPATH=/home/nonroot/.local/lib/python3.11/site-packages \
    PATH=/home/nonroot/.local/bin:$PATH

EXPOSE 5000
USER nonroot
CMD ["app.py"]