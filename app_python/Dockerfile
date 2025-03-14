FROM python:3.10-slim

RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*

RUN useradd user && mkdir /app && chown -R user /app

WORKDIR /app

COPY --chown=user:user requirements.txt app.py /app/

RUN mkdir /app/templates && chown -R user /app/templates
COPY --chown=user:user templates/ /app/templates/

COPY --chown=user:user visits/ /app/visits/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

USER user

CMD ["python", "app.py"]