FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN adduser --disabled-password --gecos "" myuser
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

USER myuser

EXPOSE 5000

CMD ["python", "lab1.py"]



