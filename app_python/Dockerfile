FROM python:3.12.8-alpine3.21

RUN adduser nonroot --system --shell=/bin/false
USER nonroot

WORKDIR /src

COPY api/main.py requirements.txt ./
COPY api/templates/ ./templates/
COPY api/static/ ./static

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]