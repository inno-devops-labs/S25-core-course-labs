FROM python:3.11.6-slim

RUN useradd -m appuser
USER appuser

WORKDIR /app

COPY app.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
