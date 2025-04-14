FROM python:3-alpine3.15

RUN addgroup -g 1001 app && adduser -u 1001 -G app -D app

WORKDIR /app_python
RUN chown -R app:app /app_python

USER app

COPY templates templates
COPY app.py .
COPY requirements.txt .

RUN python -m venv venv && \
    source venv/bin/activate && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0


CMD ["/app_python/venv/bin/python", "-m", "flask", "run"]
