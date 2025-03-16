FROM python:3.12-slim-bookworm AS base

ARG UID=10001
ARG GID=10001

RUN groupadd -g "${GID}" user \
    && useradd -u "${UID}" -g "${GID}" user
WORKDIR /app_python

COPY --chown=user:user requirements.txt ./
COPY --chown=user:user app/ ./app/
COPY --chown=user:user app/templates/ ./app/templates/

RUN pip install -r requirements.txt

RUN mkdir -p ./app/data/
RUN chown -R user:user ./app

USER user
EXPOSE 8081

CMD ["sh", "-c", "python3 -m gunicorn --bind 0.0.0.0:8081 app.app:app"]