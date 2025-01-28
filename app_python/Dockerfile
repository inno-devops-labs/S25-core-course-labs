FROM python:3.11-alpine3.18

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

WORKDIR /app

COPY requirements.txt /app/
COPY app.py /app/
COPY templates/ /app/templates/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["python", "app.py"]
