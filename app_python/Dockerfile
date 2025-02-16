FROM python:alpine3.21@sha256:f9d772b2b40910ee8de2ac2b15ff740b5f26b37fc811f6ada28fce71a2542b0e

WORKDIR /usr/local/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY resources ./resources
COPY app.py ./
EXPOSE 8000

RUN addgroup -S app && adduser -S app -G app
USER app

CMD ["waitress-serve", "--host", "0.0.0.0", "--port", "8000", "app:app"]
