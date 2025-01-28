FROM python:alpine3.12

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN adduser --disabled-password docker-user

WORKDIR app
COPY main.py .
COPY templates/ ./templates/
ENTRYPOINT [ "python" ]

USER docker-user
CMD ["main.py"]