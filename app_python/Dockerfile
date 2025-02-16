FROM python:3.12.2-alpine3.19
WORKDIR /app
RUN adduser -D webUser && chown -R webUser /app
COPY requirements.txt .
RUN pip3.12 install -r requirements.txt
COPY app/ app/
USER webUser
CMD ["python", "-u", "app/app.py"]
EXPOSE 5000
