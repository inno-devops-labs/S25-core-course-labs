FROM python:3-slim-bookworm

ARG UID=10001
ARG GID=10001

RUN groupadd -g -l "${GID}" user \
    && useradd -u -l "${UID}" -g "${GID}" user

WORKDIR /service

COPY --chown=user:user service ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /data && chown -R user:user /service && chown -R user:user /data

USER user

EXPOSE 8080

ENV PYTHONPATH=/

CMD [ "python3", "main.py" ]
