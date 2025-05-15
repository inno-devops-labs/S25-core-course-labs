FROM python:3.9-slim

RUN useradd -ms /bin/bash nonroot
USER nonroot

WORKDIR /src

COPY main.py requirements.txt ./
COPY static/ ./static
COPY templates/ ./templates/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]
