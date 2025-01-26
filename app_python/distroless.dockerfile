# Step 1: Build Stage
FROM python:3.12.8-alpine3.21 AS build

WORKDIR /app_python

COPY app.py requirements.txt ./
COPY templates/ ./templates/

RUN pip install --no-cache-dir -r requirements.txt &&\
    cp $(which gunicorn) /app_python

# Step 2: Distroless Runtime Stage
FROM gcr.io/distroless/python3 AS final

COPY --from=build /app_python /app_python
COPY --from=build /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
ENV PYTHONPATH=/usr/local/lib/python3.12/site-packages

WORKDIR /app_python

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:wsgi_app"]
