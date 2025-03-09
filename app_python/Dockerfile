FROM python:3.9-slim-bullseye

WORKDIR /app

# Устанавливаем явные UID/GID (совпадают с вашим пользователем на хосте)
ARG USER_ID=1000
ARG GROUP_ID=1000

# Создаем группу и пользователя с фиксированными UID/GID
RUN groupadd --gid $GROUP_ID appgroup && \
    useradd --uid $USER_ID --gid appgroup appuser

# Создаем директорию /data и даем права
RUN mkdir -p /data && \
    chown -R appuser:appgroup /data && \
    chmod 777 /data  # Разрешаем запись всем

# Копируем зависимости и устанавливаем
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Меняем владельца файлов приложения
RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 5000

CMD ["python3", "app.py"]
