# Используем конкретную версию Python-образа
FROM python:3.12.8-alpine3.21@sha256:ba13ef990f6e5d13014e9e8d04c02a8fdb0fe53d6dccf6e19147f316e6cc3a84

# Информация о мейнтейнере
LABEL maintainer="a.fadeenkov@innopolis.university"

# Отключаем создание .pyc файлов и включаем логирование сразу в stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Создаем пользователя и группу для безопасного запуска
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Устанавливаем рабочую директорию
WORKDIR /app_python

# Копируем файлы с правами для непривилегированного пользователя
COPY --chown=appuser:appgroup . /app_python

# Устанавливаем зависимости с фиксированными версиями
RUN apk add --no-cache --virtual .build-deps \
    gcc=14.2.0-r4 \
    musl-dev=1.2.5-r8 \
    libffi-dev=3.4.6-r0 && \
    pip install --no-cache-dir --upgrade pip==25.0 && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

# Переключаемся на непривилегированного пользователя
USER appuser

# Открываем порт
EXPOSE 5000

# Запускаем приложение
CMD ["python", "app.py"]
