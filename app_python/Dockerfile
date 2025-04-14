FROM python:3.10-alpine3.15

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

COPY requirements.txt .
COPY app.py .
COPY templates/ templates/
COPY start.sh .

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x start.sh
RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 5000
EXPOSE 8000

CMD ["python", "app.py"]