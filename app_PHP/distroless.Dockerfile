FROM gcr.io/distroless/python3-debian12:nonroot

WORKDIR /usr/local/app
COPY templates ./templates
COPY app.py ./

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

RUN addgroup -S myApp && adduser -S myApp -G myApp
USER myApp

CMD ["python", "app.py"]
