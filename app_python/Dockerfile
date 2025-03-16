FROM python:3.12.7-slim

WORKDIR /usr/src/app

RUN addgroup --system appgroup && useradd --system appuser --groups appgroup

COPY requirements.txt .

COPY app/ ./app
COPY run.sh .

RUN chown -R appuser:appgroup /usr/src/app


ENV PATH="/home/appuser/.local/bin:${PATH}"

RUN pip install --no-cache-dir -r requirements.txt 

USER appuser
RUN chmod +x run.sh

EXPOSE 8080

CMD ["sh", "./run.sh"]