FROM python:3.11-slim-bookworm AS build

WORKDIR /app

# install requirements
COPY requirements.txt .
RUN pip install --target=/app/lib --no-cache-dir -r requirements.txt

# copy app
COPY src/ src/

FROM gcr.io/distroless/python3-debian12:nonroot

WORKDIR /app

# copy from build
COPY --from=build /app/lib /app/lib
COPY --from=build /app/src /app/src

# use installed libraries
ENV PYTHONPATH=/app/lib

EXPOSE 8000

# command to run application
ENTRYPOINT ["python3", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
