FROM python:3.11-slim

WORKDIR /app_python

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app_python/ . 

EXPOSE 5000

CMD ["python", "app.py"]