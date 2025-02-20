FROM python:3.11.7-slim AS builder
RUN useradd -m appuser
WORKDIR /app_python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11.7-slim
RUN useradd -m appuser
WORKDIR /app_python
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY . .

RUN mkdir -p /app_python/logs && chown -R appuser:appuser /app_python/logs

USER appuser
EXPOSE 5000
CMD ["python", "app.py"]
