FROM python:3.11-alpine3.18

ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

COPY requirements.txt ./

RUN python -m venv venv && \
    venv/bin/pip install --no-cache-dir -r requirements.txt

COPY time_app.py ./
COPY templates/ templates/

RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 5000

CMD ["/app/venv/bin/python", "time_app.py"]