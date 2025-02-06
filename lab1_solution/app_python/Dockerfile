FROM python:3.13.1-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \ 
    PYTHONDONTWRITEBYTECODE=1 \
    SERVICE_NAME="flask-app"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY web_app .

EXPOSE 5000

RUN addgroup --system $SERVICE_NAME && \
    adduser --system --ingroup $SERVICE_NAME --shell /bin/false --disabled-password $SERVICE_NAME && \
    chown -R $SERVICE_NAME:$SERVICE_NAME /app

USER $SERVICE_NAME

CMD ["python3", "-u", "web_app"]
