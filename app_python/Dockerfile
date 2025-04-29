FROM python:3.9-slim

USER root
RUN apt-get update && apt-get install -y dnsutils iputils-ping

RUN adduser --disabled-password myuser
USER myuser

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /app/
COPY templates /app/templates
COPY static /app/static

EXPOSE 5000

CMD ["python", "app.py"]
