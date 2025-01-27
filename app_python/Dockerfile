FROM python:3.10-slim

# working directory is app
WORKDIR /app
COPY . /app


RUN pip install --no-cache-dir -r requirements.txt

# creating non-root user
RUN groupadd -g 1000 appgroup && useradd -m -u 1000 -g appgroup appuser
USER appuser

EXPOSE 5000
CMD ["python3", "app.py"]