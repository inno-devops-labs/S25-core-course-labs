FROM python:3.12-slim

# create non-root user
RUN groupadd -r appuser && useradd --no-log-init -r -g appuser appuser

# working directory
WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/src/app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/* \
    && chown -R appuser:appuser /src

# switch to non-root user
USER appuser

# python dependencies installation
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy application code
COPY --chown=appuser:appuser . .

# expose port
EXPOSE 8000

# run fastapi application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]