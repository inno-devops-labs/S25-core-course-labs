FROM python:3-alpine3.15

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN addgroup -S group && adduser -S user -G group
USER user

EXPOSE 5000

CMD ["python", "app.py"]