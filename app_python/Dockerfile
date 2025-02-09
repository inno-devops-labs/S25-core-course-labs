FROM python:3.11-slim

RUN groupadd -r appuser && useradd -r -g appuser appuser

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY run.py .
COPY /src ./src

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

CMD ["python", "run.py"]
