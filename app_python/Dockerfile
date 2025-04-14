ARG PYTHON_VERSION=3.11.4
ARG SHA256=c46b0ae5728c2247b99903098ade3176a58e274d9c7d2efeaaab3e0621a53935


FROM python:${PYTHON_VERSION}-slim@sha256:${SHA256} AS build

WORKDIR /app

RUN groupadd -r appuser && useradd -r -g appuser -s /sbin/nologin appuser
RUN chown -R appuser:appuser /app && \
    chown -R appuser:appuser /usr/local/lib/python*/site-packages && \
    chown -R appuser:appuser /usr/local/bin
USER appuser

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY --chown=appuser:appuser requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appuser main.py .
COPY --chown=appuser:appuser ./templates ./templates


EXPOSE 8000

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
