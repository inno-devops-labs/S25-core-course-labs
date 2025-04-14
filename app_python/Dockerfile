FROM python:3.11-slim-bullseye

WORKDIR /app

COPY requirements.txt /app

RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

COPY app.py /app

RUN adduser --system --no-create-home nonroot
USER nonroot

EXPOSE 8000

CMD ["python", "app.py"]
