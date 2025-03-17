FROM python:3.13-alpine AS base_image
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir --no-deps &&\
    adduser -D -h /app appuser
USER appuser

FROM base_image AS dev_image
COPY requirements.dev.txt .
RUN pip install -r requirements.txt --no-cache-dir --no-deps
COPY --chown=appuser . . 
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

FROM base_image AS release_image
COPY --chown=appuser . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]