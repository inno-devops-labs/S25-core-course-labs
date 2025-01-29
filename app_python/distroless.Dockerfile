FROM debian:12-slim@sha256:f70dc8d6a8b6a06824c92471a1a258030836b26b043881358b967bf73de7c5ab AS build

LABEL description="Distroless python app" maintainer="s.asekrea@innopolis.university"

# prevents Python from writing compiled Python files to the disk --> reduces image size
ENV PYTHONDONTWRITEBYTECODE=1

# logs and output are shown in real-time on terminal --> easier to debug
ENV PYTHONUNBUFFERED=1

# create a virtual environment
# i think it's better than copy all the python-package-site in term of image size...
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv=3.11.2-1+b1 libpython3-dev=3.11.2-1+b1 && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip==24.3.1

# i can add this clean up for the venv to reduce the image size but i think it's not the best practice
# RUN find /venv -name '__pycache__' -type d -exec rm -rf {} + && \
# find /venv -name '*.pyc' -delete && \
# find /venv -name 'tests' -type d -exec rm -rf {} +

COPY requirements.txt /requirements.txt
RUN /venv/bin/pip install --no-cache-dir --disable-pip-version-check -r /requirements.txt

FROM gcr.io/distroless/python3-debian12:nonroot@sha256:66f3e24fd4906156a7360d2861731d31d3457a02f34fd3c4491f0b710a259988

WORKDIR /app

# Copy the virtual environment with the installed dependencies from the previous stage
COPY --from=build /venv /venv

COPY __init__.py app.py time_template.html app_service.py /app/app_python/


EXPOSE 8001

ENTRYPOINT ["/venv/bin/gunicorn", "app_python.app:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8001"]
