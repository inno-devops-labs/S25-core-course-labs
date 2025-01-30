FROM python:3.10-alpine

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app
COPY requirements.txt ./
COPY app.py ./


RUN pip install --no-cache-dir -r requirements.txt
USER appuser

CMD ["python", "app.py"]
     
