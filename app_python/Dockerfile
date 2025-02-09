FROM python:3.9-alpine3.15

WORKDIR /app
RUN adduser -D user1 && chown -R user1 /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

USER user1
COPY app.py .

EXPOSE 5000
CMD ["python", "app.py"]