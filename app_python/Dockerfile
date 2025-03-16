FROM python:3.12.7-slim-bookworm

WORKDIR /usr/src/app

RUN addgroup --system appgroup && useradd --system appuser --groups appgroup

COPY requirements.txt .

COPY app/ ./app
COPY run.sh .

RUN chown -R appuser:appgroup /usr/src/app
RUN mkdir -p /usr/src/app/data && touch /usr/src/app/data/visits.txt && chmod 777 /usr/src/app/data/visits.txt


ENV PATH="/home/appuser/.local/bin:${PATH}"

RUN pip install --no-cache-dir -r requirements.txt 

# USER appuser
RUN chmod +x run.sh

EXPOSE 8081

CMD ["sh", "./run.sh"]