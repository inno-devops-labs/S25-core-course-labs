FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt main.py ./

RUN pip install --no-cache-dir -r requirements.txt

RUN useradd nonroot
RUN mkdir -p /app/data && chown -R nonroot:nonroot /app/data && chmod -R 777 /app/data

USER nonroot

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
