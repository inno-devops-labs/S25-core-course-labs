FROM python:3.11-alpine3.18 AS build

WORKDIR /app_python

COPY requirements.txt .
RUN python3 -m venv venv && \
    ./venv/bin/pip install -r requirements.txt

COPY time_app /app_python/time_app

FROM gcr.io/distroless/python3:nonroot

WORKDIR /app_python

COPY --from=build /app_python/venv /app_python/venv
COPY --from=build /app_python/time_app /app_python/time_app

EXPOSE 8000

CMD ["/app_python/venv/bin/python3", "time_app/manage.py", "runserver", "0.0.0.0:8000"]
