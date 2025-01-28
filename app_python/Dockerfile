FROM python:alpine3.12

RUN useradd -u 1234 nonroot
USER nonroot

WORKDIR app
COPY requirements.txt .
COPY main.py .
COPY templates/ ./templates/
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ["main.py"]