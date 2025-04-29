FROM python:3.13.1-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \ 
    PYTHONDONTWRITEBYTECODE=1 \
    SERVICE_NAME="flask-app"

COPY ./app_python/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app_python/web_app.py .

EXPOSE 5000

RUN addgroup --system $SERVICE_NAME && \
    adduser --system --ingroup $SERVICE_NAME --shell /bin/false --disabled-password $SERVICE_NAME && \
    chown -R $SERVICE_NAME:$SERVICE_NAME /app

USER $SERVICE_NAME

CMD ["python3", "-u", "web_app.py"]
