FROM python:3.12-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN adduser -D person && chown -R person /app
USER person

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "app.py"]
