FROM python:3-slim-bookworm

ARG USERUID=10001
ARG USERGID=10001

# Create user and group
RUN addgroup -g "${USERGID}" user && \
    adduser -D -u "${USERUID}" -G user user

WORKDIR /service

COPY --chown=user:user service ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /data && chown -R user:user /service && chown -R user:user /data

USER user

EXPOSE 8080

ENV PYTHONPATH=/

CMD [ "python3", "main.py" ]
