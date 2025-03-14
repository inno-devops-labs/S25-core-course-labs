FROM python:3-slim-bookworm

ARG USERUID=10001
ARG USERGID=10001

RUN apt-get update && apt-get install --no-install-recommends -y dnsutils && rm -rf /var/lib/apt/lists/*

# Create user and group
RUN addgroup --gid "${USERGID}" user && \
    adduser --disabled-password --uid "${USERUID}" --gid "${USERGID}" --gecos "" user

WORKDIR /service

COPY --chown=user:user service ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /data && chown -R user:user /service && chown -R user:user /data

USER user

EXPOSE 8080

ENV PYTHONPATH=/

CMD [ "python3", "main.py" ]
