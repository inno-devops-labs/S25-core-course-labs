FROM python:3-alpine3.21 AS build

RUN adduser --system --no-create-home fastapi

RUN apk add --no-cache curl=8.12.1-r0

HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost/ || exit 1

WORKDIR /app_python

COPY requirements.txt /app_python

RUN pip install --no-cache-dir --upgrade -r /app_python/requirements.txt

COPY src/ /app_python/src/

USER fastapi

EXPOSE 80/tcp

CMD ["fastapi", "run", "src/main.py", "--port", "80"]