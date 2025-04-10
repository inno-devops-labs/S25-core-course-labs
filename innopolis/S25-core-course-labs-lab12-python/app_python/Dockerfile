FROM python:3.10-alpine
ENV PYTHONUNBUFFERED=1

WORKDIR /app_python

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
