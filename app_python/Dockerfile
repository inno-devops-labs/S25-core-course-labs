FROM python:3.13 AS builder

WORKDIR /build

RUN apt-get update && apt-get install -y --no-install-recommends build-essential gcc  # ignore: DL3008

COPY requirements.txt .

RUN python -m venv venv && /build/venv/bin/pip install -r requirements.txt

FROM python:3.13-slim AS RUNTIME

RUN useradd --create-home --shell /bin/bash pydev

WORKDIR /opt/app

COPY --from=builder /build/venv/ /opt/app/venv
COPY *.py /opt/app/

RUN chown -R pydev:pydev /opt/app

USER pydev

ENV APP_HOST="0.0.0.0"

EXPOSE 8000

CMD ["/opt/app/venv/bin/python", "/opt/app/main.py"]
