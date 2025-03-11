FROM python:3.11-alpine3.18

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

COPY . /app
RUN chown -R appuser:appgroup /app

RUN mkdir -p /data && chown appuser:appgroup /data

RUN touch /data/visits && chmod 777 /data/visits

USER appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python3", "app.py"]
