FROM python:3.11-slim-bullseye AS build-env

WORKDIR /app

COPY requirements.txt /app

RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt


FROM gcr.io/distroless/python3-debian12:nonroot

WORKDIR /app
COPY --from=build-env /app /app
COPY --from=build-env /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY app.py /app
ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages

EXPOSE 8000

CMD ["app.py"]