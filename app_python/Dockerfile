FROM python:3.12-alpine3.18

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN addgroup -S webgroup && adduser -S webuser -G webgroup && \
    mkdir /app && \
    mkdir -p /var/log/app_logs && \
    touch /var/log/app_logs/python_app.log && \
    apk add --no-cache curl && \
    chown -R webuser:webgroup /app /var/log /var/log/app_logs && \
    chmod -R 777 /var/log/app_logs/python_app.log

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=webuser:webgroup main.py test_main.py ./

USER webuser

EXPOSE 8000

HEALTHCHECK --interval=60s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8000/ || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
