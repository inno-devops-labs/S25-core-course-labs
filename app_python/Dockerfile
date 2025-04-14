FROM python:3.9-alpine3.15
WORKDIR /app_python
RUN adduser -D flask_app_user
USER flask_app_user
COPY requirements.txt /app_python/
RUN pip install --no-cache-dir -r requirements.txt
COPY web.py /app_python/
COPY templates/ /app_python/templates/
COPY static/ /app_python/static/
EXPOSE 5000
ENV FLASK_APP=web.py
ENV FLASK_ENV=production
CMD ["python", "web.py"]