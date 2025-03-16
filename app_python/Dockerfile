FROM python:3.12-slim

WORKDIR /app_python

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt update && apt install -y dnsutils

COPY visits/ visits/

COPY app.py .

RUN addgroup --system user && \
    adduser --system --ingroup user user && \
    chown -R user:user /app_python
USER user

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]