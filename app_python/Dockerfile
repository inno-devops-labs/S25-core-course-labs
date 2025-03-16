FROM python:alpine3.21@sha256:f9d772b2b40910ee8de2ac2b15ff740b5f26b37fc811f6ada28fce71a2542b0e

WORKDIR /usr/local/app
COPY templates ./templates
COPY app.py ./
RUN mkdir -p /data

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

RUN addgroup -S myApp && adduser -S myApp -G myApp
USER myApp

CMD ["python", "app.py"]
