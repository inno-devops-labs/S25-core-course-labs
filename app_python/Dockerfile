FROM python:3.9-slim

WORKDIR /app

COPY app.py .
COPY requirements.txt .
COPY templates/ templates/

RUN pip install --no-cache-dir -r requirements.txt

RUN addgroup --system appuser && \
  adduser --system --group appuser && \
  chown -R appuser:appuser /app

USER appuser

ENV FLASK_APP="app.py"

EXPOSE 8080

ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8080"]