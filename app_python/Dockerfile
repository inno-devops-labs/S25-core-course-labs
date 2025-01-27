FROM python:3.12-slim

# working directory
WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# dependencies installation
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всю папку app_python
COPY . .

ENV PYTHONPATH=/src/app

# expose port
EXPOSE 8000

# run time application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]