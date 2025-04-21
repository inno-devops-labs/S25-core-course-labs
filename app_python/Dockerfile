FROM python:alpine3.12

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN adduser --disabled-password docker-user

WORKDIR app
COPY main.py .
COPY templates/ ./templates/
RUN touch visits.txt && chmod 777 visits.txt
ENTRYPOINT [ "python" ]

USER docker-user
EXPOSE 5000
CMD ["main.py"]
