FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y dnsutils wget
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN mkdir -p /data
VOLUME /data
CMD ["python", "app.py"] 