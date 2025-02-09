FROM python:3.10-alpine3.21

WORKDIR /app

# install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY src/ src/

# using nonroot user
RUN addgroup --system user && \
    adduser --system --ingroup user user && \
    chown -R user:user /app
USER user

EXPOSE 8000

# command to run application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
