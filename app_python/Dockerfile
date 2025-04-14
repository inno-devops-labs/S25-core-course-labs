FROM python:3.9-slim

RUN useradd -ms /bin/bash nonroot
USER nonroot

WORKDIR /src

COPY api/main.py requirements.txt ./
COPY api/templates/ ./templates/
COPY api/static/ ./static

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]


