FROM python:alpine3.12
COPY . /app
WORKDIR app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ["main.py"]