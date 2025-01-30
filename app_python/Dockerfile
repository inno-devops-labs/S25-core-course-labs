FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /app/
COPY templates/index.html /app/templates/index.html

EXPOSE 5000

CMD ["python", "app.py"]