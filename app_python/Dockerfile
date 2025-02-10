FROM python:3.9-alpine3.17

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app_python

USER appuser

COPY app_python/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]