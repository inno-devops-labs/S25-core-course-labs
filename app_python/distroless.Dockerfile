# Setting base image as Python 3.11 slim
FROM python:3.11-slim AS build-env

# Copying source code & static files
COPY /static /app/static
COPY /templates /app/templates
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt

# Setting working directory
WORKDIR /app

# Installing requirements
RUN pip install --no-cache-dir -r requirements.txt && cp $(which uvicorn) /app

# Setting Distroless image as final
FROM gcr.io/distroless/python3:nonroot as final

# Copyint source code, python packages to final image
COPY --from=build-env /app /app
COPY --from=build-env /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages

# Setting working directory
WORKDIR /app

# Setting start script
CMD ["./uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
