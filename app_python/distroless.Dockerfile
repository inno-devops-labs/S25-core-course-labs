FROM python:3.11-slim AS build

WORKDIR /app_python

COPY app.py .

COPY requirements.txt .

COPY templates/ templates/

RUN pip install --no-cache-dir  -r requirements.txt

FROM gcr.io/distroless/python3:nonroot AS final

COPY --from=build /app_python /app_python

COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

WORKDIR /app_python

EXPOSE 5000

ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages

CMD ["app.py"]


