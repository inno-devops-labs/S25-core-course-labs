FROM python:3-alpine

WORKDIR /app_python

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create the /data directory and set permissions
RUN mkdir -p /data && chmod 777 /data


EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:application"]