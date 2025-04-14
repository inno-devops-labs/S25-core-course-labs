FROM python:3.11-alpine3.20 AS build

COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

FROM gcr.io/distroless/python3-debian12:nonroot

WORKDIR /app

COPY templates ./templates
COPY app.py ./
EXPOSE 8000

ENV PYTHONPATH=/app/site-packages

COPY --from=build /usr/local/lib/python3.11/site-packages /app/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

CMD ["app.py"]
