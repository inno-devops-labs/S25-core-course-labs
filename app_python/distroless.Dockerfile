FROM python:3.11-slim as build

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt 

RUN cp $(which uvicorn) /app/uvicorn

COPY app/ ./app

FROM gcr.io/distroless/python3-debian12:nonroot

COPY --from=build /app /python-app

COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages

WORKDIR /python-app

EXPOSE 8080

CMD ["./uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
