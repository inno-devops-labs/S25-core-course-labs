FROM python:3.11-alpine3.20 as builder
WORKDIR /app
ENV PYTHONUSERBASE=/app/packages
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11-alpine3.20
WORKDIR /app
RUN apk add --no-cache tzdata && \
    mkdir -p /data && \
    chmod 777 /data
COPY --from=builder /app/packages/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY app.py .
USER 1000  # Используем явное указание UID вместо имени пользователя
EXPOSE 8080
CMD ["python", "app.py"]