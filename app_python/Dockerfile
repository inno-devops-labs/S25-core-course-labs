FROM python:3.9-slim

# adding new user
RUN groupadd -r myuser && useradd --no-log-init -r -g myuser myuser

WORKDIR /app

COPY --chown=myuser:myuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=myuser:myuser . .

USER myuser

CMD ["python", "app.py"]