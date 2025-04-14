FROM python:3-alpine3.15

RUN adduser --system --shell=/bin/false service

WORKDIR /service

COPY --chown=service:service service ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

USER service

EXPOSE 8080

CMD [ "python3", "main.py" ]
