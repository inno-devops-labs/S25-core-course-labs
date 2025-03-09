FROM python:3.11-slim AS build

WORKDIR /app_python

COPY requirements.txt /app_python

RUN pip install --no-cache-dir --upgrade -r /app_python/requirements.txt && cp "$(command -v fastapi)" /app_python

COPY src/ /app_python/src/


FROM gcr.io/distroless/python3:nonroot AS run

WORKDIR /app_python

COPY --from=build /app_python /app_python
COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages

EXPOSE 80/tcp

CMD ["fastapi", "run", "src/main.py", "--port", "80"]