FROM python:3.12-slim

# Создаем пользователя
RUN groupadd -r appuser && useradd --no-log-init -r -g appuser appuser

WORKDIR /app

# Устанавливаем зависимости сначала
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY ./app ./app

# Меняем владельца
RUN chown -R appuser:appuser /app

# Переключаемся на пользователя
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]