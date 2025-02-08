# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.11.1
FROM python:${PYTHON_VERSION}-slim

# Prevents Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Create a non-privileged user that the app will run under
ARG UID=10001
ARG GID=10001
RUN addgroup --gid "${GID}" appgroup && \
  adduser \
  --disabled-password \
  --gecos "" \
  --home "/nonexistent" \
  --shell "/sbin/nologin" \
  --no-create-home \
  --uid "${UID}" \
  --gid "${GID}" \
  appuser

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Switch to the non-privileged user to run the application
USER appuser

COPY --chown=appuser:appuser app.py .

COPY --chown=appuser:appuser templates/ ./templates/

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]
