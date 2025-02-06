FROM python:3.12-alpine3.18 AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN addgroup -S buildgroup && adduser -S builder -G buildgroup

WORKDIR /src

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

COPY . .

FROM gcr.io/distroless/python3-debian12:nonroot

USER 65532:65532

WORKDIR /app

COPY --from=builder /src /app

EXPOSE 8000

HEALTHCHECK --interval=60s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8000/ || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]