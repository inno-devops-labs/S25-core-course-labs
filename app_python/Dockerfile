FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN mkdir -p /app/data && chmod -R 777 /app/data

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
