FROM python:3.11.6-slim

RUN useradd -m appuser

RUN mkdir -p /data && chown appuser:appuser /data
VOLUME /data

USER appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
